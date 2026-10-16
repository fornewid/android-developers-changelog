---
title: https://developer.android.com/develop/connectivity/minimize-effect-regular-updates
url: https://developer.android.com/develop/connectivity/minimize-effect-regular-updates
source: md.txt
---

Requests that your app makes to the network are a major cause of battery drain
because they turn on power-consuming cellular or Wi-Fi radios. Beyond the power
needed to send and receive packets, these radios expend extra power just
turning on and keeping awake. Something as simple as a network request every 15
seconds can keep the mobile radio on continuously and quickly use up battery
power.

There are three general types of regular updates:

- **User-initiated.** Performing an update based on some user behavior, such as a pull-to-refresh gesture.
- **App-initiated.** Performing an update on a recurring basis.
- **Server-initiated.** Performing an update in response to a notification from a server.

This topic looks at each of these and discusses additional ways they can be
optimized to reduce battery drain.

## Optimize user-initiated requests

User-initiated requests typically occur in response to some user behavior. For
example, an app used to read the latest news articles may allow the user to
perform a pull-to-refresh gesture to check for new articles. You can use the
following techniques to respond to user-initiated requests while optimizing
network use.

### Throttle user requests

You may want to disregard some user-initiated requests if there is no need for
them, such as multiple pull-to-refresh gestures over a short period of time to
check for new data while the current data is still fresh. Acting on each
request could waste a significant amount of power by keeping the radio awake. A
more efficient approach is to throttle the user-initiated requests so that
only one request can be made over a period of time, reducing how often the
radio is used.

### Use a cache

By caching your app's data, you're creating a local copy of the information
that your app needs to reference. Your app can then access the same local
copy of the information multiple times without having to open a network
connection to make new requests.

You should cache data as aggressively as possible, including static
resources and on-demand downloads such as full-size images. You can use HTTP
cache headers to ensure that your caching strategy doesn't result in your app
displaying stale data. For more information on caching network responses, see
[Avoid redundant
downloads](https://developer.android.com/training/efficient-downloads/redundant_redundant#LocalCache).

On Android 11 and higher, your app can use the same large datasets that other
apps use for use cases such as machine learning and media playback. When your
app needs to access a shared dataset, it can first check for a cached version
before attempting to download a new copy. To learn more about shared datasets,
see [Access shared datasets](https://developer.android.com/preview/features/shared-datasets).

### Use greater bandwidth to download more data less often

When connected over a wireless radio, higher bandwidth generally comes at the
price of higher battery cost, meaning that 5G typically consumes more energy
than LTE, which is in turn more expensive than 3G.

This means that while the underlying radio state varies based on the
radio technology, generally speaking the relative battery impact of the state
change tail-time is greater for higher bandwidth radios. For more information on
tail-time, see [The radio state
machine](https://developer.android.com/develop/connectivity/network-ops/network-access-optimization#radio-state).

At the same time, the higher bandwidth means you can prefetch more
aggressively, downloading more data over the same time. Perhaps less
intuitively, because the tail-time battery cost is relatively higher, it's also
more efficient to keep the radio active for longer periods during each transfer
session to reduce the frequency of updates.

For example, if an LTE radio has double the bandwidth and double the energy cost
of 3G, you should download four times as much data during each session---or
potentially as much as 10MB. When downloading this much data, it's important to
consider the effect of your prefetching on the available local storage and flush
your prefetch cache regularly.

You can use the
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) to register
a listener for the default network, and the
[`TelephonyManager`](https://developer.android.com/reference/android/telephony/TelephonyManager) to register
a [`PhoneStateListener`](https://developer.android.com/reference/android/telephony/PhoneStateListener) to
determine the current device connection type. Once the connection type is known,
you can modify your prefetching routines accordingly:

### Kotlin

```kotlin
val cm = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
val tm = getSystemService(Context.TELEPHONY_SERVICE) as TelephonyManager

private var hasWifi = false
private var hasCellular = false
private var cellModifier: Float = 1f

private val networkCallback = object : ConnectivityManager.NetworkCallback() {
    // Network capabilities have changed for the network
    override fun onCapabilitiesChanged(
            network: Network,
            networkCapabilities: NetworkCapabilities
    ) {
        super.onCapabilitiesChanged(network, networkCapabilities)
        hasCellular = networkCapabilities
    .hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR)
        hasWifi = networkCapabilities
    .hasTransport(NetworkCapabilities.TRANSPORT_WIFI)
    }
}

private val phoneStateListener = object : PhoneStateListener() {
override fun onPreciseDataConnectionStateChanged(
    dataConnectionState: PreciseDataConnectionState
) {
  cellModifier = when (dataConnectionState.networkType) {
      TelephonyManager.NETWORK_TYPE_LTE or TelephonyManager.NETWORK_TYPE_HSPAP -> 4f
      TelephonyManager.NETWORK_TYPE_EDGE or TelephonyManager.NETWORK_TYPE_GPRS -> 1/2f
      else -> 1f

  }
}

private class NetworkState {
    private var defaultNetwork: Network? = null
    private var defaultCapabilities: NetworkCapabilities? = null
    fun setDefaultNetwork(network: Network?, caps: NetworkCapabilities?) = synchronized(this) {
        defaultNetwork = network
        defaultCapabilities = caps
    }
    val isDefaultNetworkWifi
        get() = synchronized(this) {
            defaultCapabilities?.hasTransport(TRANSPORT_WIFI) ?: false
        }
    val isDefaultNetworkCellular
        get() = synchronized(this) {
            defaultCapabilities?.hasTransport(TRANSPORT_CELLULAR) ?: false
        }
    val isDefaultNetworkUnmetered
        get() = synchronized(this) {
            defaultCapabilities?.hasCapability(NET_CAPABILITY_NOT_METERED) ?: false
        }
    var cellNetworkType: Int = TelephonyManager.NETWORK_TYPE_UNKNOWN
        get() = synchronized(this) { field }
        set(t) = synchronized(this) { field = t }
    private val cellModifier: Float
        get() = synchronized(this) {
            when (cellNetworkType) {
                TelephonyManager.NETWORK_TYPE_LTE or TelephonyManager.NETWORK_TYPE_HSPAP -> 4f
                TelephonyManager.NETWORK_TYPE_EDGE or TelephonyManager.NETWORK_TYPE_GPRS -> 1 / 2f
                else -> 1f
            }
        }
    val prefetchCacheSize: Int
        get() = when {
            isDefaultNetworkWifi -> MAX_PREFETCH_CACHE
            isDefaultNetworkCellular -> (DEFAULT_PREFETCH_CACHE * cellModifier).toInt()
            else -> DEFAULT_PREFETCH_CACHE
        }
}
private val networkState = NetworkState()
private val networkCallback = object : ConnectivityManager.NetworkCallback() {
    // Network capabilities have changed for the network
    override fun onCapabilitiesChanged(
            network: Network,
            networkCapabilities: NetworkCapabilities
    ) {
        networkState.setDefaultNetwork(network, networkCapabilities)
    }

    override fun onLost(network: Network?) {
        networkState.setDefaultNetwork(null, null)
    }
}

private val telephonyCallback = object : TelephonyCallback(), TelephonyCallback.PreciseDataConnectionStateListener {
    override fun onPreciseDataConnectionStateChanged(dataConnectionState: PreciseDataConnectionState) {
        networkState.cellNetworkType = dataConnectionState.networkType
    }
}

connectivityManager.registerDefaultNetworkCallback(networkCallback)
telephonyManager.registerTelephonyCallback(telephonyCallback)


private val prefetchCacheSize: Int
get() {
    return when {
        hasWifi -> MAX_PREFETCH_CACHE
        hasCellular -> (DEFAULT_PREFETCH_CACHE * cellModifier).toInt()
        else -> DEFAULT_PREFETCH_CACHE
    }
}

}
```

### Java

```java
ConnectivityManager cm =
 (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
TelephonyManager tm =
  (TelephonyManager) getSystemService(Context.TELEPHONY_SERVICE);

private boolean hasWifi = false;
private boolean hasCellular = false;
private float cellModifier = 1f;

private ConnectivityManager.NetworkCallback networkCallback = new ConnectivityManager.NetworkCallback() {
@Override
public void onCapabilitiesChanged(
    @NonNull Network network,
    @NonNull NetworkCapabilities networkCapabilities
) {
        super.onCapabilitiesChanged(network, networkCapabilities);
        hasCellular = networkCapabilities
    .hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR);
        hasWifi = networkCapabilities
    .hasTransport(NetworkCapabilities.TRANSPORT_WIFI);
}
};

private PhoneStateListener phoneStateListener = new PhoneStateListener() {
@Override
public void onPreciseDataConnectionStateChanged(
    @NonNull PreciseDataConnectionState dataConnectionState
    ) {
    switch (dataConnectionState.getNetworkType()) {
        case (TelephonyManager.NETWORK_TYPE_LTE |
            TelephonyManager.NETWORK_TYPE_HSPAP):
            cellModifier = 4;
            Break;
        case (TelephonyManager.NETWORK_TYPE_EDGE |
            TelephonyManager.NETWORK_TYPE_GPRS):
            cellModifier = 1/2.0f;
            Break;
        default:
            cellModifier = 1;
            Break;
    }
}
};

cm.registerDefaultNetworkCallback(networkCallback);
tm.listen(
phoneStateListener,
PhoneStateListener.LISTEN_PRECISE_DATA_CONNECTION_STATE
);

public int getPrefetchCacheSize() {
if (hasWifi) {
    return MAX_PREFETCH_SIZE;
}
if (hasCellular) {
    return (int) (DEFAULT_PREFETCH_SIZE * cellModifier);
    }
return DEFAULT_PREFETCH_SIZE;
}
```

## Optimize app-initiated requests

App-initiated requests typically occur on a schedule, such as an app that sends
logs or analytics to a backend service. When dealing with app-initiated
requests, consider the priority of those requests, whether they can be batched
together, and whether they can be deferred until the device is charging or
connected to an unmetered network. These requests can be optimized with careful
scheduling and by using libraries such as
[WorkManager](https://developer.android.com/jetpack/androidx/releases/work).

### Batch network requests

On a mobile device, the process of turning on the radio, making a connection,
and keeping the radio awake uses a large amount of power. For this reason,
processing individual requests at random times can consume significant power
and reduce battery life. A more efficient approach is to queue a set of network
requests and process them together. This allows the system to pay the power
cost of turning on the radio just once, and still get all the data requested by
an app.

### Use WorkManager

You can use the `WorkManager` library to perform work on an efficient schedule
that considers whether specific conditions are met, such as network availability
and power status. For example, suppose you have a
[`Worker`](https://developer.android.com/reference/androidx/work/Worker) subclass called
`DownloadHeadlinesWorker` that retrieves the latest news headlines. This worker
can be scheduled to run every hour, provided the device is connected to an
unmetered network and device's battery isn't low, with a custom retry strategy
if there are any problems retrieving the data, as shown below:

### Kotlin

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.UNMETERED)
    .setRequiresBatteryNotLow(true)
    .build()
val request =
    PeriodicWorkRequestBuilder<DownloadHeadlinesWorker>(1, TimeUnit.HOURS)
        .setConstraints(constraints)
        .setBackoffCriteria(BackoffPolicy.LINEAR, 1L, TimeUnit.MINUTES)
        .build()
WorkManager.getInstance(context).enqueue(request)
```

### Java

```java
Constraints constraints = new Constraints.Builder()
        .setRequiredNetworkType(NetworkType.UNMETERED)
        .setRequiresBatteryNotLow(true)
        .build();
WorkRequest request = new PeriodicWorkRequest.Builder(DownloadHeadlinesWorker.class, 1, TimeUnit.HOURS)
        .setBackoffCriteria(BackoffPolicy.LINEAR, 1L, TimeUnit.MINUTES)
        .build();
WorkManager.getInstance(this).enqueue(request);
```

In addition to WorkManager, the Android platform provides several other tools
to help you create an efficient schedule for completing networking tasks, such
as polling. To learn more about using these tools, see the
[Guide to background processing](https://developer.android.com/guide/background).

## Optimize server-initiated requests

Server-initiated requests typically occur in response to a notification from a
server. For example, an app used to read the latest news articles may receive
a notification about a new batch of articles that fit the user's
personalization preferences, which it then downloads.

### Send server updates with Firebase Cloud Messaging

[Firebase Cloud Messaging
(FCM)](https://firebase.google.com/docs/cloud-messaging/) is a lightweight
mechanism used to transmit data from a server to a particular app instance.
Using FCM, your server can notify your app running on a particular device that
there is new data available for it.

Compared to polling, where your app must regularly ping the server to query for
new data, this event-driven model allows your app to create a new connection
only when it knows there is data to download. The model minimizes unnecessary
connections and reduces latency when updating information within your app.

FCM is implemented using a persistent TCP/IP connection. This minimizes the
number of persistent connections and allows the platform to optimize bandwidth
and minimize the associated impact on battery life.