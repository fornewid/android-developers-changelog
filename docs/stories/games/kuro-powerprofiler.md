---
title: https://developer.android.com/stories/games/kuro-powerprofiler
url: https://developer.android.com/stories/games/kuro-powerprofiler
source: md.txt
---

# Kuro Games reduces 9.68% power consumption through Android Studio Power Profiler and ODPM for Wuthering Waves

[Wuthering Waves](https://play.google.com/store/apps/details?id=com.kurogame.wutheringwaves.global)is a high fidelity action RPG game developed by Kuro Games. Optimizing the power consumption is very important to sustainably deliver a premium user experience for long gaming sessions.
![](https://developer.android.com/static/images/cards/distribute/stories/kuro_game_screenshot.jpg)**Figure 1.**Wuthering Waves Screenshot

Android Studio introduced the[Power Profiler](https://developer.android.com/studio/profile/power-profiler)from Hedgehog (2023.1.1) that can help developers understand power consumption data based on On Device Power Rails Monitor (ODPM).

With power profiling capabilities in Android Studio, you can also[effectively A/B test power consumption](https://android-developers.googleblog.com/2024/04/how-to-effectively-ab-test-power-consumption-for-your-android-app-features.html)for your Android app's features (as shown below).
![](https://developer.android.com/static/images/cards/distribute/stories/kuro_AS_screenshot.png)**Figure 2.**Android Studio Power Profiler Screenshot

## What they did

Kuro Games began by using the Android Studio Power Profiler to understand how game behaviors impact device power consumption. This experience led them to develop a customized tool based on Perfetto and ODPM, incorporating the following enhancements:

- Customized views - the developer can filter power rails and preset flexible time ranges.
- Better maintenance - the developer can upload the power consumption data to their customized QA system and compare data across game versions.

### Process ODPM data

To access ODPM data, Kuro Games used[Perfetto Trace Processor (Python) Metric API](https://perfetto.dev/docs/analysis/trace-processor-python#metric)to process`avg_used_power_mw data`of 30-second session from`android_powerrails`metric, which is defined as`AndroidPowerRails`in[Pertetto metrics proto](https://android.googlesource.com/platform/external/perfetto/+/main/protos/perfetto/metrics/perfetto_merged_metrics.proto), into the following format:

|      Power Rail       | Graphics Quality | FPS | Brightness | Average Power consumption | Percentage(Per Rail / Total) |
|-----------------------|------------------|-----|------------|---------------------------|------------------------------|
| power.rail.cpu.big    | High             | 30  | Low        | 474.158mW                 | 14.70%                       |
| power.rail.cpu.mid    | High             | 30  | Low        | 470.916mW                 | 14.60%                       |
| power.rail.cpu.little | High             | 30  | Low        | 438.662mW                 | 13.60%                       |
| power.rail.gpu        | High             | 30  | Low        | 346.761mW                 | 10.70%                       |
| ...                   | ...              | ... | ...        | ...                       | ...                          |

| **Note:**Screen brightness contributes significantly to power consumption, so it is important to set the same brightness throughout power consumption testing.

### Identify high-power-consumed power rails

There is no standard value for each power rail. To identify high-power-consumed power rails, Kuro Games created A/B tests using different test cases including idle, running and combating. Specific power rails with obviously high values can be identified by comparing values of the same power rails. By comparing the behavioral differences across various test cases, the root cause of the power consumption issue will be figured out gradually.

### Optimizations

With ODPM data, Kuro Games can measure the improvement of each optimization scenario:

- Changing the CPU core scheduling strategy and adjusting priority of different threads to reduce the workload of big cores
- Pre-compiling the PSO (Pipeline State Object) to reduce the runtime shader compiling workload of CPU
- Implementing PVS (Potentially Visible Sets) culling to reduce the GPU rendering workload
- Baking offline shadow occlusion culling to reduce the GPU rendering workload

To compare test results under identical and reproducible conditions, Kuro Games retrieved the ODPM data in a test case using the same 3D scene and camera perspective with the same duration.
| **Note:** If you don't have a customized profile system, you can refer to this[blog post](https://android-developers.googleblog.com/2024/04/how-to-effectively-ab-test-power-consumption-for-your-android-app-features.html)about how to compare power consumption ODPM data of different tests with the same duration through Power Profiler.

## Results

By leveraging data from ODPM and power profiling, Kuro Games reduced total power consumption by 9.68%, from 3233mW in the September release (version 0904) to 2920mW in the November release (version 1.4 final). The following figure details this power reduction under consistent FPS and graphics settings.
![](https://developer.android.com/static/images/cards/distribute/stories/kuro_powerrail_data.png)**Figure 3.**Power rail data differences between September version and November version

ODPM data is currently only available for Pixel 6 and higher devices, but improvements can be seen on all Android devices through other metrics including CPU Usage, GPU Usage and Batterystats. For example, Kuro Games also saw an overall 9.6% reduction in GPU usage in the same scene for Oppo Reno 5.

## Get started

You can start from[Power Profiler](https://developer.android.com/studio/profile/power-profiler), or[Perfetto Power Rails](https://perfetto.dev/docs/reference/trace-packet-proto#PowerRails)data for advanced use cases.

ODPM Power Rail names are device-specific. A rail name may be something like "S2S_VDD_G3D"; specific knowledge of the device hardware is required to interpret the corresponding power monitor data. From Android API level 35, you can use[`PowerMonitor`](https://developer.android.com/reference/android/os/PowerMonitor)from[`getSupportedPowerMonitors`](https://developer.android.com/reference/android/os/health/SystemHealthManager#getSupportedPowerMonitors(java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.util.List%3Candroid.os.PowerMonitor%3E%3E)). With PowerMonitor, you can retrieve the mapping between human-readable labels and the raw power rails names set by each individual OEMs.

To verify improvement on devices without ODPM, you can use CPU clocks, GPU clocks, and memory bandwidth estimates as a proxy for power consumption.

## Additional resources

[Optimize power efficiency](https://developer.android.com/games/optimize/power)