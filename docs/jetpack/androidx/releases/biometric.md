---
title: https://developer.android.com/jetpack/androidx/releases/biometric
url: https://developer.android.com/jetpack/androidx/releases/biometric
source: md.txt
---

# Biometric

# Biometric

[User Guide](https://developer.android.com/training/sign-in/biometric-auth)[Code Sample](https://github.com/android/security-samples)  
API Reference  
[androidx.biometric](https://developer.android.com/reference/kotlin/androidx/biometric/package-summary)  
Authenticate with biometrics or device credentials, and perform cryptographic operations.  

| Latest Update |                                  Stable Release                                  | Release Candidate | Beta Release |                                          Alpha Release                                           |
|---------------|----------------------------------------------------------------------------------|-------------------|--------------|--------------------------------------------------------------------------------------------------|
| May 20, 2025  | [1.1.0](https://developer.android.com/jetpack/androidx/releases/biometric#1.1.0) | -                 | -            | [1.4.0-alpha04](https://developer.android.com/jetpack/androidx/releases/biometric#1.4.0-alpha04) |

## Declaring dependencies

To add a dependency on Biometric, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Java language implementation
    implementation "androidx.biometric:biometric:1.1.0"

    // Kotlin
    implementation "androidx.biometric:biometric-ktx:1.4.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    // Java language implementation
    implementation("androidx.biometric:biometric:1.1.0")

    // Kotlin
    implementation("androidx.biometric:biometric:1.4.0-alpha02")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:559537+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=559537&template=1214425)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.4

### Version 1.4.0-alpha04

May 20, 2025

`androidx.biometric:biometric:1.4.0-alpha04`is released. Version 1.4.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/biometric/biometric).

**New Features**

- Always use`KeyguardManager`API internally for Wear apps ([I9b7fd](https://android-review.googlesource.com/q/I9b7fd31ca5e3298ba350aefaf8c6fb79d2472f19))

**API Changes**

- Add a privileged authenticator bit`IDENTITY_CHECK`([I706bb](https://android-review.googlesource.com/#/q/I706bb650beea8f778788a950d77e9b927125bb96))

### Version 1.4.0-alpha03

March 26, 2025

`androidx.biometric:biometric:1.4.0-alpha03`is released. Version 1.4.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fcae1dc9e94201f2646e67b240aba31b52b964e9..78132378b67c86698d1ade3dc368c9f15d738a71/biometric/biometric).

**New Features**

- Introduced a new authentication entry point`registerForAuthenticationResult()`API to replace the`androidx.biometric:biometric-ktx`module and`androidx.BiometricPrompt`. This new API is modeled after the Activity Result API, and it provides seamless compatibility with both Kotlin and Java development.

**API Changes**

- Rename`ERROR_MORE_OPTIONS_BUTTON`to`ERROR_CONTENT_VIEW_MORE_OPTIONS_BUTTON`([I71d07](https://android-review.googlesource.com/#/q/I71d07855c221201e6770b325999b1546a7be446b))
- Add`@Deprecated`annotation for`IdentityCredential`to keep consistent with the framework. ([I6ac90](https://android-review.googlesource.com/#/q/I6ac906032150503829af6a4aca028037be7934af),[b/140252778](https://issuetracker.google.com/issues/140252778),[b/217942278](https://issuetracker.google.com/issues/217942278),[b/251211046](https://issuetracker.google.com/issues/251211046),[b/239955609](https://issuetracker.google.com/issues/239955609))
- \[1/3\] Remove biometric.auth and kotlin library, which will be redesigned. ([I2f67c](https://android-review.googlesource.com/#/q/I2f67c9f8993063fa5d981db7ae6021747e1bf74a))
- \[2/3\] Add`AuthenticationRequest`as authentication input and`AuthenticationResult`as authentication result type. There are two kinds of`AuthenticationRequest`, with builders. ([I50fd9](https://android-review.googlesource.com/#/q/I50fd9dbbeeae0cfbff504773530189b0dda01146))
  1. `BiometricRequest`for biometric authentication with different`Strength`and optional`Fallback`.
  2. `CredentialRequest`for device credential only authentication.
- \[3/3\] Add new activity-result-pattern APIs for biometric module. Specifically, add a registration API called`registerForAuthenticationResult()`, which registers the`AuthenticationResultCallback`and the optional`onAuthenticationFailedCallback`, and results a`AuthenticationResultLauncher`to start authentication with all input. ([I2b06e](https://android-review.googlesource.com/#/q/I2b06ecabb29f328741a260f10c11dbbc5dddf18b))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ib49b4](https://android-review.googlesource.com/#/q/Ib49b42a617d1fa3db7a57d4473553806c685bbb8),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Fixed an issue of being unable to instantiate fragment`androidx.biometric.FingerprintDialogFragment`. ([I51c4a](https://android-review.googlesource.com/q/I51c4a339887a885fbe3d4e11bc75784aabde6957),[b/181805603](https://issuetracker.google.com/issues/181805603))
- Fixed an issue where`BiometricPrompt`is not dismissed when the device's home button is pressed. ([I8c393](https://android-review.googlesource.com/q/I8c393f400d60f2b2af075671c4cf2727e63d82b8),[I0ca8c](https://android-review.googlesource.com/q/I0ca8caa58e11fc2cab3bf574a761c00ad4f3ae8d),[b/149770989](https://issuetracker.google.com/issues/149770989))
- Fixed error code inconsistencies for disabling biometric app auth on API 34/35. ([Ice99d](https://android-review.googlesource.com/q/Ice99d17108791cf093d033e16c32ccdb43222e4a),[b/386918213](https://issuetracker.google.com/issues/386918213))
- Apply forcing strong biometrics on older devices to combined authenticatiors too. ([Ibb853](https://android-review.googlesource.com/q/Ibb8532b5210407cfb530020f67d77210f58cfbc7),[I5cfb3](https://android-review.googlesource.com/q/I5cfb3b659781a1570ccd6aa607df3da61a559ebf),[b/257670132](https://issuetracker.google.com/issues/257670132))

### Version 1.4.0-alpha02

August 7, 2024

`androidx.biometric:biometric:1.4.0-alpha02`and`androidx.biometric:biometric-ktx:1.4.0-alpha02`are released. Version 1.4.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1d94b891f799ccff9307032b0d7531bfe80a4e3d..fcae1dc9e94201f2646e67b240aba31b52b964e9/biometric).

**New Features**

- `PromptContentView`allows developers to show the custom content view as an additional option of plain description text view
- App logo on Biometric Prompt is shown - automatically added using application icon.

**API Changes**

- Add APIs to support custom content view
  - `BiometricPrompt.PromptInfo.Builder#setContentView`
  - `BiometricPrompt.PromptInfo#getContentView`
  - `PromptContentView`interface
  - `PromptVerticalListContentView`class
  - `PromptContentViewWithMoreOptionsButton`class (for privileged apps only)
- Add APIs to support logo (for privileged apps only)
  - `BiometricPrompt.PromptInfo.Builder#setLogoBitmap`
  - `BiometricPrompt.PromptInfo.Builder#setLogoRes`
  - `BiometricPrompt.PromptInfo.Builder#setLogoDescription`
  - `BiometricPrompt.PromptInfo#getLogoBitmap`
  - `BiometricPrompt.PromptInfo#getLogoRes`
  - `BiometricPrompt.PromptInfo#getLogoDescription`[58c35c6](https://android.googlesource.com/platform/frameworks/support/+/58c35c67770fa9af042d5949f42d3e67c6dabee5)

**Bug Fixes**

- Update`compileSdk`to 35[5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f)

### Version 1.4.0-alpha01

May 29, 2024

`androidx.biometric:biometric:1.4.0-alpha01`and`androidx.biometric:biometric-ktx:1.4.0-alpha01`are released. This version is developed in an internal branch and targets Android 15 Beta 2.

**Bug Fixes**

- Update UI to be consistent with platform changes in Android 15

## Version 1.2.0

### Version 1.2.0-alpha05

September 21, 2022

`androidx.biometric:biometric:1.2.0-alpha05`and`androidx.biometric:biometric-ktx:1.2.0-alpha05`are released.[Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..4d0423307d5a9798592c75b46ecff047a14f36da/biometric)

**API Changes**

- Added`CryptoObject`support for`android.security.identity.PresentationSession`in Android 13. ([C5f1ec](https://android.googlesource.com/platform/frameworks/support/+/c5f1ecf9b0b80304bd430654ff81d1ebc25fe8e4),[b/197965513](https://issuetracker.google.com/issues/197965513))

**Bug Fixes**

- Removed unnecessary resource variants to reduce library size. ([I3601e](https://android-review.googlesource.com/#/q/I3601ea0d92720b4456c6311917bb8a3728c97d02),[b/220178553](https://issuetracker.google.com/issues/220178553))
- Fixed issue for`BiometricPrompt`hosted in non-activity contexts. ([Ife255](https://android-review.googlesource.com/q/Ife255c7e5d55ecd0439eda2c7c386e53da2907af))

### Version 1.2.0-alpha04

November 17, 2021

`androidx.biometric:biometric:1.2.0-alpha04`and`androidx.biometric:biometric-ktx:1.2.0-alpha04`are released.[Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..cc1240d00b28657ee0c1a937f60430eaf1b03b09/biometric)

**New Features**

- Improved BiometricPrompt support for fragments that are hosted by non-activity contexts ([I9312b](https://android-review.googlesource.com/#/q/I9312befb2355f746e8fc4d1d68db4b80ae71d80f))

**API Changes**

- Added support for the Android 12[BiometricManager.Strings](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings)API ([I12f2d](https://android-review.googlesource.com/#/q/I12f2d943fcb69e7430f701338d5a392b63fe9923))
- Changed target and source compatibility from Java 7 to Java 8 ([I16129](https://android-review.googlesource.com/#/q/I16129eb28425183bc2f1f016c89ac6a96668574f))

**Bug Fixes**

- Fixed an issue on API 29 where some devices (including emulators) would receive a cancellation error when falling back to PIN/pattern/password. Note that, for some devices on API 29, this may cause the user to be prompted for their screen lock even if a biometric is available and enrolled. ([b/142740104](https://issuetracker.google.com/issues/142740104))
- Fixed an issue on API 29 where devices with no biometric hardware would not correctly fall back to PIN/pattern/password ([b/170517889](https://issuetracker.google.com/issues/170517889))

### Version 1.2.0-alpha03

February 24, 2021

`androidx.biometric:biometric:1.2.0-alpha03`and`androidx.biometric:biometric-ktx:1.2.0-alpha03`are released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..5c90131a69042a6a3e13952e1da9e7ffc571c31d/biometric/biometric)

**API Changes**

- Added suspending coroutine extensions for CredentialAuthPrompt similar to those that exist for other AuthPrompt types. ([I9ac70](https://android-review.googlesource.com/#/q/I9ac70c62d19f3b3d07d60023aabaf7c0e39eabac))

### Version 1.2.0-alpha02

January 27, 2021

`androidx.biometric:biometric:1.2.0-alpha02`and`androidx.biometric:biometric-ktx:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2475d1f697cc729edc0b1b3dbfd991929626c748..aee18b103203a91ee89df91f0af5df2ecff356d6/biometric)

**API Changes**

- Refactored some`AuthPrompt`fields that were previously set via a builder into`startAuthentication(...)`method arguments. ([I18896](https://android-review.googlesource.com/#/q/I1889656362afd7190adb22d34f047766d312735b),[b/174098373](https://issuetracker.google.com/issues/174098373))
- Added minimum API level requirements for`AuthPrompt`types with limited or no support on older Android versions. ([I18896](https://android-review.googlesource.com/#/q/I1889656362afd7190adb22d34f047766d312735b))
- Added getter methods for all`AuthPrompt`fields that are set via a builder. ([I18896](https://android-review.googlesource.com/#/q/I1889656362afd7190adb22d34f047766d312735b))
- Added suspending coroutine Kotlin extensions for biometric authentication via the`AuthPrompt`APIs. These functions will return the`AuthenticationResult`directly on success or throw an exception on error or failure (credential rejection). ([Iffc9e](https://android-review.googlesource.com/#/q/Iffc9eeab8f3d866027830acdab09d91dba86e812))

**Bug Fixes**

- Fixed an issue where`BiometricManager.canAuthenticate(int)`would sometimes return the wrong status code for a device with a fingerprint sensor on Android 10 (API level 29). ([I72420](https://android-review.googlesource.com/#/q/I72420b5721ea41bae8b037f43ab8fbd49250ebf2),[b/176921662](https://issuetracker.google.com/issues/176921662))
- Fixed an issue where`BiometricManager.canAuthenticate(int)`would return the wrong status code for a device with no biometric hardware and no enrolled PIN, pattern, or password on Android 10 (API level 29) and prior SDK versions. ([I79b7d](https://android-review.googlesource.com/#/q/I79b7dbf009c44582c4693be5d27dd850777ab4d1),[b/174505824](https://issuetracker.google.com/issues/174505824))
- Fixed a memory leak that would occur when`BiometricPrompt`was hosted in a fragment with a shorter lifecycle than its associated activity. ([I70864](https://android-review.googlesource.com/#/q/I7086460fac3921a490f4e2abf0671adec5c146bd),[b/167014923](https://issuetracker.google.com/issues/167014923))

### Version 1.2.0-alpha01

December 2, 2020

`androidx.biometric:biometric:1.2.0-alpha01`and`androidx.biometric:biometric-ktx:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2475d1f697cc729edc0b1b3dbfd991929626c748/biometric)

**New Features**

- Introduced the`androidx.biometric:biometric-ktx`module, which adds Kotlin-specific APIs and extensions on top of`androidx.biometric:biometric`.

**API Changes**

- Added new`AuthPrompt`APIs for constructing a`BiometricPrompt`and performing authentication. These APIs do*not* require the`BiometricPrompt`to be constructed in an early lifecycle callback, such as`onCreate`. ([I19022](https://android-review.googlesource.com/#/q/I1902297133cb02b745bda185c2c9497cf52b73a5))
- Added Kotlin extensions to`Fragment`and`FragmentActivity`for the new`AuthPrompt`APIs. ([Iaf98c](https://android-review.googlesource.com/#q/Iaf98c1f4ef874394239e2722c60093a148a90dc3))

## Version 1.1.0

### Version 1.1.0

January 27, 2021

`androidx.biometric:biometric:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/53eb1a11c149d2d5924eb88ae2ebb86bc61eb27b..c70e4a93bc85cc874a265a67336315991aff82e5/biometric/biometric)

**Major changes since 1.0.0**

- Added backwards-compatible support for new biometric authentication[features and API updates](https://developer.android.com/about/versions/11/features#biometric-auth)introduced in Android 11.
- Significantly reduced the app size footprint of the library (by \>100 KB, in some cases).
- Removed various sources of memory leaks that were previously caused by the library.
- Fixed class verification failures that could affect performance on older Android versions.
- Made various additional improvements to the stability and behavior of the library.

### Version 1.1.0-rc01

November 11, 2020

`androidx.biometric:biometric:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..53eb1a11c149d2d5924eb88ae2ebb86bc61eb27b/biometric)

**Bug Fixes**

- Fixed an issue on some devices where certain actions (authenticating, canceling, etc.) would sometimes throw a`NullPointerException`. ([b/151316421](https://issuetracker.google.com/issues/151316421))
- Fixed an issue where some Pixel devices would report the wrong status when using`BiometricManager#canAuthenticate(int)`to check for**Class 3** biometrics on Android 10. ([b/170406186](https://issuetracker.google.com/issues/170406186))

### Version 1.1.0-beta01

October 1, 2020

`androidx.biometric:biometric:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/biometric/biometric)

**New Features**

- Significantly reduced the library's APK size footprint (by \>100 KB compressed, in some cases) by replacing dialog animations with static assets on Android 8.1 and earlier. ([I4844e](https://android-review.googlesource.com/q/I4844e5d47da629c1a7017edbc6b84f4f10e12a5f))
- `BiometricPrompt`now automatically falls back to device credential authentication (if allowed) on all supported Android versions when biometric authentication is locked out. ([b/149579143](https://issuetracker.google.com/issues/149579143))

**Bug Fixes**

- Fixed an issue where`BiometricPrompt`caused a crash on some Android 9 devices without a fingerprint sensor. ([b/151443237](https://issuetracker.google.com/issues/151443237))
- Fixed a potential`NullPointerException`in`FingerprintDialogFragment`. ([b/167951429](https://issuetracker.google.com/issues/167951429))
- Fixed an issue where the wrong`CryptoObject`type was used for a reflective method invocation in`BiometricManager`. ([b/165824669](https://issuetracker.google.com/issues/165824669))
- Fixed an issue where showing`BiometricPrompt`again shortly after dismissal caused the new prompt to be dismissed automatically on some Android 10 devices. ([b/157783075](https://issuetracker.google.com/issues/157783075))
- Fixed memory leaks related to the use of`FingerprintManagerCompat`. ([b/165840273](https://issuetracker.google.com/issues/165840273))
- Fixed issues with the fingerprint dialog UI being hidden or shown incorrectly on some Android 9 devices. ([b/154868505](https://issuetracker.google.com/issues/154868505),[b/148350291](https://issuetracker.google.com/issues/148350291))

### Version 1.1.0-alpha02

August 19, 2020

`androidx.biometric:biometric:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..96eb302ee1740ba656c90c9fb27df3723a1a89c1/biometric/biometric)

**New Features**

- `BiometricManager#canAuthenticate()`may now return`BIOMETRIC_STATUS_UNKNOWN`to indicate that the user*may* still be able to authenticate, or`BIOMETRIC_ERROR_UNSUPPORTED`to indicate that a given authenticator combination is not supported by the device.
- `BiometricPrompt#authenticate()`may now be used for device credential authentication with an associated`CryptoObject`on Android 11 (API level 30) and above*only*.

**API Changes**

- Made it optional to provide an explicit`Executor`when constructing an instance of`BiometricPrompt`. ([I6bb8a](https://android-review.googlesource.com/#/q/I6bb8ad575f02611ca235fe1ff3123a032f2e6d1d))
- Added the[`BiometricManager#canAuthenticate(int)`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager#canAuthenticate(int))method from Android 11. ([Ia3f1c](https://android-review.googlesource.com/#/q/Ia3f1c378e2d1638f872dfb0a18589d61d8ddb087))
- Updated`BiometricPrompt`to add support for[`BiometricManager.Authenticators`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Authenticators)constants from Android 11. ([I39bd8](https://android-review.googlesource.com/#/q/I39bd8917d35f8f38db52106a9a77d47af24a6d30))
- Added the[`BiometricPrompt.AuthenticationResult#getAuthenticationType()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.AuthenticationResult#getAuthenticationType())method from Android 11. ([Icfad5](https://android-review.googlesource.com/#/q/Icfad54cdf7baa5719e54464e0d33fc6757bb12c2))
- Added the[`BiometricPrompt.ERROR_SECURITY_UPDATE_REQUIRED`](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt#BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED)error code from Android 11. ([I6610b](https://android-review.googlesource.com/#/q/I6610b1602ef48de1e093c2dd58d742257eaeb268))
- Updated`BiometricPrompt.CryptoObject`to support[`IdentityCredential`](https://developer.android.com/reference/android/security/identity/IdentityCredential)on Android 11 (API level 30) and above*only* . ([I1d9f6](https://android-review.googlesource.com/#/q/I1d9f661240f8a5ce889ce5caef6c95933d60559d))

**Bug Fixes**

- Fixed memory leaks reported by LeakCanary in`BiometricFragment`and`BiometricViewModel`. ([b/144919472](https://issuetracker.google.com/issues/144919472))
- Ensured that`BiometricViewModel`will no longer call`MutableLiveData#setValue()`from a background thread. ([b/159983244](https://issuetracker.google.com/issues/159983244))
- Fixed an issue where`BiometricPrompt`was not correctly handling temporary lockout on some API levels. ([9acfce9](https://android-review.googlesource.com/#/q/9acfce9decd30444242fbfee799ff509511817f3))
- Fixed an issue where`BiometricPrompt`would return the wrong error code for a device not secured with a screen lock credential on some API levels. ([b/148626482](https://issuetracker.google.com/issues/148626482))
- Fixed an issue where`BiometricManager`and`BiometricPrompt`would return the wrong error codes for a device with no keyguard implementation on some API levels. ([891c6e0](https://android-review.googlesource.com/#/q/891c6e0c97fbe94b47a544994d8abd6162e583f8))

### Version 1.1.0-alpha01

June 24, 2020

`androidx.biometric:biometric:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33c93675e3a1ba85a74980937fb3df96824f7888..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/biometric/biometric)

**New Features**

- Refactored the internal library implementation to address potential sources of memory leaks and other unintended behavior:
  - Internal fragments now share and persist data using a`ViewModel`that is tied to the client application's activity lifecycle.
  - Device credential authentication prior to Android 10 (API level 29) no longer starts a transparent activity within the client application.

**Bug Fixes**

- Resolved deprecation warnings related to the use of`FingerprintManagerCompat`. ([b/142967618](https://issuetracker.google.com/issues/142967618))
- Changed how SDK-gated platform methods are called to avoid class verification issues on older Android versions. ([94beb4b](https://android.googlesource.com/platform/frameworks/support/+/94beb4b7bf9f66e78bd767bc4e4e3c0448e25689))
- Gradle dependencies that are not part of the public API are no longer exported by the library. ([f289d9e](https://android.googlesource.com/platform/frameworks/support/+/f289d9eca14bc9d88d6fae7599fd3137437972b9))

## Version 1.0.1

### Version 1.0.1

December 18, 2019

`androidx.biometric:biometric:1.0.1`is released.[Version 1.0.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/5232c33def2f56cb56ae395aba84c7cf95f27864..33c93675e3a1ba85a74980937fb3df96824f7888/biometric).

**Bug fixes**

- Extended the existing fingerprint fallback workaround for crypto-based authentication to known affected vendors, while also limiting it to API 28 ([b/143361271](https://issuetracker.google.com/143361271))
- Fixed an issue on certain devices where the biometric dialog was shown under a system overlay ([b/143230260](https://issuetracker.google.com/143230260))
- Fixed several issues with`setDeviceCredentialAllowed(true)`([b/143091227](https://issuetracker.google.com/143091227),[b/143097321](https://issuetracker.google.com/143097321),[b/143653944](https://issuetracker.google.com/143653944))
- Fixed an issue on certain Android versions where`onAuthenticationSuccess`was not always called after the user confirmed their device credential ([b/145232806](https://issuetracker.google.com/145232806))
- Fixed an issue on certain Android versions where`onAuthenticationError`was not always called when the prompt was dismissed on rotation ([b/145230042](https://issuetracker.google.com/145230042))
- Fixed an issue on certain Android versions where the prompt was not dismissed when receiving certain error codes ([b/143683687](https://issuetracker.google.com/143683687))
- Fixed a potential`NullPointerException`in`BiometricFragment`([b/142599311](https://issuetracker.google.com/142599311))

## Version 1.0.0

### Version 1.0.0

November 7, 2019

`androidx.biometric:biometric:1.0.0`is released with no changes since`1.0.0-rc02`.[Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/4be2d81a8c67ebabf9c92d684f7fa293015f418e..5232c33def2f56cb56ae395aba84c7cf95f27864/biometric).

**Major features of 1.0.0**

- Compatibility version of the`BiometricPrompt`and`BiometricManager`APIs, as implemented in Android 10, with full feature support back to Android 6.0 (API 23)
- Built-in lifecycle management for`BiometricPrompt`within a`Fragment`or`FragmentActivity`
- Special handling for devices known to incorrectly present weak biometrics during crypto-based authentication

### Version 1.0.0-rc02

October 23, 2019

`androidx.biometric:biometric:1.0.0-rc02`is released.[Version 1.0.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/fe945d3eaf74d53a53dfbb4a0ba51bb0781be415..4be2d81a8c67ebabf9c92d684f7fa293015f418e/biometric).

**Bug fixes**

- Added a workaround for certain devices that are known to incorrectly provide a weak biometric when crypto-based authentication is invoked on API versions 28 and 29 ([b/142150327](https://issuetracker.google.com/issues/142150327))

### Version 1.0.0-rc01

October 9, 2019

`androidx.biometric:biometric:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2606d2aabf9da268b7680e9bcd791e4797425dbd..fe945d3eaf74d53a53dfbb4a0ba51bb0781be415/biometric).

**Bug fixes**

- Fixed a potential crash with`FingerprintDialogFragment`when dismissing it while the screen is rotating ([b/141356362](https://issuetracker.google.com/issues/141356362))
- Fixed an issue where receiving a null`AuthenticationResult`from the framework API could cause a crash ([b/138862251](https://issuetracker.google.com/issues/138862251))
- Fixed crashes caused by`BiometricPrompt`being dismissed after`onSaveInstanceState()`([b/138825362](https://issuetracker.google.com/issues/138825362),[b/140447194](https://issuetracker.google.com/issues/140447194))

### Version 1.0.0-beta02

September 18, 2019

`androidx.biometric:biometric:1.0.0-beta02`is released.[Version 1.0.0-beta02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/a3b34e760b913aaf27b25e76cc171bdd86ec3d3b..2606d2aabf9da268b7680e9bcd791e4797425dbd/biometric).

**Bug fixes**

- Fixed issues with device credential support in version`1.0.0-beta01`
- Removed Java 8 dependencies and switched to depending on Java 7 ([b/140508526](https://issuetracker.google.com/issues/140508526))
- `FingerprintHelperFragment`now correctly throws`ERROR_HW_NOT_PRESENT`when no fingerprint hardware is detected ([b/140427586](https://issuetracker.google.com/issues/140427586))

### Version 1.0.0-beta01

August 29, 2019

`androidx.biometric:biometric:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8de83833a365a0342a01630807c96f42e64782b..a3b34e760b913aaf27b25e76cc171bdd86ec3d3b/biometric).

**New features**

We've introduced a second constructor for BiometricPrompt that allows it to be hosted in a Fragment (as opposed to the existing constructor, which requires a FragmentActivity).

We're also excited to bring the following functionality from Android 10 to the AndroidX Biometric library:

1. `BiometricManager#canAuthenticate`
2. `BiometricPrompt.PromptInfo#setConfirmationRequired`
3. `BiometricPrompt.PromptInfo#setDeviceCredentialAllowed`

On Android 10, the library will invoke the corresponding methods from the platform API. On older API levels, the library will emulate the behavior.

**API changes**

- Added fragment-specific constructor for biometric prompt ([b/131980596](https://issuetracker.google.com/issues/131980596))
- See the "New features" section above.

**Bug fixes**

- Add BiometricPrompt device credential support for L+
- Fixed BiometricPrompt to use public error constants ([b/137788194](https://issuetracker.google.com/issues/137788194))
- Fix`NullPointerException`in`BiometricPrompt.onAttach()`([b/136103103](https://issuetracker.google.com/issues/136103103))
- Changed behavior to not allow BiometricPrompt to be cancelled by a touch event outside the prompt ([b/135684487](https://issuetracker.google.com/issues/135684487))
- Fixed onAuthenticationError crash when a null error value is returned in Kotlin ([b/128350861](https://issuetracker.google.com/issues/128350861))
- FingerprintDialogFragment is now style-able ([b/127878106](https://issuetracker.google.com/issues/127878106))
- FingerprintDialog is now scrollable ([b/126367887](https://issuetracker.google.com/issues/126367887))
- Fixed bug where rotating the biometric dialog raises an`IllegalStateException`([b/124153656](https://issuetracker.google.com/issues/124153656)), ([b/123811924](https://issuetracker.google.com/issues/123811924))
- Fixed inconsistent behavior on API Levels 23 to 27. ([b/124066957](https://issuetracker.google.com/issues/124066957))
- Fixed issue where Fingerprint Login Dialog read incorrect text using Talkback. ([b/123572331](https://issuetracker.google.com/issues/123572331))

### Version 1.0.0-alpha04

April 3, 2019

`androidx.biometric:biometric:1.0.0-alpha04`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/82b61c231e74262ac499b9788e8af46e2c4bf779..b8de83833a365a0342a01630807c96f42e64782b/biometric).

**Bug fixes**

- Fixed Biometric fragments don't clean up in all cases. ([b/121117380](https://issuetracker.google.com/issues/121117380))
- Fixed`BiometricPrompt`only allows one instance of`BiometricPrompt.AuthenticationCallback`([b/123857949](https://issuetracker.google.com/issues/123857949))
- Fixed`BiometricPrompt`error behavior inconsistent between system and compat versions. ([b/123572326](https://issuetracker.google.com/issues/123572326))
- Fixed callback`onAuthenticationError()`with`@NotNull errString`causes`NullPointerException`at runtime ([b/123167217](https://issuetracker.google.com/issues/123167217))
- Fixed`androidx.BiometricPrompt`Cancel button Crashes ([b/122054485](https://issuetracker.google.com/issues/122054485))
- Fixed`androidx.biometric.PromptInfo`title/description not changed on Android P ([b/122856773](https://issuetracker.google.com/issues/122856773))

### Version 1.0.0-alpha03

December 17, 2018

**Bug fixes**

- Fixed fragment-related issues
- On devices O and older, lockout errors are returned immediately to be consistent with P and above