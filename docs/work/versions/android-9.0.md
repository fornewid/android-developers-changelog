---
title: https://developer.android.com/work/versions/android-9.0
url: https://developer.android.com/work/versions/android-9.0
source: md.txt
---

# What’s in Android 9 for enterprise apps

This page provides an overview of the enterprise APIs, features, and behavior changes that are available in the Android 9.

## Work profile user interface

Android 9 (API level 28) includes user interface changes in the default launcher to help users separate personal and work apps. Device manufacturers supporting this can present users' apps in separate work and personal tabs. We've also made it easier for device users to turn the work profile on and off by including a switch in the launcher's work tab.
![](https://developer.android.com/static/images/about/versions/pie/p-work-profile.jpg)**Figure 1.**The default launcher's personal tab and work tab with work profile switch

When provisioning work profiles and managed devices, Android 9 includes animated illustrations to help device users understand these features.

### Switch apps across profiles

Android 9 includes APIs to launch another instance of an app in a different profile to help users switch between accounts. For example, an email app can provide a UI that lets the user switch between the personal profile and the work profile to access two email accounts. All apps can call these APIs to launch the main activity of the same app if it's already installed in the other profile. To add cross-profile account switching to your app, follow the steps below calling methods of the[`CrossProfileApps`](https://developer.android.com/reference/android/content/pm/CrossProfileApps)class:

1. Call[`getTargetUserProfiles()`](https://developer.android.com/reference/android/content/pm/CrossProfileApps#getTargetUserProfiles())to get a list of profiles you can launch another instance of the app in. This method checks that the app is installed in the profiles.
2. Call[`getProfileSwitchingIconDrawable()`](https://developer.android.com/reference/android/content/pm/CrossProfileApps#getProfileSwitchingIconDrawable(android.os.UserHandle))to get an icon that you can use to represent another profile.
3. Call[`getProfileSwitchingLabel()`](https://developer.android.com/reference/android/content/pm/CrossProfileApps#getProfileSwitchingLabel(android.os.UserHandle))to get localized text that prompts the user to switch profiles.
4. Call[`startMainActivity()`](https://developer.android.com/reference/android/content/pm/CrossProfileApps#startMainActivity(android.content.ComponentName,%20android.os.UserHandle))to launch an instance of your app in another profile.

Check that the main activity you want to launch is declared in your app's manifest file, with an[`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN)intent action, and includes a[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)intent category.

### Programmatically turn work profiles on or off

The default launcher (or apps that have the permission`MANAGE_USERS`or`MODIFY_QUIET_MODE`) can turn the work profile on or off by calling[`UserManager.requestQuietModeEnabled()`](https://developer.android.com/reference/android/os/UserManager#requestQuietModeEnabled(boolean,%20android.os.UserHandle)). You can inspect the return value to know if the user needs to confirm their credentials before the state changes. Because the change might not happen instantly, listen for the[`ACTION_MANAGED_PROFILE_AVAILABLE`](https://developer.android.com/reference/android/content/Intent#ACTION_MANAGED_PROFILE_AVAILABLE)or[`ACTION_MANAGED_PROFILE_UNAVAILABLE`](https://developer.android.com/reference/android/content/Intent#ACTION_MANAGED_PROFILE_UNAVAILABLE)broadcast to know when to update the user interface.

Your app can check the status of the work profile by calling[`UserManager.isQuietModeEnabled()`](https://developer.android.com/reference/android/os/UserManager#isQuietModeEnabled(android.os.UserHandle)).

## Lock down any app to a device

Starting in Android 9, device owners and profile owners (of secondary users) can lock*any* app to a device's screen by putting the app into lock task mode. Previously, app developers had to[add support for lock task mode](https://developer.android.com/work/cosu)in their apps. Android 9 also extends the lock task APIs to profile owners of non-affiliated secondary users. Follow the steps below to lock an app to the screen:

1. Call[`DevicePolicyManager.setLockTaskPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskPackages(android.content.ComponentName,%20java.lang.String%5B%5D))to allowlist apps for lock task mode.
2. Call[`ActivityOptions.setLockTaskEnabled()`](https://developer.android.com/reference/android/app/ActivityOptions#setLockTaskEnabled(boolean))to launch an allowlisted app into lock task mode.

To stop an app in lock task mode, remove the app from the lock task mode allowlist using[`DevicePolicyManager.setLockTaskPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskPackages(android.content.ComponentName,%20java.lang.String%5B%5D)).

#### Enable system UI features

When lock task mode is enabled, device owners and profile owners can enable certain system UI features on the device by calling[`DevicePolicyManager.setLockTaskFeatures()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskFeatures(android.content.ComponentName,%20int))and passing a bit field of the following feature flags:

- [`LOCK_TASK_FEATURE_NONE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_NONE)
- [`LOCK_TASK_FEATURE_SYSTEM_INFO`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_SYSTEM_INFO)
- [`LOCK_TASK_FEATURE_HOME`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_HOME)
- [`LOCK_TASK_FEATURE_NOTIFICATIONS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_NOTIFICATIONS)can only be used in combination with`LOCK_TASK_FEATURE_HOME`.
- [`LOCK_TASK_FEATURE_KEYGUARD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_KEYGUARD)
- [`LOCK_TASK_FEATURE_OVERVIEW`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_OVERVIEW)can only be used in combination with`LOCK_TASK_FEATURE_HOME`.
- [`LOCK_TASK_FEATURE_GLOBAL_ACTIONS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LOCK_TASK_FEATURE_GLOBAL_ACTIONS)

You can call[`DevicePolicyManager.getLockTaskFeatures()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getLockTaskFeatures(android.content.ComponentName))to get the list of features available on a device when lock task mode is enabled. When a device exits lock task mode, it returns to the state mandated by other device policies.

### Suppress error dialogs

In some environments, such as retail demonstrations or public information displays, you might not want to show error dialogs to users. A device policy controller (DPC) can suppress system error dialogs for crashed or unresponsive apps by adding the[`DISALLOW_SYSTEM_ERROR_DIALOGS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SYSTEM_ERROR_DIALOGS)user restriction. This restriction affects all dialogs when applied by a device owner but only the error dialogs shown in the primary or secondary user are suppressed when the restriction is applied by profile owners. This restriction doesn't affect work profiles.

In Android 9, apps running in[immersive full-screen mode](https://developer.android.com/training/system-ui/immersive)don't show the reminder bubble when in lock task mode. The reminder bubble is a panel shown to users (on first launch) that explains how to exit the immersive mode.

## Support multiple users on dedicated devices

Android 9 introduces the concept of an**ephemeral user** for dedicated devices (previously called[COSU](https://developer.android.com/work/cosu)devices). Ephemeral users are short-term users intended for cases where multiple users share a single dedicated device. This includes public user sessions on devices such as library or hospitality check-in kiosks, as well as persistent sessions between a fixed set of users on devices, for example, shift workers.

Ephemeral users should be created in the background. They are created as secondary users on a device and are removed (along with associated apps and data) when they are stopped, switched, or the device reboots. To create an ephemeral user, device owners can:

1. Set the[`MAKE_USER_EPHEMERAL`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#MAKE_USER_EPHEMERAL)flag when calling[`DevicePolicyManager.createAndManageUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#createAndManageUser(android.content.ComponentName,%20java.lang.String,%20android.content.ComponentName,%20android.os.PersistableBundle,%20int)).
2. Call[`DevicePolicyManager.startUserInBackground()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#startUserInBackground(android.content.ComponentName,%20android.os.UserHandle))to start the ephemeral user in the background.

Note, apps targeting Android 9 should catch[`UserManager.UserOperationException`](https://developer.android.com/reference/android/os/UserManager.UserOperationException)when calling`createAndManageUser()`. Call the exception's[`getUserOperationResult()`](https://developer.android.com/reference/android/os/UserManager.UserOperationException#getUserOperationResult())method to find out why the user wasn't created.

### Receive event notifications

The[`DeviceAdminReceiver`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)receives notifications for the following events:

- [`onUserStarted()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserStarted(android.content.Context,%20android.content.Intent,%20android.os.UserHandle)): Called when a user starts.
- [`onUserSwitched()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserSwitched(android.content.Context,%20android.content.Intent,%20android.os.UserHandle)): Called when a[user switch](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#switchUser(android.content.ComponentName,%20android.os.UserHandle))is completed.
- [`onUserStopped()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserStopped(android.content.Context,%20android.content.Intent,%20android.os.UserHandle)): Called along with[`onUserRemoved()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserRemoved(android.content.Context,%20android.content.Intent,%20android.os.UserHandle))when a[user stops](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#stopUser(android.content.ComponentName,%20android.os.UserHandle))or[logs out](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#logoutUser(android.content.ComponentName)).

### Display event messages to users

Device owners can configure the messages that are displayed to users when they start and end their sessions:

- Use[`DevicePolicyManager.setStartUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setStartUserSessionMessage(android.content.ComponentName,%20java.lang.CharSequence))to set the message that's displayed to a user when the user's session begins. To retrieve the message, call[`DevicePolicyManager.getStartUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getStartUserSessionMessage(android.content.ComponentName)).
- Use[`DevicePolicyManager.setEndUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setEndUserSessionMessage(android.content.ComponentName,%20java.lang.CharSequence))to set the message that's displayed to the user when the user's session ends. To retrieve the message, call[`DevicePolicyManager.getEndUserSessionMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getEndUserSessionMessage(android.content.ComponentName)).

### Log out and stop users

Device owners can use[`DevicePolicyManager.setLogoutEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLogoutEnabled(android.content.ComponentName,%20boolean))to specify whether logout is enabled for secondary users. To check if logout is enabled, call[`DevicePolicyManager.isLogoutEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isLogoutEnabled()).

Profile owners of secondary users can call[`DevicePolicyManager.logoutUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#logoutUser(android.content.ComponentName))to stop the secondary user and switch back to the primary user.

Device owners can use[`DevicePolicyManager.stopUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#stopUser(android.content.ComponentName,%20android.os.UserHandle))to stop a specified secondary user.

### Package caching

To streamline user provisioning on shared devices with a fixed set of users, such as devices for shift workers, it's possible to cache packages that are needed for multi-user sessions:

1. Call[`DevicePolicyManager.setKeepUninstalledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeepUninstalledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E))to specify the list of packages to keep as APKs. To retrieve a list of these packages, call[`DevicePolicyManager.getKeepUninstalledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getKeepUninstalledPackages(android.content.ComponentName)).

2. Call[`DevicePolicyManager.installExistingPackage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installExistingPackage(android.content.ComponentName,%20java.lang.String))to install a package that has been kept after removal via[`setKeepUninstalledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeepUninstalledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E)).

| **Note:** If a profile owner calls[`DevicePolicyManager.installExistingPackage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installExistingPackage(android.content.ComponentName,%20java.lang.String)), the user must be affiliated with the device. To check if a[user is affiliated](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users)with the device, use[`DevicePolicyManager.isAffiliatedUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isAffiliatedUser()).

### Additional methods and constants

Android 9 also includes the following methods and constants to further support user sessions on shared devices:

- [`DevicePolicyManager.getSecondaryUsers()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getSecondaryUsers(android.content.ComponentName))gets a list of all secondary users on a device.
- [`DISALLOW_USER_SWITCH`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_USER_SWITCH)is a user restriction you can enable by calling[`DevicePolicyManager.addUserRestriction()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addUserRestriction(android.content.ComponentName,%20java.lang.String))to block user switching.
- [`LEAVE_ALL_SYSTEM_APPS_ENABLED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#LEAVE_ALL_SYSTEM_APPS_ENABLED)is a flag available for[`DevicePolicyManager.createAndManageUser()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#createAndManageUser(android.content.ComponentName,%20java.lang.String,%20android.content.ComponentName,%20android.os.PersistableBundle,%20int)). When set, system apps aren't disabled during user provisioning.
- [`UserManager.UserOperationException`](https://developer.android.com/reference/android/os/UserManager.UserOperationException)is thrown by`DevicePolicyManager.createAndManageUser()`when a user can't be created---the exception contains the reason for the failure.

## Clear package data and remove accounts

Device owners and profile owners can call[`clearApplicationUserData()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#clearApplicationUserData(android.content.ComponentName,%20java.lang.String,%20java.util.concurrent.Executor,%20android.app.admin.DevicePolicyManager.OnClearApplicationUserDataListener))to clear the user data for a given package. To remove an account from the[`AccountManager`](https://developer.android.com/reference/android/accounts/AccountManager), device and profile owners can call[`removeAccount()`](https://developer.android.com/reference/android/accounts/AccountManager#removeAccount(android.accounts.Account,%20android.app.Activity,%20android.accounts.AccountManagerCallback%3Candroid.os.Bundle%3E,%20android.os.Handler)).

## User restrictions and increased control over settings

Android 9 introduces a set of user restrictions for DPCs, as well as the ability to configure APNs, time and timezone, and system settings on a device.

### Configure APNs

Device owners can use the following methods in the[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class to configure APNs on a device:

- [`addOverrideApn()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addOverrideApn(android.content.ComponentName,%20android.telephony.data.ApnSetting))
- [`updateOverrideApn()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#updateOverrideApn(android.content.ComponentName,%20int,%20android.telephony.data.ApnSetting))
- [`removeOverrideApn()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeOverrideApn(android.content.ComponentName,%20int))
- [`getOverrideApns()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getOverrideApns(android.content.ComponentName))
- [`setOverrideApnEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setOverrideApnsEnabled(android.content.ComponentName,%20boolean))
- [`isOverrideApnEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isOverrideApnEnabled(android.content.ComponentName))

### Configure time and timezone

Device owners can use the following methods in the[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class to set the time and timezone on a device:

- [`setTime()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setTime(android.content.ComponentName,%20long))
- [`setTimeZone()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setTimeZone(android.content.ComponentName,%20java.lang.String))

### Enforce user restrictions on important settings

Android 9 adds user restrictions to disable system features and settings. To add a restriction, call[`DevicePolicyManager.addUserRestriction()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addUserRestriction(android.content.ComponentName,%20java.lang.String))with one of the following`UserManager`constants:

- [`DISALLOW_AIRPLANE_MODE`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_AIRPLANE_MODE)
- [`DISALLOW_AMBIENT_DISPLAY`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_AMBIENT_DISPLAY)
- [`DISALLOW_CONFIG_BRIGHTNESS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_BRIGHTNESS)
- [`DISALLOW_CONFIG_DATE_TIME`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_DATE_TIME)
- [`DISALLOW_CONFIG_LOCATION`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_LOCATION)
- [`DISALLOW_CONFIG_SCREEN_TIMEOUT`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_SCREEN_TIMEOUT)
- [`DISALLOW_PRINTING`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_PRINTING)

If[`DISALLOW_CONFIG_BRIGHTNESS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_BRIGHTNESS)and[`DISALLOW_CONFIG_SCREEN_TIMEOUT`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_SCREEN_TIMEOUT)are enforced on a device, device owners can still set the[screen brightness](https://developer.android.com/reference/android/provider/Settings.System#SCREEN_BRIGHTNESS),[screen brightness mode](https://developer.android.com/reference/android/provider/Settings.System#SCREEN_BRIGHTNESS_MODE), and[screen timeout](https://developer.android.com/reference/android/provider/Settings.System#SCREEN_OFF_TIMEOUT)settings on the device using the API[`DevicePolicyManager.setSystemSetting()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSystemSetting(android.content.ComponentName,%20java.lang.String,%20java.lang.String)).

### Metered data

Device owners and profile owners can prevent apps from using a device's metered-data networks. A network is considered metered when when the user is sensitive to heavy data usage because of cost, data limits, or battery and performance issues. To prevent apps from using metered networks, call[`DevicePolicyManager.setMeteredDataDisabledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setMeteredDataDisabledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E))passing a list of package names. To retrieve the currently restricted apps, call[`DevicePolicyManager.getMeteredDataDisabledPackages()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getMeteredDataDisabledPackages(android.content.ComponentName)).

To learn more about metered data in Android, read[Optimizing Network Data Usage](https://developer.android.com/training/basics/network-ops/data-saver).

## Migrate DPCs

Device policy controllers (DPCs) can transfer their ownership of a device or work profile to another DPC. You might transfer ownership to move some features to the[Android Management API](https://developers.google.com/android/management/), to migrate devices from your legacy DPC, or to help IT admins migrate to your EMM. Because you're just changing the DPC ownership, you can't use this feature to change the type of management, for example, migrating from a managed device to a work profile or vice-versa.

You can use the[device admin policies](https://developer.android.com/work/device-admin#manifest)XML resource to indicate that this version of your DPC supports migration. A target DPC indicates it can receive ownership by including a element named`<support-transfer-ownership>`. The example below shows how you might do this in your DPC's device admin XML file:  

    <device-admin xmlns:android="http://schemas.android.com/apk/res/android">
        <support-transfer-ownership />
        <uses-policies>
            <limit-password />
            <watch-login />
            <reset-password />
        </uses-policies>
    </device-admin>

DPCs that want to migrate ownership to new DPC app can check if a target DPC's version supports migration by calling the`DeviceAdminInfo`method[`supportsTransferOwnership()`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#supportsTransferOwnership()). Before transferring ownership, it's the source DPC's responsibility to verify the target DPC by comparing app signatures. The[`PackageManager`](https://developer.android.com/reference/android/content/pm/PackageManager)class includes methods to work with code-sign signatures.

Android maintains the source DPC's system and user policies through an ownership transfer---DPCs don't need to migrate these. A source DPC can pass custom data to the target DPC using key-value pairs in a`PersistableBundle`. After a successful transfer, the target DPC can retrieve this data by calling[`DevicePolicyManager.getTransferOwnershipBundle()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getTransferOwnershipBundle()).

The steps to transfer ownership of a managed device or a work profile are the same:

1. The source DPC checks that the target DPC's version supports migration and confirms that the target DPC's app signature matches an expected value.
2. The source DPC calls[`transferOwnership()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#transferOwnership(android.content.ComponentName,%20android.content.ComponentName,%20android.os.PersistableBundle))to start the transfer.
3. The system makes the target DPC the[active admin](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getActiveAdmins())and sets it as the owner of the managed device or work profile.
4. The target DPC receives the callback[`onTransferOwnershipComplete()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onTransferOwnershipComplete(android.content.Context,%20android.os.PersistableBundle))and can configure itself using values from the`bundle`argument.
5. If something goes wrong with the transfer, the system reverts ownership to the source DPC. If your source DPC needs to confirm that the ownership transfer succeeded, call[`isAdminActive()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isAdminActive(android.content.ComponentName))to check that the source DPC is no longer the active admin.

All apps running in the work profile receive the[`ACTION_PROFILE_OWNER_CHANGED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_PROFILE_OWNER_CHANGED)broadcast when the profile owner changes. Apps running on a managed device receive the[`ACTION_DEVICE_OWNER_CHANGED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_DEVICE_OWNER_CHANGED)broadcast when the device owner changes.

#### Work profiles on fully managed devices

Transferring two instances of a DPC running as device owner and profile owner happens in two stages. When the personal profile and work profile[are affiliated](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users), complete the transfer in the following order:

1. First, transfer ownership of the work profile.
2. Wait for the`DeviceAdminReceiver`callback[`onTransferAffiliatedProfileOwnershipComplete()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onTransferAffiliatedProfileOwnershipComplete(android.content.Context,%20android.os.UserHandle))to confirm that the work profile was transferred to the target DPC.
3. Finally, transfer ownership of the managed device to the target DPC.

## Postpone Over-the-air (OTA) updates

| **Warning:** Postponing OTA updates can prevent devices from receiving critical updates.

Device owners can postpone OTA system updates to devices for up to 90 days to freeze the OS version running on these devices over critical periods (such as holidays). The system enforces a mandatory 60-day buffer after any defined freeze period to prevent freezing the device indefinitely.

During a freeze period:

- Devices don't receive any notifications about pending OTA updates.
- Devices don't install any OTA updates to the OS.
- Device users aren't able to manually check for OTA updates in Settings.

To set a freeze period, call[`SystemUpdatePolicy.setFreezePeriods()`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#setFreezePeriods(java.util.List%3Candroid.util.Pair%3Cjava.lang.Integer,%20java.lang.Integer%3E%3E)). Because the freeze period repeats annually, the start and end dates of the period are represented by integers counting the number of days since year start. The start day must begin at least 60 days after the end of any previous freeze period. Device owners can call[`SystemUpdatePolicy.getFreezePeriods()`](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy#getFreezePeriods())to get a list of freeze periods previously set on the system update policy object.[`DevicePolicyManager.getSystemUpdatePolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getSystemUpdatePolicy())has been updated to return any freeze periods set by the device owner.

## Restrict sharing into a work profile

Profile owners can prevent users from sharing personal data into a work profile on the device by adding the user restriction[`DISALLOW_SHARE_INTO_MANAGED_PROFILE`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SHARE_INTO_MANAGED_PROFILE). This restriction prevents the following intent handling and sharing:

- Personal profile apps sharing data and files with work profile apps.
- Work profile apps picking items from the personal profile---for example, pictures or files.

After setting this restriction, your DPC can still permit cross-profile Activity intents by calling[`addCrossProfileIntentFilter()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#addCrossProfileIntentFilter(android.content.ComponentName,%20android.content.IntentFilter,%20int)).

## Hardware-secured keys and machine certificates

Android 9 adds APIs to help you work with keys and certificates that you can combine to securely identify devices. A DPC running in profile owner or device owner modes, or a[delegated certificate installer](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_CERT_INSTALL), can complete the following tasks:

- Generate keys and certificates in the secure hardware (such as a trusted execution environment (TEE) or Secure Element (SE)) of the Android device. The generated keys never leave the secure hardware and can be used from the[Android KeyChain](https://developer.android.com/reference/android/security/KeyChain). Call[`DevicePolicyManager.generateKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#generateKeyPair(android.content.ComponentName,%20java.lang.String,%20android.security.keystore.KeyGenParameterSpec,%20int))supplying the algorithm (see[`KeyPairGenerator`](https://developer.android.com/reference/java/security/KeyPairGenerator)) and any hardware IDs you want attested, such as the serial number or IMEI. To learn more about secure hardware changes, see the[Android 9 Security enhancements](https://developer.android.com/about/versions/pie/android-9.0#security).
- Associate a certificate with an existing device-generated key. Call[`DevicePolicyManager.setKeyPairCertificate()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyPairCertificate(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.security.cert.Certificate%3E,%20boolean))supplying the alias of the existing key and the certificate chain---starting with the leaf certificate and including the chain of trust in order.
- Confirm that the secure hardware protects the key before using it. To check which mechanisms protect the key, follow the steps in[Key Attestation](https://developer.android.com/training/articles/security-key-attestation).
- Device owners and delegated certificate installers can receive a signed statement of the devices' hardware IDs with Android system versions. Call[`DevicePolicyManager.generateKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#generateKeyPair(android.content.ComponentName,%20java.lang.String,%20android.security.keystore.KeyGenParameterSpec,%20int))passing one or more of[`ID_TYPE_BASE_INFO`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_BASE_INFO),[`ID_TYPE_SERIAL`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_SERIAL),[`ID_TYPE_IMEI`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI), or[`ID_TYPE_MEID`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_MEID)in the`idAttestationFlags`argument. The returned certificate includes the hardware IDs in the attestation record. If you don't want the hardware IDs included, pass`0`. Profile owners can only receive manufacturer information (by passing`ID_TYPE_BASE_INFO`). To check that the device can attest IDs, call[`isDeviceIdAttestationSupported()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isDeviceIdAttestationSupported()).
- Prevent device users from misusing enterprise keys (in non-enterprise tasks) by making the key certificates unselectable. The system doesn't include unselectable certificates in the picker panel. In your[`DeviceAdminReceiver.onChoosePrivateKeyAlias()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onChoosePrivateKeyAlias(android.content.Context,%20android.content.Intent,%20int,%20android.net.Uri,%20java.lang.String))callback method, return the alias to your enterprise key so that the system automatically selects the certificate on behalf of the user. To make a key unselectable, call the following`DevicePolicyManager`methods:
  - [`setKeyPairCertificate()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyPairCertificate(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.security.cert.Certificate%3E,%20boolean))and pass`false`for the`isUserSelectable`argument.
  - [`installKeyPair (ComponentName, PrivateKey, Certificate[], String, int)`](https://developer.android.com/work/versions/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName,%20java.security.PrivateKey,%20java.security.cert.Certificate%5B%5D,%20java.lang.String,%20boolean,%20int))and omit[`INSTALLKEY_SET_USER_SELECTABLE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#INSTALLKEY_SET_USER_SELECTABLE)from the`flags`argument.

By combining these APIs, enterprises can securely identify devices and confirm their integrity before providing access:

1. The Android device generates a new private key in the secure hardware. Because the private key never leaves the secure hardware, it remains secret.
2. The device uses the key to create and send a certificate signing request (CSR) to the server. The CSR includes the attestation record containing the device IDs.
3. The server validates the certificate chain (rooted to a Google certificate) and extracts the device metadata from the attestation record.
4. The server confirms that the secure hardware protects the private key and that the device IDs match the enterprise's records. The server can also check that the Android system and patch versions meet any requirements.
5. The server generates a certificate from the CSR and sends the certificate to the device.
6. The device pairs the certificate with the private key (that's remained in the secure hardware) enabling apps to connect to enterprise services.

## More security APIs, features, and changes

### IDs for security logs and network logs

Android 9 includes IDs in security and network activity logs. The numeric ID monotonically increases for each event, making it easier for IT admins to spot gaps in their logs. Because security logs and network logs are separate collections, the system maintains separate ID values.

Call[`SecurityEvent.getId()`](https://developer.android.com/reference/android/app/admin/SecurityLog.SecurityEvent#getId()),[`DnsEvent.getId()`](https://developer.android.com/reference/android/app/admin/NetworkEvent#getId()), or[`ConnectEvent.getId()`](https://developer.android.com/reference/android/app/admin/NetworkEvent#getId())to get the ID value. The system resets the ID whenever a DPC enables logging or when the device restarts. Security logs fetched by calling[`DevicePolicyManager.retrievePreRebootSecurityLogs()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrievePreRebootSecurityLogs(android.content.ComponentName))don't include these IDs.

### Security logging

Security logging assigns each`SecurityEvent`a log level. To get the log level, call[`getLogLevel()`](https://developer.android.com/reference/android/app/admin/SecurityLog.SecurityEvent#getLogLevel()). This method returns a log level value that can be one of:[`LEVEL_INFO`](https://developer.android.com/reference/android/app/admin/SecurityLog#LEVEL_INFO),[`LEVEL_WARNING`](https://developer.android.com/reference/android/app/admin/SecurityLog#LEVEL_WARNING), or[`LEVEL_ERROR`](https://developer.android.com/reference/android/app/admin/SecurityLog#LEVEL_ERROR).

Android 9 logs the events listed in the table below into[security logs](https://developer.android.com/work/dpc/security#log_enterprise_device_activity). To check an event's tag, call[`getTag()`](https://developer.android.com/reference/android/app/admin/SecurityLog.SecurityEvent#getTag()). To retrieve the event data, call[`getData()`](https://developer.android.com/reference/android/app/admin/SecurityLog.SecurityEvent#getData()).

|                                                                       Tag                                                                        |                                    Event description                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [`TAG_CERT_AUTHORITY_INSTALLED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_CERT_AUTHORITY_INSTALLED)             | An attempt to install a new root certificate into the system's credential storage.       |
| [`TAG_CERT_AUTHORITY_REMOVED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_CERT_AUTHORITY_REMOVED)                 | An attempt to remove a root certificate from the system's credential storage.            |
| [`TAG_CERT_VALIDATION_FAILURE`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_CERT_VALIDATION_FAILURE)               | A Wi-Fi certificate failed a validation check during connection.                         |
| [`TAG_CRYPTO_SELF_TEST_COMPLETED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_CRYPTO_SELF_TEST_COMPLETED)         | The system completed the cryptographic self test.                                        |
| [`TAG_KEYGUARD_DISABLED_FEATURES_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_KEYGUARD_DISABLED_FEATURES_SET) | An admin app disabled features of a device or work profile lock screen.                  |
| [`TAG_KEY_DESTRUCTION`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_KEY_DESTRUCTION)                               | An attempt to delete a cryptographic key.                                                |
| [`TAG_KEY_GENERATED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_KEY_GENERATED)                                   | An attempt to generate a new cryptographic key.                                          |
| [`TAG_KEY_IMPORT`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_KEY_IMPORT)                                         | An attempt to import a new cryptographic key.                                            |
| [`TAG_KEY_INTEGRITY_VIOLATION`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_KEY_INTEGRITY_VIOLATION)               | Android detected a damaged encryption or authentication key.                             |
| [`TAG_LOGGING_STARTED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_LOGGING_STARTED)                               | Security logging started recording.                                                      |
| [`TAG_LOGGING_STOPPED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_LOGGING_STOPPED)                               | Security logging stopped recording.                                                      |
| [`TAG_LOG_BUFFER_SIZE_CRITICAL`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_LOG_BUFFER_SIZE_CRITICAL)             | The security log buffer reached 90% of its capacity.                                     |
| [`TAG_MAX_PASSWORD_ATTEMPTS_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_MAX_PASSWORD_ATTEMPTS_SET)           | An admin app set the number of allowed incorrect-password attempts.                      |
| [`TAG_MAX_SCREEN_LOCK_TIMEOUT_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_MAX_SCREEN_LOCK_TIMEOUT_SET)       | An admin app set a maximum screen-lock timeout.                                          |
| [`TAG_MEDIA_MOUNT`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_MEDIA_MOUNT)                                       | The device mounted removable storage media.                                              |
| [`TAG_MEDIA_UNMOUNT`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_MEDIA_UNMOUNT)                                   | The device unmounted removable storage media.                                            |
| [`TAG_OS_SHUTDOWN`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_OS_SHUTDOWN)                                       | The Android system shut down.                                                            |
| [`TAG_OS_STARTUP`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_OS_STARTUP)                                         | The Android system started up.                                                           |
| [`TAG_PASSWORD_COMPLEXITY_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_PASSWORD_COMPLEXITY_SET)               | An admin app set password complexity requirements.                                       |
| [`TAG_PASSWORD_EXPIRATION_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_PASSWORD_EXPIRATION_SET)               | An admin app set a password expiry duration.                                             |
| [`TAG_PASSWORD_HISTORY_LENGTH_SET`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_PASSWORD_HISTORY_LENGTH_SET)       | An admin app set a password history length, preventing users from reusing old passwords. |
| [`TAG_REMOTE_LOCK`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_REMOTE_LOCK)                                       | An admin app locked the device or work profile.                                          |
| [`TAG_USER_RESTRICTION_ADDED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_USER_RESTRICTION_ADDED)                 | An admin app set a user restriction.                                                     |
| [`TAG_USER_RESTRICTION_REMOVED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_USER_RESTRICTION_REMOVED)             | An admin app removed a user restriction.                                                 |
| [`TAG_WIPE_FAILURE`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_WIPE_FAILURE)                                     | An attempt to wipe a device or work profile failed.                                      |

### Work profile lock screen challenge

Beginning in Android 9, profile owners can require users to set a separate lock screen challenge for their work profile using the[`DISALLOW_UNIFIED_PASSWORD`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_UNIFIED_PASSWORD)user restriction. To check whether a user has the same lock screen challenge set for their device and work profile, call[`DevicePolicyManager.isUsingUnifiedPassword()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isUsingUnifiedPassword(android.content.ComponentName)).

If a device has a separate work profile lock screen,[`DevicePolicyManager.setMaximumTimeToLock()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setMaximumTimeToLock(android.content.ComponentName,%20long))only sets a lock screen timeout for the work profile instead of for the entire device.

### Developer tools access

To help keep work data in the work profile, the Android Debug Bridge (adb) tool can't access directories and files in the work profile.

### Support for more biometric options

Android 9 adds fine-grained control over biometric hardware authentication in a work profile's lock screen. Call the existing[`DevicePolicyManager.setKeyguardDisabledFeatures()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyguardDisabledFeatures(android.content.ComponentName,%20int))method with[`KEYGUARD_DISABLE_FACE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_FACE)and[`KEYGUARD_DISABLE_IRIS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_IRIS). To disable all biometric authentication methods provided by the device, add[`KEYGUARD_DISABLE_BIOMETRICS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#KEYGUARD_DISABLE_BIOMETRICS).

## Deprecation of device admin policies

Android 9 marks the policies listed below as deprecated for DPCs using[device admin](https://developer.android.com/work/device-admin). The policies continue to function in Android 9 as they have done previously. Starting with the Android 10 release, the same policies will throw a SecurityException when invoked by a device admin.

- [`USES_POLICY_DISABLE_CAMERA`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_DISABLE_CAMERA)
- [`USES_POLICY_DISABLE_KEYGUARD_FEATURES`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_DISABLE_KEYGUARD_FEATURES)
- [`USES_POLICY_EXPIRE_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_EXPIRE_PASSWORD)
- [`USES_POLICY_LIMIT_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_LIMIT_PASSWORD)

Some applications use device admin for consumer device administration. For example, locking and wiping a lost device. The following policies will continue to be available to enable this:

- [`USES_POLICY_WIPE_DATA`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_WIPE_DATA)
- [`USES_POLICY_FORCE_LOCK`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_FORCE_LOCK)
- [`USES_POLICY_RESET_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_RESET_PASSWORD)

For more information about these changes, read[Device admin deprecation](https://developers.google.com/android/work/device-admin-deprecation).

## Streamlined QR-code enrollment

### Built-in QR library

Android 9 comes bundled with a QR library to streamline QR-code device provisioning. IT admins no longer have to manually enter Wi-Fi details to set up a device. Instead, with Android 9 it's possible to include these Wi-Fi details within a QR code. When an IT admin scans the QR code with a company-owned device, the device automatically connects to Wi-Fi and enters the provisioning process without any additional manual input.

The QR-code provisioning method supports the following provisioning extras to specify Wi-Fi details:

- [`EXTRA_PROVISIONING_WIFI_HIDDEN`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_HIDDEN)
- [`EXTRA_PROVISIONING_WIFI_PAC_URL`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PAC_URL)
- [`EXTRA_PROVISIONING_WIFI_PASSWORD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PASSWORD)
- [`EXTRA_PROVISIONING_WIFI_PROXY_BYPASS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PROXY_BYPASS)
- [`EXTRA_PROVISIONING_WIFI_PROXY_HOST`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PROXY_HOST)
- [`EXTRA_PROVISIONING_WIFI_PROXY_PORT`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PROXY_PORT)
- [`EXTRA_PROVISIONING_WIFI_SECURITY_TYPE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_SECURITY_TYPE)
- [`EXTRA_PROVISIONING_WIFI_SSID`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_SSID)

### Set date and timezone using provisioning extras

The QR-code provisioning method supports provisioning extras to set the time and timezone on a device:

- [`EXTRA_PROVISIONING_TIME_ZONE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_TIME_ZONE)
- [`EXTRA_PROVISIONING_LOCAL_TIME`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_LOCAL_TIME)
- [`EXTRA_PROVISIONING_LOCALE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_LOCALE)

## Wiping data options

Device admins can show a personalized message to users when removing a work profile or secondary user. The message helps device users understand that their IT admin removed the work profile or secondary user. Call[`wipeData(int, CharSequence)`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int,%20java.lang.CharSequence))and supply a short explanatory message. When called by the primary user or device owner, the system doesn't show a message and begins a factory reset of the device.

To remove subscription data from an embedded eUICC SIM, call[`wipeData()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int,%20java.lang.CharSequence))and include[`WIPE_EUICC`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#WIPE_EUICC)in the`flags`argument.

## Methods for affiliated profile owners

The following methods are available to[affiliated profile](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users)owners:

- [`DevicePolicyManager.setKeyguardDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyguardDisabled(android.content.ComponentName,%20boolean))
- [`DevicePolicyManager.setStatusBarDisabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setStatusBarDisabled(android.content.ComponentName,%20boolean))
- [`PackageInstaller.createSession()`](https://developer.android.com/reference/android/content/pm/PackageInstaller#createSession(android.content.pm.PackageInstaller.SessionParams))