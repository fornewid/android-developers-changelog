---
title: https://developer.android.com/topic/performance/memory
url: https://developer.android.com/topic/performance/memory
source: md.txt
---

# Manage your app's memory

This page explains how to proactively reduce memory usage within your app. For information about how the Android operating system manages memory, see[Overview of memory management](https://developer.android.com/topic/performance/memory-overview).

Random-access memory (RAM) is a valuable resource for any software development environment, and it's even more valuable for a mobile operating system where physical memory is often constrained. Although both the Android Runtime (ART) and Dalvik virtual machine perform routine garbage collection, this doesn't mean you can ignore when and where your app allocates and releases memory. You still need to avoid introducing memory leaks---usually caused by holding onto object references in static member variables---and release any[Reference](https://developer.android.com/reference/java/lang/ref/Reference)objects at the appropriate time as defined by lifecycle callbacks.

## Monitor available memory and memory usage

You must find your app's memory usage problems before you can fix them. The[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)in Android Studio helps you find and diagnose memory issues in the following ways:

- See how your app allocates memory over time. The Memory Profiler shows a realtime graph of how much memory your app is using, the number of allocated Java objects, and when garbage collection occurs.
- Initiate garbage collection events and take a snapshot of the Java heap while your app runs.
- Record your app's memory allocations, inspect all allocated objects, view the stack trace for each allocation, and jump to the corresponding code in the Android Studio editor.

### Release memory in response to events

Android can reclaim memory from your app or stop your app entirely if necessary to free up memory for critical tasks, as explained in[Overview of memory management](https://developer.android.com/topic/performance/memory-overview). To further help balance the system memory and avoid the system's need to stop your app process, you can implement the[ComponentCallbacks2](https://developer.android.com/reference/android/content/ComponentCallbacks2)interface in your[Activity](https://developer.android.com/reference/android/app/Activity)classes. The provided[onTrimMemory()](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))callback method notifies your app of lifecycle or memory-related events that present a good opportunity for your app to voluntarily reduce its memory usage. Freeing memory may reduce the likelihood of your app being killed by the[low-memory killer](https://developer.android.com/topic/performance/memory-management#low-memory_killer).

You can implement the`onTrimMemory()`callback to respond to different memory-related events, as shown in the following example:  

### Kotlin

```kotlin
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
```

### Java

```java
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
```

### Check how much memory you need

To allow multiple running processes, Android sets a hard limit on the heap size allotted for each app. The exact heap size limit varies between devices based on how much RAM the device has available overall. If your app reaches the heap capacity and tries to allocate more memory, the system throws an[OutOfMemoryError](https://developer.android.com/reference/java/lang/OutOfMemoryError).

To avoid running out of memory, you can query the system to determine how much heap space is available on the current device. You can query the system for this figure by calling[getMemoryInfo()](https://developer.android.com/reference/android/app/ActivityManager#getMemoryInfo(android.app.ActivityManager.MemoryInfo)). This returns an[ActivityManager.MemoryInfo](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo)object that provides information about the device's current memory status, including available memory, total memory, and the memory threshold---the memory level at which the system begins to stop processes. The`ActivityManager.MemoryInfo`object also exposes[lowMemory](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo#lowMemory), which is a simple boolean that tells you whether the device is running low on memory.

The following example code snippet shows how to use the`getMemoryInfo()`method in your app.  

### Kotlin

```kotlin
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
```

### Java

```java
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
```

## Use more memory-efficient code constructs

Some Android features, Java classes, and code constructs use more memory than others. You can minimize how much memory your app uses by choosing more efficient alternatives in your code.

### Use services sparingly

We strongly recommend you don't leave services running when it's unnecessary. Leaving unnecessary services running is one of the worst memory-management mistakes an Android app can make. If your app needs a[service](https://developer.android.com/guide/components/services)to work in the background, don't leave it running unless it needs to run a job. Stop your service when it completes its task. Otherwise, you might cause a memory leak.

When you start a service, the system prefers to keep the process for that service running. This behavior makes service processes very expensive because the RAM used by a service remains unavailable for other processes. This reduces the number of cached processes that the system can keep in the LRU cache, making app switching less efficient. It can even lead to thrashing in the system when memory is tight and the system can't maintain enough processes to host all the services currently running.

Generally, avoid using persistent services because of the ongoing demands they place on available memory. Instead, we recommend you use an alternative implementation, such as[WorkManager](https://developer.android.com/reference/androidx/work/WorkManager). For more information about how to use`WorkManager`to schedule background processes, see[Persistent work](https://developer.android.com/guide/background/persistent).

### Use optimized data containers

Some of the classes provided by the programming language aren't optimized for use on mobile devices. For example, the generic[HashMap](https://developer.android.com/reference/java/util/HashMap)implementation can be memory inefficient because it needs a separate entry object for every mapping.

The Android framework includes several optimized data containers, including[SparseArray](https://developer.android.com/reference/android/util/SparseArray),[SparseBooleanArray](https://developer.android.com/reference/android/util/SparseBooleanArray), and[LongSparseArray](https://developer.android.com/reference/androidx/collection/LongSparseArray). For example, the`SparseArray`classes are more efficient because they avoid the system's need toautoboxthe key and sometimes the value, which creates yet another object or two per entry.

If necessary, you can always switch to raw arrays for a lean data structure.

### Be careful with code abstractions

Developers often use abstractions as a good programming practice because they can improve code flexibility and maintenance. However, abstractions are significantly more costly because they generally require more code that needs to be executed, requiring more time and RAM to map the code into memory. If your abstractions aren't significantly beneficial, avoid them.

### Use lite protobufs for serialized data

[Protocol buffers (protobufs)](https://developers.google.com/protocol-buffers/docs/overview)are a language-neutral, platform-neutral, extensible mechanism designed by Google for serializing structured data---similar to XML, but smaller, faster, and simpler. If you use protobufs for your data, always use lite protobufs in your client-side code. Regular protobufs generate extremely verbose code, which can cause many problems in your app, such as increased RAM use, significant APK size increase, and slower execution.

For more information, see the[protobuf readme](https://android.googlesource.com/platform/external/protobuf/+/master/java/README.md#installation-lite-version-with-maven).

### Avoid memory churn

Garbage collection events don't affect your app's performance. However, many garbage collection events that occur over a short period of time can quickly drain the battery as well as marginally increase the time to set up frames due to necessary interactions between the garbage collector and app threads. The more time the system spends on garbage collection, the faster the battery drains.

Often,*memory churn*can cause a large number of garbage collection events to occur. In practice, memory churn describes the number of allocated temporary objects that occur in a given amount of time.

For example, you might allocate multiple temporary objects within a`for`loop. Or, you might create new[Paint](https://developer.android.com/reference/android/graphics/Paint)or[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)objects inside the[onDraw()](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas))function of a view. In both cases, the app creates a lot of objects quickly at high volume. These can quickly consume all the available memory in the young generation, forcing a garbage collection event to occur.

Use the[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)to find the places in your code where the memory churn is high before you can fix them.

After you identify the problem areas in your code, try to reduce the number of allocations within performance-critical areas. Consider moving things out of inner loops or perhaps moving them into a[factory-based](https://en.wikipedia.org/wiki/Factory_method_pattern)allocation structure.

You can also evaluate whether object pools benefit the use case. With an object pool, instead of dropping an object instance on the floor, you release it into a pool after it's no longer needed. The next time an object instance of that type is needed, you can acquire it from the pool rather than allocating it.

Thoroughly evaluate performance to determine if an object pool is suitable in a given situation. There are cases in which object pools might make performance worse. Even though pools avoid allocations, they introduce other overheads. For example, maintaining the pool usually involves synchronization, which has non-negligible overhead. Also, clearing the pooled object instance to avoid memory leaks during release and then its initialization during acquisition can have non-zero overhead.

Holding back more object instances in the pool than needed also puts a burden on the garbage collection. While object pools reduce the number of garbage collection invocations, they end up increasing the amount of work needed for every invocation, as it is proportional to the number of live (reachable) bytes.

## Remove memory-intensive resources and libraries

Some resources and libraries within your code can consume memory without you realizing. The overall size of your app, including third-party libraries or embedded resources, can affect how much memory your app consumes. You can improve your app's memory consumption by removing redundant, unnecessary, or bloated components, or resources and libraries from your code.

### Reduce overall APK size

You can significantly reduce your app's memory usage by reducing the overall size of your app. Bitmap size, resources, animation frames, and third-party libraries can all contribute to the size of your app. Android Studio and the Android SDK provide multiple tools to help reduce the size of your resources and external dependencies. These tools support modern code-shrinking methods, such as[R8 compilation](https://developer.android.com/studio/build/shrink-code).

For more information about reducing your overall app size, see[Reduce your app size](https://developer.android.com/topic/performance/reduce-apk-size).

### Use Hilt or Dagger 2 for dependency injection

Dependency injection frameworks can simplify the code you write and provide an adaptive environment that's useful for testing and other configuration changes.

If you intend to use a dependency injection framework in your app, consider using[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)or[Dagger](http://dagger.dev/). Hilt is a dependency injection library for Android that runs on top of Dagger. Dagger doesn't use reflection to scan your app's code. You can use Dagger's static compile-time implementation in Android apps without needless runtime cost or memory usage.

Other dependency injection frameworks that use reflection initialize processes by scanning your code for annotations. This process can require significantly more CPU cycles and RAM, and can cause a noticeable lag when the app launches.

### Be careful about using external libraries

External library code often isn't written for mobile environments and can be inefficient for working on a mobile client. When you use an external library, you might need to optimize that library for mobile devices. Plan for this work ahead of time and analyze the library in terms of code size and RAM footprint before using it.

Even some mobile-optimized libraries can cause problems due to differing implementations. For example, one library might use lite protobufs while another uses micro protobufs, resulting in two different protobuf implementations in your app. This can happen with different implementations of logging, analytics, image-loading frameworks, caching, and many other things you don't expect.

Although[ProGuard](https://developer.android.com/tools/help/proguard)can help remove APIs and resources with the right flags, it can't remove a library's large internal dependencies. The features you want in these libraries might require lower-level dependencies. This becomes especially problematic when you use an[Activity](https://developer.android.com/reference/android/app/Activity)subclass from a library---which can have wide swaths of dependencies---when libraries use reflection, which is common and requires manually tweaking ProGuard to make it work.

Avoid using a shared library for just one or two features out of dozens. Don't pull in a large amount of code and overhead that you don't use. When you consider whether to use a library, look for an implementation that strongly matches what you need. Otherwise, you might decide to create your own implementation.