---
title: https://developer.android.com/jetpack/androidx/releases/credentials-providerevents
url: https://developer.android.com/jetpack/androidx/releases/credentials-providerevents
source: md.txt
---

# credentials providerevents

API Reference  
[androidx.credentials.providerevents](https://developer.android.com/reference/kotlin/androidx/credentials/providerevents/package-summary)  
This library provides a set of APIs for credential providers to participate in provider events, such as credential transfer and signal credential changes.  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | - | - | - | [1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/credentials-providerevents#1.0.0-alpha05) |

## Declaring dependencies

To add a dependency on credentials providerevents, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement credentials providereventss
    implementation "androidx.credentials.providerevents:providerevents:1.0.0-alpha05"
    implementation "androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha05"
```

### Kotlin

```kotlin
dependencies {
    // Use to implement credentials providereventss
    implementation("androidx.credentials.providerevents:providerevents:1.0.0-alpha05")
    implementation("androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha05")


}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1301097+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1301097&template=1773864)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha05

January 28, 2026

`androidx.credentials.providerevents:providerevents:1.0.0-alpha05` and `androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..c26c6f088b95903b7b9cd5e6f2092988f1e64dc3/credentials/providerevents).

**Bug Fixes**

- Removed the unit test dependencies from the artifact. ([Ib02d9](https://android-review.googlesource.com/#/q/Ib02d923a0db5b278500fdec8195ecdfbb64431b6))

### Version 1.0.0-alpha04

December 17, 2025

`androidx.credentials.providerevents:providerevents:1.0.0-alpha04` and `androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..ec985eed3cba8444e5aaa52a748333397a1298f3/credentials/providerevents).

**API Changes**

- Refactor `ImportCredentialsRequest` parameters ([I29458](https://android-review.googlesource.com/#/q/I29458b7140bed58de40b47e88a49b6a6117943ca))
- Added new API to clear all ExportEntry ([I882ca](https://android-review.googlesource.com/#/q/I882caa7a623f11f233411accf42a23b58360e4ef))
- Creating a new exception class, `ImportCredentialsNoExportOptionException`, for when the import request does not get matched ([I71d96](https://android-review.googlesource.com/#/q/I71d96d5300885ea1bc713a28b86d8af01da7316e))

### Version 1.0.0-alpha03

September 24, 2025

`androidx.credentials.providerevents:providerevents:1.0.0-alpha03` and `androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a/credentials/providerevents).

**API Changes**

- Changing the `CredentialType` constant prefix ([If5dac](https://android-review.googlesource.com/#/q/If5dacc17d8ce3934756b42a9a5578cc300df9a96), [b/436531602](https://issuetracker.google.com/issues/436531602))
- Added a new set of APIs for credential transfer. Credential providers can now request credentials from another provider by passing the `ImportCredentialsRequest` ([Idc79d](https://android-review.googlesource.com/#/q/Idc79d77a585e759b5ac2f0a46cc56e22c053ef61))
- Make `requestJson` required parameter of `CredentialTransferCapabilitiesRequest`. ([Id867a](https://android-review.googlesource.com/#/q/Id867a47c85b629a50714406502ad1274024edc84))
- Added a new set of APIs for credential transfer. Credential providers can now import credentials from another provider by passing the `ImportCredentialsRequest` ([If54f7](https://android-review.googlesource.com/#/q/If54f7290e769c38e41ccf05e1621fc7bbc74ba0a))
- Minor documentation fixes. ([Ieff7c](https://android-review.googlesource.com/#/q/Ieff7c4277be545680b3a7cb78ef68ce0193b220c), [b/435703922](https://issuetracker.google.com/issues/435703922))
- Changing the `CredentialType` constant prefix ([If5dac](https://android-review.googlesource.com/#/q/If5dacc17d8ce3934756b42a9a5578cc300df9a96), [b/436531602](https://issuetracker.google.com/issues/436531602))
- Added a new set of APIs for credential transfer. Credential providers can now request credentials from another provider by passing the `ImportCredentialsRequest` ([Idc79d](https://android-review.googlesource.com/#/q/Idc79d77a585e759b5ac2f0a46cc56e22c053ef61))
- Make `requestJson` required parameter of `CredentialTransferCapabilitiesRequest` ([Id867a](https://android-review.googlesource.com/#/q/Id867a47c85b629a50714406502ad1274024edc84))
- Added new apis for credential exchange ([I77c1c](https://android-review.googlesource.com/#/q/I77c1ce3a524eacbdf08003bcf414c4b7c59703c4))

### Version 1.0.0-alpha02

August 13, 2025

`androidx.credentials.providerevents:providerevents:1.0.0-alpha02` and `androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..c359e97fece91f3767a7d017e9def23c7caf1f53/credentials/providerevents).

**API Changes**

- Minor refactors to exception classes and `GetCapabilitiesRequest` ([Ia6ee3](https://android-review.googlesource.com/#/q/Ia6ee3ffde660611001aaad53a0d4decb3dfdb311))
- Added APIs that allow relying parties (RPs) to send credential state signals to credential providers, such that they can update the state of the credentials on their end. ([Ia7a65](https://android-review.googlesource.com/#/q/Ia7a6505fc70cc69ac5e49c9fc2069744d6ea68e9))
- Refactor `ExportCredentialsResponse` such that the metrics reported are grouped by the credential type ([I3a088](https://android-review.googlesource.com/#/q/I3a08855bb616b3c77fda1c3f9821fc54145df871))
- Added new APIs for device setup service ([Icc9d5](https://android-review.googlesource.com/#/q/Icc9d59659d8a613accd78eecdb669e7140d2d142))

**Bug Fixes**

- Added new apis for credential exchange ([I77c1c](https://android-review.googlesource.com/#/q/I77c1ce3a524eacbdf08003bcf414c4b7c59703c4))

### Version 1.0.0-alpha01

May 7, 2025

`androidx.credentials.providerevents:providerevents:1.0.0-alpha01` and `androidx.credentials.providerevents:providerevents-play-services:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4/credentials/providerevents).

**New Features**

- A new `CredentialProviderEventsService` is being added that credential providers will support to receive events from Credential Manager APIs. One of the features that credential providers can now support through this service is the passkey conditional create experience. This service is designed to propagate other credential provider updates as well in the future.

**API Changes**

- `CredentialProviderEventsService` - a new service for credential providers to extend from in order to receive events from Credential manager API.