---
title: https://developer.android.com/jetpack/androidx/releases/credentials-registry
url: https://developer.android.com/jetpack/androidx/releases/credentials-registry
source: md.txt
---

# credentials registry

# credentials registry

API Reference  
[androidx.credentials.registry](https://developer.android.com/reference/kotlin/androidx/credentials/registry/package-summary)  
To solve for these, we are adding a new registry mechanism that allows an app to provide digital credentials in a privacy-preserving way. At a high level, the provider app will be pre-registering all their candidate digital credentials with the Credential Manager; When Credential Manager receives an app request for a specific digital credential, it will run the credential matching and user selector UI in a sandbox.  

|  Latest Update  | Stable Release | Release Candidate | Beta Release |                                                Alpha Release                                                |
|-----------------|----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| October 8, 2025 | -              | -                 | -            | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/credentials-registry#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on credentials registry, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement credentials registrys

    implementation "androidx.credentials.registry:registry-digitalcredentials-mdoc:1.0.0-alpha03"
    implementation "androidx.credentials.registry:registry-digitalcredentials-preview:1.0.0-alpha03"
    implementation "androidx.credentials.registry:registry-provider:1.0.0-alpha03"
    implementation "androidx.credentials.registry:registry-provider-play-services:1.0.0-alpha03"

}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement credentials registrys

    implementation("androidx.credentials.registry:registry-digitalcredentials-mdoc:1.0.0-alpha03")
    implementation("androidx.credentials.registry:registry-digitalcredentials-preview:1.0.0-alpha03")
    implementation("androidx.credentials.registry:registry-provider:1.0.0-alpha03")
    implementation("androidx.credentials.registry:registry-provider-play-services:1.0.0-alpha03")

}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1301097+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1301097&template=1773864)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Credentials Registry 1.0

### Version 1.0.0-alpha03

October 08, 2025

`androidx.credentials.registry:registry-*:1.0.0-alpha03`is released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..4350deab5806bf95370a4d012d7eeaa70a10be44/credentials/registry).

**New Features**

- Optimized large data serialization

### Version 1.0.0-alpha02

September 24, 2025

`androidx.credentials.registry:registry-*:1.0.0-alpha02`is released. Version 1.0.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..0c132271cd448b355c7c853ce868820bbb8acbbd/credentials/registry).

**API Changes**

- Registry API for OpenID4VP 1.0 ([Ifdda3](https://android-review.googlesource.com/#/q/Ifdda33a48739e8b7c87050693e45d48c5d3a0e88),[b/439430789](https://issuetracker.google.com/issues/439430789))
- Added API for clearing a credential registry. ([I64c0d](https://android-review.googlesource.com/#/q/I64c0d978b015cbaa9a9a1a4f9c9cd47f6fda7245),[b/368092001](https://issuetracker.google.com/issues/368092001))
- Support credential registry with a customized intent action. ([I09d92](https://android-review.googlesource.com/#/q/I09d9250d9fd8f70df01634bf2a559a54b51d6e57),[b/402293724](https://issuetracker.google.com/issues/402293724))
- Credential set selection support. ([Ia1f80](https://android-review.googlesource.com/#/q/Ia1f809b54d255e7b96bdd0a00a7fd906e617cbe0),[b/444332219](https://issuetracker.google.com/issues/444332219))

### Version 1.0.0-alpha01

October 16, 2024

`androidx.credentials.registry:registry-*:1.0.0-alpha01`is released. Version 1.0.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7/credentials/registry).

**New Features**

- New Credential Manager provider registry support: allow providers to pre-register credential metadata with Credential Manager which can be later surfaced to the user by the Credential Manager upon an incoming app request.
- Added ISO/IEC mdoc credential APIs for registering mdoc credentials
- Also added a preview protocol based registry to demonstrate the end-to-end capability