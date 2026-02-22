---
title: https://developer.android.com/work/versions/android-11
url: https://developer.android.com/work/versions/android-11
source: md.txt
---

This page provides an overview of the new enterprise APIs, features, and
behavior changes introduced in Android 11.

## Work profile

The following new features are available in Android 11 for work
profiles.

### Work profile enhancements for company-owned devices

Android 11 introduces improved support for work profiles on
company-owned devices. If a work profile is added from the setup wizard using
the [provisioning tools added in Android 10](https://developer.android.com/work/versions/android-10#improved_provisioning_tools_for_work_profiles),
the device is recognized as company-owned and a wider range of asset management
and device security policies is made available to the device policy controller
(DPC). These capabilities enable easier management of both work and personal use
on company-owned devices, while maintaining the privacy protections of the work
profile.

If a work profile is added to a device using any other method, Android 11
recognizes the device as personally-owned. The behavior and features available
to work profiles on personally-owned devices remains unchanged.

#### Devices upgrading to Android 11

[Work profiles on fully managed devices](https://developer.android.com/work/managed-profiles)
will be upgraded to the enhanced work profile experience on Android 11.
For customers, this means devices will receive the improved privacy benefits and
consistency of a single work profile experience across both personally-owned and
company-owned devices, without the need to re-enroll legacy work profile on
fully managed devices. Or if you prefer, by removing the work profile before
upgrade you can maintain a fully managed device experience across the upgrade.

Customers can contact their EMM to ensure their devices are prepared to upgrade
to Android 11. EMMs can find more detailed migration guidance in
the [Android Enterprise EMM Provider community](https://emm.androidenterprise.dev/s/)
(login required).

### UX improvements

The separate [work and personal tabs](https://developer.android.com/work/versions/android-9.0#work-profile-ui)
introduced to the default launcher in Android 9 have been extended to more
device features. In Android 11, device manufacturers can present
work and personal tabs:

- In the Settings app, specifically for Location, Storage, Accounts, and App info.
- When a user taps Share share.
- When a user is presented with the option to open a selected item with another app (*Open with* menu).
- When selecting documents.

![](https://developer.android.com/static/images/about/versions/11/work-profile-ux.png) **Figure 1.** (Left) Personal tab and work tab in *Settings \> App info*. (Right) Work apps icons when the work profile is paused.

Android 11 also introduces UX enhancements that make it clearer to users when
their work profile is paused. And when a user turns on their work profile,
they no longer have to enter their work passcode if it's the same as their
device passcode.

### Reset work profile passcode button

When a work profile is paused, the work profile lock screen now supports a
*forgot my password* button for Android 11 devices that have separate device
and work profile passwords. If your [DPC is direct boot
aware](https://developer.android.com/training/articles/direct-boot), you can [set and activate a
token](https://developer.android.com/work/dpc/security#set_and_activate_a_token) to enable the button.

When a user presses the button, they're shown text that instructs them to
contact their IT admin. Pressing the button also starts the work profile in
direct boot (locked) mode, allowing your DPC to complete the steps to perform a
[secure work profile passcode reset](https://developer.android.com/work/dpc/security#secure-passcode-reset).

## Company-owned devices

The following new features are available for company-owned devices. The term
*company-owned device* refers to both fully managed devices and [work profile
devices that are company-owned](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isOrganizationOwnedDeviceWithManagedProfile()).

### Common Criteria Mode

This mode addresses [Common Criteria](https://www.commoncriteriaportal.org/)
[Mobile Device Fundamentals Protection Profile](https://www.commoncriteriaportal.org/files/ppfiles/pp_md_v3.1.pdf)
(MDFPP) specific requirements. Admins of company-owned devices can now [enable
Common Criteria Mode](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCommonCriteriaModeEnabled(android.content.ComponentName,%20boolean)) (and [check if it's enabled](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isCommonCriteriaModeEnabled(android.content.ComponentName)))
on a device. When enabled, Common Criteria Mode increases security in certain
security components on a device, including AES-GCM encryption of Bluetooth Long
Term Keys, and Wi-Fi configuration stores.

### Individual key attestation support

| **Note:** This feature is only available for devices with a [StrongBox security chip](https://developer.android.com/training/articles/keystore#HardwareSecurityModule).

In Android 11, admins of company-owned devices can [request device attestation](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#generateKeyPair(android.content.ComponentName,%20java.lang.String,%20android.security.keystore.KeyGenParameterSpec,%20int)) using individual attestation certificates:

- Ensure [`KeyGenParameterSpec` is built with StrongBox specified](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setIsStrongBoxBacked(boolean)).
- Pass [`ID_TYPE_INDIVIDUAL_ATTESTATION`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_INDIVIDUAL_ATTESTATION) for the `idAttestationFlags` argument.

A new method is also available to [check if a device supports unique device ID attestation](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isUniqueDeviceAttestationSupported()).

## Other

- Users are now notified when an admin:

  - [Enables location services](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLocationEnabled(android.content.ComponentName,%20boolean)) on their company-owned device. If the admin sets a global policy to auto-accept all permissions, the user is notified when an app requests, and is granted, location permission because of this policy.
  - [Grants an app the permission](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermissionGrantState(android.content.ComponentName,%20java.lang.String,%20java.lang.String,%20int)) to use the location of a personally-owned device.
- Pre-grant certificate access to work apps: DPCs targeting Android 11
  now have the option to [grant individual apps access to specific `KeyChain` keys](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#grantKeyPairToApp(android.content.ComponentName,%20java.lang.String,%20java.lang.String)), allowing these apps
  to call [`getCertificateChain()`](https://developer.android.com/reference/android/security/KeyChain#getCertificateChain(android.content.Context,%20java.lang.String)) and [`getPrivateKey()`](https://developer.android.com/reference/android/security/KeyChain#getPrivateKey(android.content.Context,%20java.lang.String)) without having to first
  call [`choosePrivateKeyAlias()`](https://developer.android.com/reference/android/security/KeyChain#choosePrivateKeyAlias(android.app.Activity,%20android.security.KeyChainAliasCallback,%20java.lang.String%5B%5D,%20java.security.Principal%5B%5D,%20java.lang.String,%20int,%20java.lang.String)).

  For example, VPN apps that run as a background service can use this feature to
  gain access to the certificates they need without requiring any user
  interaction. A new method is also available to revoke access.
  | **Note:** Apps installed on unmanaged devices or in a device's personal profile can no longer install CA certificates using [`createInstallIntent()`](https://developer.android.com/reference/android/security/KeyChain#createInstallIntent()). Instead, users must manually install CA certificates in **Settings**.
- [All methods related to setting password minimums](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordMinimumLength(android.content.ComponentName,%20int))
  require an appropriate [password quality](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordQuality(android.content.ComponentName,%20int)) before they can be enforced.

  - [`setPasswordMinimumLength()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordMinimumLength(android.content.ComponentName,%20int)) requires at least [`PASSWORD_QUALITY_NUMERIC`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_QUALITY_NUMERIC).
  - All other password minimum methods require at least [`PASSWORD_QUALITY_COMPLEX`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_QUALITY_COMPLEX).
- Always-on VPN enhancements: Users can no longer disable always-on VPN when
  it's [configured by an admin](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAlwaysOnVpnPackage(android.content.ComponentName,%20java.lang.String,%20boolean)).

- Updates to [`ADMIN_POLICY_COMPLIANCE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_ADMIN_POLICY_COMPLIANCE):

  - When provisioning an Android 11 device, the system now sends [`ADMIN_POLICY_COMPLIANCE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_ADMIN_POLICY_COMPLIANCE) before setting [`DEVICE_PROVISIONED`](https://developer.android.com/reference/android/provider/Settings.Global#DEVICE_PROVISIONED) to `true`.
  - [`ADMIN_POLICY_COMPLIANCE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_ADMIN_POLICY_COMPLIANCE) can also be optionally used when [adding a Google Account](https://developers.google.com/android/work/play/emm-api/prov-devices#google_account_method) to provision a device. In the 2021 Android release, it will be required for this provisioning method.
- New APIs are also available to:

  - [Check](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAutoTimeEnabled(android.content.ComponentName)) and [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTimeEnabled(android.content.ComponentName,%20boolean)) whether auto time is enabled on a device. If enabled, the time automatically obtained from the network. Replaces `setAutoTimeRequired()` and `getAutoTimeRequired()` (see [Deprecations](https://developer.android.com/work/versions/android-11#deprecations) for more information).
  - [Check](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAutoTimeZoneEnabled(android.content.ComponentName)) and [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTimeZoneEnabled(android.content.ComponentName,%20boolean)) whether auto time zone is enabled on a device. If enabled, the time zone is automatically obtained from the network.
  - [Check](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getFactoryResetProtectionPolicy(android.content.ComponentName)) and [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setFactoryResetProtectionPolicy(android.content.ComponentName,%20android.app.admin.FactoryResetProtectionPolicy)) the factory reset protection (FRP) policy on a company-owned device.
  - [Check](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#hasLockdownAdminConfiguredNetworks(android.content.ComponentName)) and [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setConfiguredNetworksLockdownState(android.content.ComponentName,%20boolean)) whether a user can change admin-configured network settings on a company-owned device.
  - [Check](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getUserControlDisabledPackages(android.content.ComponentName)) and [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUserControlDisabledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E)) the protected packages on a fully managed device. Users can't clear app data or force-stop protected packages.
  - [Set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLocationEnabled(android.content.ComponentName,%20boolean)) the primary location settings on a device.

## Deprecations

Android 11 includes the following notable API deprecations:

- The `Settings.Secure.LOCATION_MODE` setting is deprecated. Apps shouldn't use
  this value as the `setting` argument for the
  [`setSecureSetting()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecureSetting(android.content.ComponentName,%20java.lang.String,%20java.lang.String))
  method. Device owners should instead call
  [`setLocationEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setLocationEnabled(android.content.ComponentName,%20boolean)).

- [`resetPassword()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPassword(java.lang.String,%20int))
  is now fully deprecated. All DPCs should use [secure passcode reset](https://developer.android.com/work/dpc/security#secure-passcode-reset)
  instead.

- [`setAutoTimeRequired()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTimeRequired(android.content.ComponentName,%20boolean))
  and [`getAutoTimeRequired()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAutoTimeRequired()). Use [`setAutoTime()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAutoTime(android.content.ComponentName,%20boolean)) and [`getAutoTime()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAutoTime(android.content.ComponentName)) instead.

- [`setStorageEncryption`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setStorageEncryption(android.content.ComponentName,%20boolean)) and [`getStorageEncryption()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getStorageEncryption(android.content.ComponentName)). Use [`getStorageEncryptionStatus()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getStorageEncryptionStatus()) instead.

- [`setGlobalSetting()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalSetting(android.content.ComponentName,%20java.lang.String,%20java.lang.String)) and [`setSecureSetting()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecureSetting(android.content.ComponentName,%20java.lang.String,%20java.lang.String)) are mostly deprecated---dedicated setter methods and user restrictions are available to replace most settings (see reference for more details).

- [`setOrganizationColor()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setOrganizationColor(android.content.ComponentName,%20int)) is fully deprecated.

## Learn more

To learn about other changes that might affect your app, read the Android 11
behavior changes pages (for [apps targeting Android 11](https://developer.android.com/about/versions/11/behavior-changes-11)
and [for all apps](https://developer.android.com/about/versions/11/behavior-changes-all)).