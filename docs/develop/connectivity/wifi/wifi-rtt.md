---
title: https://developer.android.com/develop/connectivity/wifi/wifi-rtt
url: https://developer.android.com/develop/connectivity/wifi/wifi-rtt
source: md.txt
---

You can use the Wi-Fi location functionality provided by the
[Wi-Fi RTT (Round-Trip-Time) API](https://developer.android.com/reference/android/net/wifi/rtt/package-summary)
to measure the distance to nearby RTT-capable Wi-Fi access points and peer
[Wi-Fi Aware](https://developer.android.com/develop/connectivity/wifi-aware) devices.

If you measure the distance to three or more access points, you can use a
multilateration algorithm to estimate the device position that best fits those
measurements. The result is typically accurate within 1-2 meters.

With this accuracy, you can develop fine-grained location-based services, such
as indoor navigation, disambiguated voice control (for example, "Turn on this
light"), and location-based information (for example, "Are there special offers
for this product?").

The requesting device doesn't need to connect to the access points to measure
distance with Wi-Fi RTT. To maintain privacy, only the requesting device is able
to determine the distance to the access point; the access points don't have
this information. Wi-Fi RTT operations are unlimited for foreground apps but are
throttled for background apps.

Wi-Fi RTT and the related *Fine-Time-Measurement* (FTM) capabilities are
specified by the IEEE 802.11-2016 standard. Wi-Fi RTT requires the precise time
measurement provided by FTM because it calculates the distance between two
devices by measuring the time a packet takes to make a round trip between the
devices and multiplying that time by the speed of light.

Android 15 (API level 35) introduced support for IEEE 802.11az non-trigger based
(NTB) ranging.

## Implementation differences based on Android version

Wi-Fi RTT was introduced in Android 9 (API level 28). When using this protocol
to determine a device's position using multilateration with devices running
Android 9, you need to have access to pre-determined access point (AP) locations
data in your app. It is up to you to decide how to store and retrieve this data.

On devices running Android 10 (API level 29) and higher, AP location data can be
represented as
[`ResponderLocation`](https://developer.android.com/reference/android/net/wifi/rtt/ResponderLocation)
objects, which include latitude, longitude, and altitude. For Wi-Fi RTT APs that
support Location Configuration Information/Location Civic Report (LCI/LCR data),
the protocol will return a `ResponderLocation` object during the
[ranging process](https://developer.android.com/develop/connectivity/wifi/wifi-rtt#request-ranging).

This feature allows apps to query APs to ask them for their position directly
rather than needing to store this information ahead of time. So, your app can
find APs and determine their positions even if the APs were not known before,
such as when a user enters a new building.

IEEE 802.11az NTB ranging support is available on devices running Android 15
(API level 35) and higher. That means that if the device supports IEEE 802.11az
NTB initiator mode (indicated by
[`WifiRttManager.CHARACTERISTICS_KEY_BOOLEAN_NTB_INITIATOR`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager#CHARACTERISTICS_KEY_BOOLEAN_NTB_INITIATOR)),
your app can find both IEEE 802.11mc and IEEE 802.11az capable APs with a single
range request. The `RangingResult` API has been extended to provide information
about the minimum and maximum value that can be used for the interval between
ranging measurements, leaving the exact interval in the control of your app.

## Requirements

- The hardware of the device making the ranging request must implement the 802.11-2016 FTM standard or 802.11az standard (non-trigger based ranging).
- The device making the ranging request must be running Android 9 (API level 28) or later. IEEE 802.11az non-trigger based ranging is enabled on devices running Android 15 (API level 35) and higher.
- The device making the ranging request must have location services enabled and Wi-Fi scanning turned on (under **Settings \> Location**).
- If the app that's making the ranging request targets Android 13 (API level 33) or higher, it must have the [`NEARBY_WIFI_DEVICES`](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES) permission. If such an app targets an earlier version of Android, it must have the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission instead.
- The app must query the range of access points while the app is visible or in a foreground service. The app cannot [access location information from the
  background](https://developer.android.com/training/location/background).
- The access point must implement the IEEE 802.11-2016 FTM standard or IEEE 802.11az standard (non-trigger based ranging).

## Setup

To set up your app to use Wi-Fi RTT, perform the following steps.

#### 1. Request permissions

Request the following permissions in your app's manifest:  

    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <!-- If your app targets Android 13 (API level 33)
         or higher, you must declare the NEARBY_WIFI_DEVICES permission. -->
    <uses-permission android:name="android.permission.NEARBY_WIFI_DEVICES"
                     <!-- If your app derives location information from Wi-Fi APIs,
                          don't include the "usesPermissionFlags" attribute. -->
                     android:usesPermissionFlags="neverForLocation" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
                     <!-- If any feature in your app relies on precise location
                          information, don't include the "maxSdkVersion"
                          attribute. -->
                     android:maxSdkVersion="32" />

The `NEARBY_WIFI_DEVICES` and `ACCESS_FINE_LOCATION` permissions are dangerous
permissions, so you need to request them at runtime every time the user wants to
perform an RTT scan operation. Your app will need to request the user's
permission if the permission has not already been granted. For more information
about runtime permissions, see
[Request App Permissions](https://developer.android.com/training/permissions/requesting).
| **Note:** If the necessary permission is revoked during a ranging operation, the operation will be aborted and a failure reported.

#### 2. Check whether the device supports Wi-Fi RTT

To check whether the device supports Wi-Fi RTT, use the
[`PackageManager`](https://developer.android.com/reference/android/content/pm/PackageManager) API:  

### Kotlin

```kotlin
context.packageManager.hasSystemFeature(PackageManager.FEATURE_WIFI_RTT)
```

### Java

```java
context.getPackageManager().hasSystemFeature(PackageManager.FEATURE_WIFI_RTT);
```

#### 3. Check whether Wi-Fi RTT is available

Wi-Fi RTT may exist on the device, but it may not be available because the user
has disabled Wi-Fi. Depending on their hardware and firmware capabilities, some
devices may not support Wi-Fi RTT if SoftAP or tethering are in use. To check
whether Wi-Fi RTT is available, call
[`isAvailable()`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager#isAvailable()).

The availability of Wi-Fi RTT can change at any time. Your app should register a
[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver)
to receive
[`ACTION_WIFI_RTT_STATE_CHANGED`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager#ACTION_WIFI_RTT_STATE_CHANGED),
which is sent when availability changes. When your app receives the broadcast
intent, the app should check the current state of availability and adjust its
behavior accordingly.

For example:  

### Kotlin

```kotlin
val filter = IntentFilter(WifiRttManager.ACTION_WIFI_RTT_STATE_CHANGED)
val myReceiver = object: BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        if (wifiRttManager.isAvailable) {
            ...
        } else {
            ...
        }
    }
}
context.registerReceiver(myReceiver, filter)
```

### Java

```java
IntentFilter filter =
    new IntentFilter(WifiRttManager.ACTION_WIFI_RTT_STATE_CHANGED);
BroadcastReceiver myReceiver = new BroadcastReceiver() {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (wifiRttManager.isAvailable()) {
            ...
        } else {
            ...
        }
    }
};
context.registerReceiver(myReceiver, filter);
```
| **Note:** Make sure that you register the broadcast receiver before checking availability. Otherwise, there could be a period of time when the app thinks that Wi-Fi RTT is available but isn't notified if availability changes.

For more information, see [Broadcasts](https://developer.android.com/guide/components/broadcasts).

## Create a ranging request

A ranging request
([`RangingRequest`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest)) is created
by specifying a list of APs or Wi-Fi Aware peers to which a range
is requested. Multiple access points or Wi-Fi Aware peers can be specified in a
single ranging request; the distances to all devices are measured and returned.

For example, a request can use the
[`addAccessPoint()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest.Builder#addAccessPoint(android.net.wifi.ScanResult))
method to specify an access point to which to measure the distance:  

### Kotlin

```kotlin
val req: RangingRequest = RangingRequest.Builder().run {
    addAccessPoint(ap1ScanResult)
    addAccessPoint(ap2ScanResult)
    build()
}
```

### Java

```java
RangingRequest.Builder builder = new RangingRequest.Builder();
builder.addAccessPoint(ap1ScanResult);
builder.addAccessPoint(ap2ScanResult);

RangingRequest req = builder.build();
```

An access point is identified by its
[`ScanResult`](https://developer.android.com/reference/android/net/wifi/ScanResult) object, which can be
obtained by calling
[`WifiManager.getScanResults()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getscanresults).
You can use
[`addAccessPoints(List<ScanResult>)`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest.Builder#addaccesspoints)
to add multiple access points in a batch.

`ScanResult` objects can contain both IEEE 802.11mc (`is80211mcResponder()`) and
IEEE 802.11az non-trigger based ranging (`is80211azNtbResponder()`) supported
APs. Devices that support IEEE 802.11az NTB ranging perform either 802.11mc or
802.11az ranging depending on the AP's capability, defaulting to 802.11az when
the AP supports both. Devices that don't support IEEE 802.11az perform all
ranging using the IEEE 802.11mc protocol.

Similarly, a ranging request can add a Wi-Fi Aware peer using either its MAC
address or its [`PeerHandle`](https://developer.android.com/reference/android/net/wifi/aware/PeerHandle), using
the
[`addWifiAwarePeer(MacAddress peer)`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest.Builder#addwifiawarepeer)
and [`addWifiAwarePeer(PeerHandle peer)`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest.Builder#addwifiawarepeer_3)
methods, respectively. For more information about discovering Wi-Fi Aware peers,
see the [Wi-Fi Aware documentation](https://developer.android.com/develop/connectivity/wifi-aware).

## Request ranging

An app issues a ranging request using the
[`WifiRttManager.startRanging()`](https://developer.android.com/reference/android/net/wifi/rtt/WifiRttManager#startRanging(android.net.wifi.rtt.RangingRequest,%20java.util.concurrent.Executor,%20android.net.wifi.rtt.RangingResultCallback))
method and providing the following: a
[`RangingRequest`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest) to specify the
operation, an [`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor) to specify
the callback context, and a
[`RangingResultCallback`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback)
to receive the results.

For example:  

### Kotlin

```kotlin
val mgr = context.getSystemService(Context.WIFI_RTT_RANGING_SERVICE) as WifiRttManager
val request: RangingRequest = myRequest
mgr.startRanging(request, executor, object : RangingResultCallback() {

    override fun onRangingResults(results: List<RangingResult>) { ... }

    override fun onRangingFailure(code: Int) { ... }
})
```

### Java

```java
WifiRttManager mgr =
      (WifiRttManager) Context.getSystemService(Context.WIFI_RTT_RANGING_SERVICE);

RangingRequest request ...;
mgr.startRanging(request, executor, new RangingResultCallback() {

  @Override
  public void onRangingFailure(int code) { ... }

  @Override
  public void onRangingResults(List<RangingResult> results) { ... }
});
```

The ranging operation is performed asynchronously, and ranging results are
returned in one of the callbacks of
[`RangingResultCallback`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback):

- If the whole ranging operation fails, the [`onRangingFailure`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback#onrangingfailure) callback is triggered with a status code described in [`RangingResultCallback`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback). Such a failure may happen if the service cannot execute a ranging operation at the time--for example, because Wi-Fi is disabled, because the application has requested too many ranging operations and is throttled, or because of a permission issue.
- When the ranging operation completes, the [`onRangingResults`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback#onrangingresults) callback is triggered with a list of results that matches the list of requests---one result for each request. The order of the results does not necessarily match the order of the requests. Note that ranging operation may complete but each result may still indicate a failure of that specific measurement.

## Interpret ranging results

Each of the results returned by the
[`onRangingResults`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResultCallback#onrangingresults)
callback is specified by a [`RangingResult`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult)
object. On each request, do the following.

#### 1. Identify the request

Identify the request based on the information provided when creating the
[`RangingRequest`](https://developer.android.com/reference/android/net/wifi/rtt/RangingRequest):
most often a MAC address provided in the `ScanResult` identifying an access
point. The MAC address can be obtained from the ranging result using the
[`getMacAddress()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getMacAddress())
method.

The list of ranging results may be in different order than the peers (access
points) specified in the ranging request, so you should use the MAC address to
identify the peer, not the order of results.

#### 2. Determine whether each measurement was successful

To determine whether a measurement was successful, use the
[`getStatus()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getstatus)
method. Any value other than
[`STATUS_SUCCESS`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#status_success)
indicates a failure. A failure means that all other fields of this result
(except the request identification above) are invalid, and the corresponding
`get*` method will fail with an
[`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException) exception.

#### 3. Get results for each successful measurement

For each successful measurement (`RangingResult`), you can retrieve result
values with the respective `get` methods:

- Distance, in mm, and the standard deviation of the measurement:

  [`getDistanceMm()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getdistancemm)

  [`getDistanceStdDevMm()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getdistancestddevmm)
- RSSI of the packets used for the measurements:

  [`getRssi()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getrssi)
- Time in milliseconds at which the measurement was taken (indicating time
  since boot):

  [`getRangingTimestampMillis()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getrangingtimestampmillis)
- Number of measurements that were attempted and the number of measurements
  that succeeded (and on which the distance measurements are based):

  [`getNumAttemptedMeasurements()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getnumattemptedmeasurements)

  [`getNumSuccessfulMeasurements()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getnumsuccessfulmeasurements)
- Minimum and maximum time a client device must wait between 11az NTB
  measurements:

  [`getMinTimeBetweenNtbMeasurementsMicros()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getMinTimeBetweenNtbMeasurementsMicros())
  and
  [`getMaxTimeBetweenNtbMeasurementsMicros()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#getMaxTimeBetweenNtbMeasurementsMicros())
  return the minimum and maximum time. If the next ranging measurement is
  requested before the minimum time has elapsed, then the API returns the
  cached ranging result. If the next ranging measurement is requested after
  the maximum time has elapsed, then the API terminates the non-trigger
  ranging session and negotiates a new ranging session with the responding
  station. You should avoid requested a new ranging session, because it adds
  overhead to the ranging measurement time. To take full advantage of 802.11az
  non-trigger based ranging efficiency, trigger the next ranging request
  between the minimum and maximum measurement time specified in the previous
  `RangingResult` measurement.
- Long Training Field (LTF) repetitions that responder and initiator stations
  used in the preamble for the IEEE 802.11az NTB result:

  [`get80211azResponderTxLtfRepetitionsCount()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#get80211azResponderTxLtfRepetitionsCount())

  [`get80211azInitiatorTxLtfRepetitionsCount()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#get80211azInitiatorTxLtfRepetitionsCount())
- Number of transmit and receive spatial time streams (STS) that the initiator
  station used for the IEEE 802.11az NTB result:

  [`get80211azNumberOfTxSpatialStreams()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#get80211azNumberOfTxSpatialStreams())

  [`get80211azNumberOfRxSpatialStreams()`](https://developer.android.com/reference/android/net/wifi/rtt/RangingResult#get80211azNumberOfRxSpatialStreams())

| **Note:** Both LTF repetitions and number of transmit and receive space time streams (STS) can be used to estimate the accuracy of an IEEE 802.11az NTB result.

## Android devices that support WiFi-RTT

The following tables list some [phones](https://developer.android.com/develop/connectivity/wifi/wifi-rtt#supported-phones), [access points](https://developer.android.com/develop/connectivity/wifi/wifi-rtt#supported-aps), and [retail, warehousing and distribution center devices](https://developer.android.com/develop/connectivity/wifi/wifi-rtt#retail-devices)
that support WiFi-RTT. These are far from comprehensive. We encourage you to
[reach out to us](mailto:Location-Partners-Feedback@google.com?subject=%5BRTT%5D)
to list your RTT capable-products here.

### Access points

| Manufacturer and model | Support date | Protocol |
|---|---|---|
| [Nest Wifi Pro (Wi-Fi 6E)](https://store.google.com/product/nest_wifi_pro) | Supported | mc |
| [Compulab WILD AP](https://fit-iot.com/web/products/wild/) | Supported | mc |
| [Google Wi-Fi](https://store.google.com/product/google_wifi_first_gen) | Supported | mc |
| [Google Nest Wi-Fi Router](https://store.google.com/us/product/nest_wifi_specs) | Supported | mc |
| [Google Nest Wi-Fi Point](https://store.google.com/us/product/nest_wifi_specs) | Supported | mc |
| [Aruba AP-635](https://www.arubanetworks.com/assets/ds/DS_AP630Series.pdf) | Supported | mc |
| Cisco 9130 | Supported | mc |
| Cisco 9136 | Supported | mc |
| Cisco 9166 | Supported | mc |
| Cisco 9164 | Supported | mc |
| Cisco CW9172I | Supported | mc/az |
| Cisco CW9172H | Supported | mc/az |
| Cisco CW9176I | Supported | mc/az |
| Cisco CW9178I | Supported | mc/az |
| Aruba AP-505 | Supported | mc |
| Aruba AP-515 | Supported | mc |
| Aruba AP-575 | Supported | mc |
| Aruba AP-518 | Supported | mc |
| Aruba AP-505H | Supported | mc |
| Aruba AP-565 | Supported | mc |
| Aruba AP-535 | Supported | mc |
| Aruba AP567 | Supported | mc |
| Aruba AP577 | Supported | mc |
| Aruba AP555 | Supported | mc |
| Aruba AP635 | Supported | mc |
| Aruba AP655 | Supported | mc |
| Aruba AP615 | Supported | mc |
| Aruba AP734 | Supported | mc/az |
| Aruba AP735 | Supported | mc/az |
| Aruba AP754 | Supported | mc/az |
| Aruba AP755 | Supported | mc/az |

### Phones

| Manufacturer and model | Android version |
|---|---|
| Google Pixel 9 Pro XL | 14+ |
| Google Pixel 9 | 14+ |
| Google Pixel 9 Pro | 14+ |
| Google Pixel 9 Pro XL | 14+ |
| Google Pixel 7a | 14+ |
| Google Pixel 7 | 14+ |
| Google Pixel 8 | 14+ |
| Google Pixel 8 Pro | 14+ |
| Google Pixel 8a | 14+ |
| Samsung SM-S918B | 14+ |
| Samsung SM-A515F | 14+ |
| Google Pixel 9 Pro | 14+ |
| Samsung SM-A546E | 14+ |
| Samsung SM-S928B | 14+ |
| Samsung SM-A217F | 14+ |
| Samsung SM-A715F | 14+ |
| Samsung SM-A528B | 14+ |
| Samsung SM-A135F | 14+ |
| Samsung SM-S911B | 14+ |
| Xiaomi 21091116AI | 14+ |
| Google Pixel 9 | 14+ |
| Samsung SM-A127F | 14+ |
| Google Pixel 7 Pro | 14+ |
| Samsung SM-A556E | 14+ |
| Pixel 6 | 9.0+ |
| Pixel 6 Pro | 9.0+ |
| Pixel 5 | 9.0+ |
| Pixel 5a | 9.0+ |
| Pixel 5a 5G | 9.0+ |
| Xiaomi Mi 10 Pro | 9.0+ |
| Xiaomi Mi 10 | 9.0+ |
| Xiaomi Redmi Mi 9T Pro | 9.0+ |
| Xiaomi Mi 9T | 9.0+ |
| Xiaomi Mi 9 | 9.0+ |
| Xiaomi Mi Note 10 | 9.0+ |
| Xiaomi Mi Note 10 Lite | 9.0+ |
| Xiaomi Redmi Note 9S | 9.0+ |
| Xiaomi Redmi Note 9 Pro | 9.0+ |
| Xiaomi Redmi Note 8T | 9.0+ |
| Xiaomi Redmi Note 8 | 9.0+ |
| Xiaomi Redmi K30 Pro | 9.0+ |
| Xiaomi Redmi K20 Pro | 9.0+ |
| Xiaomi Redmi K20 | 9.0+ |
| [Xiaomi Redmi Note 5 Pro](https://www.mi.com/in/redmi-note-5-pro/) | 9.0+ |
| Xiaomi Mi CC9 Pro | 9.0+ |
| LG G8X ThinQ | 9.0+ |
| LG V50S ThinQ | 9.0+ |
| LG V60 ThinQ | 9.0+ |
| [LG V30](https://www.lg.com/us/cell-phones/lg-US998-Unlocked-v30) | 9.0+ |
| Samsung Galaxy Note 10+ 5G | 9.0+ |
| Samsung Galaxy S20+ 5G | 9.0+ |
| Samsung Galaxy S20+ | 9.0+ |
| Samsung Galaxy S20 5G | 9.0+ |
| Samsung Galaxy S20 Ultra 5G | 9.0+ |
| Samsung Galaxy S20 | 9.0+ |
| [Samsung Galaxy Note 10+](https://www.samsung.com/us/mobile/galaxy-note10/) | 9.0+ |
| Samsung Galaxy Note 10 5G | 9.0+ |
| Samsung Galaxy Note 10 | 9.0+ |
| [Samsung A9 Pro](https://www.samsung.com/sg/smartphones/galaxy-a9-pro-a910/SM-A910FZWDXSP/) | 9.0+ |
| Google Pixel 4 XL | 9.0+ |
| [Google Pixel 4](https://store.google.com/us/product/pixel_4_specs) | 9.0+ |
| Google Pixel 4a | 9.0+ |
| Google Pixel 3 XL | 9.0+ |
| [Google Pixel 3](https://store.google.com/us/product/pixel_3_specs) | 9.0+ |
| Google Pixel 3a XL | 9.0+ |
| Google Pixel 3a | 9.0+ |
| Google Pixel 2 XL | 9.0+ |
| [Google Pixel 2](https://www.android.com/intl/en_uk/phones/google-pixel-2/) | 9.0+ |
| Google Pixel 1 XL | 9.0+ |
| [Google Pixel 1](https://www.android.com/intl/en_ca/phones/pixel/) | 9.0+ |
| Poco X2 | 9.0+ |
| Sharp Aquos R3 SH-04L | 9.0+ |

### Retail, warehousing, and distribution center devices

| Manufacturer and model | Android version |
|---|---|
| Zebra PS20 | 10.0+ |
| Zebra TC52/TC52HC | 10.0+ |
| Zebra TC57 | 10.0+ |
| Zebra TC72 | 10.0+ |
| Zebra TC77 | 10.0+ |
| Zebra MC93 | 10.0+ |
| Zebra TC8300 | 10.0+ |
| Zebra VC8300 | 10.0+ |
| Zebra EC30 | 10.0+ |
| Zebra ET51 | 10.0+ |
| Zebra ET56 | 10.0+ |
| Zebra L10 | 10.0+ |
| Zebra CC600/CC6000 | 10.0+ |
| Zebra MC3300x | 10.0+ |
| Zebra MC330x | 10.0+ |
| Zebra TC52x | 10.0+ |
| Zebra TC57x | 10.0+ |
| Zebra EC50 (LAN and HC) | 10.0+ |
| Zebra EC55 (WAN) | 10.0+ |
| Zebra WT6300 | 10.0+ |
| [Skorpio X5](https://cdn.barcodesinc.com/themes/barcodesinc/pdf/Datalogic/skorpio-x5.pdf) | 10.0+ |