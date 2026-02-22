---
title: https://developer.android.com/ndk/guides/debug
url: https://developer.android.com/ndk/guides/debug
source: md.txt
---

# Debug your project

## Debug native crashes

If you're struggling to understand a native crash dump or tombstone,[Debugging Native Android Platform Code](https://source.android.com/devices/tech/debug/index.html)is a good introduction.

For a fuller catalog of common types of crash and how to investigate them, see[Diagnosing Native Crashes](https://source.android.com/devices/tech/debug/native-crash).

The[ndk-stack](https://developer.android.com/ndk/guides/ndk-stack)tool can help symbolize your crashes. You can debug crashes in Android Studio as described in the general[Debug your app](https://developer.android.com/studio/debug)documentation. If you prefer to use the command-line,[ndk-gdb](https://developer.android.com/ndk/guides/ndk-gdb)lets you attach either`gdb`or`lldb`from your shell.

### Provide apps direct access to tombstone traces

Starting in Android 12 (API level 31), you can access your app's native crash tombstone as a[protocol buffer](https://developers.google.com/protocol-buffers/)through the[`ApplicationExitInfo.getTraceInputStream()`](https://developer.android.com/reference/android/app/ApplicationExitInfo#getTraceInputStream())method. The protocol buffer is serialized using[this schema](https://android.googlesource.com/platform/system/core/+/refs/heads/main/debuggerd/proto/tombstone.proto). Previously, the only way to get access to this information was through the[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)(adb).

Here's an example of how to implement this in your app:  

    ActivityManager activityManager: ActivityManager = getSystemService(Context.ACTIVITY_SERVICE);
    MutableList<ApplicationExitInfo> exitReasons = activityManager.getHistoricalProcessExitReasons(/* packageName = */ null, /* pid = */ 0, /* maxNum = */ 5);
    for (ApplicationExitInfo aei: exitReasons) {
        if (aei.getReason() == REASON_CRASH_NATIVE) {
            // Get the tombstone input stream.
            InputStream trace = aei.getTraceInputStream();
            // The tombstone parser built with protoc uses the tombstone schema, then parses the trace.
            Tombstone tombstone = Tombstone.parseFrom(trace);
        }
    }

## Debug native memory issues

### Address Sanitizer (HWASan/ASan)

[HWAddress Sanitizer](https://developer.android.com/ndk/guides/hwasan)(HWASan) and[Address Sanitizer](https://developer.android.com/ndk/guides/asan)(ASan) are similar to Valgrind, but significantly faster and much better supported on Android.

These are your best option for debugging memory errors on Android.

### Malloc debug

See[Malloc Debug](https://android.googlesource.com/platform/bionic/+/main/libc/malloc_debug/README.md)and[Native Memory Tracking using libc Callbacks](https://android.googlesource.com/platform/bionic/+/main/libc/malloc_debug/README_api.md)for a thorough description of the C library's built-in options for debugging native memory issues.

### Malloc hooks

If you want to build your own tools, Android's libc also supports intercepting all allocation/free calls that happen during program execution. See the[malloc_hooks documentation](https://android.googlesource.com/platform/bionic/+/main/libc/malloc_hooks/README.md)for usage instructions.

### Malloc statistics

Android supports the[mallinfo(3)](http://man7.org/linux/man-pages/man3/mallinfo.3.html)and[malloc_info(3)](http://man7.org/linux/man-pages/man3/malloc_info.3.html)extensions to`<malloc.h>`.

The`malloc_info`functionality is available in Android 6.0 (Marshmallow) and higher and its XML schema is documented in Bionic's[malloc.h](https://android.googlesource.com/platform/bionic/+/main/libc/include/malloc.h)header.

## Profiling

For CPU profiling of native code, you can use[Simpleperf](https://developer.android.com/ndk/guides/simpleperf).