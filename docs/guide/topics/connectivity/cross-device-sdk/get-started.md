---
title: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/get-started
url: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/get-started
source: md.txt
---

The Cross device SDK Developer Preview is distributed through an [open-source
project](https://github.com/google/cross-device-sdk). This preview is available for the developer community to prototype and
validate multidevice experiences but is not intended for use in production
applications.
| **Note:** Quick Share must be turned on to use the Cross device SDK. See [Share files and links with nearby devices](https://support.google.com/android/answer/9286773) to learn more.

## Set up Google Play Services

Before you start coding,
[ensure Google Play Services is installed](https://developers.google.com/android/guides/setup#check-whether-installed).
The Cross device SDK is in Developer Preview and is available only through the
Google Play Services Beta Program. See
[this guide](https://developers.google.com/android/guides/beta-program) on how
to enroll in the Beta Program.

Once you enroll in the Beta Program and install the appropriate beta version of
Google Play Services, you're ready to begin developing multidevice experiences
with the Cross device SDK.

## Dependencies and permissions

First, open your app module `build.gradle` file and add a dependency on the
Cross device SDK as follows:

    dependencies {
        implementation 'com.google.ambient.crossdevice:crossdevice:0.1.0-preview01'
    }

During Developer Preview, the API is subject to change, so check release notes
regularly to ensure you're using the latest version of the Cross device SDK.

One of the benefits of using the Cross device SDK is that it abstracts away
local discovery, such as `BLUETOOTH_CONNECT`, `BLUETOOTH_SCAN`, and
`ACCESS_FINE_LOCATION`.
| **Note:** You still have to declare and request runtime permissions required by your app features and API outside of the Cross device SDK. For instance, you might need `BLUETOOTH_SCAN` permission to perform a Bluetooth scan outside of the Cross device SDK.

## Cross device APIs

Each API in the Cross device SDK is aimed at solving a common task within a
multidevice framework:

- Device discovery: Easily find nearby devices, authorize peer-to-peer communication, and start the target application on the receiving device.
- Secure communications: Enable encrypted, low-latency, bi-directional data sharing between authorized devices.
- Multidevice sessions: Transfer or extend an application's user-experience across devices.

These APIs are available through the `Discovery` and `Sessions` classes:

### Kotlin

```kotlin
val discovery = Discovery.create(context)
val sessions = Sessions.create(context)
```

### Java

```java
Discovery discovery = Discovery.create(context);
Sessions sessions = Sessions.create(context);
```

You can learn more about the specific uses of these APIs in the following
sections, or refer to our
[sample app repository](https://github.com/android/connectivity-samples).
| **Note:** The Cross device SDK is asynchronous by design. If you are unfamiliar with asynchronous operations, we encourage you to learn about [`Coroutines`](https://kotlinlang.org/docs/coroutines-guide.html) for Kotlin or [`ListenableFuture`](https://developer.android.com/guide/background/listenablefuture) for Java.

## Sample Applications

We've prepared a number of apps to demonstrate the Cross device SDK in action.
These sample apps are built around a simple Rock, Paper, Scissors game as an
intuitive and interactive way to familiarize yourself with the APIs. We
encourage you to explore and modify the sample code to see how to use:

- Device Discovery
- Secure Connections
- Sessions Transfer
- Shared Sessions

Check out
[Cross-device Rock, Paper, Scissors on Github](https://github.com/android/connectivity-samples/tree/main/CrossDeviceRockPaperScissors).