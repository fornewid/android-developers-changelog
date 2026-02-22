---
title: https://developer.android.com/games/agde/address-sanitizer
url: https://developer.android.com/games/agde/address-sanitizer
source: md.txt
---

This document shows you how to enable special debugging tools when using
AGDE. These tools can help with hard-to-diagnose memory
corruption and overwrite errors.

## HWAddress Sanitizer and Address Sanitizer

[HWAddress Sanitizer](https://developer.android.com/ndk/guides/hwasan) (HWASan) and [Address
Sanitizer](https://developer.android.com/ndk/guides/asan) (ASan) are memory corruption debugging tools that
help with debugging memory corruption and overwrite errors, such as the
following:

- Stack buffer overflows and underflows
- Heap buffer overflows and underflows
- Stack use outside of its scope
- Double free and wild free errors
- Stack use after return (HWASan only)

We recommend enabling HWASan or ASan only when you're debugging an issue or as
part of automated testing. While these tools are performant, their use does
incur a penalty.

### Runtime behavior

When enabled, both HWASan and ASan automatically check for memory corruption in
your app.

If a memory error is detected, the app crashes with a `SIGBART` (signal abort)
error and prints a detailed message to logcat. A copy of the message is
also written to a file under `/data/tombstones`.

The error message looks similar to the following:

    ERROR: HWAddressSanitizer: tag-mismatch on address 0x0042a0826510 at pc 0x007b24d90a0c
    WRITE of size 1 at 0x0042a0826510 tags: 32/3d (ptr/mem) in thread T0
        #0 0x7b24d90a08  (/data/app/com.example.hellohwasan-eRpO2UhYylZaW0P_E0z7vA==/lib/arm64/libnative-lib.so+0x2a08)
        #1 0x7b8f1e4ccc  (/apex/com.android.art/lib64/libart.so+0x198ccc)
        #2 0x7b8f1db364  (/apex/com.android.art/lib64/libart.so+0x18f364)
        #3 0x7b8f2ad8d4  (/apex/com.android.art/lib64/libart.so+0x2618d4)

    0x0042a0826510 is located 0 bytes to the right of 16-byte region [0x0042a0826500,0x0042a0826510)
    allocated here:
        #0 0x7b92a322bc  (/apex/com.android.runtime/lib64/bionic/libclang_rt.hwasan-aarch64-android.so+0x212bc)
        #1 0x7b24d909e0  (/data/app/com.example.hellohwasan-eRpO2UhYylZaW0P_E0z7vA==/lib/arm64/libnative-lib.so+0x29e0)
        #2 0x7b8f1e4ccc  (/apex/com.android.art/lib64/libart.so+0x198ccc)

## Prerequisites

| **Note:** Use HWASan rather than ASan, as HWASan is faster and has lower memory overhead. However, HWASan has some additional requirements.

### HWASan requirements

To use HWASan:

- You must use AGDE 24.1.99 or higher.
- The app must be built using NDK 26 or higher.
- The app must be built with target SDK 34 or higher.
- The target must be an `arm64-v8a` device running Android 14 (API level 34) or higher.

### Use the shared C++ Standard Library in your project

Due to a known issue, ASan is incompatible with C++ exception handling when
using `libc++_static`. This issue is not seen when using `libc++_shared`.

HWASan has its own implementation of operators `new` and `delete`, which can't
be used if the standard library is statically linked into the project.
| **Caution:** You must use the shared version of the Standard Library in your project when using these features.

To change this setting, see the [Linking the C++ Standard Library](https://developer.android.com/games/agde/address-sanitizer#linking-c++)
section of this document.
| **Note:** If you've enabled ASan and haven't enabled the shared C++ library, you'll encounter a build error.

### Enable Frame Pointer generation

HWASan and ASan use a fast frame pointer-based unwinder to generate stack trace
information for memory allocation and deallocation events. This means that you
must enable frame pointer generation in your C++ compiler settings to use these
features. That is, you need to disable frame pointer omission optimization.

To change this setting, see the [Enabling Frame Pointer
generation](https://developer.android.com/games/agde/address-sanitizer#enabling-frame) section of this document.
| **Note:** If you've enabled ASan and haven't enabled Frame Pointer generation, you'll encounter a build error.

## Configuring your Visual Studio project to use HWASan or ASan

### Enabling HWASan or ASan

To enable HWASan or ASan, go to **Configuration Properties \> General** in the
**Property Pages** for your project.

![The Visual Studio Solution Explorer properties menu for the current
project.](https://developer.android.com/games/agde/images/solution-explorer-project-properties-menu.png)

**Figure 1** : The project's **Properties** option in the Visual Studio Solution
Explorer window.

![The project Property Pages dialog with General properties shown, and Address
Sanitizer settings highlighted.](https://developer.android.com/games/agde/images/project-properties-asan-setting.png)

**Figure 2** : The **Address Sanitizer (ASan)** setting in the general project
properties.

To enable HWASan for your project, change the **Address Sanitizer (ASan)**
setting to
**Hardware ASan Enabled (fsanitize=hwaddress)**.

To enable ASan for your project, change the **Address Sanitizer (ASan)** setting
to **ASan Enabled (fsanitize=address)**.
| **Caution:** To avoid unnecessary overhead, remember to set the property value back to **Disabled** when you no longer need to use these tools.

### Enabling Frame Pointer generation

Frame Pointer generation is controlled by the **Omit Frame Pointer** C/C++
compiler setting and can be found in your project **Property Pages** under
**Configuration Properties \> C/C++ \> Optimization**.

![The project Property Pages dialog with C/C++ Optimization properties shown,
and Omit Frame Pointer settings
highlighted.](https://developer.android.com/games/agde/images/project-properties-cpp-frame-pointer-setting.png)

**Figure 3** : Where to find the **Omit Frame Pointer** setting.

When using HWASan or ASan, set the **Omit Frame Pointer** setting to
**No (-fno-omit-frame-pointer)**.
| **Caution:** Be sure to reset this property value back to your original setting when not using HWASan or ASan.

### Linking the C++ Standard Library in shared library mode

The linker mode setting for the C++ Standard Library can be found in your
project's **Property Pages** under **Configuration Properties \> General** , in
the **Project Defaults** section.

![The project Property Pages dialog with the General category selected, and the
Use of STL setting
highlighted.](https://developer.android.com/games/agde/images/project-properties-cpp-stl-setting.png)

**Figure 4**: Where to find linker mode setting for the C++ Standard Library.

While using HWASan or ASan, set
**Use of STL** to **Use C++ Standard Libraries (.so)** . This value links the C++
standard library into your project as a *shared library*, which is required for
HWASan and ASan to function correctly.
| **Caution:** Don't use **GNU STL** libraries here, as they are unsupported by versions 25 or higher of the NDK. For more information, see the NDK documentation on [C++ Support](https://developer.android.com/ndk/guides/cpp-support).
| **Note:** Remember to restore these settings back to their original values once you're done using HWASan or ASan.

### Creating a Build Configuration for Address Sanitizer use

If you prefer to use HWASan or ASan *transiently*, you might not want to create
a new build configuration solely for their use. This might be the case if your
project is small, you're exploring the feature, or in response to a problem you
discover during testing.

However, if you find it useful and plan to use it regularly, you might consider
creating a new build configuration for HWASan or ASan as demonstrated in the
[Teapot sample](https://developer.android.com/games/agde/samples#teapot). You might do this if, for example,
you regularly run Address Sanitizer as part of your unit tests, or during
overnight smoke-tests of your game.

Creating a separate build configuration might be especially useful if you have a
large project which consumes a large number of different third party libraries
where you normally statically link them with the C++ standard library. Dedicated
build configurations can help to ensure that your project settings remain
accurate at all times.

To create a build configuration, from your project's **Property Pages** , click
the
**Configuration Manager...** button, and then open the
**Active solution configuration** drop-down. Then selection , and
create a new build configuration with an appropriate name (for example, *HWASan
enabled*).

### Using HWASan with custom memory allocators

HWASan automatically intercepts memory allocated via `malloc` (or `new`)
so that it can inject tags into pointers and check for tag mismatches.

However, when using a custom memory allocator, HWASan is not able to
automatically intercept your custom memory allocation methods. Therefore, if you
want to use HWASan with your custom memory allocator,
instrument your memory allocator to call HWASan explicitly. This can be
done with only a few lines of code.
| **Note:** See the [PoolAllocator sample](https://developer.android.com/games/agde/samples#poolallocator) that shows how to integrate HWASan into a custom memory allocator.

#### Prerequisites

The HWASan methods you need to call are defined in this header:

    #include "sanitizer/hwasan_interface.h"

#### Instrument your memory allocation method

1. Allocate objects at 16-byte block granularity and alignment.
   For instance, if you have a pool allocator that serves fixed-size objects of
   24-byte size, round your allocations up to 32-bytes, and
   align to 16 bytes.

2. Generate an 8-bit tag. Your tag must not use values 0-16, as those
   values are reserved for internal use.

3. Enable HWASan to start tracking the memory region with that tag:

       __hwasan_tag_memory((void*) address, tag, size);

4. Inject the tag to the top 8-bits of your pointer:

       address = __hwasan_tag_pointer((void*) address, tag);

#### Instrument your memory deallocation method

1. Reset the tag for the memory region to cause further accesses via the
   existing tagged pointers to fail:

       __hwasan_tag_memory(__hwasan_tag_pointer(ptr, 0), 0, size);

#### Working with a preallocated pool of objects

If your memory allocator preallocates objects in a pool and returns objects
back into the pool instead of actually freeing them, then your deallocation
method can directly overwrite the tag for the memory and the pointer with a new
value:

    ```
    __hwasan_tag_memory(__hwasan_tag_pointer(ptr, 0), tag, size);
    ptr = __hwasan_tag_pointer((void*)ptr, tag);
    ```

If you use this technique, your allocation methods do not need to tag pointers
or memory blocks, but tag the pointers and memory blocks when you preallocate the objects
in your pool. See [PoolAllocator sample](https://developer.android.com/games/agde/samples#poolallocator) for
an example that uses this style.