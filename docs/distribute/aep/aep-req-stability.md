---
title: https://developer.android.com/distribute/aep/aep-req-stability
url: https://developer.android.com/distribute/aep/aep-req-stability
source: md.txt
---

Implement specific quality standards to ensure a premium user experience across
different hardware categories. This approach accounts for technical limitations,
ensuring that stability benchmarks like Crash, ANR, and Jank are applied only to
the intended device categories to maintain a high-quality ecosystem.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

**Stability requirements**:

|---|---|---|
| **Android vitals** | [**Reference Devices**](https://developer.android.com/distribute/aep/aep-req-stability#reference-device) | **4GB+ RAM Android Devices** |
| [**Crashes**](https://developer.android.com/games/optimize/vitals/crash) | \<1% average crash rate | \<2% average crash rate |
| [**ANRs**](https://developer.android.com/games/optimize/vitals/anr) | \<2% average ANR rate | \<3% average ANR rate |
| [**Jank**](https://developer.android.com/topic/performance/vitals/render) | \<2% Excessive Slow Frames | N/A |

> [!NOTE]
> **Note:** The [bad behaviour thresholds](https://developer.android.com/topic/performance/vitals#what_are_the_bad_behavior_thresholds) that affect visibility within the Play Store are **not** the same as the Apps Experience program. The values documented here are used to determine eligibility of the Apps Experience program.

To reduce volatility, these thresholds will be enforced based on the trailing 28
days of data considering only devices within the approved set for which your app
has at least 1,500 sessions in the last 28 days.

**Memory usage requirements**:

To deliver a premium experience, [Android 17](https://android-developers.googleblog.com/2026/06/Android-17.html) is introducing
optimized memory handling and stricter platform requirements later this
year--accompanied by new, actionable memory telemetry in the Play Console.
Because **meeting these standard memory limits will be required for the Apps
Experience Program** , we strongly encourage [implementing these memory
optimization strategies](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html) early to ensure app stability and a
great user experience. More detailed compliance criteria to maintain your
program status will be shared in the coming months.

## Guideline applicability

This guideline applies to all apps that want to qualify for AEP across all form
factors. There are no exemptions from this guideline.

## Feature documentation and resources

The following resources provide implementation guidance for the **Stability**
guideline. These resources are for your reference only and don't contain
additional program requirements.

- [Android Vitals - Diagnose and fix vital issues](https://developer.android.com/topic/performance/vitals/lmk)
- [Managing your app's memory - Proactively reduce memory used by your app](https://developer.android.com/topic/performance/memory)

## Reference Device List

The following devices are used to test the AEP **Stability** guideline. Because
Android hardware and features evolve, this list can be updated to ensure
comprehensive coverage.

### Device list

| Year | System on a Chip vendor | System on a Chip model | Manufacturer | Marketing name | Form factor |
|---|---|---|---|---|---|
| 2026 | GOOGLE | TENSOR G5 | GOOGLE | PIXEL 10 PRO XL | PHONE |
| 2026 | GOOGLE | TENSOR G5 | GOOGLE | PIXEL 10 PRO FOLD | FOLDABLE |
| 2026 | MEDIATEK | MT6993 | VIVO | X300 | PHONE |
| 2026 | MEDIATEK | MT6993 | VIVO | X300 PRO | PHONE |
| 2026 | MEDIATEK | MT6993 | OPPO | FIND X9 PRO | PHONE |
| 2026 | MEDIATEK | MT6993 | OPPO | FIND X9 | PHONE |
| 2026 | QTI | SM8845 | ONEPLUS | ONEPLUS 15R | PHONE |
| 2026 | QTI | SM8845 | LENOVO | MOTOROLA SIGNATURE | PHONE |
| 2026 | QTI | SM8850 | SAMSUNG | GALAXY S26 ULTRA | PHONE |
| 2026 | QTI | SM8850 | SAMSUNG | GALAXY S26 | PHONE |
| 2026 | QTI | SM8850 | SAMSUNG | GALAXY S26+ | PHONE |
| 2026 | QTI | SM8850 | ONEPLUS | ONEPLUS 15 | PHONE |
| 2026 | QTI | SM8850 | OPPO | FIND N6 | FOLDABLE |
| 2026 | QTI | SM8850 | XIAOMI | XIAOMI 17 | PHONE |
| 2026 | QTI | SM8850 | XIAOMI | XIAOMI 17 ULTRA | PHONE |
| 2026 | QTI | SM8850 | XIAOMI | LEITZPHONE POWERED BY XIAOMI | PHONE |
| 2026 | QTI | SM8850 | XIAOMI | XIAOMI 17 PRO MAX | PHONE |
| 2026 | SAMSUNG | S5E9965 | SAMSUNG | GALAXY S26 | PHONE |
| 2026 | SAMSUNG | S5E9965 | SAMSUNG | GALAXY S26+ | PHONE |
| 2025 | GOOGLE | TENSOR G4 | GOOGLE | PIXEL 9 PRO XL | PHONE |
| 2025 | GOOGLE | TENSOR G4 | GOOGLE | PIXEL 9 PRO FOLD | FOLDABLE |
| 2025 | MEDIATEK | MT6991 | XIAOMI | XIAOMI 15T PRO | PHONE |
| 2025 | MEDIATEK | MT6991 | SAMSUNG | GALAXY TAB S11 | TABLET |
| 2025 | MEDIATEK | MT6991 | SAMSUNG | GALAXY TAB S11 ULTRA | TABLET |
| 2025 | MEDIATEK | MT6991 | SAMSUNG | GALAXY TAB S11 ULTRA 5G | TABLET |
| 2025 | MEDIATEK | MT6991 | SAMSUNG | GALAXY TAB S11 5G | TABLET |
| 2025 | MEDIATEK | MT6991 | VIVO | VIVO X200 | PHONE |
| 2025 | MEDIATEK | MT6991 | VIVO | X200 PRO | PHONE |
| 2025 | MEDIATEK | MT6991 | VIVO | X200T | PHONE |
| 2025 | MEDIATEK | MT6991 | OPPO | FIND X8 | PHONE |
| 2025 | MEDIATEK | MT6991 | OPPO | FIND X8 PRO | PHONE |
| 2025 | QTI | SM8735 | XIAOMI | XIAOMI PAD 8 | TABLET |
| 2025 | QTI | SM8750 | SAMSUNG | GALAXY S25 ULTRA | PHONE |
| 2025 | QTI | SM8750 | SAMSUNG | GALAXY S25 | PHONE |
| 2025 | QTI | SM8750 | SAMSUNG | GALAXY S25+ | PHONE |
| 2025 | QTI | SM8750 | SAMSUNG | GALAXY S25 EDGE | PHONE |
| 2025 | QTI | SM8750 | SAMSUNG | GALAXY Z FOLD7 | FOLDABLE |
| 2025 | QTI | SM8750 | ONEPLUS | ONEPLUS 13 | PHONE |
| 2025 | QTI | SM8750 | ONEPLUS | ONEPLUS 13S | PHONE |
| 2025 | QTI | SM8750 | ONEPLUS | PAD 3 | TABLET |
| 2025 | QTI | SM8750 | OPPO | FIND N5 | FOLDABLE |
| 2025 | QTI | SM8750 | XIAOMI | XIAOMI 15 | PHONE |
| 2025 | QTI | SM8750 | XIAOMI | XIAOMI 15 ULTRA | PHONE |
| 2025 | QTI | SM8750 | SONY | XPERIA 1 VII | PHONE |
| 2025 | QTI | SM8750 | VIVO | IQOO 13 | PHONE |

Comprehensive testing across every specific model may not be required because
several devices in the list use identical SoCs and exhibit comparable
performance. Developers are eligible to self-certify for the guidelines once
they have successfully verified requirements on at least one device from each
listed SoCs:

**Phones**

| Year | System on a Chip | Devices |
|---|---|---|
| **2026** | **Tensor G5** | **PIXEL 10 PRO XL** |
| **2025** | **Tensor G4** | **PIXEL 9 PRO XL** |
| **2026** | **MTK MT6993** | **X300, FIND X9** |
| **2025** | **MTK MT6991** | **XIAOMI 15T PRO, GALAXY TAB S11, VIVO X200, FIND X8** |
| **2026** | **QCOM SM8845/8850** | **ONEPLUS 15R, MOTOROLA SIGNATURE, GALAXY S26, ONEPLUS 15, XIAOMI 17** |
| **2025** | **QCOM SM8750** | **GALAXY S25, ONEPLUS 13, PAD 3, XIAOMI 15. XPERIA 1 VII, IQOO 13** |
| **2026** | **Exynos S5E9965** | **GALAXY S26** |

**Tablet**

| **Year** | **System on a Chip** | **Devices** |
|---|---|---|
| **2025** | **MTK MT6991** | **GALAXY TAB S11** |
| **2025** | **QCOM SM8735** | **XIAOMI PAD 8** |
| **2025** | **QCOM SM8750** | **OPPO PAD 3** |