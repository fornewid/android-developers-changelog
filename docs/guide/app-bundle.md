---
title: https://developer.android.com/guide/app-bundle
url: https://developer.android.com/guide/app-bundle
source: md.txt
---

| **Important:** From August 2021, new apps are required to publish with the[Android App Bundle](https://developer.android.com/guide/app-bundle)on Google Play. New apps larger than 200 MB are now supported by either[Play Feature Delivery](https://developer.android.com/guide/app-bundle/dynamic-delivery)or[Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). From June 2023, new and existing[TV apps are required to be published as App Bundles](https://developer.android.com/docs/quality-guidelines/tv-app-quality#SC-E1).

An*Android App Bundle*is a publishing format that includes all your app's compiled code and resources, and defers APK generation and signing to Google Play.

Google Play uses your app bundle to generate and serve optimized APKs for each device configuration, so only the code and resources that are needed for a specific device are downloaded to run your app. You no longer have to build, sign, and manage multiple APKs to optimize support for different devices, and users get smaller, more-optimized downloads.

Most app projects won't require much effort to build app bundles that support serving optimized APKs. If you already[organize your app's code and resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)according to established conventions,[build signed Android App Bundles](https://developer.android.com/studio/publish/app-signing#sign-apk)using Android Studio or by[using the command line](https://developer.android.com/studio/build/building-cmdline), and[upload them to Google Play](https://developer.android.com/studio/publish/upload-bundle), then optimized APK serving becomes an automatic benefit.

When you use the app bundle format to publish your app, you can also optionally take advantage of[Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery), which lets you add*feature modules* to your app project. These modules contain features and resources that are only included with your app based on conditions that you specify, or are available later at runtime for download[Using the Play Core Library](https://developer.android.com/guide/playcore).

Game developers who publish their apps with app bundles can use[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery): Google Play's solution for delivering large amounts of game assets that offers developers flexible delivery methods and high performance.

Watch the following video for an overview of why you should publish your app using Android App Bundles.  

## Compressed download size restriction

Publishing with Android App Bundles helps your users to install your app with the smallest downloads possible and increases the**compressed download size** . That is, when a user downloads your app, the total size of the compressed APKs required to install your app (for example, the base APK + configuration APKs) must be no more than 4 GB. Any subsequent downloads, such as downloading a feature module (and its configuration APKs) on demand, must also meet this compressed download size restriction. Asset packs don't contribute to this size limit, but they do have other[size restrictions](https://developer.android.com/guide/app-bundle/asset-delivery#size-limits).

If the Play Console finds any of the possible downloads of your app or its on demand features to be more than the[maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits), you will get an error.

Keep in mind,**Android App Bundles do not support APK expansion (`*.obb`) files**. So, if you encounter this error when publishing your app bundle, use one of the following resources to reduce compressed APK download sizes:

- Make sure you[enable all configuration APKs](https://developer.android.com/studio/projects/dynamic-delivery#disable_config_apks)by setting`enableSplit = true`for each type of configuration APK. This makes sure that users download only the code and resources they need to run your app on their device.
- Make sure you[shrink your app](https://developer.android.com/studio/build/shrink-code)by removing unused code and resources.
- Follow best practices to further[reduce app size](https://developer.android.com/topic/performance/reduce-apk-size).
- Consider converting features that are used by only some of your users into[feature modules](https://developer.android.com/studio/projects/dynamic-delivery#dynamic_feature_modules)that your app can download later, on demand. Keep in mind, this may require some refactoring of your app, so make sure to first try the other suggestions described.

## Other considerations

The following are known issues when building or serving your app with Android App Bundles. If you experience issues that are not already described here,[report a bug](https://issuetracker.google.com/issues/new?component=398856&template=1084213).

- Partial installs of sideloaded apps---that is, apps that are not installed using the Google Play Store and are missing one or more required split APKs---fail on all Google-certified devices and devices running Android 10 (API level 29) or higher. When downloading your app through the Google Play Store, Google ensures that all required components of the app are installed.
- If you use tools that dynamically modify resource tables, APKs generated from app bundles might behave unexpectedly. So, when building an app bundle, it is recommended that you disable such tools.

- It is possible to configure properties in a feature module's build configuration that conflict with those from the base (or other) modules. For example, you can set`buildTypes.release.debuggable =
  true`in the base module and set it to`false`in a feature module. Such conflicts might cause build and runtime issues. Keep in mind, by default, feature modules inherit some build configurations from the base module. So, make sure you understand which configurations you should keep, and which ones you should omit, in your[feature module build configuration](https://developer.android.com/guide/app-bundle/configure#feature_build_config).

## Additional resources

To learn more about Android App Bundles, consult the following resources.

### Blog posts

- [Building your first App Bundle](https://medium.com/androiddevelopers/building-your-first-app-bundle-bbcd228bf631)
- [What a new publishing format means for the future of Android](https://medium.com/googleplaydev/what-a-new-publishing-format-means-for-the-future-of-android-2e34981793a)
- [New features to help you develop, release, and grow your business on Google Play](https://android-developers.googleblog.com/2019/05/whats-new-in-play.html)
- [The latest Android App Bundle updates including the additional languages API](https://android-developers.googleblog.com/2019/03/the-latest-android-app-bundle-updates.html)
- [Patchwork Plaid --- A modularization story](https://medium.com/androiddevelopers/a-patchwork-plaid-monolith-to-modularized-app-60235d9f212e)
- [Google Santa Tracker --- Moving to an Android App Bundle](https://medium.com/androiddevelopers/google-santa-tracker-moving-to-an-android-app-bundle-dde180716096)
- [Developer tools on Play Console](https://medium.com/androiddevelopers/developer-tools-on-play-store-85fb710ee33b)

### Videos

- [Everything to know about Play App Signing](https://www.youtube.com/watch?v=odv_1fxt9BI)
- [Building your first App Bundle](https://www.youtube.com/watch?v=IPLhLu0kvYw)
- [App Bundles: Testing with Bundletool and the Play Console](https://www.youtube.com/watch?v=vAEAZPU7w-I)
- [Customizable Delivery with the App Bundle and Easy Sharing of Test Builds](https://www.youtube.com/watch?v=flhib2krW7U)
- [New Tools to Optimize Your App's Size and Boost Installs on Google Play](https://www.youtube.com/watch?v=rEuwVWpYBOY)