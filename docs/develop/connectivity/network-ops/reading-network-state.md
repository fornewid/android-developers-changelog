---
title: https://developer.android.com/develop/connectivity/network-ops/reading-network-state
url: https://developer.android.com/develop/connectivity/network-ops/reading-network-state
source: md.txt
---

Android enables apps to learn about dynamic changes in connectivity. Use the
following classes to track and respond to connectivity changes:

- [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) tells your app about the state of connectivity in the system.
- The [`Network`](https://developer.android.com/reference/android/net/Network) class represents one of the networks that the device is connected to. You can use the `Network` object as a key to gather information about the network with `ConnectivityManager` or to bind sockets on the network. When the network disconnects, the `Network` object stops being usable. Even if the device later reconnects to the same appliance, a new `Network` object represents the new network.
- The [`LinkProperties`](https://developer.android.com/reference/android/net/LinkProperties) object contains information about the link for a network, such as the list of DNS servers, local IP addresses, and network routes installed for the network.
- The [`NetworkCapabilities`](https://developer.android.com/reference/android/net/NetworkCapabilities) object contains information about properties of a network, such as the transports (Wi-Fi, mobile, Bluetooth) and what the network is capable of. For example, you can query the object to determine whether the network is capable of sending MMS, is behind a captive portal, or is metered.

Apps interested in the immediate state of connectivity at any given time can
call `ConnectivityManager` methods to find out what kind of network is
available. These methods are helpful for debugging and to occasionally review a
snapshot of connectivity available at any given time.

However, the synchronous
`ConnectivityManager` methods don't tell your app about anything happening
after a call, so they don't let you update your UI. They also can't adjust app
behavior based on the network disconnecting or when the network capabilities
change.

Connectivity can change at any time, and most apps need to have an
always-fresh, up-to-date view of the state of networking on the device. Apps can
register a callback with `ConnectivityManager` to be alerted to changes that the
app cares about. Using the callback, your app can react immediately to any
relevant change in connectivity, without having to resort to expensive polling
that might miss fast updates.

> [!NOTE]
> **Note:** If your app needs to schedule tasks for when the device next has connectivity or is on an unmetered network, such as to do background downloads, see [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) instead. Although `ConnectivityManager` tells you about these states, WorkManager lets your app run its jobs at more appropriate times with finer control---and with a lot less work.

Using `NetworkCallback` and other ways of finding out about the
connectivity state of the device doesn't require any particular permission.
However, some networks are subject to specific permissions.
For
example, there might be restricted networks not available to apps. Binding to a
background network requires the `CHANGE_NETWORK_STATE` permission. And some
calls might need specific permissions to run. Refer to the specific
documentation for each call for details.

## Get instantaneous state

An Android-powered device can maintain many connections at the same time.
To get information about the current network state, first obtain
an instance of `ConnectivityManager`:

### Kotlin

```kotlin
val connectivityManager = getSystemService(ConnectivityManager::class.java)
```

### Java

```java
ConnectivityManager connectivityManager = getSystemService(ConnectivityManager.class);
```

Next, use this instance to get a reference to the current default network for your
app:

### Kotlin

```kotlin
val currentNetwork = connectivityManager.getActiveNetwork()
```

### Java

```java
Network currentNetwork = connectivityManager.getActiveNetwork();
```

With a reference to a network, your app can request information about it:

### Kotlin

```kotlin
val caps = connectivityManager.getNetworkCapabilities(currentNetwork)
val linkProperties = connectivityManager.getLinkProperties(currentNetwork)
```

### Java

```java
NetworkCapabilities caps = connectivityManager.getNetworkCapabilities(currentNetwork);
LinkProperties linkProperties = connectivityManager.getLinkProperties(currentNetwork);
```

For more useful functionality, register a
[`NetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback).
For more information about registering network callbacks, see
[Listen to network events](https://developer.android.com/develop/connectivity/network-ops/reading-network-state#listening-events).

## NetworkCapabilities and LinkProperties

The `NetworkCapabilities` and `LinkProperties` objects provide information about
all attributes that the system knows about a network.

The `LinkProperties`
object knows about the routes, link addresses, interface name, proxy info (if
any), and DNS servers. Call the relevant method on the `LinkProperties` object
to retrieve the information you need.

The `NetworkCapabilities` object
encapsulates information about the network *transports* and their *capabilities*.

A transport is an abstraction of a physical medium over which a network
operates. Common examples of transports are Ethernet, Wi-Fi, and mobile.
VPNs and Peer-to-Peer Wi-Fi can also be transports.
On Android, a network can have multiple transports at the same time. An example
of this is a VPN operating over both Wi-Fi and mobile networks. The VPN has the
Wi-Fi, mobile, and VPN transports. To find out if a
network has a particular transport, use the
[`NetworkCapabilities.hasTransport(int)`](https://developer.android.com/reference/android/net/NetworkCapabilities#hasTransport(int))
method with one of the `NetworkCapabilities.TRANSPORT_*` constants.

A capability describes a property of the network. Example capabilities include
`MMS`, `NOT_METERED`, and `INTERNET`. A network with the MMS capability can send
and receive Multimedia Messaging Service messages, and a network without this
capability can't. A network with the `NOT_METERED` capability doesn't bill the
user for data. Your app can check for appropriate capabilities by using the
[`NetworkCapabilities.hasCapability(int)`](https://developer.android.com/reference/android/net/NetworkCapabilities#hasCapability(int))
method with one of the `NetworkCapabilities.NET_CAPABILITY_*` constants.

The most-useful `NET_CAPABILITY_*` constants include:

- [`NET_CAPABILITY_INTERNET`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_INTERNET):
  indicates that the network is set up
  to access the internet. This is about *setup* and not actual
  *ability* to reach public servers. For example, a network can be set up to
  access the internet but be subject to a captive portal.

  A carrier's mobile network typically has the `INTERNET` capability, while a
  local P2P Wi-Fi network typically doesn't. For actual connectivity, see
  `NET_CAPABILITY_VALIDATED`.
- [`NET_CAPABILITY_NOT_METERED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_METERED):
  indicates that the network isn't metered. A network is
  classified as metered when the user is sensitive to heavy data usage on that
  connection due to monetary costs, data limitations, or battery performance
  issues.

- [`NET_CAPABILITY_NOT_VPN`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_VPN):
  indicates that the network isn't a virtual private network.

- [`NET_CAPABILITY_VALIDATED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_VALIDATED):
  indicates that the network provides actual access
  to the public internet when it is probed. A network behind a captive
  portal or a network that doesn't provide domain name resolution doesn't have
  this capability. This is the nearest the system can tell about a network
  actually providing access, although a validated network can still,
  in principle, be subject to IP-based filtering or suffer sudden losses of
  connectivity due to issues such as poor signal.

- [`NET_CAPABILITY_CAPTIVE_PORTAL`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_CAPTIVE_PORTAL):
  indicates that the network has a captive portal when it is probed.

There are other capabilities that more specialized apps might be interested in.
For more information, read the parameter definitions in
[`NetworkCapabilities.hasCapability(int)`](https://developer.android.com/reference/android/net/NetworkCapabilities#hasCapability(int)).

The capabilities of a network can change at any time. When the system detects a
captive portal, it shows a notification inviting the user to log in. While this
is ongoing, the network has the `NET_CAPABILITY_INTERNET` and
`NET_CAPABILITY_CAPTIVE_PORTAL` capabilities but not the
`NET_CAPABILITY_VALIDATED` capability.

When the user takes action and logs in to
the captive portal page, the device becomes able to access the public internet
and the network gains the `NET_CAPABILITY_VALIDATED` capability and loses the
`NET_CAPABILITY_CAPTIVE_PORTAL` capability.

Likewise, the transports of a network can change dynamically.
For example, a VPN can reconfigure itself to use
a faster network that just came up, like switching from mobile to Wi-Fi for
its underlying network. In this case, the network loses the `TRANSPORT_CELLULAR`
transport and gains the `TRANSPORT_WIFI` transport, while keeping the
`TRANSPORT_VPN` transport.

## Listen to network events

To find out about network events, use the
[`NetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)
class together with
[`ConnectivityManager.registerDefaultNetworkCallback(NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#registerDefaultNetworkCallback(android.net.ConnectivityManager.NetworkCallback))
and
[`ConnectivityManager.registerNetworkCallback(NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback)). These two methods serve different
purposes.

All Android apps have a default network, which is determined by the system.
The system typically prefers unmetered networks to
metered ones and faster networks to slower ones.

When an app issues a network request, such as with
[`HttpsURLConnection`](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection), the
system satisfies this request using the default network. Apps can send traffic
on other networks, too. For more information, see the section about [additional
networks](https://developer.android.com/develop/connectivity/network-ops/reading-network-state#additional-networks).

The network that is set as the default network can change at any time during the
lifetime of an app. A typical example is the device coming within range of
a known, active, unmetered, and faster-than-mobile Wi-Fi access point. The
device
connects to this access point and switches the default network for all
apps to the new Wi-Fi network.

When a new network becomes the default, any new connection the app opens uses
this network. At some point later, all remaining connections on the previous
default network are forcefully terminated. If it is important for the app to
know when the default network changes, it registers a default network
callback as follows:

### Kotlin

```kotlin
connectivityManager.registerDefaultNetworkCallback(object : ConnectivityManager.NetworkCallback() {
    override fun onAvailable(network : Network) {
        Log.e(TAG, "The default network is now: " + network)
    }

    override fun onLost(network : Network) {
        Log.e(TAG, "The application no longer has a default network. The last default network was " + network)
    }

    override fun onCapabilitiesChanged(network : Network, networkCapabilities : NetworkCapabilities) {
        Log.e(TAG, "The default network changed capabilities: " + networkCapabilities)
    }

    override fun onLinkPropertiesChanged(network : Network, linkProperties : LinkProperties) {
        Log.e(TAG, "The default network changed link properties: " + linkProperties)
    }
})
```

### Java

```java
connectivityManager.registerDefaultNetworkCallback(new ConnectivityManager.NetworkCallback() {
    @Override
    public void onAvailable(Network network) {
        Log.e(TAG, "The default network is now: " + network);
    }

    @Override
    public void onLost(Network network) {
        Log.e(TAG, "The application no longer has a default network. The last default network was " + network);
    }

    @Override
    public void onCapabilitiesChanged(Network network, NetworkCapabilities networkCapabilities) {
        Log.e(TAG, "The default network changed capabilities: " + networkCapabilities);
    }

    @Override
    public void onLinkPropertiesChanged(Network network, LinkProperties linkProperties) {
        Log.e(TAG, "The default network changed link properties: " + linkProperties);
    }
});
```

When a new network becomes the default, the app receives a call to
[`onAvailable(Network)`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onAvailable(android.net.Network))
for the new network. Implement
[`onCapabilitiesChanged(Network,NetworkCapabilities)`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onCapabilitiesChanged(android.net.Network,%20android.net.NetworkCapabilities)),
[`onLinkPropertiesChanged(Network,LinkProperties)`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onLinkPropertiesChanged(android.net.Network,%20android.net.LinkProperties)),
or both to react appropriately to changes in connectivity.

> [!CAUTION]
> **Caution:** Don't call the synchronous methods to find out about the properties of a newly available network in the callback, as this suffers from race conditions. Instead, wait for calls to `onCapabilitiesChanged()` and `onLinkPropertiesChanged()` for that network, which are called immediately after `onAvailable()` on devices running Android 8.0 (API level 26) and higher.

For a callback registered with `registerDefaultNetworkCallback()`, `onLost()`
means the network has lost the status of being the default network. It might be disconnected.

Although you can learn about the transports that the default network is using by
querying
[`NetworkCapabilities.hasTransport(int)`](https://developer.android.com/reference/android/net/NetworkCapabilities#hasTransport(int)),
this is a poor proxy for the bandwidth or meteredness of the network. Your app
can't assume Wi-Fi is always unmetered and always supplies better bandwidth
than mobile.

Instead use
[`NetworkCapabilities.getLinkDownstreamBandwidthKbps()`](https://developer.android.com/reference/android/net/NetworkCapabilities#getLinkDownstreamBandwidthKbps())
to measure bandwidth, and
[`NetworkCapabilites.hasCapability(int)`](https://developer.android.com/reference/android/net/NetworkCapabilities#hasCapability(int))
with
[`NET_CAPABILITY_NOT_METERED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_METERED)
arguments to determine meteredness. For more information, see the section about
[NetworkCapabilities and LinkProperties](https://developer.android.com/develop/connectivity/network-ops/reading-network-state#introducing-net-capabilities).

By default, the callback methods are called on the connectivity thread of
your app, which is a separate thread used by `ConnectivityManager`. If your
implementation of the callbacks needs to do any longer work, call them on a
separate worker thread by using the variant
[`ConnectivityManager.registerDefaultNetworkCallback(NetworkCallback, Handler)`](https://developer.android.com/reference/android/net/ConnectivityManager#registerDefaultNetworkCallback(android.net.ConnectivityManager.NetworkCallback,%20android.os.Handler)).

Unregister your callback when you have no use for it anymore by calling
[`ConnectivityManager.unregisterNetworkCallback(NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#unregisterNetworkCallback(android.net.ConnectivityManager.NetworkCallback)).
Your main activity's [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause())
is a good place to do this, especially if you register the callback in
[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()).

> [!NOTE]
> **Note:** There is a limit to the number of callbacks that can be registered concurrently. Unregister callbacks once they are no longer needed so that your app can register more.

## Additional networks (advanced use cases)

> [!CAUTION]
> **Caution:** Most apps don't need to use additional networks, and instead should use the default network. Only apps that must use other networks should register additional network callbacks. For example, an app that must use Wi-Fi, and only Wi-Fi, for a particular operation is an app that must use additional networks.

Although the default network is the only relevant network for most apps, some
apps
might be interested in other available networks. To find out about these, apps
build a [`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest) matching their
needs and call
[`ConnectivityManager.registerNetworkCallback(NetworkRequest, NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback)).

The process is similar to listening
to a default network. However, although there might only be one
default network that applies to an app at any given time, this version lets your
app see all the available networks simultaneously, so a call to
[`onLost(Network)`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onLost(android.net.Network))
means the network has disconnected for good, not that it's not the default
anymore.

The app builds a `NetworkRequest` to inform `ConnectivityManager` of what kind
of networks it wants to listen to. The following example shows how to build a
`NetworkRequest` for an app that is only interested in unmetered internet
connections:

### Kotlin

```kotlin
val request = NetworkRequest.Builder()
  .addCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED)
  .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
  .build()

connectivityManager.registerNetworkCallback(request, myNetworkCallback)
```

### Java

```java
NetworkRequest request = new NetworkRequest.Builder()
  .addCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED)
  .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
  .build();

connectivityManager.registerNetworkCallback(request, myNetworkCallback);
```

This means your app hears about all changes concerning any unmetered
network on the system.

As for the default network callback, there is a version of
[`registerNetworkCallback(NetworkRequest, NetworkCallback, Handler)`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback,%20android.os.Handler))
that accepts a `Handler` so it doesn't load the `Connectivity` thread of your
app.

Call
[`ConnectivityManager.unregisterNetworkCallback(NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#unregisterNetworkCallback(android.net.ConnectivityManager.NetworkCallback))
when the callback isn't relevant anymore. An app can concurrently register
multiple network callbacks.

For convenience, the
[`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest) object contains the
common capabilities most apps need, including the following:

- [`NET_CAPABILITY_NOT_RESTRICTED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_RESTRICTED)
- [`NET_CAPABILITY_TRUSTED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_TRUSTED)
- [`NET_CAPABILITY_NOT_VPN`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_VPN)

When writing your app, check the defaults to see whether they match your
use case, and clear them if you want your app to be notified about networks
that don't have these capabilities. On the other hand, add
capabilities to avoid being called for any connectivity change in networks that
your app doesn't interact with.

For example, if your app needs to send MMS messages, add
[`NET_CAPABILITY_MMS`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_MMS)
to the `NetworkRequest` to avoid being told about all the networks that can't
send MMS messages. Add
[`TRANSPORT_WIFI_AWARE`](https://developer.android.com/reference/android/net/NetworkCapabilities#TRANSPORT_WIFI_AWARE)
if your app is only interested in P2P Wi-Fi connectivity.
`NET_CAPABILITY_INTERNET` and
[`NET_CAPABILITY_VALIDATED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_VALIDATED)
are helpful if you are interested in the ability to transfer data with a server
on the internet.

## Sample callback sequence

This section describes the sequence of callbacks an app might get if it
registers both a default callback and a regular callback on a device that
has mobile connectivity. In this example, the device connects to a
good Wi-Fi access point, then disconnects from it. The example also assumes the
device has the **Mobile data always on** setting enabled.

The timeline is as follows:

1. When the app calls `registerNetworkCallback()`, the callback immediately
   receives calls from `onAvailable()`, `onNetworkCapabilitiesChanged()`, and
   `onLinkPropertiesChanged()` for the mobile network, because only that
   network is available. If another network is available, the app
   also receives callbacks for the other network.

   <br />

   ![State diagram showing the register network callback event and the callbacks triggered by the event](https://developer.android.com/static/images/develop/network-ops/register-network-callbacks-01.png)   

   **Figure 1.** App state after calling `registerNetworkCallback()`.
2. Then, the app calls `registerDefaultNetworkCallback()`. The default network
   callback starts receiving calls to `onAvailable()`,
   `onNetworkCapabilitiesChanged()`, and `onLinkPropertiesChanged()` for the
   mobile network, because the mobile network is the default network. If
   another, non-default network is up, the app can't receive
   calls for the non-default network.

   ![State diagram showing register the default network callback event and the
   callbacks triggered by the event](https://developer.android.com/static/images/develop/network-ops/register-network-callbacks-02.png)   

   **Figure 2.** App state after registering a default network.
3. Later, the device connects to an (unmetered) Wi-Fi network. The regular
   network callback receives calls to `onAvailable()`,
   `onNetworkCapabilitiesChanged()`, and `onLinkPropertiesChanged()` for the
   Wi-Fi network.

   ![State diagram showing the callbacks triggered when the app connects to a
   new network](https://developer.android.com/static/images/develop/network-ops/register-network-callbacks-03.png)   

   **Figure 3.** App state after connecting to an unmetered Wi-Fi network.
4. At this point, it is possible the Wi-Fi network takes a while to validate. In
   this case, the `onNetworkCapabilitiesChanged()` calls for the regular network
   callback don't include capability `NET_CAPABILITY_VALIDATED`. After a
   short time, it receives a call to `onNetworkCapabilitiesChanged()`, where
   the new capabilities include `NET_CAPABILITY_VALIDATED`. In most cases,
   the validation is very quick.

   When the Wi-Fi network validates, the system prefers it to the mobile
   network, mainly because it is unmetered. The Wi-Fi network becomes the
   default network, so the default network callback receives a call to
   `onAvailable()`, `onNetworkCapabilitiesChanged()`, and
   `onLinkPropertiesChanged()` for the Wi-Fi network. The mobile network goes
   to the background, and the regular network callback receives a call to
   `onLosing()` for the mobile network.

   Because this example assumes mobile data is always on for this device, the
   mobile network never disconnects. If the setting is turned off, then after a
   while the mobile network disconnects, and the regular network callback
   receives a call to `onLost()`.

   ![State diagram showing the callbacks triggered when a Wi-Fi network
   connection validates](https://developer.android.com/static/images/develop/network-ops/register-network-callbacks-04.png)   

   **Figure 4.** App state after Wi-Fi network validates.
5. Later still, the device suddenly disconnects from Wi-Fi, because it went out
   of range. Because the Wi-Fi disconnects, the regular network callback
   receives a
   call to `onLost()` for Wi-Fi. Because mobile is the new default network,
   the default network callback receives calls to `onAvailable()`,
   `onNetworkCapabilitiesChanged()`, and `onLinkPropertiesChanged()` for the
   mobile network.

   ![State diagram showing the callbacks triggered when a Wi-Fi network
   connection is lost](https://developer.android.com/static/images/develop/network-ops/register-network-callbacks-05.png)   

   **Figure 5.** App state after disconnecting from Wi-Fi network.

If the **Mobile data always on** setting is turned off, then when Wi-Fi
disconnects the device tries to reconnect to a mobile network. The picture is
similar, but with a short additional delay for the `onAvailable()` calls, and
the regular network callback also receives calls to `onAvailable()`,
`onNetworkCapabilitiesChanged()`, and `onLinkPropertiesChanged()` because
mobile becomes available.

## Restrictions on the use of the network for data transfer

Being able to see a network with a network callback doesn't mean your app can
use the network for data transfer. Some networks don't provide internet
connectivity, and some networks might be restricted to
privileged apps. To check for internet connectivity, see
[`NET_CAPABILITY_INTERNET`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_INTERNET)
and
[`NET_CAPABILITY_VALIDATED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_VALIDATED).

Use of background networks is also subject to permission checks. If your app
wants to use a background network, it needs the
[`CHANGE_NETWORK_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_NETWORK_STATE)
permission.

Apps with this permission let the system try
to bring up a network that isn't up, such as the mobile network
when the device is connected to a Wi-Fi network. Such an app calls
[`ConnectivityManager.requestNetwork(NetworkRequest, NetworkCallback)`](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
with a `NetworkCallback` to be called when the network is brought up.