---
title: https://developer.android.com/games/playgames/faq
url: https://developer.android.com/games/playgames/faq
source: md.txt
---

This topic answers common questions about developing for
Google Play Games on PC.

## Q: Is there a size limit for an Google Play Games on PC upload?

A: For the app bundle format, the limit is 150MB base + 2GB
[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery). If this
isn't sufficient, reach out to your Google Play point of contact.

## Q: What if HPE fails to start

![A screenshot of a "Google HPE Error" dialog box that says "Unable to start
Google HPE as initialization failed."](https://developer.android.com/static/images/games/playgames/faq-hpe-failed-to-start.png)

A: There are a few quick debugging steps you can try:

1. Make sure Windows has been updated the May 2020 patch or later.
2. Make sure that you have not moved HPE, it must be on the \`C:\` drive.
3. Reach out to your Google Play point of contact. You should send all available log files as well to ensure a speedy fix.

## Q: How do I setup my tester track properly?

A: See the
[Android development](https://developer.android.com/games/playgames/publish-deploy#users-tracks)
guide.

## Q: My game only supports 32bit x86 builds rather than x86-64; can I still comply with Play's 64bit requirements?

A: No.

In order to achieve
[full certification](https://developer.android.com/games/playgames/checklist#optimized-requirements),
a game must ship a 64 bit executable. 64 bit games tend to be more stable
and lead to a better player experience.

If it is technically infeasible for your game to ship a 64 bit version, such as
the lack of game engine support for x86-64, a game may be considered
"playable". It can not achieve full certification in this case.

## Q: How do I collect the log files?

A: The log files are stored in
``%LocalAppData%\Google\Play Games Developer Emulator\Logs\` and all end with
the file extension``.log`. Normally, this path expands to`C:\\Users\<username\>\\AppData\\Local\\Google\\Play Games Developer Emulator\\Logs\`,
although it may vary on your system. If you'd like to quickly gather all the log
files and archive them to send to your Google Play point of contact, you can use
this PowerShell command:

    Compress-Archive -Path "$env:LocalAppData\Google\Play Games Developer Emulator\Logs\" -DestinationPath HpeLogs.zip

## Q: How can I reconnect to the emulator if it disappears from `adb devices`?

A: The emulator connects over localhost port 6520. You can run this command to
reconnect:

    adb connect localhost:6520

## Q: What is Package visibility filtering and why do I need to add a `<queries>` tag?

[Package visibility](https://developer.android.com/training/package-visibility)
applies to any game or application targeting Android 11 (API level 30). In many
cases, developers' Google Play Games on PC builds are their first experience interacting
with the package visibility rules. With the new system, developers must
explicitly
[declare](https://developer.android.com/training/package-visibility/declaring)
the packages that they intend to interact with unless it is an
[automatically visible](https://developer.android.com/training/package-visibility/automatic)
package.

## Q: How do I resolve the error **requires the Google Play Store, but it is missing**, or why do features like billing work when I install the game from the Play Store but not when I sideload my game?

The new [package visibility](https://developer.android.com/games/playgames/faq#package_visibility) rules may block your game
from accessing Play Services if it's not installed from the Play Store. You can
resolve this by adding a query to the package `"com.android.vending"` in your
`AndroidManifest.xml` file:

    <manifest>
        <queries>
            <package android:name="com.android.vending" />
        </queries>
    </manifest>

## Q: Do I need to implement [window resizing](https://developer.android.com/topic/arc/window-management#resizing_windows) for Google Play Games on PC?

No.

## Q: Can I change the mouse mode between raw input and touchscreen emulation in the Google Play Games on PC emulator?

A: To switch between simulated touch screen mode and "raw" mouse inputs, you can use the context menu on the HPE_Dev taskbar icon:

![A screenshot of the Windows 11 taskbar. The carrot image is selected to show hidden icons, and a red square is shown around the](https://developer.android.com/static/images/games/playgames/faq-taskbar-icon.png)

Right click, select "Developer Options", and choose the input mode you'd like to simulate under "Mouse Input Mode".

![A screenshot showing the context menu expanded on the HPE_Dev taskbar icon. The menu option](https://developer.android.com/static/images/games/playgames/faq-touchscreen-relative.png)

In the player experience, declaring that your game uses the feature `android.hardware.type.pc` will automatically switch like it [currently does on ChromeOS](https://developer.android.com/guide/topics/large-screens/input-compatibility-large-screens#input_translation_mode).

    <uses-feature
        android:name="android.hardware.type.pc"
        android:required="false" />

## Q: Why does Play Games Services v2 auto sign-in fail on a mobile device?

A: At the moment there're two dependencies for Play Games Services v2
Sign-in to work on a device: **GMS Core** and **Play Games App**.

1. The **GMS Core** version must be later than 21.30.xx. To check the version,
   use this command:

       adb shell dumpsys package com.google.android.gms | grep -i -e "versionCode" -e "versionName"
       versionCode=213016046 minSdk=30 targetSdk=31
       versionName=21.30.16 (150400-391784508)
       versionCode=202117048 minSdk=30 targetSdk=30
       versionName=20.21.17 (150408-316502805)

   The first `versionName` is the version to check. The GMS Core update should be
   automatically pushed onto an Android device. Please inform us if it hasn't.
2. The Google Play Games app version must be 2021.08.29094 and above. You can
   check this by going to **Settings \> Apps**, selecting the Play Games App,
   then finding the version number at the bottom of the details page.

   Please note that you no longer need to sideload the Play Games app to test
   Play Games Services v2 - the necessary version should be available
   now on user devices.

## Q: Can I use [frame pacing](https://developer.android.com/games/sdk/frame-pacing) in Google Play Games on PC (or "Why does my Unity game crash on launch")?

A: The [frame pacing](https://developer.android.com/games/sdk/frame-pacing) library is supported in Google Play Games on PC, but the version included with the Unity game currently causes a crash on launch. If you're using the Unity game engine, look for the "Optimize Frame Pacing" build option and ensure that it's disabled.

![A screenshot of the](https://developer.android.com/static/images/games/playgames/faq-optimize-frame-pacing.png)

> [!NOTE]
> **Note:** This feature is well supported on phones, and you may want to leave it enabled if you make your ARM build independently. There is no easy way to toggle this feature in Unity procedurally.

## Q: Is it possible to allow players to upload locally stored images from Google Play Games on PC?

A: The emulator currently doesn't have a meaningful local filesystem abstraction
for choosing or aggregating images stored on a player's PC. If you currently use
[`Intent.ACTION_PICK`](https://developer.android.com/reference/android/content/Intent#ACTION_PICK)
mixed with
[`MediaStore.Images.Media`](https://developer.android.com/reference/android/provider/MediaStore.Images.Media),
you should remove this code in Google Play Games on PC builds for now.

## Q: Can you run multiple instance of the emulator, or multiple games in the emulator at once?

A: The emulator only supports running one emulator instance, and only supports
running one game at a time. The emulator also does not support running multiple
instances of the same game.

## Q: Can we use push notifications for Google Play Games?

A: Because Google Play Games uses an emulator, push notifications have limited
support.

## Q: Can we use in-game ads with Google Play Games on PC?

A: Yes. Please contact your ad network to confirm that they support
Google Play Games on PC. If you are an ad network, please see this
[Developer's Guide](https://developer.android.com/games/playgames/ad-guidance) for more information on how
to best support Google Play Games on PC.

## Q: How do we support Google Play Games on PC as an ad network?

A: Please see this [Developer's Guide](https://developer.android.com/games/playgames/ad-guidance) for how ad
networks can best support Google Play Games on PC.

## Q: How do I analyze Google Play Games on PC data in Google Play Console?

A: You can find out reporting of Google Play Games on PC in Statistic, Android
Vitals, and Reach \& devices. Filter with the **Form factor** and select **Google
Play Games on PC** to see the data on the platform.