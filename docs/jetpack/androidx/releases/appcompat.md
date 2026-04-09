---
title: https://developer.android.com/jetpack/androidx/releases/appcompat
url: https://developer.android.com/jetpack/androidx/releases/appcompat
source: md.txt
---

# Appcompat

# Appcompat

[User Guide](https://developer.android.com/guide/topics/ui/look-and-feel)[Code Sample](https://github.com/material-components/material-components-android-examples)  
API Reference  
[androidx.appcompat.app](https://developer.android.com/reference/androidx/appcompat/app/package-summary)  
[androidx.appcompat.content.res](https://developer.android.com/reference/androidx/appcompat/content/res/package-summary)  
[androidx.appcompat.graphics.drawable](https://developer.android.com/reference/androidx/appcompat/graphics/drawable/package-summary)  
[androidx.appcompat.view](https://developer.android.com/reference/androidx/appcompat/view/package-summary)  
[androidx.appcompat.widget](https://developer.android.com/reference/androidx/appcompat/widget/package-summary)  
Allows access to new APIs on older API versions of the platform (many using Material Design).  

| Latest Update |                                  Stable Release                                  | Release Candidate | Beta Release | Alpha Release |
|---------------|----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| June 4, 2025  | [1.7.1](https://developer.android.com/jetpack/androidx/releases/appcompat#1.7.1) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Appcompat, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    def appcompat_version = "1.7.1"

    implementation "androidx.appcompat:appcompat:$appcompat_version"
    // For loading and tinting drawables on older versions of the platform
    implementation "androidx.appcompat:appcompat-resources:$appcompat_version"
}
```

### Kotlin

```kotlin
dependencies {
    val appcompat_version = "1.7.1"

    implementation("androidx.appcompat:appcompat:$appcompat_version")
    // For loading and tinting drawables on older versions of the platform
    implementation("androidx.appcompat:appcompat-resources:$appcompat_version")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460343+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460343&template=1422420)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.7

### Version 1.7.1

June 4, 2025

`androidx.appcompat:appcompat:1.7.1`and`androidx.appcompat:appcompat-resources:1.7.1`are released. Version 1.7.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/31e0791ed498d528e1ee51f54e0c7cd334729997..e144631ecabce2e5206abae98d8f18101bac88e0/appcompat).

**Bug Fixes**

- `AppCompat`has been updated to use Activity 1.8.0 to allow it to use the`initializeViewTreeOwners()`API from`ComponentActivity`to ensure that it always has the correct`ViewTreeOwners`set. This fixes an incompatibility between`AppCompatActivity`and[NavigationEvent](https://developer.android.com/jetpack/androidx/releases/navigationevent)and libraries that build on top of it such as[Navigation 3](https://developer.android.com/jetpack/androidx/releases/navigation3). ([I96919](https://android-review.googlesource.com/#/q/I969192dacdbae2c6feb9734cafc21cd0ee352680),[b/419208471](https://issuetracker.google.com/issues/419208471))

### Version 1.7.0

May 29, 2024

`androidx.appcompat:appcompat:1.7.0`and`androidx.appcompat:appcompat-resources:1.7.0`are released. Version 1.7.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6424b9a28d12f04e043d5257a3e821c152b0187d..31e0791ed498d528e1ee51f54e0c7cd334729997/appcompat).

**Important changes since 1.6.0**

- `AppCompatDialog`now correctly sets the`LifecycleOwner`,`SavedStateRegistryOwner`, and`OnBackPressedDispatcherOwner`on the dialog's decor view via the`ViewTree`APIs, fixing issues when hosting a`ComposeView`within an`AppCompatDialog`.
- `AppCompatActivity`now sets the`ViewTreeOnBackPressedDispatcherOwner`so that it is possible to retrieve the dispatcher from the view.
- Significantly improved the performance of`SupportMenuInflater`.
- `Locale.getDefault()`now returns the system locale after a cold start.
- `LinearLayoutCompat`now preserves margin layout params.

**Dependency Updates**

- `AppCompat`now depends on Activity 1.7.0.
- `AppCompat`now depends on Fragment version 1.5.4.

### Version 1.7.0-rc01

May 14, 2024

`androidx.appcompat:appcompat:1.7.0-rc01`and`androidx.appcompat:appcompat-resources:1.7.0-rc01`are released. Version 1.7.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..6424b9a28d12f04e043d5257a3e821c152b0187d/appcompat).

### Version 1.7.0-beta01

May 1, 2024

`androidx.appcompat:appcompat:1.7.0-beta01`and`androidx.appcompat:appcompat-resources:1.7.0-beta01`are released. Version 1.7.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..fbd1ac175922f44c69a13545d194066ee428b342/appcompat).

### Version 1.7.0-alpha03

July 26, 2023

`androidx.appcompat:appcompat:1.7.0-alpha03`and`androidx.appcompat:appcompat-resources:1.7.0-alpha03`are released.[Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..4aed940027a19667e67d155563fc5fa8b7279313/appcompat)

**New Features**

- Support for getting per-app locales in non-Activity contexts ([I58e753](https://android-review.googlesource.com/c/platform/frameworks/support/+/2577875)). Four new APIs have been added for this feature:

  - `LocaleManagerCompat.getApplicationLocales()`: for developers to get per-app locales out of activity scope.

  - `ContextCompat.getString()`: return localized strings based on per-app locales.

  - `ContextCompat.getContextForLanguage()`: the context returned by this method will respect the per-app locales.

  - `ConfigurationCompat.setLocales()`: for above APIs, to set the configuration's locale.

**Other API Changes**

- Added`setLineHeight(unit, lineHeight)`to`TextView`compat classes ([Ia9fa9](https://android-review.googlesource.com/#/q/Ia9fa96f6ab74ebb6fe73b080c21c8afe419215cc))
- Added`setLineHeight(unit, lineHeight)`to`TextView`compat classes ([Ib2ee1](https://android-review.googlesource.com/#/q/Ib2ee1334bd0396a8d92a87b8c2268029a36b1148))
- Added`setLineHeight(unit, lineHeight)`to`TextView`compat classes ([I15716](https://android-review.googlesource.com/#/q/I1571669714d19c2e26d514b512f485d8dc5f6b97))

**Bug Fixes**

- `AppCompatDialog`now correctly sets the`LifecycleOwner`,`SavedStateRegistryOwner`, and`OnBackPressedDispatcherOwner`on the dialog's decor view via the`ViewTree`APIs, fixing issues when hosting a`ComposeView`within an`AppCompatDialog`.`AppCompat`now depends on Activity 1.7.0. ([Ib28ab](https://android-review.googlesource.com/#/q/Ib28abb12cc3c617b9ffed9e1450e48308dc7c3df),[b/261314581](https://issuetracker.google.com/issues/261314581))
- Significantly improve the performance of`SupportMenuInflater`([I0b087](https://android-review.googlesource.com/#/q/I0b0875546d4817576a9d360a890eccce60555884))

### Version 1.7.0-alpha02

February 8, 2023

`androidx.appcompat:appcompat:1.7.0-alpha02`and`androidx.appcompat:appcompat-resources:1.7.0-alpha02`are released.[Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..7d3ac1ab1206c01fae3ebb500b5b942636070155/appcompat)

**Bug Fixes**

- Fixed a memory leak in`AppCompatDelegate.getLocaleManagerForApplication()`([44b57fd](https://android.googlesource.com/platform/frameworks/support/+/44b57fdf82a60828a67be98be7bf1221f6f04a9f))
- `AppCompat`now depends on Fragment version 1.5.4 ([I54dcd](https://android-review.googlesource.com/#/q/I54dcd5bc370b3835215ae76a4726013849f1344f))

### Version 1.7.0-alpha01

October 5, 2022

`androidx.appcompat:appcompat:1.7.0-alpha01`and`androidx.appcompat:appcompat-resources:1.7.0-alpha01`are released.[Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cb1f3b62a11fbe655951402b7e04cd65b79d4209..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/appcompat)

**Bug Fixes**

- `AppCompatActivity`now sets the`ViewTreeOnBackPressedDispatcherOwner`so that it is possible to retrieve the dispatcher from the view. ([I1a115](https://android-review.googlesource.com/#/q/I1a115d42a68a37bab113927e9e6975f1a83b2b54),[b/235416503](https://issuetracker.google.com/issues/235416503))
- `Locale.getDefault()`now returns the system locale after a cold start ([I6a94b](https://android-review.googlesource.com/#/q/I6a94bcd50611551bf39b4e83edf9146baa2eddd5))
- `LinearLayoutCompat`now preserves margin layout params ([Id2af4](https://android-review.googlesource.com/#/q/Id2af4ca48dd192ae01fc569a8d9298cf40d3378c))

## Version 1.6.1

### Version 1.6.1

February 8, 2023

`androidx.appcompat:appcompat:1.6.1`and`androidx.appcompat:appcompat-resources:1.6.1`are released.[Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df6065a09f422100fee98ee050457db71d43f0bb..481dd991240c3469339ec7b93fc74dcabd4f6656/appcompat)

**Bug Fixes**

- Fixed a memory leak in`AppCompatDelegate.getLocaleManagerForApplication()`([44b57fd](https://android.googlesource.com/platform/frameworks/support/+/44b57fdf82a60828a67be98be7bf1221f6f04a9f))

## Version 1.6.0

### Version 1.6.0

January 11, 2023

`androidx.appcompat:appcompat:1.6.0`and`androidx.appcompat:appcompat-resources:1.6.0`are released.[Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df6065a09f422100fee98ee050457db71d43f0bb/appcompat)

**Important changes since 1.5.0**

- Added support for customizing application locales. See[`AppCompatDelegate.setApplicationLocales(LocaleListCompat)`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setApplicationLocales(androidx.core.os.LocaleListCompat))for more information. Provides backward compatibility for the new[per-language preferences API](https://developer.android.com/about/versions/13/features#language-support)available in Android 13.
- Nullability updates to align with Android 13 (Tiramisu, API level 33) SDK.
- Added`DrawableWrapper`,`DrawableContainer`, and`StateListDrawable`compat classes to public API surface

### Version 1.6.0-rc01

September 7, 2022

`androidx.appcompat:appcompat:1.6.0-rc01`and`androidx.appcompat:appcompat-resources:1.6.0-rc01`are released.[Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..cb1f3b62a11fbe655951402b7e04cd65b79d4209/appcompat)

**Bug Fixes**

- `AppCompatActivity`now sets the`ViewTreeOnBackPressedDispatcherOwner`so that it is possible to retrieve the dispatcher from the view. ([I1a115](https://android-review.googlesource.com/#/q/I1a115d42a68a37bab113927e9e6975f1a83b2b54),[b/235416503](https://issuetracker.google.com/issues/235416503))
- Reverted a bug fix that overwrote the configuration passed to`onConfigurationChanged`, which had caused issues for tests that injected their own custom configurations through`onConfigurationChanged`.

### Version 1.6.0-beta01

August 10, 2022

`androidx.appcompat:appcompat:1.6.0-beta01`and`androidx.appcompat:appcompat-resources:1.6.0-beta01`are released.[Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf7759d18327857b729c79132e67a91caa382827..bea814b246f89ff7244e3c6b0648f0b57e47897c/appcompat)

**API Changes**

- Move`DrawableWrapper`,`DrawableContainer`, and`StateListDrawable`compat classes to public API. ([I37f3e](https://android-review.googlesource.com/#/q/I37f3e188d926628853c3ef37ce7a32f28afd2823),[b/227789566](https://issuetracker.google.com/issues/227789566))
- Introduces a new factory for async layout inflater. ([Ia657b](https://android-review.googlesource.com/#/q/Ia657bc7de559a907465deb12a30671c53cdcea29))

**Bug Fixes**

- `Toolbar`will now call`onPrepareMenu()`before the menu is shown instead of unconditionally when the menu is created. ([I2a58d](https://android-review.googlesource.com/#/q/I2a58df0064c08b9ae87962a41d87e7bc60073df0),[b/232206677](https://issuetracker.google.com/issues/232206677))
- `AppCompat`now explicitly depends on`Lifecycle``2.5.1`and`SavedState``1.2.0`. ([I7e3e2](https://android-review.googlesource.com/#/q/I7e3e2cfbaec7fbca3b82c67ebd0c52bb60d7fd3e))
- Added support for back invoked callback to`AppCompatDelegate`and the`AppCompat`-provided Toolbar implementation. ([I24062](https://android-review.googlesource.com/#/q/I24062366905a266018caa9476a272e13cc9b099b))
- Finalize`AppCompat`APIs for 1.5.0-beta01 ([I2a43d](https://android-review.googlesource.com/#/q/I2a43d45452aef36c958e780c0678b2f62738b1f1),[b/236866227](https://issuetracker.google.com/issues/236866227))
- Finalize`AppCompat`APIs for 1.5.0-beta01 ([I2a43d](https://android-review.googlesource.com/#/q/I2a43d45452aef36c958e780c0678b2f62738b1f1),[b/236866227](https://issuetracker.google.com/issues/236866227))

### Version 1.6.0-alpha05

June 15, 2022

`androidx.appcompat:appcompat:1.6.0-alpha05`and`androidx.appcompat:appcompat-resources:1.6.0-alpha05`are released. Version 1.6.0-alpha05 was developed in a private pre-release branch and has no public commits.

**API Changes**

- Nullability updates to align with finalized API surface in Tiramisu Beta 3 SDK
- `minCompileSdk`is now 33 to align with Tiramisu Beta 3 SDK

### Version 1.6.0-alpha04

May 18, 2022

`androidx.appcompat:appcompat:1.6.0-alpha04`and`androidx.appcompat:appcompat-resources:1.6.0-alpha04`are released. This library was developed against a private pre-release branch, so no commit log is available.

**API Changes**

- Add an API to override SwitchCompat width restriction for use by MDC-Android

**Bug Fixes**

- Avoid managed configuration when config changes outside of attachBaseConfig

### Version 1.6.0-alpha03

April 27, 2022

`androidx.appcompat:appcompat:1.6.0-alpha03`and`androidx.appcompat:appcompat-resources:1.6.0-alpha03`are released.

This version requires Android 13 Beta 1 to compile and is not guaranteed to be runtime-compatible with future developer previews.

**New Features**

- Support for app-wide custom language selection via`AppCompatDelegate.setApplicationLocales()`. Delegates to platform implementation on API 33 and above.

### Version 1.6.0-alpha01

February 23, 2022

`androidx.appcompat:appcompat:1.6.0-alpha01`and`androidx.appcompat:appcompat-resources:1.6.0-alpha01`are released. Version 1.6.0-alpha01 was built from an internal branch and does not have publicly-visible commits.

This version requires Android Tiramisu DP1 to compile and is not guaranteed to be runtime-compatible with future developer previews.

**New Features**

- Added support for customizing application locales. See`AppCompatDelegate.setApplicationLocales(LocaleListCompat)`for more information. Provides backward compatibility for the new[per-language preferences API](https://developer.android.com/about/versions/13/features#language-support)available in Android 13.

## Version 1.5.1

### Version 1.5.1

September 7, 2022

`androidx.appcompat:appcompat:1.5.1`and`androidx.appcompat:appcompat-resources:1.5.1`are released.[Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/21fdaad0b74e5f72570329d6aca239ede156c3e3..54a023bc37778d1c0f38750da984339df2707edc/appcompat)

**Dependency Updates**

- `AppCompat`now explicitly depends on[Lifecycle`2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1)and[SavedState`1.2.0`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.2.0). ([I7e3e2](https://android-review.googlesource.com/#/q/I7e3e2cfbaec7fbca3b82c67ebd0c52bb60d7fd3e))

## Version 1.5.0

### Version 1.5.0

August 10, 2022

`androidx.appcompat:appcompat:1.5.0`and`androidx.appcompat:appcompat-resources:1.5.0`are released.[Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/26699d311c26986b4c92aed8ec6b79f7006910ee..21fdaad0b74e5f72570329d6aca239ede156c3e3/appcompat)

**Important changes since 1.4.0**

- This stable version includes improvements to night mode stability, bug fixes and compound drawable tinting support for AppCompat-backed text widgets, and improvements to API usability. See previous 1.5.0-series release notes for a detailed list of changes.

### Version 1.5.0-rc01

July 27, 2022

`androidx.appcompat:appcompat:1.5.0-rc01`and`androidx.appcompat:appcompat-resources:1.5.0-rc01`are released.[Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8fda1c7005de1555e6ae9b7a1ae5657c3b91eba7..26699d311c26986b4c92aed8ec6b79f7006910ee/appcompat)

**Bug Fixes**

- Fixes an issue where AppCompat's context wrapper reused the application context's backing resource implementation, resulting in`uiMode`being overwritten on the application context. ([Idf9d5](https://android-review.googlesource.com/c/platform/frameworks/support/+/2137592))

### Version 1.5.0-beta01

July 13, 2022

`androidx.appcompat:appcompat:1.5.0-beta01`and`androidx.appcompat:appcompat-resources:1.5.0-beta01`are released.[Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..8fda1c7005de1555e6ae9b7a1ae5657c3b91eba7/appcompat)

**API Changes**

- Add an overridable flag to disable the default switch width adjustment. ([I37cb7](https://android-review.googlesource.com/#/q/I37cb751f335e5388d09afdd3aafa91a47bd4d4b9))
- Add`@FloatRange`annotation to thumb position getter API ([If524c](https://android-review.googlesource.com/#/q/If524cd6196636c1dae353c6b7261f5136a3aa180))
- Add missing nullability annotations to`AnimatedStateListDrawableCompat`([Ieb4ec](https://android-review.googlesource.com/#/q/Ieb4ec34c6bb43fb18a74e495fb322c65123883f3))

**Bug Fixes**

- Finalize`AppCompat`APIs for 1.5.0-beta01 ([I2a43d](https://android-review.googlesource.com/#/q/I2a43d45452aef36c958e780c0678b2f62738b1f1),[b/236866227](https://issuetracker.google.com/issues/236866227))
- Changing`className`value for`ActionMenuItemView`to treat it as a`Button`([I5ee1c](https://android-review.googlesource.com/#/q/I5ee1c4f0d26e49c647a823a6d9b7ed32007d8441))

### Version 1.5.0-alpha01

April 6, 2022

`androidx.appcompat:appcompat:1.5.0-alpha01`and`androidx.appcompat:appcompat-resources:1.5.0-alpha01`are released.[Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ee4b677c2e41c7da3fb4de56f3a4457b8ff1145..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/appcompat)

**API Changes**

- Added a new API to expose switch thumb's position to subclasses ([I9bfb4](https://android-review.googlesource.com/#/q/I9bfb4d40249f5f73122417b40669dc1b6a3d4cc2))
- Updated nullability to match Tiramisu DP2 ([I0cbb7](https://android-review.googlesource.com/#/q/I0cbb7f22651e725a4bb36d20388a949a72cc5903))
- Backported compound drawable tinting to TextView-derived widgets ([Idf98c](https://android-review.googlesource.com/#/q/Idf98ced324a724a5cb5b9d5a2f397a3b82fad900),[b/165822337](https://issuetracker.google.com/issues/165822337))
- `AppCompatDialog`now extends`ComponentDialog`for compatibility with`OnBackPressedDispatcher`([Id9b91](https://android-review.googlesource.com/#/q/Id9b9103a07564ea6d8ebbd4c0285a41ffae0b6d1),[b/217620781](https://issuetracker.google.com/issues/217620781))
- `SearchView.onQueryRefine()`is now protected visibility to allow overrides ([I6cce0](https://android-review.googlesource.com/#/q/I6cce0f178402b8952f2510fb2369d5e845bdf9a5),[b/212882845](https://issuetracker.google.com/issues/212882845))

**Bug Fixes**

- AppCompat`Toolbar`now calls`MenuHostHelper`'s`onPrepareMenu()`API. ([I9b9b5](https://android-review.googlesource.com/#/q/I9b9b57a4ffcfb94bc24a881705ec5ea4d42736da),[b/227376894](https://issuetracker.google.com/issues/227376894))
- `AppCompatEditText`,`AppCompatAutoCompleteEditText`,`AppCompatMultiAutoCompleteEditText`will no longer reset clickable or longClickable in the constructor when set in XML ([Ic5066](https://android-review.googlesource.com/#/q/Ic5066da9059eab40e3c2bff7c16edc5037430c12),[b/221094907](https://issuetracker.google.com/issues/221094907))
- `AppCompatEditText`,`AppCompatAutoCompleteTextView`, and`AppCompatMultiAutoCompleteTextView`will not call overridden`setKeyListener`during the constructor ([I5c13a](https://android-review.googlesource.com/#/q/I5c13aa13569e9a916a4af097153da40cbcf27366),[b/208480173](https://issuetracker.google.com/issues/208480173))
- Appcompat will not wrap instances of`NumberKeyListener`passed to`setKeyListener`, allowing`TextView`to correctly configure the locale on`NumberKeyListeners`([Ibf113](https://android-review.googlesource.com/#/q/Ibf113081112d05c75937eec5bc87904ebf450b26),[b/207119921](https://issuetracker.google.com/issues/207119921))
- Fixed issue with all`NumberKeyListener`subclasses introduced in AppCompat 1.4.0 that allowed unexpected characters such as punctuation to be input ([Iede7a](https://android-review.googlesource.com/#/q/Iede7af5e0599d29fd4cee78a798d5bcb07e1ab97),[b/207119921](https://issuetracker.google.com/issues/207119921))

## Version 1.4.2

### Version 1.4.2

June 1, 2022

`androidx.appcompat:appcompat:1.4.2`and`androidx.appcompat:appcompat-resources:1.4.2`are released.[Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ee4b677c2e41c7da3fb4de56f3a4457b8ff1145..228e563d8fdb0b2edcfc5a6ac230f7942c555c40/appcompat)

**Bug Fixes**

- Fix crash where`AppCompatDelegateImpl`made an internal call to`ensureSubDecor`before the action bar was created ([aosp/2048349](https://android-review.googlesource.com/c/platform/frameworks/support/+/2048349),[b/226648941](https://issuetracker.google.com/226648941))

## Version 1.4.1

January 12, 2022

`androidx.appcompat:appcompat:1.4.1`and`androidx.appcompat:appcompat-resources:1.4.1`are released.[Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/672db1aaa8de1bff350413baddb7640e2cd627d1..5ee4b677c2e41c7da3fb4de56f3a4457b8ff1145/appcompat)

**Bug Fixes**

- `AppCompatEditText`,`AppCompatAutoCompleteTextView`, and`AppCompatMultiAutoCompleteTextView`will not call overriden`setKeyListener`during the constructor. ([I5c13a](https://android-review.googlesource.com/#/q/I5c13aa13569e9a916a4af097153da40cbcf27366),[b/208480173](https://issuetracker.google.com/issues/208480173))
- `Emoji2`will not wrap instances of`NumberKeyListener`, allowing the locale to be configured by textview.
  - Appcompat will not wrap instances of`NumberKeyListener`passed to`setKeyListener`, allowing`TextView`to correctly configure the locale on`NumberKeyListeners`. ([Ibf113](https://android-review.googlesource.com/#/q/Ibf113081112d05c75937eec5bc87904ebf450b26),[b/207119921](https://issuetracker.google.com/issues/207119921))
- Fixes issue with all`NumberKeyListener`subclasses introduced in appcompat 1.4.0 that allowed unexpected characters such as punctuation to be input (b/207119921) ([Iede7a](https://android-review.googlesource.com/#/q/Iede7af5e0599d29fd4cee78a798d5bcb07e1ab97),[b/207119921](https://issuetracker.google.com/issues/207119921))

## Version 1.4.0

### Version 1.4.0

November 17, 2021

`androidx.appcompat:appcompat:1.4.0`and`androidx.appcompat:appcompat-resources:1.4.0`are released.[Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/88bc2c8e95a4edeecf71e5b2a14a8d736bdda9f2..672db1aaa8de1bff350413baddb7640e2cd627d1/appcompat)

**Important changes since 1.3.0**

- Library is now targeting Java 8 language level
- Updatable emoji support is enabled by default via the androidx.emoji2 library
- Improved attribute inspection in Android Studio's Layout Inspector ([I02d55](https://android-review.googlesource.com/#/q/I02d558e01c1e64335d190329c5a26372e17ef802))
- Added support for nested tinted resources and vector drawables in AppCompat resource loading backports. Note, however, that this means apps cannot override getDrawable() on a custom Resources object when backports are enabled. ([Ia6b03](https://android-review.googlesource.com/#/q/Ia6b034d5143311a111c31d59afbb37dbeeea2131),[b/176129022](https://issuetracker.google.com/issues/176129022))
- Backported tintable background and check mark for CheckedTextView ([I8575c](https://android-review.googlesource.com/#/q/I8575c5c23240a14153654ffafd0387fa89f2a3bc))

### Version 1.4.0-rc01

October 27, 2021

`androidx.appcompat:appcompat:1.4.0-rc01`and`androidx.appcompat:appcompat-resources:1.4.0-rc01`are released.[Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/418e77ded6b319212f986a3d211532a4b89f2468..88bc2c8e95a4edeecf71e5b2a14a8d736bdda9f2/appcompat)

### Version 1.4.0-beta01

September 29, 2021

`androidx.appcompat:appcompat:1.4.0-beta01`and`androidx.appcompat:appcompat-resources:1.4.0-beta01`are released.[Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/appcompat)

**API Changes**

- AndroidX AppCompat`Toolbar`is now a`MenuHost`and can manage`MenuProvider`s. ([I5cd95](https://android-review.googlesource.com/#/q/I5cd950583f938a8bf689cc6de517abbb7aa6bc36))

**Bug Fixes**

- Fixed AppCompatProgressBar handling of layer-list progress bars ([I6ece3](https://android-review.googlesource.com/#/q/I6ece3fa57734308b3fbd8c8d704eaf5c79c5d5de),[b/142004509](https://issuetracker.google.com/issues/142004509))
- Correctly retain`android:digits`in`AppCompatEditText`, this fixes bug 193047889 introduced in AppCompat 1.4.0-alpha03. ([I4b4fc](https://android-review.googlesource.com/#/q/I4b4fc1ccc429724743cab8a965d7e3adec356fd1),[b/193047889](https://issuetracker.google.com/issues/193047889))
- Integrated OnReceiveContentListener SDK and support lib APIs. ([Ic6914](https://android-review.googlesource.com/#/q/Ic6914c23688b4165c81ffa19a7dbce89d52bffcd),[b/173814913](https://issuetracker.google.com/issues/173814913))

### Version 1.4.0-alpha03

June 30, 2021

`androidx.appcompat:appcompat:1.4.0-alpha03`and`androidx.appcompat:appcompat-resources:1.4.0-alpha03`are released.[Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/appcompat)

**New Features**

- Library is now targeting Java 8 language level
- Add emoji2 support for more TextView subclasses (`AppCompatMultiAutoCompleteTextView`,`AppCompatAutoCompleteTextView`,`AppCompatRadioButton`,`AppCompatCheckBox`).

**API Changes**

- Added an API to configure an InputConnection to use View.performReceiveContent to handle IME calls to InputConnection.commitContent. ([I3a2ad](https://android-review.googlesource.com/#/q/I3a2ad7604145a6aba74ee7a020075f0bd3ecc266))
- Add support for EmojiCompat to`AppCompatMultiAutoCompleteTextView`([Ifece0](https://android-review.googlesource.com/#/q/Ifece0df417fedeb399f0412e732b2c197315e365))
- Add support for EmojiCompat to`AppCompatAutoCompleteTextView`([Ia1f4b](https://android-review.googlesource.com/#/q/Ia1f4b630270b4ffe4c3feb4e7c28cb4aa58fc821))
- Add support for EmojiCompat to`AppCompatRadioButton`([If08af](https://android-review.googlesource.com/#/q/If08afc3259a96d29713b75eb5066746c1810e8a9))
- Add support for EmojiCompat to`AppCompatCheckBox`([I2b3bc](https://android-review.googlesource.com/#/q/I2b3bc191bc2504d5dd83edf4735521cc2197e9d4))
- Allow null`KeyListener`in`AppCompatEditText`. This reverses the non-null annotation that was added to AppCompatEditText in 1.4-alpha01 and restores the previous behavior when passed null. ([I21482](https://android-review.googlesource.com/#/q/I214824131c0206349b73471a8c22be38bf5dd0d8),[b/189559345](https://issuetracker.google.com/issues/189559345))
- Add`PopupMenu.setForceShowIcon`for parity with platform APIs ([I43bb3](https://android-review.googlesource.com/#/q/I43bb3546cc529051e4b88e14438a9e77e8b1b177),[b/182789798](https://issuetracker.google.com/issues/182789798))

**Bug Fixes**

- Fix bug in AppCompatEditText that will reset the inputType specified in XML to remove variations. This bug was introduced in AppCompat 1.4.0-alpha01. ([I9df36](https://android-review.googlesource.com/#/q/I9df3655f05312806c46875e9d5603fe48154dd8e),[b/191061070](https://issuetracker.google.com/issues/191061070))

### Version 1.4.0-alpha02

June 2, 2021

`androidx.appcompat:appcompat:1.4.0-alpha02`and`androidx.appcompat:appcompat-resources:1.4.0-alpha02`are released.[Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/appcompat)

**API Changes**

- Added`AppCompatDialogFragment`constructor that takes a layout ID ([Icbf22](https://android-review.googlesource.com/#/q/Icbf22da2f79aa902756a8e2e319efa5a0d92bdde),[b/188119987](https://issuetracker.google.com/issues/188119987))
- Improved layout inspector support ([I02d55](https://android-review.googlesource.com/#/q/I02d558e01c1e64335d190329c5a26372e17ef802))
- Renamed package in`emoji2-views-helper`to`androidx.emoji2.viewsintegration`. This is a breaking change for AppCompat`1.4.0-alpha01`, and apps must ensure AppCompat dependency is updated to use the new emoji2 version. ([Ie8397](https://android-review.googlesource.com/#/q/Ie83972affa2281616923620e1642964eead49b4e))

**Bug Fixes**

- Fixed issue where stopped activities did not receive configuration changes from AppCompat-instrumented night mode changes. ([I8fa8f](https://android-review.googlesource.com/#/q/I8fa8fbc2849499de9cd8af2b77726f7081a37139),[b/188681415](https://issuetracker.google.com/issues/188681415))
- Fixed bug in`AppCompatEditText`which would cause views to be focusable even when`android:focusable="false"`was specified in the xml (bug introduced in AppCompat`1.4.0-alpha01`) ([Ib9412](https://android-review.googlesource.com/#/q/Ib94127fc4c6f7fcef5d9bc8652bd9c86bcdfe42b))

### Version 1.4.0-alpha01

May 18, 2021

`androidx.appcompat:appcompat:1.4.0-alpha01`and`androidx.appcompat:appcompat-resources:1.4.0-alpha01`are released.[Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3908fb8ddc16c8cb0a7603c3cce0ca7ea8a5076a..66681ad83c328d0dd821b943bb3d375f02c1db61/appcompat)

**API Changes**

- Integrated EmojiCompat support to a variety of AppCompat widgets ([Id409b](https://android-review.googlesource.com/#/q/Id409bc24e172446ce8ddb2db8dd80fb2b238c7af),[If7a1a](https://android-review.googlesource.com/#/q/If7a1add31a3ac8a2c2503a354cc7187e8cf118d4),[Ic262d](https://android-review.googlesource.com/#/q/Ic262df79e5f11a5e3acb3a2078956834c84d8324),[Ib5f4a](https://android-review.googlesource.com/#/q/Ib5f4a60f7f8321a4c3495008efc458b1ee03992c),[I4fb3c](https://android-review.googlesource.com/#/q/I4fb3ce9259064a55b4c1ee6a5f0fccf72aa4f9a4))
- Added support for nested tinted resources and vector drawables in AppCompat resource loading backports. Note, however, that this means apps cannot override`getDrawable()`on a custom Resources object when backports are enabled. ([Ia6b03](https://android-review.googlesource.com/#/q/Ia6b034d5143311a111c31d59afbb37dbeeea2131),[b/176129022](https://issuetracker.google.com/issues/176129022))
- Improved layout inspector support ([I6d771](https://android-review.googlesource.com/#/q/I6d77175d77c65e224177679055eb2ddfdfd7d7ae))

**Bug Fixes**

- Fixed a scenario where calling setSupportActionBar after setting the window callback would overwrite the callback. ([Ie43ee](https://android-review.googlesource.com/#/q/Ie43eedf8322caa44e7b201a95cbc64197953e020),[b/186791590](https://issuetracker.google.com/issues/186791590))
- Added a workaround for an issue on SDKs 29 and 30 where ColorStateListDrawable resources cloned from the drawable cache don't load a default color until they receive a state change. ([Iedb4b](https://android-review.googlesource.com/#/q/Iedb4b99763a1c33fecaef7fdc1f68ce9c4baca70))
- Avoid NPE when handling null custom selection action mode callbacks on AppCompat-backed views. ([I033c7](https://android-review.googlesource.com/#/q/I033c712ffa477853f122788f2335e7cab9a877fb),[b/173435375](https://issuetracker.google.com/issues/173435375))

**Dependency Updates**

- From[AppCompat`1.5.0`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.5.0): AppCompat now depends on Fragment[Fragment`1.3.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4). ([I13089](https://android-review.googlesource.com/#/q/I13089bfa891650845dbbf844215131d2b089f30e))
- From[AppCompat`1.5.0`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.5.0): AppCompat now depends on[Activity`1.2.3`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.3). ([I815b7](https://android-review.googlesource.com/#/q/I815b7412e1a9f8b2530a5b576f023f9f134116e8))
- From[AppCompat`1.5.0`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.5.0): AppCompat now depends on[Lifecycle`2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1). ([Ia75a1](https://android-review.googlesource.com/#/q/Ia75a16f05e4144bd7bc6d06018620e46f37378b0))

**External Contribution**

- Backport tintable background and check mark for`CheckedTextView`([I8575c](https://android-review.googlesource.com/#/q/I8575c5c23240a14153654ffafd0387fa89f2a3bc))

## Version 1.3.1

### Version 1.3.1

July 21, 2021

`androidx.appcompat:appcompat:1.3.1`and`androidx.appcompat:appcompat-resources:1.3.1`are released.[Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d95b070080d7877a6bcacca6ba04acd28c0b5d79..917b374627def8db1abcc7f1e1160aff596171f8/appcompat)

**Dependency updates**

- AppCompat now depends on[Activity`1.2.4`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.4)and[Fragment`1.3.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.6), making the fixes from those releases included by default when using AppCompat`1.3.1`. ([I8fbec](https://android-review.googlesource.com/#/q/I8fbecaffdb3a74946a8bf938f1c2722910499b34))

## Version 1.3.0

### Version 1.3.0

May 18, 2021

`androidx.appcompat:appcompat:1.3.0`and`androidx.appcompat:appcompat-resources:1.3.0`are released.[Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3908fb8ddc16c8cb0a7603c3cce0ca7ea8a5076a..d95b070080d7877a6bcacca6ba04acd28c0b5d79/appcompat)

**Important changes since 1.2.0**

- Fixed propagation of`android:theme`attributes across`<include>`d layouts on pre-Lollipop devices
- Reduced library size by converting many PNG resources to VectorDrawables
- Added support for drag-and-drop events to`AppCompatEditText`with`OnReceiveContentListener`
- Updated to support changes to Android 11 window inset handling
- Added support for RTL in menu items with icons
- Added support for inserting rich content (ex. pasting an image) in`AppCompatEditText`

- **Updated dependencies** :`appcompat`updated many of its transitive dependencies to support new functionality and fixes:

  - Updated from Fragment`1.1.0`to[Fragment`1.3.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4)
  - Updated from Activity 1.0.0 to[Activity`1.2.3`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.3)
  - Updated from Lifecycle`2.0.0`to[Lifecycle`2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1).
  - Updated from Core 1.3.0 to[Core`1.5.0`](https://developer.android.com/jetpack/androidx/releases/core#1.5.0)

### Version 1.3.0-rc01

March 24, 2021

`androidx.appcompat:appcompat:1.3.0-rc01`and`androidx.appcompat:appcompat-resources:1.3.0-rc01`are released.[Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..d4cb15fdc3d603b2628e4bfe9c57a72dea59b7e8/appcompat)

**Bug Fixes**

- Prevents permissions from being revoked prematurely when handling IME content insertion

**Dependency Updates**

- AppCompat now depends on[Activity`1.2.2`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.2),[Fragment`1.3.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.2), and[Lifecycle`2.3.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1). ([Ia75a1](https://android-review.googlesource.com/#/q/Ia75a16f05e4144bd7bc6d06018620e46f37378b0))

**External Contribution**

- Fixed propagation of`android:theme`attribute across`<include>`d layouts on pre-Lollipop devices (Simon Bergner at Opera)

### Version 1.3.0-beta01

January 13, 2021

`androidx.appcompat:appcompat:1.3.0-beta01`and`androidx.appcompat:appcompat-resources:1.3.0-beta01`are released.[Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..6207afb1646d302c5d29c2c67d332b48db87fb27/appcompat)

**New Features**

- Theme-level action mode drawables have been replaced with vector sources. This may cause slight changes in the visual appearance of individual icons. ([I741a6](https://android-review.googlesource.com/#/q/I741a66371ef5f55f9c33901a1c06335f7546e3e7))

**API Changes**

- Integrated drag-and-drop (drop events) in AppCompatEditText with OnReceiveContentListener. ([Ib26c9](https://android-review.googlesource.com/#/q/Ib26c90d51e2087e7c134dfc9331371745bfaf3ab),[b/175343405](https://issuetracker.google.com/issues/175343405))
- Updated`OnReceiveContentListener`and related APIs. See androidx.core library changes for more details. ([Ib4616](https://android-review.googlesource.com/#/q/Ib4616cb0d0cd9f8537b64de6fcc19b80442dc3fb),[b/173814913](https://issuetracker.google.com/issues/173814913))
- Moved widget.RichContentReceiverCompat to view.OnReceiveContentListener. ([Ifdab7](https://android-review.googlesource.com/#/q/Ifdab76f135e840a15430634a22e720947be4eecd),[b/173814913](https://issuetracker.google.com/issues/173814913))
- APIs to supply and retrieve initial surrounding text have been backported to`EditorInfoCompat`. They allow IME apps to avoid additional IPC latency. ([Ie3809](https://android-review.googlesource.com/#/q/Ie380919ac99373ec59f2b7162a13ab0a48e9b6bc))

### Version 1.3.0-alpha02

August 19, 2020

`androidx.appcompat:appcompat:1.3.0-alpha02`and`androidx.appcompat:appcompat-resources:1.3.0-alpha02`are released.[Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..96eb302ee1740ba656c90c9fb27df3723a1a89c1/appcompat)

**Bug Fixes**

- AppCompatRatingBar PNG drawables have been replaced with vector sources. This may cause slight changes in the visual appearance of individual stars. ([I6b99d](https://android-review.googlesource.com/#/q/I6b99d3fde8d3cd275d0fc279324066bcd7f3ecd6))
- Update WindowInsetsCompat to Android 11 APIs ([I3df9e](https://android-review.googlesource.com/#/q/I3df9e889650db916c48d5567a9bcf9c7a7b9aa85))
- Support RTL in menu items with icons ([I2f5c5](https://android-review.googlesource.com/#/q/I2f5c53696cb6e43e71c64cc7ed50c64b64cb196b))

**Dependency Updates**

- AppCompat has updated its dependency from Fragment`1.1.0`to[Fragment`1.3.0-alpha08`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha08). It is strongly recommended to read through the[Fragment`1.2.0`release notes](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)to understand the major changes introduced in the previous Fragment release.
- AppCompat has updated its dependency from Activity`1.0.0`to[Activity`1.2.0-alpha08`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha08). It is strongly recommended to read through the[Activity`1.1.0`release notes](https://developer.android.com/jetpack/androidx/releases/activity#1.1.0)to understand the major changes introduced in the previous Activity release.
  - `AppCompatActivity`now uses the`OnContextAvailableListener`API introduced in[Activity`1.2.0-alpha08`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha08)to set up the`AppCompatDelegate`. Any listeners added to subclasses of`AppCompatActivity`will run after this listener. ([I513da](https://android-review.googlesource.com/#/q/I513da73bc0862b62af4166be35ba353fc7869a09))

### Version 1.3.0-alpha01

May 20, 2020

`androidx.appcompat:appcompat:1.3.0-alpha01`and`androidx.appcompat:appcompat-resources:1.3.0-alpha01`are released.[Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..ccc6e95c574b66563952c33fbe26888b93a0e0cb/appcompat)

**New Features**

- Add a new Lint rule to flag calls to setActionBar on activities that extend AppCompatActivity
- Added support for`ViewTreeLifecycleOwner`from[Lifecycle`2.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha03),`ViewTreeViewModelStoreOwner`from[Lifecycle`2.3.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha01), and`ViewTreeSavedStateRegistryOwner`from[SavedState`1.1.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.1.0-alpha01)when using a`View`within an`AppCompatActivity`. ([b/151603528](https://issuetracker.google.com/issues/151603528),[aosp/1300264](https://android-review.googlesource.com/1300264/))
- Add common API for inserting rich content (e.g. pasting an image). The new callback provides a single API that apps can implement to support the different ways in which rich content may be inserted. For now the API is only added to`AppCompatEditText`and will be invoked for the following code paths:
  - paste from the clipboard
  - content insertion from the IME (`InputConnection.commitContent`) ([I22bf7](https://android-review.googlesource.com/#/q/I22bf76a22b795cb47c7ab12e4f5b529fff8fe5d7))

**Bug Fixes**

- From[AppCompat`1.2.0-rc01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.2.0-rc01): AppCompat no longer calls`onMenuOpened()`with a`null`menu. ([b/142843126](https://issuetracker.google.com/issues/142843126))
- Correctly resolve text link and hint colors on older devices when TextViewCompat.setTextAppearance is called with a text appearance style that has color state lists that reference theme color attributes ([b/154702995](https://issuetracker.google.com/issues/154702995))

## Version 1.2.0

### Version 1.2.0

August 5, 2020

`androidx.appcompat:appcompat:1.2.0`and`androidx.appcompat:appcompat-resources:1.2.0`are released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bbd41773d22c3cf76f582de6a786af86ac4827ef..d11577a0f2ebc8136b9df9df42fce64e0f30b32d/appcompat)

**Major changes since 1.1.0**

- Fixed support for Configuration override use cases, including custom locales and font scales. See[here](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:appcompat/appcompat/src/androidTest/java/androidx/appcompat/app/NightModeCustomApplyOverrideConfigurationActivity.java)for an example of how to correctly implement overrides using`appcompat:1.2.0`.
- Deprecated`AppCompatDelegate.attachBaseContext()`. If you are calling or overriding this method, use`AppCompatDelegate.attachBaseContext2()`instead.
- Deprecated`CollapsibleActionView`. This interface is no longer needed, use the platform-provided`android.view.CollapsibleActionView`interface.

### Version 1.2.0-rc02

July 22, 2020

`androidx.appcompat:appcompat:1.2.0-rc02`and`androidx.appcompat:appcompat-resources:1.2.0-rc02`are released.[Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/545321a76241d2243b1c20be27fdfde2a6b507c7..bbd41773d22c3cf76f582de6a786af86ac4827ef/appcompat)

**Bug Fixes**

- Fixed an issue related to night mode where calling`AppCompatDelegate.setDefaultNightMode`from a dialog would occasionally fail to recreate activities and apply the new mode. ([aosp/1348308](https://android-review.googlesource.com/1348308),[b/158923881](https://issuetracker.google.com/158923881))

### Version 1.2.0-rc01

May 14, 2020

`androidx.appcompat:appcompat:1.2.0-rc01`and`androidx.appcompat:appcompat-resources:1.2.0-rc01`are released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..545321a76241d2243b1c20be27fdfde2a6b507c7/appcompat)

**API Changes**

- `AppCompatDelegate.setLocalNightMode`has been marked as requiring SDK version 17 or higher due to a platform issue with configuration changes leaking between Activities on earlier SDKs

**Bug Fixes**

- `AppCompatDelegate.setLocalNightMode`may now be called prior to`Activity.attachBaseContext`
- Fixed`ActionBarOverlayLayout`inset consumption which was incorrectly using the cached insets
- AppCompat no longer calls`onMenuOpened()`with a`null`menu. ([b/142843126](https://issuetracker.google.com/issues/142843126))

### Version 1.2.0-beta01

April 1, 2020

`androidx.appcompat:appcompat:1.2.0-beta01`and`androidx.appcompat:appcompat-resources:1.2.0-beta01`are released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/appcompat)

**New Features**

- Added the following new lint rules that will flag incorrect usages of AppCompat in the following scenarios:
  - Loading color state lists: suggests using`ContextCompat`and`AppCompatResources`APIs for backward compatibility
  - Loading drawables: suggests using`ContextCompat`and`ResourcesCompat`APIs for backward compatibility
  - Using color state lists with alpha attribute: flags missing`android:alpha`attribute that will lead to incorrect appearance on some platform versions
  - Tinting image views: flags not using`app:tint`that will lead to incorrect appearance on older platform versions
  - Using compound drawables and tinting on text views: suggests using compat attributes and APIs for backward compatibility

**Bug Fixes**

- Fixed an issue where`ActionBarOverlayLayout`(window decor action) was not dispatching WindowInsets correctly.
- Fixed issues in tinting drawables and text appearance on older versions of the platform
- Fixed an issue where`androidx.appcompat:appcompat:1.1.0`crashes webview when webview is long pressed ([b/141351441](https://issuetracker.google.com/issues/141351441))
- Implemented fixes for issues with base context manipulation and retrieving system services during activity start up

### Version 1.2.0-alpha03

March 4, 2020

`androidx.appcompat:appcompat:1.2.0-alpha03`and`androidx.appcompat:appcompat-resources:1.2.0-alpha03`are released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/741f4aed00efbd392b4c48a59b4cb06a599e6366..666ae665acfcfa2a20eccc18e4494808169742f4/appcompat)

**Bug Fixes**

- Fixed an issue where the action mode status guard mistakenly extends into the navigation bar and has the wrong color ([Ia4a09](https://android-review.googlesource.com/#/q/Ia4a09376aa020e806db61caa43b2941f9b6b2cea))
- Fix issue where stopped Activities were not resuming on API Level 23 and below ([I45201](https://android-review.googlesource.com/#/q/I45201c5c3946d6a126e3ed00a0235b175fccd870))

### Version 1.2.0-alpha02

January 29, 2020

`androidx.appcompat:appcompat:1.2.0-alpha02`and`androidx.appcompat:appcompat-resources:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce2902e01f920f17637879b6c918ffe987d2f35b..741f4aed00efbd392b4c48a59b4cb06a599e6366/appcompat).

**Bug fixes**

- Fixed issue where appcompat 1.1.0 crashes webview when long pressed ([b/141351441](https://issuetracker.google.com/141351441))
- Fixed drawable tinting on TextView relative to compound drawables on API Level 23 ([aosp/1172194](https://android-review.googlesource.com/c/platform/frameworks/support/+/1172194))
- Ensured the base context is always a wrapper ([aosp/1194355](https://android-review.googlesource.com/c/platform/frameworks/support/+/1194355))
- Added some improvements to be more clever when modifying the base context configuration ([aosp/1204543](https://android-review.googlesource.com/c/platform/frameworks/support/+/1204543))
- Disabled`createConfigurationContext()`for Robolectric ([aosp/1186218](https://android-review.googlesource.com/c/platform/frameworks/support/+/1186218))

### Version 1.2.0-alpha01

December 4, 2019

`androidx.appcompat:appcompat:1.2.0-alpha01`and`androidx.appcompat:appcompat-resources:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/f48ce15dc1716809f45fa761daa26ba7a838ca55..ce2902e01f920f17637879b6c918ffe987d2f35b/appcompat).

**Bug fixes**

- Calls to PackageManager.getActivityInfo don't crash anymore under strict mode with boot-aware checks enabled
- Fixes for tinting drawables on AppCompatButton
- Fixes for tinting and text appearance on older versions of the platform

## Version 1.1.0

### Version 1.1.0

September 5, 2019

`androidx.appcompat:appcompat:1.1.0`and`androidx.appcompat:appcompat-resources:1.1.0`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/16509068d2009cdd24134b48887e3d8abd6b7109..f48ce15dc1716809f45fa761daa26ba7a838ca55/appcompat).

**Important changes since 1.0.0**

- **Dark Mode Improvements** :`MODE_NIGHT_AUTO`and switching of dark/light based on the current time is now deprecated. Considering using an explicit setting, or`MODE_NIGHT_AUTO_BATTERY`.
- **Activity 1.0** :`AppCompatActivity`now transitively extends from`ComponentActivity`from[Activity`1.0.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.0.0)via[Fragment`1.1.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0). See the associated release notes for information on the changes in each library.
- **AppCompatActivity LayoutId constructor** : Subclasses of`AppCompatActivity`can now optionally call into a constructor on`AppCompatActivity`that takes an`R.layout`ID, indicating the layout that should be set as the content view as an alternative to calling`setContentView()`in`onCreate()`. This does not change the requirement that your subclass have a no-argument constructor.

### Version 1.1.0-rc01

July 2, 2019

`androidx.appcompat:appcompat:1.1.0-rc01`and`androidx.appcompat:appcompat-resources:1.1.0-rc01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/376680be19694e4b5615ff485a5ded82e68cb6db..16509068d2009cdd24134b48887e3d8abd6b7109/appcompat).
| **Note:** This version will only compile against the Q Beta 4 SDK.

**Bug fixes**

- DayNight now honors`configChanges`correctly ([aosp/981105](https://android-review.googlesource.com/981105))
- Only call`onConfigurationChanged`on started Activities ([aosp/987483](https://android-review.googlesource.com/987483))

### Version 1.1.0-beta01

June 5, 2019

`androidx.appcompat:appcompat:1.1.0-beta01`and`androidx.appcompat:appcompat-resources:1.1.0-beta01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311..376680be19694e4b5615ff485a5ded82e68cb6db/appcompat).

**Bug fixes**

- Make sure we clean up receivers in AppCompatDialogs ([aosp/959376](https://android-review.googlesource.com/c/959376))
- Add support for`buttonGravity=center_vertical`on Toolbar ([b/130361721](https://issuetracker.google.com/issues/130361721))
- Fix spinner horizontal offset ([b/79477181](https://issuetracker.google.com/issues/79477181))

### Version 1.1.0-alpha05

May 7, 2019

`androidx.appcompat:appcompat:1.1.0-alpha05`and`androidx.appcompat:appcompat-resources:1.1.0-alpha05`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/2f634eec2143acd6a4ea19a375a6e3877cdcc2ed..fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311/appcompat).

**New features**

- [setDefaultNightMode()](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate.html#setDefaultNightMode(int))now automatically recreates any started activities.

**Bug fixes**

- Various fixes to DayNight mode
- Invalidate outline on any background change in ActionBar
- Fix spinner widget scroll
- Fix custom set window backgrounds being overridden in AlertDialog

### Version 1.1.0-alpha04

April 3, 2019

`androidx.appcompat:appcompat:1.1.0-alpha04`and`androidx.appcompat:appcompat-resources:1.1.0-alpha04`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/9d3db78d753254e0f74f24480b2e6f4e6a380a06..2f634eec2143acd6a4ea19a375a6e3877cdcc2ed/appcompat).

**New features**

- Added new`ThemeOverlay.AppCompat.DayNight`family of themes. These should be used when using the DayNight feature.

**API changes**

- AppCompatActivity now contain a second constructor that takes a`@LayoutRes int`, which replaces the previous behavior of annotating your AppCompatActivity class with`@ContentView`. This approach works in both app and library modules. ([b/128352521](https://issuetracker.google.com/issues/128352521))

**Bug fixes**

- Pinned internal dependencies to stable versions where possible
- Fixed`AppCompatSpinner`scrolling in dropdown mode )[b/124274573](https://issuetracker.google.com/issues/124274573))
- Only calls`applyOverrideConfiguration()`if required for DayNight

### Version 1.1.0-alpha03

March 13, 2019

`androidx.appcompat:appcompat:1.1.0-alpha03`and`androidx.appcompat:appcompat-resources:1.1.0-alpha03`are released. This is the first release of`appcompat-resources`. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/871963fd9c70c32aa57a2587530654ac1c7595bb..9d3db78d753254e0f74f24480b2e6f4e6a380a06/appcompat).

**New features**

- The new appcompat-resources library contains APIs that allow apps to load and tint drawables (including vector drawables) on older versions of the platform. This is the same functionality that was previously part of the appcompat module, but is now available without the overhead of the full appcompat backport of Material design that includes widgets, dialogs, night mode etc.
- Major fixes to DayNight mode support
- New`MODE_NIGHT_AUTO_BATTERY`option for DayNight mode
- Drawable tinting in`AppCompatTextView`
- Toolbar overflow can now be styled with themed color state lists
- Menu icons can now use colors that reference theme attributes
- The new app:menu attribute can be set on a Toolbar to provide the menu content at inflation time

**Bug fixes**

- Fixed default tint mode on ImageView on version 21
- Fixed spinner popup incorrect dismissal on device rotation
- Fixed DayNight does not respect`configChanges`in manifest
- Fixed switching to`MODE_NIGHT_FOLLOW_SYSTEM`doesn't work ([b/111345020](https://issuetracker.google.com/issues/111345020))
- Fixed WebView resets DayNight Resources ([b/37124582](https://issuetracker.google.com/issues/37124582))

### Version 1.1.0-alpha02

February 7, 2019

`androidx.appcompat:appcompat 1.1.0-alpha02`is released.

**New features**

- Extracted resource-specific drawable handling into a hook ([aosp/870976](https://android-review.googlesource.com/870976))
- Allowed Toolbar`titleTextColor`and`subtitleTextColor`to use a`ColorStateList`and added`ColorStateList`overloads of the`setTitleTextColor`and`setSubtitleTextColor`methods ([aosp/867489](https://android-review.googlesource.com/867489))

**Bug fixes**

- Fixed`fontFamily`not working on pre API 24 ([aosp/807054](https://android-review.googlesource.com/807054))
- Fixed bug where`textFontWeight`did not work when an activity extends from`AppCompatActivity`([aosp/847640](https://android-review.googlesource.com/847640))
- Fixed bug that caused the title text on the spinner widget popup (when using dialog mode) to not use the font specified in the`fontFamily`([aosp/789994](https://android-review.googlesource.com/789994))
- Fix bug that prevented widgets`AppCompatCheckBox`and`AppCompatRadioButton`from be able to change the background tint ([aosp/825160](https://android-review.googlesource.com/825160))
- Fixed bug where AppCompat did not override`android: list styles`([aosp/862350](https://android-review.googlesource.com/862350))

### Version 1.1.0-alpha01

December 3, 2018

**New features**

- AppCompatTextView now supports`app:drawableLeftCompat`,`app:drawableTopCompat`,`app:drawableRightCompat`,`app:drawableBottomCompat`,`app:drawableStartCompat`and`app:drawableEndCompat`compound drawables, supporting backported drawable types such as`VectorDrawableCompat`.

- `AppCompatCheckBox`and`AppCompatRadioButton`'s default drawables now animate check state changes.

**API changes**

- [aosp/740385](https://android-review.googlesource.com/c/platform/frameworks/support/+/740385): ActionBarOverlayLayout now implements NestedScrollingParent2 and NestedScrollingParent3, enabling it to facilitate the latest functionality in nested scrolling 3. If developer code currently overrides`ActionBarOverLayLayout.onNestedScroll(View, int, int, int, int)`, it will likely no longer be called and`ActionBarOverLayLayout.onNestedScroll(View, int, int,
  int, int, int, int[])`should be overridden instead.

## Version 1.0.2

### Version 1.0.2

November 7, 2018

Bugfix release of`core-1.0.1`and`appcompat-1.0.2`.

**Bug fixes**

- Fixed bug where`PrecomputedTextCompat`would crash when used with RTL`AppCompatTextView`.[b/113070424](https://issuetracker.google.com/113070424)

## Version 1.0.0

### Version 1.0.0

November 7, 2018

**New features**

- [`AnimatedStateListDrawableCompat`](https://developer.android.com/reference/androidx/appcompat/graphics/drawable/AnimatedStateListDrawableCompat)provides animated transitions between drawable states.