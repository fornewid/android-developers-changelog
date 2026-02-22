---
title: https://developer.android.com/develop/devices/chromeos/learn/animation
url: https://developer.android.com/develop/devices/chromeos/learn/animation
source: md.txt
---

One of the most difficult problems for app developers is creating smooth,
glitch-free animation. This can be especially hard to debug when the system is
also performing resource-intensive background tasks. It can be difficult to
determine whether a glitch is caused by your app or the system. However, a
profiler tool can help you identify the possible source of the bad behavior.

## Render on ChromeOS

A fine-tuned app, like a game, usually uses double buffering to keep the user
response time as low as possible. Still, many things can degrade
performance. For example, if rendering a frame takes too long, the rendered
result is not ready for the next buffer swap, and the previous frame repeats.

Then, the renderer can't start rendering the next frame, causing even more
problems. This scenario is familiar to Android mobile developers. When an app
runs on ChromeOS, the context is even more complicated.

An app running on the desktop doesn't render directly to the screen's display
frame. It renders its data into a texture instead. There are usually multiple
apps, each rendering its graphics into a texture. The system constructs the view
on the screen using a compositor to combine all the textures into a single
desktop image.

The compositor works transparently in the background, but it introduces a
one-frame time delay to maximize the use of the GPU pipeline. This delay
smooths system performance fluctuations and helps balance an asymmetrical load.

When the OS is working hard, the GPU can be squeezed, causing a delay between
when a frame renders and when it appears on screen. The system might use
quadruple buffering to compensate, depending on the hardware. Even with deeper
buffering, the graphic pipeline can still glitch.

## The ARC graphics tracer

ChromeOS has a profiling tool that shows how the buffers are percolating
through the system, when memory swaps occur, how busy the CPU/GPU is, and what
your application is doing at a given time, shown in the following image:
![The ARC graphics tracer UI, showing timelines for system processes.](https://developer.android.com/static/chrome-os/images/jank-profiler.svg) **Figure 1.** The ARC graphics tracer UI, showing timelines for system processes.

### Set up the profiler

To use the profiler, you must run M75 or later.
For best results, use an Intel device.

Before using the profiler, seed your app with traces.
Add `Trace.traceCounter(Trace.TRACE_TAG_GRAPHICS, "Event", <number>);` to your code
wherever you'd like to include a trace. Use an `Event` that begins with
the prefix `customTrace`. The prefix doesn't appear in the trace message.

To set up the profiler, follow these steps:

1. Turn on developer mode.
2. Turn on Chrome settings and enable the **ARC graphic buffers visualization
   tool**.
3. Navigate to `chrome://arc-graphics-tracing`.

### Run the profiler

1. Select **stop on glitch**.
2. Run the Android app.
3. When the Android app is active and has focus, press `Control`+`Shift`+`G`.

When a glitch happens, a browser window pops up.
Use the <kbd>W</kbd> and <kbd>S</kbd> keys to zoom and shrink the timeline.