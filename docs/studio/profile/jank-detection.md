---
title: https://developer.android.com/studio/profile/jank-detection
url: https://developer.android.com/studio/profile/jank-detection
source: md.txt
---

# UI jank detection

Android renders UI by generating a frame from your app and displaying it on the screen. If your app suffers from slow UI rendering, then the system is forced to skip frames. When this happens, the user perceives a recurring flicker on their screen, which is referred to as*jank*.

When jank occurs, it's usually because of some deceleration or blocking async call on the UI thread (in most apps, it's the main thread). You can use system traces to identify where the problem is.

## Detect jank on Android 12 and higher

For devices using Android 12 (API level 31) or higher, a captured trace is shown in the**Janky frames** track under the**Display**pane in the CPU Profiler.

To detect jank,

1. In Android Studio, select**View \> Tool Windows \> Profiler** or click**Profile** ![](https://developer.android.com/static/studio/images/buttons/toolbar-android-profiler_dark.png)in the toolbar.

   If prompted by the**Select Deployment Target** dialog, choose the device to which to deploy your app for profiling. If you've connected a device over USB but don't see it listed, ensure that you have[enabled USB debugging](https://developer.android.com/studio/debug/dev-options#enable).
2. Click anywhere in the**CPU**timeline to open the CPU Profiler.

3. Select**System Trace** from the configurations menu in the CPU Profiler and click**Record** . After you finish interacting with your app, click**Stop**.

4. You should see the**Janky frames** track under**Display** . By default, the Profiler only shows janky frames as candidates for investigation. Within each janky frame, the red portion highlights the duration the frame takes past its rendering deadline.![Screenshot of the Janky frames track](https://developer.android.com/static/studio/images/profile/jank_detection-janky_frames.png)

5. Once you find a janky frame, click on it; optionally, you can press**M** to adjust the zoom to focus on the selected frame. The relevant events are highlighted in these threads: the main thread,**RenderThread** and**GPU completion** .![Screenshot of Profiler displaying Janky frames and main threads](https://developer.android.com/static/studio/images/profile/jank_detection-janky_frames_detailed.png)

6. You can optionally see all frames or a breakdown of the rendering time by toggling the checkboxes**All Frames** and**Lifecycle** , respectively.![Screenshot of Profiler as above but with All Frames and Lifecycle checkboxes checked](https://developer.android.com/static/studio/images/profile/jank_detection-allframes_lifecycle_checkboxed.png)

## Detect jank on Android 11

For devices using Android 11 (API level 30), a captured trace is shown in the**Frame Lifecycle**section in the CPU Profiler.

![Frame Lifecycle section with different tracks](https://developer.android.com/static/studio/images/profile/jank_detection-frame-lifecycle-tracks.png)

The**Frame Lifecycle** section contains the layer name and four tracks. Each track represents one stage in the frame rendering pipeline. The**Frame Lifecycle**elements are as follows:

1. **Frame Lifecycle (Layer name)** : The section title contains the layer name in parentheses. A*layer*is a single unit of composition.
2. **Application** : This track shows the time from when the buffer was dequeued by the app to when it was enqueued back. This usually corresponds to the trace events in`RenderThread`.
3. **Wait for GPU** : This track shows how long the buffer was owned by the GPU. This is the time from when the buffer is sent to the GPU to when the GPU finishes its work on the buffer.**This does not indicate that the GPU was working only on this buffer during this time.** For detailed info on what the GPU works on during a given time, you may want to use[Android GPU Inspector](https://developer.android.com/agi).
4. **Composition**: This track shows the time starting from when SurfaceFlinger latches on to the buffer and sends it for composition, to when the buffer is sent to the display.
5. **Frames on display**: This track shows how long the frame was on the screen.

The**Frame Lifecycle**section illustrates how a frame buffer moves between different stages of the rendering pipeline. The frames are color coded by frame number so that it's easier to track a particular frame.

Android Studio also shows all frames in the trace in a table format in the**All Frames**tab.

![A table of all the frames in the trace in the All Frames tab](https://developer.android.com/static/studio/images/profile/jd-all-frames.png)

The**Frame #** ,**Application** ,**Wait for GPU** , and**Composition** columns represent the same data as the tracks in the**Frame Lifecycle** section as above. The column**Frame Duration** represents the time from the start of**Application** to the start of**Frames on Display**. This is essentially how long it takes to render a frame end-to-end.

You can sort the frames table by any column to quickly find the shortest or longest frame. The table also supports pagination controls that help you navigate through hundreds of frames.

To detect and investigate jank on Android 11, follow these steps:

1. Sort the**All Frames** table by the**Application**column in descending order, so that the frames that take the longest appear first.

   ![Application column sorted in descending order](https://developer.android.com/static/studio/images/profile/jank_detection-app-col-sorted.png)
2. Find the longest running frames and select the table row. This zooms in on the selected frame in the timeline view to the left.

   ![Timeline view alongside Frames table](https://developer.android.com/static/studio/images/profile/jank_detection-timeline-and-frames-table.png)
3. Look for relevant threads in the**Frame Lifecycle** and**Threads**sections.

   ![Frame Lifecycle and Threads sections](https://developer.android.com/static/studio/images/profile/jank_detection-frame-lifecycle-threads.png)

## Detect jank on Android 10 and lower

For devices using Android 10 (API level 29) and lower, relevant OS graphics pipeline information is displayed in a single section on the CPU Profiler system trace called**Display**.

![The display UI window](https://developer.android.com/static/studio/images/profile/jank_detection-system_trace.png)

- **Frames** : This section shows the UI thread and`RenderThread`trace events in your app. Events that are longer than 16ms are colored red to highlight potential janky frames because they exceed the deadline to render at 60 frames per second (fps).
- **SurfaceFlinger**: This section shows when the SurfaceFlinger processes the frame buffers. SurfaceFlinger is a system process that is responsible for sending buffers to display.
- **VSYNC**: This section displays the VSYNC, a signal that synchronizes the display pipeline. The track displays the VSYNC-app signal, which shows when your app is starting too late. Typically, this occurs because the UI thread is busy. It causes a visible flicker to appear on your screen during an animation and adds extra input latency until the animation or scroll completes. This is especially important to view for high-refresh-rate displays, as they may occur more frequently than 60 times per second or at a variable rate.
- **BufferQueue** : This section shows how many frame buffers are queued up and are waiting for SurfaceFlinger to consume. For apps deployed to devices running Android 9 (API level 28) or higher, this track shows the buffer count of the app's surface[BufferQueue](https://source.android.com/devices/graphics#bufferqueue)(`0`,`1`, or`2`). BufferQueue can help you understand the state of image buffers as they move between the Android graphics components. For example, a value of`2`means that the app is currently triple-buffered, which results in extra input latency.

The**Display** section provides useful signals to detect potential jank---for example, when the UI thread or`RenderThread`takes longer than 16 ms. To investigate exact details of what caused the jank, you can probe the**Threads**section, which shows the threads relevant to UI rendering.

![The Threads section under Display](https://developer.android.com/static/studio/images/profile/jank_detection-threads.png)

In the figure above, the**Threads** section shows the UI thread (`java.com.google.samples.apps.iosched`),`RenderThread`, and the`GPU completion`thread. These are the threads relevant to UI rendering and may contribute to jank.

To detect jank on Android 10 or lower, follow these steps:

1. Look at the**Frames** track in**Display**. The red frames are candidates for investigation.

   ![The Frames section under Display](https://developer.android.com/static/studio/images/profile/jank_detection-frames-track.png)
2. Once you find a potentially janky frame, zoom in by pressing`W`or scrolling the mouse wheel while holding<kbd>Control</kbd>(<kbd>Command</kbd>on macOS). Continue zooming in until you start to see the trace events in the UI thread and`RenderThread`.

   ![Trace events in the UI thread and RenderThread](https://developer.android.com/static/studio/images/profile/jank_detection-trace-events-ui-renderthread.png)

   In the figure above,`Choreographer#doFrame`shows when the UI thread calls[`Choreographer`](https://developer.android.com/reference/android/view/Choreographer)to coordinate animation, view layout, image drawing, and related processes.`DrawFrames`shows when`RenderThread`forms and issues actual drawing commands to the GPU.
3. If you see a particularly long trace event, you can zoom in further and find out what may have contributed to the slow rendering. The figure above shows`inflate`in the UI thread, which means the app is spending time on inflating the layout. When you zoom into one of the`inflate`events, you can find out exactly how long each UI component is taking, as shown below.

   ![Menu showing precise duration of a UI component](https://developer.android.com/static/studio/images/profile/jank_detection-ui-component-duration.png)

## Learn more

To learn more about how to reduce jank, see[Common sources of jank](https://developer.android.com/topic/performance/vitals/render#common-jank).