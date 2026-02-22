---
title: https://developer.android.com/health-and-fitness/recording-api
url: https://developer.android.com/health-and-fitness/recording-api
source: md.txt
---

The Recording API on mobile allows your app to record fitness data from a mobile
device in a battery-efficient way. For example, use this API to record steps,
similar to a pedometer retrieving step count data. This API is accountless,
meaning it does not require a Google Account to use the service, and data is
stored on-device.

If your app needs to read other health and fitness data from various sources in
addition to on-device steps, integrating with [Health Connect](https://developer.android.com/health-and-fitness/health-connect) is a
better option. Health Connect also provides access to [on-device steps](https://developer.android.com/health-and-fitness/health-connect/features/steps)
natively on Android 14 (API level 34) and higher.
| **Note:** The Recording API on mobile is a replacement for the Google Fit Android API, which is being deprecated.

This guide shows you how to use the Recording API on mobile in your health \&
fitness experiences.

See the [Recording API on mobile sample](https://github.com/android/health-samples/tree/main/recording-api-on-mobile/RecordingApiOnMobileSample) on GitHub for an
example.

## Notable details

There are several notable features unique to the Recording API on mobile:

- Once the recording subscription starts or is renewed, data since the latest subscription - for up to 10 days - is accessible.
- Data is only available when there is an active subscription. If a subscription is removed by calling `unsubscribe`, collected data won't be accessible.

## Data types

The Recording API on mobile can record the following data types:

- [`TYPE_STEP_COUNT_DELTA`](https://developers.google.com/android/reference/com/google/android/gms/fitness/data/LocalDataType#TYPE_STEP_COUNT_DELTA)
- [`TYPE_DISTANCE_DELTA`](https://developers.google.com/android/reference/com/google/android/gms/fitness/data/LocalDataType#TYPE_DISTANCE_DELTA)
- [`TYPE_CALORIES_EXPENDED`](https://developers.google.com/android/reference/com/google/android/gms/fitness/data/LocalDataType#TYPE_CALORIES_EXPENDED)

## Get Started

To get started, add the following dependency in your `build.gradle` file:  

### Kotlin DSL

    plugin {
      id("com.android.application")
    }

    ...

    dependencies {
      implementation("com.google.android.gms:play-services-fitness:21.2.0")
    }

### Groovy DSL

    apply plugin: 'com.android.application'

    ...

    dependencies {
      implementation 'com.google.android.gms:play-services-fitness:21.2.0'
    }

### Request permissions

To record data using the Recording API on mobile, your app will need to [request
the following permission](https://developer.android.com/training/permissions/requesting#workflow_for_requesting_permissions):

- `android.permission.ACTIVITY_RECOGNITION`

## Perform a Play Services version check

To use the Recording API on mobile, the user must have Google Play services
updated to `LOCAL_RECORDING_CLIENT_MIN_VERSION_CODE`. You can check for this
using the [`isGooglePlayServicesAvailable`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability#public-int-isgoogleplayservicesavailable-context-context,-int-minapkversion) method:  

    val hasMinPlayServices = isGooglePlayServicesAvailable(context, LocalRecordingClient.LOCAL_RECORDING_CLIENT_MIN_VERSION_CODE)

    if(hasMinPlayServices != ConnectionResult.SUCCESS) {
      // Prompt user to update their device's Google Play services app and return
    }

    // Continue with Recording API functions

Otherwise, if the user's Google Play services version is too low, the system
throws a [`ConnectionResult.SERVICE_VERSION_UPDATE_REQUIRED`](https://developers.google.com/android/reference/com/google/android/gms/common/ConnectionResult#SERVICE_VERSION_UPDATE_REQUIRED)
exception.

## Subscribe to Fitness Data

To request background collection of steps data, use the
`subscribe` method, as shown in the following code snippet:  

    val localRecordingClient = FitnessLocal.getLocalRecordingClient(this)
    // Subscribe to steps data
    localRecordingClient.subscribe(LocalDataType.TYPE_STEP_COUNT_DELTA)
      .addOnSuccessListener {
        Log.i(TAG, "Successfully subscribed!")
      }
      .addOnFailureListener { e ->
        Log.w(TAG, "There was a problem subscribing.", e)
      }

## Read and Process Fitness Data

Once subscribed, request the data using the `readData` method. Then, you can
obtain LocalDataPoints from the resulting [`LocalDataSet`](https://developers.google.com/android/reference/com/google/android/gms/fitness/data/LocalDataSet) by
making a [`LocalDataReadRequest`](https://developers.google.com/android/reference/com/google/android/gms/fitness/request/LocalDataReadRequest), as shown in the following code
snippet:  

    val endTime = LocalDateTime.now().atZone(ZoneId.systemDefault())
    val startTime = endTime.minusWeeks(1)
    val readRequest =
      LocalDataReadRequest.Builder()
        // The data request can specify multiple data types to return,
        // effectively combining multiple data queries into one call.
        // This example demonstrates aggregating only one data type.
        .aggregate(LocalDataType.TYPE_STEP_COUNT_DELTA)
        // Analogous to a "Group By" in SQL, defines how data should be
        // aggregated. bucketByTime allows bucketing by time span.
        .bucketByTime(1, TimeUnit.DAYS)
        .setTimeRange(startTime.toEpochSecond(), endTime.toEpochSecond(), TimeUnit.SECONDS)
        .build()

      localRecordingClient.readData(readRequest).addOnSuccessListener { response ->
        // The aggregate query puts datasets into buckets, so flatten into a
        // single list of datasets.
        for (dataSet in response.buckets.flatMap { it.dataSets }) {
          dumpDataSet(dataSet)
        }
      }
      .addOnFailureListener { e ->
        Log.w(TAG,"There was an error reading data", e)
      }

    fun dumpDataSet(dataSet: LocalDataSet) {
      Log.i(TAG, "Data returned for Data type: ${dataSet.dataType.name}")
      for (dp in dataSet.dataPoints) {
        Log.i(TAG,"Data point:")
        Log.i(TAG,"\tType: ${dp.dataType.name}")
        Log.i(TAG,"\tStart: ${dp.getStartTime(TimeUnit.HOURS)}")
        Log.i(TAG,"\tEnd: ${dp.getEndTime(TimeUnit.HOURS)}")
        for (field in dp.dataType.fields) {
          Log.i(TAG,"\tLocalField: ${field.name.toString()} LocalValue: ${dp.getValue(field)}")
        }
      }
    }

The `LocalRecordingClient` continuously updates its collection of data. You can
use `readData` to pull the latest numbers at any time.

Note that the `LocalRecordingClient` stores up to 10 days of data. To reduce the
risk of losing data, you can use WorkManager to periodically collect the data in
the background.

## Unsubscribe from fitness data

In order to free up resources, you should make sure to unsubscribe from the
collection of sensor data when your app is no longer in need of it. To
unsubscribe, use the `unsubscribe` method:  

    val localRecordingClient = FitnessLocal.getLocalRecordingClient(this)
    // Unsubscribe from steps data
    localRecordingClient.unsubscribe(LocalDataType.TYPE_STEP_COUNT_DELTA)
      .addOnSuccessListener {
        Log.i(TAG, "Successfully unsubscribed!")
      }
      .addOnFailureListener { e ->
        Log.w(TAG, "There was a problem unsubscribing.", e)
      }