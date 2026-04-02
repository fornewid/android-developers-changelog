---
title: https://developer.android.com/health-and-fitness/health-services/health-platform
url: https://developer.android.com/health-and-fitness/health-services/health-platform
source: md.txt
---

| **Note:** The Health Platform API Version 1 is deprecated as of May 11, 2022. It has been replaced with Health Connect. Health Connect is an API and platform that unifies data from multiple devices and apps, including Samsung Health, into a single ecosystem. It also provides a single interface for reading and writing a user's health and fitness data. See the [Health Connect documentation](https://developer.android.com/guide/health-and-fitness/health-connect) to learn about the platform. See [Get started](https://developer.android.com/guide/health-and-fitness/health-connect/get-started) to integrate with the API.

Health Platform API is an Android API that provides developers with a single
interface for reading, writing, and sharing a user's historic health, wellness,
and fitness data. With Health Platform, users have control of their data. Users
control which apps have read or write access to different types of data. Health
Platform API data types include height, heart rate, and more.

The Health Platform API gives users a storage and sharing mechanism that lets
them select which apps can access and display their personal health, fitness,
and wellness data. This then lets app developers show users a more complete
view of users' health and lets users more effectively monitor their data.

The Health Platform API software developer kit gives Android app developers
everything they need to provide access to a user's health and wellness data on
select Samsung devices, and it lets apps perform bulk operations
such as inserting, deleting, and reading data.
| **Note:** See the [Health Platform sample](https://github.com/android/health-samples/tree/main/health-platform-v1/HealthPlatformSample) on GitHub for a complete example of using the Health Platform API.

## Get started

When using Health Platform, keep the following things in mind:

- Client apps must obtain granular permissions for read or write access from the user.
- The user can deny permissions or revoke permissions at any point afterward.
- Health Platform API supports only select Samsung devices.
- `HealthDataClient` is the client for Health Platform and an entry point to the Health Platform.

The following image shows the necessary integration steps developers must
follow:
![Integration steps, including SDK setup, access and permissions, and CRUD operations.](https://developer.android.com/static/wear/images/HPv1_integration.png) **Figure 1.** Health Platform integration steps.

### Release files

The Health Platform V1 release contains the following:

- [**Client SDK**](https://maven.google.com/web/index.html?q=health#com.google.android.libraries.healthdata:health-data-api:1.0.0-alpha01): Include this SDK in your application to use the Health Platform API. The SDK is a Maven repository you can directly include in your application Gradle build files.

### Install Health Platform

Install Health Platform using the following steps:

In the app's root `build.gradle` file, add the repository, as shown in the
following example:  

    allprojects {
        . . .
        repositories {
            . . .
            google()
        }
    }

Add a dependency on the Health Platform SDK in your module's `build.gradle`
file, as shown in the following example:  

### Kotlin


dependencies {
. . .
implementation("com.google.android.libraries.healthdata:health-data-api:1.0.0-alpha01")
}

### Groovy


dependencies {
. . .
implementation 'com.google.android.libraries.healthdata:health-data-api:1.0.0-alpha01'
}

## Data

Health Platform stores and structures health and fitness data. It also considers
core differences between how data of different types is measured. For example, a
heart rate measurement is taken immediately, but a step count is taken over a
period of time.

Here's a look at the central objects in Health Platform and how they differ:

- **`RawData`:** a measurement and data record.
- **`DataType`:** a specifier for common types of health and fitness data, such as heart rate, body fat, or body temperature, and their formats, such as fields, read-only, or optional.
- **`SampleData`:** a `RawData` object that is an instantaneous measurement, such as heart rate, blood pressure, or running speed.
- **`IntervalData`:** a `RawData` object that is a cumulative measurement taken over a period of time, such as number of steps taken, distance traveled, or calories burned.
- **`SeriesData`:** a `RawData` object that encapsulates a sequence of measurements over a period of time. `SeriesData` is particularly suited for high-frequency sensor data, such as continuous heart rate samples during an activity session.

Each of the three `RawData` classes corresponds to a specific subclass of
`DataType`: `SampleData`, `IntervalData`, and `SeriesData` correspond to
`SampleDataType`, `IntervalDataType`, and `SeriesDataType`, respectively.

Each `RawData` object is assigned a unique identifier (UID) by the Health
Platform when inserted. You can use this UID to reference a specific `RawData`
object in read, update, or delete requests.

### Data types

Health Platform includes a wide set of data types that are commonly used across
health and fitness apps. Data stored with the available data types provides
users with a comprehensive view of their historical health, fitness, and
wellness data, giving insight into their daily activities.

Each data type is defined by its data format, which includes the following:

- **Fields:** specific or generic fields associated with the data type. For example, the blood oxygen saturation (SpO2) data type has fields like Title, Notes, and Percentage.
- **Type:** long, double, string, or enum.
- **Attribute:** read-only, required, optional, or validation range.

### List of data types

Make the most of Health Platform by understanding the available data types.
Health Platform supports the data types shown in the following table.
The data types are organized according to their format: sample, interval, or
series.

#### `SampleData` types:

|---|---|---|
| `DataType.BasalMetabolicRateDataType` | `BASAL_METABOLIC_RATE` | Required |
| `DataType.BloodGlucoseDataType` | `BLOOD_GLUCOSE` | Required and Optional |
| `DataType.BloodPressureDataType` | `BLOOD_PRESSURE` | Required and Optional |
| `DataType.BodyFatDataType` | `BODY_FAT` | Required |
| `DataType.BodyTemperatureDataType` | `BODY_TEMPERATURE` | Required and Optional |
| `DataType.BoneMassDataType` | `BONE_MASS` | Required |
| `DataType.CervicalMucusDataType` | `CERVICAL_MUCUS` | Optional |
| `DataType.CervicalPositionDataType` | `CERVICAL_POSITION` | Optional |
| `DataType.CyclingPedalingCadenceDataType` | `CYCLING_PEDALING_CADENCE` | Required |
| `DataType.DateOfBirthDataType` | `DATE_OF_BIRTH` | Read Only |
| `DataType.GenderDataType` | `GENDER` | Read Only |
| `DataType.HeartRateDataType` | `HEART_RATE` | Required |
| `DataType.HeightDataType` | `HEIGHT` | Required |
| `DataType.HipCircumferenceDataType` | `HIP_CIRCUMFERENCE` | Required |
| `DataType.HrvDifferentialIndexDataType` | `HRV_DIFFERENTIAL_INDEX` | Required |
| `DataType.HrvRmssdDataType` | `HRV_RMSSD` | Required |
| `DataType.HrvSDataType` | `HRV_S` | Required |
| `DataType.HrvSd2DataType` | `HRV_SD2` | Required |
| `DataType.HrvSdannDataType` | `HRV_SDANN` | Required |
| `DataType.HrvSdnnDataType` | `HRV_SDNN` | Required |
| `DataType.HrvSdnnIndexDataType` | `HRV_SDNN_INDEX` | Required |
| `DataType.HrvSdnnIndexDataType` | `HRV_SDNN_INDEX` | Required |
| `DataType.HrvSdsdDataType` | `HRV_SDSD` | Required |
| `DataType.HrvTinnDataType` | `HRV_TINN` | Required |
| `DataType.LeanBodyMassDataType` | `LEAN_BODY_MASS` | Required |
| `DataType.LocationDataType` | `LOCATION` | Required |
| `DataType.MenstruationDataType` | `MENSTRUATION` | Optional |
| `DataType.OvulationTestDataType` | `OVULATION_TEST` | Required |
| `DataType.OxygenSaturationDataType` | `OXYGEN_SATURATION` | Required |
| `DataType.PaceDataType` | `PACE` | Required |
| `DataType.PowerDataType` | `POWER` | Required |
| `DataType.RespiratoryRateDataType` | `RESPIRATORY_RATE` | Required |
| `DataType.RestingHeartRateDataType` | `RESTING_HEART_RATE` | Required |
| `DataType.SexualActivityDataType` | `SEXUAL_ACTIVITY` | Required |
| `DataType.SpeedDataType` | `SPEED` | Required |
| `DataType.StepsCadenceDataType` | `STEPS_CADENCE` | Required |
| `DataType.Vo2MaxDataType` | `VO2_MAX` | Required and Optional |
| `DataType.WaistCircumferenceDataType` | `WAIST_CIRCUMFERENCE` | Required |
| `DataType.WeightDataType` | `WEIGHT` | Required |
[*Table 1: Health Platform `SampleData` types*]

#### `IntervalData` types:

|---|---|---|
| `DataType.ActiveEnergyDataType` | `ACTIVE_ENERGY_BURNED` | Required |
| `DataType.ActiveTimeDataType` | `ACTIVE_TIME` | Read Only |
| `DataType.ActivityEventDataType` | `ACTIVITY_EVENT` | Required |
| `DataType.ActivityLapDataType` | `ACTIVITY_LAP` | Optional |
| `DataType.ActivitySessionDataType` | `ACTIVITY_SESSION` | Required |
| `DataType.BasalEnergyDataType` | `BASAL_ENERGY_BURNED` | Read Only |
| `DataType.DistanceDataType` | `DISTANCE` | Required |
| `DataType.ElevationGainedDataType` | `ELEVATION_GAINED` | Required |
| `DataType.FloorsClimbedDataType` | `FLOORS_CLIMBED` | Required |
| `DataType.HydrationDataType` | `HYDRATION` | Required |
| `DataType.NutritionDataType` | `NUTRITION` | Optional |
| `DataType.RepetitionsDataType` | `REPETITIONS` | Required |
| `DataType.SleepSessionDataType` | `SLEEP_SESSION` | Optional |
| `DataType.SleepStageDataType` | `SLEEP_STAGE` | Required |
| `DataType.StepsDataType` | `STEPS` | Required |
| `DataType.SwimmingStrokesDataType` | `SWIMMING_STROKES` | Required and Optional |
| `DataType.TotalEnergyDataType` | `TOTAL_ENERGY_BURNED` | Read Only |

#### `SeriesData` types:

|---|---|---|
| `DataType.CyclingPedalingCadenceSeriesDataType` | `CYCLING_PEDALING_CADENCE` | Required |
| `DataType.HeartRateSeriesDataType` | `HEART_RATE` | Required |
| `DataType.LocationSeriesDataType` | `LOCATION` | Required |
| `DataType.PaceSeriesDataType` | `PACE` | Required |
| `DataType.PowerSeriesDataType` | `POWER` | Required |
| `DataType.SpeedSeriesDataType` | `SPEED` | Required |
| `DataType.StepsCadenceSeriesDataType` | `STEPS_CADENCE` | Required |
[*Table 3: Health Platform `SeriesData` types*]

| **Note:** `SeriesData` types are a subset of `SampleData` types. These data types can be written either as `SampleData` or `SeriesData`. For performance and storage optimization, we strongly recommend that high-frequency data, such as a continuous sensor stream, be written using `SeriesData`.

## Developer functions

The following describes the set of standard data functions available within
Health Platform. The platform provides standard insert, update, and delete
functions for raw data.

### Read AggregatedData

The platform lets clients apply an aggregation function over the following types
of `AggregatedData`:

- **`StatisticalData`:** the average, minimum, or maximum values in a set of `SampleData` or `SeriesData`, such as the minimum and maximum heart rate during an activity session.
- **`CumulativeData`:** the sum of `IntervalData` values, such as the total step count within a daily interval.
- **`CountData`:** a count of the number of underlying `RawData` objects, such as the number of activity sessions in a given week. Count data can be computed for sample, interval, and series data types.

## Connect to the Health Platform API

`HealthDataClient` is the entry point to the Health Platform API.

The following steps describe how to connect to Health Platform:

1. Use `HealthDataService.getClient` to create new `HealthDataClient` instances.
2. The client app must then request permission from the user using the `requestPermissions (Set)` method.

| **Note:** Only Samsung devices with Android SDK version 26 or higher are supported.

`HealthDataClient` automatically manages its connection to the underlying
storage layer and handles all Inter-Process Communication (IPC) and
serialization of outgoing requests and incoming responses.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Active data and exercises](https://developer.android.com/training/wearables/health-services/active)
- [Passive data updates](https://developer.android.com/training/wearables/health-services/passive)
- [Use Jetpack Compose on Wear OS](https://developer.android.com/training/wearables/compose)