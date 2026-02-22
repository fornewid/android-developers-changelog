---
title: https://developer.android.com/training/wearables/watch-faces/hardware-acceleration
url: https://developer.android.com/training/wearables/watch-faces/hardware-acceleration
source: md.txt
---

# Improve your watch face performance with hardware acceleration

Wear OS apps that use standard views benefit from automatic hardware-accelerated
graphics rendering. But watch faces are usually implemented using
canvases, so they don't automatically get hardware acceleration.

## Why use a hardware-accelerated canvas for your watch face?

In most cases, your watch face renders at a higher frame rate when using a
hardware-accelerated canvas. At higher frame rates, animations and transitions
appear smoother to the eye, providing a better user experience.

When you use a hardware-accelerated canvas, you can also access more UI
performance data about your watch face. For example, you can only access the
detailed frame information described in [Measure UI
performance](https://developer.android.com/topic/performance/overview)
when you are using a hardware-accelerated canvas.

## Is my watch face using hardware acceleration?

You can check whether your watch face is using hardware acceleration
using either the developer options or `adb`.

### Check using developer options

To use developer options to check whether your watch face is using hardware acceleration,
follow these steps:

1. On a Wear OS device, navigate to **Settings** \> **Developer options**.
2. Enable **Debug GPU profiling**.

   This option draws an overlay on top of visible surfaces, one on each surface,
   to show the amount of time spent in each stage of GPU rendering for that
   surface.
3. On the device, navigate back to your watch face.

4. If your watch face uses a hardware-accelerated canvas, you see a new bar
   that moves from right to left for each rendered frame of your watch face.

### Check using adb

To use `adb` to check whether your watch face is using hardware acceleration,
follow these steps:

1. On a Wear OS device, change the watch face to your watch face that you want to test.
2. Let the watch face run for a few seconds in interactive mode.
3. Run the following `adb` command to check whether your watch face is using
   hardware acceleration:

   `adb shell dumpsys gfxinfo `<var translate="no">[package-name]</var>

After running the command, you get output similar to the following
example:  

```
Applications Graphics Acceleration Info:
Uptime: 2239933 Realtime: 13568751

** Graphics info for pid 1100 [package-name] **

Stats since: 59875589194ns
Total frames rendered: 1213
Janky frames: 0 (0.00%)
50th percentile: 7ms
90th percentile: 18ms
95th percentile: 25ms
99th percentile: 150ms
Number Missed Vsync: 0
Number High input latency: 0
Number Slow UI thread: 0
Number Slow bitmap uploads: 0
Number Slow issue draw commands: 0
Number Frame deadline missed: 0

...
```

In this sample output, notice the line reading `Total frames rendered`.
Generally, if your output shows total frames rendered greater than 0, then your
watch face uses an accelerated canvas. Otherwise the total frames rendered
and other frame data in the report is normally 0.

However, because the `gfxinfo` is output for your app's full package, you might
see some frame time information from something other than a hardware-accelerated
canvas, such as an `Activity` that your app uses for a configuration screen. To
tell the difference, make sure that your watch face is the only surface that is
visible and then rerun the `adb shell dumpsys gfxinfo` command to check whether
the value for `Total frames rendered` increases.

## Best practices

Follow these best practices to ensure the best possible experience for your
users.

### Maximize battery life

If your watch face has long-running animations, using hardware acceleration can
greatly lower the battery life of a device. This problem can get worse if
your watch face tries to draw in every frame. To avoid negatively impacting your
users, don't use long-running animations in your watch face. This
guideline is not specific to using hardware acceleration, but because using
hardware acceleration increases the number of frames you're able to draw, it is
even more important to follow. For more information, see [Best practices for
animations](https://developer.android.com/training/wearables/watch-faces/performance#Animations).

### Use supported drawing operations

Some drawing operations are are not supported when using hardware acceleration.
For information on what is supported, see [Hardware
acceleration](https://developer.android.com/topic/performance/hardware-accel#drawing-support).
If you have a small code path that uses an unsupported operation, you can create
a bitmap-backed canvas and then draw that bitmap into the watch face's canvas
using
[`canvas.drawBitmap()`](https://developer.android.com/reference/android/graphics/Canvas#drawBitmap(android.graphics.Bitmap,%20android.graphics.Rect,%20android.graphics.RectF,%20android.graphics.Paint)).

### Maintain compatibility when using hardware acceleration

Hardware acceleration is available on Wear OS devices that run Android 9 (API
level 28) or higher. If you want to avoid a specific draw operation on older
devices, where hardware acceleration is not available, or an unsupported draw
operation on a hardware accelerated canvas, you can check [`Canvas.isHardwareAccelerated()`](https://developer.android.com/reference/android/graphics/Canvas#isHardwareAccelerated()),
then provide the alternative functionality.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [dumpsys](https://developer.android.com/tools/dumpsys)
- [Slow rendering](https://developer.android.com/topic/performance/vitals/render)
- [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode)