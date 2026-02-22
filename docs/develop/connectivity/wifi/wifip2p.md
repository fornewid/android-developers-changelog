---
title: https://developer.android.com/develop/connectivity/wifi/wifip2p
url: https://developer.android.com/develop/connectivity/wifi/wifip2p
source: md.txt
---

[Wi-Fi Direct](https://www.wi-fi.org/discover-wi-fi/wi-fi-direct)
(P2P) allows devices with the appropriate hardware to connect directly to each
other via Wi-Fi without an intermediate access point. Using these APIs, you can
discover and connect to other devices when each device supports Wi-Fi P2P, then
communicate over a speedy connection across distances much longer than a
Bluetooth connection. This is useful for applications that share data among
users, such as a multiplayer game or a photo-sharing application.

The Wi-Fi P2P APIs consist of the following main parts:

- Methods that allow you to discover, request, and connect to peers, which are defined in the [`WifiP2pManager`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager) class.
- Listeners that allow you to be notified of the success or failure of `WifiP2pManager` method calls. When calling `WifiP2pManager` methods, each method can receive a specific listener passed in as a parameter.
- Intents that notify you of specific events detected by the Wi-Fi P2P framework, such as a dropped connection or a newly discovered peer.

You will often use these three main components of the APIs together. For
example, you can provide a
[`WifiP2pManager.ActionListener`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener)
to a call to
[`discoverPeers()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
so that
[`ActionListener.onSuccess()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener#onSuccess())
and
[`ActionListener.onFailure()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener#onFailure(int))
methods can notify you. A
[`WIFI_P2P_PEERS_CHANGED_ACTION`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_PEERS_CHANGED_ACTION)
intent is also broadcast if the `discoverPeers()` method discovers that the
peers list has changed.

## API overview

The `WifiP2pManager` class provides methods to enable you to interact with the
Wi-Fi hardware on your device to do things like discover and connect to peers.
The following actions are available:

**Table 1.** Wi-Fi P2P Methods

|---|---|
| **Method** | **Description** |
| ` `[initialize()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#initialize(android.content.Context,%20android.os.Looper,%20android.net.wifi.p2p.WifiP2pManager.ChannelListener))` ` | Registers the application with the Wi-Fi framework. Call this before calling any other Wi-Fi P2P method. |
| ` `[connect()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pConfig,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))` ` | Starts a peer-to-peer connection with a device with the specified configuration. |
| ` `[cancelConnect()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#cancelConnect(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))` ` | Cancels any ongoing peer-to-peer group negotiation. |
| ` `[requestConnectInfo()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestConnectionInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ConnectionInfoListener))` ` | Requests a device's connection information. |
| ` `[createGroup()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#createGroup(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))` ` | Creates a peer-to-peer group with the current device as the group owner. |
| ` `[removeGroup()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#removeGroup(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))` ` | Removes the current peer-to-peer group. |
| ` `[requestGroupInfo()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestGroupInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.GroupInfoListener))` ` | Requests peer-to-peer group information. |
| ` `[discoverPeers()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))` ` | Initiates peer discovery. |
| ` `[requestPeers()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.PeerListListener))` ` | Requests the current list of discovered peers. |

`WifiP2pManager` methods let
you pass in a listener, so that the Wi-Fi P2P framework can notify your activity
of the status of a call. The available listener interfaces and the corresponding
`WifiP2pManager` method calls
that use the listeners are described in table 2.

**Table 2.** Wi-Fi P2P Listeners

|---|---|
| **Listener interface** | **Associated actions** |
| ` `[WifiP2pManager.ActionListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener)` ` | `connect()`, `cancelConnect()`, `createGroup()`, `removeGroup()`, and `discoverPeers()` |
| ` `[WifiP2pManager.ChannelListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ChannelListener)` ` | ` initialize() ` |
| ` `[WifiP2pManager.ConnectionInfoListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ConnectionInfoListener)` ` | ` requestConnectInfo() ` |
| ` `[WifiP2pManager.GroupInfoListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.GroupInfoListener)` ` | ` requestGroupInfo() ` |
| ` `[WifiP2pManager.PeerListListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.PeerListListener)` ` | ` requestPeers() ` |

The Wi-Fi P2P APIs define intents that are broadcast when certain Wi-Fi P2P
events happen, such as when a new peer is discovered or when a device's Wi-Fi
state changes. You can register to receive these intents in your application by
[creating a broadcast receiver](https://developer.android.com/develop/connectivity/wifi/wifip2p#broadcast-receiver)
that handles these intents:

**Table 3.** Wi-Fi P2P Intents

|---|---|
| **Intent** | **Description** |
| ` `[WIFI_P2P_CONNECTION_CHANGED_ACTION](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_CONNECTION_CHANGED_ACTION)` ` | Broadcast when the state of the device's Wi-Fi connection changes. |
| ` `[WIFI_P2P_PEERS_CHANGED_ACTION](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_PEERS_CHANGED_ACTION)` ` | Broadcast when you call `discoverPeers()`. You will usually call `requestPeers()` to get an updated list of peers if you handle this intent in your application. |
| ` `[WIFI_P2P_STATE_CHANGED_ACTION](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_STATE_CHANGED_ACTION)` ` | Broadcast when Wi-Fi P2P is enabled or disabled on the device. |
| ` `[WIFI_P2P_THIS_DEVICE_CHANGED_ACTION](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_THIS_DEVICE_CHANGED_ACTION)` ` | Broadcast when a device's details have changed, such as the device's name. |

## Create a broadcast receiver for Wi-Fi P2P intents

A broadcast receiver allows you to receive intents broadcast by the Android
system, so that your application can respond to events that you are interested
in. The basic steps for creating a broadcast receiver to handle Wi-Fi P2P
intents are as follows:

1. Create a class that extends the
   [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) class.
   For the class' constructor, you will use parameters for the `WifiP2pManager`,
   `WifiP2pManager.Channel`, and the activity that this broadcast receiver will
   be registered in. This allows the broadcast receiver to send updates to the
   activity as well as have access to the Wi-Fi hardware and a communication
   channel if needed.

2. In the broadcast receiver, check for the intents that you are interested in
   in the
   [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
   method. Perform any necessary actions depending on the intent that is
   received. For example, if the broadcast receiver receives a
   `WIFI_P2P_PEERS_CHANGED_ACTION` intent, you can call the `requestPeers()`
   method to get a list of the currently discovered peers.

The following code shows you how to create a typical broadcast receiver. The
broadcast receiver takes a `WifiP2pManager` object and an activity as arguments
and uses these two classes to appropriately carry out the needed actions when
the broadcast receiver receives an intent:  

### Kotlin

```kotlin
/**
* A BroadcastReceiver that notifies of important Wi-Fi p2p events.
*/
class WiFiDirectBroadcastReceiver(
       private val manager: WifiP2pManager,
       private val channel: WifiP2pManager.Channel,
       private val activity: MyWifiActivity
) : BroadcastReceiver() {

   override fun onReceive(context: Context, intent: Intent) {
       val action: String = intent.action
       when (action) {
           WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION -> {
               // Check to see if Wi-Fi is enabled and notify appropriate activity
           }
           WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION -> {
               // Call WifiP2pManager.requestPeers() to get a list of current peers
           }
           WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION -> {
               // Respond to new connection or disconnections
           }
           WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION -> {
               // Respond to this device's wifi state changing
           }
       }
   }
}
```

### Java

```java
/**
* A BroadcastReceiver that notifies of important Wi-Fi p2p events.
*/
public class WiFiDirectBroadcastReceiver extends BroadcastReceiver {

   private WifiP2pManager manager;
   private Channel channel;
   private MyWiFiActivity activity;

   public WiFiDirectBroadcastReceiver(WifiP2pManager manager, Channel channel,
           MyWifiActivity activity) {
       super();
       this.manager = manager;
       this.channel = channel;
       this.activity = activity;
   }

   @Override
   public void onReceive(Context context, Intent intent) {
       String action = intent.getAction();

       if (WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION.equals(action)) {
           // Check to see if Wi-Fi is enabled and notify appropriate activity
       } else if (WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION.equals(action)) {
           // Call WifiP2pManager.requestPeers() to get a list of current peers
       } else if (WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION.equals(action)) {
           // Respond to new connection or disconnections
       } else if (WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION.equals(action)) {
           // Respond to this device's wifi state changing
       }
   }
}
```

On devices running Android 10 and higher, the following broadcast intents are
non-sticky:

`WIFI_P2P_CONNECTION_CHANGED_ACTION`
:   Applications can use
    `requestConnectionInfo()`,
    [`requestNetworkInfo()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestNetworkInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.NetworkInfoListener)),
    or `requestGroupInfo()` to retrieve the current connection information.

`WIFI_P2P_THIS_DEVICE_CHANGED_ACTION`
:   Applications can use
    [`requestDeviceInfo()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestDeviceInfo(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.DeviceInfoListener))
    to retrieve the current connection information.

## Create a Wi-Fi P2P application

Creating a Wi-Fi P2P application involves creating and registering a broadcast
receiver for your application, discovering peers, connecting to a peer, and
transferring data to a peer. The following sections describe how to do this.

### Initial setup

Before using the Wi-Fi P2P APIs, you must ensure that your application can
access the hardware and that the device supports the Wi-Fi P2P protocol. If
Wi-Fi P2P is supported, you can obtain an instance of `WifiP2pManager`, create
and register your broadcast receiver, and begin using the Wi-Fi P2P APIs.

1. Request permission to use the Wi-Fi hardware on the device and declare
   your application to have the correct minimum SDK version in the Android
   manifest:

       <uses-sdk android:minSdkVersion="14" />
       <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
       <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
       <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
       <uses-permission android:name="android.permission.INTERNET" />
       <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
       <!-- If your app targets Android 13 (API level 33)
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

   | **Note:** On apps that target Android 13 (API level 33) and higher, both `discoverPeers()` and `connect()` require the [`android.permission.NEARBY_WIFI_DEVICES`](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES) permission. On apps that target earlier versions of Android, these methods require the `ACCESS_FINE_LOCATION` permission instead. Since these permissions are [dangerous
   | permissions](https://developer.android.com/develop/permissions/overview#runtime), you must [request them at runtime](https://developer.android.com/training/permissions/requesting) before you can call `discoverPeers()` or `connect()`.

   Besides the preceding permissions, the following APIs also require Location
   Mode to be enabled:
   - [`discoverPeers()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
   - [`discoverServices()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverServices(android.net.wifi.p2p.WifiP2pManager.Channel,%2520android.net.wifi.p2p.WifiP2pManager.ActionListener))
   - [`requestPeers()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.PeerListListener))
2. Check to see if Wi-Fi P2P is on and supported. A good place to check this is
   in your broadcast receiver when it receives the
   `WIFI_P2P_STATE_CHANGED_ACTION` intent. Notify your activity of the Wi-Fi P2P
   state and react accordingly:

   ### Kotlin

   ```kotlin
   override fun onReceive(context: Context, intent: Intent) {
   ...
   val action: String = intent.action
   when (action) {
      WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION -> {
          val state = intent.getIntExtra(WifiP2pManager.EXTRA_WIFI_STATE, -1)
          when (state) {
              WifiP2pManager.WIFI_P2P_STATE_ENABLED -> {
                  // Wifi P2P is enabled
              }
              else -> {
                  // Wi-Fi P2P is not enabled
              }
          }
      }
   }
   ...
   }
   ```

   ### Java

   ```java
   @Override
   public void onReceive(Context context, Intent intent) {
   ...
   String action = intent.getAction();
   if (WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION.equals(action)) {
      int state = intent.getIntExtra(WifiP2pManager.EXTRA_WIFI_STATE, -1);
      if (state == WifiP2pManager.WIFI_P2P_STATE_ENABLED) {
          // Wifi P2P is enabled
      } else {
          // Wi-Fi P2P is not enabled
      }
   }
   ...
   }
   ```
3. In your activity's
   [`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))
   method, obtain an instance of `WifiP2pManager` and register your application
   with the Wi-Fi P2P framework by calling `initialize()`. This method returns a
   `WifiP2pManager.Channel`, which is used to connect your application to the
   Wi-Fi P2P framework. You should also create an instance of your broadcast
   receiver with the `WifiP2pManager` and `WifiP2pManager.Channel` objects along
   with a reference to your activity. This enables your broadcast receiver to
   notify your activity of interesting events and update it accordingly. It also
   enables you to manipulate the device's Wi-Fi state if necessary:

   ### Kotlin

   ```kotlin
   val manager: WifiP2pManager? by lazy(LazyThreadSafetyMode.NONE) {
      getSystemService(Context.WIFI_P2P_SERVICE) as WifiP2pManager?
   }

   var channel: WifiP2pManager.Channel? = null
   var receiver: BroadcastReceiver? = null

   override fun onCreate(savedInstanceState: Bundle?) {
      ...

      channel = manager?.initialize(this, mainLooper, null)
      channel?.also { channel ->
          receiver = WiFiDirectBroadcastReceiver(manager, channel, this)
      }
   }
   ```

   ### Java

   ```java
   WifiP2pManager manager;
   Channel channel;
   BroadcastReceiver receiver;
   ...
   @Override
   protected void onCreate(Bundle savedInstanceState){
      ...
      manager = (WifiP2pManager) getSystemService(Context.WIFI_P2P_SERVICE);
      channel = manager.initialize(this, getMainLooper(), null);
      receiver = new WiFiDirectBroadcastReceiver(manager, channel, this);
      ...
   }
   ```
4. Create an intent filter and add the same intents that your broadcast receiver
   checks for:

   ### Kotlin

   ```kotlin
   val intentFilter = IntentFilter().apply {
      addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION)
      addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION)
      addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION)
      addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION)
   }
   ```

   ### Java

   ```java
   IntentFilter intentFilter;
   ...
   @Override
   protected void onCreate(Bundle savedInstanceState){
      ...
      intentFilter = new IntentFilter();
      intentFilter.addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION);
      intentFilter.addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION);
      intentFilter.addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION);
      intentFilter.addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION);
      ...
   }
   ```
5. Register the broadcast receiver in the
   [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) method of your
   activity and unregister it in the
   [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) method of your
   activity:

   ### Kotlin

   ```kotlin
   /* register the broadcast receiver with the intent values to be matched */
   override fun onResume() {
      super.onResume()
      receiver?.also { receiver ->
          registerReceiver(receiver, intentFilter)
      }
   }

   /* unregister the broadcast receiver */
   override fun onPause() {
      super.onPause()
      receiver?.also { receiver ->
          unregisterReceiver(receiver)
      }
   }
   ```

   ### Java

   ```java
   /* register the broadcast receiver with the intent values to be matched */
   @Override
   protected void onResume() {
      super.onResume();
      registerReceiver(receiver, intentFilter);
   }
   /* unregister the broadcast receiver */
   @Override
   protected void onPause() {
      super.onPause();
      unregisterReceiver(receiver);
   }
   ```
6. When you have gotten a `WifiP2pManager.Channel` and set up a broadcast
   receiver, your application can make Wi-Fi P2P method calls and receive Wi-Fi
   P2P intents.

7. Implement your application, using the Wi-Fi P2P features by calling the
   methods in `WifiP2pManager`.

The next sections describe how to do common actions such as discovering and
connecting to peers.

### Discover peers

Call `discoverPeers()` to detect available peers that are in range and available
for connection. The call to this function is asynchronous and a success or
failure is communicated to your application with `onSuccess()` and `onFailure()`
if you created a `WifiP2pManager.ActionListener`. The `onSuccess()` method only
notifies you that the discovery process succeeded and does not provide any
information about the actual peers that it discovered, if any. The following
code sample shows how to set this up.  

### Kotlin

```kotlin
manager?.discoverPeers(channel, object : WifiP2pManager.ActionListener {

   override fun onSuccess() {
       ...
   }

   override fun onFailure(reasonCode: Int) {
       ...
   }
})
```

### Java

```java
manager.discoverPeers(channel, new WifiP2pManager.ActionListener() {
   @Override
   public void onSuccess() {
       ...
   }

   @Override
   public void onFailure(int reasonCode) {
       ...
   }
});
```

If the discovery process succeeds and detects peers, the system broadcasts the
`WIFI_P2P_PEERS_CHANGED_ACTION` intent, which you can listen for in a broadcast
receiver to get a list of peers. When your application receives the
`WIFI_P2P_PEERS_CHANGED_ACTION` intent, you can request a list of the discovered
peers with `requestPeers()`. The following code shows how to set this up.  

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
   val action: String = intent.action
   when (action) {
       ...
       WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION -> {
           manager?.requestPeers(channel) { peers: WifiP2pDeviceList? ->
               // Handle peers list
           }
       }
       ...
   }
}
```

### Java

```java
PeerListListener myPeerListListener;
...
if (WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION.equals(action)) {

   // request available peers from the wifi p2p manager. This is an
   // asynchronous call and the calling activity is notified with a
   // callback on PeerListListener.onPeersAvailable()
   if (manager != null) {
       manager.requestPeers(channel, myPeerListListener);
   }
}
```

The `requestPeers()` method is also asynchronous and can notify your activity
when a list of peers is available with
[`onPeersAvailable()`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.PeerListListener#onPeersAvailable(android.net.wifi.p2p.WifiP2pDeviceList)),
which is defined in the `WifiP2pManager.PeerListListener` interface. The
`onPeersAvailable()` method provides you with a
[`WifiP2pDeviceList`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pDeviceList), which
you can iterate through to find the peer to connect to.

### Connect to peers

Once you have gotten a list of possible peers and selected a device to connect
to, call the `connect()` method to connect to the device. This method call
requires a [`WifiP2pConfig`](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pConfig)
object that contains information about the device to connect to.
`WifiP2pManager.ActionListener` can notify you of a connection success or
failure. The following code shows you how to create a connection to a device.  

### Kotlin

```kotlin
val device: WifiP2pDevice = ...
val config = WifiP2pConfig()
config.deviceAddress = device.deviceAddress
channel?.also { channel ->
   manager?.connect(channel, config, object : WifiP2pManager.ActionListener {

       override fun onSuccess() {
           //success logic
       }

       override fun onFailure(reason: Int) {
           //failure logic
       }
   }
)}
```

### Java

```java
//obtain a peer from the WifiP2pDeviceList
WifiP2pDevice device;
WifiP2pConfig config = new WifiP2pConfig();
config.deviceAddress = device.deviceAddress;
manager.connect(channel, config, new ActionListener() {

   @Override
   public void onSuccess() {
       //success logic
   }

   @Override
   public void onFailure(int reason) {
       //failure logic
   }
});
```

### Transfer data

Once a connection is established, you can transfer data between the devices with
sockets. The basic steps of transferring data are as follows:

1. Create a [`ServerSocket`](https://developer.android.com/reference/java/net/ServerSocket). This socket waits for a connection from a client on a specified port and blocks until it happens, so do this in a background thread.
2. Create a client [`Socket`](https://developer.android.com/reference/java/net/Socket). The client uses the IP address and port of the server socket to connect to the server device.
3. Send data from the client to the server. When the client socket successfully connects to the server socket, you can send data from the client to the server with byte streams.
4. The server socket waits for a client connection (with the [`accept()`](https://developer.android.com/reference/java/net/ServerSocket#accept()) method). This call blocks until a client connects, so call this in another thread. When a connection happens, the server device can receive the data from the client.

The following example, modified from the [Wi-Fi P2P
Demo](https://android.googlesource.com/platform/development/+/master/samples/WiFiDirectDemo/),
shows you how to create this client-server socket communication and transfer
JPEG images from a client to a server with a service. For a complete working
example, compile and run the demo.  

### Kotlin

```kotlin
class FileServerAsyncTask(
       private val context: Context,
       private var statusText: TextView
) : AsyncTask<Void, Void, String?>() {

   override fun doInBackground(vararg params: Void): String? {
       /**
        * Create a server socket.
        */
       val serverSocket = ServerSocket(8888)
       return serverSocket.use {
           /**
            * Wait for client connections. This call blocks until a
            * connection is accepted from a client.
            */
           val client = serverSocket.accept()
           /**
            * If this code is reached, a client has connected and transferred data
            * Save the input stream from the client as a JPEG file
            */
           val f = File(Environment.getExternalStorageDirectory().absolutePath +
                   "/${context.packageName}/wifip2pshared-${System.currentTimeMillis()}.jpg")
           val dirs = File(f.parent)

           dirs.takeIf { it.doesNotExist() }?.apply {
               mkdirs()
           }
           f.createNewFile()
           val inputstream = client.getInputStream()
           copyFile(inputstream, FileOutputStream(f))
           serverSocket.close()
           f.absolutePath
       }
   }

   private fun File.doesNotExist(): Boolean = !exists()

   /**
    * Start activity that can handle the JPEG image
    */
   override fun onPostExecute(result: String?) {
       result?.run {
           statusText.text = "File copied - $result"
           val intent = Intent(android.content.Intent.ACTION_VIEW).apply {
               setDataAndType(Uri.parse("file://$result"), "image/*")
           }
           context.startActivity(intent)
       }
   }
}
```

### Java

```java
public static class FileServerAsyncTask extends AsyncTask {

   private Context context;
   private TextView statusText;

   public FileServerAsyncTask(Context context, View statusText) {
       this.context = context;
       this.statusText = (TextView) statusText;
   }

   @Override
   protected String doInBackground(Void... params) {
       try {

           /**
            * Create a server socket and wait for client connections. This
            * call blocks until a connection is accepted from a client
            */
           ServerSocket serverSocket = new ServerSocket(8888);
           Socket client = serverSocket.accept();

           /**
            * If this code is reached, a client has connected and transferred data
            * Save the input stream from the client as a JPEG file
            */
           final File f = new File(Environment.getExternalStorageDirectory() + "/"
                   + context.getPackageName() + "/wifip2pshared-" + System.currentTimeMillis()
                   + ".jpg");

           File dirs = new File(f.getParent());
           if (!dirs.exists())
               dirs.mkdirs();
           f.createNewFile();
           InputStream inputstream = client.getInputStream();
           copyFile(inputstream, new FileOutputStream(f));
           serverSocket.close();
           return f.getAbsolutePath();
       } catch (IOException e) {
           Log.e(WiFiDirectActivity.TAG, e.getMessage());
           return null;
       }
   }

   /**
    * Start activity that can handle the JPEG image
    */
   @Override
   protected void onPostExecute(String result) {
       if (result != null) {
           statusText.setText("File copied - " + result);
           Intent intent = new Intent();
           intent.setAction(android.content.Intent.ACTION_VIEW);
           intent.setDataAndType(Uri.parse("file://" + result), "image/*");
           context.startActivity(intent);
       }
   }
}
```

On the client, connect to the server socket with a client socket and transfer
data. This example transfers a JPEG file on the client device's file system.  

### Kotlin

```kotlin
val context = applicationContext
val host: String
val port: Int
val len: Int
val socket = Socket()
val buf = ByteArray(1024)
...
try {
   /**
    * Create a client socket with the host,
    * port, and timeout information.
    */
   socket.bind(null)
   socket.connect((InetSocketAddress(host, port)), 500)

   /**
    * Create a byte stream from a JPEG file and pipe it to the output stream
    * of the socket. This data is retrieved by the server device.
    */
   val outputStream = socket.getOutputStream()
   val cr = context.contentResolver
   val inputStream: InputStream = cr.openInputStream(Uri.parse("path/to/picture.jpg"))
   while (inputStream.read(buf).also { len = it } != -1) {
       outputStream.write(buf, 0, len)
   }
   outputStream.close()
   inputStream.close()
} catch (e: FileNotFoundException) {
   //catch logic
} catch (e: IOException) {
   //catch logic
} finally {
   /**
    * Clean up any open sockets when done
    * transferring or if an exception occurred.
    */
   socket.takeIf { it.isConnected }?.apply {
       close()
   }
}
```

### Java

```java
Context context = this.getApplicationContext();
String host;
int port;
int len;
Socket socket = new Socket();
byte buf[]  = new byte[1024];
...
try {
   /**
    * Create a client socket with the host,
    * port, and timeout information.
    */
   socket.bind(null);
   socket.connect((new InetSocketAddress(host, port)), 500);

   /**
    * Create a byte stream from a JPEG file and pipe it to the output stream
    * of the socket. This data is retrieved by the server device.
    */
   OutputStream outputStream = socket.getOutputStream();
   ContentResolver cr = context.getContentResolver();
   InputStream inputStream = null;
   inputStream = cr.openInputStream(Uri.parse("path/to/picture.jpg"));
   while ((len = inputStream.read(buf)) != -1) {
       outputStream.write(buf, 0, len);
   }
   outputStream.close();
   inputStream.close();
} catch (FileNotFoundException e) {
   //catch logic
} catch (IOException e) {
   //catch logic
}

/**
* Clean up any open sockets when done
* transferring or if an exception occurred.
*/
finally {
   if (socket != null) {
       if (socket.isConnected()) {
           try {
               socket.close();
           } catch (IOException e) {
               //catch logic
           }
       }
   }
}
```