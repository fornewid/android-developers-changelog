---
title: https://developer.android.com/health-and-fitness/health-connect/aggregate-data
url: https://developer.android.com/health-and-fitness/health-connect/aggregate-data
source: md.txt
---

Aggregating data in Health Connect includes basic aggregations or aggregating
data into buckets. The following workflows show you how to do both.
| **Tip:** For further guidance on aggregating data, take a look at the [Android
| Developer video for reading and writing data](https://www.youtube.com/watch?v=NAx7Gv_Hk7E&t=149) in Health Connect.

## Basic aggregation

To use basic aggregation on your data, use the [`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#aggregate(androidx.health.connect.client.request.AggregateRequest)) function
on your [`HealthConnectClient`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient) object. It accepts an
[`AggregateRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/AggregateRequest) object where you add the metric types
and the time range as its parameters. How basic aggregates are called depends on
the metric types used.

### Cumulative aggregation

Cumulative aggregation computes the total value.

The following example shows you how to aggregate data for a data type:

    suspend fun aggregateDistance(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(DistanceRecord.DISTANCE_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            // The result may be null if no data is available in the time range
            val distanceTotalInMeters = response[DistanceRecord.DISTANCE_TOTAL]?.inMeters ?: 0L
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Filter by data origin

You can also filter aggregate data by its origin. For example, only including
data written by a specific app.

The following example shows how to use `dataOriginFilter` and
[`AggregateRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/AggregateRequest) to aggregate steps from a specific app:

    suspend fun aggregateStepsFromSpecificApp(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant,
        appPackageName: String
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                    dataOriginFilter = setOf(DataOrigin(appPackageName))
                )
            )
            // The result may be null if no data is available in the time range
            val totalSteps = response[StepsRecord.COUNT_TOTAL] ?: 0L
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Statistical aggregation

Statistical aggregation computes the minimum, maximum, or average values of
records with samples.

The following example shows how to use statistical aggregation:

    suspend fun aggregateHeartRate(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response =
                healthConnectClient.aggregate(
                    AggregateRequest(
                        setOf(HeartRateRecord.BPM_MAX, HeartRateRecord.BPM_MIN),
                        timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                    )
                )
            // The result may be null if no data is available in the time range
            val minimumHeartRate = response[HeartRateRecord.BPM_MIN] ?: 0L
            val maximumHeartRate = response[HeartRateRecord.BPM_MAX] ?: 0L
        } catch (e: Exception) {
            // Run error handling here
        }
    }

## Buckets

Health Connect can also let you aggregate data into *buckets* . The two types of
buckets you can use include **duration** and **period**.

Once called, they return a list of buckets. Note that the list can be sparse, so
a bucket is not included in the list if it doesn't contain any data.

### Duration

In this case, aggregated data is split into buckets within a fixed length of
time, such as a minute or an hour. To aggregate data into buckets, use
[`aggregateGroupByDuration`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#aggregateGroupByDuration(androidx.health.connect.client.request.AggregateGroupByDurationRequest)). It accepts an
[`AggregateGroupByDurationRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/AggregateGroupByDurationRequest) object where you add the
metric types, the time range, and the [`Duration`](https://developer.android.com/reference/java/time/Duration) as parameters.
You can use pairs of [`Instant`](https://developer.android.com/reference/java/time/Instant) or
[`LocalDateTime`](https://developer.android.com/reference/java/time/LocalDateTime) objects for `startTime` and `endTime` in
`TimeRangeFilter`.

The following shows an example of aggregating steps into minute-long buckets:

    suspend fun aggregateStepsIntoMinutes(
        healthConnectClient: HealthConnectClient,
        startTime: LocalDateTime,
        endTime: LocalDateTime
    ) {
        try {
            val response =
                healthConnectClient.aggregateGroupByDuration(
                    AggregateGroupByDurationRequest(
                        metrics = setOf(StepsRecord.COUNT_TOTAL),
                        timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                        timeRangeSlicer = Duration.ofMinutes(1L)
                    )
                )
            for (durationResult in response) {
                // The result may be null if no data is available in the time range
                val totalSteps = durationResult.result[StepsRecord.COUNT_TOTAL] ?: 0L
            }
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Period

In this case, aggregated data is split into buckets within a date-based amount
of time, such as a week or a month. To aggregate data into buckets, use
[`aggregateGroupByPeriod`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#aggregateGroupByPeriod(androidx.health.connect.client.request.AggregateGroupByPeriodRequest)). It accepts an
[`AggregateGroupByPeriodRequest`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/request/AggregateGroupByPeriodRequest) object where you add the
metric types, the time range, and the [`Period`](https://developer.android.com/reference/java/time/Period) as parameters.

The following shows an example of aggregating steps into monthly buckets:

    suspend fun aggregateStepsIntoMonths(
        healthConnectClient: HealthConnectClient,
        startTime: LocalDateTime,
        endTime: LocalDateTime
    ) {
        try {
            val response =
                healthConnectClient.aggregateGroupByPeriod(
                    AggregateGroupByPeriodRequest(
                        metrics = setOf(StepsRecord.COUNT_TOTAL),
                        timeRangeFilter = TimeRangeFilter.between(startTime, endTime),
                        timeRangeSlicer = Period.ofMonths(1)
                    )
                )
            for (monthlyResult in response) {
                // The result may be null if no data is available in the time range
                val totalSteps = monthlyResult.result[StepsRecord.COUNT_TOTAL] ?: 0L
            }
        } catch (e: Exception) {
            // Run error handling here
        }
    }

| **Note:** When running bucket aggregates per period, make sure that the start and end times set are not using the [`Instant`](https://developer.android.com/reference/java/time/Instant) class. Otherwise, the app returns an `IllegalStateException`.

## Read restrictions

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

## Aggregate data affected by user-selected apps priorities

End users can set priority for the Sleep and Activity apps that they have
integrated with Health Connect. Only end users can alter these priority
lists. When you perform an aggregate read, the Aggregate API accounts for
any duplicate data and keeps only the data from the app with the highest
priority. Duplicate data could exist if the user has multiple apps writing
the same kind of data---such as the number of steps taken or the distance
covered---at the same time.
![Figure showing Reorder app priorities](https://developer.android.com/static/health-and-fitness/health-connect/images/reorder_apps_priorities.svg) **Figure 1**: Reorder app priorities

![Figure showing reorder app priorities](https://developer.android.com/static/health-and-fitness/health-connect/images/reorder_apps_priorities.svg)

For information on how end users can prioritize their apps,
see [Manage Health Connect data](https://support.google.com/android/answer/12990553).

The user can add or remove apps as well as change their priorities. A user might
want to remove an app that is writing duplicate data so that the data totals on
the Health Connect screen are identical to the app they have
given the highest priority. The data totals are updated in real time.

Even though the Aggregate API calculates Activity and Sleep apps' data by
deduping data according to how the user has
set priorities, you can still build your
own logic to calculate the data separately for each app writing that data.

Only the Activity and Sleep data types are deduped by Health Connect, and
the data totals shown are the values after the dedupe has been performed
by the Aggregate API. These totals show the most recent full day where
data exists for steps and distance. For other types of data, the
aggregated results combine all data of the type in Health Connect from all
apps which wrote the data.

## Background reads

You can request that your application run in the background and read data from
Health Connect. If you request the
[Background Read](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example)
permission, your user can grant your app access to read data in the background.

## Supported aggregate data types by record

This table lists all the supported aggregate data types by Health Connect
record.

<br />

| Record | Aggregate data type |
|---|---|
| [`ActiveCaloriesBurnedRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActiveCaloriesBurnedRecord) | [`ACTIVE_CALORIES_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActiveCaloriesBurnedRecord#ACTIVE_CALORIES_TOTAL()) |
| [`ActivityIntensityRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord) | [`DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord#DURATION_TOTAL()), [`INTENSITY_MINUTES_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord#INTENSITY_MINUTES_TOTAL()), [`MODERATE_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord#MODERATE_DURATION_TOTAL()), [`VIGOROUS_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord#VIGOROUS_DURATION_TOTAL()) |
| [`BasalMetabolicRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BasalMetabolicRateRecord) | [`BASAL_CALORIES_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BasalMetabolicRateRecord#BASAL_CALORIES_TOTAL()) |
| [`BloodPressureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord) | [`DIASTOLIC_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#DIASTOLIC_AVG()), [`DIASTOLIC_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#DIASTOLIC_MAX()), [`DIASTOLIC_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#DIASTOLIC_MIN()), [`SYSTOLIC_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#SYSTOLIC_AVG()), [`SYSTOLIC_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#SYSTOLIC_MAX()), [`SYSTOLIC_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord#SYSTOLIC_MIN()) |
| [`CyclingPedalingCadenceRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CyclingPedalingCadenceRecord) | [`RPM_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CyclingPedalingCadenceRecord#RPM_AVG()), [`RPM_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CyclingPedalingCadenceRecord#RPM_MAX()), [`RPM_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CyclingPedalingCadenceRecord#RPM_MIN()) |
| [`DistanceRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/DistanceRecord) | [`DISTANCE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/DistanceRecord#DISTANCE_TOTAL()) |
| [`ElevationGainedRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ElevationGainedRecord) | [`ELEVATION_GAINED_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ElevationGainedRecord#ELEVATION_GAINED_TOTAL()) |
| [`ExerciseSessionRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSessionRecord) | [`EXERCISE_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSessionRecord#EXERCISE_DURATION_TOTAL()) |
| [`FloorsClimbedRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/FloorsClimbedRecord) | [`FLOORS_CLIMBED_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/FloorsClimbedRecord#FLOORS_CLIMBED_TOTAL()) |
| [`HeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord) | [`BPM_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord#BPM_AVG()), [`BPM_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord#BPM_MAX()), [`BPM_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord#BPM_MIN()), [`MEASUREMENTS_COUNT`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord#MEASUREMENTS_COUNT()) |
| [`HeightRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeightRecord) | [`HEIGHT_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeightRecord#HEIGHT_AVG()), [`HEIGHT_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeightRecord#HEIGHT_MAX()), [`HEIGHT_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeightRecord#HEIGHT_MIN()) |
| [`HydrationRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HydrationRecord) | [`VOLUME_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HydrationRecord#VOLUME_TOTAL()) |
| [`MindfulnessSessionRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MindfulnessSessionRecord) | [`MINDFULNESS_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MindfulnessSessionRecord#MINDFULNESS_DURATION_TOTAL()) |
| [`NutritionRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord) | [`BIOTIN_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#BIOTIN_TOTAL()), [`CAFFEINE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#CAFFEINE_TOTAL()), [`CALCIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#CALCIUM_TOTAL()), [`CHLORIDE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#CHLORIDE_TOTAL()), [`CHOLESTEROL_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#CHOLESTEROL_TOTAL()), [`CHROMIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#CHROMIUM_TOTAL()), [`COPPER_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#COPPER_TOTAL()), [`DIETARY_FIBER_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#DIETARY_FIBER_TOTAL()), [`ENERGY_FROM_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#ENERGY_FROM_FAT_TOTAL()), [`ENERGY_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#ENERGY_TOTAL()), [`FOLATE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#FOLATE_TOTAL()), [`FOLIC_ACID_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#FOLIC_ACID_TOTAL()), [`IODINE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#IODINE_TOTAL()), [`IRON_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#IRON_TOTAL()), [`MAGNESIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#MAGNESIUM_TOTAL()), [`MANGANESE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#MANGANESE_TOTAL()), [`MOLYBDENUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#MOLYBDENUM_TOTAL()), [`MONOUNSATURATED_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#MONOUNSATURATED_FAT_TOTAL()), [`NIACIN_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#NIACIN_TOTAL()), [`PANTOTHENIC_ACID_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#PANTOTHENIC_ACID_TOTAL()), [`PHOSPHORUS_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#PHOSPHORUS_TOTAL()), [`POLYUNSATURATED_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#POLYUNSATURATED_FAT_TOTAL()), [`POTASSIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#POTASSIUM_TOTAL()), [`PROTEIN_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#PROTEIN_TOTAL()), [`RIBOFLAVIN_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#RIBOFLAVIN_TOTAL()), [`SATURATED_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#SATURATED_FAT_TOTAL()), [`SELENIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#SELENIUM_TOTAL()), [`SODIUM_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#SODIUM_TOTAL()), [`SUGAR_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#SUGAR_TOTAL()), [`THIAMIN_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#THIAMIN_TOTAL()), [`TOTAL_CARBOHYDRATE_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#TOTAL_CARBOHYDRATE_TOTAL()), [`TOTAL_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#TOTAL_FAT_TOTAL()), [`TRANS_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#TRANS_FAT_TOTAL()), [`UNSATURATED_FAT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#UNSATURATED_FAT_TOTAL()), [`VITAMIN_A_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_A_TOTAL()), [`VITAMIN_B12_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_B12_TOTAL()), [`VITAMIN_B6_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_B6_TOTAL()), [`VITAMIN_C_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_C_TOTAL()), [`VITAMIN_D_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_D_TOTAL()), [`VITAMIN_E_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_E_TOTAL()), [`VITAMIN_K_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#VITAMIN_K_TOTAL()), [`ZINC_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord#ZINC_TOTAL()) |
| [`PowerRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PowerRecord) | [`POWER_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PowerRecord#POWER_AVG()), [`POWER_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PowerRecord#POWER_MAX()), [`POWER_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PowerRecord#POWER_MIN()) |
| [`RestingHeartRateRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord) | [`BPM_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord#BPM_AVG()), [`BPM_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord#BPM_MAX()), [`BPM_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord#BPM_MIN()) |
| [`SkinTemperatureRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord) | [`TEMPERATURE_DELTA_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_AVG()), [`TEMPERATURE_DELTA_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_MAX()), [`TEMPERATURE_DELTA_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord#TEMPERATURE_DELTA_MIN()) |
| [`SleepSessionRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SleepSessionRecord) | [`SLEEP_DURATION_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SleepSessionRecord#SLEEP_DURATION_TOTAL()) |
| [`SpeedRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SpeedRecord) | [`SPEED_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SpeedRecord#SPEED_AVG()), [`SPEED_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SpeedRecord#SPEED_MAX()), [`SPEED_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SpeedRecord#SPEED_MIN()) |
| [`StepsRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord) | [`COUNT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord#COUNT_TOTAL()) |
| [`StepsCadenceRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord) | [`RATE_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_AVG()), [`RATE_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_MAX()), [`RATE_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord#RATE_MIN()) |
| [`TotalCaloriesBurnedRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/TotalCaloriesBurnedRecord) | [`ENERGY_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/TotalCaloriesBurnedRecord#ENERGY_TOTAL()) |
| [`WeightRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WeightRecord) | [`WEIGHT_AVG`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WeightRecord#WEIGHT_AVG()), [`WEIGHT_MAX`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WeightRecord#WEIGHT_MAX()), [`WEIGHT_MIN`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WeightRecord#WEIGHT_MIN()) |
| [`WheelchairPushesRecord`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WheelchairPushesRecord) | [`COUNT_TOTAL`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WheelchairPushesRecord#COUNT_TOTAL()) |
[*Table: Supported aggregate data types by record*]

<br />