---
title: https://developer.android.com/develop/devices/chromeos/learn/manifest
url: https://developer.android.com/develop/devices/chromeos/learn/manifest
source: md.txt
---

As you prepare your Android app to run on Chromebooks, consider the
device features that your app uses. Chromebooks don't support all the
hardware and software features that are available on other devices running
Android. If your app requires specific features that aren't supported on
Chromebooks, it won't be available for installation on Chromebooks.


You declare your app's requirements for hardware features and certain software
features in the [manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro).
This document describes the app manifest feature declarations that aren't
compatible with Chromebooks.

## Incompatible manifest entries

The manifest entries listed in this section aren't compatible with Chromebooks. If
your app uses any of these entries, consider removing them or including the
`required="false"` attribute value with them so that your app can be installed on
Chromebooks.

For more information about declaring feature use without requiring that the feature be
available on the device, see the guide for the [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-
element#market-feature-filtering) manifest element. For
a complete list of app manifest features and descriptions see the
[Features reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference) .

**Note** : Android Studio has built-in lint checks to
automatically validate the manifest file. In Android Studio, select
**File \> Settings \> Editor \> Inspections \> Android \> Lint \> Correctness \> ChromeOS.**

### Hardware features


Support for hardware features varies on Chromebooks. Some features aren't
supported on any Chromebooks, while others are supported on only some Chromebooks.

### Special features


For better hardware support on Chromebooks, `android.hardware.type.pc` disables input emulation for mouse
and touchpad. You must indicate `required="false"`
for this entry, or your app can *only* run on Chromebooks.

#### Unsupported hardware features


The following list includes the hardware features that aren't
supported on Chromebooks:

- `android.hardware.camera`: back-facing camera
- `android.hardware.camera.autofocus`: camera that uses autofocus
- `android.hardware.camera.capability.manual_post_processing`: camera that uses the `MANUAL_POST_PROCESSING` feature, including functionality for overriding auto white balance
- `android.hardware.camera.capability.manual_sensor`: camera that uses the `MANUAL_SENSOR` feature, including auto-exposure locking support
- `android.hardware.camera.capability.raw`: camera that uses the `RAW` feature, including the ability to save DNG (raw) files and provide DNG-related metadata
- `android.hardware.camera.flash`: camera that uses flash
- `android.hardware.camera.level.full`: camera that uses `FULL`-level image-capturing support
- `android.hardware.consumerir`: infrared (IR)
- `android.hardware.location.gps`: Global Positioning System (GPS)
- `android.hardware.nfc`: Near-Field Communication (NFC)
- `android.hardware.nfc.hce`: NFC card emulation, which is deprecated
- `android.hardware.sensor.barometer`: barometer (air pressure)
- `android.hardware.telephony`: telephony, including radio with data communication services
- `android.hardware.telephony.cdma`: telephony Code Division Multiple Access (CDMA) network support
- `android.hardware.telephony.gsm`: telephony Global System for Mobile Communications (GSM) network support
- `android.hardware.type.automotive`: Android Automotive OS device
- `android.hardware.type.television`: television, which is deprecated
- `android.hardware.usb.accessory`: USB accessory mode
- `android.hardware.usb.host`: USB host mode

#### Partially supported hardware features


The following list includes hardware features that might be available on some
Chromebooks:

- `android.hardware.sensor.accelerometer`: accelerometer (device orientation)
- `android.hardware.sensor.compass`: compass
- `android.hardware.sensor.gyroscope`: gyroscope (device rotation and twist)
- `android.hardware.sensor.light`: light
- `android.hardware.sensor.proximity`: proximity (to user)
- `android.hardware.sensor.stepcounter`: step counter
- `android.hardware.sensor.stepdetector`: step detector

#### Touchscreen hardware support


As of ChromeOS version M53, all Android apps that don't explicitly require the
[`android.hardware.touchscreen`](https://developer.android.com/guide/topics/manifest/uses-feature-element#touchscreen-hw-features) feature also work on ChromeOS
devices that support the
[`android.hardware.faketouch`](https://developer.android.com/guide/topics/manifest/uses-feature-element#touchscreen-hw-features) feature.

Devices that have fake
touch interfaces provide a user input system that emulates basic touch events.
For example, the user can interact with a mouse or remote control to move an
on-screen cursor, scroll through a list, and drag elements from one part of the
screen to another.


If you don't want your app to be installed on devices that have fake touch
interfaces but not touchscreens, you can complete one of the following actions:

- Exclude specific devices in the [Google Play Console](https://play.google.com/console).
- Filter devices with no touchscreen hardware by explicitly declaring [`android.hardware.touchscreen`](https://developer.android.com/guide/topics/manifest/uses-feature-element#touchscreen-hw-features) as being required in order to install your app.

### Software features


The following list includes the software features that aren't
supported on Chromebooks:

- `android.software.app_widgets`: app widgets on the Home screen
- `android.software.device_admin`: device policy administration
- `android.software.home_screen`: replaces device's Home screen
- `android.software.input_methods`: custom input methods (instances of [`InputMethodService`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService))
- `android.software.leanback`: UI designed for large-screen viewing
- `android.software.live_wallpaper`: animated wallpapers
- `android.software.live_tv`: streaming live TV programs
- `android.software.managed_users`: secondary users and managed profiles
- `android.software.sip`: Session Initiation Protocol (SIP) service, which supports video conferencing and instant messaging
- `android.software.sip.voip`: Voice Over Internet Protocol (VoIP) service based on SIP, which supports two-way video conferencing

## Permissions that imply feature requirements


Some permissions that you request in your manifest files can create implied
requests for hardware and software features. By requesting these permissions,
you prevent your app from being installed on Chromebooks.


For details about how to prevent permission requests from making your app
unavailable on Chromebooks, see the [Incompatible
manifest entries](https://developer.android.com/develop/devices/chromeos/learn/manifest#incompat-entries) section of this page.


The following table shows the permissions that imply feature
requirements that make an app incompatible with Chromebooks:


**Table 1.**Device permissions that imply hardware features which
are incompatible with Chromebooks.

| Category | This permission | Implies this feature requirement |
|---|---|---|
| Camera | `CAMERA` | `android.hardware.camera` and `android.hardware.camera.autofocus` |
| Telephony | `CALL_PHONE` | `android.hardware.telephony` |
| Telephony | `CALL_PRIVILEGED` | `android.hardware.telephony` |
| Telephony | `MODIFY_PHONE_STATE` | `android.hardware.telephony` |
| Telephony | `PROCESS_OUTGOING_CALLS` | `android.hardware.telephony` |
| Telephony | `READ_SMS` | `android.hardware.telephony` |
| Telephony | `RECEIVE_SMS` | `android.hardware.telephony` |
| Telephony | `RECEIVE_MMS` | `android.hardware.telephony` |
| Telephony | `RECEIVE_WAP_PUSH` | `android.hardware.telephony` |
| Telephony | `SEND_SMS` | `android.hardware.telephony` |
| Telephony | `WRITE_APN_SETTINGS` | `android.hardware.telephony` |
| Telephony | `WRITE_SMS` | `android.hardware.telephony` |