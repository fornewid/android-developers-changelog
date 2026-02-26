---
title: https://developer.android.com/develop/connectivity/wifi/wifi-aware
url: https://developer.android.com/develop/connectivity/wifi/wifi-aware
source: md.txt
---

Wi-Fi Aware capabilities enable devices running Android 8.0 (API level 26) and
higher to discover and connect directly to each other without any other type of
connectivity between them. Wi-Fi Aware is also known as *Neighbor Awareness
Networking* (NAN).

Wi-Fi Aware networking works by forming clusters with neighboring devices, or
by creating a new cluster if the device is the first one in an area. This
clustering behavior applies to the entire device and is managed by the Wi-Fi
Aware system service; apps have no control over clustering behavior. Apps use
the Wi-Fi Aware APIs to talk to the Wi-Fi Aware system service, which manages
the Wi-Fi Aware hardware on the device.

The Wi-Fi Aware APIs let apps perform the following operations:

- **Discover other devices:** The API has a mechanism for finding other
  nearby devices. The process starts when one device *publishes* one
  or more discoverable services. Then, when a device *subscribes* to one or more
  services and enters the publisher's Wi-Fi range, the subscriber receives a
  notification that a matching publisher has been discovered. After the
  subscriber discovers a publisher, the subscriber can either send a short
  message or establish a network connection with the discovered device.
  Devices can concurrently be both publishers and subscribers.

- **Create a network connection:** After two devices have discovered each
  other they can create a
  bi-directional Wi-Fi Aware network connection without an access point.

Wi-Fi Aware network connections support higher throughput rates across longer
distances than [Bluetooth](https://developer.android.com/develop/connectivity/bluetooth)
connections. These types of connections are useful for apps that share large
amounts of data between users, such as photo-sharing apps.

## Android 13 (API level 33) enhancements

On devices running Android 13 (API level 33) and higher that support instant
communication mode, apps can use the
[`PublishConfig.Builder.setInstantCommunicationModeEnabled()`](https://developer.android.com/reference/android/net/wifi/aware/PublishConfig.Builder#setInstantCommunicationModeEnabled(boolean,%20int)) and
[`SubscribeConfig.Builder.setInstantCommunicationModeEnabled()`](https://developer.android.com/reference/android/net/wifi/aware/SubscribeConfig.Builder#setInstantCommunicationModeEnabled(boolean,%20int)) methods to
enable or disable instant communication mode for a publisher or subscriber
discovery session. Instant communication mode speeds up message exchange,
service discovery, and any data-path set up as part of a publisher or subscriber
discovery session. To determine whether a device supports instant communication
mode, use the [`isInstantCommunicationModeSupported()`](https://developer.android.com/reference/android/net/wifi/aware/Characteristics#isInstantCommunicationModeSupported()) method.

> [!NOTE]
> **Note:** Because instant communication mode uses additional power, this mode only remains enabled for 30 seconds from the time a publisher or subscriber discovery session is started.

## Android 12 (API level 31) enhancements

Android 12 (API level 31) adds some enhancements to Wi-Fi Aware:

- On devices running Android 12 (API level 31) or higher, you can use the [`onServiceLost()`](https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onServiceLost(android.net.wifi.aware.PeerHandle,%20int)) callback to be alerted when your app has lost a discovered service due to the service stopping or moving out of range.
- The setup of Wi-Fi Aware data paths has been simiplified. Earlier versions used L2 messaging to provide the MAC address of the initiator, which introduced latency. On devices running Android 12 and higher, the responder (server) can be configured to accept any peer---that is, it doesn't need to know the MAC address of the initator upfront. This speeds up datapath bringup and enables multiple point-to-point links with only one network request.
- Apps running on Android 12 or higher can use the [`WifiAwareManager.getAvailableAwareResources()`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#getAvailableAwareResources()) method to get the number of currently available data paths, publish sessions, and subscribe sessions. This can help the app determine if there are enough available resources to execute their desired functionality.

## Initial setup

To set up your app to use Wi-Fi Aware discovery and networking, perform the
following steps:

1. Request the following permissions in your app's manifest:

   ```xml
   <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
   <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
   <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
   <uses-permission android:name="android.permission.INTERNET" />
   <!-- If your app targets Android 13 (API level 33)
        or higher, you must declare the NEARBY_WIFI_DEVICES permission. -->
   <uses-permission android:name="android.permission.NEARBY_WIFI_DEVICES"
                    <!-- If your app derives location information from
                         Wi-Fi APIs, don't include the "usesPermissionFlags"
                         attribute. -->
                    android:usesPermissionFlags="neverForLocation" />
   <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
                    <!-- If any feature in your app relies on precise location
                         information, don't include the "maxSdkVersion"
                         attribute. -->
                    android:maxSdkVersion="32" />
   ```
2. Check whether the device supports Wi-Fi Aware with the
   `https://developer.android.com/reference/android/content/pm/PackageManager`
   API, as shown below:

   ### Kotlin

   ```kotlin
   context.packageManager.hasSystemFeature(PackageManager.FEATURE_WIFI_AWARE)
   ```

   ### Java

   ```java
   context.getPackageManager().hasSystemFeature(PackageManager.FEATURE_WIFI_AWARE);
   ```
3. Check whether Wi-Fi Aware is currently available. Wi-Fi Aware may exist on
   the device, but may not be currently available because the user has disabled
   Wi-Fi or Location. Depending on their hardware and firmware capabilities, some devices
   may not support Wi-Fi Aware if Wi-Fi Direct, SoftAP, or tethering is in
   use. To check whether Wi-Fi Aware is currently available, call
   `https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#isAvailable()`.

   The availability of Wi-Fi Aware can change at any time. Your app should
   register a `https://developer.android.com/reference/android/content/BroadcastReceiver` to receive
   `https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#ACTION_WIFI_AWARE_STATE_CHANGED`,
   which is sent whenever availability changes. When your app receives the
   broadcast intent, it should discard all existing sessions (assume that
   Wi-Fi Aware service was disrupted), then check the
   current state of availability and adjust its behavior accordingly.
   For example:

   ### Kotlin

   ```kotlin
   val wifiAwareManager = context.getSystemService(Context.WIFI_AWARE_SERVICE) as WifiAwareManager?
   val filter = IntentFilter(WifiAwareManager.ACTION_WIFI_AWARE_STATE_CHANGED)
   val myReceiver = object : BroadcastReceiver() {

       override fun onReceive(context: Context, intent: Intent) {
           // discard current sessions
           if (wifiAwareManager?.isAvailable) {
               ...
           } else {
               ...
           }
       }
   }
   context.registerReceiver(myReceiver, filter)
   ```

   ### Java

   ```java
   WifiAwareManager wifiAwareManager = 
           (WifiAwareManager)context.getSystemService(Context.WIFI_AWARE_SERVICE)
   IntentFilter filter =
           new IntentFilter(WifiAwareManager.ACTION_WIFI_AWARE_STATE_CHANGED);
   BroadcastReceiver myReceiver = new BroadcastReceiver() {
       @Override
       public void onReceive(Context context, Intent intent) {
           // discard current sessions
           if (wifiAwareManager.isAvailable()) {
               ...
           } else {
               ...
           }
       }
   };
   context.registerReceiver(myReceiver, filter);
   ```

For more information, see [Broadcasts](https://developer.android.com/guide/components/broadcasts).

> [!NOTE]
> **Note:** Make sure that you register the broadcast receiver *before* checking availability. Otherwise, there could be a period of time when the app thinks that Wi-Fi Aware is available but isn't notified if availability changes.

## Obtain a session

To start using Wi-Fi Aware, your app must obtain a
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession` by calling
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#attach(android.net.wifi.aware.AttachCallback, android.net.wifi.aware.IdentityChangedListener, android.os.Handler)`. This method
does the following:

- Turns on the Wi-Fi Aware hardware.
- Joins or forms a Wi-Fi Aware cluster.
- Creates a Wi-Fi Aware session with a unique namespace that acts as a container for all discovery sessions created within it.

If the app attaches successfully, the system executes the
`https://developer.android.com/reference/android/net/wifi/aware/AttachCallback#onAttached(android.net.wifi.aware.WifiAwareSession)` callback.
This callback provides a `https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession` object
that your app should use for all further session operations. An app can use the
session to [publish a service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#publish_a_service) or
[subscribe to a service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#subscribe_to_a_service).

Your app should call
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#attach(android.net.wifi.aware.AttachCallback, android.net.wifi.aware.IdentityChangedListener, android.os.Handler)` only once. If
your app calls `https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#attach(android.net.wifi.aware.AttachCallback, android.net.wifi.aware.IdentityChangedListener, android.os.Handler)`
multiple times, the app receives a different session for each call, each with
its own namespace. This could be useful in complex scenarios, but should
generally be avoided.

> [!NOTE]
> **Note:** As long as there are active sessions, the system maintains synchronization with a Wi-Fi Aware cluster. This clustering consumes resources and battery. To conserve resources, call `https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession#close()` when the session is no longer needed.

## Publish a service

To make a service discoverable, call the
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession#publish(android.net.wifi.aware.PublishConfig, android.net.wifi.aware.DiscoverySessionCallback, android.os.Handler)` method, which
takes the following parameters:

- `https://developer.android.com/reference/android/net/wifi/aware/PublishConfig` specifies the name of the service and other configuration properties, such as match filter.
- `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback` specifies the actions to execute when events occur, such as when the subscriber receives a message.

Here's an example:

### Kotlin

```kotlin
val config: PublishConfig = PublishConfig.Builder()
        .setServiceName(AWARE_FILE_SHARE_SERVICE_NAME)
        .build()
awareSession.publish(config, object : DiscoverySessionCallback() {

    override fun onPublishStarted(session: PublishDiscoverySession) {
        ...
    }

    override fun onMessageReceived(peerHandle: PeerHandle, message: ByteArray) {
        ...
    }
})
```

### Java

```java
PublishConfig config = new PublishConfig.Builder()
    .setServiceName("Aware_File_Share_Service_Name")
    .build();

awareSession.publish(config, new DiscoverySessionCallback() {
    @Override
    public void onPublishStarted(PublishDiscoverySession session) {
        ...
    }
    @Override
    public void onMessageReceived(PeerHandle peerHandle, byte[] message) {
        ...
    }
}, null);
```

If publication succeeds, then the
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onPublishStarted(android.net.wifi.aware.PublishDiscoverySession)`
callback method is called.

After publication, when devices running matching subscriber apps move into the
Wi-Fi range of the publishing device, the subscribers discover the service. When
a subscriber discovers a publisher, the publisher does not receive a
notification; if the subscriber sends a message to the publisher, however, then
the publisher receives a notification. When that happens, the
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onMessageReceived(android.net.wifi.aware.PeerHandle, byte[])`
callback method is called. You can use the
`https://developer.android.com/reference/android/net/wifi/aware/PeerHandle` argument from this method to
[send a message](https://developer.android.com/develop/connectivity/wifi/wifi-aware#send_a_message) back to the subscriber or
[create a connection](https://developer.android.com/develop/connectivity/wifi/wifi-aware#create_a_connection) to it.

To stop publishing the service, call
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession#close()`.
Discovery sessions are associated with their parent
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession`. If the parent session is
closed, its associated discovery sessions are also closed. While discarded
objects are closed as well, the system doesn't guarantee when out-of-scope
sessions are closed, so we recommend that you explicitly call the `close()`
methods.

## Subscribe to a service

To subscribe to a service, call the
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession#subscribe(android.net.wifi.aware.SubscribeConfig, android.net.wifi.aware.DiscoverySessionCallback, android.os.Handler)` method,
which takes the following parameters:

- `https://developer.android.com/reference/android/net/wifi/aware/SubscribeConfig` specifies the name of the service to subscribe to and other configuration properties, such as match filter.
- `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback` specifies the actions to execute when events occur, such as when a publisher is discovered.

Here's an example:

### Kotlin

```kotlin
val config: SubscribeConfig = SubscribeConfig.Builder()
        .setServiceName(AWARE_FILE_SHARE_SERVICE_NAME)
        .build()
awareSession.subscribe(config, object : DiscoverySessionCallback() {

    override fun onSubscribeStarted(session: SubscribeDiscoverySession) {
        ...
    }

    override fun onServiceDiscovered(
            peerHandle: PeerHandle,
            serviceSpecificInfo: ByteArray,
            matchFilter: List<ByteArray>
    ) {
        ...
    }
}, null)
```

### Java

```java
SubscribeConfig config = new SubscribeConfig.Builder()
    .setServiceName("Aware_File_Share_Service_Name")
    .build();

awareSession.subscribe(config, new DiscoverySessionCallback() {
    @Override
    public void onSubscribeStarted(SubscribeDiscoverySession session) {
        ...
    }

    @Override
    public void onServiceDiscovered(PeerHandle peerHandle,
            byte[] serviceSpecificInfo, List<byte[]> matchFilter) {
        ...
    }
}, null);
```

If the subscribe operation succeeds, the system calls the
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onSubscribeStarted(android.net.wifi.aware.SubscribeDiscoverySession)`
callback in your app. Because you can use the
`https://developer.android.com/reference/android/net/wifi/aware/SubscribeDiscoverySession` argument in the
callback to communicate with a publisher after your app has discovered one, you
should save this reference. You can update the subscribe session at any time by
calling
`https://developer.android.com/reference/android/net/wifi/aware/SubscribeDiscoverySession#updateSubscribe(android.net.wifi.aware.SubscribeConfig)`
on the discovery session.

At this point, your subscription waits for matching publishers to come into
Wi-Fi range. When this happens, the system executes the
[`onServiceDiscovered()`](https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onServiceDiscovered(android.net.wifi.aware.PeerHandle,%20byte%5B%5D,%20java.util.List%3Cbyte%5B%5D%3E))
callback method. You can use the `https://developer.android.com/reference/android/net/wifi/aware/PeerHandle`
argument from this callback to [send a message](https://developer.android.com/develop/connectivity/wifi/wifi-aware#send_a_message) or
[create a connection](https://developer.android.com/develop/connectivity/wifi/wifi-aware#create_a_connection) to that publisher.

To stop subscribing to a service, call
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession#close()`.
Discovery sessions are associated with their parent
`https://developer.android.com/reference/android/net/wifi/aware/WifiAwareSession`. If the parent session is
closed, its associated discovery sessions are also closed. While discarded
objects are closed as well, the system doesn't guarantee when out-of-scope
sessions are closed, so we recommend that you explicitly call the `close()`
methods.

## Send a message

To send a message to another device, you need the following objects:

- A `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession`. This object allows you
  to call
  `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession#sendMessage(android.net.wifi.aware.PeerHandle, int, byte[])`.
  Your app gets a `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession` by either
  [publishing a service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#publish_a_service) or [subscribing to a
  service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#subscribe_to_a_service).

- The other device's `https://developer.android.com/reference/android/net/wifi/aware/PeerHandle`, to route the
  message. Your app gets another device's
  `https://developer.android.com/reference/android/net/wifi/aware/PeerHandle` in one of two ways:

  - Your app publishes a service and receives a message from a subscriber. Your app gets the subscriber's `https://developer.android.com/reference/android/net/wifi/aware/PeerHandle` from the `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onMessageReceived(android.net.wifi.aware.PeerHandle, byte[])` callback.
  - Your app subscribes to a service. Then, when it discovers a matching publisher, your app gets the publisher's `https://developer.android.com/reference/android/net/wifi/aware/PeerHandle` from the [`onServiceDiscovered()`](https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onServiceDiscovered(android.net.wifi.aware.PeerHandle,%20byte%5B%5D,%20java.util.List%3Cbyte%5B%5D%3E)) callback.

To send a message, call
`https://developer.android.com/reference/android/net/wifi/aware/DiscoverySession#sendMessage(android.net.wifi.aware.PeerHandle, int, byte[])`. The
following callbacks might then occur:

- When the message is successfully received by the peer, the system calls the `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onMessageSendSucceeded(int)` callback in the *sending* app.
- When the peer receives a message, the system calls the `https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onMessageReceived(android.net.wifi.aware.PeerHandle, byte[])` callback in the *receiving* app.

> [!NOTE]
> **Note:** Messages are generally used for lightweight messaging, as they might not be delivered (or be delivered out-of-order or more than once) and are limited to about 255 bytes in length. To determine the exact length limit, call `https://developer.android.com/reference/android/net/wifi/aware/Characteristics#getMaxServiceSpecificInfoLength()`. For high speed, bi-directional communication, your app should [create a connection](https://developer.android.com/develop/connectivity/wifi/wifi-aware#create_a_connection) instead.

Though the `PeerHandle` is required to communicate with peers, you should not
rely on it as a permanent identifier of peers. Higher-level identifiers can be
used by the application--embedded in the discovery service itself or in
subsequent messages. You can embed an identifier in the discovery service with
the
[`setMatchFilter()`](https://developer.android.com/reference/android/net/wifi/aware/PublishConfig.Builder#setMatchFilter(java.util.List%3Cbyte%5B%5D%3E))
or
[`setServiceSpecificInfo()`](https://developer.android.com/reference/android/net/wifi/aware/PublishConfig.Builder#setServiceSpecificInfo(byte%5B%5D))
method of [`PublishConfig`](https://developer.android.com/reference/android/net/wifi/aware/PublishConfig) or
[`SubscribeConfig`](https://developer.android.com/reference/android/net/wifi/aware/SubscribeConfig). The
`setMatchFilter()` method affects discovery, whereas the
`setServiceSpecificInfo()` method does not affect discovery.

Embedding an identifier in a message implies modifying the message byte array to
include an identifier (for example, as the first couple of bytes).

## Create a connection

Wi-Fi Aware supports client-server networking between two Wi-Fi Aware devices.

To set up the client-server connection:

1. Use Wi-Fi Aware discovery to [publish a service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#publish_a_service) (on the
   server) and [subscribe to a service](https://developer.android.com/develop/connectivity/wifi/wifi-aware#subscribe_to_a_service) (on the
   client).

2. Once the subscriber discovers the publisher,
   [send a message](https://developer.android.com/develop/connectivity/wifi/wifi-aware#send_a_message) from the subscriber to the publisher.

3. Start a [`ServerSocket`](https://developer.android.com/reference/java/net/ServerSocket) on the publisher
   device and either set or obtain its port:

   ### Kotlin

   ```kotlin
   val ss = ServerSocket(0)
   val port = ss.localPort
   ```

   ### Java

   ```java
   ServerSocket ss = new ServerSocket(0);
   int port = ss.getLocalPort();
   ```
4. Use the [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) to
   request a Wi-Fi Aware network on the publisher using a
   [`WifiAwareNetworkSpecifier`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareNetworkSpecifier),
   specifying the discovery session and the
   [`PeerHandle`](https://developer.android.com/reference/android/net/wifi/aware/PeerHandle) of the subscriber,
   which you obtained from the message transmitted by the subscriber:

   ### Kotlin

   ```kotlin
   val networkSpecifier = WifiAwareNetworkSpecifier.Builder(discoverySession, peerHandle)
       .setPskPassphrase("somePassword")
       .setPort(port)
       .build()
   val myNetworkRequest = NetworkRequest.Builder()
       .addTransportType(NetworkCapabilities.TRANSPORT_WIFI_AWARE)
       .setNetworkSpecifier(networkSpecifier)
       .build()
   val callback = object : ConnectivityManager.NetworkCallback() {
       override fun onAvailable(network: Network) {
           ...
       }

       override fun onCapabilitiesChanged(network: Network, networkCapabilities: NetworkCapabilities) {
           ...
       }

       override fun onLost(network: Network) {
           ...
       }
   }

   connMgr.requestNetwork(myNetworkRequest, callback);
   ```

   ### Java

   ```java
   NetworkSpecifier networkSpecifier = new WifiAwareNetworkSpecifier.Builder(discoverySession, peerHandle)
       .setPskPassphrase("somePassword")
       .setPort(port)
       .build();
   NetworkRequest myNetworkRequest = new NetworkRequest.Builder()
       .addTransportType(NetworkCapabilities.TRANSPORT_WIFI_AWARE)
       .setNetworkSpecifier(networkSpecifier)
       .build();
   ConnectivityManager.NetworkCallback callback = new ConnectivityManager.NetworkCallback() {
       @Override
       public void onAvailable(Network network) {
           ...
       }

       @Override
       public void onCapabilitiesChanged(Network network, NetworkCapabilities networkCapabilities) {
           ...
       }

       @Override
       public void onLost(Network network) {
           ...
       }
   };

   ConnectivityManager connMgr.requestNetwork(myNetworkRequest, callback);
   ```
5. Once the publisher requests a network it should
   [send a message](https://developer.android.com/develop/connectivity/wifi/wifi-aware#send_a_message) to the subscriber.

6. Once the subscriber receives the message from publisher, request a Wi-Fi
   Aware network on the subscriber using the same method as on the publisher. Do
   not specify a port when creating the
   [`NetworkSpecifier`](https://developer.android.com/reference/android/net/NetworkSpecifier). The
   appropriate callback methods are called when the network connection is
   available, changed, or lost.

7. Once the `onAvailable()` method is called on the subscriber, a
   [`Network`](https://developer.android.com/reference/android/net/Network) object is available with
   which you can open a [`Socket`](https://developer.android.com/reference/java/net/Socket) to communicate
   with the `ServerSocket` on the publisher, but you need to know the
   `ServerSocket`'s IPv6 address and port. You get these from the
   [`NetworkCapabilities`](https://developer.android.com/reference/android/net/NetworkCapabilities) object
   provided in the `onCapabilitiesChanged()` callback:

   ### Kotlin

   ```kotlin
   val peerAwareInfo = networkCapabilities.transportInfo as WifiAwareNetworkInfo
   val peerIpv6 = peerAwareInfo.peerIpv6Addr
   val peerPort = peerAwareInfo.port
   ...
   val socket = network.getSocketFactory().createSocket(peerIpv6, peerPort)
   ```

   ### Java

   ```java
   WifiAwareNetworkInfo peerAwareInfo = (WifiAwareNetworkInfo) networkCapabilities.getTransportInfo();
   Inet6Address peerIpv6 = peerAwareInfo.getPeerIpv6Addr();
   int peerPort = peerAwareInfo.getPort();
   ...
   Socket socket = network.getSocketFactory().createSocket(peerIpv6, peerPort);
   ```
8. When you're finished with the network connection, call
   [`unregisterNetworkCallback()`](https://developer.android.com/reference/android/net/ConnectivityManager#unregisterNetworkCallback(android.app.PendingIntent)).

   > [!NOTE]
   > **Note:** Building a network request and specifying the required network capabilities aren't specific to the Wi-Fi Aware API. For more information on working with network requests, see [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager).

## Ranging peers and location-aware discovery

A device with [Wi-Fi RTT location](https://developer.android.com/develop/connectivity/wifi-rtt)
capabilities can directly measure distance to peers and use this information to
constrain Wi-Fi Aware service discovery.

The Wi-Fi RTT API allows direct ranging to a Wi-Fi Aware peer using either its
MAC address or its [PeerHandle](https://developer.android.com/reference/android/net/wifi/aware/PeerHandle).

Wi-Fi Aware discovery can be constrained to only discover services within a
particular geofence. For example, you can set up a geofence that allows discovery
of a device publishing an `"Aware_File_Share_Service_Name"` service that is no
closer than 3 meters (specified as 3,000 mm) and no further than 10 meters
(specified as 10,000 mm).

To enable geofencing, the publisher and the subscriber both must take action:

- The publisher must enable ranging on the published service using
  [setRangingEnabled(true)](https://developer.android.com/reference/android/net/wifi/aware/PublishConfig.Builder#setrangingenabled).

  If the publisher doesn't enable ranging, then any geofence constraints
  specified by the subscriber are ignored and normal discovery is performed,
  ignoring distance.
- The subscriber must specify a geofence using some combination of
  [setMinDistanceMm](https://developer.android.com/reference/android/net/wifi/aware/SubscribeConfig.Builder#setmindistancemm)
  and
  [setMaxDistanceMm](https://developer.android.com/reference/android/net/wifi/aware/SubscribeConfig.Builder#setmaxdistancemm).

  For either value, an unspecified distance implies no limit. Only specifying
  the maximum distance implies a minimum distance of 0. Only specifying the
  minimum distance implies no maximum.

When a peer service is discovered within a geofence, the
[onServiceDiscoveredWithinRange](https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onServiceDiscoveredWithinRange(android.net.wifi.aware.PeerHandle,%20byte%5B%5D,%20java.util.List%3Cbyte%5B%5D%3E,%20int))
callback is triggered, which provides the measured distance to the peer. The
direct Wi-Fi RTT API can then be called as necessary to measure distance at
later times.