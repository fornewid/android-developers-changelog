---
title: Build games for cars  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/parked/games
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Build games for cars Stay organized with collections Save and categorize content based on your preferences.




The Games category is in beta

At this time, anyone can publish games to internal testing and closed testing tracks on the Play Store. Publishing to open testing and production tracks will be permitted at a later date.

[Nominate yourself to be an early access partner →](https://forms.gle/VsXEdDEBidxw8q8u8)

![](/static/images/picto-icons/test-tube-2.svg)

Games offer a unique opportunity to engage users in a fun and interactive way
while their car is parked. By bringing your game to cars, you can reach a new
audience and provide entertainment during downtime.

In addition to the guidance on this page, follow the platform-specific
requirements for each platform that your game is compatible with:

* [Add support for Android Auto to your parked app](/training/cars/parked/auto)
* [Add support for Android Automotive OS to your parked app](/training/cars/parked/automotive-os)

**Important:** Make sure your game meets the [quality guidelines for
games](/docs/quality-guidelines/car-app-quality?category=game), as it is [reviewed against them](/training/cars/distribute#understand-review)
when submitted to tracks other than internal testing.

## Mark your app as a game

To indicate that your app is a game, you must add the
[`android:appCategory="game"`](/guide/topics/manifest/application-element#appCategory) attribute to the
[`<application>`](/guide/topics/manifest/application-element) element of your manifest.

```
<manifest ...>
    ...
    <application
      ...
      android:appCategory="game">
        ...
    </application>
</manifest>
```

## Declare support for game controllers (optional)

If your app [supports controller input](/develop/ui/views/touch-and-input/game-controllers), include the following
manifest declaration for the [`android.hardware.gamepad`](/guide/topics/manifest/uses-feature-element#gamepad-hw-features)
feature, as OEMs can use this information to improve the user experience:

```
<manifest ...>
  ...
  <uses-feature android:name="android.hardware.gamepad" android:required="false"/>
  ...
</manifest>
```

**Caution:** Be careful not to set the [`android:required`](/guide/topics/manifest/uses-feature-element#required) attribute to `true`, as
not all devices have this feature present even if they can pair with a
controller.