---
title: https://developer.android.com/studio/run/emulator-record-screen
url: https://developer.android.com/studio/run/emulator-record-screen
source: md.txt
---

# Record the screen

You can record video and audio from the Android Emulator and save the recording to a WebM or animated GIF file.

The screen recording controls are in the**Record and Playback** tab of the[**Extended Controls**](https://developer.android.com/studio/run/emulator-extended-controls)window.

**Tip:** You can open the screen recording controls by pressing<kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>(<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>on macOS).

- To begin screen recording, click the**Start recording** button in the**Record and Playback**tab.
- To stop recording, click**Stop recording**.

To save the recorded video:

1. Controls for playing and saving the recorded video are at the bottom of the**Record and Playback**tab.
2. Choose**WebM** or**GIF**from the menu at the bottom of the tab.
3. Click**Save**.

You can also record and save a screen recording from the emulator using the following command on the command line:

`adb emu screenrecord start --time-limit 10 `<var translate="no">[path to save video]</var>`/sample_video.webm`