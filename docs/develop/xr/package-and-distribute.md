---
title: https://developer.android.com/develop/xr/package-and-distribute
url: https://developer.android.com/develop/xr/package-and-distribute
source: md.txt
---

Through Google Play, Android XR brings a wide variety of apps and experiences to
XR headsets, ranging from the existing catalog of mobile apps to spatialized and
immersive XR experiences.

Review this guide to learn how to prepare and distribute your apps to Android XR
users through Google Play. Be sure to read the [Android XR app quality
guidelines](https://developer.android.com/docs/quality-guidelines/android-xr) for information on usability and quality standards.

> [!IMPORTANT]
> **Important:** App distribution through the Google Play Store is only available for [immersive app experiences](https://developer.android.com/develop/xr/explore/immersive) on XR headsets and wired XR glasses devices. For [augmented experiences on AI glasses](https://developer.android.com/develop/xr/explore/augmented), [get started developing](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/build), [run and
> debug your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/augmented) on the Android XR emulator, and stay tuned for more updates on distribution in the future.

Follow this guidance to:

- Get started with the Play Store and Play Console
- Learn about Android app bundles and size restrictions
- Choose a release track for your app
- Manage device exclusions

## Get started with the Play Store and Play Console

If you already have a mobile app published in the Play Store, then publishing an
app for Android XR will feel familiar. If you are new to the [Play Store](https://play.google.com) or
[Play Console](https://play.google.com/console/about), then these resources will help you get started.

With Android XR, a user can visit the Play Store on an XR headset and download
an app directly to the headset.

Uploading and publishing an app requires a Play Console account. You can develop
and publish using your existing Play Console account or [create one](https://support.google.com/googleplay/android-developer/answer/6112435) if you
are new to the platform.

The [Play Console Help Center](https://support.google.com/googleplay/android-developer#topic=3450769) has the information you need to get started:

- Register for a [Google Play Developer account](https://support.google.com/googleplay/android-developer/answer/6112435)
- Review the [Google Play Developer Policy Center](https://support.google.com/googleplay/android-developer/topic/9858052)
- [Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152) using Play Console
- [Set up pricing](https://support.google.com/googleplay/android-developer/answer/6334373) for your app
- Set up an [open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/9845334)
- Learn about the [Android App Bundle publishing format](https://developer.android.com/guide/app-bundle) and the [app
  bundle explorer](https://support.google.com/googleplay/android-developer/answer/9844279)
- [View reports, statistics, and insights](https://support.google.com/googleplay/android-developer/topic/3450942) about your app and its users

## Learn about Android app bundles and size restrictions

An [Android App Bundle](https://developer.android.com/guide/app-bundle/app-bundle-format) is a publishing format that includes all your app's
compiled code and resources, and defers APK generation and signing to Google
Play.

Google Play uses your app bundle to generate and serve optimized APKs for each
device configuration, so only the code and resources that are needed for a
specific device are downloaded to run your app. You don't necessarily have to
build, sign, and manage multiple APKs to optimize support for different devices,
and users get smaller, more-optimized downloads.

Most app projects won't require much effort to build app bundles that support
serving optimized APKs. Optimized APK serving becomes an automatic benefit if
you're already doing any of these things:

- [Organize your code and resources according to established conventions](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)
- [Build signed Android App Bundles](https://developer.android.com/studio/publish/app-signing#sign-apk) using Android Studio or by [using the
  command line](https://developer.android.com/studio/build/building-cmdline) and [upload them to Google Play](https://developer.android.com/studio/publish/upload-bundle)

[Google Play's maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits) also apply to Android XR apps.

> [!NOTE]
> **Note:** These sizes reflect the *compressed download size* as calculated by Play when the app is uploaded in the Play Console.

You may want to take advantage of [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) or [Play Feature
Delivery](https://developer.android.com/guide/playcore/feature-delivery) for Android XR apps, particularly if your app includes a lot of
large assets. Play Feature Delivery uses advanced capabilities of app bundles,
allowing certain features of your app to be delivered conditionally or
downloaded on demand. Play Asset Delivery is Google Play's solution for
delivering large amounts of game assets, and it offers flexible delivery methods
and high performance.

## Choose a release track for your app

Play Console provides you options for how you publish and manage your apps. For
Android XR, you can choose from two [release tracks](https://support.google.com/googleplay/android-developer/answer/13295490): mobile release track
or the [dedicated Android XR release track](https://support.google.com/googleplay/android-developer/answer/13295490#zippy=%2Cuse-a-dedicated-release-track-for-android-xr-apps).

The release track you choose depends primarily on whether you're adding [spatial
UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), or [spatial environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments) to an existing mobile
app or building a new [XR app](https://developer.android.com/develop/xr/get-started). Read the following sections for guidance on
release track options.

### Spatialize an existing mobile app

Existing apps published on the mobile release track are automatically
discoverable on Google Play for Android XR users, as long as the app doesn't
include any [unsupported features](https://developer.android.com/develop/xr/get-started#unsupported-features) for Android XR.

If you choose to differentiate your mobile app for XR by adding features such as
[spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), or [spatial environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments), you have two
options for how you can distribute the app to Android XR users. In either case,
use the same package name as your existing app.

#### Continue publishing to the mobile track

In most cases, you can bundle [XR features or content into your existing mobile
APK](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing). You won't need to make any specific publishing changes in the Play
Console; you can continue working with your existing APK and publish the same
assets on the mobile release track. Android XR users will receive artifacts from
the mobile release track.

> [!IMPORTANT]
> **Important:** If you use this track, make sure you've correctly [configured the `uses-feature` element for
> `android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) in your app's manifest file.

#### Publish your XR experience to the Android XR dedicated release track

In some situations, your XR app and your mobile app may have significantly
different features or requirements. For example, your XR app might require a
different set of permissions or it may offer very different functionality that
makes it difficult to refactor it to serve both mobile and XR use cases. In
these cases, you may choose to create a new APK for your XR experience using the
existing registered app entry in Play. The new APK will share a package name
with your existing mobile app. Your existing mobile app will stay published on
the mobile track, and your new XR variation of the app will be published on the
Android XR dedicated track.

While this option can provide extra flexibility over your releases, it does have
more overhead, since you have multiple APKs to release and manage. To publish to
the Android XR dedicated track, the application must include the
[`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) feature or the
[`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/openxr/get-started#android.software.xr.api.openxr) in the app manifest, depending upon
whether the app is built with the Jetpack XR SDK or built with OpenXR or Unity.
Learn more about PackageManager [features for XR apps](https://developer.android.com/develop/xr/get-started#packagemanager-features).

Apps that are published to the Android XR dedicated track will only be visible
to Android XR devices that support either the `android.software.xr.api.spatial`
feature or the `android.software.xr.api.openxr` feature, depending upon what is
specified in the app manifest.

For detailed instructions on how to use the dedicated release track for Android
XR, see the [Play Console guide](https://support.google.com/googleplay/android-developer/answer/13295490).

### Building a new XR app

For new applications that are intended solely for XR devices, you should publish
exclusively to the Android XR dedicated track. To publish to the Android XR
dedicated track, the application must include the
[`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) feature or the
[`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/openxr/get-started#android.software.xr.api.openxr) in the app manifest, depending upon
whether the app is built with the Jetpack XR SDK or built with OpenXR or Unity.
For more information about PackageManager features for XR apps, see the
corresponding sections in the [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#packagemanager-features) and [OpenXR](https://developer.android.com/develop/xr/get-started#packagemanager-features) pages.

Apps that are published to the Android XR dedicated track will only be visible
to Android XR devices that support either the
[`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) feature or the
[`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/openxr/get-started#android.software.xr.api.openxr) feature, depending upon what is specified
in the app manifest.

For detailed instructions on how to use the dedicated release track for Android
XR, see [the Play Console guide](https://support.google.com/googleplay/android-developer/answer/13295490).

## Manage device exclusions

After you've uploaded at least one app bundle to the Play Console, you can view
the catalog of available devices and review which devices are compatible with
your app. Visit the [Play Console help center](https://support.google.com/googleplay/android-developer/answer/7353455) to understand how to view and
restrict your app's compatible devices.

> [!NOTE]
> **Note:** If you want to exclude your app from being available on a particular XR headset, note that unlaunched devices may not be visible in the device catalog in the Play Console until closer to their launch.

## See also

- [Prepare your app for release](https://developer.android.com/studio/publish#publishing-prepare)
- [Add preview assets to showcase your app](https://support.google.com/googleplay/android-developer/answer/9866151)
- [Sign your app](https://developer.android.com/studio/publish/app-signing)
- [Upload your app](https://developer.android.com/studio/publish/upload-bundle)
- [Set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/9845334)
- [Release with confidence](https://developer.android.com/distribute/best-practices/launch/launch-checklist)
- [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?ref_topic=7072031)
- [Google Play Developer Center](https://support.google.com/googleplay/android-developer/topic/9858052)

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.