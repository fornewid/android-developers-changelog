---
title: https://developer.android.com/agi/sys-trace/long
url: https://developer.android.com/agi/sys-trace/long
source: md.txt
---

# Estimate CPU and GPU frame processing times

Estimating CPU and GPU frame processing times (frame times) is essential for understanding your app's performance and locating bottlenecks. When you profile an app with AGI, System Profiler provides trace data that you can use to estimate frame times.

## CPU times

In AGI, you can view the total and active CPU frame times in the CPU track of a[system profile](https://developer.android.com/agi/sys-trace/sytem-profiler).

### Total CPU time

To measure the total CPU time spent,[select the time range](https://developer.android.com/agi/sys-trace/system-profiler-gui#select-a-time-range)that includes the time between successive frame submission events. The frame submission events are`eglSwapBuffers`(for OpenGL) and`vkQueuePresentKHR`(for Vulkan).
![A screenshot of eglSwapBuffer events.](https://developer.android.com/static/images/agi/long-images/image3.png)**Figure 1.** Time between two`eglSwapBuffer`events.

<br />

![A screenshot of a vkQueuePresentKHR event.](https://developer.android.com/static/images/agi/long-images/image19.png)**Figure 2.** Time between two`vkQueuePresentKHR`events.

This measurement is an estimate of total CPU time,but does not necessarily represent the active CPU time. For example, in GPU-bound apps, the CPU may wait for the GPU to complete its work before submitting a new frame. This often happens when a`dequeueBuffer`,`eglSwapBuffer`(for OpenGL), or`vkQueuePresent`(for Vulkan) event takes up a large portion of the CPU time. The wait time is included in the total CPU time, but not the active CPU time.
![A screenshot that displays a large amount of idling during dequeueBuffer and eglSwapBuffer events.](https://developer.android.com/static/images/agi/long-images/image1.png)**Figure 3.** A large amount of CPU idling during`dequeueBuffer`and`eglSwapBuffer`events.

### Active CPU time

Active CPU time determines when the CPU is running the app code without being in an idle state.

To measure the active CPU time, view the**Running** slices just above the CPU events. Count all portions of the trace between the two frame submission events that are in the*Running*state. Ensure that you include working threads.
![A screenshot of two periods of CPU time that can be used to measure the active CPU time.](https://developer.android.com/static/images/agi/long-images/image5.png)**Figure 5.**Two periods of CPU time that can be used to measure the active CPU time.

<br />

![A screenshot of a multithreaded app that has other working threads while the main thread is idle.](https://developer.android.com/static/images/agi/long-images/image10.png)**Figure 6.**A multithreaded app that has other working threads while the main thread is idle.

Another way to measure the active CPU time is to view the app slices in the CPU tracks. These slices indicated when the CPU is running and they correspond with the**Running**slices.
![A screenshot that displays the running state of a pinned thread that matches the CPU track.](https://developer.android.com/static/images/agi/long-images/image20.png)**Figure 7.**The pinned thread's running state matches the CPU track.

To help identify app slices, you can add[ATrace](https://perfetto.dev/docs/data-sources/atrace)markers to your app. This will display the markers in the CPU track of System Profiler.
![A screenshot of ATrace slices shown on a CPU track.](https://developer.android.com/static/images/agi/long-images/image2.png)**Figure 8.**ATrace slices shown on a CPU track.

## Estimate GPU frame times

To estimate GPU frame times, you can either use GPU slices or GPU counters in System Profiler. The estimate is more accurate when using GPU slices.

### GPU slices

If System Profiler has GPU slice information available, you can get very accurate GPU frame time information by measuring the total amount of time your app spends working on tasks that are associated with a single frame.

#### Mali devices

On Mali devices, GPU slices have**fragment** ,**non-fragment** , and occasionally**supplementary non-fragment**tracks. For less complex frames, the fragment and non-fragment work is sequential, so distinguishing one frame's work from another can be done by looking for gaps between active GPU work.

As an alternative, if you're familiar with the work that's being submitted to the GPU, identifying the pattern of the submitted render passes provides information about when a frame starts and ends.
![A screenshot of multiple frames being executed in sequence.](https://developer.android.com/static/images/agi/long-images/image14.png)**Figure 9.**Multiple frames being executed in sequence.![A screenshot where AGI is zoomed in on an individual frame’s work.](https://developer.android.com/static/images/agi/long-images/image6.png)**Figure 10.**Zoomed in on an individual frame's work.

For apps that have a more heavily-parallelized GPU workflow, you can get the GPU frame times by looking for all the frames that have the same**submissionID** in the**Selection**pane for each slice.

For Vulkan-based apps, multiple submissions can be used to compose a frame. Keep track of the submission IDs by using the**Vulkan Events**track, which contains a slice for each submission. Selecting a submission slice will highlight all the GPU activity slices that correspond to the submission.
![A screenshot of a parallelized GPU workload, where work on one frame can overlap with another.](https://developer.android.com/static/images/agi/long-images/image7.png)**Figure 11.**A parallelized GPU workload, where work on one frame can overlap with another.

<br />

![A screenshot of several Vulkan events selected for a frame.](https://developer.android.com/static/images/agi/long-images/image16.png)**Figure 12.**Several Vulkan events selected for a frame.

#### Adreno devices

On Adreno devices, GPU slices appear in the**GPU Queue 0**track and are always represented sequentially, so you can look at all the slices that represent the render passes for a frame and use them to measure GPU frame times.
![A screenshot of multiple frames being executed in sequence.](https://developer.android.com/static/images/agi/long-images/image13.png)**Figure 13.**Multiple frames being executed in sequence.![A screenshot where AGI is zoomed in on a frame with multiple render passes.](https://developer.android.com/static/images/agi/long-images/image11.png)**Figure 14.**Zoomed in on a frame with multiple render passes.

Similar to the Mali scenario described previously: if the app is using Vulkan, the**Vulkan Events** track provides information on the work being submitted to execute the frame. To highlight the render passes, click the**Vulkan Events**slices that are associated with the frame.
![A screenshot of a Vulkan-based app where Vulkan events of frame are selected.](https://developer.android.com/static/images/agi/long-images/image8.png)**Figure 15.**A Vulkan-based app where Vulkan events for a frame are selected.

There are some scenarios where the GPU frame boundaries are more challenging to distinguish due to the app being heavily GPU bound. In these scenarios, if you're familiar with the work that's being submitted to the GPU, you can identify the pattern that render passes are being executed with and determine the frame boundaries from that information.
![A screenshot of a heavily GPU bound app with a render pass pattern that helps identify frame boundaries.](https://developer.android.com/static/images/agi/long-images/image21.png)**Figure 16.**A heavily GPU bound app with a render pass pattern that helps identify frame boundaries.

### GPU counters

If GPU slice information is not available in a trace, you can estimate the GPU frame time using the**GPU counter**tracks.

#### Mali devices

On Mali devices, you can use the**GPU utilization** track to estimate the GPU frame time for an app that isn't GPU intensive. When apps are less GPU intensive, they have regular periods of high and low GPU activity, instead of consistently high activity. To estimate the GPU frame times using the**GPU utilization**track, measure the duration of high activity periods in the track.
![A screenshot of the GPU utilization and GPU Queue tracks on a Mali device.](https://developer.android.com/static/images/agi/long-images/image4.png)**Figure 17.**The GPU utilization and GPU Queue tracks on a Mali device.

If the app is more GPU-intensive, the GPU utilization can be consistently very high. In this case, you can use the**fragment queue utilization** and**non-fragment queue utilization** tracks to monitor GPU activity and estimate GPU frame times. By looking for patterns in**fragment** and**non-fragment**tracks, you can get a rough estimate of where the boundaries of a frame are, and use that to measure the GPU frame time.
![A screenshot of fragment and non-fragment tracks.](https://developer.android.com/static/images/agi/long-images/image9.png)**Figure 18.** **Fragment** and**non-fragment**tracks.

#### Adreno devices

On Adreno devices, if the app is not GPU-intensive, you can estimate GPU frame times the same way you can with[Mali devices](https://developer.android.com/agi/sys-trace/long#gpu-counters-mali)in the previous section.
![A screenshot of the GPU utilization percentage and GPU Queue tracks on an Adreno device.](https://developer.android.com/static/images/agi/long-images/image12.png)**Figure 19.**The GPU utilization percentage and GPU Queue tracks on an Adreno device.

If the app is more GPU-intensive, and the application has consistently high GPU utilization percentage, you can use the**Vertex Instructions / Second** and**Fragment Instructions / Second**tracks to estimate GPU frame times. By looking for patterns in the activity levels of these tracks, you can get a rough estimate of where the boundaries of a frame are, and use that to measure the GPU frame time.
![A screenshot of the Vertex Instructions / Second track.](https://developer.android.com/static/images/agi/long-images/image18.png)**Figure 20.** The**Vertex Instructions / Second**track.

These other tracks may provide similar information:

- **Vertices Shaded / Second**
- **Fragments Shaded / Second**
- **% Time Shading Vertices**
- **% Time Shading Fragments**