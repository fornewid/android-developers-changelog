---
title: https://developer.android.com/games/develop/multiplatform/make-your-game-compatible-with-all-form-factors
url: https://developer.android.com/games/develop/multiplatform/make-your-game-compatible-with-all-form-factors
source: md.txt
---

# Make your game compatible with all form factors

Tablets, foldables, Android Auto, Android Automotive OS cars, ChromeOS devices,
and PCs have the following baseline quality requirements:

|                                                          Requirement                                                          |                                                                                                                                         Tablets, foldables                                                                                                                                          |                                       Android Auto                                       |                                                        Android Automotive OS                                                        |                                                         ChromeOS                                                         |                                           Google Play Games on PC                                            |
|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| x86-64                                                                                                                        | Not required                                                                                                                                                                                                                                                                                        | Not required                                                                             | Recommended                                                                                                                         | Recommended                                                                                                              | Required                                                                                                     |
| Support resizability, different window sizes, and aspect ratios                                                               | Resizability support recommended                                                                                                                                                                                                                                                                    | Required                                                                                 | [Portrait and landscape support required](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=game#DO-1) | Resizability support recommended                                                                                         | Support any or all of the following aspect ratios: 16:9, 16:10, 3:2, 21:9 or a portrait aspect ratio of 9:16 |
| Maintain game state without restarting on configuration change (for example, resize, rotate, or fold or unfold)               | Required Support for foldable postures recommended                                                                                                                                                                                                                                                  | Required                                                                                 | Required                                                                                                                            | Required: resize, rotate, keyboard change                                                                                | N/A                                                                                                          |
| Remove unsupported features and permissions                                                                                   | [Recommended](https://android-developers.googleblog.com/2023/12/increase-your-apps-availability-across-device-types.html) In particular, for maximum tablet device reach, do not require: - `android.hardware.camera.autofocus` - `android.hardware.camera.flash` - `android.hardware.location.gps` | N/A                                                                                      | [Required](https://developer.android.com/training/cars/parked/automotive-os#config-manifest)                                        | [Required](https://developer.android.com/topic/arc/manifest?unsupported-hardware-features#unsupported-hardware-features) | [Required](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)      |
| Game controls, visuals, and performance don't detract from playability (for example, not blurry or unreadable, all UI usable) | Required                                                                                                                                                                                                                                                                                            | Required                                                                                 | Required                                                                                                                            | Required                                                                                                                 | Required                                                                                                     |
| Mouse and keyboard support                                                                                                    | Recommended                                                                                                                                                                                                                                                                                         | Optional                                                                                 | Optional                                                                                                                            | Required if the game cannot be played with single-touch input                                                            | Required if the game cannot be played with single-touch input                                                |
| Game controller support                                                                                                       | Recommended                                                                                                                                                                                                                                                                                         | [Recommended](https://developer.android.com/training/cars/parked/games#game-controllers) | [Recommended](https://developer.android.com/training/cars/parked/games#game-controllers)                                            | Recommended                                                                                                              | Recommended                                                                                                  |
| High-resolution graphics                                                                                                      | Recommended                                                                                                                                                                                                                                                                                         | Recommended                                                                              | Recommended                                                                                                                         | Recommended                                                                                                              | Recommended                                                                                                  |
| Input SDK                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                 | N/A                                                                                      | N/A                                                                                                                                 | N/A                                                                                                                      | Required if the game needs keyboard to play                                                                  |
| PGS v2                                                                                                                        | Not required                                                                                                                                                                                                                                                                                        | Not required                                                                             | Recommended                                                                                                                         | Not required                                                                                                             | Required                                                                                                     |

## Include x86-64 ABI architecture

Add x86-64 ABI compatible versions to all the libraries included in your game to ensure the best performance and stability on form factors such as Android Automotive OS cars, ChromeOS devices, and [Google Play Games on PC](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement).

Google has worked with game engine and 3rd-party library providers to ensure device support. You should be able to implement an x86_64 version of your game with minimal work.

With Android App Bundles, the increased x86-64 `.so` file affects only the upload size to the Play console. Play Store delivers the necessary ABI to each device, so the download size on target form factors remains unchanged.

## Audit Android manifest to ensure form factor compatibility

Some common mobile phone and tablet hardware features, such as camera or geolocation, are not available on other form factors. Games that have feature requirements can't be downloaded and installed on form factor devices that lack the features.

You can view a complete list of available features with the following ADB command:  

    adb shell pm list features

To make your game compatible with as many devices as possible, follow these do's and don'ts:

- **Do** mark features as optional in your manifest by adding `android:required="false"` to the `<uses-feature>` declaration. This only applies to the features already declared in your manifest. Ensure your code doesn't assume the feature is present.
- **Do** be aware of [implicit feature requirements](https://developer.android.com/guide/topics/manifest/uses-feature-element#implicit) your game may have.
- **Don't** attempt to use missing features at runtime.
- **Don't** request unsupported Android permissions at runtime.
- **Do** detect the available features at runtime and avoid the form factor‑specific code paths.

For more information about manifest compatibility, see the following:

- Android Automotive OS: [Configure your app's manifest file](https://developer.android.com/training/cars/parked#config-manifest)
- ChromeOS: [App manifest compatibility for Chromebooks](https://developer.android.com/topic/arc/manifest)
- Google Play Games on PC: [PC compatibility and optimization for Google Play Games on PC](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)

A common challenge is that many games request `android.hardware.wifi` just to check whether a player is on a metered network but could instead use the `ConnectivityManager` API without requesting any extra permissions (see [Monitor connectivity status and connection metering](https://developer.android.com/training/monitoring-device-state/connectivity-status-type)).

## Use Google Play Developer Console to help distribution

### Form factor filter

Play console support uses form factor as a filter in the following places:

- Android vitals (except for Android Automotive OS)
- Reach and devices
- Statistics
- Rating and reviews

For example, you can filter "Chromebook" in Android vitals to find out your crash rate and ANRs on all ChromeOS devices. Then optimize your game with a clear target.

### Device catalog

[Device catalog](https://play.google.com/console/about/devicecatalog/) is a useful tool for finding out compatible devices and unsupported devices for your game. Use the form factor filter to find out what devices are unsupported and why. After going to the device detail page, click **Show more** to check the exact reasons why your games are not supported on certain devices, for example:

- Unsupported ABI
- Unsupported features and permissions
- Unsupported graphic APIs

Fixing the requirements enables players on those devices to find your game in the Google Play Store.

### Form factor tracks

You can manage your form factor setting through **Setup \> Advanced settings \> Form factors** in the Play console. Mobile, tablets, foldables, and ChromeOS are bound to your default tracks. It is always easier to manage your release when using a single release artifact for serving all the form factors.

You can choose to create a [dedicated release track](https://support.google.com/googleplay/android-developer/answer/13295490) to manage your Google Play Games on PC (if you are in the beta program), [Android Automotive OS](https://developer.android.com/training/cars/distribute#choose-track-aaos), or Android TV releases if you need a separate build to manage the features. When you use separate tracks to manage form factor releases, you have access to different form factors through production and testing tracks.

## Use Android App Bundles to manage different features

[An Android App Bundle](https://developer.android.com/guide/app-bundle)is a publishing format that includes all your app's compiled code and resources and defers APK generation and signing to Google Play.

Supporting different form factors often requires specific ABIs, assets, libraries, or code paths for different form factors. You can take advantage of [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery), which allows you to add *feature modules* to your project. The modules contain features and resources that are only included with your app based on conditions that you specify or are available later at runtime for download using the [Play Core libraries](https://developer.android.com/guide/playcore).

You can also use [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery), Google Play's solution for delivering large amounts of game assets with flexible delivery methods and high performance.
| **Note:** For apps that target Android 16 (API level 36), the system ignores screen orientation, aspect ratio, and app resizablility restrictions to improve the layout of apps on form factors with smallest width \>= 600dp. See [App
| orientation, aspect ratio, and
| resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).