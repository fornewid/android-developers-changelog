---
title: https://developer.android.com/studio/preview/backup-restore-testing-release-notes
url: https://developer.android.com/studio/preview/backup-restore-testing-release-notes
source: md.txt
---

> [!WARNING]
> **Experimental:** Automated backup and restore testing is in active development, and its features and APIs might change between alpha releases. Report feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=2258505&template=2395410).

For the complete list of changes in each library version, see the
[`androidx.test.backup` release notes](https://developer.android.com/jetpack/androidx/releases/test-backup).

### 1.0.0-alpha04

November 4, 2026

- Added `StorageDomain` types for `runBackupRestoreFlow`: `DataStorePreference` for Preferences DataStore, `CustomData` for [custom device actions](https://developer.android.com/studio/preview/backup-restore-testing#custom-actions), and `ExcludedData` to check that excluded data isn't restored. For more information, see [Built-in storage types](https://developer.android.com/studio/preview/backup-restore-testing#storage-types).
- Added `isDeviceProtectedStorage` to built-in `StorageDomain` types to test device-protected storage. Added `Set<String>` value support to `StorageDomain.Preference`.
- Added `restoreOn` to `runBackupRestoreFlow` for [transfers between devices](https://developer.android.com/studio/preview/backup-restore-testing#device-to-device), `uninstallApp` to `BackupRestoreController`, and `minApi` and `maxApi` bounds to `@Device`. For more information, see [Choose devices](https://developer.android.com/studio/preview/backup-restore-testing#choose-devices).
- Added `BackupActionResult.data` and `BackupActionResult.getOrThrow` to read data returned by device actions and fail when an action fails.
- Updated `BackupRestoreExtension` to save logcat from each device when a test fails and list the file paths in the failure output. To turn off log saving, pass `-Dandroidx.test.backup.device.logs.enabled=false`. For more information, see [Inspect test reports](https://developer.android.com/studio/preview/backup-restore-testing#test-reports).
- Registered `BackupRestoreTestRunner` with `InstrumentationRegistry` so device actions can call `getInstrumentation`. Added an optional `testApplicationId` value to `@BackupRestoreConfig` and made `applicationId` optional.
- Removed `BackupDeviceAction.phase`, `PHASE_POPULATE`, `PHASE_VERIFY`, and the `BackupRestoreExtension(AdbSession)` constructor. Remove `override val phase` from custom device actions.

To use this version, set `backupTestLibraryVersion` to `"1.0.0-alpha04"` in your
test suite.

### 1.0.0-alpha03

October 21, 2026

- Tests in a backup test suite run against the app variant that the suite targets, so they no longer need `@BackupRestoreConfig`.
- You can bind a `@Device` role to a device with the `androidx.test.backup.device.serial.{role}` system property. For more information, see [Choose devices](https://developer.android.com/studio/preview/backup-restore-testing#choose-devices).
- When Google Play services skips your app or needs an update to restore it, the restore fails with an error message that says why. For more information, see [Troubleshoot failed restores](https://developer.android.com/studio/preview/backup-restore-testing#troubleshoot-restores).
- Bug fixes and reliability improvements.

To use this version, set `backupTestLibraryVersion` to `"1.0.0-alpha03"` in
your test suite.

### 1.0.0-alpha02

October 7, 2026

Bug fixes and improved integration with AGP test suites.

### 1.0.0-alpha01

September 23, 2026

Initial release for the [automated backup and restore testing](https://developer.android.com/studio/preview/backup-restore-testing) libraries,
`androidx.test.backup:backup` and `androidx.test.backup:backup-host`.