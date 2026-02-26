---
title: https://developer.android.com/jetpack/androidx/releases/credentials
url: https://developer.android.com/jetpack/androidx/releases/credentials
source: md.txt
---

# credentials

[User Guide](https://developer.android.com/training/sign-in/passkeys) API Reference  
[androidx.credentials](https://developer.android.com/reference/kotlin/androidx/credentials/package-summary)  
This library provides unified access to a user's credentials. This can include passwords, passkeys and federated credentials. This library should be used to provide seamless and secure sign-in experiences.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/credentials#1.5.0) | [1.6.0-rc02](https://developer.android.com/jetpack/androidx/releases/credentials#1.6.0-rc02) | - | [1.6.0-rc02](https://developer.android.com/jetpack/androidx/releases/credentials#1.6.0-rc02) |

## Declaring dependencies

To add a dependency on credentials, you must add the Google Maven repository to
your project. Read [Google's Maven
repository](https://developer.android.com/studio/build/dependencies#google-maven) for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.credentials:credentials:1.6.0-rc02")
    implementation("androidx.credentials:credentials-play-services-auth:1.6.0-rc02")
}
```

### Groovy

```groovy
dependencies {
    implementation "androidx.credentials:credentials:1.6.0-rc02"
    implementation "androidx.credentials:credentials-play-services-auth:1.6.0-rc02"
}
```

For more information about dependencies, see
[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1301097+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1301097&template=1773864)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Credentials e2ee Version 1.0.

### Version 1.0.0-alpha02

April 17, 2024

`androidx.credentials:credentials-e2ee:1.0.0-alpha02` is released. This version contains source jars that were missing from the previous release.

### Version 1.0.0-alpha01

April 3, 2024

`androidx.credentials:credentials-e2ee:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55/credentials/credentials-e2ee).

**New Features**

- Support for creating an `IdentityKey` from a passkey ([Iba31e](https://android-review.googlesource.com/#/q/Iba31e191a7c1b74e7762613ca7abe8e69e37c83c))

## Version 1.6

### Version 1.6.0-rc02

February 25, 2026

`androidx.credentials:credentials:1.6.0-rc02` and `androidx.credentials:credentials-play-services-auth:1.6.0-rc02` are released. Version 1.6.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/01c19981455eaa37cb7d93540367aef6e5bc2449..b24fc20d261f635de24bde3d4bc0328ac5b635a5/credentials).

**Bug Fixes**

- Fixes the fall back mechanism for Pre-U create credential flow on devices with an unsupported GMSCore version.

### Version 1.6.0-rc01

December 17, 2025

`androidx.credentials:credentials:1.6.0-rc01` and `androidx.credentials:credentials-play-services-auth:1.6.0-rc01` are released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..01c19981455eaa37cb7d93540367aef6e5bc2449/credentials).

**API Changes**

- Add APIs for the registration and clearance of creation options in Credential Manager. ([I01073](https://android-review.googlesource.com/#/q/I010739ff96a7491ec709aa6109c572a30f436144))
- Added new Signal API Exception to indicate request is rate limited ([Ie2733](https://android-review.googlesource.com/#/q/Ie273300e85b23c1544c31c74bf3d144299f47453) )

### Version 1.6.0-beta03

October 22, 2025

`androidx.credentials:credentials:1.6.0-beta03` and `androidx.credentials:credentials-play-services-auth:1.6.0-beta03` are released. Version 1.6.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/credentials).

**New Features**

- Minor internal data serialization changes

### Version 1.6.0-beta02

October 08, 2025

`androidx.credentials:credentials:1.6.0-beta02` and `androidx.credentials:credentials-play-services-auth:1.6.0-beta02` are released. Version 1.6.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..4350deab5806bf95370a4d012d7eeaa70a10be44/credentials).

**New Features**

- Optimized large data serialization.

### Version 1.6.0-beta01

September 24, 2025

`androidx.credentials:credentials:1.6.0-beta01` and `androidx.credentials:credentials-play-services-auth:1.6.0-beta01` are released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..0c132271cd448b355c7c853ce868820bbb8acbbd/credentials).

**Bug Fixes**

- Minor documentation fixes ([Ieff7c](https://android-review.googlesource.com/#/q/Ieff7c4277be545680b3a7cb78ef68ce0193b220c), [b/435703922](https://issuetracker.google.com/issues/435703922))

### Version 1.6.0-alpha05

August 13, 2025

`androidx.credentials:credentials:1.6.0-alpha05` and `androidx.credentials:credentials-play-services-auth:1.6.0-alpha05` are released. Version 1.6.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..c359e97fece91f3767a7d017e9def23c7caf1f53/credentials).

**API Changes**

- Added APIs that allow relying parties (RPs) to send credential state signals to credential providers, such that they can update the state of the credentials on their end. ([Ia7a65](https://android-review.googlesource.com/#/q/Ia7a6505fc70cc69ac5e49c9fc2069744d6ea68e9))

**Bug Fixes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.6.0-alpha04

July 16, 2025

`androidx.credentials:credentials:1.6.0-alpha04` and `androidx.credentials:credentials-play-services-auth:1.6.0-alpha04` are released. Version 1.6.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/credentials).

**New Features**

- The Credential Manager dialogs will now look more consistent across Android versions before and after Android 14, on mobile and wearable devices

### Version 1.6.0-alpha03

June 18, 2025

`androidx.credentials:credentials:1.6.0-alpha03` and `androidx.credentials:credentials-play-services-auth:1.6.0-alpha03` are released. Version 1.6.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..e8af6ab7417811bf386c52a59ab5d0b94d194eeb/credentials).

**New Features**

- Pre Android 14, update the Credential Manager dialogs to be more consistent with Android 14+.

**API Changes**

- Update `CreateDigitalCredentialRequest` constructor API ([I6f6da](https://android-review.googlesource.com/#/q/I6f6da3f7f4602dbb1f71a93e26e7d000f87749c3))

### Version 1.6.0-alpha02

May 20, 2025

`androidx.credentials:credentials:1.6.0-alpha02` and `androidx.credentials:credentials-play-services-auth:1.6.0-alpha02` are released. Version 1.6.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/credentials).

**API Changes**

- Support Digital Credentials issuance ([I4e6f9](https://android-review.googlesource.com/#/q/I4e6f97b470baf7081c16f33dd1600c7d25fd3aa7))

### Version 1.6.0-alpha01

May 7, 2025

`androidx.credentials:credentials:1.6.0-alpha01` and `androidx.credentials:credentials-play-services-auth:1.6.0-alpha01` are released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9aca98b55b132550a298cc52cb2e42cedb32c452..b6c541571b9fb5471f965fc52612cb280713e5e4/credentials).

**New Features**

- Passkey conditional create - Enables the passkey conditional create feature, whereby developers can request for a conditional passkey creation. A conditional creation request will be propagated to the preferred credential provider and then based on some internal conditions, a passkey will be created without the typical bottom sheet UI experience. Users will see a notification with information about the passkey that was just created.

**API Changes**

- Expose `CreateCredentialResponse.createFrom` API ([Ic0494](https://android-review.googlesource.com/#/q/Ic049446d51b70bf988039a3adbf1d0b0aef364a4))
- Exposed `isConditionalCreate` bit to allow silent passkey creation. ([I3a1bb](https://android-review.googlesource.com/#/q/I3a1bb2a18377dbff01a1cb82bbe75fcf2c8d2d76))

## Version 1.5

### Version 1.5.0

March 12, 2025

`androidx.credentials:credentials:1.5.0` and `androidx.credentials:credentials-play-services-auth:1.5.0` are released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c21f3bc469f2586b3241fae2c8f46a007e8628e8..4fec16dcf4d565b5728b351888615c364d031a25/credentials).

**Important changes since 1.3.0**

- Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same `GetCredentialRequest` with a given view, such as a username or a password field. Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.
- Restore Credentials: The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a `RestoreCredential` for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.

### Version 1.5.0-rc01

January 15, 2025

`androidx.credentials:credentials:1.5.0-rc01` and `androidx.credentials:credentials-play-services-auth:1.5.0-rc01` are released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..c21f3bc469f2586b3241fae2c8f46a007e8628e8/credentials).

**New Features**

- A version bump release along with small implementation updates

**API Changes**

- Add `@Deprecated` annotation for `IdentityCredential` to keep consistent with framework. ([I6ac90](https://android-review.googlesource.com/#/q/I6ac906032150503829af6a4aca028037be7934af), [b/140252778](https://issuetracker.google.com/issues/140252778), [b/217942278](https://issuetracker.google.com/issues/217942278), [b/251211046](https://issuetracker.google.com/issues/251211046), [b/239955609](https://issuetracker.google.com/issues/239955609))

**External Contribution**

- Deprecate `BuildCompat.isAtLeastV`. Callers should check SDK_INT against 35 directly instead. ([I294d1](https://android-review.googlesource.com/#/q/I294d117a8fea924e7f1b739d52268a9a54be6db7))

### Version 1.5.0-beta01

October 30, 2024

`androidx.credentials:credentials:1.5.0-beta01` and `androidx.credentials:credentials-play-services-auth:1.5.0-beta01` are released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/credentials).

**New Features**

Beta release for the following new features:

- Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same `GetCredentialRequest` with a given view, such as a username or a password field. Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.
- Restore Credentials. The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a `RestoreCredential` for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.

**API Changes**

- Allow developers the flexibility to condition within the `CryptoObject` and `BiometricPromptData` setters. ([Ie7e8e](https://android-review.googlesource.com/#/q/Ie7e8efa57f2a2374a8463724e92eee186cb42879))

### Version 1.5.0-alpha06

October 16, 2024

`androidx.credentials:credentials:1.5.0-alpha06` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha06` are released. Version 1.5.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d716245947072d167bfb451effda3e07384dcc5d..b8a68b0896897fa158508d73a31998a26161d9a7/credentials).

**New Features**

- Prepare the library for entering a stable release soon.

### Version 1.5.0-alpha05

September 4, 2024

`androidx.credentials:credentials:1.5.0-alpha05` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha05` are released. Version 1.5.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fcae1dc9e94201f2646e67b240aba31b52b964e9..d716245947072d167bfb451effda3e07384dcc5d/credentials).

**API Changes**

- Support a new credential type - `DigitalCredential` ([I12952](https://android-review.googlesource.com/#/q/I129527c249c9d59d0236856d01d34b90adca0044))
- Expose bundle conversion APIs: expose more `asBundle` and `fromBundle` helpers to allow these classes be passed across IPC more easily ([I1a017](https://android-review.googlesource.com/#/q/I1a0176c99ed7226e7aed4b72c41cb5bc15ee7215))
- Make`PendingIntentHandler` backward compatible. ([I34c13](https://android-review.googlesource.com/#/q/I34c13e0e6b9672019a5261fddbca44e7f5ba7122))
- Make `CallingAppInfo` backward compatible ([I65085](https://android-review.googlesource.com/#/q/I65085499b383fd4962f0236ee6424f628ffeb136))
- Expose `ClearCredentialRequestTypes` constants.

### Version 1.5.0-alpha04

August 7, 2024

`androidx.credentials:credentials:1.5.0-alpha04` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha04` are released. Version 1.5.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/020fe18a007b47f57cc750fdf45ca933da1aeae0..fcae1dc9e94201f2646e67b240aba31b52b964e9/credentials).

**API Changes**

- Added a default value for `isCloudBackupEnabled` parameter of `CreateRestoreCredentialRequest`.

**Bug Fixes**

- Removed `minSdkVersion` for `credentials-play-services-auth`.

### Version 1.5.0-alpha03

July 24, 2024

`androidx.credentials:credentials:1.5.0-alpha03` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha03` are released. This version is developed in an internal branch.

**New Features**

- Introduces a new feature, the Restore Credentials. The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a `RestoreCredential` for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.

**API Changes**

- New classes are added for requesting Restore Credentials.
- A new credential type, `RestoreCredential`, that can restore credentials in a new device.
- `CreateRestoreCredentialRequest` for creating a new `RestoreCredential`.
- `GetRestoreCredentialOption` for fetching `RestoreCredential`.
- `ClearCredentialStateRequest` can be modified to clear the `RestoreCredential`.

**Bug Fixes**

- Added a new `RestoreCredential` API for app-restore purposes ([If2d40](https://android-review.googlesource.com/#/q/If2d40bfded85a64a0e02e005acc1d0790e454b28))

### Version 1.5.0-alpha02

June 12, 2024

`androidx.credentials:credentials:1.5.0-alpha02` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha02` are released. This version is developed in an internal branch.

**New Features**

- The ability for `CredentialManager` to directly imbue a `BiometricPrompt` within the credential creation and retrieval flows is now available for use through Jetpack for providers.

**API Changes**

- Added the `BiometricPromptData` to the API surface to allow utilizing the new imbued `BiometricPrompt` flow through `CredentialManager` ([I3b159](https://android-review.googlesource.com/q/I3b1595a588645d3628fb3051660a2f628a1c6f0a))
- Modified all entry classes and subclasses across `CreateEntry` and `CredentialEntry` to gain the utility of the `BiometricPromptData` for Providers. ([I16936](https://android-review.googlesource.com/q/I16936d64cf2fbba47294a112173aebe25d3ccdb9), [I8e5bc](https://android-review.googlesource.com/q/I8e5bc104b7337850ca6c49064502044d29c1308b))
- Added the types needed to encode the error and results from the imbued `BiometricPrompt` flows with `CredentialManager`. ([I8e5bc](https://android-review.googlesource.com/q/I8e5bc104b7337850ca6c49064502044d29c1308b))

### Version 1.5.0-alpha01

May 29, 2024

`androidx.credentials:credentials:1.5.0-alpha01` and `androidx.credentials:credentials-play-services-auth:1.5.0-alpha01` are released. This version is developed in an internal branch.

**New Features**

Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same `GetCredentialRequest` with a given view, such as a username or a password field.

Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.

**API Changes**

- A `PendingGetCredentialRequest` class that takes in a (pre-existing) `GetCredentialRequest`, and a callback to be invoked with a (pre-existing) `GetCredentialResponse`, when available asynchronously.
- New extension setter API for the android View class, that allows setting an instance of `PendingGetCredentialRequest`. Usage of this API will prepare the given view, such that when the user taps on it, credential suggestions will show up on secondary UI experiences like keyboard/dropdown suggestions.

## Version 1.3

### Version 1.3.0

October 2, 2024

`androidx.credentials:credentials:1.3.0` and `androidx.credentials:credentials-play-services-auth:1.3.0` are released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baedf2c9e120baecebea61b8f86ce43e1237b790..fc11c24f364154f26d135fcee8a16a5718084d51/credentials).

**Important changes since 1.2.0**

Various important improvements in making the library more reliable and consistent, including but not limited to:

- Support `preferImmediatelyAvailableCredentials` on all android versions.
- Improved proguard rule to reduce the app size increase.
- Various minor bug fixes.

### Version 1.3.0-rc01

July 10, 2024

`androidx.credentials:credentials:1.3.0-rc01` and `androidx.credentials:credentials-play-services-auth:1.3.0-rc01` are released. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..baedf2c9e120baecebea61b8f86ce43e1237b790/credentials).

**New Features**

- A version bump release along with small implementation updates.

### Version 1.3.0-beta02

June 12, 2024

`androidx.credentials:credentials:1.3.0-beta02` and `androidx.credentials:credentials-play-services-auth:1.3.0-beta02` are released. Version 1.3.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..f5541f29d045c6ba9734689ec67891f8d667412b/credentials).

**Bug Fixes**

- Fixed logic to correctly check for `NOT_ALLOWED_ERR` instead of `CONSTRAINT_ERR` in public key credential flows that contain an error on pre-U devices ([I31b37](https://android-review.googlesource.com/q/I31b3798bf9eabe17c927fe25dd01dd82816edd09))

### Version 1.3.0-beta01

May 29, 2024

`androidx.credentials:credentials:1.3.0-beta01` and `androidx.credentials:credentials-play-services-auth:1.3.0-beta01` are released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/credentials).

**API Changes**

- Rename the `reateCredentialRequest` Bundle conversion API. ([I46b95](https://android-review.googlesource.com/#/q/I46b956754cd004befb8a3d34584ae3e5b774c419))
- Update the priorityhints API ([Ida554](https://android-review.googlesource.com/#/q/Ida55401340bf127d664d81e322cea40964cabdc9))

### Version 1.3.0-alpha04

May 14, 2024

`androidx.credentials:credentials:1.3.0-alpha04` and `androidx.credentials:credentials-play-services-auth:1.3.0-alpha04` are released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5c17ac8d339b80b5f509f83792f5923e337612c7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/credentials).

**Bug Fixes**

- Move to 21 as the default `minSdkVersion` of androidx libraries. ([I6ec7f](https://android-review.googlesource.com/#/q/I6ec7f80aafbe04c64c8f2d8fef82d4cd5c68525e))
- Support PRF creation for Android versions 13 and below.
- Support `preferImmediatelyAvailableCredentials` for Android versions 13 and below.

### Version 1.3.0-alpha03

April 17, 2024

`androidx.credentials:credentials:1.3.0-alpha03` and `androidx.credentials:credentials-play-services-auth:1.3.0-alpha03` are released. This version contains source jars that were missing from the previous release.

### Version 1.3.0-alpha02

April 3, 2024

`androidx.credentials:credentials:1.3.0-alpha02` and `androidx.credentials:credentials-play-services-auth:1.3.0-alpha02` are released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..02b55f664eba38e42e362e1af3913be1df552d55/credentials).

**New Features**

- Added new APIs that assist credential entries to be clearly displayed in the credential selector during a `getCredential` or `createCredential` call.

**API Changes**

- Extended the Credential Options API Surface to contain information on display priorities ([Ied6fe](https://android-review.googlesource.com/#/q/Ied6fe0b5d34ce320fe91372a0369e7adb669dd61))
- Exposed raw Bundle to structured data conversion helpers ([If03a0](https://android-review.googlesource.com/#/q/If03a002c7ca243e305161a8aae64f26580f992e2))
- Exposed `isDefaultIcon` and `isAutoSelectAllowedFromOption` APIs ([I05c59](https://android-review.googlesource.com/#/q/I05c59718b5fcd617f44da8495549c828c475e60a))
- Extended the credential entry API surface to contain information on defaulting an icon ([I9fe00](https://android-review.googlesource.com/#/q/I9fe005a526ccc3347e155146ba8d89852a0a598e))
- Added an `entryGroupId` bit to the credential entries ([Id995c](https://android-review.googlesource.com/#/q/Id995c01e337ecbef082fc2cbc1f576852982bb8d))
- Added a new `affiliationName` property to the `CredentialEntry` API surface. ([I6261e](https://android-review.googlesource.com/#/q/I6261ec1d8cc36b2d96b284014d4ba4bc2773c1e3))
- Exposed `fromXYZEntry` APIs to be used in the framework ([I645a1](https://android-review.googlesource.com/#/q/I645a1177a06d5325a26fe333eeb93570a91d166c))

**Bug Fixes**
- Provided fallback solution when platform credential manager is not available. ([b/310701473](https://issuetracker.google.com/issues/310701473))
- Fix NPE caused by `clearCredentialState` API ([b/327686881](https://issuetracker.google.com/issues/327686881))

### Version 1.3.0-alpha01

December 13, 2023

`androidx.credentials:credentials:1.3.0-alpha01` and `androidx.credentials:credentials-play-services-auth:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1b17367013411d8043b8de6ee9d7791a2a04b4f2..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/credentials)

**Bug Fixes**

- The minimum APK version needed for Google Play services is now 2023 v08.23 (APK version APK version 230815045), and this check is baked into the library. ([aosp/2856137](https://android.googlesource.com/c/platform/frameworks/support/+/2856137))
- Fix the already-resume error caused by race condition of multiple in-flight requests ([Ic3567](https://android-review.googlesource.com/#/q/Ic3567e1c159b45d1a63cf86ce8ee2f07a9415975))

## Version 1.2

### Version 1.2.2

April 3, 2024

`androidx.credentials:credentials:1.2.2` and `androidx.credentials:credentials-play-services-auth:1.2.2` are released. Version 1.2.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/517ad3204c27e1d328f853d3a5f3632a92e42d60..ed68fe604b26a5efd5d6be2e45fc6231994fa031/credentials).

**Bug Fixes**

- Fix the already-resume error caused by race condition of multiple in-flight requests ([Ic3567](https://android-review.googlesource.com/q/Ic3567e1c159b45d1a63cf86ce8ee2f07a9415975))
- Fix NPE caused by `clearCredentialState` API ([b/327686881](https://issuetracker.google.com/issues/327686881))

### Version 1.2.1

March 6, 2024

`androidx.credentials:credentials:1.2.1` and `androidx.credentials:credentials-play-services-auth:1.2.1` are released. Version 1.2.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b17367013411d8043b8de6ee9d7791a2a04b4f2..517ad3204c27e1d328f853d3a5f3632a92e42d60/credentials).

**Bug Fixes**

- Provided fallback solution when platform credential manager is not available. ([b/310701473](https://issuetracker.google.com/issues/310701473))

### Version 1.2.0

November 1, 2023

`androidx.credentials:credentials:1.2.0` and `androidx.credentials:credentials-play-services-auth:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b03ea635a1664645b27282ba4a3126017f631c3..1b17367013411d8043b8de6ee9d7791a2a04b4f2/credentials)

**Important changes since 1.0.0**

- This release added a new set of APIs for supporting Credential Provider in storing and fetching passwords, passkeys per users' requests.

### Version 1.2.0-rc01

October 4, 2023

`androidx.credentials:credentials:1.2.0-rc01` and `androidx.credentials:credentials-play-services-auth:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..4b03ea635a1664645b27282ba4a3126017f631c3/credentials)

- A version bump release along with small implementation updates

### Version 1.2.0-beta04

September 20, 2023

`androidx.credentials:credentials:1.2.0-beta04` and `androidx.credentials:credentials-play-services-auth:1.2.0-beta04` are released. [Version 1.2.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/credentials)

**New Features**

- Added get sign in intent flow for sign in with google. ([Ib6559](https://android-review.googlesource.com/q/Ib65592eb8ab347f7fc07b03025ba4e856edffc8d),[I7a042](https://android-review.googlesource.com/q/I7a042640e0246ebd6b2b522e98b490dfd443ca1b))
- Added single signature checking for allowlisted packages. ([Ie6ff5](https://android-review.googlesource.com/q/Ie6ff59011999077b19dafae607bb26f54ce89290))
- Updated `PublicKeyCredential` json parsing to utilize updated `toJson()` methods. ([I708e3](https://android-review.googlesource.com/q/I708e3c2183f3b57595ccfa43bfe43497904bbc7c), [I00402](https://android-review.googlesource.com/q/I00402356887ef0a75f09e7969fce24e8a1de1aeb))

**Bug Fixes**

- Fixed missing Proguard rules ([b/288120539](https://issuetracker.google.com/issues/288120539))

### Version 1.2.0-beta03

August 23, 2023

`androidx.credentials:credentials:1.2.0-beta03` and `androidx.credentials:credentials-play-services-auth:1.2.0-beta03` are released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d02aa58ef50902c5b6abea5c6db4d2bba9257c9..3315f1ef094c312203fe26841287902916fbedf5/credentials)

**Bug Fixes**

- Removes uvm extensions, due to planned deprecation from the webauthn spec. ([I2d46d](https://android-review.googlesource.com/q/I2d46d60d9e6384b7233d7825d2dedfc409df369b))
- Ensure compliance to webauthn spec regarding `clientExtensions`, `credProps`, and rk properties ([I3ab01](https://android-review.googlesource.com/q/I3ab0122b871e3308f0d3271a8ef9fe56cf81864c))

### Version 1.2.0-beta02

August 1, 2023

`androidx.credentials:credentials:1.2.0-beta02` and `androidx.credentials:credentials-play-services-auth:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..3d02aa58ef50902c5b6abea5c6db4d2bba9257c9/credentials)

**Bug Fixes**

- [b/293743991](http://b/293743991) - Fix the constant value for the `authenticatorData` field, in order to correctly parse the `authenticationResponseJson` property in [PublicKeyCredential](https://developer.android.com/reference/kotlin/androidx/credentials/PublicKeyCredential)

### Version 1.2.0-beta01

July 26, 2023

`androidx.credentials:credentials:1.2.0-beta01` and `androidx.credentials:credentials-play-services-auth:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..4aed940027a19667e67d155563fc5fa8b7279313/credentials)

**API Changes**

- Expose an API that determines whether the origin is populated or not ([Ia91f4](https://android-review.googlesource.com/#/q/Ia91f4d9db4a9550f57148da6cf4a79849a94c456))
- Makes custom exceptions semantically correct ([Ibf6f4](https://android-review.googlesource.com/#/q/Ibf6f46188d2fd60fc69930d2f9015995acf3ee2b))
- add test api ([I61c1d](https://android-review.googlesource.com/#/q/I61c1defb310542ba8e256ba9420226fbdfeaa4b8))
- add test api ([Iaeb6f](https://android-review.googlesource.com/#/q/Iaeb6f89f9afe954a896f256e36a11c33a128aa80))
- Removed usages of experimental `isAtLeastU()` API ([Ie9117](https://android-review.googlesource.com/#/q/Ie9117598f70e8873011f98ebbe0e6cd502772c87), [b/289269026](https://issuetracker.google.com/issues/289269026))
- Expose a custom origin getter that takes in allowlist ([I0c1b4](https://android-review.googlesource.com/#/q/I0c1b48411a1b0ec8480e8a87e4ae16507d5b89bd))
- Added `VisibleForTest` annotation ([I5467a](https://android-review.googlesource.com/#/q/I5467a49db2fd9ab937afe851adb51e5e6b25c77a))
- Added `VisibleForTest` annotation ([Idf57a](https://android-review.googlesource.com/#/q/Idf57a079daf6ddc9c9d57677401310371416ce50))
- Remove test only apis ([Idcc05](https://android-review.googlesource.com/#/q/Idcc05c940bf6304d96116a5b18ee20a1dc291ca6))
- Expose provider entry classes to lower API levels ([I2e00a](https://android-review.googlesource.com/#/q/I2e00aea2f31527f8724739f48b0f3268b30e31bd))
- Add test apis ([Id6b9e](https://android-review.googlesource.com/#/q/Id6b9e95fe9e75af9402f6de42baea2152217681d))

**Bug Fixes**

- Add test APIs ([I0d243](https://android-review.googlesource.com/#/q/I0d243c9bba06d270baa6d84e94cf305b2a5fe81f))
- Add new testing APIs ([I6fa12](https://android-review.googlesource.com/#/q/I6fa128ffe3ca2fffebe1b737ba49259213dd8563))
- Expose autoselect for Create requests ([I84eee](https://android-review.googlesource.com/#/q/I84eeee6067586bf8f9140505f0885885d40d8c15))
- Make JSON encoding errors more detailed ([I7a865](https://android-review.googlesource.com/#/q/I7a865860f5b64c1ec2bdd21b2d2b190b5562a090))
- Gracefully report a developer error upon a non-activity context parameter ([/I20dd7](https://android-review.googlesource.com/q/I20dd7634c03159c11e7a751d69084189ee8e9566), [b/288288940](https://issuetracker.google.com/issues/288288940))
- Corrected Exception Parsing for Exceptions returned from Providers ([Iaa2af](),[I0d243](),[I55151]())
- Improved documentation for `toSlice`

### Version 1.2.0-alpha05

June 7, 2023

`androidx.credentials:credentials:1.2.0-alpha05` and `androidx.credentials:credentials-play-services-auth:1.2.0-alpha05` are released. This version is developed in an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- Backwards compatible parsing for the get API across GMS modules introduced alongside the public branch.

### Version 1.2.0-alpha04

May 10, 2023

`androidx.credentials:credentials:1.2.0-alpha04` and `androidx.credentials:credentials-play-services-auth:1.2.0-alpha04` are released. This version is developed in an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 Beta 2 SDK.

### Version 1.2.0-alpha03

April 12, 2023

`androidx.credentials:credentials:1.2.0-alpha03` and `androidx.credentials:credentials-play-services-auth:1.2.0-alpha03` are released. This was released from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 Beta 1 SDK.

### Version 1.2.0-alpha02

March 8, 2023

`androidx.credentials:credentials:1.2.0-alpha02` and `androidx.credentials:credentials-play-services-auth:1.2.0-alpha02` are released. Developed from an internal branch.

> [!NOTE]
> **Note:** This version will only compile against the Android 14 Developer Preview 2 SDK.

**API Changes**

- Enable testing of provider request classes by making constructors public.
- Make icons required in all entry classes. However if credential providers do not provide icons, this library will have fallback icons.
- Allow credential providers to set multiple authentication action entries, and set a title for each.
- Remove all privileged request classes. Providers can now simply get the origin from `android.service.credentials.CallingAppInfo` class, and do not need to handle special request classes for privileged calls (calls on behalf of another app).

### Version 1.2.0-alpha01

February 8, 2023

`androidx.credentials:credentials:1.2.0-alpha01` and `androidx.credentials:credentials-play-services-auth:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bb0eba3464d207147e8ee1914b1576efdc6af02a/)

> [!NOTE]
> **Note:** This version will only compile against the Android 14 Developer Preview 1 SDK.

**New Features**

- This release added a new set of APIs for supporting Credential Provider in storing and fetching passwords, passkeys per users' requests.

**API Changes**

- New APIs added to support Credential Providers.

## Version 1.0

> [!NOTE]
> **Note:** All projects should use the [latest 1.2
> version of `androidx.credentials`](https://developer.android.com/jetpack/androidx/releases/credentials#latest). Earlier versions of `androidx.credentials` will throw an exception `UnsupportedOperationException("Post-U not supported yet")` when run on Android 14.

### Version 1.0.0-alpha09

June 7, 2023

`androidx.credentials:credentials:1.0.0-alpha09` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..73f902dee011bfe400d8a0330bfd8d4bb632065f/credentials)

**Bug Fixes**

- Validate that exception types are accurate and consistent. ([Id13d7](https://android-review.googlesource.com/q/Id13d7bda70f1020671151d4cf7f454f69754cfc9))
- Support the json format on get passkey request. ([I25100](https://android-review.googlesource.com/q/I25100adf372e101390b9a719aed97da8dc2d3cb2))
- Passkey Retrieval flow is backwards compatible with earlier GMS modules.([I23878](https://android-review.googlesource.com/q/I23878189ac283ca352c88852832f4527a700645a))

### Version 1.0.0-alpha08

May 3, 2023

`androidx.credentials:credentials:1.0.0-alpha08` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/07707e9f27eff2cebbd758a493ed2f38f9cf4739..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/credentials)

**Bug Fixes**

- Improved debug output readability and error messages.

### Version 1.0.0-alpha07

April 19, 2023

`androidx.credentials:credentials:1.0.0-alpha07` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..5418c9440f5def1af3c43cfb46de70bda1de09f6/credentials)

**Bug Fixes**

- Fix bug caused by configuration changes ([a75fca](https://android-review.googlesource.com/#/q/a75fcac0d319a411a6d750119b9ac2e0f3585a7c), [b/276316128](https://issuetracker.google.com/issues/276316128))
- Don't break the post U flow for the pre-U only SDK ([5418c9](https://android-review.googlesource.com/#/q/5418c9440f5def1af3c43cfb46de70bda1de09f6), [b/278148300](https://issuetracker.google.com/issues/278148300))

### Version 1.0.0-alpha06

April 5, 2023

`androidx.credentials:credentials:1.0.0-alpha06` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/credentials)

**New Features**

- Update the integration with Google ID, will work with `com.google.android.libraries.identity.googleid:googleid:1.0.0`

### Version 1.0.0-alpha05

March 22, 2023

`androidx.credentials:credentials:1.0.0-alpha05` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..5e7d256f82fbafb6d059ab7b18fddd87c7531553/credentials)

**Bug Fixes**

- Properly report the user cancellation error when the user cancels the modal sheet. ([/I9ff3](https://android-review.googlesource.com/#/q/I9ff3448a98cd8df945b2589f0b8ab64d636d2b09), [b/271863184](https://issuetracker.google.com/issues/271863184))

### Version 1.0.0-alpha04

March 8, 2023

`androidx.credentials:credentials:1.0.0-alpha04` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/credentials)

**API Changes**

- Added `android.permission.CREDENTIAL_MANAGER_SET_ORIGIN` requirement for setting origin in Jetpack Library. ([Ibaad4](https://android-review.googlesource.com/#/q/Ibaad45214490a891ad12302ec804f369145cb36f))
- Added passkey get flow exceptions ([I4f654](https://android-review.googlesource.com/#/q/I4f65428a0b5427b09eb60a4b3d0dfb224624dd4b))
- `CredentialManager` api autoselect behavior update ([I576dd](https://android-review.googlesource.com/#/q/I576ddece4d6eeeb10af9289ae577a19e9a0f8f19))
- `CreateCredentialRequest.DisplayInfo` now uses `CharSequence` rather than `String` fields. ([I85e70](https://android-review.googlesource.com/#/q/I85e70871ae9f675a6e77c4d111d03fa3e892b99a))

**Bug Fixes**

- Add proguard rules to ensure the play auth module won't be removed by R8. ([9543977](https://android-review.googlesource.com/#/q/I56381b53927a0fa7293d55b5ba5de97d933ae508))

### Version 1.0.0-alpha03

February 22, 2023

`androidx.credentials:credentials:1.0.0-alpha03` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/55580794d4c440e976bb7192109cea2b7da2bf63..87533b4ff06971ed59028936cd9b6da988cd4522/credentials)

**New Features**

- Added support for Sign-in with Google.

**API Changes**

- Allows `UnsupportedException` to function correctly ([I68208](https://android-review.googlesource.com/#/q/I68208c9cee42d1cd8b960ba0d283d9375d834b72))
- Adding a new exception type to account for cases such as when the device does not contain the necessary flags ([If08dd](https://android-review.googlesource.com/#/q/If08ddbfaefbc192973c1c7344f16de958b18d3f6))
- `CredentialManager` exception api ([I72947](https://android-review.googlesource.com/#/q/I7294752b0db08007284a589dc3487d658956e226))

### Version 1.0.0-alpha02

February 8, 2023

`androidx.credentials:credentials:1.0.0-alpha02` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..7d3ac1ab1206c01fae3ebb500b5b942636070155/credentials)

**API Changes**

- `CredentialManager` api signature changes ([Iabdec](https://android-review.googlesource.com/#/q/Iabdec2bc7154f9443a997923ae944cc241f44428))
- `CredentialManager` api signature changes ([I977ed](https://android-review.googlesource.com/#/q/I977ede12b0bd29e670f9b34ca1af342414b5926f))
- `CredentialManager` api signature changes ([Ia6e9b](https://android-review.googlesource.com/#/q/Ia6e9b6f3b9bf76612d6c7706db30b3a21e5727ca))

**Bug Fixes**

- Older 'cable' is no longer supported in the [webauthn spec](https://w3c.github.io/webauthn/#enum-transport), and its replacement, 'hybrid' is now returned for the transport list.
- Transports were given back in two dimensional lists, this has been fixed to be the correct 1d list.

### Version 1.0.0-alpha01

January 11, 2023

`androidx.credentials:credentials:1.0.0-alpha01` and `androidx.credentials:credentials-play-services-auth:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b/credentials)

**New Features**

- This release contains a new jetpack library which provides a unified access to a user's credentials. This can include passwords, passkeys and federated credentials. This library should be used to provide seamless and secure sign-in experiences.
- \`androidx.credentials:credentials-play-services-auth:1.0.0-alpha01 ' is an optional library that allows credentials to be stored to, and retrieved from Google Password Manager. This dependency is needed for devices running Android API level \<= 33.

**API Changes**

- New library with new APIs