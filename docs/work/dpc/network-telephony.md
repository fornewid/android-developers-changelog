---
title: https://developer.android.com/work/dpc/network-telephony
url: https://developer.android.com/work/dpc/network-telephony
source: md.txt
---

# Networking and telephony

The features in this guide describe networking and telephony management
capabilities you can implement in your [device policy
controller](https://developer.android.com/work/dpc/build-dpc) (DPC) app. This document contains code
samples and you can also use the [Test
DPC](https://github.com/googlesamples/android-testdpc/) app as a
source of sample code for Android's enterprise features.

A DPC app can run in profile owner mode on personal devices or in device owner
mode on fully managed devices. This table indicates which features are
available when the DPC runs in [profile owner mode or device owner
mode](https://developers.google.com/android/work/play/emm-api/prov-devices#modes_of_operation):

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|
| **Feature**                                                                                                                                                         | **Profile owner** | **Device owner** |
| [Access work contacts across profiles](https://developer.android.com/work/dpc/network-telephony#access_work_contacts_across_profiles)                               | ✓                 |                  |
| [Ensure a secure network connection for work traffic](https://developer.android.com/work/dpc/network-telephony#ensure_a_secure_network_connection_for_work_traffic) | ✓                 | ✓                |
| [Set up a single wireless network ID across regions](https://developer.android.com/work/dpc/network-telephony#set_up_a_single_wireless_network_id_across_regions)   | ✓                 | ✓                |
| [Specify a separate dialer for the work profile](https://developer.android.com/work/dpc/network-telephony#specify_a_separate_dialer_for_the_work_profile)           | ✓                 |                  |

## Access work contacts across profiles

EMMs can allow a user's personal profile to access their work contacts so that
a user's personal and work contacts are accessible through local search and
remote directory lookup. On personal devices, a single dialer in the personal
profile can make and receive personal calls as well as work calls. In addition,
work contacts are well integrated into the system UI. If the work profile is
encrypted, its data isn't available to the personal profile.

### Integrated with system UI

The system UI indicates incoming work calls using a briefcase icon. The
[callLog](https://developer.android.com/reference/android/provider/CallLog) also shows the
icon to designate incoming and outgoing work calls. The personal dialer and
contact apps can display a work contact's caller ID information using a remote
directory lookup, so it isn't required that the contact is already synced on the
local device. The messaging app can do local caller ID and search.

The [Android Compatibility Definition
Document](https://source.android.com/compatibility/) (CDD) includes requirements
for work contacts to display in the default dialer, and requirements that
contacts and messaging apps are badged to indicate they're from the work
profile.

### Work contacts are accessible and searchable

The user can access and call work contacts from their personal profile, which
display in the search screen of the dialer app. The user can search for work
contacts---using autocomplete---that are synced locally to the device, and listed
through a remote directory lookup.

### Control work contacts in the primary profile

The DPC controls the permission to search work contacts. Running in profile owner
mode, the DPC manages the visibility of work contacts in the personal profile.
For more information, see [Build a device policy
controller](https://developer.android.com/work/dpc/build-dpc).

Searching work contacts by the personal profile is enabled by default.

- To see how the policy is set, use
  [DevicePolicyManager.getCrossProfileContactsSearchDisabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getCrossProfileContactsSearchDisabled(android.content.ComponentName)).

- To enable or disable searching work contacts by the personal profile, use
  [DevicePolicyManager.setCrossProfileContactsSearchDisabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileContactsSearchDisabled(android.content.ComponentName,%20boolean)).

## Ensure a secure network connection for work traffic

Running in either a device owner mode or profile owner mode, a device policy
controller can use an always-on Virtual Private Network (VPN) connection to
force applications to pass traffic through a specified VPN app that can't be
bypassed. Using an always-on VPN connection, the DPC can ensure that network
traffic from a work profile or managed device passes through a VPN service, and
without user intervention. This process creates a secure network connection for
continual traffic within a work profile.

### About always-on VPN connections

As part of the system framework, VPN routing is automatically managed so the
user can't bypass the VPN service. If the VPN service is disconnected while in
lockdown mode, traffic can't leak to the open Internet. For applications
implementing
[VpnService](https://developer.android.com/reference/android/net/VpnService),
always-on VPN provides a framework for managing a secure VPN connection through
a trusted server and keeping it up. The VPN service automatically restarts the
connection across app updates, regardless if the connection is over Wi-Fi or
cellular. And if the device reboots, the framework restarts the VPN connection.

The connection to the VPN service is transparent to the user. For a
company-owned device, the user isn't required to confirm a consent dialog for a
VPN in always-on mode. The user's VPN network settings allow for enabling an
always-on connection manually.

If [DISALLOW_CONFIG_VPN](https://developer.android.com/reference/android/os/UserManager#DISALLOW_CONFIG_VPN)
is `true`, the user is prevented from configuring the VPN. Enable
[DISALLOW_DEBUGGING_FEATURES](https://developer.android.com/reference/android/os/UserManager#DISALLOW_DEBUGGING_FEATURES)
to restrict users from overriding the always-on VPN using the adb debug command.
To prevent a user from uninstalling the VPN, call
[DevicePolicyManager.setUninstallBlocked](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUninstallBlocked(android.content.ComponentName,%20java.lang.String,%20boolean)).

### Set up the VPN service

The organization that uses your enterprise solution for Android sets up VPN.

1. Install a VPN app that implements [VpnService](https://developer.android.com/reference/android/net/VpnService). You can find active VPN services by using an intent filter that matches the action [VpnService.SERVICE_INTERFACE](https://developer.android.com/reference/android/net/VpnService#SERVICE_INTERFACE).
2. Declare a [VpnService](https://developer.android.com/reference/android/net/VpnService) in the app's manifest guarded by the permission [BIND_VPN_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VPN_SERVICE).
3. Configure the [VpnService](https://developer.android.com/reference/android/net/VpnService) so it's started by the system. Avoid setting the VPN app to start itself by listening for a system boot and controlling its own life cycle.
4. Set the [managed
   configurations](https://developer.android.com/work/managed-configurations.html) for the VPN app (see [example below](https://developer.android.com/work/dpc/network-telephony#example)).

### Enable the always-on VPN connection

The DPC can configure an always-on VPN connection through a specific app by
calling
[DevicePolicyManager.setAlwaysOnVpnPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAlwaysOnVpnPackage(android.content.ComponentName,%20java.lang.String,%20boolean)).

This connection is automatically granted and persists after a reboot. If
`lockdownEnabled` is false, network traffic may be unsecured from the time the
phone reboots and the VPN connects. This is useful if you don't want to stop
network connectivity whenever the VPN fails, or if the VPN is not essential.

### Verify the always-on VPN connection

The DPC can read the name of the package administering an always-on VPN
connection for the current user with
[DevicePolicyManager.getAlwaysOnVpnPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getAlwaysOnVpnPackage(android.content.ComponentName))`.`

If there's no such package, or the VPN was created within the system Settings
app, `null` is returned.

### Example

In the [TestDPC](https://github.com/googlesamples/android-testdpc) app, [AlwaysOnVpnFragment.java](https://github.com/googlesamples/android-testdpc/blob/master/app/src/main/java/com/afwsamples/testdpc/policy/networking/AlwaysOnVpnFragment.java) uses these APIs to enable the setting for an always-on VPN connection.

In the following example:

- The [managed
  configurations](https://developer.android.com/work/managed-configurations.html) of the VPN service are set by the [DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager) using its [setApplicationRestrictions()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictions(android.content.ComponentName,%20java.lang.String,%20android.os.Bundle)) method.
- Managed configurations use arbitrary key-value pairs and this example app uses them elsewhere to configure the VPN's network settings (see [Check Managed Configurations](https://developer.android.com/work/app-restrictions.html#check-configuration)).
- The example adds the Android package installer to a denylist so it doesn't update system packages over the VPN. All of the user's network traffic within the work profile or device goes through this VPN app, except the package installer; its updates use the open Internet.
- The `DevicePolicyManager` then enables the always-on VPN connection for the VPN package using [setAlwaysOnVpnPackage()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAlwaysOnVpnPackage(android.content.ComponentName,%20java.lang.String,%20boolean)), and enabling lockdown mode.

### Kotlin

```kotlin
// Set VPN's managed configurations
val config = Bundle().apply {
  putString(Extras.VpnApp.ADDRESS, "192.0.2.0")
  putString(Extras.VpnApp.IDENTITY, "vpn.account1")
  putString(Extras.VpnApp.CERTIFICATE, "keystore://auth_certificate")
  putStringArray(Extras.VpnApp.DENYLIST,
        arrayOf("com.android.packageinstaller"))
}

val dpm = getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager

val admin = myDeviceAdminReceiver.getComponentName(this)

// Name of package to update managed configurations
val vpnPackageName = "com.example.vpnservice"

// Associate managed configurations with DeviceAdminReceiver
dpm.setApplicationRestrictions(admin, vpnPackageName, config)

// Enable always-on VPN connection through VPN package
try {
  val lockdownEnabled = true
  dpm.setAlwaysOnVpnPackage(admin, vpnPackageName, lockdownEnabled)
} catch (ex: Exception) {
  throw PolicyException()
}
```

### Java

```java
// Set VPN's managed configurations
final Bundle config = new Bundle();
config.putString(Extras.VpnApp.ADDRESS, "192.0.2.0");
config.putString(Extras.VpnApp.IDENTITY, "vpn.account1");
config.putString(Extras.VpnApp.CERTIFICATE, "keystore://auth_certificate");
config.putStringArray(Extras.VpnApp.DENYLIST,
                      new String[]{"com.android.packageinstaller"});

DevicePolicyManager dpm = (DevicePolicyManager) getSystemService(Context.DEVICE_POLICY_SERVICE);

ComponentName admin = myDeviceAdminReceiver.getComponentName(this);

// Name of package to update managed configurations
final String vpnPackageName = "com.example.vpnservice";

// Associate managed configurations with DeviceAdminReceiver
dpm.setApplicationRestrictions(admin, vpnPackageName, config);

// Enable always-on VPN connection through VPN package
try {
  boolean lockdownEnabled = true;
  dpm.setAlwaysOnVpnPackage(admin, vpnPackageName, lockdownEnabled));
} catch (Exception ex) {
  throw new PolicyException(...);
}
```

## Set up a single wireless network ID across regions

Running in either a device owner mode or profile owner mode, a device policy
controller (DPC) can associate multiple certificate authority (CA) certificates
with a single wireless network configuration. With this configuration, a device
can connect to wireless access points that have the same network name, or
service set identifier (SSID), but are configured with different CA
certificates. This is useful if your organization's wireless networks are
located across multiple geographic regions, and each region requires a different
certificate authority. For example, legal signatures can require a local
authority that needs a regional CA.

**Note:** Android has supported
[setCaCertificate](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setCaCertificate(java.security.cert.X509Certificate))
since API 18 (Jelly Bean), but IT admins must provision their networks
separately with each CA to ensure devices have seamless authentication at each
access point, regardless of their region.

### Specify CA certificates to identify the server

To specify a list of X.509 certificates that identify the server using the same
SSID, include all relevant CAs in the wireless configuration using [WifiEnterpriseConfig.setCaCertificates()](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setCaCertificates(java.security.cert.X509Certificate%5B%5D)).

A server's certificate is valid if its CA matches one of the given certificates.
Default names are automatically assigned to the certificates and used within the
configuration. The
[WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager)
installs the certificate and automatically saves the configuration when the
network is enabled, and removes the certificate when the configuration is
deleted.

To get all the CA certificates associated with the wireless configuration, use
[WifiEnterpriseConfig.getCaCertificates()](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#getCaCertificates()) to return a list of
[X509Certificate](https://developer.android.com/reference/javax/security/cert/X509Certificate) objects.

### Add a wireless configuration using multiple CA certificates

1. Verify the server's identity:
   1. Load the X.509 CA certificates.
   2. Load the client's private key and certificate. See [Security with HTTPS and SSL](https://developer.android.com/training/articles/security-ssl.html) for an example of how to read a certificate file.
2. Create a new [WifiConfiguration](https://developer.android.com/reference/android/net/wifi/WifiConfiguration) and set its SSID and key management.
3. Set up the [WifiEnterpriseConfig](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig) instance on this `WifiConfiguration`.
   1. Identify the server with a list of [X509Certificate](https://developer.android.com/reference/java/security/cert/X509Certificate) objects using [setCaCertificates()](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setCaCertificate(java.security.cert.X509Certificate)).
   2. Set the client credentials, identity, and password.
   3. Set the Extensible Authentication Protocol (EAP) and Phase 2 method as part of establishing the connection.
4. Add the network with the [WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager).
5. Enable the network. WifiManager automatically saves the configuration during setup.

This example ties the steps together:  

### Kotlin

```kotlin
// Verify the server's identity
val caCert0 = getCaCert("cert0.crt")
val caCert1 = getCaCert("cert1.crt")
val clientKey = getClientKey()
val clientCert = getClientCert()

// Create Wi-Fi configuration
val wifiConfig = WifiConfiguration().apply {
  SSID = "mynetwork"
  allowedKeyManagement.set(KeyMgmt.WPA_EAP)
  allowedKeyManagement.set(KeyMgmt.IEEE8021X)

  // Set up Wi-Fi enterprise configuration
  enterpriseConfig.setCaCertificates(arrayOf<X509Certificate>(caCert0, caCert1))
  enterpriseConfig.setClientKeyEntry(clientKey, clientCert)
  enterpriseConfig.setIdentity("myusername")
  enterpriseConfig.setEapMethod(Eap.TLS)
  enterpriseConfig.setPhase2Method(Phase2.NONE)
}


// Add network
val wifiManager = getSystemService(Context.WIFI_SERVICE) as WifiManager
val netId = wifiManager.addNetwork(wifiConfig)

// Enable network
if (netId < 0) {
  // Error creating new network
} else {
  wifiManager.enableNetwork(netId, true)
}
```

### Java

```java
// Verify the server's identity
X509Certificate caCert0 = getCaCert("cert0.crt");
X509Certificate caCert1 = getCaCert("cert1.crt");
PrivateKey clientKey = getClientKey();
X509Certificate clientCert = getClientCert();

// Create Wi-Fi configuration
WifiConfiguration wifiConfig = new WifiConfiguration();
wifiConfig.SSID = "mynetwork";
wifiConfig.allowedKeyManagement.set(KeyMgmt.WPA_EAP);
wifiConfig.allowedKeyManagement.set(KeyMgmt.IEEE8021X);

// Set up Wi-Fi enterprise configuration
wifiConfig.enterpriseConfig.setCaCertificates(new X509Certificate[] {caCert0, caCert1});
wifiConfig.enterpriseConfig.setClientKeyEntry(clientKey, clientCert);
wifiConfig.enterpriseConfig.setIdentity("myusername");
wifiConfig.enterpriseConfig.setEapMethod(Eap.TLS);
wifiConfig.enterpriseConfig.setPhase2Method(Phase2.NONE);

// Add network
WifiManager wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
int netId = wifiManager.addNetwork(wifiConfig);

// Enable network
if (netId < 0) {
  // Error creating new network
} else {
  wifiManager.enableNetwork(netId, true);
}
```

## Specify a separate dialer for the work profile

You can allowlist a separate dialer application to be used in a work profile.
This can be the dialer itself, or a Voice over IP (VoIP) app that implements the
[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)
API for the calling backend. This provides the same integrated system UI dialing
experience to VoIP applications in the work profile, effectively making the work
dialer a core feature. Incoming calls to the work calling accounts are
differentiated from incoming calls to the personal calling accounts.

The user can choose to make and receive calls from the allowlisted work dialer
on a phone account. All calls made from that dialer, or incoming to the work
phone account, are recorded in the work profile's
[CallLog](https://developer.android.com/reference/android/provider/CallLog)
provider. The work dialer maintains a work-only call log with only access to
work contacts. Incoming circuit-switch calls are handled by the primary dialer
and stored in a personal call log. If a work profile is deleted, the call log
associated with that work profile is deleted as well, as with all work profile
data.

### Third-party apps must implement ConnectionService

Third-party VoIP apps that need to make phone calls and have those calls
integrated into the built-in phone app can implement the
[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)
API. This is required for any VoIP service used for work calling. These apps
benefit by having their calls treated like traditional cellular calls, for
example, they show up in the built-in system dialer and the call log. If the
app implementing
[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)
is installed in the work profile, it is only accessible by a dialer also
installed in that work profile.

Once the developer has implemented
[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService),
they should add it to the app's manifest file and register a
[PhoneAccount](https://developer.android.com/reference/android/telecom/PhoneAccount)
with the
[TelecomManager](https://developer.android.com/reference/android/telecom/TelecomManager).
A phone account represents a distinct method to place or receive phone calls,
and there can be multiple `PhoneAccounts` for each
`ConnectionService`. After the phone account is registered, the user
can enable it through the dialer settings.

### System UI integration and notifications

The system UI provides users with a consistent and integrated dialing experience
for third-party apps that use the
[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)
API as a backend to make calls. If using the app in a work profile, a briefcase
icon displays on incoming calls and in the status bar. An app that implements
`ConnectionService` that is installed in the work profile can use the
system dialer or build a separate work dialer. These can be a single app or
separate apps.

The dialer application determines if it's making or receiving a work call by
checking for the flag
[android.telecom.Call.Details.PROPERTY_ENTERPRISE_CALL](https://developer.android.com/reference/android/telecom/Call.Details#PROPERTY_ENTERPRISE_CALL).
If the call is a work call, the dialer indicates this to the user by adding a
work badge (the briefcase icon):  

### Kotlin

```kotlin
// Call placed through a work phone account. getCurrentCall() is defined by the
// dialer.
val call = getCurrentCall()
if (call.hasProperty(android.telecom.Call.Details.PROPERTY_ENTERPRISE_CALL)) {
  // Set briefcase icon
}
```

### Java

```java
// Call placed through a work phone account. getCurrentCall() is defined by the
// dialer.
Call call = getCurrentCall();
if (call.hasProperty(android.telecom.Call.Details.PROPERTY_ENTERPRISE_CALL)) {
  // Set briefcase icon
}
```