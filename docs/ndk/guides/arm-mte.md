---
title: https://developer.android.com/ndk/guides/arm-mte
url: https://developer.android.com/ndk/guides/arm-mte
source: md.txt
---

| **Note:** This document covers running Android applications under MTE. For information about using MTE for Android platform development, see the [AOSP
| documentation](https://source.android.com/docs/security/test/memory-safety/arm-mte).
| **Important:** MTE is one of many tools available for memory debugging and mitigation. See [Memory error debugging and mitigation](https://developer.android.com/ndk/guides/memory-debug) for an overview of all the tools.

## Why MTE?

Memory safety bugs, which are errors in handling memory in native programming
languages,
are common code issues. They lead to security vulnerabilities as well as
stability problems.

Armv9 introduced the Arm Memory Tagging Extension (MTE), a hardware
extension that allows you to catch use-after-free and buffer-overflow bugs in
your native code.

## Check for support

Starting from Android 13, select devices have support for MTE.
To check whether your device is running with MTE enabled, run the following
command:

    adb shell grep mte /proc/cpuinfo

If the result is `Features : [...] mte`, your device is running with MTE
enabled.

Some devices don't enable MTE by default, but allow developers to reboot with
MTE enabled. This is an experimental configuration that is not recommended for
normal use as it might decrease device performance or stability, but can be
useful for app development. To access this mode, navigate to
[Developer Options](https://developer.android.com/studio/debug/dev-options) \> Memory Tagging Extension in your Settings App. If this
option is not present, your device does not support enabling MTE this way.

## Devices with MTE support

The following devices are known to support MTE:

- Pixel 8 (Shiba)
- Pixel 8 Pro (Husky)
- Pixel 8a (Akita)
- Pixel 9 (Tokay)
- Pixel 9 Pro (Caiman)
- Pixel 9 Pro XL (Komodo)
- Pixel 9 Pro Fold (Comet)
- Pixel 9a (Tegu)

## MTE operating modes

MTE supports two modes: SYNC and ASYNC. SYNC mode provides better diagnostic
information and thus is more suited for development purposes, while ASYNC mode
has high performance that allows it to be enabled for released apps.

### Synchronous mode (SYNC)

This mode is optimized for debuggability over performance and can
be used as a precise bug detection tool, when higher performance overhead is
acceptable. When enabled, MTE SYNC also acts as a security mitigation.

On a tag mismatch, the processor terminates the process on the offending load or
store instruction with SIGSEGV (with si_code SEGV_MTESERR) and full information
about the memory access and the faulting address.

This mode is useful during testing as an faster alternative to [HWASan](https://developer.android.com/ndk/guides/hwasan) that
does not require you to recompile your code, or in production, when the your app
represents a vulnerable attack surface.
In addition, when ASYNC mode (described below) has found a
bug, an accurate bug report can be obtained by using the runtime APIs to switch
execution to SYNC mode.

Moreover, when running in SYNC mode, the Android allocator records the
stack trace of every allocation and deallocation and uses them to provide better
error reports that include explanation of a memory error, such as
use-after-free or buffer-overflow, and the stack traces of the relevant memory
events (see [Understanding MTE reports](https://source.android.com/docs/security/test/memory-safety/mte-reports) for more details). Such
reports provide more contextual information and make bugs easier to trace and
fix than in ASYNC mode.

### Asynchronous mode (ASYNC)

This mode is optimized for performance over accuracy of bug reports and can be
used for low-overhead detection of memory safety bugs. On a tag mismatch, the
processor continues execution until the nearest kernel entry (such as a syscall
or timer interrupt), where it terminates the process with SIGSEGV (code
SEGV_MTEAERR) without recording the faulting address or memory access.

This mode is useful for mitigating memory-safety vulnerabilities in
production on well tested codebases where the density of memory safety bugs is
known to be low, which is achieved by using the SYNC mode during testing.

## Enable MTE

### For a single device

For experimentation, app compatibility changes can be used to set the default
value of `memtagMode` attribute for an application that does not specify
any value in the manifest (or specifies `"default"`).

These can be found under System \> Advanced \> Developer options \> App
Compatibility Changes in the global setting menu. Setting `NATIVE_MEMTAG_ASYNC`
or `NATIVE_MEMTAG_SYNC` enables MTE for a particular application.

Alternatively, this can be set using the `am` command as follows:

- For SYNC mode: `$ adb shell am compat enable NATIVE_MEMTAG_SYNC my.app.name`
- For ASYNC mode: `$ adb shell am compat enable NATIVE_MEMTAG_ASYNC my.app.name`

### In Gradle

You can enable MTE for all debug builds of your Gradle project by putting

    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools">

        <application android:memtagMode="sync" tools:replace="android:memtagMode"/>
    </manifest>

into `app/src/debug/AndroidManifest.xml`. This will override your manifest's
`memtagMode` with sync for debug builds.

Alternatively, you can enable MTE for all builds of a custom buildType. To do
so, [create your own buildType](https://developer.android.com/build/build-variants#build-types) and put the
XML into `app/src/<name of buildType>/AndroidManifest.xml`.

### For an APK on any capable device

MTE is disabled by default. Apps that want to use MTE can
do so by setting `android:memtagMode` under the `<application>` or `<process>`
tag in the `AndroidManifest.xml`.
| **Warning:** Applications that enable MTE should be thoroughly tested on an MTE-compatible device before being shipped to the Play Store. Failure to do so may lead to critical bugs being discovered only on MTE-capable devices, which may harm usability of the app.

    android:memtagMode=(off|default|sync|async)

When set on the `<application>` tag, the attribute affects all processes used
by the application, and can be overridden for individual processes by setting
the `<process>` tag.

## Build with instrumentation

| **Important:** Apps built with MTE instrumentation are **for debugging purposes only**.
| **Note:** MTE Stack Tagging is available starting in Android 14 QPR3.

Enabling MTE as explained earlier helps detect memory corruption bugs on the
native heap. To detect memory corruption on the stack, in addition to enabling
MTE for the app, the code needs to be rebuilt with instrumentation. The
resulting app **will only run on MTE-capable devices**.
| **Important:** Make sure you are using an up-to-date NDK to build your code.

To build your app's native (JNI) code with MTE, do the following:

### ndk-build

In your `Application.mk` file:

    APP_CFLAGS := -fsanitize=memtag -fno-omit-frame-pointer -march=armv8-a+memtag
    APP_LDFLAGS := -fsanitize=memtag -fsanitize-memtag-mode=sync -march=armv8-a+memtag

### CMake

For each target in your CMakeLists.txt:

    target_compile_options(${TARGET} PUBLIC -fsanitize=memtag -fno-omit-frame-pointer -march=armv8-a+memtag)
    target_link_options(${TARGET} PUBLIC -fsanitize=memtag -fsanitize-memtag-mode=sync -march=armv8-a+memtag)

## Run your app

Having enabled MTE, use and test your app as normal. If a memory safety issue
is detected, your app crashes with a tombstone that looks similar to this (note
the `SIGSEGV` with `SEGV_MTESERR` for SYNC or `SEGV_MTEAERR` for ASYNC):

    pid: 13935, tid: 13935, name: sanitizer-statu  >>> sanitizer-status <<<
    uid: 0
    tagged_addr_ctrl: 000000000007fff3
    signal 11 (SIGSEGV), code 9 (SEGV_MTESERR), fault addr 0x800007ae92853a0
    Cause: [MTE]: Use After Free, 0 bytes into a 32-byte allocation at 0x7ae92853a0
    x0  0000007cd94227cc  x1  0000007cd94227cc  x2  ffffffffffffffd0  x3  0000007fe81919c0
    x4  0000007fe8191a10  x5  0000000000000004  x6  0000005400000051  x7  0000008700000021
    x8  0800007ae92853a0  x9  0000000000000000  x10 0000007ae9285000  x11 0000000000000030
    x12 000000000000000d  x13 0000007cd941c858  x14 0000000000000054  x15 0000000000000000
    x16 0000007cd940c0c8  x17 0000007cd93a1030  x18 0000007cdcac6000  x19 0000007fe8191c78
    x20 0000005800eee5c4  x21 0000007fe8191c90  x22 0000000000000002  x23 0000000000000000
    x24 0000000000000000  x25 0000000000000000  x26 0000000000000000  x27 0000000000000000
    x28 0000000000000000  x29 0000007fe8191b70
    lr  0000005800eee0bc  sp  0000007fe8191b60  pc  0000005800eee0c0  pst 0000000060001000

    backtrace:
          #00 pc 00000000000010c0  /system/bin/sanitizer-status (test_crash_malloc_uaf()+40) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
          #01 pc 00000000000014a4  /system/bin/sanitizer-status (test(void (*)())+132) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
          #02 pc 00000000000019cc  /system/bin/sanitizer-status (main+1032) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
          #03 pc 00000000000487d8  /apex/com.android.runtime/lib64/bionic/libc.so (__libc_init+96) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)

    deallocated by thread 13935:
          #00 pc 000000000004643c  /apex/com.android.runtime/lib64/bionic/libc.so (scudo::Allocator<scudo::AndroidConfig, &(scudo_malloc_postinit)>::quarantineOrDeallocateChunk(scudo::Options, void*, scudo::Chunk::UnpackedHeader*, unsigned long)+688) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)
          #01 pc 00000000000421e4  /apex/com.android.runtime/lib64/bionic/libc.so (scudo::Allocator<scudo::AndroidConfig, &(scudo_malloc_postinit)>::deallocate(void*, scudo::Chunk::Origin, unsigned long, unsigned long)+212) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)
          #02 pc 00000000000010b8  /system/bin/sanitizer-status (test_crash_malloc_uaf()+32) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
          #03 pc 00000000000014a4  /system/bin/sanitizer-status (test(void (*)())+132) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)

    allocated by thread 13935:
          #00 pc 0000000000042020  /apex/com.android.runtime/lib64/bionic/libc.so (scudo::Allocator<scudo::AndroidConfig, &(scudo_malloc_postinit)>::allocate(unsigned long, scudo::Chunk::Origin, unsigned long, bool)+1300) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)
          #01 pc 0000000000042394  /apex/com.android.runtime/lib64/bionic/libc.so (scudo_malloc+36) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)
          #02 pc 000000000003cc9c  /apex/com.android.runtime/lib64/bionic/libc.so (malloc+36) (BuildId: 6ab39e35a2fae7efbe9a04e9bbb14331)
          #03 pc 00000000000010ac  /system/bin/sanitizer-status (test_crash_malloc_uaf()+20) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
          #04 pc 00000000000014a4  /system/bin/sanitizer-status (test(void (*)())+132) (BuildId: 953fc93301472d0b72709b2b9a9f6f30)
    Learn more about MTE reports: https://source.android.com/docs/security/test/memory-safety/mte-report

See [Understanding MTE reports](https://source.android.com/docs/security/test/memory-safety/mte-reports) in the AOSP documentation for more details. You
can also [debug your app with Android Studio](https://developer.android.com/studio/debug) and the debugger stops at the
line causing the invalid memory access.

## Advanced Users: Using MTE in your own allocator

| **Note:** if you are not aware that you are using custom allocators, you can skip this section.

To use MTE for memory not allocated through the normal system allocators, you
need to modify your allocator to tag memory and pointers.

The pages for your allocator need to be allocated using `PROT_MTE` in the
`prot` flag of `mmap` (or `mprotect`).

All tagged allocations need to be 16-byte aligned, as tags can only be assigned
for 16-byte chunks (also known as granules).

Then, before returning a pointer, you need to use the [`IRG`](https://developer.arm.com/documentation/ddi0596/2020-12/Base-Instructions/IRG--Insert-Random-Tag-) instruction to
generate a random tag and store it in the pointer.

Use the following instructions to tag the underlying memory:

- [`STG`](https://developer.arm.com/documentation/ddi0602/2021-12/Base-Instructions/STG--Store-Allocation-Tag-): tag a single 16-byte granule
- [`ST2G`](https://developer.arm.com/documentation/ddi0602/2022-06/Base-Instructions/ST2G--Store-Allocation-Tags-): tag two 16-byte granules
- [`DC GVA`](https://developer.arm.com/documentation/ddi0601/2020-12/AArch64-Instructions/DC-GVA--Data-Cache-set-Allocation-Tag-by-VA): tag cacheline with the same tag

Alternatively, the following instructions also zero-initialize the memory:

- [`STZG`](https://developer.arm.com/documentation/ddi0596/2020-12/Base-Instructions/STZG--Store-Allocation-Tag--Zeroing-): tag and zero-initialize a single 16-byte granule
- [`STZ2G`](https://developer.arm.com/documentation/ddi0596/2020-12/Base-Instructions/STZ2G--Store-Allocation-Tags--Zeroing-): tag and zero-initialize two 16-byte granules
- [`DC GZVA`](https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Instructions/DC-GZVA--Data-Cache-set-Allocation-Tags-and-Zero-by-VA): tag and zero-initialize cacheline with the same tag

Note that these instructions are *not supported* on older CPUs, so you need to
conditionally run them when MTE is enabled. You can check whether MTE is
enabled for your process:

    #include <sys/prctl.h>

    bool runningWithMte() {
          int mode = prctl(PR_GET_TAGGED_ADDR_CTRL, 0, 0, 0, 0);
          return mode != -1 && mode & PR_MTE_TCF_MASK;
    }

You may find the [scudo implementation](https://cs.android.com/android/platform/superproject/+/main:external/scudo/standalone/memtag.h?q=symbol:setRandomTag) helpful as a reference.

## Learn more

You can learn more in the [MTE User Guide for Android OS](https://developer.arm.com/documentation/108035/latest/) written by Arm.