---
title: https://developer.android.com/studio/run/emulator-take-screenshots
url: https://developer.android.com/studio/run/emulator-take-screenshots
source: md.txt
---

> Documentation index: https://developer.android.com/studio/run/llms.txt

To take a screenshot of the Android Emulator, click the **Take screenshot**
![](https://developer.android.com/static/images/tools/e-itakescreenshot.png) button.

In the **Take Screenshot** dialog that appears, you can recapture, edit, or copy
the captured image. Once you're satisfied with the image, click **Save** . The
emulator creates a PNG file with the name
`Screenshot_yyyymmdd-hhmmss.png`, using the year, month,
day, hour, minute, and second of the capture. You can change the name, if you
prefer, and choose where to save the file.

To take a [Play-compatible screenshot of a Wear OS emulator](https://developer.android.com/docs/quality-guidelines/wear-app-quality.md.txt#google-play-screenshots-apps),
set the drop-down to **Play Store Compatible**.
![The Take Screenshot dialog with Play Store Compatible selected in the drop-down menu.](https://developer.android.com/static/studio/images/wear-screenshot-play-compatible-dark.png) **Figure 1.** Select **Play Store Compatible** in the **Take Screenshot** dialog.

To capture foldable screenshots that meet [Google Play Store aspect ratio
specifications](https://support.google.com/googleplay/android-developer/answer/9866151#screenshots), use the preconfigured **Foldable (1:1 inner
display)** and **Foldable (4:3 inner display)** AVD profiles in Device Manager
to capture both the unfolded inner display (1:1 and 4:3) and the folded
outer display (10:16, 16:10, 9:16, and 16:9). For an end-to-end
command-line workflow across phone, foldable, tablet, and desktop emulators, see
[Capture app screenshots for Google Play](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt).

You can also take screenshots from the command line with any of the following
commands:

- [`android screen capture`](https://developer.android.com/tools/agents/android-cli/commands/screen_capture.md.txt)
- `screenrecord screenshot [destination-directory]`
- `adb emu screenrecord screenshot [destination-directory]`