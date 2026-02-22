---
title: https://developer.android.com/topic/google-play-instant/getting-started/game-unity-plugin
url: https://developer.android.com/topic/google-play-instant/getting-started/game-unity-plugin
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

The Google Play Instant plugin for Unity configures your Unity project to create an instant app version of your game. This guide describes how to install and use this plugin.

## Download and import the plugin

The plugin is part of the Google Play Plugins for Unity. To import the plugin, follow these steps:

1. Download the latest release from[Google Play Plugins for Unity releases](https://github.com/google/play-unity-plugins/releases).
2. Import the`.unitypackage`file by selecting the Unity IDE menu option**Assets \> Import package \> Custom Package**and importing all items.

## Unity Editor features

Import the plugin to add a**Google \> Play Instant**submenu in Unity. This submenu provides the following options.

### Build Settings

Opens a window that enables switching between**Installed** and**Instant** development modes. Switching to**Instant**performs the following changes:

- Creates a Scripting Define Symbol called`PLAY_INSTANT`that can be used for scripting with`#if PLAY_INSTANT`and`#endif`.
- Manages updates to the AndroidManifest.xml for certain required changes such as[**android:targetSandboxVersion**](https://developer.android.com/guide/topics/manifest/manifest-element#targetSandboxVersion).

### Player Settings

The**Player Settings**dialog, shown in Figure 1, displays suggestions to help you optimize support for Google Play Instant, develop against more compatible graphics APIs, and reduce your APK's size.
![Specific suggestions include using OpenGL ES 2.0 only and disabling Multithreaded Rendering.](https://developer.android.com/static/topic/google-play-instant/images/unity-plugin-player-settings.png)**Figure 1.** The**Player Settings**dialog

These Player Settings are divided into**Required** and**Recommended** settings. If a setting has a corresponding**Update**button, click it to change the setting to the preferred value.

To further reduce the APK size, open the Unity Package Manager and remove any unused packages.

### Quick Deploy

Quick Deploy can reduce the size of a Unity-based instant app by packaging some assets in an[AssetBundle](https://docs.unity3d.com/Manual/AssetBundlesIntro.html). When using Quick Deploy, the Unity game engine and a loading screen are packaged into an instant app APK, and after the instant app starts it retrieves the AssetBundle from a server.

## Support installation workflows

The goal of many instant apps is to give users a chance to experience the app before installing the full version. The Google Play Instant plugin for Unity provides APIs for displaying a Play Store install dialog and for transferring state from instant to installed app.

### Show an install prompt

An instant app with an**Install**button can display a Play Store install dialog by calling the following from an install button click handler:  

    Google.Play.Instant.InstallLauncher.ShowInstallPrompt();

The`ShowInstallPrompt()`method has an overload that allows for one or more of the following:

- Determining if the user cancels out of the installation process. Override`onActivityResult()`in the instant app's main activity and check for`RESULT_CANCELED`on the specified`requestCode`.
- Passing an install referrer string via the`referrer`parameter.
- Passing state about the current game session via`PutPostInstallIntentStringExtra()`.

These are demonstrated in the following example:  

    using Google.Play.Instant;
    ...
    const int requestCode = 123;
    var sessionInfo = /* Object serialized as a string representing player's current location, etc. */;
    using (var activity = UnityPlayerHelper.GetCurrentActivity())
    using (var postInstallIntent = InstallLauncher.CreatePostInstallIntent(activity))
    {
        InstallLauncher.PutPostInstallIntentStringExtra(postInstallIntent, "sessionInfo", sessionInfo);
        InstallLauncher.ShowInstallPrompt(activity, requestCode, postInstallIntent, "test-referrer");
    }

If the user completes app installation, the Play Store will re-launch the app using the provided`postInstallIntent`. The installed app can retrieve a value set in the`postInstallIntent`using the following:  

    var sessionInfo = InstallLauncher.GetPostInstallIntentStringExtra("sessionInfo");

**Notes:**

- The extras included in the`postInstallIntent`may not reach the installed app if the user installs the app but cancels the post-install launch. Passing intent extras is better suited for retaining active session state than it is for retaining persistent state; for the latter refer to the Cookie API.
- Anyone can construct an intent with extra fields to launch the installed app, so if the payload grants something of value, design the payload so that it can only be used once, cryptographically sign it, and verify the signature on a server.

### Use the Cookie API

The Cookie API provides methods for passing a cookie (e.g. player ID or level completion data) from an instant app to its corresponding installed app. Unlike`postInstallIntent`extras, the cookie state is available even if the user doesn't immediately launch the installed app. For example, an instant app could call the following code from an install button click handler:  

    using Google.Play.Instant;
    ...
    var playerInfo = /* Object serialized as a string representing game levels completed, etc. */;
    var cookieBytes = System.Text.Encoding.UTF8.GetBytes(playerInfo);
    try
    {
        var maxCookieSize = CookieApi.GetInstantAppCookieMaxSize();
        if (cookieBytes.Length > maxCookieSize)
        {
            UnityEngine.Debug.LogErrorFormat("Cookie length {0} exceeds limit {1}.", cookieBytes.Length, maxCookieSize);
        }
        else if (CookieApi.SetInstantAppCookie(cookieBytes))
        {
            UnityEngine.Debug.Log("Successfully set cookie. Now display the app install dialog...");
            InstallLauncher.ShowInstallPrompt();
        }
        else
        {
            UnityEngine.Debug.LogError("Failed to set cookie.");
        }
    }
    catch (CookieApi.InstantAppCookieException ex)
    {
        UnityEngine.Debug.LogErrorFormat("Failed to set cookie: {0}", ex);
    }

If the user completes app installation, the installed app can retrieve the cookie data using the following code:  

    var cookieBytes = CookieApi.GetInstantAppCookie();
    var playerInfoString = System.Text.Encoding.UTF8.GetString(cookieBytes);
    if (!string.IsNullOrEmpty(playerInfoString))
    {
        // Initialize game state based on the cookie, e.g. skip tutorial level completed in instant app.
    }