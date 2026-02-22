---
title: https://developer.android.com/develop/devices/chromeos/learn
url: https://developer.android.com/develop/devices/chromeos/learn
source: md.txt
---

ChromeOS devices, such as Chromebooks, support the Google Play Store and Android
apps. This document assumes you have an existing Android app designed for phones
or tablets that you want to optimize for Chromebooks. To learn the basics of
building Android apps, see [Build your first Android app](https://developer.android.com/training/basics/firstapp).

## Update your app's manifest file

To get started, update your manifest file to account for some key hardware and
software differences between Chromebooks and other devices running Android.

As of ChromeOS version M53, all Android apps that don't explicitly require the
[`android.hardware.touchscreen`](https://developer.android.com/guide/topics/manifest/uses-feature-element#touchscreen-hw-features) feature also work on ChromeOS devices that
support the `android.hardware.faketouch` feature. However, to help your app work
on all Chromebooks, update your manifest file so that the
`android.hardware.touchscreen` feature is not required, as shown in the
following example.  

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
              ... >
        <!-- Some Chromebooks don't support touch. Although not essential,
             it's a good idea to explicitly include this declaration. -->
        <uses-feature android:name="android.hardware.touchscreen"
                      android:required="false" />
    </manifest>

| **Note:** Removing the requirement for touch input means you need to review your app's support for [mouse and keyboard interactions](https://developer.android.com/develop/ui/compose/touch-input).

Different hardware devices come equipped with different sets of sensors, and
Chromebooks might not have all the sensors found in Android handheld devices,
such as GPS and accelerometers. However, in some cases the functionality of a
sensor is provided in another way. For example, Chromebooks might not have GPS
sensors, but they provide location data based on Wi-Fi connections. See the
[sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview) to learn more about the sensors that the Android platform
supports.

If you want your app to run on Chromebooks regardless of sensor availability,
update your manifest file so that no sensors are required.
| **Note:** If you don't require a particular sensor for your app but still use measurements from the sensor when it's available, make sure you dynamically check for the sensor's availability before trying to gather information from it.

Some software features are not supported on Chromebooks. For example, apps that
provide custom IMEs, app widgets, live wallpapers, and app launchers aren't
supported and can't be installed on Chromebooks. For a complete list of
software features that aren't supported on Chromebooks, see [incompatible
software features](https://developer.android.com/develop/devices/chromeos/learn/manifest#incompat-software-features).

## Update your target SDK

Update your app's [`targetSdkVersion`](https://developer.android.com/reference/android/R.attr#targetSdkVersion) attribute to the latest API level
available to take advantage of all the improvements in the Android platform.
Review the improvements in the Android platform throughout different
[versions](https://developer.android.com/about/versions).

## Check for networking requirements

Chromebooks run the entire Android OS in a container, similar to Docker or LXC.
This means that Android doesn't have direct access to the system's LAN
interface. Instead, IPv4 traffic passes through an internal layer of network
address translation (NAT), and IPv6 unicast traffic is routed through an extra
hop.

Outbound unicast connections from an Android app to the internet mostly work
as-is. In general, inbound connections are blocked. Multicast or broadcast
packets from Android are not forwarded to the LAN through the firewall.

As an exception to the multicast restriction, ChromeOS runs a service that
forwards mDNS traffic between Android and the LAN interface, so the standard
[network service discovery](https://developer.android.com/training/connect-devices-wirelessly/nsd) APIs are the recommended way to discover other
devices on the LAN segment. After finding a device on the LAN, an Android app
can use standard TCP or UDP unicast sockets to communicate with it.

IPv4 connections originating from Android use the ChromeOS host's IPv4 address.
Internally, the Android app sees a private IPv4 address assigned to the network
interface. IPv6 connections originating from Android use a different address
from the ChromeOS host, because the Android container has a dedicated public
IPv6 address.

## Use cloud and local storage effectively

Chromebooks let users easily migrate from one device to another. If a user stops
using one Chromebook and starts using another, they only have to sign in, and
all of their apps appear.

Because of this feature, back up your app's data to the cloud to enable syncing
across devices. However, don't depend on an internet connection for your app to
operate normally. Instead, save the user's work locally when the device is
offline and sync to the cloud once the device is back online.

Chromebooks can also be shared among a large number of people, such as in
schools. Since local storage is not infinite, entire accounts---together
with their storage---can be removed from the device at any point. For
educational settings, it's a good idea to keep this scenario in mind.

## Develop new test cases for your app

To develop test cases for your app, first make sure that you specify the proper
manifest flags. In particular, consider setting
[`screenOrientation`](https://developer.android.com/reference/android/R.attr#screenOrientation) to
`unspecified`. If you want to specify a landscape orientation, consider using
`sensorLandscape` to make sure that the experience on a tablet is optimal.

If you have special size or orientation needs for desktop environments, consider
adding meta tags as size or orientation hints. To include size and orientation
on phones, specify layout
[`defaultHeight`](https://developer.android.com/reference/android/R.attr#defaultHeight),
[`defaultWidth`](https://developer.android.com/reference/android/R.attr#defaultWidth), or
[`minHeight`](https://developer.android.com/reference/android/R.attr#minHeight) attributes instead.

If you are interested in specific input device handling for specific device
categories, specify `android.hardware.type.pc` to disable input compatibility
mode.

If you are using any kind of networking, make sure that the app can reconnect to
the network after a connection problem is resolved or the device wakes from
sleep mode.

We recommend checking the list of [test cases for Android apps on Chrome OS](https://developer.android.com/develop/devices/chromeos/learn/tests),
which you can use in your test plan. The test cases cover common scenarios that
Android apps should be prepared for if they are expected to run on ChromeOS
devices.

### Multi-window and orientation changes

ChromeOS's multi-window environment can make state persistence and recall issues
more obvious. Use [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel) to save and restore your state when
appropriate.

To test state persistence, minimize your app for some time, start another
resource intensive process, and restore your app to confirm that it returns to
the state you left it in.

Test window resizing by pressing the full screen key (F4), maximizing, and
restoring. To test free resizing, first enable it in the developer options, and
then check that your app smoothly resizes without crashing.

If your ChromeOS device supports it, change from laptop to tablet mode to check
whether everything works as expected. Rotate the device once in tablet mode to
test orientation changes, then transition back to laptop mode. Repeat this step
a few times.

Make sure that the top bar is not breaking your app by offsetting UI elements or
location-based touch input. For ChromeOS devices, make sure that your app
doesn't place important information in the status bar area.

If you are using the camera or another hardware feature, like the pen, make sure
that it behaves properly when performing the window and device changes outlined
previously.