---
title: https://developer.android.com/topic/performance/rendering/overdraw
url: https://developer.android.com/topic/performance/rendering/overdraw
source: md.txt
---

# Reduce overdraw

This page explains what overdraw is, how to diagnose it, and ways to eliminate or mitigate it.

When an app draws the same pixel more than once within a single frame, this is called*overdraw*. Overdraw is usually unnecessary, and it's best to eliminate it. Overdraw becomes a performance problem when it wastes GPU time to render pixels that don't contribute to what the user sees on the screen.

## About overdraw

Overdraw refers to the system's drawing a pixel on the screen multiple times in a single frame of rendering. For example, if you have a bunch of stacked UI cards, each card hides a portion of the one below it.

However, the system still needs to draw the hidden portions of the cards in the stack. This is because stacked cards are rendered according to the[painter's algorithm](https://en.wikipedia.org/wiki/Painter%27s_algorithm)---that is, in back-to-front order. This sequence of rendering lets the system apply proper alpha blending to translucent objects such as shadows.
| **Note:** Although low-end devices continue to improve in GPU performance, their displays remain at relatively low resolutions. Unless optimizing for a known low-performance GPU device, we recommend instead focusing on optimizing UI thread work to help ensure smooth app performance. In addition to this, OS optimizations avoid overdraw within your app in many cases, such as a`Fragment`background overdrawing the window background.

## Find overdraw problems

The platform offers the following tools to help you determine if overdraw is affecting your app's performance.

### Debug GPU overdraw tool

The Debug GPU Overdraw tool uses color-coding to show the number of times your app draws each pixel on the screen. The higher this count is, the more likely that overdraw affects your app's performance.

For more information, see[Visualize GPU overdraw](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering#debug_overdraw).

### Profile GPU rendering tool

The Profile GPU Rendering tool displays the time each stage of the rendering pipeline takes to display a single frame as a scrolling histogram. The**Process**part of each bar, indicated in orange, shows when the system is swapping buffers. This metric provides important clues about overdraw.

On less performant GPUs, available fill-rate---the speed at which the GPU can fill the frame buffer---can be low. As the number of pixels required to draw a frame increases, the GPU might take longer to process new commands and ask the rest of the system to wait until it can catch up. The**Process** bar shows this spike happens as the GPU gets overwhelmed trying to draw pixels as fast as possible. Issues other than raw numbers of pixels might also cause this metric to spike. For example, if the Debug GPU Overdraw tool shows heavy overdraw and**Process**spikes, there's likely an issue with overdraw.

For more information, see[Profile GPU rendering speed](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering#profile_rendering).
| **Note:** The Profile GPU Rendering tool doesn't work with apps that use the NDK. This is because the system pushes framework messages to the background whenever OpenGL takes a full-screen context. In such cases, you might find a profiling tool provided by the GPU manufacturer helpful.

## Fix overdraw

You can do the following to reduce or eliminate overdraw:

- Remove unnecessary backgrounds in layouts.
- Flatten the view hierarchy.
- Reduce transparency.

This section provides information about each of these approaches.

### Remove unnecessary backgrounds in layouts

By default, a layout doesn't have a background, which means it doesn't render anything directly by itself. However, when layouts do have backgrounds, they might contribute to overdraw.

You can improve rendering performance by removing unnecessary backgrounds. An unnecessary background might not be visible because it's completely covered by everything the app is drawing on top of it. For example, the system might completely cover a parent's background when it draws child views on top of it.

To find out why you're overdrawing, look at the hierarchy in the[Layout Inspector](https://developer.android.com/studio/debug/layout-inspector)tool. You can look for backgrounds that aren't visible to the user and eliminate them. You can eliminate unnecessary backgrounds wherever there are many containers that share a common background color. You can set the window background to the main background color of your app and leave all containers above it with no background values defined.

### Flatten the view hierarchy

Modern layouts help you stack and layer views to produce beautiful design. However, doing so can degrade performance by resulting in overdraw, especially in scenarios where each stacked view object is opaque, requiring the drawing of both seen and unseen pixels to the screen.

If you encounter this issue, you might improve performance by optimizing your view hierarchy to reduce the number of overlapping UI objects. For more information about how to accomplish this, see[Performance and view hierarchies](https://developer.android.com/topic/performance/optimizing-view-hierarchies).

### Reduce transparency

Rendering transparent pixels on screen, known as*alpha rendering*, is a key contributor to overdraw. Unlike standard overdraw---when the system completely hides existing drawn pixels by drawing opaque pixels on top of them---transparent objects require existing pixels to be drawn first, so that the right blending equation can occur.

Visual effects like transparent animations, fade-outs, and drop shadows involve some transparency, and can therefore contribute significantly to overdraw. You can improve overdraw in these situations by reducing the number of transparent objects you render. For example, you can get gray text by drawing black text in a[`TextView`](https://developer.android.com/reference/android/widget/TextView)with a translucent alpha value set on it. However, you can get the same effect with better performance by drawing the text in gray.

To learn more about performance costs that transparency imposes throughout the entire drawing pipeline, watch the video[Hidden Costs of Transparency](https://www.youtube.com/watch?v=wIy8g8yNhNk&index=46&list=PLWz5rJ2EKKc9CBxr3BVjPTPoDPLdPIFCE).