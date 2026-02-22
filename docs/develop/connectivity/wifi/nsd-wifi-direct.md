---
title: https://developer.android.com/develop/connectivity/wifi/nsd-wifi-direct
url: https://developer.android.com/develop/connectivity/wifi/nsd-wifi-direct
source: md.txt
---

The first lesson in this class, [Using Network Service
Discovery](https://developer.android.com/develop/connectivity/wifi/use-nsd), showed you
how to discover services that are connected to a local network. However, using
Wi-Fi Direct (P2P) Service Discovery allows you to discover the services of nearby devices
directly, without being connected to a network. You can also advertise the services
running on your device. These capabilities help you communicate between apps,
even when no local network or hotspot is available.

While this set of APIs is similar in purpose to the Network Service Discovery
APIs outlined in a previous lesson, implementing them in code is very different.
This lesson shows you how to discover services available from other devices,
using Wi-Fi Direct. The lesson assumes that you're already familiar with the
[Wi-Fi Direct](https://developer.android.com/guide/topics/connectivity/wifip2p) API.

## Set up the manifest

In order to use Wi-Fi P2P, add the [CHANGE_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE), [ACCESS_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE),
[ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION),
and [INTERNET](https://developer.android.com/reference/android/Manifest.permission#INTERNET)
permissions to your manifest. If your app targets Android 13 (API level 33) or higher, also add the
[NEARBY_WIFI_DEVICES](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES),
permission to your manifest. Even though Wi-Fi Direct doesn't require an
Internet connection, it uses standard Java sockets, and using these in Android
requires the requested permissions.  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.nsdchat"
    ...

    <uses-permission
        android:required="true"
        android:name="android.permission.ACCESS_WIFI_STATE"/>
    <uses-permission
        android:required="true"
        android:name="android.permission.CHANGE_WIFI_STATE"/>
    <uses-permission
        android:required="true"
        android:name="android.permission.INTERNET"/>
    <!-- If your app targets Android 13 (API level 33)
         or higher, you must declare the NEARBY_WIFI_DEVICES permission. -->
    <uses-permission
        android:name="android.permission.NEARBY_WIFI_DEVICES"
        <!-- If your app derives location information from Wi-Fi APIs,
             don't include the "usesPermissionFlags" attribute. -->
        android:usesPermissionFlags="neverForLocation" />
    <uses-permission
        android:required="true"
        android:name="android.permission.ACCESS_FINE_LOCATION"
        <!-- If any feature in your app relies on precise location information,
             don't include the "maxSdkVersion" attribute. -->
        android:maxSdkVersion="32" />
    ...
```


Besides the preceding permissions, the following APIs also require Location Mode to be enabled:

- [discoverPeers](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%20android.net.wifi.p2p.WifiP2pManager.ActionListener))
- [discoverServices](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverServices(android.net.wifi.p2p.WifiP2pManager.Channel,%2520android.net.wifi.p2p.WifiP2pManager.ActionListener))
- [requestPeers](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#requestPeers(android.net.wifi.p2p.WifiP2pManager.Channel,%2520android.net.wifi.p2p.WifiP2pManager.PeerListListener))

<br />

## Add a local service

If you're providing a local service, you need to register it for
service discovery. Once your local service is registered, the framework
automatically responds to service discovery requests from peers.

To create a local service:

1. Create a [WifiP2pServiceInfo](https://developer.android.com/reference/android/net/wifi/p2p/nsd/WifiP2pServiceInfo) object.
2. Populate it with information about your service.
3. Call [addLocalService()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#addLocalService(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.nsd.WifiP2pServiceInfo, android.net.wifi.p2p.WifiP2pManager.ActionListener)) to register the local service for service discovery.

### Kotlin

```kotlin
    private fun startRegistration() {
        //  Create a string map containing information about your service.
        val record: Map<String, String> = mapOf(
                "listenport" to SERVER_PORT.toString(),
                "buddyname" to "John Doe${(Math.random() * 1000).toInt()}",
                "available" to "visible"
        )

        // Service information.  Pass it an instance name, service type
        // _protocol._transportlayer , and the map containing
        // information other devices will want once they connect to this one.
        val serviceInfo =
                WifiP2pDnsSdServiceInfo.newInstance("_test", "_presence._tcp", record)

        // Add the local service, sending the service info, network channel,
        // and listener that will be used to indicate success or failure of
        // the request.
        manager.addLocalService(channel, serviceInfo, object : WifiP2pManager.ActionListener {
            override fun onSuccess() {
                // Command successful! Code isn't necessarily needed here,
                // Unless you want to update the UI or add logging statements.
            }

            override fun onFailure(arg0: Int) {
                // Command failed.  Check for P2P_UNSUPPORTED, ERROR, or BUSY
            }
        })
    }
```

### Java

```java
    private void startRegistration() {
        //  Create a string map containing information about your service.
        Map record = new HashMap();
        record.put("listenport", String.valueOf(SERVER_PORT));
        record.put("buddyname", "John Doe" + (int) (Math.random() * 1000));
        record.put("available", "visible");

        // Service information.  Pass it an instance name, service type
        // _protocol._transportlayer , and the map containing
        // information other devices will want once they connect to this one.
        WifiP2pDnsSdServiceInfo serviceInfo =
                WifiP2pDnsSdServiceInfo.newInstance("_test", "_presence._tcp", record);

        // Add the local service, sending the service info, network channel,
        // and listener that will be used to indicate success or failure of
        // the request.
        manager.addLocalService(channel, serviceInfo, new ActionListener() {
            @Override
            public void onSuccess() {
                // Command successful! Code isn't necessarily needed here,
                // Unless you want to update the UI or add logging statements.
            }

            @Override
            public void onFailure(int arg0) {
                // Command failed.  Check for P2P_UNSUPPORTED, ERROR, or BUSY
            }
        });
    }
```

## Discover nearby services

Android uses callback methods to notify your application of available services, so
the first thing to do is set those up. Create a [WifiP2pManager.DnsSdTxtRecordListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.DnsSdTxtRecordListener) to listen for
incoming records. This record can optionally be broadcast by other
devices. When one comes in, copy the device address and any other
relevant information you want into a data structure external to the current
method, so you can access it later. The following example assumes that the
record contains a "buddyname" field, populated with the user's identity.  

### Kotlin

```kotlin
private val buddies = mutableMapOf<String, String>()
...
private fun discoverService() {
    /* Callback includes:
     * fullDomain: full domain name: e.g. "printer._ipp._tcp.local."
     * record: TXT record dta as a map of key/value pairs.
     * device: The device running the advertised service.
     */
    val txtListener = DnsSdTxtRecordListener { fullDomain, record, device ->
        Log.d(TAG, "DnsSdTxtRecord available -$record")
        record["buddyname"]?.also {
            buddies[device.deviceAddress] = it
        }
    }
}
```

### Java

```java
final HashMap<String, String> buddies = new HashMap<String, String>();
...
private void discoverService() {
    DnsSdTxtRecordListener txtListener = new DnsSdTxtRecordListener() {
        @Override
        /* Callback includes:
         * fullDomain: full domain name: e.g. "printer._ipp._tcp.local."
         * record: TXT record dta as a map of key/value pairs.
         * device: The device running the advertised service.
         */

        public void onDnsSdTxtRecordAvailable(
                String fullDomain, Map record, WifiP2pDevice device) {
                Log.d(TAG, "DnsSdTxtRecord available -" + record.toString());
                buddies.put(device.deviceAddress, record.get("buddyname"));
            }
        };
}
```

To get the service information, create a [WifiP2pManager.DnsSdServiceResponseListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.DnsSdServiceResponseListener). This
receives the actual description and connection information. The previous code
snippet implemented a [Map](https://developer.android.com/reference/java/util/Map) object to pair a device address with the buddy
name. The service response listener uses this to link the DNS record with the
corresponding service information. Once both
listeners are implemented, add them to the [WifiP2pManager](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager) using the [setDnsSdResponseListeners()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#setDnsSdResponseListeners(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.DnsSdServiceResponseListener, android.net.wifi.p2p.WifiP2pManager.DnsSdTxtRecordListener)) method.  

### Kotlin

```kotlin
private fun discoverService() {
    ...

    val servListener = DnsSdServiceResponseListener { instanceName, registrationType, resourceType ->
        // Update the device name with the human-friendly version from
        // the DnsTxtRecord, assuming one arrived.
        resourceType.deviceName = buddies[resourceType.deviceAddress] ?: resourceType.deviceName

        // Add to the custom adapter defined specifically for showing
        // wifi devices.
        val fragment = fragmentManager
                .findFragmentById(R.id.frag_peerlist) as WiFiDirectServicesList
        (fragment.listAdapter as WiFiDevicesAdapter).apply {
            add(resourceType)
            notifyDataSetChanged()
        }

        Log.d(TAG, "onBonjourServiceAvailable $instanceName")
    }

    manager.setDnsSdResponseListeners(channel, servListener, txtListener)
    ...
}
```

### Java

```java
private void discoverService() {
...

    DnsSdServiceResponseListener servListener = new DnsSdServiceResponseListener() {
        @Override
        public void onDnsSdServiceAvailable(String instanceName, String registrationType,
                WifiP2pDevice resourceType) {

                // Update the device name with the human-friendly version from
                // the DnsTxtRecord, assuming one arrived.
                resourceType.deviceName = buddies
                        .containsKey(resourceType.deviceAddress) ? buddies
                        .get(resourceType.deviceAddress) : resourceType.deviceName;

                // Add to the custom adapter defined specifically for showing
                // wifi devices.
                WiFiDirectServicesList fragment = (WiFiDirectServicesList) getFragmentManager()
                        .findFragmentById(R.id.frag_peerlist);
                WiFiDevicesAdapter adapter = ((WiFiDevicesAdapter) fragment
                        .getListAdapter());

                adapter.add(resourceType);
                adapter.notifyDataSetChanged();
                Log.d(TAG, "onBonjourServiceAvailable " + instanceName);
        }
    };

    manager.setDnsSdResponseListeners(channel, servListener, txtListener);
    ...
}
```

Now create a service request and call [addServiceRequest()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#addServiceRequest(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.nsd.WifiP2pServiceRequest, android.net.wifi.p2p.WifiP2pManager.ActionListener)).
This method also takes a listener to report success or failure.  

### Kotlin

```kotlin
        serviceRequest = WifiP2pDnsSdServiceRequest.newInstance()
        manager.addServiceRequest(
                channel,
                serviceRequest,
                object : WifiP2pManager.ActionListener {
                    override fun onSuccess() {
                        // Success!
                    }

                    override fun onFailure(code: Int) {
                        // Command failed.  Check for P2P_UNSUPPORTED, ERROR, or BUSY
                    }
                }
        )
```

### Java

```java
        serviceRequest = WifiP2pDnsSdServiceRequest.newInstance();
        manager.addServiceRequest(channel,
                serviceRequest,
                new ActionListener() {
                    @Override
                    public void onSuccess() {
                        // Success!
                    }

                    @Override
                    public void onFailure(int code) {
                        // Command failed.  Check for P2P_UNSUPPORTED, ERROR, or BUSY
                    }
                });
```

Finally, make the call to [discoverServices()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#discoverServices(android.net.wifi.p2p.WifiP2pManager.Channel, android.net.wifi.p2p.WifiP2pManager.ActionListener)).  

### Kotlin

```kotlin
        manager.discoverServices(
                channel,
                object : WifiP2pManager.ActionListener {
                    override fun onSuccess() {
                        // Success!
                    }

                    override fun onFailure(code: Int) {
                        // Command failed. Check for P2P_UNSUPPORTED, ERROR, or BUSY
                        when (code) {
                            WifiP2pManager.P2P_UNSUPPORTED -> {
                                Log.d(TAG, "Wi-Fi Direct isn't supported on this device.")
                            }
                        }
                    }
                }
        )
```

### Java

```java
        manager.discoverServices(channel, new ActionListener() {

            @Override
            public void onSuccess() {
                // Success!
            }

            @Override
            public void onFailure(int code) {
                // Command failed.  Check for P2P_UNSUPPORTED, ERROR, or BUSY
                if (code == WifiP2pManager.P2P_UNSUPPORTED) {
                    Log.d(TAG, "Wi-Fi Direct isn't supported on this device.");
                else if(...)
                    ...
            }
        });
```

If all goes well, hooray, you're done! If you encounter problems, remember
that the asynchronous calls you've made take an
[WifiP2pManager.ActionListener](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener) as an argument, and
this provides you with callbacks indicating success or failure. To diagnose
problems, put debugging code in [onFailure()](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager.ActionListener#onFailure(int)). The error code
provided by the method hints at the problem. Here are the possible error values
and what they mean

[P2P_UNSUPPORTED](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#P2P_UNSUPPORTED)
:   Wi-Fi Direct isn't supported on the device running the app.

[BUSY](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#BUSY)
:   The system is too busy to process the request.

[ERROR](https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager#ERROR)
:   The operation failed due to an internal error.