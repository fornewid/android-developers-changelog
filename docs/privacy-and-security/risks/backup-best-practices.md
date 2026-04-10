---
title: https://developer.android.com/privacy-and-security/risks/backup-best-practices
url: https://developer.android.com/privacy-and-security/risks/backup-best-practices
source: md.txt
---

# Security recommendations for backups

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

App backups aim to preserve users' data so that it can later be restored to a new device or in case of data loss. Existing security recommendations regarding app backups are nuanced, varying between Android versions and device manufacturers. The common theme is that these recommendations aim at ensuring that no sensitive data is leaked.

The Standard Android Backup system provides the most secure, robust, and easiest solution for apps to back up their data to the cloud or to transfer data to a new device through[Auto Backup](https://developer.android.com/identity/data/autobackup)(which is[enabled by default](https://developer.android.com/identity/data/backup), requires no work to implement and can also be extended) and[key-value backup](https://developer.android.com/guide/topics/data/keyvaluebackup). We recommend using this solution because it stores the resulting backup data in directories that cannot be accessed by other 3p apps, as well as facilitating encryption at rest, encryption in transit, and configurations allowing for the exclusion of sensitive data from backups.

If instead an app implements a backup solution that is not reliant on the Standard Android Backup system, this could increase the likelihood of mistakes leading to leaks of sensitive data. Examples of non-standard backup solutions exposing user data to leaks include apps offering an "export" or "backup" capability that creates a copy of the app data in directories readable by other apps, and which is hence prone to being leaked (either directly or through other vulnerabilities).

## Impact

Following security recommendations when setting up app backups prevents the potential leak of sensitive data that backups might include. Depending on the actual data and on the attacker's intentions, sensitive data leak may lead to information disclosure, user impersonation, and financial loss.

## Mitigations

### Use the Standard Android Backup system

The Standard Android Backup system always encrypts backup data in transit and at rest. This encryption is applied regardless of the Android version in use and of whether your device has a lock screen. Starting from Android 9, if the device has a lock screen set, then the backup data is not only encrypted, but encrypted with a key not known to Google (the lock screen secret protects the encryption key, thus enabling end-to-end encryption).

In general remember to follow the[data storage](https://developer.android.com/training/data-storage)and[security guidelines](https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage).

If your backup includes particularly sensitive data, then we recommend to either exclude this data or, if you cannot exclude it, require end-to-end encryption as described in the following section.

#### Excluding data from backup

You can specify which data to exclude from a backup using a rules file, conventionally called`backup_rules.xml`and placed in the`res/xml`app folder. There are some differences in how backup rules are configured depending on the version of Android that's used:

- [For Android versions 12 (API level 31) and higher](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-12), add an`android:dataExtractionRules`attribute to the`<application>`element within the`AndroidManifest.xml`:
- xml`xml
  <application android:name="com.example.foo" android:dataExtractionRules="@xml/backup_rules_extraction">
  ...
  </application>`

Then,[configure](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-12)the`backup_rules.xml`file according to the data persistence and security requirements of the application, following the[updated configuration format](https://developer.android.com/guide/topics/data/autobackup#xml-syntax-android-12).

The format required for the`backup_rules.xml`file configuration allows developers to define custom backup rules for both Cloud and[Device-To-Device (D2D) transfers](https://developer.android.com/about/versions/12/behavior-changes-12#xml-changes). If the`<device-transfer>`attribute is not set, all the application data will be transferred during a D2D migration. It is important to highlight that even if the target application targets Android 12 or higher, a separate file with[an additional set of backup rules](https://developer.android.com/identity/data/autobackup#include-exclude-android-11)should always be specified for devices running Android 11 (API level 30) or lower.

- [For Android versions 11 and lower](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-11), add an`android:fullBackupContent`attribute to the`<application>`element within the`AndroidManifest.xml`:
- xml`xml
  <application android:name="com.example.foo" android:fullBackupContent="@xml/backup_rules_full">
  ...
  </application>`

Then, configure the`backup_rules.xml`file according to the data persistence and security requirements of the application using the syntax reported in the[back up user data](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-11)article.

#### Requiring end-to-end encryption

If you can't exclude sensitive data from your backup, then we recommend requiring end-to-end encryption which means allowing backups only on Android 9 or higher and only when the lock screen is set. You can achieve this by using the`requireFlags="clientSideEncryption"`flag, which needs to be renamed to`disableIfNoEncryptionCapabilities`and set to`true`starting from[Android 12](https://developer.android.com/identity/data/autobackup#include-exclude-android-12).

### If you can't use the Standard Android Backup system

If you can't use the Standard Android Backup system, then securely storing your backup data as well as specifying which data to exclude from your backup is more complex. This needs to be specified at code level and is consequently error-prone, risking data leaks. In this scenario, it is also recommended to regularly test your implementation to ensure that there has been no alteration to the expected backup behavior.

## Resources

- [Description of the allowBackup attribute](https://developer.android.com/guide/topics/manifest/application-element#allowbackup)
- [File-Based Encryption](https://source.android.com/docs/security/features/encryption/file-based)
- [D2D transfer behavior changes](https://developer.android.com/about/versions/12/behavior-changes-12#functionality-changes)
- [Back up user data with Auto Backup](https://developer.android.com/identity/data/autobackup)
- [Back up key-value pairs with Android Backup Service](https://developer.android.com/identity/data/keyvaluebackup)
- [Control backup on Android 12 or higher](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-12)
- [Control backup on Android 11 and lower](https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-11)
- [Understanding PII in Google's contracts and policies](https://support.google.com/analytics/answer/7686480)
- [Test backup and restore](https://developer.android.com/identity/data/testingbackup)
- [Cryptography](https://developer.android.com/guide/topics/security/cryptography)
- [Android Keystore system](https://developer.android.com/training/articles/keystore)
- [ADB](https://developer.android.com/tools/adb)
- [Developer options](https://developer.android.com/studio/debug/dev-options)