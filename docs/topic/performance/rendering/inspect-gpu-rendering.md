---
title: https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering
url: https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering
source: md.txt
---

Android includes some on-device developer options that help you visualize where your app might be running into issues rendering its UI, such as performing more rendering work than necessary, or executing long thread and GPU operations. This page describes how to debug GPU overdraw and profile GPU rendering.

To learn more about on-device developer options, including how to enable them, read[Configure on-device developer options](https://developer.android.com/studio/debug/dev-options).

## Profile GPU rendering speed

The Profile GPU Rendering tool displays, as a scrolling histogram, a visual representation of how much time it takes to render the frames of a UI window relative to a benchmark of 16.67ms per frame.

On less powerful GPUs, available fill-rate (the speed at which the GPU can fill the frame buffer) can be quite low. As the number of pixels required to draw a frame increases, the GPU might take longer to process new commands, causing the rest of the system to wait until the GPU can catch up.

The profiling tool helps you identify when the GPU gets overwhelmed trying to draw pixels or is burdened by heavy overdraw.
| **Note:** This profiling tool does not work with apps that use the NDK. This is because the system pushes framework messages to the background whenever OpenGL takes a full-screen context. In such cases, you may find a profiling tool provided by the GPU manufacturer helpful.

### Enable the profiler

Before you begin, make sure you're using a device running Android 4.1 (API level 16) or higher, and you[enable developer options](https://developer.android.com/studio/debug/dev-options#enable). To start profiling device GPU rendering while using your app, proceed as follows:

1. On your device, go to**Settings** and tap**Developer Options**.
2. In the**Monitoring** section, select**Profile GPU Rendering** or**Profile HWUI rendering**, depending on the version of Android running on the device.
3. In the Profile GPU Rendering dialog, choose**On screen as bars**to overlay the graphs on the screen of your device.
4. Open the app that you want to profile.

### Inspect the output

In the enlarged image of the Profile GPU Rendering graph shown in figure 1, you can see the colored section, as displayed on Android 6.0 (API level 23).

![](https://developer.android.com/static/images/tools/performance/profile-gpu-rendering/gettingstarted_image003.png)

**Figure 1.**Enlarged Profile GPU Rendering graph.

<br />

The following are a few things to note about the output:

- For each visible application, the tool displays a graph.
- Each vertical bar along the horizontal axis represents a frame, and the height of each vertical bar represents the amount of time the frame took to render (in milliseconds).
- The horizontal green line represents 16.67 milliseconds. To achieve 60 frames per second, the vertical bar for each frame needs to stay below this line. Any time a bar surpasses this line, there may be pauses in the animations.
- The tool highlights frames that exceed the 16.67 millisecond threshold by making the corresponding bar wider and less transparent.
- Each bar has colored components that map to a stage in the rendering pipeline. The number of components vary depending on the API level of the device.

The following table provides descriptions of each segment of a vertical bar in the profiler output when using a device running Android 6.0 and higher.

| Component of Bar |       Rendering Stage       |                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                   |
|------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | Swap Buffers                | Represents the time the CPU is waiting for the GPU to finish its work. If this bar gets tall, it means the app is doing too much work on the GPU.                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                  | Command Issue               | Represents the time spent by Android's 2D renderer issuing commands to OpenGL to draw and redraw display lists. The height of this bar is directly proportional to the sum of the time it takes each display list to execute---more display lists equals a taller red bar.                                                                                                                                                                                                                                                                                                     |
|                  | Sync \& Upload              | Represents the time it takes to upload bitmap information to the GPU. A large segment indicates that the app is taking considerable time loading large amounts of graphics.                                                                                                                                                                                                                                                                                                                                                                                                    |
|                  | Draw                        | Represents the time used to create and update the view's display lists. If this part of the bar is tall, there may be a lot of custom view drawing, or a lot of work in onDraw methods.                                                                                                                                                                                                                                                                                                                                                                                        |
|                  | Measure / Layout            | Represents the amount of time spent on[onLayout](https://developer.android.com/reference/android/view/View#onLayout(boolean, int, int, int, int))and[onMeasure](https://developer.android.com/reference/android/view/View#onMeasure(int, int))callbacks in the view hierarchy. A large segment indicates that the view hierarchy is taking a long time to process.                                                                                                                                                                                                             |
|                  | Input Handling \& Animation | Represents the amount of time it took to evaluate all of the animators that ran for that frame and handle all of the input callbacks. If this segment is large, it could indicate that a custom animator or input callback is spending too much time processing. View binding during scrolling, such as[`RecyclerView.Adapter.onBindViewHolder()`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView.Adapter#onBindViewHolder(VH,%20int)), also typically occur during this segment and are a more common source of slowdowns in this segment. |
|                  | Misc Time / VSync Delay     | Represents the time that the app spends executing operations in between two consecutive frames. It might be an indicator of too much processing happening in the UI thread that could be offloaded to a different thread.                                                                                                                                                                                                                                                                                                                                                      |

**Table 1.**Component bars in Android 6.0 and higher.

Android versions between 4.0 (API level 14) and 5.0 (API level 21) have a blue, purple, red and orange segments. Android versions below 4.0 have only the blue, red, and orange components. The following table shows the component bars in Android 4.0 and 5.0.

| Component of Bar | Rendering Stage |                                                                                                                                Description                                                                                                                                 |
|------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | Process         | Represents the time the CPU is waiting for the GPU to finish its work. If this bar gets tall, it means the app is doing too much work on the GPU.                                                                                                                          |
|                  | Execute         | Represents the time spent by Android's 2D renderer issuing commands to OpenGL to draw and redraw display lists. The height of this bar is directly proportional to the sum of the time it takes each display list to execute---more display lists equals a taller red bar. |
|                  | XFer            | Represents the time it take to upload bitmap information to the GPU. A large segment indicates that the app is taking considerable time loading large amounts of graphics. This segment isn't visible on devices running Android 4.0 or below.                             |
|                  | Update          | Represents the time used to create and update the view's display lists. If this part of the bar is tall, there may be a lot of custom view drawing, or a lot of work in onDraw methods.                                                                                    |

**Table 2.**Component bars in Android 4.0 and 5.0.

For more information about how to interpret information provided by the profiling tool, read[Analyzing with Profile GPU Rendering](https://developer.android.com/topic/performance/rendering/profile-gpu).

**Note:**While this tool is named Profile GPU Rendering, all monitored processes actually occur in the CPU. Rendering happens by submitting commands to the GPU, and the GPU renders the screen asynchronously. In certain situations, the GPU can have too much work to do, and your CPU will have to wait before it can submit new commands. When this happens, you'll see spikes in the orange and red bars, and the command submission will block until more room is made on the GPU command queue.

## Visualize GPU overdraw

Another feature in the developer options helps you identify overdraw by color-coding your UI. Overdraw occurs when your app draws the same pixel more than once within the same frame. So this visualization shows where your app might be doing more rendering work than necessary, which can be a performance problem due to extra GPU effort to render pixels that won't be visible to the user. So, you should[fix overdraw events](https://developer.android.com/topic/performance/rendering/overdraw#fixing)whenever possible.  
If you haven't already done so,[enable developer options](https://developer.android.com/studio/debug/dev-options#enable). Then, to visualize overdraw on your device, proceed as follows:

1. On your device, go to**Settings** and tap**Developer Options**.
2. Scroll down to the**Hardware accelerated rendering** section, and select**Debug GPU Overdraw**.
3. In the**Debug GPU overdraw** dialog, select**Show overdraw areas**.

Android colors UI elements to identify the amount of overdraw as follows:

- **True color:**No overdraw
- ![](https://developer.android.com/static/topic/performance/images/gpu/overdraw-blue.png)**Blue:**Overdrawn 1 time
- ![](https://developer.android.com/static/topic/performance/images/gpu/overdraw-green.png)**Green:**Overdrawn 2 times
- ![](https://developer.android.com/static/topic/performance/images/gpu/overdraw-pink.png)**Pink:**Overdrawn 3 times
- ![](https://developer.android.com/static/topic/performance/images/gpu/overdraw-red.png)**Red:**Overdrawn 4 or more times  
![](https://developer.android.com/static/topic/performance/images/gpu/gpu-overdraw-before_2x.png)

**Figure 2.**An app as it appears normally (left), and as it appears with GPU Overdraw enabled (right)  
Notice that these colors are semi-transparent, so the exact color you see on the screen depends on the content of your UI.

Now that you can recognize where overdraw occurs in your layout, read[how to reduce overdraw](https://developer.android.com/topic/performance/rendering/overdraw).

Remember that some overdraw is unavoidable. As you are tuning your app's user interface, try to arrive at a visualization that shows mostly true colors or only 1X overdraw (blue).  
![](https://developer.android.com/static/topic/performance/images/gpu/gpu-overdraw-after_2x.png)

**Figure 3.**Examples of an app with lots of overdraw (left) and much less overdraw (right)