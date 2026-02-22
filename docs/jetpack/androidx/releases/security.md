---
title: https://developer.android.com/jetpack/androidx/releases/security
url: https://developer.android.com/jetpack/androidx/releases/security
source: md.txt
---

| **Warning:** The `security-crypto` and `security-crypto-ktx` libraries have been deprecated and no further versions will be shipped. See the release notes and the [deprecation documentation](https://developer.android.com/privacy-and-security/cryptography#security-crypto-jetpack-deprecated) for details.

# Security

[User Guide](https://developer.android.com/topic/security/data) [Code Sample](https://github.com/android/security-samples) API Reference  
[androidx.security.crypto](https://developer.android.com/reference/kotlin/androidx/security/crypto/package-summary)  
Safely manage keys and encrypt files and sharedpreferences. Warning: The \`security-crypto\` and \`security-crypto-ktx\` libraries have been deprecated and no further versions will be shipped. See the release notes and the \[deprecation documentation\](/privacy-and-security/cryptography#security-crypto-jetpack-deprecated) for details.


This table lists all the artifacts in the `androidx.security` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| security-crypto | [1.1.0](https://developer.android.com/jetpack/androidx/releases/security#security-crypto-1.1.0) | - | - | - |
| security-app-authenticator | [1.0.0](https://developer.android.com/jetpack/androidx/releases/security#security-app-authenticator-1.0.0) | - | - | - |
| security-app-authenticator-testing | [1.0.0](https://developer.android.com/jetpack/androidx/releases/security#security-app-authenticator-testing-1.0.0) | - | - | - |
| security-identity-credential | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/security#security-identity-credential-1.0.0-alpha03) |

This library was last updated on: February 11, 2026

## Declaring dependencies

To add a dependency on Security, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:618647+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=618647&template=1257270)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.
| **Warning:** The `security-crypto` and `security-crypto-ktx` libraries have been deprecated and no further versions will be shipped. See the release notes and the [deprecation documentation](https://developer.android.com/privacy-and-security/cryptography#security-crypto-jetpack-deprecated) for details.

## Security-State-Provider Version 1.0

### Version 1.0.0-alpha02

February 11, 2026

`androidx.security:security-state-provider:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/security/security-state-provider).

**New Features**

- Bound Service Architecture: Replaced `UpdateInfoProvider` (ContentProvider) with `UpdateInfoService` (Bound Service). This improves performance by avoiding application startup penalties.
- Telemetry \& Observability: The new service includes built-in hooks (`onRequestCompleted`, `onClientConnected`) for monitoring request latency, lock contention, and caller attribution.

**API Changes**

- Added `UpdateInfoService`: Abstract base class for implementing update providers. Handles IPC, concurrency (double-checked locking), and caching. ([Ib0fe0](https://android-review.googlesource.com/#/q/Ib0fe06674d952c442d46ba4837774a1e5196f729))
- Added Telemetry Classes: `UpdateCheckTelemetry` and `UpdateFetchOutcome`. ([I9d852](https://android-review.googlesource.com/#/q/I9d85227424dcd98b6cf883fd7669bb13e9f136e6))
- Moved the `UpdateInfo` class from the `security-state-provider` module to the `security-state module`. ([I23ea2](https://android-review.googlesource.com/#/q/I23ea2d18f55203ec47bcbed64da43d2f3a874061))

### Version 1.0.0-alpha01

September 24, 2025

`androidx.security:security-state-provider:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a/security/security-state-provider).

**New Features**

- This is the initial alpha release of the `security-state-provider` library.
- This library makes it easy for update clients (like OTA clients) to publish the security state of updatable components (system, system modules, kernel, ...) on a device.
- It provides mechanisms to register and unregister update information, which can then be served to other applications or components via a `ContentProvider`.
- Includes `UpdateInfoProvider`: A `ContentProvider` that serves `UpdateInfo` in JSON format. Supports querying but not insert, delete, or update operations.
- Includes `UpdateInfoManager`: Manages the storage and retrieval of `UpdateInfo` objects, using `SharedPreferences` for persistence.
- Includes `UpdateInfo`: A data class to represent information about an available update for a component, including URI, component name, Security Patch Level (SPL), and published date.

## Security-State Version 1.1

### Version 1.1.0-alpha01

February 11, 2026

`androidx.security:security-state:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/security/security-state).

**New Features**

- Available SPL: Introduced new APIs that allow the device to query trusted update providers---such as OEM updaters or Google Play System Updates---to determine if a more recent security patch is available.
- Supplemental Security Patches: The `areCvesPatched()` API was updated to accommodate the Android Security Bulletin's new Risk Based Update System (RBUS) release structure. This enables applications to verify if specific vulnerabilities have been addressed through supplemental OEM patches, even when the device's official Security Patch Level (SPL) date remains unchanged.

**API Changes**

- Added `queryAllAvailableUpdates` API to `SecurityPatchState`. This API identifies every trusted update provider and retrieves the list of available updates they offer. ([Iede1f](https://android-review.googlesource.com/#/q/Iede1ffecc351d0c1c237d9b9f5cf8d264289e350))
- Added `fetchAvailableSecurityPatchLevel` API to `SecurityPatchState`. This API aggregates results and returns the latest available `SecurityPatchLevel`. ([Ib7bcf](https://android-review.googlesource.com/#/q/Ib7bcf5a0ca121eb5f26adaf59a0e84ad5ef1e9c7))
- Moved the `UpdateInfo` class from the `security-state-provider` module to the `security-state` module. ([I23ea2](https://android-review.googlesource.com/#/q/I23ea2d18f55203ec47bcbed64da43d2f3a874061))

## Security-State Version 1.0.0

### Version 1.0.0-beta01

February 26, 2025

`androidx.security:security-state:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..fd7408b73d9aac0f18431c22580d9ab612278b1e/security/security-state).

**Bug Fixes**

- Fixed an issue that prevented `getPatchedCves()` from returning patched CVEs for `COMPONENT_SYSTEM_MODULES`. ([Ice5e2](https://android-review.googlesource.com/#/q/Ice5e211448ddaade95e0dafd815b5f17a79ab199))

### Version 1.0.0-alpha05

January 29, 2025

`androidx.security:security-state:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..4c47131cd5b50c3091fc0874eb606aaac5b168fa/security/security-state).

**New Features**

- The package names of the default system modules were added to the library's manifest to allow client apps to get the Device SPL for System Modules. ([Ic259c](https://android-review.googlesource.com/#/q/Ic259c7214ec22804c37f6bae2d48fa74579156b4))

**API Changes**

- Renamed `SecurityStateManager` to `SecurityStateManagerCompat`, added additional documentation for public properties and functions, and made `getComponentSecurityPatchLevel` and `getVulnerabilityReportUrl` static methods. ([I44a0c](https://android-review.googlesource.com/#/q/I44a0c76d7c91dc3a60f44758ce0d27e0432a1203))
- The Update Availability functionality (`listAvailableUpdates()` and `getAvailableSecurityPatchLevel()` methods) has been removed from the API surface for now and is planned to return in a future update to the library. ([Idbc5e](https://android-review.googlesource.com/#/q/Idbc5e5ec03b8434cb2f93e238ec1cc06fe1b1d04))
- Accessing Vendor SPL is now guarded by a compile-time flag that is disabled by default until a future update to the library. ([I45b58](https://android-review.googlesource.com/#/q/I45b58d0673b66bbeb29faf12035e318c06dcccc8))
- `getGlobalSecurityState()` now returns the global security state from the system service for SDK 35+. ([I7b9da](https://android-review.googlesource.com/#/q/I7b9dac324d0b24748e586c26600914037c2960c5))

**Bug Fixes**

- Fixed a crash that occurred when trying to get the Published SPL for Kernel on older versions of Android where published Kernel LTS versions aren't available. ([I93dff](https://android-review.googlesource.com/#/q/I93dff60460799818203a1272e5b1e1a0df970f00))

### Version 1.0.0-alpha04

August 7, 2024

`androidx.security:security-state:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..9130b719318a69f2f3eaf82c32b131232fd721cb/security/security-state).

**Note**

- Update `compileSdk` to 35 [5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f)

**API Changes**

- Breaking change: Component enum was replaced with string constants for extensibility. ([Ia3283](https://android-review.googlesource.com/#/q/Ia32836e46ac3997026f08ff890a8c7ed0361427b))

### Version 1.0.0-alpha03

July 10, 2024

`androidx.security:security-state:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..56579bc30499ce39f0d7a6713a065b00c6194206/security/security-state).

**Bug Fixes**

- Fixing ASB-A- pattern for Android security bulletin bugs, JSON parsing for additional components, and `Webview` packaged retrieval. ([Ide86a](https://android-review.googlesource.com/#/q/Ide86ae11b67041db6aeca40ea1c54a08d3b8109d))

### Version 1.0.0-alpha02

June 26, 2024

`androidx.security:security-state:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..948119be341fa4affc055418e695d8c4c7e5e2e4/security/security-state).

**Bug Fixes**

- Fixed logic of getting kernel version. ([I5602a](https://android-review.googlesource.com/#/q/I5602a8e1eaa48985d704622195f147a81828e4f0))

### Version 1.0.0-alpha01

June 12, 2024

`androidx.security:security-state:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b/security/security-state).

**New Features**

- Security State is a new library developers can use to get actionable data about versions of updateable system components, security updates and applied fixes.

## Security-App-Authenticator-Testing Version 1.0.0

### Version 1.0.0

July 30, 2025

`androidx.security:security-app-authenticator:1.0.0` and `androidx.security:security-app-authenticator-testing:1.0.0` are released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5a63cd1b3ff7a88c2b3df6bbe7dcf4c4290a9e8e..12e7f8e66c5e70ca5c59342b4fb6c82e6e50a37c/security).

### Version 1.0.0-rc01

May 20, 2025

`androidx.security:security-app-authenticator:1.0.0-rc01` and `androidx.security:security-app-authenticator-testing:1.0.0-rc01` are released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..5a63cd1b3ff7a88c2b3df6bbe7dcf4c4290a9e8e/security).

### Version 1.0.0-beta01

March 6, 2024

`androidx.security:security-app-authenticator:1.0.0-beta01` and `androidx.security:security-app-authenticator-testing:1.0.0-beta01` are released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/security).

### Version 1.0.0-alpha02

December 13, 2023

`androidx.security:security-app-authenticator-testing:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/security/security-app-authenticator-testing)

**Bug Fixes**

- Updated test for new API behavior that no longer assumes `Binder#getCalling[Uid|Pid]` when not provided to the `[check|enforce]CallingAppIdentity` APIs. ([I1851b](https://android-review.googlesource.com/#/q/I1851bd20049e5be1d208a24633423080c5e38f7c))

### Version 1.0.0-alpha01

June 2, 2021

`androidx.security:security-app-authenticator-testing:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4/security/security-app-authenticator-testing)

**New Features**

This testing library provides a builder that can be used to configure an injectable AppAuthenticator to meet the requirements of the test. This library supports several methods to configure the AppAuthenticator:

- A generic test policy can be specified that reports a signature match for all packages declared in the configuration.
- Individual packages can be specified to return a signature match with all other packages reporting no match.
- Explicit signing identities can be set for each package; the resulting AppAuthenticator will then only report a signature match if the provided identity matches the declaration in the configuration file.
- Packages can also be treated as not installed or having an explicit uid.

## Security-App-Authenticator Version 1.0.0

### Version 1.0.0-rc01

May 20, 2025

`androidx.security:security-app-authenticator:1.0.0-rc01` and `androidx.security:security-app-authenticator-testing:1.0.0-rc01` are released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..5a63cd1b3ff7a88c2b3df6bbe7dcf4c4290a9e8e/security).

### Version 1.0.0-beta01

March 6, 2024

`androidx.security:security-app-authenticator:1.0.0-beta01` and `androidx.security:security-app-authenticator-testing:1.0.0-beta01` are released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/security).

### Version 1.0.0-alpha03

December 13, 2023

`androidx.security:security-app-authenticator:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/security/security-app-authenticator)

**API Changes**

- Added support for use cases where the UID / PID of the package to be verified is not available; the APIs now support cases such as `startActivityForResult` and activities / receivers where the calling app's identity is shared via `[Activity|Broadcast]Options#setShareIdentityEnabled`.
- The behavior of `[check|enforce]CallingAppIdentity(String, String)` has been updated to support these new use cases; these methods will no longer default to using `Binder#getCalling[Uid|Pid]` but will instead skip verification of the calling package's UID if it is not explicitly provided. ([I1851b](https://android-review.googlesource.com/#/q/I1851bd20049e5be1d208a24633423080c5e38f7c))

### Version 1.0.0-alpha02

June 2, 2021

`androidx.security:security-app-authenticator:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..86ff5b4bb956431ec884586ce0aea0127e189ec4/security/security-app-authenticator)

**API Changes**

- In preparation to support the new `knownSigner` permission protection flag introduced in Android 12, the digestAlgorithm attribute can no longer be specified in the configuration; instead all certificate digests should be computed using SHA-256.

**Bug Fixes**

- All certificate digests provided in the configuration are now normalized to ensure a successful signature match can be reported both when the digest is computed at runtime as well as when an explicit signing identity is defined when using the testing library.

### Version 1.0.0-alpha01

May 5, 2021

`androidx.security:security-app-authenticator:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/security/security-app-authenticator)

**New Features**

AppAuthenticator is a new library aimed at simplifying verification of app trust based on signing identity. An app just needs to specify an XML configuration file containing the package names and signing identities of trusted apps, and the library will take care of verifying the signing identity of apps at runtime.

## Security-Identity-Credential Version 1.0.0

### Version 1.0.0-alpha03

September 1, 2021

`androidx.security:security-identity-credential:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..47e81d1c497b8a57534a460c277855db1b0257ae/security/security-identity-credential)

**New Features**

- Added support for hardware-backed Identity Credential features in Android 12.

### Version 1.0.0-alpha02

February 24, 2021

`androidx.security:security-identity-credential:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..5c90131a69042a6a3e13952e1da9e7ffc571c31d/security/identity-credential)

**Bug Fixes**

- Update Identity Credential API to match Android 12 plans ([Iff83e](https://android-review.googlesource.com/#/q/Iff83e3fe9501e6a3a3c5239ba013f0a3703ce014))

### Version 1.0.0-alpha01

August 19, 2020

`androidx.security:security-identity-credential:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1/security/identity-credential)

**New Features**

This Jetpack release features a Jetpack version of the Identity Credential APIs which was added to Android 11 and API level 30. If running on Android 11 and the device has hardware-backed Identity Credential support then this Jetpack simply forwards calls to the platform API. Otherwise, an Android Keystore-backed implementation will be used. While the Android Keystore-backed implementation does not provide the same level of security and privacy it is perfectly adequate for both holders and issuers in cases where all data is issuer-signed. This library requires API level 24 or later.

The Identity Credential APIs provide an interface to a secure store for user identity documents. These APIs are deliberately fairly general and abstract. To the extent possible, specification of the message formats and semantics of communication with credential verification devices and Issuing Authorities (IAs) is out of scope for these APIs. The data structures that the APIs do depend on are compatible with the data structures in the soon to be released ISO/IEC IS 18013-5 Personal identification --- ISO-compliant driving licence --- Part 5: Mobile driving licence (mDL) application standard.

**API Changes**

- Added Identity Credential Jetpack. ([Icf90b](https://android-review.googlesource.com/#/q/Icf90bf39c485c00acb4485c1b402c894cde3e317))

## Security-Crypto Version 1.1.0

### Version 1.1.0

July 30, 2025

`androidx.security:security-crypto:1.1.0` and `androidx.security:security-crypto-ktx:1.1.0` are released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e716aa82e6b27956a442460a66e512a8e7376ccd..12e7f8e66c5e70ca5c59342b4fb6c82e6e50a37c/security).

### Version 1.1.0-rc01

July 2, 2025

`androidx.security:security-crypto:1.1.0-rc01` and `androidx.security:security-crypto-ktx:1.1.0-rc01` are released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..e716aa82e6b27956a442460a66e512a8e7376ccd/security).

### Version 1.1.0-beta01

June 4, 2025

`androidx.security:security-crypto:1.1.0-beta01` and `androidx.security:security-crypto-ktx:1.1.0-beta01` are released. Version 1.1.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..786176dc2284c87a0e620477608e0aca9adeff15/security).

**API Changes**

- Deprecated all APIs in favour of existing platform APIs and direct use of Android Keystore.

### Version 1.1.0-alpha07

April 9, 2025

`androidx.security:security-crypto:1.1.0-alpha07` and `androidx.security:security-crypto-ktx:1.1.0-alpha07` are released. Version 1.1.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/617e5f259a688901040e1f508ecd2d6deb84e6b8..4c37298a97c16270c139eb812ddadaba03e23a52/security).

**API Changes**

- Deprecated all APIs in favour of existing platform APIs and direct use of Android Keystore.

### Version 1.1.0-alpha06

April 19, 2023

`androidx.security:security-crypto:1.1.0-alpha06` and `androidx.security:security-crypto-ktx:1.1.0-alpha06` are released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d5d49509dce56dc77715207ebb30b068e3e70eb5..617e5f259a688901040e1f508ecd2d6deb84e6b8/security)

**New Features**

- Updated Tink dependency to 1.8.0

### Version 1.1.0-alpha05

February 22, 2023

`androidx.security:security-crypto:1.1.0-alpha05` and `androidx.security:security-crypto-ktx:1.1.0-alpha05` are released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..d5d49509dce56dc77715207ebb30b068e3e70eb5/security)

**Bug Fixes**

- Fixed a race condition in `MasterKeys.getOrCreate` ([I3391e](https://android-review.googlesource.com/#/q/I3391e7ba62acfa942432eba402e74d64e2e5e98a), [b/268572037](https://issuetracker.google.com/issues/268572037))

### Version 1.1.0-alpha04

November 9, 2022

`androidx.security:security-crypto:1.1.0-alpha04` and `androidx.security:security-crypto-ktx:1.1.0-alpha04` are released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..a1e318590b217ecfce1b2de17eed2f18b6a680bb/security)

**New Features**

- Removed log message "keyset not found, will generate a new one" on first app launch. ([b/185219606](https://issuetracker.google.com/issues/185219606))
- Upgraded Tink dependency to version 1.7.0.

**API Changes**

- Changes `EncryptedFile#openFileInput()` to throw a `FileNotFoundException`, rather than a generic `IOException` when the requested file doesn't exist. ([I80e41](https://android-review.googlesource.com/#/q/I80e415bfd53e9e9f3b9a456d50b6b90c0a00c621), [b/148804719](https://issuetracker.google.com/issues/148804719))
- Updated 'MasterKeys' class to require Android M rather than each of its methods. ([I8b4b8](https://android-review.googlesource.com/#/q/I8b4b8354c197af50300ab37f7d1aeed8fdcd79df))
- Changes all preference getters on `EncryptedSharedPreferences` (ex `#getString`, `#getInt`) to throw `SecurityException` in rare circumstances where the type of a value can not be matched with one of the defined enum variants. ([b/241699427](https://issuetracker.google.com/issues/241699427))

**Bug Fixes**

- Synchronized security-crypto-ktx library's minimum SDK version with security-crypto by lowering it to v21 ([b/193550375](https://issuetracker.google.com/issues/193550375))
- Fixed concurrency bug when building multiple `EncryptedFile`s ([b/136590547](https://issuetracker.google.com/issues/136590547))

**External Contribution**

- Received a fix for `EncryptedSharedPreferences.Editor#remove` from chr.ibbotson@gmail.com ([b/224994760](https://issuetracker.google.com/issues/224994760), [b/134197835](https://issuetracker.google.com/issues/134197835), [f44d44d](https://android-review.googlesource.com/c/platform/frameworks/support/+/2163645))

### Security-Crypto-Ktx Version 1.1.0-alpha03

May 18, 2021

`androidx.security:security-crypto-ktx:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..66681ad83c328d0dd821b943bb3d375f02c1db61/security/security-crypto-ktx)

Updated to match `androidx.security:security-crypto:1.1.0-alpha03`.

### Version 1.1.0-alpha03

December 2, 2020

`androidx.security:security-crypto:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/security/crypto)

**New Features**

- Updated Tink to stable release `1.5.0`

### Version 1.1.0-alpha02

August 5, 2020

`androidx.security:security-crypto:1.1.0-alpha02` and `androidx.security:security-crypto-ktx:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d/security)

**New Features**

- Updated Tink to stable release `1.4.0`

**Bug Fixes**

- Tink update should fix R8 and Proguard issues with shaded Protobuf dependency.
- Tink update should gracefully handle AndroidKeyStore concurrency failures.

**External Contribution**

- clear `mKeysChanged` on apply, fix for EncryptedSharedPreferences ([aosp/1323026](https://android-review.googlesource.com/c/platform/frameworks/support/+/1323026))

### Version 1.1.0-alpha01

June 10, 2020

`androidx.security:security-crypto:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6be101c2241593fee3ef9ab4e1fb337b485f2f9a..945594abd75f83bd14daf4fbcd8621796161281e/security/crypto)

**New Features**

- Lollipop (API Level 21+) is now supported. Please note that the AndroidKeyStore is *not* used for API 21 and 22. ([I7c12d](https://android-review.googlesource.com/#/q/I7c12d205273e4b652271865e53ff6c406632f407), [b/132325342](https://issuetracker.google.com/issues/132325342))
- New MasterKey class provides more options for keys, also deprecating MasterKeys to support new features and versions of Android that do not have KeyGenParamSpec.

## Security-Crypto Version 1.0.0

### Version 1.0.0

April 21, 2021

`androidx.security:security-crypto:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15da9761b41f813f22ba89ee571c696ef912bb36..fcaf14f73f7f72fb68aff12bc186eb593df0ebc1/security/crypto)

**Major features of 1.0.0**

**Feature highlights**

- `EncryptedFile`, provides encrypted input and output streams to read/write encrypted data to a File.
- `EncryptedSharedPreferences`, provides an implementation of SharedPreferences that automatically encrypts/decrypts all keys and values.
- Provides simple key generation via MasterKeys.
- Relies on Tink 1.5.0 for increased stability.

### Version 1.0.0-rc04

January 13, 2021

`androidx.security:security-crypto:1.0.0-rc04` is released. [Version 1.0.0-rc04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73e50dca45f0c39a00dd117a5ed276c7c659a8aa..15da9761b41f813f22ba89ee571c696ef912bb36/security/crypto)

**Bug Fixes**

- Upgraded Tink to 1.5.0 for increased stability.

### Version 1.0.0-rc03

August 5, 2020

`androidx.security:security-crypto:1.0.0-rc03` is released. [Version 1.0.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6be101c2241593fee3ef9ab4e1fb337b485f2f9a..73e50dca45f0c39a00dd117a5ed276c7c659a8aa/security/crypto)

**New Features**

- Updated Tink to stable release `1.4.0`

**Bug Fixes**

- Tink update should fix R8 and Proguard issues with shaded Protobuf dependency.
- Tink update should gracefully handle AndroidKeyStore concurrency failures.

**External Contribution**

- clear `mKeysChanged` on apply, fix for EncryptedSharedPreferences ([aosp/1323026](https://android-review.googlesource.com/c/platform/frameworks/support/+/1323026))

### Version 1.0.0-rc02

May 20, 2020

`androidx.security:security-crypto:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f66cdf1658639bd74ae850dfe3c1f5bb72eaebe6..6be101c2241593fee3ef9ab4e1fb337b485f2f9a/security/crypto)

**Bug Fixes**

- Updated to Tink version 1.4.0-rc2, which shades the proto buf lite dep. This solves the widely reported issue of clashing with other android sdks. ([I8a831](https://android-review.googlesource.com/#/q/I8a831b2068b8eec5642244c164882ddc312b496a))
- Fixed `apply()` in `EncryptedSharedPreferences`. ([I29069](https://android-review.googlesource.com/#/q/I2906984118a5cf4e200b5a011b9addd16de710b7), [b/154366606](https://issuetracker.google.com/issues/154366606))

### Version 1.0.0-rc01

April 15, 2020

`androidx.security:security-crypto:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8744680798c115f612a99148c5a5c3ad4bd6fbf5..f66cdf1658639bd74ae850dfe3c1f5bb72eaebe6/security/crypto)

**Bug Fixes**

- Added checks to ensure that if a `KeyGenParamSpec` is passed in to `MasterKeys.getOrCreate` that if `getUserAuthenticationRequired` returns `true` that `getUserAuthenticationValidityDurationSeconds` returns a value \>0. ([I911f5](https://android-review.googlesource.com/#/q/I911f5742c926977c80784d353d0ede65e4c07d41)) ([b/152644939](https://issuetracker.google.com/issues/152644939))

### Version 1.0.0-beta01

March 18, 2020

`androidx.security:security-crypto:1.0.0-beta01` is released with no changes since `1.0.0-alpha02`. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/a1aa570607371188c68469577de50a2505d27eb7..8744680798c115f612a99148c5a5c3ad4bd6fbf5/security/crypto).

### Version 1.0.0-alpha02

May 23, 2019

`androidx.security:security-crypto:1.0.0-alpha02` is released.
The commits included in this version can be found in this [commit log](https://android.googlesource.com/platform/frameworks/support/+log/82480af90391b75a2acf8cf522f23f4d9ced132a..a1aa570607371188c68469577de50a2505d27eb7/security).

**Bug fixes**

- Fixed issue retrieving key/values associated with shared preferences from [`getAll()`](https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences#getAll()).
- Blocked usage of restricted preference keys.
- Minor Javadoc updates.

### Version 1.0.0-alpha01

May 7, 2019

`androidx.security:security-crypto:1.0.0-alpha01` is released. The commits
included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/1e1b37f61bf5bb57b57dde40f19be03630d73c30/security).

**New feature highlights**

- `EncryptedFile`, provides encrypted input and output streams to read/write encrypted data to a File.
- `EncryptedSharedPreferences`, provides an implementation of `SharedPreferences` that automatically encrypts/decrypts all keys and values.
- Provides simple key generation via MasterKeys.