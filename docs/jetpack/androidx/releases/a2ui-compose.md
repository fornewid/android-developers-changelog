---
title: https://developer.android.com/jetpack/androidx/releases/a2ui-compose
url: https://developer.android.com/jetpack/androidx/releases/a2ui-compose
source: md.txt
---

# A2UI Compose

The Jetpack Compose Agent-to-UI (A2UI) renderer provides an implementation of the [A2UI protocol](https://a2ui.org/), enabling AI agents to generate rich, interactive user interfaces that render native Compose components---without executing arbitrary code.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| September 23, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/a2ui_compose#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on A2UI Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.a2ui.compose:compose-runtime:1.0.0-alpha01"
    implementation "androidx.a2ui.compose:compose-ui:1.0.0-alpha01"
    androidTestImplementation "androidx.a2ui.compose:compose-ui-testing:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.a2ui.compose:compose-runtime:1.0.0-alpha01")
    implementation("androidx.a2ui.compose:compose-ui:1.0.0-alpha01")
    androidTestImplementation("androidx.a2ui.compose:compose-ui-testing:1.0.0-alpha01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2097774+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2097774&template=2355003)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha01

September 23, 2026

`androidx.a2ui.compose:compose-runtime:1.0.0-alpha01`, `androidx.a2ui.compose:compose-ui:1.0.0-alpha01`, and `androidx.a2ui.compose:compose-ui-testing:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b1263fbaa920727652ed50caea8ba2ebafa5fe02/a2ui/compose).

**New Features**

The Jetpack Compose Agent-to-UI (A2UI) renderer provides an implementation of the [A2UI protocol](https://a2ui.org/), enabling AI agents to generate rich, interactive user interfaces that render native Compose components---without executing arbitrary code. This library maps the A2UI protocol messages to Compose primitives while providing fine-grained reactivity based on the Compose Snapshot state system. The library also provides APIs for creating custom components and catalogs.

**API Changes**

- Updated `A2uiBasicCatalogV1.CatalogId` from `.../v0_9_1/...` to `.../v0_9/...` to align with the canonical A2UI protocol specification. ([Idcc20](https://android-review.googlesource.com/#/q/Idcc200a889013467320122c875f5fd5fd44de290))
- Update the order of components in `A2uiBasicCatalogV` to exactly match the basic catalog specification. ([I23093](https://android-review.googlesource.com/#/q/I230939bd796e442c60e4a9ca5b5965878916f802), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `ChecksProperty` to all relevant component interfaces under `A2uiBasicCatalogV1` and made the property value available via a parameter passed to `TypedContent` of each component. ([I9f393](https://android-review.googlesource.com/#/q/I9f39367d32484b6a5b728562acd3dbe7edfb7ccd), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.ChoicePicker` and `MaterialA2uiBasicCatalogV1Defaults.choicePicker`. ([I875a6](https://android-review.googlesource.com/#/q/I875a6aea544fe4efd44cd8b8d010b081d72cc66d), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Modal` and `MaterialA2uiBasicCatalogV1Defaults.modal`. ([Icd553](https://android-review.googlesource.com/#/q/Icd553cf262a716b992a27c940d4bda2d8b4119d5), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Renamed properties in `A2uiBasicCatalogV1` to follow the pascal-case naming style. ([I91512](https://android-review.googlesource.com/#/q/I91512359e62c5276d3adf60e04cac95772d8a209), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `AccessibilityProperty` to all component interfaces under `A2uiBasicCatalogV1` and made the property value available via a parameter passed to `TypedContent` of each component. ([I76b80](https://android-review.googlesource.com/#/q/I76b8012d9e9efc3420e5345c3ea0f63019317395), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.TextField` and `MaterialA2uiBasicCatalogV1Defaults.textField`. ([Ifdaec](https://android-review.googlesource.com/#/q/Ifdaec8d793a88cb2904a32415e8dace4c488b47c), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Video` and `MaterialA2uiBasicCatalogV1Defaults.video`. ([I8595c](https://android-review.googlesource.com/#/q/I8595cade4cf6adf80020d3540588674a6a073f0e), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.AudioPlayer` and `MaterialA2uiBasicCatalogV1Defaults.audioPlayer`. ([Ida509](https://android-review.googlesource.com/#/q/Ida5091b519aa2d888cda0e49c7d46c26425cc4f3), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added support for `format` and conditional `if-then` schema keywords in `a2ui-model` and `a2ui-engine`, and updated `A2uiBasicCatalogV1.DateTimeInput` min and max property schemas. ([I556d5](https://android-review.googlesource.com/#/q/I556d546f03262b5f3a88771b827a11df59ba098f), [b/553193771](https://issuetracker.google.com/issues/553193771))
- Added `A2uiBasicCatalogV1.Slider` and `MaterialA2uiBasicCatalogV1Defaults.slider`. ([Ieb72d](https://android-review.googlesource.com/#/q/Ieb72dfb0fe03289d171f9257eb79de2f7ca996d8), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.CheckBox` and `MaterialA2uiBasicCatalogV1Defaults.checkBox`. ([I84525](https://android-review.googlesource.com/#/q/I84525d60795d5edd1e672c536e8ae593bf12b2cf), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Divider` and `MaterialA2uiBasicCatalogV1Defaults.divider`. ([I91208](https://android-review.googlesource.com/#/q/I91208bc4ac1f919f99c6b1d2c5f1016914588f57), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Tabs` and `MaterialA2uiBasicCatalogV1Defaults.tabs`. ([Ic33d3](https://android-review.googlesource.com/#/q/Ic33d317a0f1756c62f4bcff9b56ba70f8e2ace0a), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.List` and `MaterialA2uiBasicCatalogV1Defaults.list`. ([I89f73](https://android-review.googlesource.com/#/q/I89f736a2e2550dfb6070ebc051266f58f2fc3b55), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Icon` and `MaterialA2uiBasicCatalogV1Defaults.icon`. ([I65524](https://android-review.googlesource.com/#/q/I655240181d4f69497bdefc9ecd729d1ea74ad0f2), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `ProvideActionInterceptor` for intercepting actions of child components. ([I6ae69](https://android-review.googlesource.com/#/q/I6ae694a331b2aa550fbadf7aeabddc981d4fa1fc), [b/552486965](https://issuetracker.google.com/issues/552486965))
- Added support for advertising inline catalog schemas in `A2uiClientCapabilities` and `A2uiCoreCatalog`. ([I973cf](https://android-review.googlesource.com/#/q/I973cf46461377312691d5549bced426a1725a1be), [b/537714970](https://issuetracker.google.com/issues/537714970))
- Added `A2uiBasicCatalogV1.Image` and `MaterialA2uiBasicCatalogV1Defaults.image`. ([I673b3](https://android-review.googlesource.com/#/q/I673b3a7125fc503bed486e836283a7b49d3a376d), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Button` and `MaterialA2uiBasicCatalogV1Defaults.button`. ([I5215f](https://android-review.googlesource.com/#/q/I5215f800adf0c1fd42ec4f1b497fa2ab35ee764f), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Row`/`A2uiBasicCatalogV1.Column` and `MaterialA2uiBasicCatalogV1Defaults.row`/ `MaterialA2uiBasicCatalogV1Defaults.column`. ([Ibcbe7](https://android-review.googlesource.com/#/q/Ibcbe7f4266c2c9b2d101690942496c4140ca22c2), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `default` parameters to the enum, number, and boolean `A2uiProperty` types. ([Id509e](https://android-review.googlesource.com/#/q/Id509ea0050b3e3a0e075057ea56683727fe72f3d), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `A2uiBasicCatalogV1.Card` and `MaterialA2uiBasicCatalogV1Defaults.card`. ([Icf604](https://android-review.googlesource.com/#/q/Icf604e02bd57ac18730e2058dc2e77f038b6dc31), [b/547851648](https://issuetracker.google.com/issues/547851648))
- Added `isAdditionalPropertiesAllowed` and `additionalPropertiesSchema` parameters to `A2uiProperty.nested` and `A2uiProperty.nestedList`. ([I72836](https://android-review.googlesource.com/#/q/I7283655b702d654e9ee64a463e81939327cadf89), [b/547815898](https://issuetracker.google.com/issues/547815898))
- Added `minItems` and `maxItems` parameters to the list `A2uiProperty` types. ([I716d3](https://android-review.googlesource.com/#/q/I716d39da2dd792d8738e153fa733c70afae9ea6b), [b/547798330](https://issuetracker.google.com/issues/547798330))
- Added `A2uiProperty.enum`, `A2uiProperty.custom`, and `A2uiProperty.dynamicCustom` property types. ([I0647d](https://android-review.googlesource.com/#/q/I0647d44fc52e7cb17830b44c597fa28e91ff277b), [b/545522395](https://issuetracker.google.com/issues/545522395))
- Replace `A2uiCoreSurfaceModel` with `A2uiSurfaceModel` in `observeA2uiComponentState` to ensure that the public APIs in `androidx.a2ui.compose.runtime` don't expose types from `androidx.a2ui.engine`. ([Ic45e2](https://android-review.googlesource.com/#/q/Ic45e2e91a3f29f727d7ee52e70afb3e17aff79cf), [b/544705890](https://issuetracker.google.com/issues/544705890))
- Added `A2uiTestSurface` composable to mount and test A2UI surfaces and components in isolation. ([I03c8a](https://android-review.googlesource.com/#/q/I03c8ab4aae08ead8a86ddc0504e90e83c43c532c), [b/527415570](https://issuetracker.google.com/issues/527415570))
- `A2uiSchema` now support keywords within each subclass instead of dedicated subclasses for `oneOf`, `allOf`, `anyOf`, `not`, `const`, `default` and `enum`. ([I6a6f8](https://android-review.googlesource.com/#/q/I6a6f875b474a6dc8fd516c372fec70659311ca83))
- Added testing APIs for the Compose A2UI renderer. ([I59c9f](https://android-review.googlesource.com/#/q/I59c9f3756e488ee3ded63fd4bdccff9645b918ca), [b/527415570](https://issuetracker.google.com/issues/527415570))
- Added `A2uiReadinessEvaluator` and related APIs. ([Ib37d3](https://android-review.googlesource.com/#/q/Ib37d3e0e3f9097c3a7a2f4875ef90d7089578679), [b/527415547](https://issuetracker.google.com/issues/527415547), [b/524122705](https://issuetracker.google.com/issues/524122705))
- Added `A2uiComponentCollection`, `A2uiFunctionCollection`, and `A2uiCoreComponentDefinitionCollection`, and updated the catalog APIs to use the new collections. ([I96438](https://android-review.googlesource.com/#/q/I96438fba8e64135f320bed958df812445ec01ea4), [b/527415547](https://issuetracker.google.com/issues/527415547))
- Added an `A2uiMessageParser` factory function. ([I8596a](https://android-review.googlesource.com/#/q/I8596a193904d3b64666d23b5ee3974d7cf7be20d), [b/524122705](https://issuetracker.google.com/issues/524122705))
- Added the `A2uiRuntimeCatalog` marker interface, and APIs in `androidx.a2ui.compose.ui` for defining components and catalogs. ([Ibea7a](https://android-review.googlesource.com/#/q/Ibea7af8717ff058cbfce0dcb5d39acfb5ec6318f), [b/527415547](https://issuetracker.google.com/issues/527415547), [b/524122705](https://issuetracker.google.com/issues/524122705))
- Moved `androidx.compose.runtime:runtime-a2ui` to `androidx.a2ui.compose:compose-runtime`. ([Ifc7cf](https://android-review.googlesource.com/#/q/Ifc7cfd84f37b50ca0be52c5349125d787402c283), [b/524122705](https://issuetracker.google.com/issues/524122705))

**Bug Fixes**

- `androidx.lifecycle:lifecycle-runtime` dependency was updated to 2.10.0. This version is required for bundled lifecycle runtime lint checks to run with AGP version 9.5.0-alpha04 or later. ([Id18ea](https://android-review.googlesource.com/#/q/Id18ea0acdf0e152f649ce8e2435bf3d6e39d5947), [b/556807521](https://issuetracker.google.com/issues/556807521))
- `compileSdk` for Compose libraries updated to 37.1. This will require transitively updating `compileSdk` for all apps and libraries using Compose. ([I05b0f](https://android-review.googlesource.com/#/q/I05b0f9385d2b99ddcc4041b2ce2d96aea3bd391e))
- Updated default `Column` horizontal alignment to `Alignment.Start` in `A2UI Basic Catalog V1`. [Ia1c6db](https://android-review.googlesource.com/q/Ia1c6db2a2902e951bee353981ad26db57c61e251)
- Updated default `Row` vertical alignment to `Alignment.Top` in `A2UI Basic Catalog V1`. [If0bca4](https://android-review.googlesource.com/q/If0bca47da9917016a075c2537e4f82c44ddbde4e)