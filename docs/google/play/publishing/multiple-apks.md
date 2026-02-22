---
title: https://developer.android.com/google/play/publishing/multiple-apks
url: https://developer.android.com/google/play/publishing/multiple-apks
source: md.txt
---

# Multiple APK support

If you publish your app to Google Play, you should build and upload an[Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. Publishing multiple APKs is useful if you are not publishing to Google Play, but you must build, sign, and manage each APK yourself.

Multiple APK support is a feature on Google Play that allows you to publish different APKs for your application that are each targeted to different device configurations. Each APK is a complete and independent version of your application, but they share the same application listing on Google Play and must share the same package name and be signed with the same release key. This feature is useful for cases in which your application cannot reach all desired devices with a single APK.

Android-powered devices may differ in several ways and it's important to the success of your application that you make it available to as many devices as possible. Android applications usually run on most compatible devices with a single APK, by supplying alternative resources for different configurations (for example, different layouts for different screen sizes) and the Android system selects the appropriate resources for the device at runtime. In a few cases, however, a single APK is unable to support all device configurations, because alternative resources make the APK file too big or other technical challenges prevent a single APK from working on all devices.

To help you publish your application for as many devices as possible, Google Play allows you to publish multiple APKs under the same application listing. Google Play then supplies each APK to the appropriate devices based on configuration support you've declared in the manifest file of each APK.

By publishing your application with multiple APKs, you can:

- Support different OpenGL texture compression formats with each APK.
- Support different screen sizes and densities with each APK.
- Support different device feature sets with each APK.
- Support different platform versions with each APK.
- Support different CPU architectures with each APK (such as for ARM or x86, when your app uses the[Android NDK](https://developer.android.com/tools/sdk/ndk)).
- Optimize for entry-level devices such as those running Android (Go edition).

Currently, these are the only device characteristics that Google Play supports for publishing multiple APKs as the same application.

**Note:** To learn about preparing and publishing APKs on Google Play, see the[Prepare \& roll-out releases](https://support.google.com/googleplay/android-developer/answer/7159011)support article.

## How multiple APKs work

The concept for using multiple APKs on Google Play is that you have just one entry in Google Play for your application, but different devices might download a different APK. This means that:

- You maintain only one set of product details (app description, icons, screenshots, etc.). This also means you*cannot*charge a different price for different APKs.
- All users see only one version of your application on Google Play, so they are not confused by different versions you may have published that are "for tablets" or "for phones."
- All user reviews are applied to the same application listing, even though users on different devices may have different APKs.
- If you publish different APKs for different versions of Android (for different API levels), then when a user's device receives a system update that qualifies them for a different APK you've published, Google Play updates the user's application to the APK designed for the higher version of Android. Any system data associated with the application is retained (the same as with normal application updates when using a single APK).

### Supported filters

Which devices receive each APK is determined by[Google Play filters](https://developer.android.com/google/play/filters)that are specified by elements in the manifest file of each APK. However, Google Play allows you to publish multiple APKs only when each APK uses filters to support a variation of the following device characteristics:

- **OpenGL texture compression formats**

  This is based on your manifest file's[`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element)element(s).

  For example, when developing a game that uses OpenGL ES, you can provide one APK for devices that support ATI texture compression and a separate APK for devices that support PowerVR compression (among many others).
- **Screen size (and, optionally, screen density)**

  This is based on your manifest file's[`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element)*or* [`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element)element. You should never use both elements and you should use only[`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element)when possible.

  For example, you can provide one APK that supports small and normal size screens and another APK that supports large and xlarge screens. To learn more about generating separate APKs based on screen size or density, go to[Build Multiple APKs](https://developer.android.com/studio/build/configure-apk-splits).

  Consider the following best practices to support all screen sizes:
  - The Android system provides strong support for applications to support all screen configurations with a single APK. You should avoid creating multiple APKs to support different screens unless absolutely necessary and instead follow the guide to[Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support)so that your application is flexible and can adapt to all screen configurations with a single APK.
  - By default, all screen size attributes in the[`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element)element are "true" if you do not declare them otherwise. However, because the`android:xlargeScreens`attribute was added in Android 2.3 (API level 9), Google Play will assume that it is "false" if your application does not set either[`android:minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)or[`android:targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)to "9" or higher.
  - You should not combine both[`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element)and[`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element)elements in your manifest file. Using both increases the chances that you'll introduce an error due to conflicts between them. For help deciding which to use, read[Distributing to Specific Screens](https://developer.android.com/guide/practices/screens-distribution). If you can't avoid using both, be aware that for any conflicts in agreement between a given size, "false" will win.

  <br />

- **Device feature sets**

  This is based on your manifest file's[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element(s).

  For example, you can provide one APK for devices that support multitouch and another APK for devices that do not support multitouch. See[Features Reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference)for a list of features supported by the platform.
- **Android (Go edition)**

  To target devices running Android (Go edition), your APK needs to declare`<uses-feature android:name="android.hardware.ram.low" android:required="true">`, target at least API Level 26, and have a higher version code than your non-Go edition APK.
- **API level**

  This is based on your manifest file's[`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element)element. You can use both the[`android:minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)and[`android:maxSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#max)attributes to specify support for different API levels.

  For example, you can publish your application with one APK that supports API levels 16 - 19 (Android 4.1.x - 4.4.4)---using only APIs available since API level 16 or lower---and another APK that supports API levels 21 and above (Android 5.0+)---using APIs available since API level 21 or lower. To learn how to build separate APKs that each target a different range of APIs, go to[Configure Product Flavors](https://developer.android.com/studio/build/build-variants#product-flavors).

  If you use this characteristic as the factor to distinguish multiple APKs, then the APK with a higher[`android:minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)value must have a higher[`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)value. This is also true if two APKs overlap their device support based on a different supported filter. This ensures that when a device receives a system update, Google Play can offer the user an update for your application (because updates are based on an increase in the app version code). This requirement is described further in the section below about[Rules for multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks#Rules).

  You should avoid using[`android:maxSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#max)in general, because as long as you've properly developed your application with public APIs, it is always compatible with future versions of Android. If you want to publish a different APK for higher API levels, you still do not need to specify the maximum version, because if the[`android:minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)is`"16"`in one APK and`"21"`in another, devices that support API level 21 or higher will always receive the second APK (because its version code is higher, as per the previous note).

- **CPU architecture (ABI)**

  Some native libraries provide separate packages for specific CPU architectures, or[Application Binary Interfaces (ABIs)](https://developer.android.com/ndk/guides/abis). Instead of packaging all available libraries into one APK, you can build a separate APK for each ABI and include only the libraries you need for that ABI. To learn more about generating separate APKs based on target ABI, go to[Build Multiple APKs](https://developer.android.com/studio/build/configure-apk-splits).

Other manifest elements that enable[Google Play filters](https://developer.android.com/google/play/filters)---but are not listed above---are still applied for each APK as usual. However, Google Play does not allow you to publish separate APKs based on variations of those device characteristics. Thus, you cannot publish multiple APKs if the above listed filters are the same for each APK (but the APKs differ based on other characteristics in the manifest or APK). For example, you cannot provide different APKs that differ purely on the[`<uses-configuration>`](https://developer.android.com/guide/topics/manifest/uses-configuration-element)characteristics.

### Rules for multiple APKs

Before you publish multiple APKs for your application, you need to understand the following rules:

- All APKs you publish for the same application**must have the same package name and be signed with the same certificate key**.
- Each APK**must have a different version code** , specified by the[`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)attribute.
- Each APK**must not exactly match the configuration support of another APK** .

  That is, each APK must declare slightly different support for at least one of the[supported Google Play filters](https://developer.android.com/google/play/publishing/multiple-apks#SupportedFilters)(listed above).

  Usually, you will differentiate your APKs based on a specific characteristic (such as the supported texture compression formats), and thus, each APK will declare support for different devices. However, it's OK to publish multiple APKs that overlap their support slightly. When two APKs do overlap (they support some of the same device configurations), a device that falls within that overlap range will receive the APK with a higher version code (defined by[`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)).
- You cannot activate a new APK that has a version code lower than that of the APK it's replacing. For example, say you have an active APK for screen sizes small - normal with version code`0400`, then try to replace it with an APK for the same screen sizes with version code`0300`. This raises an error, because it means users of the previous APK will not be able to update the application.
- An APK that requires a**higher API level** must have a**higher version code** .

  This is true only when either: the APKs differ based*only* on the supported API levels (no other[supported filters](https://developer.android.com/google/play/publishing/multiple-apks#SupportedFilters)distinguish the APKs from each other)*or*when the APKs do use another supported filter, but there is an overlap between the APKs within that filter.

  This is important because a user's device receives an application update from Google Play only if the version code for the APK on Google Play is higher than the version code of the APK currently on the device. This ensures that if a device receives a system update that then qualifies it to install the APK for higher API levels, the device receives an application update because the version code increases.

  **Note:**The size of the version code increase is irrelevant; it simply needs to be larger in the version that supports higher API levels.

  Here are some examples:
  - If an APK you've uploaded for API levels 16 and above (Android 4.1.x+) has a version code of`0400`, then an APK for API levels 21 and above (Android 5.0+) must be`0401`or greater. In this case, the API level is the only supported filter used, so the version codes**must increase**in correlation with the API level support for each APK, so that users get an update when they receive a system update.
  - If you have one APK that's for API level 16 (and above)*and* small - large screens, and another APK for API level 21 (and above)*and* large - xlarge screens, then the version codes**must increase**in correlation with the API levels. In this case, the API level filter is used to distinguish each APK, but so is the screen size. Because the screen sizes overlap (both APKs support large screens), the version codes must still be in order. This ensures that a large screen device that receives a system update to API level 21 will receive an update for the second APK.
  - If you have one APK that's for API level 16 (and above)*and* small - normal screens, and another APK for API level 21 (and above)*and* large - xlarge screens, then the version codes**do not need to increase**in correlation with the API levels. Because there is no overlap within the screen size filter, there are no devices that could potentially move between these two APKs, so there's no need for the version codes to increase from the lower API level to the higher API level.
  - If you have one APK that's for API level 16 (and above)*and* ARMv7 CPUs, and another APK for API level 21 (and above)*and* ARMv5TE CPUs, then the version codes**must increase** in correlation with the API levels. In this case, the API level filter is used to distinguish each APK, but so is the CPU architecture. Because an APK with ARMv5TE libraries is compatible with devices that have an ARMv7 CPU, the APKs overlap on this characteristic. As such, the version code for the APK that supports API level 21 and above must be higher. This ensures that a device with an ARMv7 CPU that receives a system update to API level 21 will receive an update for the second APK that's designed for API level 21. However, because this kind of update results in the ARMv7 device using an APK that's not fully optimized for that device's CPU, you should provide an APK for both the ARMv5TE and the ARMv7 architecture at each API level in order to optimize the app performance on each CPU.**Note:** This applies*only*when comparing APKs with the ARMv5TE and ARMv7 libraries, and not when comparing other native libraries.

Failure to abide by the above rules results in an error on the Google Play Console when you activate your APKs---you will be unable to publish your application until you resolve the error.

There are other conflicts that might occur when you activate your APKs, but which will result in warnings rather than errors. Warnings can be caused by the following:

- When you modify an APK to "shrink" the support for a device's characteristics and no other APKs support the devices that then fall outside the supported range. For example, if an APK currently supports small and normal size screens and you change it to support only small screens, then you have shrunk the pool of supported devices and some devices will no longer see your application on Google Play. You can resolve this by adding another APK that supports normal size screens so that all previously-supported devices are still supported.
- When there are "overlaps" between two or more APKs. For example, if an APK supports screen sizes small, normal, and large, while another APK supports sizes large and xlarge, there is an overlap, because both APKs support large screens. If you do not resolve this, then devices that qualify for both APKs (large screen devices in the example) will receive whichever APK has the highest version code.**Note:** If you're creating separate APKs for different CPU architectures, be aware that an APK for ARMv5TE will overlap with an APK for ARMv7. That is, an APK designed for ARMv5TE is compatible with an ARMv7 device, but the reverse is not true (an APK with only the ARMv7 libraries is*not*compatible with an ARMv5TE device).

When such conflicts occur, you will see a warning message, but you can still publish your application.

## Creating multiple APKs

Once you decide to publish multiple APKs, you probably need to create separate Android projects for each APK you intend to publish so that you can appropriately develop them separately. You can do this by simply duplicating your existing project and give it a new name. (Alternatively, you might use a build system that can output different resources---such as textures---based on the build configuration.)

**Tip:** One way to avoid duplicating large portions of your application code is to use a[library project](https://developer.android.com/tools/projects#LibraryProjects). A library project holds shared code and resources, which you can include in your actual application projects.

When creating multiple projects for the same application, it's a good practice to identify each one with a name that indicates the device restrictions to be placed on the APK, so you can easily identify them. For example, "HelloWorld_21" might be a good name for an application designed for API level 21 and above.

**Note:** All APKs you publish for the same application**must have the same package name and be signed with the same certificate key** . Be sure you also understand each of the[Rules for multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks#Rules).

### Assigning version codes

Each APK for the same application**must have a unique version code** , specified by the[`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)attribute. You must be careful about assigning version codes when publishing multiple APKs, because they must each be different, but in some cases, must or should be defined in a specific order, based on the configurations that each APK supports.

#### Ordering version codes

An APK that requires a higher API level must usually have a higher version code. For example, if you create two APKs to support different API levels, the APK for the higher API levels must have the higher version code. This ensures that if a device receives a system update that then qualifies it to install the APK for higher API levels, the user receives a notification to update the app. For more information about how this requirement applies, see the section above about[Rules for multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks#Rules).

You should also consider how the order of version codes might affect which APK your users receive either due to overlap between coverage of different APKs or future changes you might make to your APKs.

For example, if you have different APKs based on screen size, such as one for small - normal and one for large - xlarge, but foresee a time when you will change the APKs to be one for small and one for normal - xlarge, then you should make the version code for the large - xlarge APK be higher. That way, a normal size device will receive the appropriate update when you make the change, because the version code increases from the existing APK to the new APK that now supports the device.

Also, when creating multiple APKs that differ based on support for different OpenGL texture compression formats, be aware that many devices support multiple formats. Because a device receives the APK with the highest version code when there is an overlap in coverage between two APKs, you should order the version codes among your APKs so that the APK with the preferred compression format has the highest version code. For example, you might want to perform separate builds for your app using PVRTC, ATITC, and ETC1 compression formats. If you prefer these formats in this exact order, then the APK that uses PVRTC should have the highest version code, the APK that uses ATITC has a lower version code, and the version with ETC1 has the lowest. Thus, if a device supports both PVRTC and ETC1, it receives the APK with PVRTC, because it has the highest version code.

In case Google Play Store is unable to identify the correct APK to install for a target device, you may want to also create a*universal* APK that includes resources for all the different device variations you want to support. If you do provide a universal APK, you should assign it the lowest`versionCode`. Because Google Play Store installs the version of your app that is both compatible with the target device and has the highest`versionCode`, assigning a lower`versionCode`to the universal APK ensures that Google Play Store tries to install one of your other APKs before falling back to the larger universal APK.

#### Using a version code scheme

In order to allow different APKs to update their version codes independent of others (for example, when you fix a bug in only one APK, so don't need to update all APKs), you should use a scheme for your version codes that provides sufficient room between each APK so that you can increase the code in one without requiring an increase in others. You should also include your actual version name in the code (that is, the user visible version assigned to[`android:versionName`](https://developer.android.com/guide/topics/manifest/manifest-element#vname)), so that it's easy for you to associate the version code and version name.

**Note:**When you increase the version code for an APK, Google Play will prompt users of the previous version to update the application. Thus, to avoid unnecessary updates, you should not increase the version code for APKs that do not actually include changes.

We suggest using a version code with at least 7 digits: integers that represent the supported configurations are in the higher order bits, and the version name (from[`android:versionName`](https://developer.android.com/guide/topics/manifest/manifest-element#vname)) is in the lower order bits. For example, when the application version name is 3.1.0, version codes for an API level 4 APK and an API level 11 APK would be something like 0400310 and 1100310, respectively. The first two digits are reserved for the API Level (4 and 11, respectively), the middle two digits are for either screen sizes or GL texture formats (not used in these examples), and the last three digits are for the application's version name (3.1.0). Figure 1 shows two examples that split based on both the platform version (API Level) and screen size.
![](https://developer.android.com/static/images/market/version-codes.png)

**Figure 1.**A suggested scheme for your version codes, using the first two digits for the API Level, the second and third digits for the minimum and maximum screen size (1 - 4 indicating each of the four sizes) or to denote the texture formats and the last three digits for the app version.

This scheme for version codes is just a suggestion for how you should establish a pattern that is scalable as your application evolves. In particular, this scheme doesn't demonstrate a solution for identifying different texture compression formats. One option might be to define your own table that specifies a different integer to each of the different compression formats your application supports (for example, 1 might correspond to ETC1 and 2 is ATITC, and so on).

You can use any scheme you want, but you should carefully consider how future versions of your application will need to increase their version codes and how devices can receive updates when either the device configuration changes (for example, due to a system update) or when you modify the configuration support for one or several of the APKs.