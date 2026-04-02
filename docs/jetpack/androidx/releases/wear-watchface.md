---
title: https://developer.android.com/jetpack/androidx/releases/wear-watchface
url: https://developer.android.com/jetpack/androidx/releases/wear-watchface
source: md.txt
---

# Wear Watchface

[User Guide](https://developer.android.com/training/wearables) [Code Sample](https://github.com/android/wear-os-samples) API Reference  
[androidx.wear.watchface](https://developer.android.com/reference/kotlin/androidx/wear/watchface/package-summary)  
Create applications for Wear OS by Google smartwatches. **Note:**As of January 2026, the Watch Face Format is required for
installing watch faces on all Wear OS devices.

Learn more about the user-facing changes in this
[Help Center
article](https://support.google.com/wearos/thread/284572445).

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/wear-watchface#1.3.0) | - | - | - |

## Declaring dependencies

To add a dependency on Wear, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement wear watchfaces
    implementation "androidx.wear.watchface:watchface:1.3.0"

    // Use to implement wear watchface complications
    implementation "androidx.wear.watchface:watchface-complications-data-source:1.3.0"
    // (Kotlin-specific extensions)
    implementation "androidx.wear.watchface:watchface-complications-data-source-ktx:1.3.0"

    // Use to implement a watchface style and complication editor
    implementation "androidx.wear.watchface:watchface-editor:1.3.0"

    // Can use to render complications.
    // This library is optional and watchfaces may have custom implementation for rendering
    // complications.
    implementation "androidx.wear.watchface:watchface-complications-rendering:1.3.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement wear watchfaces
    implementation("androidx.wear.watchface:watchface:1.3.0")

    // Use to implement wear watchface complications
    implementation "androidx.wear.watchface:watchface-complications-data-source:1.3.0"
    // (Kotlin-specific extensions)
    implementation "androidx.wear.watchface:watchface-complications-data-source-ktx:1.3.0"

    // Use to implement a watchface style and complication editor
    implementation("androidx.wear.watchface:watchface-editor:1.3.0")

    // Can use to render complications.
    // This library is optional and watchfaces may have custom implementation for rendering
    // complications.
    implementation "androidx.wear.watchface:watchface-complications-rendering:1.3.0"
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1112371+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1112371&template=1623658)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.3

### Version 1.3.0

February 25, 2026

`androidx.wear.watchface:watchface-*:1.3.0` is released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/264b14bca26ab6294c17da770ce57440099d1e4a..c23098949847d0672c4b37c6ccd58d14c6426402/wear/watchface).

**Important changes since 1.2.0:**

- The wear watchface APIs (watchface, watchface-client, watchface-client-guava, watchface-complications-rendering, watchface-data, watchface-editor, watchface-editor-guava, and watchface-style) have been deprecated in favor of the [Wear Watchface Format](https://developer.android.com/training/wearables/wff), and will eventually be removed from AndroidX. The complication APIs are not deprecated and will remain. ([Ice960](https://android-review.googlesource.com/#/q/Ice960baec89d1ff8ace8faf6425daeb4907bd548))
- Added support for static complication previews ([8b2bed3](https://android-review.googlesource.com/#/q/Ic9f861ad0bdb6778c43843eea107a047ec6f68f8))
- The utility class `ComplicationTextFormatting` has been added with support for formatting data and time as tersely as possible, which is useful for complications where space is very much at a premium.

### Version 1.3.0-rc01

January 28, 2026

`androidx.wear.watchface:watchface-*:1.3.0-rc01` is released. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/wear/watchface)

**New Features**

- Add support for static previews of complications ([8b2bed3](https://android-review.googlesource.com/#/q/Ic9f861ad0bdb6778c43843eea107a047ec6f68f8))

### Version 1.3.0-beta01

December 17, 2025

`androidx.wear.watchface:watchface-*:1.3.0-beta01` is released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c62efc9d16e01f166fe7c1393c38c6d547a5e4db..706f6038fb9429bb5809ff499418735f4cd27762/wear/watchface).

**New Features**

- Support for static complication preview data has been added, where a complication provider can specify static preview data in its manifest, see `androidx.wear.watchface.complications.data.parser.StaticPreviewDataParser` for more details.
- The utility class `ComplicationTextFormatting` has been added with support for formatting data and time as tersely as possible, which is useful for complications where space is very much at a premium.

**API Changes**

- Previously experimental property `Renderer.watchfaceColors` is now private. There are still public accessors for this property. ([Ifdf60](https://android-review.googlesource.com/#/q/Ifdf601af297d2e47a53e3254cefc6c7bd440210b), [b/409363281](https://issuetracker.google.com/issues/409363281))

**Bug Fixes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([I48968](https://android-review.googlesource.com/#/q/I48968aff6dc3022a57acab24a7f4bf152e3ed729), [b/407632515](https://issuetracker.google.com/issues/407632515))

### Version 1.3.0-alpha07

April 23, 2025

`androidx.wear.watchface:watchface-*:1.3.0-alpha07` is released. Version 1.3.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..c62efc9d16e01f166fe7c1393c38c6d547a5e4db/wear/watchface).

**New Features**

- It's been possible to define a watch face's UserStyle schema for a while, and it's possible to define `ColorUserStyleSetting` in XML.

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Added the Watch Face Push API which allows a Wear OS app to install a watch face on a watch programmatically.

**Bug Fixes**

- Complication providers using 1.3.0-alpha06 are encouraged to upgrade because a crash bug with `ComplicationDataSourceUpdateRequester` on the next version of WearOS has been fixed.

### Version 1.3.0-alpha06

March 26, 2025

`androidx.wear.watchface:watchface-*:1.3.0-alpha06` is released. Version 1.3.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..78132378b67c86698d1ade3dc368c9f15d738a71/wear/watchface).

**New Features**

- The wear watchface APIs (watchface, watchface-client, watchface-client-guava, watchface-complications-rendering, watchface-data, watchface-editor, watchface-editor-guava, and watchface-style) have been depreciated in favor of the [Wear Watchface Format](https://developer.android.com/training/wearables/wff.), and will eventually be removed from AndroidX. The complication APIs are not deprecated and will remain. ([Ice960](https://android-review.googlesource.com/#/q/Ice960baec89d1ff8ace8faf6425daeb4907bd548))
- The complication APIs are now able to communicate with `WearSDK` directly, which is more efficient due to fewer IPC hops.

### Version 1.3.0-alpha05

January 15, 2025

`androidx.wear.watchface:watchface-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..ad66672b42ec1e9359219e82b7f8189d03df40f5/wear/watchface).

**New Features**

Watch faces commonly allow the user to select colors using a `ListUserStyle`. While this works, it entails sending the icons over bluetooth to the companion editor which is inefficient, so we've introduced `ColorUserStyleSetting` where the payload is a list of one or more color per style which has a significantly more compact wire format.

We've added an OEM facing feature which allows OEM complication providers to add extras to ComplicationData for use by OEM watch faces.

**API Changes**

- `UserStyleSetting` and `UserStyleOption` classes now have builders which is the recommended way to construct them. ([Iacd03](https://android-review.googlesource.com/#/q/Iacd0336fd747dc354a60924e4195ad3d6c5c1b5b))
- Support for passing extras in `ComplicationData`. This is intended for use by OEMs where they control both the complication provider and the receiving watch face. Setting an extra requires the privileged `com.google.android.wearable.permission.COMPLICATION_EXTRAS` permission. ([I4e3b2](https://android-review.googlesource.com/#/q/I4e3b284dbbe0389a3a777f7f71adc2e9cbaf325b))
- Watch faces commonly allow the user to select colors using a `ListUserStyle`, with an icon for each `ListOption`. Since `UserStyle` schemas are sent over bluetooth, it is important to keep the size of the schema down which can be a problem if many dozens of color options are given due to all those icons. To help with this we've added `ColorUserStyleSetting` where the option contains a list of colors instead of an icon, which is much more compact. ([Ib542e](https://android-review.googlesource.com/#/q/Ib542e56a78ed0729795319a5b48447407cafc3a7))
- `ColorUserStyleSetting` and `ColorOption` require API 34 for use. ([I8771d](https://android-review.googlesource.com/#/q/I8771d0012b5e64971ba21018c9ed3df6ddad517e))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ifd363](https://android-review.googlesource.com/#/q/Ifd3632fe9756f9ba77e8191b82b816575e18c78e), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.3.0-alpha04

September 18, 2024

`androidx.wear.watchface:watchface-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..0431b84980e97d6bafdfda7c9038bc4d9529564f/wear/watchface).

**New Features**

- Added support for lazy loading of icons in `UserStyleSettings` and `UserStyleOptions` which is a performance win for loading watch faces. ([Iaf43d](https://android-review.googlesource.com/#/q/Iaf43d401f17a1cca4d1f3a48e363e14fa19c8bcd))
- Added an option for an updated screenshot to be taken whenever the system configuration changes (e.g. if the locale changed) via the new `Watchface.setUpdateScreenshotOnConfigurationChange`. By default this setting is off. ([I765a1](https://android-review.googlesource.com/#/q/I765a12a4e28f1b291c74b414e0527262ff95137a))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.3.0-alpha03

April 17, 2024

`androidx.wear.watchface:watchface-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/wear/watchface).

**API Changes**

- We've added `EditorSession#setOverrideComplications` which temporarily sets the underlying watchface instance's `ComplicationData` while editing. If complications change infrequently, this is more efficient than passing overrides in via `EditorSession#renderWatchFaceToBitmap`. ([I19384](https://android-review.googlesource.com/#/q/I1938467eb317da3e52e11e4492dd87e50b8edb19))

**Bug Fixes**

- Previously `selectComplicationDataForInstant` was calling `toApiComplicationData` for any timelines, meaning the subsequent === reference equality test would always fail. This meant complications were getting reloaded every frame leading to battery drain. ([717406](https://android.googlesource.com/platform/frameworks/support/+/7174060e4e6b92d0c3fea121a841281258793750))

### Version 1.3.0-alpha02

April 3, 2024

`androidx.wear.watchface:watchface-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..02b55f664eba38e42e362e1af3913be1df552d55/wear/watchface).

**New Features**

- We now use reference equality to compare best and `selectedData` because the equals operator is expensive. ([446b00](https://android.googlesource.com/platform/frameworks/support/+/446b00efc083c96976221e1818bc11b08fda971c))

**API Changes**

- We've added a no-fallback dynamic API for `GoalProgressComplicationData`. ([c33264](https://android.googlesource.com/platform/frameworks/support/+/c33264b62f59d6e613fe3553447b9460d619386e))

### Version 1.3.0-alpha01

February 7, 2024

`androidx.wear.watchface:watchface-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/264b14bca26ab6294c17da770ce57440099d1e4a..ca2a8cf8da3a3502fccc593974f8085653e38261/wear/watchface)

**New Features**

- `WatchFaceServices` can be initialized concurrently and as such they should be stateless, to support this we've added `StatefulWatchFaceService` in which a user defined extra created by `createExtra()` is passed into all the overrides called during initialization.
- `GlesRenderer2` now has a constructor overload which lets you specify a list of attributes to try in turn with `eglChooseConfig`.

**API Changes**

- `StatefulWatchFaceService` now supports an override of `getComplicationSlotInflationFactory` into which the user-defined extra created by `createExtra()` is passed. ([I82d9f](https://android-review.googlesource.com/#/q/I82d9f7d994b6a4a59ebee5eb6f749c701ccbad72))
- Some watch faces need to share auxiliary data created during `createUserStyleSchema` with the other initialisation methods. Because there wasn't a better alternative, developers typically made their `WatchFaceServices` stateful. This is dangerous because multiple instances can be created concurrently which can lead to bugs. To resolve this we've introduced `StatefulWatchFaceService` and `StatefulWatchFaceRuntimeService` where a user defined type is created by `createExtra()` and is passed to the various create methods as a parameter. ([If8a99](https://android-review.googlesource.com/#/q/If8a99fe4191237c14cf1e61bf326272295d2252a))
- We've added `getUserStyleFlavors` to `InteractiveWatchFaceClient`, which is of interest primarily for OEMs. ([I0f5d8](https://android-review.googlesource.com/#/q/I0f5d832b593c47769ea1c8680db7ac6248027d54))
- `GlesRenderer2` now has a constructor overload which lets you specify a list of attributes to try in turn with `eglChooseConfig`. This for example allows you to first try a config with anti-aliasing and to fallback to one without if needed. ([I1ba74](https://android-review.googlesource.com/#/q/I1ba74980b959ff3d598f2a36ff55025b507cc3da))
- From Android U, support for `SystemDataSources.DATA_SOURCE_HEART_RATE` will be added to WearOS. This complication is only guaranteed to support `SHORT_TEXT` complications, but it's recommended for the `ComplicationSlot` to accept `SMALL_IMAGE` too because OEMs may choose to serve a shortcut to their health app instead of the live value. ([I34223](https://android-review.googlesource.com/#/q/I3422313b7d1d8e7f9683ab6ddc9eed59fc96c01b))
- We've added `METADATA_KEY_CONFIG_RESTORE_SUPPORTED` which from Android U onwards, controls what happens when the system is restored from a backup for complication data source with `METADATA_KEY_DATA_SOURCE_CONFIG_ACTION`. By default the system assumes that the complication data source service supports backup of any configuration data, but if it does not then it can add metadata setting `METADATA_KEY_DATA_SOURCE_CONFIG_ACTION` to false which will mark the complication slot as not configured. ([I6c505](https://android-review.googlesource.com/#/q/I6c50542be562741c0cafd30b36ac515e4c0702da))

## Version 1.2

### Version 1.2.1

January 24, 2024

`androidx.wear.watchface:watchface-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e601766fcfbbd0dfaf0e3d36ce56bf647d7b100..264b14bca26ab6294c17da770ce57440099d1e4a/wear/watchface)

**Bug Fixes**

- Fixed a crash on Samsung Galaxy Watch 4, 5 \& 6. ([43f0b0](https://android-review.googlesource.com/#/q/43f0b08744875c68454341c7d85cccbe2eddf2a3))

### Version 1.2.0

November 29, 2023

`androidx.wear.watchface:watchface-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87003c5527bd9cba2649e62e397cd8aa2ddc8e19..1e601766fcfbbd0dfaf0e3d36ce56bf647d7b100/wear/watchface)

**Important changes since 1.1.0**

- We've added support some new complication types which are available for use from Android T:
  - `GoalProgressComplicationData` which is similar to `RangedValueComplicationData` except it's for progress towards a goal where min implicitly is zero, and the value is allowed to be larger than `targetValue`.
  - `WeightedElementsComplicationData` which consists of an array of Elements (pairs of weight and color) along with optional text/title/image. These might be displayed as a pie chart where the colors need to be meaningful given the context, since there typically isn't room in a complication to render labels.
- We've added support for optional `ColorRanges` to `RangedValueComplicationData`. Normally complications would be rendered in colors of the watch face's choosing, but sometimes the `ComplicationDataSource` is best placed to set the colors e.g. when they have a particular semantic meaning. E.g. red to blue for temperature.
- Almost every type of `ComplicationData` now supports `SmallImages`.
- We've added `ComplicationDisplayPolicy` where `DO_NOT_SHOW_WHEN_DEVICE_LOCKED` instructs a compatible watch face to not display the complication when the device is locked.
- From Android T, OEMs will be able to determine if a complication request is from a watch face in the list defined by the `android.support.wearable.complications.SAFE_WATCH_FACES` metadata in their provider's manifest by `ComplicationRequest#isForSafeWatchFace`. The provider will need the `com.google.wear.permission.GET_IS_FOR_SAFE_WATCH_FACE` permission to receive anything other than TargetWatchFaceSafety.UNKNOWN\`.
- `UserStyleFlavors` has become a non-experimental feature.

### Version 1.2.0-rc01

October 18, 2023

`androidx.wear.watchface:watchface-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..87003c5527bd9cba2649e62e397cd8aa2ddc8e19/wear/watchface)

### Version 1.2.0-beta02

September 6, 2023

`androidx.wear.watchface:watchface-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/wear/watchface)

**New Features**

- `SuspendingComplicationDataSourceService#onDestroy` is now open. Please note support for a system default weather complication has been removed.

**API Changes**

- Revert "Expose a new data source for weather complications". ([I6f335](https://android-review.googlesource.com/#/q/c3d6476ba224663d7862d0095687267a5845622b))

### Version 1.2.0-beta01

August 23, 2023

`androidx.wear.watchface:watchface-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..3315f1ef094c312203fe26841287902916fbedf5/wear/watchface)

**New Features**

- From Android T, WearOS will now support a default weather system complication.

**API Changes**

- Add weather default system fallback for complications. ([Ia0994](https://android-review.googlesource.com/#/q/Ia0994329edec853a3ff0293ec2cd291556d841c6))
- This patch adds `WatchFaceRuntimeService` and `WatchFaceControlClient.createWatchFaceRuntimeControlClient` along with guava wrappers. These add support for watch face runtimes which are a special kind of watch face that loads it's definition from another package. Currently WearOS only supports the runtime for the [Android Watch Face Format](https://developer.android.com/training/wearables/wff). ([I2799f](https://android-review.googlesource.com/#/q/I2799f9aa593a208ac5b40b768b37d7c072bb91c4))
- This patch is a follow up to [aosp/2636578](https://android-review.googlesource.com/c/platform/frameworks/support/+/2636578) where we rename the int defs so any code depending on `WatchFaceType`, `CanvasType`, `TapType` or `ComplicationsSlotBoundsType` doesn't need to change. ([I4098b](https://android-review.googlesource.com/#/q/I4098ba9d91d7783ada0c1b4e70e18249e0f68bc5))
- Updated API files to annotate compatibility suppression. ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b), [b/287516207](https://issuetracker.google.com/issues/287516207))
- This patch exposes `WatchFaceType` constants in `WatchFaceTypes`, `CanvasType` constants in `CanvasTypes`, `TapType` constants in `TapTypes` and `ComplicationsSlotBoundsType` constants in `ComplicationsSlotBoundsType`. ([I3b85a](https://android-review.googlesource.com/#/q/I3b85afb17aa66668bb1b012c1eb9849b38affeb9), [b/288750666](https://issuetracker.google.com/issues/288750666))
- `WatchFace.OverlayStyle` has very low usage and is not well supported by OEMs so we're depreciating it with intention to remove it at a later date. ([I7344a](https://android-review.googlesource.com/#/q/I7344a08f21f3a2986594288409cea11f4ec0b7d8))

### Version 1.2.0-alpha09

June 21, 2023

`androidx.wear.watchface:watchface-*:1.2.0-alpha09` is released. [Version 1.2.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..3b5b931546a48163444a9eddc533489fcddd7494/wear/watchface)

**New Features**

- `RangedValueComplicationData.Builder` now accepts `DynamicFloat`, and a new `DynamicComplicationText` is available as a subclass of `ComplicationText`, both of which can utilize dynamic expressions as well as platform bindings that are updated at 1hz on supported Wear 4 devices.

**API Changes**

- Added dynamic types for daily distance, daily calories and daily floors. Keys for platform health sources are now under `PlatformHealthSources.Keys` ([Ib7637](https://android-review.googlesource.com/#/q/Ib76376c44708ba49e4ad2253199db176f89972bf))
- Implement `PlatformDataProvider` to provide heart rate and daily steps. `SensorGateway` interface is removed from public API. ([I55b84](https://android-review.googlesource.com/#/q/I55b84b6b9bffc5f0a6b812307f1bd4ad61750d65))
- Rename `StateEntryValue` to `DynamicDataValue`, and update the state APIs to use the `DynamicDataKey`. ([If1c01](https://android-review.googlesource.com/#/q/If1c01335804c5dd98dd2c326ec560e1816ec4c77))
- Add `AppDataKey` for accessing app pushed state; Add `PlatformDataKey` for accessing platform data; Add namespace support in `StateStore`. ([I7985e](https://android-review.googlesource.com/#/q/I7985e7716a77b46a2ea3cee5f9009eead48b96d1))
- `enable`/`disablePlatformSource` methods have been removed from `DynamicTypeEvaluator`. The caller should be responsible for updates. ([I78c6d](https://android-review.googlesource.com/#/q/I78c6ded36efae049d0143eece16054c050a413c8))
- Allow capping the size of bound data types. ([Ie2966](https://android-review.googlesource.com/#/q/Ie29669c5e3fd935de8cad63b3a61d79db582d68f))

### Version 1.2.0-alpha08

April 19, 2023

`androidx.wear.watchface:watchface-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/wear/watchface)

**New Features**

- From Android T, complication providers with the privileged `com.google.wear.permission.GET_IS_FOR_SAFE_WATCH_FACE` may register `androidx.wear.watchface.complications.datasource.SAFE_WATCH_FACE_SUPPORTED_TYPES` metadata which overrides `android.support.wearable.complications.SUPPORTED_TYPES` for safe watch faces. This means a complication provider may choose to serve different types to trusted vs untrusted watchfaces.

**API Changes**

- Propagation of `@Deprecated` class to property ([I882d1](https://android-review.googlesource.com/#/q/I882d15d1d0d17f2227262e682d05d9dc7d082e8a), [b/271441831](https://issuetracker.google.com/issues/271441831))
- Value parameter name for `Enum.valueOf` changed ([Ia9b89](https://android-review.googlesource.com/#/q/Ia9b89b3c1bd0407c9beac825c49477cdfc9c1f2a))
- More thrown exceptions from enum valueOf ([I818fe](https://android-review.googlesource.com/#/q/I818fed80f3a1af1a97b5b0de7882fb2e1b99ae62))
- We've removed `renderWatchFaceToSurface` in favour of `createRemoteWatchFaceView` which is built on top of SurfaceControlViewHost and allows the caller to embed a view from the watch face, which is rendered when the client calls `RemoteWatchFaceViewHost#renderWatchFace`. ([Ib311d](https://android-review.googlesource.com/#/q/Ib311dce2ac383a94cb68492f88cde998f808cd87))
- We've added `renderWatchFaceToSurface` to `InteractiveWatchFaceClient`, `HeadlessWatchFaceClient` and `EditorSession`. Typically this will be more performant than rendering to a bitmap. ([Ieacad](https://android-review.googlesource.com/#/q/Ieacad76ca5461a512affa11a3811c58b531af86c))
- `ObservableStateStore` has been rename to `StateStore`. ([Ieb0e2](https://android-review.googlesource.com/#/q/Ieb0e23bb8e5a09ad260eac5ebe2579407b4f8c14))
- Added `DynamicTypeEvaluator.Builder` instead of constructor arguments to allow more optional arguments, including `ObservableStateStore` which now defaults to an empty store. ([I6f832](https://android-review.googlesource.com/#/q/I6f832cc86bad4e8b226d37e707a8061a5617f4cd))
- Refactored order of parameters in `DynamicTypeEvaluator`. ([Ic1ba4](https://android-review.googlesource.com/#/q/Ic1ba4a23722fdde3380903090fb97db6b3cd3af1))
- Executor has been added to the `DynamicTypeEvaluator.bind` methods. ([I346ab](https://android-review.googlesource.com/#/q/I346ab948e16e89d05f30bcf47bb558995aa26ea2))
- We have added `startEvaluation` method to the `BoundDynamicType` to trigger the evaluation after dynamic type is bound. ([I19908](https://android-review.googlesource.com/#/q/I19908be6191614c6f4beae72f576ea016688be21))
- Complication providers with the privileged `com.google.wear.permission.GET_IS_FOR_SAFE_WATCH_FACE` may register `androidx.wear.watchface.complications.datasource.SAFE_WATCH_FACE_SUPPORTED_TYPES` metadata which overrides `android.support.wearable.complications.SUPPORTED_TYPES` for safe watch faces. ([Id1c73](https://android-review.googlesource.com/#/q/Id1c73337af3bd44e59b5b6d2e6aaf75de774ccd6))
- We've renamed `CustomValueUserStyleSettings2` to `LargeCustomValueUserStyleSettings`. ([Ic17ac](https://android-review.googlesource.com/#/q/Ic17ac7042ba7e2b0fc2c29b8d35fc7e70dfb4532))

**Bug Fixes**

- `DynamicTypeValueReceiver#onPreUpdate` has been removed. ([I2dc35](https://android-review.googlesource.com/#/q/I2dc3582d8e5b586c8c1904ef26fb2f740b3d9d8d))

### Version 1.2.0-alpha07

February 22, 2023

`androidx.wear.watchface:watchface-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..87533b4ff06971ed59028936cd9b6da988cd4522/wear/watchface)

**New Features**

- From Android T, OEMs will be able to determine if a complication request is from a watch face in the list defined by the `android.support.wearable.complications.SAFE_WATCH_FACES` metadata in their provider's manifest by `ComplicationRequest#isForSafeWatchFace`. The provider will need the `com.google.wear.permission.GET_IS_FOR_SAFE_WATCH_FACE` permission to receive anything other than `TargetWatchFaceSafety.UNKNOWN`.

- Also from Android T `CustomValueUserStyleSetting2` is available for use which can hold up to 12.5kb. The previous limit for `CustomValueUserStyleSetting` was 1kb. Despite the increased size limits, watch face developers are encouraged to keep the data small because the settings get sent over bluetooth during editing and bluetooth bandwidth is limited.

**API Changes**

- We've added an optional parameter `eglContextAttribList` to `GlesRenderer` \& `GlesRenderer2` which allows you to set the `EGL14.EGL_CONTEXT_CLIENT_VERSION` passed to `EGL14.eglCreateContext`. ([I2a83e](https://android-review.googlesource.com/#/q/I2a83e7d00b07dcfbb7f17598bf9830136dfd5495))
- We've migrated watch face libs over to `androidx.core.util.Consumer` instead of `java.util.function.Consumer`. ([I273f5](https://android-review.googlesource.com/#/q/I273f5eb562aaef9d37d585e8b6c793b06de6e309))
- More thrown exceptions from KT property accessors ([Iff9d9](https://android-review.googlesource.com/#/q/Iff9d9d0a4dd67d3f89d1a1c480595152357c2a3c))
- We've added `InteractiveWatchFaceClient.isComplicationDisplayPolicySupported` so that the client can determine if it has to emulate support or not on behalf of old watch faces. ([I24c89](https://android-review.googlesource.com/#/q/I24c891bdde9ae97041d21bdc8f45fd0a5eff71ab))
- We've decided that `isForSafeWatchFace` should be a tri-state `IntDef`. ([Ief2f7](https://android-review.googlesource.com/#/q/Ief2f7f793bad4013bc68a2707d554e20199ce2a7))
- For android T we've introduced `ComplicationRequest.isForSafeWatchFace` which is intended for OEM use and it requires `com.google.wear.permission.GET_IS_FOR_SAFE_WATCH_FACE`. For data sources in the system image, this will return true if the requesting watch face is inside the list of safe watchfaces specified by the data source in it's manifest. ([I0cbb6](https://android-review.googlesource.com/#/q/I0cbb640fad087345f5eb0f68fe65b269de70c0c4))
- For android T we've added `CustomValueUserStyleSetting2` which can hold up to 12.5kb. The previous limit for `CustomValueUserStyleSetting` was 1kb. ([I0b100](https://android-review.googlesource.com/#/q/I0b100d3713bbe715a5a09be2dc46d85efaaf83e5))

### Version 1.2.0-alpha06

January 25, 2023

`androidx.wear.watchface:watchface-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/wear/watchface)

**New Features**

- Work is ongoing to add support for complication platform bindings, this isn't ready for use yet, but stay tuned!
- We've added XML `ComplicationSlot` support for the new complication types, GOAL_PROGRESS and WEIGHTED_ELEMENTS.

**Bug Fixes**

- Fixes a leak where the watch face editor was not properly released on Samsung devices. ([3b5987](https://android.googlesource.com/platform/frameworks/support/+/3b598757e0d836d1a135a080a928dc20ceadbc45))
- Fixes a bug where sometimes the complications didn't display properly when switching between a watch face with multiple favorites. ([b38ece](https://android.googlesource.com/platform/frameworks/support/+/b38ece01c6fa322a25719ed93181c8f10b00c764))
- Fixes a serialization bug with perOptionScreenReaderNames that lead to watch face crashes. ([e9f466](https://android.googlesource.com/platform/frameworks/support/+/e9f4665a9b95be6b25c91428a7fb30d9469dded5))

### Version 1.2.0-alpha05

December 7, 2022

`androidx.wear.watchface:watchface-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..4a2f5e696614339c1ac21f706c1a17c0285780e7/wear/watchface)

**New Features**

- A while back we added support for hierarchical `UserStyleSettings`, and from android T it's now possible to have more than one `ComplicationSlotsUserStyleSetting` in a hierarchy. Only one `ComplicationSlotsUserStyleSetting` will be active, based on the user's style selections.

- We're improving screen reader support for `ListOption` and `ComplicationSlotsOption` by adding a `screenReaderName` field, note prior to android T this field will be ignored by companion editors.

**API Changes**

- We've added a new optional `screenReaderName` field to `ListOption` and `ComplicationSlotsOption` for use by editors - will be ignored by companion editors on devices before android T. ([I75326](https://android-review.googlesource.com/#/q/I75326b574ad8fab39af898df547c1848d5723648))
- From android T multiple `ComplicationSlotsUserStyleSettings` are now supported in a style hierarchy as long as at most only one of them can be active at any one time. We've added a utility function `findComplicationSlotsOptionForUserStyle` to `UserStyleSchema` to help find the active `ComplicationSlotsOption` if any. ([Ic2b06](https://android-review.googlesource.com/#/q/Ic2b065c5f6374669b9bd60f26ca061cb38e87460))
- `RangedValuesTypes` have been pulled into `RangedValueComplicationData`'s companion object and renamed to `TYPE_UNDEFINED`, `TYPE_RATING` and a new `TYPE_PERCENTAGE` has been added. ([I55d02](https://android-review.googlesource.com/#/q/I55d020e09fea35f92999d233e1bbf98c89f3613b))
- We've renamed experimental `DynamicFloat` to `FloatExpression` and marked it as `@hide`. ([Idf4f1](https://android-review.googlesource.com/#/q/Idf4f17447cd68b06fbee4d9f5d747e9dffe25428))
- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.2.0-alpha04

November 9, 2022

`androidx.wear.watchface:watchface-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..a1e318590b217ecfce1b2de17eed2f18b6a680bb/wear/watchface)

**New Features**

- For Android T we've added support for two new complication types, `GoalProgressComplicationData` and `WeightedElementsComplicationData`.
- `GoalProgressComplicationData` is similar to `RangedValueComplicationData` but it's value is allowed to go past the target (for `RangedValueComplicationData` the value is clamped to the range \[min .. max\]) which has implications for visual design that might not suit all watch faces.
- `GoalProgressComplicationData` adds support for pie charts and similar breakdowns of simple data.
- We've added optional support for `ColorRamps` to `RangedValueComplicationData`.
- For Android T, We've added `ComplicationPersistencePolicy` and `setCachePolicy` to `ComplicationData` which currently allows a provider to control whether a complication is persisted or not (i.e. whether it's cached past reboot). Most complications won't need to set cache control, but doing so can fix corner cases with stale data for some complications that update frequently (e.g. health data complications). We've also added `ComplicationDisplayPolicy` where `DO_NOT_SHOW_WHEN_DEVICE_LOCKED` instructs a compatible watch face to not display the complication when the device is locked. ([Ic9574](https://android-review.googlesource.com/#/q/Ic9574b2c2055b0f4b8436efc913fe467a8a2ebde))

**API Changes**

- `GoalProgressComplicationData`, `WeightedElementsComplicationData` and `ColorRamp` are no longer experimental. ([Ica9e2](https://android-review.googlesource.com/#/q/Ica9e231f40521a66de83094b64bc9bf9c32dbf54))
- `ComplicationPersistencePolicy` and `ComplicationDisplayPolicy` are now properly marked as T APIs. ([I31d88](https://android-review.googlesource.com/#/q/I31d88c0532699c29b898682325a2ee8e66e3d607))
- The deprecated `ComplicationSlotOverlay` constructor now has `DeprecationLevel.WARNING` allowing it to be called from java once again. ([Ib308c](https://android-review.googlesource.com/#/q/Ib308c1b7b803057c40108ec5aa3251f6367a5f32))
- We've fixed some java compat issues with `ComplicationRequestListener`, `CanvasComplication`, `ComplicationTapFilter` and `InteractiveWatchFaceClient` by annotating them with `@JvmDefaultWithCompatibility` ([Id94fc](https://android-review.googlesource.com/#/q/Id94fcecaf8ff2a98c514fdea194a87c334548fa4))
- We've removed experimental `ProtoLayoutComplicationData` and `ListComplicationData`. The developer story for these was unclear, we hope to revisit in future. ([I9df05](https://android-review.googlesource.com/#/q/I9df05c0e5d405fc37071231de72207a88ae50124))
- We've added a `ValueType` back to `RangedValueComplicationData`. `WeightedElementsComplicationData` now supports a background color. We've removed `DiscreteRangedValueComplicationData` because it's functionality is a subset of `WeightedElementsComplicationData`. ([I6446c](https://android-review.googlesource.com/#/q/I6446c13658ec20c2f93f35393ecea7ff9edc9c8f))

**Bug Fixes**

- Include the `isForScreenShot` in the equals and hash code. Make sure the `onRenderParametersChanged` gets a correct `isForScreenshot` value ([I04a41](https://android-review.googlesource.com/#/q/I04a41ad0d943fa71cffe056c4fd5591cedb298a9))
- Fixed leaks of `WatchFaceControlService` from headless clients. ([e90e00](https://android.googlesource.com/platform/frameworks/support/+/e90e0098e450b78b679c5c94e106739d4fe69db9))

### Version 1.2.0-alpha03

October 5, 2022

`androidx.wear.watchface:watchface-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/wear/watchface)

**New Features**

- No new features, but we have fixed a couple of watch face editor bugs.

**API Changes**

- Deprecated `UserStyleSchema.userStyleSettings` as `rootUserStyleSettings` become non-experimental ([Ie96e3](https://android-review.googlesource.com/#/q/Ie96e3760a4601215a74c6acd6071a68ae20a4f6c))
- Move `rootUserStyleSettings` out of experimental ([I8d6b3](https://android-review.googlesource.com/#/q/I8d6b36c66e2ef0317336bdf7590856fd4d0b5628))
- We've marked `WatchFaceColors` as experimental because it is not supported by all systems ([I6d75d](https://android-review.googlesource.com/#/q/I6d75d5d541082dc14c5d36acac20261ddecfa354))
- Expose `DisconnectReasons` in the public API to make it work with`IntDef`. ([I791f8](https://android-review.googlesource.com/#/q/I791f81d7369ba9c9c1144e5dc009547272ddc147))

**Bug Fixes**

- Close any open on watch editor if `SysUI` dies. If `SysUI` dies and the on watch face editor doesn't close, the watch face could be left in an inconsistent state because the system relies on `SysUI` to persist any user style changes.([ba762a](https://android.googlesource.com/platform/frameworks/support/+/ba762a5889e851761186bf113880402bc921f4bd)
- Fix a memory leak in `ComplicationDataSourceInfoRetriever`, where a kotlin coroutine continuation was acting as a gc root and retaining the editor activity.([33ee06](https://android.googlesource.com/platform/frameworks/support/+/33ee066bbca32c30b8b7c0bc2223b548762c7a9d))

### Version 1.2.0-alpha02

September 21, 2022

`androidx.wear.watchface:watchface-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/wear/watchface)

**New Features**

- Some watch faces have configuration outside of the `UserStyle` that affects it visually, (e.g. selecting a background photo). We've added `Renderer.sendPreviewImageNeedsUpdateRequest` which allows the watch face to request an updated preview image. Note this requires a corresponding system up date to work.

- We've also added an API for watch faces to expose their colors to the system which may choose its color palette based on this. **Note** that this has been made experimental in a follow on patch.

- Just about every type of `ComplicationData` now supports `SmallImages`.

**API Changes**

- Wallpaper manager can sometimes detach from an engine and make another. We've added a `DisconnectReason` int def and extended `ClientDisconnectListener` with a new method which includes a `DisconnectReason`, allowing the listener to observe engine detaches. ([I45cce](https://android-review.googlesource.com/#/q/I45cce0becc240f9f4f270439a74ae6120394b225))
- Added two optional parameters `nameResourceId` and `screenReaderResourceId` to `ComplicationSlotOverlay` constructor ([I157e8](https://android-review.googlesource.com/#/q/I157e82bfb62ee0624731f09f5a6ecccf47c2cdeb))
- We've added a guava wrapper for the new overload of `getOrCreateInteractiveWatchFaceClient` with a `PreviewImageUpdateRequestedListener`. ([Ic31f0](https://android-review.googlesource.com/#/q/Ic31f0c4d2775f9639a642c120b82f56804877a1e))
- We've added `Renderer.sendPreviewImageNeedsUpdateRequest` which is useful for watch faces that have state outside of the `UserStyleSchema` which affects the way they look (e.g. a watch face with a selectable background image). On the client side we've added `PreviewImageUpdateRequestedListener` as an optional parameter to `getOrCreateInteractiveWatchFaceClient` to observe these requests. ([Iff44a](https://android-review.googlesource.com/#/q/Iff44af72ef6d22973fd63137dcc6e4d02f6bff12))
- We've simplified the API for exposing `WatchFaceColors`, now there's a simple property called `watchFaceColors` on the Renderer which the watch face can set, this should be updated as necessary in response to any style changes. Instead of using `WallpaperManager` to observe color changes, we've added `OnWatchFaceColorsListener` to `InteractiveWatchFaceClient`. ([I490bc](https://android-review.googlesource.com/#/q/I490bc09b380728aabb3ce38ef9f3e78b79673b24))
- We've added a `WatchFaceColors` class which holds the three most prominent watch face colors and added open methods `watchfaceColors` \& `notifyWatchFaceColorsChanged` to the Renderer, these allow the system to obtain the colors of the watch face via `WallpaperManager.getWallpaperColors`. ([I3d611](https://android-review.googlesource.com/#/q/I3d6117493efa23eadab4b6dc1dd7f4286edb5168))
- `ShortTextComplicationData`, `RangedValueComplicationData`, `NoPermissionComplicationData` (and experimental `DiscreteRangedValueComplicationData`, `GoalProgressComplicationData` and `WeightedElementsComplicationData`) now all support `SmallImages`. If a watch face chooses to render a complication with multiple colors, it now has the option to use a multi-colored `SmallImage` where previously it would have had to use a monochromatic image. ([I257df](https://android-review.googlesource.com/#/q/I257dfd7a9400ceb0db9c9851ffd88a2d24ffbe45))
- Refactor `PreviewImageUpdateRequestedListener` to be a `Consumer<>` instead ([Ia875d](https://android-review.googlesource.com/#/q/Ia875da3b0b379964240cde4ec0d1c5fb6a69a84d))
- Replace custom Single Abstract Method (SAM) type `OnWatchfaceColorsListener` with generic Java SAM type (Consumer) ([I0c489](https://android-review.googlesource.com/#/q/I0c4896c21c9fd07cbb2089a5dc86e0bf18dfaa72))
- We've deprecated the old `getOrCreateInteractiveWatchFaceClient` and `listenableGetOrCreateInteractiveWatchFaceClient` methods that don't specify a `PreviewImageUpdateRequestedListener`. ([Iec502](https://android-review.googlesource.com/#/q/Iec50236d0feb9df431eab0aafa17a06d7c0fb5af))

**Bug Fixes**

- `DisconnectReason.BINDER_DIED` has been renamed to `DisconnectReason.ENGINE_DIED`. ([I4eb0e](https://android-review.googlesource.com/#/q/I4eb0e93b77f853f692bb0cd1999482d8a3742252))

### Version 1.2.0-alpha01

August 10, 2022

`androidx.wear.watchface:watchface-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0412edaeb003a9619a2239e48e5b208f0398221b..bea814b246f89ff7244e3c6b0648f0b57e47897c/wear/watchface)

**New Features**

- We've added experimental support for various new complication formats. This is an area of active development; these new formats are subject to change without notice and currently there's no renderer support from `CanvasComplicationDrawable`.
- We've also added optional margins to complication slots which make small complications easier to tap on.

**API Changes**

- The experimental `BoundingArc` class is now immutable. ([If624a](https://android-review.googlesource.com/#/q/If624a586111c5a57fe5c8da35f430a8cc5a9fa13))
- Small complications can be tricky to tap on. To help mitigate this, we've introduced support for margins which increase the tappable area without affecting rendering. Unless specified (either in code or via XML) `ComplciationSlots` have zero sized margins. ([I14089](https://android-review.googlesource.com/#/q/I14089309eb6be3ad536c072c8248f65e445ef33b))
- Changed `getComplicationSlotInflationFactory(CurrentUserStyleRepository)` signature to return a non-null factory instance. It was an error to return null before, so this is just making the API contract clearer. ([I0fcc0](https://android-review.googlesource.com/#/q/I0fcc05f693c83f3ea854f0fa5fefe73a4f9d893d))
- We've added `currentUserStyleRepository` argument to the `WatchFaceService.getComplicationSlotInflationFactory` method to be consistent with `createComplicationSlotsManager`. ([I2ddd2](https://android-review.googlesource.com/#/q/I2ddd2927a57f83a6470907a275a57c36184b945c))
- `UserStyleFlavors` have become non-experimental feature. ([I69cdc](https://android-review.googlesource.com/#/q/I69cdc590cb06962cd62b2616e2b8918fb9fc8c62))
- We have removed the experimental `ValueType` from `RangedValueComplicationData` and instead introduced experimental `DiscreteRangedValueComplicationData` which is like `RangedValueComplicationData` except for integer range \& value. We've also introduced experimental `GoalProgressComplicationData` which is similar to `RangedValueComplicationData` except it's for progress towards a goal where min implicitly is zero, and the value is allowed to be larger than `targetValue`. Note for all `RangedValue` variants at least one of monochromeImage, text or title must be specified. ([I9590c](https://android-review.googlesource.com/#/q/I9590c240808a1c6f6235e904af403565e1c2efdb))
- We removed `boundsWithMargins` from `ComplicationSlotState` because system software doesn't have a use case for it. ([I42e26](https://android-review.googlesource.com/#/q/I42e2670faf421549d8a9d84e4e198992b474886f))
- We've added experimental support for `WeightedElementsComplicationData` which consists of an array of Elements (pairs of weight and color) along with optional text/title/image. These might be displayed as a pie chart where the colors need to be meaningful given the context, since there typically isn't room in a complication to render labels. ([I87eea](https://android-review.googlesource.com/#/q/I87eea137c8c4cf14921139f78d81a40433169f2e))
- The experimental `ColorRamps` optionally used by `RangedValueComplicationData` and `GoalProgressComplicationData` now allow you to specify a sequence of up to seven colors and a flag stating whether the colors should be smoothly tweened or whether equal sized solid steps of color should be rendered. ([I9f5bf](https://android-review.googlesource.com/#/q/I9f5bfc436a32a82d83e15c6c043c3a9d6bb8b06d))
- `RangedValueComplicationData.drawSegmented` has been changed to `valueType` which is an int with a corresponding `ValueType IntDef` which provides semantic meaning to the ranged value and may be used by the complication renderer to influence styling. ([I0616b](https://android-review.googlesource.com/#/q/I0616b9501a6fce413c02416bea148473c2274635))
- We've added experimental support for optional `ColorRanges` to `RangedValueComplicationData`. Normally complications would be rendered in colors of the watch face's choosing, but sometimes the `ComplicationDataSource` is best placed to set the colors e.g. when they have a particular semantic meaning. E.g. red to blue for temperature. ([I5153a](https://android-review.googlesource.com/#/q/I5153a3f4839ed70fb3ad6c60c6121810c3c26748))
- We've added an experimental `drawSegmented` hint to `RangedValueComplicationData`. This signals renderers to draw the ranged value indicator with segments, where 1 segment = 1 unit. ([I7d7c1](https://android-review.googlesource.com/#/q/I7d7c19c4be04051e1c0d9c92da3a6104d927974c))

**Bug Fixes**

- We've added the ability to define `ComplicationSlotBounds` relative to a predefined screen coordinate system. ([I0985d](https://android-review.googlesource.com/#/q/I0985d8c959f8e755b523a8befb523fec43d6e220))

## Version 1.1

### Version 1.1.1

August 10, 2022

`androidx.wear.watchface:watchface-*:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0412edaeb003a9619a2239e48e5b208f0398221b..a92c948fa16dd63ba561e3368cc85f605a1e26e2/wear/watchface)

- This is a bug fix release and users of version 1.1.0 are strongly encouraged to upgrade.

**Bug Fixes**

- Watch face initialization is asynchronous and if a complication is received before the watch face is ready it gets put on the `pendingInitialComplications` list and is applied later. Unfortunately `pendingInitialComplications` was applied too soon which meant there was a window of time during watch face initialization where complications would still get put on `pendingInitialComplications` and be ignored. This has now been fixed. In addition This patch fixes a bug where `ComplicationRenderer` was wrongly trying to load placeholders asynchronously, which failed leading to the compilation graphic never updating. Finally this patch fixes a hopefully theoretical bug where multiple `pendingInitialComplications` need to be merged. ([0d03ba3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2170325))

- Fix potential deadlock in `InteractiveInstanceManager` where `getExistingInstanceOrSetPendingWallpaperInteractiveWatchFaceInstance` was holding the lock longer than necessary. Usually we'd expect `engine.setUserStyle` to be quick but if for some reason it's not then we could end up with a deadlock/ANR. This patch moves unnecessary work out of the lock, removing the potential for a deadlock.([5a2adca](https://android.googlesource.com/platform/frameworks/support/+/5a2adcabf92d17285654d3579edae9d87b854cf5))

- Fix several issues that retained `WatchFaceService`. The WakeLock can sometimes retain the `WatchFaceService`, adding a `release()` call fixes this. Also the `StateFlows` can retain `WatchFaceService`, canceling the underlying `CoroutineScopes` fixes that.([fd48138](https://android.googlesource.com/platform/frameworks/support/+/fd4813820c762aa44db8ac634a1c0f26be04a0b7))

- Add timeouts to `awaitDeferredWatchFace`\* and fix `watchfaceOverlayStyle` `NullPointerException`. In normal circumstances this shouldn't timeout including after fresh install and `DirectBoot` scenarios where the CPU load is high. We've also fixed a NPE if `getWatchfaceOverlayStyle` is called after `close()`.([a4c3a5a](https://android.googlesource.com/platform/frameworks/support/+/a4c3a5a8f6cb18f3a2884787f9942d8c85f4d64c))

### Version 1.1.0

June 15, 2022

`androidx.wear.watchface:watchface-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/947b9ceb775ff5ace7ed32e57bb398c964bf5db3..0412edaeb003a9619a2239e48e5b208f0398221b/wear/watchface)

**Important changes since 1.0.0**

Improved Editing:

- We added support for hierarchical schemas, which allows a hierarchy of styles to be scribed by editor UIs. You can now specify separate icons for use by on watch face and companion editors.
- There is opt-in support for multiple instances of a watch face, each instance has a unique ID available across all API surfaces.
- You can now specify human readable names for `ComplicationSlots` for use in editors.
- Experimental support for styling "flavors", a curated selection of styles which will be visible from the companion editor.
- When editing two instances of the watchface are loaded, it's now possible for watchface instances to share resources, saving memory
- When picking a complication in the on watch face editor, the current provider is now preselected.

Improved Complications:

- You can now specify the `ComplicationType` for the primary and secondary data sources, giving developers more flexibility for the out of box experience.
- We added `ComplicationDataTimeline` which provides a sequence of time-gated data to be delivered to the watch face which can be cached and updated automatically. For example, today's weather forecast at various times or multiple upcoming calendar events.
- The `ComponentName` of the complication provider is part of the `ComplicationData`.
- Complications are now cached which provides a better experience when switching between watch faces.

Other changes:

- The `UserStyleSchema` and `ComplicationSlots` can now be defined in XML. This simplifies watch face construction and allows for faster metadata queries from the system.
- Watch faces can now influence the colors used for rendering the system overlay.

### Version 1.1.0-rc01

May 18, 2022

`androidx.wear.watchface:watchface-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b18424ac8b7d47a65751381a4f8ad4777f537107..947b9ceb775ff5ace7ed32e57bb398c964bf5db3/wear/watchface)

**New Features**

- We've made some usability tweaks to watchface XML support, making it easier to specify `ComplicationSlotBounds` and supporting references. Experimentation with edge complication `BoundingArc` continues, plumbing it through to `drawHighlight` although it's not recommended for use at that time.

**API Changes**

- We've added an experimental overload of `drawHighlight` which accepts a `BoundingArc` parameter. ([I705f8](https://android-review.googlesource.com/#/q/I705f8f92e4b133a3d76038c6520789a747c667ee))
- Watch face XML now supports resource references. It lets you use the same constants both in XML and your code. ([I3ef61](https://android-review.googlesource.com/#/q/I3ef61ab93d8e3a6a0d314a8a0425b31164a9c63f))
- We've added the ability to define `ComplicationSlotBounds` in `center_x`, `center_y`, `size_x`, `size_y` form. Now it is also possible to use different units (i.e. dp) using resource references. ([Iace98](https://android-review.googlesource.com/#/q/Iace98fc80f978037b1ae42307f2cbb278c4a8129))

**Bug Fixes**

- Fix `runBlockingWithTracing` which was running tasks on the wrong context.([4f595fe](https://android.googlesource.com/platform/frameworks/support/+/4f595fe139661c42d56fb829d085a384bf832c6b))
- Make `BaseEditorSession.close` synchronous. The problem with `BaseEditorSession.close` being asynchronous is that we release the `ComplicationDataSourceInfoRetriever` too late leading to warning spam in logcat. This was probably harmless but logcat spam is distracting and should be avoided.([35a5308](https://android.googlesource.com/platform/frameworks/support/+/35a5308a631f3db7bba4a9b186fec8b85df74659))

### Version 1.1.0-beta02

May 11, 2022

`androidx.wear.watchface:watchface-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..b18424ac8b7d47a65751381a4f8ad4777f537107/wear/watchface)

**New Features**

- We've added experimental support for new `ComplicationData` types, these are not yet ready for use but watch this space.

**API Changes**

- We've added `BoundingArc`, an experimental class that describes the geometry of an edge complication slot. This has been added to `ComplicationSlot` and plumbed through to `ComplicationSlotState` and `WatchFaceMetadataClient`. ([I61a40](https://android-review.googlesource.com/#/q/I61a40ff046d0c4f4194c4c51c3f4b7acca3bb198))
- We've added the ability to inherit settings in `UserStyleSetting` XML. It lets you reduce verbosity and share a setting between watchfaces. ([Ief841](https://android-review.googlesource.com/#/q/Ief841586eb3a4325b68b1c87a0aa1018e5cd629c))
- We have added two new experimental types of `ComplicationData`: `ListComplicationData` \& `ProtoLayoutComplicationData`. Currently there's no rendering support for either of these types and WearOS doesn't currently recognize these types if added to a `ComplicationDataSource's` manifest. ([I1811c](https://android-review.googlesource.com/#/q/I1811ca12e288f6baa3b5575dbd765b7e23143c0a))

**Bug Fixes**

- Fix serialization of `TimeLineEntry` type. We were not serializing the `TimeLineEntry` type which meant cached `TimeLineEntries` of type NoData would be incorrectly interpreted as having the parent complication's type leading to NPEs when non-existent required fields were accessed. ([55ffdf5](https://android.googlesource.com/platform/frameworks/support/+/55ffdf527dc6f684d25a91abac04b4a89c726057))
- Fix a bug where `setComplicationData` dropped timeline fields([fb392f5](https://android.googlesource.com/platform/frameworks/support/+/fb392f5a59c50a77e773ba59bbb73aee2bdfd181))
- Fixes a bug where very occasionally `runBlockingWithTracing` would lead to an NPE([12ca62e](https://android.googlesource.com/platform/frameworks/support/+/12ca62e82899e9c12a471a5d02905a3c5dd64d0c))
- Fixes a bug where we sometimes get `ClassNotFoundException: android.support.wearable.complications.ComplicationText` when receiving a complication.([217942d9](https://android.googlesource.com/platform/frameworks/support/+/217942d9feab7480e6f55cb06de0f93dc7825bc1))
- Fixes a bug in `GlesRenderer.backgroundThreadInitInternal` where it was only calling `onBackgroundThreadGlContextCreated` if `EGL14.eglCreateContext` was called. Fixes another bug where there was a visual glitch in the screenshot caused by `verticalFlip`.([c674ad2](https://android.googlesource.com/platform/frameworks/support/+/c674ad27a29cd6d6b3fc14eb7397fe85f0d78ad8))
- Fix `WatchFaceService` XML version check, it was loading from the wrong package.([dfa06f3](https://android.googlesource.com/platform/frameworks/support/+/dfa06f31a347614324d43d6a83fce2b3cc5bfd0d))
- Placeholder wire format now uses an inner bundle. We don't want placeholders to break existing watchfaces which might use the hidden inner a.s.w.c.ComplicationData. Previously the wire format of a `NoDataComplication` data stored the placeholder in the usual fields (problematic because old watch faces would render the placeholder string which isn't intended), instead we now use an inner bundle to fully isolate this.([d5e7bd2](https://android.googlesource.com/platform/frameworks/support/+/d5e7bd2ddf13f48acf10a4d4933e668a17be2086))

### Version 1.1.0-beta01

April 20, 2022

`androidx.wear.watchface:watchface-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/wear/watchface)

**API Changes**

- Now `WatchFaceMetadataClient` methods (`getUserStyleSchema`, `getComplicationSlotMetadataMap`, `getUserStyleFlavors`) and `HeadlessWatchFaceClient.getUserStyleFlavors` throw unchecked RuntimeException instead of `WatchFaceException`. ([I0718a](https://android-review.googlesource.com/#/q/I0718ae7a2fc0966a55fa60304b2c4a6848aa50d0))
- `WatchFaceMetadataClient.WatchFaceException` has been moved out of the class to allow it to be reused. ([I4e869](https://android-review.googlesource.com/#/q/I4e86906c5b7c66e2e27d04999391a23616322260))

**Bug Fixes**

- `WatchFaceMetadataClient` will no longer crash when sent partial `ComplicationSlotBounds`.([Iaafd](https://android-review.googlesource.com/#/q/Iaafdce466558ac3165e52e8ed1e0116387c87171))

### Version 1.1.0-alpha05

April 6, 2022

`androidx.wear.watchface:watchface-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/wear/watchface)

**New Features**

- You can now tell which data source sent a `ComplicationData` by inspecting `ComplicationData.dataSource`, some watch faces may use this to customize complication display. ([I44a73](https://android-review.googlesource.com/#/q/I44a73f1ddc5fa67cf0eecdc61df9ce14886dbf3f))

**API Changes**

- `Renderer.CanvasRenderer` and `Renderer.GlesRenderer` have been deprecated in favor of `Renderer.CanvasRenderer2` and `Renderer.GlesRenderer2` which support `SharedAssets` which are passed to the render methods. For java interop we've introduced `ListenableCanvasRenderer2` and `ListenableGlesRenderer2`. ([I31ffa](https://android-review.googlesource.com/#/q/I31ffac1033664bdb1c85eea5389ddb8136d1b59e))
- Added `@WatchFaceFlavorsExperimental` ability to define flavors - preconfigured list of styled watchfaces ([I04dd0](https://android-review.googlesource.com/#/q/I04dd04e303e471f92b9e08366b5b0644eb49c9ef))
- `Renderer.sharedAssets` is now a StateFlow and we've removed the unused `Renderer.SharedAssetsFactory` ([I12ac5](https://android-review.googlesource.com/#/q/I12ac5ebfadffa12088dfbfd21fc076925c8f1195))
- `UserStyleSchema.userStyleSettings` is not deprecated anymore ([Iba7e3](https://android-review.googlesource.com/#/q/Iba7e3cf82d94a58555855118ebf9b2872e743a65))
- We've added `HeadlessWatchFaceClient.getUserStyleSchemaDigestHash` which allows a `HeadlessWatchFaceClient` to avoid the relatively low overhead of passing the schema over AIDL before computing the digest hash. ([I33597](https://android-review.googlesource.com/#/q/I335977f7767a9a87c3dc99ec61a5ee6c2f312b8d))
- We've added `isUserStyleSchemaStatic` to `WatchFaceMetadataClient` which is true if and only if the `UserStyleSchema` can be relied on not to change unless the watch face APK is updated. ([I45a3f](https://android-review.googlesource.com/#/q/I45a3f5e0455e007ed5fdfaaf6f7b9f4e71a29abe))
- We have added `getDigestHash` to `UserStyleSchema` which computes a digest hash of the schema. This can be used to efficiently determine if the `UserStyleSchema` has changed. ([I2063d](https://android-review.googlesource.com/#/q/I2063df220cb9fd3a21ab50dac72eb0b13ace18bb))
- `METADATA_KEY_DATA_SOURCE_DEFAULT_CONFIGURATION_SUPPORTED` renamed to `METADATA_KEY_DATA_SOURCE_DEFAULT_CONFIG_SUPPORTED` ([I9ba5d](https://android-review.googlesource.com/#/q/I9ba5d6684d537609a8fda3a32478c120c878e824))
- `UserStyleSetting.OnWatchEditorData` has been renamed to `UserStyleSetting.WatchFaceEditorData`, it contains data that's used purely by the on watch face editor. ([If3afb](https://android-review.googlesource.com/#/q/If3afbf11dc7c3890d703e2fc23c54b1823d5f574))

### Version 1.1.0-alpha04

March 9, 2022

`androidx.wear.watchface:watchface-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..33cb12e8aba043a05b40470a5ef3be1b35114fd5/wear/watchface)

**API Changes**

- Up to date `ComplicationData` may not always be available (e.g. expired cached ComplicationData) so we've extended `NoDataComplication` with an optional placeholder ComplicationData and added `ComplicationText.PLACEHOLDER`, `MonochromaticImage.PLACEHOLDER`, `SmallImage.PLACEHOLDER`, `PhotoImage.PLACEHOLDER` which are only allowed to be used inside the context of a `NoDataComplicationData` placeholder. If selected these placeholders are suggested to be rendered with gray boxes/arcs. ([I6285d](https://android-review.googlesource.com/#/q/I6285d065676350564f74292337d982dd8e52da01))
- We've added `ComplicationData.getNextChangeInstant` which tells you the next Instant after the reference Instant at which any field of the complication may change. This is used internally to schedule frames for complication updates. E.g. if a watch face normally updates once per minute, setting the stop watch complication will cause it to update once per second. ([I7ceb2](https://android-review.googlesource.com/#/q/I7ceb222cb1f0abb5159c927ec846581365b9bfc7))
- `EditorSession.watchFaceId` can now be used on all API levels. In addition its value will now always be consistent with `WatchState.watchFaceInstanceId`. ([I323b9](https://android-review.googlesource.com/#/q/I323b949e624150437015cbe3bc522fba9fb4398a))
- The `getPendingIntentForTouchEvent` API is no longer necessary since the underlying issue has been fixed in the framework, so all the related APIs have been removed. Watchfaces do not need to do anything special for `PendingIntents` to fire, even if the home button has recently been pressed. ([I1f2e8](https://android-review.googlesource.com/#/q/I1f2e88d00fb07953c46c7dd7768398165196d943))
- We've added `RendererParameters.isForScreenShot` which will be true if the render is for a screen shot. Some watch faces with animations need to know this in order to make adjustments to ensure the best results. ([I96d99](https://android-review.googlesource.com/#/q/I96d99f6d6548ac143961e8d785e16de4ecf1b7aa))
- We've added `WatchFaceExceptionReason` to `WatchFaceException` to give some context to what went wrong. ([I01d15](https://android-review.googlesource.com/#/q/I01d1535242a5d5b580c6c748726341ce3ee5f640))
- `ComplicationDataSourceService.onImmediateComplicationRequest` has been removed, instead `ComplicationRequest.immediateResponseRequired` has been added to signal that the provider needs to respond quickly (ideally responding in \< 100ms). Note this functionality is guarded behind the privileged `com.google.android.wearable.permission.USE_IMMEDIATE_COMPLICATION_UPDATE` permission. ([Ie6b23](https://android-review.googlesource.com/#/q/Ie6b236a3b92bc4cc671f7cf4a2d2744d5b0f9ed9))
- Updated nullability in core and appcompat to match Tiramisu DP2 ([I0cbb7](https://android-review.googlesource.com/#/q/I0cbb7f22651e725a4bb36d20388a949a72cc5903))

**Bug Fixes**

- Now watchface app crashes with an exception if the schema validation fails ([Ia400f](https://android-review.googlesource.com/#/q/Ia400f2a57baa8001ba60c27c9b96fa329b96a301))

### Version 1.1.0-alpha03

February 9, 2022

`androidx.wear.watchface:watchface-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..db2ecbef194afcddfaede22e1d884a8959a9277c/wear/watchface)

**API Changes**

- We've added experimental support for hierarchical style schemas. We've added a new property to `androidx.wear.watchface.style.UserStyleSetting.Option`, childSettings which is initially only used by `ListOption`. This allows a hierarchy of styles to be described for use by Editor UIs, the underlying UserStyle is unchanged and is still a `Map<String, ByteArray>`. ([Iaf6f4](https://android-review.googlesource.com/#/q/Iaf6f4ba2862b8d1aff3ccad7f4b9bd2826b5db51))
- We've added `WatchFace.OverlayStyle` which allows the watch face to configure the rendering of the system status overlay. ([I8520d](https://android-review.googlesource.com/#/q/I8520d9761d3587c85ac7fde2de56d632c41c0687))
- We've introduced `clearWithBackgroundTintBeforeRenderingHighlightLayer` a new optional constructor parameter for `CanvasRenderer` (default is false), if set to true then the canvas will be cleared with the background tint color. ([Ie01e5](https://android-review.googlesource.com/#/q/Ie01e5b68545ec435c0b087152d332695b02bda12))
- Added `androidx.watchface.complications.datasource.DEFAULT_CONFIGURATION_SUPPORTED` metadata key which allows complication data sources to indicate they can provide a default value without any configuration ([Icc0d4](https://android-review.googlesource.com/#/q/Icc0d46e9e49cc1a688ab99e4acf535d5385e5aec))
- It's common when editing a watch face for there to be both an interactive and a headless instance. To help save memory we've introduced `Renderer.SharedAssets` which allows a watch face renderer to share immutable data (e.g. textures and shaders) between instances. `GlesRenderer.setEglConfig` and `GlesRenderer.setEglDisplay` are deprecated, it was never intended for these to be settable, and doing so would have led to undefined behavior. ([I0d9e7](https://android-review.googlesource.com/#/q/I0d9e730bb712afc24dbd84611c6917f248772a27))
- We've added `setNameResourceId` \& `setScreenReaderNameResourceId` (which reference string resources) to `ComplicationSlot.Builder` and corresponding getters in `androidx.wear.watchface.client.ComplicationSlotState`. This allows the system to fetch the names of ComplicationSlots for use in editors and screen readers. ([If6c6a](https://android-review.googlesource.com/#/q/If6c6a13d5af8392269c11e19ecfc41542c195f6c))
- `WatchfaceMetadataClient.getUserStyleSchema` and `getComplicationSlotMetadataMap` now throw `WatchFaceException` instead of `RemoteException`. ([I86f11](https://android-review.googlesource.com/#/q/I86f11f548ffe3371d8dbee3f8b9eeae34fe1b88c))
- `onSynchronousComplicationRequest` and related functions in `ComplicationDataSourceService` have been renamed to `onImmediateComplicationRequest` etc... ([I87ba0](https://android-review.googlesource.com/#/q/I87ba0857ac292cd0eb80fa2cb1a754f26e779ecc))
- Watch face editors have much less screen real estate than companion editors, therefore it makes sense to support different icons for on watch face editors. This patch adds `OnWatchEditorData` (currently containing just an icon) to all UserStyleSettings and where appropriate their Option classes. ([If1886](https://android-review.googlesource.com/#/q/If1886f42fd7d9867c1002b2a5550e051c370e80b))
- We've added `@JvmOverloads` to ListenableGlesRenderer's constructor for better java interop. ([I2974a](https://android-review.googlesource.com/#/q/I2974a4c12a66776dc8932371a1294998fd6550ac))

**Bug Fixes**

- `ListenableGlesRenderer`'s constructor is now correctly marked as `@Throws(GlesException::class)`, and it is now possible to extend this class in java. ([Iac6d0](https://android-review.googlesource.com/#/q/Iac6d0037a736c34e733622688cc3f68e9fa633c5))
- Fixes bug with `PhotoImageComplicationData` tapAction not being correctly handled ([I1cc30](https://android-review.googlesource.com/#/q/I1cc30a56e343c6f0b41406b3884e8b945f4085e8))

### Version 1.1.0-alpha02

January 12, 2022

`androidx.wear.watchface:watchface-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..f09f3e0f47cacc65a631115deac08ee8cc132ceb/wear/watchface)

**New Features**

- To aid debugging and testing, `ComplicationData` and related subclasses now have overridden hashcode, equals and toString methods making them easier to work with.

**API Changes**

- `WatchfaceMetadataClient` methods once again throw `RemoteExceptions` where appropriate, making it easier for client code to catch errors from the watch face. ([I78785](https://android-review.googlesource.com/#/q/I787857856322c765c5cfe0d3ce2fa56b61cf3eda))
- `ComplicationData` and sub classes now have hashcode, equals and toString. ([I24bc6](https://android-review.googlesource.com/#/q/I24bc6906ec7194316161ceb394d92ac07cdee370))

### Version 1.1.0-alpha01

December 15, 2021

`androidx.wear.watchface:watchface-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a0b94773cb4f134522ad5fb19f641b5fec937975..301586664b5aad60548f21866cad502d524dbf9f/wear/watchface)

**New Features**

- The `UserStyleSchema` and `ComplicationSlots` can now be defined in XML. This simplifies watch face construction. In addition, `WatchFaceMetadataClient` queries are faster because it doesn't need to bind to the service to get the metadata. The `WatchFaceMetadataClient` and `ListenableWatchFaceMetadataClient` are no longer experimental and will become part of the stable api. The system will be able to optionally support multiple instances of a watch face, each with distinct user defined styling options. These will be visible in the watch face picker. To opt into this a watch face must include the following meta data tag in its manifest.

          <meta-data
              android:name="androidx.wear.watchface.MULTIPLE_INSTANCES_ALLOWED"
              android:value="true" />

- Some watch faces have state that's not captured in the `UserStyle`, to support this and multiple instances, the watch face's instance ID is now available via `WatchState.watchFaceInstanceId`.

- `ComplicationData` is now being cached to allow complications to be displayed immediately upon loading. Sometimes `ComplicationData` is cached in memory by the system and sometimes it is serialized by the watch face libraries. When serialized any associated tapAction will be lost, if this happens `ComplicationData.tapActionLostDueToSerialization` will return `true` and the watch face should render the complication differently (e.g. grayed out or semi-transparent) to signal that it can't be tapped. The system will send updated `ComplicationData` with a `tapAction` as soon as possible.

- Some `ComplicationData` shouldn't be cached for a long time, to support this we've added a more general feature `ComplicationDataTimeline`. This can be used to provide a sequence of time-gated `ComplicationData` to be delivered to the watch face which can be cached and updated automatically. For example, today's weather forecast at various times or multiple upcoming calendar events. `ComplicationRequestListener` has been extended with a new method `onComplicationDataTimeline` which you can use to return this data.

- `DefaultComplicationDataSourcePolicy` has been extended so you can specify the `ComplicationType` for the primary and secondary data sources.

- We've added support for synchronous complication providers where the complication is updated at a higher frequency than normal, up to once per second when the watch face is visible and non-ambient. *Note:* synchronous complication providers may have limited usage due to memory pressure concerns.

- The `PendingIntentTapListener` changes are likely to be reverted because we solved the underlying problem (it's not possible for the watch face to launch activities for 5 seconds after pressing the home button) in the framework instead.

**API Changes**

- `ComplicationData.isCached` has been changed to `tapActionLostDueToSerialization` which is more useful when determining if the complication slot should be rendered differently to signal that it can't be tapped. ([I6de2f](https://android-review.googlesource.com/#/q/I6de2f4f550a31ebdbcaf2490bd1706fb85f2ab68))
- Added `ComplicationDataTimeline` to `wear-complication-data-source`. This can be used to provide a sequence of time-gated `ComplicationData` to be delivered to the watch face which can be cached and updated automatically. For example, today's weather forecast at various times or multiple upcoming calendar events. `ComplicationRequestListener` has been extended with a new method `onComplicationDataTimeline` which you can use to return this data. There's a new kotlin wrapper `SuspendingTimelineComplicationDataSourceService` for suspending data source services. ([Idecdc](https://android-review.googlesource.com/#/q/Idecdc0c92a52ff9591b7a84e500986d4817719be))
- Added `PendingIntentTapListener` and `WatchFaceControlClient.getPendingIntentForTouchEvent`. This can help watch faces that need to launch intents in response to taps to work around a problem where the framework blocks launching new activities for 5 seconds after pressing the home button. ([I98074](https://android-review.googlesource.com/#/q/I980744748c89de92da0f9e07d49e6b2d7c99410a))
- Introduced a per-watchface `ComplicationData` cache. The purpose of this is to allow the watch face to display last known complication data values upon loading until the system has had a chance to update them. There is a new API method `WatchFaceControlClient.hasComplicationCache` intended for OEMs. This may influence the system's strategy for sending complications to a watch face. In addition, `ComplicationData` has an `isCached` property and it is recommended that cached complications are rendered differently because the `tapAction` can not be cached and will be `null` in a cached complication. ([I404b0](https://android-review.googlesource.com/#/q/I404b06e624e745b0ae5d48558658825c9c1cc7f3))
- The watch face's instance ID is now available via `WatchState.watchFaceInstanceId`. Most watch faces won't need to use this, but if there's a per-watch face state that's not stored in the Schema then this is the key to use to identify the watch face instance. To help support this you can now provide an ID when calling `WatchFaceControlClient.createHeadlessWatchFaceClient`. ([I1ff98](https://android-review.googlesource.com/#/q/I1ff987d6920b71b736bd3e4c3ac8c2f4b658b77b))
- Extended `DefaultComplicationDataSourcePolicy` with the ability to set the default `ComplicationTypes` for the primary, secondary provider and for the fallback system provider. `ComplicationSlot.defaultDataSourceType` is now deprecated. ([If0ce3](https://android-review.googlesource.com/#/q/If0ce3d8de82c41b22cd178bc79c1951cc719cc87))
- `ComplicationSlot.configExtras` is now mutable and can be updated before calling `EditorSession.openComplicationDataSourceChooser()`. ([I6f852](https://android-review.googlesource.com/#/q/I6f8520a9e5574d2c778ad6ea1683ab7730235815))
- Added `WatchFace.setComplicationDeniedDialogIntent` and `setComplicationRationaleDialogIntent`. These intents are launched to to show a rationale dialog before requesting complication permissions, and another dialog explaining that complication permission is needed when trying to edit a complication when permissions have been denied (the provider chooser will fail to open so the dialog is needed). ([I3a29c](https://android-review.googlesource.com/#/q/I3a29c8eec8c80e741176596dc2fd3a320688f902))
- The `UserStyleSchema` and `ComplicationSlots` can now be defined in XML. This simplifies watch face construction and makes `WatchFaceMetadataClient` queries faster as they do not need to bind to the service to get the metadata. ([I85bfa](https://android-review.googlesource.com/#/q/I85bfa873f945e489a64abaff492466a95e7119bc))
- Added `InteractiveWatchFaceClient.supportsPendingIntentForTouchEvent` so a client can determine if a watch face supports `getPendingIntentForTouchEvent`. ([I0b917](https://android-review.googlesource.com/#/q/I0b91706e201ff5f4ed7afecab65a5a4910e4f5a4))
- `WatchFaceMetadataClient` and `ListenableWatchFaceMetadataClient` are no longer experimental. They can be used to efficiently obtain watch face metadata, where possible without opening a binder to the watch face. ([Ibb827](https://android-review.googlesource.com/#/q/Ibb827764730181ba10491f0065d6a76a225a4d41))
- Added support for synchronous complication providers where the complication is updated at a higher frequency than normal, up to once per second when the watch face is visible and non-ambient. To use this the provider must include a new `androidx.wear.watchface.complications.data.source.SYNCHRONOUS_UPDATE_PERIOD_SECONDS` metadata tag in its manifest and override `onSynchronousComplicationRequest`. Depending on the nature of the data source, it may also need to override `onStartSynchronousComplicationRequests` and `onStopInteractiveComplicationRequests` to get notifications of when the complication enters and exits interactive mode. ([I8fe9d](https://android-review.googlesource.com/#/q/I8fe9dcbd9b4a3a293322b69aa91c4c3a25325c63))

## Version 1.0

### Version 1.0.1

February 9, 2022

`androidx.wear.watchface:watchface-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a0b94773cb4f134522ad5fb19f641b5fec937975..37100a090f44e25df981ef57731aaa2e2b9afe20/wear/watchface)

**Bug Fixes**

- Fixes bug with `PhotoImageComplicationData` tapAction not being correctly handled ([I1cc30](https://android-review.googlesource.com/#/q/I1cc30a56e343c6f0b41406b3884e8b945f4085e8))

### Version 1.0.0

December 1, 2021

`androidx.wear.watchface:watchface-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e90bbb5c9ce1de64d619166e2d548e79f7a9bdf4..a0b94773cb4f134522ad5fb19f641b5fec937975/wear/watchface)

**Major Features of 1.0.0**

The `androidx.wear.watchface` package is the new recommended library for developing WearOS watch faces. It has a number of new features over the old Wearable Support Library.

- User styling (e.g. to change the color palette, the style of the watch hands, the look of the hour marks etc) is directly supported by the library (see `androidx.wear.watchface.style`). It's now much easier to develop an on watch face editor using androidx.wear.watchface.editor and your watch face can be edited from the system companion app without you needing to write any extra code.
- Best practices baked in. The library automatically generated screen reader content labels for complications (you can also add your own ones), and the framerate automatically drops when the battery is low and not charging to improve battery life.
- Less code is needed to develop a watch face, especially for complications where a lot of the boilerplate has moved into the library.

**Bug Fixes**

- Fix `EditorSession.userStyle.compareAndSet` ([I6f676](https://android-review.googlesource.com/q/I6f676876b91bbcdbed3a270fda61ab1567c3ce89))
- Fix very short watch face delays ([Iffb97](https://android-review.googlesource.com/q/Iffb9725767a97a911d1794904b6aa7aee2246d38))
- Dispatch `InteractiveWatchFaceImpl.onDestroy` on the UI thread ([I83340](https://android-review.googlesource.com/q/I8334083557fea6eb8944a66ddd9059f588aad190))
- Fix several problems with broadcast receivers ([I7d25f](https://android-review.googlesource.com/q/I7d25f091f48422a1135bd74b7092142501265303))

### Version 1.0.0-rc01

November 3, 2021

`androidx.wear.watchface:watchface-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca6054a5e12fcf05ba5e20bf93403afdab093986..e90bbb5c9ce1de64d619166e2d548e79f7a9bdf4/wear/watchface)

**Bug Fixes**

- Fix dump() (called by adb shell dumpsys) which got broken by flow migrations. ([087cf9e](https://android.googlesource.com/platform/frameworks/support/+/087cf9e9cd0e8a22ce606fe609523b302a6fe2df))

- Ensure proper ordering of writeDirectBootPrefs. We want writeDirectBootPrefs to always run after initStyleAndComplications or we risk delaying UI thread init.([37650ac](https://android.googlesource.com/platform/frameworks/support/+/37650ac346629f446d7780b68fda5188a1f7a245))

- Ensure Renderer.onDestroy is called. In the scenario where the renderer has been created but WF init has not completed and Engine.onDestroy is called, we need to call Renderer.onDestroy.
  ([f9952dc](https://android.googlesource.com/platform/frameworks/support/+/f9952dc62e10a23846123e4ecd166272784a178c))

- Optimization/fix to isBatteryLowAndNotCharging. This patch moves the initial setup of isBatteryLowAndNotCharging earlier which means it can be done in parallel with
  createWatchFace. In addition we now listen to ACTION_POWER_DISCONNECTED. ([ddffd80](https://android.googlesource.com/platform/frameworks/support/+/ddffd80227ea2c84abc0d00eb3aba2e5a7c64dab)

- InteractiveWatchFaceClientImpl.isConnectionAlive to be false after close ([ab9774e](https://android.googlesource.com/platform/frameworks/support/+/ab9774ee2c38e62152a8fb0b65d367884984813f))

### Version 1.0.0-beta01

October 27, 2021

`androidx.wear.watchface:watchface-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..ca6054a5e12fcf05ba5e20bf93403afdab093986/wear/watchface)

### Version 1.0.0-alpha24

October 13, 2021

`androidx.wear.watchface:watchface-*:1.0.0-alpha24` is released. [Version 1.0.0-alpha24 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/wear/watchface)

**API Changes**

- Classes in package `androidx.wear.watchface.complications` have been moved into a new `wear:watchface:watchface-complications` project. Note this means you can't include this library as well as any previous alpha version of `wear:watchface:watchface-complications-data` because you'll get errors about duplicate classes. ([I97195](https://android-review.googlesource.com/#/q/I9719558082a019b4a8b98fdbfa6b979b62604316))
- Renderer.dump has been renamed to Renderer.onDump and has been annotated with @UiThread. ([I44845](https://android-review.googlesource.com/#/q/I4484566d9f8ddb874f7dc23caccd2281cf14acd4))
- `InteractiveWatchFaceClient.addWatchFaceReadyListener` has been renamed to `addOnWatchFaceReadyListener` and `removeWatchFaceReadyListener` has been renamed to `removeOnWatchFaceReadyListener`. ([I48fea](https://android-review.googlesource.com/#/q/I48fea9e27af16b8521eef0237c280ca562c07a63))
- EditorSession `getComplicationsPreviewData` and `getComplicationsDataSourceInfo` are no longer suspend functions, instead they are `StateFlow<>` properties whose value is initially null. In ListenableEditorSession `getListenableComplicationPreviewData` and `getListenableComplicationsProviderInfo` have been removed in favor of the new `StateFlow<>` objects from the base class. If you need to listen to changes in java code, consider using `androidx.lifecycle.FlowLiveDataConversions.asLiveData` to convert to `LiveData<>`. ([Ic5483](https://android-review.googlesource.com/#/q/Ic5483c018ffc98879fa49bdc4e741bfa68fdc2af))

### Version 1.0.0-alpha23

September 29, 2021

`androidx.wear.watchface:watchface-*:1.0.0-alpha23` is released. [Version 1.0.0-alpha23 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/wear/watchface)

**New Features**

The watchface library is now a single library group, and as a result the libraries have moved and you will need to update your gradle imports as follows:

| Old | New |
|---|---|
| `androidx.wear:wear-complications-data` | `androidx.wear.watchface:watchface-complications-data` |
| `androidx.wear:wear-complications-data-source` | `androidx.wear.watchface:watchface-complications-data-source` |
| `androidx.wear:wear-watchface` | `androidx.wear.watchface:watchface` |
| `androidx.wear:wear-watchface-complications-rendering` | `androidx.wear.watchface:watchface-complications-rendering` |
| `androidx.wear:wear-watchface-client` | `androidx.wear.watchface:watchface-client` |
| `androidx.wear:wear-watchface-client-guava` | `androidx.wear.watchface:watchface-client-guava` |
| `androidx.wear:wear-watchface-data` | `androidx.wear.watchface:watchface-data` |
| `androidx.wear:wear-watchface-editor` | `androidx.wear.watchface:watchface-editor` |
| `androidx.wear:wear-watchface-editor-guava` | `androidx.wear.watchface:watchface-editor-guava` |
| `androidx.wear:wear-watchface-guava` | `androidx.wear.watchface:watchface-guava` |
| `androidx.wear:wear-watchface-style` | `androidx.wear.watchface:watchface-style` |

**API Changes**

- Migrate the separate `androidx.wear` Watchface and complications libraries into `androidx.wear.watchface` library group. ([b25f3c0](https://android-review.googlesource.com/#/q/b25f3c048e49c92a7a22bf03d2c78a182412a441))
- Added EditorRequest.canWatchFaceSupportHeadlessEditing to let a client know if a watchface editor supports headless editing. Note there will be some false negatives with this because support was added in asop/1756809 however it will return the correct value for all future watchfaces. ([ca55590](https://android-review.googlesource.com/#/q/ca5559018de46fa8b01153b2d8f8ac10d0ba2f17))
- Renderer now has a dump() method which can be overridden to add custom data to the information generated by ABD shell dumpsys activity service WatchFaceService. ([95235f9](https://android-review..googlesource.com/#/q/95235f99de3db4403455c83a88ee30a23f87d0b2))
- InteractiveWatchFaceClient.addWatchFaceReadyListener now specifies the executor first. ([563ac2f](https://android-review.googlesource.com/#/q/95235f99de3db4403455c83a88ee30a23f87d0b2))
- StateFlowCompatHelper has been removed. asLiveData (androidx.lifecycle.asLiveData) should be used instead. ([bd35d3](https://android-review.googlesource.com/#/q/bd35d34bfc095bbb6c8283105fc3023c6ce69793))
- CurrentUserStyleRepository.userStyle is no longer mutable. ([I44889](https://android-review.googlesource.com/#/q/I44889fc88bc7d1df2ee0b63a04de87e49b495537))
- WatchFaceReadyListener has been renamed to OnWatchFaceReadyListener. ([Ic12a9](https://android-review.googlesource.com/#/q/Ic12a9c0142d3c76d2c2dc4f9e09a1d9c02c3deae))

**Bug Fixes**

- InteractiveInstanceManager.deleteInstance to call onDestroy This is needed to ensure InteractiveWatchFaceImpl gets garbage collected.([fce4af8](https://android-review.googlesource.com/#/q/fce4af8ca27cf195956647cd002794764f9665d7), [b/199485839](https://issuetracker.google.com/issues/199485839))