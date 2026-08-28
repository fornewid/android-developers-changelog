---
title: https://developer.android.com/topic/performance/vitals/code-optimization
url: https://developer.android.com/topic/performance/vitals/code-optimization
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

Android vitals can alert you when your app's DEX code optimization levels are
low. This includes obfuscation, shrinking, and optimization for apps and games
that use R8. For apps not using R8, Android vitals attempts to check
optimization, shrinking, and obfuscation rates, but falls back to obfuscation
heuristics as a proxy where necessary.

### Monitor optimization status

Android vitals can help improve your app's performance by alerting you
[via Play Console](https://support.google.com/googleplay/android-developer/answer/9844486) when your app doesn't meet the minimum defined percentages
for code optimization. For detailed definitions of shrinking, optimization, and
obfuscation, see [Use R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer#understand-report).

For apps built with the latest patch of AGP version 8.10 or higher, these
percentages are pulled from the included `r8.json` file.

For lower versions of AGP or where the `r8.json` file isn't included, the
percentages are calculated from the `mapping.txt` file if included, or using DEX
heuristics if the mapping file isn't available.

For apps that are optimized with an alternative code optimizer, Android vitals
performs an analysis to estimate the percentage of classes, methods, and fields
that are obfuscated in the app bundle.

#### Total DEX size minimums

While Android vitals calculates code optimization metrics for all apps, you will
only receive alerts if your app bundle meets the following total DEX size
requirements:

- **Apps**: Bundle contains at least 10 MB of DEX code measured as uncompressed size
- **Games**: Bundle contains at least 50 MB of DEX code measured as uncompressed size

Android vitals displays your app's DEX size, but you can also measure this
locally using the command line:

      unzip -l <yourapp>.aab | grep -E '\.dex$' | awk '{sum+=$1} END {print sum}'

### Measure R8 code optimization locally

If your app optimizes with R8, you can measure your app bundle's optimization,
obfuscation, and shrinking using the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer). The R8
Configuration Analyzer report is also included in the [R8 Analyzer
Skill](https://github.com/android/skills/tree/main/performance/r8-analyzer).

To inspect the exact metadata that Android vitals uses to calculate your scores,
extract the `r8.json` file from your app bundle:

    unzip -p <yourapp>.aab BUNDLE-METADATA/com.android.tools/r8.json

> [!NOTE]
> **Note:** The app optimization scores in Android vitals can differ slightly from the scores returned by the R8 Configuration Analyzer. To get the matching values, inspect the `r8.json`.

## Fix the problem

To address low DEX code optimization scores, review the recommendations based
on your build system and optimizer:

### Android Gradle Plugin and R8

To improve your R8 DEX code optimization scores, see the guidance at
[Improve R8 optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#improve-r8-optimization). You can also use the [R8 Analyzer skill](https://github.com/android/skills/tree/main/performance/r8-analyzer) to get
additional guidance on optimizing your app's keep rules.

### Non-R8 build systems and DEX post-processors

If your build pipeline uses custom build tools or secondary DEX post-processors,
take the following steps to improve your app's optimization:

- Open your app bundle in Android Studio and view it in the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer).
- Select all of [the `.dex` files](https://developer.android.com/studio/debug/apk-analyzer#filter_the_dex_file_tree_view).
- Pay close attention to the files with the largest size as you toggle the "Deobfuscate names" button (note: this requires you to [upload a `mapping.txt` file](https://developer.android.com/studio/debug/apk-analyzer#load_proguard_mappings)). If you find some of those files stay large while obfuscated, it's likely they're affected by package-wide keep rules.
- Look either in your `proguard-rules.pro` file, `configuration.txt`, or the equivalent for your optimizer if you're not using R8, and search for keep rules that match the packages that aren't getting obfuscated. For example, if `com.foo.` is a large package in your dex, look for keep rules of the format `-keep com.foo.**` or `-keep com.foo.bar.**`.
- Keep in mind that library consumer keep rules might not be as straightforward to identify. If you suspect a library consumer rule is impacting optimization, you can validate locally by adding it to a standalone sample app using a recent version of AGP, and inspecting it with R8 Configuration Analyzer.