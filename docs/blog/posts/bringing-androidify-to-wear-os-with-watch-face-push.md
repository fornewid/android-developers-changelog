---
title: https://developer.android.com/blog/posts/bringing-androidify-to-wear-os-with-watch-face-push
url: https://developer.android.com/blog/posts/bringing-androidify-to-wear-os-with-watch-face-push
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Bringing Androidify to Wear OS with Watch Face Push

3 min read ![](https://developer.android.com/static/blog/assets/Androidify_Watch_e91b9acf51_Z84c6L.webp) 18 Dec 2025 [![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin) Developer Relations Engineer
[Video](https://www.youtube.com/watch?v=JgsPXZIKInw)

A few months ago we [relaunched Androidify](https://android-developers.googleblog.com/2025/09/androidify-ai-gemini-android-jetpack-compose-firebase-camerax.html) as an app for generating personalized Android bots. Androidify transforms your selfie photo into a playful Android bot using [Gemini and Imagen](https://android-developers.googleblog.com/2025/05/androidify-how-androidify-leverages-gemini-firebase-ml-kit.html).

However, given that Android spans multiple form factors,[including our most recent addition, XR](https://android-developers.googleblog.com/2025/10/bringing-androidify-to-xr-with-jetpack.html), we thought, how could we bring the fun of Androidify to Wear OS?

*An Androidify watch face*

As Androidify bots are highly-personalized, the natural place to showcase them is the watch face. Not only is it the most frequently visible surface but also the most personal surface, allowing you to represent who you are.
![demonstration.gif](https://developer.android.com/static/blog/assets/demonstration_4f5e5249cc_Qtp7f.webp)

*Personalized Androidify watch face, generated from selfie image*

Androidify now has the ability to generate a watch face dynamically within the phone app and then send it to your watch, where it will automatically be set as your watch face. All of this happens within seconds!

### High-level design

![image.png](https://developer.android.com/static/blog/assets/image_ac3a4aaaf6_10Vx6Y.webp)

*End-to-end flow for watch face creation and installation*

In order to achieve the end-to-end experience, a number of technologies need to be combined together, as shown in this high-level design diagram.

First of all, the user's avatar is combined with a pre-existing [Watch Face Format](https://developer.android.com/training/wearables/wff) template, which is then packaged into an APK. This is validated - for reasons which will be explained! - and sent to the watch.

On being received by the watch, the new [Watch Face Push API](https://developer.android.com/training/wearables/watch-face-push) - part of Wear OS 6- is used to install and activate the watch face.

Let's explore the details:

### Creating the watch face templates

The watch face is created from a template, itself designed in [Watch Face Designer](https://www.figma.com/community/plugin/1537485193225852308/watch-face-designer). This is our new Figma plugin that allows you to create [Watch Face Format](https://developer.android.com/training/wearables/wff) watch faces directly within Figma.
![image.png](https://developer.android.com/static/blog/assets/image_a957ae132a_Z2uN0X4.webp)

*An Androidify watch face template in Watch Face Designer*

The plugin allows the watch face to be exported in a [range of different ways](https://developer.android.com/training/wearables/watch-face-designer/export), including as Watch Face Format (WFF) resources. These can then be easily incorporated as [assets within the Androidify app](https://github.com/android/androidify/tree/main/watchface/src/main/assets), for dynamically building the finalized watch face.

### Packaging and validation

Once the [template and avatar have been combined](https://github.com/android/androidify/blob/main/watchface/src/main/java/com/android/developers/androidify/watchface/creator/WatchFaceCreator.kt#L49), the [Portable Asset Compiler Kit](https://github.com/google/pack) (Pack) is used to assemble an APK.

In Androidify, Pack is used as a [native library on the phone](https://github.com/android/androidify/tree/main/watchface/src/main/jniLibs). For more details on how Androidify interfaces with the Pack library, see the [GitHub repository](https://github.com/android/androidify/blob/main/watchface/pack-java/src/lib.rs).

As a final step before transmission, the APK is checked by the [Watch Face Push validator](https://developer.android.com/training/wearables/watch-face-push#validation).

This validator checks that the APK is suitable for installation. This includes checking the contents of the APK to ensure it is a valid watch face, as well as some performance checks. If it is valid, then the validator produces a token.

This token is required by the watch for installation.

### Sending the watch face

The Androidify app on Wear OS uses [WearableListenerService](https://github.com/android/androidify/blob/main/wear/src/main/java/com/android/developers/androidify/service/AndroidifyDataListenerService.kt) to listen for events on the Wearable Data Layer.

The phone app [transfers the watch face](https://github.com/android/androidify/blob/main/watchface/src/main/java/com/android/developers/androidify/watchface/transfer/WearAssetTransmitter.kt) by using a combination of `MessageClient` to set up the process, then `ChannelClient` to stream the APK.

### Installing the watch face on the watch

Once the watch face is received on the Wear OS device, the Androidify app uses the new [Watch Face Push API](https://developer.android.com/training/wearables/watch-face-push) to install the watch face:

```
val wfpManager = 

    WatchFacePushManagerFactory.createWatchFacePushManager(context)

val response = wfpManager.listWatchFaces()



try {

    if (response.remainingSlotCount > 0) {

        wfpManager.addWatchFace(apkFd, token)

    } else {

        val slotId = response.installedWatchFaceDetails.first().slotId

        wfpManager.updateWatchFace(slotId, apkFd, token)

    }

} catch (a: WatchFacePushManager.AddWatchFaceException) {

    return WatchFaceInstallError.WATCH_FACE_INSTALL_ERROR

} catch (u: WatchFacePushManager.UpdateWatchFaceException) {

    return WatchFaceInstallError.WATCH_FACE_INSTALL_ERROR

}
```

Androidify uses either the `addWatchFace` or `updateWatchFace` method, depending on the scenario: Watch Face Push defines a concept of "slots" - how many watch faces a given app can have installed at any time. For Wear OS 6, this value is in fact 1.

Androidify's approach is to install the watch face if there is a free slot, and if not, any existing watch face is swapped out for the new one.

### Setting the active watch face

Installing the watch face programmatically is a great step, but Androidify seeks to ensure the watch face is also the active watch face.

Watch Face Push introduces a new runtime permission which must be granted in order for apps to be able to achieve this:

`*com.google.wear.permission.SET_PUSHED_WATCH_FACE_AS_ACTIVE*`

Once this permission has been acquired, the `wfpManager.setWatchFaceAsActive()` method can be called, to set an installed watch face to being the active watch face.

However, there are a number of considerations that Androidify has to navigate:

- `setWatchFaceAsActive` can only be used once.
- `SET_PUSHED_WATCH_FACE_AS_ACTIVE` cannot be re-requested after being denied by the user.
- Androidify might already be in control of the active watch face.

For more details see how Androidify [implements the set active logic](https://github.com/android/androidify/blob/main/wear/src/main/java/com/android/developers/androidify/watchfacepush/WatchFaceOnboardingRepository.kt#L58).

### Get started with Watch Face Push for Wear OS

Watch Face Push is a versatile API, equally suited to enhancing Androidify as it is to building fully-featured watch face marketplaces.

Perhaps you have an existing phone app and are looking for opportunities to further engage and delight your users?

Or perhaps you're an existing watch face developer looking to create your own community and gallery through releasing a marketplace app?

Take a look at these resources:

- [Watch Face Push](https://developer.android.com/training/wearables/watch-face-push)
- [Watch Face Format](https://developer.android.com/training/wearables/wff) - Note also the [upcoming policy changes relating to watch face publishing](https://android-developers.googleblog.com/2025/06/upcoming-changes-to-wear-os-watch-faces.html).
- [Watch Face Designer](https://android-developers.googleblog.com/2025/08/introducing-watch-face-designer.html)
- [Androidify GitHub repository](https://github.com/android/androidify)
- [Androidify Play Store listing](https://play.google.com/store/apps/details?id=com.android.developers.androidify)

And also check out the [accompanying video](https://www.youtube.com/watch?v=JgsPXZIKInw&feature=youtu.be) for a greater-depth look at how we brought Androidify to Wear OS!

We're looking forward to what you'll create with Watch Face Push!
Written by:

-

  ## [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/garan-jenkin) ![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp) ![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)
Continue reading
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
- [![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)](https://developer.android.com/blog/authors/chiara-chiappini) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Bring_one_handed_gestures_Strapi_defff06599_Z1FDx9g.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring one-handed gestures to your Wear OS app](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app)

  [arrow_forward](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app) First introduced on Pixel Watch with Wear OS 6.1, one-handed gestures made quick interactions effortless, such as starting and stopping a timer, accepting calls, and controlling media.
  [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#pixel watch](https://developer.android.com/blog/topics/pixel-watch)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)