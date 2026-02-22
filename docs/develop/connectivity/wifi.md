---
title: https://developer.android.com/develop/connectivity/wifi
url: https://developer.android.com/develop/connectivity/wifi
source: md.txt
---

# Connect devices wirelessly

Besides enabling communication with the cloud, Android's wireless APIs also enable communication with other devices on the same local network, and even devices which are not on a network, but are physically nearby. The addition of Network Service Discovery (NSD) takes this further by allowing an application to seek out a nearby device running services with which it can communicate. Integrating this feature into your application helps you provide a wide range of features, such as playing games with users in the same room, pulling images from a networked NSD-enabled webcam, or remotely logging into other machines on the same network.

This class describes the key APIs for finding and connecting to other devices from your application. Specifically, it describes the NSD API for discovering available services and the Wi-Fi Peer-to-Peer (P2P) API for doing peer-to-peer wireless connections. This class also shows you how to use NSD and Wi-Fi P2P in combination to detect the services offered by a device and connect to the device when neither device is connected to a network.

If you're looking for a higher-level API for your Android application to transfer data reliably and securely between devices using a combination of Wi-Fi and Bluetooth, consider using the[Nearby Connections API](https://developers.google.com/nearby/connections/overview).  

## Lessons

**[Use network service discovery](https://developer.android.com/develop/connectivity/wifi/use-nsd)**
:   Learn how to broadcast services offered by your own application, discover services offered on the local network, and use NSD to determine the connection details for the service you want to connect to.

**[Creating P2P connections with Wi-Fi](https://developer.android.com/develop/connectivity/wifi/wifi-direct)**
:   Learn how to fetch a list of nearby peer devices, create an access point for legacy devices, and connect to other devices capable of Wi-Fi P2P connections.

**[Using Wi-Fi P2P for service discovery](https://developer.android.com/develop/connectivity/wifi/nsd-wifi-direct)**
:   Learn how to discover services published by nearby devices without being on the same network, using Wi-Fi P2P.

## You should also read

- [Wi-Fi P2P](https://developer.android.com/develop/connectivity/wifi/wifip2p)
- [Nearby Connections API](https://developers.google.com/nearby/connections/overview)