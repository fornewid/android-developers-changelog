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
private fun Context.sendDataSync(count: Int) {
    // Create a data item with the path and data to be sent
    val putDataReq: PutDataRequest = PutDataMapRequest.create("/count").run {
        dataMap.putInt("count_key", count)
        asPutDataRequest()
    }
    // Create a task to send the data to the data layer
    val task: Task<DataItem> = Wearable.getDataClient(this).putDataItem(putDataReq)
    try {
        Tasks.await(task).apply {
            // Add your logic here
        }
    } catch (e: ExecutionException) {
        // TODO: Handle exception
    } catch (e: InterruptedException) {
        // TODO: Handle exception
        Thread.currentThread().interrupt()
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
such a case, you can listen for events in an activity by implementing one or
more of the following interfaces:

- [`DataClient.OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener)
- [`MessageClient.OnMessageReceivedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient.OnMessageReceivedListener)
- [`CapabilityClient.OnCapabilityChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/CapabilityClient.OnCapabilityChangedListener)
- [`ChannelClient.ChannelCallback`](https://developers.google.com/android/reference/com/google/android/gms/wearable/ChannelClient.ChannelCallback)

To create an activity that listens for data events, follow these steps:

1. Implement the required interfaces.
2. In the `onCreate()` or `onResume()` method, call `Wearable.getDataClient(this).addListener()`, `MessageClient.addListener()`, `CapabilityClient.addListener()`, or `ChannelClient.registerChannelCallback()` to notify Google Play services that your activity is interested in data layer events.
3. In [`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()) or [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()), unregister any listeners with `DataClient.removeListener()`, `MessageClient.removeListener()`, `CapabilityClient.removeListener()`, or `ChannelClient.unregisterChannelCallback()`.
4. If an activity only needs to receive events with a specific path prefix, add a listener with a prefix filter to only receive data relevant to the current application state.
5. Implement `onDataChanged()`, `onMessageReceived()`, `onCapabilityChanged()`, or methods from [`ChannelClient.ChannelCallback`](https://developers.google.com/android/reference/com/google/android/gms/wearable/ChannelClient.ChannelCallback), depending on the interfaces that you implemented. These methods are called on the main thread, or you can specify a custom `Looper` using [`WearableOptions`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable.WearableOptions).

Here's an example that implements [`DataClient.OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener):

<br />

```kotlin
class MainActivity : Activity(), DataClient.OnDataChangedListener {

    public override fun onResume() {
        super.onResume()
        Wearable.getDataClient(this).addListener(this)
    }

    override fun onPause() {
        super.onPause()
        Wearable.getDataClient(this).removeListener(this)
    }

    override fun onDataChanged(dataEvents: DataEventBuffer) {
        dataEvents.forEach { event ->
            if (event.type == DataEvent.TYPE_DELETED) {
                Log.d(TAG, "DataItem deleted: " + event.dataItem.uri)
            } else if (event.type == DataEvent.TYPE_CHANGED) {
                Log.d(TAG, "DataItem changed: " + event.dataItem.uri)
            }
        }
    }
}
```

<br />

**Caution:** Before using the Wearable Data Layer API, check that it's available
on a device; otherwise, an exception occurs. Use the
[`GoogleApiAvailability`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability) class, as implemented in [Horologist](https://github.com/google/horologist/blob/release-0.5.x/datalayer/core/src/main/java/com/google/android/horologist/data/WearableApiAvailability.kt#L29).

### Use filters with live listeners

As previously mentioned, just as you can specify intent filters for
manifest-based `WearableListenerService` objects, you can use intent filters
when registering a live listener through the [Wearable API](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable). The same rules
apply to both API-based live listeners and manifest-based listeners.

A common pattern is to register a listener with a specific path or path prefix
in an activity's [`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) method, and then to remove the listener in
the activity's [`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) method. Implementing listeners in this fashion
lets your app more selectively receive events, improving its design and
efficiency.