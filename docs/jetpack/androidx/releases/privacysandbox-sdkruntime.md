---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime
source: md.txt
---

# privacysandbox sdkruntime

# privacysandbox sdkruntime

API Reference  
[androidx.privacysandbox.sdkruntime.client](https://developer.android.com/reference/kotlin/androidx/privacysandbox/sdkruntime/client/package-summary)  
[androidx.privacysandbox.sdkruntime.core](https://developer.android.com/reference/kotlin/androidx/privacysandbox/sdkruntime/core/package-summary)  
[androidx.privacysandbox.sdkruntime.provider](https://developer.android.com/reference/kotlin/androidx/privacysandbox/sdkruntime/provider/package-summary)  
This library provides components for SdkRuntime aware consumers  

| Latest Update | Stable Release | Release Candidate | Beta Release |                                                  Alpha Release                                                   |
|---------------|----------------|-------------------|--------------|------------------------------------------------------------------------------------------------------------------|
| July 16, 2025 | -              | -                 | -            | [1.0.0-alpha18](https://developer.android.com/jetpack/androidx/releases/privacysandbox-sdkruntime#1.0.0-alpha18) |

## Declaring dependencies

To add a dependency on privacysandbox-sdkruntime, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {

    implementation "androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha18"
    implementation "androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha18"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha18")
    implementation "androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha18"
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1301120+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1301120&template=1773601)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha18

July 16, 2025

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha18`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha18`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha18`are released. Version 1.0.0-alpha18 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/privacysandbox/sdkruntime).

**API Changes**

- `SandboxedSdkProviderCompat.getView()`completely removed. If the project also uses`androidx.privacysandbox.tools`, the latest version should be used.
- `SdkSandboxControllerCompat`migrated to`sdkruntime-provider`.`SdkSandboxControllerCompat`in`sdkruntime-core`is deprecated and will be removed next release.

**Bug Fixes**

- `SandboxedSdkProviderCompat.onLoadSdk()`now called from the main thread regardless of`loadSdk()`caller thread.

### Version 1.0.0-alpha17

March 26, 2025

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha17`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha17`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha17`are released. Version 1.0.0-alpha17 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..78132378b67c86698d1ade3dc368c9f15d738a71/privacysandbox/sdkruntime).

**New Features**

**API Changes**

- Deprecated`SandboxedSdkProviderCompat.getView()`with removal in next release. Please migrate to`androidx.privacysandbox.tools 1.0.0-alpha13`before next release.
- Dropped support for 1.0-alpha13 libraries (both App and SDK should use more recent versions to work with counterpart libraries from this release)

**Bug Fixes**

- Migrated`AppOwnedInterfaces`to local implementation on API33 devices.

### Version 1.0.0-alpha16

December 11, 2024

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha16`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha16`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha16`are released. Version 1.0.0-alpha16 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/privacysandbox/sdkruntime).

**API Changes**

- Introduce`SdkSandboxClientImportanceListenerCompat`for SDKs to getting notifications about changes in client's app importance (foreground status)

**Bug Fixes**

- Fixed a bug prevented client app with proguard from loading SDK in backcompat mode.

### Version 1.0.0-alpha15

November 13, 2024

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha15`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha15`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha15`are released. Version 1.0.0-alpha15 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8b5ab34869fa8731b13a77763ea92989ce4ef70d..6f09cf2ae979e48fdb19485f757a033e4a34bb82/privacysandbox/sdkruntime).

**New Features**

- Supported`LayoutInflater`creation from`SdkContext`in backcompat mode.
- Supported`DisplayContext/WindowContext`creation from`SdkContext`in backcompat mode.

### Version 1.0.0-alpha14

July 24, 2024

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha14`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha14`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha14`are released. Version 1.0.0-alpha14 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..8b5ab34869fa8731b13a77763ea92989ce4ef70d/privacysandbox/sdkruntime).

**New Features**

- Introduce`SdkSandboxControllerCompat#getClientPackageName`for retrieving client app package name.

**API Changes**

- `SandboxedSdkProviderAdapter`from sdkruntime-core completely removed. Please use`SandboxedSdkProviderAdapter`from sdkruntime-provider library.

### Version 1.0.0-alpha13

March 6, 2024

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha13`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha13`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha13`are released. Version 1.0.0-alpha13 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/privacysandbox/sdkruntime).

**New Features**

- `Backcompat`support for SDK-SDK loading (`SdkSandboxControllerCompat#loadSdk`) - now SDKs loaded locally (in Application process) could load other SDKs

### Version 1.0.0-alpha12

January 24, 2024

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha12`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha12`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha12`are released.[Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/privacysandbox/sdkruntime)

**New Features**

- Introduce`SdkSandboxControllerCompat#loadSdk`for loading SDKs by other SDKs in sandbox (currently supported on API 34 Extension 10 only)

**API Changes**

- Remove sandbox support on API 33 devices - backcompat (in app) mode should be used before API 34.

### Version 1.0.0-alpha11

November 15, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha11`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha11`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha11`are released.[Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..312eb9f1ddece3a18317f18515a877e0e745cb2c/privacysandbox/sdkruntime)

**New Features**

- `AppOwnedSdkSandboxInterfaceCompat`supported on API34 Ext 8 devices (before worked only on`PrivacySandbox`Developer Preview builds)

### Version 1.0.0-alpha10

October 18, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha10`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha10`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha10`are released.[Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/privacysandbox/sdkruntime)

**Bug Fixes**

- Fixed resource remapping for SDK loaded in app process.

### Version 1.0.0-alpha09

October 4, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha09`,`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha09`, and`androidx.privacysandbox.sdkruntime:sdkruntime-provider:1.0.0-alpha09`are released.[Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443/privacysandbox/sdkruntime)

**API Changes**

- First release of sdkruntime-provider library that should be used instead of sdkruntime-core library for SDKs.
- `SandboxedSdkProviderAdapter`migrated to sdkruntime-provider.`SandboxedSdkProviderAdapter`in sdkruntime-core is deprecated and will be removed soon.

**Bug Fixes**

- Unregister all`SdkSandboxActivityHandlerCompat`when SDK unloaded.
- `ActivityHolder`Lifecycle events now matches behavior of`ReportFragment`

### Version 1.0.0-alpha08

August 9, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha08`and`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha08`are released.[Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/privacysandbox/sdkruntime)

**Bug Fixes**

- Fix`SharedPreferences`migration fails when target context`SharedPreferences`didn't exist.

### Version 1.0.0-alpha07

July 26, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha07`and`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha07`are released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/privacysandbox/sdkruntime)

**New Features**

- Per-SDK`SharedPreferences`support for SDKs loaded locally (in Application process).`SandboxedSdkProviderCompat#context`customized to provide Per-SDK`SharedPreferences`support for SDKs in backcompat mode.

### Version 1.0.0-alpha06

June 21, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha06`and`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha06`are released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..3b5b931546a48163444a9eddc533489fcddd7494/privacysandbox/sdkruntime)

**New Features**

- Per-SDK Storage and Databases support for SDKs loaded locally (in Application process).
- `SandboxedSdkProviderCompat#context`customized to provide Per-SDK Storage and Database support for SDKs in backcompat mode.

### Version 1.0.0-alpha05

June 7, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha05`and`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha05`are released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- (`PrivacySandbox`Developer Preview 8+ only) Add support for App-Sandbox mediation (see`SdkSandboxManagerCompat#registerAppOwnedSdkSandboxInterface`+`SdkSandboxControllerCompat#getAppOwnedSdkSandboxInterfaces`)

### Version 1.0.0-alpha04

May 10, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-client:1.0.0-alpha04`and`androidx.privacysandbox.sdkruntime:sdkruntime-core:1.0.0-alpha04`are released. This version is developed in an internal branch.
| **Note:** This version will only compile against the[Android 14 (Upside Down Cake) Beta 2 SDK](https://developer.android.com/about/versions/14#beta-2).

**New Features**

- Initial support for starting Activities inside SDK sandbox (available for UDC+ devices): SDK need to register handler by calling`SdkSandboxControllerCompat#registerSdkSandboxActivityHandler`then App could start Activity for SDK by calling`SdkSandboxManagerCompat#startSdkSandboxActivity`.

### Version 1.0.0-alpha03

April 5, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-*:1.0.0-alpha03`is released.

**New Features**

- Added support for`SandboxProcessDeathCallback`
- Added support for SDK unloading

**API Changes**

- `SandboxedSdkCompat#create(binder)`removed, please use constructor`SandboxedSdkCompat(binder)`

### Version 1.0.0-alpha02

March 22, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-*:1.0.0-alpha02`is released.

**New Features**

- Added an API for fetching list of loaded SDKs -`SdkSandboxControllerCompat.getSandboxedSdks()`.

### Version 1.0.0-alpha01

January 11, 2023

`androidx.privacysandbox.sdkruntime:sdkruntime-*:1.0.0-alpha01`is released.

- This is a new Jetpack library that contains components for building and loading Runtime enabled SDKs (Privacy Sandbox) on old versions of Android Platform.