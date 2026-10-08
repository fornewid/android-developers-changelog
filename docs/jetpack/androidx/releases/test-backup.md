---
title: https://developer.android.com/jetpack/androidx/releases/test-backup
url: https://developer.android.com/jetpack/androidx/releases/test-backup
source: md.txt
---

# Test Backup

Automated testing framework to verify that user data and account credentials safely survive device upgrades and cloud restores.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 07, 2026 | - | - | - | [1.0.0-alpha02](https://developer.android.com/jetpack/androidx/releases/test_backup#1.0.0-alpha02) |

## Declaring dependencies

To add a dependency on test backup, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.test.backup:backup:1.0.0-alpha02"
    implementation "androidx.test.backup:backup-host:1.0.0-alpha02"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.test.backup:backup:1.0.0-alpha02")
    implementation("androidx.test.backup:backup-host:1.0.0-alpha02")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component&template)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Backup

### Version 1.0

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

## Automated Backup Restore Test Version 1.0

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