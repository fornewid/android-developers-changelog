---
title: https://developer.android.com/topic/performance/memory/guide/app-code
url: https://developer.android.com/topic/performance/memory/guide/app-code
source: md.txt
---

The code you write is itself a form of memory use. Every class, method, and
string constant in your application must be loaded into RAM when it is executed.
The larger your application's code base, the more memory it will consume just to
exist.

## File-backed memory and demand paging

Android loads executable code from your `.apk` (like `.oat` or `.so` files)
using `mmap`. This means the code is **file-backed**.

Crucially, Android uses **demand paging**. When your app starts, the kernel does
not load the entire APK into RAM immediately. Instead, it only maps the file
into the process's virtual address space. As your app executes, and the CPU
jumps to a new function, it triggers a "page fault." The kernel pauses the
thread, reads that specific 4KB page of code from the storage into physical RAM,
and resumes execution.

![A diagram illustrating demand paging, showing virtual pages being mapped to
physical RAM pages only when accessed](https://developer.android.com/static/topic/performance/memory/guide/images/app-code/demand_paging.png)

This means that code you *package* but never *execute* does not use physical
memory for the code pages themselves. However, unused libraries still increase
the overall APK size and can significantly increase the memory used by the
system's internal metadata (like DEX indices and class descriptors), which must
be read to even *know* that the code exists. Furthermore, many libraries contain
static initializers or are touched by dependency injection frameworks during app
startup, causing them to be paged into RAM anyway.

### Page eviction and slowdowns

Because file-backed memory can always be re-read from storage, the kernel
considers these pages "clean". When the system experiences memory pressure, the
kernel will **evict** (drop) these clean code pages from RAM to make room for
other things.

If your app later needs to execute that code again, the CPU will fault, and the
kernel must re-read the page from storage. **The more code your app has, the
more vulnerable it is to having its code evicted.** When a user returns to your
bloated app after using other apps, they will experience random jank and
slowdowns as the CPU constantly stalls waiting for code to be paged back in from
storage.

**The Cost of a Page Fault:** While it varies heavily based on the device's
storage speed (UFS vs. eMMC) and kernel state, a major page fault (reading 4KB
from storage) can cost anywhere from **0.5ms to 5ms**. If your startup path
touches 500 different pages of unoptimized code, you could easily introduce
several hundred milliseconds of pure I/O latency to your app startup time.

## Exploring code size with Compiler Explorer

To build an intuition for how your Java or Kotlin code translates into native
machine code (and thus memory bytes), you can use
[Compiler Explorer](https://godbolt.org/).

Android support is built directly into Godbolt. It allows you to see how
different parts of the Android toolchain (D8, R8, and dex2oat) transform your
source code.

### How to use Compiler Explorer with Android

1. Navigate to [godbolt.org](https://godbolt.org/).
2. Select **Android Java** or **Android Kotlin** from the language dropdown (top left).
3. In the compiler dropdown (top right of the code pane), you can choose between different tools:
   - **`d8`** : Shows the **Dalvik bytecode** (`.dex`). This is the closest representation to your original code and is easier to read.
   - **`r8`** : Shows how the **R8 optimizer** shrinks and optimizes your bytecode.
   - **`dex2oat`** : Shows the final **ARM64 machine code** that actually executes on the device. This is where you can see the real memory impact (4 bytes per instruction). `dex2oat` can target different ISAs, but ARM64 is the most common for mobile phones.
4. **Source\<\>Output Highlighting**: Hovering over a line of code will highlight the corresponding bytecode or machine code instructions, making it easy to trace the impact of specific statements.
5. **Optimization Pipeline** : In the disassembly view, you can click **Add
   new...** -\> **Opt Pipeline** . This allows you to see the internal steps the compiler takes. You can inspect how the **Internal Representation (IR)** is transformed at each stage (e.g., between the "Inliner (before)" and "Inliner (after)" steps) before it is lowered into the final ARM64 machine code.

![A screenshot of the Compiler Explorer UI showing a sample program and its
dex2oat output disassembly and optimization pipeline with the inlining step
shown](https://developer.android.com/static/topic/performance/memory/guide/images/app-code/compiler-explorer.png)

### Why this matters for memory

Every instruction you see in the `dex2oat` output targeting the ARM64 ISA takes
up **4 bytes** in your app's executable (`.odex` or `.oat`) file.

Try entering code that utilizes different language features and study the
compiler's output:

- **Array access vs. List Iterators** :
  - A simple **array loop** over `int[]` might compile to \~10 instructions (\~40 bytes).
  - A **foreach loop over a `List`** implicitly uses an **`Iterator`** . This can result in 30-40 instructions (\~160 bytes) because of the extra method calls (`hasNext()`, `next()`) and the allocation of the iterator object itself.
  - **R8 Optimization** : Under the right conditions (e.g., when the `List` is proven to be an `ArrayList`), the **R8 optimizer** can transform a foreach loop back into a simple indexed loop, eliminating the iterator overhead and reducing both code size and runtime memory churn.
- **Virtual Method Calls** : Involve loading the object's class, finding the method in the `vtable`, and then branching. This usually takes 4-5 instructions (\~20 bytes).
- **Direct/Static Calls** : Often translate to a single `bl` (Branch with Link) instruction (4 bytes).
- **Kotlin Lambdas**: Can generate entire anonymous classes and additional bridge methods, adding hundreds of bytes of code and metadata overhead for a simple functional block.

By using Compiler Explorer, you can see how sophisticated language features
(like Kotlin lambdas, stream APIs, or heavy use of generics) impact the final
compiled size of your application, and how optimizers such as R8 can counteract
the cost of language abstractions in some cases. This tool can help you make
informed tradeoffs in designing and implementing an app.

Broadly speaking, more complexity in your app's code leads to higher memory use.
Conversely, simpler code - or code that is simplified by R8 - results in a
smaller representation as CPU instructions and bytes in storage and RAM.

## Measuring code impact with `meminfo` and `showmap`

You can use the standard Android memory tools to see how much memory your app's
code is consuming.

### `dumpsys meminfo`

When you run `adb shell dumpsys meminfo <package>`, the **Code** category in the
**App Summary** section provides a high-level view of code-related memory:

     App Summary
                           Pss(KB)
                            ---
               Java Heap:     3244
             Native Heap:     5412
                    Code:    24512  # <--- Sum of .so, .dex, .oat, .art, etc.

### `showmap`

For a more granular view, use `showmap`. It reveals regions out of specific
files being mapped to memory.

> [!NOTE]
> **Note:** To run this `showmap`, you must build your app with `<profileable android:shell="true"/>` or `<debuggable>`.

    adb shell showmap $(pidof <package>) | grep -E "\.oat|\.odex|\.dex|\.apk"

You will see entries for your application's compiled code:

       size      RSS      PSS    clean    dirty    clean    dirty     swap  swapPSS object
    --- --- --- --- --- --- --- --- --- ---
      12288     8192     8192     8192        0        0        0        0        0 /data/app/.../base.odex

## Dead code and R8

Because every executed method takes up memory, having a "bloated" app with
unnecessary initializations or unused libraries can severely impact startup
performance and baseline memory usage.

This is why tools like [R8](https://r8.googlesource.com/r8) (ProGuard) are
critical. R8 analyzes your application's bytecode and removes any classes or
methods that are never called ("dead code stripping").

### Hands-on exercise: the cost of bloat

To demonstrate the impact of code size, consider an experiment comparing two
builds of an application containing 300 generated classes (each with 500
methods):

- **CodeBloat (Unoptimized)**: The standard, unoptimized build containing all generated classes and unique strings.
- **CodeBloatOptimized**: The same source code, but compiled with R8 shrinking enabled.

#### 1. Ahead-of-time (AOT) compilation

To maximize the file-backed memory impact, we will use the `cmd package compile`
tool to ahead-of-time (AOT) compile the apps into `.oat` files.

    adb shell cmd package compile -m speed -f com.android.codebloat
    adb shell cmd package compile -m speed -f com.android.codebloat.optimized

Please note that this is a synthetic example. Typically, apps will use the
`speed-profile` compilation mode (see further below).

#### 2. Launch and compare

To see a **truly cold** start where the system must read code from storage, we
will drop the kernel's page cache before launching each app. This requires root
access.

Launch the unoptimized app:

> [!NOTE]
> **Note:** `drop_caches` requires your device be running a userdebug build with root access.

    adb shell am force-stop com.android.codebloat
    # Drop page cache to ensure the start is truly cold
    adb shell "echo 3 > /proc/sys/vm/drop_caches"
    adb shell am start -W -n com.android.codebloat/.MainActivity
    sleep 5 # Wait for the background thread to load classes
    adb shell dumpsys meminfo -s com.android.codebloat

Now do the same for the optimized app:

    adb shell am force-stop com.android.codebloat.optimized
    # Drop page cache to ensure the start is truly cold
    adb shell "echo 3 > /proc/sys/vm/drop_caches"
    adb shell am start -W -n com.android.codebloat.optimized/com.android.codebloat.MainActivity
    sleep 5
    adb shell dumpsys meminfo -s com.android.codebloat.optimized

##### The results

If you look at the **Code** row in the `App Summary` section, you will see a
massive difference:

- **Unoptimized `Code`**: \~30,000 KB (30 MB)
- **Optimized `Code`**: \~2,000 KB (2 MB)

Because R8 determined that the 500 methods inside those classes were never
actually doing anything useful (the `doSomething()` method only calls
`method0()`, and the results are ignored), it stripped almost all of the
artificially generated code out of the final APK.

#### 3. See the impact in Perfetto

The impact of code bloat is clearly visible during the initial loading phase of
the application. Specifically, look for the **`bindApplication`** slice on the
main thread, and nested slices starting with **`madvising`** , which indicate the
system preparing to load files from the APK and its compiled code (`.odex`).

On an interactive cold start, the system will `mmap()` and `madvise()` code and
other data from these files that is necessary for the app to load and run. The
value after "size=" in the **`madvising`** slices indicates how much data needs
to be loaded. This prefetching of the app's code is done to accelerate app
startup.

From the comparison we can see that the amount of app code that needed to be
loaded from storage to RAM was much greater in the bloated app case, resulting
in longer durations that contributed to a slower app start. Additionally, the
trace of the bloated app's start shows slices for loading secondary DEX files
(`classes2.dex`, `classes3.dex`) that the bloated app was forced to "spill" into
because it wouldn't fit in one DEX file.

##### In comparison (cold start on Pixel 10a)

| Metric | Unoptimized (CodeBloat) | Optimized (CodeBloatOptimized) |
|---|---|---|
| **`base.odex` madvise size** | \~7.9 MB (2.0 ms) | \~16 KB (0.003 ms) |
| **`base.apk` madvise size** | \~2.4 MB (2.4 ms) | \~4 KB (0.001 ms) |
| **`classes2.dex` madvise size** | \~7.3 MB (8.6 ms) | N/A |
| **`classes3.dex` madvise size** | \~7.3 MB (8.0 ms) | N/A |
| **Total `madvising` duration** | **\~21 ms** | **\~0.004 ms** |

> [!NOTE]
> **Note:** These traces were captured on a physical Pixel 10a. This device has relatively fast storage (UFS 3.1) for its launch year (2025), and was tested under ideal conditions (the device was idle so nothing was competing for I/O). On a device with slower UFS or eMMC storage, or under real-world I/O pressure, or with a much larger real-world app, these "madvising" slices can take significantly more time during a cold start.

##### Unoptimized app loading performance

![A screenshot of the Perfetto UI showing the com.android.codebloat process with
the madvising slices for the primary and secondary DEX
files](https://developer.android.com/static/topic/performance/memory/guide/images/app-code/code-bloat-loading.png)

##### Optimized app loading performance

![A screenshot of the Perfetto UI showing the com.android.codebloat.optimized
process with a single, tiny madvising
slice](https://developer.android.com/static/topic/performance/memory/guide/images/app-code/code-opt-loading.png)

The impact of code bloat varies by the size of the app, the characteristics of
the user's device, and system load.

#### PerfettoSQL for loading analysis

You can use the following queries to extract these metrics from your traces.

##### 1. App startup duration

This shows the time from when an app's Activity is launched until the Activity
has drawn a first frame.

    INCLUDE PERFETTO MODULE android.startup.startups;

    SELECT package, dur, startup_type
    FROM android_startups
    WHERE package LIKE 'com.android.codebloat%';

See:
[Understand the different app startup states](https://developer.android.com/topic/performance/vitals/launch-time#startup-state)

An app's startup duration is sensitive to many factors other than the ones
covered in this guide!

##### 2. Extract `madvising` sizes and durations

This query zooms in on the `madvising` part that we saw above.

    INCLUDE PERFETTO MODULE slices.with_context;

    SELECT
      name,
      dur/1e6 AS dur_ms
    FROM thread_slice
    WHERE process_name LIKE 'com.android.codebloat%'
      AND name LIKE 'madvising %';

##### 3. Main thread state breakdown (total duration per state)

This query shows how much time the app's main thread spent in different states.

    SELECT
      p.name AS process_name,
      state,
      sum(dur)/1e6 AS total_dur_ms
    FROM thread_state ts
    JOIN thread t USING (utid)
    JOIN process p USING (upid)
    WHERE p.name LIKE 'com.android.codebloat%'
      AND t.is_main_thread = 1
    GROUP BY p.name, state;

You can refine the query to only look at main thread states during the app's
startup duration.

    INCLUDE PERFETTO MODULE android.startup.startups;

    SELECT
      p.name AS process_name,
      ts.state,
      -- Calculate only the duration that falls within the startup window
      SUM(
        MAX(0,
          MIN(ts.ts + ts.dur, s.ts + s.dur) - MAX(ts.ts, s.ts)
        )
      ) / 1e6 AS startup_dur_ms
    FROM thread_state ts
    JOIN thread t USING (utid)
    JOIN process p USING (upid)
    -- Join on the package name to align thread states with the correct startup
    JOIN android_startups s ON s.package = p.name
    WHERE p.name LIKE 'com.android.codebloat%'
      AND t.is_main_thread = 1
      -- Only select thread states that overlap with the startup interval
      AND ts.ts + ts.dur > s.ts
      AND ts.ts < s.ts + s.dur
    GROUP BY 1, 2
    ORDER BY startup_dur_ms DESC;

This can expose some interesting problems, for instance:

- **High time spent Runnable (R) but not Running**: This indicates that the app's startup was delayed by CPU contention, i.e. the app's main thread could not run because other threads (possibly from other apps) were occupying the CPUs.
- **High time spent in Interruptible Sleep (D)**: This usually indicates slow I/O or memory pressure that is stalling the app's startup.
- **High time spent Sleeping (S)**: This means that the main thread was waiting for other threads to do work. Sometimes this indicates lock contention in the app's startup path (i.e. the main thread was blocked on an exclusive resource that was occupied by another thread in the app).

##### 4. Maximum file-backed memory (RSS file)

This metric correlates well with how much code and data the app loads at
startup. A more "bloated" app will reach a higher number here, causing memory
pressure on the system. Such pressure may in turn delay the app's startup, as
the system struggles to satisfy allocation requests, or diverts CPU time from
focusing on starting the app and towards reclaiming memory from other processes
to satisfy the starting app's immediate needs.

    SELECT
      p.name AS process_name,
      max(c.value)/1024.0/1024.0 AS max_rss_file_mb
    FROM counter c
    JOIN process_counter_track t ON c.track_id = t.id
    JOIN process p USING (upid)
    WHERE p.name LIKE 'com.android.codebloat%'
      AND t.name = 'mem.rss.file'
    GROUP BY p.name;

## ART compilation modes and memory

The Android Runtime (ART) can compile your application code in one of several
different modes, also known as
[compiler filters](https://source.android.com/docs/core/runtime/configure#compiler_filters).
The selected compiler filter has a direct impact on your app's memory footprint.

- **`verify`** : ART only performs bytecode verification. No AOT compilation is performed. Code is executed via the **Interpreter** or compiled at runtime by the **JIT** compiler.
  - **Memory Impact** : Smallest on-disk size. Native code memory usage is pushed into the `JIT Cache` (anonymous dirty memory).
- **`speed`** : ART performs full AOT compilation of all methods.
  - **Memory Impact** : Largest `.odex` size. Maximizes **file-backed (clean)
    memory** usage.
- **`speed-profile`** : ART only compiles methods that have been marked as "hot" in a **JIT profile** .
  - **Memory Impact**: Balanced approach. Only the most critical code is AOT compiled.

The most common filter is `speed-profile`, which is used when installing user
apps. This is configured in the system properties `pm.dexopt.install` and
`pm.dexopt.bg-dexopt`, and is typically set in
`build/make/target/product/runtime_libart.mk`.

Some system apps will use `speed` compilation, and will also compile at system
image build time. `verify` is typically only used in development use cases.

| Use case | Typical compiler filter |
|---|---|
| Development | `verify` |
| System image | `speed` |
| User apps | `speed-profile` |

### Hands-on exercise: compilation modes and memory

We can use the `CodeBloat` app to see how these filters affect memory. To
reproduce these measurements:

1. Force re-compile the app into the target mode.
2. Force-stop and cold-start the app.
3. Wait for the background thread to finish touching classes (watch logcat or wait 5s).
4. Run `adb shell dumpsys meminfo com.android.codebloat`.

> [!NOTE]
> **Note:** These measurements were taken on a Pixel 10 Pro Fold. Actual numbers will vary by device; these are for scale.

#### Mode: `verify` (no AOT)

    adb shell cmd package compile -m verify -f com.android.codebloat
    adb shell am force-stop com.android.codebloat
    adb shell am start -W -n com.android.codebloat/.MainActivity
    sleep 5
    adb shell dumpsys meminfo com.android.codebloat

In `verify` mode, the app Summary shows: \* **Code PSS** : \~8,000 KB \* **Dalvik
Other (JIT)**: \~25,000 KB

Because no code is compiled AOT, the runtime must JIT-compile hot methods into
the **JIT Cache** , which shows up as **dirty anonymous memory** (`Dalvik
Other`).

#### Mode: `speed` (full AOT)

    adb shell cmd package compile -m speed -f com.android.codebloat
    adb shell am force-stop com.android.codebloat
    adb shell am start -W -n com.android.codebloat/.MainActivity
    sleep 5
    adb shell dumpsys meminfo com.android.codebloat

In `speed` mode, the results shift dramatically: \* **Code PSS** : \~24,000 KB \*
**Dalvik Other (JIT)**: \~5,000 KB

The application's code is now mapped from the `.odex` file as **clean
file-backed memory**. This reduces pressure on the JIT cache and makes the
memory eligible for eviction under pressure, rather than being "stuck" as dirty
RAM.

#### Mode: `speed-profile` (selective AOT)

Modern apps may bundle a `baseline.prof` baseline profile. ART uses this to
selectively compile only the code needed for a fast, memory-efficient startup.

In this exercise we will create a baseline profile to list the app's startup
classes. However in reality the compiler may also receive profiles from external
sources such as from the application store ("cloud profiles"), which can provide
crowdsourced JIT profiles for apps regardless of whether the developer also
bundled a baseline profile that they generated.

#### Generating and using on-device profiles

To see the impact of `speed-profile`, you can generate your own profile
on-device:

1. **Reset and Start**:

       adb shell am force-stop com.android.codebloat

2. **Interact**: Start the app and let it run its startup sequence.

3. **Dump Profile**:

       adb shell kill -s SIGUSR1 $(pidof com.android.codebloat)

   (This forces the app to write its current profile to disk).
4. **Install Profile**:

       adb shell cp /data/misc/profiles/cur/0/com.android.codebloat/primary.prof \
       /data/misc/profiles/ref/com.android.codebloat/primary.prof

5. **Compile**:

       adb shell cmd package compile -m speed-profile -f com.android.codebloat

When you launch again, you'll see a balance: **Code PSS** will be lower than
`speed` (e.g., \~16,000 KB) because only the "hot" startup methods were compiled,
leaving the rest to be handled by the interpreter or JIT only if they are ever
actually used.

See:

- [Baseline Profiles overview](https://developer.android.com/topic/performance/baselineprofiles/overview)
- [Difference between Baseline Profiles and Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/difference-baseline-startup)

## Deep dive into compiled code

If you want to see exactly what instructions ART is generating, refer to
`art/DISASSEMBLY_GUIDE.md`.

It provides detailed instructions on using:

- **`oatdump`** : To see ARM64 instructions inside an existing `.odex` file.
- **`dex2oat`**: To simulate compilation with verbose debug flags.

### Exercise: code inlining

One reason compiled code can grow unexpectedly is **method inlining**. The
compiler may decide to copy the body of a small, frequently called method
directly into its callers.

In our `CodeBloat` app, the `doSomething()` method in every generated class
simply calls `method0()`. When compiled in `speed` mode, ART's Optimizing
compiler will likely inline `method0()` into `doSomething()`.

**Exercise:** Verify this using `oatdump` on your device:

    # 1. Find the path to the application's APK and compiled .odex file
    adb shell pm path com.android.codebloat
    # Output: package:/data/app/~~.../base.apk

    adb shell "dumpsys package com.android.codebloat | grep 'location is' | head -n 1"
    # Example output: [location is /data/app/~~.../oat/arm64/base.odex]

    # 2. Run oatdump (substituting the correct path to base.odex)
    adb shell oatdump --oat-file=/data/app/~~.../oat/arm64/base.odex \
                      --class-filter=com.android.codebloat.GeneratedClass0

Look for the `doSomething` method in the output. If it was inlined, you will see
the instructions to load the long string constant directly within `doSomething`,
rather than a `bl` instruction targeting `method0`.

#### Visualizing the optimization (CFG)

To see exactly when the compiler decided to inline the method, you can produce a
**Control Flow Graph (CFG)**. This shows the state of the code at every stage of
the optimization pipeline, with every transformation over the compiler's
Intermediate Representation (IR) until the code is lowered to the target ISA
(e.g. ARM64).

1. **Run `dex2oat` with dump flags** : Use the `--verbose-methods` flag to limit
   the output to specific methods; otherwise, the `.cfg` file for a large app
   can grow to several gigabytes.

       # Substitution of actual paths required:
       adb shell dex2oat64 --dex-file=/data/app/~~.../base.apk \
                           --oat-file=/data/local/tmp/dump.odex \
                           --compiler-filter=speed \
                           --dump-cfg=/data/local/tmp/codebloat.cfg \
                           --verbose-methods=doSomething

2. **Pull and View** : Pull the `.cfg` file to your workstation and open it with
   [IR Hydra](https://mrale.ph/irhydra/1/).

3. **Find the Inliner** : In IR Hydra, load the compilation artifacts and search
   for `doSomething`. Compare the representation before and after the
   **Inliner** pass. You will see the graph expand as the instructions from
   `method0` are merged into the caller.

Alternatively, use the **Opt Pipeline** tool in **Compiler Explorer** (as
described in the section above) and enter similar code to see a similar
transformation performed at the **Inliner** pass.

### Exercise: volatile fields and memory barriers

In the `MemoryLab` app, the `mGarbageSink` field is marked as `volatile`. This
ensures that the compiler doesn't optimize away our garbage allocations.

    public volatile byte[] mGarbageSink;

In the ARM64 disassembly, you will see that every store to this field is
accompanied by a **Memory Barrier** (`dmb ish`) or use of
**Load-Acquire/Store-Release** instructions (`ldar`/`stlr`). This ensures thread
visibility but adds a few extra instructions to every access, increasing the
code size slightly compared to a regular field.

**Exercise:** Find the field accesses and the associated memory barriers in the
disassembly.

### Exercise: implicit suspend checks

If you disassemble a loop, like the one in `generateAllocationChurn`, you will
notice a curious instruction at the end of the loop body:

    ldr x21, [x21]

This is an **Implicit Suspend Check** . ART uses this to allow the Garbage
Collector to pause threads safely. Register `x21` normally points to itself.
When the GC needs to suspend the thread, it "poisons" that memory location. The
next time the thread executes that `ldr`, it will trigger a fault, which the
runtime catches and uses to transition the thread into a suspended state.

This pattern is repeated in every loop and at the start of every method,
contributing to the total code size of your application.

**Exercise:** Find all the implicit suspend checks in the method disassembly,
and try to correlate them to the original source code.

*** ** * ** ***

**[← WebView](https://developer.android.com/topic/performance/memory/guide/webview-memory) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \| [Threads →](https://developer.android.com/topic/performance/memory/guide/threads)**