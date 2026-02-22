---
title: Behavior changes: all apps  |  Android Developers
url: https://developer.android.com/about/versions/17/behavior-changes-all
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Behavior changes: all apps Stay organized with collections Save and categorize content based on your preferences.




The Android 17 platform includes behavior changes that might affect your app.
The following behavior changes apply to *all apps* when they run on Android 17,
regardless of [`targetSdkVersion`](/guide/topics/manifest/uses-sdk-element#target). You should test your app and then modify
it as needed to support these changes, where applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 17](/about/versions/17/behavior-changes-17).

**Note:** This page lists some of the more important changes. For more detailed
information, see the [Android 17 release notes](/about/versions/17/release-notes).

## Security

Android 17 includes the following improvements to device and app
security.

### usesClearTraffic deprecation plan

In a future release, we plan to deprecate the `usesCleartextTraffic` element.
Apps that need to make unencrypted (HTTP) connections should migrate to
using a [network security configuration](/privacy-and-security/security-config) file, which lets you
specify which domains your app needs to make cleartext connections to.

Be aware that network security configuration files are only supported on API
levels 24 and higher. If your app has a minimum API level lower than 24, you
should do *both* of the following:

* Set the `usesCleartextTraffic` attribute to `true`
* Use a network configuration file

If your app's minimum API level is 24 or higher, you can use a network
configuration file and you don't need to set `usesCleartextTraffic`.

### Restrict implicit URI grants

Currently, if an app launches an intent with a URI that has the action `Send`,
`SendMultiple`, or `ImageCapture`, the system automatically grants the read and
write URI permissions to the target app. We plan to change this behavior in
Android 18. For this reason, we recommend that apps explicitly
grant the relevant URI permissions instead of relying on the system to grant
them.

## User experience and system UI

Android 17 includes the following changes that are intended
to create a more consistent, intuitive user experience.

### Restoring default IME visibility after rotation

Beginning with Android 17, when the device's configuration changes (for
example, through rotation), and this is not handled by the app itself, the
previous IME visibility is not restored.

If your app undergoes a configuration change that it does not handle, and the
app needs the keyboard to be visible after the change,
you must explicitly request this. You can make this request in one of the
following ways:

* Set the `android:windowSoftInputMode` attribute to `stateAlwaysVisible`.
* Programmatically request the soft keyboard in your activity's `onCreate()`
  method, or add the `onConfigurationChanged()` method.

## Media

Android 17 includes the following changes to media behavior.

### Background audio hardening

Beginning with Android 17, the audio framework enforces restrictions on
background audio interactions including audio playback, audio focus requests,
and volume change APIs to ensure that these changes are started intentionally by
the user.

If the app tries to call audio APIs while the app is not in a valid lifecycle,
the audio playback and volume change APIs fail silently without throwing an
exception or providing a failure message. The audio focus API fails with the
result code `AUDIOFOCUS_REQUEST_FAILED`.

For more information, including mitigation strategies, see [Background audio
hardening](/about/versions/17/changes/bg-audio).