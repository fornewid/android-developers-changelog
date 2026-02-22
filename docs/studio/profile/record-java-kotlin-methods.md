---
title: https://developer.android.com/studio/profile/record-java-kotlin-methods
url: https://developer.android.com/studio/profile/record-java-kotlin-methods
source: md.txt
---

# Record Java/Kotlin methods

Recording the Java/Kotlin methods called during your app's code execution lets you see the callstack and CPU usage at a given time, filtered to Java/Kotlin methods. This data is useful for identifying sections of code that take a long time or a lot of system resources to execute. If you want a full view of the callstack including native call frames, use the[callstack sample](https://developer.android.com/studio/profile/sample-callstack)profiling task.

When you record Java/Kotlin methods using the Android Studio profiler, you can choose the recording type:

- Tracing: Instruments your app at runtime to record a timestamp at the beginning and end of each method call. Timestamps are collected and compared to generate method tracing data, including timing information. You should use tracing when you care about the exact methods being called. Because tracing is an intensive process, if you're using this option it's best to keep your recording around five seconds or less.

  | **Note:** The timing information from tracing might deviate from production due to the overhead introduced by the instrumentation itself.
- Sampling (legacy): Captures your app's call stack at frequent intervals during your app's Java- or Kotlin-based code execution. The profiler compares sets of captured data to derive timing and resource usage information about your app's Java- or Kotlin-based code execution. You should use sampling if you care more about timing than the exact methods being called.

| **Note:** If you're interested in tracing methods with lifecycles so short that they're likely to begin and end in between a sampling interval, and thus get missed by the profiler, you should try tracing instead.

## Java/Kotlin methods overview

After you[run the**Find CPU Hotspots**task](https://developer.android.com/studio/profile#start-profiling)the Android Studio Profiler provides the following information:

![](https://developer.android.com/static/studio/images/profiler-jk-methods-recording.png)

- **CPU Usage**: Shows CPU usage of your app as a percentage of total available CPU capacity by time. Note that the CPU usage includes not only Java/Kotlin methods but also native code. Highlight a section of the timeline to filter to the details for that time period.
- **Interactions**: Shows user interaction and app lifecycle events along a timeline.
- **Threads**: Shows the threads that your app runs on. In most cases, you'll want to first focus on the topmost thread that represents your app.

To identify the methods or call stacks that take the most time, use the[flame chart](https://developer.android.com/studio/profile/chart-glossary/flame-chart)or[top down](https://developer.android.com/studio/profile/chart-glossary/top-bottom-charts)chart.