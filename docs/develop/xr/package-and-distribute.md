---
title: https://developer.android.com/develop/xr/package-and-distribute
url: https://developer.android.com/develop/xr/package-and-distribute
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Through Google Play, Android XR brings your app's immersive and augmented
experiences to a variety of XR devices like XR headsets, wired XR glasses, and
audio glasses.

Read this guide to learn how to prepare and distribute your apps to Android XR
users through Google Play. Also make sure to review the [Android XR app quality
guidelines](https://developer.android.com/docs/quality-guidelines/android-xr) for information on usability and quality standards for different
types of app experiences.

> [!IMPORTANT]
> **Important:** App distribution through the Google Play Store is available for [immersive app experiences](https://developer.android.com/develop/xr/explore/immersive) on XR headsets and wired XR glasses devices; and for [augmented experiences](https://developer.android.com/develop/xr/explore/augmented) on audio glasses. For display glasses, [get
> started developing](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/build), [run and debug your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/augmented) on the Android XR emulator, and stay tuned for more updates on distribution in the future.

## Get started with the Play Store and Play Console

If you already have a mobile app published in the Play Store, then publishing an
app for Android XR will feel familiar. If you're new to the [Play Store](https://play.google.com) or
[Play Console](https://play.google.com/console/about), then these resources can help you get started.

On some Android XR devices like XR headsets and wired XR glasses, a user can
visit the Play Store and download an app directly to the device. On other
devices like audio glasses, a user downloads an app to their companion device
(like a phone), which then connects to the glasses to provide the app's
experience.

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
> **Note:** These sizes reflect the *compressed download size* as calculated by Play when the app is uploaded in Play Console.

You might want to take advantage of [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) or [Play Feature
Delivery](https://developer.android.com/guide/playcore/feature-delivery) for Android XR apps, particularly if your app includes a lot of
large assets. Play Feature Delivery uses advanced capabilities of app bundles,
allowing certain features of your app to be delivered conditionally or
downloaded on demand. Play Asset Delivery is Google Play's solution for
delivering large amounts of game assets, and it offers flexible delivery methods
and high performance.

## Choose a release track for your app

Play Console provides options for how you publish and manage your apps. For
Android XR, there are different [release tracks](https://support.google.com/googleplay/android-developer/answer/13295490) that you might use,
depending on the types of app experiences you're building.

### Choose a release track for apps with augmented experiences

If you're publishing your app's augmented experiences for audio glasses, use the
mobile release track. Play Console doesn't have a dedicated release track for
audio glasses.

You can implement features and content for audio glasses into your existing
mobile APK and publish the same assets on the mobile release track without any
specific publishing changes in Play Console.

### Choose a release track for apps with immersive experiences

If you're building an app with immersive experiences for XR headsets or wired XR
glasses, there are two release tracks you can use:

- **Mobile release track**: The same track that apps use to publish to Android mobile devices like phones and tablets.
- **Dedicated Android XR release track**: A dedicated track for apps and app variants that are exclusively available on Android XR devices.

The release track you choose depends primarily on whether you're adding [spatial
UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), or [spatial environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments) to an existing mobile
app or building a new [XR app](https://developer.android.com/develop/xr/get-started). Read the following sections to help you
decide which release track is right for your app.

#### 1. Spatialize an existing mobile app

Existing apps published on the mobile release track are automatically
discoverable on Google Play for Android XR users, as long as the app doesn't
include any [unsupported features](https://developer.android.com/develop/xr/get-started#unsupported-features) for Android XR.

If you choose to differentiate your mobile app for XR by adding features such as
[spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose), [3D models](https://developer.android.com/design/ui/xr/guides/3d-content), or [spatial environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments), you have two
options for how you can distribute the app to Android XR users. In either case,
use the same package name as your existing app.

##### Continue publishing to the mobile track

In most cases, you can bundle [XR features or content into your existing mobile
APK](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing). You won't need to make any specific publishing changes in Play
Console; you can continue working with your existing APK and publish the same
assets on the mobile release track. Android XR users will receive artifacts from
the mobile release track.

> [!IMPORTANT]
> **Important:** If you use this track, make sure you've correctly [configured the
> `uses-feature` element for `android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) in your app's manifest file.

##### Publish your XR experience to the Android XR dedicated release track

In some situations, your XR app and your mobile app might have significantly
different features or requirements. For example, your XR app might require a
different set of permissions, or it might offer very different functionality
that makes it difficult to refactor it to serve both mobile and XR use cases.

In these cases, you can choose to create a new APK for your XR experience using
the existing registered app entry in Play Console. If you choose this option,
keep the following things in mind:

- The new APK will share a package name with your existing mobile app.
- Your existing mobile app stays published on the mobile track.
- Your new XR variant of the app is published on the Android XR dedicated track.

While this option can provide extra flexibility over your releases, it does have
more overhead, since you have multiple APKs to release and manage.

To publish to the Android XR dedicated track, your app must declare one of the
following features in its manifest, depending on the tools you're using to build
your app:

- **Jetpack XR SDK** : Declare the [`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) feature. For more information about this and other features that you can declare, see the [corresponding section in the Jetpack XR SDK guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#packagemanager-features).
- **Unity, Godot, Unreal Engine, or OpenXR** : Declare the [`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/openxr/get-started#android.software.xr.api.openxr) feature. For more information about this and other features that you can declare, see the [corresponding section
  in the OpenXR guide](https://developer.android.com/develop/xr/openxr/get-started#packagemanager-features).

Apps that are published to the Android XR dedicated track are only visible to
Android XR devices that support either the `android.software.xr.api.spatial` or
`android.software.xr.api.openxr` features.

For more information about using the dedicated release track for Android XR, see
[the Play Console guide](https://support.google.com/googleplay/android-developer/answer/13295490).

#### 2. Build a new XR app

For new apps that are intended solely for XR devices, you should publish
exclusively to the Android XR dedicated track.

To publish to the Android XR dedicated track, your app must declare one of the
following features in its manifest, depending on the tools you're using to build
your app:

- **Jetpack XR SDK** : Declare the [`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#android.software.xr.api.spatial) feature. For more information about this and other features that you can declare, see the [corresponding section in the Jetpack XR SDK guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#packagemanager-features).
- **Unity, Godot, Unreal Engine, or OpenXR** : Declare the [`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/openxr/get-started#android.software.xr.api.openxr) feature. For more information about this and other features that you can declare, see the [corresponding section
  in the OpenXR guide](https://developer.android.com/develop/xr/openxr/get-started#packagemanager-features).

Apps that are published to the Android XR dedicated track are only visible to
Android XR devices that support either the `android.software.xr.api.spatial` or
`android.software.xr.api.openxr` features.

For more information about using the dedicated release track for Android XR, see
[the Play Console guide](https://support.google.com/googleplay/android-developer/answer/13295490).

## Help users discover your app in the Play Store with badges

Depending on the type of XR experiences you're building, your app can get badges
in the Play Store that help users discover your app's high-quality XR
experiences.

### Get a badge for building differentiated immersive experiences

If you're building immersive experiences and your app is [Android XR
differentiated](https://developer.android.com/docs/quality-guidelines/android-xr/immersive#android-xr-differentiated), it automatically gets a "Made for XR" badge in the Play
Store.

### Get a badge for building differentiated augmented experiences

If you're building augmented experiences, you can get a "Differentiated for
Glasses" badge in the Play Store. To receive this badge, [implement a projected
activity for your app's augmented experience](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/first-activity).

## Manage device exclusions

After you've uploaded at least one app bundle to Play Console, you can view the
catalog of available devices and review which devices are compatible with your
app. Visit the [Play Console help center](https://support.google.com/googleplay/android-developer/answer/7353455) to understand how to view and
restrict your app's compatible devices.

> [!NOTE]
> **Note:** If you want to exclude your app from being available on a particular XR device and that device hasn't launched yet, you might not see it in the device catalog in Play Console until closer to its launch.

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