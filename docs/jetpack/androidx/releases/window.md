---
title: https://developer.android.com/jetpack/androidx/releases/window
url: https://developer.android.com/jetpack/androidx/releases/window
source: md.txt
---

# WindowManager

<br />

# WindowManager

[Code Sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/windowmanager)[Codelab](https://developer.android.com/codelabs/android-window-manager-dual-screen-foldables)  
API Reference  
[androidx.window](https://developer.android.com/reference/kotlin/androidx/window/package-summary)  
[androidx.window.core](https://developer.android.com/reference/kotlin/androidx/window/core/package-summary)  
[androidx.window.embedding](https://developer.android.com/reference/kotlin/androidx/window/embedding/package-summary)  
[androidx.window.layout](https://developer.android.com/reference/kotlin/androidx/window/layout/package-summary)  
[androidx.window.testing.layout](https://developer.android.com/reference/kotlin/androidx/window/testing/layout/package-summary)  
The Jetpack WindowManager library enables application developers to support new device form factors and multi-window environments. The initial release targets foldable devices, but future versions will extend to more display types and window features.  

|   Latest Update   |                                Stable Release                                 | Release Candidate | Beta Release |                                         Alpha Release                                         |
|-------------------|-------------------------------------------------------------------------------|-------------------|--------------|-----------------------------------------------------------------------------------------------|
| November 19, 2025 | [1.5.1](https://developer.android.com/jetpack/androidx/releases/window#1.5.1) | -                 | -            | [1.6.0-alpha01](https://developer.android.com/jetpack/androidx/releases/window#1.6.0-alpha01) |

## Declaring dependencies

To add a dependency on WindowManager, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.window:window:1.5.1"

    // For Java-friendly APIs to register and unregister callbacks
    implementation "androidx.window:window-java:1.5.1"

    // For RxJava2 integration
    implementation "androidx.window:window-rxjava2:1.5.1"

    // For RxJava3 integration
    implementation "androidx.window:window-rxjava3:1.5.1"

    // For testing
    implementation "androidx.window:window-testing:1.5.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.window:window:1.5.1")

    // For Java-friendly APIs to register and unregister callbacks
    implementation("androidx.window:window-java:1.5.1")

    // For RxJava2 integration
    implementation("androidx.window:window-rxjava2:1.5.1")

    // For RxJava3 integration
    implementation("androidx.window:window-rxjava3:1.5.1")

    // For testing
    implementation("androidx.window:window-testing:1.5.1")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:840395+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=840395&template=1412556)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

<br />

## Version 1.6

### Version 1.6.0-alpha01

November 19, 2025

`androidx.window:window-*:1.6.0-alpha01`is released. Version 1.6.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3b3f055fe2da3f4a8a74003f8640b461b1694954..4d752a0684fb1bf991cd0d15ebd3649ee8684ca1/window).

**New Features**

- Add helper methods to construct`WindowSizeClassSets`in a grid form.

**API Changes**

- Add helper methods to construct`WindowSizeClassSets`in a grid form. ([I4d623](https://android-review.googlesource.com/#/q/I4d6236961e51ed10b3007941bb777401edaabc39),[b/444174274](https://issuetracker.google.com/issues/444174274))

## Version 1.5

### Version 1.5.1

November 19, 2025

`androidx.window:window-*:1.5.1`is released. Version 1.5.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3b3f055fe2da3f4a8a74003f8640b461b1694954..be8b763fe78ab805aa1c9a3bff09f1ff8081dbb2/window).

**Bug Fixes**

- Fixes`ClassCastException`that occurs on certain devices ([4d58979](https://android.googlesource.com/platform/frameworks/support/+/4d5897960201a8713f0f77e0dbd4b0ec2009fff7))

### Version 1.5.0

September 24, 2025

`androidx.window:window-*:1.5.0`is released. Version 1.5.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5a28662498502deafcf9966ecb43f1d6577f9713..3b3f055fe2da3f4a8a74003f8640b461b1694954/window).

**Important changes since 1.4.0:**

- Add`WindowSizeClass`breakpoints for Large and XLarge. ([I40d85](https://android-review.googlesource.com/#/q/I40d8512af8fee0ee21c3c3f4c3baa9fba9e9b94f))
- Expand calculating`WindowMetrics`to Application Context. ([I8eeeb](https://android-review.googlesource.com/#/q/I8eeeb2a6d24f0367dcfd56e7e70dbcf2afbbccc5),[b/360934048](https://issuetracker.google.com/issues/360934048))
- Provider a Getter to enable direct access to`WindowLayoutInfo`([Ie9513](https://android-review.googlesource.com/#/q/Ie95132208f8964dc046d2cb113c3dab4c7420be7))
- Introduce API to auto save embedding state and to auto restore the embedding state when the app process is restarted. ([Ie0295](https://android-review.googlesource.com/#/q/Ie0295d42ff2f0eed72d2d9eac63ee6a65cf6f937))
- Remove experimental`WindowInsets`API. ([I68a71](https://android-review.googlesource.com/#/q/I68a71eac60861d081cb6300380cb1099e3fbec37))

**Bug Fixes**

- Fixes`EmbeddingRule`returning different`hashCode`in some cases. ([I748cc](https://android-review.googlesource.com/#/q/I748cccf243a521b672be725dd8ac1508341fce3d))
- Fix for where a`NullPointerException`could occur due to errors on the device implementation.
- Fix for where our`ActivityEmbedding`safety checks would fail due to proguard removing unused classes.

**External Contribution**

- Add all KMP platforms to`window-core`([If3d7c](https://android-review.googlesource.com/#/q/If3d7ce3195d6ea4eb001cd32fd41481f2374f44b))

### Version 1.5.0-rc01

August 27, 2025

`androidx.window:window-*:1.5.0-rc01`is released. Version 1.5.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..5a28662498502deafcf9966ecb43f1d6577f9713/window).

**Bug Fixes**

- Fix for where a`NullPointerException`could occur due to errors on the device implementation.
- Fix for where our`ActivityEmbedding`safety checks would fail due to proguard removing unused classes.

### Version 1.5.0-beta02

August 13, 2025

`androidx.window:window-*:1.5.0-beta02`is released. Version 1.5.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..c359e97fece91f3767a7d017e9def23c7caf1f53/window).

**New Features**

- Minor bug fixes.

**External Contribution**

- Add all KMP platforms to`window-core`([If3d7c](https://android-review.googlesource.com/#/q/If3d7ce3195d6ea4eb001cd32fd41481f2374f44b))

### Version 1.5.0-beta01

July 2, 2025

`androidx.window:window-*:1.5.0-beta01`is released. Version 1.5.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..1b437892629a2cdedb46d9b7232575987b2cc6b5/window).

### Version 1.5.0-alpha02

May 7, 2025

`androidx.window:window-*:1.5.0-alpha02`is released. Version 1.5.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..b6c541571b9fb5471f965fc52612cb280713e5e4/window).

**API Changes**

- Add`WindowSizeClass`breakpoints for Large and XLarge. ([I40d85](https://android-review.googlesource.com/#/q/I40d8512af8fee0ee21c3c3f4c3baa9fba9e9b94f))
- Expand calculating`WindowMetrics`to Application Context. ([I8eeeb](https://android-review.googlesource.com/#/q/I8eeeb2a6d24f0367dcfd56e7e70dbcf2afbbccc5),[b/360934048](https://issuetracker.google.com/issues/360934048))
- Provider a Getter to enable direct access to`WindowLayoutInfo`([Ie9513](https://android-review.googlesource.com/#/q/Ie95132208f8964dc046d2cb113c3dab4c7420be7))
- Introduce API to auto save embedding state and to auto restore the embedding state when the app process is restarted. ([Ie0295](https://android-review.googlesource.com/#/q/Ie0295d42ff2f0eed72d2d9eac63ee6a65cf6f937))
- Remove experimental`WindowInsets`API. ([I68a71](https://android-review.googlesource.com/#/q/I68a71eac60861d081cb6300380cb1099e3fbec37))
- Hide a few constructors ([I87b8d](https://android-review.googlesource.com/#/q/I87b8d3d40d4b0e35c155ef6464a43aa1e8698702))

**Bug Fixes**

- Fixes`EmbeddingRule`returning different`hashCode`in some cases. ([I748cc](https://android-review.googlesource.com/#/q/I748cccf243a521b672be725dd8ac1508341fce3d))

### Version 1.5.0-alpha01

March 12, 2025

`androidx.window:window-*:1.5.0-alpha01`is released. Version 1.5.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870/window).

**New Features**

- Initial release of next 1.5.0.

## Version 1.4

### Version 1.4.0

May 20, 2025

`androidx.window:window-*:1.4.0`is released. Version 1.4.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/375ebde0315cbc409d193849911f3cf034a0a0dc..29ad8af1341fb670b083b88ebb5a611f1d1c6cc1/window).

**Important changes since 1.3.0**

- Activity Embedding
  - API to customize the launch animations
  - Interactive Divider
  - `ActivityStack`Pinning
  - Full Screen Dialog Dimming
  - Embedded Activity Window Info Callback
  - Improved`ActivityStack`Management
  - Launch Activity into a specified`ActivityStack`
- `WindowMetricsCalculator`
  - Improve testability support
- `WindowMetrics`
  - Convenience methods to calculate`withDp`and`heightDp`
  - Update bounds check to`isAtLeast`and use lower bounds to support adding new values
- `WindowSizeClass`
  - Add way to calculate from`WindowMetrics`
- `WindowInfoTracker`
  - Add API to detect the supported postures on the device

### Version 1.4.0-rc02

April 23, 2025

`androidx.window:window-*:1.4.0-rc02`is released. Version 1.4.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/bb3bb5854c0e0cedac67e11b0bc81c6fb09c741a..375ebde0315cbc409d193849911f3cf034a0a0dc/window).

**Bug Fixes**

- Fix a proguard crash for`ActivityEmbedding`.

### Version 1.4.0-rc01

March 12, 2025

`androidx.window:window-*:1.4.0-rc01`is released. Version 1.4.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..bb3bb5854c0e0cedac67e11b0bc81c6fb09c741a/window).

**New Features**

- Updates to the`WindowSizeClass`API.
- Updates to Activity Embedding APIs.

### Version 1.4.0-beta02

February 12, 2025

`androidx.window:window-*:1.4.0-beta02`is released. Version 1.4.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/window).

**New Features**

- Fix an annotation that was only on the property but not the getter.

### Version 1.4.0-beta01

January 15, 2025

`androidx.window:window-*:1.4.0-beta01`is released. Version 1.4.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ad66672b42ec1e9359219e82b7f8189d03df40f5/window).

**New Features**

- Add API to allow customizing`ActivityEmbedding`Animations.
- Expand`WindowMetricsCalculator`test APIs to allow faking the window metrics.

**API Changes**

- Hide a few constructors ([I87b8d](https://android-review.googlesource.com/#/q/I87b8d3d40d4b0e35c155ef6464a43aa1e8698702))
- Allow apps to customize`ActivityEmbedding`animations ([If31a8](https://android-review.googlesource.com/#/q/If31a8c9791e6e3824734d07d550ccc12001401f7))
- Adds support for`watchosDeviceArm64`KMP target and target kotlin 1.9 ([Icf15d](https://android-review.googlesource.com/#/q/Icf15d056ce2380ca3c733fb1a93fd502f60b40e4),[b/364652024](https://issuetracker.google.com/issues/364652024))
- Expose`WindowMetricsCalculator`APIs. ([I1cebf](https://android-review.googlesource.com/#/q/I1cebf90b301e6e9384d4df734dd687f29e39521c))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ie69ac](https://android-review.googlesource.com/#/q/Ie69ac5b2d25846963fd1b310663d9356eabe8251),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.4.0-alpha05

October 16, 2024

`androidx.window:window-*:1.4.0-alpha05`is released. Version 1.4.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/window).

**New Features**

- Add convenience functions to get the`widthDp`and`heightDp`from`WindowMetrics`.

**API Changes**

- Add`widthDp`and`heightDp`to`WindowMetrics`. ([Ide026](https://android-review.googlesource.com/#/q/Ide026a09aade8cbb8af9e042014c88cbbb309335))
- Remove experimental`WindowInsets`API. ([I68a71](https://android-review.googlesource.com/#/q/I68a71eac60861d081cb6300380cb1099e3fbec37))
- Update bounds check method names to`isAtLeast`([Ib0ab7](https://android-review.googlesource.com/#/q/Ib0ab7ae94584f8a11e4c34b8cb8b29ca34c52cb8))

### Version 1.4.0-alpha04

October 2, 2024

`androidx.window:window-*:1.4.0-alpha04`is released. Version 1.4.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cb8fe0a26f0e27cf7f9239f308a1d34a0146bc66..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/window).

**API Changes**

- Added a method to compute the`WindowSizeClass`from`WindowMetrics`. ([874dba](https://android.googlesource.com/platform/frameworks/support/+/874dba6e900ea46c31dec4ea448f5eb8123c513d))
- Change the`WindowSizeClass`methods to`containsWidthDp`,`containsHeightDp`, and`containsWindowSizeDp`for clarity. ([fa760d](https://android.googlesource.com/platform/frameworks/support/+/fa760ddce6f309471c5687bcd68cdf75be23e0f0))
- Convert`WindowAreaController`to abstract base class. ([I90893](https://android-review.googlesource.com/#/q/I9089333b0a810881ed409ccfa16783a358e9766e))

**Bug Fixes**

- Add support for relative bounds when creating a test`FoldingFeature`. ([2e6b3e](https://android.googlesource.com/platform/frameworks/support/+/2e6b3e6cb7eccb7bcf79b232c5dc355466af9bec))
- General bug fixes when selecting a`WindowSizeClass`.

### Version 1.4.0-alpha03

September 18, 2024

`androidx.window:window-*:1.4.0-alpha03`is released. Version 1.4.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f1a4862ceeaaa0161261ad24ea72a5430d3090d0..0431b84980e97d6bafdfda7c9038bc4d9529564f/window).

**New Features**

- Add a utility method to get a`WindowSizeClass`from`WindowMetrics`. ([I83f1f](https://android-review.googlesource.com/#/q/I83f1fb0faa8c28c212dec7b6f1628c0fa4a7e736))
- Rename`isAtLeast`to`containsBreakpoint`. ([I85b47](https://android-review.googlesource.com/#/q/I85b47cd3fd17000e9c8a35af4dc6b4e315b73a5d))
- Add overload to`computeWindowSizeClass`using floats. ([I3dcb2](https://android-review.googlesource.com/#/q/I3dcb254105a286b2edaa38f7be453be024a0a7e4),[b/364677934](https://issuetracker.google.com/issues/364677934),[b/364677802](https://issuetracker.google.com/issues/364677802),[b/364680886](https://issuetracker.google.com/issues/364680886))

**Bug Fixes**

- Add missing breakpoints to the default`WindowSizeClass`breakpoint set.
- Fixed a bug where compact dimensions were not being selected correctly in some cases.

### Version 1.4.0-alpha02

September 4, 2024

`androidx.window:window-*:1.4.0-alpha02`is released. Version 1.4.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..cb8fe0a26f0e27cf7f9239f308a1d34a0146bc66/window).

**New Features**

Add support for custom`WindowSizeClass`.

- Open the constructor for`WindowSizeClass`so devs can use their own.
- Add`isAtLeast`utility methods so that developers can process a range of`WindowSizeClass`values.
- Add an extension function on`Set<WindowSizeClass>`to compute the best match from the Set.
- Add constants for the Android recommended breakpoints.
- Add the breakpoint set corresponding to the Android recommended breakpoints.

**API Changes**

- Update bounds method names for`WindowSizeClass`. ([If89a6](https://android-review.googlesource.com/#/q/If89a645d13a20168a2a9af6febf50a21a1012b9a))
- Update the`WindowSizeClass`API to support adding new breakpoint values in the future. Instead of having absolute bounds we use the lower bounds and recommend devs use lower bound checks when processing a`WindowSizeClass`. The existing`WindowWidthSizeClass`and`WindowHeightSizeClass`will be deprecated as they will not be developed further. ([I014ce](https://android-review.googlesource.com/#/q/I014cef212823dc5dfa8bb430fdbe0b505f0b81ff))

### Version 1.4.0-alpha01

August 7, 2024

`androidx.window:window-*:1.4.0-alpha01`is released. Version 1.4.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c50bbb6627cd345df69ae3c3e7f4a133dec7fe48..9130b719318a69f2f3eaf82c32b131232fd721cb/window).

**New Features**

- **ActivityStack Pinning**allows apps to pin the content in one container and have its navigation isolated from the other container.
- **Interactive Divider**allows apps to display a fixed or draggable divider between the two activities in a split presentation.
- **Fullscreen Dialog Dimming**allows apps to specify the dialog dim area, to either dim the entire task window or only dim the container that shows the dialog.
- **Embedded Activity Window Info Callback**allows apps to continuously receive updates of the embedded activity window.
- **Embedding Animation Background** allows apps to specify the animation background, improving the transition animation quality when`ActivityEmbedding`is used.
- **Improved ActivityStack Management** allows apps to have more control over the`ActivityStacks`when`ActivityEmbedding`is used, including:
- Launching an activity into a specified`ActivityStack`
- Finishing an`ActivityStack`

**API Changes**

- A new API`WindowInfoTracker#supportedPostures`:

  - An API to determine if the device supports TableTop mode for foldables. Adds WindowAreaSessionPresenter#getWindow
- Add APIs to support`ActivityStack`pinning:

  - `SplitPinRule`class
  - `SplitController#pinTopActivityStack`
  - `SplitController#unpinTopActivityStack`
- Add APIs to enable and configure the interactive divider

  - `DividerAttributes`class
  - `SplitAttributes.Builder#setDividerAttributes`
- Add APIs to set`EmbeddingConfiguration`and`DimAreaBehavior`for dialogs

  - `EmbeddingConfiguration`class
  - `DimAreaBehavior`class
  - `ActivityEmbeddingController#setEmbeddingConfiguration`
- Add APIs to receive embedded activity window info updates

  - `EmbeddedActivityWindowInfo`class
  - `ActivityEmbeddingController#embeddedActivityWindowInfo`
- Add APIs to set embedding animation background

  - `EmbeddingAnimationBackground`
  - `SplitAttributes.Builder#setAnimationBackground`
- Add APIs to finish`ActivityStacks`

  - `ActivityEmbeddingController#finishActivityStacks`
- Add APIs to set launching`ActivityStack`

  - `ActivityEmbeddingOptions#setLaunchingActivityStack`
- The following APIs are stable and no longer experimental:

  - `ActivityEmbeddingController#invalidateVisibleActivityStacks`(moved from SplitController#invalidateTopVisibleSplitAttributes)
  - `ActivityEmbeddingController#getActivityStack`
  - `SplitController#updateSplitAttributes`
- Add APIs for 1.4. ([I56774](https://android-review.googlesource.com/#/q/I567747b6a039b2c00183107a301842db3b6d77f4))

**Bug Fixes**

- Fixes bug on certain devices where UNAVAILABLE would be returned instead of ACTIVE when a session is active.
- Removes support for`transferActivityToWindowArea`on devices with a`vendorApiLevel`of 2 due to unstable API support.
- Introduce API to enable drag-to-fullscreen for Activity Embedding draggable divider. ([I645c9](https://android-review.googlesource.com/#/q/I645c92453fed1f59d20a8f2e9bb3df7118576511))
- Allow apps to disable`ActivityEmbedding`animations via animation params for`SplitAttributes`. ([Idc01a](https://android-review.googlesource.com/#/q/Idc01a0d4a13321f8de21806693b67ebdeb283fc2))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8),[b/345472586](https://issuetracker.google.com/issues/345472586))
- Allow extensions to take animation params for`SplitAttributes`so that the device can use it for animation transitions. ([Iede00](https://android-review.googlesource.com/#/q/Iede006641fa40fe036cb1eb3c2a858a194b80f05))
- Hide overlay APIs ([Ic4251](https://android-review.googlesource.com/#/q/Ic4251735cb5869a2152c2389af350288d9f74710))
- Introduce APIs to configure the fixed or draggable divider for the split ([Ia7a78](https://android-review.googlesource.com/#/q/Ia7a78dd767ea32edc4c8971b61bc136c16214c4f))
- Added density to`WindowMetrics`([Id6723](https://android-review.googlesource.com/#/q/Id6723149c9ba7f3aa924ef53f0ae9a21e5f8c7c8))
- Add API to get the`SupportedPostures`. ([If557a](https://android-review.googlesource.com/#/q/If557a7c17ae8f3473f1ab81520038848c11f775c))
- Remove`setLaunchingActivityStack`from experimental API ([I191cf](https://android-review.googlesource.com/#/q/I191cf1aaa2e94724a9f82bea3d178a2889178319))
- Introduce`ActivityEmbeddingController#embeddedActivityWindowInfo`([I24312](https://android-review.googlesource.com/#/q/I243121796a50d3c96e4852dbf83aa1f5cc1eea6e))
- Deprecate`#getToken`and add`#getActivityStackToken`([Ie0471](https://android-review.googlesource.com/#/q/Ie047116259409389ae6c544929f50a6a8114774a))
- Introduce callback adapter for`embeddedActivityWindowInfo`flow API ([Ida77f](https://android-review.googlesource.com/#/q/Ida77f3109a0bf624c445162834d7e2019d0bf601))
- Add callback adapter for overlayInfo flow API ([I7264f](https://android-review.googlesource.com/#/q/I7264f347c5ceaf44ed65335c573d67fd2300b3d8))
- Introduce`WindowSdkExtensionsRule`to override`extensionsVersion`for testing. ([Ifb928](https://android-review.googlesource.com/#/q/Ifb9285d4851195d02895bd510d7a8a32aa91057c))
- - Migrate`#setLaunchingActivityStack`to Bundle to compat with`ActivityOptionsCompat`usages.
  - Users should pass`activityOptions.toBundle`instead of`ActvityOptions`itself.
  - Remove`#setLaunchingActivityStack(Activity)`. Users should migrate to use`ActivityEmbeddingController#getActivityStac(Activity)`to get an`ActivityStack`, and pass the`ActivityStack`to`#setLaunchingActivityStack`. ([Ie0ccc](https://android-review.googlesource.com/#/q/Ie0ccc35e5459c9031d6890185d6472388eb68320))
- - Introduce`ActivityStack.Token`and`SpltInfo.Token`as an identifier to communicate between WM Jetpack and extensions.
  - Deprecate/Replace APIs to take/return Token instead of IBinder. ([I12b24](https://android-review.googlesource.com/#/q/I12b24006a004e9c361554e21bb9a7564b27da406))
- - Introduce`ActivityEmbeddingController#invalidateVisibleActivityStacks`
  - Remove`SplitController#invalidateTopVisibleSplitAttributes`because the feature is consolidate to`#invalidateVisibleActivityStacks`([I02ef5](https://android-review.googlesource.com/#/q/I02ef5fed3ab71287e23f5bf5ac2b5a124fd2a0ed))
- - Adding API to set embedding configuration. ([I59a4a](https://android-review.googlesource.com/#/q/I59a4a238e0ec3bb207b8ddf7862ca613c1d1cf58))
- - Adding pin/unpin top`ActivityStack``androidx.Window`APIs
  - Updating demo app to allow pin/unpin top`ActivityStack`([I24dd3](https://android-review.googlesource.com/#/q/I24dd34679d9540d9f2b0d6d7fa87635ef9d43155))
- Re-add`#finishActivityStacks`and`ActivityEmbeddingOptions`([Ic1ab3](https://android-review.googlesource.com/#/q/Ic1ab39e9c5a3f9833f8112e847cac7bdf2b27cd8))
- Remove unstable APIs. ([Ibc534](https://android-review.googlesource.com/#/q/Ibc534a8ba5f81f0fdcde569335a581e605d1c69e),[b/302380585](https://issuetracker.google.com/issues/302380585))

## Version 1.3

### Version 1.3.0

May 29, 2024

`androidx.window:window-*:1.3.0`is released. Version 1.3.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0ef82c0673456addf3c611f9081d4d8cbbcf1c62..c50bbb6627cd345df69ae3c3e7f4a133dec7fe48/window).

**Important changes since 1.2.0**

- Kotlin Multiplatform support for Window Size Classes.

### Version 1.3.0-rc01

May 14, 2024

`WindowManager`Jetpack 1.3 brings Kotlin Multiplatform support for`WindowSizeClass`features as well as multiple bug fixes.

`androidx.window:window-*:1.3.0-rc01`is released. Version 1.3.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..0ef82c0673456addf3c611f9081d4d8cbbcf1c62/window).

### Version 1.3.0-beta02

May 1, 2024

`androidx.window:window-*:1.3.0-beta02`is released. Version 1.3.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..fbd1ac175922f44c69a13545d194066ee428b342/window).

**API Changes**

- Remove support for creating and using custom`WindowSizeClass`'s. ([Id1143](https://android-review.googlesource.com/#/q/Id1143662800446f3868a5324a2f647956610a84e))

**Bug Fixes**

- Fixes`KotlinReflectionInternalError`caused by proguard stripping out some files on certain device implementations. ([I01b02](https://android-review.googlesource.com/c/platform/frameworks/support/+/3059406))

### Version 1.3.0-beta01

April 3, 2024

`androidx.window:window-*:1.3.0-beta01`is released. Version 1.3.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..02b55f664eba38e42e362e1af3913be1df552d55/window).

### Version 1.3.0-alpha03

March 6, 2024

`androidx.window:window-*:1.3.0-alpha03`is released. Version 1.3.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/window).

**API Changes**

- Split`WindowSizeClassUtil`into more focused methods. ([Ie9292](https://android-review.googlesource.com/#/q/Ie929241cd5acc56ecf352590f03374f2165b4e31))
- Restore`WindowSizeClass#compute`([I21355](https://android-review.googlesource.com/#/q/I213553e2526ff370b02f9c1a7943252faa918be3),[b/324293374](https://issuetracker.google.com/issues/324293374))

**Bug Fixes**

- Fixes crash where the context provided wasn't being unwrapped correctly. ([94d10ce](https://android-review.googlesource.com/#/q/Id97daf9f78c33aedb73a1e481d7486b00e70af46),[b/318787482](https://issuetracker.google.com/issues/318787482))

### Version 1.3.0-alpha02

February 7, 2024

`androidx.window:window-*:1.3.0-alpha02`is released.[Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..ca2a8cf8da3a3502fccc593974f8085653e38261/window)

**New Features**

- Updates made to the API surface of the Window Size Class API's to improve flexibility for developers who want to use their own size classes.

**API Changes**

- Add height constraints to the width selector. ([I23393](https://android-review.googlesource.com/#/q/I2339319ad7edd567d661cd6e828e16247cf311e1))
- Add utility functions for picking a`WindowSizeClass`from a set. Add experimental scoring functions so developers can write their own selectors. Add a selector extension function to pick the widest`WindowSizeClass`within a given bound. ([I0c944](https://android-review.googlesource.com/#/q/I0c944f0ad6cf4bf4e04886ebbc60b6bde0e6e27d))
- Open the`WindowSizeClass`constructor so custom breakpoints can be added. ([Ic1ff3](https://android-review.googlesource.com/#/q/Ic1ff3f438cc9eacec87fbdb1288f31cf10edf9e0))
- Add convenience function to create size class from width, height, and density. ([If67f4](https://android-review.googlesource.com/#/q/If67f47857f31d412f1007ef5ac734d462b642e2d))

**Bug Fixes**

- Fix exception when float value is truncated to 0. ([272ffac](https://android-review.googlesource.com/#/q/I59fa9997695c03cd68cc82349801edc7450145b1))

### Version 1.3.0-alpha01

November 15, 2023

`androidx.window:window-*:1.3.0-alpha01`is released.[Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c/window)

**New Features**

- Expose experimental window APIs for accessing the rear screen.
- Test APIs for creating a`FoldingFeature`is now stable.
- Test APIs for setting up fake`ActivityEmbedding`values are now stable.
- `WindowLayoutInfoPublisherRule`now reports the override when obtaining a value from a`UiContext`.
- `WindowInfoTracker`reports folding feature data to`UiContext`parameters.
- Expose the Extensions Version on the device.
- `WindowProperties`constants for user per-app overrides:
  - `PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_OVERRIDE`--- Informs the system the app has opted out of the user-facing aspect ratio compatibility override.
  - `PROPERTY_COMPAT_ALLOW_USER_ASPECT_RATIO_FULLSCREEN_OVERRIDE`--- Informs the system the app has opted out of the full-screen option of the user aspect ratio compatibility override settings

## Version 1.2

### Version 1.2.0

November 15, 2023

`androidx.window:window-*:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/06e4d421091d61357319a483cbc0e42ee323eced..773c9e51174927e05d2fb969a9652753345d22d5/window)

**Important changes since 1.1.0**

- Expose experimental window APIs for accessing the rear screen.
- Test APIs for creating a`FoldingFeature`is now stable.
- Test APIs for setting up fake`ActivityEmbedding`values are now stable.
- `WindowLayoutInfoPublisherRule`now reports the override when obtaining a value from a`UiContext`.
- `WindowInfoTracker`reports folding feature data to`UiContext`parameters.
- Expose the Extensions Version on the device.

### Version 1.2.0-rc01

November 1, 2023

`androidx.window:window-*:1.2.0-rc01`is released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..06e4d421091d61357319a483cbc0e42ee323eced/window)

**New Features**

- Expose experimental window APIs for accessing the rear screen.
- Test APIs for creating a`FoldingFeature`is now stable.
- Test APIs for setting up fake`ActivityEmbedding`values are now stable.
- `WindowLayoutInfoPublisherRule`now reports the override when obtaining a value from a`UiContext`.
- `WindowInfoTracker`reports folding feature data to`UiContext`parameters.
- Expose the Extensions Version on the device.

### Version 1.2.0-beta04

October 18, 2023

`androidx.window:window-*:1.2.0-beta04`is released.[Version 1.2.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/window)

**API Changes**

- Remove unstable APIs. ([Ibc534](https://android-review.googlesource.com/#/q/Ibc534a8ba5f81f0fdcde569335a581e605d1c69e),[b/302380585](https://issuetracker.google.com/issues/302380585))

### Version 1.2.0-beta03

September 20, 2023

`androidx.window:window-*:1.2.0-beta03`is released.[Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee513bb6c09a651ba4c537a3d054395349a10ed..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/window)

**New Features**

- Add`RequiresApi`checks for APIs that need a specific version of extensions to function correctly.
- Add an API to expose the extensions version on the device.

**API Changes**

- Annotate required window SDK extension version on public APIs.
  - Remove`isXXXSupported`in the Activity Embedding component. ([Ie3dae](https://android-review.googlesource.com/#/q/Ie3dae75663e9b67b03182d2d60dfc365dff5a1dc))
- Introduce`WindowSdkExtensions`to report the extension version on the device.
  - Introduce`RequiresWindowSdkExtension`to annotate the minimum required extension version. ([I05fd4](https://android-review.googlesource.com/#/q/I05fd41eea44fcdf1dd5f7366677339a09db22b76))
- Makes`WindowAreaInfo#getCapability`non-nullable. ([I17048](https://android-review.googlesource.com/#/q/I17048df0d2fbac0751bab031d9fa38d0eefd00e7))

### Version 1.2.0-beta01

July 26, 2023

`androidx.window:window-*:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..aee513bb6c09a651ba4c537a3d054395349a10ed/window)

**New Features**

- Expose experimental window APIs for accessing the rear screen.
- Test APIs for creating a`FoldingFeature`is now stable.
- Test APIs for setting up fake`ActivityEmbedding`values are now stable.
- `WindowLayoutInfoPublisherRule`now reports the override when obtaining a value from a`UiContext`.
- `WindowInfoTracker`reports folding feature data to`UiContext`parameters.

**API Changes**

- Marks`WindowArea`API's as experimental to allow API changes to continue for a stable release in 1.3 ([I857f5](https://android-review.googlesource.com/#/q/I857f50abe5a893e7c036cffe0e2ff7d4050f6c9c))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b),[b/287516207](https://issuetracker.google.com/issues/287516207))

### Version 1.2.0-alpha03

June 21, 2023

`androidx.window:window-*:1.2.0-alpha03`is released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..3b5b931546a48163444a9eddc533489fcddd7494/window)

**New Features**

- Removing deprecated APIs from the API surface.
- Add APIs to support concurrent displays.
- Add a property to opt out of forced resize override.
- Add property to opt out of min aspect ratio override.
- Stabilize`ActivityEmbeddingRule`to support unit testing around Activity Embedding.

**API Changes**

- Remove deprecated APIs ([I18d39](https://android-review.googlesource.com/#/q/I18d39bf6b92aabbb8a7335a8aef35ab2b6ca81d3))
- Add support for concurrent displays. ([Ifcbb0](https://android-review.googlesource.com/#/q/Ifcbb04c397686ac8d2d1dd833d67ce6e6b6f56ec))

**Bug Fixes**

- Adding opt-out compat property for force resize override ([Ie7ab1](https://android-review.googlesource.com/#/q/Ie7ab1fecfa45b3ef1bc7a62995dd2ef30947154f))
- Removes`SESSION_STATE_CONTENT_INVISIBLE`from extensions interface. ([I6ed19](https://android-review.googlesource.com/#/q/I6ed198517d14371a16ef41c276308403522cacc0))
- Stabilize`ActivityEmbeddingRule`to support unit testing around Activity embedding. ([I8d6b6](https://android-review.googlesource.com/#/q/I8d6b66ee5d79792fb5ef737c0818dbff2f590354))
- Adding opt-out compat property for min aspect ratio override. ([I66390](https://android-review.googlesource.com/#/q/I663907d38aa69ae6fab57fd89a41654673dde4cd))
- Removes deprecated WindowArea API's ([Ieb67c](https://android-review.googlesource.com/#/q/Ieb67c84ff436c0a09d22b9e3f566746e51e777ca))
- Rename orientation request loop property to`PROPERTY_COMPAT_ALLOW_IGNORING_ORIENTATION_REQUEST_WHEN_LOOP_DETECTED`. ([Ie2fbd](https://android-review.googlesource.com/#/q/Ie2fbded0e86b922755f0f916ad1c39c05a247cce))
- Updates window area session constant names ([I83675](https://android-review.googlesource.com/#/q/I8367506c3a871d6bcf59e654967aa5b0b59fedfb))
- Adding opt-out compat property that ignores orientation request loop when detected ([I0a7a2](https://android-review.googlesource.com/#/q/I0a7a2feaaa1bd5eb3b1071dbed038828e444a0ba))
- Add`WindowAreaComponent#STATUS_ACTIVE`to signify that the feature is already active. ([I62bc3](https://android-review.googlesource.com/#/q/I62bc30d1effe5ecd76591beea4e35ba8b225755f))
- Add`RearDisplayPresentationMode`APIs ([I0401c](https://android-review.googlesource.com/#/q/I0401c4abe23a95620e35808000146da11da06faa))
- Remove background color API for stable. ([I34c3e](https://android-review.googlesource.com/#/q/I34c3ecf8bbb63a0229633268c58a67da9dc51642))
- Hide Window Area APIs. ([I39de0](https://android-review.googlesource.com/#/q/I39de0de444eb61393bb597baedbfa5b1278ee900))
- Add methods to override the`SplitInfo`in`SplitController`. Add test methods to create double for`SplitInfo`and`ActivityStack`. ([Icd69f](https://android-review.googlesource.com/#/q/Icd69f1d06e0470425d6126906bcac3fa3540430d))
- Make tag optional for`ActivityRule.Builder`. ([Ib0b44](https://android-review.googlesource.com/#/q/Ib0b449169f9a72c5affd25123d3220e55dcbf532))
- Remove`RatioSplitType`,`ExpandContainersSplit`and`HingeSplitType`. They are`SplitType`now.
  - Replace`#splitEqually()`,`#expandContainers()`and`#splitByHinge`to constant`SplitType SPLIT_TYPE_EQUAL`,`SPLIT_TYPE_EXPAND`and`SPLIT_TYPE_HINGE`
  - Remove the functionality to set fallback type of hinge split type. If the hinge split type cannot be applied due to the current device or window state, it fallbacks to split the parent task container equally. Use`SplitController#setSplitAttributesCalculator`to customize the fallback split type. ([Ifcc59](https://android-review.googlesource.com/#/q/Ifcc59d8ad1ea8fd7de04b65c597fff20f024bc13))
- Deprecate`add`/`removeSplitCallback`
  - Move`add`/`removeSplitCallback`to`SplitControllerCallbackAdapter`
  - Add`Flow`support to get`SplitInfo`list ([I7f1b6](https://android-review.googlesource.com/#/q/I7f1b6eab2a463c466045dff9f1ef41da1f380285))
- Add a test rule for`ActivityEmbeddingController`([I42e9b](https://android-review.googlesource.com/#/q/I42e9b0c5593b2b0d226ec2246e909958179e342b))
- Renaming`ActivityOptionsCompat`to`ActivityEmbeddingOptions`([I89301](https://android-review.googlesource.com/#/q/I893010468c45524f63b5256176473f3327cbf7c7))
- Add`splitSupportStatus`to indicate if Activity embedding is available. ([I10024](https://android-review.googlesource.com/#/q/I100240855cb3213d42b38ee1dace73fc0e595843))
- Introduce`SplitAttributes.BackgroundColor`to better represent the`DEFAULT`value. Clarify that non-opaque animation background color is not supported, so any non-opaque colors will be treated as the default, which means to use the current theme window background color. ([Ic6b95](https://android-review.googlesource.com/#/q/Ic6b95aad1f2f5a265f3467c00d125414a33e0137))
- Replace`alwaysAllow()`and`alwaysDisallow()`with`ALWAYS_ALLOW`and`ALWAYS_DISALLOW`. ([I3057b](https://android-review.googlesource.com/#/q/I3057bfd575704c75010470cc6b31733747ac9c39))
- Add APIs for`SplitRule`,`SplitAttributes`,`SplitAttributesCalculator`. ([I92d23](https://android-review.googlesource.com/#/q/I92d234efb38620fcefc85adb4cc9ef79e0a515fc))
- Add`TestActivityStack`to create`ActivityStack`for testing
  - Add`TestSplitInfo`to create`SplitInfo`for testing. ([I8e779](https://android-review.googlesource.com/#/q/I8e7797d8a2ffc53adbaa8b150beb97404b939b41))
- Add a way to create fake`SplitAttributesCalculatorParams`so that developers can verify their customized`SplitAttributesCalculator`([Id4a6e](https://android-review.googlesource.com/#/q/Id4a6e7294d2ae79db3a3cc7f5887e45cd726fa16))
- Add`WindowMetricsCalculator#computeCurrentWindowMetrics(@UiContext context: Context)`and`WindowMetricsCalculator#computeMaximumWindowMetrics(@UiContext context: Context)`([I66c7f](https://android-review.googlesource.com/#/q/I66c7f69171101da6c89babbb42ba9ed456117ab8))

### Version 1.2.0-alpha02

June 7, 2023

`androidx.window:window-*:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..73f902dee011bfe400d8a0330bfd8d4bb632065f/window)

**New Features**

- Update test API to have a constant for unspecified folding features.
- Overriding with`WindowLayoutInfoPublishRule`will override all values of`windowLayoutInfo`, including the Context based API.

**API Changes**

- Add constant for unspecified center folding feature. ([I7530c](https://android-review.googlesource.com/#/q/I7530cd0345d6daa59d0744153e7b820f26ca9dea))

**Bug Fixes**

- Update`WindowLayoutInfoPublishRule`to support overrides on`Context`based`WindowLayoutInfo`. ([I2037a](https://android-review.googlesource.com/#/q/I2037aeb49b5ec6193457bbc11cd04ff56c8b764d))

### Version 1.2.0-alpha01

May 24, 2023

`androidx.window:window-*:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0c26f64947eb47c353adc923210c3d786bcf1931..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/window)

**New Features**

Stabilize testing APIs around Activity Embedding and`WindowLayoutInfoTracker`.`ActivityEmbeddingRule`has been promoted to stable.`WindowMetricsCalculatorRule`has been promoted to stable. Utility functions to create a`FoldingFeature`for test have been promoted to stable.

**API Changes**

- Stabilize`ActivityEmbeddingRule`to support unit testing around Activity embedding. ([I8d6b6](https://android-review.googlesource.com/#/q/I8d6b66ee5d79792fb5ef737c0818dbff2f590354))
- `WindowMetrisCalculatorTestRule`is stable allowing stub metrics for JVM tests. We recommend using an emulator for accurate results.
- Stabilize test APIs for`WindowLayoutInfo`to support JVM testing. ([Ie036e](https://android-review.googlesource.com/#/q/Ie036e78bfd1784057c252a45917e2185687ae6b3))
- Add`IntRange`for test folding feature values. ([I69f7d](https://android-review.googlesource.com/#/q/I69f7d7f298a08765c835862978b9a7a26bbb3e9f))

## Version 1.1

### Version 1.1.0

June 7, 2023

`androidx.window:window-*:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0c26f64947eb47c353adc923210c3d786bcf1931..0dfa2a434822994e57d9d6a84225c31e7b395591/window)

**Important changes since 1.0.0**

**Activity Embedding**

- Added`PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED`as a boolean property of the`<application>`tag in the app manifest.
- Deprecated`isSplitSupported`and replaced with`splitSupportStatus`to provide more detailed information about why the split feature is not available.
- Added the`SplitController.SplitSupportStatus`nested class to provide state constants for the`splitSupportStatus`property.
- Refactored`SplitController`to several modules:
  - `ActivityEmbeddingController`module for`Activity`or`ActivityStack`related APIs.
  - Moved`isActivityEmbedded`from`SplitController`to`ActivityEmbeddingController`.
  - `RuleController`module for`EmbeddingRule`related operations:
  - Removed`SplitController`APIs:
  - `clearRegisteredRules()`
  - `getSplitRules()`
  - `initialize()`
  - `registerRule()`
  - `unregisterRule()`
  - Added`RuleController`APIs:
  - `addRule()`--- Adds a rule or updates the rule that has the same tag.
  - `removeRule()`--- Removes a rule from the collection of registered rules.
  - `setRules()`--- Establishes a collection of rules.
  - `clearRules()`--- Removes all registered rules.
  - `parseRules()`--- Parses rules from XML rule definitions.
- All modules require a context to be initialized by`#getInstance()`method, including:
  - `ActivityEmbeddingController#getInstance(Context)`
  - `SplitController#getInstance(Context)`
  - `RuleController#getInstance(Context)`
- Added the`EmbeddingAspectRatio`class to define enum-like behavior constants related to display aspect ratio.
- Added the`SplitAttributes`class to define the split layout.
- Added`SplitAttributes`calculator functions to`SplitController`to customize split layouts:
  - `setSplitAttributesCalculator(Function)`
  - `clearSplitAttributesCalculator()`
  - `isSplitAttributesCalculatorSupported()`to check if the`SplitAttributesCalculator`APIs are supported on the device
- Added`EmbeddingRule#tag`field.
- API updates in`SplitRule`:
  - Added`defaultSplitAttributes`--- Defines the default split layout of a split; replaces`splitRatio`and`layoutDirection`.
  - Added translation of the XML properties`splitRatio`and`splitLayoutDirection`to`defaultSplitAttributes`.
  - Changed minimum dimension definitions to use density-independent pixels (dp) instead of pixels.
  - Added`minHeightDp`with default value 600dp.
  - Changed`minWidth`to`minWidthDp`with default value 600dp.
  - Changed`minSmallestWidth`to`minSmallestWidthDp`with default value 600dp.
  - Added`maxAspectRatioInHorizontal`with default value`ALWAYS_ALLOW`.
  - Added`maxAspectRatioInPortrait`with default value 1.4.
  - Defined`FinishBehavior`nested class to replace finish behavior constants.
  - Applied the property changes to the Builder nested class of`SplitPairRule`and`SplitPlaceholderRule`.
- Replaced`SplitInfo#getSplitRatio()`with`SplitInfo#getSplitAttributes()`to provide additional split-related information.

**WindowLayout**

- Added experimental non-activity UI context support to`WindowInfoTracker`.
- Added experimental non-activity UI context to`WindowMetricsCalculator`.

**Migration Steps**

- To enable activity embedding to display activities in splits, apps must add the`PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED`property to the manifest`<application>`tag:`xml
  <property android:name="android.window.PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED"
  android:value="true" />`This allows the system to optimize the split behaviors for an application ahead of time.
- `SplitInfo`ratio
  - Check if the current split is stacked:`kotlin
    SplitInfo.splitAttributes.splitType is SplitAttributes.SplitType.ExpandContainersSplitType`
  - Check the current ratio:`kotlin
    if (SplitInfo.splitAttributes.splitType is SplitAttributes.SplitType.RatioSplitType)
    { val ratio = splitInfo.splitAttributes.splitType.ratio } else
    { // Ratio is meaningless for other types. }`
- SplitController migrations:
  - `SplitController.getInstance()`changes to`SplitController.getInstance(Context)`.
  - `SplitController.initialize(Context, @ResId int)`changes to`RuleController.getInstance(Context).setRules(RuleController.parse(Context, @ResId int))`.
  - `SplitController.getInstance().isActivityEmbedded(Activity)`changes to`ActivityEmbeddingController.getInstance(Context).isActivityEmbedded(Activity)`.
  - `SplitController.getInstance().registerRule(rule)`changes to`RuleController.getInstance(Context).addRule(rule)`.
  - `SplitController.getInstance().unregisterRule(rule)`changes to`RuleController.getInstance(Context).removeRule(rule)`.
  - `SplitController.getInstance().clearRegisteredRules()`changes to`RuleController.getInstance(Context).clearRules()`.
  - `SplitController.getInstance().getSplitRules()`changes to`RuleController.getInstance(Context).getRules()`.
- `SplitRule`property migrations:
  - `minWidth`and`minSmallestWidth`now use dp units instead of pixels. Apps can use the following call:`kotlin
    TypedValue.applyDimension( COMPLEX_UNIT_DIP, minWidthInPixels, resources.displayMetrics )`or simply divide`minWith`in pixels by`displayMetrics#density`.
- Finish behavior constants must be migrated to`FinishBehavior`enum-like class constants:
  - `FINISH_NEVER`changes to`FinishBehavior.NEVER`.
  - `FINISH_ALWAYS`changes to`FinishBehavior.ALWAYS`.
  - `FINISH_ADJACENT`changes to`FinishBehavior.ADJACENT`.
- Layout direction must be migrated to`SplitAttributes.LayoutDirection`:
  - `ltr`changes to`SplitAttributes.LayoutDirection.LEFT_TO_RIGHT`.
  - `rtl`changes to`SplitAttributes.LayoutDirection.RIGHT_TO_LEFT`.
  - `locale`changes to`SplitAttributes.LayoutDirection.LOCALE`.
  - `splitRatio`must be migrated to`SplitAttributes.SplitType.ratio(splitRatio)`.
- `SplitPairRule.Builder`migrations:
  - `SplitPairRule.Builder(filters, minWidth, minSmallestWidth)`changes to`kotlin
    SplitPairRule.Builder(filters) .setMinWidthDp(minWidthInDp)
    // Optional if minWidthInDp is 600. .setMinSmallestWidthDp(minSmallestWidthDp)
    // Optional if minSmallestWidthInDp is 600.`
  - `setLayoutDirection(layoutDirection)`and`setSplitRatio(ratio)`changes to`kotlin
    setDefaultSplitAttributes( SplitAttributes.Builder() .setLayoutDirection(layoutDirection) .setSplitType(SplitAttributes.SplitType.ratio(ratio)) .build() )`
  - `setFinishPrimaryWithSecondary`and`setFinishSecondaryWithPrimary`take the`FinishBehavior`enum-like constants. See "SplitRule migrations" for details.
  - Use`setMaxAspectRatioInPortrait(EmbeddingAspectRatio.ALWAYS_ALLOW)`to show splits on portrait devices.
- `SplitPlaceholder.Builder`migrations:
  - Has only`filters`and`placeholderIntent`parameters. Other properties move to setters. See "SplitPairRule.Builder migrations" for details.
  - `setFinishPrimaryWithPlaceholder`takes the`FinishBehavior`enum-like constants. See "SplitRule migrations" for details.
  - `setLayoutDirection(layoutDirection)`and`setSplitRatio(ratio)`change to:`kotlin
    setDefaultSplitAttributes( SplitAttributes.Builder() .setLayoutDirection(layoutDirection) .setSplitType(SplitAttributes.SplitType.ratio(ratio)) .build() )`
  - Use`setMaxAspectRatioInPortrait(EmbeddingAspectRatio.ALWAYS_ALLOW)`to show splits on portrait devices.

### Version 1.1.0-rc01

May 10, 2023

`androidx.window:window-*:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..0c26f64947eb47c353adc923210c3d786bcf1931/window)
| **Note:** Please refer to[What's new in WindowManager 1.1.0-beta01](https://android-developers.googleblog.com/2023/04/whats-new-in-windowmanager-110-beta01.html).

**New Features**

- Release`ActivityEmbedding`as a stable API.
- Various bug fixes.

### Version 1.1.0-beta02

April 5, 2023

`androidx.window:window-*:1.1.0-beta02`is released.[Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/window)

**New Features**

- Internal fixes and clean up.

### Version 1.1.0-beta01

March 22, 2023

`androidx.window:window-*:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..5e7d256f82fbafb6d059ab7b18fddd87c7531553/window)

**Activity Embedding**

- Added`PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED`as a boolean property of the`<application>`tag in the app manifest.
- Deprecated`isSplitSupported`and replaced with`splitSupportStatus`to provide more detailed information about why the split feature is not available.
- Added the`SplitController.SplitSupportStatus`nested class to provide state constants for the`splitSupportStatus`property.
- Refactored`SplitController`to several modules:
  - `ActivityEmbeddingController`module for`Activity`or`ActivityStack`related APIs.
  - Moved`isActivityEmbedded`from`SplitController`to`ActivityEmbeddingController`.
  - `RuleController`module for`EmbeddingRule`related operations:
  - Removed`SplitController`APIs:
    - `clearRegisteredRules()`
    - `getSplitRules()`
    - `initialize()`
    - `registerRule()`
    - `unregisterRule()`
  - Added`RuleController`APIs:
    - `addRule()`--- Adds a rule or updates the rule that has the same tag.
    - `removeRule()`--- Removes a rule from the collection of registered rules.
    - `setRules()`--- Establishes a collection of rules.
    - `clearRules()`--- Removes all registered rules.
    - \`parseRules() --- Parses rules from XML rule definitions.
- All modules require a context to be initialized by`#getInstance()`method, including:
  - `ActivityEmbeddingController#getInstance(Context)`
  - `SplitController#getInstance(Context)`
  - `RuleController#getInstance(Context)`
- Added the`EmbeddingAspectRatio`class to define enum-like behavior constants related to display aspect ratio.
- Added the`SplitAttributes`class to define the split layout.
- Added`SplitAttributes`calculator functions to`SplitController`to customize split layouts:
  - `setSplitAttributesCalculator(Function)`
  - `clearSplitAttributesCalculator()`
  - `isSplitAttributesCalculatorSupported()`to check if the SplitAttributesCalculator APIs are supported on the device
- Added`EmbeddingRule#tag`field.
- API updates in`SplitRule`:
  - Added`defaultSplitAttributes`--- Defines the default split layout of a split; replaces`splitRatio`and`layoutDirection`.
  - Added translation of the XML properties`splitRatio`and`splitLayoutDirection`to`defaultSplitAttributes`.
  - Changed minimum dimension definitions to use density-independent pixels (dp) instead of pixels.
  - Added`minHeightDp`with default value 600dp.
  - Changed`minWidth`to`minWidthDp`with default value 600dp.
  - Changed`minSmallestWidth`to`minSmallestWidthDp`with default value 600dp.
  - Added`maxAspectRatioInHorizontal`with default value`ALWAYS_ALLOW`.
  - Added`maxAspectRatioInPortrait`with default value`1.4`.
  - Defined`FinishBehavior`nested class to replace finish behavior constants.
  - Applied the property changes to the`Builder`nested class of`SplitPairRule`and`SplitPlaceholderRule`.
- Replaced`SplitInfo#getSplitRatio()`with`SplitInfo#getSplitAttributes()`to provide additional split-related information.

**WindowLayout**

- Added non-activity UI context support to`WindowInfoTracker`.
- Added non-activity UI context to`WindowMetricsCalculator`.

**Migration Steps**

- To enable activity embedding to display activities in splits, apps must add the`PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED`property to the manifest`<application>`tag:`xml
  <property
  android:name="android.window.PROPERTY_ACTIVITY_EMBEDDING_SPLITS_ENABLED"
  android:value="true" />`This allows the system to optimize the split behaviors for an application ahead of time.
- `SplitInfo`ratio
  - Check if the current split is stacked:`kotlin
    SplitInfo.splitAttributes.splitType is SplitAttributes.SplitType.ExpandContainersSplitType`
  - Check the current ratio:`kotlin
    if (SplitInfo.splitAttributes.splitType is SplitAttributes.SplitType.RatioSplitType) {
    val ratio = splitInfo.splitAttributes.splitType.ratio
    } else {
    // Ratio is meaningless for other types.
    }`
- `SplitController`migrations:
  - `SplitController.getInstance()`changes to`SplitController.getInstance(Context)`.
  - `SplitController.initialize(Context, @ResId int)`changes to`RuleController.getInstance(Context).setRules(RuleController.parse(Context, @ResId int))`.
  - `SplitController.getInstance().isActivityEmbedded(Activity)`changes to`ActivityEmbeddingController.getInstance(Context).isActivityEmbedded(Activity)`.
  - `SplitController.getInstance().registerRule(rule)`changes to`RuleController.getInstance(Context).addRule(rule)`.
  - `SplitController.getInstance().unregisterRule(rule)`changes to`RuleController.getInstance(Context).removeRule(rule)`.
  - `SplitController.getInstance().clearRegisteredRules()`changes to`RuleController.getInstance(Context).clearRules()`.
  - `SplitController.getInstance().getSplitRules()`changes to`RuleController.getInstance(Context).getRules()`.
- `SplitRule`property migrations:
  - `minWidth`and`minSmallestWidth`now use dp units instead of pixels. Apps can use the following call:`kotlin
    TypedValue.applyDimension(
    COMPLEX_UNIT_DIP,
    minWidthInPixels,
    resources.displayMetrics
    )`or simply divide`minWith`in pixels by`displayMetrics#density`.
- Finish behavior constants must be migrated to`FinishBehavior`enum-like class constants:
  - `FINISH_NEVER`changes to`FinishBehavior.NEVER`.
  - `FINISH_ALWAYS`changes to`FinishBehavior.ALWAYS`.
  - `FINISH_ADJACENT`changes to`FinishBehavior.ADJACENT`.
- Layout direction must be migrated to`SplitAttributes.LayoutDirection`:
  - `ltr`changes to`SplitAttributes.LayoutDirection.LEFT_TO_RIGHT`.
  - `rtl`changes to`SplitAttributes.LayoutDirection.RIGHT_TO_LEFT`.
  - `locale`changes to`SplitAttributes.LayoutDirection.LOCALE`.
  - `splitRatio`must be migrated to`SplitAttributes.SplitType.ratio(splitRatio)`.
- `SplitPairRule.Builder`migrations:
  - `SplitPairRule.Builder(filters, minWidth, minSmallestWidth)`changes to`kotlin
    SplitPairRule.Builder(filters)
    .setMinWidthDp(minWidthInDp) // Optional if minWidthInDp is 600.
    .setMinSmallestWidthDp(minSmallestWidthDp)
    // Optional if minSmallestWidthInDp is 600.`
  - `setLayoutDirection(layoutDirection)`and`setSplitRatio(ratio)`change to`kotlin
    setDefaultSplitAttributes(
    SplitAttributes.Builder()
    .setLayoutDirection(layoutDirection)
    .setSplitType(SplitAttributes.SplitType.ratio(ratio))
    .build()
    )`
  - `setFinishPrimaryWithSecondary`and`setFinishSecondaryWithPrimary`take the`FinishBehavior`enum-like constants. See "SplitRule migrations" for details.
  - Use`setMaxAspectRatioInPortrait(EmbeddingAspectRatio.ALWAYS_ALLOW)`to show splits on portrait devices.
- `SplitPlaceholder.Builder`migrations:
  - Has only`filters`and`placeholderIntent`parameters. Other properties move to setters. See "SplitPairRule.Builder migrations" for details.
  - `setFinishPrimaryWithPlaceholder`takes the`FinishBehavior`enum-like constants. See "SplitRule migrations" for details.
  - `setLayoutDirection(layoutDirection)`and`setSplitRatio(ratio)`change to:`kotlin
    setDefaultSplitAttributes(
    SplitAttributes.Builder()
    .setLayoutDirection(layoutDirection)
    .setSplitType(SplitAttributes.SplitType.ratio(ratio))
    .build()
    )`
  - Use`setMaxAspectRatioInPortrait(EmbeddingAspectRatio.ALWAYS_ALLOW)`to show splits on portrait devices.

### Version 1.1.0-alpha06

February 22, 2023

`androidx.window:window-*:1.1.0-alpha06`is released.[Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..87533b4ff06971ed59028936cd9b6da988cd4522/window)

**New Features**

- Expose experimental version of getting the`WindowLayoutInfo`from a UI context.

**API Changes**

- Add`splitSupportStatus`to indicate if Activity embedding is available. ([I10024](https://android-review.googlesource.com/#/q/I100240855cb3213d42b38ee1dace73fc0e595843))
- Make UI Context`WindowLayoutInfo`API as experimental. ([I58ee0](https://android-review.googlesource.com/#/q/I58ee049cac8cc74c61f222cc44375f266bbca027))
- Introduces the`WindowAreaController`and API's to enable`RearDisplay`Mode to move the current window to the display that is aligned with the rear camera. ([Iffcbf](https://android-review.googlesource.com/#/q/Iffcbf39a129e84d825f2b3796e377ef54987b7c2))
- Update default background color. ([I1ac1b](https://android-review.googlesource.com/#/q/I1ac1b4e54e06a9ccb31781c9d3a7d35f811d0687))
- Add`SplitAttributes`params. ([I18bdd](https://android-review.googlesource.com/#/q/I18bdd66483bafb868ea33ed3f5e7eea79bdfcdb7))
- Add APIs for`SplitRule`,`SplitAttributes`,`SplitAttributesCalculator`. ([I92d23](https://android-review.googlesource.com/#/q/I92d234efb38620fcefc85adb4cc9ef79e0a515fc))
- Improve the APIs around`maxAspectRatio`:
  1. Replace`alwaysAllow()`and`alwaysDisallow()`with`ALWAYS_ALLOW`and`ALWAYS_DISALLOW`.
  2. Update API documentation of @see with standalone documentation. ([I3057b](https://android-review.googlesource.com/#/q/I3057bfd575704c75010470cc6b31733747ac9c39))
- The following constructors are removed from public APIs because they are not supposed to be called by apps.
  - `SplitInfo`constructor
  - `ActivityStack`constructor ([Ide534](https://android-review.googlesource.com/#/q/Ide5342d450a1cedb51d7c6593e3e5e2f5cfc2537))
- `SplitRule`now takes`maxAspectRatioInPortrait/Landscape`. It only allows activities split when the aspect ratio of the parent bounds is smaller or equal to the requested`maxAspectRatio`. ([Ia5990](https://android-review.googlesource.com/#/q/Ia5990b64c87987a9328c228753e792bd293e139a))
- Change`RuleController#parseRules`to be static ([I785df](https://android-review.googlesource.com/#/q/I785df661ce66a6fdb21842ad2569b2051995c2a0))
- Improve the APIs around ActivityEmbedding
  1. Align the API naming - Use add/remove for multiple instances:
  2. `registerRule`changes to`addRule`
  3. `unregisterRule`changes to`removeRule`
  4. Replace`getSplitRules`with`getRules`since`ActivityRule`is not a split rule
  5. Add`RuleController#setRules`to set a bunch of rules
  6. Extract rule related APIs from`SplitController`to singleton`RuleController`. They are:
  7. `addRule`
  8. `removeRule`
  9. `getRules`
  10. `setRules`
  11. `clearRules`
  12. `parseRules`
  13. Extract`#isActivityEmbedded`from`SplitController`to singleton`ActivityEmbeddingController`. They are:
  14. `isActivityEmbedded`
  15. Remove`SplitController#initialize`. To set rules from XML file, please use`RuleController#parseRules`and`#setRules`. Before this change:`SplitController.initialize(context, R.xml.static_rules)`After this change:`val ruleController = RuleController.getInstance(context)
      val rules = ruleController.parseRules(R.xml.static_rules)
      ruleController.setRules(rules)`
  16. We don't distinguish static rules with runtime rules anymore. That said, calling`#clearRules`results to clear all rules no matter they are registered with static XML rule definitions or at runtime. To hav the legacy behavior of`SplitController#clearRegisteredRules`, please call`RuleController#parseRules`with the XML resources id and call`RuleController#setRules`to set back the rules again. Before this change:`SplitController.getInstance(context).clearRegisteredRules()`After this change:`val ruleController = RuleController.getInstance(context)
      val rules = ruleController.parseRules(R.xml.static_rules)
      ruleController.setRules(rules)`([Ib3967](https://android-review.googlesource.com/#/q/Ib39671fb22a9ccef3b0aa8967ee18c3168c54c63))
- Improve the SplitRule APIs:
  1. Take min dimensions in DP instead of pixels for`SplitRule`.
  2. Refactor for`SplitRule`Builder to take min dimensions as optional. ([I95f17](https://android-review.googlesource.com/#/q/I95f17ce89844d18708e6fb03924d38a00af115ac))
- Pass a Context to initialize`SplitController`([I42549](https://android-review.googlesource.com/#/q/I42549aeb1b5df27093dc6c7de73a2c4d7c97e75f))
- Renamed`SplitRule#layoutDir`to`#layoutDirection`and`SplitRule Builder#setLayoutDir`to`Builder#setLayoutDirection`. ([I3f6d1](https://android-review.googlesource.com/#/q/I3f6d1bea1d82e104c31c5458fe1f715927061cd8))

### Version 1.1.0-alpha04

November 9, 2022

`androidx.window:window-*:1.1.0-alpha04`is released.[Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..a1e318590b217ecfce1b2de17eed2f18b6a680bb/window)

**New Features**

- Expose a method to determine if an`ActivityStack`is empty for`ActivityEmbedding`.
- Removed experimental API tags from`ActivityEmbedding`APIs.
- Hide`ActivityRule`constructor as the`Builder`is the preferred way to construct.
- Add an experimental method to get the`WindowInsets`on`WindowMetrics`.
- Update`SplitPlaceholderFinishBehavior`to prevent finishing the placeholder. Finishing the placeholder caused some confusing behavior.

**API Changes**

- Make val`isEmpty`public to replace fun`isEmpty`.
- Rename`ActivityStack`parameter activities to`activitiesInProcess`. ([Ia5055](https://android-review.googlesource.com/#/q/Ia505530dbc6c86baf049060791202461bc1a191c))
- Remove`ActivityFilter#matchesClassName`and`ActivityFilter#matchesClassNameOrWildCard`because they are confusing.
- Add`ActivityFilter#componentName`abd`ActivityFilter#intentAction`to allow the caller to distinguish different filters ([I41f22](https://android-review.googlesource.com/#/q/I41f220f8ecfb3deebfc515061c1eced568aaf30f))
- Remove the`@Deprecated`APIs from the experimental API ([I216b3](https://android-review.googlesource.com/#/q/I216b3d3c43ded16fc84510cf2666d485cf75e7aa))
- Remove`@ExperimentalWindowApi`for Activity Embedding APIs ([I69ebe](https://android-review.googlesource.com/#/q/I69ebe86d328e1314826eba87ad57d2f640900994))
- Hide`ActivityRule`constructor, use Builder instead. ([If4eb6](https://android-review.googlesource.com/#/q/If4eb6a461f82ab1176b336e28b0338d12fabce77))
- Add APIs to check if an Activity is part of the`ActivityFilter`. ([Ia43cf](https://android-review.googlesource.com/#/q/Ia43cfc0fe4d7108a4a2d84d204bba51913309c8f))
- Update API files to reflect changes in`WindowMetrics`and`WindowMetricsCalculatorCompat`classes ([I667fe](https://android-review.googlesource.com/#/q/I667fe7908615b044eb3d6423e124b6d697a9a100))
- Update`ActivityEmbedding`Property Javadoc and class name ([Ia1386](https://android-review.googlesource.com/#/q/Ia1386fcbdffb219199486316f23a92a156a86ee6))
- Adding`ActivityEmbedding`property tag names to be used in AndroidManifest.xml ([Id1ad4](https://android-review.googlesource.com/#/q/Id1ad453a295639a8cf53542d28c3991ecd4cc3da))
- Added new API`SplitPlaceholderFinishBehavior`and`SplitPlaceholderRule.finishPrimaryWithPlaceholder`, this replaces existing`SplitPlaceholderRule.finishPrimaryWithSecondary`which defines when placeholder activites are finished, how associated activites in Activity Embedding should behave. ([I64647](https://android-review.googlesource.com/#/q/I64647ee85533e8bebeefdef55b6252e919768fa7))

**Bug Fixes**

- Introduces the`WindowAreaController`and API's to enable`RearDisplay`Mode to move the current window to the display that is aligned with the rear camera. ([I388ab](https://android-review.googlesource.com/#/q/I388ab775740713650e6142135fbfc57891d2214b))

### Version 1.1.0-alpha03

July 27, 2022

`androidx.window:window-*:1.1.0-alpha03`is released.[Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/window)

**New Features**

- Update the default values for embedding rules.

**API Changes**

- Update default values for embedding rule properties. ([Ic4d35](https://android-review.googlesource.com/#/q/Ic4d357169a86583665ff27bb7f239159267ec42c))

### Version 1.1.0-alpha02

May 11, 2022

`androidx.window:window-*:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/53d512be6fd26bc30bffa7cae8e9769ec5c4bfbf/window)

**New Features**

- Release the adapter libraries to support Java and RxJava.

### Version 1.1.0-alpha01

May 11, 2022

`androidx.window:window-*:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64cc4d2fc346bde9fe41f047a665695fed2b5baf..c0a89ec374961b3015097ab307ebb8196dbe3888/window)

**New Features**

- Release adapters to support java and RxJava

### Version 1.1.0-alpha01

April 20, 2022

`androidx.window:window:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64cc4d2fc346bde9fe41f047a665695fed2b5baf..c0a89ec374961b3015097ab307ebb8196dbe3888/window/window)

**New Features**

- Fixes a bug where backgrounding an app stops emitting fold features.
- Expand on the experimental ActivityEmbedding API.

**API Changes**

- A public API to check if an activity is being embedded. ([I39eb7](https://android-review.googlesource.com/#/q/I39eb7a9e5c5c0be78e0acdfe71eed3c17bd483a0))

**Bug Fixes**

- Add APIs that customize finishing behavior for containers in activity splits ([I1a1e4](https://android-review.googlesource.com/#/q/I1a1e4824a983555539c1ccacf4c6c73fad5d1841))
- Added a new configuration option for activity split rules. ([Iec6af](https://android-review.googlesource.com/#/q/Iec6af1c9c7c7209f9d38d30aaa32e1961cd78ddd))

## Version 1.0

### Version 1.0.0

January 26, 2022

`androidx.window:window-*:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1106d327dbc4c8703e732bb015303a3cd1c36ee7..64cc4d2fc346bde9fe41f047a665695fed2b5baf/window)

**Major features of 1.0.0**

- Support for folding phones through`WindowInfoTracker`and`FoldingFeature`.`WindowMetricsCalculator`to help calculate the current WindowMetrics.

### Version 1.0.0-rc01

December 15, 2021

`androidx.window:window-*:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..1106d327dbc4c8703e732bb015303a3cd1c36ee7/window)

**New Features**

- Add support for folding phones through`WindowInfoTracker`.
- Add methods to calculate the current and maximum`WindowMetrics`.
- Add supporting test APIs.

### Version 1.0.0-beta04

November 17, 2021

`androidx.window:window-*:1.0.0-beta04`is released.[Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41fb7767c8521ac3a81010ce2a48df33b54c9d02..cc1240d00b28657ee0c1a937f60430eaf1b03b09/window)

**New Features**

- Rename WindowInfoRepository to WindowInfoTracker.
- Make Activity an explicit method dependency for WindowInfoTracker.
- Add a simple TestRule for WindowMetricsCalculator to support developers using Robolectric.

**API Changes**

- Extract extensions ([I25a5f](https://android-review.googlesource.com/#/q/I25a5fda9e895d05c05bff1e11f3db6fed4bfa989))
- add isEmpty in ActivityStack ([I5a4e6](https://android-review.googlesource.com/#/q/I5a4e6533fc30d0cf1298ee5d08fffd4d34ca1792))
- Rename WindowInfoRepository to WindowInfoTracker.
  - Update java/rxjava/testing dependencies to match. ([I0da63](https://android-review.googlesource.com/#/q/I0da639d9722c5a0c1a588a93535c2b256958c268))
- Add a test rule for a simple WindowMetricsCalculator. ([Ibacdb](https://android-review.googlesource.com/#/q/Ibacdb52705d86c127cd1021a36069602440a5aaa))

### Version 1.0.0-beta03

October 27, 2021

`androidx.window:window-*:1.0.0-beta03`is released.[Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..41fb7767c8521ac3a81010ce2a48df33b54c9d02/window)

**New Features**

- Add experimental Activity Embedding APIs. This initial layout version allows showing two Activities side by side.

**API Changes**

- Removed the currentWindowMetrics API since we can not provide it accurately. Please use WindowMetricsCalculator instead ([Icda5f](https://android-review.googlesource.com/#/q/Icda5f3802692e70d0220a491c90999866a1b73cb))
- Updated the extensions api. ([Ica92b](https://android-review.googlesource.com/#/q/Ica92bbdb8300f51b2d2906f38b40a9ed027b7810))
- Added an interface for a new feature that allows embedding activities and showing them side-by-side within the parent task window. ([I5711d](https://android-review.googlesource.com/#/q/I5711d3dfcfd27212fd8c0f83e4b3277863460c0))
- Hid the constructors for WindowMetrics and WindowLayoutInfo, please use the test APIs instead. ([I5a1b5](https://android-review.googlesource.com/#/q/I5a1b5b9197c7c26274f6f48a2a3e3b8f525f338f))
- Add an API to create fake WindowLayoutInfo objects. ([I4a2fd](https://android-review.googlesource.com/#/q/I4a2fd3a8da2e40fbabcb72c4f323f0090a573bd4))

**Bug Fixes**

- Fixed memory leak. ([I3fc79](https://android-review.googlesource.com/#/q/I3fc799fa458528a5cb18dac373aa024f99fa5a6a),[b/202989046](https://issuetracker.google.com/issues/202989046))

### Version 1.0.0-beta02

September 1, 2021

`androidx.window:window-*:1.0.0-beta02`is released.[Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f659ade9a1989a7e7f26d1e7f66b19d832ce1cb5..47e81d1c497b8a57534a460c277855db1b0257ae/window)

**New Features**

- Add an experimental annotation to annotate experimental APIs. ([I9f1b6](https://android-review.googlesource.com/#/q/I9f1b65a2ed713e5334ef8334a0173fc8794f4d35))
- Add a test method to create a test FoldingFeature that accepts a Rect. This will make it easie to test when using Robolectric as opposed to an actual Activity. ([Id1cca](https://android-review.googlesource.com/#/q/Id1cca363c9967bfa560a700e978670472284410f))

### Version 1.0.0-beta01

August 18, 2021

`androidx.window:window-*:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..f659ade9a1989a7e7f26d1e7f66b19d832ce1cb5/window)

**New Features**

- Removed old constants and made`FoldingFeature`into an interface.

**API Changes**

- Remove old constants and make FoldFeature an interface. ([I9a2d5](https://android-review.googlesource.com/#/q/I9a2d53acc03284cbdf274f12186e969a769fbd33))

**Bug Fixes**

- Libraries that depend on the`Test Core`library have been upgraded to version`1.4.0`and will now work with Android platform version S. ([I88b72](https://android-review.googlesource.com/#/q/I88b726b2d76735ac012ea47298e0bf02092cd857),[b/189353863](https://issuetracker.google.com/issues/189353863))

### Version 1.0.0-alpha10

August 4, 2021

`androidx.window:window-*:1.0.0-alpha10`is released.[Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/window)

**New Features**

- Rename WindowInfoRepo to WindowInfoRepository and adjust corresponding classes / files.
- Convert current window metrics to a Flow in WindowInfoRepository since the value changes over time.
- Rename WindowInfoRepoJavaAdapter to WindowInfoRepoCallbackAdapter
- Add helper method to create test FoldingFeature objects
- Update packages to group classes based on the feature they are supporting.

**API Changes**

- Rename ActivityExt to ActivityExtensions Change from Repo to Repository. ([I61a16](https://android-review.googlesource.com/#/q/I61a16da6f3ad5afdfb3171aaf6232d77b07e2466))
- Update packages for classes. ([I23ae2](https://android-review.googlesource.com/#/q/I23ae25660737c35c61685a4b3078282dd23fd0cf))
- Remove WindowMetrics from WindowInfoRepo ([I24663](https://android-review.googlesource.com/#/q/I24663dd37f91f2402b88ab2a90803d8f91da9aca))
- Remove WindowManager and use WindowInfoRepo
  - Make WindowBackend internal. ([I06d9a](https://android-review.googlesource.com/#/q/I06d9a0047401fe2426b78f30f7a8e25bee7d9b1a))
- Convert window metrics to Flow.
  - Rename java adapter to WindowInfoRepoCallbackAdapter
  - Remove callbackFlow so no more experimental APIs are in use. ([Ia4d15](https://android-review.googlesource.com/#/q/Ia4d152c3cc21ef8c3f90255e65721702cad40585))
- Add helper method to create test display features.
  - Change from occlusionMode to occlusionType ([If4cff](https://android-review.googlesource.com/#/q/If4cff35f63b253d14abf92f7cd70b69a0858ead5))

**Bug Fixes**

- Fix proguard error where core library was being removed.
- Fix error where WindowLayoutInfo was not being delivered to additional subscribers.
- Fix error where config changes would not trigger folding feature updates.

### Version 1.0.0-alpha09

June 30, 2021

`androidx.window:window-*:1.0.0-alpha09`is released.[Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..19ae3a88ff0824d615355b492cb56049e16991f2/window)

**New Features**

- Change from integer constants to unbounded enums.
- Add a test util to create test folding features.

**API Changes**

- Add helper method to create test display features. ([I3cf54](https://android-review.googlesource.com/#/q/I3cf548611ee5838486f817b15c82ede61f442f3d))
  - Change from`occlusionMode`to`occlusionType`.

**Bug Fixes**

- Emit initial value when adding multiple consumers of the data streams.

### Version 1.0.0-alpha08

June 16, 2021

`androidx.window:window-*:1.0.0-alpha08`is released.[Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b/window)

**New Features**

- Released a testing artifact to make it easier to test when using WindowInfoRepository. Use WindowInfoRepository to get information about DisplayFeatures and the WindowMetrics. ([I57f66](https://android-review.googlesource.com/c/platform/frameworks/support/+/1702526),[Ida620](https://android-review.googlesource.com/c/platform/frameworks/support/+/1730611))

### Version 1.0.0-alpha07

June 2, 2021

`androidx.window:window-*:1.0.0-alpha07`is released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4/window)

**New Features**

- Migrate core window library to Kotlin. Will use coroutines and suspend functions to expose asynchronous data going forward.
- Add WindowInfoRepo as the main interaction point for getting the WindowMetrics and the stream of WindowLayoutInfo.
- New`window-java`artifact to expose Java-friendly APIs to register and unregister callbacks.
- New`window-rxjava2`and`window-rxjava3`artifacts to expose RxJava adapted APIs.

**API Changes**

- Add`WindowServices`to provide dependencies uniformly.
  - Add coroutine based api to consume window layout info. ([Iab70f](https://android-review.googlesource.com/#/q/Iab70f2a65f5e8db0de2d6d342fc3ab398df91c9e))
- Migrate core window manager library to Kotlin. ([Icca34](https://android-review.googlesource.com/#/q/Icca34320c487d70d1d7605f8db2c9965f722dbbb))

**Bug Fixes**

- Add new data class to represent feature bounds. ([I6dcd1](https://android-review.googlesource.com/#/q/I6dcd12b98be8281c0876c6a7dff3ad7221102cc9))

### Version 1.0.0-alpha06

May 5, 2021

`androidx.window:window:1.0.0-alpha06`is released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/window/window)

**New Features**

- We have started our migration to Kotlin and will finish in the next release.
- DeviceState has been removed from the public API, please use FoldingFeature instead.
- We have removed`STATE_FLIPPED`from the FoldingFeature states since it is not supported by any use-case at the moment.
- We have also removed other deprecated APIs.

**API Changes**

- Adding Kotlin as a dependency.
  - Migrate core library to Kotlin. ([Idd995](https://android-review.googlesource.com/#/q/Idd995cb977e2eadc79623dfb8390cf136f0b5cdf))
- Removed`DisplayFeature`builder. ([I61fa4](https://android-review.googlesource.com/#/q/I61fa463a930f9a98556e5c56b45860fbdc88a04c))
- Removed`DeviceState`from public api, use`FoldingFeature`instead. ([Id6079](https://android-review.googlesource.com/#/q/Id6079a0980a7a89e1f72f8074024926ebb646ab9))
- Remove device state callback from extensions. ([I5ea83](https://android-review.googlesource.com/#/q/I5ea837baa8880474f2db5944a9a2878321f32733))
- Remove`STATE_FLIPPED`from FoldingFeature. ([I9c4e1](https://android-review.googlesource.com/#/q/I9c4e1819214647440a1a7886593691f85b385f4d))
- Remove deprecated registration methods. ([Ib381b](https://android-review.googlesource.com/#/q/Ib381b2f3ec48fc9181160fc43e231f6457d5ff4e))

### Version 1.0.0-alpha05

March 24, 2021

`androidx.window:window:1.0.0-alpha05`is released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/080f233e07421eca8f842f05f11c12b4cdb84f5b..5c42896eb6591b09e3952030fb7ea8d9b8c42713/window/window)

**New Features**

We have added convenience methods to FoldingFeature so that apps can tell if the feature is separating, occluding, and determine the orientation of the hinge. We are also hiding the hinge type so that

We are removing the synchronous read methods from WindowManager. Synchronous read methods are error prone since there is an implicit race condition. Register listeners and callbacks to receive updates on the WindowLayoutInfo.

**API Changes**

- Add convenience methods for working with FoldingFeatures ([Ie733f](https://android-review.googlesource.com/#/q/Ie733f53b8eaf2226704bb097ed83dc1b6b0e057c))
- Removes synchronous read methods from WindowManager ([I96fd4](https://android-review.googlesource.com/#/q/I96fd460f1dbde8028d85c7ec9703d71094531411))

### Version 1.0.0-alpha04

March 10, 2021

`androidx.window:window:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/window/window)

**New Features**

- Fixes a bug where no WindowLayoutInfo is emitted if there isn't an OEM implementation. Now we emit an empty WIndowLayoutInfo.
- Fix a bug where state would not update properly if the hinge state changed while the app was backgrounded. Now the state should be consistent.
- Update our proguard files to ignore warnings from runtime dependencies.

**Bug Fixes**

- Emit an empty value when the OEM library is missing. ([Ide935](https://android-review.googlesource.com/#/q/Ide935358cb94670673234f2ac6fcc8c689b63244))

### Version 1.0.0-alpha03

February 18, 2021

`androidx.window:window:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..080f233e07421eca8f842f05f11c12b4cdb84f5b/window/window)

**New Features**

- Emit an empty value for WindowLayoutInfo when the OEM implementation is empty. This should make it easier to use the library on more devices. Since the APIs are asynchronous it is still recommended that apps write some defensive code and emit a default value after a timeout. We do not have any guarantees on OEM implementations and the initial value may be delayed.

**Bug Fixes**

- Emit an empty value when the OEM library is missing. ([Ide935](https://android-review.googlesource.com/#/q/Ide935358cb94670673234f2ac6fcc8c689b63244))

### Version 1.0.0-alpha02

January 27, 2021

`androidx.window:window:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fca183fb525b93d2002528fbafdb042f2bffdf36..aee18b103203a91ee89df91f0af5df2ecff356d6/window/window)

**New Features**

- We have deprecated some APIs to help streamline the api and reduce mistakes. Some notable examples are removing the synchronous read operations from WindowManager and deprecating DeviceState. Synchronous read operations can lead to race conditions and have incorrect UI.

- We have converted DisplayFeature to an interface that other features will implement going forward. Our first feature is FoldingFeature which is now the representation of a screen fold or a hinge. This also contains the state of the hinge replacing DeviceState.

- WindowMetrics was introduced in Android 11 to provide developers with a simple way to query for metrics about a window, for example its position and size on screen and any system insets. We've backported the API in this release so that developers can leverage WindowMetrics and continue to support older Android versions. WindowMetrics can be obtained through the`WindowManager#getCurrentWindowMetrics()`and WindowManager#getMaximumWindowMetrics() APIs.

**API Changes**

- Deprecate APIs that will be removed in the next alpha ([Ib7cc4](https://android-review.googlesource.com/#/q/Ib7cc4ad14fea8c34ef8b94aaa9366fc8cb235a46))
- Updates`ExtensionInterface`to accept explicit Activity references. ([I07ded](https://android-review.googlesource.com/#/q/I07ded6e81dd3d1006adc11c8b66dccd9caa3000d))
- Introduces the WindowMetrics API. ([I3ccee](https://android-review.googlesource.com/#/q/I3ccee32e7f1b9121de6ad63bae71a5b3d9fb1330))
- Remove synchronous read methods from WindowManager ([I69983](https://android-review.googlesource.com/#/q/I699831b8f202b7b7f70a030b105be8724bb52da3))
- Make ExtensionWindowBackend package protected. ([Ied208](https://android-review.googlesource.com/#/q/Ied2085250ffeb8ec253d4b5dd742300eb08835bc))

**Bug Fixes**

- Update`ExtensionInterface`APIs to accept visual contexts. ([I8e827](https://android-review.googlesource.com/#/q/I8e827eb510c0c36d8877ea589408aab9269db9ea))

**External Contribution**

- Merge DeviceState and WindowLayoutInfo so it is easier to access data. ([Id34f4](https://android-review.googlesource.com/#/q/Id34f448e9403aa6462a63b574073a6762365ed6f))

### Version 1.0.0-alpha01

February 27, 2020

`androidx.window:window:1.0.0-alpha01`and`androidx.window:window-extensions:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fca183fb525b93d2002528fbafdb042f2bffdf36/window)This is the first release of the Window Manager library.

**New features**

- `DisplayFeature`: This new API identifies disruptions in the continuous flat screen surfaces such as hinges or folds
- `DeviceState`: This new API provides the current posture of the phone from a list of defined postures (For example,`CLOSED`,`OPENED`,`HALF_OPENED`, etc.)