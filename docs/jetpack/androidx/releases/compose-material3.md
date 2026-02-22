---
title: https://developer.android.com/jetpack/androidx/releases/compose-material3
url: https://developer.android.com/jetpack/androidx/releases/compose-material3
source: md.txt
---

# Compose Material 3

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.material3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)  
(*See the API reference docs for all compose packages*) Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.4.0) | - | - | [1.5.0-alpha14](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.5.0-alpha14) |

| **Note:** To develop UIs for Wear OS apps using Material 3 Expressive, use the [Wear Compose Material 3](https://developer.android.com/jetpack/androidx/releases/wear-compose-m3) library instead of this one.

## Structure

Compose is combination of seven Maven Group IDs within `androidx`. Each Group
contains a targeted subset of functionality, each with its own set of release
notes.

This table explains the groups and links to each set of release notes.

| Group | Description |
|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | Build animations in their Jetpack Compose applications to enrich the user experience. |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | Transform @Composable functions and enable optimizations with a Kotlin compiler plugin. |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces. |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io. |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI. |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target. |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input. |

## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.material3:material3:1.4.0"
    implementation "androidx.compose.material3:material3-window-size-class:1.4.0"
    implementation "androidx.compose.material3:material3-adaptive-navigation-suite:1.5.0-alpha14"
}

android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.1.1"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.material3:material3:1.4.0")
    implementation("androidx.compose.material3:material3-window-size-class:1.4.0")
    implementation("androidx.compose.material3:material3-adaptive-navigation-suite:1.5.0-alpha14")
}

android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.1.1"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:742043+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=742043&template=1346811)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Compose Material3 Common Version 1.0

### Version 1.0.0-alpha01

April 17, 2024

`androidx.compose.material3:material3-common:1.0.0-alpha01`, `androidx.compose.material3:material3-common-android:1.0.0-alpha01`, and `androidx.compose.material3:material3-common-desktop:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943/compose/material3/material3-common).

**New Features**

Themeless components that can be used to build Material Design components:

- Tonal Palette
  - [`TonalPalette`](https://developer.android.com/reference/kotlin/androidx/compose/material3/common/package-summary#tonalpalette)
- Icon
  - [`Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/common/package-summary#icon)
- Touch target size
  - [`LocalMinimumInteractiveComponentSize`](https://developer.android.com/reference/kotlin/androidx/compose/material3/common/package-summary#localminimuminteractivecomponentSize)

## Compose Material3 Adaptive Navigation Suite Version 1.0

| **Note:** As of 1.0.0-alpha07, the `androidx.compose.material3:material3-adaptive-navigation-suite` package is released as part of the Compose Material3 package (Material3 versions 1.3.0-\*). As a result, Compose Material3 adaptive navigation suite versioning has jumped from 1.0.0-xxxx to 1.3.0-xxxx. To find the current and future navigation suite release notes and commits, see [Compose Material3 Version 1.3.0](https://developer.android.com/jetpack/androidx/releases/compose-material3#1.3.0) and later versions.

### Version 1.0.0-alpha07

May 1, 2024

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha07`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha07`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha07` are released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..fbd1ac175922f44c69a13545d194066ee428b342/compose/material3/material3-adaptive-navigation-suite).

**API Changes**

- Make navigation suite APIs non-experimental ([If62af](https://android-review.googlesource.com/#/q/If62af6676c961bd59a5a7af82f53f780aa4e73f5))

**Bug Fixes**

- Consume insets for content by default ([50266df](https://android-review.googlesource.com/#/q/50266df68eafe76b3270cedd99fc824fcd6529a3))

### Version 1.0.0-alpha06

April 17, 2024

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha06`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha06`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..67004410fdbff19f90caa4cc43965ab21dca1943/compose/material3/material3-adaptive-navigation-suite).

**API Changes**

- Add `containerColor` and `contentColor` to `NavigationSuiteScaffoldDefaults`. ([I64e3a](https://android-review.googlesource.com/#/q/I64e3a16859641091a69829c4d949bef0aaaeb445), [b/331993720](https://issuetracker.google.com/issues/331993720))
- Adding `itemColors` function to `NavigationSuiteDefaults`. ([Idf719](https://android-review.googlesource.com/#/q/Idf719f8da341e0127880023fe1c431ba30bc42a4), [b/328480012](https://issuetracker.google.com/issues/328480012))
- Make `NavigationSuiteScope` sealed. ([Iefa57](https://android-review.googlesource.com/#/q/Iefa575ae140202e21852e31a5ba0e87fa993b3d9))

### Version 1.0.0-alpha05

March 6, 2024

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha05`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha05`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/88dfe1dd1c2dab49147d5ee69f6dbd1c7d1fe1a5..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/material3/material3-adaptive-navigation-suite).

**API Changes**

- Make `NavigationSuiteItemColors` constructor public. ([Ica83a](https://android-review.googlesource.com/#/q/Ica83a426b2fbbc3804a01d0ffef654e33d5f3cee), [b/324886877](https://issuetracker.google.com/issues/324886877))

### Version 1.0.0-alpha04

February 21, 2024

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha04`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha04`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..2288333f5f81813efb4bb7b5d15563724792fc06/compose/material3/material3-adaptive-navigation-suite)

**Dependency Updates**

- Update Material3 adaptive dependencies to the new module paths. ([Ibc421](https://android-review.googlesource.com/#/q/Ibc421a02906bc5cccf2feed6e61564ef1c1f59ca))
- Migrate to use Window Manager version of window size classes. ([I3794d](https://android-review.googlesource.com/#/q/I3794dc4b7a7a225d5fe05e934a2bdb0284590b09))

### Version 1.0.0-alpha03

February 7, 2024

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha03`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha03`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6e1356c0137f362794c44812fa4f1c51dc46635f..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/material3/material3-adaptive-navigation-suite)

**API Changes**

- Update package name to navigationsuite from navigation-suite ([I7eff7](https://android-review.googlesource.com/#/q/I7eff77fcda4cd4d6c22361d922fb439ce7ba3a19))
- Material3 components exposing a `MutableInteractionSource` in their API have been updated to now expose a nullable `MutableInteractionSource` that defaults to null. There are no semantic changes here: passing null means that you do not wish to hoist the `MutableInteractionSource`, and it will be created inside the component if needed. Changing to null allows for some components to never allocate a `MutableInteractionSource`, and allows for other components to only lazily create an instance when they need to, which improves performance across these components. If you are not using the `MutableInteractionSource` you pass to these components, it is recommended that you pass null instead. It is also recommended that you make similar changes in your own components. ([I41abb](https://android-review.googlesource.com/#/q/I41abb601499b4a735b6302b96cdc1f0d066dbbdc), [b/298048146](https://issuetracker.google.com/issues/298048146))

### Version 1.0.0-alpha02

December 13, 2023

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha02`, `androidx.compose.material3:material3-adaptive-navigation-suite-android:1.0.0-alpha02`, and `androidx.compose.material3:material3-adaptive-navigation-suite-desktop:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03b3b94c9895b338f1b3eeec7c39f44cc72b9b89..6e1356c0137f362794c44812fa4f1c51dc46635f/compose/material3/material3-adaptive-navigation-suite)

**New Features**

- Add a 'None' `NavigationSuiteType` ([If8cb1](https://android-review.googlesource.com/#/q/If8cb157e6e26784fbc32ee7d3938d4e94b5930da), [b/313688598](https://issuetracker.google.com/issues/313688598))

**Bug Fixes**

- Fix navigation component filling entire screen when root surface has `modifier.fillMaxSize`. ([c9cf250](https://android-review.googlesource.com/#/q/c9cf25062fed6a75c01e6fb7bad692ad6320a6e9), [b/312664933](https://issuetracker.google.com/issues/312664933))

### Version 1.0.0-alpha01

November 15, 2023

`androidx.compose.material3:material3-adaptive-navigation-suite:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03b3b94c9895b338f1b3eeec7c39f44cc72b9b89/compose/material3/material3-adaptive-navigation-suite)

**New Features**

- [NavigationSuiteScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0))
  - [NavigationSuiteScaffoldLayout](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffoldLayout(kotlin.Function0,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,kotlin.Function0))
  - [NavigationSuite](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuite(androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,kotlin.Function1))

## Compose Material3 Adaptive Version 1.0

| **Note:** As of 1.0.0-alpha07, `androidx.compose.material3:material3-adaptive` was migrated to `androidx.compose.material3.adaptive`. For future releases, please use `androidx.compose.material3.adaptive` and the associated release notes on our [Compose Material3 Adaptive](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) page.

### Version 1.0.0-alpha06

February 7, 2024

`androidx.compose.material3:material3-adaptive:1.0.0-alpha06`, `androidx.compose.material3:material3-adaptive-android:1.0.0-alpha06`, and `androidx.compose.material3:material3-adaptive-desktop:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/material3/material3-adaptive)

**New Features**

- Added additional behavior options for `ThreePaneScaffoldNavigator` back navigation. ([I858aa](https://android-review.googlesource.com/#/q/I858aa6423627fda10a421885ebab6f3aa3145222))
- Added optional destination content to navigation history. ([Ibd7e6](https://android-review.googlesource.com/#/q/Ibd7e6650654d78e66152105d4d40c61b51945998))

### Version 1.0.0-alpha05

January 24, 2024

`androidx.compose.material3:material3-adaptive:1.0.0-alpha05`, `androidx.compose.material3:material3-adaptive-android:1.0.0-alpha05`, and `androidx.compose.material3:material3-adaptive-desktop:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a2738e2803219745cf6082a30c608d95527cd4d5..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/compose/material3/material3-adaptive)

**New Features**

- Support history-awareness in scaffold navigation and value calc ([I71d46](https://android-review.googlesource.com/#/q/I71d469ee9415a502687dfcdfca7847bcb88bc7df))

### Version 1.0.0-alpha04

January 10, 2024

`androidx.compose.material3:material3-adaptive:1.0.0-alpha04`, `androidx.compose.material3:material3-adaptive-android:1.0.0-alpha04`, and `androidx.compose.material3:material3-adaptive-desktop:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6e1356c0137f362794c44812fa4f1c51dc46635f..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/compose/material3/material3-adaptive)

**New Features**

- Added edge-to-edge support in pane scaffolds ([I1b462](https://android-review.googlesource.com/#/q/I1b462afad6fdba66ddbbeaba3113da36c983cb0b))

**API Changes**

- Moved hinge bounds properties in Posture to a list of hinge info ([I24f90](https://android-review.googlesource.com/#/q/I24f90b83c594e547afb74e6b1b1d867f19e11054))

**Bug Fixes**

- Fix `AnimatedPane` is not recomposed ([c3f573d](https://android-review.googlesource.com/#/q/I7ea91ed34b7bde2cb3f773f6fe3c6227eea9c057))

### Version 1.0.0-alpha03

December 13, 2023

`androidx.compose.material3:material3-adaptive:1.0.0-alpha03`, `androidx.compose.material3:material3-adaptive-android:1.0.0-alpha03`, and `androidx.compose.material3:material3-adaptive-desktop:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/064f85294a9be2e86650737b91db1bff868926e2..6e1356c0137f362794c44812fa4f1c51dc46635f/compose/material3/material3-adaptive)

**API Changes**

- Change scaffold roles to aliases of `ThreePaneScaffoldRole`. ([I65bd1](https://android-review.googlesource.com/#/q/I65bd1795bf03c17f229d983f87c4ce20ee9ca93a))
- Create a base class for scaffold roles ([I4784d](https://android-review.googlesource.com/#/q/I4784d97d30a1488414f5a0b40de72b82124e61eb))
- Remove unnecessary parameter from `AnimatedPane`'s content ([Ibc73b](https://android-review.googlesource.com/#/q/Ibc73b4428c62d07879064adb054716b83e1b8ce2))
- Renames `collectWindowSizeAsState` and returns raw values instead ([I480f4](https://android-review.googlesource.com/#/q/I480f4cc3371be856221bd738fb0b39383b0244fd))

### Version 1.0.0-alpha02

November 29, 2023

`androidx.compose.material3:material3-adaptive:1.0.0-alpha02`, `androidx.compose.material3:material3-adaptive-android:1.0.0-alpha02`, and `androidx.compose.material3:material3-adaptive-desktop:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03b3b94c9895b338f1b3eeec7c39f44cc72b9b89..064f85294a9be2e86650737b91db1bff868926e2/compose/material3/material3-adaptive)

**API Changes**

- Split navigation APIs from adaptive scaffold APIs. ([Ic4045](https://android-review.googlesource.com/#/q/Ic4045258ae44356dcf6d79ae72e28c5ad3b9bcbc))
- Remove `GutterSize` class. ([I785b3](https://android-review.googlesource.com/#/q/I785b38171a262c797b1a151b0f0749870f51ddf5))

**Bug Fixes**

- Fix panes are not switched when `AnimatedPane` is not used ([d88f181](https://android.googlesource.com/platform/frameworks/support/+/d88f181cb56e830a4dd5ab39b9a86d533e9d5fad))

### Version 1.0.0-alpha01

November 15, 2023

`androidx.compose.material3:material3-adaptive:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03b3b94c9895b338f1b3eeec7c39f44cc72b9b89/compose/material3/material3-adaptive)

**New Features**

Material3 adaptive condition APIs:

- [Posture](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/Posture)

Material3 adaptive pane scaffold directive APIs:

- [PaneScaffoldDirective](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/PaneScaffoldDirective)
  - [calculateStandardPaneScaffoldDirective](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#calculateStandardPaneScaffoldDirective(androidx.compose.material3.adaptive.WindowAdaptiveInfo,androidx.compose.material3.adaptive.HingePolicy))
  - [calculateDensePaneScaffoldDirective](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#calculateDensePaneScaffoldDirective(androidx.compose.material3.adaptive.WindowAdaptiveInfo,androidx.compose.material3.adaptive.HingePolicy))
  - [AdaptStrategy](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/AdaptStrategy)
  - [ThreePaneScaffoldAdaptStrategies](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/ThreePaneScaffoldAdaptStrategies)
  - [HingePolicy](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/HingePolicy)

Material3 adaptive pane scaffold APIs:

- Pane scaffold basic APIs
  - [PaneScaffoldScope](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/PaneScaffoldScope)
  - [ThreePaneScaffoldRole](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/ThreePaneScaffoldRole)
  - [PaneAdaptedValue](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/PaneAdaptedValue)
  - [ThreePaneScaffoldValue](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/ThreePaneScaffoldValue)
  - [calculateThreePaneScaffoldValue](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#calculateThreePaneScaffoldValue(kotlin.Int,androidx.compose.material3.adaptive.ThreePaneScaffoldAdaptStrategies,androidx.compose.material3.adaptive.ThreePaneScaffoldRole))
  - [AnimatedPane](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary#(androidx.compose.material3.adaptive.ThreePaneScaffoldScope).AnimatedPane(androidx.compose.ui.Modifier,kotlin.Function2))

## Compose Material3 Version 1.5

### Version 1.5.0-alpha14

February 11, 2026

`androidx.compose.material3:material3-*:1.5.0-alpha14` is released. Version 1.5.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/compose/material3).

**Workaround**

- Added `isAnchoredDraggableComponentsStrictOffsetCheckEnabled`. This flag controls whether `BottomSheetScaffold`, `ModalBottomSheet`, `SwipeToDismissBox` and `WideNavigation` rail strictly require their internal offsets to be initialized. When disabled, the components won't place their content until the offset is initialized. This flag can help temporarily work around a bug where these components throw an exception due to the offset not being initialized. ([I36870](https://android-review.googlesource.com/#/q/I368705ceaf1c74785c552f1448257acd1267907f), [b/477038695](https://issuetracker.google.com/issues/477038695), [b/478210200](https://issuetracker.google.com/issues/478210200), [b/471818801](https://issuetracker.google.com/issues/471818801), [b/475249572](https://issuetracker.google.com/issues/475249572), [b/475598146](https://issuetracker.google.com/issues/475598146))

**API Changes**

- Add `isTextButtonContentPaddingFixEnabled` that when true makes `TextButton` have correct paddings specs. ([Ib986e](https://android-review.googlesource.com/#/q/Ib986e0ffd0c55fe04a47696749f2922c0d7c856a))
- Added `indicatorPadding` param for `WideNavigationRailItem`. ([I3d5dc](https://android-review.googlesource.com/#/q/I3d5dc893a2a5112c972b9dcf13ff996d85450096))
- Add `contentPadding` and `horizontalArrangement` parameters to `SuggestionChip` and `ElevatedSuggestionChip`. Add `horizontalArrangement` and `ContentPadding` defaults to `SuggestionChipDefaults`. Create `ChipArrangement` class. ([Ida874](https://android-review.googlesource.com/#/q/Ida8740cbd48eab366fa86fbdcea966c594215499), [b/304853782](https://issuetracker.google.com/issues/304853782))
- Update the selectable menu items to contain a parameter for supporting text. Deprecate the previous APIs that didn't include the supporting text parameter. Also add the recommended default icon sizes for the leading and trailing icons. ([I89e4b](https://android-review.googlesource.com/#/q/I89e4b9622847ac95f54a10118feb434b407a8762), [b/417731599](https://issuetracker.google.com/issues/417731599))
- Updated the Snackbar layout to improve multi-line text alignment. To minimize UI disruption, the `isSnackbarStylingFixEnabled` flag has been introduced to assist with migration. Please enable this flag manually in your application, it will be removed in a future release. ([I37d63](https://android-review.googlesource.com/#/q/I37d6306d8ca13aeff670af79631a45138ea84ec2), [b/322866101](https://issuetracker.google.com/issues/322866101))
- Fixed a bug in `BottomSheetScaffold`, `ModalBottomSheet`, `SwipeToDismissBox` and `WideNavigationRail` where the anchors were not recalculated in some cases. This fix is behind a feature flag, `ComposeMaterial3Flags#isAnchoredDraggableComponentsInvalidationFixEnabled`. ([I9acb1](https://android-review.googlesource.com/#/q/I9acb1dfdcac30d07d7bed9d5032142f718103296), [b/478210200](https://issuetracker.google.com/issues/478210200))
- Add content padding param to the `WideNavigationRail` and `ModalWideNavigationRail` so that the default paddings are customizable. ([I49106](https://android-review.googlesource.com/#/q/I491062cf9abbb6aeb851918efad919c061e93320))

**Bug Fixes**

- Setting `BottomSheetScaffold sheetPeekHeight` to 0 disables `partiallyExpanded` anchor. `PartiallyExpanded` anchor is preserved in its first layout pass to allow for layout calculation. ([Ia33a4](https://android-review.googlesource.com/#/q/Ia33a48c9c625c11d25a7fd208ffa8f1c04eaa3e9), [b/465158677](https://issuetracker.google.com/issues/465158677))
- `SheetState#targetValue` prefers it's current anchor if the current offset is valid. This prevents initialValue from immediately updating. ([Ied2c4](https://android-review.googlesource.com/#/q/Ied2c47456acd9118bac9faec21017fcb35ff9441), [b/477279704](https://issuetracker.google.com/issues/477279704))
- Fix `WideNavigationRailItem`'s icon not being vertically centered if item height changes. ([Ib8c83](https://android-review.googlesource.com/#/q/Ib8c83416eee15d41b9f5d96e272b157c2302af67))

### Version 1.5.0-alpha13

January 28, 2026

`androidx.compose.material3:material3-*:1.5.0-alpha13` is released. Version 1.5.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..c26c6f088b95903b7b9cd5e6f2092988f1e64dc3/compose/material3).

**API Changes**

- Added support for search bar `animationSpecForContentExpand` and `animationSpecForContentCollapse`. ([I033a5](https://android-review.googlesource.com/#/q/I033a5fc3e829c992a5c051d74390ee2ddfe1329d))

**Bug Fixes**

- Fixed an issue where the content of an expanded `SearchBar` did not use a theme-aware color ([I878e0](https://android-review.googlesource.com/#/q/I878e0aa496b701c61de73723e4bb22f658039e6b), [b/379441904](https://issuetracker.google.com/issues/379441904))
- Fixed a bug where `BottomSheetScaffold` would invoke `SheetState`'s `confirmValueChange` callback with incorrect values when passing a drag handle to `BottomSheetScaffold`. Please note that `confirmValueChange` should only be used to veto state changes. Use a `snapshotFlow` to observe state changes. ([Ice9ee](https://android-review.googlesource.com/#/q/Ice9ee5830e802faf6c3cca96f4ac8cd8e5f7176f), [b/465824174](https://issuetracker.google.com/issues/465824174), [b/477031833](https://issuetracker.google.com/issues/477031833))

### Version 1.5.0-alpha12

January 14, 2026

`androidx.compose.material3:material3-*:1.5.0-alpha12` is released. Version 1.5.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/material3).

**API Changes**

- Updates `TopAppBarDefaults` (`enterAlways` and pinned behaviors) to support `lazyListState`, `scrollState`, and `reverseScrolling`. This fixes layout direction issues and correctly handles initially scrolled content. ([I9d5c2](https://android-review.googlesource.com/#/q/I9d5c2261d6b2881eb2c897751a1f608816ba5bcc), [b/262234750](https://issuetracker.google.com/issues/262234750))
- Add `contentPadding` and `horizontalSpacing` parameters to `AssistChip` and `ElevatedAssistChip`. Add `HorizontalSpacing` and `ContentPadding` defaults to `AssistChipDefaults`. ([I2ac90](https://android-review.googlesource.com/#/q/I2ac901717dd2cf8cde42fc438be981a72ad592a4), [b/304853782](https://issuetracker.google.com/issues/304853782))
- The `DatePicker` APIs using Java Time classes are no longer tagged as experimental. ([I5039c](https://android-review.googlesource.com/#/q/I5039cab1b1dd773f71210c439cdce00960a169f0), [b/457537971](https://issuetracker.google.com/issues/457537971))

**Bug Fixes**

- Fix a `DatePicker` date-formatting crash on API 23 ([I67a94](https://android-review.googlesource.com/#/q/I67a949f476a9d10f1e41b79461ec8702aee733f2), [b/452713222](https://issuetracker.google.com/issues/452713222))
- Fixed visual alignment bug in the fancy animated indicator sample when used with scrollable tab rows. ([Iae0f3](https://android-review.googlesource.com/#/q/Iae0f31e4d0c97d632e35313450bc0f3c2d848342), [b/466790304](https://issuetracker.google.com/issues/466790304))
- Fixed an issue where the `TimePicker`'s AM/PM selector did not use text style defined by Material Design specification. ([Ie908a](https://android-review.googlesource.com/#/q/Ie908a466f5f17525c2a5155f3c75d3a8a9b4e0ad), [b/469788786](https://issuetracker.google.com/issues/469788786))
- Fixed a crash in `HorizontalFloatingToolbar` that could occur in landscape mode when the on-screen keyboard was displayed. ([Ia13c1](https://android-review.googlesource.com/#/q/Ia13c1d8b141384110fb360423345053768249099), [b/466692323](https://issuetracker.google.com/issues/466692323))
- Fixed an issue where the `TopAppBar` title could overlap with its `actions` when no `navigationIcon` was provided. The title is now correctly constrained to its available space. ([I2ba97](https://android-review.googlesource.com/#/q/I2ba97299b87f3e4997253e88907b05b0394b253a), [b/428697836](https://issuetracker.google.com/issues/428697836))
- Support RTL with pane expansion anchors ([I0770b](https://android-review.googlesource.com/#/q/I0770bf84ce74eb1ba0534712a47689bebc7f8765), [b/467775639](https://issuetracker.google.com/issues/467775639))

### Version 1.5.0-alpha11

December 17, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha11` is released. Version 1.5.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/material3).

**New Features**

- Added `ExpandedFullScreenContainedSearchBar`. ([Ie472d](https://android-review.googlesource.com/#/q/Ie472da54accba9823347f4cb9507fbc103fa39d9),[b/454658635](https://issuetracker.google.com/issues/454658635))
- Added support to create multi-aspect carousels using lazy grids. ([I2b109](https://android-review.googlesource.com/#/q/I2b1093fea1767575e0f09669b7d4d5d5171d0661), [b/462137656](https://issuetracker.google.com/issues/462137656))
- Material expressive list items are now available, supporting interactions and segmented styling. Additional color fields have been added to `ListItemColors`. ([I54057](https://android-review.googlesource.com/#/q/I5405718266bfcc508787e22939040977a0c11d28), [b/441569230](https://issuetracker.google.com/issues/441569230))
- Multi-browse and uncontained carousel APIs are now stable. ([I7a558](https://android-review.googlesource.com/#/q/I7a558f8f00f0a70e3473f9953baff8fe043cd7d4), [b/401537465](https://issuetracker.google.com/issues/401537465))
- Add `contentPadding` and `horizontalSpacing` parameters to `FilterChip` and `ElevatedFilterChip`. Add `HorizontalSpacing` and `ContentPadding` defaults to `FilterChipDefaults`. ([Iec6e3](https://android-review.googlesource.com/#/q/Iec6e389d599c12824a40715ae10dd760fc24e9d9), [b/455596578](https://issuetracker.google.com/issues/455596578))

**Bug Fixes**

- Setting `BottomSheetScaffold sheetPeekHeight` to 0 disables `partiallyExpanded` anchor. ([I52dc9](https://android-review.googlesource.com/#/q/I52dc9547c8453c6c8d1100be7cecda30787420df), [b/465158677](https://issuetracker.google.com/issues/465158677))

### Version 1.5.0-alpha10

December 03, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha10` is released. Version 1.5.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4d752a0684fb1bf991cd0d15ebd3649ee8684ca1..deb96499dfe95073f5c1215c1287787683cb1e92/compose/material3).

**New Features**

- Added multi-aspect carousel ([I15247](https://android-review.googlesource.com/#/q/I1524749a33eb28de3c6b8afb21e0d60b37485e92), [b/411232854](https://issuetracker.google.com/issues/411232854))

**API Changes**

- Feature flag `isCheckboxStylingFixEnabled` is now provided through `ComposeMaterial3Flags` object. ([I97baf](https://android-review.googlesource.com/#/q/I97baff4d10013601d267c97104516b2c347be1e7), [b/457504316](https://issuetracker.google.com/issues/457504316))
- The `disabledCheckmarkColor` parameter in `CheckboxColors` has been moved to the end of the parameter list to ensure binary compatibility. ([I734d8](https://android-review.googlesource.com/#/q/I734d8eddd92f7e6543e66bce76450bf643b477d2), [b/457504316](https://issuetracker.google.com/issues/457504316))

**Bug Fixes**

- Revert all arrow keys changing slider values to fix focus getting trapped in certain devices without a tab key. ([I154dd](https://android-review.googlesource.com/#/q/I154dd4bebc1972f021e595e47ee1bfeee4920f24), [b/460912699](https://issuetracker.google.com/issues/460912699))

### Version 1.5.0-alpha09

November 19, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha09` is released. Version 1.5.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c907d5394acb1b40d6145046653734db55e55b8b..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/compose/material3).

**New Features**

- Adding expressive menu updates. This includes a new toggleable menu item, selectable menu item, menu groups, and menu popup. It also includes new expressive menu default values in `MenuDefaults`. ([I5cdd4](https://android-review.googlesource.com/#/q/I5cdd4602ebdbdaafe64530aa90b941b3f8f78d28), [b/417731597](https://issuetracker.google.com/issues/417731597), [b/448646125](https://issuetracker.google.com/issues/448646125), [b/448646896](https://issuetracker.google.com/issues/448646896), [b/448646891](https://issuetracker.google.com/issues/448646891))
- The `Modifier.minimumInteractiveComponentSize` now provides two new public `AlignmentLines: MinimumInteractiveTopAlignmentLine` and `MinimumInteractiveLeftAlignmentLine`. These lines mark the visual edges of a component before extra space is added to meet minimum touch target requirements. ([I7f485](https://android-review.googlesource.com/#/q/I7f485758ac96d65dda9cb5c9a3720dad938cd031), [b/458124197](https://issuetracker.google.com/issues/458124197))
- Added `ExpandedDockedSearchBarWithGap`. ([Idb7f8](https://android-review.googlesource.com/#/q/Idb7f84f427518f29f7098981453059c1e2d125cf))

**API Changes**

- Add checks to enable precision pointer component sizing. ([I8108d](https://android-review.googlesource.com/#/q/I8108d4aa8e847e4bbd534d9879cd13e32a178dae))
- Add `Modifier.align` to `ButtonGroupScope` ([I03890](https://android-review.googlesource.com/#/q/I0389016a088f07194e58088670c7b679c5f3dc6e), [b/416590906](https://issuetracker.google.com/issues/416590906))
- Remove deprecated experimental `ModalBottomSheet` APIs that have been in at least one stable release. ([Ifbe1d](https://android-review.googlesource.com/#/q/Ifbe1da0ba4e86e08461e425ea6bd72c3e958147f), [b/449757604](https://issuetracker.google.com/issues/449757604))
- New `ButtonGroup` overload with `verticalAlignment` parameter. ([I23a37](https://android-review.googlesource.com/#/q/I23a37b349bb151e6c6c4bd4a443b588c970ee6c1), [b/416590906](https://issuetracker.google.com/issues/416590906))
- Removed deprecated hidden experimental APIs that have been in at least one stable release. ([I4f68d](https://android-review.googlesource.com/#/q/I4f68d0bc899a40c729e52d16eee103c9545d73cd), [b/449754465](https://issuetracker.google.com/issues/449754465), [b/449749933](https://issuetracker.google.com/issues/449749933), [b/401311419](https://issuetracker.google.com/issues/401311419), [b/449749928](https://issuetracker.google.com/issues/449749928), [b/449756019](https://issuetracker.google.com/issues/449756019))

**Bug Fixes**

- Add tooltip to floating toolbar's default overflow button. ([Ife952](https://android-review.googlesource.com/#/q/Ife952463b108fbe81cde436742b6407a2047b1f2), [b/422781172](https://issuetracker.google.com/issues/422781172))
- Fix `WideNavigationRail`'s indicator being cut if its set to a larger width via a larger label size. ([I9d740](https://android-review.googlesource.com/#/q/I9d740694039f775f71282d64cf86b9268c550fec), [b/444728723](https://issuetracker.google.com/issues/444728723))
- Update split button trailing buttons to center the icon optically depending on the given shape even in RTL. ([Icab82](https://android-review.googlesource.com/#/q/Icab824524076ab63c857f77b19acfd3007de3697))

### Version 1.5.0-alpha08

November 05, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha08` is released. Version 1.5.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..c907d5394acb1b40d6145046653734db55e55b8b/compose/material3).

**API Changes**

- `hourInput` and `minuteInput` properties added to the `TimePickerState` interface. These properties are intended to hold the raw, unvalidated input from the user. The existing hour and minute properties remain and represent the last known valid time. ([I09d74](https://android-review.googlesource.com/#/q/I09d74e7f175ee2ab5339384e568a48e388914c66), [b/394612017](https://issuetracker.google.com/issues/394612017))

**Bug Fixes**

- A bug where Switch could not be used with `ReusableContent` without animating has been fixed. ([I61093](https://android-review.googlesource.com/#/q/I61093900125d4d045c5bcf129e3a2d420044cefe),[b/455909150](https://issuetracker.google.com/issues/455909150))

### Version 1.5.0-alpha07

October 22, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha07` is released. Version 1.5.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/compose/material3).

**API Changes**

- Enhanced `SearchBar.InputField` with a `keyboardOptions` parameter, allowing for optimized text input by specifying keyboard options and `lineLimits` parameter allowing to specify text wrapping scrolling ([Id08a4](https://android-review.googlesource.com/#/q/Id08a487cf9a79efe15c0acb50ff765e7e9f9281a), [b/416991049](https://issuetracker.google.com/issues/416991049))

**Bug Fixes**

- Fixed a bug in Slider where press interactions were not emitted on touch down. This change ensures that a `PressInteraction.Press` is emitted immediately on `awaitFirstDown`, providing instant visual feedback. ([If9e25](https://android-review.googlesource.com/#/q/If9e25e59fe9131e40414b33692dfa7cfcac529e4), [b/308501482](https://issuetracker.google.com/308501482))
- Fixed an issue with the `Tooltip` caret not changing directions when scrolling. The `TooltipBox` now triggers a recomposition whenever the tooltip popup switches sides, ensuring the caret's direction is updated correctly. ([I5ad1e](https://android-review.googlesource.com/#/q/I5ad1ebd9f53e4ef8084aadb10c685a04fb9bafe8), [b/438875827](https://issuetracker.google.com/438875827))

### Version 1.5.0-alpha06

October 08, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha06` is released. Version 1.5.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9ac371e13def566b9138a983e5dd9327a6244ae..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/material3).

**API Changes**

- Added scrolled colors for `AppBarWithSearch`. In addition, the container color of a search bar input field is now transparent by default. The default container color of the search bar itself remains unchanged. ([I4fe32](https://android-review.googlesource.com/#/q/I4fe320aa9d372ece71cc0cbad4fd263d324d83f0))
- Added a default overflow indicator composable to `FloatingToolbar`. ([I6a6f8](https://android-review.googlesource.com/#/q/I6a6f8d4e77581863516de42b87581f3c01e0381c), [b/415833723](https://issuetracker.google.com/issues/415833723))
- Update `isExpanded` to `isShowing` for menu APIs in button group. ([I86309](https://android-review.googlesource.com/#/q/I86309e968189b22d482e24a6b4d91f0275bbfeec), [b/412419514](https://issuetracker.google.com/issues/412419514))
- Updated `initialIsExpanded` to `initialIsShowing` and added a default overflow indicator composable in `ButtonGroupDefaults`. ([I6e67c](https://android-review.googlesource.com/#/q/I6e67c1d0238c065a62bb8be6d2c82f4618832a5a), [b/412419514](https://issuetracker.google.com/issues/412419514))
- Remove the drag-to-resize feature from the public API surface ([Ic85ba](https://android-review.googlesource.com/#/q/Ic85ba48ddc8f358abe1996c0d4c8a5c2b938f380), [b/437953743](https://issuetracker.google.com/issues/437953743), [b/442636084](https://issuetracker.google.com/issues/442636084))

**Bug Fixes**

- Fix focus order of keys keyboard navigation, and also fix it for RTL. ([Ibba27](https://android-review.googlesource.com/#/q/Ibba27b91409ec477b11d9b7a887697585b99f48b), [b/422220597](https://issuetracker.google.com/issues/422220597))
- Fix date picker's year selection grid keyboard navigation. ([I02363](https://android-review.googlesource.com/#/q/I02363e343f215ddf5ee4716c559739e36a64fa23), [b/422425720](https://issuetracker.google.com/issues/422425720), [b/446814683](https://issuetracker.google.com/issues/446814683))
- Fixed keyboard navigation for date selection grid in date pickers. ([I594ef](https://android-review.googlesource.com/#/q/I594efc7c3b083139e72ee92d88aeac7e803f8a29), [b/422220597](https://issuetracker.google.com/issues/422220597), [b/422223115](https://issuetracker.google.com/issues/422223115))
- Fixed offscreen toolbar receiving keyboard focus. ([I01a73](https://android-review.googlesource.com/#/q/I01a7394f2c13c285bef085b537bb87dc027cb13f), [b/422786812](https://issuetracker.google.com/issues/422786812))
- Fixed `RangeSlider` and Slider keyboard navigation. ([Ib6bcf](https://android-review.googlesource.com/#/q/Ib6bcf6d6cab3ab3f20ee4c40d02190eb2a015dd8), [b/424845268](https://issuetracker.google.com/issues/424845268), [b/422942624](https://issuetracker.google.com/issues/422942624))

### Version 1.5.0-alpha04

September 10, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha04` is released. Version 1.5.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..f9ac371e13def566b9138a983e5dd9327a6244ae/compose/material3).

**New Features**

- Added `Text` composable overloads accepting a `ColorProducer` lambda that enables efficient color changes without triggering a full recomposition. ([I9ff25](https://android-review.googlesource.com/#/q/I9ff250bbfbb5a6012ce3d9c80572fc8c96a7747e), [b/407055128](https://issuetracker.google.com/issues/407055128))

**API Changes**

- Rename `Scrim()` to `LevitatedPaneScrim()` and hide properties of Levitated and Reflowed classes. ([I090e1](https://android-review.googlesource.com/#/q/I090e1d157101c385c0fefab8d9c48b0d59599053), [b/427953101](https://issuetracker.google.com/issues/427953101))
- Hide `calculatePosture()` API as internal ([Ie7227](https://android-review.googlesource.com/#/q/Ie72276123a57e9565e2e170571cf3c3af2919672), [b/424442112](https://issuetracker.google.com/issues/424442112))
- Expose `PaneScaffoldHorizontalOrder` as a sealed public API ([Ia4ebe](https://android-review.googlesource.com/#/q/Ia4ebe8bda3df76c0470774401235559878af580d))
- Mark window size and posture related APIs as experimental. ([I4ee96](https://android-review.googlesource.com/#/q/I4ee962a4c17597fc77f378a158cd35f841378982))

**Bug Fixes**

- Fixed keyboard navigation order so that focus goes from the fab button to the first item at the top. ([Icaaa1](https://android-review.googlesource.com/#/q/Icaaa120ad129f6ba0e6ba2c4b09435996ab91d0b), [b/422762939](https://issuetracker.google.com/issues/422762939))
- Improve Navigation Drawer keyboard a11y: drawer is no longer focusable when dismissed, it can be closed via esc key, and its content receives focus when opened. ([Idb995](https://android-review.googlesource.com/#/q/Idb995d9885535c8b1a28a846bf0b9d8a38466b5c), [b/422793544](https://issuetracker.google.com/issues/422793544), [b/422793651](https://issuetracker.google.com/issues/422793651), [b/422797424](https://issuetracker.google.com/issues/422797424))
- Time picker's clock face now responds to keyboard navigation/input. ([I9d5d9](https://android-review.googlesource.com/#/q/I9d5d983f06d8cfd50945873ba718e6df22bc53d3), [b/425710631](https://issuetracker.google.com/issues/425710631))
- Use new initial anchor when pane expansion anchor list changes ([I91cd1](https://android-review.googlesource.com/#/q/I91cd1ecdcc587722214757e05c8b33a6ef70a43b), [b/438829477](https://issuetracker.google.com/issues/438829477))

### Version 1.5.0-alpha03

August 27, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha03` is released. Version 1.5.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/material3).

**Behavior Change**

- The size of the checkbox and indicator colors has been adjusted to align with the specification. To minimize UI disruption, the flag `isCheckboxStylingFixEnabled` has been added to help migration. Please enable it manually in your apps. This flag will eventually be removed in a future version. ([I5bcd3](https://android-review.googlesource.com/#/q/I5bcd3bed3448b601dfcab13c7a583dc021404220), [b/304300693](https://issuetracker.google.com/issues/304300693))

**API Changes**

- Added `contentPadding` parameter for `TopAppBar` ([Ia5fea](https://android-review.googlesource.com/#/q/Ia5feacb06bdebf8da1853cc50fa99782e8de1821))
- Add component override for nav suite scaffold ([I85312](https://android-review.googlesource.com/#/q/I8531250caec5cf86da31ac6f9e25af9c4b588ab3))

**Bug Fixes**

- The `containerColor` parameter in `TimePickerDialog` is now correctly applied, allowing customization of the dialog's background color. ([I47f89](https://android-review.googlesource.com/#/q/I47f898cc7d83f0dbbbbc6eaa14c5762d31c306cc), [b/403183883](https://issuetracker.google.com/issues/403183883))
- Modal navigation rail no longer loses focus when collapsing, and now closes in response to the ESC key. ([4255257](https://android-review.googlesource.com/#/q/42552577df09bdc798a73cdda6338f450fd04ade))
- `Snackbar` now has correct keyboard focus order for action and dismiss buttons, dismiss button also supports displaying a tooltip. ([11fa13d](https://android-review.googlesource.com/#/q/Id97abd02948e8ead083249cc9877b1a06b6a6e90))

### Version 1.5.0-alpha02

August 13, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha02` is released. Version 1.5.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/material3).

**API Changes**

- In `PullToRefreshDefaults`, renamed `shape` to `indicatorShape` and `containerColor` to `indicatorContainerColor` and added `indicatorMaxDistance` for indicator use. ([Ib6cbe](https://android-review.googlesource.com/#/q/Ib6cbea0165b6db16fddb1da795f4887a0170222f))
- Remove deprecation tag from `PullToRefreshDefaults.indicatorColor` ([Iaaee2](https://android-review.googlesource.com/#/q/Iaaee2d3579f1ac5fe1b1283d1bcecb1f48b75592))
- Added `AppBarWithSearch`, replacing `TopSearchBar` and supporting navigation/action icons. ([I213a5](https://android-review.googlesource.com/#/q/I213a50fcc776f6dde4726ac0dc4b15507d7a581c))

**Bug Fixes**

- Fix bug where backpress incorrectly updates drawer offset. ([I85624](https://android-review.googlesource.com/#/q/I85624c34198ed45fafa226d93b302227fe3a57db), [b/427778135](https://issuetracker.google.com/issues/427778135))
- `SwipeToDismissBox` now falls back to a settled `targetValue` if no other anchors exist. `BottomSheetScaffold` now falls back to an Expanded `targetValue` if no other anchors exist. ([I73d5e](https://android-review.googlesource.com/#/q/I73d5ede5fb3138d9f074bf405f04b6b5bc4788a3), [b/428856426](https://issuetracker.google.com/issues/428856426))
- Fixed button padding in `AlertDialog` when stacked vertically. ([Ia2118](https://android-review.googlesource.com/#/q/Ia211824e59881137b52bff81ad98ed848f6b899b))
- \[FAB\] Fix bug where FAB is still clickable after `Modifier.animateFloatingActionButton` hides it ([I8ea6c](https://android-review.googlesource.com/#/q/I8ea6c63477b5fdd9360ac5083ee964a238d37d1a), [b/430336834](https://issuetracker.google.com/issues/430336834))
- \[Slider\] Fixed keyboard navigation for Slider ([I3a405](https://android-review.googlesource.com/#/q/I3a405e64970f27574d702d5b28385e1b9c03bcd0))

### Version 1.5.0-alpha01

July 30, 2025

`androidx.compose.material3:material3-*:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..5fa9d0954ece0376736164b0f7bc2ef33506ab70/compose/material3).

**New Features**

- Add more position provider for tooltips so now developers can control if tooltip is placed above, below, left, or right of the anchor. Add an API that takes in a Shape for carets, so more custom shapes can be provided. ([Ie513c](https://android-review.googlesource.com/#/q/Ie513c947d881a2afc8dea1f09929dc58bacf29d5))

**API Changes**

- `TextFieldColors` methods to calculate component colors based on state are now public. ([I03165](https://android-review.googlesource.com/#/q/I03165f12203751534e4b5d119ff969012c9059fd))
- Suspend annotation has been removed from `onDismiss` callback. ([Ie3166](https://android-review.googlesource.com/#/q/Ie3166e9e4e79847c1d78eaa64dfce8e6af2fe9bd))
- `DatePickerState.getDisplayedMonth(): YearMonth?` and `DateRangePickerState.getDisplayedMonth(): YearMonth?` were updated to return non nullable value. ([Ice09c](https://android-review.googlesource.com/#/q/Ice09c319e142bdef969e4390e074a3ecc1661eb3), [b/427952972](https://issuetracker.google.com/issues/427952972))
- Remove `ModalWideNavigationRailDefaults`, move its contents to `WideNavigationRailDefaults` and rename its shape related names. ([Ic5e61](https://android-review.googlesource.com/#/q/Ic5e61ac9e32f9ae221c83993d33205917742675e))
- `WideNavigationRailItem`'s colors and copy deprecated functions should be level Hidden. ([Id7e82](https://android-review.googlesource.com/#/q/Id7e82014c42e0d6f0c3a6bdc589143e70c8483e1))
- Change level of deprecated `WideNavigationRail` apis to Warning and make them experimental. ([I89085](https://android-review.googlesource.com/#/q/I890852a7b06e5316d63d00eb08a281bf36200888))

**Bug Fixes**

- Ensures `DatePicker` respects its own locale for number formatting. Previously, if `DatePicker` was configured for an Arabic locale, it could incorrectly render Latin digits if the device's system locale used a different numbering system. ([Iccf76](https://android-review.googlesource.com/#/q/Iccf76f4da39890f51100c39771a1da15dbfb1189), [b/432616196](https://issuetracker.google.com/issues/432616196))
- Fix a `LinearProgressIndicator` issue that did not render a stop indicator correctly in RTL layouts. ([I0734c](https://android-review.googlesource.com/#/q/I0734c8928efeb4825acbb76518a96c1372d5363e))
- `PrimaryScrollableTabRow` and `SecondaryScrollableTabRow` divider now extends to the full screen size, even when tab content does not extend to the end of the screen. ([Ic1e9c](https://android-review.googlesource.com/#/q/Ic1e9c6b97f7c26ca7c3d2865e384e9e1d6527e17), [b/261741384](https://issuetracker.google.com/issues/261741384))

## Compose Material3 Version 1.4

### Version 1.4.0

September 24, 2025

`androidx.compose.material3:material3-*:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/122e65c91203d7bc66192871c72c08bd149d5777..5113b82a4ed6416d6344efa50e41db8cb65928ff/compose/material3).

**Important changes since 1.3.0:**

**Library change announcements**

The `androidx.compose.material.icons` library is **no longer recommended** for displaying Material Icons in Compose, as Material Symbols are the new way forward. We have stopped publishing updates to this library and it has been removed from the latest Material 3 library release, you can still manually reference it if you cannot migrate yet.

Instead, we recommend downloading a Vector Drawable XML file from the Android tab of https://fonts.google.com/icons to get access to the latest styled icons: Material Symbols.

Why are we not recommending the library anymore? The icons library ("Material Icons") have been superseded by the newer look of Material Symbols and we've seen that the library can increase the build time of your apps significantly as it includes all the various icons that may not be needed.

For more information: https://developer.android.com/develop/ui/compose/graphics/images/material

**Behavior Changes**

- This library no longer adds a dependency to `material-icons-core` so if your project relied on that, you will have to explicitly add that dependency in your build.gradle\[.kts\] files. ([I735ff](https://android-review.googlesource.com/#/q/I735ffb809330e77356492b3f63ad4bd5081cdd8e), [b/349894318](https://issuetracker.google.com/issues/349894318))

- `NavigationBarItem` and `NavigationRailItem`'s active label color change from `onSurface` to secondary in order to improve usability, color contrast and improve coherence within the system ([Ibc297](https://android-review.googlesource.com/q/Ibc29737146ee5534ad192db1fe7f0dfaa7a39b88)), to revert to the previous behavior, copy the default colors and change the `selectedTextColor` to `MaterialTheme.colorScheme.onSurface`.

- Material 3 components are now using the new `MotionScheme` to define their motion. ([Ie0f93](https://android-review.googlesource.com/#/q/Ie0f93b23b9623ea8f33310606359291fc6fd2b1d))

- Indeterminate circular Progress Indicator motion changes ([I3c07e](https://android-review.googlesource.com/#/q/I3c07e932ab6ef5bcf6fb44f136dcabd03cc830b9))

**New Material Design 3 Components**

- [`HorizontalCenteredHeroCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalCenteredHeroCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2))
- [`VerticalDragHandle`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#VerticalDragHandle(androidx.compose.ui.Modifier,androidx.compose.material3.DragHandleSizes,androidx.compose.material3.DragHandleColors,androidx.compose.material3.DragHandleShapes,androidx.compose.foundation.interaction.MutableInteractionSource))
- Secure text fields for password entry fields
  - [`SecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedSecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource))
  - [`OutlinedSecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedSecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource))

**Enhancements to existing Material Design 3 components**

- Text now supports `autoSize`
  - Text with [string](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.ui.text.TextStyle))
  - Text with [annotatedString](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle))
- Added Material 3 decorators for `BasicTextField2`
  - [`Textfield`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.ScrollState,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource))
  - [`OutlineTextfield`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.ScrollState,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource))
- Added an `TimePickerDialog` API that can be used for `TimePicker`, `TimeInput` or to have a switchable version.
- New search bar APIs:
  - Collapsed search bars and expanded search "views" are now separate composables:
  - `SearchBar` represents a search bar in the collapsed state.
  - `ExpandedFullScreenSearchBar` and `ExpandedDockedSearchBar` represent the search bar in the expanded state. These open in a new window.
  - [`SearchBarState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SearchBarState) to control the state of the search bar
- Promoted experimental APIs to stable!
- Performance improvements

### Version 1.4.0-rc01

September 10, 2025

`androidx.compose.material3:material3-*:1.4.0-rc01` is released. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/690cd9e6d85d0e8202c0d5eaa02b4e06a259aef8..9f79be9d3fb39a1127a51d360967d1c2e779c520/compose/material3).

### Version 1.4.0-beta03

August 27, 2025

`androidx.compose.material3:material3-*:1.4.0-beta03` is released. Version 1.4.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f82229d415d571aeea085bb20b4e9ca785c185ba..690cd9e6d85d0e8202c0d5eaa02b4e06a259aef8/compose/material3).

### Version 1.4.0-beta02

August 13, 2025

`androidx.compose.material3:material3-*:1.4.0-beta02` is released. Version 1.4.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2faad11c72811d0bdb214ceb70cf8494109b24c..f82229d415d571aeea085bb20b4e9ca785c185ba/compose/material3).

**Dependency Changes**

- Remove `graphics-shapes` dependency ([I219e0](https://android-review.googlesource.com/q/I219e0896c984379610dde86d5a87fae20273eb3c), [b/436230765](https://issuetracker.google.com/issues/436230765))

**API Changes**

- In `PullToRefreshDefaults`, renamed `shape` to `indicatorShape` and `containerColor` to `indicatorContainerColor` and added `indicatorMaxDistance` for indicator use. ([Ib6cbe](https://android-review.googlesource.com/#/q/Ib6cbea0165b6db16fddb1da795f4887a0170222f))
- Remove deprecation tag from `PullToRefreshDefaults.indicatorColor` ([Iaaee2](https://android-review.googlesource.com/#/q/Iaaee2d3579f1ac5fe1b1283d1bcecb1f48b75592))
- `BasicAlertDialogOverrideScope` was accidentally promoted to stable and had its experimental annotation removed in [aosp/3701846](https://android-review.googlesource.com/c/platform/frameworks/support/+/3701846). Marking it as internal. It will stay as public experimental in 1.5.0-alpha ([I9182a](https://android-review.googlesource.com/#/q/I9182a409be38f7674a4af4f53a24fbb85f61da44))

**Bug Fixes**

- Fix bug where backpress incorrectly updates drawer offset. ([I85624](https://android-review.googlesource.com/#/q/I85624c34198ed45fafa226d93b302227fe3a57db), [b/427778135](https://issuetracker.google.com/issues/427778135))

### Version 1.4.0-beta01

July 30, 2025

`androidx.compose.material3:material3-*:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..b2faad11c72811d0bdb214ceb70cf8494109b24c/compose/material3).

**Breaking changes**

- All public APIs tagged with `ExperimentalMaterial3ExpressiveApi` or `ExperimentalMaterial3ComponentOverrideApi` have been removed, please switch to `1.5.0-alpha` to continue enjoying these features. ([Ie4ae0](https://android-review.googlesource.com/#/q/Ie4ae0a56d36492708932ac502398e093bd52cbea))
- Please expect the following stabilized `pullToRefresh` APIs to be renamed in the next release. ([Ib6cbe](https://android-review.googlesource.com/q/Ib6cbea0165b6db16fddb1da795f4887a0170222f))

**New Features**

- `Tooltip` now supports custom caret shape and custom caret position (above, below, left, or right of the anchor). ([Ie513c](https://android-review.googlesource.com/#/q/Ie513c947d881a2afc8dea1f09929dc58bacf29d5))

**API Changes**

- Suspend annotation has been removed from `onDismiss` callback. ([Ie3166](https://android-review.googlesource.com/#/q/Ie3166e9e4e79847c1d78eaa64dfce8e6af2fe9bd))
- `DatePickerState.getDisplayedMonth(): YearMonth?` and `DateRangePickerState.getDisplayedMonth(): YearMonth?` were updated to return non nullable value. ([Ice09c](https://android-review.googlesource.com/#/q/Ice09c319e142bdef969e4390e074a3ecc1661eb3), [b/427952972](https://issuetracker.google.com/issues/427952972))
- Remove `ModalWideNavigationRailDefaults`, move its contents to `WideNavigationRailDefaults` and rename its shape related names. ([Ic5e61](https://android-review.googlesource.com/#/q/Ic5e61ac9e32f9ae221c83993d33205917742675e))

**Bug Fixes**

- Ensures `DatePicker` respects its own locale for number formatting. Previously, if `DatePicker` was configured for an Arabic locale, it could incorrectly render Latin digits if the device's system locale used a different numbering system. ([Iccf76](https://android-review.googlesource.com/#/q/Iccf76f4da39890f51100c39771a1da15dbfb1189), [b/432616196](https://issuetracker.google.com/issues/432616196))
- Fix a `LinearProgressIndicator` issue that did not render a stop indicator correctly in RTL layouts. ([I0734c](https://android-review.googlesource.com/#/q/I0734c8928efeb4825acbb76518a96c1372d5363e))
- `PrimaryScrollableTabRow` and `SecondaryScrollableTabRow` divider now extends to the full screen size, even when tab content does not extend to the end of the screen. ([Ic1e9c](https://android-review.googlesource.com/#/q/Ic1e9c6b97f7c26ca7c3d2865e384e9e1d6527e17), [b/261741384](https://issuetracker.google.com/issues/261741384))

### Version 1.4.0-alpha18

July 16, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha18` is released. Version 1.4.0-alpha18 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/compose/material3).

**New Features**

- `ModalBottomSheetProperties` now provides the option to disable dismissRequest from a scrim click. ([I8e715](https://android-review.googlesource.com/#/q/I8e7150834b8faf34f6edeff45349257118a6e8d3))
- Add `trackCornerSize` support to `RangeSlider`'s Track. ([Iec529](https://android-review.googlesource.com/#/q/Iec529a17d9bc34855bed3e71028f912f13a679f4))

**API Changes**

- Made `railExpanded` a required param for `WideNavigationRailItem`, added `modalContentColor` for `WideNavigationRailColors` and moved `WideNavigationRailDefaults.modalContainerShape` to `ModalWideNavigationRailDefaults.containerShape`. ([Id60c5](https://android-review.googlesource.com/#/q/Id60c51d3de934f9aee73ecf940b94c871cde90b8))
- Move `WideNavigationRail`'s new colors function param to be the last one, and deprecate the old function. ([Iac7f7](https://android-review.googlesource.com/#/q/Iac7f78e565416ac4d87f5212066accee577c0aca))
- `PullToRefresh` is now an stable API ([I18537](https://android-review.googlesource.com/#/q/I18537278ac7fae85fbe6c4df413f8d584dbcba39))
- Updates to the `DatePickers` API. We removed the default null end date for `DateRangePicker` and made it mandatory to pass in. We also clarified the midnight UTC usage of the date representation in the API documentation, and marked the latest getters and setters that use the java.time APIs as experimental for now. ([I121b3](https://android-review.googlesource.com/#/q/I121b3e8edc705f864210a7f25f3d46552c7ffbce), [b/427952972](https://issuetracker.google.com/issues/427952972))
- Graduate the Icon with `tint: ColorProducer` param API to non-experimental. ([Ia0133](https://android-review.googlesource.com/#/q/Ia0133c49af8c7211182a71c64cc3e2209ea76303))
- Removed the experimental annotations from `DatePicker`, `DateRangePicker`, and their supporting states, classes, and types. ([I0e4e0](https://android-review.googlesource.com/#/q/I0e4e0e1fb7ca05d21f9fc62e2411d533b4c5521b), [b/391848485](https://issuetracker.google.com/issues/391848485))
- Changed default focusable value to false to fix a11y focus, and added `hasAction` param to `TooltipBox`. ([I62998](https://android-review.googlesource.com/#/q/I629981242b5179d109908ff2b6fe7907adbf074f))
- Graduate experimental `WideNavigationRail`, `ShortNavigationBar` and `NavigationItem` APIs. ([I3ca3c](https://android-review.googlesource.com/#/q/I3ca3ccae35dcc22d532a27506473c6345b4af9f6))
- Remove the `@ExperimentalMaterial3Api` annotations from some of the top app bar functions, supporting classes, and objects. ([I0a9b7](https://android-review.googlesource.com/#/q/I0a9b731ae0f1aeb18d3180cf9ea3d8e3e32a326c))

### Version 1.4.0-alpha17

July 2, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha17` is released. Version 1.4.0-alpha17 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..1b437892629a2cdedb46d9b7232575987b2cc6b5/compose/material3).

**New Features**

- Update button group's animation to animate to 75% of the animation when clicked instead of pressed. ([593942a](https://android-review.googlesource.com/#/q/593942a2659820e583a7ebbe193bcaeaf791aa0b), [b/423596967](https://issuetracker.google.com/423596967))

**Bug Fixes**

- Fixed an issue where a carousel item could, in some cases, exceed the large element size during layout calculations, that cut the whole widget. ([I1c3d7](https://android-review.googlesource.com/#/q/I1c3d7e0f6102d8987666e5a059ba93f591ddaaa0), [b/397489534](https://issuetracker.google.com/issues/397489534))
- Fixed jumping past `beforeContentPadding` when scrolling carousels with start and end shift offsets that overlapped. ([c3d5f3a](https://android-review.googlesource.com/#/q/c3d5f3a39fce8096888709e558573b4aba467286), [b/420618979](https://issuetracker.google.com/issues/420618979))
- Update `SwipeToDismiss`' enabled behavior to observe settled state instead of current. Restores existing behavior where anchor behavior is only disabled when the component is settled at a dismissed state. ([3844e07](https://android-review.googlesource.com/#/q/3844e079efd0f392f65e2ba9368b87d6ad5c7e01), [b/425006844](https://issuetracker.google.com/issues/425006844))
- `ExposedDropdownMenu`'s popup menu can now be opened via keyboard input. Also fix the menu is now reachable via keyboard for the editable variation. ([46ead03](https://android-review.googlesource.com/#/q/46ead03680650cd163468745e6438564d8dbc83a))

### Version 1.4.0-alpha16

June 18, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha16` is released. Version 1.4.0-alpha16 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/compose/material3).

**New Features**

- Added a center aligned hero carousel component ([I6f6d3](https://android-review.googlesource.com/#/q/I6f6d394a433c4ad504953178dd9bed876d17243a))

**API Changes**

- Implement XR overrides vertical toolbar ([Ia1604](https://android-review.googlesource.com/#/q/Ia1604be7016bf8e6edab1d72a7df85f03f56b5aa))
- Added programmatic scroll functions to `CarouselState` ([I12f8e](https://android-review.googlesource.com/#/q/I12f8e446c9a7ec87e10017bf7ce87dab3c88ff42))
- Add `ComponentOverride` for `ModalWideNavigationRail` ([I4f440](https://android-review.googlesource.com/#/q/I4f4409318bef1ba08b1ee2ef58236a7780d2a2d5))
- Add `ComponentOverride` for `WideNavigationRail` ([I6354f](https://android-review.googlesource.com/#/q/I6354f5bba9a142266e7ded59d75a47fdfb51952f))
- Create `ComponentOverride` for `HorizontalFloatingToolbar` ([I51116](https://android-review.googlesource.com/#/q/I51116b1b7e6ecf2cb7f09c01f1f435f15be63844))
- Create `ComponentOverride` for `ShortNavigationBar` ([I30e24](https://android-review.googlesource.com/#/q/I30e24b3f2babba93f96c5d29262e3ae022d8913e))
- `SwipeToDismissBoxState` references to `confirmValueChange` have been marked deprecated. Users should instead leverage `SwipeToDismissBox` API `onDismissed` callback. ([Iee780](https://android-review.googlesource.com/#/q/Iee78075f58ebeec35601d0b6b8488e2acf750ab4))
- Added userScrollEnabled parameter to Carousel composables. ([I1d4d2](https://android-review.googlesource.com/#/q/I1d4d2148831bab460f14526948a21d63a3c0a169))
- Carousel's `currentItem` can now be observed from `CarouselState`. ([Ie87e9](https://android-review.googlesource.com/#/q/Ie87e963f557d21c96c6661391710d2c551baf91f))

**Bug Fixes**

- Fix an issue where an arbitrary shape on a FAB that is passed to a `FloatingToolbar` that was not applying its shadow correctly. ([Icdcc9](https://android-review.googlesource.com/#/q/Icdcc9be21d9c7951520f9a1cd1f6fe1d136f5320), [b/423336922](https://issuetracker.google.com/issues/423336922))
- All Carousels now use the Carousel semantic role by default. ([I7af12](https://android-review.googlesource.com/#/q/I7af12f562685ee22caac58cf5e62c679d9a75e2c))
- Fixed incorrect thumb movement when the slider state was updated via `LaunchedEffect` ([Id9f31](https://android-review.googlesource.com/#/q/Id9f31c57b794c941b3232fb72ba3f6e45972041d), [b/302774166](https://issuetracker.google.com/issues/302774166))

### Version 1.4.0-alpha15

May 20, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha15` is released. Version 1.4.0-alpha15 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/compose/material3).

**API Changes**

- Added `MotionTheme.LocalMotionScheme`, composition local. This allows access to the theme motion scheme from `CompositionLocalConsumerModifierNodes`, with `currentValueOf(MotionTheme.LocalMotionScheme)`. ([I014b1](https://android-review.googlesource.com/#/q/I014b19111ca39ee99fabbbd4c64e02ee2bad3240))
- `ColorScheme` constructor without Fixed color roles is now deprecated. Please migrate to constructor that includes fixed roles. ([Iad0ee](https://android-review.googlesource.com/#/q/Iad0ee3cda230dc25f3e31a0c2853200c71a53a37))
- M3 Text component now supports `TextAutoSize`. ([I7f524](https://android-review.googlesource.com/#/q/I7f52466da732f4413392203e92950598085995c0))
- Add api for constructing split button size variants and add samples. ([Ice30b](https://android-review.googlesource.com/#/q/Ice30bdc1fb4345e9de9efc92973ae2cb7067c100))

**Bug Fixes**

- Fixed an issue where `Snackbar` and `FloatingActionButton` were incorrectly positioned when edge-to-edge was enabled. Scaffold now correctly applies horizontal insets to these components. ([Ib7c30](https://android-review.googlesource.com/#/q/Ib7c305b334fa739b9201dd6d5ca66ef66db88f1b), [b/244400727](https://issuetracker.google.com/issues/244400727))
- Fix the `BottomSheet` motion from fully expanded to partially expanded. The `BottomSheet` now uses the `MotionScheme`'s fast-effect when hiding or collapsing, and default-spatial when expanding. ([Ifa46f](https://android-review.googlesource.com/#/q/Ifa46f46838ce467bc5e7d98b350adebb3bc8990b), [b/416063171](https://issuetracker.google.com/issues/416063171))
- `ColorScheme` constructor without surface container roles has been marked hidden and no longer recommended for use. ([Ia7237](https://android-review.googlesource.com/#/q/Ia7237e02d795e5173f900f224ab1c83d7e2d7309))
- Removed a `CircularWavyProgressIndicator` `Size.minDimension > 0` requirement, which used to throw an exception, to allow more flexibility. ([Ic9418](https://android-review.googlesource.com/#/q/Ic9418a95bb919e27118bf1d34e325d7e14e56d5c), [b/377531195](https://issuetracker.google.com/issues/377531195))
- Hyperlinks in `Text(AnnotatedString)` now have Material styling by default. ([I78288](https://android-review.googlesource.com/#/q/I782887c4bf08d3be9e53df8af308c5879144c37c), [b/339843816](https://issuetracker.google.com/issues/339843816))
- Fix an issue where the `toShape()` function in the `RoundedPolygon` is caching a Path and causing an issue when multiple `createOutline` calls are made with different sizes. ([I4026d](https://android-review.googlesource.com/#/q/I4026db55ff35bf1adb02b8e9e74951b312abad49))

### Version 1.4.0-alpha14

May 7, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha14` is released. Version 1.4.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/008cbd021e3a2b4d1f36ea7f48200c4692bfc169..b6c541571b9fb5471f965fc52612cb280713e5e4/compose/material3).

**API Changes**

- Added a new `AppBarColumn` composable working in the same fashion as `AppBarRow` but for content laid out in a column. ([Iaf6bd](https://android-review.googlesource.com/#/q/Iaf6bdf5ca9b86266456705b18a314afa71f5479f))
- Added max items to `AppBarRow`, this is necessary to correctly implement the material spec for top app bars. ([I92ce4](https://android-review.googlesource.com/#/q/I92ce4f973aff14999947ddc290da1e2b98780e88))
- Added a method in `TooltipScope` to obtain the `layoutCoordinates` of the anchor. Deprecating the `drawCaret` method because developers can use this new method to obtain the anchor bounds `layoutCoordinates` and create an appropriate shape that contains a caret. ([Ia2e12](https://android-review.googlesource.com/#/q/Ia2e12291cc6316ec435a07ac033273dbe7826364), [b/329470609](https://issuetracker.google.com/issues/329470609))
- Added `java.time` support for Date Pickers: Introduced `rememberDatePickerState/rememberDateRangePickerState` overloads that accept java.time objects (e.g., initial `LocalDate`, `YearMonth`). Also added extension functions on the state objects to get/set values using types like `LocalDate` and `YearMonth`. Requires API 26+ or desugaring. ([I70f29](https://android-review.googlesource.com/#/q/I70f29b86307c7186c20d4f412925a04bc8342d26), [b/266202516](https://issuetracker.google.com/issues/266202516), [b/281859606](https://issuetracker.google.com/issues/281859606))
- Add `CenteredTrack` composable allowing using a Slider with a track that starts from the center. ([I5b1d6](https://android-review.googlesource.com/#/q/I5b1d67e64cd64bfa6b2661df4803fc036e8eaa30))

**Bug Fixes**

- Enhanced the performance of Wavy Progress Indicators: Linear types now load \~8.5% faster with \~11% fewer allocations, while Circular types see a substantial \~47% speed boost and \~39% reduced allocations. ([I595d8](https://android-review.googlesource.com/#/q/I595d869e0ac95737cf0b2a48e19c4a4eba984641))

### Version 1.4.0-alpha13

April 23, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha13` is released. Version 1.4.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/74a1f5957757ddb19a2ebe9bddd8b81a6f833844..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/material3).

**API Changes**

- `isAppearanceLightStatusBars` and `isAppearanceLightNavigationBars` reintroduced to `ModalBottomSheetProperties` as android only params. ([Id4bc0](https://android-review.googlesource.com/#/q/Id4bc03e0f4b0a7c0cef3000e0d2904a4f743fd34))
- Add an `AppBarRow` composable, that handles overflow of items that would fit outside its bounds. ([I742bd](https://android-review.googlesource.com/#/q/I742bdfac6caf49e87853b993f3887813ab2e4139))
- Update the the `DatePicker` and `DateRangePicker` API for requesting a focus when switching to a date-input mode. We've replaced the `requestFocus` boolean parameter with an optional `focusRequester` param that takes a `FocusRequester`. ([I14b69](https://android-review.googlesource.com/#/q/I14b69b7502caafbe87f94e772e64150667300f99))
- Remove modifier and interaction source from the default clickable and toggleable items. Have it as an implementation detail instead. ([I95ed6](https://android-review.googlesource.com/#/q/I95ed632afc89e9feeb0d921964b1ed8cadc9fa14))
- Updated `ButtonGroup` to overflow into a dropdown menu when there are too many buttons to fit on the screen. ([I7b88b](https://android-review.googlesource.com/#/q/I7b88b25ef4e3e803a41e942241f8d78edba0723a))

**Bug Fixes**

- Bottomsheet now consumes top insets when smaller than current offset. This allows users to provide top insets for expanded behavior. `BottomSheetDefaults.windowInsets` now includes `WindowInsets.safeDrawing.Top`. ([I0ab67](https://android-review.googlesource.com/#/q/I0ab67236576ae407a3bf9f6d6a64618aa7bfb465), [b/321877275](https://issuetracker.google.com/issues/321877275), [b/336962418](https://issuetracker.google.com/issues/336962418), [b/342093067](https://issuetracker.google.com/issues/342093067))
- Enabled enter/exit animations (fade/slide) for Chip leading icons/avatars and trailing icons when they are added or removed. This primarily benefits selectable Chips (Filter, Input) but applies generally. ([I9af21](https://android-review.googlesource.com/#/q/I9af21567e5a63ed456d8e9ebb9e66150a33a8a3d))
- Fix the broken RTL Slider behavior caused by `LookaheadScope`. ([Ieb152](https://android-review.googlesource.com/#/q/Ieb1528e77d3efb971302216b31398773ee347517), [b/408118041](https://issuetracker.google.com/issues/408118041))
- Fix the Bottom `AppBar` crash related to scrolling with a hidden system UI. ([Ic6140](https://android-review.googlesource.com/#/q/Ic61400fcd39b489a716683f3db3c6f07d200253d), [b/405996228](https://issuetracker.google.com/issues/405996228))

### Version 1.4.0-alpha12

April 9, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha12` is released. Version 1.4.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a767811381d88baed6503d9aa2bd8defbd849351..74a1f5957757ddb19a2ebe9bddd8b81a6f833844/compose/material3).

**API Changes**

- Removed android specific parameters from `ModalBottomSheetProperties` ([Iab97f](https://android-review.googlesource.com/#/q/Iab97f15996145e8a999c1e3f9c16d3c056146b95), [b/362539765](https://issuetracker.google.com/issues/362539765))
- Introduce overloading functions for drag handle size defaults ([I0ed0d](https://android-review.googlesource.com/#/q/I0ed0d201a533d6e8acaa1d3128ae222fabc9eabb))
- Add new `NavigationSuiteScaffold` and `NavigationSuiteScaffoldLayout` functions to support new layout types and add support for an optional primary action content. ([Ib262a](https://android-review.googlesource.com/#/q/Ib262a707e78acfac10f440a937cfde52985485be), [b/353144478](https://issuetracker.google.com/issues/353144478))
- Deprecate `Modifier.weight` with fill parameter in `ButtonGroup`. Adding a version without fill. ([Id32bb](https://android-review.googlesource.com/#/q/Id32bb227c53ca61b19a4e90b76c381c8e0fdbfa9))
- Rename `xSmall-` and `xLarge-` IconButton component defaults to spell out `extra`. ([Ib6e0f](https://android-review.googlesource.com/#/q/Ib6e0f3fb5bcec5700764bcd936e40b982614a393))
- Add new `NavigationSuite`, `NavigationSuiteItem` and `NavigationSuiteColors` functions to support new layout types. ([I203d6](https://android-review.googlesource.com/#/q/I203d63abd13c9805abbd14e44452a25b9259ae58))
- Add new `NavigationSuiteTypes` and add new `navigationSuiteType` function that include those layout choices ([If68f9](https://android-review.googlesource.com/#/q/If68f973b0ba82a4232c387a412cdf93a8f361d8c))

**Bug Fixes**

- `ColorScheme.contentColorFor` now maps `surfaceDim` to `onSurface`. ([I8891a](https://android-review.googlesource.com/#/q/I8891af481686a8b228134fe9003f1b60414a33c4))
- Updated `DateInputTextField` implementation to address an issue where the input field did not reflect programmatically set date. ([I6c8d1](https://android-review.googlesource.com/#/q/I6c8d1488c71391474c7cbc78629f0e88723d7528), [b/401143451](https://issuetracker.google.com/issues/401143451))
- Fixed the talkback focus order for the navigation rail and wide navigation rail ([I6cf6f](https://android-review.googlesource.com/#/q/I6cf6f8911d170f3a5291c1d6aa308fadb38e7b9a), [b/407048224](https://issuetracker.google.com/issues/407048224))

### Version 1.4.0-alpha11

March 26, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha11` is released. Version 1.4.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..a767811381d88baed6503d9aa2bd8defbd849351/compose/material3).

**API Changes**

- Update capitalization for composable properties in default objects for button and toggle button. Add methods in `ToggleButtonDefaults` and `ButtonDefaults` for recommended content padding, shapes, icon size, icon spacing, and text style depending on container height. ([Iea69e](https://android-review.googlesource.com/#/q/Iea69e8bd0c9da1e6023d4bc85c45c3449a266dca))
- Removed deprecated experimental functions and constants from the `FloatingToolbar`. ([I8f339](https://android-review.googlesource.com/#/q/I8f339c6702a6084366783fbbc067a367dd2163aa))
- Elevation components now share a common interface and have public constructors and properties. ([Ibb172](https://android-review.googlesource.com/#/q/Ibb172060c7f26c0bf4f19ef48d75ae56e4c0057c))
- Adding `animateWidth` modifier in `ButtonGroupScope` that will need to be used with button group's children to correctly animate the children. ([Ia3bb6](https://android-review.googlesource.com/#/q/Ia3bb63650b255054524581f6fece6c759beff45a))

**Bug Fixes**

- Fixed Floating Toolbar padding to ensure visual balance during collapse, and improved flexibility for larger content. ([I06c00](https://android-review.googlesource.com/#/q/I06c00c626b67d7eaa98fd4969806ad7b00862b74))

### Version 1.4.0-alpha10

March 12, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha10` is released. Version 1.4.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/compose/material3).

**API Changes**

- `TabRowDefaults.tabIndicatorOffset` has been deprecated in favor of `TabIndicatorScope.tabIndicatorOffset`. ([Ib36b3](https://android-review.googlesource.com/#/q/Ib36b3508934af324279b2451d09459e0211b8642))
- Fix typo for small content padding in button defaults. ([I19bfe](https://android-review.googlesource.com/#/q/I19bfea364015de9e888441caa8a51bb15388a0d7))
- `TabRow` and `ScrollableTabRow` are deprecated in favor of Primary and Secondary variants of each. Primary and Secondary tab rows are more performant and accurate to spec. ([I918e2](https://android-review.googlesource.com/#/q/I918e2c22e4ec59c9162a730c4c1223ef735d6da0))
- Added `rememberSliderState` and `rememberRangeSliderState`. ([I8e384](https://android-review.googlesource.com/#/q/I8e384ffc4525900fa6247321bc477075f0733a00))
- Added `shouldAutoSnap` to `SliderState` to control the auto-snapping mechanism, disabling it may be useful for custom animations. ([I07745](https://android-review.googlesource.com/#/q/I07745a5d8803efc3a8257a67324b2157249e3796))
- Scrollable tab row's minimum tab width is now a parameter. Primary and Secondary tab row variants are no longer experimental. ([If6f15](https://android-review.googlesource.com/#/q/If6f15c267353bf23a8faaa486bd52ed2a61dd29b), [b/226665301](https://issuetracker.google.com/issues/226665301))
- Made the class `ExitAlwaysFloatingToolbarScrollBehavior` public allowing creation without composition. ([Ibf31c](https://android-review.googlesource.com/#/q/Ibf31cf33c3c34705783163abc7dab6b69118d9f8))

### Version 1.4.0-alpha09

February 26, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha09` is released. Version 1.4.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/12f38ed3744a6cb1592cbc6d053dc2adb328f142..fd7408b73d9aac0f18431c22580d9ab612278b1e/compose/material3).

**API Changes**

- Rename `DragHandle`'s setting fields in the default state; separate pressed and dragged states; make the default sizes be public. ([I787b9](https://android-review.googlesource.com/#/q/I787b99318e0385608e02e358ff97adb34263c0f1))
- Updates to the `TowRowsTopAppBar` API. Removed the `expanded` lambda parameter and added separate parameters for the expanded and collapsed heights. ([Idd677](https://android-review.googlesource.com/#/q/Idd6777bc381871b9e77c040762c6bca7355cda8a), [b/306697446](https://issuetracker.google.com/issues/306697446), [b/229134133](https://issuetracker.google.com/issues/229134133), [b/268068946](https://issuetracker.google.com/issues/268068946))

**Bug Fixes**

- The bottom app bars now observe the touch exploration service (e.g., `TalkBack`) and keep them visible whenever the service is on. ([I4b34d](https://android-review.googlesource.com/#/q/I4b34d33c477a95790b8a519c01d02adecb3450b6))

### Version 1.4.0-alpha08

February 12, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha08` is released. Version 1.4.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82aef93384cbb5515cac6b2380d567d813e47308..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/compose/material3).

**New Features**

- Added an `TimePickerDialog` API that can be used for `TimePicker`, `TimeInput` or to have a switchable version. ([Id2d83](https://android-review.googlesource.com/#/q/Id2d83901b116fcc17820ccefc390f6c52474b815))

- New search bar APIs:

  - Collapsed search bars and expanded search "views" are now separate composables.
  - `SearchBar` represents a search bar in the collapsed state.
  - `ExpandedFullScreenSearchBar` and `ExpandedDockedSearchBar` represent the search bar in the expanded state. These open in a new window.
  - `SearchBarState` to control the state of the search bar
  - `TopSearchBar` to add insets handling and scroll behavior
  - New overload of `InputField` which uses `SearchBarState` ([Ie0723](https://android-review.googlesource.com/#/q/Ie0723015eddd66c82f420481dc6f366a7e26f4a8), [b/261496232](https://issuetracker.google.com/issues/261496232), [b/283311462](https://issuetracker.google.com/issues/283311462), [b/350916229](https://issuetracker.google.com/issues/350916229), [b/352872248](https://issuetracker.google.com/issues/352872248))

**API Changes**

- Support corner shape morphing of icon buttons on press. ([I21843](https://android-review.googlesource.com/#/q/I21843ae412a281a77593f39274dabd7bc70a2221))
- Text field decorator/decoration box APIs are no longer experimental. ([I31d95](https://android-review.googlesource.com/#/q/I31d95194ccb98e89b91712859391b1ba0316cce2))
- Added samples and defaults for the connected variant for `ButtonGroup`. ([I5c8ce](https://android-review.googlesource.com/#/q/I5c8ce7b58c59e640139add9698740d9562eefa54))
- Make state param the last one in `NavigationSuiteScaffold` and `NavigationSuiteScaffoldLayout`. ([I9cc7b](https://android-review.googlesource.com/#/q/I9cc7ba039f0de54798d40580700a1761f778e6fa))

**Bug Fixes**

- Added custom accessibility actions to the `FloatingToolbars` so accessibility services can now expand or collapse all `FloatingToolbar` variations. The FAB-equipped version applies this to the FAB, while the FAB-less version applies it to the main content. ([I26420](https://android-review.googlesource.com/#/q/I2642077e03ca8784e6889272b816ac170d4dc61d))
- The `FloatingToolbars` now observe the touch exploration service (e.g., TalkBack) and keep the toolbar expanded and visible whenever the service is on. ([I02172](https://android-review.googlesource.com/#/q/I02172a3c568b628c3ef4070140b2bef0f317d5d3))
- Fixed a crash at the progress and loading indicators in case a `Float.NaN` is passed in as a progress. ([I4fa96](https://android-review.googlesource.com/#/q/I4fa969a1d46358a6f1db8b28cb0a375a809102c2), [b/352364576](https://issuetracker.google.com/issues/352364576))

### Version 1.4.0-alpha07

January 29, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha07` is released. Version 1.4.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..82aef93384cbb5515cac6b2380d567d813e47308/compose/material3).

**New Features**

- Added more flexibility in customizing the appearance of Checkboxes with a new API. This API provides Stroke parameters that allow for greater control over how the checkmark and the checkbox-outline are rendered. ([I65a88](https://android-review.googlesource.com/#/q/I65a88a59b14b903f0bfeec293a3a723e0e5b4ac8))
- Added `TwoRowsTopAppBar` API, a more customizable alternative to Medium and Large app bars for creating two-row top app bars. Developers now have control over the content of titles and subtitles in both collapsed and expanded states, with customizable heights for each state. ([I0be3c](https://android-review.googlesource.com/#/q/I0be3cd4f82ca3d0e74ea8b5dc0f2dcc0cea43e52), [b/306697446](https://issuetracker.google.com/issues/306697446), [b/229134133](https://issuetracker.google.com/issues/229134133), [b/268068946](https://issuetracker.google.com/issues/268068946))

**API Changes**

- Renamed an experimental `BottomAppBar` variation to `FlexibleBottomAppBar`, providing more control over content arrangement and height. ([Iaa448](https://android-review.googlesource.com/#/q/Iaa448f6f976f7514f69da961001b649069019b1a))
- Update naming for properties in Button Group default object to be `CapitalCase`. Update the name of `animateFraction` to be more precise to the behavior that it's representing. ([I545cd](https://android-review.googlesource.com/#/q/I545cd269545c88a7ff407ca4e3d35b400afbe097))
- Adding overloads for common buttons that allow for animated shapes on press interaction. Added cached button shapes. ([I5ec20](https://android-review.googlesource.com/#/q/I5ec20ca7a120c56b0c7f8dc6584b85f8b444b391))
- You can now control how a `FloatingToolbar` with FAB reacts to scrolling by providing a `FloatingToolbarScrollBehavior`. For toolbars positioned along a center edge (like top or bottom center), we recommend using a scroll behavior to hide the entire component on scroll for a cleaner look. This also prevents the FAB from becoming off-center, which could happen when using the `expanded` flag for collapsing. ([I33f67](https://android-review.googlesource.com/#/q/I33f677552d9df2cba5a8bab076945c265a4b7dd3))
- Updates the experimental `TopAppBar` APIs to use `Alignment.Horizontal` instead of a custom `TopAppBarTitleAlignment` when setting the alignment of the title and subtitle. ([I70ca2](https://android-review.googlesource.com/#/q/I70ca21eab2dd7532cd8ab7303a7fa9a5b3514825))
- `SliderState#onValueChange` is now public to give more control to the user ([I104eb](https://android-review.googlesource.com/#/q/I104eb4984db4341fefad59bac8662f0b4b918afd))
- Introduce `NavigationSuiteScaffoldState` to allow for animation of the navigation component. Also introduce overloads of `NavigationSuiteScaffold` and `NavigationSuiteScaffoldLayout` that have a state param. ([I6a8c9](https://android-review.googlesource.com/#/q/I6a8c9f505503c4c8ed9cd94912cbee7606c02b12), [b/328674235](https://issuetracker.google.com/issues/328674235))

**Bug Fixes**

- Move `IconButtonColors` and `IconToggleButtonColors` classes from `IconButtonDefaults.kt` back to `IconButton.kt`. ([I3c233](https://android-review.googlesource.com/#/q/I3c2331d18510e4ee523889621d797b93d66e0322))

**External Contribution**

- `SliderState#isDragging` is now public. ([I8458a](https://android-review.googlesource.com/#/q/I8458a21a809ebfb79778a4fe57708a54e15347cf))

### Version 1.4.0-alpha06

January 15, 2025

`androidx.compose.material3:material3-*:1.4.0-alpha06` is released. Version 1.4.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce211eef13c32d283bb64f2db117d93783070672..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/material3).

**Behavior Change**

- Added `displayCutout` to the group of insets that Material components take into account by default, to avoid content overlapping with the display cutout. This is a behavior change that will impact how inset-aware components behave around a display cutout. This includes the default value of the `WindowInsets` parameter for inset-aware Material 3 components, and the `WindowInsets` values provided in the component Defaults objects for both Material 2 and Material 3. If this change causes undesirable behavior, manually specify the `WindowInsets` parameter on a per-component basis. ([I43ee9](https://android-review.googlesource.com/#/q/I43ee9ad12db0450ebb9c65ce10d5c39d12628b6c), [b/362508045](https://issuetracker.google.com/issues/362508045))

**API Changes**

- Updates to the `TopAppBar` API. Rename the medium and large top app bars with a subtitle to `*FlexibleTopAppBar`. Unified the color variations into a single `TopAppBarDefault.topAppBarColors()` function, and added a `subtitle` color parameter to be applied for a provided subtitle Composable ([I41b65](https://android-review.googlesource.com/#/q/I41b658469205cbb138f90fe0d35a1939c92b068f))
- Remove `WideNavigationRailArrangement` API in favor of `Arrangement.Vertical` ([Id0341](https://android-review.googlesource.com/#/q/Id034135613504c56601b4101f95633c1e3089d08))
- Add a new `VerticalSlider @Composable`. ([I2bfba](https://android-review.googlesource.com/#/q/I2bfba20f1848252c3daabae8f5e944eef96af4b8))
- Add a new Track `@Composable` that allows specifying custom external track corners and track icons. ([I436a4](https://android-review.googlesource.com/#/q/I436a423b79bf88f6243fa91e02797b509996a2dc))
- Update the floating toolbar APIs to use the `FloatingToolbarColors` object instead of a single container color. ([I9a054](https://android-review.googlesource.com/#/q/I9a054e407d8f3518c289a1a09924ce871ad0b400))
- Add and use new experimental annotation `ExperimentalMaterial3ComponentOverrideApi` ([Ia1eaf](https://android-review.googlesource.com/#/q/Ia1eaf5578ad029fc94c5aee60146e6aebc36ca2a))
- `Modifier.indicatorLine` now takes a shape for the text field to handle clipping. ([I8c5f3](https://android-review.googlesource.com/#/q/I8c5f31cc77134107ae7895a273895f71ee6b2cc6), [b/380704151](https://issuetracker.google.com/issues/380704151))
- Rename the experimental `FloatingAppBar` functions to `FloatingToolbar` ([I1dbf8](https://android-review.googlesource.com/#/q/I1dbf88e729754da6848ed3ad571c6854812bdd57))
- Added a new `floatingToolbarVerticalNestedScroll` that can be attached to a scrollable container to update the floating toolbar expansion state based on a scroll motion that crosses a threshold. ([I6d65f](https://android-review.googlesource.com/#/q/I6d65f467fb88e31233dbb9a266d8aed70d5aea32))
- Introducing a new API for creating a floating toolbar with an attached Floating Action Button (FAB). The API provides flexible customization options, allowing you to arrange the toolbar horizontally or vertically and place the FAB at the start or end of the toolbar. ([I9e350](https://android-review.googlesource.com/#/q/I9e3508dd059b8f6d4c5fd220d9b756ea4829d962))

**Bug Fixes**

- Fix a Snackbar accessibility issue that caused it to announce itself on dismiss when `TalkBack` is on. ([/I9db53](https://android-review.googlesource.com/#/q/I9db535aa1aadc875b1f9712c352e0d40c6f73fc5))

**External Contribution**

- Commonized `BasicTooltip` in foundation and `BasicTooltip/Tooltip` in material3. ([Ifc2e6](https://android-review.googlesource.com/#/q/Ifc2e61bf8dac507072ec7e52a803f40422367c68))

### Version 1.4.0-alpha05

December 12, 2024

`androidx.compose.material3:material3-*:1.4.0-alpha05` is released. Version 1.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..604900a0795c06c6bc66e4db8d0aefb08bea3cc1/compose/material3).

**API Changes**

- Replace type in `WideNavigationRailState.current/target` value for an enum for better readability ([I2d6ab](https://android-review.googlesource.com/#/q/I2d6abfd48f2111270a8006acc7c26afd8376fd11))
- `SplitButton` change Shape api from data class to class for binary compatibility. ([I53812](https://android-review.googlesource.com/#/q/I5381213967af44f2fe37dafba1f1ad0b0863a637))
- Added a tooltip API that has a `onDismissRequest` parameter so makers can decide what happens when a user clicks outside of the tooltip. Deprecated the old API that doesn't contain this new parameter. ([I99aef](https://android-review.googlesource.com/#/q/I99aef78418a6bb25f499bd67fac956a2c87be72e))
- Change naming of `opticalCentering` to `horizontalCenterOptically`. Making the modifier internal. Replace padding parameter with max start and end offset. ([I0b904](https://android-review.googlesource.com/#/q/I0b904925a852f44df024911bb9204dc508aebdd4))
- Change `WideNavigationRailState` to have current/target value, remove enums in favor of boolean. ([Idfa29](https://android-review.googlesource.com/#/q/Idfa29aad7efd1d0e943bf175f5bcb1fc347fdf0e), [b/356039090](https://issuetracker.google.com/issues/356039090))
- Add `NavigationBarItemComponentOverride`. ([I3a06a](https://android-review.googlesource.com/#/q/I3a06a587c543d6a7aac7ced35adeb189c2c0deb6))

**Bug Fixes**

- Fix the top and bottom app-bar behaviors to reliably change color when content is scrolled all the way. ([Idc4e8](https://android-review.googlesource.com/#/q/Idc4e834695cbd7cb8099f7b63cf21d5b764f1c81), [b/293665988](https://issuetracker.google.com/issues/293665988))
- Scroll behavior functions for top and bottom app bars now return a remembered behavior to perform better across recompositions. ([I0fdbe](https://android-review.googlesource.com/#/q/I0fdbe6e2ffb01d97b4c57d3a41a76f8531a2d72a), [b/207957336](https://issuetracker.google.com/issues/207957336))
- Modifier pararemeter is now applied after internal modifiers such as dragging behavior and semantics, instead of before. This affects the ordering in which modifiers are applied. ([I8d83f](https://android-review.googlesource.com/#/q/I8d83fd447173da5cd76aa6e03ca2d0b4921c7a59))
- Expanded bottom sheet remains expanded on size change. ([I2870b](https://android-review.googlesource.com/#/q/I2870ba38420d18b02676e6f280ef96dddc6a3a8a), [b/324934884](https://issuetracker.google.com/issues/324934884))
- Correctly route status and navigation bar flags for windows properties. ([Ie674d](https://android-review.googlesource.com/#/q/Ie674d4f080aafa8a41aeb3732797916169a07198), [b/362539765](https://issuetracker.google.com/issues/362539765))
- Move modifier parameter to the scaffolds root, as documented. This aligns implementation with M2. ([I0235e](https://android-review.googlesource.com/#/q/I0235ea935c42700a5e0aa5205d0d8a7bc8ffe88e), [b/372311595](https://issuetracker.google.com/issues/372311595))

**External Contribution**

- Commonized `DatePickerDialog` function. ([I7dced](https://android-review.googlesource.com/#/q/I7dceda6b682e488b82c0e64d2310fb9e38f1b8cd))

### Version 1.4.0-alpha04

November 13, 2024

`androidx.compose.material3:material3-*:1.4.0-alpha04` is released. Version 1.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/material3).

**Behavior Changes**

- Revert color changes introduced in [aosp/3212478](https://r.android.com/3212478) to `iconButtonColors`, `iconToggleButtonColors`, `outlinedIconButtonColors`, `outlinedIconToggleButtonColors` and `outlinedIconToggleButtonBorder`. Moved the now-reverted behavior into a new set of functions called `iconButtonVibrantColors` and so forth to emphasize the high contrast colors being returned. ([Iffd8d](https://android-review.googlesource.com/#/q/Iffd8db14ef78fd4b4f25008be8fac97f6144bc89))

**New Features**

- Introduce `VerticalDragHandle` component ([I6c770](https://android-review.googlesource.com/#/q/I6c7701b190d72b3655c5fcad1393497936472e80))

**API Changes**

- Rename `DismissibleModalWideNavigationRailDefaults` to `ModalWideNavigationRailDefaults`. ([I8e877](https://android-review.googlesource.com/#/q/I8e8775fca9c78f66e7621168e1552fc66ddc73a9))
- Add `NavigationBarComponentOverrides`. ([I8a3f3](https://android-review.googlesource.com/#/q/I8a3f37783f45b0c0ef72ee45439b1738eaf03e20))
- Add `NavigationRailComponentOverride`. ([I83e13](https://android-review.googlesource.com/#/q/I83e13c5643d792a173220f086cbe3899b468eb27))
- Introduce `WideNavigationRailState` to handle collapsing/expanding of the rail, allow `ModalWideNavigationRail` to be dismissible and delete `DismissibleModalWideNavigationRail`. ([I88568](https://android-review.googlesource.com/#/q/I8856843a858432a670f46a0897ffb691a4edc82a))
- Add xSmall, medium, large, and xLarge size defaults into toggle button defaults. ([Ie95d1](https://android-review.googlesource.com/#/q/Ie95d1b6e2c56c51aa6d8d8ad66564f79e6e1acb0))
- Add xSmall, medium, large, and xLarge size defaults into button defaults. ([If8b6d](https://android-review.googlesource.com/#/q/If8b6dd8a50b010dc3a3b7045a9dacea859489669))

**Bug Fixes**

- Filter chip trailing icon color has been updated from Primary to `OnSurfaceContainer`, per spec. All chip outline colors have been updated from Outline to Outline Variant, per spec. ([I68bd4](https://android-review.googlesource.com/#/q/I68bd4ca71c7ed6a01ee7046d3d89f617d62a4e90))

### Version 1.4.0-alpha03

October 30, 2024

`androidx.compose.material3:material3-*:1.4.0-alpha03` is released. Version 1.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/955f3c40a6dc8e5772c53a0edaa2f36f94d43bb0..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/material3).

**API Changes**

- `SheetState` constructor with density has been deprecated in favor of positional and velocity thresholds. ([Ifd16e](https://android-review.googlesource.com/#/q/Ifd16e81baddd9cd4d45fbef54e69145ad52ab1c6))
- Added `rememberTooltipPositionProvider` that contains an updated positioning logic. Deprecated `rememberPlainTooltipPositionProvider` and `rememberRichTooltipPositionProvider`. ([Ie66e2](https://android-review.googlesource.com/#/q/Ie66e2ec58567cc38fc06bb8e13ef928160db114a))
- Additional `ModalBottomSheetProperties` allow for customization of status and navigation bar colors. By default, these update based on content color instead of system dark theme status. ([Ib874e](https://android-review.googlesource.com/#/q/Ib874e2b06477ef077534e5af31c1c7be97a4e134), [b/362539765](https://issuetracker.google.com/issues/362539765))
- Improved the input experience for date pickers: when in input mode, the date text field will be focused for immediate text entry. The change adds a `requestFocus` parameter to the `DatePicker` and the `DateRangePicker`. You may prevent a focus by passing `false`. ([I12d09](https://android-review.googlesource.com/#/q/I12d09f5f8d432ea57281466c3a6565987426404a), [b/286399710](https://issuetracker.google.com/issues/286399710), [b/340102743](https://issuetracker.google.com/issues/340102743))
- Caching the shape defaults into the Shape object. Making the shape defaults `@Composable` for toggle button. Collapsing the shapes into one shape default since the variants point to the same token file. ([Iaa014](https://android-review.googlesource.com/#/q/Iaa0145dd90586e6f8508c4310c89bbf12f3d0313))

**Bug Fixes**

- Optimize Scaffold `contentPadding` behavior to avoid always recomposing the body content when the `contentPadding` changes. ([I8c8e2](https://android-review.googlesource.com/#/q/I8c8e226666d916662d5f5c22d4b02ca9ad0d6f97), [b/373904168](https://issuetracker.google.com/issues/373904168))
- `TextFieldLabelScope` `progress` renamed to `labelMinimizedProgress`
- `TextFieldLabelPosition` `Default` renamed to `Attached`. Interface members have been removed. ([If75c6](https://android-review.googlesource.com/#/q/If75c6603cace4c5942842b47d33544d893177672))
- Fixed an issue with the `DatePicker` in input mode where validation errors could cause the component's height to change. ([I2e229](https://android-review.googlesource.com/#/q/I2e229559964acd9522e8a696bb0e89698c20bdd9), [b/280462363](https://issuetracker.google.com/issues/280462363))
- Make the material Slider change its value when control keys are pressed. ([I1c442](https://android-review.googlesource.com/#/q/I1c442dee1c87e48a2d34c0277d36a9a5d3e14a5b))

### Version 1.4.0-alpha02

October 16, 2024

`androidx.compose.material3:material3-*:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fea5a8a99788fe9368f7be39aab0d1bbee389feb..b8a68b0896897fa158508d73a31998a26161d9a7/compose/material3).

**API Changes**

- Updates to the date pickers to ensure consistent Locale usage throughout the `DatePicker` and `DateRangePicker` when setting a Locale directly through a `DatePickerState` or a `DateRangePickerState`. Note that when setting Locales directly to the state, it's up to you to ensure that the title and headline texts are localized accordingly, as their default text will still be applied according to the default platform Locale. ([I37073](https://android-review.googlesource.com/#/q/I370735477b6adae8628fb967b6aa6c6138216883), [b/326490763](https://issuetracker.google.com/issues/326490763), [b/321657276](https://issuetracker.google.com/issues/321657276))
- `SheetState.isAnimationRunning` is now exposed. ([I9a3d7](https://android-review.googlesource.com/#/q/I9a3d7fd89aef2731c794a8a0ee379debb6a6d77d))
- `DatePickerColors` now correctly take precedence over any conflicting colors defined at the theme's Typography text styles. Also note that this update adjusts the `color` parameter's position in the date picker functions and introduces a `contentColor` parameter for customizing the header and title text colors. ([I30d03](https://android-review.googlesource.com/#/q/I30d0307b11ba2e1a02535928ab4e4131100692a8), [b/347031394](https://issuetracker.google.com/issues/347031394))
- Rename `SplitButton` to `SplitButtonLayout` and remove `SplitButton` color variants APIs, variants will be achieve by re-using button variants provided by `SplitButtonDefaults`. ([I44c36](https://android-review.googlesource.com/#/q/I44c36b66afc26ffd4a1b7d20c33b409ada12e0f8))
- `ModalBottomSheet` now has `sheetGestureEnabled` parameter ([I856cb](https://android-review.googlesource.com/#/q/I856cbb6b8907ce773d47589f2c83a828a5740eb8), [b/288211587](https://issuetracker.google.com/issues/288211587))
- Renamed the `standardMotionScheme` and the `expressiveMotionScheme` to standard and expressive. Both functions are now accessible through the `MotionScheme` companion object by calling `MotionScheme.standard()` and `MotionScheme.expressive()`. ([Iceccf](https://android-review.googlesource.com/#/q/Iceccf241c8a9b729d3d7eb97432c2e2abedec332))
- Adding `maxWidth` parameter to plain and rich tooltips. It defaults to the design spec of 200 dp for plain tooltips and 320 dp for rich tooltips. ([I30ce9](https://android-review.googlesource.com/#/q/I30ce99fa9a23048859335aa781ac7b67dc92042d))

**Bug Fixes**

- The `DatePicker` and `DateRangePicker` now correctly update the displayed month when set via their state's `displayedMonthMillis`. ([If9e47](https://android-review.googlesource.com/#/q/If9e47133cb89ea689612133e10a31bfa20f45fd6), [b/333414302](https://issuetracker.google.com/issues/333414302))
- `ModalBottomSheet` content now moves content away from status bar. ([I5114c](https://android-review.googlesource.com/#/q/I5114c66808d155f5db97908520bad2efd93be08e), [b/321877275](https://issuetracker.google.com/issues/321877275), [b/336962418](https://issuetracker.google.com/issues/336962418), [b/342093067](https://issuetracker.google.com/issues/342093067))
- \[Bottom Sheet\] Change back callback priority to `PRIORITY_DEFAULT` to allow IME keyboard to dismiss first. ([I447fb](https://android-review.googlesource.com/#/q/I447fba3df4f9178532cccf2832abd87d106f1c64))
- Fix crashes in the `DatePicker` and `DateRangePicker` when the minimum selectable year is set to a future year. ([I78656](https://android-review.googlesource.com/#/q/I78656c7fcf507532603e08f4bb4ef34bdba99f87), [b/319395747](https://issuetracker.google.com/issues/319395747))
- Fix a date-picker issue to update the UI when an updated `SelectableDates` instance is applied. ([Iad59a](https://android-review.googlesource.com/#/q/Iad59a46ee1c6484c2dc2409c9cc135070aa94bc2), [b/290135807](https://issuetracker.google.com/issues/290135807), [b/339898760](https://issuetracker.google.com/issues/339898760))

### Version 1.4.0-alpha01

October 2, 2024

`androidx.compose.material3:material3-*:1.4.0-alpha01` is released. Version 1.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fea5a8a99788fe9368f7be39aab0d1bbee389feb/compose/material3).

**Behavior Changes**

- Library no longer adds a dependency to `material-icons-core` so if your project relied on that, you will have to explicitly add that dependency in your `build.gradle[.kts]` files. ([I735ff](https://android-review.googlesource.com/#/q/I735ffb809330e77356492b3f63ad4bd5081cdd8e), [b/349894318](https://issuetracker.google.com/issues/349894318))
- `NavigationBarItem` and `NavigationRailItem`'s active label color change from `onSurface` to `secondary` in order to improve usability, color contrast and improve coherence within the system ([Ibc297](https://android-review.googlesource.com/q/Ibc29737146ee5534ad192db1fe7f0dfaa7a39b88)), to revert to the previous behavior, copy the default colors and change the `selectedTextColor` to `MaterialTheme.colorScheme.onSurface`.
- Material 3 components are now using the new `MotionScheme` to define their motion. ([Ie0f93](https://android-review.googlesource.com/#/q/Ie0f93b23b9623ea8f33310606359291fc6fd2b1d))
- Indeterminate circular Progress Indicator motion changes ([I3c07e](https://android-review.googlesource.com/#/q/I3c07e932ab6ef5bcf6fb44f136dcabd03cc830b9))
- Update `OutlinedIconButtonColors` and `OutlinedIconToggleButtonColors` for better color contrast. ([I2743d](https://android-review.googlesource.com/q/I2743dfdb345ae11350bf2539f12b9f40c58ef45f))
- Updated container and content color for `FilledIconToggleButtonColors` and `FilledTonalIconToggleButtonColors`. ([Ic5d0f](https://android-review.googlesource.com/q/Ic5d0fafa3514169fd8233bd94a9bbb6b4b47deeb))
- Updated `OutlinedButton` border color from `outline` to `outlineVariant`. ([057f00](https://android-review.googlesource.com/q/I1f562c325dcad2156f73a38da69619ae49057f00))

**API Changes**

- Added an optional `reverseLayout` parameter to the `TopAppBar`'s `enterAlwaysScrollBehavior` function to better support content that was set with a `reverseLayout`. ([I4e0e5](https://android-review.googlesource.com/#/q/I4e0e597d1c7f417832dd200432a64422d7775d5b))
- `SegmentedButton` now supports `contentPadding` argument. ([I5ad91](https://android-review.googlesource.com/#/q/I5ad917641162a5c21a1309087510e93a5c7c6b0b), [b/358414376](https://issuetracker.google.com/issues/358414376))
- `PullToRefreshState` does no longer have default implementation for `isAnimating` ([I6a593](https://android-review.googlesource.com/#/q/I6a593e67f5823a14880d3c8fc68f294779148d05))
- Added new overloads of Material `TextField` and `OutlinedTextField` that use `TextFieldState`. Added decoration box APIs that are compatible with `TextFieldDecorator`. ([If13a1](https://android-review.googlesource.com/#/q/If13a1360d6122af7eca19598a8c8eeb94b617f42))
- Added parameter to control text field's `labelPosition`. Using `alwaysMinimize` allows the UI pattern of displaying a label and placeholder in a text field at the same time even when the field is unfocused. ([I1ef2c](https://android-review.googlesource.com/#/q/I1ef2c9de19a3ac129840e6f1f3457261b5b4de5c))
- Added Material `SecureTextField` and `OutlinedSecureTextField` for password entry fields. ([I7e22d](https://android-review.googlesource.com/q/I7e22dded59654584e6911f8a4c87a6f436cf9739))
- Added a scope to text field labels to query animation progress. ([If5ec8](https://android-review.googlesource.com/q/If5ec804b801fe388d3f87cbf5291ddd34f018de1))
- Adds support for `MotionEvent.CLASSIFICATION_DEEP_PRESS` to tooltips. ([I62e6a](https://android-review.googlesource.com/q/I62e6a314ef30fdc6913ca179cc038433f7faf04d))
- `TimePickerState`'s `isAfternoon` is now an extension val instead of a var in the interface, renamed to `isPm` ([I89a97](https://android-review.googlesource.com/q/I89a97ad00240aa50e39ded989b8ae6533b63800e))
- Updating typography class to support emphasized type scales. ([Ifa13c](https://android-review.googlesource.com/q/Ifa13ca828b6e10ea50a4059b1aa0e0f609759037))
- Added `ModalWideNavigationRail` API and renamed `ModalExpandedNavigationRail` APIs to `DismissibleModalWideNavigationRail`. ([Ic9118](https://android-review.googlesource.com/#/q/Ic91182a291d352e6977e82188bae15b2fee0d6bb))
- Updated `FloatingAppBarScrollBehavior` to auto-calculate the `screenOffset` and not require a `@Composable`. ([Idf349](https://android-review.googlesource.com/#/q/Idf34988717c62c75424246eae311736bee061847))
- Updates to the `LoadingIndicator` API to fix the naming at its defaults object. Added a `LoadingIndicatorElevation` constant at the `PullToRefresh`. ([I1d72b](https://android-review.googlesource.com/#/q/I1d72b770c2561e52b1f4a94138f508e094c11cfe))
- Updates to the `LoadingIndicator` API to fix the naming at its defaults object. Added a `LoadingIndicatorElevation` constant at the `PullToRefresh`. ([I1d72b](https://android-review.googlesource.com/#/q/I1d72b770c2561e52b1f4a94138f508e094c11cfe))
- Added an `amplitude` and a `waveSpeed` parameters to the indeterminate variations of the `LinearWavyProgressIndicator` and the `CircularWavyProgressIndicator`. ([I2a0c5](https://android-review.googlesource.com/#/q/I2a0c51939c47aa8697444fbcff55b98dc8744d14))
- Support changing an icon toggle button's shape based on its pressed or checked state. ([Ibc781](https://android-review.googlesource.com/#/q/Ibc781e9c82f22f36a7991fb342ac61e26b72b44d))
- Updating typography class to support emphasized type scales. ([Ifa13c](https://android-review.googlesource.com/#/q/Ifa13ca828b6e10ea50a4059b1aa0e0f609759037))
- `SplitButton` shape morphs based on default / pressed state. Removed `AnimatedTrailingButton` api because `TrailingButton` api can offer the same customizations ([I95066](https://android-review.googlesource.com/#/q/I95066488f2244072cf1928bc1d06b9bb5796af9b))
- Add modifier to animate showing and hiding of FAB, e.g. when content scrolls. ([I8338d](https://android-review.googlesource.com/#/q/I8338dc6a8b9457d241642bae88352723ac7bb605))
- Adding connected button group shapes and spacing to `ButtonGroupDefaults` to be used in a sample. ([I68e30](https://android-review.googlesource.com/#/q/I68e307005e9d2a441ef99950a8f0c799c01f3726))
- Split button add horizontal padding for trailing button and enable optical centering calculated from start and end corner differences ([I122e2](https://android-review.googlesource.com/#/q/I122e287fb52270e93032d29c9ee0d3da2469ae8b))
- Introducing a new Material `MotionScheme` to allow setting a scheme for the component's motion. The scheme is set through the `MaterialTheme`. ([Id50c2](https://android-review.googlesource.com/#/q/Id50c27c7dea488e88511c0e2c3ad5a67a673b038))

**Bug Fixes**

- Apply the correct focus traversal index to `Scaffold` child Composables. The order is `topBar`, `bottomBar`, fab, content, snackbar. ([I5936b](https://android-review.googlesource.com/#/q/I5936be7f2f78a87a9423cff988a42c6288392603))
- Fixed an issue at the `DatePicker` and `DateRangePicker` where in certain locales and format-skeletons some of the date elements (e.g. month names) did not start with a capital letter. ([I1430f](https://android-review.googlesource.com/#/q/I1430f55bc95fb8e90da51057340c5004c72c4bea))
- Integrate FAB and FAB Menu component tokens (minor visual updates to paddings and text) ([Ib57f3](https://android-review.googlesource.com/#/q/Ib57f3f24c92774a0692758e0a46cedeebf291800))
- `ModalBottomSheet` is now first in semantic traversal order, followed by the scrim. ([I436f9](https://android-review.googlesource.com/#/q/I436f9692595a637e75592a02304b3e2ca3a7a158), [b/358594665](https://issuetracker.google.com/issues/358594665))
- Fix bottom app bar not disappearing entirely when scrolling under the navigation pill in edge to edge mode ([I3ee21](https://android-review.googlesource.com/q/I3ee211d7d56465391aca50f9a694fefccb47a8e5))

## Compose Material3 Version 1.3

### Version 1.3.2

April 9, 2025

`androidx.compose.material3:material3-*:1.3.2` is released. Version 1.3.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/065f8f4c9800a64e5344e69e1a0aef65fa981370..a8c757d3d74ce0f52c23b8562468fbcc09a7e62f/compose/material3).

**Bug Fixes**

- `ListItem` corrects its intrinsic height calculation, now reserving the appropriate amount of space in Layout.
- Remove excess `NavigationBarItem` label padding, correctly aligning with spec.
- Corrects `TabRow` Layout in RTL mode.

### Version 1.3.1

October 30, 2024

`androidx.compose.material3:material3-*:1.3.1` is released. Version 1.3.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/122e65c91203d7bc66192871c72c08bd149d5777..065f8f4c9800a64e5344e69e1a0aef65fa981370/compose/material3).

**Bug Fixes**

- The `DatePicker` and `DateRangePicker` now correctly update the displayed month when set via their state's `displayedMonthMillis`. ([If9e47](https://android-review.googlesource.com/#/q/If9e47133cb89ea689612133e10a31bfa20f45fd6), [b/333414302](https://issuetracker.google.com/issues/333414302))
- Fix crashes in the `DatePicker` and `DateRangePicker` when the minimum selectable year is set to a future year. ([I78656](https://android-review.googlesource.com/#/q/I78656c7fcf507532603e08f4bb4ef34bdba99f87), [b/319395747](https://issuetracker.google.com/issues/319395747))
- Fix a date-picker issue to update the UI when an updated `SelectableDates` instance is applied. ([Iad59a](https://android-review.googlesource.com/#/q/Iad59a46ee1c6484c2dc2409c9cc135070aa94bc2), [b/290135807](https://issuetracker.google.com/issues/290135807), [b/339898760](https://issuetracker.google.com/issues/339898760))
- Change back callback priority used by bottom sheets to `PRIORITY_DEFAULT` to allow IME keyboard to dismiss first. ([I447fb](https://android-review.googlesource.com/#/q/I447fba3df4f9178532cccf2832abd87d106f1c64))

### Version 1.3.0

September 4, 2024

`androidx.compose.material3:material3-*:1.3.0` is released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/677dcf61d60ab5702e37deefb378de88774d0f8e..122e65c91203d7bc66192871c72c08bd149d5777/compose/material3).

**Important changes since 1.2.0**

Major features of 1.3.0

New Material Design 3 components

- [Carousel](https://m3.material.io/components/carousel/overview)
  - [`HorizontalMultiBrowseCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalMultiBrowseCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) and [`HorizontalUncontainedCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalUncontainedCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) Enhancements to existing Material Design 3 components.
- \[`ModalBottomSheet`\] now supports Predictive Back on U+ ([Iccf32](https://android-review.googlesource.com/#/q/Iccf324cb6dfc7f4ea1fe413b69e035658282360d), [b/281967264](https://issuetracker.google.com/issues/281967264), [b/304850357](https://issuetracker.google.com/issues/304850357))
- \[`SearchBar`\] now supports Predictive Back on U+ ([I657f8](https://android-review.googlesource.com/#/q/I657f8859433717fe5e4058bcd7a74649adece529))
- Nav Drawer (`ModalDrawerSheet` and `DismissibleDrawerSheet`) now supports Predictive Back on U+ as opt-in ([Ie5b0b](https://android-review.googlesource.com/#/q/Ie5b0b1662087258f4573372df4ff600eb1a5a025))
- `DropdownMenu` now supports custom color, shape, elevation, and border. ([I8e981](https://android-review.googlesource.com/#/q/I8e9818a88b1aca1f16370c668ae60d19b0c5a89d),[b/289554448](https://issuetracker.google.com/issues/289554448), [b/301887035](https://issuetracker.google.com/issues/301887035), [b/283654243](https://issuetracker.google.com/issues/283654243))
- Updated Slider to improve accessibility by adding a gap and stop indicator. ([I3058e](https://android-review.googlesource.com/#/q/I3058e77cfa7017a781f70e498889ab11330990af))
- Updated `ProgressIndicator` to improve accessibility by adding a gap and stop indicator. ([I21451](https://android-review.googlesource.com/#/q/I2145171a393ef661a91799f4e1d39bdd69))
- Added a default caret for rich tooltip, support custom caret to be drawn given anchor `LayoutCoordinates`. ([Ifd42c](https://android-review.googlesource.com/#/q/Ifd42c2be34f72060cccce6414e28c1b2c01e025a)) Breaking Changes
- New pull-to-refresh APIs:
  - Simplified `PullToRefreshState` to use fractional values instead of Dp units.
  - `isRefreshing` state is controlled by the user instead of `PullToRefreshState`.
  - Separated out the nested scroll connection from `PullToRefreshState`. It is handled by the new `PullToRefreshBox` or `Modifier.pullToRefresh`.
  - This update is a breaking change to previous experimental APIs. ([I0adeb](https://android-review.googlesource.com/#/q/I0adeb950063988d1a05aca7aa135ccd982431423), [b/314496282](https://issuetracker.google.com/issues/314496282), [b/317177684](https://issuetracker.google.com/issues/317177684), [b/323787138](https://issuetracker.google.com/issues/323787138), [b/324573502](https://issuetracker.google.com/issues/324573502), [b/317177683](https://issuetracker.google.com/issues/317177683)) Visual Breaking Changes
- Update focus state overlay to be 0.1f to ensure sufficient color contrast. ([I7ea77](https://android-review.googlesource.com/#/q/I7ea77012950bc900bc868cce2c2322ab86474508))
- Small adjustments to surface and background color defaults in `lightColorScheme` and `darkColorScheme`. ([I9db52](https://android-review.googlesource.com/#/q/I9db5226e26371223bc46f37ddfe226acf7767041))
- Updated Slider and `ProgressIndicator` colors to follow the new Non-Text Contrast specs. ([I26807](https://android-review.googlesource.com/#/q/I26807868d150434976e911f0812d3a009aa612ec))
- `SurfaceContainer` variants are now used by components. Components which formally calculated color with `Surface` and `TonalElevation` now use `SurfaceContainer` roles by default, which are not affected by tonal elevation. ([b/304584161](https://issuetracker.google.com/issues/304584161))
- Surface and Surface container baseline roles have been slightly adjusted, providing more tint in light and dark themes. ([I677a5](https://android-review.googlesource.com/#/q/I677a5570757aee5d90e3518bf379a63e3d5fba0d))
- Promoted experimental APIs to stable!
- Performance improvements

### Version 1.3.0-rc01

August 21, 2024

`androidx.compose.material3:material3-*:1.3.0-rc01` is released. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/37922ee451c7e281c262f8570e84cba4efcaec47..677dcf61d60ab5702e37deefb378de88774d0f8e/compose/material3).

**Bug Fixes**

- `ModalBottomSheet` is now first in semantic traversal order, followed by the scrim. ([I436f9](https://android-review.googlesource.com/#/q/I436f9692595a637e75592a02304b3e2ca3a7a158), [b/358594665](https://issuetracker.google.com/issues/358594665))

### Version 1.3.0-beta05

July 24, 2024

`androidx.compose.material3:material3-*:1.3.0-beta05` is released. Version 1.3.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd4111597651ae0fbd21781f47d06fb3a214bbd6..37922ee451c7e281c262f8570e84cba4efcaec47/compose/material3).

- Fixed issue where `BottomSheet` content is missing or cut off on Android N and O ([a10a2d](https://android-review.googlesource.com/q/I0462448c8ad157e2a676cbeb46a2b56c3da10a2d))
- Increased slider's semantics bounds in order for `TalkBack` to properly show the focus indicators around the thumbs. ([0b5a1d](https://android-review.googlesource.com/q/I2b780abefd12f89b9586063eaaa633b2290b5a1d))

### Version 1.3.0-beta04

June 26, 2024

`androidx.compose.material3:material3-*:1.3.0-beta04` is released. Version 1.3.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..cd4111597651ae0fbd21781f47d06fb3a214bbd6/compose/material3).

### Version 1.3.0-beta03

June 12, 2024

`androidx.compose.material3:material3-*:1.3.0-beta03` is released. Version 1.3.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..f5541f29d045c6ba9734689ec67891f8d667412b/compose/material3).

**External Contribution**

- Make `androidx.compose.material3.DropdownMenu` available from common source set. ([If62c0](https://android-review.googlesource.com/#/q/If62c08a313c09acf91de71950c9405e3e5968f89))

### Version 1.3.0-beta02

May 29, 2024

`androidx.compose.material3:material3-*:1.3.0-beta02` is released. Version 1.3.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/compose/material3).

**API Changes**

- `Modifier.pullToRefreshIndicator` supports elevation, update Pull To Refresh APIs to have enabled be a boolean, instead of a lambda. Support content alignment in `PullToRefreshBox` ([I75679](https://android-review.googlesource.com/#/q/I75679e45af151b0ad1741f8c4513ee25fb20b225))
- Making `TooltipScope` a sealed interface and creating an internal implementation to use in `TooltipBox` and Label. ([I3833e](https://android-review.googlesource.com/#/q/I3833ea874e67e9c835bbbdf397caf54df8771122))
- Added two new modifiers to `CarouselItemScope` - `maskClip` and `maskBorder` - to easily add a shape and border to any carousel item ([Id67a1](https://android-review.googlesource.com/#/q/Id67a1e2ac1e9a3cc1a6654f20c0fc5ea95fc9ed4))
- `TimePickerState` is now an interface and allows for setting the time ([I88546](https://android-review.googlesource.com/#/q/I88546d3967a854fb64099eddbbf9ee3bc52490cb))
- Updated API for styling the links: moved the `TextLinkStyles` to the `TextStyle` and removed the `TextDefaults` from material. ([I5477b](https://android-review.googlesource.com/#/q/I5477bdb498b6b4f33ab3bc998e2be59d8a4ff7e4))

**Bug Fixes**

- `ModalBottomSheet` status and nav bar icons now respond to dark theme status. ([Ie1fe7](https://android-review.googlesource.com/#/q/Ie1fe7e1f792c39d52b4d419a08209c2577bf1175), [b/338342149](https://issuetracker.google.com/issues/338342149))
- Added close sheet semantics to `ModalBottomSheet` scrim. ([0e61cb](https://android-review.googlesource.com/c/platform/frameworks/support/+/3085729),[b/328801864](https://issuetracker.google.com/issue?id=328801864&query=328801864))

**External Contribution**

- Make `androidx.compose.material3.AlertDialog` available from common source set ([Ia33f5](https://android-review.googlesource.com/#/q/Ia33f513f472f6d200de922fdef0fd2f73f62b007))
- Make `ModalBottomSheet` available from common source set ([Id7cc7](https://android-review.googlesource.com/#/q/Id7cc733003fc7c2cdceb95a30b6d7183d39fdffc))

### Version 1.3.0-beta01

May 14, 2024

`androidx.compose.material3:material3-*:1.3.0-beta01` is released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/material3).

**API Changes**

- Using `DpSize` instead of `CaretProperties`. Removing `CaretProperties`. Rename `CaretScope` to `TooltipScope`. ([Id9a76](https://android-review.googlesource.com/#/q/Id9a76372b428a4114009250e322f8ee3315e3a7d))
- Updated the API for getting Material themed links in text. Specifically, removed the methods from the `TextDefaults` for constructing themed `LinkAnnotations` and parse HTML with themed links. Instead, added a `TextLinkStyles` class that allows to style the links as a parameter to the Text composable. ([I31b93](https://android-review.googlesource.com/#/q/I31b93f4460f4a0a50c7a86996a499d359ba455c8))

### Version 1.3.0-alpha06

May 1, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha06` is released. Version 1.3.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..fbd1ac175922f44c69a13545d194066ee428b342/compose/material3).

**Breaking Changes**

- New pull-to-refresh APIs:

  - Simplified `PullToRefreshState` to use fractional values instead of Dp units.
  - `isRefreshing` state is controlled by the user instead of `PullToRefreshState`.
  - Separated out the nested scroll connection from `PullToRefreshState`. It is handled by the new `PullToRefreshBox` or `Modifier.pullToRefresh`.
  - This update is a breaking change to previous experimental APIs. ([I0adeb](https://android-review.googlesource.com/#/q/I0adeb950063988d1a05aca7aa135ccd982431423), [b/314496282](https://issuetracker.google.com/issues/314496282), [b/317177684](https://issuetracker.google.com/issues/317177684), [b/323787138](https://issuetracker.google.com/issues/323787138), [b/324573502](https://issuetracker.google.com/issues/324573502), [b/317177683](https://issuetracker.google.com/issues/317177683))

**API Changes**

- `RippleConfiguration#isEnabled` has been removed, and `LocalRippleConfiguration` has been made nullable. To disable a ripple, instead of providing a `RippleConfiguration` with `isEnabled = false`, provide `null` to `LocalRippleConfiguration`. ([I22725](https://android-review.googlesource.com/#/q/I22725ce120f27f7dd0041bfabff5f3faff614ea9))
- `ModalBottomSheet` more accurately draws scrim over status bar when edge to edge is enabled. Modal bottom sheet content can now consume window insets, allowing for visible content above the navigation bar. `ModalBottomSheet` parameter `windowInsets` renamed to `contentWindowInsets` to specify where the insets will be applied, these are no longer tied to window logic. `contentWindowInsets` type has been changed to a function which returns `WindowInsets`, to allow it to be resolved within its new window. ([I39630](https://android-review.googlesource.com/#/q/I39630f2d9a1b159ef27fa62750ffa26b00e078a0), [b/274872542](https://issuetracker.google.com/issues/274872542), [b/300280229](https://issuetracker.google.com/issues/300280229), [b/290893168](https://issuetracker.google.com/issues/290893168))
- `PrimaryScrollableTabRow` and `SecondaryScrollableTabRow` now use custom layout instead of subcomposition, which should improve performance. ([I991e0](https://android-review.googlesource.com/#/q/I991e05b5b44b3c8bf0cd0e80c4ab5fd0d580ba46))
- Text links got pressed state styling option in addition to normal styling, hovered and focused. `TextDefaults` methods each got a `pressedStyle` argument to support that. ([Ic473f](https://android-review.googlesource.com/#/q/Ic473f81fd32d95ad84d6bc452c8dcbf6de7ba4ba), [b/139312671](https://issuetracker.google.com/issues/139312671))

**Bug Fixes**

- Navigation drawer drag anchors now match the `drawerContent`'s width. ([Ibc72f](https://android-review.googlesource.com/#/q/Ibc72f1f09657bbf2162f1ad609553dd7cc9f34ef), [b/245355396](https://issuetracker.google.com/issues/245355396))
- `OutlinedTextField` top padding for label now accounts for system font size. ([Idc781](https://android-review.googlesource.com/#/q/Idc78176ca566364b041b5863aa477ada660d05a9))
- Fixed package location of `CalendarLocale`. ([Ifa235](https://android-review.googlesource.com/#/q/Ifa235f8e3562e2cba9a0a3a90a48e76930cc9fd0))
- \[Predictive Back\] Update predictive back animations to use interpolation curve of (0.1, 0.1, 0, 1) ([I2591a](https://android-review.googlesource.com/#/q/I2591a653d70f25e4da39b39bc92bb1ac94735d31))

### Version 1.3.0-alpha05

April 17, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/material3).

**New Features**

- `SearchBar` and `DockedSearchBar` have new overloads that take a text field parameter. This allows styling the text field separately from the rest of the search bar as well as passing in custom text fields. The text field of the current implementation has been made available as `SearchBarDefaults.InputField`. ([I50c73](https://android-review.googlesource.com/#/q/I50c73509b4a67247df7240207e7ad13d5863a7ff), [b/275074248](https://issuetracker.google.com/issues/275074248), [b/278773336](https://issuetracker.google.com/issues/278773336), [b/326627700](https://issuetracker.google.com/issues/326627700))
- the lambda `drawTick` has been added to the public API in order to customize the ticks if needed ([I0c048](https://android-review.googlesource.com/#/q/I0c048c627d7c5a3a0dfde4b7743cdb6a2802aee9))

**API Changes**

- Text links got pressed state styling option in addition to normal styling, hovered and focused ([I5f864](https://android-review.googlesource.com/#/q/I5f864b3fd1b1af6ff39dee03e1aa65ede7e16d32), [b/139312671](https://issuetracker.google.com/issues/139312671))
- Updated `CarouselItemInfo` to expose a mask Rect that the item is being clipped by ([I785d8](https://android-review.googlesource.com/#/q/I785d821b4d008bd649243c034a4df92077823667))
- Removed `BasicTooltipState` from the Material 3 public API. Its functionality is combined with `TooltipState` until Foundation's `BasicTooltip` is stabilized. ([Icda29](https://android-review.googlesource.com/#/q/Icda29a4fd0ddd1fb4a7362464916a58ae88ef859))
- Added a `TextDefaults` object that contains methods to construct a `LinkAnnotation` and parse HTML-tagged string which apply `MaterialTheme` to the links ([I98532](https://android-review.googlesource.com/#/q/I98532f3512d1930416f66dd195746eeeba884497), [b/139312671](https://issuetracker.google.com/issues/139312671))
- `ExposedDropdownMenuBoxScope` no longer permits subclasses. Exposed dropdown menus now have a `MenuAnchorType` which should be passed to `menuAnchor` to support better a11y. This should be used instead of passing `focusable` to `ExposedDropdownMenu`, which is now deprecated. `menuAnchor` has a new parameter to control `enabled` state. ([I55ee6](https://android-review.googlesource.com/#/q/I55ee632daf66ef4df90297350cbff901e26ea446), [b/257209915](https://issuetracker.google.com/issues/257209915), [b/308840226](https://issuetracker.google.com/issues/308840226))
- Fixed the border color of `OutlinedButton` when disabled. Added `ButtonDefaults.outlinedButtonBorder("enabled")` overload that takes the enabled state. ([Ie650b](https://android-review.googlesource.com/#/q/Ie650bd6f38d9802f4040c0f1c90688d66446019b), [b/318461363](https://issuetracker.google.com/issues/318461363))
- Added a new `CarouselItemInfo` class to help clients get information about the item sizes. ([I9070c](https://android-review.googlesource.com/#/q/I9070c8284c49315b5a6d676cc235974bcf7a70c8))
- `ColorScheme` constructor without surface containers is now deprecated. Please migrate to the constructor that includes surface containers. ([I35c11](https://android-review.googlesource.com/#/q/I35c11d8e95b77a5b9c44e5103ccedc55196f65f0))
- \[Outlined\]`TextFieldDefaults` `ContainerBox` renamed to `Container`. ([Ie8d3b](https://android-review.googlesource.com/#/q/Ie8d3bef9cfd4b2b8e1a355e6f167ee98e0605c16))

**Bug Fixes**

- `BottomSheetScaffold` will no longer scroll from nested scroll if `sheetSwipeEnabled` is false. ([I5e1c1](https://android-review.googlesource.com/#/q/I5e1c1adb83167184f2baa4457cf1b3c70272a72c), [b/306464779](https://issuetracker.google.com/issues/306464779))
- Removed some `ExperimentalMaterial3Api` OptIn annotation in `IconButtonSamples.kt`. ([I111d1](https://android-review.googlesource.com/#/q/I111d1cd1939c1788d5e216d7c09d691bd3bc9473))

### Version 1.3.0-alpha04

April 3, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/material3).

**New Features**

- Added two experimental versions of the [Material3 Carousel](https://m3.material.io/components/carousel/overview) - `HorizontalMultiBrowseCarousel` and `HorizontalUncontainedCarousel` ([I88d64](https://android-review.googlesource.com/#/q/I88d64ec4f07b00ce744813886aee22f00aa58ab3))
- Updated Compose M3 Nav Drawer (`ModalDrawerSheet` and `DismissibleDrawerSheet`) to support Predictive Back on U+ as opt-in ([Ie5b0b](https://android-review.googlesource.com/#/q/Ie5b0b1662087258f4573372df4ff600eb1a5a025))
- Added a new API in Icon to allow passing color tint as lambda to avoid recomposing. ([I5b5a2](https://android-review.googlesource.com/#/q/I5b5a2a18f400315ec2fcb6220e4103fb45e48406))
- Top app bar APIs now support custom heights for both fixed and collapsible sections. ([Ib8b0c](https://android-review.googlesource.com/#/q/Ib8b0ce45ed461e7d5110e1473a90ab48c268caa6), [b/323403446](https://issuetracker.google.com/issues/323403446))

**API Changes**

- Top app bar APIs now support custom heights for both fixed and collapsible sections. Fixed an issue that caused single-line top app bars to recompose too many times when scrolling content. Resolved an issue where `MediumTopAppBar` truncated titles on devices with large font/display settings. ([Ib8b0c](https://android-review.googlesource.com/#/q/Ib8b0ce45ed461e7d5110e1473a90ab48c268caa6), [b/323403446](https://issuetracker.google.com/issues/323403446), [b/300953236](https://issuetracker.google.com/issues/300953236), [b/286296147](https://issuetracker.google.com/issues/286296147), [b/330410290](https://issuetracker.google.com/issues/330410290), [b/308540676](https://issuetracker.google.com/issues/308540676))
- `SegmentedButton` and associated APIs are now stable ([I8a158](https://android-review.googlesource.com/#/q/I8a158168edd209070b43efc93d4ce343b9cf34fe))
- `SwipeToDismissBox`, `SwipeToDismissBoxDefaults`, `SwipeToDismissBoxState` and `SwipeToDismissBoxValue` are now marked stable. ([I5f000](https://android-review.googlesource.com/#/q/I5f000aae3526aa9570feb09b5310124f9568e953))
- Removed deprecated `DismissDirection` and `DismissValue` enums and APIs. ([I89ccd](https://android-review.googlesource.com/#/q/I89ccd7ced015310756da041a3712455cb0dd7202))
- Added an experimental tag to Carousel's `CarouselState` companion object. ([I94154](https://android-review.googlesource.com/#/q/I94154527c26e286eef436f80c87bdd02e4a285e0))
- Deprecate `LocalMinimumInteractiveComponentEnforcement` and introduced `LocalMinimumInteractiveComponentSize` to replace it. ([I7a7ac](https://android-review.googlesource.com/#/q/I7a7ac4e5e03e7e03a759ac894ad1a7e5575a9136))
- `SearchBarColors` constructor is now public. ([I769ca](https://android-review.googlesource.com/#/q/I769caa93b90ab7ee82c24e6b23d1a6d08a5b3d8b))
- Added a `gesturesEnabled` parameter to `SwipeToDismissBox`. ([Idc59f](https://android-review.googlesource.com/#/q/Idc59f4bc393c36d58022b459056074b1e9986b37), [b/324170119](https://issuetracker.google.com/issues/324170119))
- Removed text field APIs that were marked as deprecated and experimental. ([I1305f](https://android-review.googlesource.com/#/q/I1305f9b42a718eecb7b5702c46edc5cc0e5e4e22))

### Version 1.3.0-alpha03

March 20, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/material3).

**Visual Breaking Changes**

- Update focus state overlay to be 0.1f to ensure sufficient color contrast. ([I7ea77](https://android-review.googlesource.com/#/q/I7ea77012950bc900bc868cce2c2322ab86474508))
- Small adjustments to surface and background color defaults in `lightColorScheme` and `darkColorScheme`. ([I9db52](https://android-review.googlesource.com/#/q/I9db5226e26371223bc46f37ddfe226acf7767041))

**New Features**

- Added parameters to customize `ExposedDropdownMenu`. In particular, menus now have a `focusable` parameter (default `true`) that should be set to `false` when working with editable text fields. ([I4184c](https://android-review.googlesource.com/#/q/I4184c21ee9f6ac3a5dcffceb1014b3e4b26eccb9), [b/323694447](https://issuetracker.google.com/issues/323694447), [b/278609042](https://issuetracker.google.com/issues/278609042))

**API Changes**

- The `ScaffoldSubcomposeInMeasureFix` flag has been removed. ([Ie2a4b](https://android-review.googlesource.com/#/q/Ie2a4b40e050d12a0c136a54f3e0da6d37bb4582c))
- `NavigationRailItemColors` is now marked as `@Immutable`. ([If6112](https://android-review.googlesource.com/#/q/If6112d3f7fb20f381917a5ac4c148cf5bdb073f9), [b/327660613](https://issuetracker.google.com/issues/327660613))
- `NavigationBarItemColors` is now marked as `@Immutable`. ([I42a30](https://android-review.googlesource.com/#/q/I42a30ae37fe4bf69c85151cee825873e7b3d42b0), [b/298064514](https://issuetracker.google.com/issues/298064514))
- Reorder params in Slider Track composable. ([I9f315](https://android-review.googlesource.com/#/q/I9f315c41cba97f1d9997d93708475a04e42ec984))
- `ExposedDropdownMenu` is now implemented using `Popup`. The behavior should be the same except focusable menus with editable text fields may be dismissed when typing on the keyboard.

**Bug Fixes**

- Surface and Surface container baseline roles have been slightly adjusted, providing more tint in light and dark themes. ([I677a5](https://android-review.googlesource.com/#/q/I677a5570757aee5d90e3518bf379a63e3d5fba0d))
- Updated Slider and `ProgressIndicator` colors to follow the new Non-Text Contrast specs. ([I26807](https://android-review.googlesource.com/#/q/I26807868d150434976e911f0812d3a009aa612ec))
- Update focus state overlay to be 0.1f to ensure sufficient color contrast. ([I7ea77](https://android-review.googlesource.com/#/q/I7ea77012950bc900bc868cce2c2322ab86474508))
- Small adjustments to surface and background color defaults in `lightColorScheme` and `darkColorScheme`. ([I9db52](https://android-review.googlesource.com/#/q/I9db5226e26371223bc46f37ddfe226acf7767041))

### Version 1.3.0-alpha02

March 6, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/material3).

**API Changes**

- Making the slider states stable again. Making `State.onValueChangeFinished` a val again. Wrapping `onValueChangeFinished` in a `rememberUpdatedState`. ([I82ab2](https://android-review.googlesource.com/#/q/I82ab29f469b01077eb17a70204f43b7a154abc1d), [b/322269951](https://issuetracker.google.com/issues/322269951))
- The Navigation components now use the new `SurfaceContainer` roles. `DrawerDefaults` now provides distinct `standardContainerColor` and `modalContainerColor` attributes. `DrawerDefaults.ModalDrawerElevation` is now `0.dp`. ([I7fbac](https://android-review.googlesource.com/#/q/I7fbacfbf3b79a4077bae2b84973d6db7e1d94f2f))
- Removing `@Stable` from the states of `Slider` since we're changing `state.onValueChangeFinished` to a `var`. ([Ied34a](https://android-review.googlesource.com/#/q/Ied34a92fed040ceeb5d676d6f75767ee33762cfb), [b/322269951](https://issuetracker.google.com/issues/322269951))
- `ModalBottomSheet` and `StandardBottomSheet` animation spec is now a `TweenSpec`, updated from a spring animation. This resolves an issue with a visible overshoot. Deprecated `SheetState` constructors without density have now been removed. ([I7babc](https://android-review.googlesource.com/#/q/I7babc194825f4cf6c05f9724eeba14d556c0840c), [b/285847707](https://issuetracker.google.com/issues/285847707))

**Bug Fixes**

- `SurfaceContainer` variants are now used by components. Components which formally calculated color with Surface and `TonalElevation` now use `SurfaceContainer` roles by default, which are not affected by tonal elevation. ([b/304584161](https://issuetracker.google.com/issues/304584161))
- Fixed bug that caused `ElevatedFilterChip`'s unselected, disabled container color to be black. ([I400e6](https://android-review.googlesource.com/#/q/I400e69a7f00c00c3c77e3fdef1e947156483731b), [b/322407043](https://issuetracker.google.com/issues/322407043))
- Fix indeterminate progress indicator when the progress is 0 ([Id6582](https://android-review.googlesource.com/#/q/Id658289077d4189ce18d7fc1e7cb167cc1068043))
- Fixed an issue with `Slider` and `RangeSlider` on RTL layout ([Iab0e1](https://android-review.googlesource.com/#/q/Iab0e100af81859c5baaaa43ef3119113eee748ce))
- Adding `SliderRangeTolerance` for the slider range calculation since Float rounding can be inaccurate. ([Ic918a](https://android-review.googlesource.com/#/q/Ic918adc77cd76bd1e988e0b3e7aa92c54cf19ade), [b/324934900](https://issuetracker.google.com/issues/324934900))
- Ensure that the `DatePickerDialog` displays its buttons when nesting a `DateRangePicker` or when displaying any type of date picker on small screens with larger fonts. ([Ie4758](https://android-review.googlesource.com/#/q/Ie4758e82b94eb2d5e448a973c550302ff1601f3f), [b/325107799](https://issuetracker.google.com/issues/325107799), [b/277768544](https://issuetracker.google.com/issues/277768544))
- `Menu` now leverages the `SurfaceContainer` role for container color. `MenuDefaults.TonalElevation` is now `0.dp`. ([I135b7](https://android-review.googlesource.com/#/q/I135b7b5609dcb272a4458e14062495cca2a52ec8))
- `TextField` now leverages the `SurfaceContainerHighest` role for container color. ([I4dced](https://android-review.googlesource.com/#/q/I4dced0c76604b38aff9d58ba63f1450818054caa))
- Elevated chips now leverage the `SurfaceContainerLow` role ([I7cd2f](https://android-review.googlesource.com/#/q/I7cd2f8866db81c2c930406a631ad927b4ea755a8))
- `DatePicker` container color is now `SurfaceContainerHigh`. `DatePickerDefaults.TonalElevation` is now `0.dp`. ([Ida753](https://android-review.googlesource.com/#/q/Ida75315148a0eeafda207121bd58cf5ad6ef9987))
- Updates Bottom Sheets container color and drag handle color. ([I72a0a](https://android-review.googlesource.com/#/q/I72a0a4c343584952d0dc66c4f7de7be28955a4ae))
- `RichTooltip` container color is now `SurfaceContainer`. ([Ia8b45](https://android-review.googlesource.com/#/q/Ia8b459ba7ed2809286896f442654c75dec9c350a))
- `SearchBar` container color is now `SurfaceContainerHighest`. `SearchBarDefaults.TonalElevation` is now `0.dp`. ([I88604](https://android-review.googlesource.com/#/q/I886044e0819b603b0fc4265079bbd445759197c8))
- Updates switch disabled and unselected tracks/icons to leverage the `SurfaceContainerHighest` color role. ([I7687a](https://android-review.googlesource.com/#/q/I7687aa6aa79d2eb2381c9d0f64dffe2c2e958673))
- `AlertDialog` container color is now `SurfaceContainerHigh`. ([Ie0433](https://android-review.googlesource.com/#/q/Ie0433fc844ba6faab004e5f93f61681eb675045e))
- `BottomAppBar` container color is now `SurfaceContainer`. `TopAppBar` `onScroll` color is now `SurfaceContainer`. ([I41630](https://android-review.googlesource.com/#/q/I416308fdb2b68d77d41857598ce30f09ddae36fe))
- `ElevatedCard` container color is now `SurfaceContainerLow`. `FilledCard`'s container color of `SurfaceContainerHighest`. ([I35141](https://android-review.googlesource.com/#/q/I35141af0d7a069353309f267143e5808a9c0afca))
- `ElevatedButton` container color is now `SurfaceContainerLow`. `FilledIconButton`'s when unselected now have a container color of `SurfaceContainerHighest`. ([I792c9](https://android-review.googlesource.com/#/q/I792c9da5cc2cee2bc06e2acd99c47162ff59e872))
- Updates `TimePicker` container color and clock dial color role to `SurfaceContainerHighest`. ([I43b93](https://android-review.googlesource.com/#/q/I43b9360aa0ee69d8b898c6d9dfb97234f2c138fb))

### Version 1.3.0-alpha01

February 21, 2024

`androidx.compose.material3:material3-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9d6f951af96c8a1ab87b069a10f40b9a7b8a721..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/material3)

**New Features**

- Update Compose M3 `ModalBottomSheet` to support Predictive Back on U+ ([Iccf32](https://android-review.googlesource.com/#/q/Iccf324cb6dfc7f4ea1fe413b69e035658282360d), [b/281967264](https://issuetracker.google.com/issues/281967264), [b/304850357](https://issuetracker.google.com/issues/304850357))
- Updated Compose M3 `SearchBar` to support Predictive Back on U+ ([I657f8](https://android-review.googlesource.com/#/q/I657f8859433717fe5e4058bcd7a74649adece529))
- Updated Slider to improve accessibility by adding a gap and stop indicator. ([I3058e](https://android-review.googlesource.com/#/q/I3058e77cfa7017a781f70e498889ab11330990af))
- Updated `ProgressIndicator` to improve accessibility by adding a gap and stop indicator. ([I21451](https://android-review.googlesource.com/#/q/I2145171a393ef661a91799f4e1d39bdd69))
- Adding a default caret for rich tooltip, new rich tooltip API now allows for custom caret to be drawn given anchor `LayoutCoordinates`. ([Ifd42c](https://android-review.googlesource.com/#/q/Ifd42c2be34f72060cccce6414e28c1b2c01e025a))

**Behavior Changes**

- Material components have been migrated to use the new ripple APIs, and no longer query `RippleTheme`.

**API Changes**

- The fun `drawStopIndicator` is now public. ([I3f59f](https://android-review.googlesource.com/#/q/I3f59f30d4182bf3d296d13cf048d2077bccb35dc))
- Mark the `DatePicker`'s `formatWithSkeleton` function as internal ([Ic65dc](https://android-review.googlesource.com/#/q/Ic65dcccfde74a292180c92be96d69dd6468421f7))
- `DropdownMenu` now supports custom color, shape, elevation, and border. ([I8e981](https://android-review.googlesource.com/#/q/I8e9818a88b1aca1f16370c668ae60d19b0c5a89d), [b/289554448](https://issuetracker.google.com/issues/289554448), [b/301887035](https://issuetracker.google.com/issues/301887035), [b/283654243](https://issuetracker.google.com/issues/283654243))
- Material3 components exposing a `MutableInteractionSource` in their API have been updated to now expose a nullable `MutableInteractionSource` that defaults to `null`. There are no semantic changes here: passing null means that you do not wish to hoist the `MutableInteractionSource`, and it will be created inside the component if needed. Changing to null allows for some components to never allocate a `MutableInteractionSource`, and allows for other components to only lazily create an instance when they need to, which improves performance across these components. If you are not using the `MutableInteractionSource` you pass to these components, it is recommended that you pass null instead. It is also recommended that you make similar changes in your own components. ([I41abb](https://android-review.googlesource.com/#/q/I41abb601499b4a735b6302b96cdc1f0d066dbbdc), [b/298048146](https://issuetracker.google.com/issues/298048146))
- Adds `RippleConfiguration` and `LocalRippleConfiguration` to allow for per-component / sub-tree customization of ripples using fixed values. For example, to change the color of a component you don't control, or to disable a ripple for a component. In most cases the default values should be used: these APIs are an escape hatch for customization of individual components / limited sub-trees. For wider changes and custom design systems, you should instead build your own ripple using `createRippleModifierNode`. ([I7b5d6](https://android-review.googlesource.com/#/q/I7b5d62fd50ee78bb3559f83886aa1e7d9f964fb1), [b/298048146](https://issuetracker.google.com/issues/298048146))
- Adds new ripple API in material3 which replaces the deprecated `rememberRipple`. Also adds a temporary `CompositionLocal`, `LocalUseFallbackRippleImplementation`, to revert material3 components to using the deprecated `rememberRipple` / `RippleTheme` APIs. This will be removed in the next stable release, and is only intended to be a temporary migration aid for cases where you are providing a custom `RippleTheme`. ([I34cbc](https://android-review.googlesource.com/#/q/I34cbc2834133de4f3e8dde389ed4dab8c54b0c95), [b/298048146](https://issuetracker.google.com/issues/298048146))

**Bug Fixes**

- Removed subcomposition inside `ModalBottomSheet` to improve performance. Fixed an issue where `ModalBottomSheet` could crash in specific scenarios in combination with `LookaheadScope`. ([I2a198](https://android-review.googlesource.com/#/q/I2a198c788c55484541e5baa1a9fe2f9146e1e37c))
- Removed subcomposition inside `BottomSheetScaffold` to improve performance. Fixed an issue where `BottomSheetScaffold` would crash in specific scenarios in combination with `LookaheadScope`. ([Ie6401](https://android-review.googlesource.com/#/q/Ie6401d2db363ef3377ffd16bdf456c5f0b5a1667))
- The badge alignment is adjusted to be closer to the center of the anchor content in respect to the top-right corner. ([I18a28](https://android-review.googlesource.com/#/q/I18a28437cf249cd7d7ddffe103c89bdbe200399a))
- Fix an a11y issue with the `DateRangePicker` where the Month-Year text title was conveyed as actionable to the screen reader, Switch access, and Voice access users. ([I2ac55](https://android-review.googlesource.com/#/q/I2ac55010a9f9a39a8b0c3c76ed149488fba651d8))
- Fixed `mediumTopAppBarColors` param order bug. ([Ibe64a](https://android-review.googlesource.com/#/q/Ibe64a4f96541f9379e43c137c6f4f30eeaf1794a))

## Version 1.2

### Version 1.2.1

March 6, 2024

`androidx.compose.material3:material3-*:1.2.1` is released. Version 1.2.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d9d6f951af96c8a1ab87b069a10f40b9a7b8a721..93f0ae12e7922676c5010cdc5d10f3da59640c42/compose/material3).

**Bug Fixes**

- Make the Slider states stable again. Making `State.onValueChangeFinished` a val again. Wrapping `onValueChangeFinished` in a `rememberUpdatedState`. ([Ie8fd0](https://android-review.googlesource.com/#/q/Ie8fd041e069aa00a93541248631e3d59f68df56e), [b/322269951](https://issuetracker.google.com/issues/322269951))
- Removing `@Stable` from the states of `Slider` since we're changing `state.onValueChangeFinished` to a `var`. ([I82ba1](https://android-review.googlesource.com/#/q/I82ba1489fd131525790df3d7051bb9aa35e8ad71), [b/322269951](https://issuetracker.google.com/issues/322269951))
- Fix `NavigationBar` custom colors to copy from defaults. ([80a779](https://android-review.googlesource.com/#/q/f660a827d39245668e4edd0a30df044d135c6733), [b/326894020](https://issuetracker.google.com/issues/326894020))
- Fix regression in `ExposedDropdownMenu` to make it focusable again ([3fcec1](https://android-review.googlesource.com/#/q/Iabcf320c0fa1762463ce2fe2f38bae7ea73fcec1), [b/323694447](https://issuetracker.google.com/issues/323694447))
- Fix button color caching issue ([3e5bbc](https://android-review.googlesource.com/#/q/I7ffc4bffce91df28b572815cae21a316123e5bbc)[b/327371655](https://issuetracker.google.com/issues/327371655))

### Version 1.2.0

February 7, 2024

`androidx.compose.material3:material3-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..d9d6f951af96c8a1ab87b069a10f40b9a7b8a721/compose/material3)

**Known Issue**

- A View-Compose interop rendering [bug](https://issuetracker.google.com/issues/321997863) was introduced in `PrimaryTabRow` as part of a performance improvement change. The workaround is to use `TabRow` with `TabRowDefaults.PrimaryIndicator`

**Important changes since 1.1.0**

**New Material Design 3 Components**

- Pull to refresh
  - [PullToRefreshContainer](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshContainer(androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color))
  - [PullToRefreshState](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/PullToRefreshState)
- [Segmented Button](https://m3.material.io/components/segmented-buttons/overview)
  - [SegmentedButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#(androidx.compose.material3.SingleChoiceSegmentedButtonRowScope).SegmentedButton(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.SegmentedButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0,kotlin.Function0))
  - [SingleChoiceSegmentedButtonRow](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SingleChoiceSegmentedButtonRow(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,kotlin.Function1))
  - [MultiChoiceSegmentedButtonRow](https://developer.android.com/kotlin/androidx/compose/material3/package-summary#MultiChoiceSegmentedButtonRow(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,kotlin.Function1))

**Enhancements to existing Material Design 3 components.**

- Bottom app bar (RTL alignment, auto-hide on scroll)
  - [BottomAppBarScrollBehavior](https://developer.android.com/reference/kotlin/androidx/compose/material3/BottomAppBarScrollBehavior)
- Tabs visual update
  - [PrimaryIndicator](https://developer.android.com/reference/kotlin/androidx/compose/material3/TabRowDefaults#PrimaryIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Shape))
  - [SecondaryIndicator](https://developer.android.com/reference/kotlin/androidx/compose/material3/TabRowDefaults#SecondaryIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color))
- Badge (alignment update)

**Promoted experimental APIs to stable!**

**Performance improvements**

- Please see [this blog post](https://material.io/blog/material-3-compose-1-2) for more details!

### Version 1.2.0-rc01

January 24, 2024

`androidx.compose.material3:material3-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a2738e2803219745cf6082a30c608d95527cd4d5..71b01fc4c1e7e20ae46d9f142a348fd1d8f2b52c/compose/material3)

**Bug Fixes**

- Fixed `mediumTopAppBarColors` param order bug. ([Ibe64a](https://android-review.googlesource.com/#/q/Ibe64a4f96541f9379e43c137c6f4f30eeaf1794a))
- Fixed a bug introduced in `1.2.0-beta02` in `CardDefaults.cardColors` that did not update `contentColor` based on the `containerColor` param value. ([Iee041](https://android-review.googlesource.com/#/q/Iee041b79156739af98a1d6fc0a0b36bc99ba1586), [b/319671246](https://issuetracker.google.com/issues/319671246))
- Fixed a bug in `disabledContentColor` introduced in `1.2.0-beta02` and added small optimization. ([I6dda1](https://android-review.googlesource.com/#/q/I6dda1a8531aaa21a8e679155861e9c2eb063f123), [b/318428829](https://issuetracker.google.com/issues/318428829))

### Version 1.2.0-beta02

January 10, 2024

`androidx.compose.material3:material3-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f4aac2ed38164890551d06cae49210b2afb31336..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/compose/material3)

**Known Bug**

- A bug in `IconButtonColors` will by default assign `disabledContentColor` to an alpha (0.38f) of `LocalContentColor` instead of the user specified `contentColor`. The workaround is to explicitly set the `disabledContentColor`. This will be fixed in the next release.

**API Changes**

- Adding the capability to enable tooltip carets for Plain `Tooltip` APIs. ([Ibf767](https://android-review.googlesource.com/#/q/Ibf767f249315a4c4c327b62a487c6770435c13c7))
- `SwipeToDismissState`, `rememberSwipeToDismiss` and `SwipeToDismissValue` are all renamed to have `_SwipeToDismissBox_`. ([I68d6d](https://android-review.googlesource.com/#/q/I68d6dcb43013ec07c340276c0f578960a80bd0d1))

**Bug Fixes**

- Fixed `ListItem` end padding value to align with spec. ([Ibd68b](https://android-review.googlesource.com/#/q/Ibd68bcdc69da576e47b83fa793c0d626874aa4be), [b/305342674](https://issuetracker.google.com/issues/305342674))
- Outline color for outlined card is now correctly mapped to `OutlineVariant`. ([I75480](https://android-review.googlesource.com/#/q/I754802e26a95258d2c3b5b0d9e3030f64b9b630f), [b/310979715](https://issuetracker.google.com/issues/310979715))
- Dynamic color now pulls from system defined color roles. This improves contrast for accessible content, and more closely aligns dynamic color to the Material spec. ([I1de96](https://android-review.googlesource.com/#/q/I1de966bfc4f27259e1f07244ad10bc4c01b520f3))
- Fixed `ModalBottomSheet` back handling on Android T/13+ when `android:enableOnBackInvokedCallback="true"`. ([I728dc](https://android-review.googlesource.com/#/q/I728dc69c651c3b9d44857037ff8047ee67f13430), [b/306196110](https://issuetracker.google.com/issues/306196110))

### Version 1.2.0-beta01

December 13, 2023

`androidx.compose.material3:material3-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/064f85294a9be2e86650737b91db1bff868926e2..f4aac2ed38164890551d06cae49210b2afb31336/compose/material3)

**API Changes**

- Mark `TabIndicatorScope` as experimental. ([I45c88](https://android-review.googlesource.com/#/q/I45c88927d22d78743fe50f332addc9433454292a))
- Removing deprecated experimental APIs for tooltip. ([I438cb](https://android-review.googlesource.com/#/q/I438cbd0987e03da47d55eca56c8617c0c7b6f941))
- Change new `TabRow` overloads to not use subcompositions. This results in a different way to build the `TabRow` indicators with custom modifiers provided. ([Ife741](https://android-review.googlesource.com/#/q/Ife741ac95e65785e0f0673ab65414b7f74971d6d))
- Deprecate `DismissDirection` and `DismissValue` API's. These have been merged to `SwipeToDismissValue`, whose values indicate both position and direction of `SwipeToDismissBox`. `DismissState.progress` is now marked as a `FloatRange` between `0.0` and `1.0`. `DismissState` deprecated Saver and Constructor have now been removed. `SwipeToDismiss` component, state and defaults object have been remarked as experimental. ([Ib54f2](https://android-review.googlesource.com/#/q/Ib54f2c6707fdf2fa10fb5c19166c583f24c2bc6f))

**Bug Fixes**

- The default indicator for `PullToRefresh` is now an open arrowhead instead of a solid triangle. ([I67be3](https://android-review.googlesource.com/#/q/I67be3e670a96c3aa42d9c760fe318739dfb45650))

### Version 1.2.0-alpha12

November 29, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha12` is released. [Version 1.2.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03b3b94c9895b338f1b3eeec7c39f44cc72b9b89..064f85294a9be2e86650737b91db1bff868926e2/compose/material3)

**API Changes**

- `RangeSlider` now takes a Kotlin range (e.g., `0f..1f`) instead of a custom `FloatRange` value class. `SnapFlingBehavior.kt` now also uses a Kotlin range. ([I025cb](https://android-review.googlesource.com/#/q/I025cb6717a8f59e4ce70a8017fb76594383489ce))
- Mark Modifier factory functions as `@Stable`. ([Ib109f](https://android-review.googlesource.com/#/q/Ib109fa4fe56a3f2d79ad94e46163236f8ef6e046))

### Version 1.2.0-alpha11

November 15, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha11` is released. [Version 1.2.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..03b3b94c9895b338f1b3eeec7c39f44cc72b9b89/compose/material3)

**New Features**

- Implements `PullToRefreshContainer` and `PullToRefreshState`, which together provide a pull to refresh implementation in Material3. ([I16456](https://android-review.googlesource.com/#/q/I1645695db83e706b2f20e25b82bb937885d95abf), [b/261760718](https://issuetracker.google.com/issues/261760718))

**API Changes**

- Mark the `SwipeToDismissBox` `DismissDirection` and `DismissValue` as experimental. ([I517b0](https://android-review.googlesource.com/#/q/I517b00a95360086eba237d32c08386ac9c00e3d7))
- Rename `SwipeToDismiss` to `SwipeToDismissBox`. Rename `background` to `backgroundContent` and `dismissContent` to trailing `content` lambda. ([I7f4d3](https://android-review.googlesource.com/#/q/I7f4d3606d0b79b827f79780a9b0b86fdfb4bd810))
- Make the constructor for `ChipElevation` and `SelectableChipElevation` public. ([Ie0c48](https://android-review.googlesource.com/#/q/Ie0c48d7eec6b96d0276d434ed91ad94e53ad6a6c), [b/308432421](https://issuetracker.google.com/issues/308432421))
- Adding `ModalBottomSheetProperties`. Moving `securePolicy` into `ModalBottomSheetProperties`. Adding `isFocusable` and `shouldDismissOnBackPress` to `ModalBottomSheetProperties`. These new booleans help determine how modal bottom sheet should handle IME events. ([Iea56f](https://android-review.googlesource.com/#/q/Iea56ff84fd2f8a70037607e8aef0ceaf7a47e3d0), [b/278216859](https://issuetracker.google.com/issues/278216859))
- Updated `RangeSlider` and `Slider` states to remove `initialOnValueChange`, the initial prefixes, and appropriate kdocs. ([I57d30](https://android-review.googlesource.com/#/q/I57d302c9d3660381df37c4b1e756e84787c45219))
- Deprecate `ChipBorder` class and its associated function calls, recommend using `BorderStroke` directly instead. ([I89cc2](https://android-review.googlesource.com/#/q/I89cc2875d4179ee0ab09e4204b798a529da69e35))
- Foundation Tooltip APIs are now `@ExperimentalFoundationApi`. ([I30b0b](https://android-review.googlesource.com/#/q/I30b0b47c0d7d048369779600071fde5f2452e71d))
- `TabRow` and `ScrollableTabRow` are no longer deprecated. The new Primary and Secondary variants are marked as experimental. ([I0def6](https://android-review.googlesource.com/#/q/I0def68f453857ab8b40ff708ce09408251111067))
- Filter and input chips now use `BorderStroke` directly. ([I07a8d](https://android-review.googlesource.com/#/q/I07a8d2b2157599c7c3345ed7b2723bd4903b85df))
- `SegmentedButton` now uses `BorderStroke` directly. ([I89b9b](https://android-review.googlesource.com/#/q/I89b9bb765e0d31f97a8140c961e284cd025a321f))
- Renamed the generic `AlertDialog` function to `BasicAlertDialog`, and deprecate the previous function. ([Idbe52](https://android-review.googlesource.com/#/q/Idbe52197df664e1d98a6484f7052ec274f2b8be9))
- Rename `SwipeToDismiss` APIs to `SwipeDismiss`, and promote the new `SwipeDismiss` APIs to stable. ([I14cbe](https://android-review.googlesource.com/#/q/I14cbe61714d822b6481c1c6f30102b57de1fcfde))
- Adding `tonalElevation` and `shadowElevation` to tooltip APIs. Additionally, moving `TooltipBox`, `PlainTooltip`, and `RichTooltip` APIs back to experimental since they were accidentally released as stable. ([If0f66](https://android-review.googlesource.com/#/q/If0f66a8ccc737a0c163fd2b2a890ce60ad3d5fe4), [b/293939035](https://issuetracker.google.com/issues/293939035))
- Promote experimental chip APIs to stable. ([Iea2c3](https://android-review.googlesource.com/#/q/Iea2c35aaa8ebfb81720fcd42f9955aecdeb1643a))
- Removed the `@ExperimentalMaterial3Api` annotation from the Material3 clickable Cards. ([I88dbf](https://android-review.googlesource.com/#/q/I88dbfe41b25f0fd7603964b63a3e8adff0eeb16c))

**Bug Fixes**

- Fixed an issue where `SwipeToDismiss` would crash in certain scenarios with nested Lookahead and Lazy layouts. ([Ica8d1](https://android-review.googlesource.com/#/q/Ica8d19764426a0b8d6f7033a03d28687eab77d17), [b/297226562](https://issuetracker.google.com/issues/297226562))

### Version 1.2.0-alpha10

October 18, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha10` is released. [Version 1.2.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/80156d02f56222d46dbad403c3adb812faaf62d6..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/material3)

**API Changes**

- Promoting `Badge` and `BadgedBox` to stable. ([I67f16](https://android-review.googlesource.com/#/q/I67f1626a474c5c043f27c277a1dea8df8ae8a439), [b/261565132](https://issuetracker.google.com/issues/261565132))
- Adding `securePolicy` as a parameter to `ModalBottomSheet`, so users can define the behavior for `WindowManager.LayoutParams.FLAG_SECURE`. ([Icdac8](https://android-review.googlesource.com/#/q/Icdac86a7c7f358c9d4c023bf987a5c6c9227cd76), [b/296250262](https://issuetracker.google.com/issues/296250262))
- Added new overloads of `LinearProgressIndicator` and `CircularProgressIndicator` that take `progress` as a lambda. These should be more performant than the previous versions. ([I824e6](https://android-review.googlesource.com/#/q/I824e6ba4d57e713ad47f97f25a41c330b3439eb0), [b/295616656](https://issuetracker.google.com/issues/295616656))
- Renames `StandardSizeClasses` to `AllSizeClasses`. ([I8cb07](https://android-review.googlesource.com/#/q/I8cb076fc9f490695b2f639b02e2654661dab6eee))
- Combine calculation functions of window size classes. ([Iad935](https://android-review.googlesource.com/#/q/Iad935dc48d04040a7b3335f014ae0118f1d1d01d))

**Bug Fixes**

- Fix a `DatePicker` crash when quickly clicking the navigation arrow buttons when the displayed month is at the edge of the allowed range of years. ([I46f36](https://android-review.googlesource.com/#/q/I46f360883dc57d677a545863ff2d913903861928), [b/290954897](https://issuetracker.google.com/issues/290954897), [b/297002119](https://issuetracker.google.com/issues/297002119))
- \[Nav rail/bar\] Support transparent color for indicator. ([Ie0a9b](https://android-review.googlesource.com/c/platform/frameworks/support/+/2726373), [b/267289987](https://issuetracker.google.com/issues/267289987))

### Version 1.2.0-alpha09

October 4, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha09` is released. [Version 1.2.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..80156d02f56222d46dbad403c3adb812faaf62d6/compose/material3)

**API Changes**

- Migrated `ModalNavigationDrawer` and `DismissibleNavigationDrawer` to use new `AnchoredDraggable` APIs. `DrawerState`'s `animateTo` has been replaced by the open and close methods, and the offset is now exposed as a float instead of a state object. You can access the offset directly through `currentOffset`. ([I0a72c](https://android-review.googlesource.com/#/q/I0a72c377bd15770825efdce43c63a84ddfbeb0f4))
- Non-Composable functions have been added for creating a `DatePickerState` and `DateRangePickerState` directly. These functions can be used as an alternative to the Composable `rememberDatePickerState` and `rememberDateRangePickerState` functions when needed. ([I70326](https://android-review.googlesource.com/#/q/I703262a5a9d3e87da82adf1c9993b462cd8d941a), [b/291524052](https://issuetracker.google.com/issues/291524052))
- Fixed and Scrollable `TabRows` now have Primary and Secondary variants. These correctly map to the color and indicator behavior as defined in Material3.
- `PrimaryScrollableTabRow` and `SecondaryScrollableTabRow` now expose scroll state. ([Iec8f5](https://android-review.googlesource.com/#/q/Iec8f5a2876a15865842a6f0d4a584b539e16892a), [b/260572337](https://issuetracker.google.com/issues/260572337))
- Adding a new `sheetMaxWidth` parameter that developers can set to specify a maximum width that the sheet will span. Dp.Unspecified can be passed in for the parameter if a sheet that spans the entire screen width is desired. ([Ifb7c9](https://android-review.googlesource.com/#/q/Ifb7c9ee4d0066e86787e8fcbf0d156b9f92e5cfb), [b/266697696](https://issuetracker.google.com/issues/266697696))
- Adding back `PlainTooltipBox` and `RichTooltipBox` APIs as deprecated methods. ([I246fa](https://android-review.googlesource.com/#/q/I246fa14bd02246c864f1db1b98e34a352fd32e55))

**Bug Fixes**

- Fix a crash when the`DatePicker` is initialized with a `DatePickerFormatter` that has certain date skeletons that stay the same when converted to date patterns (such as YY). ([I01f29](https://android-review.googlesource.com/#/q/I01f2902849d4dd5c2426f4d3c13f52463692e3f4))

### Version 1.2.0-alpha08

September 20, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/material3)

**Behavior Breaking Change**

- `ColorScheme` is now Immutable, making individual color updates less efficient, but making more common usage of colors more efficient. The reasoning behind this change is that the majority of apps wouldn't have updating individual colors as a main use case. This is still possible but it will recompose more than before, in turn we significantly decrease the amount of state subscriptions through all of Material code and will impact initialization and runtime cost of more standard use cases. ([Ic447d](https://android-review.googlesource.com/#/q/Ic447d95734c3399733c49f4b6d018ec296fc251a), [b/297212873](https://issuetracker.google.com/issues/297212873))
- Tonal Elevation no longer animates in different interaction states to match spec. ([Icdd12](https://android-review.googlesource.com/#/q/Icdd12f4e11256ea166b3f4808f05228c28442ae7))

**API Changes**

- Added a new `BottomAppBar` that takes as parameter a `BottomAppBarScrollBehavior` in order to auto-hide it when content is scrolled. Also added `FabPosition.EndOverlay` allowing the FAB to overlay the bottom app bar in the scaffold instead of being anchored above it. ([Iecb47](https://android-review.googlesource.com/#/q/Iecb47accb59cbf44a49d0099289ef89736a84f2b))
- Added a simple Label component that builds on top of `BasicTooltipBox` that won't dismiss when tapping outside of the bounds of the label. ([I821f9](https://android-review.googlesource.com/#/q/I821f9f124e3d1933f3fc629c106d48d157929079))

**Bug Fixes**

- Removed the use of `rememberSaveable` for tooltips. ([Icc131](https://android-review.googlesource.com/#/q/Icc131c852cc3b3c722954aecb0a002711e13ca96), [b/299500338](https://issuetracker.google.com/issues/299500338))
- Introduced a temporary flag to control whether Scaffold should measure its children during measurement or during placement. By default, this will measure in measurement. If you are facing issues with the new behavior, please file an issue. ([I0b354](https://android-review.googlesource.com/#/q/I0b354a595fa56d96c4d48cfae5b394c7203bd23c))
- Fixed horizontal Edge to Edge in `BottomSheet` by using the correct measurement for device screen width. ([I1df0c](https://android-review.googlesource.com/#/q/I1df0cdf2ec735c17b914aee04ed20d54a1896573), [b/299058752](https://issuetracker.google.com/issues/299058752))
- Fixed a bug where `ModalBottomSheet` was not calling `onDismissedRequest` when dismissing it by swiping down on the sheet. ([Idfdd8](https://android-review.googlesource.com/#/q/Idfdd8b490caed6486292ae244ba9e4e9fb813f96))

### Version 1.2.0-alpha07

September 6, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/material3)

**New Features**

- Auto-mirror icons support has been added in `compose material 1.6.0-alpha05`, please see the [release notes](https://developer.android.com/jetpack/androidx/releases/compose-material#1.6.0-alpha05) for details on auto-mirror icons.

**API Changes**

- `SliderState` implements `DraggableState` ([I9b116](https://android-review.googlesource.com/#/q/I9b11656ba75c1f01060265735a75280858d5f4ae))
- Change shape to be a required param. Rename `position` to `index` in shape helper function. ([I34941](https://android-review.googlesource.com/#/q/I3494194f783157e24a10b643083fb99ff41777b9))
- Updates the `DatePicker` `formatWithSkeleton` to include a map that is used as a cache for performance improvements. ([I3195f](https://android-review.googlesource.com/#/q/I3195fdb04c8cab7fdf9bcf6e5cfd03d9a5700343))
- Added `BasicTooltipBox` to `compose.foundation` and updated `PlainTooltipBox` and `RichTooltipBox` to use `TooltipBox` with new `PlainTooltip` and `RichTooltip` composables. ([I79e1d](https://android-review.googlesource.com/#/q/I79e1df0ac02fdccc3399dcf8d24a515d6461fde9))

**Bug Fixes**

- `dynamicLightColorScheme` and `dynamicDarkColorScheme` now return higher chroma colors for surface and `surfaceContainer` roles. ([I5e901](https://android-review.googlesource.com/#/q/I5e90155620f5f6a5adbe5df4288a249744ba1699))
- Fixed an issue where some components using Subcomposition (e.g. `BottomSheetScaffold`) inside a Scaffold inside a `LookaheadScope` were attempting to read their size too early. ([I297b4](https://android-review.googlesource.com/#/q/I297b401ce6fd3b01ac5a2fba5fd617f66bc34550), [I871f1](https://android-review.googlesource.com/#/q/I871f1f655d0bf504490a040ec793b1b07ce195e4), [b/295536718](https://issuetracker.google.com/issues/295536718))

### Version 1.2.0-alpha06

August 23, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..3315f1ef094c312203fe26841287902916fbedf5/compose/material3)

**Bug Fixes**

- Fixed `DropdownMenu`'s `offset` calculation so x offsets depend solely on the local layout direction, and y offsets will no longer be reversed when the menu is near the bottom of the screen. ([Iccc74](https://android-review.googlesource.com/#/q/Iccc743f3306d9b259f0cc21d1089d9479df203fb), [b/294103942](https://issuetracker.google.com/issues/294103942))
- Fixed `DropdownMenu`'s `offset` calculation so x offsets depend solely on the local layout direction, and y offsets will no longer be reversed when the menu is near the bottom of the screen. ([Ib87a2](https://android-review.googlesource.com/#/q/Ib87a2157a9870409fdf066337c00585fd3ae005c), [b/294103942](https://issuetracker.google.com/issues/294103942))

### Version 1.2.0-alpha05

August 9, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/material3)

**API Changes**

- Updates to the Checkbox and `TriStateCheckbox` colors. The `CheckboxDefaults.colors()` `disabledUncheckedColor` now only affects the border of the checkbox. Special cases that require you to set the internal box color when disabled and unchecked requires a custom constructed instance of a `CheckboxColors` with the desired color values. ([I77d17](https://android-review.googlesource.com/#/q/I77d1777868ed6f869730610f0de5bd2caffff01a), [b/291943198](https://issuetracker.google.com/issues/291943198))

### Version 1.2.0-alpha04

July 26, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/material3)

**New Features**

- Experimental Segmented Button API ([Ifc8fb](https://android-review.googlesource.com/#/q/Ifc8fb7a7aba0f8712ed6f0b8508cb21f803795bb))
- Dividers now have a parameter to control orientation to support vertical dividers. ([I4c899](https://android-review.googlesource.com/#/q/I4c8999504b8f853c5c898fd960d5b4a0e9c02491), [b/288438593](https://issuetracker.google.com/issues/288438593))

**API Changes**

- We are moving the density dependency to the component level. This applies to the following components: `SwipeToDismiss` and Sheet based components. Please use the new overload provided where density is a parameter. ([I1846e](https://android-review.googlesource.com/#/q/I1846ea6aeb659f53eb8bff6895f7aea19af46fe8))
- Additional annotations to specify allowed inputs to composables ([Ief234](https://android-review.googlesource.com/#/q/Ief2342371876dcbdeed01122dd533759d189a01e))
- Add an icon parameter to segmented button, split semantics so that segmented buttons can be selectable to implement single-select, and toggleable to implement multi-select, with `SelectableSegmentedButtonRow` and `ToggelableSegmentedButtonRow` respectively. ([I38740](https://android-review.googlesource.com/#/q/I38740a995876133539f108629cf9a82d02c49cc2))
- Divider has been renamed to `HorizontalDivider`. Added `VerticalDivider` functionality. ([I5975c](https://android-review.googlesource.com/#/q/I5975c8c0a45299f1b2ad5f9be6f77f4f1f04542b))
- Change the use of `ClosedFloatingPointRange` for the lighter weight `FloatRange` in experimental Material3 APIs to minimize autoboxing. ([I4aab5](https://android-review.googlesource.com/#/q/I4aab509d1a5302f50556bd187882587eacc985b5))
- Added new Start alignment for `FabPosition` ([Ib7aea](https://android-review.googlesource.com/#/q/Ib7aea97d6ac5c6ee33fd10916c74c540ff5889de), [b/170592777](https://issuetracker.google.com/issues/170592777))

**Bug Fixes**

- `ModalBottomSheet` respects local layout direction. ([Ib4f44](https://android-review.googlesource.com/#/q/Ib4f44471ba73a6fbbbdb28e73ea876b91618c406), [b/285628622](https://issuetracker.google.com/issues/285628622))

### Version 1.2.0-alpha03

June 21, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..3b5b931546a48163444a9eddc533489fcddd7494/compose/material3)

**Behavior Changes**

- `includeFontPadding` is now `false` by default in Material 3 typography. The default line height style has also been changed to `Trim.None` and `Alignment.Center`, and explicit `lineHeight` (in sp) have been added to the `TextStyle`s of `Typography`. Consult [the API docs](https://developer.android.com/jetpack/compose/text/style-paragraph#adjust-line-height) if you want to customize these values, and see [the blog post](https://medium.com/androiddevelopers/fixing-font-padding-in-compose-text-768cd232425b) for an in-depth explainer of these changes. ([I6266f](https://android-review.googlesource.com/#/q/I6266fefa603c4079ec506a53d1372cebcc8dc50e), [Icabc3](https://android-review.googlesource.com/#/q/Icabc31f64e23ba0b8b92c909a8df1fe5f72ce9ed))

**New Features**

- Added an overload for `RangeSlider` that is a stateful version of the component. Created `RangeSliderState` that holds all of the information for the current active track, the measurements of the components of the `RangeSlider`, and the drag and gesture logic. ([I8c270](https://android-review.googlesource.com/#/q/I8c270fd01856f713bb5a40bf356f2875e64fd6e1))
- Search bar now supports shadows via the newly added `shadowElevation` parameter. ([Ia5369](https://android-review.googlesource.com/#/q/Ia5369b93f692ff1289148eb13a0fd0c44af8ec4e), [b/271040353](https://issuetracker.google.com/issues/271040353))
- `ColorScheme` now supports new [`SurfaceContainer` roles](https://material.io/blog/tone-based-surface-color-m3).
- Surface tonal elevation overlay can now be disabled with the `LocalTonalElevationEnabled` composition local. ([Ic203c](https://android-review.googlesource.com/#/q/Ic203c029337ab0892d1efdbecef069ad3c771f46), [b/277774590](https://issuetracker.google.com/issues/277774590))

**API Changes**

- Open the component colors constructors. ([I8c4a6](https://android-review.googlesource.com/#/q/I8c4a6ce56fb4a77a1e3eb17c6cad139b16bdc6ff))
- Adding focusable parameter to both tooltip APIs, so that developers can have the tooltip consume touch events or not. Be cautious that this might break accessibility focus automatic traversal. ([Ie32d8](https://android-review.googlesource.com/#/q/Ie32d8060e23253e7e7763ac882b07c8f54b113a3))
- Optimized accessibility for performance and memory allocations. ([Iede48](https://android-review.googlesource.com/#/q/Iede48198c2709b0736a39287ebc8f082d3869ae2))
- Expose `DefaultSizeClasses` and create `StandardSizeClasses` for `WindowSizeClasses` ([I91838](https://android-review.googlesource.com/#/q/I9183896b65cae68d142f0d4c2e8a023a958eb082))
- change `WindowWidth/HeightSizeClass` to float value classes ([Ie686e](https://android-review.googlesource.com/#/q/Ie686e093b760eb4e7bc055b03b848b026221554a))

**Bug Fixes**

- Scaffold's `contentWindowInsets` parameter now respects consumed window insets. Note that the behavior of content padding based on `topBar` and `bottomBar` remains unchanged when these parameters are provided. ([I08b73](https://android-review.googlesource.com/#/q/I08b739c22d2f2ac541801ae92e466ae41f265ff4), [b/264601542](https://issuetracker.google.com/issues/264601542))
- Fix the alignment of the center top app bar to ensure that a long title doesn't render over the action icons or the navigation icon. ([I4369f](https://android-review.googlesource.com/#/q/I4369f6c51c711129bb30b1de58684131b02499ae), [b/236994621](https://issuetracker.google.com/issues/236994621))
- Tab positions now enforce a minimum content width of 24.dp. This provides an accessible touch target for tab indicators. ([Id8861](https://android-review.googlesource.com/#/q/Id8861dce93609e920311f95b31151a778cc06222))
- Dynamic color palettes from `dynamicLightColorScheme` and `dynamicDarkColorScheme` now support new surface roles. ([I1252e](https://android-review.googlesource.com/#/q/I1252ebaf56aa26fab7a211ffcb0df306ab831b4d))
- Updating the badge notification alignment to not clip when colliding with great grandparent. ([Idf75a](https://android-review.googlesource.com/#/q/Idf75aadf4f6e06f3697ca2ae8420681772f7b48e))

### Version 1.2.0-alpha02

May 24, 2023

`androidx.compose.material3:material3-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/258b72327bc8e1d5a2205e37886d37e4de48495a..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/compose/material3)

**API Changes**

- Add window insets parameter to `ModalBottomSheet`.
  - Scrim for `ModalBottomSheet` may now be drawn behind status bar with `windowInsets` set to zero
  - Updated default `ModalBottomSheet` functionality to stay outside of system bars including navigation
  - Status bar inset handling is provided by drag handle in edge-to-edge mode.
  - `BottomSheetDefaults` includes window insets for `BottomSheetWindow`. ([I31200](https://android-review.googlesource.com/#/q/I312008e48573ebd21326f77216be0bcd0372aa78), [b/274872542](https://issuetracker.google.com/issues/274872542), [b/272973615](https://issuetracker.google.com/issues/272973615), [b/272334475](https://issuetracker.google.com/issues/272334475), [b/268432129](https://issuetracker.google.com/issues/268432129), [b/275849044](https://issuetracker.google.com/issues/275849044), [b/275486106](https://issuetracker.google.com/issues/275486106), [b/268433162](https://issuetracker.google.com/issues/268433162))
- Deprecate `Indicator` and add `Primary`/`SecondaryIndicator` to match the M3 specs. `PrimaryIndicator` matches the width of the tab's content whereas `SecondaryIndicator` spans the full available width. `SecondaryIndicator` is equivalent to the now deprecated `Indicator` and can be a direct replacement. ([I27604](https://android-review.googlesource.com/#/q/I27604bde8305f90ea2549993df676c92babfbaef))
- Added an option to pass in a `ScrollState` when constructing a `DropdownMenu` or an `ExposedDropdownMenu` for controlling the vertical scroll state of the displayed menu items. ([Ia0734](https://android-review.googlesource.com/#/q/Ia0734c832441988ff0047f25719d7c8edae8db5c), [b/185304441](https://issuetracker.google.com/issues/185304441))
- Added an overload for `Slider` that is a stateful version of the component. Created `SliderState` that holds all of the information for the current active track, the measurements of the components of the `Slider`, and the drag and gesture logic. ([I124a5](https://android-review.googlesource.com/#/q/I124a5957177062146d7994a115c486a299f1bbb3))
- Renaming the Semantics property `isContainer` to `isTraversalGroup` ([I121f6](https://android-review.googlesource.com/#/q/I121f64d7e7be332c41a1fbf10a70ef1ec14ce0dc))
- Added optimized `TextStyle.merge(...)` with full parameter list. ([Iad234](https://android-review.googlesource.com/#/q/Iad23419809af1c7405ba9a9d42569521e7647034), [b/246961787](https://issuetracker.google.com/issues/246961787))
- Made `TooltipState`, `RichTooltipState`, and `PlainTooltipState` public interfaces. Added `RichTooltipStateImpl` and `PlainTooltipStateImpl` for default states. Added `remember*State` functions to obtain these implemented states. Removed `TooltipSync` in favor of an `TooltipDefault.GlobalMutatorMutex`. ([I7813d](https://android-review.googlesource.com/#/q/I7813de158d25c43169dfb12cdf6b183332f753d9))
- Updated the `DatePickerColors` to include additional customization options for the date picker divider, navigation, and text input fields colors. ([I1a685](https://android-review.googlesource.com/#/q/I1a6856afd9a84e2aec18ece4ed6646b7f4ff4079), [b/274626815](https://issuetracker.google.com/issues/274626815))
- `DatePickerState` and the `DateRangePickerState` are now public interfaces with default implementations that can be retrieved by the `rememberDatePickerState` and `rememberDateRangePickerState`. ([I71c52](https://android-review.googlesource.com/#/q/I71c523826e8295772291dd5e3459c50037ac14a7))
- Removed the `dateValidator` from `DatePicker` and `DateRangePicker` and introduced a `SelectableDates` interface that can be set on the state to control which dates or years are selectable in the UI. ([Ic2fc6](https://android-review.googlesource.com/#/q/Ic2fc6f681417f632e7279016bd67ccbe372d653e))
- `TimePicker` removed from stable API, further changes are expected in the state API ([I3f39a](https://android-review.googlesource.com/#/q/I3f39a13a8cfd4ae5fdc2c05b644452b7bceea963))
- `ModalBottomSheet` moved to android only. `ModalBottomSheet` is not recommended for desktop use, and the functionality is not actively maintained. ([Ib3778](https://android-review.googlesource.com/#/q/Ib37784ddf10366ce34ecbcab3bcf15cc534b26fc))

**Bug Fixes**

- Fixed the `AlertDialog` dismiss action to appear below the confirm action when the actions stacked over each other to fit into the dialog's width. This fix aligns the implementation with the Material Design spec. ([I029de](https://android-review.googlesource.com/#/q/I029ded5c6dd79f38b1a060afb3d24dcfb9cf119a), [b/235454277](https://issuetracker.google.com/issues/235454277))
- Fixed bug in `ListItem` using incorrect padding for three-line items. ([I6e235](https://android-review.googlesource.com/#/q/I6e235866f4f873b16a0d5f8e37fdc7f4370b76aa))
- `ModalBottomSheet` now can display IME keyboard ([Idc508](https://android-review.googlesource.com/#/q/Idc5082008acb547cac2100a69cab4be7db85f50f), [b/262140644](https://issuetracker.google.com/issues/262140644), [b/268380384](https://issuetracker.google.com/issues/268380384), [b/272483584](https://issuetracker.google.com/issues/272483584))

### Version 1.2.0-alpha01

May 10, 2023

`androidx.compose.material3:material3:1.2.0-alpha01` and `androidx.compose.material3:material3-window-size-class:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a2cccd4facfdd7aba23b74cfb5253196d1c0fc31..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/material3)

## Version 1.1

### Version 1.1.2

September 20, 2023

`androidx.compose.material3:material3:1.1.2` and `androidx.compose.material3:material3-window-size-class:1.1.2` are released. [Version 1.1.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/28298029d8a95189089eace9273d608da3c6b81a..444f88fb647c26b3426a9a95eac755624463514e/compose/material3)

**Bug Fixes**

- Fixed modifier incorrectly being passed to two composables. ([b/282761472](https://issuetracker.google.com/issue?id=282761472))
- Fixed `TimePickerState` returns incorrect hours when initialized with 23 hours. ([b/278242122](https://issuetracker.google.com/issue?id=278242122))
- Fixed initial toggle state for noon and minute validation. ([b/269768197](https://issuetracker.google.com/issue?id=269768197), [b/282790635](https://issuetracker.google.com/issue?id=282790635))
- Fixed `state.hour` returning incorrect value for 11pm. ([b/282761472](https://issuetracker.google.com/issue?id=282761472), [b/278242122](https://issuetracker.google.com/issue?id=278242122))

### Version 1.1.1

June 21, 2023

`androidx.compose.material3:material3:1.1.1` and `androidx.compose.material3:material3-window-size-class:1.1.1` are released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/27c69a0a8f6f433a0e969ff934e622adcfd5a947..28298029d8a95189089eace9273d608da3c6b81a/compose/material3)

**Bug Fixes**

- Adds call for `ModalBottomSheet` without `windowInset` param for binary compatibility. ([Ib7959](https://android-review.googlesource.com/#/q/Ib79592db8c08b657aae3b46c51f708a57d7e52d6))
- Add window insets parameter to `ModalBottomSheet`.
  - Scrim for `ModalBottomSheet` may now be drawn behind status bar with `windowInsets` set to zero
  - Updated default `ModalBottomSheet` functionality to stay outside of system bars including navigation
  - Status bar inset handling is provided by drag handle in edge-to-edge mode.
  - `BottomSheetDefaults` includes window insets for `BottomSheetWindow`. ([I31200](https://android-review.googlesource.com/#/q/I312008e48573ebd21326f77216be0bcd0372aa78), [b/274872542](https://issuetracker.google.com/issues/274872542), [b/272973615](https://issuetracker.google.com/issues/272973615), [b/272334475](https://issuetracker.google.com/issues/272334475), [b/268432129](https://issuetracker.google.com/issues/268432129), [b/275849044](https://issuetracker.google.com/issues/275849044), [b/275486106](https://issuetracker.google.com/issues/275486106), [b/268433162](https://issuetracker.google.com/issues/268433162))

### Version 1.1.0

May 10, 2023

`androidx.compose.material3:material3:1.1.0` and `androidx.compose.material3:material3-window-size-class:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a2cccd4facfdd7aba23b74cfb5253196d1c0fc31..27c69a0a8f6f433a0e969ff934e622adcfd5a947/compose/material3)

**Major features of 1.1.0**

**New Material Design 3 components**

- [Bottom sheets](https://m3.material.io/components/bottom-sheets/overview)
  - [ModalBottomSheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function1)), [BottomSheetScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomSheetScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.BottomSheetScaffoldState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function0,kotlin.Boolean,kotlin.Function0,kotlin.Function1,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1))
- [Date pickers](https://m3.material.io/components/date-pickers/overview)
  - [DatePicker](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePicker(androidx.compose.material3.DatePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)), [DateRangePicker](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DateRangePicker(androidx.compose.material3.DateRangePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)), [DatePickerDialog](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.material3.DatePickerColors,androidx.compose.ui.window.DialogProperties,kotlin.Function1))
- [Search](https://m3.material.io/components/search/overview)
  - [SearchBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)), [DockedSearchBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DockedSearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1))
- [SwipeToDismiss](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SwipeToDismiss(androidx.compose.material3.DismissState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.collections.Set))
- [Time Pickers](https://m3.material.io/components/time-pickers/overview)
  - [TimePicker](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType))
  - [TimeInput](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimeInput(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors))
- [Tooltips](https://m3.material.io/components/tooltips/overview)
  - [PlainTooltipBox](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#PlainTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.PlainTooltipState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)), [RichTooltip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RichTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.RichTooltipState,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.RichTooltipColors,kotlin.Function1))

**Enhancements to existing Material Design 3 components.**

**Promoted experimental APIs to stable!**

Please see this [blog post](https://material.io/blog/material-3-compose-1-1) for more details!

### Version 1.1.0-rc01

April 19, 2023

`androidx.compose.material3:material3:1.1.0-rc01` and `androidx.compose.material3:material3-window-size-class:1.1.0-rc01` are released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/258b72327bc8e1d5a2205e37886d37e4de48495a..a2cccd4facfdd7aba23b74cfb5253196d1c0fc31/compose/material3)

**API Changes**

- `TimePicker` removed from stable API, further changes are expected in the state API ([I3f39a](https://android-review.googlesource.com/#/q/I3f39a13a8cfd4ae5fdc2c05b644452b7bceea963))
- `ModalBottomSheet` moved to android only. `ModalBottomSheet` is not recommended for desktop use, and the functionality is not actively maintained. ([Ib3778](https://android-review.googlesource.com/#/q/Ib37784ddf10366ce34ecbcab3bcf15cc534b26fc))

### Version 1.1.0-beta02

April 5, 2023

`androidx.compose.material3:material3:1.1.0-beta02` and `androidx.compose.material3:material3-window-size-class:1.1.0-beta02` are released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/material3)

**API Changes**

- `SheetState` now has optional `skipHiddenState` parameter
- `rememberStandardBottomSheetState` now has optional `skipHiddenState` parameter
- `BottomSheetScaffold` now has a defined Hidden anchor, though it is disabled by default
- `SheetState.requireOffset` documentation has been updated
- `BottomSheetDefaults.MinimizedShape` has been renamed as `BottomSheetDefaults.HiddenShape` ([I839f4](https://android-review.googlesource.com/#/q/I839f464c556eafb1b6fd823134da46943475919d), [b/273870234](https://issuetracker.google.com/issues/273870234))

**Bug Fixes**

- Do not switch the dial face from hour to minute when touch exploration is enabled. ([I717d0](https://android-review.googlesource.com/#/q/I717d015a566423b1006a9549dbc6850cde3ae356))
- `ModalBottomSheet` and `BottomSheetScaffold` drag handle semantics are now merged. ([I05afb](https://android-review.googlesource.com/#/q/I05afb36b9bd2f2cff6127478b1be715450aff687))
- `BottomSheetScaffold` modifier, `containerColor` and `contentColor` parameters now only affect content. ([I992cb](https://android-review.googlesource.com/#/q/I992cb8a410e827be2e97f35e64f3070320abc1cb))
- `BottomSheetScaffold nestedScroll` for sheet content now implements flings. ([I992cb](https://android-review.googlesource.com/#/q/I992cb8a410e827be2e97f35e64f3070320abc1cb))

### Version 1.1.0-beta01

March 22, 2023

`androidx.compose.material3:material3:1.1.0-beta01` and `androidx.compose.material3:material3-window-size-class:1.1.0-beta01` are released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ba23752ee1dc6eae18f1350f0815ed79d605e9c5..5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/material3)

**API Changes**

- Add layout type param to `TimePicker` composable. It allows to use different layouts, depending on the screen configuration ([Ia0e16](https://android-review.googlesource.com/#/q/Ia0e164e18f9be63fd93446f03e0eb24f435ed4d2))
- `SearchBarDefaults` has been marked as experimental. ([I65561](https://android-review.googlesource.com/#/q/I65561ee442e307fed389d8379982354af729acab))
- Added shadow elevation to `BottomSheetScaffold` ([I94e0f](https://android-review.googlesource.com/#/q/I94e0f2e736f142ce44b97ca1f86ad70640efd9d3))
- Added support for displaying the date pickers without the header part. API changes to allow passing a null headline when creating a date picker. You can now pass null headline, title, and `showToggleMode = false` in order to display a headless picker. ([Id3f3a](https://android-review.googlesource.com/#/q/Id3f3a800c84c12f7c96a3654e59258933da0ec0b), [b/266132421](https://issuetracker.google.com/issues/266132421), [b/267194809](https://issuetracker.google.com/issues/267194809))

**Bug Fixes**

- Search bars now automatically clear focus when made inactive. ([I22a7c](https://android-review.googlesource.com/#/q/I22a7c93c7d06f39b6413c3f1d40f141b0d141fd8), [b/261444487](https://issuetracker.google.com/issues/261444487))
- Updated the `DateRangePicker` to allow selecting a range with the same date for its start and end. ([I16529](https://android-review.googlesource.com/#/q/I16529402422cca8b5a370483fa14e4f429548e7c), [b/272882497](https://issuetracker.google.com/issues/272882497))
- Text fields now properly position their text elements when font size is smaller than expected. This may result in a few pixels change in your apps based on font settings and script. ([I8b8d0](https://android-review.googlesource.com/#/q/I8b8d0c81e2882446a0fb3e68e1744efc07cb990d))
- Bottom sheet semantic actions now have labels. ([I277b0](https://android-review.googlesource.com/#/q/I277b088568cf9f3a3448386d5da1b32425b83c05))

### Version 1.1.0-alpha08

March 8, 2023

`androidx.compose.material3:material3:1.1.0-alpha08` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha08` are released. [Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..ba23752ee1dc6eae18f1350f0815ed79d605e9c5/compose/material3)

**New Features**

- Added support for `BottomSheetScaffold` and `BottomSheetScaffoldState`. ([I063d4](https://android-review.googlesource.com/#/q/I063d432e10628475a8c902cd30e75f12fd40d99c))

**API Changes**

- Added functionality to the `DatePickerState` and the `DateRangePickerState` to allow setting dates after the initial creation of the state, as well as resetting selections by setting null timestamps. Setting dates manually should be made with caution, and the new `setSelection` function will throw an exception in case a provided date fails a precondition (see documentation). ([Ifa645](https://android-review.googlesource.com/#/q/Ifa6451a9e32ad031ac3223cb8b5fea132a2d0191), [b/268609314](https://issuetracker.google.com/issues/268609314), [b/270427389](https://issuetracker.google.com/issues/270427389))
- Rename Collapsed `SheetValue` to `PartiallyExpanded` to more accurately and flexibly depict behavior in this state. ([Ia1491](https://android-review.googlesource.com/#/q/Ia1491d68dc636ca9d80a31372a64e63f69ee4013))
- Updated `ListItem` parameter names to _content instead of _text. Default getters are now `ReadOnlyComposables` where relevant. ([I69a25](https://android-review.googlesource.com/#/q/I69a252e0a5bc6ebb63c7be08746ace65dfe02d62))
- Graduate interactive Surface APIs from experimental. ([I90d59](https://android-review.googlesource.com/#/q/I90d596d5aa4141884f1b7878ae61053aa4fc7161), [b/261561812](https://issuetracker.google.com/issues/261561812))

**Bug Fixes**

- Fixed an issue where `ModalBottomSheet`'s `HalfExpanded` state was calculated incorrectly and the sheet would appear to be floating. ([I45e84](https://android-review.googlesource.com/#/q/I45e84ba00263f4bea61a3abac54bf05a6494bce8), [b/268411386](https://issuetracker.google.com/issues/268411386))
- Add `confirmValueChange` check to scrim tap for `ModalBottomSheet`. ([I2311a](https://android-review.googlesource.com/#/q/I2311a043ffbac63c4278fce9d0e73450fc808201), [b/270425759](https://issuetracker.google.com/issues/270425759))
- Move semantic `BottomSheet` actions to drag handle. ([I158ba](https://android-review.googlesource.com/#/q/I158bae5303952975da627224926043322175c1a2))
- `ModalBottomSheet` now commands focus on launch, handles back button. ([I4d2ab](https://android-review.googlesource.com/#/q/I4d2ab70ac620fd98835125b84794ce24dfcf5ebd))
- `ModalBottomSheet onDismissRequest` is now also handled during nested scroll flings. ([I655c5](https://android-review.googlesource.com/#/q/I655c581c067056b1815fe50befd32333c78e30bb), [b/268433166](https://issuetracker.google.com/issues/268433166))

### Version 1.1.0-alpha07

February 22, 2023

`androidx.compose.material3:material3:1.1.0-alpha07` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha07` are released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/material3)

**New Features**

- Add a Time Input composable that works with `rememberTimePickerState()`, it follows the M3 spec for time input ([Ia4fab](https://android-review.googlesource.com/#/q/Ia4fab49a74980251b5dee8d9dacacf2012811c7d))
- Added a Material 3 `DateRangePicker` API for selecting a range of dates. ([I7a6c3](https://android-review.googlesource.com/#/q/I7a6c3bd20c0330eec911786619dcc7b86c3dad04), [b/267194809](https://issuetracker.google.com/issues/267194809))
- Added a Material 3 input mode support for selecting date ranges via the `DateRangePicker` API. ([Ifdbc4](https://android-review.googlesource.com/#/q/Ifdbc4d78f6e5029ae68c6d30d80a843f30843309))
- Text field colors now allow customizing:
  - The input field and placeholder text colors based on focus and error state. The `textColor` parameter has been renamed to `unfocusedTextColor`, and `placeholderColor` has been renamed to `unfocusedPlaceholderColor`.
  - The container color for filled text fields based on error state with the new `errorContainerColor` param.
- Exposed dropdown menu text field colors have been updated with parameters to support the new prefix and suffix API. ([I9c8b4](https://android-review.googlesource.com/#/q/I9c8b4f070921d64f8a7a3ac74074c12d7773348b), [b/254284181](https://issuetracker.google.com/issues/254284181), [b/264766350](https://issuetracker.google.com/issues/264766350))

**API Changes**

- Reverting some Slider API versions and removing redundant Slider overloads that are covered by the new experimental Slider with custom thumb and track. Promoting `RangeSlider` to be stable. ([Ie8fbd](https://android-review.googlesource.com/#/q/Ie8fbdf564fa3e2a83ff891a79bc0baa5c12e586d))
- Renamed `defaultElevation` to `elevation` in chip's elevation functions. ([I0f872](https://android-review.googlesource.com/#/q/I0f87254cdb91bec8c6ace6fd3883342733755ad9))
- The following Material 3 text field APIs are no longer experimental: `TextField`, `OutlinedTextField`, `textFieldWithLabelPadding`, `textFieldWithoutLabelPadding`, `outlinedTextFieldPadding`. ([Ieb5c0](https://android-review.googlesource.com/#/q/Ieb5c0ab1f3270ee3fd45265f143f49a5cdaa2d08), [b/261561819](https://issuetracker.google.com/issues/261561819))
- `TimePickers` `is24Hour` uses system setting ([I18856](https://android-review.googlesource.com/#/q/I18856a395db9ce7e4dbd099299ded52407fd2873))
- Removed experimental annotation from scaffold apis. ([Ibb51e](https://android-review.googlesource.com/#/q/Ibb51eaf53f07ec6407de4acd4a3174137b171d1e), [b/261565765](https://issuetracker.google.com/issues/261565765), [b/261436953](https://issuetracker.google.com/issues/261436953))

**Bug Fixes**

- `ModalBottomSheet` default shape is now always `SheetDefaults.ExpandedShape`. ([I0dfca](https://android-review.googlesource.com/#/q/I0dfcaa455e676e5280abb399db53e31a61870679))
- Accessibility improvements for Material 3 `DatePicker` and `DateRangePicker`. ([I5087e](https://android-review.googlesource.com/#/q/I5087ec38bd740387f9b42197f72511d0eda4b0c7))
- Fix bug where max height constraint is propagated and may crash. ([I30d8c](https://android-review.googlesource.com/#/q/I30d8c5eb63c4c9a5078cb10e5a591d6ac2c8a065))
- Removed semantic roles from clickable and selectable surfaces, updated components that used them to set roles using modifier.semantics ([I793d9](https://android-review.googlesource.com/#/q/I793d92a6d882bb8d0cae537a365709f9483e950d))

### Version 1.1.0-alpha06

February 8, 2023

`androidx.compose.material3:material3:1.1.0-alpha06` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/material3)

**New Features**

- Text fields now support prefix and suffix text ([Ia8578](https://android-review.googlesource.com/#/q/Ia85786c582981e8f16a7053a869e06c2c1a43fb8), [b/179884561](https://issuetracker.google.com/issues/179884561))
- Added a `TimePicker` function to show a time picker following the Material 3 spec, used in conjunction with `TimePickerState` and convenience method `rememberTimePickerState` ([I71910](https://android-review.googlesource.com/#/q/I71910979841fd934153da109380a5078ba1a9741))
- A date input is now a display mode at the `DatePicker`. Added support for switching between date picker and date input modes. ([Ieeff7](https://android-review.googlesource.com/#/q/Ieeff707da21566b0b8d4fe365662ce6ae2a6acd1))
- Added API for `RichTextTooltips`. ([I58ef3](https://android-review.googlesource.com/#/q/I58ef33c950cdcb0461e0cf5f192fb730444d6fb4))
- Modal bottom sheet implementation for Material 3, including `ModalBottomSheet` and `ModalBottomSheetDefaults`. Also introduces `SheetState` and `rememberSheetState` which can be used for future sheet components. ([I0853a](https://android-review.googlesource.com/#/q/I0853a6ec6d06166787701db1edb4a09b90dd563e), [b/244189383](https://issuetracker.google.com/issues/244189383))

**API Changes**

- Stablize the API `showSnackbar` ([I195c2](https://android-review.googlesource.com/#/q/I195c2c308e2597acf97dc90b5c0f3315b3556e90), [b/261424370](https://issuetracker.google.com/issues/261424370))
- Stablize the APIs for assist chip and suggestion chip ([Ibb67b](https://android-review.googlesource.com/#/q/Ibb67b1b2a21c8cb37213a22a76d49357b4097621), [b/261424370](https://issuetracker.google.com/issues/261424370))
- Promotes `ListItem`, `ListItemDefaults` and `ListItemColors` API to non-experimental ([I7e7fa](https://android-review.googlesource.com/#/q/I7e7faed87feb7ab15de0dbda181eda60d6a9cebc), [b/261438882](https://issuetracker.google.com/issues/261438882))
- Promoting `SliderPositions`, `SliderDefaults.Thumb`, and `SliderDefaults.Track` to stable and adding non-experimental `Slider` and `RangeSlider` APIs that contain custom thumbs and track. Also deprecating the previous `Slider` and `RangeSlider` APIs. ([Ie5ea6](https://android-review.googlesource.com/#/q/Ie5ea6c578fc9335e658305bdf2b64365eb4fab01), [b/261566890](https://issuetracker.google.com/issues/261566890))
- Made `Modifier.tooltipAnchor()` public, so devs can pass it to the anchor to indicate a tooltip should be displayed on long press. Updated `PlainTooltipBox` API to no longer make `TooltipState` nullable and now has a default. ([Ie2fb7](https://android-review.googlesource.com/#/q/Ie2fb71e5fdbe4266d075861f2eac972e1ba0de03))
- `ProgressIndicatorDefaults.circularTrackColor` has been marked `@Composable` for consistency. ([Id29cc](https://android-review.googlesource.com/#/q/Id29cc370fda15a68076e546550582298a64f17b4))
- Restored property getter `LocalMinimuTouchTargetEnforcement` and mark it as deprecated and redirect to `LocalMinimumInteractiveComponentEnforcement`. ([I60dd5](https://android-review.googlesource.com/#/q/I60dd5ceb7c5703c8ba68f1b7d4a4a883b3f961a8))

### Version 1.1.0-alpha05

January 26, 2023

`androidx.compose.material3:material3:1.1.0-alpha05` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/material3)

**New Features**

- `DatePickerDialog` and accessibility support
- Added Custom thumb and track to `RangeSlider`.

**Dependency Updates**

- `Compose UI` and `Compose Material` now depend on [Lifecycle 2.6.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.0).

### Version 1.1.0-alpha04

January 11, 2023

`androidx.compose.material3:material3:1.1.0-alpha04` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha04` are released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/material3)

**New Features**

- Initial `DatePicker` API for picking a single date via a calendar UI. This API is still undergoing changes. ([I722b9](https://android-review.googlesource.com/#/q/I722b9884403da2d615167f6572a2da9256dbae2a))
- Added support for plain tooltips via `PlainTooltipBox`. ([I0cdfb](https://android-review.googlesource.com/#/q/I0cdfb8dc51bc3691b948184adc4fcb9cf61be107))
- Search bar ([Iad128](https://android-review.googlesource.com/#/q/Iad1280bb7c3eaeac73116f73567bb6de07a81eb2))
- `SwipeToDismiss` ([I458a8](https://android-review.googlesource.com/#/q/I458a8e1359896712a2a8aede43e0283977be4601), [b/242889540](https://issuetracker.google.com/issues/242889540))

**API Changes**

- Added in `IsContainer` semantics property on Surfaces. This property will be used in a later change that determines traversal order based on the semantic meaning of elements such as surfaces. ([I63379](https://android-review.googlesource.com/#/q/I63379fde102abbee7d5464c50b1c86a59e01e768))
- Mark navigation drawer related APIs as stable. ([Iab01e](https://android-review.googlesource.com/#/q/Iab01ec21f7ef0de980ffc868f46b54966186e6ed), [b/261439597](https://issuetracker.google.com/issues/261439597))
- Added a track color parameter for circular progress indicators, and a stroke cap parameter for both circular and linear progress indicators. ([Ie668c](https://android-review.googlesource.com/#/q/Ie668cc47ce9ce3aa688ad3c3ed9e9e15fdbda5e9), [b/216325962](https://issuetracker.google.com/issues/216325962), [b/222964817](https://issuetracker.google.com/issues/222964817))
- More return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Add `Modifier.minimumInteractiveComponentSize`. It can be used to reserve at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. ([I33f58](https://android-review.googlesource.com/#/q/I33f58e4c11cf74668e97167b91dad26b64ac554b), [b/258495559](https://issuetracker.google.com/issues/258495559))
- Added experimental API for `AlertDialog` composable that has a content slot. ([Iec4a2](https://android-review.googlesource.com/#/q/Iec4a21dc5ad723f1a66527f3aea82a204fba4fd6))

**Bug Fixes**

- Progress for progress indicators is now properly bounded to its expected range. ([I8a7eb](https://android-review.googlesource.com/#/q/I8a7eb76931af76bac20dbd2879674a60c2899672), [b/262262727](https://issuetracker.google.com/issues/262262727))

**Known Issue**

- When updating from `androidx.compose.foundation:1.4.0-alpha03` to `androidx.compose.foundation:1.4.0-alpha04`, you might experience a `java.lang.NoSuchFieldError` error. [Here](https://issuetracker.google.com/issues/265172081) is where the issue was orginially reported. A fix has been submitted, and will be available on the next Compose update. As a work around, update your `androidx.compose.material` and `androidx.compose.material3` libraries to the latest version(1.1.0-alpha04) or downgrade your `androidx.compose.foundation` to 1.4.0-alpha03.

### Version 1.1.0-alpha03

December 7, 2022

`androidx.compose.material3:material3:1.1.0-alpha03` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha03` are released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/material3)

**API Changes**

- Renamed `consumedWindowInsets()` to `consumeWindowInsets()` and `withConsumedWindowInsets()` to `onConsumedWindowInsetsChanged()` and made the Modifiers public. ([Ie44e1](https://android-review.googlesource.com/#/q/Ie44e1304babf2007f6dc5894716ca92c2ef6d067))
- Add new default content padding for text button with icon to use. ([I8f662](https://android-review.googlesource.com/#/q/I8f662b35818c5d513029e1f49b23a313a3eeadef))
- Added disabled colors for navigation bar and rail. ([Ia7892](https://android-review.googlesource.com/#/q/Ia78923757cb5c72813789a09f4fabb9a64c615af), [b/258867034](https://issuetracker.google.com/issues/258867034))
- Added an Modifier API to query ancestors scroll info. ([I2ba9d](https://android-review.googlesource.com/#/q/I2ba9d6d55f853e5d2775fe9a9f15e7a41d41e359), [b/203141462](https://issuetracker.google.com/issues/203141462))
- Used in `Clickable` to correctly delay press interactions, when gestures could become scroll events.
- Fixed `Clickables` not correctly delaying ripples, when used inside an `Scrollable ViewGroup`.
- Updated Drawers and Sheets to correctly delay presses in case gestures can become scroll events.

**Dependency Updates**

- `Compose UI` and `Compose Material` now depend on Lifecycle 2.5.1. ([I05ab0](https://android-review.googlesource.com/#/q/I05ab08e48f49eee1a1e573d172ba22efc47640a6), [b/258038814](https://issuetracker.google.com/issues/258038814))

### Version 1.1.0-alpha02

November 9, 2022

`androidx.compose.material3:material3:1.1.0-alpha02` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/material3)

**API Changes**

- `awaitFirstDown` and `waitForUpOrCancellation` now accept a `PointerEventPass` for greater flexibility (also fixes `ExposedDropdownMenuBox` showing a menu while scrolling).([I7579a](https://android-review.googlesource.com/#/q/I7579a2dbb44c748a3fd3e515d2e7ab086aaff443), [b/212091796](https://issuetracker.google.com/issues/212091796))
- Added `minLines` parameter into material and material3 Text, `TextField` and `OutlinedTextField` which allows setting the minimum height of the component in terms of number of lines ([I4af1d](https://android-review.googlesource.com/#/q/I4af1df6521acaa97edbed5048079b5e81b647dd8))
- Deprecate the `TopAppBarDefaults smallTopAppBarColors` function in favor of a new `topAppBarColors` function that should be used when creating a `TopAppBar`. ([Ie6cb9](https://android-review.googlesource.com/#/q/Ie6cb94d2ff4278f1315b4acbf4d0a816afa7050f))
- Added `minLines` parameter to the `BasicText` and `BasicTextField`. It allows to set the minimum height of these composables in terms of number of lines ([I24294](https://android-review.googlesource.com/#/q/I2429479960eef317f467fa054b979c12fd73689d), [b/122476634](https://issuetracker.google.com/issues/122476634))

**Bug Fixes**

- Clip the content of a Material3 `IconButton` and `IconToggleBotton` to the component's state-layer shape (e.g. circular shape). ([I9da8f](https://android-review.googlesource.com/#/q/I9da8fcc755e0fc30c870f908f9018ea2dc1ffb86))
- Updates Material3 Medium and Large top app bars to apply the same background color across their entire surface, and to allow setting overriding the default colors with transparent color values. ([I67659](https://android-review.googlesource.com/#/q/I67659d8754b953165a5b2fa3c7a5720a0976665e), [b/249688556](https://issuetracker.google.com/issues/249688556), [b/250838918](https://issuetracker.google.com/issues/250838918))

### Version 1.1.0-alpha01

October 24, 2022

`androidx.compose.material3:material3:1.1.0-alpha01` and `androidx.compose.material3:material3-window-size-class:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b/compose/material3)

**Bug Fixes**

- Fixes to the top app bar when title is applied with a TextStyle and a Brush. ([If667e](https://android-review.googlesource.com/q/If667ed1ddaa162e64279aff534f94250db4bf0b6))

## Version 1.0

### Version 1.0.1

November 9, 2022

`androidx.compose.material3:material3:1.0.1` and `androidx.compose.material3:material3-window-size-class:1.0.1` are released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/material3)

**Bug Fixes**

- Updates Material3 Medium and Large top app bars to apply the same background color across their entire surface, and to allow setting overriding the default colors with transparent color values. ([I67659](https://android-review.googlesource.com/#/q/I67659d8754b953165a5b2fa3c7a5720a0976665e), [b/249688556](https://issuetracker.google.com/issues/249688556), [b/250838918](https://issuetracker.google.com/issues/250838918))

### Version 1.0.0

October 24, 2022

`androidx.compose.material3:material3:1.0.0` and `androidx.compose.material3:material3-window-size-class:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/material3)

**Major features of 1.0.0**

This is the first stable release of Compose Material 3!

#### Material Design 3 theming and Material You dynamic color

- [MaterialTheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#materialtheme)
- [Color](https://m3.material.io/styles/color/overview)
  - [ColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme)
  - [lightColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#lightcolorscheme), [darkColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#darkcolorscheme)
- [Dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)
  - [dynamicLightColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamiclightcolorscheme), [dynamicDarkColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamicdarkcolorscheme)
- [Typography](https://m3.material.io/styles/typography/overview)
  - [Typography](https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography)
- [Shapes](https://m3.material.io/styles/shape/overview)
  - [Shapes](https://developer.android.com/reference/kotlin/androidx/compose/material3/Shapes)

#### Material Design 3 components

- [Badge](https://m3.material.io/components/badges/overview)
  - [Badge](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#badge), [BadgedBox](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#badgedbox)
- [Bottom App Bar](https://m3.material.io/components/bottom-app-bar/overview)
  - [BottomAppBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomAppBar)
- [Buttons](https://m3.material.io/components/buttons/overview)
  - [Button](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#button), [ElevatedButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#elevatedbutton), [FilledTonalButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#filledtonalbutton), [OutlinedButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#outlinedbutton), [TextButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#textbutton)
- [FAB](https://m3.material.io/components/floating-action-button/overview) and [extended FAB](https://m3.material.io/components/extended-fab/overview)
  - [SmallFloatingActionButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#smallfloatingactionbutton), [FloatingActionButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#floatingactionbutton), [LargeFloatingActionButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#largefloatingactionbutton), [ExtendedFloatingActionButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#extendedfloatingactionbutton)
- [Cards](https://m3.material.io/components/cards/overview)
  - [Card](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#card), [OutlinedCard](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#outlinedcard), [ElevatedCard](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#elevatedcard)
- [Checkbox](https://m3.material.io/components/checkbox/overview)
  - [Checkbox](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#checkbox)
- [Chips](https://m3.material.io/components/chips/overview)
  - [AssistChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AssistChip), [ElevatedAssistChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedAssistChip), [FilterChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FilterChip), [ElevatedFilterChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedFilterChip), [InputChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#InputChip), [SuggestionChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SuggestionChip), [ElevatedSuggestionChip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedSuggestionChip)
- [Dialogs](https://m3.material.io/components/dialogs/overview)
  - [AlertDialog](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#alertdialog)
- [Divider](https://m3.material.io/components/divider/overview)
  - [Divider](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Divider)
- [Dropdown Menu](https://m3.material.io/components/menus/overview)
  - [DropdownMenu](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DropdownMenu), [DropdownMenuItem](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DropdownMenuItem), [ExposedDropdownMenuBox](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ExposedDropdownMenuBox)
- [List](https://m3.material.io/components/lists/overview)
  - [ListItem](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem)
- [Navigation bar](https://m3.material.io/components/navigation-bar/overview)
  - [NavigationBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationbar)
- [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview)
  - [ModalNavigationDrawer](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#modalnavigationdrawer), [ModalDrawerSheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#modaldrawersheet), [DismissibleNavigationDrawer](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dismissiblenavigationdrawer), [DismissibleDrawerSheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dismissibledrawersheet), [PermanentNavigationDrawer](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#permanentnavigationdrawer), [PermanentDrawerSheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#permanentdrawersheet)
- [Navigation rail](https://m3.material.io/components/navigation-rail/overview)
  - [NavigationRail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- [Progress Indicator](https://m3.material.io/components/progress-indicators/overview)
  - [CircularProgressIndicator](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CircularProgressIndicator), [LinearProgressIndicator](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LinearProgressIndicator)
- [Radio Button](https://m3.material.io/components/radio-button/overview)
  - [RadioButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RadioButton)
- [Slider](https://m3.material.io/components/sliders/overview)
  - [Slider](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Slider), [RangeSlider](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RangeSlider)
- [Switch](https://m3.material.io/components/switch/overview)
  - [Switch](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Switch)
- [Tabs](https://m3.material.io/components/tabs/overview)
  - [Tab](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Tab), [LeadingIconTab](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LeadingIconTab), [TabRow](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TabRow), [ScrollableTabRow](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ScrollableTabRow)
- [Text Fields](https://m3.material.io/components/text-fields/overview)
  - [TextField](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TextField), [OutlinedTextField](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedTextField)
- [Top app bar](https://m3.material.io/components/top-app-bar/overview)
  - [TopAppBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#topappbar), [CenterAlignedTopAppBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#centeralignedtopappbar), [MediumTopAppBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#mediumtopappbar), [LargeTopAppBar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeTopAppBar)
- Icon
  - [Icon](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#icon), [IconButton](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#iconbutton)
- Text
  - [Text](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#text)
- Surface
  - [Surface](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#surface)
- Layout
  - [Scaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#scaffold)
- Content color
  - [LocalContentColor](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LocalContentColor())

#### Window Size Class

- `material3-window-size-class` is a new library that provides support for window size classes: a set of opinionated viewport breakpoints for you to design, develop, and test resizable application layouts against. You can use `calculateWindowSizeClass` to retrieve a window size class instance, which you can use to determine how your UI should appear, such as showing a navigation rail instead of bottom navigation for larger window sizes. For more information and sample usage see the API reference [documentation](https://developer.android.com/reference/kotlin/androidx/compose/material3/windowsizeclass/package-summary) for `WindowSizeClass`.

- Please see this [blog post](http://material.io/blog/material-3-compose-stable) for more details!

### Version 1.0.0-rc01

October 5, 2022

`androidx.compose.material3:material3:1.0.0-rc01` and `androidx.compose.material3:material3-window-size-class:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/material3)

**API Changes**

- Added slot param for supporting text to text field API ([Iaac0d](https://android-review.googlesource.com/#/q/Iaac0d260b17ccf2999a4ea99a132b80e8f0bbadc), [b/227146125](https://issuetracker.google.com/issues/227146125))

### Version 1.0.0-beta03

September 21, 2022

`androidx.compose.material3:material3:1.0.0-beta03` and `androidx.compose.material3:material3-window-size-class:1.0.0-beta03` are released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/520c85b133ddf020d8f9e0a9a2240ed75df1cdfa..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/material3)

**API Changes**

- `ExposedDropdownMenuDefaults` now exposes a padding value for menu items. ([I34ee1](https://android-review.googlesource.com/#/q/I34ee1c4b4f07261c704aad64d97565b3752ef650))
- `ExposedDropdownMenuBoxScope` now has a `Modifier.menuAnchor()` modifier that should be passed to the text field for proper a11y behavior. ([I27fa3](https://android-review.googlesource.com/#/q/I27fa36b864d5b3c923b538b480dfcda76ab0e863))
- Adding two overloaded methods for the current Slider API to allow users to pass in a thumb or track to populate the slider. ([I21c00](https://android-review.googlesource.com/#/q/I21c0022c3882f896f1d4ca855a24cec5d317f641))

**Bug Fixes**

- Updated dark theme color mapping for On Error Container to tone 90 ([Ic5612](https://android-review.googlesource.com/#/q/Ic561226d89432381ac900475cc0f677f7bc33ffe))
- Fix to allow setting a transparent background for small Material 3 top app bars. ([I645e2](https://android-review.googlesource.com/#/q/I645e29cd35cefb6e8effb2e455b53c5ff777568a), [b/245575782](https://issuetracker.google.com/issues/245575782))

### Version 1.0.0-beta02

September 7, 2022

`androidx.compose.material3:material3:1.0.0-beta02` and `androidx.compose.material3:material3-window-size-class:1.0.0-beta02` are released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/material3)

**API Changes**

- Default components insets introduced in m3 components in beta01 version no longer account for IME insets.
- Material3 Scaffold component now has a `contentWindowInsets` parameter, allowing to specify the amount of insets to handle for the content slot. ([Icf11a](https://android-review.googlesource.com/#/q/Icf11a4169c801d2670d88066984328205f48bb4f), [b/243713323](https://issuetracker.google.com/issues/243713323))
- Deprecates the experimental Material 3 `SmallTopAppBar` function and introduces an equivalent `TopAppBar` function. Please migrate your usage to the new one. ([I74404](https://android-review.googlesource.com/#/q/I74404a64a5764ea02895358d2db5dc9bb18c5aba), [b/226918634](https://issuetracker.google.com/issues/226918634))
- Adds control over the top app bar fling and snap behaviors. ([I15c81](https://android-review.googlesource.com/#/q/I15c817b5c615d43c22d96ca8b5b539df03e68dfa))
- Removes startIndent from Divider, moves color to last parameter. ([If7be2](https://android-review.googlesource.com/#/q/If7be24e6a8dc6b3386a4419b87ee275dd513d630))

**Bug Fixes**

- Have Dialogs identify themselves to talkback users by announcing the word Dialog when they are displayed. ([I857ef](https://android-review.googlesource.com/#/q/I857ef62e308faf491c696679ebd570a2ac50f804))

### Version 1.0.0-beta01

August 24, 2022

`androidx.compose.material3:material3:1.0.0-beta01` and `androidx.compose.material3:material3-window-size-class:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/material3)

**API Reference**

To see latest theming, component and other composables available check out the [Compose Material 3 API reference overview](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#overview).

**API Changes**

- Updated the Material 3 top app bar to snap into a fully collapsed to a fully extended state. Also, updated the `TopAppBarDefaults` behavior function to be Composables and provide default values for their top app bar state and animation spec. ([I642b3](https://android-review.googlesource.com/#/q/I642b393470e6a29a8a02cb5589fea02f601be8ec))
- Updated FAB component signatures to match surface API ([I3afaa](https://android-review.googlesource.com/#/q/I3afaaa86e1ed658f4f7f8d2bb3cff19f8ff874be))
- Added insets Build-in support for Top app bars, drawers, navigation bar and rail. These components, when used separately or with Scaffold will automatically handle insets for developers. Note: This change doesn't add automatic handling of status bar icons and transparency of the status and navigation bars. Please, continue to do it manually to ensure the best edge-to-edge experience. ([I7e4e6](https://android-review.googlesource.com/#/q/I7e4e67bd1a84d62bd5ab1eddc7dbed8efdb471d1), [b/183161866](https://issuetracker.google.com/issues/183161866))
- Updated component defaults to reduce API surface for future flexibility and performance improvements. ([I31820](https://android-review.googlesource.com/#/q/I31820a25a7d9807634856b52fa7258c84a729ddc))
- Reordered chip and navigation drawer sheet parameters to maintain consistency within the API ([I45d0b](https://android-review.googlesource.com/#/q/I45d0bd7f072d80fca60c397cc294aa65bc80782d))
- Removed `startIndent` from Divider and moved color to be the last parameter.([If7be2](https://android-review.googlesource.com/#/q/If7be24e6a8dc6b3386a4419b87ee275dd513d630))

### Version 1.0.0-alpha16

August 10, 2022

`androidx.compose.material3:material3:1.0.0-alpha16` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha16` are released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/material3)

**New Features**

- Support specifying a custom width on a navigation drawer. ([Ia7f10](https://android-review.googlesource.com/#/q/Ia7f10a73922f252481f6dbc448b6fa8fb21184e4))

**API Changes**

- Reorder Tab and Leading icon tab parameters to maintain consistency within the API ([Ie2637](https://android-review.googlesource.com/#/q/Ie2637a746c3b0ad1ec937797f9c84ea0a492fae7))
- Marked `BadgeDefaults` as experimental. ([I98ef3](https://android-review.googlesource.com/#/q/I98ef3634788c18cf72dc99ebb94bc0ebffca53c9))
- Remove deprecated navigation drawer function. ([I4f2db](https://android-review.googlesource.com/#/q/I4f2db8d83436f0c0ea29bb1859808d7012cbdda2))
- Reorder Slider parameters in Material 3 to maintain consistency within the API ([I0aee7](https://android-review.googlesource.com/#/q/I0aee767c8c0a35f81d9315e14a6fd4b26bb56fd2))
- Reorder `NavigationBar` and `NavigationRail` parameters to maintain consistency within the API ([I51cda](https://android-review.googlesource.com/#/q/I51cda43da7eb060d14ad72e4194cbec6c4ced88a))
- Reorder parameters in Material 3 to maintain consistency across the API. ([If4ae1](https://android-review.googlesource.com/#/q/If4ae1ed910477dc66e678811f260bfe29a78f929))
- Reorder Slider parameters in Material 3 to maintain consistency within the API ([I62673](https://android-review.googlesource.com/#/q/I62673725050d204f7cb8929cf15d7c97508a3f45))
- Renamed icons parameter to actions to be consistent with top app bar ([Id75be](https://android-review.googlesource.com/#/q/Id75beabf735837ea874997126e234f6d5f0f75ce))
- Mark `Badge` and `BadgedBox` as experimental because the anchor alignment is still influx. ([I1712e](https://android-review.googlesource.com/#/q/I1712ebf74e212414f3fb6b3dde9834a7f9ec0a16), [b/236524516](https://issuetracker.google.com/issues/236524516))
- Change `@ExperimentalMaterial3Api` annotations on icon button variants to `@OptIn` ([I070b5](https://android-review.googlesource.com/#/q/I070b51abf2438730a2a7cabc02b01a522dc1b7d8))
- Separated a navigation drawer's content to its own composable to support specifying a custom width on it. ([Ia7f10](https://android-review.googlesource.com/#/q/Ia7f10a73922f252481f6dbc448b6fa8fb21184e4))
- Removes `Divider` from `MenuDefaults` and `TabDefaults` ([I4e33c](https://android-review.googlesource.com/#/q/I4e33c470db42695c3530397cbda9ed64012a04a2))

### Version 1.0.0-alpha15

July 27, 2022

`androidx.compose.material3:material3:1.0.0-alpha15` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha15` are released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/material3)

**New Features**

- Allow dragging the top app bar from the bar itself. ([I65c00](https://android-review.googlesource.com/#/q/I65c00deb7acc54e900d72ed157cc6d2dcea7a3fa), [b/205873416](https://issuetracker.google.com/issues/205873416))

**API Changes**

- Updates to the `FilterChip` and `ElevatedFilterChip` APIs to remove the `selectedIcon` slot and promote reusing the `leadingIcon` for displaying a selected state. ([Ie5dc2](https://android-review.googlesource.com/#/q/Ie5dc23eb277c567af46c6b2697a5b3c54efa629d))
- Add scrim and outline variant color roles. ([Id6d54](https://android-review.googlesource.com/#/q/Id6d54d4005fc5e1b6ce839fa3a5f83a559b3ba71))
- Fix naming conventions for composable defaults. ([I62b27](https://android-review.googlesource.com/#/q/I62b27a186bdad34390c0a7bda567f824f3def1ab))
- Mark `ListItemDefaults` and `ListItemColors` as experimental. ([I1f3ec](https://android-review.googlesource.com/#/q/I1f3ecdb59759371eaba5647ec5f3488d18130a89))
- Changes to the top app bar API to better reflect the meaning of its state properties. Also, mark the top app bar API as experimental. ([Ic0ad8](https://android-review.googlesource.com/#/q/Ic0ad8f51bf0d251b3936146088d596cfb4cce02f))
- Text selection colors have now been added to `TextFieldColors` for better discoverability. ([Iba1b8](https://android-review.googlesource.com/#/q/Iba1b860479606ee11496a813f916fd76fbd03fb8))
- Adding `ButtonDefault.ButtonWithIconContentPadding` to be used with buttons that contain an icon. ([I2bf9c](https://android-review.googlesource.com/#/q/I2bf9c8e665c6f31b4c797c7f5438202e41c8f8ab))
- Text fields have been marked as experimental to allow for more flexibility in future API changes. ([I127b5](https://android-review.googlesource.com/#/q/I127b5151fe3cb977e8a837db9d0aa92a42a88491))
- Removed the `@ExperimentalMaterial3Api` annotation from the `Checkbox` function. ([I5eefc](https://android-review.googlesource.com/#/q/I5eefc0b2a1eb930c3045e803c9dacf2f52c7b875))
- Removed the `@ExperimentalMaterial3Api` annotation from the `RadioButton` function. ([I17e2a](https://android-review.googlesource.com/#/q/I17e2a5f940590e90addc7b3f5cf792e03b3b6c7b))
- Removed the `@ExperimentalMaterial3Api` annotation from the non-interactive Cards. ([I9bd49](https://android-review.googlesource.com/#/q/I9bd49630bfcc32b609f54e23572303a6dfe29f17))
- Updates various component defaults objects to include colors, shapes etc. ([I96e11](https://android-review.googlesource.com/#/q/I96e11c23407209aa6f1575cc1e7d9ae0920d3769))

**Bug Fixes**

- Removed non-functioning trailing icons from input chip samples to avoid user confusion in the catalog app. ([I9846a](https://android-review.googlesource.com/#/q/I9846a1cdabf98b75368f2077a872deb7eeb8eb5d))

### Version 1.0.0-alpha14

June 29, 2022

`androidx.compose.material3:material3:1.0.0-alpha14` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha14` are released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..8094b683499b4098092c01028b55a38b49e357f2/compose/material3)

**New Features**

- Added M3 list implementation, see the documentation for sample usage ([Id7a20](https://android-review.googlesource.com/#/q/Id7a201348bf6d891a98263d05f9d2768627a333a))

**API Changes**

- Change parameter name from values to value in `RangeSlider` ([I3b79a](https://android-review.googlesource.com/#/q/I3b79aaaebf9b3080e9d775e10d287355c7d03ca5))
- API changes to the `InputChip` implementation to support a selectable state per the Material Design spec. Additional support at the `FilterChip` colors for selected disabled state. ([I55244](https://android-review.googlesource.com/#/q/I552440f329616d514ea67c724b8aec6e985066e1), [b/235792432](https://issuetracker.google.com/issues/235792432))
- Add `BottomAppBar` default FAB ([Ida4c8](https://android-review.googlesource.com/#/q/Ida4c8f2760e6476d5283b5b1df6b6608441da405))
- `ColorScheme.surfaceColorAtElevation` was added ([Id41af](https://android-review.googlesource.com/#/q/Id41afb06b2df2cfbf2cb023a18ced47e8a5222b5))
- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))
- `WindowWidthSizeClass` and `WindowHeightSizeClass` now implement Comparable, so they can be compared using operators (\<, \<=, \>=, \>) and other APIs. ([I747d0](https://android-review.googlesource.com/#/q/I747d0a41291662ae049e9188061b9a08fef3186c))

**Bug Fixes**

- Update badge sample to provide more meaningful content description. ([I10b9d](https://android-review.googlesource.com/#/q/I10b9d99db01ac3844fa8b84b70aae231512e9d99))
- Adds option to use the system font size to the Material 3 catalog's theme picker. ([I10605](https://android-review.googlesource.com/#/q/I106053e3243d09607c36d30bfb038aacfcc7cd79))
- Adds sample code for Badge and indeterminate progress indicators. ([I8fbe0](https://android-review.googlesource.com/#/q/I8fbe0c9d411928269761b4ac5ace64e26d05ceca))

### Version 1.0.0-alpha13

June 1, 2022

`androidx.compose.material3:material3:1.0.0-alpha13` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha13` are released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/54b662674ce4727aaf8ea0c38a07939a5c29a3a2..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/material3)

**API Changes**

- Supports maintaining the top app bar position on configuration change. ([I10459](https://android-review.googlesource.com/#/q/I104599fa724196bbf1fec1bfa424a2a70abaf2fe), [b/216160958](https://issuetracker.google.com/issues/216160958))

### Version 1.0.0-alpha12

May 18, 2022

`androidx.compose.material3:material3:1.0.0-alpha12` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha12` are released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..3b9b6af3f1b771c21aa90b87e466318ad8f9a2f0/compose/material3)

**Bug Fixes**

- Slider parent can now have 0 width. ([b/231707291](https://issuetracker.google.com/231707291))

### Version 1.0.0-alpha11

May 11, 2022

`androidx.compose.material3:material3:1.0.0-alpha11` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha11` are released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/material3)

**New Features**

- Added `RangeSlider` to Material 3 ([I18e38](https://android-review.googlesource.com/#/q/I18e381050eca3330cd52e733e01acc311033da51))
- Adds Material3 `AssistChip` and `InputChip` support ([I0d25a](https://android-review.googlesource.com/#/q/I0d25ac7b16a3ddbdcca7cbcc4fa3c6ae176a004e))
- Adds Material3 `FilterChip` and `SuggestionChip` support ([I9fdf3](https://android-review.googlesource.com/#/q/I9fdf3f5b6eda1ecd59c398fa9cdab251fd71f0aa))

**API Changes**

- Renamed `TextFieldDefaults.BorderStroke` composable that draws a border stroke in `OutlinedTextField` to `TextFieldDefaults.BorderBox`. ([I5f295](https://android-review.googlesource.com/#/q/I5f295062ff2a3ebc72115df2412062558d226273))
- Switch m3 visual changes ([Iab30e](https://android-review.googlesource.com/#/q/Iab30e7135d8fd2d9f0254b14057023e8ce1dad38))
- Allow passing colors to the standard icon buttons. ([Ia2445](https://android-review.googlesource.com/#/q/Ia24458ae2e6bc32b799db152b3825534f14ac6d4))

**Bug Fixes**

- Add lint check to material3/Scaffold to ensure that the inner padding is used ([I72293](https://android-review.googlesource.com/#/q/I72293ba593b57caaacee5d86702b10b281b0246c), [b/226951418](https://issuetracker.google.com/issues/226951418))

### Version 1.0.0-alpha10

April 20, 2022

`androidx.compose.material3:material3:1.0.0-alpha10` and `androidx.compose.material3:material3-window-size-class:1.0.0-alpha10` are released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f/compose/material3)

**New Features**

- `material3-window-size-class` is a new library that provides support for window size classes: a set of opinionated viewport breakpoints for you to design, develop, and test resizable application layouts against. You can use `calculateWindowSizeClass` to retrieve a window size class instance, which you can use to determine how your UI should appear, such as showing a navigation rail instead of bottom navigation for larger window sizes. For more information and sample usage see the API reference documentation for `WindowSizeClass`. For more information on window size class definitions, see the public guidance on supporting different screen sizes.

**API Changes**

- Adds default FAB elevation for `BottomAppBar`, removes trailing lambda from `BottomAppBar` with FAB. ([I92c47](https://android-review.googlesource.com/#/q/I92c479d1978bc1d2a2e2d5f66d63afee870363fa))
- Adds Material3 `FilledIconButton`, `FilledTonalIconButton`, and `OutlinedIconButton`. ([Ib2bda](https://android-review.googlesource.com/#/q/Ib2bda93643f833d04a989233cc3b1bc09bcdfa2d))
- Updates Material 3 Snackbar API to accept color values for the optional action and dismiss-action. ([Ibe4b4](https://android-review.googlesource.com/#/q/Ibe4b49cdf157005f98eda5c1bb5a2e2c40668d63))
- Partial consumption (down OR position) has been deprecated in `PointerInputChange`. You can use `consume()` to consume the change completely. You can use `isConsumed` to determine whether or not someone else has previously consumed the change.
- `PointerInputChange::copy()` now always makes a shallow copy. It means that copies of `PointerInputChange` will be consumed once one of the copies is consumed. If you want to create an unbound `PointerInputChange`, use constructor instead. ([Ie6be4](https://android-review.googlesource.com/#/q/Ie6be471e6ed2a843e38712922c2231fdfd26213a), [b/225669674](https://issuetracker.google.com/issues/225669674))
- Changes to the Cards API to receive the container and content colors via a `CardColors` interface, and to support a disabled state for clickable cards. ([I927df](https://android-review.googlesource.com/#/q/I927dfb2b7723e3d2f5c36de86c6ea9a78582c153))
- The parameter `backgroundColor` has been renamed `containerColor` in Material 3 text fields for improved consistency with other components. ([I6fbd9](https://android-review.googlesource.com/#/q/I6fbd9b4114b8bbd699ed57a8ff1df73b8fd16c33))

**Bug Fixes**

- Updates to the standard `IconButton` to align it with the Material3 spec. ([I09eab](https://android-review.googlesource.com/#/q/I09eab8e771f182abcafaabf8679ce1374126181b))
- Move the top bar height of material3 Scaffold into the padding passed to content, allowing the content to render underneath the top app bar. If the `PaddingValues` are ignored, then the content might be obscured by the top bar. ([I83cbc](https://android-review.googlesource.com/#/q/I83cbc17a8068a04ea8b18609f12bd9e103630229), [b/217776202](https://issuetracker.google.com/issues/217776202))

### Version 1.0.0-alpha09

April 6, 2022

`androidx.compose.material3:material3:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/material3/material3)

**New Features**

- Added Material 3 Switch API ([I2c3ad](https://android-review.googlesource.com/#/q/I2c3ad5eee4f628be3e437436da1c1fb63fdb6962))

**API Changes**

- Added support for dropdown menus with text fields (aka 'exposed dropdown menus' or 'combo boxes'.) ([I1b832](https://android-review.googlesource.com/#/q/I1b8326ccc1e1d89f96d5c459d83c2aeb05881f52))
- Added shape parameter to MaterialTheme and Shape sub system. ([I37426](https://android-review.googlesource.com/#/q/I374265da432fceb6c72a1b3a61335e7fdefd825e))
- Added an expanded parameter to `ExtendedFloatingActionButton` to control whether the FAB is expanded or collapsed, with animations between each state. Added Extended FAB overload for extended FABs with trailing text for ExtendedFABs without icon. ([Iba7f1](https://android-review.googlesource.com/#/q/Iba7f1a4ece7c4a6e1fd294d04245b5dfcd5609de))

### Version 1.0.0-alpha08

March 23, 2022

`androidx.compose.material3:material3:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/material3/material3)

**New Features**

- Added support for Material 3 text fields. ([I795cc](https://android-review.googlesource.com/#/q/I795cc83e59b56200517e2d5b5dfbbd48cf51aeda), [b/199377790](https://issuetracker.google.com/issues/199377790))

**API Changes**

- Add default divider for menu ([I01374](https://android-review.googlesource.com/#/q/I013746cec4c0d9b24ee72a70aaca04d70259d2ab))
- Added `surfaceTint` color parameter to `ColorScheme` class. ([I2f558](https://android-review.googlesource.com/#/q/I2f558f3f0de6cc4d1bc06ba876102fae5273afdd))

**Bug Fixes**

- Fix at the Material3 Button to read its default text style value from the MaterialTheme. ([Ie62fc](https://android-review.googlesource.com/#/q/Ie62fcb0c42f3ec6940734f9c80989f0ee57bb99e))

### Version 1.0.0-alpha07

March 9, 2022

`androidx.compose.material3:material3:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/material3/material3)

**API Changes**

- Updates to Material 3 Surface API that brings back the overloaded functions for clickable Surfaces, as well as adding a function to support selectable and toggleable Surfaces. ([I4bf18](https://android-review.googlesource.com/#/q/I4bf182d38d4c503cc5f16f5c966294d9f042930d))
- `LazyVerticalGrid` and `LazyHorizontalGrid` are now stable. ([I307c0](https://android-review.googlesource.com/#/q/I307c0ce412c7bc762e334e429013c0442bd22fde))
- `LazyVerticalGrid/LazyHorizontalGrid` and all related apis were moved into .grid subpackage. Please update your imports from androidx.compose.foundation.lazy to androidx.compose.foundation.lazy.grid. ([I2d446](https://android-review.googlesource.com/#/q/I2d446e0bed6f27f0394b7dcab1152301e3404b0f))
- Reverted previous change of relying solely on a View for `WindowInsetsControllerCompat`, and again require a Window which is required for managing some window flags. Deprecated `ViewCompat.getWindowInsetsController` in favor of `WindowCompat.getInsetsController` to ensure that the correct Window is used (such as if the View is in a dialog). ([I660ae](https://android-review.googlesource.com/#/q/I660aee32108b59516232b41e05b3f05ae2538554), [b/219572936](https://issuetracker.google.com/issues/219572936))
- Added a new `LazyVerticalGrid` API to define cross axis sizes ([I17723](https://android-review.googlesource.com/#/q/I17723fdc6302a345dd643fb637e1644168a2a321))

**Bug Fixes**

- Updates to the Card API to follow changes at the Surface API ([I3c8b9](https://android-review.googlesource.com/#/q/I3c8b9adfb1ece2e8861f8646620c47772270c25c))

### Version 1.0.0-alpha06

February 23, 2022

`androidx.compose.material3:material3:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/material3/material3)

**API Changes**

- `NavigationDrawerItem` is added that represents a single destination within the drawers ([Ic396f](https://android-review.googlesource.com/#/q/Ic396fe99d1f26080a3e3a9d2ed505e72008c85aa), [b/218286829](https://issuetracker.google.com/issues/218286829))
- `PermanentNavigationDrawer` and `DismissibleNavigationDrawer` have been added as experimental APIs. Those are the drawers suitable well for large screen devices. ([I5f8ab](https://android-review.googlesource.com/#/q/I5f8abcd6137f0819ceccae0f8cacd2a44af5ad2e), [b/218286829](https://issuetracker.google.com/issues/218286829))
- Adds Material 3 bottom app bar support ([Ic432a](https://android-review.googlesource.com/#/q/Ic432a12f98ac1db62a8f38f1a02c937e8ed49172))
- `NavigationDrawer` has been renamed to `ModalNavigationDrawer` ([I1807d](https://android-review.googlesource.com/#/q/I1807d3c889c63efa7a569416daaed58d94a3b17a), [b/218286829](https://issuetracker.google.com/issues/218286829))
- Added Material 3 Slider class and tokens ([I1ccee](https://android-review.googlesource.com/#/q/I1ccee0420983203697b724abfda838a32895885b))
- Added Tab implementation, see the documentation for sample usage ([Ie0146](https://android-review.googlesource.com/#/q/Ie0146154fa799787662992b74b6d39e49e669eb1))

**Bug Fixes**

- Fixed an issue where the `TalkBack` screen reader linear navigation selected an empty top app bar title. ([Id4690](https://android-review.googlesource.com/#/q/Id46909e5999c82f0ec7ac702e9d3f7d78263973c))
- Added `IconSize` to `FloatingActionButtonDefaults`. ([Ia71cf](https://android-review.googlesource.com/#/q/Ia71cf97eac903d9cf6b46195145c502122f478b0))
- Bug fix for hidden `AlertDialog` buttons when a long text is added with a `LazyColumn`. ([Ib2cc9](https://android-review.googlesource.com/#/q/Ib2cc936b917bdb64c13fe92820c47482e0b1e200), [b/216663029](https://issuetracker.google.com/issues/216663029))

### Version 1.0.0-alpha05

February 9, 2022

`androidx.compose.material3:material3:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/material3/material3)

**New Features**

Added Material Design 3 components

- Dropdown menu
  - [DropdownMenu](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dropdownmenu), [DropdownMenuItem](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dropdownmenuitem)
- [Cards](https://m3.material.io/components/cards/overview)
  - [Card](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#card), [OutlinedCard](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#outlinedcard), [ElevatedCard](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#elevatedcard)

**API Changes**

- Deprecated `Surface` function that takes an onClick callback. Clickable surfaces should be created with an `InteractionSource` and a `Modifier.clickable()`. ([I211c6](https://android-review.googlesource.com/#/q/I211c691cf894c2c3cc6a4fbc60983a7bcb608cd4))
- Added pressed and focused elevation support for FAB. ([Ibb584](https://android-review.googlesource.com/#/q/Ibb58423650a4765994c13db4743a666db9fcfe1c))
- Changed the `Surface` API to receive an InteractionSource which allows controlling its appearance in different states. ([Iafbc8](https://android-review.googlesource.com/#/q/Iafbc81a22ad4c1bf36d20ff34e081209f668a8e7))

**Bug Fixes**

- Added missing tertiary colors in dynamic color schemes ([I456c4](https://android-review.googlesource.com/#/q/I456c4ebaa493451db1020cd30536f5dc1bea6e05), [b/214588434](https://issuetracker.google.com/issues/214588434))

### Version 1.0.0-alpha04

January 26, 2022

`androidx.compose.material3:material3:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/material3/material3)

**API Changes**

- Added `NonRestartableComposable` to methods that are overloads of existing methods without complex logic. This reduces compiler generated memoization checks (equals) for all parameters which are repeated in the inner function that is called. ([I90490](https://android-review.googlesource.com/#/q/I90490b1a28bada20840ab59e47245c00c6253d11))
- Added Material 3 divider. ([Ica5fc](https://android-review.googlesource.com/#/q/Ica5fc42b0d81b0443e99367a97628efc6053da90))
- Mark the Checkbox and RadioButton with an experimental API annotation. ([Ie44bb](https://android-review.googlesource.com/#/q/Ie44bbc92b214e8f55414ae46dcf6f9286c8531e8))
- Added support for Material 3 progress indicators. ([Iff232](https://android-review.googlesource.com/#/q/Iff232ace50948f646ca8e7586343dba163628418), [b/205023841](https://issuetracker.google.com/issues/205023841))

**Bug Fixes**

- Update a disabled `TextButton's` container color to be transparent ([I6b248](https://android-review.googlesource.com/#/q/I6b2483a1bc2d1964af3e7b61602a1161bbd92b90), [b/213339737](https://issuetracker.google.com/issues/213339737))

### Version 1.0.0-alpha03

January 12, 2022

`androidx.compose.material3:material3:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/material3/material3)

**Bug Fixes**

- Add `LocalIndication` to Material 3's `MaterialTheme`. ([I7ce4e](https://android-review.googlesource.com/#/q/I7ce4e5c232d16bd8991a2c3d26eb53c30edc9448))
- Fix the corner radius that is applied for Checkboxes ([I38b03](https://android-review.googlesource.com/#/q/I38b03cda11bf28245a3af3d726ddd0bb9cbe8fa6), [b/175198975](https://issuetracker.google.com/issues/175198975), [b/202309440](https://issuetracker.google.com/issues/202309440))

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

### Version 1.0.0-alpha02

December 1, 2021

`androidx.compose.material3:material3:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9aadd5bc6f9a252350ef0f107d0f3b14ea653028..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/material3/material3)

**New Features**

- Add support for checkbox and radiobutton.
- Updated to be compatible with Kotlin `1.6.0`

**API Changes**

- Remove drawer from Material 3's scaffold. ([I04f51](https://android-review.googlesource.com/#/q/I04f51fd532e4c4e3f43928a14407af5bae72514c))
- Adds Material 3 `Checkbox` support. ([Id5542](https://android-review.googlesource.com/#/q/Id55427028a18e4d72fea288413a2bc2eb8a148d6))
- Adds Material 3 `RadioButton` support. ([I20334](https://android-review.googlesource.com/#/q/I20334d6768b9c335047006ddb7b8cdca4e11133b))

**Bug Fixes**

- Reduce `IconButton` ripple radius from 40dp to 20dp. ([I68bbe](https://android-review.googlesource.com/#/q/I68bbe3303f412d17dcc2b2836b30005acae9cc75), [b/206674345](https://issuetracker.google.com/issues/206674345))
- Port string fast path for `Text` changes from `compose.material` ([I30b03](https://android-review.googlesource.com/#/q/I30b0334952793d44f811e8df63096811b0b164ee))
- Fixed but that hardcoded button to always be enabled. ([Iea832](https://android-review.googlesource.com/#/q/Iea83268475294e78cb91b5da802d11ab4a7a6f3a), [b/205335456](https://issuetracker.google.com/issues/205335456))

### Version 1.0.0-alpha01

October 27, 2021

`androidx.compose.material3:material3:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9aadd5bc6f9a252350ef0f107d0f3b14ea653028/compose/material3/material3)

**New Features**

Material Design 3 theming and Material You dynamic color

- [`MaterialTheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#materialtheme)
- [Color](https://m3.material.io/styles/color/overview)
  - [`ColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme)
  - [`lightColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#lightcolorscheme), [`darkColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#darkcolorscheme)
- [Dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)
  - [`dynamicLightColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamiclightcolorscheme), [`dynamicDarkColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#dynamicdarkcolorscheme)
- [Typography](https://m3.material.io/styles/typography/overview)
  - [`Typography`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography)

Material Design 3 components

- [Buttons](https://m3.material.io/components/buttons/overview)
  - [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#button), [`ElevatedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#elevatedbutton), [`FilledTonalButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#filledtonalbutton), [`OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#outlinedbutton), [`TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#textbutton)
- [FAB](https://m3.material.io/components/floating-action-button/overview) and [extended FAB](https://m3.material.io/components/extended-fab/overview)
  - [`SmallFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#smallfloatingactionbutton), [`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#floatingactionbutton), [`LargeFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#largefloatingactionbutton), [`ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#extendedfloatingactionbutton)
- [Dialogs](https://m3.material.io/components/dialogs/overview)
  - [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#alertdialog)
- [Navigation bar](https://m3.material.io/components/navigation-bar/overview)
  - [`NavigationBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationbar)
- [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview)
  - [`NavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationdrawer)
- [Navigation rail](https://m3.material.io/components/navigation-rail/overview)
  - [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- [Top app bar](https://m3.material.io/components/top-app-bar/overview)
  - [`SmallTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#smalltopappbar), [`CenterAlignedTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#centeralignedtopappbar), [`MediumTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#mediumtopappbar), [`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#largetopappbar)
- Badge
  - [`Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#badge), [`BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#badgedbox)
- Icon
  - [`Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#icon), [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#iconbutton)
- Text
  - [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#text)
- Surface
  - [`Surface`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#surface)
- Layout
  - [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#scaffold)
- Content color
  - [`LocalContentColor`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LocalContentColor())

For more information, check out the [Material Design 3 and Material You](https://developer.android.com/jetpack/compose/themes/material#material3) section in the Material Theming in Compose guide.