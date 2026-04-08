---
title: https://developer.android.com/agi/frame-trace-gui/report-pane
url: https://developer.android.com/agi/frame-trace-gui/report-pane
source: md.txt
---

![Report pane](https://developer.android.com/static/images/agi/report-pane/report-pane.png) **Figure 1.**Report pane

The **Report** pane shows any issues found with the capture and its replay.
This includes issues caused by incorrect parameter usage, invalid command sequences or errors reported by the driver used for replay.

If you are using GAPID to diagnose incorrect rendering, check the **Report** pane
for any issues.

## Note for Vulkan

The **Report** pane currently shows very few messages for Vulkan. Furthermore,
given Vulkan's explicit and low-level nature, replaying a Vulkan trace on a
target that is different than the tracing target is unlikely to work for any
but the most straightforward traces.