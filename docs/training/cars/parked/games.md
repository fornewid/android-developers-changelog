---
title: https://developer.android.com/training/cars/parked/games
url: https://developer.android.com/training/cars/parked/games
source: md.txt
---

Games offer a unique opportunity to engage users in a fun and interactive way
while their car is parked. By bringing your game to cars, you can reach a new
audience and provide entertainment during downtime.

In addition to the guidance on this page, follow the platform-specific
requirements for each platform that your game is compatible with:

- [Add support for Android Auto to your parked app](https://developer.android.com/training/cars/parked/auto)
- [Add support for Android Automotive OS to your parked app](https://developer.android.com/training/cars/parked/automotive-os)

> [!IMPORTANT]
> **Important:** Make sure your game meets the [quality guidelines for
> games](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=game), as it is [reviewed against them](https://developer.android.com/training/cars/distribute#understand-review) when submitted to tracks other than internal testing.

## Mark your app as a game

To indicate that your app is a game, you must add the
[`android:appCategory="game"`](https://developer.android.com/guide/topics/manifest/application-element#appCategory) attribute to the
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element of your manifest.

    <manifest ...>
        ...
        <application
          ...
          android:appCategory="game">
            ...
        </application>
    </manifest>

## Support common display aspect ratios

For the best user experience, make your game [fully adaptive](https://developer.android.com/develop/ui/compose/build-adaptive-apps) to
different screen sizes so that it runs in full screen without letterboxing or
pillarboxing. Refer to the
[car app quality guidelines for games](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=game) for a list of
criteria your game must meet. Target the following common aspect ratios for
each platform and
orientation:

### Android Auto

- Landscape: 16:9 anchor aspect ratio
- Portrait: 9:16 aspect ratio

See [Test against canonical screen sizes](https://developer.android.com/training/cars/parked/auto#test-screen-sizes) for more
information on testing with Desktop Head Unit configurations for common screen
sizes.

### Android Automotive OS

- Landscape: 4:3 anchor aspect ratio
- Portrait: 10:16 aspect ratio

See [Use bundled hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles) for more information
on testing with the Android Automotive OS emulator using hardware profiles for
common screen sizes and aspect ratios.

## Declare support for game controllers (optional)

If your app [supports controller input](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers), include the following
manifest declaration for the [`android.hardware.gamepad`](https://developer.android.com/guide/topics/manifest/uses-feature-element#gamepad-hw-features)
feature, as OEMs can use this information to improve the user experience:

    <manifest ...>
      ...
      <uses-feature android:name="android.hardware.gamepad" android:required="false"/>
      ...
    </manifest>

> [!CAUTION]
> **Caution:** Be careful not to set the [`android:required`](https://developer.android.com/guide/topics/manifest/uses-feature-element#required) attribute to `true`, as not all devices have this feature present even if they can pair with a controller.

## Minimum hardware specifications

### Android Automotive OS

To learn more about the minimum hardware specifications for Android Automotive
OS devices, see the *Automotive Requirements* section of the
[Android Compatibility Definition Document (CDD)](https://source.android.com/docs/compatibility/cdd) for the Android
versions your app supports.

### Android Auto

Apps that support Android Auto run on the user's Android phone. Learn more about
supported Android phones and versions in the
[Get started with Android Auto](https://support.google.com/androidauto/answer/6348019?ref_topic=6106969#zippy=%2Candroid-auto-on-your-car-display-with-a-usb-cable%2Candroid-auto-on-your-car-display-wireless) section of the Android
Auto Help Center. Apps in parked app categories, like the Games category, are
supported on mobile devices running Android 15 (API level 35) and higher.

## Resources for building Android games

The [Android Games Dev Center](https://developer.android.com/games) has many other resources to help
you build high-quality games with great performance.

- [Get started with Android games](https://developer.android.com/games/guides)
- [About Android game development tools](https://developer.android.com/games/develop/overview)
- [Make your game compatible with all form factors](https://developer.android.com/games/develop/multiplatform/make-your-game-compatible-with-all-form-factors)
- [Analyze and optimize game performance](https://developer.android.com/games/optimize/gameperformance)
- [Google Play Games Services overview](https://developer.android.com/games/pgs/overview)