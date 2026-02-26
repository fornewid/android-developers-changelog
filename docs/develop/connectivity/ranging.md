---
title: https://developer.android.com/develop/connectivity/ranging
url: https://developer.android.com/develop/connectivity/ranging
source: md.txt
---

Android 16 introduces the Ranging module, which provides a unified and
standardized interface for precise ranging between devices. You can use this
API surface to measure the distance and position of peer devices without
needing to handle each ranging technology individually.

The Ranging module supports the following technologies:

- [Ultra-wideband](https://developer.android.com/develop/connectivity/uwb)
- Bluetooth channel sounding
- [Wi-Fi NAN RTT](https://developer.android.com/develop/connectivity/wifi/wifi-rtt)
- Bluetooth RSSI ranging

## Ranging capabilities and availabilities

The [`RangingManager`](https://developer.android.com/reference/android/ranging/RangingManager) class provides apps with information
about the ranging technologies supported by the local device, as well as the
availability and capabilities of each technology. Apps can register for a
[`Callback`](https://developer.android.com/reference/android/ranging/RangingManager#registerCapabilitiesCallback(java.util.concurrent.Executor,%20android.ranging.RangingManager.RangingCapabilitiesCallback)) to receive updates on any changes to the availability
or capabilities of any supported technologies.

## Device roles

A device participating in a ranging session must be either an *initiator* or
a *responder* . The initiator device starts the ranging session with one or
more responder devices. A responder device responds to ranging requests from
only one initiator at a time. You can specify the role for a given device in
a ranging session with the [`RangingPreference`](https://developer.android.com/reference/android/ranging/RangingPreference) class.

## Ranging session types

When starting a ranging session between devices, it's often necessary to
establish an out-of-band (OOB) data transport to exchange parameters for the
session.

The Ranging module can handle OOB negotiations for you, but it also supports
custom OOB implementations.
![](https://developer.android.com/static/images/develop/connectivity/ranging_oob_flow.png) **Figure 1.** OOB flow for session types.

### Default OOB implementation

In this session type ([`RANGING_SESSION_OOB`](https://developer.android.com/reference/android/ranging/RangingConfig#RANGING_SESSION_OOB)), the Ranging module
handles OOB negotiations to start a ranging session. It selects suitable
parameters based on the ranging preferences provided by the app, and it uses
the appropriate technologies based on what both devices support. This session
type uses a standardized [`OOB specification`](https://source.android.com/partners/android-16/core/connect/ranging-oob-spec).

The Ranging module only defines the OOB data format and sequence to be used
to interact with a peer device. It doesn't handle peer device discovery or
connection establishment.

### Custom OOB implementation

In this session type ([`RANGING_SESSION_RAW`](https://developer.android.com/reference/android/ranging/RangingConfig#RANGING_SESSION_RAW)), the app bypasses the
Ranging module's OOB flow and handles its own OOB negotiation and parameters.
That means the app much determine which technologies the peer device
supports, negotiate ranging parameters, and begin the ranging session.

## Ranging preferences

Use a [`RangingPreference`](https://developer.android.com/reference/android/ranging/RangingPreference) object to specify the desired parameters
for a ranging session. This includes the following:

- **Device role.** This indicates whether the device will be the initiator or the responder.
- **Ranging configuration.** A [`RangingConfig`](https://developer.android.com/reference/android/ranging/RangingConfig) object specifies the ranging session type and other parameters needed to start a ranging session.
- **Session configuration.** A [`SessionConfig`](https://developer.android.com/reference/android/ranging/SessionConfig) object specifies parameters to be enforced on the ranging session such as measurement limit, sensor fusion, geofence configuration, and more.

## Ranging permission

The Ranging module requires a new unified permission
(`android.permission.RANGING`) to access all current and future ranging
technologies. This permission is in the `NEARBY_DEVICES_PERMISSIONS` list.

    <uses-permission android:name="android.permission.RANGING" />

## Restrictions and limitations

The Ranging module might restrict ranging due to several reasons, including
the following:

- Third-party apps are only allowed to perform background ranging with ultra-wideband, and only on [supported devices](https://developer.android.com/develop/connectivity/uwb#uwb-enabled_mobile_devices). Ranging in the background with other technologies is not allowed.
- Ranging is not allowed when the maximum number of concurrent ranging sessions by device has been reached.
- Ranging might be restricted due to system health concerns such as battery, performance, or memory.

The Ranging module also has the following known limitations:

- The Ranging module only supports delivery of ranging data to peer devices for ultra-wideband. For other technologies, the Ranging module only delivers ranging data to the initiator device.
- The Ranging module only supports dynamic addition of devices in [raw
  ranging mode](https://developer.android.com/develop/connectivity/ranging#custom), and only for ultra-wideband.
- The Ranging module doesn't support one-to-many ultra-wideband sessions for [default OOB implementations](https://developer.android.com/develop/connectivity/ranging#default). If you pass in multiple device handles, the module creates a one-to-one session for each peer device that supports ultra-wideband.

## Conduct a ranging session

To conduct a ranging session using the Ranging module, follow these steps:

1. Verify that all devices are operating on Android 16 or higher.
2. Request the `android.permission.RANGING` [permission](https://developer.android.com/develop/connectivity/ranging#permission) in the app manifest.
3. Assess the capabilities and availability of ranging technologies.
4. Discover a peer device for ranging operations.
5. Establish a connection for an out-of-band exchange, using either of the session types described in [Ranging session types](https://developer.android.com/develop/connectivity/ranging#session-types).
6. Initiate ranging and continuously acquire ranging data.
7. Terminate the ranging session.

The following code sample demonstrates these steps for both the initiator
role and the responder role.

### Kotlin

    class RangingApp {

        // Starts a ranging session on the initiator side.
        fun startRangingInitiator(
            context: Context,
            deviceHandle: DeviceHandle,
            executor: Executor,
            callback: RangingSessionCallback
        ) {

            // Get the RangingManager which is the entry point for ranging module.
            val manager = context.getSystemService(RangingManager::class.java)

            // Create a new RangingSession using the provided executor and callback.
            val session = manager.createRangingSession(executor, callback)

            // Create an OobInitiatorRangingConfig, which specifies the ranging parameters for
            // the initiator role.
            val config = OobInitiatorRangingConfig.Builder()
                .setFastestRangingInterval(Duration.ofMillis(100))
                .setSlowestRangingInterval(Duration.ofMillis(5000))
                .setRangingMode(RANGING_MODE_AUTO)
                .setSecurityLevel(SECURITY_LEVEL_BASIC)
                .addDeviceHandle(deviceHandle)
                .build()

            // Create a RangingPreference, which specifies the role (initiator) and
            // configuration for the ranging session.
            val preference =
                RangingPreference.Builder(DEVICE_ROLE_INITIATOR, config).build()

            // Start ranging session.
            session.start(preference)

            // If successful, the ranging data will be sent through callback#onResults

            // Stop ranging session
            session.stop()
        }

        // Starts a ranging session on the responder side.
        fun startRangingResponder(
            context: Context,
            deviceHandle: DeviceHandle,
            executor: Executor,
            callback: RangingSessionCallback
        ) {

            // Get the RangingManager which is the entry point for ranging module.
            val manager = context.getSystemService(RangingManager::class.java)

            // Create a new RangingSession using the provided executor and callback.
            val session = manager.createRangingSession(executor, callback)

            // Create an OobResponderRangingConfig, which specifies the ranging parameters for
            // the responder role.
            val config = OobResponderRangingConfig.Builder(deviceHandle).build()

            // Create a RangingPreference, which specifies the role (responder) and
            // configuration for the ranging session.
            val preference =
                RangingPreference.Builder(DEVICE_ROLE_RESPONDER, config).build()

            // Start the ranging session.
            session.start(preference)

            // Stop the ranging session
            session.stop()
        }
    }

### Java

    public class RangingApp {

        // Starts a ranging session on the initiator side.
        void startRangingInitiator(Context context, DeviceHandle deviceHandle, Executor executor, RangingSessionCallback callback) {

            // Get the RangingManager which is the entry point for ranging module.
            RangingManager manager = context.getSystemService(RangingManager.class);

            // Create a new RangingSession using the provided executor and callback.
            RangingSession session = manager.createRangingSession(executor, callback);

            // Create an OobInitiatorRangingConfig, which specifies the ranging parameters for
            // the initiator role.
            OobInitiatorRangingConfig config = new OobInitiatorRangingConfig.Builder()
                    .setFastestRangingInterval(Duration.ofMillis(100))
                    .setSlowestRangingInterval(Duration.ofMillis(5000))
                    .setRangingMode(RANGING_MODE_AUTO)
                    .setSecurityLevel(SECURITY_LEVEL_BASIC)
                    .addDeviceHandle(deviceHandle)
                    .build();

            // Create a RangingPreference, which specifies the role (initiator) and
            // configuration for the ranging session.
            RangingPreference preference =
                    new RangingPreference.Builder(DEVICE_ROLE_INITIATOR, config).build();

            // Start ranging session.
            session.start(preference);

            // If successful, the ranging data will be sent through callback#onResults

            // Stop ranging session
            session.stop();

        }

        // Starts a ranging session on the responder side.
        void startRangingResponder(Context context,  DeviceHandle deviceHandle, Executor executor, RangingSessionCallback callback) {

            // Get the RangingManager which is the entry point for ranging module.
            RangingManager manager = context.getSystemService(RangingManager.class);

            // Create a new RangingSession using the provided executor and callback.
            RangingSession session = manager.createRangingSession(executor, callback);

            // Create an OobResponderRangingConfig, which specifies the ranging parameters for
            // the responder role.
            OobResponderRangingConfig config = new OobResponderRangingConfig.Builder(  deviceHandle).build();

            // Create a RangingPreference, which specifies the role (responder) and
            // configuration for the ranging session.
            RangingPreference preference =
                    new RangingPreference.Builder(DEVICE_ROLE_RESPONDER, config).build();

            // Start the ranging session.
            session.start(preference);

            // Stop the ranging session
            session.stop();
        }
    }

## Sample app

For an end-to-end example of how to use the Ranging module, see the [sample
app](https://cs.android.com/android/platform/superproject/main/+/main:packages/modules/Uwb/ranging/test_app/) in AOSP. This sample app covers all ranging technologies
supported by the Ranging module and includes flows for both supported session
types.