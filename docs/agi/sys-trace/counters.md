---
title: https://developer.android.com/agi/sys-trace/counters
url: https://developer.android.com/agi/sys-trace/counters
source: md.txt
---

Android GPU Inspector (AGI) can sample GPU performance counters from Arm® Mali™,
Imagination® PowerVR™, and Qualcomm® Adreno™ GPUs. You can use this data to
identify bottlenecks in your app's GPU usage.

You can enable each supported counter when you
[configure system profiling](https://developer.android.com/agi/start#system-profile) in AGI, and then view
the results in the
[GPU counters section](https://developer.android.com/agi/sys-trace/system-profiler-gui#gpu_counter_tracks)
of the System Profiler UI.

The names and descriptions of the supported counters for your Android device are
listed in the **GPU \> Counters \> Select** option of the **Capture System
Profiler** dialog. For information about configuring the **Counters** option,
see [Profile a system](https://developer.android.com/agi/start#system-profile).

For additional details about any GPU performance counters, check the developer
guides that are provided by your GPU manufacturer. The following guides include
GPU counter information; however, the level of detail can vary based on how much
the manufacturer chooses to publish:

- For Arm Mali, see
  [Mali GPU Performance Counters](https://developer.arm.com/ip-products/graphics-and-multimedia/mali-gpus/mali-performance-counters)
  in the Arm Developer guide.

- For Imagination PowerVR, see the
  [PVRTune Counter List and Description](https://cdn.imgtec.com/sdk-documentation/PVRTune.Counter%20List%20and%20Description.pdf)
  guide.

- For Qualcomm Adreno, see the
  [Adreno GPU guide](https://developer.qualcomm.com/sites/default/files/docs/adreno-gpu/snapdragon-game-toolkit/learn_guides.html).