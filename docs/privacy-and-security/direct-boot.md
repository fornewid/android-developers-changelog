---
title: https://developer.android.com/privacy-and-security/direct-boot
url: https://developer.android.com/privacy-and-security/direct-boot
source: md.txt
---

Android 7.0 runs in a secure, *Direct Boot* mode
when the device has been powered on but the user hasn't unlocked the
device. To support this, the system provides two storage locations for data:

- **Credential encrypted storage**, which is the default storage location and only available after the user has unlocked the device.
- **Device encrypted storage**, which is a storage location available both during Direct Boot mode and after the user has unlocked the device.

By default, apps don't run during Direct Boot mode.
If your app needs to take action during Direct Boot mode, you can register
app components to be run during this mode. Some common use cases
for apps needing to run during Direct Boot mode include:

- Apps that have scheduled notifications, such as alarm clock apps.
- Apps that provide important user notifications, like SMS apps.
- Apps that provide accessibility services, like Talkback.

If your app needs to access data while running in Direct Boot mode, use
device encrypted storage. Device encrypted storage contains data
encrypted with a key that is only available after a device has performed a
successful verified boot.

For data that must be encrypted with a key associated with user
credentials, such as a PIN or password, use credential encrypted storage.
Credential encrypted storage is available after the user has successfully
unlocked the device and until the user restarts the device. If the
user enables the lock screen after unlocking the device,
credential encrypted storage remains available.

## Request access to run during Direct Boot

Apps must register their components with the system before they
can run during Direct Boot mode or access device encrypted
storage. Apps register with the system by marking components as
*encryption aware* . To mark your component as encryption aware, set the
`android:directBootAware` attribute to true in your manifest.

Encryption aware components can register to receive an
[ACTION_LOCKED_BOOT_COMPLETED](https://developer.android.com/reference/android/content/Intent#ACTION_LOCKED_BOOT_COMPLETED) broadcast message from the
system when the device has been restarted. At this point device encrypted
storage is available, and your component can execute tasks that need to be
run during Direct Boot mode, such as triggering a scheduled alarm.

The following code snippet is an example of how to register a
[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) as encryption aware, and add an
intent filter for `ACTION_LOCKED_BOOT_COMPLETED`, in the app manifest:  

```xml
<receiver
  android:directBootAware="true" >
  ...
  <intent-filter>
    <action android:name="android.intent.action.LOCKED_BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

Once the user has unlocked the device, all components can access both the
device encrypted storage as well as credential encrypted storage.

## Access device encrypted storage

To access device encrypted storage, create a second
[Context](https://developer.android.com/reference/android/content/Context) instance by calling
[Context.createDeviceProtectedStorageContext()](https://developer.android.com/reference/android/content/Context#createDeviceProtectedStorageContext()). All storage API
calls made using this context access the device encrypted storage. The
following example accesses the device encrypted storage and opens an existing
app data file:  

### Kotlin

```kotlin
val directBootContext: Context = appContext.createDeviceProtectedStorageContext()
// Access appDataFilename that lives in device encrypted storage
val inStream: InputStream = directBootContext.openFileInput(appDataFilename)
// Use inStream to read content...
```

### Java

```java
Context directBootContext = appContext.createDeviceProtectedStorageContext();
// Access appDataFilename that lives in device encrypted storage
FileInputStream inStream = directBootContext.openFileInput(appDataFilename);
// Use inStream to read content...
```

Use device encrypted storage only for
information that must be accessible during Direct Boot mode.
Don't use device encrypted storage as a general-purpose encrypted store.
For private user information, or encrypted data that isn't needed during
Direct Boot mode, use credential encrypted storage.

## Get notified of user unlock

When the user unlocks the device after restart, your app can switch to
accessing credential encrypted storage and use regular system services that
depend on user credentials.

To get notified when the user unlocks the device after a reboot,
register a `BroadcastReceiver` from a running component
to listen for unlock notification messages. When the user unlocks the device
after boot:

- If your app has foreground processes that need immediate notification, listen for the [ACTION_USER_UNLOCKED](https://developer.android.com/reference/android/content/Intent#ACTION_USER_UNLOCKED) message.
- If your app only uses background processes that can act on a delayed notification, listen for the [ACTION_BOOT_COMPLETED](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED) message.

If the user has unlocked the device, you can find out by calling
[UserManager.isUserUnlocked()](https://developer.android.com/reference/android/os/UserManager#isUserUnlocked()).

## Migrate existing data

If a user updates their device to use Direct Boot mode, you might have
existing data that needs to get migrated to device encrypted storage. Use
[Context.moveSharedPreferencesFrom()](https://developer.android.com/reference/android/content/Context#moveSharedPreferencesFrom(android.content.Context, java.lang.String)) and
[Context.moveDatabaseFrom()](https://developer.android.com/reference/android/content/Context#moveDatabaseFrom(android.content.Context, java.lang.String)), with the destination context as the method caller and the source context as the argument, to migrate preference and database
data between credential encrypted storage and device encrypted storage.

Don't migrate private user information, such as passwords or authorization tokens, from
credential encrypted storage to device encrypted storage. Use your best judgment when deciding what
other data to migrate to device encrypted storage. In some scenarios, you might need to manage
separate sets of data in the two encrypted stores.

## Test your encryption aware app

Test your encryption aware app with Direct Boot mode enabled.

Most devices running recent versions of Android enable Direct Boot mode
whenever a lockscreen credential (PIN, pattern, or password) has been set.
Specifically, this is the case on all devices that use file-based encryption.
To check whether a device uses file-based encryption, run the following
shell command:  

```
adb shell getprop ro.crypto.type
```

If the output is `file`, then the device has file-based encryption
enabled.

On devices that don't use file-based encryption by default, there might be
other options for testing Direct Boot mode:

- Some devices that use full-disk encryption
  (`ro.crypto.type=block`) and are running Android 7.0 through
  Android 12 can be converted to file-based
  encryption. There are two ways to do this:

  - **Warning:**Either method of converting to file-based encryption wipes all user data on the device.
  - On the device, enable **Developer options** if you haven't already by going to **Settings \> About phone** and tapping **Build
    number** seven times. Then go to **Settings \> Developer
    options** and select **Convert to file encryption**.
  - Alternatively, run the following shell commands:  

        adb reboot-bootloader
        fastboot --wipe-and-use-fbe

- Devices running Android 13 or lower support an
  "emulated" Direct Boot mode that uses file permissions to simulate the
  effects of encrypted files being locked and unlocked. Only use emulated mode
  during development; it can cause data loss. To enable emulated
  Direct Boot mode, set a lock pattern on the device, choose "No thanks" if
  prompted for a secure start-up screen when setting a lock pattern, and then
  run the following shell command:

  ```
  adb shell sm set-emulate-fbe true
  ```

  To turn off emulated Direct Boot mode, run the following shell
  command:  

  ```
  adb shell sm set-emulate-fbe false
  ```

  Running either of these commands causes the device to reboot.

## Check device policy encryption status

Device administration apps can use
[DevicePolicyManager.getStorageEncryptionStatus()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getStorageEncryptionStatus())
to check the current encryption status of the device.

If your app targets an API level lower than Android 7.0 (API 24),
`getStorageEncryptionStatus()` returns
[ENCRYPTION_STATUS_ACTIVE](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ENCRYPTION_STATUS_ACTIVE)
if the device is using either full-disk encryption
or file-based encryption with Direct Boot. In both of these cases, data is
always stored encrypted at rest.

If your app is targets Android 7.0 (API 24) or higher,
`getStorageEncryptionStatus()` returns
`ENCRYPTION_STATUS_ACTIVE` if the device is using full-disk encryption. It returns
[ENCRYPTION_STATUS_ACTIVE_PER_USER](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ENCRYPTION_STATUS_ACTIVE_PER_USER) if the device is using file-based encryption
with Direct Boot.

If you build a device administration app
that targets Android 7.0, make sure to check for both
`ENCRYPTION_STATUS_ACTIVE` and
`ENCRYPTION_STATUS_ACTIVE_PER_USER` to determine whether the device is
encrypted.

## Additional code samples

The [DirectBoot](https://github.com/android/security-samples/tree/main/DirectBoot/)
sample further demonstrates the use of the APIs covered on this page.