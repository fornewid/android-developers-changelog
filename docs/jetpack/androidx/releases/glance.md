---
title: https://developer.android.com/jetpack/androidx/releases/glance
url: https://developer.android.com/jetpack/androidx/releases/glance
source: md.txt
---

# Glance

# Glance

[Code Sample](https://github.com/android/user-interface-samples/tree/main/AppWidget)  
API Reference  
[androidx.glance](https://developer.android.com/reference/kotlin/androidx/glance/package-summary)  
Build layouts for remote surfaces using a Jetpack Compose-style API.  

|  Latest Update  |                                Stable Release                                 | Release Candidate |                                        Beta Release                                         | Alpha Release |
|-----------------|-------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------|---------------|
| August 27, 2025 | [1.1.1](https://developer.android.com/jetpack/androidx/releases/glance#1.1.1) | -                 | [1.2.0-beta01](https://developer.android.com/jetpack/androidx/releases/glance#1.2.0-beta01) | -             |

## Declaring dependencies

To add a dependency on Glance, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // For Glance support
    implementation "androidx.glance:glance:1.2.0-beta01"
    // For AppWidgets support
    implementation "androidx.glance:glance-appwidget:1.2.0-beta01"

    // For Wear-Tiles support
    implementation "androidx.glance:glance-wear-tiles:1.0.0-alpha07"
}

android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.1.0-beta03"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
dependencies {
    // For Glance support
    implementation("androidx.glance:glance:1.2.0-beta01")
    
    // For AppWidgets support
    implementation("androidx.glance:glance-appwidget:1.2.0-beta01")

    // For Wear-Tiles support
    implementation("androidx.glance:glance-wear-tiles:1.0.0-alpha07")
}

android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.1.0-beta03"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1097239+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1097239&template=1611667)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.0-beta01

August 27, 2025

`androidx.glance:glance-*:1.2.0-beta01`is released. Version 1.2.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c9f159488663c9bc1798b1526ee7e2b8b3cf0d49..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/glance).

**Bug Fixes**

- Moving the default`minSdk`from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.2.0-alpha01

May 7, 2025

`androidx.glance:glance-*:1.2.0-alpha01`is released. Version 1.2.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/54a06695b700f449577a763921b8d75c1a59578a..c9f159488663c9bc1798b1526ee7e2b8b3cf0d49/glance).

**API Changes**

- `currentCompositeKeyHash`is now deprecated. Use`currentCompositeKeyHashCode`instead. The replacement API encodes the same hash with more bits, which exponentially reduces the chance of two random unrelated groups in the composition hierarchy from having the same hash key.([I4cb6a](https://android-review.googlesource.com/#/q/I4cb6a801d12447ac52bc92bb899ae84d69c4a6ed),[b/177562901](https://issuetracker.google.com/issues/177562901))
- Adds a new api to specify alpha (`0f`to`1f`) for the glance Image composable and the background image modifier. When not specified, retains the alpha from the source image. ([I8ad05](https://android-review.googlesource.com/#/q/I8ad0585ccf7c7c641de4380e6d9e73322c68db80))
- Add Glance APIs for generated previews. Override`GlanceAppWidget.providePreview`to provide a preview layout for your widget. Then, call`GlanceAppWidgetManager.setWidgetPreview`to set your preview. ([Iced16](https://android-review.googlesource.com/#/q/Iced163063939f2c3bc2c12bbcfd6cd45bc33df9b))
- Add`MultiProcessGlanceAppWidget`to support multiprocess configurations ([Idbb90](https://android-review.googlesource.com/#/q/Idbb90ba663c1b469462077017548f3dae230906a))
- Removes experimental tag, we now support lambdas ([I74d98](https://android-review.googlesource.com/#/q/I74d983d9a0022e9cd67d39ebb3187f581f406355),[b/299361317](https://issuetracker.google.com/issues/299361317))
- Allow specifying the lambda receiver for`GlanceAppWidget.runComposition`([I84829](https://android-review.googlesource.com/#/q/I848294da1379aa3c9e4a4ee0d80e584265cd930b))
- Add`previewSize`parameter to`requestPinGlanceAppWidget`([I9f8f0](https://android-review.googlesource.com/#/q/I9f8f0822428208e2be3eed5a837692debab078ad),[b/303256067](https://issuetracker.google.com/issues/303256067))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))
- Update`glance-appwidget`libraries to`compileSdk 35`([I2e26b](https://android-review.googlesource.com/#/q/I2e26b04663cbbd9670009e9620a0428fb10a1bb4))

## Version 1.1

### Version 1.1.1

October 16, 2024

`androidx.glance:glance-*:1.1.1`is released. Version 1.1.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c19aed31b001308c51b4f54c1690e43170516216..54a06695b700f449577a763921b8d75c1a59578a/glance).

**Security Fixes**

- As of[this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address[CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on version 1.1.0 of`androidx.glance:glance-appwidget-proto`and`androidx.glance:glance-appwidget-external-protobuf`to 1.1.1 to address the vulnerability risk.

### Version 1.1.0

June 12, 2024

`androidx.glance:glance-*:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9bf02c72eae9ac630e994275470e66a612bcef56..c19aed31b001308c51b4f54c1690e43170516216/glance).

**Important changes since 1.0.0**

- Moves Glance to 1.1.0 stable.

### Version 1.1.0-rc01

May 14, 2024

`androidx.glance:glance-*:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..9bf02c72eae9ac630e994275470e66a612bcef56/glance).

**New Features**

- Added width and height parameters to Preview annotations for Glance. Moves 1.1.0 to Release Candidate.

**API Changes**

- Adds optional parameter to Scaffold. ([If753f](https://android-review.googlesource.com/#/q/If753f541b74ca0e2bb532ca2fd61ffe3ce240400))
- Add width and height parameters to Glance`@Preview`. ([Ibabe8](https://android-review.googlesource.com/#/q/Ibabe8a1ac71ff0a34c888956fc134b2fdda317d9))
- Remove support for glance wear tile previews. ([I3850a](https://android-review.googlesource.com/#/q/I3850a8362a8e22401d14b2d7053b09957446c1b4))
- Added API for setting custom weight values for`FontStyle`. ([I7390a](https://android-review.googlesource.com/#/q/I7390ad4d90d0c4ef4eef5c6ab60fc8d5fac6c2dd))
- Rename`Viewfinder`'s`ImplementationMode`Enums to better reflect underlying implementations, and add fixed constants for`TransformationInfo.sourceRotation`([Ic6149](https://android-review.googlesource.com/#/q/Ic61497ab594cf68858566e7ea21cbdb35376a58a))

**Bug Fixes**

- Fixed a bug that caused rendering issues for`ViewGroups`in backwards compatibility mode ([I8de92](https://android-review.googlesource.com/#/q/I8de92044eee18d7aee96cb04e62e7d1ca89b2a12))

**External Contribution**

- Experimental`SharedTransitionScope`is now an interface rather than a class. ([Iaf856](https://android-review.googlesource.com/#/q/Iaf856b84ad2d91f94f8e294f015b6341808fcc74),[b/338415048](https://issuetracker.google.com/issues/338415048),[b/338414702](https://issuetracker.google.com/issues/338414702))

### Version 1.1.0-beta02

April 17, 2024

`androidx.glance:glance-*:1.1.0-beta02`is released. This version contains source jars that were missing from the previous release.

### Version 1.1.0-beta01

April 3, 2024

`androidx.glance:glance-*:1.1.0-beta01`is released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/29997d5d985705337c8ee155f0419b38c3115d0a..4298815aa64270cd2d4f6bb763a8671ec1a6421b/glance).

### Version 1.1.0-alpha01

February 7, 2024

`androidx.glance:glance-*:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29997d5d985705337c8ee155f0419b38c3115d0a/glance)

**New Features**

- Unit test library for Glance that doesn't require UI Automator. Glance code can be tested directly without having to inflate the view.
- Higher level components for simpler layouts.
- New Modifiers and theme options.
- New API for getting a flow of RemoteViews from a composition,`runComposition`

**API Changes**

- Adds a new`widgetBackground`color role to Glance themes. ([Ia2ab8](https://android-review.googlesource.com/#/q/Ia2ab8f629fbed26c42074ab52e39bc81b3cf8792))
- Add`GlanceAppWidget.runComposition`([I6344c](https://android-review.googlesource.com/#/q/I6344ce93a486a86b7484dfd704453da118e3aa79),[b/298066147](https://issuetracker.google.com/issues/298066147))
- Adds new`TopBar`component ([Ibd361](https://android-review.googlesource.com/#/q/Ibd3614d2c41d23d677fc726eb8976f4f1e07d9e6))
- Adds overrides to the`clickable`modifier. ([Iacecf](https://android-review.googlesource.com/#/q/Iacecf6b4d414fdfee85456ec04a1fcdb7f2b8003))
- Adds a new api for tinting buttons. This should be experimental until 1.0 ships. ([I92523](https://android-review.googlesource.com/#/q/I9252308e5e15af2cea79b0732098a8e9b0a598ff))
- Adds`runGlanceAppWidgetUnitTest`that provides scope to call methods on`GlanceAppWidgetUnitTest`such as`provideComposable`to provide a small isolated composable for test,`onNode`to find a Glance composable element in the provided content. This enables you to write unit tests for individual composable functions in your appWidget to verify that given certain inputs the function outputs the intended set of glance composable elements. ([I2f682](https://android-review.googlesource.com/#/q/I2f682d9ee00def5d768bd41f44cc097fc049794b))
- Adds a`testTag`modifier in semantics for use in unit tests. ([I8f62f](https://android-review.googlesource.com/#/q/I8f62ffd327c46c10653ae8638315c5a6434be866))
- update`TitleBar`- text and icon individually tintable. ([Ia0a60](https://android-review.googlesource.com/#/q/Ia0a608e6058bcf4c80407ea0d161cf3be73ce545))
- Adds scaffold component ([I8a736](https://android-review.googlesource.com/#/q/I8a73651ddb86aa007faaa2866f7c06c5445babfb))
- Adds`hasActionRunCallbackClickAction`filter and`assertHasActionRunCallbackClickAction`assertion to test`actionRunCallack`. Also, adds additional shorthand variant functions for action related test filters -`hasStartActivityClickAction<activityClass>(..)`,`hasStartServiceAction<receiverClass>(..)`,`hasSendBroadcastAction<receiverClass>(..)`. Adds similar variants for their`assertHasXXX`counterparts. ([Ieca63](https://android-review.googlesource.com/#/q/Ieca63a50ab1f7c09514f247987f3989cdb9001be))
- Moves unreleased api around. Changes a modifier from internal to public but library restricted ([If2a08](https://android-review.googlesource.com/#/q/If2a080ee52df86bf5d600cdd5d0d2899d4acaff1))
- Adds`onCompositionError`method where developers can run code when an error occurs ([I9b56f](https://android-review.googlesource.com/#/q/I9b56f60b54671e82cfed777e25d4cc79865ee674))
- Adds button and iconbutton apis to glance ([I0fd6f](https://android-review.googlesource.com/#/q/I0fd6f71d10b79647c5f5d49cd2e92056c58c1e51))
- Adds`isLinearProgressIndicator`,`isIndeterminateLinearProgressIndicator`,`isIndeterminateCircularProgressIndicator`filters to match progress indicators. Additional includes`hasAnyDescendants`filter to test if a node has a descendant in its sub-hierarchy that matches a specific matcher ([Ifd426](https://android-review.googlesource.com/#/q/Ifd4261e129826ea0701772067479cbc0a9da6685))
- Adds assertions and filters to enable testing of click actions that start service / activity or broadcasts. Also includes testing if input elements are checked. ([I3041c](https://android-review.googlesource.com/#/q/I3041cf8e63e246abac1d47865ba0b1cb27ed8843))

## Version 1.0.0

### Version 1.0.0-alpha07

August 27, 2025

`androidx.glance:glance-wear-tiles:1.0.0-alpha07`is released. Version 1.0.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/glance/glance-wear-tiles).

**New Features**

- Glance wear tiles is now deprecated and will be removed in an upcoming release. It will replaced by the new glance wear widgets library.

**API Changes**

- Deprecates glance-wear-tiles ([I82afd](https://android-review.googlesource.com/#/q/I82afd442748c57d9cf06feb1b58c9db0224183cd))
- Removing obsolete`@RequiresApi(21)`annotations ([Ic4792](https://android-review.googlesource.com/#/q/Ic47923dcc82f4b7c4638fadb10c2c0268b414fcd))
- Removing obsolete`@RequiresApi(21)`annotations ([I9103b](https://android-review.googlesource.com/#/q/I9103beb2d5f73470f3abfdf034bc2b473be923e6))
- Removes an unused module. We are not moving forward with Templates. ([I3fc90](https://android-review.googlesource.com/#/q/I3fc90515732289cde0a280b764bfd30828ea8a81),[b/430070874](https://issuetracker.google.com/issues/430070874))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Fixes api council feedback ([I284c8](https://android-review.googlesource.com/#/q/I284c8e935fe99eeeec6b752cf248adbf1ada5a71))
- Adds a new api for tinting buttons. This should be experimental until 1.0 ships ([I92523](https://android-review.googlesource.com/#/q/I9252308e5e15af2cea79b0732098a8e9b0a598ff))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b),[b/287516207](https://issuetracker.google.com/issues/287516207))
- protolayout types are now fully supported across all tile-renderer APIS. ([I428b0](https://android-review.googlesource.com/#/q/I428b0c469c5638045802f7f014a0fb5d6185da34))
- Merged public and experimental API files for d,e,f,g-paths ([I03646](https://android-review.googlesource.com/#/q/I03646bc0839d44b40105cff9bd4662c77e0d3c50),[b/278769092](https://issuetracker.google.com/issues/278769092))
- Added`*Defaults`API for`Button`,`Checkbox`,`RadioButton`and`Switch`. It brings glance closer in line with the patterns of Jetpack Compose. ([I94828](https://android-review.googlesource.com/#/q/I94828ffb4f1452ea70b4e6703c375b518844f810))
- New Glance templates module ([I94459](https://android-review.googlesource.com/#/q/I944599e5a6c93f2015bb7d15255cd45c6dfe6f63))
- We've added support for`androidx.wear.protolayout`types to`TileRenderer`([I4ac7f](https://android-review.googlesource.com/#/q/I4ac7f21c084b6706b02927b5609d51ac1d1b71bc))
- More return type nullability of deprecated-hidden functions ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Adding`@JvmDefaultWithCompatibility`annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36),[b/251463569](https://issuetracker.google.com/issues/251463569))
- Added support for using lambdas as callbacks ([Ia0bbd](https://android-review.googlesource.com/#/q/Ia0bbd2d85366b4931c53cce98d58fe716fd9662b))

**Bug Fixes**

- Update glance-appwidget libraries to`compileSdk`35 ([I2e26b](https://android-review.googlesource.com/#/q/I2e26b04663cbbd9670009e9620a0428fb10a1bb4))

### Version 1.0.0-alpha06

February 7, 2024

`androidx.glance:glance-appwidget-preview:1.0.0-alpha06`and`androidx.glance:glance-preview:1.0.0-alpha06`are released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29997d5d985705337c8ee155f0419b38c3115d0a/glance)

**New Features**

- Version updated to follow the main Glance module.

### Version 1.0.0

September 6, 2023

`androidx.glance:glance-*:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/60e4ce35a176ad03abe983b645bee8af066204db..2ad4439fc8e377e0ce07ecdee1c65ba758835f3b/glance)

**Major features of 1.0.0**

- Move Glance to stable version 1.0.0

### Version 1.0.0-rc01

July 26, 2023

`androidx.glance:glance-*:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe1a67aea083dbab61c2e05ffe23a1fadf7b40fd..60e4ce35a176ad03abe983b645bee8af066204db/glance)

Moves Glance to rc01 on the way to stable release for 1.0.0.

**New Features**

- Adds key parameters to action lambdas for more stable action invocation.
- Adds the ability to provide to`ActvityOptions`to`startActivity`actions.
- Adds support for Android 14

**API Changes**

- Added an optional key parameter for all elements that accept lambdas. ([Id96c1](https://android-review.googlesource.com/#/q/Id96c1c5754d4f39551a72cc2698451e341308bc8),[b/282445798](https://issuetracker.google.com/issues/282445798))
- Add support for setting`ActivityOptions`bundle for`actionStartActivity`([I6a08d](https://android-review.googlesource.com/#/q/I6a08dbc0759e062d755e37a5987b4ab96c59fe45))
- Merged public and experimental API files for d,e,f,g-paths ([I03646](https://android-review.googlesource.com/#/q/I03646bc0839d44b40105cff9bd4662c77e0d3c50),[b/278769092](https://issuetracker.google.com/issues/278769092))
- N/A, API file changes are just reordering methods ([I5fa95](https://android-review.googlesource.com/#/q/I5fa95ca42073461bed8e5020c91b4c0894b70753))
- Add API for setting`CoroutineContext`for`GlanceAppWidgetReceiver`requests ([I0a100](https://android-review.googlesource.com/#/q/I0a100fe2469766c887983784441cc4c0494f9669))
- Added a new API to provide`ActivityOptions`for`LazyColumn`and`LazyVerticalGrid`that will be used for all actions in the list.([Id8d71](https://android-review.googlesource.com/#/q/Id8d710b4f5c9fa02f4a76311d14b77462fc76ece))

**Bug Fixes**

- N/A, API file changes are just reordering methods ([I5fa95](https://android-review.googlesource.com/#/q/I5fa95ca42073461bed8e5020c91b4c0894b70753))
- Glance text component style demo ([Ie78a4](https://android-review.googlesource.com/#/q/Ie78a45a31acf99f8f5dce00ba5c9c55acade4e2f))

### Version 1.0.0-beta01

May 10, 2023

`androidx.glance:glance-*:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe1a67aea083dbab61c2e05ffe23a1fadf7b40fd/glance)

**New Features**

- Moves the library into beta.
- Support for themeing using`GlanceTheme`, adds glance-material and glance-material3 modules to support material 2 and material 3 style themes in Glance.
- Support for`FontFamily`added to text apis.
- Moved`GlanceAppWidget`to a`WorkManager`session based update mechanism. Users of Glance for`AppWidgets`should now override`GlanceAppWidget.provideGlance`instead of the old`Content`method. As this now happens in a worker, this is now a good place to load resources, database or network items without having to have a separate worker.

**API Changes**

- Added`*Defaults`API for`Button`,`Checkbox`,`RadioButton`and`Switch`. It brings glance closer in line with the patterns of Jetpack Compose. ([I94828](https://android-review.googlesource.com/#/q/I94828ffb4f1452ea70b4e6703c375b518844f810))
- New Glance templates module ([I94459](https://android-review.googlesource.com/#/q/I944599e5a6c93f2015bb7d15255cd45c6dfe6f63))
- Making`ResourceColorProvider`internal to module. Breaking change. Needed because`ResourceColorProvider`should only be used for dynamic theming to avoid situations where some colors are dynamic resources and some are fully resolved. ([Ib0db7](https://android-review.googlesource.com/#/q/Ib0db71fb5dbc4cd15d36652f2362624f8e92fc7a))
- Adds`FontFamily`as an option for`TextStyle`. ([Ic19ba](https://android-review.googlesource.com/#/q/Ic19ba264e49a5c985baed0debb5faedda6c17711),[b/274179837](https://issuetracker.google.com/issues/274179837))
- Value parameter name for`Enum.valueOf`changed ([Ia9b89](https://android-review.googlesource.com/#/q/Ia9b89b3c1bd0407c9beac825c49477cdfc9c1f2a))
- More thrown exceptions from enum`valueOf`([I818fe](https://android-review.googlesource.com/#/q/I818fed80f3a1af1a97b5b0de7882fb2e1b99ae62))
- Updated`GlanceAppWidget`to use`provideGlance`as the main entrypoint.`GlanceAppWidget.Content`is now deprecated. ([I202b5](https://android-review.googlesource.com/#/q/I202b5a19c818bed3da0c7bd85f1cf2fa51a38fde))
- Adds an option to supply tint color for images ([I26192](https://android-review.googlesource.com/#/q/I26192fa891c91e373dc25a51005416f08a593205),[b/212418562](https://issuetracker.google.com/issues/212418562))
- More return type nullability of deprecated-hidden functions. ([Ibf7b0](https://android-review.googlesource.com/#/q/Ibf7b0ada56eb08983e6109d30fad5294f6b841f0))
- Adding`@JvmDefaultWithCompatibility`annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))
- Removed the unused`SingleEntityTemplateData.displayHeader`. ([I7f094](https://android-review.googlesource.com/#/q/I7f094742309c86bfdbe0cf368886378260f58c0b))
- Added support for using lambdas as callbacks ([Ia0bbd](https://android-review.googlesource.com/#/q/Ia0bbd2d85366b4931c53cce98d58fe716fd9662b))
- Moved`DayNightColorProvider`to glance module ([I1842c](https://android-review.googlesource.com/#/q/I1842c292997b94b7a63239741b8cd9afe20d1c49),[b/256934779](https://issuetracker.google.com/issues/256934779))
- Removes`LocalColorProvider`from Templates. Templates will now use`GlanceTheme.colors`([Ic15e2](https://android-review.googlesource.com/#/q/Ic15e2c35f3d7922ae806860f5fa324586d02ffa6))
- Removed nullability from`Text(style: TextStyle)`([I7123b](https://android-review.googlesource.com/#/q/I7123b0342ac50051847f3b88de905839593ad5db),[b/237012816](https://issuetracker.google.com/issues/237012816))
- Default text color to black. remove nullability ([I3072c](https://android-review.googlesource.com/#/q/I3072ce2d5d6fcf98a6323e5d7f018bbf6bbac27e),[b/237012816](https://issuetracker.google.com/issues/237012816))
- Making dynamic theme`ColorProviders`its own object. Making`ResourceColorProvider`internal to the module. ([Id0e2d](https://android-review.googlesource.com/#/q/Id0e2db07ff278b7e4e64b23f8870b1ab6ea80391),[b/237012816](https://issuetracker.google.com/issues/237012816))
- Add the Undefined category to`ImageSize`. ([I2fa39](https://android-review.googlesource.com/#/q/I2fa39a9987a4675733003fb5ccee8b0e93f917cf))
- Remove deprecated`GlanceAppWidget.Content`function ([Ib05f6](https://android-review.googlesource.com/#/q/Ib05f6bb39ede221592c10e73a7769f63d7f7a7ea))
- Adds modifier as a parameter to`AndroidRemoteViews`. ([I515d4](https://android-review.googlesource.com/#/q/I515d4b17438146f6d4be4577275e3bf6018163bc))
- Add`GlanceAppWidget.compose`to make unit testing easier ([Ie9b28](https://android-review.googlesource.com/#/q/Ie9b28492b5f8e863ddd4613c93e370c3edf89c59))

**Bug Fixes**

- Added a demo widget for Glance text fonts ([I5c3d7](https://android-review.googlesource.com/#/q/I5c3d7aca18f55e379f8188db7b6dff04c416b0ca))
- Makes`AndroidRemoteViews`sizable with Modifier.
- Issues with inconsistent theme colors resolved
- All resources now prefixed to avoid collisions

### Version 1.0.0-alpha05

October 5, 2022

`androidx.glance:glance:1.0.0-alpha05`,`androidx.glance:glance-appwidget:1.0.0-alpha05`, and`androidx.glance:glance-wear-tiles:1.0.0-alpha05`are released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/glance)

**New Features**

- Adds`requestPinGlanceAppWidget`to`GlanceAppWidgetManager`, allowing apps to prompt a user to add their Glance based widget to their home screen. ([Ic6e47](https://android-review.googlesource.com/#/q/Ic6e47bd3316560f000a4bccffadec31066b62b3c))
- Adds`ACTION_DEBUG_UPDATE`to`GlanceAppWidgetReceiver`to allow developers to force their widget to update from adb on rooted devices and emulators. ([I94ae1](https://android-review.googlesource.com/#/q/I94ae10f32edab98dbacd88f8a423075cda2ecd38))

**API Changes**

- Remove header action buttons in Glance templates to simplify use case. ([Ie4387](https://android-review.googlesource.com/#/q/Ie438754b17134c0446e8e646746eadcc820106c4))
- Refactored Single Entity Template to reuse the Block subsystem design. ([Iecd2c](https://android-review.googlesource.com/#/q/Iecd2c0518ebdf5a90655f49e71a76c9f8550359e))
- Refactored Glance List Template to use`Text/Image/Action`Block design. ([If0cc1](https://android-review.googlesource.com/#/q/If0cc19530cabc6c532bcd5a9fd4224fc680c3549))
- Add priority number range for`TextBlock`and`ImageBlock`. ([I73100](https://android-review.googlesource.com/#/q/I73100492fedc879ea75b507b9fe302079baa4ef6))

**Bug Fixes**

- Removed Material3 dependency. ([I28d1c](https://android-review.googlesource.com/#/q/I28d1c877c05abfc3ec53040873bf8dc2fc7a3872))
- Moves toward a more consistent system for adding margins and spacing in glance template layouts. ([I29773](https://android-review.googlesource.com/#/q/I2977384c1f9b48664d6f7c2af57b2720c8ed2083))
- Fixes malformed Proguard rule that was blocking minified releases from building.

### Version 1.0.0-alpha04

August 10, 2022

`androidx.glance:glance:1.0.0-alpha04`,`androidx.glance:glance-appwidget:1.0.0-alpha04`, and`androidx.glance:glance-wear-tiles:1.0.0-alpha04`are released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..bea814b246f89ff7244e3c6b0648f0b57e47897c/glance)

**New Features**

- Adds Button coloring features.
- Adds`GlanceComposable`annotation for better compile time checking.
- Adds Wear specific Glance features.

**API Changes**

- Update Glance Gallery Data API and Condensed View. ([Ibc7a8](https://android-review.googlesource.com/#/q/Ibc7a8f2b117454814c51080d33a906b1c8ea84c1))
- Adds`ButtonColors`for configuring buttons. ([Iea88d](https://android-review.googlesource.com/#/q/Iea88d3b5345d11832d881f342a96ac1fc88924cf),[b/236305351](https://issuetracker.google.com/issues/236305351))
- Rename`ColorProvider.resolve`to`ColorProvider.getColor`([Ic9dfe](https://android-review.googlesource.com/#/q/Ic9dfe9f8f5f200517063dfb306e7fee41885bd69))
- Adds`copy()`method to`TextStyle`. ([I9aef6](https://android-review.googlesource.com/#/q/I9aef641dd415a7ce65ec70ecc9a4f77d635c946d))
- Adds a`ColorProviders`class that can be used as part of themes for Glance. ([I848b9](https://android-review.googlesource.com/#/q/I848b91655b34e5542551e9c581bc72097229f92c),[b/237012816](https://issuetracker.google.com/issues/237012816))
- Add List Template support to list styles and collapsed view. ([I50cdc](https://android-review.googlesource.com/#/q/I50cdc75d8f72916fafa327fc85851f97b1856633))
- Add semantics to`GlanceModiier`and`GlanceCurvedModifier`. ([Ifda7e](https://android-review.googlesource.com/#/q/Ifda7e5f8e301079f0ea1c109e1008ae411755a0f))
- Add`GlanceComposable`annotation. ([I5dbf0](https://android-review.googlesource.com/#/q/I5dbf06e2530eb00501f238c1ea7fb428447e88bb))
- Moves Glance Templates into the main Glance project. ([I9db94](https://android-review.googlesource.com/#/q/I9db94bba00c04e37f32a6c69b2bd3cd56ada8f1a))
- Add`ColorProvider.resolve()`([Ife532](https://android-review.googlesource.com/#/q/Ife532c3a9d5093c727a979e56847915fe36a83ca),[b/214733442](https://issuetracker.google.com/issues/214733442))
- New method to get`GlanceId`from an existing`appWidgetId`or an intent from a configuration activity ([Icb70c](https://android-review.googlesource.com/#/q/Icb70ca815f0858d0002c860a1446301f6a138db1),[b/230391946](https://issuetracker.google.com/issues/230391946))
- Add`GlanceComposable`annotation. ([I2c21f](https://android-review.googlesource.com/#/q/I2c21fdbd58bfcc6ce6eec32c447f1552953cef2f))
- Added`GlanceRemoteViews`for running composition outside of`GlanceAppWidget`. ([I18f92](https://android-review.googlesource.com/#/q/I18f92c28b453f7fbd0f82473bea1cdb38f109d65))
- Remove Color in`ProgressIndicatorDefaults`. ([I40299](https://android-review.googlesource.com/#/q/I402990f012830a59bc83271ae596659e42683c38))
- Rename`ActionCallback`'s onRun method to onAction, for consistency with the public APIs, as required by the API review feedback. ([Icfa57](https://android-review.googlesource.com/#/q/Icfa57d8382384a3f1d34741722d15b90fedff545))
- Convert glance template layouts to use a map ([I46bfd](https://android-review.googlesource.com/#/q/I46bfde93ec59407940b40f8e8fb2790b7509ac11))
- Add`RadioButton`composable ([I4ecce](https://android-review.googlesource.com/#/q/I4ecced2d5caec706c7dfeaa2a347c45e6ef3f002))
- Added`GlanceWearTiles`for composing wear tiles ([Ia9f65](https://android-review.googlesource.com/#/q/Ia9f65cfb0f678ae704e15c5ba48b3f8e4d0de383))
- Added clickable to`GlanceCurvedModifier`([Iec2a0](https://android-review.googlesource.com/#/q/Iec2a008d78f0fa149235691f0f1591bb296dd96a))
- Implement`CurvedRow`as a scope and create a DSL to add normal composable and/or curved elements. Also added`curvedLine`and`curvedSpacer`which are translated to`ArcLine`and`ArcSpacer`in proto tiles ([Ib955b](https://android-review.googlesource.com/#/q/Ib955b15dc19dbf0bfa7a43bd1df1723d0418af8b))
- Updated nullability in core and appcompat to match Tiramisu DP2 ([I0cbb7](https://android-review.googlesource.com/#/q/I0cbb7f22651e725a4bb36d20388a949a72cc5903))
- Add support for`RuncallbackAction`in glance-wear-tiles, only`RunCallbackAction`with NO parameter is supported for now ([Ide64a](https://android-review.googlesource.com/#/q/Ide64a3f77296c00a72409df78a0fcfaceb6d32d9))

**External Contribution**

- Updated :compose:ui:ui-test api (updateApi) due to test-coroutines-lib migration ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

### Version 1.0.0-alpha03

February 23, 2022

`androidx.glance:glance-*:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/glance)

**New Features**

- Simplified state definition to default to Preferences.

**API Changes**

- Simplify state handling by make`PreferencesGlanceStateDefinition`the default state handling. Removed`GlanceAppWidget.updateAppWidgetState`and introduced`updateAppWidgetState`that uses`Preferences`by default. ([I58963](https://android-review.googlesource.com/#/q/I589635adb59bcb4c6f87fd2c37e9f5db433fb360))
- Add Glance TemplateText class and update Template design ([I4e146](https://android-review.googlesource.com/#/q/I4e14614704cc36199f02b97c4291ed038845a36a))
- Adds outline infrastructure for the Freeform template ([If03d6](https://android-review.googlesource.com/#/q/If03d6b7fb5dce677935378c183d340bd741ad08b))
- Updates to`SingleEntityTemplate`layouts ([If925d](https://android-review.googlesource.com/#/q/If925d9d5667fbdbc5f00c8ff1de671f2831b502e))
- Added`LazyVerticalGrid`([I5f442](https://android-review.googlesource.com/#/q/I5f44228f63daa11c4b43caf5434fb4d604ace6e3))
- Use`ColorProvider`on`SingleEntityTemplate`([I01ee0](https://android-review.googlesource.com/#/q/I01ee0a0c3d8b3e660ae937daaedbd7a4c713a067))
- Update template class name ([I3720e](https://android-review.googlesource.com/#/q/I3720e31fe015807e0b7a28e1886261250272afd3))
- Added`LinearProgressIndicator`and`CircularProgressIndicator`composable. ([Ie116b](https://android-review.googlesource.com/#/q/Ie116b422d01c2a23c1fb4f41f638d872e732a109))

**Bug Fixes**

- Initial glance templates implementation, defines "single item template" data and example template layout ([I35837](https://android-review.googlesource.com/#/q/I35837a2865709be5aee9922ff1aeb3e36a619bca))
- Align the tile cotent to center by default ([I264be](https://android-review.googlesource.com/#/q/I264be13bd346ca18415b3cf7631671a13639544a))
- Bug fix with fillMaxSize/Width/Height in glance-wear-tiles ([I0a39f](https://android-review.googlesource.com/#/q/I0a39f94b75561d17410c6d164701625a2e61ad54))

### Version 1.0.0-alpha02

January 26, 2022

`androidx.glance:glance-*:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..9dceceb54300ed028a7e8fc7a3454f270337ffde/glance)

**New Features**

This release contains the set of APIs to build Wear Tiles using Compose runtime with composables optimized for "Glanceable"

- Declare your wear tile service by extending`GlanceTileService`, a service to create your tile in the composable Content() function.
- Wear tiles specific glance composables:`CurvedRow`,`CurvedText`.
- Handle different timeline modes for tile by defining`TimelineMode.SingleEntry`and`TimelineMode.TimeBoundEntries`.
- `LocalTimeInterval`, the Local composition refer to a specific time interval.
- `BorderModifer`is a`GlanceModifier`applying a border around an element.

This release also adds Progress Indicators to AppWidget Glance.

**API Changes**

- Added`LinearProgressIndicator`and`CircularProgressIndicator`composable. ([Ie116b](https://android-review.googlesource.com/#/q/Ie116b422d01c2a23c1fb4f41f638d872e732a109))
- Change`actionStartBroadcastReceiver`to`actionSendBroadcast`([I7d555](https://android-review.googlesource.com/#/q/I7d555ef9a609a53dca6f923a3649f39fd20c29e0))
- Pass Context to`GlanceAppWidget`onDelete callback ([I4c795](https://android-review.googlesource.com/#/q/I4c7953e962072c4f88e0c34f6bff045c7fe3bbf1))

**Bug Fixes**

- Correct handling of OPTIONS_APPWIDGET_SIZES if present but empty. ([I01f82](https://android-review.googlesource.com/#/q/I01f8212b96b44467bfa336b8831f76369d702214))

### Version 1.0.0-alpha01

December 15, 2021

`androidx.glance:glance:1.0.0-alpha01`,`androidx.glance:glance-appwidget:1.0.0-alpha01`, and`androidx.glance:glance-appwidget-proto:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f/glance)

**Features in initial release**

- The first release of Glance includes the first set of APIs to build AppWidget using Compose Runtime with a set of new Composables optimized for "Glanceables".

| **Note:** Glance uses its own set of Composables. Do not combine`androidx.compose`and`androidx.glance`composables.

**Features**

- Declare your app widgets with[GlanceAppWidget](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/GlanceAppWidget)and[GlanceAppWidgetReceiver](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/GlanceAppWidgetReceiver).
- Compose your UI with the initial set of Glance Composables:[Box](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#box),[Row](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#row),[Column](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#column),[Text](https://developer.android.com/reference/kotlin/androidx/glance/text/package-summary#text),[Button](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#button),[LazyColumn](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/lazy/package-summary#lazycolumn),[Image](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#image),[Spacer](https://developer.android.com/reference/kotlin/androidx/glance/layout/package-summary#spacer).
- Apply modifiers to the composables using[GlanceModifier](https://developer.android.com/reference/kotlin/androidx/glance/GlanceModifier.html)methods.
- Handle user interaction with predefined[Action](https://developer.android.com/reference/kotlin/androidx/glance/action/package-summary)s.
  - [actionStartActivity](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionstartactivity)
  - [actionRunCallback](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionruncallback)
  - [actionStartService](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionstartservice)
  - [actionStartBroadcastReceiver](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionstartbroadcastreceiver)
- Provide parameters to[Action](https://developer.android.com/reference/kotlin/androidx/glance/action/package-summary)with[ActionParameters](https://developer.android.com/reference/kotlin/androidx/glance/action/ActionParameters).
- Handle[different size modes](https://developer.android.com/guide/topics/appwidgets/layouts)by defining[SizeMode.Single](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/SizeMode.Single),[SizeMode.Exact](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/SizeMode.Exact)or[SizeMode.Responsive](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/SizeMode.Responsive).
- Persist[GlanceAppWidget state](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/state/package-summary)by providing a[GlanceStateDefinition](https://developer.android.com/reference/kotlin/androidx/glance/state/GlanceStateDefinition.html).
- Local compositions like[LocalContext](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#localcontext),[LocalState](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#localstate),[LocalGlanceId](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#localglanceid),[LocalSize](https://developer.android.com/reference/kotlin/androidx/glance/package-summary#localsize).
- Interop with your existing[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews.html)with the[AndroidRemoteViews](https://developer.android.com/reference/kotlin/androidx/glance/appwidget/package-summary#androidremoteviews)Composable.