---
title: https://developer.android.com/jetpack/androidx/releases/xr-compose-material3
url: https://developer.android.com/jetpack/androidx/releases/xr-compose-material3
source: md.txt
---

# Material Design for XR

[User Guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design)  
API Reference  
[androidx.xr.compose.material3](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary)  
Build with Material components and layouts that adapt for XR  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | - | - | - | [1.0.0-alpha14](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3#1.0.0-alpha14) |

## Declaring dependencies

To add a dependency on XR Compose Material3 core, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement XR Compose Material3
    implementation "androidx.xr.compose.material3:material3:1.0.0-alpha14"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement XR Compose Material3
   implementation("androidx.xr.compose.material3:material3:1.0.0-alpha14")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1689595+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1689595&template=2070827)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha14

January 28, 2026

`androidx.xr.compose.material3:material3:1.0.0-alpha14` is released. Version 1.0.0-alpha14 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..715e22619094effc2ba1fd528cd9a07b1f5d0046/xr/compose/material3/material3).

### Version 1.0.0-alpha13

December 03, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha13` is released. Version 1.0.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..deb96499dfe95073f5c1215c1287787683cb1e92/xr/compose/material3/material3).

**New Features**

- Create XR implementation and `ComponentOverride` for `WideNavigationRail` and `ModalWideNavigationRail` ([I1e86d](https://android-review.googlesource.com/#/q/I1e86dfdd8c733c0108d8c96499b60c57ab5ea5d9), [b/407769444](https://issuetracker.google.com/issues/407769444))
- `NavigationSuiteScaffold`, `ListDetailPaneScaffold`, and `SupportingPaneScaffold` now use `recommendedContentBoxInFullSpace` to set their default sizes ([Ic54f1](https://android-review.googlesource.com/#/q/Ic54f1855d639c552742e419c9d4779ced507cb6b), [b/388111668](https://issuetracker.google.com/issues/388111668), [b/394913962](https://issuetracker.google.com/issues/394913962), [b/394913962](https://issuetracker.google.com/issues/394913962))

### Version 1.0.0-alpha12

October 22, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/xr/compose/material3/material3).

**New Features**

- Added `SpaceModeToggleButton` for switching between `HomeSpace` and `FullSpace` ([Ic6865](https://android-review.googlesource.com/#/q/Ic6865b7d30281b44a4b1161eeb672bf862486e6d))

**Bug Fixes**

- Improve XR Toolbars ([Ied1f5](https://android-review.googlesource.com/#/q/Ied1f5b80fde287732cf0b91c3286b7cc12d67aaf))

### Version 1.0.0-alpha11

August 27, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/xr/compose/material3/material3).

**Bug Fixes**

- Fix behavior of FAB in XR NavRail ([Ibe20b](https://android-review.googlesource.com/#/q/Ibe20be29adcdfd365ec99decae390f53eced2b0c))

### Version 1.0.0-alpha10

July 30, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..5fa9d0954ece0376736164b0f7bc2ef33506ab70/xr/compose/material3/material3).

**New Features**

- Create XR implementation and `ComponentOverride` for Horizontal and Vertical Toolbar ([0e9496c](https://android.googlesource.com/platform/frameworks/support/+/0e9496c5c35f4747ccb629f053b1999efc3f3f98), [dcfef96](https://android.googlesource.com/platform/frameworks/support/+/dcfef96117b9c969aef92250650ee9b3137340f9))

**Bug Fixes**

- Fix XR dialog not showing some content ([c82e61b](https://android.googlesource.com/platform/frameworks/support/+/c82e61be5a39a988d4c96643587b0ba832d1edfd))

### Version 1.0.0-alpha08

May 20, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/xr/compose/material3/material3).

**Bug Fixes**

- Fix crash when `ListDetailPaneScaffold` or `SupportingPaneScaffold` has no children ([46df990](https://android.googlesource.com/platform/frameworks/support/+/46df9907128cffc5d20dfb9e86d9771f773e2705))
- Lower Material XR minSdk to 24 ([6064706](https://android.googlesource.com/platform/frameworks/support/+/6064706950c8ee3c66c55e58ae3b1478cfccd9e6))

### Version 1.0.0-alpha07

May 7, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a767811381d88baed6503d9aa2bd8defbd849351..b6c541571b9fb5471f965fc52612cb280713e5e4/xr/compose/material3/material3).
| **Note:** You'll need Android Emulator version 35.6.7 or later to use this version of the library.

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.0.0-alpha06

March 26, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..a767811381d88baed6503d9aa2bd8defbd849351/xr/compose/material3/material3).

### Version 1.0.0-alpha05

March 12, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/xr/compose/material3/material3).

**New Features**

- `TopAppBar` is spatialized into an Orbiter by default when using `EnableXrComponentOverrides`.
- Material `AlertDialog` is spatialized into a `SpatialPanel` by default when using `EnableXrComponentOverrides`.

**API Changes**

- Rename `ComponentOverride` types to `Override`, and `ComponentOverrideContext` types to `OverrideScope` ([Id973c](https://android-review.googlesource.com/#/q/Id973c0d2fd806e8d5f53375690e0e487afb7fd91))

**Bug Fixes**

- Fix aliasing and incorrect scrimming on spatialized `NavigationRail` and `NavigationBar`. ([I9db52](https://android-review.googlesource.com/#/q/I9db52f98f921b5a25d6e7a841bd4495c512c750c))

### Version 1.0.0-alpha04

February 26, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/12f38ed3744a6cb1592cbc6d053dc2adb328f142..fd7408b73d9aac0f18431c22580d9ab612278b1e/xr/compose/material3/material3).

**New Features**

- `ListDetailPaneScaffold` and `SupportingPaneScaffold` use `SpatialPanels` by default when using `EnableXrComponentOverrides` ([I166b0](https://android-review.googlesource.com/#/q/I166b04e5039887ac1ab6d84d0b235445b6bf1b9c))

**API Changes**

- `DefaultNavigationRailOrbiterProperties` and `DefaultNavigationBarOrbiterProperties` getters are no longer`@Composable` ([I61618](https://android-review.googlesource.com/#/q/I616188e8dbdf9c0ace4cb7d393249b14c4d1fff8))
- `LocalNavigationRailOrbiterProperties` and `LocalNavigationBarOrbiterProperties` are no longer nullable ([I61618](https://android-review.googlesource.com/#/q/I616188e8dbdf9c0ace4cb7d393249b14c4d1fff8))

### Version 1.0.0-alpha03

February 12, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha03` is released with no notable changes since the last alpha. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82aef93384cbb5515cac6b2380d567d813e47308..12f38ed3744a6cb1592cbc6d053dc2adb328f142/xr/compose/material3/material3).

### Version 1.0.0-alpha02

January 29, 2025

`androidx.xr.compose.material3:material3:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e2e2729abc59df52d40af80a8bbfe010c02455c6..82aef93384cbb5515cac6b2380d567d813e47308/xr/compose/material3/material3).

**New Features**

- Enable customization of `Orbiter` properties on XR `NavigationBar` and `NavigationRail`. ([Ic300f](https://android-review.googlesource.com/#/q/Ic300f3b6640d4b7d357835f69c349d0dfd71de92))

**API Changes**

- Create ability to override `ThreePaneScaffold` on XR ([Ib66f1](https://android-review.googlesource.com/#/q/Ib66f1e183ea54d81d5c0a7a1a2a30f0ff93481e9))
- Implement non-animated Pane override for XR ([I7f620](https://android-review.googlesource.com/#/q/I7f620ecf9c734801b44dcc753618bb88855d2ba2))
- Add and use new experimental annotation `ExperimentalMaterial3ComponentOverrideApi` ([Ia1eaf](https://android-review.googlesource.com/#/q/Ia1eaf5578ad029fc94c5aee60146e6aebc36ca2a))

**Bug Fixes**

- Pin Material3 XR's dependency on XR Compose. ([Ia02cc](https://android-review.googlesource.com/#/q/Ia02ccefbc8408e7bcbb08fd61cb7b0f8dd136a80))

### Version 1.0.0-alpha01

December 12, 2024

`androidx.xr.compose.material3:material3:1.0.0-alpha01` is released.

**Features of Initial Release**

Initial developer release of Material Design for XR. Using the existing Material 3 library, components and adaptive layouts are enhanced with spatial UI behaviors. You can build directly with M3 XR components, or adapt your current implementation by adding the `EnableXrComponentOverrides` wrapper. Learn more in this [developer guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design).

Supported XR adaptations:

- Navigation rail in any Compose layout, including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation) will automatically adapt to XR Orbiter. For more information, read [Material Design guidelines](https://m3.material.io/components/navigation-rail/xr).

- Navigation bar in any Compose layout, including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation) will automatically adapt to XR Orbiter. For more information, read [Material Design guidelines](https://m3.material.io/components/navigation-bar/xr).

**Known Issues**

- ListDetailPaneScaffold and SupportingPaneScaffold currently don't support multiple spatial panels