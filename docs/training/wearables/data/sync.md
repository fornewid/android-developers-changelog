---
title: https://developer.android.com/training/wearables/data/sync
url: https://developer.android.com/training/wearables/data/sync
source: md.txt
---

This document describes how to synchronize data between a Wear OS device and a
handheld device.

## Send and sync data directly from the network

Build Wear OS apps to [communicate directly with the network](https://developer.android.com/training/wearables/data-layer/network-access). Use the same
APIs that you use for mobile development, but keep some Wear-OS-specific
differences in mind.

## Synchronize data using the Wear OS Data Layer API

A `DataClient` exposes an API for components to read or write to a `DataItem` or
`Asset`.

> [!NOTE]
> **Note:** The class is meant to transfer data and not serve as a storage mechanism. Create your own copy of the data that your app can access, such as in a [Room
> database](https://developer.android.com/training/data-storage/room).

It's possible to set data items and assets while not connected to any devices.
They're synchronized when the devices establish a network connection. This data
is private to your app and is only accessible to your app on other devices.

- A `DataItem` is synchronized across all devices in a Wear OS network.
  They're generally small in size.

  > [!NOTE]
  > **Note:** When an app is uninstalled on the phone, data items and assets are reset.

- Use an `Asset` to transfer a larger object, such as an image. The system
  keeps track of which assets have already been transferred and performs
  deduplication automatically.

### Listen for events in services

Extend the [`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService) class. The system manages the
lifecycle of the base `WearableListenerService`, binding to the service when it
needs to send data items or messages and unbinding the service when no work is
needed.

### Listen for events in activities

Implement the [`OnDataChangedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient.OnDataChangedListener) interface. Use this interface instead
of a `WearableListenerService` when you want to listen for changes only when the
user is actively using your app.

## Transfer data

To send binary large objects over the Bluetooth transport, such as a voice recording
from another device, you can attach an
[`Asset`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Asset) to a data item and then put the data item into the replicated datastore.

> [!NOTE]
>
> **Note:** The Data Layer API can send messages and synchronize data only with Android phones or
> Wear OS watches. If a Wear OS device is paired with an iOS device, the Data Layer
> API won't work.
>
>
> For this reason, don't use the Data Layer API as the primary way to
> communicate with a network. Instead, follow the same pattern in your Wear app as in a
> mobile app---with some minor differences, as described in
> [Network access and sync on Wear OS](https://developer.android.com/training/wearables/data-layer/network-access).

Assets automatically handle caching of data to prevent retransmission and
to conserve Bluetooth bandwidth.
A common pattern is for a handheld app to download an image, shrink it to an appropriate size
for display on the wearable, and transmit it to the wearable app as an asset. The following examples
demonstrate this pattern.


**Note:** Although the size of data items is theoretically limited to 100 KB, in practice larger data items can be used. For
larger data items, separate data by unique paths and avoid
using a single path for all data. Transferring large assets affects the user experience in many
cases, so test your apps to help ensure that they perform well when transferring large assets.

### Transfer an asset

Create the asset using one of the `create...()` methods in the
[`Asset`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Asset.html) class.
Convert a bitmap to a byte stream and then call
[`createFromBytes()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Asset.html#createFromBytes(byte[]))
to create the asset, as shown in the following sample.

### Kotlin

```kotlin
private fun createAssetFromBitmap(bitmap: Bitmap): Asset =
    ByteArrayOutputStream().let { byteStream ->
        bitmap.compress(Bitmap.CompressFormat.PNG, 100, byteStream)
        Asset.createFromBytes(byteStream.toByteArray())
    }
```

### Java

```java
private static Asset createAssetFromBitmap(Bitmap bitmap) {
    final ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
    bitmap.compress(Bitmap.CompressFormat.PNG, 100, byteStream);
    return Asset.createFromBytes(byteStream.toByteArray());
}
```

Next, attach the asset to a data item with the `putAsset()` method in
[`DataMap`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataMap.html) or
[`PutDataRequest`](https://developers.google.com/android/reference/com/google/android/gms/wearable/PutDataRequest.html). Then put the data item into the datastore using the
[`putDataItem()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataApi.html#putDataItem(com.google.android.gms.common.api.GoogleApiClient, com.google.android.gms.wearable.PutDataRequest)) method, as shown in the following samples.

The following sample uses `PutDataRequest`:

### Kotlin

```kotlin
val asset: Asset = BitmapFactory.decodeResource(resources, R.drawable.image).let { bitmap ->
    createAssetFromBitmap(bitmap)
}
val request: PutDataRequest = PutDataRequest.create("/image").apply {
    putAsset("profileImage", asset)
}
val putTask: Task<DataItem> = Wearable.getDataClient(context).putDataItem(request)
```

### Java

```java
Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.image);
Asset asset = createAssetFromBitmap(bitmap);
PutDataRequest request = PutDataRequest.create("/image");
request.putAsset("profileImage", asset);
Task<DataItem> putTask = Wearable.getDataClient(context).putDataItem(request);
```

<br />

The following sample uses `PutDataMapRequest`:

### Kotlin

```kotlin
val asset: Asset = BitmapFactory.decodeResource(resources, R.drawable.image).let { bitmap ->
    createAssetFromBitmap(bitmap)
}
val request: PutDataRequest = PutDataMapRequest.create("/image").run {
    dataMap.putAsset("profileImage", asset)
    asPutDataRequest()
}
val putTask: Task<DataItem> = Wearable.getDataClient(context).putDataItem(request)
```

### Java

```java
Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.image);
Asset asset = createAssetFromBitmap(bitmap);
PutDataMapRequest dataMap = PutDataMapRequest.create("/image");
dataMap.getDataMap().putAsset("profileImage", asset);
PutDataRequest request = dataMap.asPutDataRequest();
Task<DataItem> putTask = Wearable.getDataClient(context).putDataItem(request);
```

<br />

> [!CAUTION]
> **Caution:** Before using the Wearable Data Layer API, check that it's available on a device; otherwise, an exception occurs. Use the [`GoogleApiAvailability`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability) class, as implemented in [Horologist](https://github.com/google/horologist/blob/release-0.5.x/datalayer/core/src/main/java/com/google/android/horologist/data/WearableApiAvailability.kt#L29).

### Receive assets


When an asset is created, you probably want to read and extract
it on other side of the connection. Here's an example of how to implement the
callback to detect an asset change and extract the asset:

<br />

```kotlin
override fun onDataChanged(dataEvents: DataEventBuffer) {
    dataEvents
        .filter { it.type == DataEvent.TYPE_CHANGED && it.dataItem.uri.path == "/image" }
        .forEach { event ->
            val bitmap: Bitmap? = DataMapItem.fromDataItem(event.dataItem)
                .dataMap.getAsset("profileImage")
                ?.let { asset -> loadBitmapFromAsset(asset) }
            // Do something with the bitmap
        }
}

fun loadBitmapFromAsset(asset: Asset): Bitmap? {
    // Convert asset into a file descriptor and block until it's ready
    val assetInputStream: InputStream? =
        Tasks.await(Wearable.getDataClient(this).getFdForAsset(asset))
            ?.inputStream

    return assetInputStream?.let { inputStream ->
        // Decode the stream into a bitmap
        BitmapFactory.decodeStream(inputStream)
    } ?: run {
        // Requested an unknown asset
        null
    }
}
```

<br />

For more information, see the [DataLayer sample project](https://github.com/android/wear-os-samples/tree/main/DataLayer) on GitHub.