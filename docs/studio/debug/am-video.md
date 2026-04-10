---
title: https://developer.android.com/studio/debug/am-video
url: https://developer.android.com/studio/debug/am-video
source: md.txt
---

# Record a video

![Device Video](https://developer.android.com/static/images/tools/am-video.jpg)

**Figure 1.**Record a video of your app.

[Logcat](https://developer.android.com/studio/debug/am-logcat)lets you record an MP4 video from your device, such as for marketing materials or for debugging. Videos are a maximum of three minutes long, and audio is not recorded with the video file.

To record a video of your app, do the following:

1. Open an app project.
2. [Run the app](https://developer.android.com/studio/run#RunningApp)on a device.
3. Click**View \> Tool Windows \> Logcat**.
4. Interact with the display on the device to stage the start of the video.
5. Click**Screen Record** ![](https://developer.android.com/static/images/tools/am-ivideo.png)in the left side of the Logcat window.
6. In the**Screen Recorder Options**dialog, set the recording options:
   - **Bit Rate:**Enter a bit rate. The default is 4 Mbps.
   - **Resolution:**Enter a width and height value in pixels. The value must be a multiple of 16. The default is the resolution of the device.
   - **Show Taps:**Enable visual feedback for taps.
7. Click**Start Recording**to start the recording.
8. Click**Stop Recording**to stop the recording.
9. In the**Save As**dialog, save the MP4 file.
10. In the**Screen Recorder**dialog, click one of the buttons to show the file location, open the recording in a player, or dismiss the dialog.

## Record video with the emulator

If you are using an emulator, you can record video directly from the**Record and Playback** tab in**Extended Controls**. Once you have recorded a video, you can save it as either WEBM or GIF format:
![](https://developer.android.com/static/studio/images/debug/video-emulator_2x.png)**Figure 2.**Record a video using an emulator.