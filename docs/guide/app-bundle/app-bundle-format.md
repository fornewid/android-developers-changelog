---
title: https://developer.android.com/guide/app-bundle/app-bundle-format
url: https://developer.android.com/guide/app-bundle/app-bundle-format
source: md.txt
---

# The Android App Bundle format

An Android App Bundle is a file (with the`.aab`file extension) that you upload to Google Play.

App bundles are signed binaries that organize your app's code and resources into modules, as illustrated in figure 1. Code and resources for each module are organized similarly to what you would find in an APK---and that makes sense because each of these modules may be generated as separate APKs. Google Play then uses the app bundle to generate the various APKs that are served to users, such as the base APK, feature APKs, configuration APKs, and (for devices that do not support split APKs) multi-APKs. The directories that are colored in blue---such as the`drawable/`,`values/`, and`lib/`directories---represent code and resources that Google Play uses to create configuration APKs for each module.

![App bundles organize your app into directories that each represent a module. Within each module directory, code and resources are organized similar to that of a typical APK.](https://developer.android.com/static/images/app-bundle/aab_format-2x.png)

**Figure 1.**The contents of an Android App Bundle with one base module, two feature modules, and two asset packs.

<br />

| **Note:** You build an app bundle for each unique app, or applicationID. That is, if you use product flavors to create multiple versions of your app from a single app project, and each of those versions use a unique[applicationID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id), you need to build a separate app bundle for each version of your app.

The following list describes some of the app bundle's files and directories in more detail:

- **base/, feature1/, and feature2/:** Each of these top-level directories represent a different module of your app. The base module for your app is always contained in a`base`directory of the app bundle. However, the directory for each feature module is given the name specified by the`split`attribute in the module's manifest. To learn more, read about the[feature module manifest](https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest).
- **asset_pack_1/ and asset_pack_2/:** For large, graphically-demanding apps or games, you can modularize assets into asset packs. Asset packs are ideal for games due to their large size limits. You can customize how and when each asset pack is downloaded onto a device according to three delivery modes: install-time, fast-follow, and on-demand. All asset packs are hosted on and served from Google Play. To learn more about how to add asset packs to your app bundle, see the[Play Asset Delivery overview](https://developer.android.com/guide/app-bundle/asset-delivery).
- **BUNDLE-METADATA/:**This directory includes metadata files that contain information useful for tools or app stores. Such metadata files may include ProGuard mappings and the complete list of your app's DEX files. Files in this directory are not packaged into your app's APKs.
- **Module Protocol Buffer (`*.pb`) files:** These files provide metadata that helps describe the contents of each app module to app stores, such as Google Play. For example,`BundleConfig.pb`provides information about the bundle itself, such as which version of the build tools were used to build the app bundle, and`native.pb`and`resources.pb`describe the code and resources in each module, which is useful when Google Play optimizes APKs for different device configurations.
- **manifest/:** Unlike APKs, app bundles store the`AndroidManifest.xml`file of each module in this separate directory.
- **dex/:**Unlike APKs, app bundles store the DEX files for each module in this separate directory.
- **res/, lib/, and assets/:**These directories are identical to those in a typical APK. When you upload your app bundle, Google Play inspects these directories and packages only the files that satisfy the target device configuration, while preserving file paths.
- **root/:** This directory stores files that are later relocated to the root of any APK that includes the module that this directory is located in. For example, the`base/root/`directory of an app bundle may include Java-based resources that your app loads using[`Class.getResource()`](https://developer.android.com/reference/java/lang/Class#getResource(java.lang.String)). Those files are later relocated to the root directory of your app's base APK and every multi-APK that Google Play generates. Paths within this directory are also preserved. That is, directories (and their subdirectories) are also relocated to the root of the APK.

  | **Caution:** If the contents in this directory conflict with other files and directories at the root of the APK, Play Console rejects the entire app bundle at upload time. For example, you can not include a`root/lib/`directory because it would conflict with the`lib`directory that each APK already includes.

# Overview of split APKs

A fundamental component of serving optimized applications is the*split APK*mechanism available on Android 5.0 (API level 21) and higher. Split APKs are very similar to regular APKs---they include compiled DEX bytecode, resources, and an Android manifest. However, the Android platform is able to treat multiple installed split APKs as a single app. That is, you can install multiple split APKs that have access to common code and resources, and appear as one installed app on the device.

The benefit of split APKs is the ability to break up a monolithic APK---that is, an APK that includes code and resources for all features and device configurations your app supports---into smaller, discrete packages that are installed on a user's device*as required*.

For example, one split APK may include the code and resources for an additional feature that only a few of your users need, while another split APK includes resources for only a specific language or screen density. Each of these split APKs is downloaded and installed when the user requests it or it's required by the device.

The following describes the different types of APKs that may be installed together on a device to form your full app experience. You'll learn how to configure your app project to support these APKs in later sections on this page.

- **Base APK:**This APK contains code and resources that all other split APKs can access and provides the basic functionality for your app. When a user requests to download your app, this APK is downloaded and installed first. That's because only the base APK's manifest contains a full declaration of your app's services, content providers, permissions, platform version requirements, and dependencies on system features. Google Play generates the base APK for your app from your project's app (or base) module. If you are concerned with reducing your app's initial download size, it's important to keep in mind that all code and resources included in this module are included in your app's base APK.
- **Configuration APKs:** Each of these APKs includes native libraries and resources for a specific screen density, CPU architecture, or language. When a user downloads your app, their device downloads and installs only the configuration APKs that target their device. Each configuration APK is a dependency of either a base APK or feature module APK. That is, they are downloaded and installed along with the APK they provide code and resources for. Unlike the base and feature modules, you don't create a separate module for configuration APKs. If you use standard practices to[organize alternative, configuration-specific resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)for your base and feature modules,**Google Play automatically generates configuration APKs for you**.
- **Feature module APKs:** Each of these APKs contains code and resources for a feature of your app that you modularize using feature modules. You can then customize how and when that feature is downloaded onto a device. For example,[using the Play Core Library](https://developer.android.com/guide/app-bundle/playcore), features may be installed on demand after the base APK is installed on the device to provide additional functionality to the user. Consider a chat app that downloads and installs the ability to capture and send photos only when the user requests to use that functionality. Because feature modules may not be available at install time, you should include any common code and resources in the base APK. That is, your feature module should assume that code and resources of only the base APK are available at install time. Google Play generates feature module APKs for your app from your project's feature modules.

Consider an app with three feature modules and support for multiple device configurations. Figure 1 below illustrates what the dependency tree for the app's various APKs may look like. Note that the base APK forms the head of the tree, and all other APKs depend on the base APK. (If you're curious about how the modules for these APKs are represented in an Android App Bundle, see[The Android App Bundle format](https://developer.android.com/guide/app-bundle/build).)

![The base APK is at the head of the tree with feature module APKs having a dependency on it. Configuration APKs, which include device configuration-specific code and resources for the base and each feature module APK, form the leaf nodes of the dependency tree.](https://developer.android.com/static/images/app-bundle/apk_splits_tree-2x.png)

**Figure 1.**Dependency tree for an app served using split APKs

<br />

Keep in mind, you don't need to build these APKs yourself---Google Play does it for you using a single signed app bundle you build with Android Studio. To learn more about the app bundle format and how to build one, go to[Build, deploy, and upload Android App Bundles](https://developer.android.com/guide/app-bundle/build).

## Devices running Android 4.4 (API level 19) and lower

Because devices running Android 4.4 (API level 19) and lower don't support downloading and installing split APKs, Google Play instead serves those devices a single APK, called a*multi-APK*, that's optimized for the device's configuration. That is, multi-APKs represent your full app experience but do not include unnecessary code and resources---such as those for other screen densities and CPU architectures.

They do, however, include resources for all languages that your app supports. This allows, for example, users to change your app's preferred language setting without having to download a different multi-APK.

Multi-APKs do not have the ability to later download feature modules on demand. To include a feature module in this APK, you must either disable**On-demand** or enable**Fusing** when[creating the feature module](https://developer.android.com/studio/projects/dynamic-delivery#create_dynamic_feature).

Keep in mind, with app bundles, you don't need to build, sign, upload, and manage APKs for each device configuration your app supports. You still build and upload only a single app bundle for your entire app, and Google Play takes care of the rest for you. So whether or not you plan to support devices running Android 4.4 or lower, Google Play provides a flexible serving mechanism for both you and your users.

## User language changes

With app bundles, devices download only the code and resources they require to run your app. So, for language resources, a user's device downloads only your app's language resources that match the one or more languages currently selected in the device's settings.

When a user switches their language in the device settings, Google Play may need to download and install some additional split APKs before the app can be displayed in the new language.

Google Play tries to download the additional languages immediately after the switch. If the user device is offline, the download fails, or the resources are too large, Google Play attempts the download again in the background when the device conditions are more favourable. When running on a device with Android 9.0 (API level 28) or lower, if your app is in the foreground during the installation of the new language split APKs, then the app is killed.

If your app requires all languages to be available on the device at any time, you can[disable language splitting in your build configuration](https://developer.android.com/guide/app-bundle/configure-base#disable_config_apks).

If your app requires downloading additional languages independently from the user languages selected in the device settings---for instance to implement an in-app language picker---you can use the Play Core library to[download them on demand](https://developer.android.com/guide/playcore/feature-delivery/on-demand#lang_resources).