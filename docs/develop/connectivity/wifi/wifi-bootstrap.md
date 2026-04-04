---
title: Wi-Fi Network Request API for peer-to-peer connectivity  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/wifi/wifi-bootstrap
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Wi-Fi Network Request API for peer-to-peer connectivity Stay organized with collections Save and categorize content based on your preferences.



On Android 10 (API level 29) and higher devices, you can use a new peer to peer API to
bootstrap configuration for secondary devices like Chromecast and Google Home
hardware. This feature enables your app to prompt the user to change the access
point that the device is connected to by using
[`WifiNetworkSpecifier`](/reference/android/net/wifi/WifiNetworkSpecifier)
to describe properties of a requested network.

To use this API, do the following:

1. Create a Wi-Fi network specifier using
   [`WifiNetworkSpecifier.Builder`](/reference/android/net/wifi/WifiNetworkSpecifier.Builder).
2. Set a network filter to match networks to connect to, along with required
   credentials.
3. Decide on a combination of [`SSID`](/reference/android/net/wifi/WifiNetworkSpecifier.Builder#setssid),
   [`SSID pattern`](/reference/android/net/wifi/WifiNetworkSpecifier.Builder#setssidpattern),
   [`BSSID`](/reference/android/net/wifi/WifiNetworkSpecifier.Builder#setbssid),
   and [`BSSID pattern`](/reference/android/net/wifi/WifiNetworkSpecifier.Builder#setbssidpattern)
   to set the network filter in each request, subject to the following
   requirements:

   * Each request should provide at least one of `SSID`, `SSID pattern`,
     `BSSID`, or `BSSID pattern`
   * Each request can set only one of `SSID` or `SSID pattern`
   * Each request can set only one of `BSSID` or `BSSID pattern`
4. Add the specifiers to the network request along with a
   [`NetworkCallback`](/reference/android/net/ConnectivityManager.NetworkCallback)
   instance to track the status of the request.

   If the user accepts the request and the connection to the network is
   successful,
   [`NetworkCallback.onAvailable()`](/reference/android/net/ConnectivityManager.NetworkCallback#onAvailable(android.net.Network))
   is invoked on the callback object. If the user denies the request or if the
   connection to the network is unsuccessful,
   [`NetworkCallback.onUnavailable()`](/reference/android/net/ConnectivityManager.NetworkCallback#onUnavailable())
   is invoked on the callback object.

Initiating the request to connect to a peer device launches a dialog box on the
same device, from which that device's user can accept the connection request.

**Note:** Creating a connection using this API does not provide an internet
connection to the app or to the device. To provide an internet
connection to the apps on a device, use the
[Wi-Fi Suggestion API](/develop/connectivity/wifi/wifi-suggest) instead.

## Bypassing user approval

Once the user approves a network to connect to in response to a request from a
specific app, the device stores the approval for the particular access point.
If the app makes a specific request to
connect to that access point again, the device skips the user approval phase
and automatically connects to the network. If the user chooses to forget the
network while connected to a network requested by the API, then this stored
approval for that combination of app and network is removed, and any future
request from the app must be approved by the user again. If the app
makes a non-specific request, such as with an SSID or BSSID pattern, then the
user must approve the request.

## Code sample

The following code sample shows how to connect to an open network with an SSID
prefix of `"test"` and a BSSID OUI of `"10:03:23"`:

### Kotlin

```
val specifier = WifiNetworkSpecifier.Builder()
    .setSsidPattern(PatternMatcher("test", PatternMatcher.PATTERN_PREFIX))
    .setBssidPattern(MacAddress.fromString("10:03:23:00:00:00"), MacAddress.fromString("ff:ff:ff:00:00:00"))
    .build()

val request = NetworkRequest.Builder()
    .addTransportType(NetworkCapabilities.TRANSPORT_WIFI)
    .removeCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    .setNetworkSpecifier(specifier)
    .build()

val connectivityManager = context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager

val networkCallback = object : ConnectivityManager.NetworkCallback() {
    ...
    override fun onAvailable(network: Network?) {
        // do success processing here..
    }

    override fun onUnavailable() {
        // do failure processing here..
    }
    ...
}
connectivityManager.requestNetwork(request, networkCallback)
...
// Release the request when done.
connectivityManager.unregisterNetworkCallback(networkCallback)
```

### Java

```
final NetworkSpecifier specifier =
  new WifiNetworkSpecifier.Builder()
  .setSsidPattern(new PatternMatcher("test", PatternMatcher.PATTERN_PREFIX))
  .setBssidPattern(MacAddress.fromString("10:03:23:00:00:00"), MacAddress.fromString("ff:ff:ff:00:00:00"))
  .build();

final NetworkRequest request =
  new NetworkRequest.Builder()
  .addTransportType(NetworkCapabilities.TRANSPORT_WIFI)
  .removeCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
  .setNetworkSpecifier(specifier)
  .build();

final ConnectivityManager connectivityManager = (ConnectivityManager)
  context.getSystemService(Context.CONNECTIVITY_SERVICE);

final NetworkCallback networkCallback = new NetworkCallback() {
  ...
  @Override
  void onAvailable(...) {
      // do success processing here..
  }

  @Override
  void onUnavailable(...) {
      // do failure processing here..
  }
  ...
};
connectivityManager.requestNetwork(request, networkCallback);
...
// Release the request when done.
connectivityManager.unregisterNetworkCallback(networkCallback);
```