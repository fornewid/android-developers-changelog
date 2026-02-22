---
title: https://developer.android.com/work/versions/android-10
url: https://developer.android.com/work/versions/android-10
source: md.txt
---

# What&#39;s new for enterprise in Android 10

This page provides an overview of the new enterprise APIs, features, and behavior changes introduced in Android 10.

## Work profiles for company-owned devices

Android 10 introduces new provisioning and attestation features for company-owned devices that only require a work profile.

### Improved provisioning tools for work profiles

You can provision work profiles on Android 10 and later devices enrolled using[QR code](https://developers.google.com/android/work/requirements?api=playemm#14-qr-code-device-provisioning)or[Zero touch](https://developers.google.com/android/work/requirements?api=playemm#15-zero-touch-enrollment). During the provisioning of a company-owned device, a new intent extra allows device policy controller apps (DPCs) to initiate work profile*or*fully managed setup. After a work profile is created or full management is established, DPCs must launch policy compliance screens to enforce any initial policies.
| **Important:** This features doesn't affect existing DPC implementations that only support fully managed provisioning---they'll still work on Android 10 and later devices.

In your DPC's manifest file, declare a new intent filter for[`GET_PROVISIONING_MODE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_GET_PROVISIONING_MODE)in an activity and add the[`BIND_DEVICE_ADMIN`](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN)permission to prevent arbitrary apps from starting the activity. For example:  

    <activity
        android:name=".GetProvisioningModeActivity"
        android:label="@string/app_name"
        android:permission="android.permission.BIND_DEVICE_ADMIN">
        <intent-filter>
            <action
                android:name="android.app.action.GET_PROVISIONING_MODE" />
            <category android:name="android.intent.category.DEFAULT"/>
        </intent-filter>
    </activity>

During provisioning, the system launches the activity associated with the intent filter. The purpose of this activity is to specify a management mode (work profile or fully managed).

It may be useful to retrieve provisioning extras before determining the appropriate management mode for the device. The activity can call[`getIntent()`](https://developer.android.com/reference/android/app/Activity#getIntent())to retrieve the following:

- [`EXTRA_PROVISIONING_IMEI`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_IMEI)
- [`EXTRA_PROVISIONING_SERIAL_NUMBER`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_SERIAL_NUMBER)
- [`EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE)

DPCs can also create a new result intent and add the following extras to it:

- [`EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE): Add to the existing bundle or create a new bundle. This bundle is sent as an intent extra when your DPC launches its policy compliance screens.
- [`EXTRA_PROVISIONING_ACCOUNT_TO_MIGRATE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_ACCOUNT_TO_MIGRATE): Only specify an account to migrate if adding a work account as part of work profile provisioning.
- [`EXTRA_PROVISIONING_SKIP_EDUCATION_SCREENS`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_SKIP_EDUCATION_SCREENS)

To set the management mode on the device, call`putExtra(DevicePolicyManager.EXTRA_PROVISIONING_MODE,desiredProvisioningMode)`, where`desiredProvisioningMode`is:

- Work profile:`PROVISIONING_MODE_MANAGED_PROFILE`
- Fully managed:`PROVISIONING_MODE_FULLY_MANAGED_DEVICE`

Complete work profile or fully managed provisioning by sending provisioning details back to setup via[`setResult(RESULT_OK,
Intent)`](https://developer.android.com/reference/android/app/Activity#setResult(int,%20android.content.Intent))and close all active screens with[`finish()`](https://developer.android.com/reference/android/app/Activity#finish()).
| **Note:** To prevent failed provisioning, don't launch any activities or background services after returning to setup.

After provisioning is complete, a new Intent is available for DPCs to launch their compliance screens and enforce initial policy settings. On work profile devices, compliance screens are displayed in the work profile. Your DPC must ensure that its compliance screens are shown to users, even if a user escapes the setup flow.

In your DPC's manifest file, declare a new intent filter for[`ADMIN_POLICY_COMPLIANCE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_ADMIN_POLICY_COMPLIANCE)in an activity and add the[`BIND_DEVICE_ADMIN`](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN)permission to prevent arbitrary apps from starting the activity. For example:  

    <activity
        android:name=".PolicyComplianceActivity"
        android:label="@string/app_name"
        android:permission="android.permission.BIND_DEVICE_ADMIN">
        <intent-filter>
            <action android:name="android.app.action.ADMIN_POLICY_COMPLIANCE" />
            <category android:name="android.intent.category.DEFAULT"/>
        </intent-filter>
    </activity>

Your DPC**must** use this new Intent instead of listening for the[`ACTION_PROFILE_PROVISIONING_COMPLETE`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#ACTION_PROFILE_PROVISIONING_COMPLETE)broadcast.

The activity associated with the intent filter can call[`getIntent()`](https://developer.android.com/reference/android/app/Activity#getIntent())to retrieve the[`EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_ADMIN_EXTRAS_BUNDLE). After performing policy compliance,`ADMIN_POLICY_COMPLIANCE`must return[`setResult(RESULT_OK,
Intent)`](https://developer.android.com/reference/android/app/Activity#setResult(int,%20android.content.Intent))and close all active screens with[`finish()`](https://developer.android.com/reference/android/app/Activity#finish()).

Fully managed devices return users to the homescreen. Work profile devices prompt users to add their personal account before returning them to the home screen.

### Work-profile device-ID attestation

DPCs set as the admin of a work profile provisioned using zero-touch enrollment can get secure-hardware-attested device IDs, such as an IMEI or manufacturer's serial number. The device must include secure hardware (such as a trusted execution environment (TEE) or Secure Element (SE)) and support device-ID attestation and zero-touch enrollment.

The admin component of a work profile can call[`DevicePolicyManager.generateKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#generateKeyPair(android.content.ComponentName,%20java.lang.String,%20android.security.keystore.KeyGenParameterSpec,%20int)), passing one or more of[`ID_TYPE_SERIAL`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_SERIAL),[`ID_TYPE_IMEI`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI), or[`ID_TYPE_MEID`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_MEID)for the`idAttestationFlags`argument.

To learn more about extracting and validating device IDs, see[Verifying hardware-backed key pairs with Key Attestation](https://developer.android.com/training/articles/security-key-attestation).

## Work profile improvements

New APIs are available for supporting cross-profile calendar visibility and device-wide blocking of app installations from unknown sources.

### Work profile, device-wide unknown sources

Apps downloaded from sources other than Google Play (or other trusted app stores) are called apps from unknown sources. In Android 10, admins of work profiles can prevent any user or profile from installing apps from unknown sources anywhere on the device by adding the new user restriction[`DISALLOW_INSTALL_UNKNOWN_SOURCES_GLOBALLY`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES_GLOBALLY). After adding this restriction, however, a person using the device can still install apps using[adb](https://developer.android.com/studio/command-line/adb).

To prevent users from mistakenly installing apps from unknown sources, we recommend adding this user restriction because it doesn't require Google Play services to be installed. If you want to support older Android versions, you can set a[managed configuration value for Google Play](https://developer.android.com/work/dpc/security#unknown-sources).

### Limit permitted input devices to work profiles

When admins of work profiles call[`DevicePolicyManager.setPermittedInputMethods()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermittedInputMethods(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E)), users are only restricted to the permitted input methods inside their work profile instead of the entire device, giving users full control over input methods on the personal side of their device.

### Silently wipe work profiles

Added[`WIPE_SILENTLY`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#WIPE_SILENTLY)flag to[`DevicePolicyManager.wipeData()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int)). If the flag is set, users won't be notified after their work profile is wiped using[`wipeData()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#wipeData(int)).

## New features for fully managed devices

Android 10 introduces new features and APIs for fully managed devices, including manual system updates, extending QR-code and NFC provisioning to include the credentials for an EAP Wi-Fi network, and support for DNS over TLS.

### Manual system update installation

In Android 10, admins of fully managed devices can install system updates via a system update file. Manual system updates allow IT admins to do the following:

- Test an update on a small number of devices before installing them widely.
- Avoid duplicate downloads on bandwidth-limited networks.
- Stagger installations, or update devices only when they're not being used.

First, an IT admin sets a[postponed system-update policy](https://developer.android.com/work/dpc/system-updates#set-policy)to delay automatic installation (if required). Next, a device's DPC calls[`installSystemUpdate()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installSystemUpdate(android.content.ComponentName,%20android.net.Uri,%20java.util.concurrent.Executor,%20android.app.admin.DevicePolicyManager.InstallUpdateCallback))with the path to a device manufacturer's system update file. Pass an[`InstallSystemUpdateCallback`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager.InstallSystemUpdateCallback)object that the system can use to report errors that happen before the device restarts. If something goes wrong, the system calls[`onInstallUpdateError()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager.InstallUpdateCallback#onInstallUpdateError(int,%20java.lang.String))with the error code.

After the device restarts, your DPC needs to confirm a successful installation using a version API, such as[`Build.FINGERPRINT`](https://developer.android.com/reference/android/os/Build#FINGERPRINT). If the update fails, report the failure to an IT admin.

### EAP Wi-Fi provisioning

In Android 10, QR codes and NFC data used for device provisioning can contain EAP config and credentials---including certificates. When a person scans a QR code or taps an NFC tag, the device automatically authenticates to a local Wi-Fi network using EAP and starts the provisioning process without any additional manual input.

To authenticate Wi-Fi using EAP, add an[`EXTRA_PROVISIONING_WIFI_SECURITY_TYPE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_SECURITY_TYPE)extra with the value`"EAP"`. To specify the EAP authentication, you can add the following provisioning extras to your intent:

- [`EXTRA_PROVISIONING_WIFI_EAP_METHOD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_EAP_METHOD)
- [`EXTRA_PROVISIONING_WIFI_IDENTITY`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_IDENTITY)
- [`EXTRA_PROVISIONING_WIFI_ANONYMOUS_IDENTITY`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_ANONYMOUS_IDENTITY)
- [`EXTRA_PROVISIONING_WIFI_DOMAIN`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_DOMAIN)
- [`EXTRA_PROVISIONING_WIFI_PHASE2_AUTH`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_PHASE2_AUTH)
- [`EXTRA_PROVISIONING_WIFI_USER_CERTIFICATE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_USER_CERTIFICATE)
- [`EXTRA_PROVISIONING_WIFI_CA_CERTIFICATE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PROVISIONING_WIFI_CA_CERTIFICATE)

### Private DNS support

Organizations can use[DNS over TLS](https://android-developers.googleblog.com/2018/04/dns-over-tls-support-in-android-p.html)(called*Private DNS*on Android devices) to avoid leaking DNS queries, including those of internal hostnames. Admin components of fully managed devices can control the Private DNS settings of the device. To set the Private DNS mode, call:

- [`setGlobalPrivateDnsModeOpportunistic()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalPrivateDnsModeOpportunistic(android.content.ComponentName))for the device to use private DNS when the system can discover a supporting name server, or
- [`setGlobalPrivateDnsModeSpecifiedHost()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setGlobalPrivateDnsModeSpecifiedHost(android.content.ComponentName,%20java.lang.String))to specify the hostname of a name server that supports[RFC7858](https://tools.ietf.org/html/rfc7858)in the`privateDnsHost`argument.

When your DPC calls either of these methods, the system returns[`PRIVATE_DNS_SET_NO_ERROR`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PRIVATE_DNS_SET_NO_ERROR)if the call was successful. Otherwise it returns an error.

To retrieve the Private DNS mode and host set on a device, call[`getGlobalPrivateDnsMode()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getGlobalPrivateDnsMode(android.content.ComponentName))and[`getGlobalPrivateDnsHost()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getGlobalPrivateDnsHost(android.content.ComponentName)). You can prevent users from changing private DNS settings by adding the[`DISALLOW_CONFIG_PRIVATE_DNS`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_PRIVATE_DNS)user restriction.

## VPN lockdown mode exemption

VPN lockdown mode allows a DPC to[block any network traffic](https://developer.android.com/guide/topics/connectivity/vpn#blocked_connections)that doesn't use the VPN.[Admins](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)of fully managed devices and work profiles can exempt apps from lockdown mode. Exempted apps use a VPN by default, but automatically connect to other networks if the VPN isn't available. Exempted apps that are also[explicitly denied access the VPN](https://developer.android.com/reference/android/net/VpnService.Builder#addDisallowedApplication(java.lang.String))will only use other networks.

To exempt an app from lockdown mode, call the new[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)method[`setAlwaysOnVpnPackage()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAlwaysOnVpnPackage(android.content.ComponentName,%20java.lang.String,%20boolean,%20java.util.List%3Cjava.lang.String%3E))that accepts a list of exempted app packages. Any app packages the DPC adds must be installed on the device when the method is called. If an app is uninstalled and reinstalled, the app must be exempted again. To get the apps previously exempted from lockdown mode, call[`getAlwaysOnVpnLockdownWhitelist()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAlwaysOnVpnLockdownWhitelist(android.content.ComponentName)).

To help admins of fully managed devices and work profiles get the lockdown mode status, Android 10 adds the[`isAlwaysOnVpnLockdownEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isAlwaysOnVpnLockdownEnabled(android.content.ComponentName))method.

## New delegation scopes

Android 10 extends the list of functions that a DPC can delegate to other, more specialized apps. Android groups the API methods needed for a task into*scopes* . To delegate a scope, call[`setDelegatedScopes()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setDelegatedScopes(android.content.ComponentName,%20java.lang.String,%20java.util.List%3Cjava.lang.String%3E))and pass one or more of the following scopes:

- [`DELEGATION_NETWORK_LOGGING`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_NETWORK_LOGGING)to delegate[network activity logging](https://developer.android.com/work/versions/android-10#network-activity-logging)
- [`DELEGATION_CERT_SELECTION`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_CERT_SELECTION)to delegate[certificate selection](https://developer.android.com/work/versions/android-10#certificate-selection)

Android 10 introduces the new class[`DelegatedAdminReceiver`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver)for delegate apps. The system uses this broadcast receiver to send DPC-like callbacks to delegate apps. Apps that have been delegated network activity logging and certificate selection should implement this class. To add this component to a delegate app, follow these steps:

1. Add a subclass of[`DelegatedAdminReceiver`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver)to the delegate app.
2. Declare the[`<receiver>`](https://developer.android.com/guide/topics/manifest/receiver-element)in the app manifest, adding an intent-filter action for each callback. For example,[`ACTION_NETWORK_LOGS_AVAILABLE`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#ACTION_NETWORK_LOGS_AVAILABLE)or[`ACTION_CHOOSE_PRIVATE_KEY_ALIAS`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#ACTION_CHOOSE_PRIVATE_KEY_ALIAS).
3. Protect the broadcast receiver with the[`BIND_DEVICE_ADMIN`](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN)permission.

The following snippet shows the app manifest of a single delegate app that handles both network logging and certificate selection:  

    <receiver android:name=".app.DelegatedAdminReceiver"
            android:permission="android.permission.BIND_DELEGATED_ADMIN">
        <intent-filter>
            <action android:name="android.app.admin.action.NETWORK_LOGS_AVAILABLE">
            <action android:name="android.app.action.CHOOSE_PRIVATE_KEY_ALIAS">
        </intent-filter>
        </receiver>

### Network activity logging

To help organizations detect and track malware, DPCs can[log TCP connections and DNS lookups](https://developer.android.com/work/dpc/logging)by the system. In Android 10,[admins](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)of fully managed devices can delegate network logging to a specialized app.

To[retrieve network logs](https://developer.android.com/work/dpc/logging#retrieve_logs)after the system makes a batch available, delegate apps should first subclass[`DelegatedAdminReceiver`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver)(described previously). In your subclass, implement the[`onNetworkLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver#onNetworkLogsAvailable(android.content.Context,%20android.content.Intent,%20long,%20int))callback by following the guidance in[Retrieve logs](https://developer.android.com/work/dpc/logging#retrieve_logs).

Delegate apps can call the following[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)methods (passing`null`for the`admin`argument):

- [`setNetworkLoggingEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName,%20boolean))
- [`isNetworkLoggingEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isNetworkLoggingEnabled(android.content.ComponentName))
- [`retrieveNetworkLogs()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrieveNetworkLogs(android.content.ComponentName,%20long))

To avoid losing logs, DPC's shouldn't[enable network logging](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName,%20boolean))if planning to delegate to another app. The delegate app should enable and collect network logs. After a DPC delegates network logging, it won't receive any further[`onNetworkLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onNetworkLogsAvailable(android.content.Context,%20android.content.Intent,%20long,%20int))callbacks.

To learn how to report network activity logging from a delegate app, read the developer's guide[Network activity logging](https://developer.android.com/work/dpc/logging).

### Certificate selection

In Android 10,[admins](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)of fully managed devices, work profiles, and secondary users can delegate certificate selection to a specialized app.

To select a certificate alias, delegate apps should first subclass[`DelegatedAdminReceiver`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver)(described previously). In your subclass, implement the[`onChoosePrivateKeyAlias()`](https://developer.android.com/reference/android/app/admin/DelegatedAdminReceiver#onChoosePrivateKeyAlias(android.content.Context,%20android.content.Intent,%20int,%20android.net.Uri,%20java.lang.String))callback and return an alias for a preferred certificate or, to prompt the user to select a certificate, return`null`.

## Deprecation of device admin policies

Android 10 prevents apps and DPCs from applying legacy[device admin](https://developer.android.com/work/device-admin)policies. We recommend customers and partners transition to fully managed devices or work profiles. The following policies throw a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)when invoked by a device admin targeting Android 10:

- [`USES_POLICY_DISABLE_CAMERA`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_DISABLE_CAMERA)
- [`USES_POLICY_DISABLE_KEYGUARD_FEATURES`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_DISABLE_KEYGUARD_FEATURES)
- [`USES_POLICY_EXPIRE_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_EXPIRE_PASSWORD)
- [`USES_POLICY_LIMIT_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_LIMIT_PASSWORD)

| **Note:** As a replacement for the keyguard and password policies listed above, apps should use the method described in[Screen lock quality check](https://developer.android.com/work/versions/android-10#screen_lock_quality_check).

Some applications use device admin for consumer device administration. For example, locking and wiping a lost device. To enable this, the following policies continue to be available:

- [`USES_POLICY_WIPE_DATA`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_WIPE_DATA)
- [`USES_POLICY_FORCE_LOCK`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_FORCE_LOCK)
- [`USES_POLICY_RESET_PASSWORD`](https://developer.android.com/reference/android/app/admin/DeviceAdminInfo#USES_POLICY_RESET_PASSWORD)

For more information about these changes, read[Device admin deprecation](https://developers.google.com/android/work/device-admin-deprecation).

## New features for apps

Apps targeting Android 10 can query the screen lock complexity set on a device before displaying confidential data or launching critical features. Apps calling the[`KeyChain`](https://developer.android.com/reference/android/security/KeyChain)API benefit from behavior improvements, while new features are also available for VPN apps.

### Screen lock quality check

Starting in Android 10, apps with critical features that require a screen lock can query a device or work profile's screen lock complexity. Apps needing a stronger screen lock can direct the user to the system screen lock settings, allowing them to update their security settings.

To check screen lock quality:

- Add the new`REQUEST_PASSWORD_COMPLEXITY`permission to your app's manifest.
- Call[`DevicePolicyManager.getPasswordComplexity()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPasswordComplexity()). Complexity is divided into four categories:
  - [`PASSWORD_COMPLEXITY_NONE`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_COMPLEXITY_NONE)
  - [`PASSWORD_COMPLEXITY_LOW`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_COMPLEXITY_LOW)
  - [`PASSWORD_COMPLEXITY_MEDIUM`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_COMPLEXITY_MEDIUM)
  - [`PASSWORD_COMPLEXITY_HIGH`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PASSWORD_COMPLEXITY_HIGH)

To launch system screen lock settings, use[`ACTION_SET_NEW_PASSWORD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_SET_NEW_PASSWORD)with extra[`EXTRA_PASSWORD_COMPLEXITY`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#EXTRA_PASSWORD_COMPLEXITY)---options that don't meet the complexity specified in the intent extra are grayed out. Users can choose from the available screen lock options or exit the screen.

**Best practice:** Display a message in your app before launching the system screen lock page. When your app resumes, call[`DevicePolicyManager.getPasswordComplexity()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPasswordComplexity())again. If a stronger screen lock is still required, restrict access rather than repeatedly prompting users to update their security settings.

### HTTP proxy support in VPN apps

In Android 10,[VPN apps](https://developer.android.com/guide/topics/connectivity/vpn)can set an HTTP proxy for their VPN connection. To add an HTTP proxy, a VPN app must configure a[`ProxyInfo`](https://developer.android.com/reference/android/net/ProxyInfo)instance with a host and port, before calling[`VpnService.Builder.setHttpProxy()`](https://developer.android.com/reference/android/net/VpnService.Builder#setHttpProxy(android.net.ProxyInfo)). The system and many networking libraries use this proxy setting but the system doesn't force apps to proxy HTTP requests.

For sample code that shows how to set an HTTP proxy, see the[ToyVPN](https://android.googlesource.com/platform/development/+/master/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnConnection.java#349)sample app.

### VPN service modes

VPN apps can discover if the service is running because of[always-on Vpn](https://developer.android.com/guide/topics/connectivity/vpn#always-on)and if[lockdown mode](https://developer.android.com/guide/topics/connectivity/vpn#blocked_connections)is active. New methods added in Android 10 can help you adjust your user interface. For example, you might disable your disconnect button when always-on VPN controls the lifecycle of your service.

VPN apps can call the following[`VpnService`](https://developer.android.com/reference/android/net/VpnService)methods after[connecting to the service](https://developer.android.com/guide/topics/connectivity/vpn#connect_a_service)and establishing the local interface:

- [`isAlwaysOn()`](https://developer.android.com/reference/android/net/VpnService#isAlwaysOn())to find out if the system started the service because of always-on VPN
- [`isLockdownEnabled()`](https://developer.android.com/reference/android/net/VpnService#isLockdownEnabled())to find out if the system is blocking connections that don't use the VPN

The always-on status remains the same while your service is running but the lockdown-mode status might change.

### Keychain improvements

Android 10 introduces several improvements related to the[`KeyChain`](https://developer.android.com/reference/android/security/KeyChain)API.

When an app calls`KeyChain.choosePrivateKeyAlias()`, Android 10 and later devices filter the list of certificates a user can choose from based on the issuers and key algorithms specified in the call.

For example, when a TLS server sends a[Certificate Request](https://tools.ietf.org/html/rfc8446#section-4.3.2)message as part of a TLS handshake and the browser calls`KeyChain.choosePrivateKeyAlias()`, the certificate selection prompt only includes options that match the issuers parameter. If no matching options are available or there are no certificates installed on the device, then the selection prompt won't be displayed to the user.

Additionally,[`KeyChain`](https://developer.android.com/reference/android/security/KeyChain)no longer requires a device to have a screen lock before keys or CA certificates can be imported.