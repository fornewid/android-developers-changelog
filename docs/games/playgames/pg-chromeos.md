---
title: https://developer.android.com/games/playgames/pg-chromeos
url: https://developer.android.com/games/playgames/pg-chromeos
source: md.txt
---

This page describes how to run your game on a
[ChromeOS device that supports Android](https://www.chromium.org/chromium-os/chrome-os-systems-supporting-android-apps/)
for testing purposes. You can use ChromeOS as an alternate testing plarform for
Google Play Games on PC if you don't have access to the
[developer emulator](https://developer.android.com/games/playgames/emulator).

If you have access to the
[developer emulator](https://developer.android.com/games/playgames/emulator), we recommend you use it to
test your game because it is the closest environment to
Google Play Games on PC.

## Load and run your game

You can use [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb) to load
APK files to your ChromeOS devices. If you haven't already done so,
we recommend that you install one of the following
tools, which include the latest version of adb:

- [Android Studio](https://developer.android.com/studio)

- [Android SDK Platform tools](https://developer.android.com/studio/releases/platform-tools#downloads)

You also need to [enable ADB connection on your ChromeOS devices](https://support.google.com/chromebook/answer/9770692?ref_topic=3415446).

You can run your app directly from Android Studio, or use the `adb install`
command to deploy your APK file to ChromeOS devices. If your game uses an
Android App Bundle, use [`bundletool install-apks`](https://developer.android.com/studio/command-line/bundletool#deploy_with_bundletool) to deploy the files.

        adb install C:\yourpath\yourgame.apk

## Detect the platform

If you need to toggle gameplay features based on device type, look for the
`"org.chromium.arc"` system feature to detect ChromeOS devices:

### Kotlin

```kotlin
var isPC = packageManager.hasSystemFeature("org.chromium.arc")
  
```

### Java

```java
PackageManager pm = getPackageManager();
boolean isPC = pm.hasSystemFeature("org.chromium.arc")
  
```

### C#

```c#
var unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
var currentActivity = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
var packageManager = currentActivity.Call<AndroidJavaObject>("getPackageManager");
var isPC = packageManager.Call<bool>("hasSystemFeature", "org.chromium.arc");
  
```