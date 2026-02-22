---
title: https://developer.android.com/training/wearables/creating-app-china
url: https://developer.android.com/training/wearables/creating-app-china
source: md.txt
---

When creating Wear OS apps for China, you need to account for handsets without Google Play
services pre-installed. This page contains common changes that developers might need to adopt for
the Chinese market.

## Use the correct version of Google Play services

Google Play services version 10.2.0 provides worldwide support for the
[Fused Location Provider API](https://developers.google.cn/android/reference/com/google/android/gms/location/FusedLocationProviderClient) and the
[Data Layer API](https://developers.android.google.cn/training/wearables/data-layer). You must use this version of Google Play services if you use these APIs to
ensure support of a wider array of Wear OS devices in China. In other cases this dependency is
optional.

**Note:** Although Google Play services contains
APIs for Wear OS apps, Wear OS apps for China should continue to
use APIs related to `GoogleApiClient`; see
[Access the Wearable API](https://developers.google.com/android/guides/google-api-client#access_the_wearable_api).

#### Fused Location Provider API

If you use the Fused Location Provider API, include the following dependency in
the `build.gradle` file of your Wear OS module:  

### Groovy

```groovy
dependencies {
    ...
    implementation 'com.google.android.gms:play-services-location:10.2.0'
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("com.google.android.gms:play-services-location:10.2.0")
}
```

#### Data Layer API

|
| **Note:** The Data Layer API can send messages and synchronize data only with Android phones
| and Wear OS watches. If your Wear OS device is paired with an iOS device, the Data
| Layer API won't work.
|
|
| For this reason, don't use the Data Layer API as the primary way to
| communicate with a network. Instead, follow the same pattern in your Wear OS app
| as in a mobile app, with some minor differences as described in
| [Network access and sync on Wear OS](https://developer.android.com/training/wearables/data-layer/network-access).

If your app uses the Data Layer API, you need to add the following line to the
`build.gradle` file of your Wear OS module. The line requires use of the 10.2.0 version of
the client library.  

### Groovy

```groovy
dependencies {
    ...
    implementation 'com.google.android.gms:play-services-wearable:10.2.0'
    ...
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("com.google.android.gms:play-services-wearable:10.2.0")
    ...
}
```

Add the following line to the `build.gradle` file of
your mobile module. Replace the Google Play services dependency with a reference to the
10.2.0 version.  

### Groovy

```groovy
dependencies {
    ...
    implementation 'com.google.android.gms:play-services-wearable:10.2.0'
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("com.google.android.gms:play-services-wearable:10.2.0")
}
```

## Authentication

Before implementing authentication, review your use cases to see whether authentication is actually
needed. For example, for an app delivering the weather forecast, there likely is no need for
sign-in and thus for authentication.

If you do require authentication, we recommend using the
[AndroidX Oauth library](https://developer.android.com/reference/kotlin/androidx/wear/phone/interactions/authentication/package-summary).
This requires using the
[Authorization Code Grant with PKCE](https://developer.android.com/training/wearables/apps/auth-wear#oath) flow.
You can also use one of the other methods described in
[Authentication on wearables](https://developer.android.com/training/wearables/apps/auth-wear#auth-methods).
Use of the Wearable Support Library is not recommended.


For more information, see the
[Wear OS OAuth Sample](https://github.com/android/wear-os-samples/tree/main/WearOAuth)
on GitHub.

## Bridged notifications

[Bridged notifications](https://developers.android.google.cn/training/wearables/notifications) aren't supported in China. Phone notifications are bridged to
Wear OS only if the Wear OS device is connected to the phone using Bluetooth.

## Location and mapping coordinates compatibility

Use the [`FusedLocationProvider` (FLP)](https://developers.android.google.cn/training/articles/wear-location-detection#fused) to detect the user's location in China, as you would
for the rest of the world. This ensures that your app takes into account the best information
regardless of the watch hardware and the phone platform that the watch is paired to.
Using the FLP also adds battery optimization that is built into the Wear OS platform.

When integrating `FusedLocationProvider` with third-party map SDKs,
take into account the coordinates compatibility among providers.
`FusedLocationProvider` reports the location according to the
[WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System) standard.
Be sure to convert coordinate systems, as appropriate.

## Google Fit support

Google Fit's [accumulated-step counter, move minutes, and heart points](https://developers.google.cn/fit/android/history) are supported in China, with up to
seven days of history. You can access this without providing a user credential.

## Voice action support


The Wear OS platform provides several voice intents that are based on user actions such as _"Show
heart rate"_ or _"Set an alarm"_. This lets users say what they want to do and lets the system
figure out the best activity to start.

When users speak a voice action, your app can filter for the intent that is fired to start an
activity. To start a service in the background, show an activity as a visual cue and start the
service in the activity. Make sure to call [finish()](https://developer.android.com/reference/android/app/Activity#finish()) to get rid of the visual cue.

Here is a list of the voice intents supported by the Wear OS platform:

|---|---|---|
| **Category** | **Example** | **Intent spec** |
| Car hailing | 打车去三里屯 | **Action** [com.google.android.gms.actions.RESERVE_TAXI_RESERVATION](https://developers.google.com/android/reference/com/google/android/gms/actions/ReserveIntents#ACTION_RESERVE_TAXI_RESERVATION) **Extra** `to`: the recognized destination The extra is optional. |
| Set alarm | 设置一个明早七点的闹钟 | **Action** `android.intent.action.SET_ALARM` **Extras** `android.provider.AlarmClock.EXTRA_HOUR`: an integer with the hour of the alarm `android.provider.AlarmClock.EXTRA_MINUTES`: an integer with the minute of the alarm These extras are optional. Provide either, both, or neither of these extras. |
| Set timer | 设置一个三分钟的倒计时 | **Action** `android.intent.action.SET_TIMER` **Extras** `android.provider.AlarmClock.EXTRA_LENGTH`: an integer in the range of 1 to 86400 (the number of seconds in 24 hours), representing the length of the timer |
| Start stopwatch | 开始计时 | **Action** `com.google.android.wearable.action.STOPWATCH` |
| Start or stop a bike ride | 开始骑车 | **Action** `vnd.google.fitness.TRACK` **Mime type** `vnd.google.fitness.activity/biking` **Extras** `actionStatus`: a string with the value `ActiveActionStatus` when starting and `CompletedActionStatus` when stopping |
| Start or stop a run | 开始跑步 | **Action** `vnd.google.fitness.TRACK` **Mime type** `vnd.google.fitness.activity/running` **Extras** `actionStatus`: a string with the value `ActiveActionStatus` when starting, and `CompletedActionStatus` when stopping |
| Start or stop a workout | 开始锻炼 | **Action** `vnd.google.fitness.TRACK` **Mime type** `vnd.google.fitness.activity/other` **Extras** `actionStatus`: a string with the value `ActiveActionStatus` when starting, and `CompletedActionStatus` when stopping |
| Show heart rate | 查看心率 | **Action** `vnd.google.fitness.VIEW` **Mime type** `vnd.google.fitness.data_type/com.google.heart_rate.bpm` |
| Show step count | 查看步数 | **Action** `vnd.google.fitness.VIEW` **Mime type** `vnd.google.fitness.data_type/com.google.step_count.cumulative` |
| Navigation | 导航去三里屯 | **Action** [` android.intent.action.VIEW`](https://developer.android.google.cn/reference/android/content/Intent#ACTION_VIEW) **Data** geo:latitude,longitude?q=融科资讯中心 |


Voice Assistant can also use existing
[Android common intents](https://developer.android.google.cn/guide/components/intents-common)
to trigger certain behaviors where applicable.

## Emulator support

You can use the China version of the Wear OS emulator image to test your apps. This
is supported by Android Studio 3.0 and higher.

To test your apps on the China version of the emulator, follow these steps:

1. Install the Android Emulator.
2. Download the Wear OS for China images from the SDK manager. Use the version for Wear OS 3.5 (API level 30).
3. Choose the Wear OS for China image when creating an AVD profile.
4. Run the Wear OS for China emulator for development.
![](https://developer.android.com/static/wear/images/emulator-ch.png) ![](https://developer.android.com/static/wear/images/emulator-screen.png)
5. **Figure 1.** Examples of the China version of the Wear OS emulator.

This version of the Wear OS emulator comes with several pre-installed apps:

- Ambient mode
- Contacts
- Google Handwriting Input
- Google Play services
- Health Services for Wear OS
- Hotword recognition for LE devices
- Pinyin
- Play Store (adapted for devices in China)
- Pocketwatch
- TalkBack
- Watchfaces (both analog and digital versions)
- Wear Core Services

## Initiate an app-specific Bluetooth and Wi-Fi channel

Wear OS automatically routes network requests. In most cases, there's no requirement
for the app to open an app-specific Bluetooth and Wi-Fi channel.

If an app does request an app-specific Bluetooth and Wi-Fi channel in China, the request
silently fails. Instead, a dialog displays
asking the user for confirmation. If the user confirms, the channel opens. This happens every
time, not just on first use. `BluetoothAdapter.enable()` or
`WifiManager.setEnabled(true)` is
called.

**Note:** For an app targeting
Android 10 (API level 29) or higher to call
`WifiManager.setEnabled()`, it must be a system app or a
[device policy controller (DPC)](https://developer.android.com/work/dpc/build-dpc).

## Permission review mode

In China, Wear OS for China devices run in Permission Review Mode, which
imposes some limits on how to use apps with a `targetApiLevel` lower than 23. Review the following limits:

- Even though permissions are granted at installation time, when an app with a `targetApiLevel` lower than 23 starts for the first time, a dialog appears asking the user to confirm permissions for this app.
- Components in the app, such as broadcast receivers, services, and activities don't respond to corresponding events before the app is used for the first time.

As a result, we recommend you use `targetApiLevel` 23 or higher
and adopt the
[app permissions
best practices](https://developers.android.google.cn/training/permissions/usage-notes).

## Use other Google Play services APIs

If your app uses [Google Play services APIs](https://developers.android.google.cn/reference/android/support/wearable/packages) other than the Wearable API, then your app needs to check whether
these APIs are available to use during runtime and respond appropriately.
There are two ways to check the availability of Google Play service APIs:

1. Use a separate [GoogleApiClient](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient) instance for connecting to other APIs. This interface contains callbacks to alert your app to the [success](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient.ConnectionCallbacks) or [failure](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient.OnConnectionFailedListener) of the connection. In the case of failed connection, the [ConnectionResult](https://developers.google.cn/android/reference/com/google/android/gms/common/ConnectionResult) shows [API_UNAVAILABLE](https://developers.google.cn/android/reference/com/google/android/gms/common/ConnectionResult#API_UNAVAILABLE). To learn how to handle connection failures, see [Access Google APIs](https://developers.google.cn/android/guides/api-client).
2. Use the [`addApiIfAvailable()`](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient.Builder#public-googleapiclient.builder-addapiifavailable-apio-api,-o-options,-scope...-scopes) method of [`
   GoogleApiClient.Builder`](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient.Builder) to connect to the required APIs. After the [`onConnected()`](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient.ConnectionCallbacks#onConnected(android.os.Bundle)) callback fires, use the [`hasConnectedApi()`](https://developers.google.cn/android/reference/com/google/android/gms/common/api/GoogleApiClient#hasConnectedApi(com.google.android.gms.common.api.Api%3C?%3E)) method to ensure that each of the requested APIs is connected correctly.

## Distribute apps in China

To effectively reach users of Wear OS for China, you can distribute through
third-party Wear OS app stores such as the following:

- [Galaxy Store](https://support-cn.samsung.com/App/DeveloperChina/home/index) for Samsung devices
- [Xiaomi Store](https://dev.mi.com/console/app/phone.html) for Xiaomi devices
- [Mobvoi](http://developer.chumenwenwen.com/en/plan/android-wear.html) for all other devices