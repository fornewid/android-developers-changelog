---
title: https://developer.android.com/ndk/guides/memory-debug
url: https://developer.android.com/ndk/guides/memory-debug
source: md.txt
---

# Memory error debugging and mitigation

Android supports multiple tools for debugging memory errors. There are tradeoffs
to each, so read below to decide which is best for your use case. This doc gives
you an overview of the tools available so you can decide which to investigate
further, but it aims to be succinct, so read the tool-specific docs for details.

## tl;dr

- Use a [memory safe language](https://developer.android.com/ndk/guides/memory-debug#memory-safe-languages) whenever possible to make memory errors impossible
- Always use [PAC/BTI](https://developer.android.com/ndk/guides/memory-debug#pacbti) to mitigate ROP/JOP attacks
- Always use [GWP-ASan](https://developer.android.com/ndk/guides/memory-debug#gwp-asan) for detecting rare memory errors in production
- Use [HWASan](https://developer.android.com/ndk/guides/memory-debug#hwasan) to detect memory errors during testing
- [MTE](https://developer.android.com/ndk/guides/memory-debug#mte) is available as an option on [select devices](https://developer.android.com/ndk/guides/arm-mte#hwsupport).
- Use [ASan](https://developer.android.com/ndk/guides/memory-debug#asan) during testing only as a last resort

## Memory safe languages

A memory safe language is the only way to entirely avoid and mitigate memory
errors. The other tools on this page can help you make your memory unsafe code
safer and more reliable, but using a memory safe language eliminates the entire
class of problems.

The officially supported memory safe languages for Android are Java and Kotlin.
Most Android applications are easier to develop in one of those languages.

That said, there are app developers shipping code written in Rust, and if you're
reading this page you probably do have a good reason to need native code
(portability, performance, or both). Rust is the best choice for memory safe
native code on Android. The NDK team is not necessarily able to help you with
the problems you face if you go that route, but we are interested in
[hearing about them](https://github.com/android/ndk/discussions)!

## PAC/BTI

[Pointer Authentication and Branch Target Identification](https://developer.android.com/ndk/guides/abis#armv9_enabling_pac_and_bti_for_cc),
also known as PAC/BTI, are mitigation tools suitable for use in production.
Though separate technologies, they are controlled by the same compiler flag so
are always used together.

These features are backward compatible with devices that don't support them
because the new instructions used are no-ops on earlier devices. It's also
necessary to have a new enough kernel and a new enough version of the OS.
Looking for `paca` and `bti` in `/proc/cpuinfo` shows you whether you have new
enough hardware and a new enough kernel. Android 12 (API 31) has the necessary
userspace support.
| **Key Point:** Good mitigation requires defense in depth. Consider combining PAC/BTI with [MTE](https://developer.android.com/ndk/guides/memory-debug#mte).

Pros:

- Can be enabled in all builds without causing problems on older devices or kernels (but make sure you've actually tested on a device/kernel/OS combination that *does* support it!)

Cons:

- Only available for 64-bit apps
- Doesn't mitigate errors on devices that don't support it
- 1% code size overhead

## GWP-Asan

[GWP-ASan](https://developer.android.com/ndk/guides/gwp-asan) can be used to detect memory errors in the
field, but the sampling rate is too low to be an effective mitigation.

Pros:

- No significant CPU or memory overhead
- Trivial to deploy: does not require rebuilding native code
- Works for 32-bit apps

Cons:

- Low sampling rate requires a large number of users to find bugs effectively
- Only detects heap errors, not stack errors

## HWASan

[Hardware address sanitizer](https://developer.android.com/ndk/guides/hwasan), also known as HWASan, is the
best fit for catching memory errors during testing. It's most useful when used
with automated testing, especially if you're running fuzz tests, but depending
on your app's performance needs it may also be usable on high end phones in a
dogfood setting.

Pros:

- No false positives
- Detects additional classes of errors that ASan cannot (stack use after return)
- Lower rate of false negatives than MTE (1 in 256 vs 1 in 16)
- Lower memory overhead than ASan, its closest alternative

Cons:

- Significant CPU (\~100%), code size (\~50%), and memory (10% - 35%) overhead
- Until API 34 and NDK r26, requires flashing a HWASan compatible image
- Only works on 64-bit apps

## MTE

[Memory tagging extension](https://developer.android.com/ndk/guides/arm-mte), also known as MTE, is a lower-
cost alternative to HWASan. In addition to debugging and testing capabilities,
it can be used to detect and mitigate memory corruption in production. If you
have [the hardware to test MTE builds](https://developer.android.com/ndk/guides/arm-mte#check), you should
enable it.

Pros:

- Low enough overhead to be tolerable in production for many apps
- No false positives
- Does not require rebuilding code to detect heap errors (but does to detect stack errors)

Cons:

- There are no commercially available devices with MTE enabled by default in 2024, but Arm's documentation explains [how to enable MTE for testing on Pixel 8/Pixel 8 Pro](https://learn.arm.com/learning-paths/smartphones-and-mobile/mte_on_pixel8/).
- False negative rate of 1 in 16 vs HWASan's 1 in 256
- Only available for 64-bit apps
- Requires building separate libraries for targeting both MTE-enabled and non- MTE enabled devices

## ASan

[Address sanitizer](https://developer.android.com/ndk/guides/asan), also known as ASan, is the oldest and
most widely available of the tools available. It is useful for catching memory
errors during testing and debugging issues that only affect old devices where
none of the other tools are available. **Whenever possible, prefer HWASan.**
| **Deprecated:** ASan has been superseded by the other tools on this page, so is no longer receiving active development or support. ASan should only be used when HWASan is not an option.

Pros:

- Widely available. May work on devices as old as KitKat
- No false positives or negatives when used correctly

Cons:

- Difficult to build and package correctly
- Highest overhead of all options: \~100% CPU, \~50% code size, \~100% memory use
- No longer supported
- Has known bugs that won't be fixed