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

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [DEX code optimization](https://developer.android.com/topic/performance/issues/code-optimization).

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

To inspect the exact metadata that Android vitals uses to calculate your scores,
extract the `r8.json` file from your app bundle:

    unzip -p <yourapp>.aab BUNDLE-METADATA/com.android.tools/r8.json

> [!NOTE]
> **Note:** The app optimization scores in Android vitals may differ from the scores returned by the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer). This is because the R8 Configuration Analyzer scores reflect the initial evaluation of the keep rules before optimizations. To get the matching values, inspect the `r8.json`.