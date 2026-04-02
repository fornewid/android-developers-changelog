---
title: Test your game on ChromeOS devices  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/pg-chromeos
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Test your game on ChromeOS devices Stay organized with collections Save and categorize content based on your preferences.




This page describes how to run your game on a
[ChromeOS device that supports Android](https://www.chromium.org/chromium-os/chrome-os-systems-supporting-android-apps/)
for testing purposes. You can use ChromeOS as an alternate testing plarform for
Google Play Games on PC if you don't have access to the
[developer emulator](/games/playgames/emulator).

If you have access to the
[developer emulator](/games/playgames/emulator), we recommend you use it to
test your game because it is the closest environment to
Google Play Games on PC.

## Load and run your game

You can use [Android Debug Bridge (adb)](/studio/command-line/adb) to load
APK files to your ChromeOS devices. If you haven't already done so,
we recommend that you install one of the following
tools, which include the latest version of adb:

* [Android Studio](/studio)
* [Android SDK Platform tools](/studio/releases/platform-tools#downloads)

You also need to [enable ADB connection on your ChromeOS devices](https://support.google.com/chromebook/answer/9770692?ref_topic=3415446).

You can run your app directly from Android Studio, or use the `adb install`
command to deploy your APK file to ChromeOS devices. If your game uses an
Android App Bundle, use [`bundletool install-apks`](/studio/command-line/bundletool#deploy_with_bundletool) to deploy the files.

```
    adb install C:\yourpath\yourgame.apk
```

## Detect the platform

If you need to toggle gameplay features based on device type, look for the
`"org.chromium.arc"` system feature to detect ChromeOS devices:

### Kotlin

```
var isPC = packageManager.hasSystemFeature("org.chromium.arc")
```

### Java

```
PackageManager pm = getPackageManager();
boolean isPC = pm.hasSystemFeature("org.chromium.arc")
```

### C#

```
var unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
var currentActivity = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
var packageManager = currentActivity.Call<AndroidJavaObject>("getPackageManager");
var isPC = packageManager.Call<bool>("hasSystemFeature", "org.chromium.arc");
```






Send feedback