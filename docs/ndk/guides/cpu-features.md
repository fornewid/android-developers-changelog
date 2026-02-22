---
title: https://developer.android.com/ndk/guides/cpu-features
url: https://developer.android.com/ndk/guides/cpu-features
source: md.txt
---

# CPU features

There are several ways to check for CPU features in your code, each with a different set of trade-offs.

## ABI: Use the preprocessor's pre-defined macros

It's usually most convenient to determine the ABI at build time using`#ifdef`in conjunction with:

- `__arm__`for 32-bit ARM
- `__aarch64__`for 64-bit ARM
- `__i386__`for 32-bit X86
- `__x86_64__`for 64-bit X86

Note that 32-bit X86 is called`__i386__`, not`__x86__`as you might expect!

## CPU core counts: Use libc's sysconf(3)

[sysconf(3)](http://man7.org/linux/man-pages/man3/sysconf.3.html)lets you query both`_SC_NPROCESSORS_CONF`(the number of CPU cores in the system) and`_SC_NPROCESSORS_ONLN`(the number of CPU cores currently online).

## Features: Use libc's getauxval(3)

In API level 18 and newer,[getauxval(3)](http://man7.org/linux/man-pages/man3/getauxval.3.html)is available in Android's C library. The`AT_HWCAP`and`AT_HWCAP2`arguments return bitmasks listing CPU-specific features. See the various`hwcap.h`headers in the NDK for the constants to compare against, such as`HWCAP_SHA512`for arm64's SHA512 instructions, or`HWCAP_IDIVT`for arm's Thumb integer division instructions.

## The Google cpu_features library

One problem with`AT_HWCAP`is that sometimes devices are mistaken. Some old devices, for example, claim to have integer division instructions but do not.

[Google's cpu_features](https://github.com/google/cpu_features)library works around such issues by applying its own knowledge of specific SoCs (by parsing`/proc/cpuinfo`to work out the specific SoC in question).

This library is maintained for use by Google's first-party app teams, and has workarounds for every problematic device they've encountered in the wild.

## The NDK cpufeatures library (deprecated)

The NDK still provides a deprecated library named`cpufeatures`for source compatibility with apps that already use it. Unlike the newer and more complete[cpu_features](https://github.com/google/cpu_features)library, this historical library does not have workarounds for as many specific SoCs.