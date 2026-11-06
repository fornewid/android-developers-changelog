---
title: https://developer.android.com/google/play/vitals/code-optimization
url: https://developer.android.com/google/play/vitals/code-optimization
source: md.txt
---

DEX code optimization is an Android vitals finding that helps you monitor and
improve your app's compilation quality, size, and performance. Optimizing and
obfuscating your code using [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) or alternative tools (such as
ProGuard-compatible optimizers or secondary DEX post-processors) reduces your
app's DEX size, improves runtime performance, and minimizes its memory
footprint.

DEX, or [Dalvik Executable](https://source.android.com/docs/core/runtime/dex-format), files contain the compiled code used
to run your app. This typically includes Java and Kotlin code, as opposed to
compiled C++ code or `.so` files.

Android vitals reports DEX code optimization metrics for all apps and games, but
only enforces thresholds for apps and games that meet specific size
requirements.

## Detect the problem

Android vitals can alert you [in Play Console](https://support.google.com/googleplay/android-developer/answer/9844486) when your app's DEX code
optimization, shrinking, or obfuscation levels don't meet the minimum
[defined percentages](https://developer.android.com/google/play/vitals#dex_code_optimization).

### How optimization scores are calculated

For apps built with the latest patch version of AGP 8.10 or higher (for example,
`8.10.1` rather than `8.10.0`), these percentages are pulled from the included
`r8.json` file. Make sure you use the latest patch version of AGP and R8 for
your minor version so that accurate metadata is generated.

For apps built with earlier versions of AGP, or apps optimized with an
alternative code optimizer where `r8.json` isn't included, Android vitals
estimates obfuscation percentages as a proxy using the `mapping.txt` file (if
included) or DEX heuristics.

### Total DEX size minimums

While Android vitals calculates code optimization metrics for all apps, you will
only receive alerts if your app bundle meets the following total DEX size
requirements:

- **Apps**: Bundle contains at least 10 MB of DEX code measured as uncompressed size
- **Games**: Bundle contains at least 50 MB of DEX code measured as uncompressed size

### Measure code optimization locally

To measure your app bundle's uncompressed DEX size and get the optimization,
shrinking, and obfuscation percentages that match the findings in Android
vitals, run [`android analyze`](https://developer.android.com/tools/agents/android-cli/commands/analyze):

    android analyze <yourapp>.aab

## Fix the problem

To address low DEX code optimization scores, review the recommendations based
on your build system and optimizer:

### R8

To improve your R8 DEX code optimization scores, see the guidance at
[Improve R8 optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#improve-r8-optimization), and use the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) to
understand how your keep rules affect your optimization, shrinking, and
obfuscation scores (for detailed definitions of these metrics, see
[Understand the report](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer#understand-report)).

If you use the Android Gradle Plugin (AGP), you can also use the
[R8 Analyzer skill](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer#skill-title_r8-configuration-analyzer) to get additional guidance on optimizing your app's keep
rules. If you use Bazel, you also have access to the R8 Configuration Analyzer;
see the [`rules_android` R8 optimization documentation](https://github.com/bazelbuild/rules_android/tree/main/docs/r8-optimization.md#r8-configuration-analyzer).

> [!NOTE]
> **Note:** The app optimization scores in Android vitals may differ from the scores returned by the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer). This is because the R8 Configuration Analyzer scores reflect the initial evaluation of the keep rules before optimizations. To get the values that match Android vitals, use [`android analyze`](https://developer.android.com/tools/agents/android-cli/commands/analyze).

### Non-R8 optimizers and DEX post-processors

If your build pipeline uses custom build tools or secondary DEX post-processors,
take the following steps to improve your app's optimization:

- Open your app bundle in Android Studio and view it in the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer).
- Select all of [the `.dex` files](https://developer.android.com/studio/debug/apk-analyzer#view_dex_files).
- Pay close attention to the files with the largest size as you toggle the "Deobfuscate names" button (note: this requires you to [load a `mapping.txt` file](https://developer.android.com/studio/debug/apk-analyzer#load_proguard_mappings)). If you find some of those files stay large while obfuscated, it's likely they're affected by package-wide keep rules.
- Look either in your `proguard-rules.pro` file, `configuration.txt`, or the equivalent for your optimizer if you're not using R8, and search for keep rules that match the packages that aren't getting obfuscated. For example, if `com.foo.` is a large package in your DEX files, look for keep rules of the format `-keep com.foo.**` or `-keep com.foo.bar.**`.
- Keep in mind that library consumer keep rules might not be as straightforward to identify. If you suspect a library consumer rule is impacting optimization, you can inspect the library directly using `android analyze <library>.aar`, or validate it by adding the library to a standalone sample app using a recent version of AGP and inspecting it with the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer).