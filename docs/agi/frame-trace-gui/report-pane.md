---
title: Report pane  |  Android Developers
url: https://developer.android.com/agi/frame-trace-gui/report-pane
source: html-scrape
---

Join us for ⁠the [Google for Games Developer Summit](https://gamedevsummit.withgoogle.com/) on March 15!

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Report pane Stay organized with collections Save and categorize content based on your preferences.



![Report pane](/static/images/agi/report-pane/report-pane.png)


**Figure 1.** Report pane

The **Report** pane shows any issues found with the capture and its replay.
This includes issues caused by incorrect parameter usage, invalid command sequences or errors reported by the driver used for replay.

If you are using GAPID to diagnose incorrect rendering, check the **Report** pane
for any issues.

## Note for Vulkan

The **Report** pane currently shows very few messages for Vulkan. Furthermore,
given Vulkan's explicit and low-level nature, replaying a Vulkan trace on a
target that is different than the tracing target is unlikely to work for any
but the most straightforward traces.