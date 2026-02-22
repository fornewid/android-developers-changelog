---
title: https://developer.android.com/training/wearables/apps/standalone-apps
url: https://developer.android.com/training/wearables/apps/standalone-apps
source: md.txt
---

We recommend that Wear OS apps work independently of a phone so users can
complete tasks on a watch without access to an Android or iOS phone.
If your watch app
requires phone interaction, you must mark your Wear OS app as non-standalone
and take steps to ensure that the user has the phone app available.

## Plan your app


You can use [Android App Bundle](https://developer.android.com/guide/app-bundle)
to automatically generate optimized Android Package Kits (APKs) for each user's device configuration under the same
application listing. This lets users download only the code and resources they need to
run your app.


For information about setting up your app for distribution through
the Google Play Store, see [Package and distribute Wear OS Apps](https://developer.android.com/training/wearables/packaging) and the guide to getting started with
[Android App Bundles](https://developer.android.com/guide/app-bundle#get_started).


For new apps, the target API level must be 30 or higher. For more information, see
[Meet Google Play's target API
level requirement](https://developer.android.com/google/play/requirements/target-sdk). Set the
`targetSdkVersion` to API level 30 (Wear OS 3) to help ensure that your app works well
on the latest platform version.


For information about network requests and high-bandwidth network access,
see [Network access and sync on Wear OS](https://developer.android.com/training/wearables/data-layer/network-access).

### Define an app as a Wear OS app


You must define the `https://developer.android.com/guide/topics/manifest/uses-feature-element` tag in your app's Android manifest file.
To indicate that it is a watch app, add an entry like the following:

```xml
<uses-feature android:name="android.hardware.type.watch" />
```

### Identify an app as standalone or non-standalone


A watch app is considered either standalone or non-standalone:

- **Standalone**: a completely independent app that doesn't require a phone app for core features. Although "Open on phone" prompts are acceptable, the app must provide alternative means for users to complete an app function---such as a shortlink or QR code---without depending on a tethered phone.
- **Non-standalone**: a dependent app that requires an app on a phone or another device for core features. This option is best for apps when they can't easily provide an alternative means---such as a QR code or shortlink---for completing a core app function, such as authentication.

**Note:** Even for non-standalone apps, users can install the
Wear OS app before the mobile app. So if your Wear OS app detects that a
nearby handheld device lacks the necessary companion app, prompt the user
to install the companion app.

Google validates the accuracy of an app's standalone status during app
serving. This value affects the visibility of apps within the Play Store on
untethered devices, such as Wear OS devices that aren't paired to handheld
devices. Non-standalone apps---as well as apps that developers incorrectly
designate as "standalone"---aren't available to users on these untethered
devices.


In your Wear OS app, set the value of `
https://developer.android.com/guide/topics/manifest/meta-data-element` element `com.google.android.wearable.standalone`
in the Android manifest file to declare whether your app is standalone or non-standalone.


If your watch app is a completely independent, standalone app, indicate
this to the Google Play store by setting the
value of `com.google.android.wearable.standalone` to `true`:

```xml
<meta-data
    android:name="com.google.android.wearable.standalone"
    android:value="true" />
```


If your watch app is non-standalone and depends on another app for core features,
set the value of `com.google.android.wearable.standalone` to
`false`. This signifies that the watch app requires another device, but doesn't
affect your app promotion on the Google Play Store.


**Note:**
Even if the value of `com.google.android.wearable.standalone` is
`false`, the watch
app can be installed before the phone app is installed.
Therefore, if your watch app
[detects](https://developer.android.com/training/wearables/apps/standalone-apps#detecting-your-app) that a companion phone
lacks the necessary phone app, as described on this page,
prompt the user to install the phone app.

## Shared code and data storage


Code can be shared between a Wear OS app and a phone app.
For example, common code for networking can be in a shared library.


Optionally, code
that is specific to a form factor can be in a separate module.


You can use standard Android storage APIs to store data locally, as you
would on a phone. For example, you can use the
[SharedPreferences
APIs](https://developer.android.com/reference/android/content/SharedPreferences) or the [Room](https://developer.android.com/training/data-storage/room)
persistence library.

## Detect your app on another device


Your watch app and corresponding phone app
can each detect whether the other app is available.


Your phone and watch apps can use the
[`CapabilityClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/CapabilityClient) to advertise their presence
to a paired device. They can do so statically or dynamically.


When an app
is on a node in a user's Wear OS network, such as on a phone, paired watch, or
in the cloud, the `CapabilityClient` lets other
apps detect it. For more information, see
[Advertise capabilities](https://developer.android.com/training/wearables/data-layer/messages#advertise-capabilities).


If one of your apps can't detect the other, you can prompt
the user to open the Play Store listing on the affected device.
This is a solution for watch apps that require their
companion phone app's presence to function properly.


You must check whether the Play Store is available on
the device, because not all phones---such as iPhones---support the
Play Store.


The following sections describe best practices for two scenarios:

- Your standalone watch app needs your phone app.
- Your phone app needs your standalone watch app.


You can also review the [Datalayer helpers sample](https://github.com/google/horologist/tree/v0.6.10/datalayer/sample), which shows how to use the
[Datalayer helpers libraries](https://google.github.io/horologist/datalayer-helpers-guide/), part of [Horologist](https://google.github.io/horologist/). These helpers let you monitor the connection between a handheld
device and a Wear OS device.
For more information
about the classes described in the following section, see the
[Wear OS API reference](https://developer.android.com/reference/packages-wearable-support).
That reference also includes information about the
[`PhoneTypeHelper`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper) class, which contains a
[`getPhoneDeviceType()`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#getPhoneDeviceType(android.content.Context)) method that lets your
Wear OS app check whether a companion phone is an Android or iOS device.

### Specify capability names for detecting your apps


For the app corresponding to each device type, either watch or phone, specify a
unique string for the capability name in the
`res/values/wear.xml` file.


For example, in your mobile module, the `wear.xml` file
could include the following:

```xml
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@array/android_wear_capabilities">
    <string-array name="android_wear_capabilities">
        <item>verify_remote_example_phone_app</item>
    </string-array>
</resources>
```


In your Wear OS module, the `wear.xml` file includes a
different value for the capability name,
such as the following:

```xml
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@array/android_wear_capabilities">
    <string-array name="android_wear_capabilities">
        <item>verify_remote_example_wear_app</item>
    </string-array>
</resources>
```


For more information, see [Advertise capabilities](https://developer.android.com/training/wearables/data-layer/messages#advertise-capabilities).

### App detection and opening a URL from a watch

Your watch app can detect whether a user's companion phone has your
phone app. Follow these steps:

1. Use the `CapabilityClient` to check whether your phone app is installed on the paired phone. For more information, see the [Datalayer helpers sample](https://github.com/google/horologist/tree/v0.6.10/datalayer/sample) on GitHub.
2. If your phone app isn't installed on the phone, use the [`PhoneDeviceType.getPhoneDeviceType()`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#getPhoneDeviceType(android.content.Context)) method to check the type of the phone. See the following section for details.
3. If [`PhoneDeviceType.DEVICE_TYPE_ANDROID`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_ANDROID()) is returned, the phone is an Android phone. Call [`RemoteActivityHelper.startRemoteActivity()`](https://developer.android.com/reference/kotlin/androidx/wear/remote/interactions/RemoteActivityHelper#startRemoteActivity(android.content.Intent,kotlin.String)) on the Wear OS device to open the Play Store on the phone. Use the market URI for your phone app, which might be different from your Wear app's URI. For example, use a market URI such as: `market://details?id=com.example.android.wearable.wear.finddevices`.
4. If
   [`PhoneDeviceType.DEVICE_TYPE_IOS`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_IOS())
   is returned, the phone is an iOS phone with no Play
   Store available. Open the App Store on the iPhone
   by calling `RemoteActivityHelper.startRemoteActivity()` on the Wear
   OS device. You can specify your app's iTunes URL, such as
   `https://itunes.apple.com/us/app/yourappname`.

   From Wear OS, you cannot programmatically determine whether
   your phone app is installed on an iOS device. As a best practice, provide a
   mechanism to the user to manually trigger the
   opening of the App Store.


**Note** : Use the `RemoteActivityHelper` API previously described to
specify that any URL be opened on the phone from the watch,
and that no phone app is required.

### Details for detecting the type of paired phone


Here is a snippet that uses the `getPhoneDeviceType()` method to
check the type of phone to which the watch is paired:

```kotlin
var phoneDeviceType: Int = PhoneTypeHelper.getPhoneDeviceType(this)
```


The value returned by the `getPhoneDeviceType()`
method is one of the following:

| **Return value** | **Description** |
|---|---|
| [`DEVICE_TYPE_ANDROID`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_ANDROID()) | The companion phone is an Android device. |
| [`DEVICE_TYPE_IOS`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_IOS()) | The companion phone is an iOS device. |
| [`DEVICE_TYPE_UNKNOWN`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_UNKNOWN()) | The companion phone is an unknown device. |
| [`DEVICE_TYPE_ERROR`](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/PhoneTypeHelper#DEVICE_TYPE_ERROR()) | An error occurred in determining the type of the paired phone; another check should be made later. |

### App detection starting from an Android phone


Your Android phone can detect whether a user's Wear OS devices have your
watch app. Follow these steps:

1. Using the [`NodeClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/NodeClient), find all watches connected to the user's phone. For more information, see the [Datalayer helpers sample](https://github.com/google/horologist/tree/v0.6.10/datalayer/sample) on GitHub.
2. Using the `CapabilityClient`, check which of the user's watches has your app installed.
3. If your app isn't installed on all of the user's watches, let the user open the Play Store on the remaining Wear OS devices from the phone using the `RemoteActivityHelper.startRemoteActivity()` method. Use the market URI for the Wear OS app, which might be different from your phone app's URI. For example, use a market URI such as: `market://details?id=com.example.android.wearable.wear.finddevices`.

## Location data for watches paired to iPhones


For watches paired with iPhones, use the
[Fused Location Provider (FLP)](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient) to get location data on the watch.
For more information, see
[Detect location on Wear OS](https://developer.android.com/training/articles/wear-location-detection).


If the companion phone is available, FLP uses the companion phone for
location data.

## Obtain only necessary data


Generally, when obtaining data from the internet, get only the
necessary data. Otherwise, you may introduce unnecessary latency, memory
use, and battery use.


When a watch is connected over a Bluetooth LE connection, your app might
have access to a bandwidth of only 4 kilobytes per second, depending
on the watch. Therefore, the following steps are recommended:

- Audit your network requests and responses for extra data that is only needed for a phone app.
- Shrink large images before you send them over a network to a watch.


For cases where a high-bandwidth network is needed, see
[High-bandwidth network access](https://developer.android.com/training/wearables/data-layer/network-access#high-bandwidth-network-access).

## Additional code samples


The
[Datalayer helpers sample](https://github.com/google/horologist/tree/v0.6.10/datalayer/sample) further demonstrates the use of the APIs covered on this page.