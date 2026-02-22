---
title: https://developer.android.com/training/monitoring-device-state/connectivity-status-type
url: https://developer.android.com/training/monitoring-device-state/connectivity-status-type
source: md.txt
---

The [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) provides
an API that enables you to request that the device connect to a network based on
various conditions that include device capabilities and data transport options.

The callback implementation provides information to your app about the device's
connection status as well as the capabilities of the currently connected
network. The API enables you to determine whether the device is currently
connected to a network that satisfies your app's requirements.

## Configure a network request

To specify the transport type of the network, such as Wi-Fi or cellular
connection, and the currently connected network's capabilities, such as internet
connection, you must configure a network request.

Declare a [`NetworkRequest`](https://developer.android.com/reference/android/net/NetworkRequest) that
describes your app's network connection needs. The following code creates a
request for a network that is connected to the internet and uses a Wi-Fi,
ethernet, or cellular connection for the transport type.  

### Kotlin

```kotlin
val networkRequest = NetworkRequest.Builder()
        .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
        .addTransportType(NetworkCapabilities.TRANSPORT_ETHERNET)
        .addTransportType(NetworkCapabilities.TRANSPORT_WIFI)
        .addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
        .build()
```

### Java

```java
NetworkRequest networkRequest = new NetworkRequest.Builder()
        .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
        .addTransportType(NetworkCapabilities.TRANSPORT_ETHERNET)
        .addTransportType(NetworkCapabilities.TRANSPORT_WIFI)
        .addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
        .build();
```

Note that some connections can be significantly more expensive than others (for
example, a mobile connection is typically expensive). Use
[`NetworkCapabilities#NET_CAPABILITY_NOT_METERED`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_NOT_METERED)
to determine whether the connection is expensive. When on a metered connection,
try to reduce your app's data consumption, or delay it until the device has a
non-metered connection.

## Configure a network callback

When you register the `NetworkRequest` with the `ConnectivityManager`, you must
implement a
[`NetworkCallback`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)
to receive notifications about changes in the connection status and network
capabilities.

The most commonly implemented functions in the `NetworkCallback` include the
following:

- [`onAvailable()`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onAvailable(android.net.Network)) indicates that the device is connected to a new network that satisfies the capabilities and transport type requirements specified in the `NetworkRequest`.
- [`onLost()`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onLost(android.net.Network)) indicates that the device has lost connection to the network.
- [`onCapabilitiesChanged()`](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback#onCapabilitiesChanged(android.net.Network,%20android.net.NetworkCapabilities)) indicates that the capabilities of the network have changed. The [`NetworkCapabilities`](https://developer.android.com/reference/android/net/NetworkCapabilities) object provides information about the current capabilities of the network.

### Kotlin

```kotlin
private val networkCallback = object : ConnectivityManager.NetworkCallback() {
    // network is available for use
    override fun onAvailable(network: Network) {
        super.onAvailable(network)
    }

    // Network capabilities have changed for the network
    override fun onCapabilitiesChanged(
            network: Network,
            networkCapabilities: NetworkCapabilities
    ) {
        super.onCapabilitiesChanged(network, networkCapabilities)
        val unmetered = networkCapabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED)
    }

    // lost network connection
    override fun onLost(network: Network) {
        super.onLost(network)
    }
}
```

### Java

```java
private ConnectivityManager.NetworkCallback networkCallback = new ConnectivityManager.NetworkCallback() {
    @Override
    public void onAvailable(@NonNull Network network) {
        super.onAvailable(network);
    }

    @Override
    public void onLost(@NonNull Network network) {
        super.onLost(network);
    }

    @Override
    public void onCapabilitiesChanged(@NonNull Network network, @NonNull NetworkCapabilities networkCapabilities) {
        super.onCapabilitiesChanged(network, networkCapabilities);
        final boolean unmetered = networkCapabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED);
    }
};
```

## Register for network updates

After you declare the `NetworkRequest` and `NetworkCallback`, use the
[`requestNetwork()`](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
or [`registerNetworkCallback()`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
functions to search for a network to connect from the device that satisfies the
`NetworkRequest`. The status is then reported to the `NetworkCallback`.  

### Kotlin

```kotlin
val connectivityManager = getSystemService(ConnectivityManager::class.java) as ConnectivityManager
connectivityManager.requestNetwork(networkRequest, networkCallback)
```

### Java

```java
ConnectivityManager connectivityManager =
        (ConnectivityManager) getSystemService(ConnectivityManager.class);
connectivityManager.requestNetwork(networkRequest, networkCallback);
```