---
title: https://developer.android.com/studio/run/emulator-take-screenshots
url: https://developer.android.com/studio/run/emulator-take-screenshots
source: md.txt
---

# Take screenshots

To take a screenshot of the Android Emulator, click the**Take screenshot** ![Take Screenshot icon](https://developer.android.com/static/images/tools/e-itakescreenshot.png)button.

In the**Take Screenshot** dialog that appears, you can recapture, edit, or copy the captured image. Once you're satisfied with the image, click**Save** . The emulator creates a PNG file with the name`Screenshot_`<var translate="no">yyyymmdd-hhmmss</var>`.png`, using the year, month, day, hour, minute, and second of the capture. You can change the name, if you prefer, and choose where to save the file.

To take a[Play-compatible screenshot of a Wear OS emulator](https://developer.android.com/docs/quality-guidelines/wear-app-quality#google-play-screenshots-apps), set the drop-down to**Play Store Compatible**.

![Take screenshot dialog including Play Store Compatible drop-down.](https://developer.android.com/static/studio/images/wear-screenshot-play-compatible-dark.png)

You can also take screenshots from the command line with either of the following commands:

- `screenrecord screenshot `<var translate="no">[destination-directory]</var>
- `adb emu screenrecord screenshot `<var translate="no">[destination-directory]</var>