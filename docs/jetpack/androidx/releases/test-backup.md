---
title: https://developer.android.com/jetpack/androidx/releases/test-backup
url: https://developer.android.com/jetpack/androidx/releases/test-backup
source: md.txt
---

# Test Backup

Automated testing framework to verify that user data and account credentials safely survive device upgrades and cloud restores.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 21, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/test-backup#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on test backup, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.test.backup:backup:1.0.0-alpha03"
    implementation "androidx.test.backup:backup-host:1.0.0-alpha03"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.test.backup:backup:1.0.0-alpha03")
    implementation("androidx.test.backup:backup-host:1.0.0-alpha03")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2258505+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2258505&template=2395410)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Automated Backup Restore Test Version 1.0

### Version 1.0.0-alpha03

October 21, 2026

`androidx.test.backup:backup:1.0.0-alpha03` and `androidx.test.backup:backup-host:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/988ac9734e8223273eb7f186ee1639ee68deb025..b4c15a8e351e6cfa93e90cce2cfbd0dbbe4805a7/test/backup).

**New Features**

- Simplified test setup in Android Gradle Plugin backup test suites by automatically targeting the tested app when `@BackupRestoreConfig` is omitted. ([I1452b](https://android-review.googlesource.com/#/q/I1452bba1b2e53201759bede479f36b565c72ac72))
- Added support for inheriting `@BackupRestoreConfig` and `@Isolation` settings from an outer test class in `@Nested` test classes. ([Ia45a8](https://android-review.googlesource.com/#/q/Ia45a8d0a216d27f4ebd1030f2f75c72e2466e9f8))
- Added support for injecting `BackupRestoreController` directly into test class constructors and `@BeforeAll` setup methods. ([I6e822](https://android-review.googlesource.com/#/q/I6e8226eb8e2ff548e0e227abcf39c3ffd82cb400), [Ia2ebd](https://android-review.googlesource.com/#/q/Ia2ebd2a66c49b105e0e4dcb3a47a5856d654e216))
- Added support for pinning a specific device to a `@Device` role in multi-device tests using the `androidx.test.backup.device.serial.{role}` property. ([I484be](https://android-review.googlesource.com/#/q/I484be83239feb2511051d0cd83f58fcd405c1d05))

**Bug Fixes**

- Fixed `performBackup` and `performRestore` so tests fail immediately instead of passing silently when a backup is skipped or empty, when the backup service errors out, or when a local backup archive belongs to a different app or device. ([I7673d](https://android-review.googlesource.com/#/q/I7673ddf7d8a255184ebc9162dcc77129a44fffdb), [I478ad](https://android-review.googlesource.com/#/q/I478ad5b3f45cfae35d59e3a652a9535e3a51d26b), [I0b989](https://android-review.googlesource.com/#/q/I0b989f9af98f585c3fccdaeb4fde795aa1bf1f73), [I9a0ea](https://android-review.googlesource.com/#/q/I9a0ea44887908ffaf596a0652fb38cf2499837f7), [I79567](https://android-review.googlesource.com/#/q/I7956782d099ffcff4ffae3133299a19ad2214c8f))
- Fixed tests hanging indefinitely on unresponsive devices by enforcing timeouts across backup, restore, device actions, and cleanup steps. ([I10661](https://android-review.googlesource.com/#/q/I1066158011a9c52086d40e4769ad2f3602ce38ff), [I9cdee](https://android-review.googlesource.com/#/q/I9cdeee7855f2eaf50bdab809a0fb9d9720c30bf2), [If5f92](https://android-review.googlesource.com/#/q/If5f92025f93827ac7890d08f9bbac4486ba43125))
- Fixed `performBackup` deleting generated backup files when the test run finished, so backup archives are now kept on disk after tests exit. ([I8c13f](https://android-review.googlesource.com/#/q/I8c13f9973086b7ff45cb52e2e8f759dcf3a766b5))
- Fixed database test helpers (`StorageDomain.Database`) to properly store and check `null` values, overwrite existing rows when seeding test data, catch invalid table configurations early, and fail when an expected database file is missing. ([Ib4767](https://android-review.googlesource.com/#/q/Ib47677fff9977a08e54a2f143de58fc0841e5987), [Iddf87](https://android-review.googlesource.com/#/q/Iddf87bf275e934bf00781b482b5759f75daba9e3), [I19c43](https://android-review.googlesource.com/#/q/I19c4353550902839c053398e2aba3ace1fdc160b), [Ie8d78](https://android-review.googlesource.com/#/q/Ie8d78a64ba6c660e63072af7b9d08f6d8ff94ade), [I8bc18](https://android-review.googlesource.com/#/q/I8bc1866b00b4c6b8ec87aa7f21010d8084db7e3b))
- Fixed `SharedPreferences` test helpers to preserve data types accurately and support checking for `null` or removed preferences. ([I8456d9](https://android-review.googlesource.com/#/q/I8456d9a242cc804897edce9b959c642d3c0514bd), [I1d0fc2](https://android-review.googlesource.com/#/q/I1d0fc22ee6640d6827847c270b365c9d0a00a3c7))
- Fixed `runOnDevice` to handle large test payloads without crashing, pause for the debugger when `waitForDebugger` is enabled, find the test runner in custom test APK package names, and block internal runner flags from leaking into device actions. ([Ic73bd](https://android-review.googlesource.com/#/q/Ic73bdc7275d9b8e61a8e821e1a996cfe258e2874), [Iede17](https://android-review.googlesource.com/#/q/Iede174c930233de86fe463b57abf3e0c20ef5372), [I1d172](https://android-review.googlesource.com/#/q/I1d172015314fadac542bfe9b25bc567f1314bad6), [I84c15](https://android-review.googlesource.com/#/q/I84c15c3232235168631332b5781b6dd99a6931c2))
- Improved test stability and speed by sharing a single ADB connection across the test run, installing APKs only once per device, and failing clearly when an APK fails to install or launch. ([I62717](https://android-review.googlesource.com/#/q/I62717c5b6f8f22d864d4eeb58539931d7340c197), [Iabf75](https://android-review.googlesource.com/#/q/Iabf75f0751aa6164936d87080ef37af417fe1062), [I14e6f](https://android-review.googlesource.com/#/q/I14e6fda3a4325cf38a60db39a41bf040226bc518), [I4c3da5](https://android-review.googlesource.com/#/q/I4c3da50913a726c754deed726ad0f87c01f965ae), [I54077](https://android-review.googlesource.com/#/q/I540777aa6d63f76501993c1f290ed2014e81ff85), [Iee84e](https://android-review.googlesource.com/#/q/Iee84e35c6d504f902f73bf1b0a262f109449ffd1))
- Fixed `fetchDeviceLogs` writing empty log files, and stopped cancelled test runs from generating false failure reports. ([I736c4](https://android-review.googlesource.com/#/q/I736c40fb4a858b8536cee9c8b7dbd11bb3692939), [I7b199](https://android-review.googlesource.com/#/q/I7b1990f00eeb871e7d34fb33730faf67e7dc0f11), [Ia847e](https://android-review.googlesource.com/#/q/Ia847e2fc30ee78174c7d258599ef6b32e2c3a914))
- Cleaned up `backup-host` dependencies so `adblib` is available directly to callers and internal logging or test libraries no longer clash with your project's classpath. ([I6e822](https://android-review.googlesource.com/#/q/I6e8226eb8e2ff548e0e227abcf39c3ffd82cb400), [Iba9a4](https://android-review.googlesource.com/#/q/Iba9a4b46c39bf491d2bb7f4dadc9a83427730791), [Ib4ec9](https://android-review.googlesource.com/#/q/Ib4ec9530e581ba390b61dfabe16cc46e6e6b0cca))

#### Version 1.0.0-alpha02

October 07, 2026

`androidx.test.backup:backup:1.0.0-alpha02` and `androidx.test.backup:backup-host:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2b5ae7b0fe1bb4eece7018878fe5f18c5967a2f..83c1be95c76b4ae3480add6acbbe7e318857f969/test/backup).

**API Changes**

- Payload keys are now documented as `BackupActionInputKeys`, `BackupActionOutputKeys`, and `BackupActionValues`, replacing the constants on `BackupDeviceAction`. Added `BackupDeviceActionResult.success()` and `failure()` factories, along with `isSuccess` and `errorMessage` accessors. ([Ibd493](https://android-review.googlesource.com/#/q/Ibd4939a7e2f5b8b9959fb4e885b3ab8788ff58ab))

**Bug Fixes**

- `BackupRestoreController.clearAppData` now throws `IOException` when `pm clear` does not report success, instead of continuing silently. ([I61556](https://android-review.googlesource.com/#/q/I615561663d7e1d834c812fc5c39a16ba5f4895b0))
- Shell arguments passed to `BackupRestoreController` for device execution are now correctly escaped to prevent command injection and ensure file paths with spaces are handled securely.
- Hardened the bundled storage actions (`PopulateStorageAction` and `AssertStorageAction`) against silent verification passes to ensure tests strictly fail when expected data is missing.
- Host-side test orchestrators now correctly honor in-band action failures reported by the device instead of ignoring them.
- Fixed an issue with database row population by percent-encoding the database `'values'` wire format, preventing data corruption during payload transport.
- Addressed security vulnerabilities in `androidx.test.backup:backup-host` by upgrading dependencies.

### Version 1.0.0-alpha01

September 23, 2026

`androidx.test.backup:backup:1.0.0-alpha01` and `androidx.test.backup:backup-host:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e42fbca3c858f229d1319744151dff704521b19/test/backup).

**Features of Initial Release**

Initial release of the Automated Backup and Restore Testing framework for Android. This library provides an automated, end-to-end way to test that user data and account credentials safely survive device upgrades and cloud restores. Instead of relying on manual testing, developers can automate the full lifecycle: seeding app state, backing it up according to your configured rules (`dataExtractionRules` and `fullBackupContent`), wiping the app, and verifying post-restore data integrity. The framework provides two artifacts: `androidx.test.backup:backup-host` (which runs on the host computer to orchestrate backup, wipe, and restore passes over ADB) and `androidx.test.backup:backup` (which runs on the device to populate and verify app data).

- `BackupRestoreController`: The primary host-side interface used to control backup, wipe, restore, and verification workflows for a test device. Provides convenience pipelines such as `runBackupRestoreFlow` as well as fine-grained operations (`performBackup`, `performRestore`, `clearAppData`, `fetchDeviceLogs`, and `runOnDevice`). Supports both Kotlin coroutines and Java `ListenableFuture` asynchronous execution.
- `BackupRestoreExtension`: A JUnit 5 Jupiter extension that resolves and injects `BackupRestoreController` parameters into test methods. Manages standalone or shared ADB sessions, automatically installs tested and test APKs, dismisses device lockscreens and keyguards to unlock credential-protected storage, and enforces test sandbox isolation.
- `BackupRestoreTestRunner`: An on-device `Instrumentation` test runner executing inside the application sandbox. Dynamically resolves and executes requested `BackupDeviceAction` implementations dispatched by host orchestrators and safely redirects large JSON result payloads to disk to prevent Binder transaction buffer limits.
- `BackupDeviceAction`: The contract for custom device-side actions executing directly within the target application sandbox during data seeding (`PHASE_POPULATE`) or post-restore validation (`PHASE_VERIFY`).
- `StorageDomain`: Strongly typed descriptors (`Preference`, `Database`, `TextFile`, and `BinaryFile`) used alongside prebuilt action helpers (`PopulateStorageAction` and `AssertStorageAction`) to automatically seed and assert `SharedPreferences`, SQLite databases, and raw files across both Credential Protected (CE) and Device Protected (DE) storage contexts without boilerplate.
- `BackupTransportMode`: Specifies the platform backup transport topology to simulate during test passes, including `DEVICE_TO_DEVICE` (physical device migration via USB or Wi-Fi Direct), `CLOUD_ENCRYPTED` (cloud backup with client-side end-to-end encryption), `CLOUD_UNENCRYPTED` (standard cloud backup), and `LOCAL` (offline local filesystem backup).
- `@Device` and `@Isolation`: Host annotations for selecting connected devices matching specific serials, API levels, or multi-device roles, and configuring sandbox isolation policies between test runs (`IsolationPolicy.AUTOMATIC` vs. `IsolationPolicy.MANUAL`).