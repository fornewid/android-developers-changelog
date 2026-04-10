---
title: https://developer.android.com/training/wearables/data/cloud-backup-restore
url: https://developer.android.com/training/wearables/data/cloud-backup-restore
source: md.txt
---

Data backup on Wear OS 4 is similar to [data backup](https://developer.android.com/guide/topics/data/backup) for mobile apps, and it
follows [similar rules for automatically backing up user data](https://developer.android.com/training/wearables/data/cloud-backup-restore#automatic-backup). This document
explains how you can add support for backup and restore in your Wear OS app.

On devices that support backup and run Wear OS 4 or higher, users can back up
their data to the cloud in order to transfer data off that device, and they can
restore data from the cloud to transfer data onto a new Wear OS device. For
example, users can [perform backup and restore on Google Pixel Watch](https://support.google.com/googlepixelwatch/answer/13579590#zippy=%2Cpair-your-phone-with-a-new-pixel-watch).
| **Note:** Cloud backup and restore, where the user restores data to a new Wear OS device, is different from [transferring Wear OS data to a new mobile device](https://developer.android.com/training/wearables/data/transfer-to-new-mobile), where the user connects their existing Wear OS device to a new mobile device.

## Simulate cloud transfer using local storage

To test the backup and restore flow using simulated cloud storage, complete
these steps:

1. In your app, [enable backup](https://developer.android.com/guide/topics/data/autobackup#EnablingAutoBackup) and follow the steps outlined
   at [Control backup on Android 12 or higher](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-12). For Wear OS, you don't need to
   specify the [additional set of backup rules](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-11) to support devices that target
   API level 29 or lower.

   | **Note:** If you implement a custom [`BackupAgent`](https://developer.android.com/guide/topics/data/autobackup#ImplementingBackupAgent), you should avoid calling the [Data Layer](https://developer.android.com/training/wearables/data/data-layer) inside your backup agent's methods because it may not work correctly if called there.
2. Connect your device that's running Wear OS 4 or higher to your development
   machine using a [Wi-Fi connection](https://developer.android.com/training/wearables/get-started/debugging#wifi-debugging).

3. Follow the steps in the guide to [test cloud backup and restore](https://developer.android.com/guide/topics/data/testingbackup#TestingBackup).

## Automatic backup rules

On Wear OS, the conditions required to [back up data automatically](https://developer.android.com/guide/topics/data/autobackup) differ
slightly from those on mobile devices. In order for a Wear OS device to
automatically back up data, each of the following conditions must be true:

- The device is charging.
- The device is connected to a Wi-Fi network. This is required even if the device is LTE-enabled.
- The device is signed into a Google Account.
- At least 24 hours have elapsed since the last backup.

Unlike other devices, wearables running Wear OS aren't required to be idle
before backups occur automatically.

In addition, the system automatically backs up any [tiles](https://developer.android.com/training/wearables/tiles),
[complications](https://developer.android.com/training/wearables/tiles/complications), and [watch faces](https://developer.android.com/training/wearables/watch-faces) associated with your Wear OS app.

## Backup storage and size limit

Similar to mobile backup and restore, backup data is [stored in a private
folder](https://developer.android.com/guide/topics/data/autobackup#BackupLocation) in the user's Google Drive account, limited to 25 MB per app.
If you have both a mobile app and a Wear OS app, the backups are stored
separately, and the two apps don't contribute to each other's size limit.

Any data in the `DataStore` -- **Files \> DataStore** -- is backed up by default
unless you explicitly exclude the corresponding files and directories.
| **Caution:** Partial backups aren't supported. If the total size of the files and directories within a Wear OS backup is greater than 25 MB, then no data from the Wear OS app is backed up.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Save simple data with SharedPreferences](https://developer.android.com/training/data-storage/shared-preferences)
- [DataStore (Kotlin Multiplatform)](https://developer.android.com/kotlin/multiplatform/datastore)
- [Working with Proto DataStore](https://developer.android.com/codelabs/android-proto-datastore)