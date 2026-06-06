---
title: https://developer.android.com/android-performance-analyzer/analyze/frame-times
url: https://developer.android.com/android-performance-analyzer/analyze/frame-times
source: md.txt
---

Estimating CPU and GPU frame processing times (or *frame times* ) is essential
for understanding your app's performance and finding potential bottlenecks.
When you use the System Profiler in Android Performance Analyzer to [record a system trace](https://developer.android.com/android-performance-analyzer/run), the
[resulting trace view](https://developer.android.com/android-performance-analyzer/view) provides data that you can use to estimate
frame times.

## Measure CPU frame times

In the System Profiler, you can view the total and active CPU frame times in the
process tracks.

### Total CPU time

To measure the total CPU time for a frame, [select the time range](https://developer.android.com/android-performance-analyzer/view#select-range)
between successive frame submission events. For Vulkan, the frame submission
events are named `vkQueuePresentKHR`.
![](https://developer.android.com/static/android-performance-analyzer/images/frame-vk-events.png) **Figure 1** : A screenshot of a highlighted time range between two `vkQueuePresentKHR` events on a thread track.

This measurement is an estimate of the total CPU time, but doesn't necessarily
represent the active CPU time. For example, in GPU-bound apps, the CPU might
wait for the GPU to complete its work before submitting a new frame. This often
happens when a `dequeueBuffer` or `vkQueuePresent` (for Vulkan) event takes up a
large portion of the CPU time. The wait time is included in the total CPU time,
but not the active CPU time.

### Active CPU time

Active CPU time is the time when the CPU is running the app code without being in an idle state.

To measure the active CPU time, view the `Running` slices in the thread track
just above the CPU events. Count all portions of the trace that are in a
`Running` state between the two frame submission events. Make sure you include
working threads.
![](https://developer.android.com/static/android-performance-analyzer/images/running-slices.png) **Figure 2** : A screenshot showing `Running` slices used to measure the active CPU time. ![](https://developer.android.com/static/android-performance-analyzer/images/parallel-threads.png) **Figure 3**: A screenshot showing thread tracks in a multithreaded app.

## Estimate GPU frame times

The most accurate way to estimate GPU frame times is to [use GPU
slices](https://developer.android.com/android-performance-analyzer/analyze/frame-times#gpu-slices), but if tracing GPU slices isn't supported for your test
device, then you can also [use GPU counters](https://developer.android.com/android-performance-analyzer/analyze/frame-times#gpu-counters). The System Profiler in Android Performance Analyzer
supports both approaches.

### Estimate with GPU slices

If GPU slice information is available in your trace data, you can get very
accurate GPU frame time information by measuring the total amount of time your
app spends working on tasks that are associated with a single frame.

### Adreno

On Adreno devices, GPU slices appear in the **GPU Queue 0**track and are
always represented sequentially, so you can look at all the slices that
represent the render passes for a frame and use them to measure GPU frame
times.
![](https://developer.android.com/static/android-performance-analyzer/images/adreno-sequential.png) **Figure 4** : A screenshot showing the **GPU Queue 0** track with multiple frames being executed in sequence.

### Mali

On Mali devices, GPU slices have **fragment** , **non-fragment** , and sometimes
**supplementary non-fragment** tracks. The **fragment** and **non-fragment**
work is sequential for less complex frames, so distinguishing one frame's work
from another can be done by looking for gaps between active GPU work.
![](https://developer.android.com/static/android-performance-analyzer/images/mali-sequential.png) **Figure 5** : A screenshot showing the **fragment** and **non-fragment** tracks with multiple frames being executed in sequence.

For apps and games that have a more heavily-parallelized GPU workflow, you
can get the GPU frame times by looking for all of the frames that have the
same `submissionID` value in the detail view for each slice.

For Vulkan-based apps, multiple submissions can be used to compose a frame. Keep
track of the submission IDs by using the **Vulkan Events** track, which contains
a slice for each submission. Selecting a submission slice highlights all the GPU
activity slices that correspond to the submission.
![](https://developer.android.com/static/android-performance-analyzer/images/vulkan-submissions.png) **Figure 6** : A screenshot of a **Vulkan Events** track with a submission slice selected and the corresponding GPU activity slices highlighted.

To trace complex submissions back to specific engine subsystems, assign
distinct, descriptive names to your render pass objects using object naming
extensions like `vkSetDebugUtilsObjectNameEXT`. Then, enable the **Render Pass
Debug Names (Experimental)** [Vulkan layer](https://developer.android.com/android-performance-analyzer/run#vulkan) when configuring your trace.

### Estimate with GPU counters

If GPU slice information isn't available in a trace or isn't appropriate for
your needs, you can also estimate the GPU frame time using the GPU counter
tracks.

### Adreno

For apps that aren't GPU intensive, you can use the **GPU % Utilization**
counter track to estimate the GPU frame time. When apps are less GPU
intensive, they have regular periods of high and low GPU activity, instead of
consistently high activity. To estimate the GPU frame times using this track,
measure the duration of high activity periods in the track.
![](https://developer.android.com/static/android-performance-analyzer/images/adreno-spikes.png) **Figure 7** : A screenshot showing the **GPU %
Utilization** track with pronounced higher-intensity periods.

For apps or games that *are* GPU intensive, the GPU utilization can be
consistently very high. In this case, you can use the **Vertex
Instructions/Second** and **Fragment Instructions/Second** counter tracks to
monitor GPU activity and estimate GPU frame times. By looking for patterns in
these tracks, you can get a rough estimate of where the boundaries of the
frame are.
![](https://developer.android.com/static/android-performance-analyzer/images/adreno-gpu-intensive.png) **Figure 8** : A screenshot showing the **GPU %
Utilization** , **Vertex Instructions/Second** , and **Fragment
Instructions/Second** counter tracks.

### Mali

For apps that aren't GPU intensive, you can use the **GPU utilization**
counter track to estimate the GPU frame time. When apps are less GPU
intensive, they have regular periods of high and low GPU activity, instead of
consistently high activity. To estimate the GPU frame times using this track,
measure the duration of high activity periods in the track.
![](https://developer.android.com/static/android-performance-analyzer/images/mali-spikes.png) **Figure 9** : A screenshot showing the **GPU utilization** track with pronounced higher-intensity periods.

For apps or games that are GPU intensive, the GPU utilization can be
consistently very high. In this case, you can use the **Fragment queue
utilization** and **Non-fragment queue utilization** counter tracks to monitor
GPU activity and estimate GPU frame times. By looking for patterns in these
tracks, you can get a rough estimate of where the boundaries of the frame
are.
![](https://developer.android.com/static/android-performance-analyzer/images/mali-gpu-intensive.png) **Figure 10** : A screenshot showing the **Fragment queue
utilization** and **Non-fragment queue utilization** counter tracks.