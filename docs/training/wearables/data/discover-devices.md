---
title: https://developer.android.com/training/wearables/data/discover-devices
url: https://developer.android.com/training/wearables/data/discover-devices
source: md.txt
---

# Discover devices on a network using Data Layer APIs

Devices may establish a connection to the internet either directly using a Wi-Fi or cellular connection, or indirectly through a paired Bluetooth device.

## Reachable and nearby nodes

A device is considered*reachable*when it's online and available to communicate with another device, either directly through Bluetooth or indirectly using the cloud as an intermediary.

A device is considered*nearby*if it can be connected directly through Bluetooth, without using the cloud.

## Activities that affect reconnection time

Under certain circumstances, devices may require up to 4 minutes to re-establish a connection. These scenarios include the following:

- **Wear OS device inactivity:**If a Wear OS device is removed from the user's wrist or otherwise isn't actively used for an extended period, the reconnection time might be extended.
- **Doze state:** A handheld's[power-saving Doze state](https://developer.android.com/training/monitoring-device-state/doze-standby#understand_doze)can limit background processes, potentially increasing the device's reconnection time.
- **User interaction:**If the user starts interacting with both a handheld device and a Wear OS device at approximately the same time, it often expedites the reconnection process.

## Discover all devices using a node client

A`NodeClient`object identifies and broadcasts to the list of Android-powered devices connected to a network, regardless of the capability of each device. All apps on a device receive these event notifications, such as a new device joining the network or an existing device going offline.

The`NodeClient`class is particularly helpful for discovering devices that don't have your app installed.

## Discover specific devices using a capability client

A`CapabilityClient`object provides information about which devices on the Wear OS network support specific app capabilities. A*capability* is a feature that an app either[defines at build time](https://developer.android.com/training/wearables/data/messages#advertise-capabilities)or[configures dynamically at runtime](https://developers.google.com/android/reference/com/google/android/gms/wearable/CapabilityClient#addLocalCapability(java.lang.String)).

For example, a mobile Android app could advertise that it supports remote control of video playback. The Wear OS version of that app can use the`CapabilityClient`to check whether the mobile version of the app is installed on a nearby device and supports that feature. If it does, the Wear OS app can show play and pause buttons so that users can control a video, which is playing on their mobile device, from their Wear OS device. The capability broadcast works in the opposite direction, too; Wear OS apps can list the capabilities that they support.

## Check for your app's new capabilities

Use the`CapabilityClient`to determine the node ID of a device you need to communicate with. For example, if you need to check for the presence of a new feature in your app on handheld devices, create a capability for that new feature on the handheld side. Your Wear OS app can then query for the devices that support that capability. If the capability is missing on all devices, it means that the user doesn't have a version of your app that supports this feature, which you should gracefully handle in your app's logic. If you assume that the handheld device is always the correct node to communicate with, your messages might end up not being delivered, because the phone app does not support the feature.

## Determine whether a Wear OS device is the only one on a network

You can use the`CapabilityClient`to check if your app must operate in standalone mode because no other Android-powered devices are nearby. By passing in`FILTER_ALL`, no other devices should appear in the results.