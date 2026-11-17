---
title: https://developer.android.com/develop/connectivity/overview
url: https://developer.android.com/develop/connectivity/overview
source: md.txt
---

> Documentation index: https://developer.android.com/develop/connectivity/llms.txt

Your app can connect with the outside world using a variety of different
communication technologies, including Wi-Fi, Bluetooth, and USB. The guides
listed below cover adding support for these technologies and for optimizing
your app for connectivity.

## Supported technologies

Android supports the following protocols and frameworks for connecting your
device to the outside world.

| Guides ||
|---|---|
| Networks: [**Overview**](https://developer.android.com/develop/connectivity/network-ops.md.txt) | Overview of guides that cover performing various network operations, including connections, management, parsing XML, monitoring, and more. |
| Networks: [**5G**](https://developer.android.com/develop/connectivity/5g/enhance-with-5g.md.txt) | Take advantage of 5G networking. |
| Networks: [**VPN**](https://developer.android.com/develop/connectivity/vpn.md.txt) | Develop and test your own VPN client for a device that runs Android. |
| Networks: [**Wi-Fi scanning**](https://developer.android.com/develop/connectivity/wifi-scan) | Get a list of Wi-Fi access points visible from a device. |
| Networks: [**Wi-Fi Direct (P2P)**](https://developer.android.com/develop/connectivity/wifip2p) | Connect supported devices directly to each other without an intermediate access point. |
| Networks: [**Wi-Fi Aware**](https://developer.android.com/develop/connectivity/wifi-aware) | Enable devices running Android 8.0 (API level 26) and higher to discover and connect directly to each other without any other type of connectivity between them. Also known as Neighbor Awareness Networking (NAN). |
| Networks: [**Wi-Fi Round-Trip Time (RTT)**](https://developer.android.com/develop/connectivity/wifi-rtt) | Measure the distance to nearby RTT-capable Wi-Fi access points and peer Wi-Fi Aware devices. |
| Networks: [**Wi-Fi local-only hotspot**](https://developer.android.com/develop/connectivity/localonlyhotspot) | Enable apps on devices connected to a Wi-Fi hotspot to communicate with each other. |
| Bluetooth: [**Overview**](https://developer.android.com/develop/connectivity/bluetooth.md.txt) | Overview of Android Bluetooth support, including basics and key classes and interfaces. |
| Bluetooth: [**Bluetooth Classic**](https://developer.android.com/develop/connectivity/bluetooth/setup.md.txt) | Set up baseline Bluetooth connectivity on your app. |
| Bluetooth: [**Bluetooth Low Energy (BLE)**](https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview.md.txt) | Transfer small amounts of data between nearby devices and interacting with proximity sensors. |
| Bluetooth: [**BLE Audio**](https://developer.android.com/develop/connectivity/bluetooth/ble-audio/overview.md.txt) | Receive high fidelity audio without sacrificing battery life, and let users seamlessly switch between different use cases. |
| [**Near Field Communication (NFC)**](https://developer.android.com/develop/connectivity/nfc.md.txt) | NFC is a set of short-range wireless technologies, typically requiring a distance of 4 cm or less to initiate a connection. |
| [**Ranging**](https://developer.android.com/develop/connectivity/ranging.md.txt) | Handle ranging sessions across multiple technologies. |
| [**Telecom**](https://developer.android.com/develop/connectivity/telecom.md.txt) | Manage audio and video calls, including eSIMs and SIM cards. |
| [**Ultra Wideband (UWB) communication**](https://developer.android.com/develop/connectivity/uwb.md.txt) | Measure precise ranging between devices. |
| [**USB**](https://developer.android.com/develop/connectivity/usb.md.txt) | Use USB accessory and USB host modes to support a variety of USB peripherals and Android USB accessories. |

## Optimizations

The following guides can help you optimize your app for connectivity.

| Guides ||
|---|---|
| [Reduce network battery drainage](https://developer.android.com/develop/connectivity/preserving-battery.md.txt) | Learn about strategies for preserving battery, user experience, and system health. |
| [Reduce latency and increase network throughput](https://developer.android.com/develop/connectivity/cronet.md.txt) | Learn how to use Cronet, a library derived from the Chromium network stack, to reduce latency and increase throughput of network requests. |