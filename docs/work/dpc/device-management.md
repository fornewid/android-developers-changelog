---
title: https://developer.android.com/work/dpc/device-management
url: https://developer.android.com/work/dpc/device-management
source: md.txt
---

# Device control

The features in this guide describe device management capabilities you can implement in your[device policy controller](https://developer.android.com/work/dpc/build-dpc)(DPC) app. You can also use the[TestDPC](https://github.com/googlesamples/android-testdpc/)app as a source of sample code for Android's enterprise features.

A DPC app can run in profile owner mode on personal devices or in device owner mode on fully managed devices. This table indicates which features are available when the DPC runs in[profile owner mode or device owner mode](https://developers.google.com/android/work/play/emm-api/prov-devices#modes_of_operation):

|                                                                                 **Feature**                                                                                 | **Profile owner** | **Device owner** |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|
| [Create a custom lock screen message](https://developer.android.com/work/dpc/device-management#create_a_custom_lock_screen_message)                                         |                   | ✓                |
| [Disable data roaming](https://developer.android.com/work/dpc/device-management#disable_data_roaming)                                                                       |                   | ✓                |
| [Give users a customized message if a setting is blocked](https://developer.android.com/work/dpc/device-management#give_users_a_customized_message_if_a_setting_is_blocked) | ✓                 | ✓                |
| [Lock down the wallpaper](https://developer.android.com/work/dpc/device-management#lock_down_the_wallpaper)                                                                 | ✓                 | ✓                |
| [Lock down a customer user icon](https://developer.android.com/work/dpc/device-management#lock_down_a_customer_user_icon)                                                   | ✓                 | ✓                |
| [Remotely monitor device health and status](https://developer.android.com/work/dpc/device-management#remotely_monitor_device_health_and_status)                             | ✓                 | ✓                |
| [Remotely reboot an Android device](https://developer.android.com/work/dpc/device-management#remotely_reboot_an_android_device)                                             |                   | ✓                |
| [Prevent users sending files over Bluetooth](https://developer.android.com/work/dpc/device-management#prevent_users_sending_files_over_bluetooth)                           | ✓                 | ✓                |

## Create a custom lock screen message

Running in device owner mode, a DPC can create a custom lock screen message on their users' devices using the[`setDeviceOwnerLockScreenInfo`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setDeviceOwnerLockScreenInfo(android.content.ComponentName,%20java.lang.CharSequence))method. This message displays on the device screen when locked, and is useful for a lost or stolen device. A common message is "This phone belongs to*`<company name>`* , call*`<phone number>`*if found."

## Disable data roaming

Data roaming can cause significant charges on Mobile carrier bills. To help streamline those costs, a DPC running in device owner mode can disable data roaming by setting the[`DISALLOW_DATA ROAMING`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_DATA_ROAMING)restriction. Once the user restriction is set by the DPC, a user can't change data roaming using**Settings**on their device.

## Give users a customized message if a setting is blocked

When a user clicks a setting or feature blocked by their IT department, the support message gives a brief explanation of why they can't access the feature.

These messages can be more descriptive than "Action not allowed". A DPC running in device owner or profile owner mode can customize these messages using the[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)[`setShortSupportMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setShortSupportMessage(android.content.ComponentName,%20java.lang.CharSequence))and[`setLongSupportMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLongSupportMessage(android.content.ComponentName,%20java.lang.CharSequence))methods.

### Create support messages

To explain why a setting is restricted, you can use short or long messages:

- **To create a short message** , use the[`setShortSupportMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setShortSupportMessage(android.content.ComponentName,%20java.lang.CharSequence))method.

  - The short message is restricted to 200 characters.
  - A common message is "This setting is disabled by your admin. Contact*'[yourITdepartment@example.com](mailto:yourITdepartment@example.com)'*for support."
- **To create a long message** , use the[`setLongSupportMessage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLongSupportMessage(android.content.ComponentName,%20java.lang.CharSequence))method. The user can view this message on their device under**Settings** \>**Security** \>**Device admins**, and then select a specific admin.

If either of these messages needs to be translated, the[`DeviceAdminReceiver`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)needs to listen to the[`ACTION_LOCALE_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_LOCALE_CHANGED)broadcast and set a new version of this string accordingly.

## Lock down the wallpaper

Organizations such as schools or companies that run Android devices as shared devices can block their users from changing the wallpaper on their device home screen.

To lock down the wallpaper, a DPC running in device owner or profile owner mode can set[`DISALLOW_SET_WALLPAPER`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SET_WALLPAPER)to`true`. The default for this setting is`false`.

## Lock down a customer user icon

A DPC running in either device owner or profile owner mode can add users and specify an icon for each user. This user icon is only on the device and is separate from the profile icon that appears in other Google properties, such as a Gmail message or Google Plus profile.

A DPC can configure the[`DISALLOW_SET_USER_ICON`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SET_USER_ICON)to`true`to restrict a user from changing their icon. The default for this setting is`false`.

## Remotely monitor device health and status

A DPC running in device owner or profile owner mode can monitor unattended devices running in a remote location, such as digital signage displays or kiosks run off of Android devices. To do this, a DPC uses the[`HardwarePropertiesManager`](https://developer.android.com/reference/android/os/HardwarePropertiesManager)interface to get information about device health, such as GPU temperatures and CPU usage. This is useful to diagnose issues with devices that automatically turn off because of overheating or other issues.

To access the device's Hardware Property Manager service, use[`Context.getSystemService()`](https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String))with string[`Context.HARDWARE_PROPERTIES_SERVICE`](https://developer.android.com/reference/android/content/Context#HARDWARE_PROPERTIES_SERVICE).
| **Note:** Not all properties monitored by[`HardwarePropertiesManager`](https://developer.android.com/reference/android/os/HardwarePropertiesManager)are available to all Android devices.

## Remotely reboot an Android device

A DPC can remotely reboot Android devices only when it runs in device owner mode. In some cases, devices deployed in public places inside enclosures or as digital signage displays can prevent easy access to the power button. If a device needs to be rebooted, a DPC can do so using the[`DevicePolicyManager.reboot()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#reboot(android.content.ComponentName))method.

A device doesn't reboot if there's an ongoing call. The device needs to be in an idle state to reboot. This is to prevent an admin interrupting a user's phone call with a reboot request. If the device is active, it throws an`IllegalStateException`until[`CALL_STATE_IDLE`](https://developer.android.com/reference/android/telephony/TelephonyManager#CALL_STATE_IDLE).

## Prevent users sending files over Bluetooth

Device owners and profile owners can prevent users from sending files over Bluetooth using[`DISALLOW_BLUETOOTH_SHARING`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_BLUETOOTH_SHARING). Receiving files isn't affected. When set by a device owner,`DISALLOW_BLUETOOTH_SHARING`applies to all users on the device.

This option allows the IT admins to control the behavior of[Quick Share](https://support.google.com/android/answer/9286773).