---
title: https://developer.android.com/work/versions/android-7.0
url: https://developer.android.com/work/versions/android-7.0
source: md.txt
---

# What&#39;s new in Android 7.0

This page provides an overview of the new APIs, features, and behavior changes introduced in Android 7.0 (API level 25) that affect Android in the enterprise.

## QR code provisioning

Android enterprise now supports using QR codes to provision corporate-liable devices. The setup wizard now allows you to scan a QR code to provision the device.

## Work profile security challenge

Profile owners can require users to specify a security challenge for apps running in the work profile. The system shows the security challenge when the user attempts to open any work apps. If the user successfully completes the security challenge, the system unlocks the work profile and decrypts it if necessary.

If a profile owner sends an[`ACTION_SET_NEW_PASSWORD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_SET_NEW_PASSWORD)intent, the system prompts a user to set up a security challenge. The profile owner can also send an`ACTION_SET_NEW_PARENT_PROFILE_PASSWORD`intent to prompt the user to set a device lock.

Profile owners can choose to set the password policies for the work challenge differently from the policies for other device passwords. For example, the minimum length for the device challenge response can be different from the length required for other passwords. Profile owners set the challenge policies using the usual[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)methods, such as[`setPasswordQuality()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordQuality(android.content.ComponentName,%20int))and[`setPasswordMinimumLength()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordMinimumLength(android.content.ComponentName,%20int)). The profile owner can also set the device lock, by using the[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)instance returned by the new`DevicePolicyManager.getParentProfileInstance()`method. Additionally, profile owners can customize the credentials screen for the work challenge by using the[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class's new`setOrganizationColor()`and`setOrganizationName()`methods.

## Disable access to apps

Device owners and profile owners can temporarily suspend access to packages by calling the new`DevicePolicyManager.getPackagesSuspended()`method. Owners can use the same method to re-enable those packages.

While a package is suspended, it cannot start activities, notifications to the package are suppressed, and the app's entry in the[overview](https://developer.android.com/guide/components/activities/recents)screen is hidden. Suspended packages do not show in the[overview](https://developer.android.com/guide/components/activities/recents)screen, and they cannot show dialogs (including toasts and snackbars). They also cannot play audio or vibrate the device.

Launchers should apply a distinctive UI to suspended apps to show that the apps aren't currently available; for example, they might render the app icon in gray. Launchers can find out which apps are suspended by calling the new`DevicePolicyManager.getPackagesSuspended()`method.

## Toggle work mode

On dual-profile devices, users can toggle work mode on and off. While work mode is turned off, the managed profile is temporarily shut down. Work profile apps, background sync, and notifications are all disabled, including the profile owner app. While the work profile is disabled, the system displays a persistent status icon to remind users that they can't launch work apps. The system launcher indicates that work apps and widgets are not accessible.

## Always-on VPN

Device owners and profile owners can require that work apps always connect to the network through a specified VPN. If owners set this requirement, the device automatically starts that VPN at boot time.

Owners can require use of a VPN by calling the new`DevicePolicyManager.setAlwaysOnVpnPackage()`method. To find out if the owner has set a VPN requirement, call the`newDevicePolicyManager.GetAlwaysOnVpnPackage()`method.

Because the system can directly bind VPN services without app interaction, VPN clients need to handle new entry points for always-on VPN. As before, you can find active services by using an intent filter that matches the action[`android.net.VpnService`](https://developer.android.com/reference/android/net/VpnService).

Users can manually set an always-on VPN client that implements[`VpnService`](https://developer.android.com/reference/android/net/VpnService)by using the**Settings** \>**More** \>**VPN screen**.

## Contacts integration with work profile

Profile owners can allow local search and directory lookup of work contacts from the primary user. For example, a user can access both personal and work directory contacts from their personal dialer or contacts application (if permitted by their profile administrator).

Developers that leverage the Contact Provider can use the Enterprise Contacts API to access work profile directory entries from the primary user if allowed by policy:

- `ContactsContract.Contacts.ENTERPRISE_CONTENT_FILTER_URI`
- `ContactsContract.Phone.ENTERPRISE_CONTENT_FILTER_URI`
- `ContactsContract.Email.ENTERPRISE_CONTENT_FILTER_URI`
- `ContactsContract.Callable.ENTERPRISE_CONTENT_FILTER_URI`
- `ContactsContract.Directory.ENTERPRISE_CONTENT_URI`
- `ContactsContract.Directory.isEnterpriseDirectoryId()`

Profile owners can control the visibility of work contacts in the primary user using the following new methods:

- `DevicePolicyManager.setCrossProfileContactsSearchDisabled()`
- `DevicePolicyManager.getCrossProfileContactsSearchDisabled()`

## Remote reboot

Device owners can remotely reboot devices. In some cases, devices deployed in public places inside enclosures can prevent access to the power button. If a device needs to be rebooted, administrators can do so using the new`DevicePolicyManager.reboot()`method.

## Location off switch

Users can disable location permissions for work apps while continuing to access location information in their personal apps. A separate location access switch in Location Settings allows users to deny location updates or last-location queries for apps running in the work profile.

The top level location off switch disables location access for both the primary profile and the managed profile.

## Customized provisioning

An application can customize the profile owner and device owner provisioning flows with corporate colors and logos.

- `DevicePolicyManager.EXTRA_PROVISIONING_MAIN_COLOR`: Customizes flow color.
- `DevicePolicyManager.EXTRA_PROVISIONING_LOGO_URI`: Customizes the flow with a corporate logo.

## Multiple Wi-Fi CA certificates

Profile owners and device owners can set multiple CA certificates for a given Wi-Fi configuration. When corporate Wi-Fi networks have separate CAs for separate access points with the same SSID, IT administrators can include all relevant CAs in the Wi-Fi configuration using the new method`setCaCertificates()`.

APIs added are:

- `WifiEnterpriseConfig.setCaCertificates()`
- `WifiEnterpriseConfig.getCaCertificates()`

## Customized lock screen message

Device owners can provide owner information to be shown on the lockscreen. This information takes precedence the user lock screen message (if one is set). New[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)methods are:

- `setDeviceOwnerLockScreenInfo()`
- `getDeviceOwnerLockScreenInfo()`

## Work profile connection service

Profile owners can specify a work dialer application that uses a work-specific[`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService)for the calling backend (calling accounts). The work dialer maintains a work-only call log and relies on work contacts only. Users have a consistent in-call UI experience regardless of dialing application. Incoming work calls to the work calling accounts are distinguished from personal incoming calls to the personal calling accounts.

The dialer should check for the new flag`android.telecom.Call.PROPERTY_WORK_CALL`to determine if a call is a work call. If a call is a work call, the dialer should indicate this, such as by adding a work badge.

## Lock down wallpaper

A new user restriction (`DISALLOW_SET_WALLPAPER`) prevents the user from changing their wallpaper. The device owner or profile owner can still change the wallpaper, but they can only change the wallpaper for the user or profile they control. For example, a profile owner can't change the wallpaper of the parent user, but a profile owner in the primary profile or device owner can. A profile owner or device owner that wants to change the wallpaper should check whether the user or profile they manage has a wallpaper ([`isWallpaperSupported()`](https://developer.android.com/reference/android/app/WallpaperManager#isWallpaperSupported())) and whether they are allowed to change it (with the new method`WallpaperManager.isWallpaperSettingAllowed()`).

## Lock down user icon

A new user restriction (`DISALLOW_SET_USER_ICON`) prevents the user from changing their user icon. The user's device owner or profile owner can still change the icon. However, a profile owner can only change the user icon for the profile it controls.

## Device health monitoring

A device owner or profile owner can use the new`HardwarePropertiesManager`interface to retrieve information about device health, such as CPU or GPU temperatures and CPU usage. The new monitoring interface is especially useful for monitoring unattended devices running in a remote location.