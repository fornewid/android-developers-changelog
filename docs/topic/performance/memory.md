---
title: https://developer.android.com/topic/performance/memory
url: https://developer.android.com/topic/performance/memory
source: md.txt
---

This page explains how to proactively reduce memory usage within your app. For
information about how the Android operating system manages memory, see [Overview
of memory management](https://developer.android.com/topic/performance/memory-overview).

Random-access memory (RAM) is a valuable resource for any software development
environment, and it's even more valuable for a mobile operating system where
physical memory is often constrained. Although both the Android Runtime (ART)
and Dalvik virtual machine perform routine garbage collection, this doesn't mean
you can ignore when and where your app allocates and releases memory. You still
need to avoid introducing [memory leaks](https://developer.android.com/topic/performance/memory-leaks)---usually caused by holding onto
object references in static member variables---and release any [`Reference`](https://developer.android.com/reference/java/lang/ref/Reference)
objects at the appropriate time as defined by lifecycle callbacks.

## Reduce your app's code and resource footprint

Some resources and libraries within your code can consume memory without you
realizing. The overall size of your app, including third-party libraries or
embedded resources, can affect how much memory your app consumes. You can
improve your app's memory consumption by removing redundant, unnecessary, or
bloated components, resources, and libraries from your code.

### Reduce overall app size by enabling R8

Your compiled application code is an active part of your runtime memory
footprint. Every class, method, library dependency, and string constant must be
loaded into RAM when run. The larger your compiled codebase, the more physical
RAM your app requires to exist.

You can [use R8 to reduce your app's memory footprint](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization). While R8 is
traditionally known for [shrinking APK size](https://developer.android.com/topic/performance/reduce-apk-size), it has a direct, positive
impact on runtime memory (RAM). R8 analyzes your app's bytecode to strip away
dead code, merge redundant classes, inline methods, and minify identifiers. By
loading less compiled bytecode from the APK into RAM, it decreases the app's
overall baseline memory footprint. Additionally, minifying class, method, and
field names into shorter identifiers directly reduces RAM overhead.
Optimizations like class merging and extensive method inlining also replace
costly runtime lookups and allocation patterns, resulting in optimized heap and
stack memory.

#### Understand keep rules

Keep rules are configuration instructions that tell R8 which parts of your code
to preserve during optimization, preventing it from removing or minifying code
that your app relies on. For more information, see the [Keep rules overview](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview).

Poorly written keep rules prevent R8 from optimizing large portions of your
codebase. Avoid over-broad keep rules and follow these best practices:

- **Global rules to avoid:**
  - `-dontoptimize`: Completely disables optimization for the entire app, resulting in larger, slower executables.
  - `-dontshrink`: Prevents the removal of unused code and resources.
  - `-dontobfuscate`: Prevents name minification, missing out on valuable memory savings (especially in large apps).
- **Avoid package-wide wildcards:** Broad rules like `-keep class
  com.example.package.** { *; }` force R8 to preserve every class, field, and
  method in that package. This completely halts R8's ability to remove,
  optimize, or minify code in that package.

- **Use the default R8 configuration file:** Always use
  `proguard-android-optimize.txt`.

For more information about writing keep rules, see the [Keep rules overview](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview).
For specific patterns to use and avoid, see [Keep rules best practices](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices).

The R8 Configuration Analyzer provides insights into your R8 configuration and
how each keep rule impacts your app. For more information about how to identify
rules that block optimization, see [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer).

### Be careful about using external libraries

External library code often isn't written for mobile environments and can be
inefficient for working on a mobile client. When you use an external library,
you might need to optimize that library for mobile devices. Plan for this work
ahead of time and analyze the library in terms of code size and RAM footprint
before using it.

Even some mobile-optimized libraries can cause problems due to differing
implementations. For example, one library might use lite protobufs while another
uses micro protobufs, resulting in two different protobuf implementations in
your app. This can happen with different implementations of logging, analytics,
image-loading frameworks, caching, and many other things you don't expect.

While [optimizing your app using R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) can remove unused code from
dependencies, its effectiveness is often limited by the library's internal
configuration. For example, broad keep rules or the use of reflection within a
library can prevent R8 from shrinking its code, leading to a larger memory
footprint. For strategies on selecting efficient libraries, see [Choose
libraries wisely](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely).

Avoid using a shared library for just one or two features out of dozens. Don't
pull in a large amount of code and overhead that you don't use. When you
consider whether to use a library, look for an implementation that strongly
matches what you need. Otherwise, you might decide to create your own
implementation.

### Use Hilt or Dagger 2 for dependency injection

Dependency injection frameworks can simplify the code you write and provide an
adaptive environment that's useful for testing and other configuration changes.

If you intend to use a dependency injection framework in your app, consider
using [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) or [Dagger](http://dagger.dev/). Hilt is a dependency injection library for
Android that runs on top of Dagger. Dagger doesn't use reflection to scan your
app's code. You can use Dagger's static compile-time implementation in Android
apps without needless runtime cost or memory usage.

Other dependency injection frameworks that use reflection initialize processes
by scanning your code for annotations. This process can require significantly
more CPU cycles and RAM, and can cause a noticeable lag when the app launches.

When using dependency injection, be careful to avoid memory leaks by ensuring
that objects are scoped appropriately. Retaining objects longer than necessary
by binding them to the wrong lifecycle can lead to memory leaks. For more
information, see the guidance on [avoiding memory leaks with scoped
objects](https://developer.android.com/topic/performance/memory-leaks#singleton-ui-scoped).

### Be intentional with image loading

Graphic bitmaps are usually the largest common objects residing in your app's
memory. Even if you're working with compressed files like JPEGs, the file has to
be inflated into an uncompressed bitmap to be displayed on screen. A small
compressed image file can expand into a very large bitmap.

For example, most bitmaps use the `ARGB_8888` configuration, which means each
pixel requires 4 bytes of memory--one byte each for red, green, blue, and alpha
(transparency). If you have a 100KB JPEG and you display it in a 1000×1000 pixel
view, the bitmap will require 4 bytes for each of those 1,000,000 pixels, adding
up to 4MB of memory.

There are several things you can do to optimize your use of images. For example,
using image loading libraries can help you release memory when it isn't needed.
For information on how to handle images efficiently, see [Optimizing bitmap
images](https://developer.android.com/develop/ui/compose/graphics/images/optimization).

## Monitor available memory and memory usage

You must find your app's memory usage problems before you can fix them. The
Android Studio [memory profiler](https://developer.android.com/studio/profile/memory-profiler) helps you find and diagnose memory issues
in the following ways:

- [See how your app allocates memory over time.](https://developer.android.com/studio/profile/inspect-app-live) The memory profiler shows a realtime graph of how much memory your app is using, the number of allocated Java objects, and when garbage collection occurs.
- Initiate garbage collection events and [take a snapshot of the Java heap](https://developer.android.com/studio/profile/capture-heap-dump) while your app runs.
- [Record your app's memory allocations](https://developer.android.com/studio/profile/record-java-kotlin-allocations), inspect all allocated objects, view the stack trace for each allocation, and jump to the corresponding code in the Android Studio editor.

The memory profiler also integrates with the [LeakCanary](https://square.github.io/leakcanary/) leak detection
library. By using LeakCanary, you can move memory leak analysis from the test
device to your development machine, which can significantly speed up your
workflow. For more information, see the [Android Studio release notes](https://developer.android.com/studio/preview/features#leakcanary).

There are other tools you can use to diagnose memory issues based on data from
users running your production app:

- [Use Android Vitals to track low memory kill (LMK) events.](https://developer.android.com/topic/performance/memory#lmk)
- [Use the Profiling Manager](https://developer.android.com/topic/performance/memory#profiling-triggers) to track out of memory errors, as well as anomalous app behavior that might be caused by memory leaks.

### Release memory in response to events

Android can reclaim memory from your app or stop your app entirely if necessary
to free up memory for critical tasks, as explained in [Overview of memory
management](https://developer.android.com/topic/performance/memory-overview). To further help balance the system memory and avoid the system's
need to stop your app process, you can implement the [`ComponentCallbacks2`](https://developer.android.com/reference/android/content/ComponentCallbacks2)
interface in your [`Activity`](https://developer.android.com/reference/android/app/Activity) classes. The provided [`onTrimMemory()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))
callback method notifies your app of lifecycle or memory-related events that
present a good opportunity for your app to voluntarily reduce its memory usage.
Freeing memory may reduce the frequency of your app being killed by the
[low-memory killer](https://developer.android.com/topic/performance/memory-management#low-memory_killer).

Your implementation of `onTrimMemory()` should focus exclusively on the
`TRIM_MEMORY_UI_HIDDEN` and `TRIM_MEMORY_BACKGROUND` events. (Beginning with
Android 14, the system no longer delivers notifications for the other, legacy
constants. Those constants were formally deprecated in Android 15.)

- `TRIM_MEMORY_UI_HIDDEN`: This signal indicates that your app's UI has
  transitioned out of the user's view. This transition provides an opportunity
  to release substantial memory allocations tied strictly to the UI, such as
  bitmaps, video playback buffers, or complex animation resources.

- `TRIM_MEMORY_BACKGROUND`: This signal indicates that your process is
  residing in the background and is now a candidate for termination to satisfy
  the system's global memory needs. To extend the duration your process
  remains in the cached state, and reduce the number of app cold starts, you
  should aggressively release any resources that can be easily reconstructed
  once the user resumes their session.

This code sample shows how to implement the `onTrimMemory()` callback to respond
to different memory-related events:

### Kotlin

    import android.content.ComponentCallbacks2
    // Other import statements.

    class MainActivity : AppCompatActivity(), ComponentCallbacks2 {

        // Other activity code.

        /**
         * Release memory when the UI becomes hidden or when system resources become low.
         * @param level the memory-related event that is raised.
         */
        override fun onTrimMemory(level: Int) {

            if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
                // Release memory related to UI elements, such as bitmap caches.
            }

            if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
                // Release memory related to background processing, such as by
                // closing a database connection.
            }
        }
    }

### Java

    import android.content.ComponentCallbacks2;
    // Other import statements.

    public class MainActivity extends AppCompatActivity
        implements ComponentCallbacks2 {

        // Other activity code.

        /**
         * Release memory when the UI becomes hidden or when system resources become low.
         * @param level the memory-related event that is raised.
         */
        public void onTrimMemory(int level) {

            if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
                // Release memory related to UI elements, such as bitmap caches.
            }

            if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
                // Release memory related to background processing, such as by
                // closing a database connection.
            }
        }
    }

### Check how much memory you need

To allow multiple running processes, Android sets a hard limit on the heap size
allotted for each app. The exact heap size limit varies between devices based on
how much RAM the device has available overall. If your app reaches the heap
capacity and tries to allocate more memory, the system throws an
[`OutOfMemoryError`](https://developer.android.com/reference/java/lang/OutOfMemoryError).

To avoid running out of memory, you can query the system to determine how much
heap space is available on the current device. You can query the system for this
figure by calling [`getMemoryInfo()`](https://developer.android.com/reference/android/app/ActivityManager#getMemoryInfo(android.app.ActivityManager.MemoryInfo)). This returns an
[`ActivityManager.MemoryInfo`](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo) object that provides information about the
device's current memory status, including available memory, total memory, and
the memory threshold---the memory level at which the system begins to stop
processes. The `ActivityManager.MemoryInfo` object also exposes
[`lowMemory`](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo#lowMemory), which is a simple boolean that tells you whether the device
is running low on memory.

The following example code snippet shows how to use the `getMemoryInfo()` method
in your app.

### Kotlin

    fun doSomethingMemoryIntensive() {

        // Before doing something that requires a lot of memory,
        // check whether the device is in a low memory state.
        if (!getAvailableMemory().lowMemory) {
            // Do memory intensive work.
        }
    }

    // Get a MemoryInfo object for the device's current memory status.
    private fun getAvailableMemory(): ActivityManager.MemoryInfo {
        val activityManager = getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
        return ActivityManager.MemoryInfo().also { memoryInfo ->
            activityManager.getMemoryInfo(memoryInfo)
        }
    }

### Java

    public void doSomethingMemoryIntensive() {

        // Before doing something that requires a lot of memory,
        // check whether the device is in a low memory state.
        ActivityManager.MemoryInfo memoryInfo = getAvailableMemory();

        if (!memoryInfo.lowMemory) {
            // Do memory intensive work.
        }
    }

    // Get a MemoryInfo object for the device's current memory status.
    private ActivityManager.MemoryInfo getAvailableMemory() {
        ActivityManager activityManager = (ActivityManager) this.getSystemService(ACTIVITY_SERVICE);
        ActivityManager.MemoryInfo memoryInfo = new ActivityManager.MemoryInfo();
        activityManager.getMemoryInfo(memoryInfo);
        return memoryInfo;
    }

### Monitor low memory kills

User-visible low memory kills (LMKs) occur when system memory gets critically
low. When memory is low, the
[`lmkd`](https://source.android.com/docs/core/perf/lmkd) (low memory killer
daemon) terminates processes based on their `oom_adj_score`. Apps that are
cached, or are running a service with no associated UI (such as a job), have the
highest scores and are terminated first. If memory remains critically low, the
daemon is forced to reclaim memory from processes with an `oom_adj_score` of 0.
Because that score is reserved for visible apps, their termination results in an
immediate, non-graceful process exit. To the end user, it looks like the app
crashed, often bypassing standard lifecycle state-saving mechanisms and
resulting in lost user progress.

Kills of foreground processes are a primary focus in Android Vitals because they
serve as a high-fidelity proxy for memory mismanagement. While any LMK rate
higher than 1% indicates a critical need for immediate action, a low rate is not
necessarily an indicator of health. A low user-perceived LMK rate might mean
that the LMK daemon is frequently killing processes while they are in the
background, which degrades "warm start" performance and multitasking fluidity.
Therefore, we recommend adhering to memory best practices regardless of your
current LMK score, to ensure long-term stability and device health.

### Use `ProfilingManager` to track memory issues

[The Android platform provides
`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/overview), an
advanced observability API that lets you capture user data in production based
on triggers you set. Doing this can help you identify hard-to-reproduce memory
issues.

Two new triggers [introduced with Android
17](https://developer.android.com/about/versions/17/features#profilingmanager-new-triggers) are especially
useful for spotting memory problems:

- [`TRIGGER_TYPE_OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM) indicates that the app has thrown an `OutOfMemoryError`. It triggers the next time the app starts *after* the crash, when the app registers for profiling triggers.
- [`TRIGGER_TYPE_ANOMALY`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANOMALY) triggers when when the system detects anomalous behavior from the app. Among other things, this can be triggered by excessive memory usage. It triggers after the app has exhibited excessive memory usage, and *before* the system takes any action to stop the offending process. For example, if the app exceeds the [memory limits introduced in Android
  17](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits), `TRIGGER_TYPE_ANOMALY` triggers before the system kills the app.

For more information on using `ProfilingManager` to programmatically register
and retrieve triggers, see the [trigger-based
profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture)
documentation.

You can also [use app-driven
profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) to
manually define start and end trace points. We recommend doing this to manually
capture heap dumps or heap profiles in areas you suspect might have memory leaks
or excessive memory usage.

## Use more memory-efficient code constructs

Some Android features, Java classes, and code constructs use more memory than
others. You can minimize how much memory your app uses by choosing more
efficient alternatives in your code.

### Use services sparingly

We strongly recommend you don't leave services running when it's unnecessary.
Leaving unnecessary services running is one of the worst memory-management
mistakes an Android app can make. If your app needs a
[service](https://developer.android.com/guide/components/services) to work in the background, don't
leave it running unless it needs to run a job. Stop your service when it
completes its task. Otherwise, you might cause a memory leak.

When you start a service, the system prefers to keep the process for that
service running. This behavior makes service processes very expensive because
the RAM used by a service remains unavailable for other processes. This reduces
the number of cached processes that the system can keep in the LRU cache, making
app switching less efficient. It can even lead to thrashing in the system when
memory is tight and the system can't maintain enough processes to host all the
services currently running.

Generally, avoid using persistent services because of the ongoing demands they
place on available memory. Instead, we recommend you use an alternative
implementation, such as [`WorkManager`](https://developer.android.com/reference/androidx/work/WorkManager).
For more information about how to use `WorkManager` to schedule background
processes, see [Persistent work](https://developer.android.com/guide/background/persistent).

### Use optimized data containers

Some of the classes provided by the programming language aren't optimized for
use on mobile devices. For example, the generic
[`HashMap`](https://developer.android.com/reference/java/util/HashMap) implementation can be memory
inefficient because it needs a separate entry object for every mapping.

The Android framework includes several optimized data containers, including
[`SparseArray`](https://developer.android.com/reference/android/util/SparseArray),
[`SparseBooleanArray`](https://developer.android.com/reference/android/util/SparseBooleanArray), and
[`LongSparseArray`](https://developer.android.com/reference/androidx/collection/LongSparseArray). For
example, the `SparseArray` classes are more efficient because they avoid the
system's need to autobox the key and sometimes the value, which creates yet
another object or two per entry.

If necessary, you can always switch to raw arrays for a lean data structure.

### Be careful with code abstractions

Developers often use abstractions as a good programming practice because they
can improve code flexibility and maintenance. However, abstractions generally
require more code to be executed. As detailed in [Reduce your app's code and
resource footprint](https://developer.android.com/topic/performance/memory#reduce-footprint), a larger compiled codebase directly
increases the physical RAM your app requires. If your abstractions aren't
significantly beneficial, avoid them.

### Use lite protobufs for serialized data

[Protocol buffers
(protobufs)](https://developers.google.com/protocol-buffers/docs/overview) are a
language-neutral, platform-neutral, extensible mechanism designed by Google for
serializing structured data---similar to XML, but smaller, faster, and simpler. If
you use protobufs for your data, always use lite protobufs in your client-side
code. Regular protobufs generate extremely verbose code, which increases your
app's code footprint in RAM (see [Manage and optimize your app's code
footprint](https://developer.android.com/topic/performance/memory#reduce-footprint)) and contributes to APK size increase.

For more information, see the [protobuf
readme](https://android.googlesource.com/platform/external/protobuf/+/master/java/README.md#installation-lite-version-with-maven).

### Be cautious about memory leaks

Improper reference management can lead to memory leaks where objects outlive
their useful lifespans, preventing the garbage collector from reclaiming the
leaked object's memory. To avoid memory leaks, implement lifecycle-aware design.

For more information, see [Memory leaks](https://developer.android.com/topic/performance/memory-leaks).

### Avoid memory churn

Garbage collection events don't affect your app's performance. However, many
garbage collection events that occur over a short period of time can quickly
drain the battery as well as marginally increase the time to set up frames due
to necessary interactions between the garbage collector and app threads. The
more time the system spends on garbage collection, the faster the battery
drains.

Often, *memory churn* can cause a large number of garbage collection events to
occur. In practice, memory churn describes the number of allocated temporary
objects that occur in a given amount of time.

For example, you might allocate multiple temporary objects within a `for` loop.
Or, you might create new [`Paint`](https://developer.android.com/reference/android/graphics/Paint) or
[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap) objects inside the
[`onDraw()`](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas))
function of a view. In both cases, the app creates a lot of objects quickly at
high volume. These can quickly consume all the available memory in the young
generation, forcing a garbage collection event to occur.

Use the [Memory Profiler](https://developer.android.com/studio/profile/memory-profiler) to find the
places in your code where the memory churn is high before you can fix them.

After you identify the problem areas in your code, try to reduce the number of
allocations within performance-critical areas. Consider moving things out of
inner loops or perhaps moving them into a
[factory-based](https://en.wikipedia.org/wiki/Factory_method_pattern) allocation
structure.

You can also evaluate whether object pools benefit the use case. With an object
pool, instead of dropping an object instance on the floor, you release it into a
pool after it's no longer needed. The next time an object instance of that type
is needed, you can acquire it from the pool rather than allocating it.

Thoroughly evaluate performance to determine if an object pool is suitable in a
given situation. There are cases in which object pools might make performance
worse. Even though pools avoid allocations, they introduce other overheads. For
example, maintaining the pool usually involves synchronization, which has
non-negligible overhead. Also, clearing the pooled object instance to avoid
memory leaks during release and then its initialization during acquisition can
have non-zero overhead.

Holding back more object instances in the pool than needed also puts a burden on
the garbage collection. While object pools reduce the number of garbage
collection invocations, they end up increasing the amount of work needed for
every invocation, as it is proportional to the number of live (reachable) bytes.