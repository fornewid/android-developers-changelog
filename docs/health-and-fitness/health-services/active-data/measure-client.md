---
title: Take spot health measurements with MeasureClient  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-services/active-data/measure-client
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Fitness Guides](https://developer.android.com/health-and-fitness/fitness)

# Take spot health measurements with MeasureClient Stay organized with collections Save and categorize content based on your preferences.




With the
[`MeasureClient`](/reference/kotlin/androidx/health/services/client/MeasureClient)
API, your app registers callbacks to receive data for a short amount of time.
This is meant for situations in which your app is in use and requires rapid data
updates. If possible, create this with a foreground UI so that the user is
aware.

**Note:** `MeasureClient` is not suitable for workout tracking. Instead,
[record an exercise](/training/wearables/health-services/active-data/exercise-client) using `ExerciseClient`.

## Add dependencies

To add a dependency on Health Services, you must add the Google Maven repository
to your project. For more information, see
[Google's Maven repository](/studio/build/dependencies#google-maven).

Then, in your module-level `build.gradle` file, add the following dependency:

### Groovy

```
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-rc01"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-rc01")
}
```

**Note:** This API is asynchronous and relies on `ListenableFuture` extensively. See
[Using a ListenableFuture](/guide/background/listenablefuture) for more
information about this concept.

## Check capabilities

Before registering for data updates, check that the device can provide the type
of data your app needs. By checking capabilities first, you can enable or
disable certain features or modify your app's UI to compensate for capabilities
that are not available.

The following example shows how to check whether a device can provide the
`HEART_RATE_BPM` data type:

```
val healthClient = HealthServices.getClient(this /*context*/)
val measureClient = healthClient.measureClient
lifecycleScope.launch {
    val capabilities = measureClient.getCapabilitiesAsync().await()
    supportsHeartRate = DataType.HEART_RATE_BPM in capabilities.supportedDataTypesMeasure
}
```

## Register for data

**Note:** Request necessary permissions before registering to receive data that
requires a permission.

Each callback you register is for a single data type. Note that some data types
might have varying states of availability. For example, heart rate data might
not be available when the device is not properly attached to the wrist.

It's important to minimize the amount of time that your callback is registered,
as callbacks cause an increase in sensor sampling rates, which in turn increases
power consumption.

The following example shows how to register and unregister a callback to receive
`HEART_RATE_BPM` data:

```
val heartRateCallback = object : MeasureCallback {
    override fun onAvailabilityChanged(dataType: DeltaDataType<*, *>, availability: Availability) {
        if (availability is DataTypeAvailability) {
            // Handle availability change.
        }
    }

    override fun onDataReceived(data: DataPointContainer) {
        // Inspect data points.
    }
}
val healthClient = HealthServices.getClient(this /*context*/)
val measureClient = healthClient.measureClient

// Register the callback.
measureClient.registerMeasureCallback(DataType.Companion.HEART_RATE_BPM, heartRateCallback)

// Unregister the callback.
awaitClose {
    runBlocking {
        measureClient.unregisterMeasureCallbackAsync(DataType.Companion.HEART_RATE_BPM, heartRateCallback)
    }
}
```

**Note:** Kotlin developers can use `callbackFlow` to take advantage of coroutines
and lifecycle. See the
[Measure Data sample](https://github.com/android/health-samples/tree/main/health-services/MeasureDataCompose)
on GitHub for an example.