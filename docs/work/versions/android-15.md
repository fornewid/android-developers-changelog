---
title: https://developer.android.com/work/versions/android-15
url: https://developer.android.com/work/versions/android-15
source: md.txt
---

This page provides an overview of the enterprise APIs, features, and behavior
changes introduced in Android 15 (API level 35).

## Enhanced employee and device protection

Android 15 enhances employee and device protection with features like theft
protection, phishing controls, and private space for personal profiles.

### Android theft protection

- Protect sensitive business data from theft.
- Enhance your privacy and prevent unauthorized access to users' personal data.

### Private space for personal profile

- [Private space](https://developer.android.com/about/versions/15/features#private-space) is a new feature in Android 15 that lets users create a separate area within their personal profile under an additional layer of authentication, to shield specific personal apps while working in public spaces.
- On managed devices:
  - Administrators are able to block users from having a private space and remove an existing private space on the personal profile of a corporate owned device. See [`UserManager.DISALLOW_ADD_PRIVATE_PROFILE`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_ADD_PRIVATE_PROFILE).
  - Existing personal app allowlists and blocklists also apply to the private space on devices managed by the [`Android Management API`](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies#PersonalApplicationPolicy). This feature will be available to [`custom DPCs`](https://developer.android.com/work/dpc/build-dpc) in the future.
  - Private space is not available on fully managed devices.
  - A new [`UserManager.USER_TYPE_PROFILE_PRIVATE`](https://developer.android.com/reference/android/os/UserManager#USER_TYPE_PROFILE_PRIVATE) is now available.

### NIAP compliance maintenance

Android 15 migrates existing backup service audit logging events from logcat to
security log with the formal definition of
[`SecurityLog.TAG_BACKUP_SERVICE_TOGGLED`](https://developer.android.com/reference/android/app/admin/SecurityLog#TAG_BACKUP_SERVICE_TOGGLED).

## Stronger management of company-owned devices

Android 15 strengthens company-owned device management by simplifying eSIM
management, adding controls for Circle to Search on Android Work Profile, and
adding more customization options for corporate-owned devices.

### Simplify eSIM management on managed devices

- Android 15 adds platform APIs to allow an IT Admin to remotely provision eSIM profiles onto managed devices. This also includes new controls over the eSIM profiles.
- We introduce the concept of a "Managed SIM"/"Managed Subscription", supporting the following features:
  - IT admins can download and delete the eSIM profiles programmatically.
  - On company-owned devices, the IT admin can activate the eSIM silently after download. Also, users can't delete the admin-downloaded managed eSIM. IT admins can set [`DISALLOW_CONFIG_MOBILE_NETWORKS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_MOBILE_NETWORKS) user restriction to disallow users from deleting the managed eSIM.
  - Bring your own device (BYOD) users can choose to delete the SIM at any time.

### Controls for Circle to Search on Android Work Profile

- Admins can choose to block the Circle to Search feature on fully managed devices or within an Android Work Profile.
- Users can search more seamlessly at work.

### Additional customization for corporate-owned devices

- Extend battery life with customizable screen brightness and timeout controls, which are included in Android 15 for corporate-owned, personally enabled (COPE) devices. This feature already existed for fully managed devices.
- Enforce the defaults for the personal profile on company-owned, personally enabled (COPE) devices.
  - IT admins can enforce the OEM-default dialer, messages, and browser apps prior to set up, and prevent the end user from changing them using [`DISALLOW_CONFIG_DEFAULT_APPS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_DEFAULT_APPS).
  - Setting the defaults after setup must be combined with app allowlist controls.
  - IT admins can only make an app the default if it's already in the user's personal profile.