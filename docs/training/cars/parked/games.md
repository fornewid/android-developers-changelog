---
title: https://developer.android.com/training/cars/parked/games
url: https://developer.android.com/training/cars/parked/games
source: md.txt
---

# Build games for cars

The Games category is in beta  
At this time, anyone can publish games to internal testing and closed testing tracks on the Play Store. Publishing to open testing and production tracks will be permitted at a later date.  
[Nominate yourself to be an early access partner →](https://forms.gle/VsXEdDEBidxw8q8u8)  
![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

Games offer a unique opportunity to engage users in a fun and interactive way while their car is parked. By bringing your game to cars, you can reach a new audience and provide entertainment during downtime.

In addition to the guidance on this page, follow the platform-specific requirements for each platform that your game is compatible with:

- [Add support for Android Auto to your parked app](https://developer.android.com/training/cars/parked/auto)
- [Add support for Android Automotive OS to your parked app](https://developer.android.com/training/cars/parked/automotive-os)

| **Important:** Make sure your game meets the[quality guidelines for games](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=game), as it is[reviewed against them](https://developer.android.com/training/cars/distribute#understand-review)when submitted to tracks other than internal testing.

## Mark your app as a game

To indicate that your app is a game, you must add the[`android:appCategory="game"`](https://developer.android.com/guide/topics/manifest/application-element#appCategory)attribute to the[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)element of your manifest.  

    <manifest ...>
        ...
        <application
          ...
          android:appCategory="game">
            ...
        </application>
    </manifest>

## Declare support for game controllers (optional)

If your app[supports controller input](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers), include the following manifest declaration for the[`android.hardware.gamepad`](https://developer.android.com/guide/topics/manifest/uses-feature-element#gamepad-hw-features)feature, as OEMs can use this information to improve the user experience:  

    <manifest ...>
      ...
      <uses-feature android:name="android.hardware.gamepad" android:required="false"/>
      ...
    </manifest>

| **Caution:** Be careful not to set the[`android:required`](https://developer.android.com/guide/topics/manifest/uses-feature-element#required)attribute to`true`, as not all devices have this feature present even if they can pair with a controller.