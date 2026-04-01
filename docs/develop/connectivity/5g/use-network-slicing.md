---
title: https://developer.android.com/develop/connectivity/5g/use-network-slicing
url: https://developer.android.com/develop/connectivity/5g/use-network-slicing
source: md.txt
---

5G network slicing gives carriers the ability to provide network performance
boosts for specific use cases. This guide explains how an app can use the
network slicing feature.

This guide also covers how to trigger the [network slicing upsell UX
flow](https://developer.android.com/develop/connectivity/5g/use-network-slicing#ux-flow) in cases where a purchase is required before the app can
access the premium connection.

### Step 1: Declare premium capability intents

In order for your app's request for a premium slicing capability to be honored,
your app must declare its intent to request that capability in the app manifest.
Otherwise, the network request fails throwing a `SecurityException`.

To do this, your app must declare the
[`PackageManager.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES`](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES)
property in the `AndroidManifest.xml` file and include a corresponding XML
resource file.

A capability declaration in the manifest file looks like this:

    <property android:name="android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES"
              android:resource="@xml/network_capabilities" />

The corresponding `network_capabilities.xml` resource file looks like this:

    <network-capabilities-declaration> xmlns:android="http://schemas.android.com/apk/res/android">
        <uses-network-capability android:name="NET_CAPABILITY_PRIORITIZE_LATENCY"/>
    </network-capabilities-declaration>

> [!NOTE]
> **Note:** The only premium capability supported in Android 14 is [`NET_CAPABILITY_PRIORITIZE_LATENCY`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_PRIORITIZE_LATENCY).

### Step 2: Verify if the premium capability is available

Call the
[`requestNetwork()`](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
API method to determine whether the premium capability is available.

    Context mContext;
    Network mNetwork;

    public void requestPremiumCapabilityNetwork(@NetCapability int capability) {
        ConnectvityManager cm = mContext.getSystemService(ConnectivityManager.class);
        NetworkRequest request = NetworkRequest.Builder()
                .addCapability(capability)
                .build();
        cm.requestNetwork(request, new NetworkCallback() {
            @Override
            public void onAvailable(Network network) {
                log("Premium capability %d network is available.", capability);
                mNetwork = network;
            }

            @Override
            public void onLost(Network network) {
                log("Premium capability %d network is not available.", capability);
                mNetwork = null;
            }
        });
    }

When you build a `NetworkRequest` object, the capability that you add is **not**
the same capability that you pass to the `TelephonyManager` APIs.
The following table maps the constants from the `TelephonyManager` class to the
corresponding constants in `NetworkCapabilities`.

| `TelephonyManager` constant | `NetworkCapabilities` constant |
|---|---|
| [`PREMIUM_CAPABILITY_PRIORITIZE_LATENCY`](https://developer.android.com/reference/android/telephony/TelephonyManager#PREMIUM_CAPABILITY_PRIORITIZE_LATENCY) | [`NET_CAPABILITY_PRIORITIZE_LATENCY`](https://developer.android.com/reference/android/net/NetworkCapabilities#NET_CAPABILITY_PRIORITIZE_LATENCY) |

### Step 3: If the premium capability is not available, check availability to purchase

> [!NOTE]
> **Note:** The network slicing upsell feature is only available in Android 14 and higher for apps that have the [`READ_BASIC_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_BASIC_PHONE_STATE) permission.

Call the [`isPremiumCapabilityAvailableForPurchase()`](https://developer.android.com/reference/android/telephony/TelephonyManager#isPremiumCapabilityAvailableForPurchase(int))
API method to determine whether the selected premium capability is available.
This method returns `true` if the capability is available for purchase from the
carrier using the upsell notification workflow.

    Context mContext;

    public boolean isPremiumCapabilityAvailableForPurchase(@PremiumCapability int capability) {
        TelephonyManager tm = mContext.getSystemService(TelephonyManager.class);
        boolean isAvailable = tm.isPremiumCapabilityAvailableForPurchase(capability);
        log("Premium capability %d %s available to purchase.",
                capability,
                isAvailable ? "is" : "is not");
        return isAvailable;
    }

### Step 4: Initiate the upsell notification flow

After confirming that the premium capability is available, your app should call
[`purchasePremiumCapability()`](https://developer.android.com/reference/android/telephony/TelephonyManager#purchasePremiumCapability(int,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.lang.Integer%3E))
to initiate the upsell notification flow. If the user has not already purchased
the specified capability and all preconditions are satisfied, then the platform
shows the user a notification to let them know that performance boost options
might be available from their carrier. If the user taps the notification, the
platform opens the carrier's webview so that the purchase process can continue.

    Context mContext;

    public void purchasePremiumCapability(@PremiumCapability int capability) {
        TelephonyManager tm = mContext.getSystemService(TelephonyManager.class);
        tm.purchasePremiumCapability(capability, Runnable::run, new Consumer<Integer>() {
            @Override
            public void accept(Integer result) {
                log("Purchase premium capability %d result: %d", capability, result);
                int purchaseResult = result;
            }
        });
    }

The `parameter` callback passed to `purchasePremiumCapability()` returns a
result code for the purchase request.

The result codes
[`PURCHASE_PREMIUM_CAPABILITY_RESULT_SUCCESS`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_SUCCESS)
and
[`PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_PURCHASED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_PURCHASED)
represent successful results where your app may proceed to requesting the
selected premium capability.

The result codes in the following list represent failed purchase requests. See
the API reference to learn more about them.

- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_IN_PROGRESS`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_IN_PROGRESS)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_DISABLED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_DISABLED)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_ERROR`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_ERROR)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_ENTITLEMENT_CHECK_FAILED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_ENTITLEMENT_CHECK_FAILED)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_FEATURE_NOT_SUPPORTED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_FEATURE_NOT_SUPPORTED)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_NETWORK_NOT_AVAILABLE`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_NETWORK_NOT_AVAILABLE)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_DEFAULT_DATA_SUBSCRIPTION`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_DEFAULT_DATA_SUBSCRIPTION)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_FOREGROUND`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_FOREGROUND)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_PENDING_NETWORK_SETUP`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_PENDING_NETWORK_SETUP)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_REQUEST_FAILED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_REQUEST_FAILED)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_THROTTLED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_THROTTLED)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_TIMEOUT`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_TIMEOUT)
- [`PURCHASE_PREMIUM_CAPABILITY_RESULT_USER_CANCELED`](https://developer.android.com/reference/android/telephony/TelephonyManager#PURCHASE_PREMIUM_CAPABILITY_RESULT_USER_CANCELED)

If the purchase request fails, your app may use the default network instead.
There is no automatic fallback behavior if the premium slice request cannot be
fulfilled.

### UX flow for slicing upsell

![The UX flow shows the user a notification that opens up a carrier
websheet where they can complete the purchase.](https://developer.android.com/static/images/develop/connectivity/5g/upsell-ux-flow.png)