---
title: https://developer.android.com/develop/connectivity/wifi/wifi-direct
url: https://developer.android.com/develop/connectivity/wifi/wifi-direct
source: md.txt
---

[Wi-Fi Direct](https://www.wi-fi.org/discover-wi-fi/wi-fi-direct) (also known as peer-to-peer or P2P) allows your application to quickly find and interact with nearby
devices, at a range beyond the capabilities of Bluetooth.

The Wi-Fi Direct (P2P) APIs allow applications to connect to nearby devices without
needing to connect to a network or hotspot.
If your app is designed to be a part of a secure, near-range network, Wi-Fi
Direct is a more suitable option than traditional Wi-Fi ad-hoc
networking for the following reasons:

- Wi-Fi Direct supports WPA2 encryption. (Some ad-hoc networks support only WEP encryption.)
- Devices can broadcast the services that they provide, which helps other devices discover suitable peers more easily.
- When determining which device should be the group owner for the network, Wi-Fi Direct examines each device's power management, UI, and service capabilities and uses this information to choose the device that can handle server responsibilities most effectively.
- Android doesn't support Wi-Fi ad-hoc mode.


This lesson shows you how to find and connect to nearby devices using Wi-Fi P2P.

## Set up application permissions

To use Wi-Fi Direct, add the
`https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION`,
`https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE`,
`https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE`, and
`https://developer.android.com/reference/android/Manifest.permission#INTERNET` permissions to your manifest.
If your app targets Android 13 (API level 33) or higher, also add the
`https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES`
permission to your manifest. Wi-Fi
Direct doesn't require an internet connection, but it does use standard Java
sockets, which requires the `https://developer.android.com/reference/android/Manifest.permission#INTERNET`
permission. So you need the following permissions to use Wi-Fi Direct:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.nsdcha<t"
    ...
    !-- If your  app targets  Android13 (API level33)
         or higher, you must declare the NEARBY_WIFI_DE>VICES per<mission. --
        uses-permission android:name="android.permission.NEAR<BY_WIFI_DEVICES"
        !-- If your app derives location information from Wi-Fi APIs,
             don't include the &>quot;usesPermissionFlags" attribute. --
        andr>oid:usesPermis<sionFlags="neverForLocation" /
        
    uses-permission
        android:required="true"
       < android:name="android.permission.ACCESS_FINE_LOCATION"
        !-- If any feature in your app relies on precise location> information,
             don't >inclu<de the "maxSdkVersion" attribute. --
        android:maxSdkVersion="32" /
    uses-permi>ssion<
        android:required="true"
        android:name="android.permission.ACCESS_WIFI_STATE&q>uot;/<
    uses-permission
        android:required="true"
        android:name="android.p>ermission.CHANGE_WIFI_STATE"/
    uses-permission
        android:required="true"
        android:name="android.permission.INTERNET"/
    ...
```


Besides the preceding permissions, the following APIs also require Location Mode to be enabled:

- `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener)`
- `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverServices(android.net.wifi.p2p.WifiP2pManager.Channel,%2520android.net.wifi.p2p.WifiP2pManager.ActionListener)`
- `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%2520android.net.wifi.p2p.WifiP2pManager.PeerListListener)`

<br />

## Set up a broadcast receiver and peer-to-peer manager

To use Wi-Fi Direct, you need to listen for broadcast intents that tell your
application when certain events have occurred. In your application, instantiate
an `https://developer.android.com/reference/android/content/IntentFilter` and set it to listen for the following:

`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_STATE_CHANGED_ACTION`
:   Indicates whether Wi-Fi Direct is enabled

`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_PEERS_CHANGED_ACTION`
:   Indicates that the available peer list has changed.

`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_CONNECTION_CHANGED_ACTION`
:
    Indicates the state of Wi-Fi Direct connectivity has changed. Starting with
    Android 10, this is not sticky. If your app has relied on receiving these
    broadcasts at registration because they had been sticky, use the appropriate `get`
    method at initialization to obtain the information instead.

`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_THIS_DEVICE_CHANGED_ACTION`
:
    Indicates this device's configuration details have changed. Starting with
    Android 10, this is not sticky. If your app has relied on receiving these
    broadcasts at registration because they had been sticky, use the appropriate `get`
    method at initialization to obtain the information instead.

### Kotlin

```kotlin
private val intentFilter = IntentFilter()
...
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main)

    // Indicates a change in the Wi-Fi Direct status.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION)

    // Indicates a change in the list of available peers.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION)

    // Indicates the state of Wi-Fi Direct connectivity has changed.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION)

    // Indicates this device's details have changed.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION)
    ...
}
```

### Java

```java
private final IntentFilter intentFilter = new IntentFilter();
...
@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main);

    // Indicates a change in the Wi-Fi Direct status.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION);

    // Indicates a change in the list of available peers.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION);

    // Indicates the state of Wi-Fi Direct connectivity has changed.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION);

    // Indicates this device's details have changed.
    intentFilter.addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION);
    ...
}
```

At the end of the `https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)` method, get an instance of the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager`, and call its `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#initialize(android.content.Context, android.os.Looper, android.net.wifi.p2p.WifiP2pManager.ChannelListener)`
method. This method returns a `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.Channel` object, which you'll use later to
connect your app to the Wi-Fi Direct framework.

### Kotlin

```kotlin
private lateinit var channel: WifiP2pManager.Channel
private lateinit var manager: WifiP2pManager

override fun onCreate(savedInstanceState: Bundle?) {
    ...
    manager = getSystemService(Context.WIFI_P2P_SERVICE) as WifiP2pManager
    channel = manager.initialize(this, mainLooper, null)
}
```

### Java

```java
Channel channel;
WifiP2pManager manager;

@Override
public void onCreate(Bundle savedInstanceState) {
    ...
    manager = (WifiP2pManager) getSystemService(Context.WIFI_P2P_SERVICE);
    channel = manager.initialize(this, getMainLooper(), null);
}
```

Now create a new `https://developer.android.com/reference/android/content/BroadcastReceiver` class that you'll use to listen for changes
to the system's Wi-Fi state. In the `https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)`
method, add a condition to handle each state change listed above.

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    when(intent.action) {
        WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION -> {
            // Determine if Wi-Fi Direct mode is enabled or not, alert
            // the Activity.
            val state = intent.getIntExtra(WifiP2pManager.EXTRA_WIFI_STATE, -1)
            activity.isWifiP2pEnabled = state == WifiP2pManager.WIFI_P2P_STATE_ENABLED
        }
        WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION -> {

            // The peer list has changed! We should probably do something about
            // that.

        }
        WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION -> {

            // Connection state changed! We should probably do something about
            // that.

        }
        WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION -> {
            (activity.supportFragmentManager.findFragmentById(R.id.frag_list) as DeviceListFragment)
                    .apply {
                        updateThisDevice(
                                intent.getParcelableExtra(
                                        WifiP2pManager.EXTRA_WIFI_P2P_DEVICE) as WifiP2pDevice
                        )
                    }
        }
    }
}
```

### Java

```java
@Override
public void onReceive(Context context, Intent intent) {
    String action = intent.getAction();
    if (WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION.equals(action)) {
        // Determine if Wi-Fi Direct mode is enabled or not, alert
        // the Activity.
        int state = intent.getIntExtra(WifiP2pManager.EXTRA_WIFI_STATE, -1);
        if (state == WifiP2pManager.WIFI_P2P_STATE_ENABLED) {
            activity.setIsWifiP2pEnabled(true);
        } else {
            activity.setIsWifiP2pEnabled(false);
        }
    } else if (WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION.equals(action)) {

        // The peer list has changed! We should probably do something about
        // that.

    } else if (WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION.equals(action)) {

        // Connection state changed! We should probably do something about
        // that.

    } else if (WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION.equals(action)) {
        DeviceListFragment fragment = (DeviceListFragment) activity.getFragmentManager()
                .findFragmentById(R.id.frag_list);
        fragment.updateThisDevice((WifiP2pDevice) intent.getParcelableExtra(
                WifiP2pManager.EXTRA_WIFI_P2P_DEVICE));

    }
}
```

Finally, add code to register the intent filter and broadcast receiver when
your main activity is active, and unregister them when the activity is paused.
The best place to do this is the `https://developer.android.com/reference/android/app/Activity#onResume()` and
`https://developer.android.com/reference/android/app/Activity#onPause()` methods.

### Kotlin

```kotlin
/** register the BroadcastReceiver with the intent values to be matched  */
public override fun onResume() {
    super.onResume()
    receiver = WiFiDirectBroadcastReceiver(manager, channel, this)
    registerReceiver(receiver, intentFilter)
}

public override fun onPause() {
    super.onPause()
    unregisterReceiver(receiver)
}
```

### Java

```java
/** register the BroadcastReceiver with the intent values to be matched */
@Override
public void onResume() {
    super.onResume();
    receiver = new WiFiDirectBroadcastReceiver(manager, channel, this);
    registerReceiver(receiver, intentFilter);
}

@Override
public void onPause() {
    super.onPause();
    unregisterReceiver(receiver);
}
```

## Initiate peer discovery

To start searching for nearby devices with Wi-Fi P2P, call `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.ActionListener)`. This method takes the
following arguments:

- The `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.Channel` you received back when you initialized the peer-to-peer mManager
- An implementation of `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener` with methods the system invokes for successful and unsuccessful discovery.

### Kotlin

```kotlin
manager.discoverPeers(channel, object : WifiP2pManager.ActionListener {

    override fun onSuccess() {
        // Code for when the discovery initiation is successful goes here.
        // No services have actually been discovered yet, so this method
        // can often be left blank. Code for peer discovery goes in the
        // onReceive method, detailed below.
    }

    override fun onFailure(reasonCode: Int) {
        // Code for when the discovery initiation fails goes here.
        // Alert the user that something went wrong.
    }
})
```

### Java

```java
manager.discoverPeers(channel, new WifiP2pManager.ActionListener() {

    @Override
    public void onSuccess() {
        // Code for when the discovery initiation is successful goes here.
        // No services have actually been discovered yet, so this method
        // can often be left blank. Code for peer discovery goes in the
        // onReceive method, detailed below.
    }

    @Override
    public void onFailure(int reasonCode) {
        // Code for when the discovery initiation fails goes here.
        // Alert the user that something went wrong.
    }
});
```

Keep in mind that this only *initiates* peer discovery. The
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.ActionListener)` method starts the discovery process and then
immediately returns. The system notifies you if the peer discovery process is
successfully initiated by calling methods in the provided action listener.
Also, discovery remains active until a connection is initiated or a P2P group is
formed.

## Fetch the list of peers

Now write the code that fetches and processes the list of peers. First
implement the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.PeerListListener`
interface, which provides information about the peers that Wi-Fi Direct has
detected. This information also allows your app to determine when peers join or
leave the network. The following code snippet illustrates these operations
related to peers:

### Kotlin

```kotlin
private val peers = mutableListOf<WifiP2pDevice>()
...

private val peerListListener = WifiP2pManager.PeerListListener { peerList ->
    val refreshedPeers = peerList.deviceList
    if (refreshedPeers != peers) {
        peers.clear()
        peers.addAll(refreshedPeers)

        // If an AdapterView is backed by this data, notify it
        // of the change. For instance, if you have a ListView of
        // available peers, trigger an update.
        (listAdapter as WiFiPeerListAdapter).notifyDataSetChanged()

        // Perform any other updates needed based on the new list of
        // peers connected to the Wi-Fi P2P network.
    }

    if (peers.isEmpty()) {
        Log.d(TAG, "No devices found")
        return@PeerListListener
    }
}
```

### Java

```java
private List<WifiP2pDevice> peers = new ArrayList<WifiP2pDevice>();
...

private PeerListListener peerListListener = new PeerListListener() {
    @Override
    public void onPeersAvailable(WifiP2pDeviceList peerList) {

        List<WifiP2pDevice> refreshedPeers = peerList.getDeviceList();
        if (!refreshedPeers.equals(peers)) {
            peers.clear();
            peers.addAll(refreshedPeers);

            // If an AdapterView is backed by this data, notify it
            // of the change. For instance, if you have a ListView of
            // available peers, trigger an update.
            ((WiFiPeerListAdapter) getListAdapter()).notifyDataSetChanged();

            // Perform any other updates needed based on the new list of
            // peers connected to the Wi-Fi P2P network.
        }

        if (peers.size() == 0) {
            Log.d(WiFiDirectActivity.TAG, "No devices found");
            return;
        }
    }
}
```

Now modify your broadcast receiver's `https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)`
method to call `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.PeerListListener)` when an intent with the action `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_PEERS_CHANGED_ACTION` is received. You
need to pass this listener into the receiver somehow. One way is to send it
as an argument to the broadcast receiver's constructor.

### Kotlin

```kotlin
fun onReceive(context: Context, intent: Intent) {
    when (intent.action) {
        ...
        WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION -> {

            // Request available peers from the wifi p2p manager. This is an
            // asynchronous call and the calling activity is notified with a
            // callback on PeerListListener.onPeersAvailable()
            mManager?.requestPeers(channel, peerListListener)
            Log.d(TAG, "P2P peers changed")


        }
        ...
    }
}
```

### Java

```java
public void onReceive(Context context, Intent intent) {
    ...
    else if (WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION.equals(action)) {

        // Request available peers from the wifi p2p manager. This is an
        // asynchronous call and the calling activity is notified with a
        // callback on PeerListListener.onPeersAvailable()
        if (mManager != null) {
            mManager.requestPeers(channel, peerListListener);
        }
        Log.d(WiFiDirectActivity.TAG, "P2P peers changed");
    }...
}
```

Now, an intent with the action `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_PEERS_CHANGED_ACTION` intent
triggers a request for an updated peer list.

## Connect to a peer

In order to connect to a peer, create a new `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pConfig` object, and copy data into it from the
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pDevice` representing the device you want to
connect to. Then call the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pConfig, android.net.wifi.p2p.WifiP2pManager.ActionListener)`
method.

### Kotlin

```kotlin
override fun connect() {
    // Picking the first device found on the network.
    val device = peers[0]

    val config = WifiP2pConfig().apply {
        deviceAddress = device.deviceAddress
        wps.setup = WpsInfo.PBC
    }

    manager.connect(channel, config, object : WifiP2pManager.ActionListener {

        override fun onSuccess() {
            // WiFiDirectBroadcastReceiver notifies us. Ignore for now.
        }

        override fun onFailure(reason: Int) {
            Toast.makeText(
                    this@WiFiDirectActivity,
                    "Connect failed. Retry.",
                    Toast.LENGTH_SHORT
            ).show()
        }
    })
}
```

### Java

```java
@Override
public void connect() {
    // Picking the first device found on the network.
    WifiP2pDevice device = peers.get(0);

    WifiP2pConfig config = new WifiP2pConfig();
    config.deviceAddress = device.deviceAddress;
    config.wps.setup = WpsInfo.PBC;

    manager.connect(channel, config, new ActionListener() {

        @Override
        public void onSuccess() {
            // WiFiDirectBroadcastReceiver notifies us. Ignore for now.
        }

        @Override
        public void onFailure(int reason) {
            Toast.makeText(WiFiDirectActivity.this, "Connect failed. Retry.",
                    Toast.LENGTH_SHORT).show();
        }
    });
}
```

If each of the devices in your group supports Wi-Fi direct, you don't need
to explicitly ask for the group's password when connecting. To allow a device
that doesn't support Wi-Fi Direct to join a group, however, you need to
retrieve this password by calling
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestGroupInfo(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.GroupInfoListener)`, as
shown in the following code snippet:

### Kotlin

```kotlin
manager.requestGroupInfo(channel) { group ->
    val groupPassword = group.passphrase
}
```

### Java

```java
manager.requestGroupInfo(channel, new GroupInfoListener() {
  @Override
  public void onGroupInfoAvailable(WifiP2pGroup group) {
      String groupPassword = group.getPassphrase();
  }
});
```

Note that the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener` implemented in
the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pConfig, android.net.wifi.p2p.WifiP2pManager.ActionListener)` method only notifies you when the *initiation*
succeeds or fails. To listen for *changes* in connection state, implement the
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ConnectionInfoListener` interface.
Its `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ConnectionInfoListener#onConnectionInfoAvailable(android.net.wifi.p2p.WifiP2pInfo)` callback notifies you when the state of the
connection changes. In cases where multiple devices are going to be connected to
a single device (like a game with three or more players, or a chat app), one device
is designated the "group owner". You can designate a particular device as
the network's group owner by following the steps in the
[Create a Group](https://developer.android.com/develop/connectivity/wifi/wifi-direct#create-group) section.

### Kotlin

```kotlin
private val connectionListener = WifiP2pManager.ConnectionInfoListener { info ->

    // String from WifiP2pInfo struct
    val groupOwnerAddress: String = info.groupOwnerAddress.hostAddress

    // After the group negotiation, we can determine the group owner
    // (server).
    if (info.groupFormed && info.isGroupOwner) {
        // Do whatever tasks are specific to the group owner.
        // One common case is creating a group owner thread and accepting
        // incoming connections.
    } else if (info.groupFormed) {
        // The other device acts as the peer (client). In this case,
        // you'll want to create a peer thread that connects
        // to the group owner.
    }
}
```

### Java

```java
@Override
public void onConnectionInfoAvailable(final WifiP2pInfo info) {

    // String from WifiP2pInfo struct
    String groupOwnerAddress = info.groupOwnerAddress.getHostAddress();

    // After the group negotiation, we can determine the group owner
    // (server).
    if (info.groupFormed && info.isGroupOwner) {
        // Do whatever tasks are specific to the group owner.
        // One common case is creating a group owner thread and accepting
        // incoming connections.
    } else if (info.groupFormed) {
        // The other device acts as the peer (client). In this case,
        // you'll want to create a peer thread that connects
        // to the group owner.
    }
}
```

Now go back to the `https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)` method of the broadcast receiver, and modify the section
that listens for a `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#WIFI_P2P_CONNECTION_CHANGED_ACTION` intent.
When this intent is received, call `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestConnectionInfo(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.ConnectionInfoListener)`. This is an asynchronous call,
so results are received by the connection info listener you provide as a
parameter.

### Kotlin

```kotlin
when (intent.action) {
    ...
    WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION -> {

        // Connection state changed! We should probably do something about
        // that.

        mManager?.let { manager ->

            val networkInfo: NetworkInfo? = intent
                    .getParcelableExtra(WifiP2pManager.EXTRA_NETWORK_INFO) as NetworkInfo

            if (networkInfo?.isConnected == true) {

                // We are connected with the other device, request connection
                // info to find group owner IP

                manager.requestConnectionInfo(channel, connectionListener)
            }
        }
    }
    ...
}
```

### Java

```java
    ...
    } else if (WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION.equals(action)) {

        if (manager == null) {
            return;
        }

        NetworkInfo networkInfo = (NetworkInfo) intent
                .getParcelableExtra(WifiP2pManager.EXTRA_NETWORK_INFO);

        if (networkInfo.isConnected()) {

            // We are connected with the other device, request connection
            // info to find group owner IP

            manager.requestConnectionInfo(channel, connectionListener);
        }
        ...
```

## Create a group

If you want the device running your app to serve as the group owner for a
network that includes legacy devices---that is, devices that don't support
Wi-Fi Direct---you follow the same sequence of steps as in the
[Connect to a Peer](https://developer.android.com/develop/connectivity/wifi/wifi-direct#connect) section, except you create a new
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener`
using `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#createGroup(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.ActionListener)` instead of `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pConfig, android.net.wifi.p2p.WifiP2pManager.ActionListener)`. The callback handling within the
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener`
is the same, as shown in the following code snippet:

### Kotlin

```kotlin
manager.createGroup(channel, object : WifiP2pManager.ActionListener {
    override fun onSuccess() {
        // Device is ready to accept incoming connections from peers.
    }

    override fun onFailure(reason: Int) {
        Toast.makeText(
                this@WiFiDirectActivity,
                "P2P group creation failed. Retry.",
                Toast.LENGTH_SHORT
        ).show()
    }
})
```

### Java

```java
manager.createGroup(channel, new WifiP2pManager.ActionListener() {
    @Override
    public void onSuccess() {
        // Device is ready to accept incoming connections from peers.
    }

    @Override
    public void onFailure(int reason) {
        Toast.makeText(WiFiDirectActivity.this, "P2P group creation failed. Retry.",
                Toast.LENGTH_SHORT).show();
    }
});
```

**Note:** If all the devices in a network support Wi-Fi
Direct, you can use the `https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#connect(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pConfig, android.net.wifi.p2p.WifiP2pManager.ActionListener)` method on each device because the
method then creates the group and selects a group owner automatically.

After you create a group, you can call
`https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestGroupInfo(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.GroupInfoListener)` to retrieve details about the peers on
the network, including device names and connection statuses.