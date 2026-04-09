---
title: https://developer.android.com/training/wearables/data/data-items
url: https://developer.android.com/training/wearables/data/data-items
source: md.txt
---

A [`DataItem`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItem.html)
defines the interface that the system uses to synchronize data between handhelds and
wearables. A `DataItem` generally consists of the following components:

- **Payload:** A byte array that you can set with data, letting you do your own object serialization and deserialization. The size of the payload is limited to 100 KB.
- **Path:** A unique string that must start with a forward slash, such as `"/path/to/data"`.


**Note:**
The Data Layer API can only send messages and synchronize data with Android phones or Wear OS
watches. If your Wear OS device is paired with an iOS device, the Data Layer API won't
work.  

For this reason, don't use the Data Layer API as the
primary way to communicate with a network. Instead, follow the
[same pattern as a mobile app, with some minor differences](https://developer.android.com/training/wearables/data-layer/network-access).


You normally don't implement [`DataItem`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItem.html)
directly. Instead, you do the following:

1. Create a [`PutDataRequest`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest.html) object, specifying a string path to uniquely identify the item.
2. Call [`setData()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest.html#setData(byte[])) to set the payload.
3. If a delay in syncing would negatively impact user experience, call [`setUrgent()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest#setUrgent()).
4. Use the `putDataItem` method of the [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) class to request that the system create the data item.


When requesting data items, the system returns objects that properly implement the
`DataItem` interface. However, instead of working with raw bytes using
`setData()`, we recommend that you
[use a data map](https://developer.android.com/training/wearables/data-layer/data-items#SyncData),
which exposes a data item with a `https://developer.android.com/reference/android/os/Bundle`-like interface.


For more information, see the [DataLayer Sample](https://github.com/android/wear-os-samples/tree/main/DataLayer) app.

## Sync data with a data map


When possible, use the [`DataMap`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataMap.html) class.
This approach lets you work with data items in the form of an Android `https://developer.android.com/reference/android/os/Bundle`,
so the system does object serialization and deserialization for you, and you can manipulate data
with key-value pairs.

To use a data map:

1. Create a [`PutDataMapRequest`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataMapRequest.html) object, setting the path of the data item.

   **Note:** The path string is a unique identifier for the
   data item that lets you access it from either side of the connection. The path
   must begin with a forward slash. If you're using hierarchical data in your
   app, create a path scheme that matches the structure of the data.
2. Call [`PutDataMapRequest.getDataMap()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataMapRequest.html#getDataMap()) to obtain a data map that you can set values on.
3. Set values for the data map using the `put...()` methods, such as [`putString()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataMap.html#putString(java.lang.String, java.lang.String)).
4. If a delay in syncing would negatively impact user experience, call [`setUrgent()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest#setUrgent()).
5. Call [`PutDataMapRequest.asPutDataRequest()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataMapRequest.html#asPutDataRequest()) to obtain a [`PutDataRequest`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest.html) object.
6. Use the `putDataItem` method of the [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) class to request that the system create the data item.

   **Note:**
   If the handset and wearable devices are disconnected,
   the data is buffered and synced when the connection is re-established.

The `increaseCounter()` method in the following example shows how to create a
data map and put data in it:

```kotlin
private fun increaseCounter(): Task<DataItem> {
    val putDataReq: PutDataRequest = PutDataMapRequest.create("/count").run {
        dataMap.putInt(COUNT_KEY, count++)
        asPutDataRequest()
    }
    return Wearable.getDataClient(this)
        .putDataItem(putDataReq)
}
```


For more information about handling
[`Tasks`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Tasks), see the
[reference documentation](https://developers.google.com/android/reference/com/google/android/gms/tasks/package-summary).

**Caution:**
Before using the Wearable Data Layer API, check that it's available on
a device; otherwise, an exception occurs. Use the [`GoogleApiAvailability`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability)
class, as implemented in [Horologist](https://github.com/google/horologist/blob/release-0.5.x/datalayer/core/src/main/java/com/google/android/horologist/data/WearableApiAvailability.kt#L29).

### Set DataItem priority


The [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) API allows urgent requests for syncing of
[`DataItem`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItem.html)
objects.
Normally, the system delays delivery of data items
to the Wear OS network to improve battery life for user devices, but
if a delay in syncing data items negatively impacts user experience, you can mark
them as urgent. For example, in a remote control app where the user expects their
actions to be reflected immediately, you can have the system sync your data items
immediately by calling
[`setUrgent()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest#setUrgent()).


If you don't call `setUrgent()`, the system might delay up to 30 minutes before
syncing non-urgent data items, though you can usually expect the delay to be only a few
minutes. The default urgency is non-urgent, so you must use
`setUrgent()` if you need to retain the immediate-sync behavior from
previous versions of the Wear OS API.

## Listen for data item events

If one side of the data layer connection changes a data item, notify
the user of any changes on the other side of the connection.
You can do this by implementing a listener for data item events.

The code snippet in the following example notifies the app when the value of the
counter defined in the previous example changes:

```kotlin
override fun onDataChanged(dataEvents: DataEventBuffer) {

    dataEvents.forEach { event ->
        // DataItem changed
        if (event.type == DataEvent.TYPE_CHANGED) {
            event.dataItem.also { item ->
                if (item.uri.path?.compareTo("/count") == 0) {
                    DataMapItem.fromDataItem(item).dataMap.apply {
                        updateCount(getInt(COUNT_KEY))
                    }
                }
            }
        } else if (event.type == DataEvent.TYPE_DELETED) {
            // DataItem deleted
        }
    }
}
```


This activity implements the [`DataClient.OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener.html) interface. The activity adds itself
as a listener for data item events inside
the `onResume()` method and removes the listener in the
`onPause()` method. To see an implementation using images, view models, and
services, see the [DataLayer Sample](https://github.com/android/wear-os-samples/tree/main/DataLayer)
app.

You can also implement the listener as a service. For more information, see
[Listen for Data Layer
events](https://developer.android.com/training/wearables/data-layer/events#Listen).