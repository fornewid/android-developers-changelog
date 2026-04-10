---
title: https://developer.android.com/identity/sign-in/test-restore-credentials
url: https://developer.android.com/identity/sign-in/test-restore-credentials
source: md.txt
---

The [Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials) feature within Credential Manager ensures a
frictionless transition for users moving to a new device. While testing the
feature, you can use either of the following approaches:

- **Separate devices**: Use a source device to perform the backup and a separate target device to perform the restore, or use two separate Android Studio emulators.
- **Single device**: Use one physical device or an Android Studio emulator. After the app backs up its data, uninstall and reinstall the app, and then perform the restore.

This guide describes how you can use Android Studio to test Restore Credentials
for a debuggable app on an emulator, simulating both situations of separate
devices or a single device.

## Prerequisites

To use Android Studio's Backup and Restore feature, you need the following:

- [Android Studio Otter \| 2025.2.1](https://developer.android.com/studio/releases#test-backup-restore) or higher.
- A [virtual device](https://developer.android.com/studio/run/managing-avds) or emulator.
- An app built with `debuggable true` or running in [`debug`](https://developer.android.com/studio/debug) mode. Debugging is enabled by default for emulators.

## Use Android Studio's Backup and Restore feature

To test the Restore Credentials functionality using Android Studio, first back
up data from a device, and then restore app data on another device. After
restoring the app, the authentication state is automatically restored.

### Back up authentication data in Android Studio

To test the backup flow in Android Studio, complete the following steps:

1. Run your app on the emulator.
2. Sign in to the app using any authentication mechanism (for example, username and password, passkeys, or Sign in with Google).
3. Click **Backup App Data** on the device options at the top of the running device window. ![Backup App Data in Android Studio](https://developer.android.com/static/identity/sign-in/images/test-restore-step1.png) Backup App Data in Android Studio
4. For **Backup type** , select **Device to Device** or **Cloud**.

   > [!NOTE]
   > **Note:** When testing Restore Credentials from a **Cloud** backup, ensure that the `android:allowBackup` property is set to `true` in the Android manifest, which is the recommendation. If the `android:allowBackup` property is set to `false`, authentication state is automatically restored only for **Device to Device** backups when testing in Android Studio.

5. Click **OK**.

### Test restored authentication

After the backup is completed, either use the same device to test the restore
step or use a different device.

To test the restore flow in Android Studio, complete the following steps:

1. To test with the same device, uninstall and reinstall the app. This clears
   all data on the device. To use it on a new device, install the app on the
   new device.

   > [!NOTE]
   > **Note:** In a production environment, users typically navigate the setup wizard while onboarding. However, Android Studio's restore flow simulates the setup wizard flow, enabling you to test the restoration process without manually performing the initial device setup.

2. After the app is installed, check the current state of the app. If you are
   redirected to the authentication page, the restore key is not yet available
   on the device.

3. Click **Restore App data** on the device options of the running device
   window and select the recently created backup.

   ![Restore App Data in Android Studio](https://developer.android.com/static/identity/sign-in/images/test-restore-step2.png) Restore App Data in Android Studio

   <br />

4. Reopening the app signs you in with the restore credential.