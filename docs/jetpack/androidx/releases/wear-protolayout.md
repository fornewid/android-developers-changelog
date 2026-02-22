---
title: https://developer.android.com/jetpack/androidx/releases/wear-protolayout
url: https://developer.android.com/jetpack/androidx/releases/wear-protolayout
source: md.txt
---

# wear protolayout

API Reference  
[androidx.wear.protolayout](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/package-summary)  
This library allows defining a set of UI layouts and non-UI expressions to be rendered/evaluated on remote surfaces.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/wear-protolayout#1.3.0) | - | [1.4.0-beta01](https://developer.android.com/jetpack/androidx/releases/wear-protolayout#1.4.0-beta01) | - |

## Declaring dependencies

To add a dependency on wear-protolayout, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to implement support for Wear ProtoLayout Expressions
    implementation "androidx.wear.protolayout:protolayout-expression:1.3.0"

    // Use to implement support for Wear ProtoLayout
    implementation "androidx.wear.protolayout:protolayout:1.3.0"

    // Use to utilize components and layouts with Material design in your ProtoLayout
    implementation "androidx.wear.protolayout:protolayout-material:1.3.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement support for Wear ProtoLayout Expressions
    implementation("androidx.wear.protolayout:protolayout-expression:1.3.0")

    // Use to implement support for Wear ProtoLayout
    implementation("androidx.wear.protolayout:protolayout:1.3.0")

    // Use to utilize components and layouts with Material design in your ProtoLayout
    implementation("androidx.wear.protolayout:protolayout-material:1.3.0")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1300646+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1300646&template=1773709)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.4

### Version 1.4.0-beta01

February 11, 2026

`androidx.wear.protolayout:protolayout-*:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..2e98d140740558dc55710bde96311d2e0e8d5cfd/wear/protolayout).

**New Features**

The 1.4.0-beta01 release of Wear ProtoLayout indicates that this release of the library is feature-complete and the API is locked (except where marked as experimental). Wear ProtoLayout 1.4 includes the following new functionalities and APIs:

- **Inlined Image Resources and performance improvements:** Introduced an improved resource handling concept where `ImageResource` can be directly inlined within the layout itself.
  - This significantly simplifies development by removing the need for manual resource mapping in the `onTileResourcesRequest` and overriding that method.
  - This significantly improves Tiles loading time by removing the need for two binder calls as only the `onTileResourcesRequest` method can be implemented.
  - All `Image` APIs now support this concept by providing new methods that accept `ProtoLayoutScope` responsible for this.
- **Material3 Scope \& Resources Auto-Registration:** Added `materialScopeWithResources` to support the Material3 `MaterialScope` concept with the Inline Image Resources. This scope handles automatic resource registration and includes new helper methods for images (`backgroundImage`, `avatarImage`, and `icon`) to streamline components usage.

  - Simplified code snippet:

        materialScopeWithResources(
        context = context,
        deviceConfiguration = deviceParameters,
            protoLayoutScope = protoLayoutScope) {
          primaryLayout(
          // layout setup here
        iconContent = { **icon**(
        **imageResource**(
        **androidImageResource**(R.drawable.myIcon)))})
        //...
        }

- **PendingIntent support:** Added support for `PendingIntent` for Tiles. The `PendingIntent` clickables accept fallback actions (`LoadAction` or `LaunchAction`). This ensures that if the `ProtoLayout` Renderer is an older version that doesn't support `PendingIntent`, a valid fallback action is automatically used.

- **Many Kotlin DSL Improvements:**

  - Added specialized Kotlin helpers for `Image` and all `ImageResources` types to improve the developer experience for Kotlin users.
  - Added helpers for container types such as `Box`, `Row`, `Column`, etc. to adhere more with modern Android development.
  - Added a new Kotlin `Transformation` modifier and helper methods for fade in animation.
- **Customizing Lottie animation:** Added API in `AndroidLottieResourceByResId` to allow customizing Lottie animation via properties and added concrete support and API for creating property to theme a slot based on slot ID with the specified color.

- **Ambient Mode Awareness:** Added a new Platform event source, `isInAmbientMode`, allowing layouts to react and update expressions based on whether the device is in ambient mode.

**API Changes**

- **Material3 Image Helpers:** Deprecated existing Material3 image helpers in favor of new overloads that utilize `ProtoLayoutScope` and the new Inlined Resource handling.
- **MaterialScope Updates:** The `protoLayoutScope` field within `MaterialScope` is `NonNull` for easier usage when created via `materialScopeWithResources`. A new `hasProtoLayoutScope` function has been added to check for its presence. The `MaterialScope` also exposes the public field for `Context`.
- **Semantics heading** is available as an API in `LayoutModifier`.
- **Arc direction support** The `ARC_DIRECTION_*` consts are now exposed as public for use in `Arc`/`ArcLine`/`ArcText`/`DashedArcLine` elements.

**Bug Fixes**

- **Resource Comparison:** Optimized performance by implementing improved `hash` and `equals` methods for comparing resource types.
- Apply default content description to the single slot textButton.
- Fix calculations for adjusting max lines in the renderer side.

### Version 1.4.0-alpha05

January 28, 2026

`androidx.wear.protolayout:protolayout-*:1.4.0-alpha05` is released. Version 1.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..715e22619094effc2ba1fd528cd9a07b1f5d0046/wear/protolayout).

**API Changes**

- A new kotlin `Transformation` modifier has been added. ([I195a7](https://android-review.googlesource.com/#/q/I195a75d32fec3fea75102a9ee4c7e472990b014f), [b/397169191](https://issuetracker.google.com/issues/397169191))

**Bug Fixes**

- We have fixed the issue with better resource handling by removing stateful `ProtoLayoutScope` from `TileService`. ([I5dc0a](https://android-review.googlesource.com/#/q/I5dc0abfbb5aa41721dd75f14765ccde449229611), [b/474614772](https://issuetracker.google.com/issues/474614772))

### Version 1.4.0-alpha04

January 14, 2026

`androidx.wear.protolayout:protolayout-*:1.4.0-alpha04` is released. Version 1.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/wear/protolayout).

**API Changes**

- We have deprecated Material3 image helpers in favour of new overloads that are using `ProtoLayoutScope` and better resources handling concept where `ImageResource` can be directly inlined in the layout itself, removing the need for `onTileResourcesRequest` method for resources mappings. For the best experience, use it with `androidx.wear.tiles.Material3TileService` added in Wear Tiles 1.6-alpha04 version. ([I8198c](https://android-review.googlesource.com/#/q/I8198c47723abcbffbd2e9d5cb727ce844159bc1a), [b/440376391](https://issuetracker.google.com/issues/440376391))

### Version 1.4.0-alpha03

December 17, 2025

`androidx.wear.protolayout:protolayout-*:1.4.0-alpha03` is released. Version 1.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..ec985eed3cba8444e5aaa52a748333397a1298f3/wear/protolayout).

**Bug Fixes**

- Comparing two resources types for the better resource handling and performance improvements is now done using the optimized hash and equals methods. ([82f21b2f](https://android.googlesource.com/platform/frameworks/support/+/82f21b2f6d39b9aa0c0d415863c0658cb9f7a978))

### Version 1.4.0-alpha02

October 22, 2025

`androidx.wear.protolayout:protolayout-*:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/wear/protolayout).

**New Features**

- Added new Platform event source (`isInAmbientMode`) describing whether the device is in ambient mode or not ([Ief832](https://android-review.googlesource.com/#/q/Ief832d113049af76507d9186ea50b00f274929da))

**API Changes**

- The `PendingIntent` `clickable` now accepts a fallback action (`LoadAction`/`LaunchAction`) to be used when `PendingIntent` is not supported by the `ProtoLayout` Renderer. Fallback action will automatically be picked up and placed in the layout when the version of the Renderer is lower than the one supporting `PendingIntent`. ([I6eee2](https://android-review.googlesource.com/#/q/I6eee26a6f710e00ee264e6ab4842766ff87c17fe), [b/450259727](https://issuetracker.google.com/issues/450259727))
- `protoLayoutScope` field within `MaterialScope` is now made `NonNull` for easier usage when `MaterialScope` is created via `materialScopeWithResources`. In addition, there is a `hasProtoLayoutScope` function to check for the presence of it. ([I1858f](https://android-review.googlesource.com/#/q/I1858f9cb4ee014f2147ced6487368b5b891b8b80), [b/450067019](https://issuetracker.google.com/issues/450067019))

### Version 1.4.0-alpha01

September 24, 2025

`androidx.wear.protolayout:protolayout-*:1.4.0-alpha01` is released. Version 1.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/90062705131fa122cdd8d9bed30380b183dc48bd..0c132271cd448b355c7c853ce868820bbb8acbbd/wear/protolayout).

**New Features**

- Added helper method for `LayoutModifier` that makes an element fade in as the tile is becoming visible. ([I38531](https://android-review.googlesource.com/#/q/I38531e66bb598e141f317dea07df21fa94932b7d), [b/390345969](https://issuetracker.google.com/issues/390345969))
- Added `materialScopeWithResources` to support M3 `MaterialScope` concept that also takes care of automatic resource registration. Within it, added new helper methods for images (`backgroundImage` `avatarImage` and icon) that remove the need for manually registering resources in `onTileResourceRequest` when used. ([I525bd](https://android-review.googlesource.com/#/q/I525bd14639347178af77677e48b306f7fe937d6b), [b/428692714](https://issuetracker.google.com/issues/428692714))
- `ProtoLayout` Kotlin helpers for `Image` and `ImageResources` for usage with `ProtoLayoutScope` and automatic resource registration. ([Iada82](https://android-review.googlesource.com/#/q/Iada82004deba3b3f30762c8f8d4a10d580614ae0), [b/430584304](https://issuetracker.google.com/issues/430584304))
- Added getter for how many Lottie properties are allowed in customization of one Lottie animation. ([I73733](https://android-review.googlesource.com/#/q/I73733ededc4c7f2b2e53d76cc2da6c93ffe74006), [b/436532706](https://issuetracker.google.com/issues/436532706))
- Add API in `AndroidLottieResourceByResId` to allow customizing Lottie animation via properties and add API for creating property for theming slot with the slot ID to the specified color. ([I301b3](https://android-review.googlesource.com/#/q/I301b306474eb909a4949f648a9aba2c3dc603f09), [b/423581481](https://issuetracker.google.com/issues/423581481))
- Add provider APIs for accepting `PendingIntent` as click action ([I01978](https://android-review.googlesource.com/#/q/I019786be77ba4a959d43da286dc05e52531238e0), [b/433802488](https://issuetracker.google.com/issues/433802488))
- Add new API in `Image.Builder` - `setImageResource` to set resource object directly to the Image in `onTileRequest`, without a need to register it in mapping in `onTileResourcesRequest`. ([Ifa69a](https://android-review.googlesource.com/#/q/Ifa69afec0f50789934af2b6d7f5dd9a6853eef01), [b/428693523](https://issuetracker.google.com/issues/428693523))
- Added `ProtoLayoutScope` concept in preparation for better resources handling in Tiles. ([I132ce](https://android-review.googlesource.com/#/q/I132ce6910147839f15c95c14ccc4f354b819f387), [b/428692423](https://issuetracker.google.com/issues/428692423))
- `ProtoLayout` Material3 `MaterialScope` now exposes `Context` field as public, for use in methods within the scope, without the need to pass it around. ([I0e5cc](https://android-review.googlesource.com/#/q/I0e5ccaf7605cb50373ee9b8d862a72b57a60bb26), [b/414559956](https://issuetracker.google.com/issues/414559956))
- Make heading semantic APIs public ([I75299](https://android-review.googlesource.com/#/q/I752994155174f5dafbefecd8e8a2eed550a197b2), [b/413653475](https://issuetracker.google.com/issues/413653475))
- Expose `ARC_DIRECTION_*` consts as public for use in `Arc/ArcLine/ArcText/DashedArcLine`. ([I83959](https://android-review.googlesource.com/#/q/I83959aafc7577b3086ce547197bdeea00cbbe567), [b/427556439](https://issuetracker.google.com/issues/427556439))

**API Changes**

- We have deprecated `Image.Builder()` and `Image.Builder.setResourceId` methods in favour of the new automatic resource registration API, available in `Image.Builder(ProtoLayoutScope)` and `Image.Builder.setImageResource` APIs that remove the need for overriding `onTileResourcesRequest`. ([I7bfe6](https://android-review.googlesource.com/#/q/I7bfe6ecc4e5849a27eda55dd993273e440ba69ae), [b/432758526](https://issuetracker.google.com/issues/432758526))
- Move APIs for creating `ProtoLayoutScope` from restricted to public. However, they shouldn't be used as the system already handles those calls. ([I1d8e8](https://android-review.googlesource.com/#/q/I1d8e8d1da2f50eeb9c644b50aa605c42a44fee36), [b/432758251](https://issuetracker.google.com/issues/432758251))

**Bug Fixes**

- Add implementation for supporting `PendingIntent` in `ProtoTiles` ([I38167](https://android-review.googlesource.com/#/q/I38167189ae91141338112412e5f7e90edb7f7e46), [b/430610429](https://issuetracker.google.com/issues/430610429))
- Add `invalidateLayout` method. ([Ief898](https://android-review.googlesource.com/#/q/Ief898a3d891f979937866b5d0208d5b38ead05fa))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- `ImageResource` now has `hashCode` and `equals` methods. ([I650ee](https://android-review.googlesource.com/#/q/I650eece74a9494253f75839454bef2f35bb8c7e6), [b/428692423](https://issuetracker.google.com/issues/428692423), [b/428693523](https://issuetracker.google.com/issues/428693523))
- Add new proto message `PendingIntentAction` and its wrapper builder ([Ie2aca](https://android-review.googlesource.com/#/q/Ie2aca02e235b09b72bf7cf5879fc5158e78b179e), [b/427643502](https://issuetracker.google.com/issues/427643502))
- Reduce how often `ZoneId` instance is created. ([I284d3](https://android-review.googlesource.com/#/q/I284d34506ef0436cec5b25b18eda47c031531966))
- Apply default content description to the single slot `textButton`. ([I0dc8a](https://android-review.googlesource.com/#/q/I0dc8adb271c72f53b7133df4e01d6f44149d8456), [b/415001534](https://issuetracker.google.com/issues/415001534))
- Fix calculations for adjusting max lines in the renderer side. ([I933bc](https://android-review.googlesource.com/#/q/I933bc3969a34c5de4eb320225f3f695db88db4ff), [b/414353620](https://issuetracker.google.com/issues/414353620))

## Version 1.3

### Version 1.3.0

June 4, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0` is released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7938d4e7647114b0f950c73aa11b9ebde3e446b..90062705131fa122cdd8d9bed30380b183dc48bd/wear/protolayout).

**Important changes since 1.2.0**

- Material 3 design comes to the watch, with components and layouts that are optimized for the round display and scale appropriately from small to large screen sizes
  - This includes Kotlin-only, `protolayout-material3` library with more Compose-like APIs for the following components and features:
  - Dynamic color theme coming from the system and watch face with the latest Material3 theme for colors, shapes and typography
  - `MaterialScope` for taking care of all opinionated defaults and easier customization
  - `iconEdgeButton`, `textEdgeButton`
  - `iconButton`, `textButton`, `button`, `imageButton`, `avatarButton`, `compactButton`
  - `titleCard`, `appCard`, `graphicDataCard`, `iconDataCard`, `textDataCard`
  - `circularProgressIndicator`, `segmentedCircularProgressIndicator`
  - `primaryLayout`, `buttonGroup`
  - All components work across any SDK levels and `ProtoLayout` Renderer version, supplying sensible fallbacks where applicable
- More Kotlin-friendly, Compose-like APIs for base ProtoLayout elements
  - `LayoutModifier` with ability to add the most of modifiers as chained functions (`padding`, `contentDescription` (including `clearSemantics`), `background`, `clip`, `opacity` etc.), convertible to the existing `Modifiers` object
  - `LayoutColors` and `LayoutString` as types with easier support for using dynamic fields and constraints
  - `text` and `fontStyle`
  - better map support for `StateBuilder`, including `DynamicDataMap` and factory methods such as `intAppDataKey` for easier creation of `AppDataKey` objects
- Lottie animations support including option to set different triggers on when animation should start, for example when layout is loaded or when layout becomes visible
  - Improved gradient support:
  - Linear gradient API as part of `Brush` that can be used in `Background` modifiers for elements such as `Box`, `Spacer`, etc. ...
  - Allow dynamic color values in `ColorStop` used for linear and sweep gradient
  - Existing Sweep Gradient in arc objects now supports dynamic colors and start and end angles
- Platform data binding in `protolayout-expression` to receive information anytime that layout's visibility is changed, which for example can be use to hide certain parts of the layout while tile is being swiped to
- Testing library - `protolayout-testing` - has been added to support easier Unit test coverage for any ProtoLayout elements
- New element `DashedArcLine` with improved set of features so that line can have dashes, as opposed to the existing `ArcLine`
- `ArcSpacer` support for setting its length in DP dimension instead of degrees
- Added roundness `FontSetting` axis applicable to some fonts

### Version 1.3.0-rc01

May 20, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-rc01` is released with no changes from the previous release. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..c7938d4e7647114b0f950c73aa11b9ebde3e446b/wear).

### Version 1.3.0-beta02

May 7, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-beta02` is released. Version 1.3.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..b6c541571b9fb5471f965fc52612cb280713e5e4/wear/protolayout).

**Bug Fixes**

- We have made an important improvement in the Typography design values that are applied on API 36 and above. This is because from API 36, all Tiles will be in the system font, so this change introduces better consistency in the Tiles carousel. ([If316f](https://android-review.googlesource.com/#/q/If316f7d1e0fe55fbef49c13cfaa354928f34c865))
- `Text`,`Spacer`, `ArcLine` and `DashedArcLine` builders won't throw if `layoutConstraints`for dynamic values are not set. Note that older renderers still require the `layoutConstraints` to be set and will ignore any dynamic value that doesn't have it set. ([Ic52e8](https://android-review.googlesource.com/#/q/Ic52e8094e65c42b6db72c1279ca54b039dd5b182))
- Add heading semantics modifier to indicate that a layout element is heading for a section of content for accessibility purpose, and mark the text in the title slot of `primaryLayout` to be accessibility heading by default. ([Iae1fb](https://android-review.googlesource.com/#/q/Iae1fb4b9202140a5e6e15ed7b877fc9247cc0957))
- Final UX polish of the `primaryLayout` where space between title slot and main slot is decreased to 4dp instead of 6dp on smaller screens. ([I0e056](https://android-review.googlesource.com/#/q/I0e05622367aa163bf743de4a66977ba6ac72fab8))
- Apply default content description to `textEdgeButton`. ([Ifaf8b](https://android-review.googlesource.com/#/q/Ifaf8b4ea0e93381fcce976e80727aeafe1371c1e))
- Minor update to the `avatarButton` inner padding. ([I0910b](https://android-review.googlesource.com/#/q/I0910b02e0b772ee4386e45da71f7e38578bcea52))

### Version 1.3.0-beta01

April 9, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-beta01` is released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..4c37298a97c16270c139eb812ddadaba03e23a52/wear/protolayout).

**New Features**

The 1.3.0-beta01 release of Wear ProtoLayout indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear ProtoLayout 1.3 includes the following new functionalities and APIs:

- Material 3 design comes to the watch, with components and layouts that are optimized for the round display and scale appropriately from small to large screen sizes
  - This includes Kotlin-only, `protolayout-material3` library with more Compose-like APIs for the following components and features:
  - Dynamic color theme coming from the system and watch face with the latest Material3 theme for colors, shapes and typography
  - `MaterialScope` for taking care of all opinionated defaults and easier customization
  - `iconEdgeButton`, `textEdgeButton`
  - `iconButton`, `textButton`, `button`, `imageButton`, `avatarButton`, `compactButton`
  - `titleCard`, `appCard`, `graphicDataCard`, `iconDataCard`, `textDataCard`
  - `circularProgressIndicator`, `segmentedCircularProgressIndicator`
  - `primaryLayout`, `buttonGroup`
  - All components work across any SDK levels and ProtoLayout Renderer version, supplying sensible fallbacks where applicable
- More Kotlin-friendly, Compose-like APIs for base ProtoLayout elements
  - `LayoutModifier` with ability to add the most of modifiers as chained functions (`padding`, `contentDescription` (including `clearSemantics`), `background`, `clip`, `opacity` etc.), convertible to the existing `Modifiers` object
  - `LayoutColors` and `LayoutString` as types with easier support for using dynamic fields and constraints
  - `text` and `fontStyle`
  - better map support for `StateBuilder`, including `DynamicDataMap` and factory methods such as `intAppDataKey` for easier creation of `AppDataKey` objects
- Lottie animations support including option to set different triggers on when animation should start, for example when layout is loaded or when layout becomes visible
  - Improved gradient support:
  - Linear gradient API as part of `Brush` that can be used in `Background` modifiers for elements such as `Box`, `Spacer`, etc. ...
  - Allow dynamic color values in `ColorStop` used for linear and sweep gradient
  - Existing Sweep Gradient in arc objects now supports dynamic colors and start and end angles
- Platform data binding in `protolayout-expression` to receive information anytime that layout's visibility is changed, which for example can be use to hide certain parts of the layout while tile is being swiped to
- Testing library - `protolayout-testing` - has been added to support easier Unit test coverage for any ProtoLayout elements
- New element `DashedArcLine` with improved set of features so that line can have dashes, as opposed to the existing `ArcLine`
- `ArcSpacer` support for setting its length in DP dimension instead of degrees
- Added roundness `FontSetting` axis applicable to some fonts

### Version 1.3.0-alpha10

March 12, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha10` is released. Version 1.3.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/wear/protolayout).

**New Features**

- Add helper for Brush in kotlin Background Modifier. ([I995de](https://android-review.googlesource.com/#/q/I995de06689b1e61d072326ef35fc87612376e81c))
- Mandatory Android Context field has been made public in `MaterialScope` to allow for easier usage in developers' functions that are creating components for Material3 tiles. ([I7df73](https://android-review.googlesource.com/#/q/I7df732e3393013728baf5ec88838cbd6418c0cbf))

**API Changes**

- Rename api `platformVisibilityStatus` to `PlatformEventSources.isLayoutVisible` and add a new experimental API `PlatformEventSources.isLayoutUpdatePending`. ([Ie1e04](https://android-review.googlesource.com/#/q/Ie1e0441eff97a756e750d9fa4a6772135fdbd313))

**Bug Fixes**

- Margins for `primaryLayout` are now properly rounded up instead, which can have effect on some layout up to 2dp space less for the main slot. ([I8f5d3](https://android-review.googlesource.com/#/q/I8f5d39e5a019e783a40fa5392fd4686c0d1b82ea))
- Clarification of default dynamic color theme in `ProtoLayout` Material3 components. ([Iff5f3](https://android-review.googlesource.com/#/q/Iff5f33ef8761b2d5cf4c7c3e2e2e603d5233eb42))
- `Typography.NUMERAL_*` typographies are no longer tabular/monospace by default. If text is animating, it is highly recommended to add `FontSetting.tabularNum()` setting to it. In all other cases this monospace option is not needed and there will be more available characters by not using it. ([Id3cd9](https://android-review.googlesource.com/#/q/Id3cd9c16f8095200e396152e5df7475c3b93df8f))
- Clarification of default dynamic color theme in `ProtoLayout` Material3 components. ([I9d831](https://android-review.googlesource.com/#/q/I9d831a7a73a5f6f06af872a27ca226f3d7365583))

### Version 1.3.0-alpha09

February 26, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha09` is released. Version 1.3.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..fd7408b73d9aac0f18431c22580d9ab612278b1e/wear/protolayout).

**New Features**

- Added experimental modifiers for `enterTransition` and `exitTransition` ([I4a4d6](https://android-review.googlesource.com/#/q/I4a4d6b19d45a9a5ff47eb01924063e156809bb61))
- We have added additional platform binding to receive the visibility status of full layout, whenever it's changed. ([I250c3](https://android-review.googlesource.com/#/q/I250c33d50f6daf8a1ae12ca05acef3069ded68d9))
- Allow injecting testing app state and platform data into `LayoutElementAssertionsProvider` for evaluating dynamic values. ([Ib5fcb](https://android-review.googlesource.com/#/q/Ib5fcb446454230b411cb9955c8285ced27dc6b39))
- Add corner filters to the protolayout testing library ([Ie2361](https://android-review.googlesource.com/#/q/Ie23616f7d5f74929e1ea76cf7e45d4e9c27f5793))
- `ButtonColors`, `CardColors` and `ProgressIndicatorColors` now support copy method, with optional override of some parameters. ([Ie2054](https://android-review.googlesource.com/#/q/Ie20549c875a103d5a2b5629c3c503f96dc9d7034))

**API Changes**

- Add dynamic data binding support to the testing library ([Ib98de](https://android-review.googlesource.com/#/q/Ib98de4912953fc5c2aa877cbf3e47ab6a5c4baea))
- Fix `imageButton` when used with `backgroundImage` function by removing overlay. Additionally, allow for `backgroundImage` function to allow specifying null for overlay color, meaning that overlay won't be applied. ([Ibec3c](https://android-review.googlesource.com/#/q/Ibec3c43dc1fa5c2116c7c4162180f31ebcc66033))

**Bug Fixes**

- Changed default `hasValueOfType` method to throw `UnsupportedOperationException` instead of `IllegalArgumentException`. ([Ia36c3](https://android-review.googlesource.com/#/q/Ia36c325b602670fc5a1ff214a0361471952d1368))
- Default color token values are update to reflect the latest spec. ([I75d44](https://android-review.googlesource.com/#/q/I75d44e1d8e588dd0439220e00f34d6c4508896de))
- Fixes for aliasing issue visible on arc lines in AndroidX tiles renderer. ([I88190](https://android-review.googlesource.com/#/q/I88190b9940492c4a69e71f52ffdce1d62dd5fd7f))

### Version 1.3.0-alpha08

February 12, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha08` is released. Version 1.3.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/wear/protolayout).

**New Features**

- Add `FontSetting` list parameter for Material3 text. ([Ic102d](https://android-review.googlesource.com/#/q/Ic102d8e67624b4379690dc6144f5f0a164ae60f4))
- Added `DynamicDataMap` class which `StateBuilder` now supports for a better type safe Kotlin API for app states ([I012ba](https://android-review.googlesource.com/#/q/I012ba7f0d41d0e9d7da410167857f06b55526f53))
- Added factory methods such as `intAppDataKey` for easier creation of `AppDataKey` objects ([Icea2a](https://android-review.googlesource.com/#/q/Icea2aef015631a8e5db95bf64369a721476f18d0))
- `DynamicDataValue` now has a `hasValueOfType(Class<?>)` method in addition to `hasInt/hasColor/`.... methods ([I4f7a6](https://android-review.googlesource.com/#/q/I4f7a651b21960e8a490e344470ed87975887c7f3))
- We have added `errorDim` to the Material3 ProtoLayout `ColorScheme`, for high priority errors or emergency actions such as safety alerts. ([Ia17bb](https://android-review.googlesource.com/#/q/Ia17bbb91fbe327cc4ac0e57ba22c5cf2b445fac4))
- We have added a guard against a crash when accessing the global reducemotion setting, which was triggered on some platforms where that setting was not provided. ([I01e2c](https://android-review.googlesource.com/q/I01e2c1aa38cc435ff02c1364d337f33df057bd08))

**API Changes**

- `addKeyToValueMapping` is renamed to `addToStateMap` and `DynamicDataMap.put` methods are removed as they were redundant. ([Ibe9dd](https://android-review.googlesource.com/#/q/Ibe9dd9e96cf53e7a394b8996fe3ef546d82317f6))
- Material3 Typography now supports roundness variable axis for system fonts that support this axis. ProtoLayout `FontSetting` supports roundness axis for fonts that support this axis. ([I33eb5](https://android-review.googlesource.com/#/q/I33eb569d1bb26e30fef2681af4ab8b1188a443e5))
- Renamed `multilineAlignment` to alignment in Material3 text method. ([I2b66b](https://android-review.googlesource.com/#/q/I2b66bf21eadebc88ccc4735fde94b895383be9f2))
- Update the circular progress indicator to be Box type, also specify the `mainContent` in `constructGraphic` to be Box type ([I5a3dc](https://android-review.googlesource.com/#/q/I5a3dc270edf5923bd471b1e99db45dc12eff6455))
- Better support for using circular progress indicator in graph ([I039db](https://android-review.googlesource.com/#/q/I039dbfd70937336db2423259963e78a4855aca8d))

**Bug Fixes**

- Allow dynamic values in `ColorStop` and also for start/end angles in `SweepGradient`. ([I0146d](https://android-review.googlesource.com/#/q/I0146d14eaa17e10e6d3012d25348ecd9cc277baa))
- Docs fixes. ([I4a63a](https://android-review.googlesource.com/#/q/I4a63aeb399a23339446e116e09f4f7cf1395af5e))
- Updated Material 3 components (`graphicCard` and `avatarButton`) to provide fallback when `weight` expand dimension is not supported (e.g. below API 33). Updated text component to fallback to `TEXT_OVERFLOW_ELLIPSIZE_END` when `TEXT_OVERFLOW_ELLIPSIZE` is not supported by the renderer. ([I19e2c](https://android-review.googlesource.com/#/q/I19e2cd328c6a6ff6022b51b9cab9347527f984ea))
- Docs update for `PrimaryLayoutMargins`. ([Ibaf7b](https://android-review.googlesource.com/#/q/Ibaf7b9c9f8905d81ac6b89c76ac78e19e5494b1c))

### Version 1.3.0-alpha07

January 29, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha07` is released. Version 1.3.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..4c47131cd5b50c3091fc0874eb606aaac5b168fa/wear/protolayout).

**New Features**

- Added API option to set different triggers for Lottie animations. Additionally, added API for triggers fired when layout is visible ([I8272d](https://android-review.googlesource.com/#/q/I8272de3ae3986ea04debedec2820496fe19e062e))
- Added `border`, `visibility` and `opacity` modifiers. ([I6d3dd](https://android-review.googlesource.com/#/q/I6d3ddd0b40db3f4796aac56e64605ae9d2db1fc7))
- Added avatar button to ProtoLayout Material3 component. ([Idb5ae](https://android-review.googlesource.com/#/q/Idb5aea121b876a50b8e67970d279ff60eb863c3a))
- We are now allowing margins (side and in some cases bottom) to be customized in Material3 `primaryLayout`. ([Ib22f6](https://android-review.googlesource.com/#/q/Ib22f60aa2e9517fc9d0b29611124870fd3346b6d))
- Add the segmented variant of the circular progress indicator. ([I6a648](https://android-review.googlesource.com/#/q/I6a6487139553f9b2c78e1b6a3dd289341cfd85b8))
- Added compact button component to ProtoLayout Material3. ([Ia3c5c](https://android-review.googlesource.com/#/q/Ia3c5c7826057c4aba8816ecfdc8465ea9d4e9e13))
- Added pill shape button and image button components to ProtoLayout Material3. ([Ifb88a](https://android-review.googlesource.com/#/q/Ifb88aa0ebce1b3923f08c012b8e4d65735d0c49b))

**API Changes**

- `LayoutModfier.foldIn` is now called `foldRight` to better reflect its expected behaviour ([Idf242](https://android-review.googlesource.com/#/q/Idf242cd95d2488992ceefd1527bea8a24a3c58ab))
- `VisibleOnce` trigger is now experimental. ([Ib2d26](https://android-review.googlesource.com/#/q/Ib2d26f112223932535db64753c248215865f187d))
- Remove `withOpacity` from the public API as there is a graphics library alternative. ([I030c2](https://android-review.googlesource.com/#/q/I030c2303260eff628957c3ea61dd3261abc1ce89))
- Renamed top level methods in `LayoutString.kt` and `LayoutColor.kt` to have Java friendly names. ([I7aff0](https://android-review.googlesource.com/#/q/I7aff07552243adfc536f87d97e5074ec2e50f8f6))
- Removed non-ProtoLayout typographies in Material3. ([Idd9ae](https://android-review.googlesource.com/#/q/Idd9ae00a09b92406498b4f6a0582907af3725362))
- Add suffix Color to fields in `*Colors` classes in Material3. ([I2d114](https://android-review.googlesource.com/#/q/I2d11471173f508dca1c71f68dbc44177f1d1034d))

**Bug Fixes**

- Add `EdgeButton` fallback implementation for older renderer without asymmetrical corners support. ([I63364](https://android-review.googlesource.com/#/q/I633643616c6621bb7e849a07ee50cefbd958fea7))
- Add fallback implementation of the circular progress indicator with older renderer. ([I0f134](https://android-review.googlesource.com/#/q/I0f134f6b47d2deb395b9b6cae6e042e2f7cbc48c))

### Version 1.3.0-alpha06

January 15, 2025

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha06` is released. Version 1.3.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/wear/protolayout).

**New Features**

- `LayoutColor` to support both static and dynamic color types ([I4c89b](https://android-review.googlesource.com/#/q/I4c89be37830eeed53acd7e45e31c313bad9cea8f))
- Added `ProtoLayout Material3` textButton component. ([Id680d](https://android-review.googlesource.com/#/q/Id680dccddc4e0b21ee0ae2265923c147ccb836d6))
- Add `iconButton` ProtoLayout Material3 component. ([Ica3f0](https://android-review.googlesource.com/#/q/Ica3f073552234d75ab943da53353404cae9c0716))
- Added ProtoLayout Material3 button container component. ([I17a38](https://android-review.googlesource.com/#/q/I17a3855ee16154a756c8a409edaa36413bd958e2))
- Added support for Chainable semantic modifiers to protolayout-material3 ([I4af62](https://android-review.googlesource.com/#/q/I4af627ee03a1befb0332a2b50afe43aaf1a41bcf))
- Added ProtoLayout Material3 single segment `CircularProgressIndicator` ([I2c8a2](https://android-review.googlesource.com/#/q/I2c8a2ca03388b310a5e41a12219a699b04d903c8))
- Added `padding`,`metadata` modifiers ([I8720a](https://android-review.googlesource.com/#/q/I8720ad1c37558445e4aaf142f47f7b10be2bca35))
- Added `background`,`clip` and `clickable` modifiers ([I35478](https://android-review.googlesource.com/#/q/I3547832ab3ace51ea7c39a7be1c7e8818aad11c0))
- Add `LinearGradient` to Brush and allow it to be used in the Background Modifier. ([Ic4dea](https://android-review.googlesource.com/#/q/Ic4dea35a7bdcb089fe91d2d4cdb56af581deca14))
- Add small size for appCard and `titleCard`. ([I91f98](https://android-review.googlesource.com/#/q/I91f983e2c76d5af7c91b1d0c0d36cf4f0d4b94a3))
- Added ProtoLayout Material3 `graphicDataCard` component. ([I92be7](https://android-review.googlesource.com/#/q/I92be7a6fde1c9e0e82c3090227e3a764b270d3f2))
- Added ProtoLayout Material3 `iconDataCard` and `textDataCard` components. ([I4e1e4](https://android-review.googlesource.com/#/q/I4e1e490e7694eb8a00c3114921246c60fc40dc17))
- Added ProtoLayout Material3 `appCard` component. ([Id4c57](https://android-review.googlesource.com/#/q/Id4c5760373f51401aaa17c43cef37665071329fb))
- Abstract `EdgeButtonColors` to `ButtonColors`. ([I83624](https://android-review.googlesource.com/#/q/I83624da0e4585dbcea732dc2485e515ac90121ff))
- Added ProtoLayout Material3 `titleCard` component. ([I2dc72](https://android-review.googlesource.com/#/q/I2dc729f1e0d638a03a6b48355ec5956a8975445c))

**API Changes**

- ProtoLayout Material3 API now accepts `LayoutString` to support both static and dynamic texts. ([I9c24a](https://android-review.googlesource.com/#/q/I9c24a24c4e6b0076ec0256dfdc5302899a0b24a1))

**Bug Fixes**

- Add renderer implementation for inflating `DashedArcLine` ([I0c700](https://android-review.googlesource.com/#/q/I0c70072c7705ff8b43bb4e9aecf2cb97efd3e907))
- Renderer change for allowing `ArcSpacer` to take dp length. ([I1437b](https://android-review.googlesource.com/#/q/I1437b46f7b76d845cbaa6a0a4d073a774b253d38))

### Version 1.3.0-alpha05

December 11, 2024

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9f3e1b6fc190040f287dcfe745fbc438cbed93f9..46295bc0b75a16f452e8e0090e8de41073d4dbb6/wear/protolayout).

**New Features**

- Added `LayoutString` to support bindable layout string fields. ([Ida650](https://android-review.googlesource.com/#/q/Ida6508fcc8298d664f2ad890fa4d7d2ed5b016c0))
- Added `ProtoLayout Material3` card container component. ([Ic985a](https://android-review.googlesource.com/#/q/Ic985a5183b2328de2a01c3cb59b6e76b97cdf16b))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Id1f9b](https://android-review.googlesource.com/#/q/Id1f9b9941068a0c1d4800f112776bb4cf981c7ec), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.3.0-alpha04

November 13, 2024

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/wear/protolayout).

**New Features**

- Updated Material3 shape to be a class with fields that hold the actual Corner value, same as in Wear Compose. ([Ied8cd](https://android-review.googlesource.com/#/q/Ied8cd17340a5d595b8a5ae82540c10760ff2ad95))
- Updated Material3 colors to include `ColorScheme` concept, same as in Wear Compose. ([If645e](https://android-review.googlesource.com/#/q/If645e30349a8fb5372678903069da00f744bdc9e))
- Add multiple commonly used matcher to the testing library. ([Ie5cec](https://android-review.googlesource.com/#/q/Ie5cecd75697f4a3d27b26da40e05e43562cd29b2))

### Version 1.3.0-alpha03

October 30, 2024

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/wear/protolayout).

**New Features**

- Add `LayoutElementAssertionsProvider`, `LayoutElementAssertion` and `LayoutElementMatcher` to the testing library ([Id1110](https://android-review.googlesource.com/#/q/Id11101d0217410f4ab0ddfb571d7624a9fcf0e43))

### Version 1.3.0-alpha02

October 16, 2024

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7/wear).

**New Features**

- Initial version of Material 3 library. Includes `text`, `edgeButton`, `buttonGroup` and `primaryLayout` components.

**Security Fixes**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on version 1.3.0-alpha01 of `androidx.wear.protolayout:protolayout-proto` and `androidx.wear.protolayout:protolayout-external-protobuf` to 1.3.0-alpha02 to address the vulnerability risk.

**External Contribution**

### Version 1.3.0-alpha01

October 2, 2024

`androidx.wear.protolayout:protolayout-*:1.3.0-alpha01` is released. Version 1.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6cfd01b64fd559c7ae948030d262d8bb49e8d19..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/wear/protolayout).

**Bug Fixes**

- Clarified that Roboto and Roboto Flex font family names availability is device dependent. ([I193be](https://android-review.googlesource.com/#/q/I193bed4fdbe2be9d0d2094b058c5b8e38daa37de))
- Enabled Roboto Flex font family in AndroidX Tile renderer. ([I08e94](https://android-review.googlesource.com/#/q/I08e944d64cecd39c293402d617697ef14bf96a8b))

## Version 1.2

### Version 1.2.1

October 16, 2024

`androidx.wear.protolayout:protolayout-*:1.2.1` is released. Version 1.2.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6cfd01b64fd559c7ae948030d262d8bb49e8d19..c082c8e53e6ef0e5f04f181b92dc4b9bc99aae3c/wear/protolayout).

**Security Fixes**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on version 1.2.0 of `androidx.wear.protolayout:protolayout-proto` and `androidx.wear.protolayout:protolayout-external-protobuf` to 1.2.1 to address the vulnerability risk.

### Version 1.2.0

August 7, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0` is released. Version 1.2.0 contains. [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a90014340290143c500c38a4029aea80a9a45c05..d6cfd01b64fd559c7ae948030d262d8bb49e8d19/wear/protolayout).

**Important changes since 1.1.0**

- `FontStyle` has been updated to have additional font support for the variable axes and better font selection API to support upcoming Flex fonts.
- Additional Modifiers support:
  - Transformation modifier offering translation, rotation and scaling with or without animations.
  - Specifying different values (horizontal and vertical) for each corner radius.
- Improved accessibility of all touch targets by extending the tappable area of any element that uses Clickable modifier to be at least `48dp` by `48dp`.
- Improved `PrimaryLayout` and `EdgeContentLayout` by adding `setResponsiveContentInsetEnabled` to better support responsive behavior of these layouts across different screen sizes and improve Tiles consistency.
- Improved scaling/non-scaling of the Material Text for Android 14's non-linear font scaling.
- Improved support for RTL layout direction on all arc elements.

**Additional changes**

- For a more complete set of the changes introduced in version 1.1.0, see the [beta01 release notes](https://developer.android.com/jetpack/androidx/releases/wear-protolayout#1.2.0-beta01).

### Version 1.2.0-rc01

July 24, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..a90014340290143c500c38a4029aea80a9a45c05/wear).

**Bug Fixes**

- We have fixed the standard Material Chip so it can be used as an icon only if none of the primary or secondary label is passed in. ([Iceef9](https://android-review.googlesource.com/#/q/Iceef99c5f276878e544547b66eefb20e97334b10))
- Documentation for Material layouts has been updated to include [visuals](https://developer.android.com/design/ui/wear/guides/surfaces/tiles-layouts#layout-templates) from the relevant page for easier understanding of layouts. ([I0256a](https://android-review.googlesource.com/#/q/I0256ae5900343da270b5bc0c8a27b807a92f9f84))

### Version 1.2.0-beta01

July 10, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..56579bc30499ce39f0d7a6713a065b00c6194206/wear/protolayout).

**New Features**

The 1.2.0-beta01 release of Wear ProtoLayout indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear ProtoLayout 1.2 includes the following new functionalities and APIs:

- `FontStyle` has been updated to have additional font support as following:
  - Setting different font variation setting such as `FontSetting.weight` and `FontSetting.width`
  - Setting the same width for all numeric characters - tabular numerals (`FontSetting.tnum` font feature setting)
  - Improved font selection APIs to support the upcoming flex fonts by specifying preferred font family names to be used.
- Extended `Corner` modifier to support specifying each `CornerRadius` with a separate horizontal and vertical values to allow building elements with asymmetric corners.
- Added a new `Transformation` modifier offering translation, rotation and scaling of `LayoutElement`. These transformations can be animated by using dynamic values.
- Added `setArcDirection` with `Clockwise`, `CounterClockwise` and `Normal` options to all arc elements (`Arc`, `ArcLine` and `ArcText`) for better support in different layout directions (such as LTR and RTL).
- Improved accessibility of all touch targets by extending the tappable area of any element that uses `Clickable` modifier to be at least `48dp` by `48dp`.
- Improved `PrimaryLayout` and `EdgeContentLayout` by adding `setResponsiveContentInsetEnabled` to better support responsive behavior of these layouts across different screen sizes and improve Tiles consistency. Added linter warning to suggest usage of these APIs with a quick fix.
- Improved scaling/non-scaling of the Material `Text` for Android 14's non-linear font scaling.

**API Changes**

- Default font family name (`DEFAULT_SYSTEM_FONT`) is removed as it is implied by not using the `preferredFontFamilies` API. ([I39dab](https://android-review.googlesource.com/#/q/I39dab419cb0ae1461136d8f1a6181ba04ab80985))
- Parameter passed in to the `FontSetting.width` should be positive. ([I1266f](https://android-review.googlesource.com/#/q/I1266f60f35a6bd94e8159fd40e2f1f2ca0b0a8f6))

### Version 1.2.0-alpha05

June 26, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-alpha05` is released. Version 1.2.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..948119be341fa4affc055418e695d8c4c7e5e2e4/wear/protolayout).

**New Features**

- Add `hasText` method to `Material.CompactChip` to check whether the text content has been set. ([I6e8fc](https://android-review.googlesource.com/#/q/I6e8fc44f8f16016c32d958be538ae8b1428e961d))

**API Changes**

- `FontFamily` const are moved to be in `FontStyle` instead of its Builder class. ([I06ced](https://android-review.googlesource.com/#/q/I06cedbe09c134ea693b77b2ed171c60d82113614))
- Update `FontSetting.weight` and `FontSetting.width` API to include Range annotations and change weight's parameter to be int. ([Ia726c](https://android-review.googlesource.com/#/q/Ia726c90657bf0c11b8feb8497e1e646e17da6762))

**Bug Fixes**

- Non-scalable texts in Material library now work correctly with Android 14's non-linear font scaling. ([I6601e](https://android-review.googlesource.com/#/q/I6601e2af6f197ac7da8407a43349bad799fecbc5))

### Version 1.2.0-alpha04

May 29, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-alpha04` is released. Version 1.2.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/wear/protolayout).

**API Changes**

- Added asymmetrical corners API to be able to specify separately each corner's radius with 2 values. ([Icbd69](https://android-review.googlesource.com/#/q/Icbd699ec4aad1c81ab31d854ba91867ea7c3e9d1))
- Extended the `FontSetting` API to include:
  - font feature setting such as setting the font to be tabular. ([If12b7](https://android-review.googlesource.com/#/q/If12b7cbdce9a8db38308408ccc3a28d2d25d2a8e))
  - font variation setting such as setting custom width for variable fonts. ([I2b36d](https://android-review.googlesource.com/#/q/I2b36d8876971c16376a7ab24fc022cfd039bf32c))
- Added font family API to `FontStyle` to allow specifying an order list of which font families should be used. ([Iba9f5](https://android-review.googlesource.com/#/q/Iba9f5cb44a178ccf9748a05b39b192b6d4653b6d))
- Renamed constants for space height between content and secondary label in Material's `LayoutDefaults` that were initially prefixed with "Edge content" to be more generic as they can be applied to both `PrimaryLayout` and `EdgeContentLayout`. ([I4dc32](https://android-review.googlesource.com/#/q/I4dc32916f927888e0e2f10144ea84b14f11b26c1))

**Bug Fixes**

- Renamed naming for variable font axes from `axisName` to `axisTag`. ([I02ba3](https://android-review.googlesource.com/#/q/I02ba3d37e99a048ddbba9134d8957765bc633082))

### Version 1.2.0-alpha03

May 14, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-alpha03` is released. Version 1.2.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/wear/protolayout).

**New Features**

- Added API for setting custom weight values for `FontStyle`. ([I7390a](https://android-review.googlesource.com/#/q/I7390ad4d90d0c4ef4eef5c6ab60fc8d5fac6c2dd))

**Bug Fixes**

- Fix the failure in `getTouchDelegateInfo` due to empty target map. ([I2accf](https://android-review.googlesource.com/#/q/I2accff1bc54b958f9a737a782747c28e91a40dda))

### Version 1.2.0-alpha02

May 1, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-alpha02` is released. Version 1.2.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..fbd1ac175922f44c69a13545d194066ee428b342/wear/protolayout).

**API Changes**

- We've added support for disabling ripple feedback on individual clickable elements. ([If1ede](https://android-review.googlesource.com/#/q/If1ede07acafe2c240dedb7ffd02e4b78488ae080))
- The API for transformation has been removed from `ArcModifiers` as they don't support that feature ([Ic0827](https://android-review.googlesource.com/#/q/Ic08270e4e9c16ec4dc0059b1fa9b0b85100510ec))
- `ArcDirectionProp` Builder now expects a value in the constructor. ([I76ada](https://android-review.googlesource.com/#/q/I76adad8062d98bc57f9ee955a9d88d1b2aaaacd7))
- The `PlatformDataValues.Builder.putAll` method will allow merging one `PlatformDataValue` into another one. ([I50ba3](https://android-review.googlesource.com/#/q/I50ba3f85643fb1916b95e3a29137ac7760b510a6))
- `Text#setIsScalable` is renamed to `Text#setScalable`. ([If920e](https://android-review.googlesource.com/#/q/If920edc451aef10f8161a5acce2fa368dcb5009c))
- Material Text can set whether to use scalable size (grows when user font size is changed) or not. ([Ibc849](https://android-review.googlesource.com/#/q/Ibc849d3ddcfb79dd782669ac09597a599c10d69d))
- We've added the option to set content description to `TitleChip`. ([I5d21f](https://android-review.googlesource.com/#/q/I5d21fef571a06d600b849d509738bd4dd279506d))
- Fixed `CompactChip` to work correctly with icon only and update the API to allow this option. ([I6589e](https://android-review.googlesource.com/#/q/I6589e045abb7beb2d2d7332b9a83258385aa6ab9))

**Bug Fixes**

- Fixed an issue of potential duplicate platform data during initialization. ([Iba0fd](https://android-review.googlesource.com/#/q/Iba0fd638eddf4ca0ffc5f14c9f0f4cc4b1f272c0))
- Introduce a new getter to `DynamicDataNode` to retrieve node cost. The cost is used when acquiring dynamic node quota. Currently, Nodes with fixed values will have a cost of 0, all the other nodes will have a cost of 1. ([Ia33e1](https://android-review.googlesource.com/#/q/Ia33e17613a64eb25db850af0d7a5e004638c4941))
- Remove counting logic from the `NO_OP_QUOTA_MANAGER`. ([Ib50b8](https://android-review.googlesource.com/#/q/Ib50b8872b3f9341b994f758a3c0d5baebae8cc70))
- We have added a lint rule to report a warning when `PrimaryLayout` is used without `setResponsiveContentInsetEnabled` and provide a quick fix. ([I12025](https://android-review.googlesource.com/#/q/I120257c20dfa8912c2a0b4ecaabe843140d16285))
- There is a limit to a number of dynamic expression nodes. ([Iffae8](https://android-review.googlesource.com/#/q/Iffae8e910bac092461fc97ab9a2e02ff9799eaad))

### Version 1.2.0-alpha01

March 6, 2024

`androidx.wear.protolayout:protolayout-*:1.2.0-alpha01` is released. Version 1.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8a15acd27e433b62c26328806e1b2983aa146db1..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/wear/protolayout).

**New Features**

- `ProtoLayout Arc` elements now have the option to add `ArcDirection` (`Clockwise`, `Counterclockwise` or `Normal`) to it. Adding this behavior to `Arc`, `ArcLine` or `ArcText` will fix their behavior on RTL layouts. ([I90699](https://android-review.googlesource.com/#/q/I9069975f2cd49f52bd6f59c2b5b19513fcda5cc8))
- `EdgeContentLayout` has been updated with a new `setResponsiveContentInsetEnabled` setter to achieve better alignment with the UX guidelines, consistency in Tiles by having primary label at the fixed place on top and responsive inset for labels. ([I60175](https://android-review.googlesource.com/#/q/I601758f8aded4afd9fd40ce0df4f54d5b4176416))
- We have added `PrimaryLayout.setResponsiveContentInsetEnabled` that adds responsive inset to the primary label, secondary label and bottom chip in this layout, to avoid that content going off the screen edge. ([I0c457](https://android-review.googlesource.com/#/q/I0c457c7da75beeb9d41536478d3c6e25d515a030))
- Adds method to remove outer margins from `CircularProgressIndicator` so it can be used as a smaller component. ([I55c06](https://android-review.googlesource.com/#/q/I55c060580dee3bf3719a340043faf81d91c930f2))

**API Changes**

- Tiles renderer now excludes font padding on all text elements by default, without an option to include it. ([I3e300](https://android-review.googlesource.com/#/q/I3e30040588339a2e95df3491ff384fbd518af939))

**Bug Fixes**

- Fixed Text alignment issue when ellipsize, letter spacing and center align are all used on Text. ([I716c7](https://android-review.googlesource.com/#/q/I716c70d5c35ac599c9bb87eaa1cbd4f2172cbdf9))
- Add a workaround for a skia arc drawing issue. ([I08f09](https://android-review.googlesource.com/#/q/I08f09eb58257228bb74aba3319a8510fb85d57f8))
- Fix `ArcLine` drawing direction for RTL layouts. ([I6c141](https://android-review.googlesource.com/#/q/I6c141ef4786547dd1c4ea8f681bf32850c1dbdbb))

## Version 1.1

### Version 1.1.0

February 7, 2024

`androidx.wear.protolayout:protolayout-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38756a2fd525d921dd921f38b03e0d9a23150db7..8a15acd27e433b62c26328806e1b2983aa146db1/wear/protolayout)

**Important changes since 1.0.0**

- Gradient support and better representation of lengths larger than 360 degrees in `ArcLine`.
- Date-time formatting supports different time zones for dynamic data types.
- Better text autosizing and ellipsizing options, to handle truncated text.
- Spacer supports expanded dimensions with optional weight.
- Schema version requirement annotation to all `ProtoLayout` APIs.
- Extended target area to any `Clickable` element to 48 dp x 48 dp, to satisfy accessibility requirements.
- Font padding is turned off by default and is the only behavior across all Text elements and Material components that contain text.

**Additional changes**

- For a more complete set of the changes introduced in version 1.1.0, see the [beta01 release notes](https://developer.android.com/jetpack/androidx/releases/wear-protolayout#1.1.0-beta01).

### Version 1.1.0-rc01

January 24, 2024

`androidx.wear.protolayout:protolayout-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..38756a2fd525d921dd921f38b03e0d9a23150db7/wear)

**Bug Fixes**

- `PlatformTimeUpdateNotifierImpl` ticks immediately after enabling update. ([I77145](https://android-review.googlesource.com/#/q/I77145ea4660494b356cf9a41b6382a048f9073d0))
- `CircularProgressIndicator` has been fixed for RTL layouts. From now on, it will go clockwise in all cases. ([I95ee3](https://android-review.googlesource.com/#/q/I95ee33900bd0a83ccf11f530351209b8daada68a))
- Add a workaround for a skia arc drawing issue. ([I08f09](https://android-review.googlesource.com/#/q/I08f09eb58257228bb74aba3319a8510fb85d57f8))

### Version 1.1.0-beta01

January 10, 2024

`androidx.wear.protolayout:protolayout-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/wear/protolayout)

**New Features**

The 1.1.0-beta01 release of Wear ProtoLayout indicates that this release of the library is feature complete and the API is locked (except where marked as experimental). Wear ProtoLayout 1.1 includes the following new functionalities and APIs:

- `ArcLine` now supports gradient by adding `Brush` with `SweepGradient` and having a shadow on the cap to better represent length larger than 360 degrees by adding `Shadow` on the existing `StrokeCap`.
- `DynamicInstant` has support for zoned date-time formatting. `DynamicInstant` and `DynamicDuration` can be used as state or platform data types.
- Autosizing feature for text size that allows setting multiple sizes to `FontStyle.setSizes` where the Text size will automatically scale based on the space it has inside of the parent. Additionally, we improved ellipsizing options for text that overflows by adding `TEXT_OVERFLOW_ELLIPSIZE` and deprecating `TEXT_OVERFLOW_ELLIPSIZE_END`.
- `Spacer` now supports having expanded dimensions with optional weight. For building `ExpandedDimensionProp` we have added a helper method `DimensionBuilders.weight`.
- Support for dynamically hiding and unhiding layout elements with `Modifier.visible`. This includes having dynamic values in `BoolProp`.
- All `ProtoLayout` APIs now have schema version requirement annotation and version can be checked before calling a newer API.
- Every element that has `Clickable` now has its target area extended to at least 48x48 in the renderer to better support accessibility requirements.
- Following other Material components and Compose initiatives, we have now turned off font padding by default on all `Text` elements. Additionally, `AndroidTextStyle` and related setters have been removed from the public API. with following bug fixes:
- Added a setter for positioning the edge content in `EdgeContentLayout` so it can be positioned before other content.
- Consistently throwing an exception when encountering an unrecognized enum value.
- Invalidate the result of an expression when it yields an invalid numeric value (NaN or infinite) or throws an `ArithmeticException`.

**API Changes**

- Updates to `SweepGradient` API to allow accepting either colors or `ColorStops` in the constructor. ([I6676f](https://android-review.googlesource.com/#/q/I6676fc2767a57f9ed2f88e07acebf929de56ef5e))

**Bug Fixes**

- Adding a restricted API and renderer support for setting a direction in which arc elements are drawn. ([Idef5a](https://android-review.googlesource.com/#/q/Idef5af32d4b85f0d398448142a80507e4f8c10d4))
- `RoundMode` defaults to `Floor` in `FloatToInt32Node` when unspecified. The node will still throw an exception if the provided `RoundMode` is unrecognized. ([I1b2d8](https://android-review.googlesource.com/#/q/I1b2d8c2b8b98fd28fc7062e339e193d88dd80d8f))

### Version 1.1.0-alpha04

December 13, 2023

`androidx.wear.protolayout:protolayout-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/wear/protolayout)

**New Features**

- `VersionInfo` class not implements the `Comparable` interface. ([I8d13c](https://android-review.googlesource.com/#/q/I8d13c23e60d8e7b562a3c422859120883983e942))
- Renderer now supports `TEXT_OVERFLOW_ELLIPSIZE` option. ([I7f085](https://android-review.googlesource.com/#/q/I7f085fb841240511cd136c1e095d9c2ff0d60205))

**API Changes**

- Text overflow option `TEXT_OVERFLOW_ELLIPSIZE_END` is now deprecated. Please use the new API `TEXT_OVERFLOW_ELLIPSIZE` with very similar behavior. ([I822d8](https://android-review.googlesource.com/#/q/I822d8a88c003c79d6c0e93f9294bbb3933cda8f1))
- Following other Material components and Compose initiatives, we have now turned off font padding by default on all Text elements. Additionally, `AndroidTextStyle` and related setters have been removed from the public API. ([I79094](https://android-review.googlesource.com/#/q/I790940f33bd42f023182d4e3a467ee66f4329bce), [Ib0b03](https://android-review.googlesource.com/#/q/Ib0b035f942641f3d1dbbd6ba2254a0720e1b7951), [I32959](https://android-review.googlesource.com/#/q/I329598c92ed34d0ee80ce2db7d2d7f021d2c6883), [Iaf7d5](https://android-review.googlesource.com/#/q/Iaf7d5d0b44de4aee42461b1d2d6a3a54bbb978c9), [Ifa298](https://android-review.googlesource.com/#/q/Ifa298973d6e9df7431d07749b04b4dffb764dcac), [I0a4ae](https://android-review.googlesource.com/#/q/I0a4ae3f8afc6acaa220a6beec029e783cd2910d0), [Ida9d3](https://android-review.googlesource.com/#/q/Ida9d3572ccee63386d6b12c6c475e8b2e9647a9c))
- `Modifier.hidden` is replaced with `Modifier.visible` ([I56902](https://android-review.googlesource.com/#/q/I569023c9beaf2e2a0b1a99e6d7cb982432d9538a))
- `FontStyle#setSizes` now accepts int instead of `SpProp` arguments. ([I02b37](https://android-review.googlesource.com/#/q/I02b37ecda691c52a664e5e8f251be0758bbf9a59))

**Bug Fixes**

- Throw an exception when encountering an Undefined or Unrecognized enum value. ([I9d2cf](https://android-review.googlesource.com/#/q/I9d2cf9b006cbcb2769c70218a1c16e0b97a20b6d))
- Refactor `DynamicTypeBindingRequest`. ([I27b57](https://android-review.googlesource.com/#/q/I27b579480071330a12f6655d1d8396e25ef97dab))
- Invalidate the result of an expression when it yields an invalid numeric value (NaN or infinite) or throws an `ArithmeticException`. ([I681ae](https://android-review.googlesource.com/#/q/I681ae666cda14e9f9dbccd8f561ea94b6170b9f3))

### Version 1.1.0-alpha03

November 29, 2023

`androidx.wear.protolayout:protolayout-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/wear/protolayout)

**New Features**

- Add experimental support for dynamically hiding/unhiding layout elements ([I64a78](https://android-review.googlesource.com/#/q/I64a78ae6173cc74e28db2ba8b9225df9fdc0b217))
- Add dynamic value support to `BoolProp` ([I2fe96](https://android-review.googlesource.com/#/q/I2fe96d0ce123d694d15d14ede02e6f20c8b4f95c))
- Add schema version requirement annotation to `ProtoLayout` APIs ([I0f03c](https://android-review.googlesource.com/#/q/I0f03cc51fa3374cda092b93e3c38b068f76cf235))
- Extending the API with the new option in `TextOverflow` for ellipsizing the Text in a fixed parent container even when max lines is not reached (but there's not enough space for Text). ([I110a9](https://android-review.googlesource.com/#/q/I110a9598aca5c6bcf58afe24b47a6f4264f9a72c))
- Added helper method `DimensionBuilders.weight` for building `ExpandedDimensionProp` with weight. ([I4f72b](https://android-review.googlesource.com/#/q/I4f72bee665cbd4e908cc0a85c81f25004257506b))
- `DynamicInstant` and `DynamicDuration` can be used as state or platform data types. ([I6819f](https://android-review.googlesource.com/#/q/I6819f24246778cd1e3ed709f2c2c109ed83fa3ea))

**API Changes**

- Update The API to hide `DynamicZonedDateTime` and move all its operations to `DyanamicInstant` ([I34b94](https://android-review.googlesource.com/#/q/I34b948f1881e44ed417bc2a68d9ac340567e025a))
- Spacer now supports Expanded dimension for width/height. ([Ie7c94](https://android-review.googlesource.com/#/q/Ie7c94f96a028f9f31a74bf6641e19023e10d6625))
- Support click target area extension in Renderer ([I39c79](https://android-review.googlesource.com/#/q/I39c79d4f9d6dcf2afb2a2fdc6bbae8a249beaca5))

### Version 1.1.0-alpha02

November 15, 2023

`androidx.wear.protolayout:protolayout-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..312eb9f1ddece3a18317f18515a877e0e745cb2c/wear/protolayout)

**New Features**

- Added an `ArcLine` `StrokeCap` `Shadow` field to the API. ([I830ec](https://android-review.googlesource.com/#/q/I830ec5416f94cd789bc536759bfd85c17957d097))
- Extending the API to be able to specify Spacer's width or height to expand. ([I757ca](https://android-review.googlesource.com/#/q/I757ca61bd85315ae0ea22a1d68ccf7010d0e3031))
- We have added an experimental API to automatically scale the text size based on the space it has inside of the parent. ([Ibbe63](https://android-review.googlesource.com/#/q/Ibbe632447dcf28a9948a0877f193b4912acb23d1))
- Support minimum clickable size ([I178e3](https://android-review.googlesource.com/#/q/I178e33822f11755435236a4ca13cd754ab1244c5))
- Added renderer support for `StrokeCap` `Shadow`. ([I48b17](https://android-review.googlesource.com/#/q/I48b177194ede8fb8d365cab01998c89e0a2b44cd))
- Add renderer support for Sweep Gradient in `ArcLine`. ([I4d5bb](https://android-review.googlesource.com/#/q/I4d5bb5948d2216dca2a29d2449fd97519b2b65bb))

### Version 1.1.0-alpha01

October 18, 2023

`androidx.wear.protolayout:protolayout-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b9b10aa25e1bd67bdb78cc13bac036cb58657587..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/wear/protolayout)

**New Features**

- Added a brush option to `Arcline`, with support for `SweepGradient`. ([Ie7ce3](https://android-review.googlesource.com/#/q/Ie7ce34644bccd3bfe17f0d551be4a2b57caaa767))
- Added support for zoned date-time formatting. ([Ibfae0](https://android-review.googlesource.com/#/q/Ibfae0abe71a3b7e88dd72500293afc6f59032856))
- Added protos and java Wrappers required for zoned date-time formatting. ([I97126](https://android-review.googlesource.com/#/q/I971267de203f5c9c8a29246fa78eefe505e59c00))
- Added getters for reading back the value stored in a `DynamicDataValue`. ([Ie6cea](https://android-review.googlesource.com/#/q/Ie6cea66c8938ea363ad0067f75cbae856df0917f))
- Added a setter for positioning the edge content in `EdgeContentLayout` so it can be positioned before other content. ([Ie8e8a](https://android-review.googlesource.com/#/q/Ie8e8a4d033d8ef2059620094b38e5119a4ab08d7))

**Bug Fixes**

- Fixed an issue when an expression with multiple time data source registrations was not being updated immediately. ([I8e1a8](https://android-review.googlesource.com/#/q/I8e1a80ea606a831433f81c9454605803a24b4c8e))
- Fixed a bug to center root element during diff updates. ([Ie48f7](https://android-review.googlesource.com/#/q/Ie48f781568c7a6295e816c613173b90432bb54ec))
- Unset (or empty) layout constraint values will not be ignored anymore. ([Ibc785](https://android-review.googlesource.com/#/q/Ibc78519a3a1f8a433cb1d846e1eed783f5a81fa2))
- Reduced delay between a layout becoming visible and its pipeline nodes being initialized. ([I38d4e](https://android-review.googlesource.com/#/q/I38d4e8cd73037e5099f1b88f595b659cbc8436a5))

## Version 1.0

### Version 1.0.0

August 9, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/07457ca20d6ae00c8e2ca5fb141efd40de8ac6ee..b9b10aa25e1bd67bdb78cc13bac036cb58657587/wear/protolayout)

**Major features of 1.0.0**

ProtoLayout library introduces APIs for creating layouts and expressions that can be used across different Wear OS surfaces. For example Tiles library uses these APIs to support platform data binding (for faster tile data updates) and animations.

### Version 1.0.0-rc01

July 26, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..07457ca20d6ae00c8e2ca5fb141efd40de8ac6ee/wear/protolayout)

- To migrate from Tiles to `ProtoLayout`, please follow the instructions [here](https://gist.github.com/NedaTop/68c6e708f5584061a3daf8a9e7321cfd).

**API Changes**

- We have removed `setLayoutConstraintForDynamicAnchorAngle`and `getLayoutConstraintForDynamicAnchorAngle` methods from Arc element. These methods have been added by mistake and they didn't have any effect on the provided layout. ([If7d01](https://android-review.googlesource.com/#/q/If7d011f5ea0b36422aed9688d1801285a1c6c0aa))
- We have limited the maximum depth that a `ProtoLayout`'s layout can have to 30 nested `LayoutElements`. ([I8a74b](https://android-review.googlesource.com/#/q/I8a74b20b153652f324aa31ef9595edfaa72266c4))

**Bug Fixes**

- We have added a check to throw if `DynamicColor` has been set for a `SpanText`. ([I0e5bc](https://android-review.googlesource.com/#/q/I0e5bc52a43969117a6f009fca2aa134b17ee1023))
- It is clarified that `DAILY_CALORIES` data source unit is kcal. ([Iaa785](https://android-review.googlesource.com/#/q/Iaa78565952cd7d86ce767a97e768b629c4504ad3))

### Version 1.0.0-beta01

June 21, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..3b5b931546a48163444a9eddc533489fcddd7494/wear/protolayout)

**New Features**

- Allow setting clock for time binding tests. ([I05622](https://android-review.googlesource.com/#/q/I05622de839bbdce144e6f6863a2b4d1a310ee17d))

**API Changes**

- `PlatformDataReceiver.onData()` and `StateBuilders.Builder.addKeyToValueMapping` now accept type-safe mapping of `DynamicDataKey` to `DynamicDataValue` rather than unsafe generics. That means that `DynamicDataValue` is now typed with its `DynamicType`. `HEART_RATE_ACCURACY_X` constants moved to the root of `PlatformHealthSources`, to match other Android constants positioning. `HEART_RATE_ACCURACY_X` int constants are now used directly in `DynamicHeartRateAccuracy.constant()` and `DynamicHeartRateAccuracy.dynamicDataValueOf()` instead of value constant. ([I82ff5](https://android-review.googlesource.com/#/q/I82ff585eadbbe15c7e5ed4227908a6cb7462ad23))
- The `PlatformHealthSources.Constants` class was instantiable by mistake. This has been fixed now. ([Icb849](https://android-review.googlesource.com/#/q/Icb8495d814744c05566e1440dc0a52c73619ee59))
- `PlatformTimeUpdateNotifier#setReceiver` now receives `Runnable` instead of `Supplier` function and `Executor` to notify on. ([I9d938](https://android-review.googlesource.com/#/q/I9d938801d769f050ce2e103a616d19f7f588484d))
- We have changed the parameter type in the `PlatformTimeUpdateNotifier#setReceiver` from `Callable` to `Supplier`. ([I664bf](https://android-review.googlesource.com/#/q/I664bf13fb47a8da7b8e0348d5d8cee5a2e14dbe4))
- `CompactChip` and `TitleChip` now support adding an icon to it. ([I5a01e](https://android-review.googlesource.com/#/q/I5a01e3366000b21651e686f04a3279f722cbbf1c))

**Bug Fixes**

- Update Prop messages with dynamic fields to use oneof instead ([I81739](https://android-review.googlesource.com/#/q/I817390a7f8870a6b6e4a61402fa571391b9923bc))
- Reuse setters implementation for overloads that have setters ([Ied70c](https://android-review.googlesource.com/#/q/Ied70c5e18f964fb5c46a2ca379274ff734456a05))
- Properly record fingerprints in setters that have overloads ([I86ed2](https://android-review.googlesource.com/#/q/I86ed2ffe3e48f01f7c547862b9699c5437ae3cf4))

### Version 1.0.0-alpha11

June 7, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..73f902dee011bfe400d8a0330bfd8d4bb632065f/wear/protolayout)

**New Features**

- We've added a `PlatformDataKey` for heart rate accuracy. ([I7f9b8](https://android-review.googlesource.com/#/q/I7f9b83f36e8edd2912a3dfef1eced6296330c4e5))

**API Changes**

- Rename `StateBuilders#getIdToValueMapping` to `getKeyToValueMapping` and change the return type to `Map<<AppDataKey<?>,DynamicDataValue>`. ([Iaa7ae](https://android-review.googlesource.com/#/q/Iaa7aeef4e3751e37bfc492a1dd1fd651ec5ce092))
- Make `StateStore` a final class ([I408ca](https://android-review.googlesource.com/#/q/I408cafba33169e6b07a6c9debb7d2f2b56b9b347))
- `TimeGateway` interface has been replaced by `PlatformTimeUpdateNotifier` in `protolayout-expression-pipeline` library which provides desired frequency for updating time data. ([I60869](https://android-review.googlesource.com/#/q/I6086959e2fd462f215f61a0ceebd98c36fbbb326))
- Rename `register`/`unregisterForData` in `PlatformDataProvider` to `set`/`clearReceiver` ([I14b02](https://android-review.googlesource.com/#/q/I14b02a434647104d59e17a19caba147f46ac85b7))
- In Material Text, `getExcludeFontPadding` has been renamed to `hasExcludeFontPadding`. ([Iea01d](https://android-review.googlesource.com/#/q/Iea01de087006cb97449cce8ce0ad8fff2cf3a039))
- Setter for perfectly aligning label was added to all chip components. All chips now have min tappable target applied. ([I8ae92](https://android-review.googlesource.com/#/q/I8ae92f1eadcc27322432cea3d9c7ac9f8d65a11e))
- `LayoutDefaults#BUTTON_MAX_NUMBER` has been renamed to `MAX_BUTTONS`. ([I84788](https://android-review.googlesource.com/#/q/I84788e1c725407107a85822784dd259ddd613418))
- `DAILY_DISTANCE` is renamed to `DAILY_DISTANCE_M`. ([I4f758](https://android-review.googlesource.com/#/q/I4f758b14023333b85325c8a26e28859511fc9b4e))

**Bug Fixes**

- Update Prop types docs to clarify why static value is enforced. Specify the default value used if static value wasn't provided. ([I155aa](https://android-review.googlesource.com/#/q/I155aacdd1aff6e759726984a878d7ac294b68218))
- `PlatformDataKey` namespaces should follow Java style naming. ([I47bda](https://android-review.googlesource.com/#/q/I47bda5f15c70d7da47d254e6d5d08cd821cea3ac))

### Version 1.0.0-alpha10

May 24, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/wear/protolayout)

**New Features**

- Add `AppDataKey` for accessing app pushed state; Add `PlatformDataKey` for accessing platform data; Add namespace support in `StateStore`. ([I7985e](https://android-review.googlesource.com/#/q/I7985e7716a77b46a2ea3cee5f9009eead48b96d1))
- Support `Equal` and `NotEqual` operations for `DynamicBool`. ([I6a0c1](https://android-review.googlesource.com/#/q/I6a0c1b592c5387781acbf9d550aeda936ffbf0bd))

**API Changes**

- `FontStyles` class is now final ([Iaa2ea](https://android-review.googlesource.com/#/q/Iaa2eacde5352fd55c3a6ddcbce34e3fc69a45290))
- `LayoutElementBuilders#FontStyles` has been deprecated. Please use `androidx.wear.protolayout.Typography` or create your own `FontStyle`. ([Ic929b](https://android-review.googlesource.com/#/q/Ic929b0d8210631ba4e02a79caa1e00a2db51289e))
- Hide `Action#Builder` nested interface from `Action` interface. Implementations of Builder are already provided by `LoadAction` and `LaunchAction` classes. ([I1d70c](https://android-review.googlesource.com/#/q/I1d70c15ccebf6b5a2d71d412b333e000b7d12b4a))
- Allow using `DynamicFloat` with `FloatProp`. Note that `FloatProp` do no require layout constraints as it's not used as a layout changing prop. ([I286ac](https://android-review.googlesource.com/#/q/I286acc231277d13265430b34903a79f3132c798b))
- The `LoalAction` and `SetStateAction` actions are removed as they were not really supported yet. ([I5d6a6](https://android-review.googlesource.com/#/q/I5d6a6472a235179c790d454234faf90972579e84))
- Added support for ARGB_8888 format for inline image resources. ([I8a07c](https://android-review.googlesource.com/#/q/I8a07cd77c4e2e3b850eb5d781a9777df0971271b))
- Rename `StateEntryValue` to `DynamicDataValue`, and update the state APIS to use the `DynamicDataKey` ([If1c01](https://android-review.googlesource.com/#/q/If1c01335804c5dd98dd2c326ec560e1816ec4c77))
- We are limiting the number of entries that are allowed in the `StateStore` in order to ensure that memory usage and state update time are well contained and controlled for each instance of the `StateStore`. As a result, the developer needs to ensure that they do not have more than `MAX_STATE_ENTRY_COUNT` entries in the map otherwise they will get an `IllegalStateException` when creating or updating the `StateStore`. ([Ibadb3](https://android-review.googlesource.com/#/q/Ibadb3c422ade12c5d77cfedac1a806e8d7b0c756))
- Hide `OnLoadTrigger` and `OnConditionMetTrigger` classes, and rename `setTrigger` to `setCondition` for `OnConditionMetTrigger`. ([Ibf629](https://android-review.googlesource.com/#/q/Ibf62995413059ef51f24400b5483053bf0642af8))
- For performance and compatibility reasons, the `ProtoLayout` renderers won't support the full set of features in `AnimatedVectorDrawable` resources. We're marking those APIs as experimental until we can define the supported set. ([Ic6daf](https://android-review.googlesource.com/#/q/Ic6daff3d74e67ca273a353f13cd89ffb412560bb))
- Added dynamic types for daily distance, daily calories and daily floors. Keys for platform health sources are now under `PlatformHealthSources.Keys` ([Ib7637](https://android-review.googlesource.com/#/q/Ib76376c44708ba49e4ad2253199db176f89972bf))
- The `Easing.cubicBezier` method replaces the `CubicBezierEasing.Builder`. With that the `EasingFunction` class is removed and the easing constants from that class are now directly accessible from the `Easing` interface. In addition `setInfiniteRepeatable` is replaced by `INFINITE_REPEATABLE_WITH_RESTART` and `INFINITE_REPEATABLE_WITH_REVERSE` ([Ib41e7](https://android-review.googlesource.com/#/q/Ib41e7d7be686700b87ab1658b05fce4353c5bc54))
- Implement `PlatformDataProvider` to provide heart rate and daily steps. `SensorGateway` interface is removed from public API. ([I55b84](https://android-review.googlesource.com/#/q/I55b84b6b9bffc5f0a6b812307f1bd4ad61750d65))
- Add `PlatformDataProvider`, and update `StateStore` to register to `PlatformDataProvider` when the provider's supported key is required by node from expression pipeline. ([Ib616a](https://android-review.googlesource.com/#/q/Ib616a971f2e6180f7910e17986658f5c5ff7ffde))
- `SensorGateway` is no longer `Closeable` as it no longer maintains any state. ([I6b4f7](https://android-review.googlesource.com/#/q/I6b4f7c2708e03b2b5fd6ca88f3d2fa1b87ef85ce))
- Allow using `FloatProp` with `DynamicFloat` for progress in `CircularProgressIndicator`. This is supported for renderers supporting version 1.2. Old renderers will fallback to the `staticValue` if provided, otherwise to 0 ([I0d91b](https://android-review.googlesource.com/#/q/I0d91bf75cbfb83ff24f6aac1998cb5f0e84841d0))
- `MultiButtonLayout` constants have been refactored into `LayoutDefaults.MultiButtonLayoutDefaults` class which now contains those for button sizes depending on a number of buttons in the layout. ([I13973](https://android-review.googlesource.com/#/q/I139736fe7d393a2de24a38eda667f7d4da324880))
- Support using `StringProp` with `DynamicString` in Material Text. This is supported for renderers supporting version 1.2. Old renderers will fallback to the provided static value. Update `Text#getText` return type from `String` to `StringProp`. ([I7275b](https://android-review.googlesource.com/#/q/I7275becaaadab803a6a56c5a59185bcfc009a0de))

### Version 1.0.0-alpha09

May 10, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/wear/protolayout)

**New Features**

- We've added an experimental extension layout element. Note that this can't be used by default and requires a renderer extension capable of understanding the layout element. ([I6581d](https://android-review.googlesource.com/#/q/I6581dae6a6570c761f53ddd7f5634aa59beb64ef))
- Added `StrokeCap` support for `ArcLine`. ([I94951](https://android-review.googlesource.com/#/q/I94951c20ab62491fa3d4eafdc119b80a66dc5431))
- Added support for Conditional Instant operation. ([I489a7](https://android-review.googlesource.com/#/q/I489a7a4d0dcf9a9a2429c167438090240f0a3d66))
- Added support for Conditional Duration operation. ([Iab469](https://android-review.googlesource.com/#/q/Iab469da679989bee7bbb4ffcf202a3b34cb148a4))
- Added support for creating duration from seconds. ([Ib5fa1](https://android-review.googlesource.com/#/q/Ib5fa1cd3ae4f52a065b22183182325d47c18da44))

**API Changes**

- `enable/disablePlatformSource` methods have been removed from `DynamicTypeEvaluator`. The caller should be responsible for updates. ([I78c6d](https://android-review.googlesource.com/#/q/I78c6ded36efae049d0143eece16054c050a413c8))
- Allow capping the size of bound data types. ([Ie2966](https://android-review.googlesource.com/#/q/Ie29669c5e3fd935de8cad63b3a61d79db582d68f))
- Add support for dynamic content description in `protolayout-material`. ([I62c8e](https://android-review.googlesource.com/#/q/I62c8ea3e4a3592cf96eefa32043a93e9882f9a5b))
- Use long and `@IntRange` for duration and delay in AnimationParameters. ([I388b6](https://android-review.googlesource.com/#/q/I388b606dc0f7f56e5f4c549f57e252f29ba70b3f))

### Version 1.0.0-alpha08

April 19, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/wear/protolayout)

**New Features**

- `AndroidTextStyle` has been added to `LayoutElementBuilders`. ([I8d967](https://android-review.googlesource.com/#/q/I8d9679cf4f945cbf4d833d3531fbdc7a22a15c0e))
- We have added support for setting excluding font padding in `ProtoLayout` Material Text. ([I17f5d](https://android-review.googlesource.com/#/q/I17f5d19d185f429db5946eb3c1202c27b60b25db))
- ARGB_8888 is now supported for inline images. ([I18c1e](https://android-review.googlesource.com/#/q/I18c1e776878fdca2b54bc3d7ba7dd7d43e1983fb))
- `DynamicColor` now supports `onCondition`operation. ([I10927](https://android-review.googlesource.com/#/q/I10927f4a23c6d2694cf2ed78c4fa3fc0444516ee))

**API Changes**

- Support custom duration for reverse animation ([I3251f](https://android-review.googlesource.com/#/q/I3251f683678b064261d06b15c9f878f70b472657))
- We've added the `SemanticDescription` modifier. In addition, `ContentDescription` is not bindable. ([I3f1d](https://android-review.googlesource.com/#/q/I3f1ddb095ce46e1b6f28860bd5430cf206fcf92e))
- The `DynamicBool.isFalse()`method is now replaced with `DynamicBool.negate()` and the `DynamicBool.isTrue()` is removed. In addition NaN `DynamicFloat` values and narrowing a `DynamicInt32` to a `DynamicFloat` now emit an invalid dynamic result. ([I6ac1e](https://android-review.googlesource.com/#/q/I6ac1ed2923be1f3cd8673986f37f9dff512c6f6e))
- Int and float formatters now use the Builder pattern. ([Ieb213](https://android-review.googlesource.com/#/q/Ieb2130848bf6a705a8f9004d739af6b8c33d3234))

**Bug Fixes**

- Fallback static value has been removed from animatable fields. ([Ifcb01](https://android-review.googlesource.com/#/q/Ifcb0192ad3a1f44405d7c52b4e66d559e63cbf36))
- `DynamicTypeValueReceiver#onPreUpdate` has been removed. ([I2dc35](https://android-review.googlesource.com/#/q/I2dc3582d8e5b586c8c1904ef26fb2f740b3d9d8d))
- Length of Strings in dynamic expressions are now capped. ([I4c93](https://android-review.googlesource.com/#/q/I4c9344c54ab35e165871b9831c0c85156b058dce))
- The gradle dependencies are now correctly set to `api` instead of `implementation` when required. ([I40503](https://android-review.googlesource.com/#/q/I40503c70b2ea9e9d37047b4d52f4dd1c4905f5fd))

### Version 1.0.0-alpha07

April 5, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/wear/protolayout)

**New Features**

- Add dynamic value support to `StringProp` ([I04342](https://android-review.googlesource.com/#/q/I043426ec603714a093f98ca9ff7b9861e15562af))
- Mark bindable layout elements ([Ia110b](https://android-review.googlesource.com/#/q/Ia110be4ebe6af6160bd4fa87a57a05f3d241223b))

**API Changes**

- `sensorGateway#registerSensorGatewayConsumer` takes data type as a parameter instead of method in Consumer. ([Icf314](https://android-review.googlesource.com/#/q/Icf314b204381a9b155bb5014c4966c7f804bea23))
- `ObservableStateStore` has been renamed to `StateStore`. ([Ieb0e2](https://android-review.googlesource.com/#/q/Ieb0e23bb8e5a09ad260eac5ebe2579407b4f8c14))
- Added `DynamicTypeEvaluator.Builder` instead of constructor arguments to allow more optional arguments, including `ObservableStateStore` which now defaults to an empty store. ([I6f832](https://android-review.googlesource.com/#/q/I6f832cc86bad4e8b226d37e707a8061a5617f4cd))
- Refactored order of parameters in `DynamicTypeEvaluator`. ([Ic1ba4](https://android-review.googlesource.com/#/q/Ic1ba4a23722fdde3380903090fb97db6b3cd3af1))

**Bug Fixes**

- Correctly propagate signals from platform sensor sources to downstream nodes ([I5a922](https://android-review.googlesource.com/#/q/I5a9229dc3cb9402be0c2f8d556fda1dac5772dd1))

### Version 1.0.0-alpha06

March 22, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ad9ba647b7548818fc9d4796a03a3b5510166fb3..5e7d256f82fbafb6d059ab7b18fddd87c7531553/wear/protolayout)

**New Features**

- We've added an experimental API for using heart rate and daily steps in dynamic expressions ([Ifd711](https://android-review.googlesource.com/#/q/Ifd7112dc607e90893bbb51751a9a5966e8d2402d))
- We have added support for reverse and forward delay for animations. ([Ic25f7](https://android-review.googlesource.com/#/q/Ic25f7903038f01a58242e4286a54bcf2417fa2a6))
- We've added `DynamicColor` support to Border and Background
- We've added dynamic value support to types in `DimensionBuilder`
- Layout and components from `tiles-material` are moving to `protolayout-material`

**API Changes**

- `LoadActionListener` has been added to `ProtoLayoutViewInstance`. ([If7806](https://android-review.googlesource.com/#/q/If78062e6556cf471a90f579a5f976694eb98f9db))

**Bug Fixes**

- Added `FloatNodesTest` ([Id7281](https://android-review.googlesource.com/#/q/Id7281ba16a05575fd4fb57d1198ec990e03753e8))
- Fix renderer crash when unable to load structured bitmap.

### Version 1.0.0-alpha05

March 8, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ad9ba647b7548818fc9d4796a03a3b5510166fb3/wear/protolayout)

**New Features**

- We've added an experimental "content update" animation to the `Modifiers` object. This animation will trigger whenever the element (with this modifier) or one of its children changes during a layout update. ([bd03e5d](https://android-review.googlesource.com/#/q/I2d240cc326684be0f6c725f2f3235d9ee842d994))

**API Changes**

- We've added `forwardRepeatDelayMillis` and `reverseRepeatDelayMillis` to `Repeatable`. We've also renamed `delayMillis` in `AnimationSpec` to `startDelayMillis` ([Ifb266](https://android-review.googlesource.com/#/q/Ifb266d7b8c26c7db0b2992905a207a9774b0b0db))
- `DynamicTypeEvaluator.bind` methods now accept an Executor. ([I346ab](https://android-review.googlesource.com/#/q/I346ab948e16e89d05f30bcf47bb558995aa26ea2))
- We've added the `startEvaluation` method to the `BoundDynamicType` to trigger the evaluation after the dynamic type is bound. ([I19908](https://android-review.googlesource.com/#/q/I19908be6191614c6f4beae72f576ea016688be21))

**Bug Fixes**

- The Animator object will be reused for subsequent animations of a single element. ([Ia3be9](https://android-review.googlesource.com/#/q/Ia3be95dd8a9b560d49c9164cf758e3c81d17a5d9))

### Version 1.0.0-alpha04

February 22, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..87533b4ff06971ed59028936cd9b6da988cd4522/wear/protolayout)

**New Features**

- `ObservableStateStore` now informs the listeners when a key is removed too.
- We've added renderer schema version and font scale to `DeviceParameters` (which can be used to conditionally create layouts in response to different versions and font settings).
- We've added support for animating `DynamicInt32` values ([I05485](https://android-review.googlesource.com/#/q/I05485cdc439a419a8fc5070bbc3fe48fa5fde5d5))
- We've added `OnLoad` and `OnConditionalMet` triggers. These can be used to start animations that support a trigger.
- We've added layout weight for expanded dimensions and min size for wrapped dimensions.
- We've added duration and instant dynamic types. These can be used to represent a time instant or duration in a dynamic expression.
- We've added support for `AnimatedVectorDrawable` and `SeekableAnimatedVectorDrawable` as layout resources.

**API Changes**

- Sensor data requires API 29+. ([I8099e](https://android-review.googlesource.com/#/q/I8099e5b6cfca87bd61d88e1a6fc7aaa7dd61fba6))
- We've added two `launchAction` helper methods (for launching Activities).

**Bug Fixes**

- Rename `set/getSpec` to `set/getAnimationSpec` in Tiles animation ([I3d74b](https://android-review.googlesource.com/#/q/I3d74b3bc82d99aec6775c83ee9e92789443f9439))

### Version 1.0.0-alpha03

February 8, 2023

`androidx.wear.protolayout:protolayout-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..7d3ac1ab1206c01fae3ebb500b5b942636070155/wear/protolayout)

**New Features**

- We have added `toByteArray()` and `fromByteArray()` to Dynamic types in protolayout-express library.
- We have added `toString()` to Dynamic types in protolayout-expression library.
- We have added evaluation support for Dynamic types. The `DynamicTypeEvaluator` class from the protolayout-expression-pipeline library can be used to evaluate (and receive updated values) for a previously create Dynamic type (`DynamicString`, `DynamicFloat`, ...)
- When animations can't be played (either because they are disabled by the evaluator, or the number of running animations has reached the set limit), the static values set on the animatable node will be used to replace the animation.

### Version 1.0.0-alpha02

January 25, 2023

`androidx.wear.protolayout:protolayout:1.0.0-alpha02`, `androidx.wear.protolayout:protolayout-expression:1.0.0-alpha02`, and `androidx.wear.protolayout:protolayout-proto:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/wear/protolayout)

**New Features**

- Layout builders from `androidx.wear.tiles:tiles` are moving to `androidx.wear.protolayout:protolayout`. The ones in `androidx.wear.tiles:tiles` will be deprecated in one of the next alpha releases.

### Version 1.0.0-alpha01

January 11, 2023

`androidx.wear.protolayout:protolayout-expression:1.0.0-alpha01` and `androidx.wear.protolayout:protolayout-proto:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b/wear/protolayout)

**New Features**

- This release introduces a new library "ProtoLayout Expression" for creating expressions from dynamic variables.