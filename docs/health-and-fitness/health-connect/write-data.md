---
title: https://developer.android.com/health-and-fitness/health-connect/write-data
url: https://developer.android.com/health-and-fitness/health-connect/write-data
source: md.txt
---

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

This guide covers the process of writing or updating data in Health Connect.
| **Tip:** For more guidance on how to write data, take a look at the [Android Developer video for reading and writing data](https://www.youtube.com/watch?v=NAx7Gv_Hk7E) in Health Connect.

## Handle zero values

Some data types like steps, distance, or calories might have a value of `0`.
Only write zero values when it reflects true inactivity while the user was
wearing the device. Don't write zero values if the device wasn't worn, data is
missing, or the battery died. In such cases, omit the record to avoid misleading
data.

## Set up data structure

Before writing data, we need to set up the records first. For more than 50 data
types, each have their respective structures.
See the [Jetpack reference](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/package-summary#classes) for more details about the data
types available.

### Basic records

The [Steps](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord) data type in Health Connect captures the number of steps a
user has taken between readings. Step counts represent a common measurement
across health, fitness, and wellness platforms.

The following example shows how to set steps count data:  

    val endTime = Instant.now()
    val startTime = endTime.minus(Duration.ofMinutes(15))

    val stepsRecord = StepsRecord(
        count = 120,
        startTime = startTime,
        endTime = endTime,
        startZoneOffset = ZoneOffset.UTC,
        endZoneOffset = ZoneOffset.UTC,
        metadata = Metadata.autoRecorded(
            device = Device(type = Device.TYPE_WATCH)
        )
    )

| **Note:** Only write a zero value if the device was worn and no activity occurred. Don't write data if the device was off-body or the data is incomplete. For best practices on handling time zones, see the [Time zone handling](https://developer.android.com/health-and-fitness/health-connect/write-data#time-zone-handling) section.

### Records with units of measurement

Health Connect can store values along with their units of measurement to provide
accuracy. One example is the [Nutrition](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord) data type that is vast and
comprehensive. It includes a wide variety of optional nutrient fields ranging
from total carbohydrates to vitamins. Each data point represents the nutrients
that were potentially consumed as part of a meal or food item.

In this data type, all of the nutrients are represented in units of
[Mass](https://developer.android.com/reference/kotlin/androidx/health/connect/client/units/Mass), while `energy` is represented in a unit of [Energy](https://developer.android.com/reference/kotlin/androidx/health/connect/client/units/Energy).

The following example shows how to set nutrition data for a user who has
eaten a banana:  

    val endTime = Instant.now()
    val startTime = endTime.minus(Duration.ofMinutes(1))

    val banana = NutritionRecord(
        name = "banana",
        energy = 105.0.kilocalories,
        dietaryFiber = 3.1.grams,
        potassium = 0.422.grams,
        totalCarbohydrate = 27.0.grams,
        totalFat = 0.4.grams,
        saturatedFat = 0.1.grams,
        sodium = 0.001.grams,
        sugar = 14.0.grams,
        vitaminB6 = 0.0005.grams,
        vitaminC = 0.0103.grams,
        startTime = startTime,
        endTime = endTime,
        startZoneOffset = ZoneOffset.UTC,
        endZoneOffset = ZoneOffset.UTC,
        metadata = Metadata.manualEntry(
            device = Device(type = Device.TYPE_PHONE)
        )
    )

### Records with series data

Health Connect can store a list of series data. One example is the
[Heart Rate](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord) data type that captures a series of heartbeat samples
detected between readings.

In this data type, the parameter `samples` is represented by a list of
[Heart Rate samples](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord.Sample). Each sample contains a `beatsPerMinute`
value and a `time` value.

The following example shows how to set heart rate series data:  

    val endTime = Instant.now()
    val startTime = endTime.minus(Duration.ofMinutes(5))

    val heartRateRecord = HeartRateRecord(
        startTime = startTime,
        startZoneOffset = ZoneOffset.UTC,
        endTime = endTime,
        endZoneOffset = ZoneOffset.UTC,
        // records 10 arbitrary data, to replace with actual data
        samples = List(10) { index ->
            HeartRateRecord.Sample(
                time = startTime + Duration.ofSeconds(index.toLong()),
                beatsPerMinute = 100 + index.toLong(),
            )
        },
        metadata = Metadata.autoRecorded(
            device = Device(type = Device.TYPE_WATCH)
        ))

## Request permissions from the user

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.  

    // Create a set of permissions for required data types
    val PERMISSIONS =
        setOf(
      HealthPermission.getReadPermission(HeartRateRecord::class),
      HealthPermission.getWritePermission(HeartRateRecord::class),
      HealthPermission.getReadPermission(StepsRecord::class),
      HealthPermission.getWritePermission(StepsRecord::class)
    )

Use [`getGrantedPermissions`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#getGrantedPermissions()) to see if your app already has the
required permissions granted. If not, use
[`createRequestPermissionResultContract`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#createRequestPermissionResultContract(kotlin.String)) to request
those permissions. This displays the Health Connect permissions screen.  

    // Create the permissions launcher
    val requestPermissionActivityContract = PermissionController.createRequestPermissionResultContract()

    val requestPermissions = registerForActivityResult(requestPermissionActivityContract) { granted ->
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions successfully granted
      } else {
        // Lack of required permissions
      }
    }

    suspend fun checkPermissionsAndRun(healthConnectClient: HealthConnectClient) {
      val granted = healthConnectClient.permissionController.getGrantedPermissions()
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions already granted; proceed with inserting or reading data
      } else {
        requestPermissions.launch(PERMISSIONS)
      }
    }

Because users can grant or revoke permissions at any time, your app needs to
periodically check for granted permissions and handle scenarios where
permission is lost.

## Write data

One of the common workflows in Health Connect is writing data. To add records,
use [`insertRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#insertRecords(kotlin.collections.List)).

The following example shows how to write data inserting step counts:  

    suspend fun insertSteps(healthConnectClient: HealthConnectClient) {
        val endTime = Instant.now()
        val startTime = endTime.minus(Duration.ofMinutes(5))
        try {
            val stepsRecord = StepsRecord(
                count = 120,
                startTime = startTime,
                endTime = endTime,
                startZoneOffset = ZoneOffset.UTC,
                endZoneOffset = ZoneOffset.UTC,
                metadata = Metadata.autoRecorded(
                    device = Device(type = Device.TYPE_WATCH)
                )
            )
            healthConnectClient.insertRecords(listOf(stepsRecord))
        } catch (e: Exception) {
            // Run error handling here
        }
    }

## Update data

If you need to change one or more records, especially when you need to
[sync](https://developer.android.com/guide/health-and-fitness/health-connect/develop/sync-data) your app datastore with data from Health Connect, you can update
your data. There are two ways to update existing data which depends on the
identifier used to find records.

### Metadata

It is worth examining the `Metadata` class first as this is necessary when
updating data. On creation, each [`Record`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/Record) in Health Connect has a
[`metadata`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Metadata) field. The following properties are relevant to
synchronization:

| Properties | Description |
|---|---|
| `id` | Every `Record` in Health Connect has a unique `id` value. **Health Connect automatically populates this** **when inserting a new record.** |
| `lastModifiedTime` | Every `Record` also keeps track of the last time the record was modified. **Health Connect automatically populates this.** |
| `clientRecordId` | Each `Record` can have a unique ID associated with it to serve as reference in your app datastore. **Your app supplies this value.** |
| `clientRecordVersion` | Where a record has `clientRecordId`, the `clientRecordVersion` can be used to allow data to stay in sync with the version in your app datastore. **Your app supplies this value.** |

### Update after reading by time range

To update data, prepare the needed records first. Perform any changes to the
records if necessary. Then, call [`updateRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#updateRecords(kotlin.collections.List)) to make
the changes.

The following example shows how to update data. For this purpose, each record
has its zone offset values adjusted into PST.  

    suspend fun updateSteps(
        healthConnectClient: HealthConnectClient,
        prevRecordStartTime: Instant,
        prevRecordEndTime: Instant
    ) {
        try {
            val request = healthConnectClient.readRecords(
                ReadRecordsRequest(
                    recordType = StepsRecord::class, timeRangeFilter = TimeRangeFilter.between(
                        prevRecordStartTime, prevRecordEndTime
                    )
                )
            )

            val newStepsRecords = arrayListOf<StepsRecord>()
            for (record in request.records) {
                // Adjusted both offset values to reflect changes
                val sr = StepsRecord(
                    count = record.count,
                    startTime = record.startTime,
                    startZoneOffset = record.startTime.atZone(ZoneId.of("PST")).offset,
                    endTime = record.endTime,
                    endZoneOffset = record.endTime.atZone(ZoneId.of("PST")).offset,
                    metadata = record.metadata
                )
                newStepsRecords.add(sr)
            }

            healthConnectClient.updateRecords(newStepsRecords)
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Upsert through Client Record ID

If you are using the optional Client Record ID and Client Record Version values,
we recommend using [`insertRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#insertRecords(kotlin.collections.List)) instead of `updateRecords`.

The `insertRecords` function has the ability to upsert data.
If the data exists in Health Connect based on the given set of
Client Record IDs, it gets overwritten. Otherwise, it is written as new data.
This scenario is useful whenever you need to [sync](https://developer.android.com/guide/health-and-fitness/health-connect/develop/sync-data) data from
your app datastore to Health Connect.

The following example shows how to perform an upsert on data pulled from
the app datastore:  

    suspend fun pullStepsFromDatastore() : ArrayList<StepsRecord> {
        val appStepsRecords = arrayListOf<StepsRecord>()
        // Pull data from app datastore
        // ...
        // Make changes to data if necessary
        // ...
        // Store data in appStepsRecords
        // ...
        var sr = StepsRecord(
            metadata = Metadata.autoRecorded(
                clientRecordId = "Your client record ID",
                device = Device(type = Device.TYPE_WATCH)
            ),
            // Assign more parameters for this record
        )
        appStepsRecords.add(sr)
        // ...
        return appStepsRecords
    }

    suspend fun upsertSteps(
        healthConnectClient: HealthConnectClient,
        newStepsRecords: ArrayList<StepsRecord>
    ) {
        try {
            healthConnectClient.insertRecords(newStepsRecords)
        } catch (e: Exception) {
            // Run error handling here
        }
    }

After that, you can call these functions in your main thread.  

    upsertSteps(healthConnectClient, pullStepsFromDatastore())

#### Value check in Client Record Version

If your process of upserting data includes the Client Record Version, Health
Connect performs comparison checks in the [`clientRecordVersion`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Metadata#clientRecordVersion())
values. If the version from the inserted data is higher than the
version from the existing data, the upsert happens. Otherwise, the process
ignores the change and the value remains the same.

To include versioning in your data, you need to supply
`Metadata.clientRecordVersion` with a `Long` value based on your versioning
logic.  

    val endTime = Instant.now()
    val startTime = endTime.minus(Duration.ofMinutes(15))

    val stepsRecord = StepsRecord(
        count = 100L,
        startTime = startTime,
        startZoneOffset = ZoneOffset.UTC,
        endTime = endTime,
        endZoneOffset = ZoneOffset.UTC,
        metadata = Metadata.manualEntry(
            clientRecordId = "Your supplied record ID",
            clientRecordVersion = 0L, // Your supplied record version
            device = Device(type = Device.TYPE_WATCH)
        )
    )

Upserts don't automatically increment `version` whenever there are changes,
preventing any unexpected instances of overwriting data. With that, you have to
manually supply it with a higher value.

## General guidance

Your app should write all supported first-party data. Optionally, you can
choose to have your app write data obtained from third-party sources. However,
if your app has read data from Health Connect, that data shouldn't be
written back into Health Connect.

When writing data that has been imported or derived from another source, you
are expected to correctly attribute its origin and source device metadata.
To do this, you must supply the following metadata for each written record:

- **`recordingMethod`** : For automatically or manually recorded data, we expect the recording method to be updated to reflect the type of activity that has been recorded:
  - `RECORDING_METHOD_AUTOMATICALLY_RECORDED`: If the data was automatically recorded, for example, a fitness band automatically detected the user went for a run.
  - `RECORDING_METHOD_ACTIVELY_RECORDED`: If the user started a new activity, such as biking on their wearable.
  - `RECORDING_METHOD_MANUAL_ENTRY`: If the user entered the data manually.
- **`device.type`** : You are required to specify a device type from one of the supported `Device` types.
- **`device.manufacturer`**: The device's manufacturer, for example, "Fitbit".
- **`device.model`**: The device's model, for example, "Charge 3".

Setting metadata correctly is crucial for data transparency and helps
users understand where their health information comes from. For complete
details, refer to the Health Connect metadata guide.

If data in your app has been imported from another app, then the responsibility
falls onto the other app to write its own data to Health Connect.

It's also a good idea to implement logic that handles write exceptions such as
data being outside of bounds, or an internal system error. You can apply your
backoff and retry strategies on a job scheduling mechanism. If writing to
Health Connect is ultimately unsuccessful, make sure that your app can move past
that point of export. Don't forget to log and report errors to aid diagnosis.

When tracking data, there are a couple of suggestions you can
follow depending on the way your app writes data.

### Time zone handling

When writing time-based records, avoid setting offsets to **zoneOffset.UTC**
by default because this can lead to inaccurate timestamps when users are in
other zones. Instead, calculate the offset based on the device's actual
location. You can retrieve the device's time zone using
`ZoneId.systemDefault()`.  

    val endTime = Instant.now()
    val startTime = endTime.minus(java.time.Duration.ofDays(1))
    val stepsRecords = mutableListOf<StepsRecord>()
    var sampleTime = startTime
    val minutesBetweenSamples = 15L
    while (sampleTime < endTime) {
        // Get the default ZoneId then convert it to an offset
        val zoneOffset = ZoneOffset.systemDefault().rules.getOffset(sampleTime)
        stepsRecords += StepsRecord(
            startTime = sampleTime.minus(java.time.Duration.ofMinutes(minutesBetweenSamples)),
            startZoneOffset = zoneOffset,
            endTime = sampleTime,
            endZoneOffset = zoneOffset,
            count = Random.nextLong(1, 100),
            metadata = Metadata.unknownRecordingMethod(),
        )
        sampleTime = sampleTime.plus(java.time.Duration.ofMinutes(minutesBetweenSamples))
    }
    healthConnectClient.insertRecords(
        stepsRecords
    )

See the [documentation for `ZoneId`](https://developer.android.com/reference/kotlin/java/time/ZoneId) for more details.

### Write frequency and granularity

When writing data to Health Connect, use appropriate resolution. Using the
appropriate resolution helps reduce storage load, while still maintaining
consistent and accurate data. Data resolution encompasses two things:

- **Frequency of writes** : How often your application write any new data into Health Connect.
  - Write data as frequently as possible when new data is available, while being mindful of device performance.
  - To avoid negatively impacting battery life and other performance aspects, the maximum interval between writes should be 15 minutes.
- **Granularity of written data** : How often the data was sampled.
  - For example, write heart rate samples every 5 seconds.
  - Not every data type requires the same sample rate. There is little benefit to updating step count data every second, as opposed to a less frequent cadence such as every 60 seconds.
  - Higher sample rates may give users a more detailed and granular look at their health and fitness data. Sample rate frequencies should strike a balance between detail and performance.

| **Note:** If your app relies on data from devices that sync less frequently than 15 minutes, adjust your writes to match the device's sync interval. This avoid empty writes to Health Connect.

### Additional guidelines

Follow these guidelines when writing data:

- On every sync, only write new data and updated data that was modified since the last sync.
- Chunk requests to at most 1000 records per write request.
- Restrict tasks to run only when the device is idle and is not low on battery.
- For background tasks, use [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) to schedule periodic tasks, with a maximum time period of 15 minutes.

The following code uses WorkManager to schedule periodic background tasks, with
a maximum time period of 15 minutes, and a flex interval of 5 minutes. This
configuration is set using the
[`PeriodicWorkRequest.Builder`](https://developer.android.com/reference/kotlin/androidx/work/PeriodicWorkRequest.Builder#Builder(java.lang.Class,kotlin.Long,java.util.concurrent.TimeUnit,kotlin.Long,java.util.concurrent.TimeUnit)) class.  

    val constraints = Constraints.Builder()
        .requiresBatteryNotLow()
        .requiresDeviceIdle(true)
        .build()

    val writeDataWork = PeriodicWorkRequestBuilder<WriteDataToHealthConnectWorker>(
            15,
            TimeUnit.MINUTES,
            5,
            TimeUnit.MINUTES
        )
        .setConstraints(constraints)
        .build()

### Active tracking

This includes apps that perform event-based tracking such as exercise and sleep,
or manual user input such as nutrition. These records are created when the app
is in the foreground, or in rare events where it is used a few times in a day.

Verify that your app doesn't keep Health Connect running for the entire
duration of the event.

Data must be written to Health Connect in one of two ways:

- Sync data to Health Connect after the event is complete. For example, sync data when the user ends a tracked exercise session.
- Schedule a one-off task using [`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager) to sync data later.

## Best practices for granularity and frequency of writes

When writing data to Health Connect, use appropriate resolution. Using the
appropriate resolution helps reduce storage load, while still maintaining
consistent and accurate data. Data resolution encompasses 2 things:

1. **Frequency of writes**: how often your application pushes any new data into
   Health Connect. Write data as frequently as possible when new data is
   available, while being mindful of device performance. To avoid negatively
   impacting battery life and other performance aspects, the maximum interval
   between writes should be 15 minutes.

2. **Granularity of written data**: how often the data that is pushed in was
   sampled. For example, write heart rate samples every 5s. Not every data type
   requires the same sample rate. There is little benefit to updating step count
   data every second, as opposed to a less frequent cadence such as every 60
   seconds. However, higher sample rates may give users a more detailed and
   granular look at their health and fitness data. Sample rate frequencies
   should strike a balance between detail and performance.

### Structure records for series data

For data types that use a series of samples, such as `HeartRateRecord`, it's
important to structure your records correctly. Instead of creating a single,
day-long record that is constantly updated, you should create multiple smaller
records, each representing a specific time interval.

For example, for heart rate data, you should create a new `HeartRateRecord` for
each minute. Each record would have a start time and end time spanning that
minute, and would contain all the heart rate samples captured during that
minute.

During regular syncs with Health Connect (for example, every 15 minutes), your
app should write all the one-minute records that have been created since the
previous sync. This keeps records at a manageable size and improves the
performance of querying and processing data.

The following example shows how to create a `HeartRateRecord` for a single
minute, containing multiple samples:  

    val startTime = Instant.now().truncatedTo(ChronoUnit.MINUTES)
    val endTime = startTime.plus(Duration.ofMinutes(1))

    val heartRateRecord = HeartRateRecord(
        startTime = startTime,
        startZoneOffset = ZoneOffset.UTC,
        endTime = endTime,
        endZoneOffset = ZoneOffset.UTC,
        // Create a new record every minute, containing a list of samples.
        samples = listOf(
            HeartRateRecord.Sample(
                time = startTime + Duration.ofSeconds(15),
                beatsPerMinute = 80,
            ),
            HeartRateRecord.Sample(
                time = startTime + Duration.ofSeconds(30),
                beatsPerMinute = 82,
            ),
            HeartRateRecord.Sample(
                time = startTime + Duration.ofSeconds(45),
                beatsPerMinute = 85,
            )
        ),
        metadata = Metadata.autoRecorded(
            device = Device(type = Device.TYPE_WATCH)
        ))

### Write data monitored throughout the day

For data collected on an ongoing basis, like steps, your application should
write to Health Connect as frequently as possible when new data is available.
To avoid negatively impacting battery life and other performance aspects, the
maximum interval between writes should be 15 minutes.

|---|---|---|---|
| **Data type** | **Unit** | **Expected** | **Example** |
| Steps | steps | Every 1 minute | 23:14 - 23:15 - 5 steps 23:16 - 23:17 - 22 steps 23:17 - 23:18 - 8 steps |
| StepsCadence | steps/min | Every 1 minute | 23:14 - 23:15 - 5 spm 23:16 - 23:17 - 22 spm 23:17 - 23:18 - 8 spm |
| Wheelchair pushes | pushes | Every 1 minute | 23:14 - 23:15 - 5 pushes 23:16 - 23:17 - 22 pushes 23:17 - 23:18 - 8 pushes |
| ActiveCaloriesBurned | Calories | Every 15 minutes | 23:15 - 23:30 - 2 Calories 23:30 - 23:45 - 25 Calories 23:45 - 00:00 - 5 Calories |
| TotalCaloriesBurned | Calories | Every 15 minutes | 23:15 - 23:30 - 16 Calories 23:30 - 23:45 - 16 Calories 23:45 - 00:00 - 16 Calories |
| Distance | km/min | Every 1 minute | 23:14-23:15 - 0.008 km 23:16 - 23:16 - 0.021 km 23:17 - 23:18 - 0.012 km |
| ElevationGained | m | Every 1 minute | 20:36 - 20:37 - 3.048m 20:39 - 20:40 - 3.048m 23:23 - 23:24 - 9.144m |
| FloorsClimbed | floors | Every 1 minute | 23:14 - 23:15 - 5 floors 23:16 - 23:16 - 22 floors 23:17 - 23:18 - 8 floors |
| HeartRate | bpm | 4 times a minute | 6:11:15am - 55 bpm 6:11:30am - 56 bpm 6:11:45 am - 56 bpm 6:12:00 am - 55 bpm |
| HeartRateVariabilityRmssd | ms | Every 1 minute | 6:11am - 23 ms |
| RespiratoryRate | breaths/minute | Every 1 minute | 23:14 - 23:15 - 60 breaths/minute 23:16 - 23:16 - 62 breaths/minute 23:17 - 23:18 - 64 breaths/minute |
| OxygenSaturation | % | Every 1 hour | 6:11 - 95.208% |
[*Table 1: Guidance for writing data*]

| **Note:** As of version 1.1.0-rc01, **RecordingMethod** and **DeviceType** are mandatory requirements when writing data.

Data should be written to Health Connect at the end of the workout or sleep
session. For active tracking, such as exercise and sleep, or manual user input
like nutrition, these records are created when the app is in the foreground, or
in rare events where it is used a few times in a day.

Verify that your app doesn't keep Health Connect running for the entire duration
of the event.

Data must be written to Health Connect in one of two ways:

- Sync data to Health Connect after the event is complete. For example, sync data when the user ends a tracked exercise session.
- Schedule a one-off task using [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) to sync data later.

#### Exercise and sleep sessions

At minimum, your application should follow the guidance in the **Expected**
column in Table 2. Where possible, follow the guidance in the
**Best** column.

The following table shows how to write data during an exercise:

|---|---|---|---|---|
| **Data type** | **Unit** | **Expected** | **Best** | **Example** |
| Steps | steps | Every 1 minute | Every 1 second | 23:14-23:15 - 5 steps 23:16 - 23:17 - 22 steps 23:17 - 23:18 - 8 steps |
| StepsCadence | steps/min | Every 1 minute | Every 1 second | 23:14-23:15 - 35 spm 23:16 - 23:17 - 37 spm 23:17 - 23:18 - 40 spm |
| Wheelchair pushes | pushes | Every 1 minute | Every 1 second | 23:14-23:15 - 5 pushes 23:16 - 23:17 - 22 pushes 23:17 - 23:18 - 8 pushes |
| CyclingPedalingCadence | rpm | Every 1 minute | Every 1 second | 23:14-23:15 - 65 rpm 23:16 - 23:17 - 70 rpm 23:17 - 23:18 - 68 rpm |
| Power | watts | Every 1 minute | Every 1 second | 23:14-23:15 - 250 watts 23:16 - 23:17 - 255 watts 23:17 - 23:18 - 245 watts |
| Speed | km/min | Every 1 minute | Every 1 second | 23:14-23:15 - 0.3 km/min 23:16 - 23:17 - 0.4 km/min 23:17 - 23:18 -0.4 km/min |
| Distance | km/m | Every 1 minute | Every 1 second | 23:14-23:15 - 0.008 km 23:16 - 23:16 - 0.021 km 23:17 - 23:18 - 0.012 km |
| ActiveCaloriesBurned | Calories | Every 1 minute | Every 1 second | 23:14-23:15 - 20 Calories 23:16 - 23:17 - 20 Calories 23:17 - 23:18 - 25 Calories |
| TotalCaloriesBurned | Calories | Every 1 minute | Every 1 second | 23:14-23:15 - 36 Calories 23:16 - 23:17 - 36 Calories 23:17 - 23:18 - 41 Calories |
| ElevationGained | m | Every 1 minute | Every 1 second | 20:36 - 20:37 - 3.048m 20:39 - 20:40 - 3.048m 23:23 - 23:24 - 9.144m |
| ExerciseRoutes | lat/lng/alt | Every 3-5 seconds | Every 1 second |   |
| HeartRate | bpm | 4 times a minute | Every 1 second | 23:14-23:15 - 150 bpm |
[*Table 2: Guidance for writing data during an exercise session*]

Table 3 shows how to write data during or after a sleep session:

|---|---|---|---|
| **Data type** | **Unit** | **Expected samples** | **Example** |
| Sleep Staging | stage | Granular period of time per sleep stage | 23:46 - 23:50 - awake 23:50 - 23:56 - light sleep 23:56 - 00:16 - deep sleep |
| RestingHeartRate | bpm | Single daily value (expected first thing in the morning) | 6:11am - 60 bpm |
| OxygenSaturation | % | Single daily value (expected first thing in the morning) | 6:11 - 95.208% |
[*Table 3: Guidance for writing data during or after a sleep session*]

#### Multi-sport events

This approach uses existing data types and structures, and it verifies
compatibility with current Health Connect implementations and data readers.
This is a common approach taken by fitness platforms.
| **Note:** Health Connect doesn't automatically calculate the total duration of a multi-sport event. Data readers must calculate this by using the start time of the first activity and the end time of the last activity.

Additionally, individual sessions such as swimming, biking, and running aren't
inherently linked within Health Connect, and data readers must infer the
relationship between these sessions based on their time proximity.
Transitions between segments, such as from swimming to biking, aren't explicitly
represented.

The following example shows how to write data for a triathlon:  

    val swimStartTime = Instant.parse("2024-08-22T08:00:00Z")
    val swimEndTime = Instant.parse("2024-08-22T08:30:00Z")
    val bikeStartTime = Instant.parse("2024-08-22T08:40:00Z")
    val bikeEndTime = Instant.parse("2024-08-22T09:40:00Z")
    val runStartTime = Instant.parse("2024-08-22T09:50:00Z")
    val runEndTime = Instant.parse("2024-08-22T10:20:00Z")

    val swimSession = ExerciseSessionRecord(
        startTime = swimStartTime,
        endTime = swimEndTime,
        exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_SWIMMING_OPEN_WATER,
        metadata = Metadata.autoRecorded(
          device = Device(type = Device.TYPE_WATCH)
        )
    )

    val bikeSession = ExerciseSessionRecord(
        startTime = bikeStartTime,
        endTime = bikeEndTime,
        exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_BIKING,
        metadata = Metadata.autoRecorded(
          device = Device(type = Device.TYPE_WATCH)
        )
    )

    val runSession = ExerciseSessionRecord(
        startTime = runStartTime,
        endTime = runEndTime,
        exerciseType = ExerciseSessionRecord.EXERCISE_TYPE_RUNNING,
        metadata = Metadata.autoRecorded(
          device = Device(type = Device.TYPE_WATCH)
        )
    )

    healthConnectClient.insertRecords(listOf(swimSession, bikeSession, runSession))

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