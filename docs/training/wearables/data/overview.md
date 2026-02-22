---
title: https://developer.android.com/training/wearables/data/overview
url: https://developer.android.com/training/wearables/data/overview
source: md.txt
---

![The cloud-based node is controlled by a Google-owned server](https://developer.android.com/static/images/training/wear/data-layer-node-network.svg) **Figure 1.** A sample of network of nodes with handheld and Wear OS devices.

The Wearable Data Layer API, which is part of Google Play services, provides a
communication channel between wearable devices (like smart watches) and
connected handheld devices (usually smartphones). It is a way to synchronize and
transfer data between the devices.
**Note:** This API is only available on Wear OS watches and
paired Android devices. For Wear OS watches paired with iOS phones, apps can
query other cloud-based APIs if internet connectivity is available. For more
information on these other APIs, visit
[Network access and sync on
Wear OS](https://developer.android.com/training/wearables/data/network-access).
**Caution:** Because the data layer APIs are designed for
communication between handhelds and wearables, these are the only APIs you can
use to set up communication between these devices. For example, don't try to
open low-level sockets to create a communication channel.

## Common use cases

The Data Layer API is particularly useful for fitness and media use cases.

### Fitness apps

Sending exercise data from Wear OS app to mobile app Fitness apps often need to
write the exercise data captured by a watch to a mobile app or to [Health
Connect](https://developer.android.com/health-and-fitness/guides/health-connect). If using the Data Layer API to transfer data, use a
[message client](https://developer.android.com/training/wearables/data/client-types#message-client) to send exercise data from the Wear OS app to the mobile app
in order to write to Health Connect.

#### Stream live data to the mobile device during a home workout

A [common home workout scenario](https://medium.com/androiddevelopers/wear-os-home-workouts-with-health-services-b9951fa9e0dc) is streaming heart rate data from a Wear OS
device to a mobile device and showing the user up-to-date heart rate information
on their mobile device's screen. To stream this data, use a [channel client](https://developer.android.com/training/wearables/data/client-types#channel-client).

### Media apps

To control a media player through the action of pause/resume/start/end from the
watch to the phone, use a [message client](https://developer.android.com/training/wearables/data/client-types#message-client).

## Options for communication

Data is transferred in one of the following ways:

1. **Directly**, when there is an established Bluetooth connection between the Wear OS device and another device.
2. **Over an available network**, such as LTE or Wi-Fi, using a network node on Google's servers as an intermediary.

All Data Layer clients may exchange data either using Bluetooth or using the
cloud, depending on connections available to the devices. Assume that data
transmitted using Data Layer may at some point use Google-owned servers.

### Bluetooth

When devices are connected using Bluetooth, Data Layer uses this connection.
There is a single encrypted channel between the devices, using standard
Bluetooth encryption, managed by Google Play services.

### Cloud

Data is automatically routed through Google Cloud when Bluetooth is unavailable.
All data transferred through Google Cloud is end-to-end encrypted.

## Security of communications

Google Play services enforces the following restrictions to provide more secure
communication between the app installed on a Wear OS device and the same app
installed on a nearby handheld device:

- The package name must match across devices.
- The signature of the package must match across devices.

No other apps have access to the data regardless of connection type.

## Setup

The Wearable Data Layer API has the following dependencies:

- The latest version of [Google Play services](https://developers.google.com/android).
- A Wear OS device or Wear OS emulator.

Include the following dependency in the build.gradle file of your Wear module:

    dependencies {
        ...
        implementation("com.google.android.gms:play-services-wearable:19.0.0")
    }

### Facilitate the initial pairing process

[Horologist](https://github.com/google/horologist) provides several helper libraries on top of platform APIs.
It includes a [data layer library](https://google.github.io/horologist/datalayer-helpers-guide/) that helps establish a connection between
a mobile device and a Wear OS device. Additionally, it provides convenient APIs
to do the following:

- Install the app on the other device.
- Launch the app on the other device.
- Launch a specific activity on the other device.
- Launch the companion app.

## Access the data layer

To call the Data Layer API, use the [`Wearable`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable) class to get instances of
the various client classes, such as [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) and [`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient).

For more information, refer to the [DataLayer sample](https://github.com/android/wear-os-samples/tree/main/DataLayer).

## Use a minimal client

To create a client, see the following example code:

### Kotlin

```kotlin
val dataClient: DataClient = Wearable.getDataClient(context)
```

### Java

```java
DataClient dataClient = Wearable.getDataClient(context);
```

> [!CAUTION]
> **Caution:** Before using the Wearable Data Layer API, check that it's available on a device; otherwise, an exception occurs. Use the [`GoogleApiAvailability`](https://developers.google.com/android/reference/com/google/android/gms/common/GoogleApiAvailability) class, as implemented in [Horologist](https://github.com/google/horologist/blob/release-0.5.x/datalayer/core/src/main/java/com/google/android/horologist/data/WearableApiAvailability.kt#L29).

The context can be any valid Android context. If you are using the API within
the scope of an `Activity`, use the `getDataClient()` method of the `Wearable`
class. This lets certain interactions appear as dialogs rather than as
notifications, such as when the user is asked to update their version of Google
Play services.

By default, callbacks to listeners are made on the app's main UI thread. To have
callbacks made on a different thread, use a [`WearableOptions`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable.WearableOptions) object to
specify a custom `Looper`:

### Kotlin

```kotlin
runBlocking {
    Wearable.getDataClient(context, options)
}
```

### Java

```java
WearableOptions options = new WearableOptions.Builder().setLooper(myLooper).build();
DataClient dataClient = Wearable.getDataClient(context, options);
```

For more information, see the [`WearableOptions.Builder`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable.WearableOptions.Builder) reference.

## Recreate client instances as necessary

Wearable API clients, such as [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) and [`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient), are
inexpensive to create. So instead of holding onto the clients, recreate them as
you need them, using the style that suits your app.

The client state, such as the set of registered listeners, is shared across all
clients and is preserved if Google Play services is updated while an app is
running.