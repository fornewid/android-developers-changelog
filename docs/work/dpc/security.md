---
title: https://developer.android.com/work/dpc/security
url: https://developer.android.com/work/dpc/security
source: md.txt
---

The features in this guide describe security management capabilities you can
implement in your [device policy controller](https://developer.android.com/work/dpc/build-dpc) (DPC) app. This document
contains code samples and you can also use the [Test DPC](https://github.com/googlesamples/android-testdpc/) app as
a source of sample code for Android's enterprise features.

A DPC app can run in profile owner mode on personal devices or in device owner
mode on fully managed devices. This table indicates which features are available
when the DPC runs in [profile owner mode or device owner mode](https://developers.google.com/android/work/play/emm-api/prov-devices#modes_of_operation):

| **Feature** | **Profile owner** | **Device owner** |
|---|---|---|
| [Disable access to apps](https://developer.android.com/work/dpc/security#disable_access_to_apps) | ✓ | ✓ |
| [Block apps from unknown sources](https://developer.android.com/work/dpc/security#unknown_sources) | ✓ | ✓ |
| [Restrict accounts in Google Play](https://developer.android.com/work/dpc/security#google_play_accounts) | ✓ | ✓ |
| [Enable enterprise factory reset protection](https://developer.android.com/work/dpc/security#enable_enterprise_frp) |   | ✓ |
| [Monitor enterprise process logs and remote bug reports](https://developer.android.com/work/dpc/security#monitor_logs_and_bugreports) |   | ✓ |
| [Grant access and remove access to a client certificate](https://developer.android.com/work/dpc/security#grant_and_remove_access_to_a_cc) | ✓ | ✓ |
| [Secure passcode reset](https://developer.android.com/work/dpc/security#secure_passcode_reset) | ✓ | ✓ |
| [Work profile security challenge](https://developer.android.com/work/dpc/security#work_profile_security_challenge) | ✓ |   |

## Disable access to apps

For organizations who want to block employees from playing games or watching
YouTube on their Android-powered device during certain times of the day, or
certain days of the week, a DPC can temporarily disable access to apps.

To disable access to apps, a DPC running in device owner or profile owner mode
configures [`setPackagesSuspended()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPackagesSuspended(android.content.ComponentName,%20java.lang.String%5B%5D,%20boolean)), and then the selected app acts as if
it's disabled (the Google launcher grays out the app). When a user taps the app,
they see a system dialog saying that the app is suspended.

While an app is suspended, it can't start activities, and notifications to the
package are suppressed. Suspended packages don't appear in the [overview
screen](https://developer.android.com/guide/components/recents), they can't show dialogs (including toasts and snackbars), and they
can't play audio or vibrate the device.

Launchers can find out if an app is suspended by calling the
[`isPackageSuspended()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isPackageSuspended(android.content.ComponentName,java.lang.String)) method. For details on how to configure app
suspension, see [`setPackagesSuspended`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPackagesSuspended(android.content.ComponentName,%20java.lang.String%5B%5D,%20boolean)).

## Block apps from unknown sources

Apps that aren't installed from Google Play (or other trusted app stores) are
called *apps from unknown sources*. Devices and data can be at increased risk
when people install these apps.

To prevent somebody installing apps from unknown sources, admin components of
fully managed devices and work profiles can add the
[`DISALLOW_INSTALL_UNKNOWN_SOURCES`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES) user restriction.

### Work-profile device-wide restriction

When the admin of a work profile adds [`DISALLOW_INSTALL_UNKNOWN_SOURCES`](https://developer.android.com/reference/android/os/UserManager#DISALLOW_INSTALL_UNKNOWN_SOURCES),
the restriction only applies to the work profile. However, the admin of a work
profile can place a device-wide restriction by setting a
[managed configuration](https://developer.android.com/work/managed-configurations) for Google Play. The device-wide restriction is
available in Android 8.0 (or higher) when the installed Google Play app is
version 80812500 or higher.

To restrict app installs to Google Play, follow these steps:

1. Set a managed configuration bundle for the Google Play package `com.android.vending`.
2. In the bundle, put a boolean value for the `verify_apps:device_wide_unknown_source_block` key.
3. Add the [`ENSURE_VERIFY_APPS`](https://developer.android.com/reference/android/os/UserManager#ENSURE_VERIFY_APPS) user restriction.

The following example shows how you can check that Google Play supports this
setting and set the value to `true`:  

### Kotlin

```kotlin
internal val DEVICE_WIDE_UNKNOWN_SOURCES = "verify_apps:device_wide_unknown_source_block"
internal val GOOGLE_PLAY_APK = "com.android.vending"

// ...

// Add the setting to Google Play's existing managed config. Supported in
// Google Play version 80812500 or higher--older versions ignore unsupported
// settings.
val dpm = context.getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager
var existingConfig = dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK)
val newConfig = Bundle(existingConfig)
newConfig.putBoolean(DEVICE_WIDE_UNKNOWN_SOURCES, true)
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig)

// Make sure that Google Play Protect verifies apps.
dpm.addUserRestriction(adminName, UserManager.ENSURE_VERIFY_APPS)
dpm.addUserRestriction(adminName, UserManager.DISALLOW_INSTALL_UNKNOWN_SOURCES)
```

### Java

```java
static final String DEVICE_WIDE_UNKNOWN_SOURCES =
    "verify_apps:device_wide_unknown_source_block";
static final String GOOGLE_PLAY_APK = "com.android.vending";

// ...


// Add the setting to Google Play's existing managed config. Supported in
// Google Play version 80812500 or higher--older versions ignore unsupported
// settings.
DevicePolicyManager dpm =
    (DevicePolicyManager) context.getSystemService(Context.DEVICE_POLICY_SERVICE);
Bundle existingConfig =
    dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK);
Bundle newConfig = new Bundle(existingConfig);
newConfig.putBoolean(DEVICE_WIDE_UNKNOWN_SOURCES, true);
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig);

// Make sure that Google Play Protect verifies apps.
dpm.addUserRestriction(adminName, UserManager.ENSURE_VERIFY_APPS);
dpm.addUserRestriction(adminName, UserManager.DISALLOW_INSTALL_UNKNOWN_SOURCES);
```

The user interface in the system settings remains active but the system blocks
app installation. This restriction affects future installations---previously
installed apps remain on the device. Device users can continue to install apps
into the personal profile using the [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb).

To learn more about unknown sources, read [Alternative distribution
options](https://developer.android.com/distribute/marketing-tools/alternative-distribution#unknown-sources).

## Restrict accounts in Google Play

Sometimes an organization might want to allow people to add personal Google
Accounts (to read mail in Gmail for example) but doesn't want the personal
account to install apps. Your DPC can set a list of accounts people can use in
Google Play.

Admin components of fully managed devices or work profiles can restrict the
accounts by setting a [managed configuration](https://developer.android.com/work/managed-configurations) for Google Play. The account
restriction is available when the installed Google Play app is version 80970100
or higher.

To limit the accounts in Google Play, do the following:

1. Set a managed configuration bundle for the Google Play package `com.android.vending`.
2. In the bundle, put the comma-separated email addresses as a string value for the `allowed_accounts` key.

The following example shows how you can limit accounts:  

### Kotlin

```kotlin
internal val ALLOWED_ACCOUNTS = "allowed_accounts"
internal val GOOGLE_PLAY_APK = "com.android.vending"

// ...

// Limit Google Play to one work and one personal account. Use
// a comma-separated list of account email addresses (usernames).
val googleAccounts = "ali@gmail.com,ali.connors@example.com"

// Supported in Google Play version 80970100 or higher.
val existingConfig = dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK)
val newConfig = Bundle(existingConfig)
newConfig.putString(ALLOWED_ACCOUNTS, googleAccounts)
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig)
```

### Java

```java
static final String ALLOWED_ACCOUNTS = "allowed_accounts";
static final String GOOGLE_PLAY_APK = "com.android.vending";

// ...


// Limit Google Play to one work and one personal account. Use
// a comma-separated list of account email addresses (usernames).
String googleAccounts = "ali@gmail.com,ali.connors@example.com";

// Supported in Google Play version 80970100 or higher.
Bundle existingConfig =
    dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK);
Bundle newConfig = new Bundle(existingConfig);
newConfig.putString(ALLOWED_ACCOUNTS, googleAccounts);
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig);
```

To limit Google Play to just the work account, set `allowed_accounts` to the
single managed account as soon as your DPC knows the account's email address. An
empty string prevents people using any account in Google Play.

## Enable enterprise factory reset protection

Using enterprise factory reset protection, organizations can specify which
Google Accounts can provision a device that has been factory reset.

Consumer factory reset protection is designed to deter device theft. Before
allowing anyone to provision the device after unauthorized factory reset (such
as using an EMM), the setup wizard requires the user to authenticate against any
Google Accounts that were previously on the personal profile of the device.

In an enterprise environment, factory reset is an important tool for managing
employee devices when an employee leaves the organization. However, if the
organization doesn't know an employee's account credentials, factory reset
protection can block the organization's ability to issue a device to another
employee.
| **Note:** Factory reset protection is disabled if OEM unlocking is enabled in Developer Options.

### Control provisioning after a factory reset

When running in device owner mode, your DPC can use
[`setFactoryResetProtectionPolicy()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setFactoryResetProtectionPolicy(android.content.ComponentName,%20android.app.admin.FactoryResetProtectionPolicy)) to control which accounts are
authorized to provision a device after a factory reset. If this configuration
is set to `null` or set to an empty list, the accounts authorized to provision
a device after a factory reset are the accounts on the personal profile of the
device.

A DPC can configure these accounts throughout the lifetime of a fully managed
device.
| **Note:** The DPC uses the `userID` value to configure which accounts can provision a device after a factory reset.

1. The IT admin can use the [`people.get`](https://developers.google.com/people/api/rest/v1/people/get) method from the People API [with the special value `me`](https://developers.google.com/people/api/rest/v1/people/get?apix_params=%7B%22resourceName%22:%22people/me%22,%22personFields%22:%22names%22%7D). This retrieves the `userId` for the logged in account. The `userID` is returned in the `resourceName` key in the form `people/[userId]` as an integer string. Newly-created accounts might not be available for factory reset purposes for 72 hours.
2. You may also want to enable one or more IT admins to unlock the device after a factory reset. Have each of these IT admins log into their Google Account and also follow step 1 and share their `userId` with you, so that you can add these `userIds` to the List in the next step.
3. The DPC sets an appropriate app restriction using `setFactoryResetProtectionPolicy()` to set the List of `userId` that can provision a factory reset device.
4. The DPC enables the accounts that can provision devices after a factory reset by sending the broadcast `com.google.android.gms.auth.FRP_CONFIG_CHANGED` as an explicit intent to prevent being dropped due to background restrictions.

### Kotlin

```kotlin
const val ACTION_FRP_CONFIG_CHANGED =
    "com.google.android.gms.auth.FRP_CONFIG_CHANGED"
const val GMSCORE_PACKAGE = "com.google.android.gms"

// ...

// List of userId that can provision a factory reset device.
// You can use the value returned calling people/me endpoint.
val accountIds = listOf("000000000000000000000")

dpm.setFactoryResetProtectionPolicy(
    adminName,
    FactoryResetProtectionPolicy.Builder()
        .setFactoryResetProtectionAccounts(accountIds)
        .setFactoryResetProtectionEnabled(true)
        .build()
)

val frpChangedIntent = Intent(ACTION_FRP_CONFIG_CHANGED)

frpChangedIntent.setPackage(GMSCORE_PACKAGE)
context.sendBroadcast(frpChangedIntent)
```

### Java

```java
static final String ACTION_FRP_CONFIG_CHANGED =
    "com.google.android.gms.auth.FRP_CONFIG_CHANGED";
static final String GMSCORE_PACKAGE = "com.google.android.gms";

// ...

// List of userId that can provision a factory reset device.
// You can use the value returned calling people/me endpoint.
List<String> accountIds = new ArrayList<String>();
accountIds.add("000000000000000000000");

dpm.setFactoryResetProtectionPolicy(
    adminName,
    new FactoryResetProtectionPolicy.Builder()
        .setFactoryResetProtectionAccounts(accountIds)
        .setFactoryResetProtectionEnabled(true)
        .build());

Intent frpChangedIntent = new Intent(ACTION_FRP_CONFIG_CHANGED);

frpChangedIntent.setPackage(GMSCORE_PACKAGE);
context.sendBroadcast(frpChangedIntent);
```

#### Legacy

For devices that cannot use `setFactoryResetProtectionPolicy()`, introduced with
API Level 30, your DPC can use [`setApplicationRestrictions`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictions(android.content.ComponentName,%20java.lang.String,%20android.os.Bundle)) to add
the chosen accounts to the `factoryResetProtectionAdmin` managed configuration
for the `com.google.android.gms` package.  

### Kotlin

```kotlin
const val GOOGLE_PLAY_APK = "com.android.vending"
const val FACTORY_RESET_PROTECTION_ADMIN = "factoryResetProtectionAdmin"
const val DISABLE_FACTORY_RESET_PROTECTION_ADMIN = "disableFactoryResetProtectionAdmin"
const val GMSCORE_PACKAGE = "com.google.android.gms"

// ...

val existingConfig = dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK)
val newConfig = Bundle(existingConfig)
newConfig.putBoolean(DISABLE_FACTORY_RESET_PROTECTION_ADMIN, false)
newConfig.putString(FACTORY_RESET_PROTECTION_ADMIN, googleAccounts)
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig)

val frpChangedIntent = Intent(ACTION_FRP_CONFIG_CHANGED)

frpChangedIntent.setPackage(GMSCORE_PACKAGE)
context.sendBroadcast(frpChangedIntent)
```

### Java

```java
static final String GOOGLE_PLAY_APK = "com.android.vending";
static final String FACTORY_RESET_PROTECTION_ADMIN = "factoryResetProtectionAdmin";
static final String DISABLE_FACTORY_RESET_PROTECTION_ADMIN = "disableFactoryResetProtectionAdmin";
static final String GMSCORE_PACKAGE = "com.google.android.gms";

// ...

Bundle existingConfig =
        dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK);
Bundle newConfig = new Bundle(existingConfig);
newConfig.putBoolean(DISABLE_FACTORY_RESET_PROTECTION_ADMIN, false);
newConfig.putStringArray(FACTORY_RESET_PROTECTION_ADMIN,
        accountIds.toArray(new String[accountIds.size()]));
dpm.setApplicationRestrictions(adminName, GOOGLE_PLAY_APK, newConfig);

Intent frpChangedIntent = new Intent(ACTION_FRP_CONFIG_CHANGED);

frpChangedIntent.setPackage(GMSCORE_PACKAGE);
context.sendBroadcast(frpChangedIntent);
```

### Disable enterprise factory reset protection

To disable factory reset protection, your DPC can use
`setFactoryResetProtectionPolicy()`passing the value `null`.  

### Kotlin

```kotlin
const val ACTION_FRP_CONFIG_CHANGED =
    "com.google.android.gms.auth.FRP_CONFIG_CHANGED"
const val GMSCORE_PACKAGE = "com.google.android.gms"

// ...

dpm.setFactoryResetProtectionPolicy(adminName, null)

val frpChangedIntent = Intent(ACTION_FRP_CONFIG_CHANGED)

frpChangedIntent.setPackage(GMSCORE_PACKAGE)
context.sendBroadcast(frpChangedIntent)
```

### Java

```java
static final String ACTION_FRP_CONFIG_CHANGED =
    "com.google.android.gms.auth.FRP_CONFIG_CHANGED";
static final String GMSCORE_PACKAGE = "com.google.android.gms";

// ...

dpm.setFactoryResetProtectionPolicy(adminName, null);

Intent frpChangedIntent = new Intent(ACTION_FRP_CONFIG_CHANGED);

frpChangedIntent.setPackage(GMSCORE_PACKAGE);
context.sendBroadcast(frpChangedIntent);
```

#### Legacy

For devices that cannot use `setFactoryResetProtectionPolicy()`, introduced with
API Level 30, your DPC can use [`setApplicationRestrictions`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setApplicationRestrictions(android.content.ComponentName,%20java.lang.String,%20android.os.Bundle)) to set a key
value of `true` in the `disableFactoryResetProtectionAdmin` managed
configuration for the `com.google.android.gms` package.
**Note:** Simply leaving `factoryResetProtectionAdmin` managed configuration unset does *not* disable factory reset protection.  

### Kotlin

```kotlin
const val GOOGLE_PLAY_APK = "com.android.vending"
const val FACTORY_RESET_PROTECTION_ADMIN = "factoryResetProtectionAdmin"
const val DISABLE_FACTORY_RESET_PROTECTION_ADMIN = "disableFactoryResetProtectionAdmin"
const val GMSCORE_PACKAGE = "com.google.android.gms"

// ...

val existingConfig = dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK)
val newConfig = Bundle(existingConfig)
newConfig.putBoolean(DISABLE_FACTORY_RESET_PROTECTION_ADMIN, true)

dpm.setApplicationRestrictions(
    adminName, GOOGLE_PLAY_SERVICES_PACKAGE, restrictions
)

val frpChangedIntent = Intent(ACTION_FRP_CONFIG_CHANGED)

frpChangedIntent.setPackage(GMSCORE_PACKAGE)
context.sendBroadcast(frpChangedIntent)
```

### Java

```java
static final String GOOGLE_PLAY_APK = "com.android.vending";
static final String FACTORY_RESET_PROTECTION_ADMIN = "factoryResetProtectionAdmin";
static final String DISABLE_FACTORY_RESET_PROTECTION_ADMIN = "disableFactoryResetProtectionAdmin";
static final String GMSCORE_PACKAGE = "com.google.android.gms";

// ...

Bundle existingConfig =
        dpm.getApplicationRestrictions(adminName, GOOGLE_PLAY_APK);
Bundle newConfig = new Bundle(existingConfig);
newConfig.putBoolean(DISABLE_FACTORY_RESET_PROTECTION_ADMIN, true);

dpm.setApplicationRestrictions(
    adminName, GOOGLE_PLAY_SERVICES_PACKAGE, restrictions);

Intent frpChangedIntent = new Intent(ACTION_FRP_CONFIG_CHANGED);

frpChangedIntent.setPackage(GMSCORE_PACKAGE);
context.sendBroadcast(frpChangedIntent);
```

## Monitor enterprise process logs and remote bug reports

In your EMM console, an admin can monitor fully managed devices using enterprise
process logs and remote bug reports.

### Log enterprise device activity

A DPC running in device owner mode can identify suspicious activity by remotely
tracking device activity, including app launches, Android Debug Bridge (adb)
activity, and screen unlocks. Process logs don't require user consent.

To enable or disable logging, a DPC calls [`setSecurityLoggingEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSecurityLoggingEnabled(android.content.ComponentName,%20boolean)).

When a new batch of logs is available, a `DeviceAdminReceiver` receives the
[`onSecurityLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onSecurityLogsAvailable(android.content.Context,android.content.Intent)) callback. To retrieve the logs (after
receiving the callback), a DPC calls [`retrieveSecurityLogs()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrieveSecurityLogs(android.content.ComponentName)).

DPCs can also call [`retrievePreRebootSecurityLogs()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrievePreRebootSecurityLogs(android.content.ComponentName)) to fetch security
logs generated in the previous reboot cycle. This is the interval between the
last device reboot and its preceding reboot. Devices that don't support
`retrieveSecurityLogs()` returns `null`. If your app retrieves logs using both
`retrievePreRebootSecurityLogs()` and `retrieveSecurityLogs()`, you need to
check for duplicate entries.


Note: This feature only logs activity on fully managed devices with a single
user or [affiliated users](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users) on the device. This feature doesn't work on
personal devices, because it logs device-wide activity.

This setting can be useful in post-security-event auditing because it logs the
following types of actions:

- Every time the app is freshly started. This could help identify if there's malware that starts with a compromised app.
- Unsuccessful unlock attempts on a device. This could identify if there are several failed unlock attempts in a short period of time.
- Potentially harmful adb commands when a user connects the device to a computer using a USB cable.

For details on how to read logs, see [`SecurityLog`](https://developer.android.com/reference/android/app/admin/SecurityLog).

While you're developing and testing, you can force the system to make any
existing security logs available to your DPC---you don't have to wait for a full
batch. In Android 9.0 (API level 28) or higher, run the following
[Android Debug Bridge](https://developer.android.com/studio/command-line/adb) (adb) command in your terminal:  

```
adb shell dpm force-security-logs
```

The system limits how frequently you can use the tool and reports any
intentional slowing in the terminal output. If there are logs available, your
DPC receives the [`onSecurityLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onSecurityLogsAvailable(android.content.Context,android.content.Intent)) callback.

### Remotely request a bug report

A DPC running in device owner mode can remotely request bug reports for user
devices with only one user or [affiliated users](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users). The bug report captures
the device activity the exact moment the bug report is requested, but may also
include activity from the previous few hours, depending on how often the logcat
buffer refreshes.

To remotely request bug reports, the DPC calls [`requestBugreport()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#requestBugreport(android.content.ComponentName)):

- If a user accepts sharing the bug report, the DPC receives the bug report using [`onBugreportShared()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onBugreportShared(android.content.Context,%20android.content.Intent,%20java.lang.String)).
- If a user denies sharing the bug report, the DPC receives a sharing request denied message using [`onBugreportSharingDeclined()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onBugreportSharingDeclined(android.content.Context,%20android.content.Intent)).
- If the bug report fails, the DPC sees [`onBugreportFailed()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onBugreportFailed(android.content.Context,%20android.content.Intent,%20int)) with [`BUGREPORT_FAILURE_FAILED_COMPLETING`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#BUGREPORT_FAILURE_FAILED_COMPLETING) or [`BUGREPORT_FAILURE_FILE_NO_LONGER_AVAILABLE`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#BUGREPORT_FAILURE_FILE_NO_LONGER_AVAILABLE).

## Grant access and remove access to a client certificate

If a DPC running in profile owner or device owner mode grants a third-party app
the ability to manage certificates, the app can grant itself access to
certificates it installs without intervention by a user. To install a
certificate that all apps in a profile can access, use [`installKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName,%20java.security.PrivateKey,%20java.security.cert.Certificate,%20java.lang.String)).

For which parameters to configure, see [`installKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName,%20java.security.PrivateKey,%20java.security.cert.Certificate,%20java.lang.String)). This feature
works in conjunction with the existing API for managing certificates.

#### Deployment scenario

Without the `installKeyPair()` method:

- Users need to tap the name of the certificate and tap **Allow** each time they want to grant access to a certificate.
- Users see a prompt when installing a certificate and must name the certificate.

With the `installKeyPair()` method:

- Users don't need to tap **Allow** each time they want to grant access to a certificate.
- Users can't rename certificates.
- Admins have more control in that they can block certificates for apps that shouldn't have access to specific certificates.

### Remove a client certificate

After granting access to a client certificate, to remotely remove client
certificates installed through [`installKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName,%20java.security.PrivateKey,%20java.security.cert.Certificate,%20java.lang.String)), call
[`removeKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeKeyPair(android.content.ComponentName,%20java.lang.String)).

A DPC running in device owner mode or profile owner mode, or delegated
certificate installer can call [`removeKeyPair()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#removeKeyPair(android.content.ComponentName,%20java.lang.String)). This removes a
certificate and private key pair installed under a given private key alias.

#### Deployment scenario

Use this feature if an organization is migrating to a more secure form of client
certificate. If an admin rolls out a new certificate, and its distribution
takes a significant amount of time, the admin can revoke the deprecated
certificates after the migration is complete.

## Secure passcode reset

Your DPC can reset a user's password by authorizing the change with a
preregistered, secure token. Device owners and profile owners can call secure
passcode reset APIs to change the password of devices and work profiles
respectively. Secure passcode reset replaces [`resetPassword()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPassword(java.lang.String,%20int)) with the
following improvements:

- Your DPC can reset the passcode before the user unlocks the device or profile after a reboot on devices using [file-based encryption](https://source.android.com/security/encryption/file-based).
- The Android Keystore retains [user-authenticated keys](https://developer.android.com/training/articles/keystore#UserAuthentication) after a passcode reset.

You should use secure passcode reset if your DPC build targets Android 8.0 (API
level 26) or higher. Calling `resetPassword()` throws a
[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException) in DPCs targeting Android 8.0 or higher so you might
need to update your DPC.

### Set and activate a token

Your DPC needs to set and activate a token before resetting a password. Because
your DPC might not be able to use the token straightaway, you set the token
ahead of the time an IT admin might need to use it.

A password reset token is a cryptographically strong random value and needs to
be at least 32 bytes long. Create a token for each device and profile---don't
reuse or share your generated tokens.
| **Warning:** Treat the token as you would treat user credentials. Never store the token on the device as plain text, especially in device encrypted storage. Your organization should carefully consider how you store the tokens on a server and who gets access to the tokens. Tokens might be subject to legal requests for device access.

We recommend storing tokens, or the means to decrypt an encrypted token, on a
server. If you store tokens locally in credential encrypted storage, your DPC
can't reset the password until the user unlocks the device or profile. If you
store the tokens locally in device encrypted storage, which becomes compromised,
an attacker may use the token to gain access to a work profile or a primary
user.

You can generate a new token in your DPC or fetch a token from a server. The
example below shows a DPC generating a token itself and reporting it to a
server:  

### Kotlin

```kotlin
val token = ByteArray(32)

// Generate a new token
val random = SecureRandom()
random.nextBytes(token)

// Set the token to use at a later date
val success: Boolean
success = dpm.setResetPasswordToken(DeviceAdminReceiver.getComponentName(context), token)

// Activate the token and update success variable...

// Store the token on a server
if (success) {
 sendTokenToServer(token)
}
```

### Java

```java
byte token[] = new byte[32]; // Minimum size token accepted

// Generate a new token
SecureRandom random = new SecureRandom();
random.nextBytes(token);

// Set the token to use at a later date
boolean success;
success = dpm.setResetPasswordToken(DeviceAdminReceiver.getComponentName(getContext()), token);

// Activate the token and update success variable ...

// Store the token on a server
if (success) {
 sendTokenToServer(token);
}
```

In most cases, your DPC needs to activate a token after setting it. But, when
the user doesn't have a lock screen password, the system activates a token
straightaway. To activate a token, ask the user to confirm their credentials.
Your DPC can call the `KeyguardManager` method
[`createConfirmDeviceCredentialIntent()`](https://developer.android.com/reference/android/app/KeyguardManager#createConfirmDeviceCredentialIntent(java.lang.CharSequence,%20java.lang.CharSequence)) to get an `Intent` that starts the
confirmation. Explain to the device user in the user interface, why you're
asking them to authenticate. The snippet below shows how you might activate a
token in your DPC:  

### Kotlin

```kotlin
// In your DPC, you'll need to localize the user prompt
val ACTIVATE_TOKEN_PROMPT = "Use your credentials to enable remote password reset"
val ACTIVATE_TOKEN_REQUEST = 1

// Create or fetch a token and set it in setResetPasswordToken() ...
val keyguardManager = context.getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager
val confirmIntent = keyguardManager.createConfirmDeviceCredentialIntent(null, ACTIVATE_TOKEN_PROMPT)

if (confirmIntent != null) {
 startActivityForResult(confirmIntent, ACTIVATE_TOKEN_REQUEST)
 // Check your onActivityResult() callback for RESULT_OK
} else {
 // Null means the user doesn't have a lock screen so the token is already active.
 // Call isResetPasswordTokenActive() if you need to confirm
}
```

### Java

```java
// In your DPC, you'll need to localize the user prompt
static final String ACTIVATE_TOKEN_PROMPT =
 "Use your credentials to enable remote password reset";
static final int ACTIVATE_TOKEN_REQUEST = 1;

// Create or fetch a token and set it in setResetPasswordToken() ...

KeyguardManager keyguardManager = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
Intent confirmIntent = keyguardManager.createConfirmDeviceCredentialIntent(
  null, ACTIVATE_TOKEN_PROMPT);

if (confirmIntent != null) {
 startActivityForResult(confirmIntent, ACTIVATE_TOKEN_REQUEST);
 // Check your onActivityResult() callback for RESULT_OK
} else {
 // Null means the user doesn't have a lock screen so the token is already active.
 // Call isResetPasswordTokenActive() if you need to confirm
}
```

You need to activate a token your DPC sets before the device reboots. Android
stores an unactivated token in memory and doesn't persist the token after a
reboot. If the user reboots the device before activating a token, your DPC can
set the same token again or generate a new token.

Your DPC can confirm that a token is active by calling
[`isResetPasswordTokenActive()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isResetPasswordTokenActive(android.content.ComponentName)) and checking the result is `true`.

After your DPC sets and activates a token, it's valid until your DPC deletes or
replaces the token (or the device is factory reset). The token is independent of
the password and isn't affected by the user changing or clearing the password.

### Delete a token

You can call [`clearResetPasswordToken()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#clearResetPasswordToken(android.content.ComponentName)) to delete a token that your DPC
set earlier. You might need to revoke a compromised token or you might want to
remove the ability to reset the password. The sample below shows how you can do
this in your DPC:  

### Kotlin

```kotlin
val dpm = getDpm()
val admin = DeviceAdminReceiver.getComponentName(requireActivity())

// Clear the token
if (!dpm.clearResetPasswordToken(admin)) {
 // Report the failure and possibly try later ...
}
```

### Java

```java
DevicePolicyManager dpm = getDpm();
ComponentName admin = DeviceAdminReceiver.getComponentName(getActivity());

// Clear the token
if (!dpm.clearResetPasswordToken(admin)) {
 // Report the failure and possibly try later ...
}
```

### Reset the password

When an IT admin needs to reset the password, call
[`resetPasswordWithToken()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPasswordWithToken(android.content.ComponentName,%20java.lang.String,%20byte%5B%5D,%20int)) and pass the token your DPC set and activated
in advance:  

### Kotlin

```kotlin
val token: ByteArray = getTokenFromServer()
val newPassword = "password"

try {
 val result: Boolean = dpm.resetPasswordWithToken(
 DeviceAdminReceiver.getComponentName(requireContext()),
 newPassword,
 token,
 0
 )

 if (result) {
 // The password is now 'password'
 } else {
 // Using 'password' doesn't meet password restrictions
 }
} catch (e: IllegalStateException) {
 // The token doesn't match the one set earlier.
}
```

### Java

```java
byte token[] = getTokenFromServer();
String newPassword = "password";

try {
 boolean result = dpm.resetPasswordWithToken(
  DeviceAdminReceiver.getComponentName(getContext()), newPassword, token, 0);

 if (result) {
 // The password is now 'password'
 } else {
 // Using `password` doesn't meet password restrictions
 }
} catch (IllegalStateException e) {
 // The token doesn't match the one set earlier.
}
```

A call to `resetPasswordWithToken()` returns `false`, and the password doesn't
change, when the new password doesn't meet the following constraints:

- The number of characters meets any minimum password length constraint. Call [`getPasswordMinimumLength()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPasswordMinimumLength(android.content.ComponentName)) to know if an IT admin set a length constraint.
- The range and complexity of characters in the password meets a composition constraint. Call [`getPasswordQuality()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getPasswordQuality(android.content.ComponentName)) to know if an IT admin set a composition constraint.

If the password quality constraints don't require a password to be set, you can
pass `null` or an empty string to `resetPasswordWithToken()` to remove the
password.

## Work profile security challenge

A DPC running in profile owner mode can require users to specify a security
challenge for apps running in the work profile. The system shows the security
challenge when the user attempts to open any work apps. If the user successfully
completes the security challenge, the system unlocks the work profile and
decrypts it, if necessary.
| **Note:** The separate work challenge is a feature that a user can also set, and if the user chooses the unified lock option, they can access work apps once they unlock their personal lock on the device.

### How work profile security challenge works

1. If a DPC sends an [`ACTION_SET_NEW_PASSWORD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_SET_NEW_PASSWORD) intent, the system prompts the user to set up a security challenge.
2. The DPC can also send an[`ACTION_SET_NEW_PARENT_PROFILE_PASSWORD`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ACTION_SET_NEW_PARENT_PROFILE_PASSWORD) intent to prompt the user to set a device lock.

A DPC can set the password policies for the work challenge differently from the
policies for other device passwords. For example, the minimum length for the
device challenge response can be different from the length required for other
passwords. A DPC sets the challenge policies using the usual
[`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager) methods, such as [`setPasswordQuality()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordQuality(android.content.ComponentName,%20int)) and
[`setPasswordMinimumLength()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPasswordMinimumLength(android.content.ComponentName,%20int)).

### Considerations

- The DPC can reset the password on the work profile, but can't reset the device (personal) password. If a user chooses to set work and personal passwords to be the same, then [`resetPassword()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPassword(java.lang.String,%20int)) on the work profile causes the password to be reset on work profile only, and the password won't be the same as the one for the device lock screen.
- A DPC can customize the credentials screen for the work challenge by using [`setOrganizationColor()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setOrganizationColor(android.content.ComponentName,%20int)) and [`setOrganizationName()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setOrganizationName(android.content.ComponentName,%20java.lang.CharSequence)).
- Device admins can't use [`resetPassword()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#resetPassword(java.lang.String,%20int)) to clear passwords or change ones that are already set. Device admins can still set a password, but only when the device has no password, PIN, or pattern.

For additional information, see [`getParentProfileInstance()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getParentProfileInstance(android.content.ComponentName)) and reference
documentation under [`DevicePolicyManager`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager).