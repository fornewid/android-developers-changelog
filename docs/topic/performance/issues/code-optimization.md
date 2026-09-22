---
title: https://developer.android.com/topic/performance/issues/code-optimization
url: https://developer.android.com/topic/performance/issues/code-optimization
source: md.txt
---

Optimizing and obfuscating your code using [R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) or alternative tools (such as
ProGuard-compatible optimizers or secondary DEX post-processors) reduces your
app's DEX size, improves runtime performance, and minimizes its memory
footprint.

DEX, or [Dalvik Executable](https://source.android.com/docs/core/runtime/dex-format), files contain the compiled code used
to run your app. This typically includes Java and Kotlin code, as opposed to
compiled C++ code or `.so` files.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [DEX code optimization in Android vitals](https://developer.android.com/google/play/vitals/code-optimization).

## Measure R8 code optimization locally

To measure your app bundle's uncompressed DEX size locally using the command
line, run:

    unzip -l <yourapp>.aab | grep -E '\.dex$' | awk '{sum+=$1} END {print sum}'

If your app optimizes with R8, you can measure your app bundle's optimization,
obfuscation, and shrinking using the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer). For
detailed definitions of shrinking, optimization, and obfuscation, see [Use R8
Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer#understand-report). The R8 Configuration Analyzer report is also
included in the [R8 Analyzer Skill](https://github.com/android/skills/tree/main/performance/r8-analyzer).

To inspect the post-optimization metadata embedded in your app bundle (for AGP
version 8.10 or higher), extract the `r8.json` file:

    unzip -p <yourapp>.aab BUNDLE-METADATA/com.android.tools/r8.json

> [!NOTE]
> **Note:** The scores returned by the R8 Configuration Analyzer reflect the initial evaluation of the keep rules before optimizations. To get the post-optimization values, inspect the `r8.json` file.

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