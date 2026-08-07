---
title: https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster
url: https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# How R8 made Kotlin Coroutines on Android 2x faster

7 min read ![](https://developer.android.com/static/blog/assets/0707_Faster_Kotlin_coroutines_on_Android_with_R8_Strapi_5b162a2623_ZM78f7.webp) 27 Jul 2026 [![View Jonathan Starup's profile](https://developer.android.com/static/blog/assets/unnamed_10_16ef5ad5c7_Z1s2HD7.webp)](https://developer.android.com/blog/authors/jonathan-starup)[![View Andrei Shikov's profile](https://developer.android.com/static/blog/assets/unnamed_9_1eaaffc6a9_EPI3Y.webp)](https://developer.android.com/blog/authors/andrei-shikov) [Jonathan Starup](https://developer.android.com/blog/authors/jonathan-starup) \& [Andrei Shikov](https://developer.android.com/blog/authors/andrei-shikov) Starting from AGP 9.2.0, R8 optimizes most Atomic\*FieldUpdater calls into Unsafe variants that perform [2x to 4x better on common operations](https://github.com/Kotlin/kotlinx.coroutines/issues/3950). This has a particularly large impact on the kotlinx.atomicfu library that implements atomics for `kotlinx.coroutines`, making launching and cancelling coroutines up to 2x faster. In order to get the benefits, update your AGP to 9.2.0 or above.

With the majority of Android apps adopting Kotlin as their main language of choice, [`kotlinx.coroutines`](https://github.com/Kotlin/kotlinx.coroutines) has become a de-facto standard for asynchronous programming. The library offers a well-designed and structured way of managing concurrent flows that is native to Kotlin. Jetpack Compose was no exception, adopting coroutines for managing pointer events, animations and other interactions. At the time of writing, most concurrent APIs in Compose call `suspend` functions under the hood and are launching and/or cancelling coroutines to handle updates.

As the Compose team started to investigate performance, coroutines were discovered to be a bottleneck for many operations that happen outside of composition. As an example, 80% of the time spent on creating and updating `Modifier.clickable` was consumed by launching and cancelling internal coroutines that handled `InteractionSource` updates. Based on those observations, much of early performance work was focused on removing coroutines from the default path and delaying initialization until necessary.

## **The cost of a coroutine**

The easiest way to analyze a function's internal behavior on Android is to capture an Android Runtime (ART) method trace. An ART method trace is a tool that records the execution flow of an app, showing exactly which methods are called, their order, and how much time is spent in each, allowing developers to identify performance bottlenecks. For an empty `LaunchedEffect { }` call, it would look something like this:
![pic01_enhanced.png](https://developer.android.com/static/blog/assets/pic01_enhanced_d0e96f6d9c_2mRqPo.webp) LaunchedEffect method trace visualized in the Perfetto UI

The method trace above can be separated into three parts:

- Initializing a new coroutine
- Starting coroutine
- Completing coroutine (because it exits immediately)

Cancelling `LaunchedEffect `is similar to normal completion, except it also creates a `CancellationException`.

From the profile above, one thing that is immediately suspicious is frequent calls into `java.util.concurrent.AtomicReferenceFieldUpdater` (purple or green boxes with j... labels). While each call is relatively fast, the frequency is concerning; any non-negligible overhead that is spread out across multiple invocations might add up to a noticeable regression. Zooming in on a call reveals that most of the time is spent on... reflection checks?
![pic02-enhanced.png](https://developer.android.com/static/blog/assets/pic02_enhanced_a3ff3d0f67_2vrnuU.webp) An up-close look at the method trace of AtomicReferenceFieldUpdater.get during LaunchedEffect initialization

Coroutines implement a lock-free tree structure for parent-child relationships that makes structured concurrency possible. Turns out, the `kotlinx.atomicfu` library implements lock-free atomic operations using a well-known JVM primitive, [AtomicReferenceFieldUpdater](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicReferenceFieldUpdater.html). The updater uses a class reference and a field name to perform atomic operations at runtime, and it has to run several reflective safety checks to make sure the field exists and is accessible. Each operation in coroutines (starting, suspending, cancelling, completing) calls at least one atomic operation, so if it is slow, coroutines will not perform well.

## **Investigating AtomicReferenceFieldUpdater**

But let's not get ahead of ourselves. `AtomicReferenceFieldUpdater` is actually well-optimized on JVM [for over 10 years now](https://shipilev.net/blog/2015/faster-atomic-fu/), and method traces might capture overhead that is completely removed by a VM level optimization: just-in-time (JIT) or ahead-of-time (AOT) compilations. To verify performance, let's write a few benchmarks to measure the difference between atomic references from `kotlinx.atomicfu` and `java.util.concurrent.atomic`.

```kotlin
@RunWith(AndroidJUnit4::class)
class AtomicReferenceBenchmark {
    @get:Rule
    val benchmarkRule = BenchmarkRule()
    
    private val atomicReference = java.util.concurrent.atomic.AtomicReference(false)
    private val atomicRef = kotlinx.atomicfu.atomic<Boolean>(false)
    
    @Test
    fun atomicReference_compareAndSet() {
        benchmarkRule.measureRepeated { 
            atomicReference.compareAndSet(true, false)
            atomicReference.compareAndSet(false, true)
        }
    }

     @Test
    fun atomicRef_compareAndSet() {
        benchmarkRule.measureRepeated {
            atomicRef.compareAndSet(true, false)
            atomicRef.compareAndSet(false, true)
        }
    }

    /* measuring other methods from the method traces above */
}
```

Running this benchmark on a Pixel 5 (while ensuring `AtomicReferenceFieldUpdater#compareAndSet` is JIT compiled during warmup), yields the following results on Pixel 5 (API 33):

```
 50.7 ns  atomicReference_compareAndSet
135   ns  atomicRef_compareAndSet
```

The measurements confirm the gap, with `kotlinx.atomicfu` version clearly being approximately 2.7x slower. This confirms that ART does not perform any hidden optimization and reflective access checks add real overhead during runtime.

Looking back at the original method trace, the only meaningful work performed by the `AtomicReferenceFieldUpdater` is the internal call into `Unsafe.getObjectVolatile` that actually executes the underlying atomic operation. In most cases, the updater initializer is static, and can be proved to be always correct based on the structure of the surrounding class. Thus, one could statically analyze most of the `AtomicReferenceFieldUpdater` usages and replace them with an internal `Unsafe` variant during compilation. It also just happens that Android build toolchain has its very own optimizing compiler that can do exactly that.

## **Optimization with R8**

The `Atomic*FieldUpdater `classes support subtle, dynamic and reflection-based use, but are often used in statically obvious patterns. This both explains the slow baseline performance and the want for optimization. R8 is a full-program optimizing compiler and is well-suited to see through the simpler patterns to skim the overhead of the reflective safety checks. R8 receives JVM bytecode after the Java or the Kotlin compiler, but to ease readability these examples are presented in Java syntax. This is why there are no type arguments for `AtomicReferenceFieldUpdater`.

```java
class Example {
    volatile String data = "";
    static final AtomicReferenceFieldUpdater updater =
        AtomicReferenceFieldUpdater.newUpdater(Example.class, String.class, "data");

    void example() {
        // ...
        updater.compareAndSet(this, "", "new");
        // ...
    }
}
```

The base example creates a static final updater which accesses a volatile field with simple constant arguments for the holder, the type, and the name of the field. The reflection used is totally transparent. It is clear to see this updater references a valid field and that the site of the updater creation has valid access to the field.

In its essence, `Atomic*FieldUpdater` is a wrapper around a field offset and calls to `Unsafe`. The best case scenario for the optimization is to replace the updater field with an offset field and replace the updater calls with calls to `Unsafe`.

## Optimizing Atomic\*FieldUpdater

The optimization is implemented in three parts: Instrumentation, Replacement, and Clean-up.

### Instrumentation

The first step is to introduce offset fields alongside the updater field in order to facilitate direct access via the `Unsafe `call.

```java
static final long updater$offset =
    SyntheticUnsafe.UNSAFE.objectFieldOffset(Example.class.getDeclaredField("data"))
```

The field is accessed via reflection, and `Unsafe` is used to extract the field offset on the class. This code represents the internals of `Atomic*FieldUpdater `if you disregard reflection validation. Instead, the holder type of the updater and the field type of the volatile field are tracked statically in the compiler.

Note that the original field and its initialization are left as-is. The optimization process optimistically facilitates and optimizes uses and then later cleans up. This is a simple approach to the implementation but also allows partial optimization of updater fields, where some uses are left as they were while others are optimized.

### Replacement

At this point in the compiler, after a suitable concurrency join point, we have a list of instrumented updater fields. This means that we can optimize each call site individually based on a few conditions. Consider an example call:

```java
updater.compareAndSet(holder, expectedValue, newValue);
```

The conditions that `Atomic*FieldUpdater` requires are these:

- Does `updater` come from an instrumented field? That is, can static analysis track the value of the object back to a field read of an instrumented updater?
- Is `holder` the same class or a subclass of the originally defined holder type?
- Is `newValue` the same class or a subclass of the originally defined field type?

If all conditions are met, then the call is replaced by a call to `Unsafe` without any of the reflection checks.

```java
SyntheticUnsafe.UNSAFE.compareAndSwapObject(holder, Example.updater$offset, expectedValue, newValue)
```

This new call is faster and simpler but it differs from the original call in regards to its handling of null values in `updater` and `holder`. Unless statically ruled out, null-checks are inserted for both.

### Clean-up

At this point, the holding class has the original updater field and the new offset field along with call sites that might use either one of the two. If none of the call sites were optimized, then the offset field should be removed and if all of the call sites were optimized, then the updater field should be removed. In both cases the initializing call should also be deleted. The deletion of unused fields and removal of dead code is already done in the compiler, but removing the initializing code here requires a few more tricks.

Both the call to `newUpdater` and `getDeclaredField` might have side effects as they can throw exceptions (and their implementation is also unknown since it depends on the API version). This means that by generic optimization, they cannot safely be removed. So this clean-up required explicit consideration of the instrumented fields, since those are statically known to be free of exceptions.

In the end, the simple updater example shown above looks like this after optimization:

## **Results**

After these optimizations, `kotlinx.atomicfu` and most explicit uses of `AtomicInt/Long/ReferenceFieldUpdater` now match `AtomicReference` performance with R8 applied. In fact, it is even faster in some benchmarks; `kotlinx.atomicfu` has [a compiler plugin](https://github.com/Kotlin/kotlinx-atomicfu#atomicfu-compiler-plugin) that can inline `atomic` instances into fields, reducing allocations required to create an atomically updated field.

Jetpack Compose was the main beneficiary of this work. Compose runtime has a number of microbenchmarks that track coroutine performance very closely to catch performance regressions early. When the benchmarks were updated to a new version of R8, we noticed a [2x improvement](https://androidx-perf.skia.org/m?begin=1774346923.115&domain=date&end=1774504110.752&shortcut=1c7e462efddcffab76890e38f3888b84) when launching and cancelling coroutines in `LaunchedEffect`!
![pic03_enhanced.png](https://developer.android.com/static/blog/assets/pic03_enhanced_c6780d9684_2wRC36.webp) Benchmark graph illustrating the time taken when starting and cancelling coroutines in LaunchedEffect (lower is better). The change in the graph corresponds to an R8 update, showcasing 2x improvement.

Aside from that, the ART team is implementing these optimizations natively at the VM level. If your app is targeting API 36 and is running on a recent version of Android, it is possible that your device is already optimizing coroutines in a similar way. The coroutine benchmarks above observed \~15% improvement in performance after JIT updates in the recent versions of ART.

Your app will receive this optimization by default when upgrading to AGP 9.2.0 or by using R8 9.2.0 directly. For more information, see [D8 dexer and R8 shrinker](https://r8.googlesource.com/r8/+/refs/heads/main/README.md#replacing-r8-in-agp).
- [#Compose](https://developer.android.com/blog/topics/compose)
- [#R8](https://developer.android.com/blog/topics/r8)
- [#coroutines](https://developer.android.com/blog/topics/coroutines)
Written by:

-

  ## [Jonathan Starup](https://developer.android.com/blog/authors/jonathan-starup)

  ###### Software Engineer

  [read_more View profile](https://developer.android.com/blog/authors/jonathan-starup) ![View Jonathan Starup's profile](https://developer.android.com/static/blog/assets/unnamed_10_16ef5ad5c7_Z1s2HD7.webp) ![View Jonathan Starup's profile](https://developer.android.com/static/blog/assets/unnamed_10_16ef5ad5c7_Z1s2HD7.webp)
-

  ## [Andrei Shikov](https://developer.android.com/blog/authors/andrei-shikov)

  ###### Senior Software Engineer

  [read_more View profile](https://developer.android.com/blog/authors/andrei-shikov) ![View Andrei Shikov's profile](https://developer.android.com/static/blog/assets/unnamed_9_1eaaffc6a9_EPI3Y.webp) ![View Andrei Shikov's profile](https://developer.android.com/static/blog/assets/unnamed_9_1eaaffc6a9_EPI3Y.webp)
Continue reading
- 3 Authors 08 Jun 2026 08 Jun 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_TITLE_Strapi_b83ae0beee_i9nEs.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Datadog delivers millions of in-depth performance insights with ProfilingManager](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager)

  [arrow_forward](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager) Performance regressions are notoriously hard to reproduce, making regressions a massive bottleneck for mobile developers.
  [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan), [Arti Arutiunov](https://developer.android.com/blog/authors/arti-arutiunov), [Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov) • 4 min read
  - [#Profiling Manager](https://developer.android.com/blog/topics/profiling-manager)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +1 ↩
- [![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) 15 May 2026 15 May 2026 ![](https://developer.android.com/static/blog/assets/cross_device_discovery_to_score_record_Wear_OS_adoption_Strapi_2f9244f1db_Z23QTbE.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How FotMob leveraged cross-device discovery to score record Wear OS adoption](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption)

  [arrow_forward](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption) FotMob recently experienced its largest single-day increase on Wear OS among its installed audience in 5 years, at 2-3x the daily average. The secret? A simple cross-device installation flow that helps users discover their Wear OS app directly from their phone.
  [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
- [![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp)](https://developer.android.com/blog/authors/ash-nohe) 08 May 2026 08 May 2026 ![](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_2000x1000_7d5a00e6c2_Z2vwfIA.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Gratitude saw 25% higher retention for widget users](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users)

  [arrow_forward](https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users) The mindfulness app Gratitude encourages consistency through micro daily journaling, affirmations, and vision boards. The app has over 6 million downloads, 150 thousand 5 star ratings, and 100 million journal entries logged.
  [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev), [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe) • 3 min read
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)