---
title: https://developer.android.com/develop/sensors-and-location/location/retrieve-current
url: https://developer.android.com/develop/sensors-and-location/location/retrieve-current
source: md.txt
---

Using the Google Play services location APIs, your app can request the last
known location of the user's device. In most cases, you are interested in the
user's current location, which is usually equivalent to the last known
location of the device.

Specifically, use the
[fused
location provider](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html) to retrieve the device's last known location. The fused
location provider is one of the location APIs in Google Play services. It
manages the underlying location technology and provides a simple API so that
you can specify requirements at a high level, like high accuracy or low power.
It also optimizes the device's use of battery power.  
**Note:** When your app is running in the background,
[access to location](https://developer.android.com/training/location/background) should be
critical to the core functionality of the app and is accompanied with proper
disclosure to users.

This lesson shows you how to make a single request for the location of a
device using the
[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())
method in the fused location provider.

## Set up Google Play services

To access the fused location provider, your app's development project must
include Google Play services. Download and install the Google Play services
component via the [SDK
Manager](https://developer.android.com/tools/help/sdk-manager) and add the library to your project. For details, see the guide to
[Setting Up Google Play
Services](https://developer.android.com/google/play-services/setup).

## Specify app permissions

Apps whose features use location services must
[request location permissions](https://developer.android.com/training/location/permissions),
depending on the use cases of those features.

## Create location services client

In your activity's [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method,
create an instance of the Fused Location Provider Client as the following code snippet shows.  

### Kotlin

```kotlin
private lateinit var fusedLocationClient: FusedLocationProviderClient

override fun onCreate(savedInstanceState: Bundle?) {
    // ...

    fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
}
```

### Java

```java
private FusedLocationProviderClient fusedLocationClient;

// ..

@Override
protected void onCreate(Bundle savedInstanceState) {
    // ...

    fusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
}
```

## Get the last known location

Once you have created the Location Services client
you can get the last known location of a user's device. When your app is
connected to these you can use the fused location provider's
[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())
method to retrieve the device location. The precision of the location returned
by this call is determined by the permission setting you put in your app
manifest, as described in the guide on how to
[request location permissions](https://developer.android.com/training/location/permissions).

To request the last known location, call the
[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())
method. The following code snippet illustrates the request and a simple handling of the
response:  

### Kotlin

```kotlin
fusedLocationClient.lastLocation
        .addOnSuccessListener { location : Location? ->
            // Got last known location. In some rare situations this can be null.
        }
```

### Java

```java
fusedLocationClient.getLastLocation()
        .addOnSuccessListener(this, new OnSuccessListener<Location>() {
            @Override
            public void onSuccess(Location location) {
                // Got last known location. In some rare situations this can be null.
                if (location != null) {
                    // Logic to handle location object
                }
            }
        });
```

The
[`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient.html#getLastLocation())
method returns a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task)
that you can use to get a
[`Location`](https://developer.android.com/reference/android/location/Location)
object with the latitude and longitude coordinates of a
geographic location. The location object may be `null` in the
following situations:

- Location is turned off in the device settings. The result could be `null` even if the last location was previously retrieved because disabling location also clears the cache.
- The device never recorded its location, which could be the case of a new device or a device that has been restored to factory settings.
- Google Play services on the device has restarted, and there is no active Fused Location Provider client that has requested location after the services restarted. To avoid this situation you can create a new client and request location updates yourself. For more information, see [Request location
  updates](https://developer.android.com/training/location/receive-location-updates).

## Choose the best location estimate

The `FusedLocationProviderClient` provides several methods to retrieve device
location information. Choose from one of the following, depending on your app's
use case:

- [`getLastLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getLastLocation()) gets a location estimate more quickly and minimizes battery usage that can be attributed to your app. However, the location information might be out of date, if no other clients have actively used location recently.
- [`getCurrentLocation()`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient#getCurrentLocation(int,%20com.google.android.gms.tasks.CancellationToken))
  gets a fresher, more accurate location more consistently. However, this method
  can cause active location computation to occur on the device

  This is the recommended way to get a fresh location, whenever possible, and
  is safer than alternatives like starting and managing location updates
  yourself using `requestLocationUpdates()`. If your app calls
  `requestLocationUpdates()`, your app can sometimes consume large amounts of
  power if location isn't available, or if the request isn't stopped correctly
  after obtaining a fresh location.

## Additional resources

For more information about fetching current location in Android, view the
following materials:

### Samples

- [Sample app](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/currentLocation) to demonstrate best practices while fetching current location.