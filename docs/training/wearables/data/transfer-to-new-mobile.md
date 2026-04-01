---
title: https://developer.android.com/training/wearables/data/transfer-to-new-mobile
url: https://developer.android.com/training/wearables/data/transfer-to-new-mobile
source: md.txt
---

When users [set up a Wear OS device](https://support.google.com/wearos/answer/6056630), they connect the Wear OS device to a
particular mobile device. The user might later decide to get a new mobile device
and connect their existing Wear OS device to this new mobile device. Some data
related to a Wear OS device is stored on the currently-connected mobile device.

Starting in Wear OS 4, when users connect to a new mobile device, they can
transfer Wear OS data to the new mobile device. Data is synced automatically
when it's transferred.

> [!NOTE]
> **Note:** This process of transferring data to a new mobile device is different from [cloud backup and restore](https://developer.android.com/training/wearables/data/cloud-backup-restore), where the user restores data to a new Wear OS device.

When the user requests a transfer, the [Wearable Data Layer](https://developer.android.com/training/wearables/data/data-layer) delivers
[`DataItem`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItem) objects, originally stored on one mobile device, to the other
mobile device. This allows a seamless experience for users of your app.

This document describes how you can configure your Wear OS app, and its
companion mobile app, to support this scenario.

## Preparation

The data transfer process handles `DataItem` objects differently, depending on
which app owns the data:

Objects owned by the Wear OS app
:   These objects are preserved on the Wear OS device.

Objects owned by the mobile app

:   These objects are archived on the old device. The system then packages the
    archived data into a [`DataItemBuffer`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItemBuffer) object and delivers this data to the
    mobile app that's installed on the new mobile device.

    Immediately after the archive is delivered, the Wearable Data Layer invokes
    the [`onNodeMigrated()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService#onNodeMigrated(java.lang.String,%20com.google.android.gms.wearable.DataItemBuffer)) listener, similarly to how your app is notified
    when data is written by the Wear OS device.

    > [!NOTE]
    > **Note:** Data is transferred only if it's stored in the Wearable Data Layer.

## Preserve transferred data

> [!WARNING]
> **Warning:** To avoid losing data, follow the guidance in this section.

It's your app's responsibility to preserve the transferred `DataItem` objects.
Shortly after the data is delivered to the new mobile device, the archive is
deleted off of the old device.

Make sure each of the following conditions is true:

1. Your app is installed on both mobile devices that are involved in the transfer.
2. The mobile apps, installed on each mobile device, have package signatures that match.

Otherwise, the archived `DataItem` objects aren't delivered and are instead
discarded.

## Receive data from the old mobile device

To receive data on the new mobile device that was archived on the old mobile
device, your mobile app must implement the [`onNodeMigrated()`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService#onNodeMigrated(java.lang.String,%20com.google.android.gms.wearable.DataItemBuffer)) callback,
part of the `WearableListenerService` class. To do so, complete the following
steps:

1. In your mobile app's build file, include a dependency on the latest version
   of the wearable library in Google Play services:

   ```groovy
   dependencies {
       ...
       implementation 'com.google.android.gms:play-services-wearable:19.0.0'
   }
   ```
2. Declare and export the `WearableListenerService` in your app's
   manifest file:

   <br />

   ```xml
   <service
       android:name=".snippets.datalayer.MyWearableListenerService"
       android:exported="true"
       tools:ignore="ExportedService">
       <intent-filter>
           <action android:name="com.google.android.gms.wearable.NODE_MIGRATED" />
           <data android:scheme="wear" android:host="*" />
       </intent-filter>
   </service>
   ```

   <br />

3. Create a service class which extends `WearableListenerService` and overrides
   `onNodeMigrated()`.

   > [!CAUTION]
   > **Caution:** To preserve system resources such as battery life, and to prevent ANRs, don't execute any power-demanding or time-consuming tasks in the `onNodeMigrated()` handler.

   <br />

   ```kotlin
   class MyWearableListenerService : WearableListenerService() {
       val dataClient: DataClient = Wearable.getDataClient(this)

       private fun shouldHandleDataItem(nodeId: String, dataItem: DataItem): Boolean {
           // Your logic here
           return dataItem.uri.path?.startsWith("/my_feature_path/") == true
       }

       private fun handleDataItem(nodeId: String, dataItem: DataItem) {
           val data = dataItem.data ?: return
           val path = dataItem.uri.path ?: return
           // Your logic here
           if (data.toString().startsWith("Please restore")) {
               dataClient.putDataItem(PutDataRequest.create(path).setData(data))
           }
       }

       override fun onNodeMigrated(nodeId: String, archive: DataItemBuffer) {
           val dataItemsToHandle = mutableListOf<DataItem>()

           for (dataItem in archive) {
               if (shouldHandleDataItem(nodeId, dataItem)) {
                   dataItemsToHandle.add(dataItem.freeze())
               }
           }

           // Callback stops automatically after 20 seconds of data processing.
           // If you think you need more time, delegate to a coroutine or thread.
           runBlocking {
               for (dataItem in dataItemsToHandle) {
                   handleDataItem(nodeId, dataItem)
               }
           }
       }
   }
   ```

   <br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Integrate a Wear OS module](https://developer.android.com/health-and-fitness/guides/basic-fitness-app/integrate-wear-os)
- [Conserve power and battery](https://developer.android.com/training/wearables/apps/power)