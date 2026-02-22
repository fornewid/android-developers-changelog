---
title: https://developer.android.com/ndk/downloads/revision_history
url: https://developer.android.com/ndk/downloads/revision_history
source: md.txt
---

# NDK Revision History

This page provides information on changes in all released stable versions of the NDK. To download the latest stable version of the NDK or any currently available beta version, see the[NDK downloads](https://developer.android.com/ndk/downloads)page.

See the[android-ndk-announce](https://groups.google.com/g/android-ndk-announce)Google Group for more complete information, and subscribe to receive release announcements.
Android NDK r29*(October 2025)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r29)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki).
Android NDK r28*(February 2025)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r28)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki).
Android NDK r27 LTS*(July 2024)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r27)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki).
Android NDK r26 LTS*(September 2023)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r26)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki).

Announcements
:
    - KitKat (APIs 19 and 20) is no longer supported.
Android NDK r25 LTS*(July 2022)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r25)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki).

Announcements
:
    - Includes Android 13 APIs.
    - Updated LLVM to clang-r450784d, based on LLVM 14 development.
Android NDK r24*(March 2022)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r24)

Downloads
:
    - Downloads for this release are available[here](https://github.com/android/ndk/wiki/Unsupported-Downloads).

Announcements
:
    - The GNU Assembler (GAS), has been removed. If you were building with`-fno-integrated-as`you'll need to remove that flag. See[Clang Migration Notes](https://android.googlesource.com/platform/ndk/+/refs/heads/master/docs/ClangMigration.md)for advice on making assembly compatible with LLVM.
    - GDB has been removed. Use LLDB instead. Note that ndk-gdb uses LLDB by default, and Android Studio has only ever supported LLDB.
    - Jelly Bean (APIs 16, 17, and 18) is no longer supported. The minimum OS supported by the NDK is KitKat (API level 19).
    - Non-Neon devices are no longer supported. A very small number of very old devices do not support Neon so most apps will not notice aside from the performance improvement.
    - RenderScript build support has been removed. RenderScript was[deprecated](https://developer.android.com/about/versions/12/deprecations#renderscript)in Android 12. If you have not finished migrating your apps away from RenderScript, NDK r23 LTS can be used.
Android NDK r23 LTS*(August 2021)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r23)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads).

Announcements
:
    - GNU binutils, excluding the GNU Assembler (GAS), has been removed. GAS will be removed in the next release. If you are building with`-fno-integrated-as`, file bugs if anything is preventing you from removing that flag.
    - Support for GDB has ended. GDB will be removed from the next release. Use LLDB instead. Note that`ndk-gdb`uses LLDB by default.
    - NDK r23 is the last release that will support non-Neon. Beginning with NDK r24, the armeabi-v7a libraries in the sysroot will be built with Neon. A very small number of very old devices do not support Neon so most apps will not notice aside from the performance improvement.
    - Jelly Bean (APIs 16, 17, and 18) will not be supported in the next NDK release. The minimum OS supported by the NDK for r24 will be KitKat (API level 19).
Android NDK r22b*(March 2021)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r22)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads).

Announcements
:
    - GNU binutils is deprecated and will be removed in an upcoming NDK release. Note that the GNU assembler (`as`)**is** a part of this. If you are building with`-fno-integrated-as`, file bugs if anything is preventing you from removing that flag. If you're using`as`directly, use`clang`instead.
    - [LLD](https://lld.llvm.org/)is now the default linker. ndk-build and our CMake toolchain file have also migrated to using llvm-ar and llvm-strip.
    - ndk-gdb now uses lldb as the debugger. gdb is deprecated and will be removed in a future release. To fall back to gdb, use --no-lldb option. But please[file a bug](https://github.com/android/ndk/issues/new/choose)explaining why you couldn't use lldb.
    - `std::filesystem`support is now included. There are two known issues:
      - [Issue 1258](https://github.com/android/ndk/issues/1258):`std::filesystem::perm_options::nofollow`may not be honored on old devices.
      - [Issue 1260](https://github.com/android/ndk/issues/1260):`std::filesystem::canonical`will incorrectly succeed when passed a non-existent path on old devices.
Android NDK r21e LTS*(January 2021)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r21)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads).

Announcements
:
    - 32-bit Windows is no longer supported. This does not affect the vast majority of users. If you do still need to build NDK apps from 32-bit versions of Windows, continue using NDK r20.

      For more information on this change within Android Developer tools, see the[blog post](https://android-developers.googleblog.com/2019/06/moving-android-studio-and-android.html)on the topic.
    - [LLD](https://lld.llvm.org/)is now available for testing. AOSP has switched to using LLD by default and the NDK will follow (timeline unknown). Test LLD in your app by passing`-fuse-ld=lld`when linking. Note that[Issue 843](https://github.com/android-ndk/ndk/issues/843)will affect builds using LLD with binutils strip and objcopy as opposed to llvm-strip and llvm-objcopy.
    - The legacy toolchain install paths will be removed over the coming releases. These paths have been obsolete since NDK r19 and take up a considerable amount of space in the NDK. The paths being removed are:
      - platforms
      - sources/cxx-stl
      - sysroot
      - toolchains (with the exception of toolchains/llvm)

      In general this change should only affect build system maintainers, or those using build systems that are not up to date. ndk-build and the CMake toolchain users are unaffected, and neither are`make_standalone_toolchain.py`users (though that script has been unnecessary since r19). For information on migrating away from the legacy toolchain layout, see the[Build System Maintainers Guide](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md)for the NDK version you're using.
    - The Play Store will require 64-bit support when uploading an APK beginning in August 2019. Start porting now to avoid surprises when the time comes. For more information, see[this blog post](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
    - A macOS app bundle that is signed and notarized is now available for download from our wiki and our website. Note that because only bundles may use RPATHs and pass notarization, the traditional NDK package for macOS**cannot** be notarized. The SDK will continue to use the traditional package as the app bundle requires layout changes that would make it incompatible with Android Studio. The NDK is not quarantined when it is downloaded via the SDK manager, so is currently allowed by Gatekeeper.**The SDK manager is currently the most reliable way to get the NDK for macOS.**
Android NDK r20b*(June 2019)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r20)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads/older_releases#ndk-20b-downloads).

Announcements
:
    - [LLD](https://lld.llvm.org/)is now available for testing. AOSP is in the process of switching to using LLD by default and the NDK will follow (timeline unknown). Test LLD in your app by passing`-fuse-ld=lld`when linking.
    - The Play Store will require 64-bit support when uploading an APK beginning in August 2019. Start porting now to avoid surprises when the time comes. For more information, see[this blog post](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
    - Added Android Q APIs.
Android NDK r19c*(January 2019)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r19)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads/older_releases#ndk-19c-downloads).

Announcements
:
    - Developers should begin testing their apps with[LLD](https://lld.llvm.org/). AOSP has switched to using LLD by default and the NDK will use it by default in the next release. BFD and Gold will be removed once LLD has been through a release cycle with no major unresolved issues (estimated r21). Test LLD in your app by passing`-fuse-ld=lld`when linking. Note: lld does not currently support compressed symbols on Windows.[Issue 888](https://github.com/android-ndk/ndk/issues/888). Clang also cannot generate compressed symbols on Windows, but this can be a problem when using artifacts built from Darwin or Linux.
    - The Play Store will require 64-bit support when uploading an APK beginning in August 2019. Start porting now to avoid surprises when the time comes. For more information, see[this blog post](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
    - [Issue 780](https://github.com/android-ndk/ndk/issues/780):[Standalone toolchains](https://developer.android.com/ndk/guides/standalone_toolchain)are now unnecessary. Clang, binutils, the sysroot, and other toolchain pieces are now all installed to`$NDK/toolchains/llvm/prebuilt/<host-tag>`and Clang will automatically find them. Instead of creating a standalone toolchain for API 26 ARM, instead invoke the compiler directly from the NDK:  

      ```
      $ $NDK/toolchains/llvm/prebuilt//bin/armv7a-linux-androideabi26-clang++ src.cpp
                 
      ```
      For r19 the toolchain is also installed to the old path to give build systems a chance to adapt to the new layout. The old paths will be removed in r20. The`make_standalone_toolchain.py`script will not be removed. It is now unnecessary and will emit a warning with the above information, but the script will remain to preserve existing workflows. If you're using ndk-build, CMake, or a standalone toolchain, there should be no change to your workflow. This change is meaningful for maintainers of third-party build systems, who should now be able to delete some Android-specific code. For more information, see the[Build System Maintainers](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md)guide.
    - ndk-depends has been removed. We believe that[ReLinker](https://github.com/KeepSafe/ReLinker)is a better solution to native library loading issues on old Android versions.
    - [Issue 862](https://github.com/android-ndk/ndk/issues/862): The GCC wrapper scripts which redirected to Clang have been removed, as they are not functional enough to be drop in replacements.
Android NDK r18b*(September 2018)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r18)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads/older_releases#ndk-17c-downloads).

Announcements
:
    - GCC has been removed.
    - [LLD](https://lld.llvm.org/)is now available for testing. AOSP is in the process of switching to using LLD by default and the NDK will follow (timeline unknown). Test LLD in your app by passing`-fuse-ld=lld`when linking.
    - gnustl, gabi++, and stlport have been removed.
    - Support for ICS (android-14 and android-15) has been removed. Apps using executables no longer need to provide both a PIE and non-PIE executable.
    - The Play Store will require 64-bit support when uploading an APK beginning in August 2019. Start porting now to avoid surprises when the time comes. For more information, see[this blog post](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
Android NDK r17c*(June 2018)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r17)

Downloads
:
    - Downloads for this release are available[here](https://developer.android.com/ndk/downloads/older_releases#ndk-17c-downloads).

Announcements
:
    - GCC is no longer supported. It will be removed in NDK r18.
    - libc++ is now the default STL for CMake and standalone toolchains. If you manually selected a different STL, we strongly encourage you to move to`libc++`. Note that ndk-build still defaults to no STL. For more details, see[this blog post](https://android-developers.googleblog.com/2017/09/introducing-android-native-development.html).
    - gnustl and stlport are deprecated and will be removed in NDK r18.
    - Support for ARMv5 (armeabi), MIPS, and MIPS64 has been removed. Attempting to build any of these ABIs will result in an error.
    - Support for ICS (android-14 and android-15) will be removed from r18.
    - The Play Store will require 64-bit support when uploading an APK beginning in August 2019. Start porting now to avoid surprises when the time comes. For more information, see[this blog post](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
Android NDK r16b*(December 2017)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r16)

Downloads
Announcements
:
    - The deprecated headers have been removed.[Unified Headers](https://android.googlesource.com/platform/ndk/+/ndk-release-r16/docs/UnifiedHeaders.md)are now simply "The Headers". For migration tips, see[Unified Headers Migration Notes](https://android.googlesource.com/platform/ndk/+/ndk-release-r16/docs/UnifiedHeadersMigration.md).
    - GCC is no longer supported. It will not be removed from the NDK just yet, but is no longer receiving backports. It cannot be removed until after libc++ has become stable enough to be the default, as some parts of gnustl are still incompatible with Clang. It will be removed when the other STLs are removed in r18.
    - `libc++`is out of beta and is now the preferred STL in the NDK. Starting in r17,`libc++`is the default STL for CMake and standalone toolchains. If you manually selected a different STL, we strongly encourage you to move to`libc++`. For more details, see this[blog post](https://android-developers.googleblog.com/2017/09/introducing-android-native-development.html).
    - Support for ARM5 (armeabi), MIPS, and MIPS64 are deprecated. They will no longer build by default with ndk-build, but are still buildable if they are explicitly named, and will be included by "all", "all32", and "all64". Support for each of these has been removed in r17. Both CMake and ndk-build will issue a warning if you target any of these ABIs.

APIs

:   Added native APIs for[Android 8.1](https://developer.android.com/about/versions/oreo/android-8.1). To learn more about these APIs, see the[Native APIs overview](https://developer.android.com/ndk/guides/stable_apis#a27).

    - [Neural Networks API](https://developer.android.com/ndk/reference/neural_networks_8h)
    - [JNI Shared Memory API](https://developer.android.com/ndk/reference/sharedmem__jni_8h)
Android NDK r15c*(July 2017)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r15)

Downloads
Announcements
:
    - Unified headers are enabled by default. To learn how to use these headers, see[Unified Headers](https://android.googlesource.com/platform/ndk/+/ndk-r15-release/docs/UnifiedHeaders.md).
    - **Note:** The deprecated headers will be removed in an upcoming release. If you encounter any issues with these headers, please file a[bug](https://github.com/android-ndk/ndk/issues).
    - For migration tips, see the[unified headers migration notes](https://android.googlesource.com/platform/ndk/+/ndk-r15-release/docs/UnifiedHeadersMigration.md).
    - GCC is no longer supported. It is not removed from NDK yet, but is no longer receiving backports. It cannot be removed until after libc++ stabilizes enough to be the default, as some parts of gnustl are still incompatible with Clang.
    - Android 2.3 (`android-9`) is no longer supported. The minimum API level target in the NDK is now Android 4.0 (`android-14`). If your`APP_PLATFORM`is set lower than`android-14`,`android-14`is used instead.
    - CMake in NDK now supports building assembly code written in YASM to run on x86 and x86-64 architectures. To learn more, see[Building assembly code](https://developer.android.com/ndk/guides/cmake#yasm-cmake).

APIs

:   Added native APIs for[Android 8.0](https://developer.android.com/about/versions/oreo). To learn more about these APIs, see the[Native APIs overview](https://developer.android.com/ndk/guides/stable_apis#a26).

    - [AAudio API](https://developer.android.com/ndk/reference/a_audio_8h)
    - [Hardware Buffer API](https://developer.android.com/ndk/reference/hardware__buffer_8h)
    - [Shared Memory API](https://developer.android.com/ndk/reference/sharedmem_8h)
Android NDK r14b*(March 2017)*
[Changelog](https://github.com/android/ndk/wiki/Changelog-r14)

Downloads
Announcements
:
    - **Unified headers:** This release introduces platform headers that are synchronized and kept always up-to-date and accurate with the Android platform. Header-only bug fixes now affect all API levels. The introduction of unified headers fixes inconsistencies in earlier NDK releases, such as:
      - Headers in M and N were actually headers for L.
      - Function declarations in headers did not match their platform levels correctly; headers declared non-existent functions or failed to declare available functions.
      - Several of the old API levels had missing or incorrect constants that were in newer API levels.

      These new unified headers are not enabled by default. To learn how to enable and use these headers, see[Unified Headers](https://android.googlesource.com/platform/ndk.git/+/ndk-r14-release/docs/UnifiedHeaders.md).
    - **GCC deprecation:**This release ends active support for GCC. GCC is not removed from the NDK just yet, but will no longer receive backports. As some parts of gnustl are still incompatible with Clang, GCC won't be entirely removed until after libc++ has become stable enough to be the default.
Android NDK r13b*(October 2016)*

Downloads
Announcements
:
    - GCC is no longer supported. It will not be removed from the NDK just yet, but is no longer receiving backports. It cannot be removed until after libc++ has become stable enough to be the default, as some parts of gnustl are still incompatible with Clang. It will likely be removed after that point.
    - Added[simpleperf](https://android.googlesource.com/platform/system/extras/+/master/simpleperf/README.md), a CPU profiler for Android.

r13b
:
    - [Additional fixes](https://android-review.googlesource.com/q/topic:cxa_bad_cast-ndk-r13-release)for missing`__cxa_bad_cast`.

NDK
:
    - `NDK_TOOLCHAIN_VERSION`now defaults to Clang.
    - libc++ has been updated to r263688.
    - We've reset to a (nearly) clean upstream. This should remove a number of bugs, but we still need to clean up libandroid_support before we will recommend it as the default.
    - `make-standalone-toolchain.sh`is now simply a wrapper around the Python version of the tool. There are a few behavioral differences. See[the commit message](https://android-review.googlesource.com/#/c/245453/)for details.
    - Some libraries for unsupported ABIs have been removed (mips64r2, mips32r6, mips32r2, and x32). There might still be some stragglers.
    - Issues with crtbegin_static.o that resulted in missing atexit at link time when building a static executable for ARM android-21+ have been resolved:[Issue 132](https://github.com/android-ndk/ndk/issues/132)
    - Added CMake toolchain file in build/cmake/android.toolchain.cmake.

Known Issues
:
    - This is not intended to be a comprehensive list of all outstanding bugs.
    - Standlone toolchains using libc++ and GCC do not work. This seems to be a bug in GCC. See[the commit message](https://android-review.googlesource.com/#/c/247498)for more details.
    - Bionic headers and libraries for Marshmallow and N are not yet exposed despite the presence of android-24. Those platforms are still the Lollipop headers and libraries (not a regression from r11).
    - RenderScript tools are not present (not a regression from r11):[Issue 7](https://github.com/android-ndk/ndk/issues/7).
Android NDK r12b*(June 2016)*

Downloads
Announcements
NDK
Clang
GCC
Binutils
GDB
Known Issues
Android NDK r12*(June 2016)*

Downloads
Announcements
NDK
Clang
GCC
Binutils
GDB
Known Issues
Android NDK r11c*(March 2016)*

Changes
Android NDK r11b*(March 2016)*

NDK
:
    - Important announcements
      - We've moved our bug tracker to[GitHub.](https://github.com/android-ndk/ndk/issues)
    - Changes
      - `ndk-gdb.py`is fixed. It had[regressed entirely](https://github.com/android-ndk/ndk/issues/3)in r11.
      - `ndk-gdb`for Mac[is fixed](https://github.com/android-ndk/ndk/issues/2).
      - Added more top-level shortcuts for command line tools:
        - `ndk-depends`.
        - `ndk-gdb`.
        - `ndk-stack`.
        - `ndk-which`. This command had been entirely absent from previous releases.
      - Fixed standalone toolchains for libc++, which had been missing`__cxxabi_config.h`.
      - Fixed help documentation for`--toolchain`in`make-standalone-toolchain.sh`.

Clang
:
    - Errata
      - Contrary to what we reported in the r11 Release Notes,`__thread`does not work. This is because the version of Clang we ship is missing a bug fix for emulated TLS support.
Android NDK r11*(March 2016)*

Clang
:
    - Important announcements
      - We strongly recommend switching to Clang.
        - If you experience problems with Clang, file bugs[here](https://github.com/android-ndk/ndk/issues)for issues specific to Clang in the NDK. For more general Clang issues, file bugs by following the instructions on[this page](http://llvm.org/docs/HowToSubmitABug.html).
      - Clang has been updated to 3.8svn (r243773, build 2481030).
        - This version is a nearly pure upstream Clang.
        - The Windows 64-bit downloadable NDK package contains a 32-bit version of Clang.
    - Additions
      - Clang now provides support for emulated TLS.
        - The compiler now supports`__thread`by emulating ELF TLS with pthread thread-specific data.
        - C++11`thread_local`works in some cases, but not for data with non-trivial destructors, because those cases require support from libc. This limitation does not apply when running on Android 6.0 (API level 23) or newer.
        - Emulated TLS does not yet work with Aarch64 when TLS variables are accessed from a shared library.

GCC
:
    - Important announcements
      - GCC in the NDK is now deprecated in favor of Clang.
        - The NDK will neither be upgrading to 5.x, nor accept non-critical backports.
        - Maintenance for miscompiles and internal compiler errors in 4.9 will be handled on a case by case basis.
    - Removals
      - Removed GCC 4.8. All targets now use GCC 4.9.
    - Other changes
      - Synchronized google/gcc-4_9 to r224707. Previously, it had been synchronized with r214835.

NDK
:
    - Important announcements
      - The samples are no longer included in the NDK package. They are instead available on[GitHub.](https://github.com/android/ndk-samples)
      - The documentation is no longer included in the NDK package. Instead, it is on the[Android developer website.](https://developer.android.com/ndk)
    - Additions
      - Added a native tracing API to`android-23`.
      - Added a native multinetwork API to`android-23`.
      - Enabled libc, m, and dl to provide versioned symbols, starting from API level 21.
      - Added Vulkan headers and library to API level N.
    - Removals
      - Removed support for`_WCHAR_IS_8BIT`.
      - Removed sed.
      - Removed mclinker.
      - Removed Perl.
      - Removed from all versions of NDK libc, m, and dl all symbols which the platform versions of those libs do not support.
      - Partially removed support for mips64r2. The rest will be removed in the future.
    - Other changes
      - Changed ARM standalone toolchains to default to arm7.
        - You can restore the old behavior by passing specifying the`-target`option as`armv5te-linux-androideabi`.
      - Changed the build system to use`-isystem`for platform includes.
        - Warnings that bionic causes no longer break app builds.
      - Fixed a segfault that occurred when a binary threw exceptions via gabi++. (Issue[179410](http://b.android.com/179410))
      - Changed libc++'s inline namespace to`std::__ndk1`to prevent ODR issues with platform libc++.
      - All libc++ libraries are now built with libc++abi.
      - Bumped default`APP_PLATFORM`to Gingerbread.
        - Expect support for Froyo and older to be dropped in a future release.
    - Updated gabi++`_Unwind_Exception`struct for 64 bits.
    - Added the following capabilities to cpufeatures:
      - Detect SSE4.1 and SSE4.2.
      - Detect cpu features on x86_64.
    - Updated libc++abi to upstream[r231075](http://lists.llvm.org/pipermail/cfe-commits/Week-of-Mon-20150302/124603.html).
    - Updated`byteswap.h`,`endian.h`,`sys/procfs.h`,`sys/ucontext.h`,`sys/user.h`, and`uchar.h`from ToT Bionic.
    - Synchronized`sys/cdefs.h`across all API levels.
    - Fixed`fegetenv and fesetenv`for arm.
    - Fix end pointer size/alignment of`crtend_*`for mips64 and x86_64.
Android NDK r10e*(May 2015)*

Downloads
Important changes:
:
    - Integrated the workaround for Cortex-A53 Erratum 843419 into the`aarch64-linux-android-4.9`linker. For more information on this workaround, see[Workaround for cortex-a53 erratum 843419.](https://sourceware.org/ml/binutils/2015-03/msg00446.html)
    - Added Clang 3.6;`NDK_TOOLCHAIN_VERSION=clang`now picks that version of Clang by default.
    - Removed Clang 3.4.
    - Removed GCC 4.6.
    - Implemented multithreading support in`ld.gold`for all architectures. It can now link with or without support for multithreading; the default is to do it without.
      - To compile with multithreading, use the`--threads`option.
      - To compile without multithreading, use the`--no-threads`option.
    - Upgraded GDB/gdbserver to 7.7 for all architectures.
    - Removed the NDK package for 32-bit Darwin.
Android NDK r10d*(December 2014)*

Important changes:
:
    - Made GCC 4.8 the default for all 32-bit ABIs. Deprecated GCC 4.6, and will remove it next release. To restore previous behavior, either add`NDK_TOOLCHAIN_VERSION=4.6`to ndk-build, or add`--toolchain=arm-linux-androideabi-4.6`when executing`make-standalone-toolchain.sh`on the command line. GCC 4.9 remains the default for 64-bit ABIs.
    - Stopped all x86\[_64\] toolchains from adding`-mstackrealign`by default. The NDK toolchain assumes a 16-byte stack alignment. The tools and options used by default enforce this rule. A user writing assembly code must make sure to preserve stack alignment, and ensure that other compilers also comply with this rule. (GCC bug[38496](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=38496))
    - Added Address Sanitizer functionality to Clang 3.5 support to the ARM and x86 ABIs. For more information on this change, see the[Address Sanitizer](https://code.google.com/p/address-sanitizer/wiki/Android)project.
    - Introduced the requirement, starting from API level 21, to use`-fPIE -pie
      `when building. In API levels 16 and higher, ndk-build uses`PIE`when building. This change has a number of implications, which are discussed in[Developer Preview Issue 888](https://code.google.com/p/android-developer-preview/issues/detail?id=888). These implications do not apply to shared libraries.
Android NDK r10c*(October 2014)*

Important changes:
:
    - Made the following changes to download structure:
      - Each package now contains both the 32- and the 64-bit headers, libraries, and tools for its respective platform.
      - STL libraries with debugging info no longer need be downloaded separately.
    - Changed everything previously called`Android-L`to the official release designation:`android-21`.
    - Updated GCC 4.9 by rebasing to the`google`branch of the GCC repository. Major differences from the upstream version of GCC 4.9 include:
      - The`-O2`option now turns on vectorization, without loop peeling but with more aggressive unrolling.
      - Enhancements to FDO and[LIPO](https://gcc.gnu.org/wiki/LightweightIpo#LIPO_-_Profile_Feedback_Based_Lightweight_IPO)
      - For more detailed information, see*Important bug fixes*below.
    - Added Clang 3.5 support to all hosts:`NDK_TOOLCHAIN_VERSION=clang`now picks Clang 3.5. Note that:
      - ARM and x86 default to using the integrated assembler. If this causes issues, use`-fno-integrated-as`as a workaround.
      - Clang 3.5 issues more warnings for unused flags, such as the`-finline-functions`option that GCC supports.
      - When migrating from projects using GCC, you can use`-Wno-invalid-command-line-argument`and`-Wno-unused-command-line-argument`to ignore the unused flags until you're able decide on what to do with them longer-term.
    - Made it possible to enter ART debugging mode, when debugging on an Android 5.0 device using ART as its virtual machine, by specifying the`art-on`option. For more information, see`prebuilt/common/gdb/common.setup`in the directory containing the NDK.
    - Removed support for Clang 3.3.
    - Deprecated GCC 4.6, and may remove it from future releases.
    - Updated mclinker to 2.8 with Identical Code Folding ("ICF") support. Specify ICF using the`--icf`option.
    - Broadened`arm_neon.h`support in x86 and x86_64, attaining coverage of \~93% of NEON intrinsics. For more information about NEON support:
      - Navigate to the NDK Programmer's Guide (`docs/Programmers_Guide/html/`), and see Architectures and CPUs \> Neon.
      - Examine the updated`hello-neon`sample in`samples/`.
      - See Intel's guide to[porting from ARM NEON to Intel SSE.](https://software.intel.com/en-us/blogs/2012/12/12/from-arm-neon-to-intel-mmxsse-automatic-porting-solution-tips-and-tricks)
    - Documented support for`_FORTIFY_SOURCE`in`headers/libs/android-21`, which appeared in r10 (when`android-21`was still called`Android-L`), but had no documentation.
Android NDK r10b*(September 2014)*

Important notes:
:
    - Because of the 512MB size restriction on downloadable packages, the following 32-bit items are not in the 32-bit NDK download packages. Instead, they reside in the 64-bit ones:
      - Android-L headers
      - GCC 4.9
    - Currently, the only Renderscript support provided by the NDK is for 32-bit Renderscript with Android 4.4 (API level 19). You cannot build HelloComputeNDK (the only Renderscript sample) with any other combination of Renderscript (32- or 64-bit) and Android version.
    - To compile native-codec, you must use a 64-bit NDK package, which is where all the Android-L headers are located.

Important bug fixes:
:
    - Fixed gdb 7.6 in GCC 4.8/4.9. (Issues[74112](http://b.android.com/74112)and[74371](http://b.android.com/74371).)
    - Fixed GCC 4.8/4.9 for x86, so that they no longer enable`-msse4.2`and`-mpopcnt`by default. (Issue[73843](http://b.android.com/73843).)

Other bug fixes:
:
    - Removed`stdio.h`from the`include-fixed/`directories of all versions of GCC. (Issue[73728](http://b.android.com/73728).)
    - Removed duplicate header files from the Windows packages in the`platforms/android-L/arch-*/usr/include/linux/netfilter*/`directories. (Issue[73704](https://code.google.com/p/android/issues/detail?id=73704).)
    - Fixed a problem that prevented Clang from building HelloComputeNDK.
    - Fixed atexit. (Issue[66595](http://b.android.com/66595).)
    - Made various fixes to the docs in`docs/`and`sources/third_party/googletest/README.NDK`. (Issue[74069](http://b.android.com/74069).)
    - Made the following fixes to the Android-L headers:
      1. Added the following functions to`ctype.h`and`wchar.h`:`dn_expand()`,`grantpt()`,` inet_nsap_addr()`,`inet_nsap_ntoa()`,`insque()`,`nsdispatch()`,`posix_openpt()`,`__pthread_cleanup_pop()`,`__pthread_cleanup_push()`,`remque()`,`setfsgid()`,`setfsuid()`,`splice()`,`tee()`,`twalk()`(Issue[73719](http://b.android.com/73719)), and 42`*_l()`functions.
      2. Renamed`cmsg_nxthdr`to`__cmsg_nxthdr`.
      3. Removed`__libc_malloc_dispatch`.
      4. Changed the`ptrace()`prototype to`long ptrace(int, ...);`.
      5. Removed`sha1.h`.
      6. Extended`android_dlextinfo`in`android/dlext.h`.
      7. Annotated`__NDK_FPABI__`for functions receiving or returning float- or double-type values in`stdlib.h`,`time.h`,`wchar.h`, and`complex.h`.

Other changes:
:
    - Updated`mipsel-linux-android-4.9`and`mips64el-linux-android-4.9`, implementing a new multilib directory layout, and providing support for gdb-7.7
    - Enhanced`cpu-features`to detect more arm64 features. (Change list[100339](https://android-review.googlesource.com/#/c/100339).)
Android NDK r10*(July 2014)*

Important changes:
:
    - Added 3 new ABIs, all 64-bit: arm64-v8a, x86_64, mips64.
    Note that:
      - GCC 4.9 is the default compiler for 64-bit ABIs. Clang is currently version 3.4.`NDK_TOOLCHAIN_VERSION=clang`may not work for arm64-v8a and mips64.
      - Android-L is the first level with 64-bit support. Note that this API level is a temporary one, and only for L-preview. An actual API level number will replace it at L-release.
      - This release includes now includes`all32`and`all64`settings for`APP_ABI`.
        - `APP_ABI=all32`is equivalent to`APP_ABI=armeabi,armeabi-v7a,x86,mips`.
        - `APP_ABI=all64`is equivalent to`APP_ABI=arm64-v8a,x86_64,mips64`.
        - `APP_ABI=all`selects all ABIs.
      - The new GNU libstdc++ in Android-L contains all`<tr1/cmath>`Before defining your own math function, check`_GLIBCXX_USE_C99_MATH_TR1`to see a function with that name already exists, in order to avoid "multiple definition" errors from the linker.
      - The cpu-features library has been updated for the ARMv8 kernel. The existing cpu-features library may fail to detect the presence of NEON on the ARMv8 platform. Recompile your code with the new version.
    - Added a new`platforms/android-L/`API directory. It includes:
      - Updated Bionic headers, which had not changed from Android API levels 3 (Cupcake) to 19 (KitKat). This new version, for level L, is to be synchronized with AOSP.
      - New media APIs and a native-codec sample.
      - An updated`Android.h`header for SLES/OpenSLES, enabling support for single-precision, floating-point audio format in AudioPlayer.
      - GLES 3.1 and AEP extensions to`libGLESv3.so.`
      - GLES2 and GLES3 headers updated to the latest official Khronos versions.
    - Added GCC 4.9 compilers to the 32-/64-bit ABIs. GCC 4.9 is the default (only) compiler for 64-bit ABIs, as previously mentioned. For 32-bit ABIs, you must explicitly enable GCC 4.9, as GCC 4.6 is still the default.
      - For ndk-build, enable 32-bit, GCC 4.9 building either by adding`NDK_TOOLCHAIN_VERSION=4.9`to`Application.mk`, or exporting it as an environment variable from the command line.
      - For a standalone toolchain, use the`--toolchain=`option in the`make-standalone-toolchain.sh`script. For example:`--toolchain=arm-linux-androideabi-4.9.`
    - Upgraded GDB to version 7.6 in GCC 4.8/4.9 and x86\*. Since GDB is still at version GDB-7.3.x in GCC 4.6 (the default for ARM and MIPS), you must set`NDK_TOOLCHAIN_VERSION=4.8`or`4.9`to enable ndk-gdb to select GDB 7.6.
    - Added the`-mssse3`build option to provide SSSE3 support, and made it the default for ABI x86 (upgrading from SSE3). The image released by Google does not contain SSSE3 instructions.
    - Updated GCC 4.8 to 4.8.3.
    - Improved ARM libc++ EH support by switching from gabi++ to libc++abi. For details, see the "C++ Support" section of the documentation. Note that:
      - All tests except for locale now pass for Clang 3.4 and GCC 4.8. For more information, see the "C++ Support" section of the documentation.
      - The libc++ libraries for X86 and MIPS libc++ still use gabi++.
      - GCC 4.7 and later can now use \<atomic\>.
      - You must add`-fno-strict-aliasing`if you use` <list>`, because`__list_imp::_end`_ breaks TBAA rules. (Issue[61571](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61571).)
      - As of GCC 4.6, LIBCXX_FORCE_REBUILD:=true no longer rebuilds libc++. Rebuilding it requires the use of a different compiler. Note that Clang 3.3 is untested.
    - mclinker is now version 2.7, and has aarch64 Linux support.
    - Added precompiled header support for headers specified by`LOCAL_PCH`. (Issue[25412](http://b.android.com/25412)).
Android NDK r9d*(March 2014)*

Important changes:
:
    - Added support for the Clang 3.4 compiler. The`NDK_TOOLCHAIN_VERSION=clang`option now picks Clang 3.4. GCC 4.6 is still the default compiler.
    - Added`APP_ABI=armeabi-v7a-hard`, with additional multilib option`-mfloat-abi=hard`. These options are for use with ARM GCC 4.6/4.8 and Clang 3.3/3.4 (which use 4.8's assembler, linker, and libs). When using these options, note the following changes:
      - When executing the`ndk-build`script, add the following options for armeabi-v7a target:  

        ```
        TARGET_CFLAGS += -mhard-float -D_NDK_MATH_NO_SOFTFP=1
        TARGET_LDFLAGS += -Wl,--no-warn-mismatch -lm_hard
        ```
        The built library is copied to`libs/armeabi-v7a`. For make to behave as expected, you cannot specify both`armeabi-v7a`and`armeabi-v7a-hard`as make targets (i.e., on the APP_ABI= line). Doing so causes one of them to be ignored. Note that`APP_ABI=all`is still equivalent to`armeabi armeabi-v7a x86 mips`.
      - The`make-standalone-toolchain.sh`script copies additional libraries under`/hard`directories. Add the above`CFLAGS`and`LFLAGS`to your makefile to enable GCC or Clang to link with libraries in`/hard`.
    - Added the yasm assembler, as well as`LOCAL_ASMFLAGS`and`EXPORT_ASMFLAGS`flags for x86 targets. The`ndk-build`script uses`prebuilts/*/bin/yasm*`to build`LOCAL_SRC_FILES`that have the`.asm`extension.
    - Updated MClinker to 2.6.0, which adds`-gc-sections`support.
    - Added experimental libc++ support (upstream r201101). Use this new feature by following these steps:
      - Add`APP_STL := c++_static`or`APP_STL :=
        c++_shared`in`Application.mk`. You may rebuild from source via`LIBCXX_FORCE_REBUILD :=
        true`
      - Execute`make-standalone-toolchain.sh --stl=libc++`to create a standalone toolchain with libc++ headers/lib.

      For more information, see`CPLUSPLUS-SUPPORT.html`. (Issue[36496](http://b.android.com/36496))
Android NDK r9c*(December 2013)*

This is a bug-fix-only release.

Important bug fixes:
:
    - Fixed a problem with GCC 4.8 ARM, in which the stack pointer is restored too early. This problem prevented the frame pointer from reliably accessing a variable in the stack frame. (GCC Issue[58854](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=58854))
    - Fixed a problem with GCC 4.8 libstdc++, in which a bug in std::nth_element was causing generation of code that produced a random segfault. (Issue[62910](https://code.google.com/p/android/issues/detail?id=62910))
    - Fixed GCC 4.8 ICE in cc1/cc1plus with`-fuse-ld=mcld`, so that the following error no longer occurs:  

      ```
      cc1: internal compiler error: in common_handle_option, at
      opts.c:1774
      ```
    - Fixed`-mhard-float`support for`__builtin`math functions. For ongoing information on fixes for`-mhard-float`with STL, please follow Issue[61784](http://b.android.com/61784).

Other bug fixes:
:
    - Header fixes:
      - Changed prototype of`poll`to`poll(struct
        pollfd *, nfds_t, int);`in`poll.h`.
      - Added`utimensat`to`libc.so`for Android API levels 12 and 19. These libraries are now included for all Android API levels 12 through 19.
      - Introduced`futimens`into`libc.so`, for Android API level 19.
      - Added missing`clock_settime()`and`clock_nanosleep()`to`time.h`for Android API level 8 and higher.
      - Added`CLOCK_MONOTONIC_RAW, CLOCK_REALTIME_COARSE,
        CLOCK_MONOTONIC_COARSE, CLOCK_BOOTTIME, CLOCK_REALTIME_ALARM,`and`CLOCK_BOOTTIME_ALARM`in`time.h.`
      - Removed obsolete`CLOCK_REALTIME_HR`and`CLOCK_MONOTONIC_HR.`
    - In samples Teapot, MoreTeapots, and`source/android/ndk_helper`:
      - Changed them so that they now use a hard-float abi for armeabi-v7a.
      - Updated them to use immersive mode on Android API level 19 and higher.
      - Fixed a problem with`Check_ReleaseStringUTFChars`in`/system/lib/libdvm.so`that was causing crashes on x86 devices.
    - Fixed`ndk-build`fails that happen in cygwin when the NDK package is referenced via symlink.
    - Fixed`ndk-build.cmd`fails that happen in windows`cmd.exe`when`LOCAL_SRC_FILES`contains absolute paths. (Issue[69992](https://android-review.googlesource.com/#/c/69992))
    - Fixed the`ndk-stack`script to proceed even when it can't parse a frame due to inability to find a routine, filename, or line number. In any of these cases, it prints`??`.
    - Fixed the`ndk-stack`stack for windows-x64_64 targets so that it no longer erroneously matches a frame line with a line in the`stack:`section that doesn't contain`pc`,`eip`, or`ip`. For example:  

      ```
      I/DEBUG   ( 1151):     #00  5f09db68  401f01c4
      /system/lib/libc.so
      ```
    - Fixed gabi++ so that it:
      - Does not use malloc() to allocate C++ thread-local objects.
      - Avoids deadlocks in gabi++ in cases where libc.debug.malloc is non-zero in userdebug/eng Android platform builds.

Other changes:
:
    - Added`LOCAL_EXPORT_LDFLAGS`.
    - Introduced the`NDK_PROJECT_PATH=null`setting for use in an integrated build system where options are explicitly passed to`ndk-build`. With this setting,`ndk-build`makes no attempt to look for`NDK_PROJECT_PATH.`This setting also prevents variables from deriving default settings from NDK_PROJECT_PATH. As a result, the following variables must now be explicitly specified (with their default values if such exist):`NDK_OUT, NDK_LIBS_OUT, APP_BUILD_SCRIPT,
      NDK_DEBUG`(optional, default to 0), and other`APP_*`'s contained in`Application.mk`.
    - `APP_ABI`can now be enumerated in a comma-delimited list. For example:  

      ```
      APP_ABI := "armeabi,armeabi-v7a"
      ```
    - Provided the ability to rebuild all of STL with debugging info in an optional, separate package called`android-ndk-r9c-cxx-stl-libs-with-debugging-info.zip`, using the`-g`option. This option helps the`ndk-stack`script provide better a stack dump across STL. This change should not affect the code/size of the final, stripped file.
    - Enhanced`hello-jni`samples to report`APP_ABI`at compilation.
    - Used the`ar`tool in Deterministic mode (option`-D`) to build static libraries. (Issue[60705](http://b.android.com/60705))
Android NDK r9b*(October 2013)*

Important changes:
:
    - Updated`include/android/*h`and`math.h`for all Android API levels up to 18, including the addition of levels 13, 15, 16 and 17. For information on added APIs, see commit messages for Changes[68012](https://android-review.googlesource.com/68012)and[68014](https://android-review.googlesource.com/68014). (Issues[47150](http://b.android.com/47150),[58528](http://b.android.com/58528), and[38423](http://b.android.com/38423))
    - Added support for Android API level 19, including Renderscript binding.
    - Added support for`-mhard-float`in the existing armeabi-v7a ABI. For more information and current restrictions on Clang, see`tests/device/hard-float/jni/Android.mk`.
    - Migrated from GNU Compiler Collection (GCC) 4.8 to 4.8.2, and added diagnostic color support. To enable diagnostic colors, set`-fdiagnostics-color=auto`,`-fdiagnostics-color=always,`or export`GCC_COLORS`as shown below:  

      ```
      GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
      ```
      For more information, see[GCC Language Independent Options](http://gcc.gnu.org/onlinedocs/gcc/Language-Independent-Options.html).
    - Added two new samples to demonstrate OpenGL ES 3.0 features: Teapot and MoreTeapots. These samples run on devices with Android 4.1 (API level 16) and higher.
    - Deprecated GCC 4.7 and Clang 3.2 support, which will be removed in the next release.

Important bug fixes:
:
    - Fixed problem with ARM GCC 4.6`thumb2`failing to generate 16-bit relative jump tables. ([GCC Issue](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48328))
    - Fixed GCC 4.8 internal compiler error (ICE) on`g++.dg/cpp0x/lambda/lambda-defarg3.C`. ([Change 62770](https://android-review.googlesource.com/62770),[GCC Issue](http://gcc.gnu.org/ml/gcc/2013-07/msg00424.html))
    - Fixed a problem with Windows 32-bit`*-gdb.exe`executables failing to launch. ([Issue 58975](http://b.android.com/58975))
    - Fixed GCC 4.8 ICE when building bullet library. The error message is as follows:  

      ```
      internal compiler error: verify_flow_info failed
      ```
      ([Issue 58916](http://b.android.com/58916),[GCC Issue](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=58165))
    - Modified GDB/ARM build to skip`ARM.exidx`data for unwinding in prologue code and added a command (`set arm exidx-unwinding`) to control exidx-based stack unwinding. ([Issue 55826](http://b.android.com/55826))
    - Fixed Clang 3.3 MIPS compiler problem where HI and LO registers are incorrectly reused.
    - Fixed issue with MIPS 4.7 ICE in`dbx_reg_number`. The error message is as follows:  

      ```
      external/icu4c/i18n/decimfmt.cpp:1322:1:
      internal compiler error: in dbx_reg_number, at dwarf2out.c:10185
      ```
      ([GCC Patch](http://gcc.gnu.org/ml/gcc-patches/2012-12/msg00830.html))

Other bug fixes:
:
    - Header fixes
      - Fixed the ARM`WCHAR_MIN`and`WCHAR_MAX`to be unsigned according to spec (the X86/MIPS versions are signed). Define`_WCHAR_IS_ALWAYS_SIGNED`to restore old behavior. ([Issue 57749](http://b.android.com/57749))
      - Fixed`include/netinet/tcp.h`to contain`TCP_INFO`state enum. ([Issue 38881](http://b.android.com/38881))
      - Fixed the`cdefs_elh.h`macro`_C_LABEL_STRING`to stop generating warnings in the GCC 4.8 toolchain when using c++11 mode. ([Issue 58135](http://b.android.com/58135),[Issue 58652](http://b.android.com/58652))
      - Removed non-existent functions`imaxabs`and`imaxdiv`from header`inttypes.h`.
      - Fixed issue with`pthread_exit()`return values and`pthread_self()`. ([Issue 60686](http://b.android.com/60686))
      - Added missing`mkdtemp()`function, which already exists in`bionic`header`stdlib.h`.
    - Fixed problem building`samples/gles3jni`with Clang on Android API level 11.
    - Fixed MCLinker to allow multiple occurrences of the following options:`-gc-sections`and`--eh-frame-hdr`.
    - Fixed MCLinker to accept the`--no-warn-mismatch`option.
    - Modified`cpu-features`option to not assume all VFPv4 devices support IDIV. Now this option only adds IDIV to white-listed devices, including Nexus 4. ([Issue 57637](http://b.android.com/57637))
    - Fixed problem with`android_native_app_glue.c`erroneously logging errors on event predispatch operations.
    - Fixed all operations on`gabi++`terminate and unexpected_handler to be thread-safe.
    - Fixed several issues with Clang`-integrated-as`option so it can pass tests for`ssax-instructions`and`fenv`.
    - Fixed GCC 4.6/4.7/4.8 compiler to pass the linker option`--eh-frame-hdr`even for static executables. For more information, see the[GCC patch](http://gcc.gnu.org/ml/gcc-patches/2012-09/msg00969.html).
    - Fixed extra apostrophe in`CPU-ARCH-ABIS.html`. For more information, see`NDK-DEPENDS.html`. ([Issue 60142](http://b.android.com/60142))
    - Fixed extra quotes in ndk-build output on Windows. ([Issue 60649](http://b.android.com/60649))
    - Fixed Clang 3.3 to compile ARM's built-in, atomic operations such as`__atomic_fetch_add`,`__atomic_fetch_sub`, and`__atomic_fetch_or`.
    - Fixed Clang 3.3 ICE with customized`vfprintf`. ([Clang issue](http://llvm.org/bugs/show_bug.cgi?id=16344))

Other changes:
:
    - Enabled OpenMP for all GCC builds. To use this feature, add the following flags to your build settings:  

      ```
      LOCAL_CFLAGS += -fopenmp
      LOCAL_LDFLAGS += -fopenmp
      ```
      For code examples, see`tests/device/test-openmp`
    - Reduced the size of`ld.mcld`significantly (1.5MB vs.`ld.bfd`3.5MB and`ld.gold`7.5MB), resulting in a speed improvement of approximately 20%.
    - Added`LOCAL_CONLYFLAGS`and`APP_CONLYFLAGS`to specify options applicable to C only but not C++. The existing`LOCAL_CFLAGS`and`APP_CFLAGS`are also used for C++ compilation (to save trouble of specifying most options twice), so options such as`-std=gnu99`may fail in g++ builds with a warning and clang++ builds with an error.
    - Added`gabi++`array helper functions.
    - Modified GCC builds so that all`libgcc.a`files are built with`-funwind-tables`to allow the stack to be unwound past previously blocked points, such as`__aeabi_idiv0`.
    - Added Ingenic MXU support in MIPS GCC4.6/4.7/4.8 with new`-mmxu`option.
    - Extended MIPS GCC4.6/4.7/4.8`-mldc1-sdc1`to control ldxc1/sdxc1 too
    - Added crazy linker. For more information, see`sources/android/crazy_linker/README.TXT`.
    - Fixed`bitmap-plasma`to draw to full screen rather than a 200x200 pixel area.
    - Reduced linux and darwin toolchain sizes by 25% by creating symlinks to identical files.
Android NDK r9*(July 2013)*

Important changes:
:
    - Added support for Android 4.3 (API level 18). For more information, see`STABLE-APIS.html`and new code examples in`samples/gles3jni/README`.
    - Added headers and libraries for OpenGL ES 3.0, which is supported by Android 4.3 (API level 18) and higher.
    - Added GNU Compiler Collection (GCC) 4.8 compiler to the NDK. Since GCC 4.6 is still the default, you must explicitly enable this option:
      - For`ndk-build`builds, export`NDK_TOOLCHAIN_VERSION=4.8`or add it in`Application.mk`.
      - For standalone builds, use the`--toolchain=`option in`make-standalone-toolchain.sh`, for example:  
        `--toolchain=arm-linux-androideabi-4.8`

      **Note:** The`-Wunused-local-typedefs`option is enabled by`-Wall`. Be sure to add`__attribute__((unused))`if you use compile-time asserts like`sources/cxx-stl/stlport/stlport/stl/config/features.h`, line #311. For more information, see[Change 55460](https://android-review.googlesource.com/#/c/55460)

      **Note:** In the GCC 4.7 release and later, ARM compilers generate unaligned access code by default for ARMv6 and higher build targets. You may need to add the`-mno-unaligned-access`build option when building for kernels that do not support this feature.
    - Added Clang 3.3 support. The`NDK_TOOLCHAIN_VERSION=clang`build option now picks Clang 3.3 by default.

      **Note:**Both GCC 4.4.3 and Clang 3.1 are deprecated, and will be removed from the next NDK release.
    - Updated GNU Project Debugger (GDB) to support python 2.7.5.
    - Added MCLinker to support Windows hosts. Since`ld.gold`is the default where available, you must add`-fuse-ld=mcld`in`LOCAL_LDFLAGS`or`APP_LDFLAGS`to enable MCLinker.
    - Added`ndk-depends`tool which prints ELF library dependencies. For more information, see`NDK-DEPENDS.html`. ([Issue 53486](http://b.android.com/53486))

Important bug fixes:
:
    - Fixed potential event handling issue in`android_native_app_glue`. ([Issue 41755](http://b.android.com/41755))
    - Fixed ARM/GCC-4.7 build to generate sufficient alignment for NEON load and store instructions VST and VLD. ([GCC Issue 57271](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=57271))
    - Fixed a GCC 4.4.3/4.6/4.7 internal compiler error (ICE) for a constant negative index value on a string literal. ([Issue 54623](http://b.android.com/54623))
    - Fixed GCC 4.7 segmentation fault for constant initialization with an object address. ([Issue 56508](http://b.android.com/56508))
    - Fixed GCC 4.6 ARM segmentation fault for`-O`values when using Boost 1.52.0. ([Issue 42891](http://b.android.com/42891))
    - Fixed`libc.so`and`libc.a`to support the`wait4()`function. ([Issue 19854](http://b.android.com/19854))
    - Updated the x86 libc.so and libc.a files to include the`clone()`function.
    - Fixed`LOCAL_SHORT_COMMANDS`bug where the`linker.list`file is empty or not used.
    - Fixed GCC MIPS build on Mac OS to use CFI directives, without which`ld.mcld --eh-frame-hdr`fails frequently.
    - Fixed Clang 3.2 X86/MIPS internal compiler error in`llvm/lib/VMCore/Value.cpp`. ([Change 59021](https://android-review.googlesource.com/#/c/59021))
    - Fixed GCC 4.7 64-bit Windows assembler crash. (Error:`out of memory allocating
      4294967280 bytes`).
    - Updated`ndk-gdb`script so that the`--start`or`--launch`actions now wait for the GNU Debug Server, so that it can more reliably hit breakpoints set early in the execution path (such as breakpoints in JNI code). ([Issue 41278](http://b.android.com/41278))

      **Note:** This feature requires jdb and produces warning about pending breakpoints. Specify the`--nowait`option to restore previous behavior.
    - Fixed GDB crash when library list is empty.
    - Fixed GDB crash when using a`stepi`command past a`bx pc`or`blx pc`Thumb instruction. ([Issue 56962](http://b.android.com/56962),[Issue 36149](http://b.android.com/36149))
    - Fixed MIPS`gdbserver`to look for`DT_MIPS_RLD_MAP`instead of`DT_DEBUG`. ([Issue 56586](http://b.android.com/56586))
    - Fixed a circular dependency in the ndk-build script, for example: If A-\>B and B-\>B, then B was dropped from build. ([Issue 56690](http://b.android.com/56690))

Other bug fixes:
:
    - Fixed the`ndk-build`script to enable you to specify a version of Clang as a command line option (e.g.,`NDK_TOOLCHAIN_VERSION=clang3.2`). Previously, only specifying the version as an environment variable worked.
    - Fixed gabi++ size of`_Unwind_Exception`to be 24 for MIPS build targets when using the Clang compiler. ([Change 54141](https://android-review.googlesource.com/#/c/54141))
    - Fixed the`ndk-build`script to ensure that built libraries are actually removed from projects that include prebuilt static libraries when using the`ndk-build clean`command. ([Change 54461](https://android-review.googlesource.com/#/c/54461),[Change 54480](https://android-review.googlesource.com/#/c/54480))
    - Modified the`NDK_ANALYZE=1`option to be less verbose.
    - Fixed`gnu-libstdc++/Android.mk`to include a`backward/`path for builds that use backward compatibility. ([Issue 53404](http://b.android.com/53404))
    - Fixed a problem where`stlport new`sometimes returned random values.
    - Fixed`ndk-gdb`to match the order of`CPU_ABIS`, not`APP_ABIS`. ([Issue 54033](http://b.android.com/54033))
    - Fixed a problem where the NDK 64-bit build on MacOSX chooses the wrong path for compiler. ([Issue 53769](http://b.android.com/53769))
    - Fixed build scripts to detect 64-bit Windows Vista. ([Issue 54485](http://b.android.com/54485))
    - Fixed x86`ntonl/swap32`error:`invalid 'asm': operand number
      out of range`. ([Issue 54465](http://b.android.com/54465),[Change 57242](https://android-review.googlesource.com/#/c/57242))
    - Fixed`ld.gold`to merge string literals.
    - Fixed`ld.gold`to handle large symbol alignment.
    - Updated`ld.gold`to enable the`--sort-section=name`option.
    - Fixed GCC 4.4.3/4.6/4.7 to suppress the`-export-dynamic`option for statically linked programs. GCC no longer adds an`.interp`section for statically linked programs.
    - Fixed GCC 4.4.3`stlport`compilation error about inconsistent`typedef`of`_Unwind_Control_Block`. ([Issue 54426](http://b.android.com/54426))
    - Fixed`awk`scripts to handle`AndroidManifest.xml`files created on Windows which may contain trailing`\r`characters and cause build errors. ([Issue 42548](http://b.android.com/42548))
    - Fixed`make-standalone-toolchain.sh`to probe the`prebuilts/`directory to detect if the host is 32 bit or 64 bit.
    - Fixed the Clang 3.2`-integrated-as`option.
    - Fixed the Clang 3.2 ARM EHABI compact model`pr1`and`pr2`handler data.
    - Added Clang`-mllvm -arm-enable-ehabi`option to fix the following Clang error:  

      ```
      clang: for the -arm-enable-ehabi option: may only occur zero or one times!
      ```
    - Fixed build failure when there is no`uses-sdk`element in application manifest. ([Issue 57015](http://b.android.com/57015))

Other changes:
:
    - Header Fixes
      - Modified headers to make`__set_errno`an inlined function, since`__set_errno`in`errno.h`is deprecated, and`libc.so`no longer exports it.
      - Modified`elf.h`to include`stdint.h`. ([Issue 55443](http://b.android.com/55443))
      - Fixed`sys/un.h`to be included independently of other headers. ([Issue 53646](http://b.android.com/53646))
      - Fixed all of the`MotionEvent_getHistorical`API family to take the`const AInputEvent* motion_event`. ([Issue 55873](http://b.android.com/55873))
      - Fixed`malloc_usable_size`to take`const void*`. ([Issue 55725](http://b.android.com/55725))
      - Fixed stdint.h to be more compatible with C99. ([Change 46821](https://android-review.googlesource.com/#/c/46821))
      - Modified`wchar.h`to not redefine`WCHAR_MAX`and`WCHAR_MIN`
      - Fixed`<inttypes.h>`declaration for pointer-related`PRI`and`SCN`macros. ([Issue 57218](http://b.android.com/57218))
      - Changed the`sys/cdefs.h`header so that`__WCHAR_TYPE__`is 32-bit for API levels less than 9, which means that`wchat_t`is 32-bit for all API levels. To restore the previous behavior, define the`_WCHAR_IS_8BIT`boolean variable. ([Issue 57267](http://b.android.com/57267))
    - Added more formatting in NDK`docs/`and miscellaneous documentation fixes.
    - Added support for a thin archive technique when building static libraries. ([Issue 40303](http://b.android.com/40303))
    - Updated script`make-standalone-toolchain.sh`to support the`stlport`library in addition to`gnustl`, when you specify the option`--stl=stlport`. For more information, see`STANDALONE-TOOLCHAIN.html`.
    - Updated the`make-standalone-toolchain.sh`script so that the`--llvm-version=`option creates the`$TOOLCHAIN_PREFIX-clang`and`$TOOLCHAIN_PREFIX-clang++`scripts in addition to`clang`and`clang++`, to avoid using the host's clang and clang++ definitions by accident.
    - Added two flags to re-enable two optimizations in upstream Clang but disabled in NDK for better compatibility with code compiled by GCC:
      - Added a`-fcxx-missing-return-semantics`flag to re-enable*missing return semantics*in Clang 3.2+. Normally, all paths should terminate with a return statement for a value-returning function. If this is not the case, clang inserts an undefined instruction (or trap in debug mode) at the path without a return statement. If you are sure your code is correct, use this flag to allow the optimizer to take advantage of the undefined behavior. If you are not sure, do not use this flag. The caller may still receive a random incorrect value, but the optimizer will not exploit it and make your code harder to debug.
      - Added a`-fglobal-ctor-const-promotion`flag to re-enable promoting global variables with static constructor to be constants. With this flag, the global variable optimization pass of LLVM tries to evaluate the global variables with static constructors and promote them to global constants. Although this optimization is correct, it may cause some incompatibility with code compiled by GCC. For example, code may do`const_cast`to cast the constant to mutable and modify it. In GCC, the variable is in read-write and the code is run by accident. In Clang, the const variable is in read-only memory and may cause your application to crash.
    - Added`-mldc1-sdc1`to the MIPS GCC and Clang compilers. By default, compilers align 8-byte objects properly and emit the`ldc1`and`sdc1`instructions to move them around. If your app uses a custom allocator that does not always align with a new object's 8-byte boundary in the same way as the default allocator, your app may crash due to`ldc1`and`sdc1`operations on unaligned memory. In this case, use the`-mno-ldc1-sdc1`flag to workaround the problem.
    - Downgraded the event severity from warning to info if`APP_PLATFORM_LEVEL`is larger than`APP_MIN_PLATFORM_LEVEL`. The`APP_PLATFORM_LEVEL`may be lower than`APP_PLATFORM`in`jni/Application.mk`because the NDK does not have headers for all levels. In this case, the actual level is shifted downwards. The`APP_MIN_PLATFORM_LEVEL`is specified by the`android:minSdkVersion`in your application's manifest. ([Issue 39752](http://b.android.com/39752))
    - Added the`android_getCpuIdArm()`and`android_setCpuArm()`methods to`cpu-features.c`. This addition enables easier retrieval of the ARM CPUID information. ([Issue 53689](http://b.android.com/53689))
    - Modified`ndk-build`to use GCC 4.7's`as/ld`for Clang compiling.

      **Note:** In GCC 4.7,`monotonic_clock`and`is_monotonic`have been renamed to`steady_clock`and`is_steady`, respectively.
    - Added the following new warnings to the`ndk-build`script:
      - Added warnings if`LOCAL_LDLIBS/LDFLAGS`are used in static library modules.
      - Added a warning if a configuration has no module to build.
      - Added a warning for non-system libraries being used in`LOCAL_LDLIBS/LDFLAGS`of a shared library or executable modules.
    - Updated build scripts, so that if`APP_MODULES`is not defined and only static libraries are listed in`Android.mk`, the script force-builds all of them. ([Issue 53502](http://b.android.com/53502))
    - Updated`ndk-build`to support absolute paths in`LOCAL_SRC_FILES`.
    - Removed the`*-gdbtui`executables, which are duplicates of the`*-gdb`executables with the`-tui`option enabled.
    - Updated the build scripts to warn you when the Edison Design Group (EDG) compiler front-end turns`_STLP_HAS_INCLUDE_NEXT`back on. ([Issue 53646](http://b.android.com/53646))
    - Added the environment variable`NDK_LIBS_OUT`to allow overriding of the path for`libraries/gdbserver`from the default`$PROJECT/libs`. For more information, see`OVERVIEW.html`.
    - Changed ndk-build script defaults to compile code with format string protection`-Wformat -Werror=format-security`. You may set`LOCAL_DISABLE_FORMAT_STRING_CHECKS=true`to disable it. For more information, see`ANDROID-MK.html`
    - Added STL pretty-print support in`ndk-gdb-py`. For more information, see`NDK-GDB.html`.
    - Added tests based on the googletest frameworks.
    - Added a notification to the toolchain build script that warns you if the current shell is not`bash`.
Android NDK r8e*(March 2013)*

Important changes:
:
    - Added 64-bit host toolchain set (package name suffix`*-x86_64.*`). For more information, see`CHANGES.HTML`and`NDK-BUILD.html`.
    - Added Clang 3.2 compiler. GCC 4.6 is still the default. For information on using the Clang compiler, see`CHANGES.HTML`.
    - Added static code analyzer for Linux/MacOSX hosts. For information on using the analyzer, see`CHANGES.HTML`.
    - Added MCLinker for Linux/MacOSX hosts as an experimental feature. The`ld.gold`linker is the default where available, so you must explicitly enable it. For more information, see`CHANGES.HTML`.
    - Updated ndk-build to use topological sort for module dependencies, which means the build automatically sorts out the order of libraries specified in`LOCAL_STATIC_LIBRARIES`,`LOCAL_WHOLE_STATIC_LIBRARIES`and`LOCAL_SHARED_LIBRARIES`. For more information, see`CHANGES.HTML`. ([Issue 39378](http://b.android.com/39378))

Important bug fixes:
:
    - Fixed build script to build all toolchains in`-O2`. Toolchains in previous releases were incorrectly built without optimization.
    - Fixed build script which unconditionally builds Clang/llvm for MacOSX in 64-bit.
    - Fixed GCC 4.6/4.7 internal compiler error:`gen_thumb_movhi_clobber at config/arm/arm.md:5832`. ([Issue 52732](http://b.android.com/52732))
    - Fixed build problem where GCC/ARM 4.6/4.7 fails to link code using 64-bit atomic built-in functions. ([Issue 41297](http://b.android.com/41297))
    - Fixed GCC 4.7 linker DIV usage mismatch errors. ([Sourceware Issue](http://sourceware.org/ml/binutils/2012-12/msg00202.html))
    - Fixed GCC 4.7 internal compiler error`build_data_member_initialization, at
      cp/semantics.c:5790`.
    - Fixed GCC 4.7 internal compiler error`redirect_eh_edge_1, at tree-eh.c:2214`. ([Issue 52909](http://b.android.com/52909))
    - Fixed a GCC 4.7 segfault. ([GCC Issue](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=55245))
    - Fixed`<chrono>`clock resolution and enabled`steady_clock`. ([Issue 39680](http://b.android.com/39680))
    - Fixed toolchain to enable`_GLIBCXX_HAS_GTHREADS`for GCC 4.7 libstdc++. ([Issue 41770](http://b.android.com/41770),[Issue 41859](http://b.android.com/41859))
    - Fixed problem with the X86 MXX/SSE code failing to link due to missing`posix_memalign`. ([Change 51872](https://android-review.googlesource.com/#/c/51872))
    - Fixed GCC4.7/X86 segmentation fault in`i386.c`, function`distance_non_agu_define_in_bb()`. ([Change 50383](https://android-review.googlesource.com/#/c/50383))
    - Fixed GCC4.7/X86 to restore earlier`cmov`behavior. ([GCC Issue](http://gcc.gnu.org/viewcvs?view=revision&revision=193554))
    - Fixed handling NULL return value of`setlocale()`in libstdc++/GCC4.7. ([Issue 46718](http://b.android.com/46718))
    - Fixed`ld.gold`runtime undefined reference to`__exidx_start`and`__exidx_start_end`. ([Change 52134](https://android-review.googlesource.com/#/c/52134))
    - Fixed Clang 3.1 internal compiler error when using Eigen library. ([Issue 41246](http://b.android.com/41246))
    - Fixed Clang 3.1 internal compiler error including`<chrono>`in C++11 mode. ([Issue 39600](http://b.android.com/39600))
    - Fixed Clang 3.1 internal compiler error when generating object code for a method call to a uniform initialized`rvalue`. ([Issue 41387](http://b.android.com/41387))
    - Fixed Clang 3.1/X86 stack realignment. ([Change 52154](https://android-review.googlesource.com/#/c/52154))
    - Fixed problem with GNU Debugger (GDB) SIGILL when debugging on Android 4.1.2. ([Issue 40941](http://b.android.com/40941))
    - Fixed problem where GDB cannot set`source:line`breakpoints when symbols contain long, indirect file paths. ([Issue 42448](http://b.android.com/42448))
    - Fixed GDB`read_program_header`for MIPS PIE executables. ([Change 49592](https://android-review.googlesource.com/#/c/49592))
    - Fixed`STLport`segmentation fault in`uncaught_exception()`. ([Change 50236](https://android-review.googlesource.com/#/c/50236))
    - Fixed`STLport`bus error in exception handling due to unaligned access of`DW_EH_PE_udata2`,`DW_EH_PE_udata4`, and`DW_EH_PE_udata8`.
    - Fixed Gabi++ infinite recursion problem with`nothrow new[]`operator. ([Issue 52833](http://b.android.com/52833))
    - Fixed Gabi++ wrong offset to exception handler pointer. ([Change 53446](https://android-review.googlesource.com/#/c/53446))
    - Removed Gabi++ redundant free on exception object ([Change 53447](https://android-review.googlesource.com/#/c/53447))

Other bug fixes:
:
    - Fixed NDK headers:
      - Removed redundant definitions of`size_t`,`ssize_t`, and`ptrdiff_t`.
      - Fixed MIPS and ARM`fenv.h`header.
      - Fixed`stddef.h`to not redefine`offsetof`since it already exists in the toolchain.
      - Fixed`elf.h`to contain`Elf32_auxv_t`and`Elf64_auxv_t`. ([Issue 38441](http://b.android.com/38441))
      - Fixed the`#ifdef`C++ definitions in the`OpenSLES_AndroidConfiguration.h`header file. ([Issue 53163](http://b.android.com/53163))
    - Fixed`STLport`to abort after out of memory error instead of silently exiting.
    - Fixed system and Gabi++ headers to be able to compile with API level 8 and lower.
    - Fixed`cpufeatures`to not parse`/proc/self/auxv`. ([Issue 43055](http://b.android.com/43055))
    - Fixed`ld.gold`to not depend on host libstdc++ and on Windows platforms, to not depend on the`libgcc_sjlj_1.dll`library.
    - Fixed Clang 3.1 which emits inconsistent register list in`.vsave`and fails assembler. ([Change 49930](https://android-review.googlesource.com/#/c/49930))
    - Fixed Clang 3.1 to be able to compile libgabi++ and pass the`test-stlport`tests for MIPS build targets. ([Change 51961](https://android-review.googlesource.com/#/c/51961))
    - Fixed Clang 3.1 to only enable exception by default for C++, not for C.
    - Fixed several issues in Clang 3.1 to pass most GNU exception tests.
    - Fixed scripts`clang`and`clang++`in standalone NDK compiler to detect`-cc1`and to not specify`-target`when found.
    - Fixed`ndk-build`to observe`NDK_APP_OUT`set in`Application.mk`.
    - Fixed X86`libc.so`and`lib.a`which were missing the`sigsetjmp`and`siglongjmp`functions already declared in`setjmp.h`. ([Issue 19851](http://b.android.com/19851))
    - Patched GCC 4.4.3/4.6/4.7 libstdc++ to work with Clang in C++ 11. ([Clang Issue](http://clang.llvm.org/cxx_status.html))
    - Fixed cygwin path in argument passed to`HOST_AWK`.
    - Fixed`ndk-build`script warning in windows when running from project's JNI directory. ([Issue 40192](http://b.android.com/40192))
    - Fixed problem where the`ndk-build`script does not build if makefile has trailing whitespace in the`LOCAL_PATH`definition. ([Issue 42841](http://b.android.com/42841))

Other changes:
:
    - Enabled threading support in GCC/MIPS toolchain.
    - Updated GCC exception handling helpers`__cxa_begin_cleanup`and`__cxa_type_match`to have*default* visibility from the previous*hidden* visibility in GNU libstdc++. For more information, see`CHANGES.HTML`.
    - Updated build scripts so that Gabi++ and STLport static libraries are now built with hidden visibility except for exception handling helpers.
    - Updated build so that`STLport`is built for ARM in Thumb mode.
    - Added support for`std::set_new_handler`in Gabi++. ([Issue 52805](http://b.android.com/52805))
    - Enabled`FUTEX`system call in GNU libstdc++.
    - Updated`ndk-build`so that it no longer copies prebuilt static library to a project's`obj/local/<abi>/`directory. ([Issue 40302](http://b.android.com/40302))
    - Removed`__ARM_ARCH_5*__`from ARM`toolchains/*/setup.mk`script. ([Issue 21132](http://b.android.com/21132))
    - Built additional GNU libstdc++ libraries in thumb for ARM.
    - Enabled MIPS floating-point`madd/msub/nmadd/nmsub/recip/rsqrt`instructions with 32-bit FPU.
    - Enabled graphite loop optimizer in GCC 4.6 and 4.7 to allow more optimizations:`-fgraphite`,`-fgraphite-identity`,`-floop-block`,`-floop-flatten`,`-floop-interchange`,`-floop-strip-mine`,`-floop-parallelize-all`, and`-ftree-loop-linear`. ([info](http://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html))
    - Enabled`polly`for Clang 3.1 on Linux and Max OS X 32-bit hosts which analyzes and optimizes memory access. ([info](http://polly.llvm.org))
    - Enabled`-flto`in GCC 4.7, 4.6, Clang 3.2 and Clang 3.1 on linux (Clang LTO via LLVMgold.so). MIPS compiler targets are not supported because`ld.gold`is not available.
    - Enabled`--plugin`and`--plugin-opt`for`ld.gold`in GCC 4.6/4.7.
    - Enabled`--text-reorder`for`ld.gold`in GCC 4.7.
    - Configured GNU libstdc++ with`_GLIBCXX_USE_C99_MATH`which undefines the`isinf`script in the bionic header. For more information, see`CHANGES.html`.
    - Added`APP_LDFLAGS`to the build scripts. For more information, see`ANDROID-MK.html`.
    - Updated build scripts to allow`NDK_LOG=0`to disable the`NDK_LOG`.
    - Updated build scripts to allow`NDK_HOST_32BIT=0`to disable the host developer environment 32-bit toolchain.
    - Changed the default GCC/X86 flags`-march=`and`-mtune=`from`pentiumpro`and`generic`to`i686`and`atom`.
    - Enhanced toolchain build scripts:
      - Fixed a race condition in`build-gcc.sh`for the`mingw`build type which was preventing a significant amount of parallel build processing.
      - Updated`build-gabi++.sh`and`build-stlport.sh`so they can now run from the NDK package. ([Issue 52835](http://b.android.com/52835))
      - Fixed`run-tests.sh`in the`MSys`utilities collection.
      - Improved 64-bit host toolchain and Canadian Cross build support.
      - Updated`build-mingw64-toolchain.sh`script to more recent version.
      - Added option to build`libgnustl_static.a`and`stlport_static.a`without hidden visibility.
Android NDK r8d*(December 2012)*

Important changes:
:
    - Added the GNU Compiler Collection (GCC) 4.7 compiler to the NDK. The GCC 4.6 compiler is still the default, so you must to explicitly enable the new version as follows:
      - For`ndk-build`, export the`NDK_TOOLCHAIN_VERSION=4.7`variable*or* add it to`Application.mk`.
      - For standalone builds, add the`--toolchain=`option to`make-standalone-toolchain.sh`, for example:  

        ```
        --toolchain=arm-linux-androideabi-4.7
        ```

      **Note:** This feature is experimental. Please try it and[report any issues](http://code.google.com/p/android/issues/list).
    - Added`stlport`exception support via gabi++. Note that the new gabi++ depends on`dlopen`and related code, meaning that:
      - You can no longer build a*static* executable using the`-static`option or include`libstlport_static.a`using`APP_STL := stlport_static`. (You can still use the`-static`option with a standalone toolchain.) Compiling a*dynamic* executable using`include $(BUILD_EXECUTABLE)`continues to work because the compiler automatically adds the`-ldl`option.
      - If your project links using`-nostdlib`and {-Wl,--no-undefined}, you must manually include the`-ldl`option.

      For more information, see`CPLUSPLUS-SUPPORT.html`.

      **Note:** This feature is experimental and works better with the GCC 4.6/4.7 compilers than with GCC 4.4.3 or Clang 3.1. Please try it and[report any issues](http://code.google.com/p/android/issues/list).
    - Added a`-mstack-protector-guard=`option for x86 to choose between a*global* default path which is compatible with older Android C library (bionic) and a new*tls* path (%gs:20) for`-fstack-protector`,`-fstack-protector-all`and`-fstack-protector-strong`using the GCC 4.6 and higher compilers.

      **Note:** The`-mstack-protector-guard`setting itself does not enable any`-fstack-protector*`options.
    - Added`android_setCpu()`function to`sources/android/cpufeatures/cpu-features.c`for use when auto-detection via`/proc`is not possible in Android 4.1 and higher. ([Chromium Issue 164154](http://code.google.com/p/chromium/issues/detail?id=164154))

Important bug fixes:
:
    - Fixed unnecessary rebuild of object files when using the`ndk-build`script. ([Issue 39810](http://b.android.com/39810))
    - Fixed a linker failure with the NDK 8c release for Mac OS X 10.6.x that produced the following error:  

      ```
      dyld: lazy symbol binding failed: Symbol not found: _memmem
      Referenced from: ...../arm-linux-androideabi/bin/ld
      Expected in: /usr/lib/libSystem.B.dylib
      ```
      This problem was caused by building on Mac OS X 10.7, which produced binaries that were not compatible with Mac OS 10.6.x and the NDK.
    - Removed the`-x c++`options from the Clang++ standalone build script. ([Issue 39089](http://b.android.com/39089))
    - Fixed issues using the`NDK_TOOLCHAIN_VERSION=clang3.1`option in Cygwin. ([Issue 39585](http://b.android.com/39585))
    - Fixed the`make-standalone-toolchain.sh`script to allow generation of a standalone toolchain using the Cygwin or MinGW environments. The resulting toolchain can be used in Cygwin, MingGW or CMD.exe environments. ([Issue 39915](http://b.android.com/39915),[Issue 39585](http://b.android.com/39585))
    - Added missing`SL_IID_ANDROIDBUFFERQUEUESOURCE`option in android-14 builds for ARM and X86. ([Issue 40625](http://b.android.com/40625))
    - Fixed x86 CPU detection for the`ANDROID_CPU_X86_FEATURE_MOVBE`feature. ([Issue 39317](http://b.android.com/39317))
    - Fixed an issue preventing the Standard Template Library (STL) from using C++ sources that do not have a`.cpp`file extension.
    - Fixed GCC 4.6 ARM internal compiler error*at reload1.c:1061* . ([Issue 20862](http://b.android.com/20862))
    - Fixed GCC 4.4.3 ARM internal compiler error*at emit-rtl.c:1954* . ([Issue 22336](http://b.android.com/22336))
    - Fixed GCC 4.4.3 ARM internal compiler error*at postreload.c:396* . ([Issue 22345](http://b.android.com/22345))
    - Fixed problem with GCC 4.6/4.7 skipping lambda functions. ([Issue 35933](http://b.android.com/35933))

Other bug fixes:
:
    - NDK header file fixes:
      - Fixed`__WINT_TYPE__`and`wint_t`to be the same type.
      - Corrected typo in`android/bitmap.h`. ([Issue 15134](http://b.android.com/15134))
      - Corrected typo in`errno.h`.
      - Added check for the presence of`__STDC_VERSION__`in`sys/cdefs.h`. ([Issue 14627](http://b.android.com/14627))
      - Reorganized headers in`byteswap.h`and`dirent.h`.
      - Fixed`limits.h`to include`page.h`which provides`PAGE_SIZE`settings. ([Issue 39983](http://b.android.com/39983))
      - Fixed return type of`glGetAttribLocation()`and`glGetUniformLocation()`from`int`to`GLint`.
      - Fixed`__BYTE_ORDER`constant for x86 builds. ([Issue 39824](http://b.android.com/39824))
    - Fixed`ndk-build`script to not overwrite`-Os`with`-O2`for ARM builds.
    - Fixed build scripts to allow overwriting of`HOST_AWK`,`HOST_SED`, and`HOST_MAKE`settings.
    - Fixed issue for`ld.gold`on`fsck_msdos`builds linking objects built by the Intel C/C++ compiler (ICC).
    - Fixed ARM EHABI support in Clang to conform to specifications.
    - Fixed GNU Debugger (GDB) to shorten the time spent on walking the target's link map during`solib`events. ([Issue 38402](http://b.android.com/38402))
    - Fixed missing`libgcc.a`file when linking shared libraries.

Other changes:
:
    - Backported 64-bit built-in atomic functions for ARM to GCC 4.6.
    - Added documentation for audio output latency, along with other documentation and fixes.
    - Fixed debug builds with Clang so that non-void functions now raise a`SIGILL`signal for paths without a return statement.
    - Updated`make-standalone-toolchain.sh`to accept the suffix`-clang3.1`which is equivalent to adding`--llvm-version=3.1`to the GCC 4.6 toolchain.
    - Updated GCC and Clang bug report URL to:[https://source.android.com/source/report-bug s.html](https://source.android.com/source/report-bugs.html)
    - Added ARM ELF support to`llvm-objdump`.
    - Suppressed*treating c input as c++*warning for Clang builds.
    - Updated build so that only the 32-bit version of`libiberty.a`is built and placed in`lib32/`.
Android NDK r8c*(November 2012)*

Important changes:
:
    - Added the Clang 3.1 compiler to the NDK. The GNU Compiler Collection (GCC) 4.6 is still the default, so you must explicitly enable the Clang compiler option as follows:
      - For`ndk-build`, export`NDK_TOOLCHAIN_VERSION=clang3.1`*or* add this environment variable setting to`Application.mk`.
      - For standalone builds, add`--llvm-version=3.1`to`make-standalone-toolchain.sh`and replace`CC`and`CXX`in your makefile with`<tool-path>/bin/clang`and`<tool-path>/bin/clang++`. See`STANDALONE-TOOLCHAIN.html`for details.

      **Note:** This feature is experimental. Please try it and[report any issues](http://code.google.com/p/android/issues/list).
    - Added Gold linker`ld.gold`for the Windows toolchain. Gold linker is also the default for ARM and X86 on all hosts. You may override it to use the`ld.bfd`linker by adding`LOCAL_LDFLAGS += -fuse-ld=bfd`to`Android.mk`, or by passing`-fuse-ld=bfd`to the g++/clang++ command line that does the linking.
    - Added checks for spaces in the NDK path to the`ndk-build[.cmd]`and`ndk-gdb`scripts, to prevent build errors that are difficult to diagnose.
    - Made the following changes to API level handling:
      - Modified build logic so that projects that specify`android-10`through`android-13`in`APP_PLATFORM`,`project.properties`or`default.properties`link against`android-9`instead of`android-14`.
      - Updated build so that executables using android-16 (Jelly Bean) or higher are compiled with the`-fPIE`option for position-independent executables (PIE). A new`APP_PIE`option allows you to control this behavior. See`APPLICATION-MK.html`for details.

        **Note:** All API levels above 14 still link against`platforms/android-14`and no new`platforms/android-N`have been added.
      - Modified`ndk-build`to provide warnings if the adjusted API level is larger than`android:minSdkVersion`in the project's`AndroidManifest.xml`.
    - Updated the`cpu-features`helper library to include more ARM-specific features. See`sources/android/cpufeatures/cpu-features.h`for details.
    - Modified the long double on the X86 platform to be 8 bytes. This data type is now the same size as a double, but is still treated as a distinct type.
    - Updated build for`APP_ABI=armeabi-v7a`:
      - Modified this build type to pass the`-march=armv7-a`parameter to the linker. This change ensures that v7-specific libraries and`crt*.o`are linked correctly.
      - Added`-mfpu=vfpv3-d16`to`ndk-build`instead of the`-mfpu=vfp`option used in previous releases.

Important bug fixes:
:
    - Fixed an issue where running`make-standalone-toolchain.sh`with root privileges resulted in the stand alone tool chain being inaccessible to some users. ([Issue 35279](http://b.android.com/35279))
      - All files and executables in the NDK release package are set to have read and execute permissions for all.
      - The ownership/group of`libstdc++.a`is now preserved when copied.
    - Removed redundant`\r`from Windows prebuilt`echo.exe`. The redundant`\r`caused`gdb.setup`to fail in the GNU Debugger (GDB) because it incorrectly became part of the path. ([Issue 36054](http://b.android.com/36054))
    - Fixed Windows parallel builds that sometimes failed due to timing issues in the`host-mkdir`implementation. ([Issue 25875](http://b.android.com/25875))
    - Fixed GCC 4.4.3 GNU`libstdc++`to*not* merge`typeinfo`names by default. For more details, see`toolchain repo gcc/gcc-4.4.3/libstdc++-v3/libsupc++/typeinfo`. ([Issue 22165](http://b.android.com/22165))
    - Fixed problem on`null`context in GCC 4.6`cp/mangle.c::write_unscoped_name`, where GCC may crash when the context is`null`and dereferenced in`TREE_CODE`.
    - Fixed GCC 4.4.3 crashes on ARM NEON-specific type definitions for floats. ([Issue 34613](http://b.android.com/34613))
    - Fixed the`STLport`internal`_IteWrapper::operator*()`implementation where a stale stack location holding the dereferenced value was returned and caused runtime crashes. ([Issue 38630](http://b.android.com/38630))
    - ARM-specific fixes:
      - Fixed ARM GCC 4.4.3/4.6`g++`to not warn that the*mangling of \<va_list\> was changed in GCC 4.4* . The workaround using the`-Wno-psabi`switch to avoid this warning is no longer required.
      - Fixed an issue when a project with`.arm`or`.neon`suffixes in`LOCAL_SRC_FILES`also used`APP_STL`. With`APP_STL`, the`ndk-build`script searches for C++ files in`LOCAL_SRC_FILES`before adding STL`header/lib`paths to compilation. Modified`ndk-build`to filter out`.arm`and`.neon`suffixes before the search, otherwise items in`LOCAL_SRC_FILES`like`myfile.cpp.arm.neon`won't be compiled as C++ code.
      - Fixed`binutils-2.21/ld.bfd`to be capable of linking object from older binutils without`tag_FP_arch`, which was producing*assertion fail* error messages in GNU Binutils. ([Issue 35209](http://b.android.com/35209))
      - Removed*Unknown EABI object attribute 44* warning when`binutils-2.19/ld`links prebuilt object by newer`binutils-2.21`
      - Fixed an issue in GNU`stdc++`compilation with both`-mthumb`and`-march=armv7-a`, by modifying`make-standalone-toolchain.sh`to populate`headers/libs`in sub-directory`armv7-a/thumb`. ([Issue 35616](http://b.android.com/35616))
      - Fixed*unresolvable R_ARM_THM_CALL relocation* error. ([Issue 35342](http://b.android.com/35342))
      - Fixed internal compiler error at`reload1.c:3633`, caused by the ARM back-end expecting the wrong operand type when sign-extend from`char`. ([GCC Issue 50099](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=50099))
      - Fixed internal compiler error with negative shift amount. ([GCC Issue](http://gcc.gnu.org/ml/gcc-patches/2011-10/msg00594.html))
    - Fixed`-fstack-protector`for X86, which is also the default for the`ndk-build`x86 ABI target.
    - MIPS-specific fixes:
      - Fixed`STLport`endian-ness by setting`_STLP_LITTLE_ENDIAN`to 1 when compiling MIPS`libstlport_*`.
      - Fixed GCC`__builtin_unreachable`issue when compiling LLVM. ([GCC Issue 54369](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=54369))
      - Backported fix for`cc1`compile process consuming 100% CPU. ([GCC Issue 50380](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=50380))
    - GNU Debugger-specific fixes:
      - Disabled Python support in gdb-7.x at build, otherwise the gdb-7.x configure function may pick up whatever Python version is available on the host and build`gdb`with a hard-wired dependency on a specific version of Python. ([Issue 36120](http://b.android.com/36120))
      - Fixed`ndk-gdb`when`APP_ABI`contains`all`and matches none of the known architectures. ([Issue 35392](http://b.android.com/35392))
      - Fixed Windows pathname support, by keeping the`:`character if it looks like it could be part of a Windows path starting with a drive letter. ([GDB Issue 12843](http://sourceware.org/bugzilla/show_bug.cgi?id=12843))
      - Fixed adding of hardware breakpoint support for ARM in`gdbserver`. ([GDB Issue](http://sourceware.org/ml/gdb-patches/2011-09/msg00200.html))
      - Added fix to only read the current`solibs`when the linker is consistent. This change speeds up`solib`event handling. ([Issue 37677](http://b.android.com/37677))
      - Added fix to make repeated attempts to find`solib`breakpoints. GDB now retries`enable_break()`during every call to`svr4_current_sos()`until it succeeds. ([Change 43563](https://android-review.googlesource.com/#/c/43563))
      - Fixed an issue where`gdb`would not stop on breakpoints placed in`dlopen-ed`libraries. ([Issue 34856](http://b.android.com/34856))
      - Fixed`SIGILL`in dynamic linker when calling`dlopen()`, on system where`/system/bin/linker`is stripped of symbols and`rtld_db_dlactivity()`is implemented as`Thumb`, due to not preserving`LSB`of`sym_addr`. ([Issue 37147](http://b.android.com/37147))

Other bug fixes:
:
    - Fixed NDK headers:
      - Fixed`arch-mips/include/asm/*`code that was incorrectly removed from original kernel. ([Change 43335](https://android-review.googlesource.com/#/c/43335))
      - Replaced struct member data`__unused`with`__linux_unused`in`linux/sysctl.h`and`linux/icmp.h`to avoid conflict with`#define __unused`in`sys/cdefs.h`.
      - Fixed`fenv.h`for enclosed C functions with`__BEGIN_DECLS`and`__END_DECLS`.
      - Removed unimplemented functions in`malloc.h`.
      - Fixed`stdint.h`definition of`uint64_t`for ANSI compilers. ([Issue 1952](http://b.android.com/1952))
      - Fixed preprocessor macros in`<arch>/include/machine/*`.
      - Replaced`link.h`for MIPS with new version supporting all platforms.
      - Removed`linux-unistd.h`
      - Move GLibc-specific macros`LONG_LONG_MIN`,`LONG_LONG_MAX`and`ULONG_LONG_MAX`from`<pthread.h>`to`<limits.h>`.
    - Fixed a buffer overflow in`ndk-stack-parser`.
    - Fixed`_STLP_USE_EXCEPTIONS`, when not defined, to omit all declarations and uses of`__Named_exception`. Compiling and use of`__Named_exception`settings only occurs when`STLport`is allowed to use exceptions.
    - Fixed building of Linux-only NDK packages without also building Windows code. Use the following settings to perform this type of build:  

      ```
      ./build/tools/make-release.sh --force --systems=linux-x86
      ```
    - Fixed`libc.so`so it does not export`atexit()`and`__do_handler`. These symbols are exported for ARM builds by the system version of the C library to support legacy native libraries. NDK-generated should never reference them directly. Instead, each shared library or executable should embed its own version of these symbols, provided by`crtbegin_*.o`.

      If your project is linked with the`-nostdlib -Wl,--no-undefined`options, you must provide your own`__dso_handle`because`crtbegin_so.o`is not linked in this case. The content of`__dso_handle`does not matter, as shown in the following example code:  

      ```c++
      extern "C" {
        extern void *__dso_handle __attribute__((__visibility__ ("hidden")));
        void *__dso_handle;
      }
      ```
    - Fixed symbol decoder for ARM used in`objdump`for`plt`entries to generate a more readable form`function@plt`.
    - Removed the following symbols, introduced in GCC 4.6`libgcc.a`, from the X86 platform`libc.so`library:`__aeabi_idiv0`,`__aeabi_ldiv0`,`__aeabi_unwind_cpp_pr1`, and`__aeabi_unwind_cpp_pr2`.
    - Removed unused`.ctors`,`.dtors`, and`.eh_frame`in MIPS`crt*_so.S`.
    - Updated`ndk-gdb`so that it only takes the last line of output for`ndk-build``DUMP_XXXX`. This change ensures that if`Application.mk`or`Android.mk`print something with`$(info ...)`syntax, it does not get injected into the result of`DUMP_XXXX`. ([More info](https://groups.google.com/d/msg/android-ndk/-/ew0lTWGr1UEJ))

Other changes:
:
    - Removed`arch-x86`and`arch-mips`headers from`platforms/android-[3,4,5,8]`. Those headers were incomplete, since both X86 and MIPS ABIs are only supported at API 9 or higher.
    - Simplified c++ include path in standalone packages, as shown below. ([Issue 35279](http://b.android.com/35279))  

      ```
      <path>/arm-linux-androideabi/include/c++/4.6.x-google
        to:
      <path>/include/c++/4.6/
      ```
    - Fixed`ndk-build`to recognize more C++ file extensions by default:`.cc .cp .cxx .cpp .CPP .c++ .C`. You may still use`LOCAL_CPP_EXTENSION`to overwrite these extension settings.
    - Fixed an issue in`samples/san-angeles`that caused a black screen or freeze frame on re-launch.
    - Replaced deprecated APIs in NDK samples. ([Issue 20017](http://b.android.com/20017))
      - `hello-gl2`from android-5 to android-7
      - `native-activity`from android-9 to android-10
      - `native-audio`from android-9 to android-10
      - `native-plasma`from android-9 to android-10
    - Added new branding for Android executables with a simpler scheme in section`.note.android.ident`(defined in`crtbegin_static/dynamic.o`) so that debugging tools can act accordingly. The structure member and values are defined as follows:  

      ```c++
      static const struct {
        int32_t namesz;  /* = 8,  sizeof ("Android") */
        int32_t descsz;  /* = 1 * sizeof(int32_t) */
        int32_t type;    /* = 1, ABI_NOTETYPE */
        char name[sizeof "Android"];  /* = "Android" */
        int32_t android_api; /* = 3, 4, 5, 8, 9, 14 */
      }
      ```

      The previous branding options in section`.note.ABI-tag`are deprecated.
    - Added a new script`run-tests-all.sh`which calls`run-tests.sh`and`standalone/run.sh`with various conditions. The script`run-tests.sh`runs without the`--abi`option, and is enhanced to compile most of the tests for all supported ABIs and run on all attached devices
Android NDK r8b*(July 2012)*

The main features of this release are a new GNU Compiler Collection (GCC) 4.6 toolchain and GNU Debugger (GDB) 7.3.x which adds debugging support for the Android 4.1 (API Level 16) system image.

Important bug fixes:
:
    - Fixed`LOCAL_SHORT_COMMANDS`issues on Mac OS, Windows Cygwin environments for static libraries. List file generation is faster, and it is not regenerated to avoid repeated project rebuilds.
    - Fixed several issues in`ndk-gdb`:
      - Updated tool to pass flags`-e`,`-d`and`-s`to adb more consistently.
      - Updated tool to accept device serial names containing spaces.
      - Updated tool to retrieve`/system/bin/link`information, so`gdb`on the host can set a breakpoint in`__dl_rtld_db_dlactivity`and be aware of linker activity (e.g., rescan`solib`symbols when`dlopen()`is called).
    - Fixed`ndk-build clean`on Windows, which was failing to remove`./libs/*/lib*.so`.
    - Fixed`ndk-build.cmd`to return a non-zero`ERRORLEVEL`when`make`fails.
    - Fixed`libc.so`to stop incorrectly exporting the`__exidx_start`and`__exidx_end`symbols.
    - Fixed`SEGV`when unwinding the stack past`__libc_init`for ARM and MIPS.

Important changes:
:
    - Added GCC 4.6 toolchain (`binutils`2.21 with`gold`and GDB 7.3.x) to co-exist with the original GCC 4.4.3 toolchain (`binutils`2.19 and GDB 6.6).
      - GCC 4.6 is now the default toolchain. You may set`NDK_TOOLCHAIN_VERSION=4.4.3`in`Application.mk`to select the original one.
      - Support for the`gold`linker is only available for ARM and x86 architectures on Linux and Mac OS hosts. This support is disabled by default. Add`LOCAL_LDLIBS += -fuse-ld=gold`in`Android.mk`to enable it.
      - Programs compiled with`-fPIE`require the new`GDB`for debugging, including binaries in Android 4.1 (API Level 16) system images.
      - The`binutils`2.21`ld`tool contains back-ported fixes from version 2.22:
        - Fixed`ld --gc-sections`, which incorrectly retains zombie references to external libraries. ([more info](http://sourceware.org/bugzilla/show_bug.cgi?id=13177)).
        - Fixed ARM`strip`command to preserve the original`p_align`and`p_flags`in`GNU_RELRO`section if they are valid. Without this fix, programs built with`-fPIE`could not be debugged. ([mor e info](http://sourceware.org/cgi-bin/cvsweb.cgi/src/bfd/elf.c.diff?cvsroot=src&r1=1.552&r2=1.553))
      - Disabled`sincos()`optimization for compatibility with older platforms.
    - Updated build options to enable the Never eXecute (NX) bit and`relro`/`bind_now`protections by default:
      - Added`--noexecstack`to assembler and`-z noexecstack`to linker that provides NX protection against buffer overflow attacks by enabling NX bit on stack and heap.
      - Added`-z relro`and`-z now`to linker for hardening of internal data sections after linking to guard against security vulnerabilities caused by memory corruption. (more info:[1](http://www.akkadia.org/drepper/nonselsec.pdf),[2](http://tk-blog.blogspot.com/2009/02/relro-not-so-well-known-memory.html))
      - These features can be disabled using the following options:
        1. Disable NX protection by setting the`--execstack`option for the assembler and`-z execstack`for the linker.
        2. Disable hardening of internal data by setting the`-z norelro`and`-z lazy`options for the linker.
        3. Disable these protections in the NDK`jni/Android.mk`by setting the following options:  

           ```
           LOCAL_DISABLE_NO_EXECUTE=true  # disable "--noexecstack" and "-z noexecstack"
           DISABLE_RELRO=true             # disable "-z relro" and "-z now"
           ```

        See`docs/ANDROID-MK.html`for more details.
    - Added branding for Android executables with the`.note.ABI-tag`section (in`crtbegin_static/dynamic.o`) so that debugging tools can act accordingly. The structure member and values are defined as follows:  

      ```c++
      static const struct {
        int32_t namesz;  /* = 4,  sizeof ("GNU") */
        int32_t descsz;  /* = 6 * sizeof(int32_t) */
        int32_t type;    /* = 1 */
        char  name[sizeof "GNU"];  /* = "GNU" */
        int32_t os;      /* = 0 */
        int32_t major;   /* = 2 */
        int32_t minor;   /* = 6 */
        int32_t teeny;   /* = 15 */
        int32_t os_variant;  /* = 1 */
        int32_t android_api; /* = 3, 4, 5, 8, 9, 14 */
      }
      ```

Other bug fixes:
:
    - Fixed`mips-linux-gnu`relocation truncated to fit`R_MIPS_TLS_LDM`issue. ([more info](http://sourceware.org/bugzilla/show_bug.cgi?id=12637))
    - Fixed`ld`tool segfaults when using`--gc-sections`. ([more info](http://sourceware.org/bugzilla/show_bug.cgi?id=12845))
    - Fixed MIPS`GOT_PAGE`counting issue. ([more info](http://sourceware.org/ml/binutils/2011-05/msg00198.html))
    - Fixed follow warning symbol link for`mips_elf_count_got_symbols`.
    - Fixed follow warning symbol link for`mips_elf_allocate_lazy_stub`.
    - Moved MIPS`.dynamic`to the data segment, so that it is writable.
    - Replaced hard-coded values for symbols with correct segment sizes for MIPS.
    - Removed the`-mno-shared`option from the defaults in the MIPS toolchain. The default for Android toolchain is`-fPIC`(or`-fpic`if supported). If you do not explicitly specify`-mshared`,`-fpic`,`-fPIC`,`-fpie`, or`-fPIE`, the MIPS compiler adds`-mno-shared`that turns off PIC. Fixed compiler not to add`-mno-shared`in this case.
    - Fixed wrong package names in samples`hello-jni`and`two-libs`so that the`tests`project underneath it can compile.

Other Changes:
:
    - Changed locations of binaries:
      - Moved`gdbserver`from`toolchain/<arch-os-ver>/prebuilt/gdbserver`to`prebuilt/android-<arch>/gdbserver/gdbserver`.
      - Renamed x86 toolchain prefix from`i686-android-linux-`to`i686-linux-android-`.
      - Moved`sources/cxx-stl/gnu-libstdc++/include`and`lib`to`sources/cxx-stl/gnu-libstdc++/4.6`when compiled with GCC 4.6, or`sources/cxx-stl/gnu-libstdc++/4.4.3`when compiled with GCC 4.4.3.
      - Moved`libbfd.a`and`libintl.a`from`lib/`to`lib32/`.
    - Added and improved various scripts in the rebuild and test NDK toolchain:
      - Added`build-mingw64-toolchain.sh`to generate a new Linux-hosted toolchain that generates Win32 and Win64 executables.
      - Improved speed of`download-toolchain-sources.sh`by using the`clone`command and only using`checkout`for the directories that are needed to build the NDK toolchain binaries.
      - Added`build-host-gcc.sh`and`build-host-gdb.sh`scripts.
      - Added`tests/check-release.sh`to check the content of a given NDK installation directory, or an existing NDK package.
      - Rewrote the`tests/standalone/run.sh`standalone tests .
    - Removed`if_dl.h`header from all platforms and architectures. The`AF_LINK`and`sockaddr_dl`elements it describes are specific to BSD (i.e., they don't exist in Linux).
Android NDK r8*(May 2012)*

This release of the NDK includes support for MIPS ABI and a few additional fixes.

New features:
:
    - Added support for the MIPS ABI, which allows you to generate machine code that runs on compatible MIPS-based Android devices. Major features for MIPS include MIPS-specific toolchains, system headers, libraries and debugging support. For more details regarding MIPS support, see`docs/CPU-MIPS.html`in the NDK package.

      By default, code is generated for ARM-based devices. You can add`mips`to your`APP_ABI`definition in your`Application.mk`file to build for MIPS platforms. For example, the following line instructs`ndk-build`to build your code for three distinct ABIs:  

      ```
      APP_ABI := armeabi armeabi-v7a mips
      ```

      Unless you rely on architecture-specific assembly sources, such as ARM assembly code, you should not need to touch your`Android.mk`files to build MIPS machine code.
    - You can build a standalone MIPS toolchain using the`--arch=mips`option when calling`make-standalone-toolchain.sh`. See`docs/STANDALONE-TOOLCHAIN.html`for more details.

    **Note:**To ensure that your applications are available to users only if their devices are capable of running them, Google Play filters applications based on the instruction set information included in your application ? no action is needed on your part to enable the filtering. Additionally, the Android system itself also checks your application at install time and allows the installation to continue only if the application provides a library that is compiled for the device's CPU architecture.

Important bug fixes:
:
    - Fixed a typo in GAbi++ implementation where the result of`dynamic_cast<D>(b)`of base class object`b`to derived class`D`is incorrectly adjusted in the opposite direction from the base class. ([Issue 28721](http://b.android.com/28721))
    - Fixed an issue in which`make-standalone-toolchain.sh`fails to copy`libsupc++.*`.

Other bug fixes:
:
    - Fixed`ndk-build.cmd`to ensure that`ndk-build.cmd`works correctly even if the user has redefined the`SHELL`environment variable, which may be changed when installing a variety of development tools in Windows environments.
Android NDK r7c*(April 2012)*

This release of the NDK includes an important fix for Tegra2-based devices, and a few additional fixes and improvements:

Important bug fixes:
:
    - Fixed GNU STL armeabi-v7a binaries to not crash on non-NEON devices. The files provided with NDK r7b were not configured properly, resulting in crashes on Tegra2-based devices and others when trying to use certain floating-point functions (e.g.,`cosf`,`sinf`,`expf`).

Important changes:
:
    - Added support for custom output directories through the`NDK_OUT`environment variable. When defined, this variable is used to store all intermediate generated files, instead of`$PROJECT_PATH/obj`. The variable is also recognized by`ndk-gdb`.
    - Added support for building modules with hundreds or even thousands of source files by defining`LOCAL_SHORT_COMMANDS`to`true`in your`Android.mk`.

      This change forces the NDK build system to put most linker or archiver options into list files, as a work-around for command-line length limitations. See`docs/ANDROID-MK.html`for details.

Other bug fixes:
:
    - Fixed`android_getCpuCount()`implementation in the`cpufeatures`helper library. On certain devices, where cores are enabled dynamically by the system, the previous implementation would report the total number of*active* cores the first time the function was called, rather than the total number of*physically available*cores.
Android NDK r7b*(February 2012)*

This release of the NDK includes fixes for native Windows builds, Cygwin and many other improvements:

Important bug fixes:
:
    - Updated`sys/atomics.h`to avoid correctness issues on some multi-core ARM-based devices. Rebuild your unmodified sources with this version of the NDK and this problem should be completely eliminated. For more details, read`docs/ANDROID-ATOMICS.html`.
    - Reverted to`binutils`2.19 to fix debugging issues that appeared in NDK r7 (which switched to`binutils`2.20.1).
    - Fixed`ndk-build`on 32-bit Linux. A packaging error put a 64-bit version of the`awk`executable under`prebuilt/linux-x86/bin`in NDK r7.
    - Fixed native Windows build (`ndk-build.cmd`). Other build modes were not affected. The fixes include:
      - Removed an infinite loop / stack overflow bug that happened when trying to call`ndk-build.cmd`from a directory that was*not*the top of your project path (e.g., in any sub-directory of it).
      - Fixed a problem where the auto-generated dependency files were ignored. This meant that updating a header didn't trigger recompilation of sources that included it.
      - Fixed a problem where special characters in files or paths, other than spaces and quotes, were not correctly handled.
    - Fixed the standalone toolchain to generate proper binaries when using`-lstdc++`(i.e., linking against the GNU`libstdc++`C++ runtime). You should use`-lgnustl_shared`if you want to link against the shared library version or`-lstdc++`for the static version.

      See`docs/STANDALONE-TOOLCHAIN.html`for more details about this fix.
    - Fixed`gnustl_shared`on Cygwin. The linker complained that it couldn't find`libsupc++.a`even though the file was at the right location.
    - Fixed Cygwin C++ link when not using any specific C++ runtime through`APP_STL`.

Other changes:
:
    - When your application uses the GNU`libstdc++`runtime, the compiler will no longer forcibly enable exceptions and RTTI. This change results in smaller code.

      If you need these features, you must do one of the following:
      - Enable exceptions and/or RTTI explicitly in your modules or`Application.mk`. (recommended)
      - Define`APP_GNUSTL_FORCE_CPP_FEATURES`to`'exceptions'`,`'rtti'`or both in your`Application.mk`. See`docs/APPLICATION-MK.html`for more details.
    - `ndk-gdb`now works properly when your application has private services running in independent processes. It debugs the main application process, instead of the first process listed by`ps`, which is usually a service process.
    - Fixed a rare bug where NDK r7 would fail to honor the`LOCAL_ARM_MODE`value and always compile certain source files (but not all) to 32-bit instructions.
    - `STLport`: Refresh the sources to match the Android platform version. This update fixes a few minor bugs:
      - Fixed instantiation of an incomplete type
      - Fixed minor "==" versus "=" typo
      - Used`memmove`instead of`memcpy`in`string::assign`
      - Added better handling of`IsNANorINF`,`IsINF`,`IsNegNAN`, etc.

      For complete details, see the commit log.
    - `STLport`: Removed 5 unnecessary static initializers from the library.
    - The GNU libstdc++ libraries for armeabi-v7a were mistakenly compiled for armeabi instead. This change had no impact on correctness, but using the right ABI should provide slightly better performance.
    - The`cpu-features`helper library was updated to report three optional x86 CPU features (`SSSE3`,`MOVBE`and`POPCNT`). See`docs/CPU-FEATURES.html`for more details.
    - `docs/NDK-BUILD.html`was updated to mention`NDK_APPLICATION_MK`instead of`NDK_APP_APPLICATION_MK`to select a custom`Application.mk`file.
    - Cygwin:`ndk-build`no longer creates an empty "NUL" file in the current directory when invoked.
    - Cygwin: Added better automatic dependency detection. In the previous version, it didn't work properly in the following cases:
      - When the Cygwin drive prefix was not`/cygdrive`.
      - When using drive-less mounts, for example, when Cygwin would translate`/home`to`\\server\subdir`instead of`C:\Some\Dir`.
    - Cygwin:`ndk-build`does not try to use the native Windows tools under`$NDK/prebuilt/windows/bin`with certain versions of Cygwin and/or GNU Make.
Android NDK r7*(November 2011)*

This release of the NDK includes new features to support the Android 4.0 platform as well as many other additions and improvements:

New features
:
    - Added official NDK APIs for Android 4.0 (API level 14), which adds the following native features to the platform:
      - Added native multimedia API based on the Khronos Group OpenMAX AL 1.0.1 standard. The new`<OMXAL/OpenMAXAL.h>`and`<OMXAL/OpenMAXAL_Android.h>`headers allow applications targeting API level 14 to perform multimedia output directly from native code by using a new Android-specific buffer queue interface. For more details, see`docs/openmaxal/index.html`and<http://www.khronos.org/openmax/>.
      - Updated the native audio API based on the Khronos Group OpenSL ES 1.0.1 standard. With API Level 14, you can now decode compressed audio (e.g. MP3, AAC, Vorbis) to PCM. For more details, see`docs/opensles/index.html`and[http://www.khronos.org/opensles/](http://www.khronos.org/opensles).
    - Added CCache support. To speed up large rebuilds, define the`NDK_CCACHE`environment variable to`ccache`(or the path to your`ccache`binary). When declared, the NDK build system automatically uses CCache when compiling any source file. For example:  

      ```
      export NDK_CCACHE=ccache
      ```

      **Note:** CCache is not included in the NDK release so you must have it installed prior to using it. For more information about CCache, see<http://ccache.samba.org>.
    - Added support for setting`APP_ABI`to`all`to indicate that you want to build your NDK modules for all the ABIs supported by your given NDK release. This means that either one of the following two lines in your`Application.mk`are equivalent with this release:  

      ```
      APP_ABI := all
      APP_ABI := armeabi armeabi-v7a x86
      ```

      This also works if you define`APP_ABI`when calling`ndk-build`from the command-line, which is a quick way to check that your project builds for all supported ABIs without changing the project's`Application.mk file`. For example:  

      ```
      ndk-build APP_ABI=all
      ```
    - Added a`LOCAL_CPP_FEATURES`variable in`Android.mk`that allows you to declare which C++ features (RTTI or Exceptions) your module uses. This ensures that the final linking works correctly if you have prebuilt modules that depend on these features. See`docs/ANDROID-MK.html`and`docs/CPLUSPLUS-SUPPORT.html`for more details.
    - Shortened paths to source and object files that are used in build commands. When invoking`$NDK/ndk-build`from your project path, the paths to the source, object, and binary files that are passed to the build commands are significantly shorter now, because they are passed relative to the current directory. This is useful when building projects with a lot of source files, to avoid limits on the maximum command line length supported by your host operating system. The behavior is unchanged if you invoke`ndk-build`from a sub-directory of your project tree, or if you define`NDK_PROJECT_PATH`to point to a specific directory.

Experimental features
:   You can now build your NDK source files on Windows*without* Cygwin by calling the`ndk-build.cmd`script from the command line from your project path. The script takes exactly the same arguments as the original`ndk-build`script. The Windows NDK package comes with its own prebuilt binaries for GNU Make, Awk and other tools required by the build. You should not need to install anything else to get a working build system.

    **Important:** `ndk-gdb`does not work on Windows, so you still need Cygwin to debug.

    This feature is still experimental, so feel free to try it and report issues on the[public bug database](http://b.android.com)or[public forum](http://groups.google.com/group/android-ndk). All samples and unit tests shipped with the NDK successfully compile with this feature.

Important bug fixes
:
    - Imported shared libraries are now installed by default to the target installation location (`libs/<abi>`) if`APP_MODULES`is not defined in your`Application.mk`. For example, if a top-level module`foo`imports a module`bar`, then both`libfoo.so`and`libbar.so`are copied to the install location. Previously, only`libfoo.so`was copied, unless you listed`bar`in your`APP_MODULES`too. If you define`APP_MODULES`explicitly, the behavior is unchanged.
    - `ndk-gdb`now works correctly for activities with multiple categories in their MAIN intent filters.
    - Static library imports are now properly transitive. For example, if a top-level module`foo`imports static library`bar`that imports static library`zoo`, the`libfoo.so`will now be linked against both`libbar.a`and`libzoo.a`.

Other changes
:
    - `docs/NATIVE-ACTIVITY.HTML`: Fixed typo. The minimum API level should be 9, not 8 for native activities.
    - `docs/STABLE-APIS.html`: Added missing documentation listing EGL as a supported stable API, starting from API level 9.
    - `download-toolchain-sources.sh`: Updated to download the toolchain sources from[android.googlesource.com](http://android.googlesource.com), which is the new location for the AOSP servers.
    - Added a new C++ support runtime named`gabi++`. More details about it are available in the updated`docs/CPLUSPLUS-SUPPORT.html`.
    - Added a new C++ support runtime named`gnustl_shared`that corresponds to the shared library version of GNU libstdc++ v3 (GPLv3 license). See more info at`docs/CPLUSPLUS-SUPPORT.html`
    - Added support for RTTI in the STLport C++ runtimes (no support for exceptions).
    - Added support for multiple file extensions in`LOCAL_CPP_EXTENSION`. For example, to compile both`foo.cpp`and`bar.cxx`as C++ sources, declare the following:  

      ```
      LOCAL_CPP_EXTENSION := .cpp .cxx
      ```
    - Removed many unwanted exported symbols from the link-time shared system libraries provided by the NDK. This ensures that code generated with the standalone toolchain doesn't risk to accidentally depend on a non-stable ABI symbol (e.g. any libgcc.a symbol that changes each time the toolchain used to build the platform is changed)
    - Refreshed the EGL and OpenGLES Khronos headers to support more extensions. Note that this does*not* change the NDK ABIs for the corresponding libraries, because each extension must be probed at runtime by the client application.

      The extensions that are available depend on your actual device and GPU drivers, not the platform version the device runs on. The header changes simply add new constants and types to make it easier to use the extensions when they have been probed with`eglGetProcAddress()`or`glGetProcAddress()`. The following list describes the newly supported extensions:

      GLES 1.x
      :
          - `GL_OES_vertex_array_object`
          - `GL_OES_EGL_image_external`
          - `GL_APPLE_texture_2D_limited_npot`
          - `GL_EXT_blend_minmax`
          - `GL_EXT_discard_framebuffer`
          - `GL_EXT_multi_draw_arrays`
          - `GL_EXT_read_format_bgra`
          - `GL_EXT_texture_filter_anisotropic`
          - `GL_EXT_texture_format_BGRA8888`
          - `GL_EXT_texture_lod_bias`
          - `GL_IMG_read_format`
          - `GL_IMG_texture_compression_pvrtc`
          - `GL_IMG_texture_env_enhanced_fixed_function`
          - `GL_IMG_user_clip_plane`
          - `GL_IMG_multisampled_render_to_texture`
          - `GL_NV_fence`
          - `GL_QCOM_driver_control`
          - `GL_QCOM_extended_get`
          - `GL_QCOM_extended_get2`
          - `GL_QCOM_perfmon_global_mode`
          - `GL_QCOM_writeonly_rendering`
          - `GL_QCOM_tiled_rendering`

      GLES 2.0
      :
          - `GL_OES_element_index_uint`
          - `GL_OES_get_program_binary`
          - `GL_OES_mapbuffer`
          - `GL_OES_packed_depth_stencil`
          - `GL_OES_texture_3D`
          - `GL_OES_texture_float`
          - `GL_OES_texture_float_linear`
          - `GL_OES_texture_half_float_linear`
          - `GL_OES_texture_npot`
          - `GL_OES_vertex_array_object`
          - `GL_OES_EGL_image_external`
          - `GL_AMD_program_binary_Z400`
          - `GL_EXT_blend_minmax`
          - `GL_EXT_discard_framebuffer`
          - `GL_EXT_multi_draw_arrays`
          - `GL_EXT_read_format_bgra`
          - `GL_EXT_texture_format_BGRA8888`
          - `GL_EXT_texture_compression_dxt1`
          - `GL_IMG_program_binary`
          - `GL_IMG_read_format`
          - `GL_IMG_shader_binary`
          - `GL_IMG_texture_compression_pvrtc`
          - `GL_IMG_multisampled_render_to_texture`
          - `GL_NV_coverage_sample`
          - `GL_NV_depth_nonlinear`
          - `GL_QCOM_extended_get`
          - `GL_QCOM_extended_get2`
          - `GL_QCOM_writeonly_rendering`
          - `GL_QCOM_tiled_rendering`

      EGL
      :
          - `EGL_ANDROID_recordable`
          - `EGL_NV_system_time`
Android NDK r6b*(August 2011)*

This release of the NDK does not include any new features compared to r6. The r6b release addresses the following issues in the r6 release:

Important bug fixes
:
    - Fixed the build when`APP_ABI="armeabi x86"`is used for multi-architecture builds.
    - Fixed the location of prebuilt STLport binaries in the NDK release package. A bug in the packaging script placed them in the wrong location.
    - Fixed`atexit()`usage in shared libraries with the x86standalone toolchain.
    - Fixed`make-standalone-toolchain.sh --arch=x86`. It used to fail to copy the proper GNU libstdc++ binaries to the right location.
    - Fixed the standalone toolchain linker warnings about missing the definition and size for the`__dso_handle`symbol (ARM only).
    - Fixed the inclusion order of`$(SYSROOT)/usr/include`for x86 builds. See the[bug](http://b.android.com/18540)for more information.
    - Fixed the definitions of`ptrdiff_t`and`size_t`in x86-specific systems when they are used with the x86 standalone toolchain.
Android NDK r6*(July 2011)*

This release of the NDK includes support for the x86 ABI and other minor changes. For detailed information describing the changes in this release, read the`CHANGES.HTML`document included in the NDK package.

General notes:
:
    - Adds support for the x86 ABI, which allows you to generate machine code that runs on compatible x86-based Android devices. Major features for x86 include x86-specific toolchains, system headers, libraries and debugging support. For all of the details regarding x86 support, see`docs/CPU-X86.html`in the NDK package.

      By default, code is generated for ARM-based devices, but you can add x86 to your`APP_ABI`definition in your`Application.mk`file to build for x86 platforms. For example, the following line instructs`ndk-build`to build your code for three distinct ABIs:  

      ```
      APP_ABI := armeabi armeabi-v7a x86
      ```

      Unless you rely on ARM-based assembly sources, you shouldn't need to touch your`Android.mk`files to build x86 machine code.
    - You can build a standalone x86 toolchain using the`--toolchain=x86-4.4.3`option when calling`make-standalone-toolchain.sh`. See`docs/STANDALONE-TOOLCHAIN.html`for more details.
    - The new`ndk-stack`tool lets you translate stack traces in`logcat`that are generated by native code. The tool translates instruction addresses into a readable format that contains things such as the function, source file, and line number corresponding to each stack frame. For more information and a usage example, see`docs/NDK-STACK.html`.

Other changes:
:   `arm-eabi-4.4.0`, which had been deprecated since NDK r5, has been removed from the NDK distribution.
Android NDK r5c*(June 2011)*

This release of the NDK does not include any new features compared to r5b. The r5c release addresses the following problems in the r5b release:

Important bug fixes:
:
    - `ndk-build`: Fixed a rare bug that appeared when trying to perform parallel builds of debuggable projects.
    - Fixed a typo that prevented`LOCAL_WHOLE_STATIC_LIBRARIES`to work correctly with the new toolchain and added documentation for this in`docs/ANDROID-MK.html`.
    - Fixed a bug where code linked against`gnustl_static`crashed when run on platform releases older than API level 8 (Android 2.2).
    - `ndk-gdb`: Fixed a bug that caused a segmentation fault when debugging Android 3.0 or newer devices.
    - `<android/input.h>`: Two functions that were introduced in API level 9 (Android 2.3) were incorrect and are fixed. While this breaks the source API, the binary interface to the system is unchanged. The incorrect functions were missing a`history_index`parameter, and the correct definitions are shown below:  

      ```c++
      float AMotionEvent_getHistoricalRawX(const AInputEvent* motion_event,
                                                 size_t pointer_index,
                                                 size_t history_index);

      float AMotionEvent_getHistoricalRawY(const AInputEvent* motion_event,
                                                 size_t pointer_index,
                                                 size_t history_index);
      ```
    - Updated the C library ARM binary for API level 9 (Android 2.3) to correctly expose at link time new functions that were added in that API level (for example,`pthread_rwlock_init`).

Minor improvements and fixes:
:
    - Object files are now always linked in the order they appear in`LOCAL_SRC_FILES`. This was not the case previously because the files were grouped by source extensions instead.
    - When`import-module`fails, it now prints the list of directories that were searched. This is useful to check that the`NDK_MODULE_PATH`definition used by the build system is correct.
    - When`import-module`succeeds, it now prints the directory where the module was found to the log (visible with`NDK_LOG=1`).
    - Increased the build speed of debuggable applications when there is a very large number of include directories in the project.
    - `ndk-gdb`: Better detection of`adb shell`failures and improved error messages.
    - `<pthread.h>`: Fixed the definition of`PTHREAD_RWLOCK_INITIALIZER`for API level 9 (Android 2.3) and higher.
    - Fixed an issue where a module could import itself, resulting in an infinite loop in GNU Make.
    - Fixed a bug that caused the build to fail if`LOCAL_ARM_NEON`was set to true (typo in`build/core/build-binary.mk`).
    - Fixed a bug that prevented the compilation of`.s`assembly files (`.S`files were okay).
Android NDK r5b*(January 2011)*

This release of the NDK does not include any new features compared to r5. The r5b release addresses the following problems in the r5 release:

- The r5 binaries required glibc 2.11, but the r5b binaries are generated with a special toolchain that targets glibc 2.7 or higher instead. The Linux toolchain binaries now run on Ubuntu 8.04 or higher.
- Fixes a compiler bug in the arm-linux-androideabi-4.4.3 toolchain. The previous binary generated invalid thumb instruction sequences when dealing with signed chars.
- Adds missing documentation for the "gnustl_static" value for APP_STL, that allows you to link against a static library version of GNU libstdc++.
the
- Fixed the following`ndk-build`issues:
  - A bug that created inconsistent dependency files when a compilation error occurred on Windows. This prevented a proper build after the error was fixed in the source code.
  - A Cygwin-specific bug where using very short paths for the Android NDK installation or the project path led to the generation of invalid dependency files. This made incremental builds impossible.
  - A typo that prevented the cpufeatures library from working correctly with the new NDK toolchain.
  - Builds in Cygwin are faster by avoiding calls to`cygpath -m`from GNU Make for every source or object file, which caused problems with very large source trees. In case this doesn't work properly, define`NDK_USE_CYGPATH=1`in your environment to use`cygpath -m`again.
  - The Cygwin installation now notifies the user of invalid installation paths that contain spaces. Previously, an invalid path would output an error that complained about an incorrect version of GNU Make, even if the right one was installed.
- Fixed a typo that prevented the`NDK_MODULE_PATH`environment variable from working properly when it contained multiple directories separated with a colon.
- The`prebuilt-common.sh`script contains fixes to check the compiler for 64-bit generated machine code, instead of relying on the host tag, which allows the 32-bit toolchain to rebuild properly on Snow Leopard. The toolchain rebuild scripts now also support using a 32-bit host toolchain.
- A missing declaration for`INET_ADDRSTRLEN`was added to`<netinet/in.h>`.
- Missing declarations for`IN6_IS_ADDR_MC_NODELOCAL`and`IN6_IS_ADDR_MC_GLOBAL`were added to`<netinet/in6.h>`.
- 'asm' was replaced with '__asm__' in`<asm/byteorder.h>`to allow compilation with`-std=c99`.
Android NDK r5*(December 2010)*

This release of the NDK includes many new APIs, most of which are introduced to support the development of games and similar applications that make extensive use of native code. Using the APIs, developers have direct native access to events, audio, graphics and window management, assets, and storage. Developers can also implement the Android application lifecycle in native code with help from the new[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class. For detailed information describing the changes in this release, read the`CHANGES.HTML`document included in the downloaded NDK package.

General notes:
:
    - Adds support for native activities, which allows you to implement the Android application lifecycle in native code.
    - Adds native support for the following:
      - Input subsystem (such as the keyboard and touch screen)
      - Access to sensor data (accelerometer, compass, gyroscope, etc).
      - Event loop APIs to wait for things such as input and sensor events.
      - Window and surface subsystem
      - Audio APIs based on the OpenSL ES standard that support playback and recording as well as control over platform audio effects
      - Access to assets packaged in an`.apk`file.
    - Includes a new toolchain (based on GCC 4.4.3), which generates better code, and can also now be used as a standalone cross-compiler, for people who want to build their stuff with`./configure && make`. See docs/STANDALONE-TOOLCHAIN.html for the details. The binaries for GCC 4.4.0 are still provided, but the 4.2.1 binaries were removed.
    - Adds support for prebuilt static and shared libraries (docs/PREBUILTS.html) and module exports and imports to make sharing and reuse of third-party modules much easier (docs/IMPORT-MODULE.html explains why).
    - Provides a default C++ STL implementation (based on STLport) as a helper module. It can be used either as a static or shared library (details and usage examples are in sources/android/stlport/README). Prebuilt binaries for STLport (static or shared) and GNU libstdc++ (static only) are also provided if you choose to compile against those libraries instead of the default C++ STL implementation. C++ Exceptions and RTTI are not supported in the default STL implementation. For more information, see docs/CPLUSPLUS-SUPPORT.HTML.
    - Includes improvements to the`cpufeatures`helper library that improves reporting of the CPU type (some devices previously reported ARMv7 CPU when the device really was an ARMv6). We recommend developers that use this library to rebuild their applications then upload to Google Play to benefit from the improvements.
    - Adds an EGL library that lets you create and manage OpenGL ES textures and services.
    - Adds new sample applications,`native-plasma`and`native-activity`, to demonstrate how to write a native activity.
    - Includes many bugfixes and other small improvements; see docs/CHANGES.html for a more detailed list of changes.
Android NDK r4b*(June 2010)*

NDK r4b notes:

:   Includes fixes for several issues in the NDK build and debugging scripts --- if you are using NDK r4, we recommend downloading the NDK r4b build. For detailed information describing the changes in this release, read the CHANGES.TXT document included in the downloaded NDK package.

General notes:
:
    - Provides a simplified build system through the new`ndk-build`build command.
    - Adds support for easy native debugging of generated machine code on production devices through the new`ndk-gdb`command.
    - Adds a new Android-specific ABI for ARM-based CPU architectures,`armeabi-v7a`. The new ABI extends the existing`armeabi`ABI to include these CPU instruction set extensions:
      - Thumb-2 instructions
      - VFP hardware FPU instructions (VFPv3-D16)
      - Optional support for ARM Advanced SIMD (NEON) GCC intrinsics and VFPv3-D32. Supported by devices such as Verizon Droid by Motorola, Google Nexus One, and others.
    - Adds a new`cpufeatures`static library (with sources) that lets your app detect the host device's CPU features at runtime. Specifically, applications can check for ARMv7-A support, as well as VFPv3-D32 and NEON support, then provide separate code paths as needed.
    - Adds a sample application,`hello-neon`, that illustrates how to use the`cpufeatures`library to check CPU features and then provide an optimized code path using NEON instrinsics, if supported by the CPU.
    - Lets you generate machine code for either or both of the instruction sets supported by the NDK. For example, you can build for both ARMv5 and ARMv7-A architectures at the same time and have everything stored to your application's final`.apk`.
    - To ensure that your applications are available to users only if their devices are capable of running them, Google Play now filters applications based on the instruction set information included in your application --- no action is needed on your part to enable the filtering. Additionally, the Android system itself also checks your application at install time and allows the installation to continue only if the application provides a library that is compiled for the device's CPU architecture.
    - Adds support for Android 2.2, including a new stable API for accessing the pixel buffers of[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)objects from native code.
Android NDK r3*(March 2010)*

General notes:
:
    - Adds OpenGL ES 2.0 native library support.
    - Adds a sample application,`hello-gl2`, that illustrates the use of OpenGL ES 2.0 vertex and fragment shaders.
    - The toolchain binaries have been refreshed for this release with GCC 4.4.0, which should generate slightly more compact and efficient machine code than the previous one (4.2.1). The NDK also still provides the 4.2.1 binaries, which you can optionally use to build your machine code.
Android NDK r2*(September 2009)*

Originally released as "Android 1.6 NDK, Release 1".

General notes:
:
    - Adds OpenGL ES 1.1 native library support.
    - Adds a sample application,`san-angeles`, that renders 3D graphics through the native OpenGL ES APIs, while managing activity lifecycle with a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)object.
Android NDK r1*(June 2009)*

Originally released as "Android 1.5 NDK, Release 1".

General notes:
:
    - Includes compiler support (GCC) for ARMv5TE instructions, including Thumb-1 instructions.
    - Includes system headers for stable native APIs, documentation, and sample applications.