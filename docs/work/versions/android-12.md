---
title: https://developer.android.com/work/versions/android-12
url: https://developer.android.com/work/versions/android-12
source: md.txt
---

This page provides an overview of the new enterprise APIs, features, and
behavior changes introduced in Android 12 (API level 31).

## Work profile

The following new features are available in Android 12 for work
profiles.

### Security and privacy enhancements for work profile

The following features are available in Android 12 for personal
devices with a work profile:

- The [password
  complexity](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setRequiredPasswordComplexity(int)) feature sets device-wide password requirements in the form of predefined complexity buckets (High, Medium, Low, and None). If required, strict password requirements can instead be placed on the [work profile security
  challenge](https://developer.android.com/work/dpc/security#work_profile_security_challenge).
- Work profile security challenge onboarding has been streamlined. Setup now takes into account whether device passcode meets admin requirements, and makes it easy for the user to choose whether to increase the strength of their device passcode or to use the work profile security challenge.
- [An enrollment-specific
  ID](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setOrganizationId(java.lang.String)) provides a unique ID that identifies the work profile enrollment in a particular organization, and will remain stable across factory resets. Access to other hardware identifiers of the device (IMEI, MEID, serial number) are removed for personal devices with a work profile in Android 12.
- [Company-owned devices](https://developer.android.com/work/versions/android-12#company-owned), with and without work profiles, can adopt the features listed in the preceding list items, but are not required to adopt them in Android 12.
- You can [set](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName,%20boolean)) and [retrieve](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrieveNetworkLogs(android.content.ComponentName,%20long)) work profile network logging. You can [delegate](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_NETWORK_LOGGING) network logging on the work profile to another work application. You can't use network logging to monitor traffic in the personal profile.
- Users have additional privacy controls for work profile apps. Users can grant the following permissions to work profile apps unless denied by their IT administrator. For each app in the work profile, the user can allow or deny the following permissions:
  - Location
  - Camera
  - Microphone
  - Body sensor
  - Physical activity

## Company-owned devices

The following new features are available for company-owned devices. The term
*company-owned device* refers to both [fully managed
devices](https://developers.google.com/android/work/requirements/fully-managed-device)
and [work profile devices that are
company-owned](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isOrganizationOwnedDeviceWithManagedProfile()).

- An IT administrator can [disable
  USB](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUsbDataSignalingEnabled(boolean)),
  except for charging functions, on company-owned devices. This feature includes
  the capability to [check if this feature is
  supported](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#canUsbDataSignalingBeDisabled())
  on the device and to [check if it is currently
  enabled](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isUsbDataSignalingEnabled()).

- Company-owned devices with a work profile can [limit the input methods used in
  the personal
  profile](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermittedInputMethods(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E))
  to allow only system input methods.

- In Android 12 you can create a delegation scope. Enable and collect security
  log events by calling
  [`setDelegatedScopes()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setDelegatedScopes(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.lang.String%3E))
  and passing
  [`DELEGATION_SECURITY_LOGGING`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_SECURITY_LOGGING).
  Security logging helps organizations gather usage data from devices that can be parsed and programmatically evaluated for malicious or risky behavior. Delegate apps can [enable security
  logging](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecurityLoggingEnabled(android.content.ComponentName,%20boolean)),
  [verify that logging is
  enabled](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isSecurityLoggingEnabled(android.content.ComponentName)),
  and [retrieve the security
  logs](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrieveSecurityLogs(android.content.ComponentName)).

## Other

The following section describes changes in enterprise APIs that are not specific
to work profiles or company-owned devices.

### Unmanaged device certificate management

Devices without management are now able to take advantage of Android's on-device
key generation to manage certificates:

- The user can grant permission to a certificate management app to manage their credentials (not including CA certificates).
- The certificate management app can use Android's on-device key generation.
- The certificate management app can declare a list of apps and URIs where the credentials can be used for authentication.

New APIs provide new functionality:

- Check if the existing device-wide password is [compliant against explicit
  device password
  requirements](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isActivePasswordSufficientForDeviceRequirement()).
- Check whether a certificate and private key are [installed under a given
  alias](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#hasKeyPair(java.lang.String)).

### Privacy and transparency enhancements for fully-managed devices

IT administrators can manage permission grants or choose to opt out of managing
sensor-related permission grants during provisioning. If the administrator
chooses to manage permissions, users see an explicit message during the setup
wizard. If the administrator chooses to opt out, users are prompted to accept or
deny permissions in-app when the app is first used. Administrators can always
deny permissions.

### Network configuration

A [device policy controller](https://developer.android.com/work/dpc/build-dpc) (DPC) can get the list of a
device's configured networks without requiring the location permission by using
a new API [getCallerConfiguredNetworks](https://developer.android.com/reference/android/net/wifi/WifiManager#getCallerConfiguredNetworks())
rather than using the existing API
[getConfiguredNetworks](https://developer.android.com/reference/android/net/wifi/WifiManager#getConfiguredNetworks())
(which requires location permission). The list of networks returned is limited
to work networks.

A DPC on fully-managed devices can ensure only admin-provided networks are
configured on the device, also without requiring the location permission.

Administrators can use the keys generated in secure hardware for Wi-Fi
authentication by
[granting](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#grantKeyPairToWifiAuth(java.lang.String))
a KeyChain key to the Wi-Fi subsystem for authentication and
[configuring](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#getClientKeyPairAlias())
an enterprise Wi-Fi network with that key.

### Connected apps auto-granting

To allow a better user experience, a few preloaded applications have
auto-granted the
[configuration to share personal and work data](https://support.google.com/work/android/answer/10064639).

On Android 11+:

- depending on the device OEM, preloaded assist apps or preloaded default IMEs
- Google app, if it's preloaded.
- Gboard app, if it's preloaded and the out-of-box default IME app.

On Android 12+:

- Android Auto app, if it's preloaded.

The full list of application depends on the device OEM.
| **Note:** IT admins cannot revoke these auto-granted configurations.

## Deprecations

Android 12 includes the following notable API deprecations:

- `setPasswordQuality()` and `getPasswordQuality()` are deprecated for setting device-wide passcode on work profile devices that are personal devices rather than company-owned. DPCs should use `setRequiredPasswordComplexity()` instead.
- `setOrganizationColor()` and `getOrganizationColor()` are fully deprecated in Android 12.
- `android.app.action.PROVISION_MANAGED_DEVICE` no longer works on Android 12. DPCs must implement activities with intent filters for the `ACTION_GET_PROVISIONING_MODE` and `ACTION_ADMIN_POLICY_COMPLIANCE` intent actions. Using `ACTION_PROVISION_MANAGED_DEVICE` to start provisioning causes the provisioning to fail. To continue to support Android 11 and lower, EMMs should continue to support the `PROVISION_MANAGED_DEVICE` constant.
- `setPermissionPolicy()` and `setPermissionGrantState()` are deprecated for granting sensor-related permissions for all work profile devices targeting Android 12 and higher. The deprecations cause the following changes:
  - On devices upgrading from Android 11 to Android 12, existing permission grants remain, but new permission grants are not possible.
  - Ability to deny permissions remains.
  - If you develop and distribute applications relying on admin-granted permissions, you must ensure these follow the recommended way of requesting permissions.
  - Applications that follow the recommended way of requesting permissions continue to work as expected. Users are prompted to grant the permission; the app must be able to handle any outcome.
  - Applications that rely on admin-granted permissions and explicitly access permission-protected resources, without following the guidelines, may crash.

## Learn more

To learn about other changes that might affect your app, read the Android 12
behavior changes pages (for [apps targeting Android 12](https://developer.android.com/about/versions/12/behavior-changes-12)
and [for all apps](https://developer.android.com/about/versions/12/behavior-changes-all)).