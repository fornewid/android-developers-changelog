---
title: Take screenshots  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/run/emulator-take-screenshots
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Take screenshots Stay organized with collections Save and categorize content based on your preferences.



To take a screenshot of the Android Emulator, click the **Take screenshot**
![Take Screenshot icon](/static/images/tools/e-itakescreenshot.png) button.

In the **Take Screenshot** dialog that appears, you can recapture, edit, or copy
the captured image. Once you're satisfied with the image, click **Save**. The
emulator creates a PNG file with the name
`Screenshot_yyyymmdd-hhmmss.png`, using the year, month,
day, hour, minute, and second of the capture. You can change the name, if you
prefer, and choose where to save the file.

To take a
[Play-compatible screenshot of a Wear OS emulator](/docs/quality-guidelines/wear-app-quality#google-play-screenshots-apps),
set the drop-down to **Play Store Compatible**.

![Take screenshot dialog including Play Store Compatible drop-down.](/static/studio/images/wear-screenshot-play-compatible-dark.png)

You can also take screenshots from the command line with either of the following
commands:

* `screenrecord screenshot [destination-directory]`
* `adb emu screenrecord screenshot [destination-directory]`