---
title: https://developer.android.com/tools/bmgr
url: https://developer.android.com/tools/bmgr
source: md.txt
---

# bmgr

`bmgr`is a shell tool you can use to interact with the Backup Manager on Android devices version 2.2 (API Level 8) or higher. The tool provides commands to initiate backup and restore operations so that you don't need to repeatedly wipe data or take similar intrusive steps in order to test your application's backup functionality. The`bmgr`tool supports both[Auto Backup](https://developer.android.com/guide/topics/data/autobackup)and[Key/Value Backup](https://developer.android.com/guide/topics/data/keyvaluebackup).

Note:`bmgr restore`does not work for[encrypted backups](https://developer.android.com/guide/topics/data/autobackup#define-device-conditions).

You run`bmgr`commands on a device via[adb shell](https://developer.android.com/studio/command-line/adb)and then monitor the output of the commands with[logcat](https://developer.android.com/studio/command-line/logcat). For a list and description of available commands, run the`bmgr`tool with no arguments. For information on triggering backup and restore operations, see[Testing Backup and Restore](https://developer.android.com/guide/topics/data/testingbackup).

For information about adding support for backup in your application, read[Data Backup](https://developer.android.com/guide/topics/data/backup)