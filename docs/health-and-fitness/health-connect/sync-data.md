---
title: https://developer.android.com/health-and-fitness/health-connect/sync-data
url: https://developer.android.com/health-and-fitness/health-connect/sync-data
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

Most apps that integrate with Health Connect have their own datastore that
serves as the source of truth. Health Connect provides ways to keep your app
in sync.

Depending on your app's architecture, the sync process might involve some or
all of the following actions:

- Feed new or updated data from your app's datastore to Health Connect.
- Pull data changes from Health Connect into your app's datastore.
- Delete data from Health Connect when it's deleted in your app's datastore.

In each case, make sure that the syncing process keeps both Health Connect and
your app's datastore aligned.

## Feed data to Health Connect

The first part of the syncing process is to feed data from your app's datastore
to the Health Connect datastore.

### Prepare your data

Usually, records in your app's datastore have the following details:

- A unique key, such as a `UUID`.
- A version or timestamp.

When syncing data to Health Connect, identify and feed only the data that has
been inserted, updated, or deleted since the last sync.

### Write data to Health Connect

To feed data into Health Connect, carry out the following steps:

1. Obtain a list of new, updated, or deleted entries from your app's datastore.
2. For each entry, create a `Record` object appropriate for that data type. For example, create a `WeightRecord` object for data related to weight.
3. Specify a `Metadata` object with each `Record`. This includes
   `clientRecordId`, which is an ID from your app's datastore that you can use
   to uniquely identify the record. You can use your existing unique key for
   this. If your data is versioned, also provide a
   `clientRecordVersion` that aligns with the versioning used in your data.
   If it's not versioned, you can use the `Long` value
   of the current timestamp as an alternative.

       val recordVersion = 0L
       // Specify as needed
       // The clientRecordId is an ID that you choose for your record. This
       // is often the same ID you use in your app's datastore.
       val clientRecordId = "<your-record-id>"

       val record = WeightRecord(
           metadata = Metadata.activelyRecorded(
               clientRecordId = clientRecordId,
               clientRecordVersion = recordVersion,
               device = Device(type = Device.TYPE_SCALE)
           ),
           weight = Mass.kilograms(62.0),
           time = Instant.now(),
           zoneOffset = ZoneOffset.UTC,
       )
       healthConnectClient.insertRecords(listOf()(record))

4. [Upsert](https://developer.android.com/guide/health-and-fitness/health-connect/develop/write-data#upsert-through-client-id) data to Health Connect using
   [`insertRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#insertRecords(kotlin.collections.List)). Upserting data means that any existing
   data in Health Connect gets overwritten as long as the `clientRecordId`
   values exist in the Health Connect datastore, and the `clientRecordVersion`
   is higher than the existing value. Otherwise, the upserted data is written
   as new data.

       healthConnectClient.insertRecords(arrayListOf(record))

To learn about the practical considerations for feeding data, check out the best
practices for [Write data](https://developer.android.com/guide/health-and-fitness/health-connect/plan/best-practices#write-data).

### Store Health Connect IDs

If your app also reads data from Health Connect, store the Health Connect `id`
for records after you upsert them. You need this `id` to process deletions when
you pull data changes from Health Connect.

The [`insertRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#insertRecords(kotlin.collections.List)) function returns a
[`InsertRecordsResponse`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/response/InsertRecordsResponse) that contains the list of `id` values.
Use the response to get the Record IDs and store them.  

    val response = healthConnectClient.insertRecords(arrayListOf(record))

    for (recordId in response.recordIdsList) {
        // Store recordId to your app's datastore
    }

| **Note:** If your app needs to read data from Health Connect, you must store the `id`. This is necessary to correctly process deletion changelogs, as `DeletionChange` notifications only provide the record `id`.

## Pull data from Health Connect

The second part of the syncing process is to pull for any data changes from
Health Connect to your app's datastore. The data changes can include updates and
deletions.

### Get a Changes token

To get a list of changes to pull from Health Connect, your app needs to keep
track of *Changes* tokens. You can use them when requesting *Changes* to
return both a list of data changes, and a new *Changes* token to be used next
time.

To obtain a *Changes* token, call [`getChangesToken`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#getChangesToken(androidx.health.connect.client.request.ChangesTokenRequest)) and
supply the required data types.  

    val changesToken = healthConnectClient.getChangesToken(
        ChangesTokenRequest(recordTypes = setOf(WeightRecord::class))
    )

| **Note:** We recommend getting separate tokens per data type instead of getting them in bulk to avoid having an `Exception` in case one of the permissions is revoked.

### Check for data changes

Now that you've obtained a *Changes* token, use it to get all *Changes* .
We recommend creating a loop to get through all the *Changes* where it checks
if there are available data changes. Here are the following steps:

1. Call [`getChanges`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#getChanges(kotlin.String)) using the token to obtain a list of *Changes*.
2. Check each change whether its type of change is an [`UpsertionChange`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/changes/UpsertionChange) or a [`DeletionChange`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/changes/DeletionChange), and perform the necessary operations.
   - For `UpsertionChange`, only take changes that didn't come from the calling app to make sure you're not re-importing data.
3. Assign the next *Changes* token as your new token.
4. Repeat Steps 1-3 until there are no *Changes* left.
5. Store the next token and reserve it for a future import.

    suspend fun processChanges(token: String): String {
        var nextChangesToken = token
        do {
            val response = healthConnectClient.getChanges(nextChangesToken)
            response.changes.forEach { change ->
                when (change) {
                    is UpsertionChange ->
                        if (change.record.metadata.dataOrigin.packageName != context.packageName) {
                            processUpsertionChange(change)
                        }
                    is DeletionChange -> processDeletionChange(change)
                }
            }
            nextChangesToken = response.nextChangesToken
        } while (response.hasMore)
        // Return and store the changes token for use next time.
        return nextChangesToken
    }

To learn about the practical considerations for pulling data, check out the best
practices for [Sync data](https://developer.android.com/guide/health-and-fitness/health-connect/plan/best-practices#sync-data).

### Process data changes

Reflect the changes to your app's datastore. For `UpsertionChange`, use the `id`
and the `lastModifiedTime` from its `metadata` to [upsert](https://developer.android.com/guide/health-and-fitness/health-connect/develop/write-data#upsert-through-client-id) the record.
For `DeletionChange`, use the `id` provided to [delete](https://developer.android.com/guide/health-and-fitness/health-connect/develop/delete-data) the record.
This requires that you have stored the record `id` as mentioned in
[Store Health Connect IDs](https://developer.android.com/health-and-fitness/health-connect/sync-data#store-ids).
| **Note:** [`DeletionChange`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/changes/DeletionChange) only contains the `id` of the deleted record, and not the record type, due to privacy. With that, you can either specify only 1 data type for each call of `getChanges`, or make sure that you've stored this information separately beforehand.

## Delete data from Health Connect

When a user deletes their own data from your app, make sure that the data is
also [removed](https://developer.android.com/guide/health-and-fitness/health-connect/develop/delete-data) from Health Connect. Use [`deleteRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,kotlin.collections.List,kotlin.collections.List))
to do this. This takes a record type and list of `id` and `clientRecordId`
values, which makes it convenient to batch multiple data for deletion. An
alternative [`deleteRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,androidx.health.connect.client.time.TimeRangeFilter)) that takes in a `timeRangeFilter`
is also available.

## Low-latency synchronization from wearables

To sync data from a wearable fitness device to Health Connect with low latency,
use [`CompanionDeviceService`](https://developer.android.com/reference/android/companion/CompanionDeviceService). This approach works for
devices that support BLE GATT Notifications or Indications and
target Android 8.0 (API level 26) or higher. `CompanionDeviceService` allows
your app to receive data from wearables and write it to Health Connect, even
when the app isn't already running. For more details on BLE best practices, see
[Bluetooth Low Energy overview](https://developer.android.com/develop/connectivity/bluetooth/ble/background#stay-connected).

### Associate the device

First, your app must guide the user through a one-time process to associate
the wearable with your app using
[`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager). This grants your app the
necessary permissions to interact with the device. For more information,
see [Companion device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing).

### Declare the service in the Manifest

Next, declare `CompanionDeviceService` in your app's manifest file. Add the
following to your `AndroidManifest.xml`:  

    <manifest ...>
       <application ...>
           <service
               android:name=".MyWearableService"
               android:exported="true"
               android:permission="android.permission.BIND_COMPANION_DEVICE_SERVICE">
               <intent-filter>
                   <action android:name="android.companion.CompanionDeviceService" />
               </intent-filter>
           </service>
       </application>
    </manifest>

### Create CompanionDeviceService

Finally, create a class that extends `CompanionDeviceService`. This service
handles the connection to the wearable device and receives data through BLE
GATT callbacks. When new data is received, it's immediately written to Health
Connect.  

    import android.companion.CompanionDeviceService
    import android.bluetooth.BluetoothGatt
    import android.bluetooth.BluetoothGattCallback
    import android.bluetooth.BluetoothGattCharacteristic
    import androidx.health.connect.client.permission.HealthPermission
    import androidx.health.connect.client.HealthConnectClient
    import androidx.health.connect.client.records.HeartRateRecord
    import androidx.health.connect.client.records.StepsRecord
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.Dispatchers
    import kotlinx.coroutines.SupervisorJob
    import kotlinx.coroutines.launch

    class MyWearableService : CompanionDeviceService() {

       // A coroutine scope for handling suspend functions like writing to Health Connect
       private val serviceScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)
       private var healthConnectClient: HealthConnectClient? = null
       private var bluetoothGatt: BluetoothGatt? = null

       // This is called by the system when your wearable connects
       override fun onDeviceAppeared(address: String) {
           super.onDeviceAppeared(address)
           healthConnectClient = HealthConnectClient.getOrCreate(this)

           serviceScope.launch {
               // Check which permissions have been granted before subscribing to data from the wearable.
               // A service cannot request permissions, so your app must have already requested
               // and been granted them from an Activity.
               val granted = healthConnectClient?.permissionController?.getGrantedPermissions()

               // ... set up your GATT connection here ...

               // Once connected, subscribe to notifications for the data types you have
               // permission to write.
               if (granted?.contains(HealthPermission.getWritePermission(HeartRateRecord::class)) == true) {
                   // subscribeToHeartRate(bluetoothGatt)
               }
           }
       }

       // The core of your low-latency pipeline is the BLE callback
       private val gattCallback = object : BluetoothGattCallback() {
           override fun onCharacteristicChanged(gatt: BluetoothGatt, characteristic: BluetoothGattCharacteristic, value: ByteArray) {
               super.onCharacteristicChanged(gatt, characteristic, value)

               // 1. Instantly receive the data
               val rawData = value

               // 2. Parse the data from the wearable
               val healthData = parseWearableData(rawData) // Your custom parsing logic

               // 3. Immediately process it. For simplicity, this example writes
               //    directly to Health Connect. A real-world app might write to its
               //    own datastore first and then sync with Health Connect.
               serviceScope.launch {
                   writeToHealthConnect(healthData)
               }
           }
       }

       private suspend fun writeToHealthConnect(healthData: HealthData) {
           val records = prepareHealthConnectRecords(healthData) // Convert to Health Connect records
           try {
               healthConnectClient?.insertRecords(records)
           } catch (e: Exception) {
               // Handle exceptions
           }
       }

       // This is called by the system when your wearable disconnects
       override fun onDeviceDisappeared(address: String) {
           super.onDeviceDisappeared(address)
           // Clean up your GATT connection and other resources
           bluetoothGatt?.close()
       }
    }

## Best practices for syncing data

The following factors affect the syncing process.

### Token expiration

Since an unused *Changes* token expires within 30 days, you must use a sync
strategy that avoids losing information in such a case. Your strategy could
include the following approaches:

- Search your app datastore for the most recently consumed record that also has an `id` from Health Connect.
- Request records from Health Connect that begin with a specific timestamp, and then insert or update them in your app's datastore.
- Request a Changes token to reserve it for the next time it's needed.

#### Recommended Changes management strategies

In case your app is getting invalid or expired *Changes* tokens, we
recommend the following management strategies depending on its application in
your logic:

- **Read and dedupe all data** . This is the most ideal strategy.
  - Store the timestamp of the last time they read data from Health Connect.
  - On token expiry, re-read all data from the most recent timestamp or for the last 30 days. Then, dedupe it against the previously read data using identifiers.
  - Ideally, implement Client IDs since they are required for data updates.
- **Only read data since the last read timestamp** . This results in some data discrepancies around the time of Changes token expiry, but the time period is shorter that could take a few hours to a couple of days.
  - Store the timestamp of the last time they read data from Health Connect.
  - On token expiry, read all data from this timestamp onwards.
- **Delete then read data for the last 30 days** . This aligns more closely with what happens on the first integration.
  - Delete all data read by the app from Health Connect for the last 30 days.
  - Once deleted, read all of this data again.
- **Read data for last 30 days without deduping** . This is the least ideal strategy, and results in having duplicate data displayed to users.
  - Delete all data read by the app from Health Connect for the last 30 days.
  - Allow duplicate entries.

### Data type Changes tokens

If your app consumes more than one data type independently, use separate Changes
Tokens for each data type. Only use a list of multiple data types with the
Changes Sync API if these data types are either consumed together or not at all.

### Foreground reads

Apps can only read data from Health Connect while they are in the foreground.
When syncing data from Health Connect, access to Health Connect may be
interrupted at any point. For example, your app must handle interruptions
midway through a sync when reading a large amount of data from Health Connect,
and continue the next time the app is opened.

### Background reads

You can request that your application run in the background and read data from
Health Connect. If you request the
[`Background Read`](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example) permission, your user can grant your app
access to read data in the background.

### Import timings

As your app can't get notified of new data, check for new data at two points:

- Each time your app becomes active in the foreground. In this case, use lifecycle events.
- Periodically, while your app remains in the foreground. Notify users when new data is available, allowing them to update their screen to reflect the changes.