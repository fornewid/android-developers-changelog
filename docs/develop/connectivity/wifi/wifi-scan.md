---
title: https://developer.android.com/develop/connectivity/wifi/wifi-scan
url: https://developer.android.com/develop/connectivity/wifi/wifi-scan
source: md.txt
---

You can use the Wi-Fi scanning capabilities provided by the
[WifiManager API](https://developer.android.com/reference/android/net/wifi/WifiManager) to get a list of
Wi-Fi access points that are visible from the device.

## Wi-Fi scanning process

There are three steps to the scanning process:

1. **Register a broadcast listener** for
   [`SCAN_RESULTS_AVAILABLE_ACTION`](https://developer.android.com/reference/android/net/wifi/WifiManager#SCAN_RESULTS_AVAILABLE_ACTION),
   which is called when scan requests are completed, providing their
   success/failure status. For devices running Android 10 (API level 29) and higher, this
   broadcast will be sent for any full Wi-Fi scan performed on the device by
   the platform or other apps. Apps can passively listen to all scan
   completions on device by using the broadcast without issuing a scan of their
   own.

2. **Request a scan** using
   [`WifiManager.startScan()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan()).
   Make sure to check the return status of the method, since the call may fail
   for any of the following reasons:

   - Scan requests may be throttled because of too many scans in a short time.
   - The device is idle and scanning is disabled.
   - Wi-Fi hardware reports a scan failure.
3. **Get scan results** using
   [`WifiManager.getScanResults()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getScanResults()).
   The returned scan results are the most recently updated results, which may
   be from a previous scan if your current scan has not completed or succeeded.
   This means that you might get older scan results if you call this method
   before receiving a successful
   [`SCAN_RESULTS_AVAILABLE_ACTION`](https://developer.android.com/reference/android/net/wifi/WifiManager#SCAN_RESULTS_AVAILABLE_ACTION)
   broadcast.

The following code provides an example of how to implement these steps:  

### Kotlin

```kotlin
val wifiManager = context.getSystemService(Context.WIFI_SERVICE) as WifiManager

val wifiScanReceiver = object : BroadcastReceiver() {

  override fun onReceive(context: Context, intent: Intent) {
    val success = intent.getBooleanExtra(WifiManager.EXTRA_RESULTS_UPDATED, false)
    if (success) {
      scanSuccess()
    } else {
      scanFailure()
    }
  }
}

val intentFilter = IntentFilter()
intentFilter.addAction(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION)
context.registerReceiver(wifiScanReceiver, intentFilter)

val success = wifiManager.startScan()
if (!success) {
  // scan failure handling
  scanFailure()
}

....

private fun scanSuccess() {
  val results = wifiManager.scanResults
  ... use new scan results ...
}

private fun scanFailure() {
  // handle failure: new scan did NOT succeed
  // consider using old scan results: these are the OLD results!
  val results = wifiManager.scanResults
  ... potentially use older scan results ...
}
```

### Java

```java
WifiManager wifiManager = (WifiManager)
                   context.getSystemService(Context.WIFI_SERVICE);

BroadcastReceiver wifiScanReceiver = new BroadcastReceiver() {
  @Override
  public void onReceive(Context c, Intent intent) {
    boolean success = intent.getBooleanExtra(
                       WifiManager.EXTRA_RESULTS_UPDATED, false);
    if (success) {
      scanSuccess();
    } else {
      // scan failure handling
      scanFailure();
    }
  }
};

IntentFilter intentFilter = new IntentFilter();
intentFilter.addAction(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION);
context.registerReceiver(wifiScanReceiver, intentFilter);

boolean success = wifiManager.startScan();
if (!success) {
  // scan failure handling
  scanFailure();
}

....

private void scanSuccess() {
  List<ScanResult> results = wifiManager.getScanResults();
  ... use new scan results ...
}

private void scanFailure() {
  // handle failure: new scan did NOT succeed
  // consider using old scan results: these are the OLD results!
  List<ScanResult> results = wifiManager.getScanResults();
  ... potentially use older scan results ...
}
```

## Restrictions

Android 8.0 (API level 26) introduced restrictions regarding permissions and the
allowed frequency of Wi-Fi scans.

To improve network performance, security, and battery life, Android 9 (API
level 28) tightened permission requirements and further limited the frequency of
Wi-Fi scans.

### Permissions

| **Note:** In each of the following sections that mention location permissions or location-gathering logic, keep in mind that, when your app is running in the background, [access to location](https://developer.android.com/training/location/background) should be critical to the core functionality of the app and is accompanied with proper disclosure to users.

**Android 8.0 and Android 8.1:**

A successful call to
[`WifiManager.getScanResults()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getScanResults())
requires *any one* of the following permissions:

- [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
- [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)
- [`CHANGE_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE)

If the calling app does not have any of these permissions, the call fails with a
[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

Alternatively, on devices running Android 8.0 (API level 26) and higher, you can
use the
[`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager)
to perform a scan of nearby companion devices on behalf of your app without
requiring the location permission. For more on this option, see
[Companion device
pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing).

**Android 9:**

A successful call to
[`WifiManager.startScan()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan())
requires *all* of the following conditions to be met:

- Your app has the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) **or** [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) permission.
- Your app has the [`CHANGE_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE) permission.
- Location services are enabled on the device (under **Settings \> Location**).

**Android 10 (API level 29) and higher:**

A successful call to
[`WifiManager.startScan()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan())
requires *all* of the following conditions to be met:

- If your app is targeting Android 10 (API level 29) SDK or higher, your app has the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission.
- If your app is targeting SDK lower than Android 10 (API level 29), your app has the [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) or [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission.
- Your app has the [`CHANGE_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE) permission.
- Location services are enabled on the device (under **Settings** \> **Location**).

To successfully call
[`WifiManager.getScanResults()`](https://developer.android.com/reference/android/net/wifi/WifiManager#getScanResults()),
ensure *all* of the following conditions are met:

- If your app is targeting Android 10 (API level 29) SDK or higher, your app has the `ACCESS_FINE_LOCATION` permission.
- If your app is targeting SDK lower than Android 10 (API level 29), your app has the `ACCESS_COARSE_LOCATION` or `ACCESS_FINE_LOCATION` permission.
- Your app has the [`ACCESS_WIFI_STATE`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE) permission.
- Location services are enabled on the device (under **Settings** \> **Location**).

If the calling app doesn't meet all of these requirements, the call fails with
a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).

### Throttling

The following limitations apply to the frequency of scans using
[`WifiManager.startScan()`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan()).

**Android 8.0 and Android 8.1:**

Each background app can scan one time in a 30-minute period.

**Android 9:**

Each foreground app can scan four times in a 2-minute period. This allows for a
burst of scans in a short time.

All background apps combined can scan one time in a 30-minute period.

**Android 10 and higher:**

The same throttling limits from Android 9 apply. There is a new developer option
to toggle the throttling off for local testing (under **Developer Options \>**
**Networking \> Wi-Fi scan throttling**).