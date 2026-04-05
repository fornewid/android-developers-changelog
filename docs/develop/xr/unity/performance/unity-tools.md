---
title: https://developer.android.com/develop/xr/unity/performance/unity-tools
url: https://developer.android.com/develop/xr/unity/performance/unity-tools
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Unity provides various performance-related tools and APIs. Use these tools to
measure and monitor performance metrics, specify a display refresh rate, and
analyze how your scene is rendered frame by frame.

## Measure and monitor performance metrics

The [Unity OpenXR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/index.html) package gives you comprehensive
performance data you can use to monitor and optimize your app.

You can access these metrics through the [Performance Metrics
API](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/features/performance-metrics.html).

### Benefits

- Real-time monitoring of memory usage, CPU and GPU performance.
- System statistics from compositor and runtime layers.
- Measure the impact of optimization changes.

To get the best results, actively monitor these metrics while working on your
app and tuning the performance:

    AndroidXRPerformanceMetrics androidXRPerformanceMetrics = OpenXRSettings.Instance.GetFeature<AndroidXRPerformanceMetrics>();

    string values = "";

    if (m_Display != null && androidXRPerformanceMetrics != null && androidXRPerformanceMetrics.supportedMetricPaths != null)
      foreach (var metric in androidXRPerformanceMetrics.supportedMetricPaths)
      {
        float stat;
        XRStats.TryGetStat(m_Display, metric, out stat);

        values += string.Format("{0}: {1:F2}\n", metric, stat);
      }

## Specify a Display Refresh Rate

[Display Refresh Rate](https://docs.unity3d.com/6000.2/Documentation/ScriptReference/RefreshRate.html) lets your app request higher or lower
frame rates from the runtime, which the system tries to honor.

### Benefits

- Adjust refresh rates based on scene complexity.
- Optimize power consumption during lighter scenes.
- Adapt dynamically to app demands.

### Enable this feature

Use the [Unity API](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/features/display-utilities.html) to access the `XR_FB_display_refresh_rate`
extension.

You can request frame rates such as 72fps, 90fps, or 120fps, and then the system
switches to your requested rate if the hardware can handle it and thermal
conditions allow it.

## Enable Unity's Frame Debugger

The [Frame Debugger](https://docs.unity3d.com/6000.2/Documentation/Manual/FrameDebugger.html) is Unity's built-in tool for analyzing how
your scene is rendered frame by frame. This tool shows you the sequence of draw
calls and lets you step through them to understand rendering behavior.

### Benefits

- Identify rendering bottlenecks and unexpected draw calls.
- Verify that the [SRP Batcher](https://developer.android.com/develop/xr/unity/performance/urp-asset-settings#enable-srp-batcher) is working correctly (look for "RenderLoopNewBatcher" entries).
- Check [GPU Resident Drawer](https://developer.android.com/develop/xr/unity/performance/gpu-rendering#gpu-resident-drawer) batching (look for "Hybrid Batch Group" entries).
- Understand the order of rendering operations.

### Enable this feature

1. From the Unity main menu, click **Window \> Analysis \> Frame Debugger**.
2. Click **Enable** to start capturing frame data.
3. Step through draw calls to see what's being rendered and when.