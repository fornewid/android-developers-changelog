---
title: https://developer.android.com/training/wearables/data/events
url: https://developer.android.com/training/wearables/data/events
source: md.txt
---

When you make a call to the Data Layer API, you can receive the status of the
call when it completes. You also can listen for data events resulting from data
changes that your app makes anywhere on the Wear OS by Google network.

> [!NOTE]
> **Note:** The Data Layer API can only send messages and synchronize data with Android phones or Wear OS watches. If a Wear OS device is paired with an iOS device, the Data Layer API doesn't work. For this reason, don't use the Data Layer API as the primary way to communicate with a network. Instead, follow the same pattern in your Wear OS app as in a mobile app, with some minor differences as described in [Network access and sync on Wear OS](https://developer.android.com/training/wearables/data-layer/network-access).

For an example of effectively working with the Data Layer API, see the [Android
DataLayer Sample](https://github.com/android/wear-os-samples/tree/main/DataLayer) app.

## Wait for the status of Data Layer calls

Calls to the Data Layer API---such as a call using the `putDataItem` method of the
[`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) class---sometimes return a [`Task<ResultType>`](https://developers.google.com/android/guides/tasks) object. As
soon as the `Task` object is created, the operation is queued in the background.
If you do nothing more after this, the operation eventually completes silently.

However, you usually want to do something with the result after the operation
completes, so the `Task` object lets you wait for the result status, either
asynchronously or synchronously.

### Asynchronous calls

If your code is running on the main UI thread, don't make blocking calls to the
Data Layer API and use a coroutine to call `putDataItem`:

<br />

```kotlin
private suspend fun Context.sendDataAsync(count: Int) {
    try {
        val putDataReq: PutDataRequest = PutDataMapRequest.create("/count").run {
            dataMap.putInt("count_key", count)
            asPutDataRequest()
        }
        val dataItem = Wearable.getDataClient(this).putDataItem(putDataReq).await()
        handleDataItem(dataItem)
    } catch (e: Exception) {
        handleDataItemError(e)
    } finally {
        handleTaskComplete()
    }
}

private fun handleDataItem(dataItem: DataItem) { }
private fun handleDataItemError(exception: Exception) { }
private fun handleTaskComplete() { }
```

<br />

See the [Task API](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) for other possibilities, including chaining the execution
of different tasks.

### Synchronous calls

If your code is running on a separate handler thread in a background service,
such as in a [`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService.html), use `runBlocking` to make a
blocking call to `putDataItem`.

**Note:** Do not call this while on the main thread.

<br />

```kotlin
private fun Context.sendDataSync(count: Int) = runBlocking {
    val putDataReq = PutDataMapRequest.create("/count").run {
        dataMap.putInt("count_key", count)
        asPutDataRequest()
    }

    try {
        val result = Wearable.getDataClient(this@sendDataSync)
            .putDataItem(putDataReq)
            .await()
        // Logic for success
    } catch (e: Exception) {
        // Handle failure
    }
}
```

<br />

## Listen for Data Layer events

Because the data layer synchronizes and sends data across the handheld and
wearable devices, you usually need to listen for important events like data
items being created and messages being received.

To listen for data layer events, you have two options:

- Create a service that extends [`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService.html).
- Create an activity or class that implements the [`DataClient.OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener) interface.

With both of these options, you override the data event callback methods for the
events you are interested in handling.

**Note:** Consider your app's battery usage when choosing a listener
implementation. A `WearableListenerService` is registered in the app's manifest
and can launch the app if it is not already running. If you only need to listen
for events when your app is already running, which is often the case with
interactive applications, then don't use a `WearableListenerService`. Instead,
register a live listener. For example, use the `addListener` method of the
[`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) class. This can reduce the load on the system and reduce
battery usage.

### Use a WearableListenerService

You typically create instances of [`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService.html) in both your
wearable and handheld apps. However, if you are not interested in data events in
one of the apps, then you don't need to implement the service in that app.

For example, you can have a handheld app that sets and gets data item objects
and a wearable app that listens for these updates to update its UI. The wearable
app never updates any of the data items, so the handheld app doesn't listen for
any data events from the wearable app.

Some of the events you can listen for using `WearableListenerService` are the
following:

- [`onDataChanged()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService#onDataChanged(com.google.android.gms.wearable.DataEventBuffer)): whenever a data item object is created, deleted, or changed, the system triggers this callback on all connected nodes.
- [`onMessageReceived()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService#onMessageReceived(com.google.android.gms.wearable.MessageEvent)): a message sent from a node triggers this callback on the target node.
- [`onCapabilityChanged()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService#onCapabilityChanged(com.google.android.gms.wearable.CapabilityInfo)): when a capability that an instance of your app advertises becomes available on the network, that event triggers this callback. If you're looking for a nearby node, you can query the [`isNearby()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Node.html#isNearby()) method of the nodes provided in the callback.

You can also listen for events from [`ChannelClient.ChannelCallback`](https://developers.google.com/android/reference/com/google/android/gms/wearable/ChannelClient.ChannelCallback), such
as `onChannelOpened()`.

All the preceding events are executed in a background thread, not on the main
thread.

To create a `WearableListenerService`, follow these steps:

1. Create a class that extends `WearableListenerService`.
2. Listen for the events that you're interested in, such as `onDataChanged()`.
3. Declare an intent filter in your Android manifest to notify the system about your `WearableListenerService`. This declaration lets the system bind your service as needed.

The following example shows how to implement a `WearableListenerService`:

<br />

```kotlin
class DataLayerListenerService : WearableListenerService() {

    override fun onDataChanged(dataEvents: DataEventBuffer) {
        if (Log.isLoggable(TAG, Log.DEBUG)) {
            Log.d(TAG, "onDataChanged: $dataEvents")
        }

        // Loop through the events and send a message
        // to the node that created the data item.
        dataEvents
            .map { it.dataItem.uri }
            .forEach { uri ->
                // Get the node ID from the host value of the URI.
                val nodeId: String = uri.host!!
                // Set the data of the message to be the bytes of the URI.
                val payload: ByteArray = uri.toString().toByteArray()

                // Send the RPC.
                Wearable.getMessageClient(this)
                    .sendMessage(
                        nodeId,
                        DATA_ITEM_RECEIVED_PATH,
                        payload
                    )
            }
    }
}
```

<br />

The following section explains how to use an intent filter with this listener.

#### Use filters with WearableListenerService

An intent filter for the `WearableListenerService` example shown in the previous
section might look like this:

<br />

```xml
<service
    android:name=".snippets.datalayer.DataLayerListenerService"
    android:exported="true"
    tools:ignore="ExportedService" >
    <intent-filter>
        <action android:name="com.google.android.gms.wearable.DATA_CHANGED" />
        <data
            android:scheme="wear"
            android:host="*"
            android:path="/start-activity" />
    </intent-filter>
</service>
```

<br />

The `DATA_CHANGED` action filter tells the system your app is interested in data
layer events.

In this example, the watch listens for the `/start-activity` data item, and the
phone listens for the `/data-item-received` (`DATA_ITEM_RECEIVED_PATH`) message
response.

Standard Android filter matching rules apply. You can specify multiple services
per manifest, multiple intent filters per service, multiple actions per filter,
and multiple data stanzas per filter. Filters can match on a wildcard host or on
a specific one. To match on a wildcard host, use `host="*"`. To match on a
specific host, specify `host=<node_id>`.

You can also match a literal path or path prefix. To do this, you must specify a
wildcard or specific host. Otherwise, the system ignores the path you specify.

For more information about the filter types that Wear OS supports, see the API
reference documentation for [`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService).

For more information on data filters and matching rules, see the API reference
documentation for the [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) manifest element.

When matching intent filters, remember two important rules:

- If no scheme is specified for the intent filter, the system ignores all the other URI attributes.
- If no host is specified for the filter, the system ignores all the path attributes.

### Use a live listener

If your app only cares about data-layer events when the user is interacting with
the app, it may not need a long-running service to handle every data change. In
such a case, you can listen for events in an activity.

To recommend a cleaner and safer approach, use a **Lifecycle Observer** . By
using a Lifecycle Observer, you move the registration logic out of the
Activity's [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) and into a separate, reusable class that
implements `DefaultLifecycleObserver`.

This approach keeps your Activity lean and prevents common bugs like forgetting
to unregister the listener.

#### 1. Create the lifecycle-aware listener

This class wraps the [`DataClient.OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener) and automatically
manages its own subscription based on the Activity's lifecycle.

<br />

```kotlin
class WearDataLayerObserver(
    private val dataClient: DataClient,
    private val onDataReceived: (DataEventBuffer) -> Unit
) : DefaultLifecycleObserver, DataClient.OnDataChangedListener {

    // Implementation of the DataClient listener
    override fun onDataChanged(dataEvents: DataEventBuffer) {
        onDataReceived(dataEvents)
    }

    // Automatically register when the Activity starts
    override fun onResume(owner: LifecycleOwner) {
        dataClient.addListener(this)
    }

    // Automatically unregister when the Activity pauses
    override fun onPause(owner: LifecycleOwner) {
        dataClient.removeListener(this)
    }
}
```

<br />

#### 2. Usage in your Activity

Now, your Activity doesn't need to override [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) or
[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) for the Wear API. You add the observer once in `onCreate()`.

<br />

```kotlin
class DataLayerLifecycleActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val dataClient = Wearable.getDataClient(this)

        // Create the observer and link it to the activity's lifecycle
        val wearObserver = WearDataLayerObserver(dataClient) { dataEvents ->
            handleDataEvents(dataEvents)
        }

        lifecycle.addObserver(wearObserver)
    }

    private fun handleDataEvents(dataEvents: DataEventBuffer) {
        // ... filter and process events ...
    }
}
```

<br />

#### Why this is better:

- **Cleaner Activity:** You remove boilerplate from the Activity lifecycle methods.
- **Safety:** `DefaultLifecycleObserver` helps verify that the listener is removed even if the Activity is destroyed unexpectedly, preventing memory leaks.
- **Reusability:** You can plug this `WearDataLayerObserver` into any Activity or Fragment without rewriting the registration logic.
- **Decoupling:** The logic for when to listen is separated from the logic of what to do with the data.

> [!TIP]
> **Tip:** If you are using a `ViewModel`, collect these events as a `Flow` using `callbackFlow` and then observe that `Flow` in the `Activity` using `repeatOnLifecycle`. This completely eliminates the need for the `Activity` to even know the `DataClient` exists.

> [!CAUTION]
> **Caution:** Before using the Wearable Data Layer API, check that it's available on a device; otherwise, an exception occurs. Use the [`GoogleApiAvailability`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability) class, as demonstrated in the [overview](https://developer.android.com/training/wearables/data/overview#client).

### Use filters with live listeners

As previously mentioned, just as you can specify intent filters for
manifest-based `WearableListenerService` objects, you can use intent filters
when registering a live listener through the [Wearable API](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable). The same rules
apply to both API-based live listeners and manifest-based listeners.

A common pattern is to [register a listener with a specific path or path prefix
using a `LifecycleObserver`](https://developer.android.com/training/wearables/data/events#use-live-listener). By implementing listeners in this fashion,
your app can more selectively receive events, improving its design and
efficiency.