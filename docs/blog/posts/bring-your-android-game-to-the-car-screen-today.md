---
title: https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today
url: https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Bring your Android game to the car screen today

3 min read ![](https://developer.android.com/static/blog/assets/Games_for_car_Strapi_1_c55588726e_Z2cIhWx.webp) 21 Sep 2026 [![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)](https://developer.android.com/blog/authors/jan-kleinert) [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert) Developer Relations Engineer Today, the games category for [Android Auto](https://www.android.com/auto/) and cars powered by Android Automotive OS with [Google built-in](https://built-in.google/cars/) is officially graduating from beta to general availability. Our early access partners have already been bringing games to the parked-only experience for cars, and you can browse these in our latest collections of [games for Android Auto](https://play.google.com/store/apps/streamchild/promotion_apps_beto__games_on_android_auto__collection) and [games for Android Automotive OS](https://play.google.com/store/apps/streamchild/promotion_apps_beto_games_on_android_automotive_os_collection).
![Quote-black-bg.png](https://developer.android.com/static/blog/assets/Quote_black_bg_f48ea8b886_Zikf9X.webp)

Bringing your game to cars lets you reach users in their vehicles during natural downtime, such as while waiting at a charging station or for a curbside order pickup. Today's milestone means that we're opening up access so developers can now publish games to the open testing and production tracks on Google Play. In this post, we'll cover how to adapt your existing Android game for the car screen, focusing on key technical requirements and publishing criteria.

## Implement car support for your game

If you're already following best practices for building [adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), bringing an existing Android game to cars primarily involves configuring your app manifest and ensuring your game respects the vehicle parked state.

### Mark your app as a game

To distribute your app in the games category, you need to explicitly declare its category. Add the `android:appCategory="game"` attribute to the `<application>` element of your manifest file:

```
<application ... 
    android:appCategory="game">
    ...
</application>
```

### Declare support for Android Auto

Games are supported on Android Auto on devices running Android 15 and higher. To declare that your game supports Android Auto, include this `<category>` element in the intent filter of an activity in your manifest file:

```
<activity ... 
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        ...
        <category android:name="android.intent.category.CAR_LAUNCHER" />
    </intent-filter>
</activity>
```

Generally, the `android.intent.category.CAR_LAUNCHER` category element is placed in the same intent filter as the `android.intent.category.LAUNCHER` element, but it can be in another activity's intent filter if you prefer to launch a different activity.

### Declare support for Android Automotive OS

To declare that your game supports Android Automotive OS, include the `android.hardware.type.automotive <uses-feature>` element in your manifest file.

```
<manifest ... 
    ...
    <uses-feature android:name="android.hardware.type.automotive"
                  android:required="false" />
    ...
</manifest>
```

The `android:required` value has different restrictions depending upon which [track you choose](https://developer.android.com/training/cars/distribute#choose-track-aaos) to distribute your Android Automotive OS app. If you distribute your Android Automotive OS app on the mobile track, `android:required` must be set to `"false"`. However, if you distribute on the Android Automotive OS dedicated track, you can set `android:required` to `"true"`, `"false"`, or leave it unset. Leaving the value unset has the same effect as setting `android:required` to `"true"`, and means that your app is available only for distribution on Android Automotive OS devices.

### Handle the parked state

Cars introduce a unique physical context with a driving state and a parked state. Certain types of apps, like games, are considered parked apps and aren't permitted to run while the vehicle is in motion to avoid driver distraction. By default, Android Auto and Android Automotive OS block activities from being used or launched when the vehicle is in motion or when [user experience (UX) restrictions](https://developer.android.com/training/cars/platforms/automotive-os#ux-restrictions) are active. To make sure your game complies with driver distraction guidelines, don't include the [`distractionOptimized`](https://developer.android.com/training/cars/parked/automotive-os#prevent-use) metadata element in any activity in your manifest. You must also [ensure that your game audio stops](https://developer.android.com/training/cars/parked/automotive-os#stop-playback) when the user starts driving and can't be unpaused while the vehicle is in motion.
![TrivialKartSample.png](https://developer.android.com/static/blog/assets/Trivial_Kart_Sample_acd9d40db7_ZQ4vmz.webp) The TrivialKart for Unity sample app running on the Desktop Head Unit while in a parked state. ![UXRestrictionsActive.png](https://developer.android.com/static/blog/assets/UX_Restrictions_Active_aecfb503c4_1C1BMS.webp) The behavior of a parked app when UX restrictions are active.

Additionally, when the user relaunches the app from the home screen, your game must restore the app state as closely as possible to the previous state. Test your game for responsiveness and ensure it doesn't freeze or stutter during gameplay.

### Declare game controller support

Car screens support touch input, but many users prefer playing with a connected gamepad. If your game [supports controller input](https://developer.android.com/training/cars/parked/games#game-controllers), declare the `android.hardware.gamepad` feature in your manifest to help boost the [visibility](https://developer.android.com/games/sdk/game-controller/visibility) of your app in the Google Play Store to users specifically seeking controller-compatible experiences.

```
<uses-feature android:name="android.hardware.gamepad" android:required="false"/>
```

Set the `android:required` attribute to `false` to indicate your app supports controllers, but the use of controllers is optional. Don't set the `android:required` attribute to `true` unless a controller is mandatory for your game.

### Support common screen sizes and aspect ratios

Car displays come in various shapes and aspect ratios, including portrait and wide landscape screens. For a great user experience, make your game fully adaptive to different screen sizes so that it runs full screen without letterboxing or pillarboxing. For Android Auto, refer to the guidance for [testing against canonical screen sizes](https://developer.android.com/training/cars/parked/auto#test-screen-sizes) and use [bundled hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles) when testing with the emulator for Android Automotive OS.

## Publish your game to cars

After you've implemented the necessary changes, you can [opt in to Android Auto and Android Automotive OS form factors](https://developer.android.com/training/cars/distribute#opt-in-ff) in the Google Play Console. Before submitting to production, test your game against the [car app quality guidelines](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=games) for games.

Use the [Desktop Head Unit](https://developer.android.com/training/cars/testing/dhu) to test your app's Android Auto compatibility, and use the [Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator) to test the experience on Android Automotive OS. Your game will be reviewed against the car app quality guidelines for the games category before it is approved for open testing or production.

## Get your games on the road

With the games category now generally available, it is the perfect time to optimize your titles for cars. To learn more about implementation details, review the documentation at [Build games for cars](https://developer.android.com/training/cars/parked/games).
- [#Android Automotive OS](https://developer.android.com/blog/topics/android-automotive-os)
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- [#Android Auto](https://developer.android.com/blog/topics/android-auto)
Written by:

-

  ## [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jan-kleinert) ![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp) ![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)
Continue reading
- 3 Authors 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in Android for Cars: Unifying platforms and unlocking premium experiences](https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences) We're thrilled to see developers continuing to bring their apps and experiences to Android for Cars! Over the past year, we've continued to see strong growth and momentum in the app ecosystem on Android Auto and cars with Google built-in.
  [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert), [Noam Gefen](https://developer.android.com/blog/authors/noam-gefen), [Thomas Weathers](https://developer.android.com/blog/authors/thomas-weathers) • 3 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- 3 Authors 24 Aug 2026 24 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_1_Strapi_6f49d09922_1I8TFC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [AAOS SDV - Secure by Design](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design)

  [arrow_forward](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design) At Google, we believe our products should be secure by design, which is why we built the Android Automotive Operating System for Software Defined Vehicle (AAOS SDV) on existing, market-proven platforms, leveraging virtualization technologies like Cuttlefish.
  [Markus Vill](https://developer.android.com/blog/authors/markus-vill), [Sean Keys](https://developer.android.com/blog/authors/sean-keys), [István Nádor](https://developer.android.com/blog/authors/istvan-nador) • 5 min read
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto)
  - [#Security](https://developer.android.com/blog/topics/security)
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_21k6io.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android UI Development is Compose First](https://developer.android.com/blog/posts/android-ui-development-is-compose-first)

  [arrow_forward](https://developer.android.com/blog/posts/android-ui-development-is-compose-first) In the almost-5-years since Jetpack Compose launched, we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 2 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)