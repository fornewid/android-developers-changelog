---
title: https://developer.android.com/about/versions/17/behavior-changes-all
url: https://developer.android.com/about/versions/17/behavior-changes-all
source: md.txt
---

<br />

The Android 17 platform includes behavior changes that might affect your app.
The following behavior changes apply to *all apps* when they run on Android 17,
regardless of [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target). You should test your app and then modify
it as needed to support these changes, where applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 17](https://developer.android.com/about/versions/17/behavior-changes-17).

> [!NOTE]
> **Note:** This page lists some of the more important changes. For more detailed information, see the [Android 17 release notes](https://developer.android.com/about/versions/17/release-notes).

## Core functionality

Android 17 (API level 37) includes the following changes that modify or
expand various core capabilities of the Android system.

### App memory limits

Android 17 introduces app memory limits based on the device's total RAM
to create a more stable and deterministic environment for your apps and
Android users. In Android 17, limits are set conservatively to establish system
baselines, targeting extreme memory leaks and other outliers before they trigger
system-wide instability resulting in UI stuttering, higher battery drain, and
apps being killed. While we anticipate minimal impact on the vast majority of
app sessions, we recommend the [following memory best practices](https://developer.android.com/topic/performance/memory),
including establishing a baseline for memory.

> [!NOTE]
> **Note:** Memory limits are only imposed on a subset of Android devices.

You can determine if your app session was impacted by calling
[`getDescription`](https://developer.android.com/reference/android/app/ApplicationExitInfo#getDescription%28%29) in [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo); if your app was
affected, the exit reason will be [`REASON_OTHER`](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_OTHER) and
the description will contain the string `"MemoryLimiter:AnonSwap"` along with
other information. You can also use [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) with
[`TRIGGER_TYPE_ANOMALY`](https://developer.android.com/about/versions/17/features#anomaly-profiling-trigger) to get heap dumps that are collected when the
memory limit is hit.

The [Manage your app's memory](https://developer.android.com/topic/performance/memory) documentation gives information
to help you diagnose your app's memory issues and optimize its resource
consumption.

#### Test your app's behavior under the memory constraints

You can use [Android Debug Bridge (`adb`)](https://developer.android.com/tools/adb) to adjust or disable the
memory limits on any device that imposes them. The shell command `am`
provides three subcommands to adjust the memory limits. (These commands have
no effect on a device which does not impose memory limits.)

- `am memory-limiter ignore <uid>|none|all`
- `am memory-limiter manual <pid> <limit>|max|none`
- `am memory-limiter status`

`ignore`

:   Instructs the memory limiter to ignore some or all processes.
    Passing a [UID (Android User ID)](https://developer.android.com/tools/dumpsys#uid_stats) instructs the memory limiter to
    ignore enforcement on all processes associated with that UID.
    You can also pass `all` (ignore all apps) or `none`
    (do not ignore any apps).
    Passing `none` overrides any previous calls to `am memory-limiter ignore`.

:   If you instruct the memory limiter to ignore a UID, you can still apply
    a manual memory limit to a process within the app
    by calling `am memory-limiter manual`.

`manual`

:   Instructs the system to impose a memory constraint on the process with the
    specified PID (Process ID). The memory constraint is specified as an integer
    number of MB; for example, passing `30` specifies that the process is limited
    to 30 MB of memory. Passing `max` removes all memory limits on that process.
    Passing `none` removes any manual limits set on the process, restoring the
    system's default limit (if any).

`status`

:   Reports the current status of the memory limiter. The status includes the
    memory limits imposed on visible and non-visible processes.

## Privacy

Android 17 includes the following changes to improve user privacy.

### SMS OTP protection

Beginning with Android 17, Android is expanding its protection
for SMS messages containing one-time passwords (OTP).

In previous versions of Android, this protection was primarily focused on the
SMS Retriever format. Delivery of messages containing an SMS retriever hash was
delayed for most apps for three hours. However, certain apps (like the
default SMS handler) were exempt from the delay, and the app that owned the hash
was also exempted.

Beginning with Android 17, the protection is also applied to WebOTP
format messages. If an app has permission to read SMS messages but is not the
intended recipient of a WebOTP message (as determined by domain verification),
the message is not accessible to the app until three hours after the message's
receipt. This change is intended to improve user security by ensuring that only
apps associated with the domain mentioned in the message can programmatically
read the verification code.

During this three hour delay, the [`SMS_RECEIVED_ACTION`](https://developer.android.com/reference/android/provider/Telephony.Sms.Intents#SMS_RECEIVED_ACTION) broadcast is
withheld and [SMS provider](https://developer.android.com/reference/android/provider/Telephony.Sms) database queries are filtered. The
SMS message is available to these apps after the delay. This change applies to
**all apps**, regardless of their target API level.

Certain apps such as the default SMS assistant app, connected device companion
apps, etc., are exempted from this delay. All apps that rely on reading SMS
messages for OTP extraction should transition to using [SMS Retriever](https://developer.android.com/identity/sms-retriever) or [SMS
User Consent](https://developers.google.com/identity/sms-retriever/user-consent/overview) APIs to ensure continued functionality.

> [!NOTE]
> **Note:** If your app targets Android 17 (API level 37) or higher, this protection is also extended to standard SMS messages. For more information, see [OTP protection for standard SMS messages](https://developer.android.com/about/versions/17/behavior-changes-17#sms-otp-protection) in the [Behavior changes:
> Apps targeting Android 17](https://developer.android.com/about/versions/17/behavior-changes-17) documentation.

## Security

Android 17 includes the following improvements to device and app
security.

### usesClearTraffic deprecation plan

In a future release, we plan to deprecate the `usesCleartextTraffic` element.
Apps that need to make unencrypted (HTTP) connections should migrate to
using a [network security configuration](https://developer.android.com/privacy-and-security/security-config) file, which lets you
specify which domains your app needs to make cleartext connections to.

Be aware that network security configuration files are only supported on API
levels 24 and higher. If your app has a minimum API level lower than 24, you
should do *both* of the following:

- Set the `usesCleartextTraffic` attribute to `true`
- Use a network configuration file

If your app's minimum API level is 24 or higher, you can use a network
configuration file and you don't need to set `usesCleartextTraffic`.

### Restrict implicit URI grants

Currently, if an app launches an intent with a URI that has the action
[`ACTION_SEND`](https://developer.android.com/reference/android/content/Intent#ACTION_SEND), [`ACTION_SEND_MULTIPLE`](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE), or
[`ACTION_IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE), the system automatically grants the read and
write URI permissions to the target app. Starting in Android 18, the system will
no longer automatically grant these permissions. For this reason, we recommend
that apps explicitly grant the
relevant URI permissions instead of relying on the system to grant them.

To detect the usage of these intents in your app, use [`StrictMode`](https://developer.android.com/reference/android/os/StrictMode) with
[`detectImplicitUriPermissionGrant()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectImplicitUriPermissionGrant()) to trigger a violation:

### Kotlin

```kotlin
val policy = StrictMode.VmPolicy.Builder()
    .detectImplicitUriPermissionGrant()
    .penaltyLog()
    .build()
StrictMode.setVmPolicy(policy)
```

### Java

```java
StrictMode.VmPolicy policy = new StrictMode.VmPolicy.Builder()
    .detectImplicitUriPermissionGrant()
    .penaltyLog()
    .build();
StrictMode.setVmPolicy(policy);
```

Alternatively, you can monitor for logged exceptions containing the message
`Please set the grant explicitly in the app` that appears when system implicitly
sets the grant. You can monitor for these logs
using the following `adb` command:

    adb logcat | grep "Please set the grant explicitly in the app"

To explicitly grant the necessary permissions, add the
[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION) flag to [`ACTION_SEND`](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) and
[`ACTION_SEND_MULTIPLE`](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE) intents:

### Kotlin

```kotlin
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
```

### Java

```java
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
```

Include both [`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION) and
[`FLAG_GRANT_WRITE_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_WRITE_URI_PERMISSION) flags for
[`ACTION_IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE) intents:

### Kotlin

```kotlin
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION)
```

### Java

```java
intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
```

### Per-app keystore limits

Apps should avoid creating excessive numbers of keys in Android Keystore,
because it is a shared resource for all apps on the device. Beginning with
Android 17, the system enforces a limit on the number of keys an app can
own. The limit is 50,000 keys for non-system apps targeting
Android 17 (API level 37) or higher, and 200,000 keys for all other apps.
System apps have a limit of 200,000 keys, regardless of which API level they
target.

If an app attempts to create keys beyond the limit, the creation fails with a
[`KeyStoreException`](https://developer.android.com/reference/java/security/KeyStoreException). The exception's message string contains information
about the key limit. If the app calls [`getNumericErrorCode()`](https://developer.android.com/reference/android/security/KeyStoreException#getNumericErrorCode()) on the
exception, the return value depends on what API level the app targets:

- Apps targeting Android 17 (API level 37) or higher: `getNumericErrorCode()` returns the new `ERROR_TOO_MANY_KEYS` value.
- All other apps: `getNumericErrorCode()` returns `ERROR_INCORRECT_USAGE`.

### Block cross profile loopback traffic

Beginning with Android 17, cross-profile loopback traffic is no longer
permitted by default. Loopback traffic within the same profile is not affected.
This change applies to all apps running on Android 17 or higher,
regardless of what API level the app targets.

## User experience and system UI

Android 17 includes the following changes that are intended
to create a more consistent, intuitive user experience.

### Restoring default IME visibility after rotation

Beginning with Android 17, when the device's configuration changes (for
example, through rotation), and this is not handled by the app itself, the
previous IME visibility is not restored.

If your app undergoes a configuration change that it does not handle, and the
app needs the keyboard to be visible after the change,
you must explicitly request this. You can make this request in one of the
following ways:

- Set the `android:windowSoftInputMode` attribute to `stateAlwaysVisible`.
- Programmatically request the soft keyboard in your activity's `onCreate()` method, or add the `onConfigurationChanged()` method.

## Human input

Android 17 includes the following changes that affect how
apps interact with human input devices like keyboards and touchpads.

### Touchpads deliver relative events by default during pointer capture

Beginning with Android 17, if an app requests pointer capture using
[`View.requestPointerCapture()`](https://developer.android.com/reference/android/view/View#requestPointerCapture()) and the user uses a touchpad, the system
recognizes pointer movement and scrolling gestures from the user's touches and
reports them to the app in the same way as pointer and scroll wheel movements
from a captured mouse. In most cases, this removes the need for apps that
support captured mice to add special handling logic for touchpads. For more
details, see the documentation for [`View.POINTER_CAPTURE_MODE_RELATIVE`](https://developer.android.com/reference/android/view/View#POINTER_CAPTURE_MODE_RELATIVE).

Previously, the system did not attempt to recognize gestures from the touchpad,
and instead delivered the raw, absolute finger locations to the app in a similar
format to touchscreen touches. If an app still requires this absolute data, it
should call the new [`View.requestPointerCapture(int)`](https://developer.android.com/reference/android/view/View#requestPointerCapture(int)) method with
[`View.POINTER_CAPTURE_MODE_ABSOLUTE`](https://developer.android.com/reference/android/view/View#POINTER_CAPTURE_MODE_ABSOLUTE) instead.

## Media

Android 17 includes the following changes to media behavior.

### Background audio hardening

Beginning with Android 17, the audio framework enforces restrictions on
background audio interactions including audio playback, audio focus requests,
and volume change APIs to ensure that these changes are started intentionally by
the user.

If the app tries to call audio APIs while the app is not in a valid lifecycle,
the audio playback and volume change APIs fail silently without throwing an
exception or providing a failure message. The audio focus API fails with the
result code `AUDIOFOCUS_REQUEST_FAILED`.

> [!NOTE]
> **Note:** The restrictions are more stringent if an app targets Android 17 (API level 37). For these apps, the foreground service must have while-in-use (WIU) capabilities, unless the app has the [exact alarm](https://developer.android.com/develop/background-work/services/alarms#exact) permission and is interacting with [`USAGE_ALARM`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ALARM) audio streams.

For more information, including mitigation strategies, see [Background audio
hardening](https://developer.android.com/about/versions/17/changes/bg-audio).

## Connectivity

Android 17 includes the following changes to enhance device
connectivity.

### Autonomous re-pairing for Bluetooth bond losses

Android 17 introduces autonomous re-pairing, a system-level enhancement
designed to automatically resolve Bluetooth bond loss.

Previously, if a bond was lost, users had to manually navigate to Settings to
unpair and then re-pair the peripheral. This feature builds upon the security
improvement of Android 16 by allowing the system to re-establish bonds
in the background without requiring users to manually navigate to Settings to
unpair and re-pair peripherals.

While most apps will not require code changes, developers should be aware of the
following behavior changes in Bluetooth stack:

- **New pairing context:** The [`ACTION_PAIRING_REQUEST`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#ACTION_PAIRING_REQUEST) now includes the [`EXTRA_PAIRING_CONTEXT`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#EXTRA_PAIRING_CONTEXT) extra which allows apps to distinguish between a standard pairing request and an autonomous system-initiated re-pairing attempt.
- **Conditional key updates:** Existing security keys will only be replaced if the re-pairing is successful and new connection meets or exceeds the security level of the previous bond.
- **Modified intent timing:** The [`ACTION_KEY_MISSING`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#ACTION_KEY_MISSING) intent is now broadcast only if the autonomous re-pairing attempt fails. This reduces unnecessary error handling in the app if the system successfully recovers the bond in the background.
- **User notification:** The system manages re-pairing via new UI notifications and dialogs. Users will be prompted to confirm the re-pairing attempt to ensure they are aware of the reconnection.

Peripheral device manufacturers and companion app developers should verify that
hardware and app gracefully handle bond transitions. To test this behavior,
simulate a remote bond loss using either of the following methods:

- Manually remove the bond information from the peripheral device
- Manually unpair the device in: Settings \> Connected devices