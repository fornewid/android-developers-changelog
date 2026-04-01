---
title: https://developer.android.com/identity/data/testingbackup
url: https://developer.android.com/identity/data/testingbackup
source: md.txt
---

# Test backup and restore

This page shows you how to test the cloud backups and the device-to-device (D2D) transfer process for your app. It is important to test both of these with each major release of your app to help ensure that your users can continue to use your app on a new device. While both backup and transfer are similar, there are important differences between the two in Android 12 (API level 31) and higher--- most notably that transfer has a much larger data size limit of 2 GB, compared with 2 MB for cloud backup.

This guide shows you how you can test both cloud backup and restore and D2D transfer efficiently throughout the development cycle.

## How testing backups works

This section describes various pieces in the Android backup framework and how they interact with apps that support Auto Backup and key-value backup. During the app development phase, most of the inner working of the framework are abstracted away, so you don't need to know this information. However, during the testing phase, an understanding of these concepts becomes more important.

The following diagram illustrates how the data flows during a cloud backup and restore:
![Diagram showing data flowing from an app to the Backup Manager Service, then to a backup transport, and finally to cloud storage.](https://developer.android.com/static/identity/data/images/remote_backup.png)**Figure 1:**Cloud backup and restore data flow.

The following diagram illustrates how the data flows during a D2D transfer:
![Diagram showing data flowing from a source device app to the Backup Manager Service on the source device, then directly to the Backup Manager Service on a new device, and finally to the app on the new device.](https://developer.android.com/static/identity/data/images/device_to_device_transfer.png)**Figure 2:**Device-to-device transfer data flow.

Unlike cloud backup and restore testing, D2D testing requires a source device and a target device to copy from and to.

The*Backup Manager Service* is an Android system service that orchestrates and initiates backup and restore operations. The service is accessible through the[`Backup Manager`](https://developer.android.com/reference/android/app/backup/BackupManager)API.

During a backup operation, the service queries your app for backup data and hands it to the*backup transport*, which archives the data to the cloud. During a restore operation, the Backup Manager Service retrieves the backup data from the backup transport and restores the data to the device. For a D2D transfer, the Backup Manager Service queries your app for backup data and passes it directly to the Backup Manager Service on the new device, which loads it into your app.

*Backup Transports*are Android components responsible for storing and retrieving your app data. An Android-powered device can have zero or more backup transports, but only one can be active at a time. Available backup transports differ from device to device due to customizations by device manufacturers and service providers. Most Google Play-enabled devices ship with the following transports:

- **GMS Transport:** The active cloud backup transport on most devices, part of[Google Mobile Services](https://www.android.com/gms/). This transport stores data in the Android Backup Service.
- **D2D Transport:**This transport is used in D2D migration to transfer data directly from one device to another.

## Tools

To test your backup and restore operations, you need to know a bit about the following tools:

- [`adb`](https://developer.android.com/studio/command-line/adb): To run commands on the device or emulator.
- [`bmgr`](https://developer.android.com/studio/command-line/bmgr): To perform various backup and restore operations.
- [`logcat`](https://developer.android.com/studio/command-line/logcat): To see the output of backup and restore operations.

## Test cloud backup

Cloud backup and restore can be performed using a single device by following the steps in this section.

### Prepare your device or emulator for cloud backups

Prepare your device or emulator for backup testing by working through the following checklist:

1. For Auto Backup, check that you are using a device or emulator running Android 6.0 (API level 23) or higher.
2. For key-value backup, check that you are using a device or emulator running Android 2.2 (API level 8) or higher.
3. You must have internet access to test cloud backup.
4. Sign in to the device with a**Google Account** and set it as the backup account in**Settings \> Google \> Backup**.

To test cloud backup, trigger a cloud backup, then uninstall and reinstall the app. To make these steps repeatable, you can use the following script,`test_cloud_backup.sh`, which backs up your app, downloads the APK locally, uninstalls it, and reinstalls the APK:  

    #!/bin/bash -eu
    : "${1?"Usage: $0 package name"}"

    # Initialize and create a backup
    adb shell bmgr enable true
    adb shell bmgr transport com.android.localtransport/.LocalTransport | grep -q "Selected transport" || (echo "Error: error selecting local transport"; exit 1)
    adb shell settings put secure backup_local_transport_parameters 'is_encrypted=true'
    adb shell bmgr backupnow "$1" | grep -F "Package $1 with result: Success" || (echo "Backup failed"; exit 1)

    # Uninstall and reinstall the app to clear the data and trigger a restore
    apk_path_list=$(adb shell pm path "$1")
    OIFS=$IFS
    IFS=$'\n'
    apk_number=0
    for apk_line in $apk_path_list
    do
        (( ++apk_number ))
        apk_path=${apk_line:8:1000}
        adb pull "$apk_path" "myapk${apk_number}.apk"
    done
    IFS=$OIFS
    adb shell pm uninstall --user 0 "$1"
    apks=$(seq -f 'myapk%.f.apk' 1 $apk_number)
    adb install-multiple -t --user 0 $apks

    # Clean up
    adb shell bmgr transport com.google.android.gms/.backup.BackupTransportService
    rm $apks

    echo "Done"

### Test steps

1. Open your app, sign in, and modify all settings.
2. Run the script, passing in your package name, such as`test_cloud_backup.sh com.example.myapp`.
3. Re-open the app and validate that it works correctly, with all data retained.

You don't want your users to need to sign in, and all their settings, progress, and app data must be as they were before. If your test results don't meet these criteria, make sure you have configured backups correctly, without omitting key pieces of data, and that you are also handling the recreation of any cached data that you excluded from the backup. Repeat steps 1-3 for each test iteration.

## Test D2D transfer

The most comprehensive way to test D2D transfer is by transferring your entire phone contents to a new, factory-reset device and validating that it works correctly. However, this can be inconvenient and time-consuming if you need to repeat the process multiple times. These steps show you how to simulate a transfer with a single device without repeatedly performing a factory reset on the device.

### Prepare your device for D2D testing

To test D2D transfer on a single device, prepare it as follows:

1. Your device must be running Android 12 (API level 31) or higher.
2. To test the latest version of D2D, target Android 12 (API level 31) or higher in your app.
3. Create the following script,`test_d2d.sh`, to support repetition of the test:

    #!/bin/bash -eu
    : "${1?"Usage: $0 package name"}"

    # Initialize and create a backup
    adb shell bmgr enable true
    adb shell settings put secure backup_enable_d2d_test_mode 1
    adb shell bmgr transport com.google.android.gms/.backup.migrate.service.D2dTransport
    adb shell bmgr init com.google.android.gms/.backup.migrate.service.D2dTransport
    adb shell bmgr list transports | grep -q -F "  * com.google.android.gms/.backup.migrate.service.D2dTransport" || (echo "Failed to select and initialize backup transport"; exit 1)
    adb shell bmgr backupnow "$1" | grep -F "Package $1 with result: Success" || (echo "Backup failed"; exit 1)

    # Uninstall and reinstall the app to clear the data and trigger a restore
    apk_path_list=$(adb shell pm path "$1")
    OIFS=$IFS
    IFS=$'\n'
    apk_number=0
    for apk_line in $apk_path_list
    do
        (( ++apk_number ))
        apk_path=${apk_line:8:1000}
        adb pull "$apk_path" "myapk${apk_number}.apk"
    done
    IFS=$OIFS
    adb shell pm uninstall --user 0 "$1"
    adb shell bmgr transport com.google.android.gms/.backup.BackupTransportService
    apks=$(seq -f 'myapk%.f.apk' 1 $apk_number)
    adb install-multiple -t --user 0 $apks

    # Clean up
    adb shell bmgr init com.google.android.gms/.backup.migrate.service.D2dTransport
    adb shell settings put secure backup_enable_d2d_test_mode 0
    adb shell bmgr transport com.google.android.gms/.backup.BackupTransportService
    rm $apks

    echo "Done"

### Test steps

1. Install the app you want to test on the device.
2. Open your app, sign in, and modify your app's settings.
3. Run the script on your device, passing in your package name, such as`test_d2d.sh com.example.myapp`.
4. When the script is complete, open the app on the device and validate that it works correctly, with all data retained.

You don't want your users to need to sign in, and all their settings, progress, and app data must appear as they did prior to running the script. If your test results don't meet these criteria, make sure you have configured transfer correctly, without omitting key pieces of data, and that you are also handling the recreation of any cached data that you excluded from the transfer. Repeat steps 2-4 for each test iteration.

## Troubleshoot backup and restore

This section helps you troubleshoot some common issues.

**Transport quota exceeded**

The following messages in Logcat indicate that your app has exceeded the transport quota:  

    I/PFTBT: Transport rejected backup of <PACKAGE>, skipping

    --- or ---

    I/PFTBT: Transport quota exceeded for package: <PACKAGE>

Reduce the amount of backup data and try again. For example, verify that you are caching data only in the cache directory of your app. The cache directory isn't included in backups.

**Full backup not possible**

The following message in Logcat indicates that the full backup operation failed because no key-value backup operation has yet occurred on the device:  

    I/BackupManagerService: Full backup not currently possible -- key/value backup
    not yet run?

Trigger a key-value backup with the command`bmgr run`, and then try again.

**Timeout waiting for agent**

The following message in Logcat indicates that your app is taking more than 10 seconds to launch for backup:  

    12-05 18:59:02.033  1910  2251 D BackupManagerService:
        awaiting agent for ApplicationInfo{5c7cde0 com.your.app.package}
    12-05 18:59:12.117  1910  2251 W BackupManagerService:
        Timeout waiting for agent ApplicationInfo{5c7cde0 com.your.app.package}
    12-05 18:59:12.117  1910  2251 W BackupManagerService:
        Can't find backup agent for com.your.app.package

Notice the timestamp difference in the log output. This error typically occurs when your app makes use of a multidex configuration without ProGuard.

**Uninitialized backup account**

The following messages in Logcat indicate that the backup was halted because the backup dataset was not initialized:  

    01-31 14:32:45.698 17280 17292 I Backup: [GmsBackupTransport] Try to backup for
    an uninitialized backup account.
    01-31 14:32:45.699  1043 18255 W PFTBT: Transport failed; aborting backup: -1001
    01-31 14:32:45.699  1043 18255 I PFTBT: Full backup completed with status: -1000

Run the backup manager with the command`adb shell bmgr run`, and then try to perform the backup again.

**App methods not called**

Because Auto Backup launches your app with a base class of[`Application`](https://developer.android.com/reference/android/app/Application), your app's setup methods might not be called. Auto Backup doesn't launch any of your app's activities, either, so you might see errors if your app does setup in an activity. To learn more, read[Implement BackupAgent](https://developer.android.com/guide/topics/data/autobackup#ImplementingBackupAgent).

In contrast, key-value backup launches your app with any`Application`subclass you declare in your app manifest file.

**No data to back up**

The following messages in Logcat indicate that your app has no data to back up:  

    I Backup  : [FullBackupSession] Package com.your.app.package doesn't have any backup data.

    --- or ---

    I Backup  : [D2dTransport] Package com.your.app.package doesn't have any backup data.

If you[implemented your own BackupAgent](https://developer.android.com/guide/topics/data/autobackup#ImplementingBackupAgent), this likely means you have not added any data or files to the backup.