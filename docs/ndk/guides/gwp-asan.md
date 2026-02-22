---
title: https://developer.android.com/ndk/guides/gwp-asan
url: https://developer.android.com/ndk/guides/gwp-asan
source: md.txt
---

| **Important:** GWP-Asan is one of many tools available for memory debugging and mitigation. See [Memory error debugging and mitigation](https://developer.android.com/ndk/guides/memory-debug) for an overview of all the tools.
| **Important:** On devices that run Android 14 (API level 34) or higher, all apps use [Recoverable GWP-ASan](https://developer.android.com/ndk/guides/gwp-asan#recoverable) by default.

GWP-ASan is a native memory allocator feature that helps find
[use-after-free](https://cwe.mitre.org/data/definitions/416.html)
and
[heap-buffer-overflow](https://cwe.mitre.org/data/definitions/122.html)
bugs. Its informal name is a recursive acronym,"**G** WP-ASan **W** ill
**P** rovide **A** llocation **SAN** ity". Unlike
[HWASan](https://source.android.com/devices/tech/debug/hwasan) or
[Malloc Debug](https://android.googlesource.com/platform/bionic/+/master/libc/malloc_debug/README.md),
GWP-ASan does not require source or recompilation (that is, works with
prebuilts), and works on both 32- and 64-bit processes (although 32-bit crashes
have [less debugging information](https://developer.android.com/ndk/guides/gwp-asan#allocation-deallocation-traces-are-missing)).
This topic outlines the actions you need to take to enable this feature in your
app. GWP-ASan is available on apps that target Android 11 (API level 30) or higher.

## Overview

GWP-ASan is enabled on some randomly-selected system applications and platform
executables upon process start-up (or when the zygote forks). Enable GWP-ASan in
your own app to help you find memory-related bugs, and to prepare your app for
[ARM Memory Tagging Extension (MTE) support](https://community.arm.com/developer/ip-products/processors/b/processors-ip-blog/posts/enhancing-memory-safety).
The allocation sampling mechanisms also provide reliability against
[queries of death](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/).

Once enabled, GWP-ASan intercepts a randomly-chosen subset of heap allocations,
and places them into a special region that catches difficult-to-detect heap
memory corruption bugs. Given enough users, even this low sampling rate will
find heap memory safety bugs that aren't being found through regular testing.
For example, GWP-ASan has found
[a significant number of bugs](https://bugs.chromium.org/p/chromium/issues/list?q=Hotlist%3DGWP-ASan&can=1)
in the Chrome browser (many of which are still under restricted view).

GWP-ASan collects additional information about all of the allocations that it
intercepts. This information is available when GWP-ASan detects a memory safety
violation and is automatically placed into the native crash report, which can
aid significantly in debugging (see [Example](https://developer.android.com/ndk/guides/gwp-asan#example)).

GWP-ASan is designed to not incur any significant CPU overhead. GWP-ASan
introduces a small, fixed RAM overhead when enabled. This overhead is decided by
the Android system and is currently approximately 70 kibibytes (KiB) for each
affected process.

## Opt-in your app

GWP-ASan may be enabled by apps on a per-process level by using the
`android:gwpAsanMode` tag in the app manifest. The following options are
supported:

- Always disabled (`android:gwpAsanMode="never"`): This setting completely
  disables GWP-ASan in your app and is the default for non-system apps.

- Default (`android:gwpAsanMode="default"` or unspecified): Android 13 (API
  level 33) and lower - GWP-ASan is disabled. Android 14 (API level 34) and
  higher - [Recoverable GWP-ASan](https://developer.android.com/ndk/guides/gwp-asan#recoverable) is enabled.

- Always enabled (`android:gwpAsanMode="always"`): This setting enables
  GWP-ASan in your app, which includes the following:

  1. The operating system reserves a fixed amount of RAM for GWP-ASan
     operations, approximately \~70KiB for each affected process. (Enable
     GWP-ASan if your app is not critically sensitive to increases in memory
     usage.)

  2. GWP-ASan intercepts a randomly-chosen subset of heap allocations and
     places them into a special region that reliably detects memory safety
     violations.

  3. When a memory safety violation occurs in the special region, GWP-ASan
     terminates the process.

  4. GWP-ASan provides additional information about the fault in the crash
     report.

To enable GWP-ASan globally for your app, add the following to your
`AndroidManifest.xml` file:  

```xml
<application android:gwpAsanMode="always">
  ...
</application>
```

Additionally, GWP-ASan can be explicitly enabled or disabled for specific
subprocesses of your app. You can target activities and services using processes
that are explicitly opted-in or opted-out of GWP-ASan. See the following for an
example:  

```xml
<application>
  <processes>
    <!-- Create the (empty) application process -->
    <process />

    <!-- Create subprocesses with GWP-ASan both explicitly enabled and disabled. -->
    <process android:process=":gwp_asan_enabled"
               android:gwpAsanMode="always" />
    <process android:process=":gwp_asan_disabled"
               android:gwpAsanMode="never" />
  </processes>

  <!-- Target services and activities to be run on either the GWP-ASan enabled or disabled processes. -->
  <activity android:name="android.gwpasan.GwpAsanEnabledActivity"
            android:process=":gwp_asan_enabled" />
  <activity android:name="android.gwpasan.GwpAsanDisabledActivity"
            android:process=":gwp_asan_disabled" />
  <service android:name="android.gwpasan.GwpAsanEnabledService"
           android:process=":gwp_asan_enabled" />
  <service android:name="android.gwpasan.GwpAsanDisabledService"
           android:process=":gwp_asan_disabled" />
</application>
```

## Recoverable GWP-ASan

Android 14 (API level 34) and higher support Recoverable GWP-ASan, which helps
developers find heap-buffer-overflow and heap-use-after-free bugs in
production without degrading user experience. When `android:gwpAsanMode` is
unspecified in an `AndroidManifest.xml`, the app uses Recoverable
GWP-ASan.

Recoverable GWP-ASan differs from the base GWP-ASan in the following ways:

1. Recoverable GWP-ASan is enabled only on approximately 1% of app launches, rather than every application launch.
2. When a heap-use-after-free or heap-buffer-overflow bug is detected, this bug appears in the crash report (tombstone). This crash report is available through the [`ActivityManager#getHistoricalProcessExitReasons`](https://developer.android.com/reference/kotlin/android/app/ActivityManager#gethistoricalprocessexitreasons) API, the same as the original GWP-ASan.
3. Instead of exiting after dumping the crash report, Recoverable GWP-ASan allows memory corruption to occur, and the app continues running. While the process may continue as usual, the app's behavior is no longer specified. Due to the memory corruption, the app may crash at some arbitrary point in the future, or it may continue without any user-visible impact.
4. Recoverable GWP-ASan is disabled after the crash report is dumped. Therefore, an app can get only a single Recoverable GWP-ASan report per app launch.
5. If a custom signal handler is installed in the app, it's never called for a SIGSEGV signal that's indicative of a Recoverable GWP-ASan fault.

Because Recoverable GWP-ASan crashes indicate real instances of memory
corruption on end-user devices, we highly recommend triaging and fixing bugs
identified by Recoverable GWP-ASan with a high priority.

## Developer support

These sections outline issues that might occur when using GWP-ASan and how to
address them.

### Allocation/deallocation traces are missing

If you are diagnosing a native crash that appears to be missing
allocation/deallocation frames, your application is likely missing
[frame pointers](https://en.wikipedia.org/wiki/Call_stack#Stack_and_frame_pointers).
GWP-ASan uses frame pointers to record allocation and deallocation traces for
performance reasons, and is unable to unwind the stack trace if they are not
present.

Frame pointers are on by default for arm64 devices, and off by default for arm32
devices. Because applications don't have control over libc, it is (in general)
not possible for GWP-ASan to collect allocation/deallocation traces for 32-bit
executables or apps. 64-bit applications should ensure that they are **not**
built with `-fomit-frame-pointer` so that GWP-ASan can collect allocation and
deallocation stack traces.

### Reproducing safety violations

GWP-ASan is designed to catch heap memory safety violations on user devices.
GWP-ASan provides as much context as possible about the crash (access trace of
the violation, cause string, and allocation/deallocation traces), but it might
still be hard to deduce how the violation occurred. Unfortunately, as the bug
detection is probabilistic, GWP-ASan reports are often tricky to reproduce on a
local device.

In these instances, if the bug affects 64-bit devices, you should use
[HWAddressSanitizer](https://developer.android.com/ndk/guides/hwasan) (HWASan). HWASan detects memory safety
violations reliably on stack, heap, and globals. Running your application with
HWASan might reliably reproduce the same result that's being reported by
GWP-ASan.

In cases where running your application under HWASan is insufficient to
root-cause a bug, you should try to
[fuzz](https://source.android.com/preview/devices/tech/debug/libfuzzer) the code
in question. You can target your fuzzing efforts based on information in the
GWP-ASan report, which can reliably detect and reveal underlying code health
problems.

## Example

This example native code has a heap use-after-free bug:  

    #include <jni.h>
    #include <string>
    #include <string_view>

    jstring native_get_string(JNIEnv* env) {
       std::string s = "Hellooooooooooooooo ";
       std::string_view sv = s + "World\n";

       // BUG: Use-after-free. `sv` holds a dangling reference to the ephemeral
       // string created by `s + "World\n"`. Accessing the data here is a
       // use-after-free.
       return env->NewStringUTF(sv.data());
    }

    extern "C" JNIEXPORT jstring JNICALL
    Java_android11_test_gwpasan_MainActivity_nativeGetString(
        JNIEnv* env, jobject /* this */) {
      // Repeat the buggy code a few thousand times. GWP-ASan has a small chance
      // of detecting the use-after-free every time it happens. A single user who
      // triggers the use-after-free thousands of times will catch the bug once.
      // Alternatively, if a few thousand users each trigger the bug a single time,
      // you'll also get one report (this is the assumed model).
      jstring return_string;
      for (unsigned i = 0; i < 0x10000; ++i) {
        return_string = native_get_string(env);
      }

      return reinterpret_cast<jstring>(env->NewGlobalRef(return_string));
    }

For a test run using the example code above, GWP-ASan successfully caught the
illegal usage and triggered the crash report below. GWP-ASan has automatically
enhanced the report by providing information about the type of crash, the
allocation metadata, and the associated allocation and deallocation stack
traces.  

    *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    Build fingerprint: 'google/sargo/sargo:10/RPP3.200320.009/6360804:userdebug/dev-keys'
    Revision: 'PVT1.0'
    ABI: 'arm64'
    Timestamp: 2020-04-06 18:27:08-0700
    pid: 16227, tid: 16227, name: 11.test.gwpasan  >>> android11.test.gwpasan <<<
    uid: 10238
    signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x736ad4afe0
    Cause: [GWP-ASan]: Use After Free on a 32-byte allocation at 0x736ad4afe0

    backtrace:
          #00 pc 000000000037a090  /apex/com.android.art/lib64/libart.so (art::(anonymous namespace)::ScopedCheck::CheckNonHeapValue(char, art::(anonymous namespace)::JniValueType)+448)
          #01 pc 0000000000378440  /apex/com.android.art/lib64/libart.so (art::(anonymous namespace)::ScopedCheck::CheckPossibleHeapValue(art::ScopedObjectAccess&, char, art::(anonymous namespace)::JniValueType)+204)
          #02 pc 0000000000377bec  /apex/com.android.art/lib64/libart.so (art::(anonymous namespace)::ScopedCheck::Check(art::ScopedObjectAccess&, bool, char const*, art::(anonymous namespace)::JniValueType*)+612)
          #03 pc 000000000036dcf4  /apex/com.android.art/lib64/libart.so (art::(anonymous namespace)::CheckJNI::NewStringUTF(_JNIEnv*, char const*)+708)
          #04 pc 000000000000eda4  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (_JNIEnv::NewStringUTF(char const*)+40)
          #05 pc 000000000000eab8  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (native_get_string(_JNIEnv*)+144)
          #06 pc 000000000000edf8  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (Java_android11_test_gwpasan_MainActivity_nativeGetString+44)
          ...

    deallocated by thread 16227:
          #00 pc 0000000000048970  /apex/com.android.runtime/lib64/bionic/libc.so (gwp_asan::AllocationMetadata::CallSiteInfo::RecordBacktrace(unsigned long (*)(unsigned long*, unsigned long))+80)
          #01 pc 0000000000048f30  /apex/com.android.runtime/lib64/bionic/libc.so (gwp_asan::GuardedPoolAllocator::deallocate(void*)+184)
          #02 pc 000000000000f130  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (std::__ndk1::_DeallocateCaller::__do_call(void*)+20)
          ...
          #08 pc 000000000000ed6c  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >::~basic_string()+100)
          #09 pc 000000000000ea90  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (native_get_string(_JNIEnv*)+104)
          #10 pc 000000000000edf8  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (Java_android11_test_gwpasan_MainActivity_nativeGetString+44)
          ...

    allocated by thread 16227:
          #00 pc 0000000000048970  /apex/com.android.runtime/lib64/bionic/libc.so (gwp_asan::AllocationMetadata::CallSiteInfo::RecordBacktrace(unsigned long (*)(unsigned long*, unsigned long))+80)
          #01 pc 0000000000048e4c  /apex/com.android.runtime/lib64/bionic/libc.so (gwp_asan::GuardedPoolAllocator::allocate(unsigned long)+368)
          #02 pc 000000000003b258  /apex/com.android.runtime/lib64/bionic/libc.so (gwp_asan_malloc(unsigned long)+132)
          #03 pc 000000000003bbec  /apex/com.android.runtime/lib64/bionic/libc.so (malloc+76)
          #04 pc 0000000000010414  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (operator new(unsigned long)+24)
          ...
          #10 pc 000000000000ea6c  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (native_get_string(_JNIEnv*)+68)
          #11 pc 000000000000edf8  /data/app/android11.test.gwpasan/lib/arm64/libmy-test.so (Java_android11_test_gwpasan_MainActivity_nativeGetString+44)
          ...

## More information

To learn more about the implementation details of GWP-ASan, see the
[LLVM documentation](http://llvm.org/docs/GwpAsan.html). To learn
more about Android native crash reports, see
[Diagnosing Native Crashes](https://source.android.com/devices/tech/debug/native-crash).