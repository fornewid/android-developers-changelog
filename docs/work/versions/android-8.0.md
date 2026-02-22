---
title: https://developer.android.com/work/versions/android-8.0
url: https://developer.android.com/work/versions/android-8.0
source: md.txt
---

# What&#39;s new in Android 8.0

This page provides an overview of the new APIs, features, and behavior changes introduced in Android 8.0 (API level 26) that affect Android in the enterprise.

## New APIs and features

We've made the profile owner and device owner management modes more powerful, productive, and easier to provision than ever before. We've also enabled a whole new deployment scenario---work profiles on fully managed devices. These and other features are described in the following sections.

### Work profiles on fully managed devices

In Android 8.0, fully managed devices can also have work profiles. This gives enterprises the ability to separate apps and policies while maintaining control and visibility across both profiles. The existing device owner, or a different device policy controller (DPC), can create the managed profile.

With work profiles on fully managed devices, device owners can:

- Create a managed profile without user interaction by calling[EXTRA_PROVISIONING_SKIP_USER_CONSENT](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_SKIP_USER_CONSENT).
- Receive notifications when secondary users or managed profiles are created or removed. The callbacks are[onUserAdded()](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserAdded(android.content.Context, android.content.Intent, android.os.UserHandle))and[onUserRemoved()](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserRemoved(android.content.Context, android.content.Intent, android.os.UserHandle)).
- Prevent other DPCs from creating managed profiles using[DISALLOW_ADD_MANAGED_PROFILE](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ADD_MANAGED_PROFILE). This setting is the default in Android 8.0 for device owners on newly provisioned devices or devices upgraded to Android 8.0.
- Device owners can also prevent users from removing existing managed profiles using[DISALLOW_REMOVE_MANAGED_PROFILE](https://developer.android.com/reference/android/os/UserManager#DISALLOW_REMOVE_MANAGED_PROFILE).

Device owners and profile owners can communicate with each other if they're from the same APK and the owners are affiliated (see[User affiliation](https://developer.android.com/work/versions/android-8.0#user-affiliation)below).

For more detailed information on supporting this new deployment scenario, see the dedicated page for[work profiles on fully managed devices](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users).

### User affiliation

When a device owner and a profile owner represent the same organization:

- The device and profile owners can communicate with each other within the same APK---they might want to share policies or status (see[Work profiles on fully managed devices](https://developer.android.com/work/versions/android-8.0#work-profile-on-managed-devices)above).

- Device-wide features, such as logging or allowlisting lock task mode, can apply to affiliated users.

Affiliation IDs, attached to a profile or user, identify organizations. When affiliation IDs match, the users become affiliated. Device owners and profile owners use[setAffiliationIds()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAffiliationIds(android.content.ComponentName,%20java.util.Set%3Cjava.lang.String%3E))to set their affiliation IDs. Represent organizations using long, difficult to guess, string IDs.

#### New access for affiliated users

If all the secondary users and profiles on a device are affiliated with the device owner, then the following features are available:

- Security logging using[setSecurityLoggingEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecurityLoggingEnabled(android.content.ComponentName, boolean)).
- Network activity logging using[setNetworkLoggingEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName, boolean)).
- Bug reporting using[requestBugreport()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#requestBugreport(android.content.ComponentName)).

Security logging and bug reporting were previously only available to single-user devices, or devices with only one profile and one user.

Lock task mode is available to secondary users and managed profiles when affiliated with the device owner through[setLockTaskPackages()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLockTaskPackages(android.content.ComponentName, java.lang.String[])). For more detailed information on user affiliation, see[Affiliated users](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users).

### Customized provisioning disclaimers

DPCs can now show their own disclaimers to users during provisioning. Use[EXTRA_PROVISIONING_DISCLAIMERS](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_DISCLAIMERS),[EXTRA_PROVISIONING_DISCLAIMER_HEADER](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_DISCLAIMER_HEADER), and[EXTRA_PROVISIONING_DISCLAIMER_CONTENT](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_DISCLAIMER_CONTENT)to supply styled text disclaimers. A DPC's custom disclaimers appear in the collapsible Terms list.

### Security

Profile owners and device owners can use[setRequiredStrongAuthTimeout()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setRequiredStrongAuthTimeout(android.content.ComponentName, long))to configure a timeout period for unlocking a device or a profile with a secondary authentication method, such as fingerprints or trust agents. After the timeout period expires, the user must unlock the device or profile using a strong authentication method, such as a password, PIN, or pattern.

Device owners and profile owners can securely reset device and work profile passwords using[resetPasswordWithToken()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPasswordWithToken(android.content.ComponentName, java.lang.String, byte[], int)). For devices that support[file-based encryption](https://source.android.com/security/encryption/file-based), this API is available before a user unlocks their device or profile, provided the DPC is encryption-aware.

When locking a work profile on a device that supports file-based encryption,[lockNow(int)](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#lockNow(int))can optionally evict the work profile's primary encryption keys using[FLAG_EVICT_CREDENTIAL_ENCRYPTION_KEY](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#FLAG_EVICT_CREDENTIAL_ENCRYPTION_KEY). The encryption keys are also evicted if the user turns their work profile off.

Also, device owners can use[setNetworkLoggingEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName, boolean))to turn on network logging of DNS queries and TCP connections initiated from corporate-owned devices. For more information, see[Network Activity Logging](https://developer.android.com/work/dpc/logging).

Profile owners can restrict which of the primary user's packages can observe work profile notifications. Call[`setPermittedCrossProfileNotificationListeners()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermittedCrossProfileNotificationListeners(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E))to set the allowlisted packages that receive events through a[NotificationListenerService](https://developer.android.com/reference/android/service/notification/NotificationListenerService). Setting the permitted listeners to`null`(the default) disables the allowlisting and all packages can listen for notifications. To limit events to system packages, pass an empty Set. To view apps that can't access work profile notifications, users can tap**Settings** \>**Apps \& notifications** \>**Special app access** \>**Notification access**.

Finally, profile owners and device owners can retrieve information about the pending system updates that are available on a device using[getPendingSystemUpdate()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPendingSystemUpdate(android.content.ComponentName)).

### App management API delegation

API delegation enables device owners and profile owners to fully offload app management to other applications. The[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class provides methods to manage the delegation scopes that device and profile owners can grant to a package:

- The[`setDelegatedScopes()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setDelegatedScopes(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.lang.String%3E))method allows device owners and profile owners to grant access to privileged APIs to other apps.
- The[getDelegatedScopes()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getDelegatedScopes(android.content.ComponentName, java.lang.String))method returns the scopes granted to a package.
- The[getDelegatePackages()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getDelegatePackages(android.content.ComponentName, java.lang.String))returns the packages that have a scope.

The following table shows how various methods in[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)are organized into the different scopes:

**Table 1.**Correspondence between scopes and device policy methods

|                                                                   Group                                                                    |                                                                                                                                                                                                                                                                                                                                                                    Methods                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DELEGATION_CERT_INSTALL](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_CERT_INSTALL)           | - [installKeyPair()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName, java.security.PrivateKey, java.security.cert.Certificate, java.lang.String)) - [removeKeyPair()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeKeyPair(android.content.ComponentName, java.lang.String)) - [installCaCert()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installCaCert(android.content.ComponentName, byte[])) - [uninstallCaCert()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#uninstallCaCert(android.content.ComponentName, byte[]))                           |
| [DELEGATION_APP_RESTRICTIONS](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_APP_RESTRICTIONS)   | - [getApplicationRestrictionsManagingPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getApplicationRestrictionsManagingPackage(android.content.ComponentName)) - [setApplicationRestrictionsManagingPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictionsManagingPackage(android.content.ComponentName, java.lang.String))                                                                                                                                                                                                                                                                                                             |
| [DELEGATION_BLOCK_UNINSTALL](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_BLOCK_UNINSTALL)     | [setUninstallBlocked()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUninstallBlocked(android.content.ComponentName, java.lang.String, boolean))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [DELEGATION_PERMISSION_GRANT](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_PERMISSION_GRANT)   | - [getPermissionPolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPermissionPolicy(android.content.ComponentName)) - [setPermissionPolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermissionPolicy(android.content.ComponentName, int)) - [getPermissionGrantState()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPermissionGrantState(android.content.ComponentName, java.lang.String, java.lang.String))                                                                                                                                                                                                          |
| [DELEGATION_PACKAGE_ACCESS](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_PACKAGE_ACCESS)       | - [isApplicationHidden()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isApplicationHidden(android.content.ComponentName, java.lang.String)) - [setApplicationHidden()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationHidden(android.content.ComponentName, java.lang.String, boolean)) - [isPackageSuspended()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isPackageSuspended(android.content.ComponentName, java.lang.String)) - [setPackagesSuspended()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPackagesSuspended(android.content.ComponentName, java.lang.String[], boolean)) |
| [DELEGATION_ENABLE_SYSTEM_APP](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_ENABLE_SYSTEM_APP) | [enableSystemApp()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#enableSystemApp(android.content.ComponentName, android.content.Intent))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Long-running background services

Device and profile owners can subclass[DeviceAdminService](https://developer.android.com/reference/android/app/admin/DeviceAdminService)to create background services. The Android system attempts to keep the service running while the user is running. If you want to run periodic tasks, consider using[JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler)before creating a background service.

### Controlling the backup service

Device owners can toggle the[Android Backup Service](https://developer.android.com/google/backup)using new methods in[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager). Enable and disable the backup service using[setBackupServiceEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setBackupServiceEnabled(android.content.ComponentName, boolean)). Check the backup service status using[isBackupServiceEnabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isBackupServiceEnabled(android.content.ComponentName)).

### Wi-Fi proxy configuration

Device owners and profile owners can configure HTTP proxy servers for Wi-Fi networks. Use a PAC file or manual settings to configure a proxy server for each Wi-Fi network. To set or remove the proxy for a[WifiConfiguration](https://developer.android.com/reference/android/net/wifi/WifiConfiguration), call its[setHttpProxy()](https://developer.android.com/reference/android/net/wifi/WifiConfiguration#setHttpProxy(android.net.ProxyInfo))method. To get the proxy settings call[getHttpProxy()](https://developer.android.com/reference/android/net/wifi/WifiConfiguration#getHttpProxy()).

### Explanation dialogs for admin-disabled features

Your app should show a useful explanation to users trying to use an admin-disabled feature. All apps can now use[createAdminSupportIntent()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#createAdminSupportIntent(java.lang.String))to create an intent that displays an explanation dialog when passed to[startActivity(Intent)](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)). Intents include customized, localized explanations for disabled cameras, disabled screen captures, and all the[UserManager](https://developer.android.com/reference/android/os/UserManager)restrictions.

### Restricting Bluetooth

Device owners can disable Bluetooth---affecting all users and profiles on the device. To turn off Bluetooth, add the user restriction[DISALLOW_BLUETOOTH](https://developer.android.com/reference/android/os/UserManager#DISALLOW_BLUETOOTH).

Device owners and profile owners can prevent users sending files over Bluetooth using[DISALLOW_BLUETOOTH_SHARING](https://developer.android.com/reference/android/os/UserManager#DISALLOW_BLUETOOTH_SHARING). Receiving files isn't affected. When set by a device owner,`DISALLOW_BLUETOOTH_SHARING`applies to all users on the device. This setting is the default in Android 8.0 for new profiles and existing profiles on devices upgraded to Android 8.0.

## Behavior changes

If you're building apps for businesses, including DPCs, you should review the following behavior changes in Android 8.0 and modify your app accordingly.

### Removing users

Device owners can remove secondary users and managed profiles using[removeUser()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeUser(android.content.ComponentName, android.os.UserHandle)), even if[DISALLOW_REMOVE_USER](https://developer.android.com/reference/android/os/UserManager#DISALLOW_REMOVE_USER)is enabled.

### Security

#### Authentication

The following changes have taken effect in the[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class:

- The[lockNow()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#lockNow())method only locks the work profile if a separate work challenge is active.
- The[resetPassword()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPassword(java.lang.String, int))method is no longer available to DPCs that act as device owners or profile owners and target Android 8.0. If called, a security exception is thrown. Instead, DPCs should use[resetPasswordWithToken()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPasswordWithToken(android.content.ComponentName, java.lang.String, byte[], int)).

  **Note:**DPCs targeting Android 7.1.1 (API level 25) or lower, as well as DPCs with only device admin privileges, aren't affected by this change.
- For devices that support file-based encryption,[isActivePasswordSufficient()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isActivePasswordSufficient())isn't available before the user unlocks the device for the first time after a reboot. If called before the user unlocks the device, an exception is thrown.

#### Data from locked work profiles

Android 8.0 includes user interface changes to separate data from a locked work profile.

- Notifications for apps in the work profile might now hide their content. Previously, the notification drawer showed the content for work apps from a locked work profile.
- The[Recents](https://developer.android.com/guide/components/activities/recents)screen now shows a plain panel for running apps from a locked work profile. The plain, color-keyed panel contains an app's icon and name. Previously, activities or tasks from a locked work profile showed a preview in the Recents screen.

#### Device integrity

- The[ENSURE_VERIFY_APPS](https://developer.android.com/reference/android/os/UserManager#ENSURE_VERIFY_APPS)flag is now a global user restriction. If any user on the device has this restriction, app verification is enforced across all users on the device. For example, if a profile owner sets the restriction on the work profile, app verification is enforced on the user's personal profile.
- The[onSystemUpdatePending()](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onSystemUpdatePending(android.content.Context, android.content.Intent, long))method is now invoked for profile owners in addition to device owners.
- When using the[SystemUpdatePolicy](https://developer.android.com/reference/android/app/admin/SystemUpdatePolicy)class, the postpone policy no longer applies to security patches, so security patches can no longer be postponed. The behavior of other policy types, such as automatic and windowed, aren't affected, however.
- Device owners can trigger a factory reset using[wipeData()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int)), even if[DISALLOW_FACTORY_RESET](https://developer.android.com/reference/android/os/UserManager#DISALLOW_FACTORY_RESET)is enabled.

### Always-on VPN

Android 8.0 includes user interface changes to help users understand the status of always-on VPN connections:

- When always-on VPN connections disconnect or can't connect, users see a non-dismissible notification. Tapping the notification shows the VPN configuration settings. The notification disappears when the VPN reconnects or the user turns off the always-on VPN option.
- Always-on VPN allows the person using a device to block any network connections that don't use the VPN. When turning this option on, the Settings app warns the user that they won't have an internet connection until the VPN connects. Settings prompts the user to continue or cancel.

The[VpnService](https://developer.android.com/reference/android/net/VpnService)of VPN apps must now call its[startForeground()](https://developer.android.com/reference/android/app/Service#startForeground(int, android.app.Notification))method after launch. Because the Android system starts a VPN app's service directly, transitioning to the foreground is the app's responsibility. Android 8.0 shuts down VPN apps that don't transition the VPN service to the foreground.

### Password callbacks

The password change callbacks of[DeviceAdminReceiver](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)now include a`user`parameter to identify the user or profile the password belongs to. The new method signatures are:

- [onPasswordChanged(Context, Intent, UserHandle)](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onPasswordChanged(android.content.Context, android.content.Intent, android.os.UserHandle))
- [onPasswordExpiring(Context, Intent, UserHandle)](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onPasswordExpiring(android.content.Context, android.content.Intent, android.os.UserHandle))
- [onPasswordFailed(Context, Intent, UserHandle)](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onPasswordFailed(android.content.Context, android.content.Intent, android.os.UserHandle))
- [onPasswordSucceeded(Context, Intent, UserHandle)](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onPasswordSucceeded(android.content.Context, android.content.Intent, android.os.UserHandle))

The default implementation of each new method calls the previous version---dropping the user argument. Android 8.0 deprecates the previous methods.

### App management API delegation

The following methods in the[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class are now deprecated:

- [setCertInstallerPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCertInstallerPackage(android.content.ComponentName, java.lang.String))
- [getCertInstallerPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCertInstallerPackage(android.content.ComponentName))
- [setApplicationRestrictionsManagingPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictionsManagingPackage(android.content.ComponentName, java.lang.String))
- [getApplicationRestrictionsManagingPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getApplicationRestrictionsManagingPackage(android.content.ComponentName))

Also, it's now possible to delegate a single scope to multiple packages. In other words, device owners and profile owners can grant two different packages access to the same set of APIs simultaneously.