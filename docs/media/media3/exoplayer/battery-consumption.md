---
title: https://developer.android.com/media/media3/exoplayer/battery-consumption
url: https://developer.android.com/media/media3/exoplayer/battery-consumption
source: md.txt
---

# Battery consumption

## How important is battery consumption due to media playback?

Avoiding unnecessary battery consumption is an important aspect of developing a performant Android app. Media playback can be a major cause of battery drain, however its importance for a particular app heavily depends on its usage patterns. If an app is only used to play small amounts of media each day, then the corresponding battery consumption will only be a small percentage of the total consumption of the device. In such cases, it makes sense to prioritize feature set and reliability over optimizing for battery when selecting which player to use. On the other hand, if an app is often used to play large amounts of media each day, then optimizing for battery consumption should be weighted more heavily when choosing between a number of viable options.

## How power efficient is ExoPlayer?

The diverse nature of the Android device and media content ecosystems means that it's difficult to make widely applicable statements about ExoPlayer's battery consumption. Performance varies by hardware, Android version, and the media being played. Hence the following information should be treated as guidance only.

### Video playback

For video playback, the display and decoding of the video stream account for most of the power consumed during playback.

Choosing between`SurfaceView`and`TextureView`for output can have a significant impact on power consumption.`SurfaceView`is more power efficient, with`TextureView`increasing total power draw during video playback by as much as 30% on some devices.`SurfaceView`should therefore be preferred where possible. Read more about choosing between`SurfaceView`and`TextureView`[on the Surface page](https://developer.android.com/media/media3/ui/surface).

On some TVs, using[video tunneling](https://developer.android.com/media/media3/exoplayer/track-selection#tunneling)may provide a more efficient path for high-resolution video playback where the regular playback path is not performant enough for smooth playback.
| **Note:** Tunneling moves all video decoding and release timing to a dedicated hardware processor. However, be aware that the implementation is device-specific. Performance and reliability can vary greatly between devices. It's highly advisable to test your media streams on the specific TV devices where you intend to enable tunneling to verify it is reliable enough for your use case.

### Audio playback

For short audio playbacks or playbacks when the screen is on, audio does not have a significant impact on power.

For long playbacks with the screen off, it's possible to save power by using ExoPlayer's audio offload mode. See the[`track selection guide`](https://developer.android.com/media/media3/exoplayer/track-selection#audioOffload)for more details on how to enable it.
| **Note:** Audio offload allows audio processing to be offloaded from the CPU to a dedicated signal processor. Device and format support varies, so it's advisable to thoroughly test audio offload with your media on your target devices. Offload also limits the ability to apply audio effects, like speed changes and silence skipping.