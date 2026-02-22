---
title: https://developer.android.com/training/wearables/data/network-communication
url: https://developer.android.com/training/wearables/data/network-communication
source: md.txt
---

# Communicate directly over a network on standalone devices

With Wear OS by Google, a watch can communicate with a network directly, without access to an Android or iOS phone. Don't use the Data Layer API to connect a Wear OS app to a network. Instead, follow the guidelines and steps in this guide.

## Network access

Wear OS apps can make[network requests](https://developer.android.com/guide/topics/connectivity). When a watch has a Bluetooth connection to a phone, the watch's network traffic is generally proxied through the phone.

When a phone is unavailable, Wi-Fi and cellular networks are used, depending on the watch hardware. The Wear OS platform handles transitions between networks.

You can use protocols such as HTTP, TCP, and UDP. However, the[`android.webkit`](https://developer.android.com/reference/android/webkit/package-summary)APIs, including the[`CookieManager`](https://developer.android.com/reference/android/webkit/CookieManager)class, are not available. You can use cookies by reading and writing headers on requests and responses.

Use[`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager)for asynchronous requests, including polling at regular intervals.

If you need to connect to specific network types, see[Reading network state](https://developer.android.com/training/basics/network-ops/reading-network-state).

## High-bandwidth network access

The Wear OS platform manages network connectivity with the goal of providing the best overall user experience. The platform chooses the default active network by balancing two needs: long battery life and network bandwidth.

When battery preservation is prioritized, the active network might not have enough bandwidth for network tasks like transporting large files or streaming media.

This section provides guidance on using the[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager)class to help ensure that your app has the network bandwidth it needs. For general information about fine-grained control over network resources, see[manage network usage](https://developer.android.com/training/basics/network-ops/managing).

### Request Wi-Fi connectivity

For use cases that require high-bandwidth network access, such as transporting large files or streaming media, request connectivity with a high-bandwidth transport, such as Wi-Fi. This is shown in the following example:  

### Kotlin

```kotlin
val callback = object : ConnectivityManager.NetworkCallback() {
    override fun onAvailable(network: Network) {
        super.onAvailable(network)
        // The Wi-Fi network has been acquired. Bind it to use this network by default.
        connectivityManager.bindProcessToNetwork(network)
    }

    override fun onLost(network: Network) {
        super.onLost(network)
        // Called when a network disconnects or otherwise no longer satisfies this request or callback.
    }
}
connectivityManager.requestNetwork(
    NetworkRequest.Builder().addTransportType(NetworkCapabilities.TRANSPORT_WIFI).build(),
    callback
)
```

### Java

```java
ConnectivityManager.NetworkCallback callback = new ConnectivityManager.NetworkCallback() {
    public void onAvailable(Network network) {
        super.onAvailable(network);
        // The Wi-Fi network has been acquired. Bind it to use this network by default.
        connectivityManager.bindProcessToNetwork(network);
    }

    public void onLost(Network network) {
        super.onLost(network);
        // Called when a network disconnects or otherwise no longer satisfies this request or callback.
    }
};
connectivityManager.requestNetwork(
        new NetworkRequest.Builder().addTransportType(NetworkCapabilities.TRANSPORT_WIFI).build(),
        callback
);
```

Acquiring a network might not be instantaneous, because a watch's Wi-Fi or cellular radio might be off to preserve battery. If the watch can't connect to a network, the`onAvailable()`method of your`NetworkCallback`instance is not called.

Once`onAvailable()`is called, the device attempts to remain connected to the Wi-Fi network until the`NetworkCallback`is released. To preserve battery life, release the callback as shown in the following example when you no longer need a Wi-Fi network.  

### Kotlin

```kotlin
connectivityManager.bindProcessToNetwork(null)
connectivityManager.unregisterNetworkCallback(callback)
```

### Java

```java
connectivityManager.bindProcessToNetwork(null);
connectivityManager.unregisterNetworkCallback(callback);
```

### Launch the Wi-Fi settings activity

When requesting a Wi-Fi network, the system tries to connect to a saved network if one is configured and in range. If no saved Wi-Fi network is available, the`onAvailable`callback method of your`NetworkCallback`instance isn't called.

If you are using a`Handler`to time the network request out, you can direct the user to add a Wi-Fi network when the timeout occurs. Send the user directly to the activity for adding a Wi-Fi network using the following intent:  

### Kotlin

```kotlin
context.startActivity(Intent("com.google.android.clockwork.settings.connectivity.wifi.ADD_NETWORK_SETTINGS"))
```

### Java

```java
context.startActivity(new Intent("com.google.android.clockwork.settings.connectivity.wifi.ADD_NETWORK_SETTINGS"));
```

To launch the settings activity, your app must have the`CHANGE_WIFI_STATE`permission.

### User interface considerations

If your app requires a connection to a new Wi-Fi network for a high-bandwidth operation, make sure that the reason for connecting is clear to the user before you launch the Wi-Fi settings. Only request that the user add a new Wi-Fi network when the high-bandwidth network is required. Don't block the user from accessing app features that don't require a high-bandwidth network.

Figure 1 shows a music app. The app lets the user browse music on a lower-bandwidth network and only requires the user to add a new Wi-Fi network if they want to download or stream music.

![Music downloading](https://developer.android.com/static/wear/images/high-band-download-prompt.png)

**Figure 1.**A music app flow for downloading music.

### Power and data use considerations

To help preserve battery life and minimize mobile data usage, defer any nonessential networking tasks, such as analytics reporting or logs collection, until the Wear OS device has re-established a Bluetooth or Wi-Fi connection instead of an LTE or metered connection.

## Cloud messaging

For sending notifications, use[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/)directly.

No APIs for network access or FCM are specific to Wear OS. Refer to the existing documentation about[connecting to a network](https://developer.android.com/training/basics/network-ops/connecting)and[cloud messaging](https://firebase.google.com/docs/cloud-messaging/).

FCM works well with[Doze](https://developer.android.com/training/monitoring-device-state/doze-standby)and is the recommended way to send notifications to a watch.

Provide for messages from FCM by collecting a registration token for a device when your Wear OS app runs. Then include the token as part of the destination when your server sends messages to the FCM REST endpoint. FCM sends messages to the device identified by the token.

An FCM message is in JavaScript Object Notation (JSON) format and can include one or both of the following payloads:

- **Notification payload:**when a notification payload is received by a watch, the data displays to a user directly in the notification stream. When the user taps the notification, your app launches.
- **Data payload:**when the payload has a set of custom key or value pairs. The payload is delivered as data to your Wear OS app.

For more information and examples of payloads, see[About FCM messages](https://firebase.google.com/docs/cloud-messaging/concept-options).

By default, notifications are bridged from a phone app to a watch. If you have a standalone Wear OS app and a corresponding phone app, duplicate notifications can occur. For example, a single[notification](https://developer.android.com/training/wearables/notifications/creating)from FCM, received by both a phone and a watch, could be displayed by both devices independently. You can prevent this by using[bridging APIs](https://developer.android.com/training/wearables/notifications/bridger).

## Use background services

To help ensure that background tasks are correctly executed, they must account for[Doze](https://developer.android.com/training/monitoring-device-state/doze-standby)and App Standby.

When a screen turns off or enters ambient mode for a long enough time, a subset of Doze can occur, and background tasks can be deferred for certain periods. Later, when the device is stationary for an extended time, regular Doze occurs. Schedule requests with the[`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager)API, which lets your app register for Doze-safe code execution.

### Schedule with constraints

You can use constraints to configure requests in a way that preserves battery life. Select one or more of the following constraints to include in your requests:

- Schedule a request that requires networking.

  Specify whether the[`NetworkType`](https://developer.android.com/reference/androidx/work/NetworkType)is`CONNECTED`or`UNMETERED`.`UNMETERED`is for large data transfers, while`CONNECTED`is for small transfers.
- Schedule a request while charging.

- Schedule a request while the device is idle. This is useful for lower-priority background work or synchronization, especially when the device is charging.

For more information, review the WorkManager's[Effect of constraints on periodic work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#constraints)guide.