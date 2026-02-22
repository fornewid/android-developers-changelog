---
title: https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app
url: https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app
source: md.txt
---

# Convert an existing game to an instant game

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

The steps for setting up apps to run on[Google Play Instant](https://developer.android.com/topic/google-play-instant/overview), as explained in[Create your first instant app](https://developer.android.com/topic/google-play-instant/getting-started/first-instant-app), also apply to games. This guide emphasizes some setup steps specific to games.

You can develop games for Google Play Instant using[Unity](https://docs.unity3d.com/Manual/android-sdksetup.html)(with or without the[Google Play Instant Unity plugin](https://developer.android.com/topic/google-play-instant/getting-started/game-unity-plugin)),[Cocos2D](https://docs.cocos2d-x.org/cocos2d-x/v3/en/installation/Android-Studio.html),[Android Studio](https://developer.android.com/studio), or your own custom engine.

This guide assumes that you already know the sort of gaming experience you'd like to provide. If you'd like to see ideas and best practices for making high-quality games, read through[UX best practices for games on Google Play Instant](https://developer.android.com/topic/google-play-instant/best-practices/games).

In addition, before publishing a game that can run on Google Play Instant, you should review the[Technical requirements checklist](https://developer.android.com/topic/google-play-instant/tech-requirements).

## Specify an entry point

An activity that includes the following intent filter becomes the entry point for the Google Play Instant experience:  

    <activity android:name=".GameActivity">
       <intent-filter>
          <action android:name="android.intent.action.MAIN" />
          <category android:name="android.intent.category.LAUNCHER" />
       </intent-filter>
    </activity>

This activity is launched when a user taps the**Try Now** button in the Play Store or the[**Instant play**](https://developer.android.com/topic/google-play-instant/instant-play-games)button in Google Play Games app. You can also launch this activity directly using the[deep link API](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#Instant).
| **Note:** You can bundle this entry point activity with several other activities in a single module that represents your game's instant experience.

## Define the correct version codes

The version code of your game's instant experience needs to be less than the version code of the installable game. Versioning your app in this way allows players to move from the Google Play Instant experience to downloading and installing the game onto their device. The Android framework considers this transition to be an app update.
| **Note:** If the player has the installed version of your game on their device, that installed version always runs instead of your instant experience when users invoke the instant experience from Google Play or from a link. This is true even if the installed version is an older version of your game compared to your instant experience.

To make sure that you follow the recommended versioning scheme, follow one of these strategies:

- Restart the version codes for the Google Play Instant experience at 1.
- Increase the version code of the installable app by a large number, such as 1000, to ensure that there is enough space for your instant experience's version number to increase.

It's OK to develop your instant game and your installable game in two separate Android Studio projects. If you do so, however, you must do the following to publish your game on Google Play:

1. Use the same package name in both Android Studio projects.
2. In the Google Play Console, upload both variants to the same application.

| **Note:** The version code isn't a user-facing value and is primarily used by the system. The user-facing*version name*has no restrictions.

For more details on setting your game's version, see[Version your app](https://developer.android.com/studio/publish/versioning).

## Support the execution environment

Like other apps, games on Google Play Instant run within a limited sandbox on the device. To support this execution environment, complete the steps shown in the following sections.

### Opt out of cleartext traffic

Games on Google Play Instant don't support HTTP traffic. If your game targets Android 9 (API level 28) or higher, Android disables cleartext support in your game by default.

If your game targets Android 8.1 (API level 27) or lower, however, you must create a[Network Security Config](https://developer.android.com/training/articles/security-config)file. In this file, set`cleartextTrafficPermitted`to`false`, as shown in the following code snippet:

res/xml/network_security_config.xml  

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">secure.example.com</domain>
    </domain-config>
</network-security-config>
```

### Update the target sandbox version

Update your instant game's`AndroidManifest.xml`file so that it targets the sandbox environment that Google Play Instant supports. You can complete this update by adding the`android:targetSandboxVersion`attribute to your games's`<manifest>`element, as shown in the following code snippet:  

    <manifest
       xmlns:android="http://schemas.android.com/apk/res/android"
      ...
       android:targetSandboxVersion="2" ...>

For more information, see documentation on the[`targetSandboxVersion`](https://developer.android.com/guide/topics/manifest/manifest-element#targetSandboxVersion)attribute.

### Don't rely on the presence of a cache or app data

Your instant experience remains downloaded on a user's device until the instant experience cache is cleared, which occurs in one of the following situations:

- The instant experience cache is garbage-collected because the device is running low on available memory.
- The user restarts their device.

If either process occurs, the user must re-download your instant experience in order to interact with it.

If the system is running very low on storage space, it's possible that your instant experience's user data is removed from internal storage. Therefore, it's recommended to periodically sync user data with your game's server so that the user's progress is preserved.

## Reduce your app size

Unlike other types of apps, games on Google Play Instant have a download size limit of**15 MB**. To create a game of this size, you might need to refactor your game's logic. This section describes some tools and techniques to help optimize the size of your game.

### Tools

The following list of tools can help you determine what is contributing to the size of your game:

- [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer): Provides a holistic view of the contents of a compiled APK. Using this view, you can determine the number of bytes that each element is contributing to the overall size. Use this tool to quickly check the size of resources, assets, logic, and native libraries that your game is using.
- [Bloaty McBloatface](https://github.com/google/bloaty): Shows the size profile of binary files.
- [Android GPU Inspector](https://developer.android.com/agi): See the file size effect of reducing texture size without having to recompile your game.

### Techniques

The following is a list of techniques that you can use to reduce the size of your game:

- Extract some of your game's logic and place it in one or more[feature modules](https://developer.android.com/studio/projects/dynamic-delivery#customize_delivery), which don't count toward the size limit.
- Reduce the resolution of your game's textures.
- Consider using the[WebP](https://blog.chromium.org/2010/09/webp-new-image-format-for-web.html)format, especially if you're using uncompressed textures on the GPU. The WebP format creates images that are the same quality as JPEG images but are 15% to 30% smaller. Although it takes longer to decompress WebP images, this decompression time is still significantly shorter than the download time of your game's textures. Google has also integrated the format into an[open source game engine](https://github.com/google/fplbase/tree/master/cmake/webp).
- Compress or re-use sounds and music.
- Use different compilation flags to help make your binary file smaller:
  - `-fvisibility=hidden`-- The most important one. In`cmake`, you can specify it as follows:  

    ```
    $ set_target_properties(your-target PROPERTIES CXX_VISIBILITY_PRESET hidden)
    ```
  - `-Oz`-- Also important for reducing size. If you compile using`gcc`, use`-Os`instead.
  - `-flto`-- Sometimes decreases file size.
  - Linker flags -- Use`--gc-sections`in conjunction with compiler flags, such as`-ffunction-sections`and`-fdata-sections`.
- Use Proguard to[shrink your code and resources](https://developer.android.com/studio/build/shrink-code).
- Use Gradle 4.4 or higher to generate smaller DEX files.
- Implement[cloud delivery of assets](https://developer.android.com/topic/google-play-instant/getting-started/cloud-delivery-assets).

## Divide a large game into multiple APKs

It can be difficult to optimize the Google Play Instant experience to make your game fit in a single 15 MB APK, even after applying the recommendations to[reduce APK size](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#app-size-reduction). To address this challenge, you can divide your game into multiple APKs. Players start by downloading the primary, base APK; as they play, the remaining*split APKs*are made available to the game in the background.

For example, the base APK can contain the core game engine and the assets required to display a loading screen. As the base APK launches, it displays the loading screen and immediately requests an additional split APK that contains the game and level data. After that split APK becomes available, it can load its assets into the game engine and give the player the content they need to begin the game.

## Adopt UX best practices

After you configure your game so that it supports instant experiences, add the logic that's shown in the following sections to provide a good user experience.
| **Note:** From June 2023 on, only instant apps published using app bundles are available to users. Please ensure all APK based instant apps have been updated to instant enabled bundles.

## Support 64-bit architectures

Apps published on Google Play need to support 64-bit architectures. Adding a 64-bit version of your app provides performance improvements and sets you up for devices with 64-bit-only hardware.[Learn more about 64-bit support](https://developer.android.com/google/play/requirements/64-bit).

### Check whether game is running instant experience

If some of your game's logic depends on whether the user is engaged in your instant experience, call the[`isInstantApp()`](https://developers.google.com/android/reference/com/google/android/gms/instantapps/PackageManagerCompat.html#isInstantApp())method. This method returns`true`if the currently-running process is an instant experience.

By doing this check, you can determine whether your app needs to run within a[limited execution environment](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#execution-environment)or can take advantage of platform features.

### Display an installation prompt

If you have built a trial Google Play Instant experience, at some point the game should prompt the player to install the full version onto their device. To do so, use the[`showInstallPrompt()`](https://developers.google.com/android/reference/com/google/android/gms/instantapps/InstantApps.html#showInstallPrompt(android.app.Activity,%20android.content.Intent,%20int,%20java.lang.String))method in the[Google APIs for Android](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary).

To learn more about how and when you should prompt the player for installation, see[UX best practices for games on Google Play Instant](https://developer.android.com/topic/google-play-instant/best-practices/games).

### Transfer data to an installed experience

If a player enjoys your trial experience, they might decide to install the full version of your game. To provide a good user experience, it's important that the player's progress is transferred from your instant experience to the full version of your game.

If your game[specifies a`targetSandboxVersion`of`2`](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#target-sandbox-version), then the player's progress is transferred automatically to the full version of your game. Otherwise, you must transfer the data related to player progress manually. To do so, use the Cookie API -[sample app](https://github.com/android/app-bundle-samples/tree/main/InstantApps/cookie-api)

## Additional resources

Learn more about Google Play Instant from these additional resources:

[Codelab: Build Your First Instant App](https://codelabs.developers.google.com/codelabs/android-instant-apps/index.html)
:   Add support for Google Play Instant in an existing app.

[Codelab: Build a Multi-Feature Instant App](https://codelabs.developers.google.com/codelabs/android-multi-feature-instant-app)
:   Modularize a multi-feature app.