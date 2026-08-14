---
title: https://developer.android.com/work/versions/android-16
url: https://developer.android.com/work/versions/android-16
source: md.txt
---

This page provides an overview of the enterprise APIs, features, and behavior
changes introduced in Android 16 (API level 36). Some of the new enterprise
features and updates in Android 16 are described in the following sections:

## Thread networks

Android 16 adds a control to block the use of Thread networks. See
[`UserManager.DISALLOW_THREAD_NETWORK`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_THREAD_NETWORK) for details.

## NFC management

IT admins can enable or disable NFC on the device. See [`NfcAdapter.enable`](https://developer.android.com/reference/android/nfc/NfcAdapter#enable())
and [`NfcAdapter.disable`](https://developer.android.com/reference/android/nfc/NfcAdapter#disable()) for details. Android 16 also adds a control to
prevent users from making changes to NFC settings. See
[`UserManager.DISALLOW_CHANGE_NEAR_FIELD_COMMUNICATION_RADIO`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CHANGE_NEAR_FIELD_COMMUNICATION_RADIO) for details.

## App Function controls

Admins can choose to set a [`AppFunctionManager`](https://developer.android.com/reference/android/app/appfunctions/AppFunctionManager) policy, which
controls app functions operations on the device. An app function is a piece of
functionality that apps expose to the system for cross-app orchestration. See
[`AppFunctionManager`](https://developer.android.com/reference/android/app/appfunctions/AppFunctionManager) for more information on app functions, and
[`DevicePolicyManager.setAppFunctionsPolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAppFunctionsPolicy(int)) for available policy options.
App Functions is a
beta/experimental preview feature.

## Changes to enterprise setup flow

We're making changes to the enterprise setup flow - for devices that are
connected to the internet during setup - to reduce the number of screens and
taps and improve education and consent. While this change does not depend on
AOSP changes in Android 16, it will be available to Android 16 devices, and we
plan to begin rolling it out around a similar timeframe to the Android 16
launch. Once the rollout is complete, these changes will be present in
enterprise setup regardless of OEM, EMM, IDP or management mode. Since there are
no dedicated education screens and since education will only be shown during
loading time and require no user interaction,
[`EXTRA_PROVISIONING_SKIP_EDUCATION_SCREENS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_SKIP_EDUCATION_SCREENS) becomes redundant and will be
ignored.

## Auto time and timezone

New methods are available for enabling a DPC of a fully managed device or a work
profile on company-owned device to control whether time and time zone should be
obtained automatically from the network or not. See
[`DevicePolicyManager.setAutoTimePolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTimePolicy(int)) and
[`DevicePolicyManager.setAutoTimeZonePolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTimeZonePolicy(int)) for more details.