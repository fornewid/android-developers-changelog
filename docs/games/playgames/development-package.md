---
title: https://developer.android.com/games/playgames/development-package
url: https://developer.android.com/games/playgames/development-package
source: md.txt
---

Since Google Play Games on PC provides a standard Android runtime environment,
there are no differences between packing your game for mobile or PC outside of
ensuring that you include x86 or x86-64 binaries. When possible, you should use
the same APK or [App Bundle](https://developer.android.com/guide/app-bundle) on PC as you do for mobile
builds.

When using one package across mobile and Google Play Games on PC, it is best to
enable Google Play Games on PC specific features at runtime either by
[detecting the presence of a keyboard](https://developer.android.com/games/develop/all-screens#handle-interaction-models):

<br />

### Kotlin

<br />

    val hasKeyboard = resources.configuration.keyboard == KEYBOARD_QWERTY

<br />

### Java

<br />

    boolean hasKeyboard = getResources().getConfiguration().keyboard == KEYBOARD.QWERTY

<br />

### C#

<br />

    var unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
    var currentActivity = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
    var resources = currentActivity.Call<AndroidJavaObject>("getResources");
    var configuration = resources.Call<AndroidJavaObject>("getConfiguration");
    var keyboard = configuration.Get<int>("keyboard");
    var hasKeyboard == 2; // Configuration.KEYBOARD_QWERTY

<br />

<br />

Or by checking for the `"com.google.android.play.feature.HPE_EXPERIENCE"` system
feature:

### Kotlin

```kotlin
var isPC = packageManager.hasSystemFeature("com.google.android.play.feature.HPE_EXPERIENCE")
  
```

### Java

```java
PackageManager pm = getPackageManager();
boolean isPC = pm.hasSystemFeature("com.google.android.play.feature.HPE_EXPERIENCE")
  
```

### C#

```c#
var unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
var currentActivity = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
var packageManager = currentActivity.Call<AndroidJavaObject>("getPackageManager");
var isPC = packageManager.Call<bool>("hasSystemFeature", "com.google.android.play.feature.HPE_EXPERIENCE");
  
```