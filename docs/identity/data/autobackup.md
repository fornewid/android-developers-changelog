---
title: https://developer.android.com/identity/data/autobackup
url: https://developer.android.com/identity/data/autobackup
source: md.txt
---

*Auto Backup for Apps* automatically backs up a user's data from apps that target and run on Android 6.0 (API level 23) or higher. Android preserves app data by uploading it to the user's Google Drive, where it's protected by the user's Google Account credentials. The backup is end-to-end encrypted on devices running Android 9 or higher using the device's PIN, pattern, or password. Every app can allocate up to 25 MB of backup data per app user. There's no charge for storing backup data. Your app can customize the backup process or opt out by[disabling backups](https://developer.android.com/identity/data/autobackup#EnablingAutoBackup).

For an overview of Android's backup options and guidance about which data to back up and restore, see the[data backup overview](https://developer.android.com/guide/topics/data/backup).

## Files that are backed up

By default, Auto Backup includes files in most of the directories that are assigned to your app by the system:

- Shared preferences files

- Files saved to your app's internal storage and accessed by[`getFilesDir()`](https://developer.android.com/reference/android/content/Context#getFilesDir())or[`getDir(String,
  int)`](https://developer.android.com/reference/android/content/Context#getDir(java.lang.String,%20int))

- Files in the directory returned by[`getDatabasePath(String)`](https://developer.android.com/reference/android/content/Context#getDatabasePath(java.lang.String)), which also includes files created with the[`SQLiteOpenHelper`](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper)class

- Files on external storage in the directory returned by[`getExternalFilesDir(String)`](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String))

Auto Backup excludes files in directories returned by[`getCacheDir()`](https://developer.android.com/reference/android/content/Context#getCacheDir()),[`getCodeCacheDir()`](https://developer.android.com/reference/android/content/Context#getCodeCacheDir()), and[`getNoBackupFilesDir()`](https://developer.android.com/reference/android/content/Context#getNoBackupFilesDir()). The files saved in these locations are needed only temporarily and are intentionally excluded from backup operations.

You can configure your app to include and exclude particular files. For more information, see the[Include and exclude files](https://developer.android.com/identity/data/autobackup#IncludingFiles)section.
| **Note:** Android doesn't treat the configuration of components as user data. If your app enables or disables specific components in its manifest while it is running, Auto Backup doesn't automatically save and restore the configuration. To preserve the configuration state, store state in[shared preferences](https://developer.android.com/guide/topics/data/data-storage#pref)and recover shared preferences on restore.

## Backup location

Backup data is stored in a private folder in the user's Google Drive account, limited to 25 MB per app. The saved data does not count toward the user's personal Google Drive quota. Only the most recent backup is stored. When a backup is made, any previous backup is deleted. The backup data can't be read by the user or other apps on the device.

Users can see a list of apps that have been backed up in the Google Drive Android app. On an Android-powered device, users can find this list in the Drive app's navigation drawer under**Settings \> Backup and reset**.

Backups from each device-setup-lifetime are stored in separate datasets, as described in the following examples:

- If the user owns two devices, then a backup dataset exists for each device.

- If the user factory-resets a device and then sets up the device with the same account, the backup is stored in a new dataset. Obsolete datasets are automatically deleted after a period of inactivity.

| **Caution:** If the amount of data is over 25 MB, the system calls[`onQuotaExceeded()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onQuotaExceeded(long,%20long))and doesn't back up data to the cloud. The system periodically checks whether the amount of data later falls under the 25 MB threshold and continues Auto Backup when it does.

## Backup schedule

Backups occur automatically when all of the following conditions are met:

- The user has enabled backup on the device. In Android 9, this setting is in**Settings \> System \> Backup**.
- At least 24 hours have elapsed since the last backup.
- The device is idle.
- The device is connected to a Wi-Fi network (if the device user hasn't opted in to mobile-data backups).

In practice, these conditions occur roughly every night, but a device might never back up (for example, if it never connects to a network). To conserve network bandwidth, the upload takes place only if the app data has changed.

During Auto Backup, the system shuts down the app to make sure it is no longer writing to the file system. By default, the backup system ignores apps that are running in the foreground to avoid a poor user experience. You can override the default behavior by setting the[`android:backupInForeground`](https://developer.android.com/guide/topics/manifest/application-element#backupInForeground)attribute to true.

To simplify testing, Android includes tools that let you manually initiate a backup of your app. For more information, see[Test backup and restore](https://developer.android.com/guide/topics/data/testingbackup).

## Restore schedule

Data is restored whenever the app is installed, whether from the Play Store, during device setup (when the system installs previously installed apps), or by running`adb`install. The restore operation occurs after the APK is installed but before the app is available to be launched by the user.

During the initial device setup wizard, the user is shown a list of available backup datasets and is asked which one to restore data from. Whichever backup dataset is selected becomes the ancestral dataset for the device. The device can restore from either its own backups or the ancestral dataset. If backups from both sources are available, the device prioritizes its own backup. If the user didn't go through the device setup wizard, then the device can restore only from its own backups.

To simplify testing, Android includes tools that let you manually initiate a restore of your app. For more information, see[Test backup and restore](https://developer.android.com/guide/topics/data/testingbackup).

## Enable and disable backup

Apps that target Android 6.0 (API level 23) or higher automatically participate in Auto Backup. In your app manifest file, set the boolean value[`android:allowBackup`](https://developer.android.com/guide/topics/manifest/application-element#allowbackup)to enable or disable backup. The default value is`true`, but we recommend explicitly setting the attribute in your manifest, as shown in the following example:  

    <manifest ... >
        ...
        <application android:allowBackup="true" ... >
            ...
        </application>
    </manifest>

You can disable backups by setting`android:allowBackup`to`false`. You might want to do this if your app can recreate its state through some other mechanism or if your app deals with sensitive information.
| **Note:** For apps targeting Android 12 (API level 31) or higher, this behavior varies. On devices from some device manufacturers, specifying`android:allowBackup="false"`disables cloud-based backup and restore (such as Google Drive backups) but doesn't disable device-to-device transfers for the app. For more details, see the information about[changes in backup and restore](https://developer.android.com/about/versions/12/backup-restore#functionality-changes).

## Include and exclude files

By default, the system backs up almost all app data. For more information, see the section about[files that are backed up](https://developer.android.com/identity/data/autobackup#Files).

You can control which data is included in the backup based on the transfer type. Auto Backup supports cloud backups to Google Drive and direct device-to-device (D2D) transfers. Configuration methods vary based on the Android version and your app's`targetSdkVersion`.

- For devices running Android 11 or lower, see[Control backup on Android 11 and lower](https://developer.android.com/identity/data/autobackup#include-exclude-android-11).
- For devices running Android 12 or higher, apps targeting API level 31+ use the`data-extraction-rules`format. See[Control backup on Android 12 or higher](https://developer.android.com/identity/data/autobackup#include-exclude-android-12)for details.
- The`data-extraction-rules`format also supports**Cross-Platform Transfers** (e.g., to iOS). This capability is available from**Android 16 QPR2** . Learn more in[Configure Cross-Platform Transfers](https://developer.android.com/identity/data/autobackup#configure-cross-platform).

### Control backup on Android 11 and lower

Follow the steps in this section to control which files are backed up on devices running Android 11 (API level 30) or lower.
| **Important:** These XML backup rules are also used for devices running Android 12 or higher if your app targets Android 11 or lower. See the following section for[an additional set of XML backup rules](https://developer.android.com/identity/data/autobackup#include-exclude-android-12)to support the[changes to backup restore](https://developer.android.com/about/versions/12/backup-restore)that were introduced for devices running Android 12 or higher.

1. In your`AndroidManifest.xml`file, add the[`android:fullBackupContent`](https://developer.android.com/guide/topics/manifest/application-element#fullBackupContent)attribute to the`<application>`element, as shown in the following example. This attribute points to an XML file that contains backup rules.

   ```xml
   <application ...
    android:fullBackupContent="@xml/backup_rules">
   </application>
   ```
2. Create an XML file called`@xml/`<var translate="no">backup_rules</var>in the`res/xml/`directory. In this file, add rules with the`<include>`and`<exclude>`elements. The following sample backs up all shared preferences except`device.xml`:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <full-backup-content>
    <include domain="sharedpref" path="."/>
    <exclude domain="sharedpref" path="device.xml"/>
   </full-backup-content>
   ```

#### Define device conditions required for backup

If your app saves sensitive information on the device, you can specify conditions under which your app's data is included in the user's backup. You can add the following conditions in Android 9 (API level 28) or higher:

- `clientSideEncryption`: the user's backup is encrypted with a client-side secret. This form of encryption is enabled on devices running Android 9 or higher as long as the user has[enabled backup in Android 9 or higher](https://support.google.com/pixelphone/answer/7179901)and has[set a screen lock](https://support.google.com/android/answer/2819522)(PIN, pattern, or password) for their device.
- `deviceToDeviceTransfer`: the user is transferring their backup to another device that supports[local device-to-device transfer](https://support.google.com/pixelphone/answer/7129955)(for example, Google Pixel).

If you've upgraded your development devices to Android 9, you need to disable and then re-enable data backup after upgrading. This is because Android only encrypts backups with a client-side secret after informing users in Settings or the setup wizard.

To declare the inclusion conditions, set the`requireFlags`attribute to a chosen value or values in the`<include>`elements within your set of backup rules:

backup_rules.xml  

```xml
<?xml version="1.0" encoding="utf-8"?>
<full-backup-content>
    <!-- App data isn't included in user's backup
         unless client-side encryption is enabled. -->
    <include domain="file" path="."
             requireFlags="clientSideEncryption" />
</full-backup-content>
```
| **Note:** Because adding requirements to the XML prevents backups from working on previous Android versions,[provide alternate resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)for backups being used on devices running Android 8.1 (API level 27) or lower.

If your app implements a[key-value backup](https://developer.android.com/guide/topics/data/keyvaluebackup)system or if you[implement`BackupAgent`](https://developer.android.com/guide/topics/data/autobackup#ImplementingBackupAgent)yourself, you can also apply these conditional requirements to your backup logic by performing a bitwise comparison between a[`BackupDataOutput`](https://developer.android.com/reference/android/app/backup/BackupDataOutput)object's set of transport flags and your custom backup agent's[`FLAG_CLIENT_SIDE_ENCRYPTION_ENABLED`](https://developer.android.com/reference/android/app/backup/BackupAgent#FLAG_CLIENT_SIDE_ENCRYPTION_ENABLED)or[`FLAG_DEVICE_TO_DEVICE_TRANSFER`](https://developer.android.com/reference/android/app/backup/BackupAgent#FLAG_DEVICE_TO_DEVICE_TRANSFER)flags.

The following code snippet shows an example use of this method:  

### Kotlin

```kotlin
class CustomBackupAgent : BackupAgent() {
    override fun onBackup(oldState: ParcelFileDescriptor?,
            data: BackupDataOutput?, newState: ParcelFileDescriptor?) {
        if (data != null) {
            if ((data.transportFlags and
                    FLAG_CLIENT_SIDE_ENCRYPTION_ENABLED) != 0) {
                // Client-side backup encryption is enabled.
            }

            if ((data.transportFlags and FLAG_DEVICE_TO_DEVICE_TRANSFER) != 0) {
                // Local device-to-device transfer is enabled.
            }
        }
    }

    // Implementation of onRestore() here.
}
```

### Java

```java
public class CustomBackupAgent extends BackupAgent {
    @Override
    public void onBackup(ParcelFileDescriptor oldState, BackupDataOutput data,
            ParcelFileDescriptor newState) throws IOException {
        if ((data.getTransportFlags() &
                FLAG_CLIENT_SIDE_ENCRYPTION_ENABLED) != 0) {
            // Client-side backup encryption is enabled.
        }

        if ((data.getTransportFlags() &
                FLAG_DEVICE_TO_DEVICE_TRANSFER) != 0) {
            // Local device-to-device transfer is enabled.
        }
    }

    // Implementation of onRestore() here.
}
```

### Control backup on Android 12 or higher

If your app targets Android 12 (API level 31) or higher, follow the steps in this section to control which files are backed up on devices that are running Android 12 or higher.
| **Important:** Even if your app targets Android 12 or higher, you must also[specify another set of XML backup rules](https://developer.android.com/identity/data/autobackup#include-exclude-android-11)to support devices that run Android 11 (API level 30) or lower.

1. In your`AndroidManifest.xml`file, add the[`android:dataExtractionRules`](https://developer.android.com/reference/android/R.attr#dataExtractionRules)attribute to the`<application>`element, as shown in the following example. This attribute points to an XML file that contains backup rules.

   ```xml
   <application ...
    android:dataExtractionRules="backup_rules.xml">
   </application>
   ```
2. Create an XML file called<var translate="no">backup_rules</var>`.xml`in the`res/xml/`directory. In this file, add rules with the`<include>`and`<exclude>`elements. The following sample backs up all shared preferences except`device.xml`:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <data-extraction-rules>
    <cloud-backup [disableIfNoEncryptionCapabilities="true|false"]>
      <include domain="sharedpref" path="."/>
      <exclude domain="sharedpref" path="device.xml"/>
    </cloud-backup>
   </data-extraction-rules>
   ```

### XML config syntax

The XML syntax for the configuration file varies depending on the version of Android that your app is targeting and running on.

#### Android 11 or lower

Use the following XML syntax for the configuration file that[controls backup for devices running Android 11 or lower](https://developer.android.com/identity/data/autobackup#include-exclude-android-11).  

```xml
<full-backup-content>
    <include domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"
    requireFlags=["clientSideEncryption" | "deviceToDeviceTransfer"] />
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string" />
</full-backup-content>
```

#### Android 12 or higher

If your app targets Android 12 (API level 31) or higher, use the following XML syntax for the configuration file that[controls backup for devices running Android 12 or higher](https://developer.android.com/identity/data/autobackup#include-exclude-android-12).  

```xml
<data-extraction-rules>
  <cloud-backup [disableIfNoEncryptionCapabilities="true|false"]>
    ...
    <include domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
  </cloud-backup>
  <device-transfer>
    ...
    <include domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
  </device-transfer>
  <cross-platform-transfer platform="ios">
    ...
    <include domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
    <exclude domain=["file" | "database" | "sharedpref" | "external" |
                     "root" | "device_file" | "device_database" |
                     "device_sharedpref" | "device_root" ] path="string"/>
    ...
    <platform-specific-params bundleId="string" teamId="string" contentVersion="string"/>
    ...
  </cross-platform-transfer>
</data-extraction-rules>
```

Each section of the configuration (`<cloud-backup>`,`<device-transfer>`,`<cross-platform-transfer>`) contains rules that apply only to that type of transfer. This separation lets you, for example, exclude a file or directory from Google Drive backups while still transferring it during device-to-device (D2D) transfers or cross-platform transfers. This is useful if you have files that are too large to back up to the cloud but can be transferred between devices without issue.

If there are no rules for a particular backup mode, such as if the`<device-transfer>`section is missing, that mode is fully enabled for all content except for`no-backup`and`cache`directories, as described in the[Files that are backed up](https://developer.android.com/identity/data/autobackup#Files)section.

Your app can set the`disableIfNoEncryptionCapabilities`flag in the`<cloud-backup>`section to make sure the backup happens only if it can be encrypted, such as when the user has a lock screen. Setting this constraint stops backups from being sent to the cloud if the user's device cannot support encryption, but because D2D transfers aren't sent to the server, they continue to operate even on devices that don't support encryption.

#### Syntax for include and exclude elements

Inside the`<full-backup-content>`,`<cloud-backup>`, and`<device-transfer>`tags (depending on the device's Android version and your app's`targetSDKVersion`), you can define`<include>`and`<exclude>`elements:

`<include>`

:   Specifies a file or folder to backup. By default, Auto Backup includes almost all app files. If you specify an`<include>`element, the system no longer includes any files by default and backs up*only the files specified* . To include multiple files, use multiple`<include>`elements.

    On[Android 11 and lower](https://developer.android.com/identity/data/autobackup#xml-syntax-android-11), this element can also contain the`requireFlags`attribute, which the section describing how to[define conditional requirements for backup](https://developer.android.com/identity/data/autobackup#define-device-conditions)discusses in more detail.

    Files in directories returned by`getCacheDir()`,`getCodeCacheDir()`, or`getNoBackupFilesDir()`are always excluded even if you try to include them.
    | **Tip:** To back up user credentials and authentication tokens, don't store them in shared preferences or a file. Instead use[Block Store APIs](https://developers.google.com/identity/blockstore/android)to store and manage credentials. This helps ensure that they are securely stored and can be backed up and restored alongside other app data.

`<exclude>`

:   Specifies a file or folder to exclude during backup. Here are some files that are typically excluded from backup:

    - Files that have device-specific identifiers, either issued by a server or generated on the device. For example,[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/)needs to generate a registration token every time a user installs your app on a new device. If the old registration token is restored, the app might behave unexpectedly.

    - Files related to app debugging.

    - Large files that cause the app to exceed the 25 MB backup quota.

    | **Note:** If your configuration file specifies both elements, then the backup contains everything captured by the`<include>`elements minus the resources named in the`<exclude>`elements. In other words,`<exclude>`takes precedence.

Each`<include>`and`<exclude>`element must include the following two attributes:

`domain`

:   Specifies the location of resource. Valid values for this attribute include the following:

    - `root`: the directory on the file system where all private files belonging to this app are stored.
    - `file`: directories returned by`getFilesDir()`.
    - `database`: directories returned by`getDatabasePath()`. Databases created with`SQLiteOpenHelper`are stored here.
    - `sharedpref`: the directory where[`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences)are stored.
    - `external`: the directory returned by`getExternalFilesDir()`.
    - `device_root`: like`root`but for the device-protected storage.
    - `device_file`: like`file`but for the device-protected storage.
    - `device_database`: like`database`but for the device-protected storage.
    - `device_sharedpref`: like`sharedpref`but for the device-protected storage.

    | **Note:** You can't back up files outside these locations.

`path`

:   Specifies a file or folder to include in or exclude from backup. Note the following:

    - This attribute does not support wildcard or regular expression syntax.
    - You can reference the current directory using`./`, but you can't reference the parent directory, such as using`..`, for security reasons.
    - If you specify a directory, then the rule applies to all files in the directory and recursive subdirectories.

### Configure Cross-Platform Transfers

Starting from Android 16 QPR2 (API level 36.1) you can configure Auto Backup for data transfers to and from non-Android devices. To do this, add the`<cross-platform-transfer>`element within your`<data-extraction-rules>`configuration, as shown in the[Android 12 or higher syntax](https://developer.android.com/identity/data/autobackup#include-exclude-android-12). You must specify the target platform using the required`platform`attribute. The only supported value is`ios`.

Inside this section, you can use the standard`<include>`and`<exclude>`elements as described in[Syntax for include and exclude elements](https://developer.android.com/identity/data/autobackup#xml-include-exclude)to specify which data to transfer.

Additionally, you must include the`<platform-specific-params>`element to help the system match your app with the corresponding app on the target platform. This element has the following required attributes:

- `bundleId`: The bundle ID of the app on the other platform (e.g., your iOS app's Bundle ID).
- `teamId`: The team ID of the app on the other platform (e.g., your iOS app's Team ID).
- `contentVersion`: A version string you define, associated with the data format being exported.

The`bundleId`and`teamId`attributes are used to help verify data integrity and proper app-to-app matching. They guarantee that data is only transferred*to* the specified app on the other platform during an export, and that this Android app only imports data*from*that specific app during an import.

For more fine-grained control over the data transformation and transfer process beyond what the XML rules provide, you can implement a custom[`BackupAgent`](https://developer.android.com/identity/data/autobackup#ImplementingBackupAgent)and use the[Cross-Platform Transfer APIs](https://developer.android.com/identity/data/autobackup#cpt-backup-agent).

##### File Mapping for iOS Transfers

When transferring files to iOS, the Android`domain`and`path`you specify in the`<include>`rules map to a specific directory structure. The following table shows the destination paths on iOS relative to the transfer destination root, based on the Android`domain`:

|   Android`domain`   | Path on iOS (relative to transfer root) |
|---------------------|-----------------------------------------|
| `root`              | `app/`                                  |
| `file`              | `app/files/`                            |
| `database`          | `app/databases/`                        |
| `sharedpref`        | `app/shared_prefs/`                     |
| `external`          | `external/files/`                       |
| `device_root`       | `device/app/`                           |
| `device_file`       | `device/app/files/`                     |
| `device_database`   | `device/app/databases/`                 |
| `device_sharedpref` | `device/app/shared_prefs/`              |

For example, a file included with`<include domain="file"
path="my_settings.txt"/>`will be available on the iOS side at`app/files/my_settings.txt`relative to the transfer destination root.

## Implement BackupAgent

Apps that implement Auto Backup don't need to implement a[`BackupAgent`](https://developer.android.com/reference/android/app/backup/BackupAgent). However, you can optionally implement a custom`BackupAgent`. Typically, there are two reasons for doing this:

- You want to receive notification of backup events, such as[`onRestoreFinished()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onRestoreFinished())and[`onQuotaExceeded()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onQuotaExceeded(long,%20long)). These callback methods are executed even if the app is not running.

- You can't easily express the set of files you want to back up with XML rules. In these rare cases, you can implement a`BackupAgent`that overrides[`onFullBackup(FullBackupDataOutput)`](https://developer.android.com/reference/android/app/backup/BackupAgent#onFullBackup(android.app.backup.FullBackupDataOutput))to store what you want. To retain the system's default implementation, call the corresponding method on the superclass with`super.onFullBackup()`.

If you implement a`BackupAgent`, by default the system expects your app to perform[key-value backup and restore](https://developer.android.com/guide/topics/data/keyvaluebackup). To use the file-based Auto Backup instead, set the[`android:fullBackupOnly`](https://developer.android.com/guide/topics/manifest/application-element#fullBackupOnly)attribute to`true`in your app's manifest.

During auto backup and restore operations, the system launches the app in a restricted mode to both prevent the app from accessing files that might cause conflicts and let the app execute callback methods in its`BackupAgent`. In this restricted mode, the app's main activity is not automatically launched, its[content providers](https://developer.android.com/guide/topics/providers/content-providers)are not initialized, and the base-class[`Application`](https://developer.android.com/reference/android/app/Application)is instantiated instead of any subclass declared in the app's[manifest](https://developer.android.com/guide/topics/manifest/application-element#nm).
| **Caution:** To avoid errors, make sure that the parts of your app that execute in the restricted mode (mostly your[`BackupAgent`](https://developer.android.com/reference/android/app/backup/BackupAgent)) don't access content providers in the same app or attempt to cast the[`Application`](https://developer.android.com/reference/android/app/Application)object. If you can't avoid those patterns, then consider implementing[key-value backup](https://developer.android.com/guide/topics/data/keyvaluebackup)or disabling backup entirely.

Your`BackupAgent`must implement the abstract methods[`onBackup()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onBackup(android.os.ParcelFileDescriptor,%20android.app.backup.BackupDataOutput,%20android.os.ParcelFileDescriptor))and[`onRestore()`](https://developer.android.com/reference/android/app/backup/BackupAgent#onRestore(android.app.backup.BackupDataInput,%20int,%20android.os.ParcelFileDescriptor)), which are used for key-value backup. If you don't want to perform key-value backup, you can leave your implementation of those methods blank.

For more information, see[Extend BackupAgent](https://developer.android.com/guide/topics/data/keyvaluebackup#BackupAgent).

### Handle Cross-Platform Transfers in BackupAgent

Starting with Android 16 QPR2 (API level 36.1), several new APIs are available in`BackupAgent`to better support cross-platform data transfers.

**New Transport Flag:**

- `FLAG_CROSS_PLATFORM_TRANSFER_IOS`: This flag is added to the`transportFlags`provided to your`BackupAgent`.
  - In`onFullBackup`, this flag is set if the current backup operation is part of a data export to an iOS device.
  - In the new`onRestoreFile`overload, this flag is set if the data is being imported from an iOS device.

**New`onRestoreFile`Method:**

A new overload of`onRestoreFile`is introduced, which takes a single`FullRestoreDataInput`parameter. This object provides more context about the restore operation:

- `FullRestoreDataInput.getTransportFlags()`: Returns the transport flags for the current restore operation, which can include`FLAG_CROSS_PLATFORM_TRANSFER_IOS`.
- `FullRestoreDataInput.getContentVersion()`: Returns the content version string provided by the*source application*on the other platform during a cross-platform transfer. This value is an empty string if not provided by the source.

**New Size Estimation Method:**

- `onEstimateFullBackupBytes()`: This method lets you provide an estimated size of the data your app intends to back up. Implementation is**strongly recommended**if your app performs significant data transformations during backup or handles a large volume of data, as it can improve efficiency by avoiding the default system dry run. For apps with small, straightforward backups, this method is typically not necessary.

**Example Usage:**  

### Kotlin

    // In your custom BackupAgent class

    override fun onFullBackup(out: FullBackupDataOutput) {
        // Check if this is a cross-platform export to iOS
        if ((out.transportFlags and FLAG_CROSS_PLATFORM_TRANSFER_IOS) != 0) {
            Log.d(TAG, "onFullBackup for iOS transfer")
            // Your custom export logic here
            // Call fullBackupFile() for files to include
        }
    }

    override fun onRestoreFile(input: FullRestoreDataInput) {
        if ((input.transportFlags and FLAG_CROSS_PLATFORM_TRANSFER_IOS) != 0) {
            val sourceContentVersion = input.contentVersion
            Log.d(TAG, "onRestoreFile from iOS, content version: $sourceContentVersion")
            // Your custom import logic here, using input.data, input.destination, etc.
        }
    }

    // Optional: Provide an estimate of the backup size
    override fun onEstimateFullBackupBytes(): Long {
        return calculateEstimatedBackupSize()
    }

### Java

    // In your custom BackupAgent class

    @Override
    public void onFullBackup(FullBackupDataOutput out) throws IOException {
        // Check if this is a cross-platform export to iOS
        if ((out.getTransportFlags() & FLAG_CROSS_PLATFORM_TRANSFER_IOS) != 0) {
            Log.d(TAG, "onFullBackup for iOS transfer");
            // Your custom export logic here
            // Call fullBackupFile() for files to include
        }
    }

    @Override
    public void onRestoreFile(FullRestoreDataInput input) {
        if ((input.getTransportFlags() & FLAG_CROSS_PLATFORM_TRANSFER_IOS) != 0) {
            String sourceContentVersion = input.getContentVersion();
            Log.d(TAG, "onRestoreFile from iOS, content version: " + sourceContentVersion);
            // Your custom import logic here, using input.getData(), input.getDestination(), etc.
        }
    }

    // Optional: Provide an estimate of the backup size
    @Override
    public long onEstimateFullBackupBytes() {
        return calculateEstimatedBackupSize();
    }