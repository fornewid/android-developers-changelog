---
title: https://developer.android.com/health-and-fitness/health-connect/read-data
url: https://developer.android.com/health-and-fitness/health-connect/read-data
source: md.txt
---

The following example shows you how to read raw data as part of the common
workflow.
| **Tip:** For further guidance on reading raw data, take a look at the [Android
| Developer video for reading and writing data](https://www.youtube.com/watch?v=NAx7Gv_Hk7E&t=122) in Health Connect.

## Read data

Health Connect allows apps to read data from the datastore when the app is
in the foreground and background:

- **Foreground reads**: You can normally read data from Health Connect when
  your app is in the foreground. In these cases, you may consider using a
  foreground service to run this operation in case the user or system places your
  app in the background during a read operation.

- **Background reads** : By requesting an extra permission from the user, you
  can read data after the user or system places your app in the background.
  See the complete [background read example](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example).

The Steps data type in Health Connect captures the number of steps a user has
taken between readings. Step counts represent a common measurement across
health, fitness, and wellness platforms. Health Connect lets you read and write
step count data.

To read records, create a [`ReadRecordsRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/ReadRecordsRequest) and supply
it when you call [`readRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#readRecords(androidx.health.connect.client.request.ReadRecordsRequest)).
| **Note:** For cumulative types like `StepsRecord`, use `aggregate()` instead of `readRecords()` to avoid double counting from multiple sources and improve accuracy. See [Read aggregated
| data](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary) for more information.

The following example shows how to read step count data for a user within a
certain time. For an extended example with [`SensorManager`](https://developer.android.com/reference/android/hardware/SensorManager),
see the [step count](https://developer.android.com/health-and-fitness/guides/basic-fitness-app/read-step-count-data) data guide.  

    suspend fun readStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.readRecords(
                ReadRecordsRequest(
                    StepsRecord::class,
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            for (record in response.records) {
                // Process each record
            }
        } catch (e: Exception) {
            // Run error handling here
        }
    }

You can also read your data in an aggregated manner using
[`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary).  

    suspend fun readStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            // The result may be null if no data is available in the time range
            val stepCount = response[StepsRecord.COUNT_TOTAL]
        } catch (e: Exception) {
            // Run error handling here
        }
    }

| **Note:** If you're interested in obtaining calculated data such as averages and totals, it is recommended to use [aggregation](https://developer.android.com/health-and-fitness/guides/health-connect/develop/aggregate-data). You can set [smaller time slices](https://developer.android.com/health-and-fitness/guides/health-connect/develop/aggregate-data#buckets) whenever you aggregate. The aggregation API also contains logic to handle duplicate records, and lessens the chances of rate limiting.

## Read mobile steps

With Android 14 (API level 34) and SDK Extension version 20 or higher,
Health Connect provides on-device step counting. If any app has been granted
the `READ_STEPS` permission, Health Connect starts capturing steps from the
Android-powered device, and users see steps data automatically added to
Health Connect **Steps** entries.

To check if on-device step counting is available, you need to verify that the
device is running Android 14 (API level 34) and has at least SDK extension
version 20. You can use the following code:  

    val isStepTrackingAvailable =
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.UPSIDE_DOWN_CAKE &&
            SdkExtensions.getExtensionVersion(Build.VERSION_CODES.UPSIDE_DOWN_CAKE) >= 20

Mobile steps captured by Health Connect have their
[`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin) set to the package name `android`. If your app
simply reads aggregated step counts using [`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary) and
doesn't filter by `DataOrigin`, on-device steps are automatically included in
the total.

If your app needs to read on-device steps, or if it displays step data
broken down by source application or device, you can query for records
where the `DataOrigin` is `android`. If your app shows attribution for step
data, you should attribute data from the android package to the current device.
You can do this by using a label such as "Your phone", retrieving the device
name with `Settings.Global.getString(resolver, Settings.Global.DEVICE_NAME)`,
or inspecting the [`Device`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Device) field in the record's metadata.

The following example shows how to read aggregated mobile step count data by
filtering for the `android` data origin:  

    suspend fun readStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                    dataOriginFilter = setOf(DataOrigin("android"))
                )
            )
            // The result may be null if no data is available in the time range
            val stepCount = response[StepsRecord.COUNT_TOTAL]
        } catch (e: Exception) {
            // Run error handling here
        }
    }

| **Note:** If your app has significant users on Android 13 and lower, we recommend also maintaining or adding an integration with the local [Recording API](https://developer.android.com/health-and-fitness/recording-api).

### On-Device Step Counting

Diving deeper into the on-device step counting feature:

- **Sensor Usage** : Health Connect utilizes the [`TYPE_STEP_COUNTER`](https://developer.android.com/reference/android/hardware/Sensor#TYPE_STEP_COUNTER) sensor from `SensorManager`. This sensor is optimized for low power consumption, making it ideal for continuous background step tracking.
- **Data Granularity**: To conserve battery life, step data is typically batched and written to the Health Connect database no more frequently than once per minute.
- **Attribution** : As mentioned earlier, all steps recorded by this on-device feature are attributed to the `android` package name in the [`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin).
- **Activation** : The on-device step counting mechanism is active only when at least one application on the device has been granted the `READ_STEPS` permission within Health Connect.

### Background read example

To read data in the background, declare the following permission in your
manifest file:  

    <application>
      <uses-permission android:name="android.permission.health.READ_HEALTH_DATA_IN_BACKGROUND" />
    ...
    </application>

The following example shows how to read step count data in the background for a
user within a certain time by using [`WorkManager`](https://developer.android.com/reference/kotlin/androidx/work/WorkManager):  

    class ScheduleWorker(private val appContext: Context, workerParams: WorkerParameters):
        CoroutineWorker(appContext, workerParams) {

        override suspend fun doWork(): Result {
            // Read data and process it.
            ...

            // Return success indicating successful data retrieval
            return Result.success()
        }
    }

    if (healthConnectClient
        .features
        .getFeatureStatus(
        HealthConnectFeatures.FEATURE_READ_HEALTH_DATA_IN_BACKGROUND
        ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

        // Check if necessary permission is granted
        val grantedPermissions = healthConnectClient.permissionController.getGrantedPermissions()

        if (PERMISSION_READ_HEALTH_DATA_IN_BACKGROUND !in grantedPermissions) {
            // Perform read in foreground
            ...
        } else {
            // Schedule the periodic work request in background
            val periodicWorkRequest = PeriodicWorkRequestBuilder<ScheduleWorker>(1, TimeUnit.HOURS)
                .build()

            WorkManager.getInstance(context).enqueueUniquePeriodicWork(
                "read_health_connect",
                ExistingPeriodicWorkPolicy.KEEP,
                periodicWorkRequest
            )
        }
    } else {
      // Background reading is not available, perform read in foreground
      ...
    }

| **Note:** If the user doesn't grant all of the permissions that are required for background reads, your app should still run, and it should perform as many tasks as it can with the permissions that the user granted.

The [`ReadRecordsRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/package-summary#ReadRecordsRequest(androidx.health.connect.client.time.TimeRangeFilter,kotlin.collections.Set,kotlin.Boolean,kotlin.Int,kotlin.String)) parameter has a default `pageSize` value of 1000.
If the number of records in a single `readResponse` exceeds the
`pageSize` of the request, you need to iterate
over all pages of the response to retrieve all records by using `pageToken`.
However, be careful to avoid rate-limiting concerns.

### pageToken read example

It is recommended to use `pageToken` for reading records to retrieve all
available data from the requested time period.

The following example shows how to read all records until all page tokens have
been exhausted:  

    val type = HeartRateRecord::class
    val endTime = Instant.now()
    val startTime = endTime.minus(Duration.ofDays(7))

    try {
        var pageToken: String? = null
        do {
            val readResponse =
                healthConnectClient.readRecords(
                    ReadRecordsRequest(
                        recordType = type,
                        timeRangeFilter = TimeRangeFilter.between(
                            startTime,
                            endTime
                        ),
                        pageToken = pageToken
                    )
                )
            val records = readResponse.records
            // Do something with records
            pageToken = readResponse.pageToken
        } while (pageToken != null)
    } catch (quotaError: IllegalStateException) {
        // Backoff
    }

For information about best practices when reading large datasets, refer to
[Plan to avoid rate limiting](https://developer.android.com/health-and-fitness/guides/health-connect/plan/rate-limiting).

## Read previously written data

If an app has written records to Health Connect before, it is possible for that
app to read historical data. This is applicable for scenarios in which
the app needs to resync with Health Connect after the user has reinstalled it.

Some read restrictions apply:

- For Android 14 and higher

  - No historical limit on an app reading its own data.
  - 30-day limit on an app reading other data.
- For Android 13 and lower

  - 30-day limit on app reading any data.

The restrictions can be removed by requesting a [Read permission](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-older-data).

To read historical data, you need to indicate the package name as a
[`DataOrigin`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin) object in the `dataOriginFilter` parameter of your
[`ReadRecordsRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/ReadRecordsRequest).

The following example shows how to indicate a package name when reading
heart rate records:  

    try {
        val response =  healthConnectClient.readRecords(
            ReadRecordsRequest(
                recordType = HeartRateRecord::class,
                timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                dataOriginFilter = setOf(DataOrigin("com.my.package.name"))
            )
        )
        for (record in response.records) {
            // Process each record
        }
    } catch (e: Exception) {
        // Run error handling here
    }

## Read data older than 30 days

By default, all applications can read data from Health Connect for up to 30 days
prior to when any permission was first granted.

If you need to extend read permissions beyond any of the
[default restrictions](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-previously-written-data), request the
[`PERMISSION_READ_HEALTH_DATA_HISTORY`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/permission/HealthPermission#PERMISSION_READ_HEALTH_DATA_HISTORY()).
Otherwise, without this permission, an attempt to read records older than
30 days results in an error.

### Permissions history for a deleted app

If a user deletes your app, all permissions, including the history permission,
are revoked. If the user reinstalls your app and grants permission again,
the same [default restrictions](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-previously-written-data) apply, and your
app can read data from Health Connect for up to 30 days prior to that new date.

For example, suppose
the user deletes your app on May 10, 2023 and then reinstalls
the app on May 15, 2023, and grants read permissions. The earliest date
your app can now read data from by default
is **April 15, 2023**.

## Handle exceptions

Health Connect throws standard exceptions for CRUD operations when an issue is
encountered. Your app should catch and handle each of these exceptions as
appropriate.

Each method on `HealthConnectClient` lists the exceptions that can be thrown.
In general, your app should handle the following exceptions:


<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

| **Exception** | **Description** | **Recommended best practice** |
|---|---|---|
| `IllegalStateException` | One of the following scenarios has occurred: <br /> - The Health Connect service isn't available. - The request isn't a valid construction. For example, an aggregate request in periodic buckets where an `Instant` object is used for the `timeRangeFilter`. <br /> | Handle possible issues with the inputs first before doing a request. Preferably, assign values to variables or use them as parameters within a custom function instead of using them directly in your requests so that you can apply error handling strategies. |
| `IOException` | There are issues encountered upon reading and writing data from disk. | To avoid this issue, here are some suggestions: <br /> - Back up any user input. - Be able to handle any issues that occur during bulk write operations. For example, make sure the process moves past the issue and carry out the remaining operations. - Apply retries and backoff strategies to handle request issues. <br /> |
| `RemoteException` | Errors have occurred within, or in communicating with, the underlying service to which the SDK connects. For example, your app is trying to delete a record with a given `uid`. However, the exception is thrown after the app finds out upon checking in the underlying service that the record doesn't exist. | To avoid this issue, here are some suggestions: <br /> - Perform regular syncs between your app's datastore and Health Connect. - Apply retries and backoff strategies to handle request issues. <br /> |
| `SecurityException` | There are issues encountered when the requests require permissions that aren't granted. | To avoid this, make sure that you've [declared use of Health Connect data types](https://developer.android.com/guide/health-and-fitness/health-connect/develop/frequently-asked-questions#declare-access) for your published app. Also, you must declare Health Connect permissions [in the manifest file](https://developer.android.com/guide/health-and-fitness/health-connect/develop/get-started#step-3) and [in your activity](https://developer.android.com/guide/health-and-fitness/health-connect/develop/get-started#step-4). <br /> <br /> |
[*Table 1: Health Connect exceptions and recommended best practices*]

<br />