---
title: https://developer.android.com/develop/connectivity/wifi/wifi-permissions
url: https://developer.android.com/develop/connectivity/wifi/wifi-permissions
source: md.txt
---

Apps that target Android 13 (API level 33) or higher and manage Wi-Fi connections
should request the
[`NEARBY_WIFI_DEVICES`](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES)
[runtime permission](https://developer.android.com/guide/topics/permissions/overview#runtime). This
permission makes it easier to justify an app's access of nearby Wi-Fi devices;
on previous versions of Android, these apps needed to declare the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission instead.

> [!CAUTION]
> **Caution:** If your app tries to call a Wi-Fi API without the proper permission, a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException) occurs.

## Permission is part of the nearby devices group

The `NEARBY_WIFI_DEVICES` permission is part of the **Nearby devices**
permission group. This group, added in Android 12 (API level 31), also includes
permissions related to Bluetooth and Ultra-wideband. When you request any
combination of permissions from this permission group, the system shows a single
runtime dialog and asks the user to approve your app's access to nearby devices.
In system settings, the user must enable and disable the **Nearby devices**
permissions as a group; for example, users can't disable Wi-Fi access but keep
Bluetooth access enabled for a given app.

## Strongly assert that your app doesn't derive physical location

When you target Android 13 or higher, consider whether your app
ever derives location information from Wi-Fi APIs; if not, you should strongly
assert that. To make this assertion, set the `usesPermissionFlags` attribute to
`neverForLocation` in your app's manifest file, as shown in the following code
snippet. This process is similar to the one you do when you
[assert that Bluetooth device information is never used for location](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#assert-never-for-location):

```xml
<manifest ...>
    <uses-permission android:name="android.permission.NEARBY_WIFI_DEVICES"
                     android:usesPermissionFlags="neverForLocation" />
    <application ...>
        ...
    </application>
</manifest>
```

## Previous versions and some APIs require location permission

Several Wi-Fi APIs require the `ACCESS_FINE_LOCATION` permission, even when your
app targets Android 13 or higher. Examples include the following
methods from the `WifiManager` class:

- [`getScanResults()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getScanResults())
- [`startScan()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan())

Also, because the `NEARBY_WIFI_DEVICES` permission is available only on
Android 13 and higher, you should keep any declarations for
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
to provide backward compatibility in your app. However, as long as your app
doesn't otherwise rely on
[precise location information](https://developer.android.com/training/location/permissions#accuracy), you can
set the maximum SDK version of this permission to `32`, as shown in the
following code snippet:

```xml
<manifest ...>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
                     android:maxSdkVersion="32" />
    <application ...>
        ...
    </application>
</manifest>
```

## Check for APIs that require the permission

If your app targets Android 13 or higher, you must declare the
`NEARBY_WIFI_DEVICES` permission to call any of the following Wi-Fi APIs:

- `WifiManager`
  - [`startLocalOnlyHotspot()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startLocalOnlyHotspot(android.net.wifi.WifiManager.LocalOnlyHotspotCallback,%20android.os.Handler))
- `WifiAwareManager`
  - [`attach(AttachCallback attachCallback,
    IdentityChangedListener identityChangedListener,
    Handler handler)`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#attach(android.net.wifi.aware.AttachCallback,%20android.net.wifi.aware.IdentityChangedListener,%20android.os.Handler))
- `WifiAwareSession`
  - [`publish()`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession#publish(android.net.wifi.aware.PublishConfig,%20android.net.wifi.aware.DiscoverySessionCallback,%20android.os.Handler))
  - [`subscribe()`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession#subscribe(android.net.wifi.aware.SubscribeConfig,%20android.net.wifi.aware.DiscoverySessionCallback,%20android.os.Handler))
- `WifiP2pManager`
  - [`addLocalService()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#addLocalService(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.nsd.WifiP2pServiceInfo,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
  - [`connect()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pConfig,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
  - [`createGroup()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#createGroup(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pConfig,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
  - [`discoverPeers()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
  - [`discoverServices()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverServices(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
  - [`requestDeviceInfo()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestDeviceInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.DeviceInfoListener))
  - [`requestGroupInfo()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestGroupInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.GroupInfoListener))
  - [`requestPeers()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.PeerListListener))
- `WifiRttManager`
  - [`startRanging()`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager#startRanging(android.net.wifi.rtt.RangingRequest,%20java.util.concurrent.Executor,%20android.net.wifi.rtt.RangingResultCallback))

## Wi-Fi access workflows

Figure 1 shows the Wi-Fi access workflow on devices that run
Android 13 or higher, for apps that target
Android 13 or higher. Note that, as long as you assert that your
app doesn't derive physical location from Wi-Fi device information, you don't
need to declare the `ACCESS_FINE_LOCATION` permission anymore:
![](https://developer.android.com/static/images/develop/connectivity/nearby-wifi-permission-flow-13.svg) **Figure 1.** Flow chart to determine whether an app that targets Android 13 (API level 33) or higher can access Wi-Fi information.

Figure 2 shows the Wi-Fi access workflow on devices that run
12L or lower. Note the reliance on the
`ACCESS_FINE_LOCATION` permission.
![](https://developer.android.com/static/images/develop/connectivity/nearby-wifi-permission-flow-12L.svg) **Figure 2.** Flow chart to determine whether an app that targets 12L (API level 32) or lower can access Wi-Fi information.