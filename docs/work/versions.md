---
title: What's new for Android in the enterprise  |  Android Enterprise  |  Android Developers
url: https://developer.android.com/work/versions
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Enterprise](https://developer.android.com/work)

# What's new for Android in the enterprise Stay organized with collections Save and categorize content based on your preferences.



Each new version of Android includes a range of new features and improvements
designed for Android in the enterprise. Whether you're developing a [device
policy controller](https://developers.google.com/android/work/build-dpc) or apps for [managed Google Play](/distribute/google-play/work), you can refer to
this section to review the new APIs, features, and behavior changes introduced
in each version of Android.

## Android 16

Some of the new enterprise [features and updates in Android 16](/work/versions/android-16) include the
ability to:

* Block the use of Thread networks.
* Enable or disable the NFC controller on the device.
* Set the [`AppFunctionManager`](/reference/android/app/appfunctions/AppFunctionManager) policy.
* Streamline the enterprise setup flow.
* Control whether time and time zone should be obtained automatically from the
  network.

## Android 15

Some of the new enterprise [features and updates in Android 15](/work/versions/android-15) include:

* **Enhanced employee and device protection**
  + Android theft protection
  + Private space for personal profile
  + NIAP compliance maintenance
* **Stronger management of company-owned devices**
  + Simplify eSIM management on managed devices
  + Controls for Circle to Search on Android Work Profile
  + Additional customization for corporate-owned devices

## Android 14

Some of the new enterprise features and updates in Android 14 include:

* Enhanced PIN security with 6-digit PIN as the default length.
* Allow or disallow an approved credential manager in work profile and fully
  managed devices.
* Protect devices from 2G-based threats by disabling 2G connectivity.
* Swipe sideways to quickly switch profiles in Google apps.
* Save screenshots from work apps to your work profile.
* Choose which apps to share when screen sharing while respecting admin
  controls.
* Enable or disable [ultra-wide band (UWB)](/about/versions/14/work#uwb) to comply with National
  Information Assurance Partnership (NIAP).
* Seamless and secure cross-profile experiences which include:
  + [Cross-profile access to contacts](/about/versions/14/work#cross-profile-access)
  + [Cross-profile caller ID searches](/about/versions/14/work#cross-profile)
* [Two contact fields](/work/versions/android-14#contacts):
  + [`ContactsContract.Contacts#ENTERPRISE_CONTENT_URI`](/reference/android/provider/ContactsContract.Contacts#ENTERPRISE_CONTENT_URI)
  + [`ContactsContract.CommonDataKinds.Phone#ENTERPRISE_CONTENT_URI`](/reference/android/provider/ContactsContract.CommonDataKinds.Phone#ENTERPRISE_CONTENT_URI)
* [Headless Device Owner mode](/work/device-admin#headless-mode)
* [Some notable API deprecations](/about/versions/14/work#deprecations)

## Android 13

Some of the new enterprise features and updates in Android 13 include:

* Work apps can access NFC and can be set as default payment for business
  expenses among other use cases.
* View the device's security and privacy settings of both profiles in one
  page.
* New [security logs](/work/versions/android-13#security-logs) to comply with the NIAP's requirements.
* Place a company-owned device in [Lost Mode](https://support.google.com/work/android/answer/13581513) to lock and locate it.
* In Android 13 (API level 33) and higher, [internet connectivity is required
  by default to provision company-owned devices](/work/versions/android-13#behavior-changes).
* [`android.app.extra.PROVISIONING_LOGO_URI` is fully deprecated](/work/versions/android-13#deprecations) in
  Android 13 (API level 33) and higher.

## Android 12

Some of the new enterprise features and updates in Android 12 include:

* Password complexity and security challenge streamlining for [work
  profiles](/work/versions/android-12#privacy-enhancements).
* Enrollment-specific IDs for [work profiles](/work/versions/android-12#company-owned).
* Disable USB and limit input methods on [company-owned devices](/work/versions/android-12#company-owned).
* Certificate management for [unmanaged devices](/work/versions/android-12#unmanaged).

## Android 11

Some of the new enterprise features and updates in Android 11 include:

* [Work profile enhancements](/work/versions/android-11#work-company-owned) for company-owned devices.
* The work and personal tabs have been [extended to more device features](/work/versions/android-11#ux).
* You can now schedule work profile pausing.

## Android 10

Some of the new enterprise features and updates in Android 10 include:

* Apps running in the personal profile can [show events from the work profile
  calendar](/work/versions/android-10.0#access_to_work_profile_calendars).
* The ability to [provision work profiles](/work/versions/android-10.0#improved_provisioning_tools_for_work_profiles) on devices enrolled with QR
  codes or using Zero touch.
* New option to [install system updates on fully managed devices](/work/versions/android-10.0#manual_system_update_installation) using a
  system update file.

## Android 9

Highlights from the enterprise features in Android 9 include:

* New [user interface controls](/work/versions/android-9.0#work-profile-ui) in Android's default launcher to help
  device users separate personal and work apps.
* [APIs for lock task mode](/work/versions/android-9.0#lock-task-mode) to support all Android apps and add improved
  control over the user interface.
* Support [multiple users](/work/versions/android-9.0#multi-user) on dedicated devices.
* New APIs to help users [switch between work and personal instances](/work/versions/android-9.0#switch-apps) of
  an app.

To learn about all the new enterprise features in Android 9, read [What's new in
Android 9 for enterprise apps](/work/versions/android-9.0).

## Android 8.0

Some of the highlights introduced for Android in the enterprise in Android 8.0
include:

* A new deployment scenario that allows [work profiles on fully managed
  devices](/work/versions/android-8.0#work-profile-on-managed-devices).
* New logging and reporting features available to [affiliated users](/work/versions/android-8.0#user-affiliation).
* The ability to offload app management to other applications using [API
  delegation](/work/versions/android-8.0#app-management-api-delegation).

To see all the new enterprise features in Android 8.0, read [What's New in
Android 8.0](/work/versions/android-8.0).

## Android 7.0

Some of the new features and updates for Android in the enterprise in Android
7.0 include:

* Provisioning corp-liable devices [using a QR code](/work/versions/android-7.0#qr_code_provisioning).
* Setting [security challenges](/work/versions/android-7.0#work_profile_security_challenge) for apps running in the work profile.
* Requiring work apps to [always connect](/work/versions/android-7.0#always-on_vpn) through a specified VPN.

To see all the new enterprise features in Android 7.0, read [What's New in
Android 7.0](/work/versions/android-7.0).