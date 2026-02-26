---
title: https://developer.android.com/develop/connectivity/satellite/constrained-networks
url: https://developer.android.com/develop/connectivity/satellite/constrained-networks
source: md.txt
---

Satellite networks will someday be robust enough to function as normal networks
and work seamlessly with all app use cases; but for now, data on these networks
is a scarce resource. A satellite-based network with constraints on data use is
called a *constrained satellite network*.

Due to these constraints, Android apps don't use these networks by default. If
you want your app to operate on constrained satellite networks, you must
[identify your app as optimized for satellite data usage](https://developer.android.com/develop/connectivity/satellite/constrained-networks#self-identify) and [adapt your
app's use cases](https://developer.android.com/develop/connectivity/satellite/constrained-networks#adapt-use-cases) to conserve resources when connected to a constrained
satellite network.

## Adapt your app's use cases

All you have to do to allow your app to access constrained satellite networks is
opt in, but you might need to make further changes to optimize your app's
behavior to use limited network resources responsibly. Here are some things to
consider when you optimize for constrained data usage:

- **Satellite networks operate under significantly more constrained conditions
  than terrestrial LTE/5G networks**, characterized by lower throughput and higher latency. While we generally recommend minimizing data usage for reliability reasons, each app is unique. You should evaluate your specific use cases to determine if your current data optimization strategies provide an acceptable user experience in these constrained environments.
- **Decide whether your app is suitable for use on constrained networks.** Some apps aren't a good fit for data-constrained networks under any circumstances. For example, high-bandwidth apps, such as video streaming, should assess their data compression and content delivery mechanisms to ensure a functional user experience. If a degraded experience is unavoidable due to data constraints, the app should take the following actions:
  1. **Apps might choose not to use satellite networks at all**, though they could still identify the presence of a satellite network and inform the user that they won't function on the existing limited network.
  2. **Identify specific use cases to limit or modify.** Some of your app's features might be better suited to limited data conditions than others. For example, low-bandwidth operations like sending text messages are highly reliable. However, high-bandwidth operations, such as uploading uncompressed HD video, might experience significant buffering or failure. We recommend implementing adaptive bitrate streaming or robust compression for these demanding features. This is similar to the way many apps change behavior when roaming.
  3. **Adapt the way your app uses network resources.** Constrained networks work best when apps perform network operations in bursts and spend most of the time not using the network. Variable latency can make real-time synchronous communication challenging.

There are also specific changes you need to make if your app uses [complex
networking logic](https://developer.android.com/develop/connectivity/satellite/constrained-networks#change-behavior) or [Firebase Cloud Messaging](https://developer.android.com/develop/connectivity/satellite/constrained-networks#firebase-cloud-messaging).

## Self-identify as optimized for constrained networks

To identify your app as optimized for constrained networks and opt into using
them, update your [app manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro) with a
[`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element) element as follows:

    <meta-data android:name="android.telephony.PROPERTY_SATELLITE_DATA_OPTIMIZED"
              android:value="PACKAGE_NAME" />

This element allows your app to use a constrained satellite network when it's
the only network available. It also notifies the system that your app is
optimized for constrained networks, aiding in user discovery by listing it among
the satellite-enabled apps in the settings app.

> [!NOTE]
> **Note:** Don't add this tag to your manifest when developing a library. Let the apps that use your library self-identify as appropriate.

## Change behavior under constrained data conditions

If you need to change your app's behavior when using a constrained network, or
if your app has pre-existing logic that uses
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) to manage network use, you'll need
to make some changes to your network flow.

### Detect constrained data conditions

The [`NetworkCapabilities`](https://developer.android.com/reference/android/net/NetworkCapabilities) object used for network
requests includes a
[`NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED) bit that is
set by default on all networks and removed on networks that are
bandwidth-constrained. You can determine whether a network is
bandwidth-constrained by checking whether or not it has the
`NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED` capability.

### Work with constrained networks

[`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest) objects also include the
`NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED` capability by default. Remove this
capability to indicate that constrained networks are acceptable.

When you detect that you've connected to a constrained network, you can adapt
your app's features as necessary:

### Kotlin

```kotlin
val HandlerThread = HandlerThread("SatelliteNetworkMonitor"
handlerThread.start()
val handler = Handler(handlerThread.getLooper())

// Make the network request.
val request = NetworkRequest.Builder()
    .addCapability(NET_CAPABILITY_INTERNET
    .removeCapability(NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED)
    .build()

// Register for the callback.
val callback = NetworkCallback() {
    override fun onCapabilitiesChanged(net: Network, nc: NetWorkCapabilities) {
        updateAppUseCases(net, nc)
    }

    fun updateAppUseCases(net: Network, nc: NetworkCapabilities) {
    // Check if the network is bandwidth-constrained or if the transport is satellite.
    // Checking for the satellite transport is to make sure that application
    // continue to have optimized behavior on satellite networks irrespective of whether
    // the NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED capability is set or not. This is
    // because the capability can be removed on an unconstraned satellite Network which only
    // means applications does not need to modify to get data access but should continue
    // to optimize for data usage.
        if (!nc.hasCapability(NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED) ||
             nc.hasTransport(NetworkCapabilities.TRANSPORT_SATELLITE)) {
            // Adapt to constrained network or disable heavy data usage features.
            ...
        } else {
            // Revert to non optimized behavior for data usage
            ...
        }
    }
}
// Where cm is your ConnectivityManager object:
cm.registerBestMatchingNetworkCallback(request, callback, handler)
```

### Java

```java
HandlerThread handlerThread = new HandlerThread("SatelliteNetworkMonitor");
handlerThread.start();
Handler handler = new Handler(handlerThread.getLooper());

// Make the network request.
NetworkRequest request = new NetworkRequest.Builder()
    .addCapability(NET_CAPABILITY_INTERNET)
    .removeCapability(NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED)
    .build();

// Register for the callback.
NetworkCallback callback = new NetworkCallback() {
    @Override
    public void onCapabilitiesChanged(Network net, NetworkCapabilities nc) {
        updateAppUsecases(net, nc);
    }

    private void updateAppUsecases(Network net, NetworkCapabilities nc) {
    // Check if the network is bandwidth-constrained or if the transport is satellite.
    // Checking for the satellite transport is to make sure that application
    // continue to have optimized behavior on satellite networks irrespective of whether
    // the NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED capability is set or not. This is
    // because the capability can be removed on an unconstraned satellite Network which only
    // means applications does not need to modify to get data access but should continue
    // to optimize for data usage.
        if (!nc.hasCapability(NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED) || nc.hasTransport(NetworkCapabilities.TRANSPORT_SATELLITE)) {
            // Adapt to constrained network or disable heavy data usage features.
            ...
        } else {
            // Revert to non optimized behavior for data usage
            ...
        }
    }
};
// Where cm is your ConnectivityManager object:
cm.registerBestMatchingNetworkCallback(request, callback, handler);
```

> [!NOTE]
> **Note:** There are no specific SDK dependencies for accessing constrained satellite networks. You can hardcode the integer values for `NET_CAPABILITY_NOT_BANDWIDTH_CONSTRAINED` and `TRANSPORT_SATELLITE` on lower versions of Android, but on Android 16 and above apps need to use the net network capabilities as demonstrated, handling any exceptions thrown by `ConnectivityManager`.

## Receive FCM messages on constrained networks

If your app uses [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/android/client) to receive messages
from an app server, you can indicate that a specific message should be delivered
even on constrained networks by including the `bandwidth_constrained_ok` flag
when passing the message to the FCM server:

    {
      "message":{
        "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
        "notification":{
          "title":"Portugal vs. Denmark",
          "body":"great match!"
        }
        "android": {
           "bandwidth_constrained_ok": true
        }
      }
    }

If a message doesn't include this flag, then the FCM server only delivers it
when the device is connected through an unconstrained network.

> [!NOTE]
> **Note:** Only use the `bandwidth_constrained_ok` flag if you've updated the corresponding app to work on constrained satellite networks.