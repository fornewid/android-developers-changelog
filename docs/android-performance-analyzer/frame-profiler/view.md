---
title: https://developer.android.com/android-performance-analyzer/frame-profiler/view
url: https://developer.android.com/android-performance-analyzer/frame-profiler/view
source: md.txt
---

You can view any frame profiles that you've [captured previously](https://developer.android.com/android-performance-analyzer/frame-profiler/capture) in
the Frame Profiler in Android Performance Analyzer. This guide demonstrates how to use the trace view to interact
with recorded data and provides a detailed description of the data presented.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-profile.png) **Figure 1**: A screenshot of an example frame profile.

## Top bar

The top bar of the frame profile view includes metadata that provides an
at-a-glance view of the frame profile as a whole.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-top-bar.png) **Figure 2**: A screenshot of the top bar in the frame profile view.

### Screenshot

The far left side of the top bar is a thumbnail screenshot of the captured
frame. You can click on the thumbnail to open a resizable window providing a
zoomed-in view of the screenshot.

> [!NOTE]
> **Note:** The screenshot only appears if the Frame Profiler has completed the **Screenshot** [task](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details).

### Frame time

The **Active** and **Total** labels present the active and total frame time for
the captured frame respectively, as well as the margin of error for each.

> [!NOTE]
> **Note:** Frame time is only reported if the Frame Profiler has completed the **Frame Timing** [task](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details).

### Device details

The **Device** panel indicates whether the testing device originally used to
capture the frame profile is connected. Clicking the **Details** button opens
the **Device Details** window, which shows the device's model name, status, and
serial number.

### Task details

The **Tasks** panel shows the status of the *profiling tasks* involved in taking
the GFXR file and using it to generate the data in the frame profile. The Frame
Profiler runs these tasks after the initial frame capture; when they're
complete, the frame profile should be fully populated.

Clicking the **Details** button opens the **Task Details** window, where you can
see detailed task status, cancel running jobs, and rerun any failed tasks.

### Export

If the device you used to capture the frame profile is still connected, you can
click
![](https://developer.android.com/static/android-performance-analyzer/images/icon-export.png)
**Export** to generate an output file that you can [export into
RenderDoc](https://developer.android.com/android-performance-analyzer/frame-profiler/export#export-renderdoc) for further analysis. Triggering an export starts a
special *Export to RenderDoc* task; upon successful completion, Android Performance Analyzer
displays a pop-up notification to guide you to the output file in your file
system.

## Timeline

The timeline in the top half of the frame profile view behaves like a limited
version of the [trace view for a system profile](https://developer.android.com/android-performance-analyzer/view): the [GPU utilization
and counter data](https://developer.android.com/android-performance-analyzer/view/data#gpu) for the render time is presented in tracks and track
events.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-timeline.png) **Figure 3**: A screenshot of the timeline in the frame profile view.

You can use the following keyboard shortcuts to navigate the timeline:

- <kbd>A</kbd> and <kbd>D</kbd> (or <kbd>Left</kbd> and <kbd>Right</kbd>) to pan back and forth in the timeline.
- <kbd>W</kbd> and <kbd>S</kbd> to zoom in or out.
- <kbd>Up</kbd> and <kbd>Down</kbd> to scroll vertically.
- Hold <kbd>Shift</kbd> while using any of these shortcuts to speed up navigation.

You can also navigate by clicking and dragging, by using the scrollbars on the
right and bottom sides of the timeline, or by scrolling horizontally and
vertically with your trackpad or mouse wheel.

> [!NOTE]
> **Note:** The timeline is only populated if the Frame Profiler has completed the **Timeline** [task](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details).

## Bottom panel

The detail panel at the bottom of the frame profile view displays information
about [render stages](https://developer.android.com/android-performance-analyzer/frame-profiler/view#render-stages) and [GPU counters](https://developer.android.com/android-performance-analyzer/frame-profiler/view#gpu-counters) for the
frame.

### Render stages

The **Render Stages** tab shows a list of the render events that correspond to
the captured frame, as well as a duration and margin of error for each. These
render events correspond with the events on the GPU tracks in the timeline.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-render-stages.png) **Figure 4** : A screenshot of the **Render Stages** tab in the frame profile view.

> [!NOTE]
> **Note:** This tab is only populated if the Frame Profiler has completed the **Render Pass Timing** [task](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details).

### Frame GPU counters

The **Frame GPU Counters** tab shows a table with the value and margin of error
for all GPU counters measured.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-gpu-counters.png) **Figure 5** : A screenshot of the **Frame GPU Counters** tab in the frame profile view.

Clicking a row in this table displays further information about the
corresponding GPU counter in the detail panel on the right:

- **Name.** The name of the counter.
- **Type.** Whether the measured value is a sum or an average for this counter.
- **Units.** The unit of measurement for this counter.
- **Description.** A short description of what this counter measures.

> [!NOTE]
> **Note:** This tab is only populated if the Frame Profiler has completed the **Frame
> GPU Counters** [task](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details).