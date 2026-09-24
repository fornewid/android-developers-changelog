---
title: https://developer.android.com/jetpack/androidx/releases/test-backup
url: https://developer.android.com/jetpack/androidx/releases/test-backup
source: md.txt
---

# Automated Backup Restore Test

Automated testing framework to verify that user data and account credentials safely survive device upgrades and cloud restores.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| September 23, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/test_backup#1.0.0-alpha01) |

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