---
title: https://developer.android.com/training/cars/platforms/automotive-os/coarse-location
url: https://developer.android.com/training/cars/platforms/automotive-os/coarse-location
source: md.txt
---

To respect user privacy, app developers are encouraged to only request coarse
location permissions. Apps that need an approximate coarse position typically
use the fused network location (FLP) because it's fast and consumes less power.
As compared to Android-based mobile devices, network location in automotive apps
can be more challenging. You can use two Android APIs:

- LocationManager API requires that you use [`requestLocationUpdates`](https://developer.android.com/reference/android/location/LocationManager#requestLocationUpdates(java.lang.String,%20long,%20float,%20android.location.LocationListener)) to
  explicitly identify the preferred location provider.

- Google Play services API offers a more straightforward way for you to
  work with location in [`FusedLocationProviderClient`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient).

Many automotive apps use the FLP from the Google Play services API instead of
`LocationManager`. FLP selects the optimal location provider based on location
request criteria and policies (power and accuracy) needed by the vehicle.

You can instead opt to explicitly request and use [`NETWORK_PROVIDER`](https://developer.android.com/reference/android/location/LocationManager#NETWORK_PROVIDER)
as well as [`GPS_PROVIDER`](https://developer.android.com/reference/android/location/LocationManager#GPS_PROVIDER) for
fine positions, which uses [`android.permission.ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permissions. On Android 12 (API level 31) and higher, the [`FUSED_PROVIDER`](https://developer.android.com/reference/android/location/LocationManager#FUSED_PROVIDER),
previously accessible only through the Google Play services API, is
available as a location provider to `LocationManager`. You can see an
implementation of FLP in [`FusedLocationProvider.java`](https://cs.android.com/android/platform/superproject/+/master:frameworks/base/packages/FusedLocation/src/com/android/location/fused/FusedLocationProvider.java;l=49;drc=1679ed09011e7756e415be9086a9f0ca5dff816b).

While it's possible to use `GPS_PROVIDER` with coarse permission rights only ---
the framework artificially degrades accuracy to align with expectations --- it
makes little sense for developers targeting Android phones because overall
availability is poor and often slower to obtain a coarse position.

### Network location in automotive

The `NETWORK_PROVIDER` used on Android phones (with Google Mobile Services)
determines location based on nearby cell towers, Wi-Fi access points, and
Bluetooth (BT) beacons. As a result, `NETWORK_PROVIDER` may require a data
connection.

For automotive apps, device constraints differ. Because Gthe global navigation
satellite system (GNSS) is usually on, no penalties are incurred due to
increased power and battery usage. As a result, IVI uptime is not compromised.
We strive to minimize data exchanged with our servers.

A lot of apps therefore use FLP from the Play API instead of `LocationManager`
directly as FLP automatically does the *smart thing* by using the location
provider best able to satisfy location request criteria/policies (namely power
and accuracy).

Unlike mobile devices, vehicles rarely appear to *jump* from one place to
another. Vehicle position is known under the hood most of the time.

#### Network location provider (NLP)

Most vehicles don't implement required telephony APIs to get needed information
on a Cell ID (and signal strength). As a result and, because we minimize data
usage, no additional functional implementation of NLP is provided.

#### Fused location provider

The mobile FLP, in addition to smartly using network and GPS providers as
appropriate, fuses information from other sensors to further enhance the
quality of locations. The current implementation of Automotive's FLP on the
other hand takes advantage of the aforementioned assumptions and uses the
`GPS_PROVIDER` as an underlying source all the time. It fudges the positions
from GNSS, adding some errors to be more inaccurate when needed. For example,
when coarse locations are provided to a client.

As such, in a very few instances, there can be a longer than usual time for the
first position to be available. For example, the very first time a vehicle or,
to be more precise, its location subsystem is used or after getting towed.
| **Note:** Automotive apps should have no expectation that an NLP can be leveraged nor is it expected that the FLP perform any sensor fusion.

### Design apps to target mobile and automotive uses

For apps targeting mobile *and* automotive devices that don't
require a higher quality of precision, request
[`android.permission.ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/location/LocationManager#FUSED_PROVIDER) *only* and fall back to using
FLP when available. Alternatively, use `GPS_PROVIDER` directly with the same
permissions. The framework degrades the precision of the underlying GNSS
position to align with API expectations. To learn more, see [Accuracy](https://developer.android.com/training/location/permissions#accuracy)
in [Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions).

In addition, these apps must explicitly declare the
[`android.hardware.location.network`](https://developer.android.com/guide/topics/manifest/uses-feature-element#location-hw-features) feature as *optional* in their
manifest. For example:

    <uses-feature android:name="android.hardware.location.network" android:required="false" />

This approach helps achieve greater compatibility with devices across form
factors and, therefore, maximum app availability with no code differences for
getting positions when needed.