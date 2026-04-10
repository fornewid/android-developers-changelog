---
title: https://developer.android.com/guide/topics/androidgo/optimize-memory
url: https://developer.android.com/guide/topics/androidgo/optimize-memory
source: md.txt
---

# Optimize app memory

Memory is a valuable resource in any software development environment, but it's even more valuable on a mobile operating system where physical memory is often constrained. This is especially true for natively low-memory devices found commonly with Android (Go edition). There are a few ways to help optimize memory in your app to help it run smoothly in these environments.

## Best practices

### Release cache memory

There may not be enough memory to keep background processes running as you would in a typical environment. In this case, you can use[`onTrimMemory()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))to trim unneeded memory from your app's process. To best identify the current trim level for your app, use[`ActivityManager.getMyMemoryState(RunningAppProcessInfo)`](https://developer.android.com/reference/android/app/ActivityManager#getMyMemoryState(android.app.ActivityManager.RunningAppProcessInfo))and optimize or trim any unnecessary resources. For example, you can trim unnecessary memory usage from expressions, search, view cache, or openable extensions to reduce the number of times your app experiences crashes or ANRs due to low memory.

### Task scheduling

Concurrent scheduling can lead to multiple memory intensive operations to run in parallel, leading to competition for resources exceeding the peak memory usage of an app. Try to appropriately allocate resources by separating processes into CPU intensive, low latency tasks in the right[thread pool](https://developer.android.com/guide/background/threading)to run on devices that may face various resource constraints.

### Memory leaks

Various tools, such as[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)in Android Studio and[Perfetto](https://perfetto.dev/docs/case-studies/memory)are specifically available to help find and reduce memory leaks within your app. It's highly encouraged that you use these tools to identify and fix potential memory issues to allow other components of your app to run without additional pressure on the system.

### Other tips

- Large images or drawables consume more memory in apps. Identify and optimize large or full-colored bitmaps to reduce memory usage.
- Try to choose other options for GIFs in your app when building for Android (Go edition) as GIFs consume a lot of memory.
- You can reduce PNG file sizes without losing image quality using tools like[WebP](https://developer.android.com/studio/write/convert-webp), pngcrush, and pngquant. All of these tools can reduce PNG file size while preserving the perceptive image quality.
- The aapt tool can optimize the image resources placed in`res/drawable/`with lossless compression during the build process. For example, the aapt tool can convert a true-color PNG that does not require more than 256 colors to an 8-bit PNG with a color palette. Doing so results in an image of equal quality but a smaller memory footprint.