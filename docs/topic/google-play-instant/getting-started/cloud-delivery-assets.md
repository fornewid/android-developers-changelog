---
title: https://developer.android.com/topic/google-play-instant/getting-started/cloud-delivery-assets
url: https://developer.android.com/topic/google-play-instant/getting-started/cloud-delivery-assets
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

When shrinking your app to fit the size requirements, first try the[standard APK size optimization techniques](https://developer.android.com/topic/google-play-instant/getting-started/game-instant-app#apk-size-reduction). If you need to shrink the size down further, you might need to rely on cloud delivery of assets. This document describes how to prepare assets for cloud delivery and the support options from various game engines. While the guidance on this page focuses on games, the principles apply to any app that contains large assets.

## Preparation

When thinking about breaking up your app for cloud delivery of assets, consider how you can split your app files into sections based on*when*they need to be available to the user. This timing tends to fall into the following three categories: needed always, needed at launch, and needed later.

### Needed always

Some assets are difficult to separate into smaller blocks or are required to be bundled in the base APK. Examples include your game code and its library or engine dependencies. While[Google Play Core supports app bundles for code](https://developer.android.com/guide/app-bundle/playcore), many engines don't support code downloaded later.

### Needed at launch

After the game starts, the user should be able to play immediately. Google Play Instant requires that users can start playing your game in less than 15 seconds over an LTE or 4G connection (see the[Google Play Instant checklist](https://developer.android.com/topic/google-play-instant/tech-requirements#total-download-size)). Therefore, limit any secondary download after launch to be only as large as necessary to support the initial experience. For example, a fast-follow download immediately after launch might include the first game level and location assets, or any code required to run the first few minutes of gameplay.

### Needed later

Anything that you can afford to download later, in the background as needed, will fall into this category. This category includes most assets for long-play games. Downloading these assets later will help decrease the size of your app to as small as possible.

## Engine support

Cloud asset delivery is the primary way to enable your game to go beyond the 15 MB limit for Instant play games. Support for downloading assets will vary based on game engine. See the most common cases below, as well as options for hosting assets.

Note that fewer needed-at-launch assets allow the user to get in the game faster, which translates to lower drop-off and better player retention for that first launch.

### Play Feature Delivery (through App Bundles)

If you publish your app as an app bundle (which is the preferred method), you can use[feature modules](https://developer.android.com/guide/app-bundle/dynamic-delivery#customize_delivery)to fetch additional resources beyond the base APK. For your instant app, each feature module must set`dist:instant="true"`in the manifest. The`dist:on-demand`property should not be used; it is primarily used for on-demand modules in installed APKs. Additionally, each feature module must be under the instant APK limit of 15 MB, regardless of whether or not the module contains code. Failure to keep each module under this limit will prevent publishing to alpha or release tracks. Once properly configured, you can[fetch feature modules at runtime](https://developer.android.com/guide/playcore#request)using the PlayCore library.

### Cocos Creator

Cocos has supported cloud delivery of assets since[version v2.0.4](https://docs.cocos.com/creator/manual/en/publish/publish-android-instant.html). Cocos downloads assets on demand, rendering placeholders if assets haven't been downloaded in time. Cocos generates asset files that must be hosted with some online service as Cocos does not provide one of its own.

### Unity

Cloud delivery is supported in the[Unity Google Play Instant Plugin](https://github.com/google/play-instant-unity-plugin)for Unity versions 5.6, 2017.4, or 2018.2. Later versions of Unity offer more benefits for engine stripping, so they may be beneficial to migrate to in order to free more space. Unity cloud assets are hosted in`AssetBundle`files that Unity creates for you. Uploading these to a cloud server enables cloud delivery of assets, as Unity has innate support for[downloading asset bundles](https://docs.unity3d.com/540/Documentation/Manual/DownloadingAssetBundles.html).

### Other engines

Whether you use a custom engine or a collection of native libraries, your choice might support cloud downloading of assets out of the box. If you have enough assets that you need to download them off of the cloud, then you'll need to code or integrate a way to download assets on demand for your game. The[Firebase Hosting](https://firebase.google.com/docs/hosting/)or[Firebase Cloud Storage APIs](https://firebase.google.com/docs/storage/)are good places to start. Some engines offer simple HTTPS file fetching that might be enough for your needs as well.

## Hosting assets

Unless you're using Google Play[app bundles](https://developer.android.com/guide/app-bundle/playcore)to download your assets through Play, you'll need to host your assets elsewhere. You're free to host them with any service you'd like as long as it has a reasonable global distribution and availability. Google Play Games app users play around the world, so cloud-hosted assets need to be served to them quickly in any location.