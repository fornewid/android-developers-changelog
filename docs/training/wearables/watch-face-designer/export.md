---
title: https://developer.android.com/training/wearables/watch-face-designer/export
url: https://developer.android.com/training/wearables/watch-face-designer/export
source: md.txt
---

Watch Face Designer offers several options for seeing your watch face creation
come to life on a physical watch or using the [Android emulator](https://developer.android.com/studio/run/emulator).

## Google Play

| **Note:** This is the recommended exporting method for designers who create watch faces on Wear OS.

Google Play publishes files that use the `.aab` ([Android App Bundle](https://developer.android.com/guide/app-bundle))
format. Watch Face Designer handles everything about packaging your watch face
into a bundle for you.

To publish to Play, follow [Google Play publishing instructions](https://developer.android.com/training/wearables/watch-face-designer/publish).

## Android Studio

| **Note:** This is the recommended exporting method for developers who create watch faces on Wear OS.

Android Studio export saves a ZIP file that you can extract and use as an
Android Studio project directory. It comes preconfigured with Gradle scripts and
all the necessary resources to directly edit your generated watch face as code.
By editing your watch face in Android Studio, you can implement [more advanced
features of the Watch Face Format](https://developer.android.com/reference/wear-os/wff/watch-face), including ones that aren't supported in
Watch Face Designer.

## Other methods

Watch Face Designer supports several other exporting methods, as well.

### One-click deploy

| **Note:** This option is available only on macOS development machines. If you're developing on a Windows, Linux, or ChromeOS machine, use [APK exports](https://developer.android.com/training/wearables/watch-face-designer/export#apk) instead.

To export using one-click deploy, complete the following steps:

1. Connect your Wear OS device to your computer over USB.

   On Pixel Watch 2 and Pixel Watch 3 devices, you can do this using the
   included charging cable.

   For devices that don't support direct USB connections, such as
   Pixel Watch (1), see [Wirelessly debugging a Wear OS app](https://developer.android.com/training/wearables/get-started/debugging#wifi-debugging).

   See the manufacturer's advice for other watches.
2. Press **Export** in Watch Face Designer, then select **One-click deploy**,
   which prompts you to save a file.

3. Double-click on that file to open it, and select the **Play** button:

   ![Play button appears near the top right corner](https://developer.android.com/static/wear/images/design/watch-face-designer/one-click-deploy.png) **Figure 1**: The deployed file open, ready for exporting

   The watch face is deployed to the watch and set as the current watch face
   favorite.
   | **Note:** You may need to accept a permissions dialog. If you press **Always Allow**, you don't have to do this again in future.

### APK

An APK is an installable Android package. Watch Face Designer handles everything
about packaging and preparing your APK for you.

To deploy your APK, do the following:

1. Install [ADB](https://developer.android.com/tools/adb).
2. Connect your watch over USB or [over Wi-Fi](https://developer.android.com/training/wearables/get-started/debugging#wifi-pair).
3. Use the [`adb install`](https://developer.android.com/tools/adb#move) command.

### Raw resources

This export option saves your watch face as an uncompiled Android package, with
an `AndroidManifest.xml` and `res/` folder containing your watch face's code and
resources.

You can use this package with a tool like [AAPT2](https://developer.android.com/tools/aapt2) to customize how APKs and
AABs are generated. This is useful if you need more fine-grained tuning options
around features like signing keys and certificates.

### Watch Face Studio (experimental)

This option creates a project for use in [Watch Face Studio](https://developer.samsung.com/watch-face-studio/overview.html).
| **Note:** Some features from Figma might not appear as expected in Watch Face Studio.