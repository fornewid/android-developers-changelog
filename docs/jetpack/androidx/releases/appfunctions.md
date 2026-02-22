---
title: https://developer.android.com/jetpack/androidx/releases/appfunctions
url: https://developer.android.com/jetpack/androidx/releases/appfunctions
source: md.txt
---

# appfunctions

API Reference  
[androidx.appfunctions](https://developer.android.com/reference/kotlin/androidx/appfunctions/package-summary)  
TODO  

|   Latest Update   | Stable Release | Release Candidate | Beta Release |                                            Alpha Release                                            |
|-------------------|----------------|-------------------|--------------|-----------------------------------------------------------------------------------------------------|
| November 19, 2025 | -              | -                 | -            | [1.0.0-alpha07](https://developer.android.com/jetpack/androidx/releases/appfunctions#1.0.0-alpha07) |

## Declaring dependencies

To add a dependency on appfunctions, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.appfunctions:appfunctions:1.0.0-alpha07"
    implementation "androidx.appfunctions:appfunctions-service:1.0.0-alpha07"
    // Use Kotlin Symbol Processing (KSP) for the appfunctions compiler plugin.
    // See https://kotlinlang.org/docs/ksp-quickstart.html to add KSP to your build
    ksp "androidx.appfunctions:appfunctions-compiler:1.0.0-alpha07"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.appfunctions:appfunctions:1.0.0-alpha07")
    implementation("androidx.appfunctions:appfunctions-service:1.0.0-alpha07")
    // Use Kotlin Symbol Processing (KSP) for the appfunctions compiler plugin.
    // See https://kotlinlang.org/docs/ksp-quickstart.html to add KSP to your build
    ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-alpha07")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1709065+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1709065&template=2081773)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha07

November 19, 2025

`androidx.appfunctions:appfunctions-*:1.0.0-alpha07`is released. Version 1.0.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a3cfe112d4f736e9cd9dd1c4b222448bfcc3cfa4..fe02b1e42b486a2911eb323ef49a2caf556982bc/appfunctions).

**API Changes**

- Support deprecating`AppFunction`([I39229](https://android-review.googlesource.com/#/q/I392294f4cda7036d967d010c41f5acb2b1136abb),[b/454661174](https://issuetracker.google.com/issues/454661174))

**Bug Fixes**

- Fix issue with non-null required top-level parameters ([Ic60fc](https://android-review.googlesource.com/#/q/Ic60fc80c67ad724866313c3c744954493b9c0e78),[b/456717542](https://b.corp.google.com/issues/456717542))

### Version 1.0.0-alpha06

November 05, 2025

`androidx.appfunctions:appfunctions-*:1.0.0-alpha06`is released. Version 1.0.0-alpha06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/dac153545321dddc78a0fe286c86be49f86de8f6..a3cfe112d4f736e9cd9dd1c4b222448bfcc3cfa4/appfunctions).

**New Features**

- Support embedding resource as part of AppFunction response
- Allow using`FLAG_GRANT_PERSISTABLE_URI_PERMISSION`in`AppFunctionUriGrant`

**API Changes**

- Add`ResourceHolder`API ([I08c1c](https://android-review.googlesource.com/#/q/I08c1cd97978c0a1008a4d06a4dec7411f74d399c),[b/447530724](https://issuetracker.google.com/issues/447530724))
- Add`AppFunctionTextResource`API ([I7d54f](https://android-review.googlesource.com/#/q/I7d54f8f56818addcc43de8bf20960a5a62c4f48d),[b/447530724](https://issuetracker.google.com/issues/447530724))
- Add`AppFunctionOneOfTypeMetadata`API ([I12c67](https://android-review.googlesource.com/#/q/I12c67479b526332fa58a03164ccb51cd5daddcd6),[b/449915612](https://issuetracker.google.com/issues/449915612))
- Drop Compat suffix from Service APIs. ([Ib9291](https://android-review.googlesource.com/#/q/Ib9291c5faeb6caf1dac723b81b7642350f812674),[b/449797980](https://issuetracker.google.com/issues/449797980),[b/449797980](https://issuetracker.google.com/issues/449797980))
- Support build`AppFunctionData`from`AllOfType`([Ib1176](https://android-review.googlesource.com/#/q/Ib11763755ead6155aaa8919779ffc262e1d69227),[b/447535093](https://issuetracker.google.com/issues/447535093))
- Add get/set Parcelable API(s) in`AppFunctionData`([I3aec7](https://android-review.googlesource.com/#/q/I3aec78ef958a7c9d26d430b1033f51bbbe903de0),[b/447530985](https://issuetracker.google.com/issues/447530985))

**Bug Fixes**

- Fix the issue that ignoring nullable required field would fail when constructing`AppFunctionData`([I52195](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3791966))
- Fix the issue that using`List<PendingIntent>`with`AppFunction`would fail at compile time ([Iebde7](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3795955))
- Fix the issue that`ByteArray`'s metadata was generated incorrectly as`List<ByteArray>`([I2e499](https://android-review.git.corp.google.com/c/platform/frameworks/support/+/3810704))

### Version 1.0.0-alpha05

October 08, 2025

`androidx.appfunctions:appfunctions-*:1.0.0-alpha05`is released. Version 1.0.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9ac371e13def566b9138a983e5dd9327a6244ae..dac153545321dddc78a0fe286c86be49f86de8f6/appfunctions).

**New Features**

- Enforce required fields are provided when constructing`AppFunctionData`
- Validating`AppFunctionData`against constraint values

**API Changes**

- Add`AppFunctionService`Compat API(s). ([I2f1b1](https://android-review.googlesource.com/#/q/I2f1b1450f3a2402698b43e3559fcfcd0c34b0e64),[b/445388953](https://issuetracker.google.com/issues/445388953))

**Bug Fixes**

- Add required field`AppFunctionsData`check. ([I36b16](https://android-review.googlesource.com/#/q/I36b16cd87e420d1dbbb8918a11cfd3df9570911c),[b/394553462](https://issuetracker.google.com/issues/394553462))
- Fix the issue that parameter optional state was not respected when overriding an interface.
- Generate an empty XML file even when no`AppFunctions`are present since`AppSearch`expects the corresponding file specified in the App manifest.

### Version 1.0.0-alpha04

September 10, 2025

`androidx.appfunctions:appfunctions-*:1.0.0-alpha04`is released. Version 1.0.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0fc7aad34811cf94484effd29bc2696bb001758f..f9ac371e13def566b9138a983e5dd9327a6244ae/appfunctions).

**Bug Fixes**

- Fix R8 issues for release builds.

### Version 1.0.0-alpha03

August 13, 2025

`androidx.appfunctions:appfunctions-*:1.0.0-alpha03`is released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0fc7aad34811cf94484effd29bc2696bb001758f/appfunctions).

**New Features**

- Use KDoc(s) as`AppFunction`descriptions
- Restrict values for Int and String types using`AppFunctionIntValueConstraint`and`AppFunctionStringValueConstraint`annotations, respectively.
- Specify a natural language description for large language models and a user visible description displayed within agent apps.
- Automatically grant permissions to URI(s) returned from an app function using`AppFunctionUriGrant`class.
- Write Robolectric tests using`AppFunctionTestRule`for testing your app function setup.

**API Changes**

- Add`AppFunctionStringValueConstraint`([I10e3f](https://android-review.googlesource.com/#/q/I10e3fdff4693e4bf2088d170c0ac654457e8411c))
- Add`AppFunctionIntValueConstraint`([Ifda13](https://android-review.googlesource.com/#/q/Ifda13b0c50b2caa57de6bd7844b987ce72e70379))
- Refactor`AppFunctionPrimitiveTypeMetadata`to specific data type classes. ([I1a3b2](https://android-review.googlesource.com/#/q/I1a3b2e308411bf070c485d90fbe70e399a92642e))
- Add description field in`AppFunctionResponseMetadata`([I2332b](https://android-review.googlesource.com/#/q/I2332bb9f5cd75c6269c3b1d671a38e0cb3b20d3d))
- Remove permission requirement from`setAppFunctionEnabled`API ([I1b92a](https://android-review.googlesource.com/#/q/I1b92a6627801c98aa5fd0e49445092467b9120b9))
- Add description field in`AppFunctionParameterMetadata`([I40a67](https://android-review.googlesource.com/#/q/I40a67b95d3f6616e0d747f1be317bb758e1697e6))
- Add`AppFunctionUriGrant`([I67ca9](https://android-review.googlesource.com/#/q/I67ca988737fbe065ce8874f5b9b233c218a2f85b))
- Add`resolveAppFunctionAppMetadata`API. ([I17408](https://android-review.googlesource.com/#/q/I174089a944187498e16190cb931197cf1b763fc4))
- Add`isDescribedByKdoc`in`@AppFunctionSerializable`annotation ([Ie14e7](https://android-review.googlesource.com/#/q/Ie14e74525a708d7d775c1c0ef579f2349b06e5e8))
- Add description field in`AppFunctionDataTypeMetadata`([I1bcac](https://android-review.googlesource.com/#/q/I1bcacafddd42cd5190655d3d6b343c5058384e5e))
- Return`AppPackageMetadata`from`observeAppFunctions`API. ([I68c7e](https://android-review.googlesource.com/#/q/I68c7e47ea7f2dfc7094ae5c19978fbb3263a6868))
- Add description field in`AppFunctionMetadata`([I060e2](https://android-review.googlesource.com/#/q/I060e22469b217a09008ca291d6d76b9d76cf268a))
- Add`AppFunctionTestRule`([Id5ed0](https://android-review.googlesource.com/#/q/Id5ed0992d87e1587fb9e3c4a96a6d9f6b3c33724))
- Add`isDescribedByKdoc`in`@AppFunction`annotation ([Ia84d2](https://android-review.googlesource.com/#/q/Ia84d2a381fce668eec266c3555779be61b419315))

**Bug Fixes**

- `AppFunctionManagerCompat`only supports U+ devices ([Ifa8d0](https://android-review.googlesource.com/#/q/Ifa8d06581a37fabcd8f68b1ab6c89ae889ed57ae))
- Add property descriptions of shared serializable types in`AppFunction`'s metadata xml ([I2aab2](https://android-review.googlesource.com/#/q/I2aab2c3148393e6177c20963dd5a274d38defce2))
- Add a description element in generated`AppFunction`'s metadata xml ([Ie5bf6](https://android-review.googlesource.com/#/q/Ie5bf6e021da58c3779a8e463a1e3366637e27c08))

### Version 1.0.0-alpha02

June 4, 2025

`androidx.appfunctions:appfunctions:1.0.0-alpha02`,`androidx.appfunctions:appfunctions-compiler:1.0.0-alpha02`, and`androidx.appfunctions:appfunctions-service:1.0.0-alpha02`are released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..786176dc2284c87a0e620477608e0aca9adeff15/appfunctions).

**New Features**

- Support Android 16 API(s).
- Better support for parameterized`AppFunctionSerializable(s)`at compile time.

**API Changes**

- Introduced`AppFunctionSchemaDefinition`API, enabling agents to define their own predefined function schemas.

**Bug Fixes**

- Error handling for missing runtime enabled state of`AppFunctions`.
- Minor bugfix in`observeAppFunctions`API to observe changes in`AppFunctionComponentMetadata`.
- Additional error logs.

### Version 1.0.0-alpha01

May 7, 2025

`androidx.appfunctions:appfunctions:1.0.0-alpha01`,`androidx.appfunctions:appfunctions-compiler:1.0.0-alpha01`, and`androidx.appfunctions:appfunctions-service:1.0.0-alpha01`are released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4/appfunctions).

**New Features**

The`AppFunctions`Jetpack library is built on top of`android.app.appfunctions`platform APIs. This library simplifies exposing your app's functionality to the Assistant and allows the Assistant to interact with the app's exposed functions.

- **`androidx.appfunctions:appfunctions`** : Core client APIs for managing (enable/disable) and interacting with (search/execute)`AppFunctions`.
- **`androidx.appfunctions:appfunctions-service`** : Service-side APIs to easily expose your app's functionalities as`AppFunctions`.
- **`androidx.appfunctions:appfunctions-compiler`** : Required KSP compiler to generate necessary code for exposing`AppFunctions`.