---
title: https://developer.android.com/develop/connectivity/bluetooth/profiles
url: https://developer.android.com/develop/connectivity/bluetooth/profiles
source: md.txt
---

The Bluetooth API includes support for working with Bluetooth profiles. A
Bluetooth profile is a wireless interface specification for Bluetooth-based
communication between devices, such as the Hands-Free profile. For a mobile
device to connect to a wireless headset, both devices must support the
Hands-Free profile.

The Bluetooth API provides implementations for the following Bluetooth
profiles:

- **Headset** . The Headset profile provides support for Bluetooth headsets to be used with mobile phones. Android provides the [`BluetoothHeadset`](https://developer.android.com/reference/android/bluetooth/BluetoothHeadset) class, which is a proxy for controlling the Bluetooth Headset Service. This includes both Bluetooth Headset and Hands-Free (v1.5) profiles. The `BluetoothHeadset` class includes support for AT commands. For more on this topic, see [Vendor-specific AT commands](https://developer.android.com/develop/connectivity/bluetooth/profiles#at-commands).
- **A2DP** . The Advanced Audio Distribution Profile (A2DP) profile defines how high-quality audio can be streamed from one device to another over a Bluetooth connection. Android provides the [`BluetoothA2dp`](https://developer.android.com/reference/android/bluetooth/BluetoothA2dp) class, which is a proxy for controlling the Bluetooth A2DP Service.
- **Health Device** . Android provides support for the Bluetooth Health Device Profile (HDP). This lets you create apps that use Bluetooth to communicate with health devices that support Bluetooth, such as heart-rate monitors, blood meters, thermometers, scales, and so on. For a list of supported devices and their corresponding device data specialization codes, see [Bluetooth's HDP
  Device Data
  Specializations](https://www.bluetooth.com/specifications/assigned-numbers/health-device-profile). These values are also referenced in the ISO/IEEE 11073-20601 \[7\] specification as `MDC_DEV_SPEC_PROFILE_*` in the Nomenclature Codes Annex. For more information about HDP, see [Health Device Profile](https://developer.android.com/develop/connectivity/bluetooth/profiles#health-profile).

Here are the basic steps for working with a profile:

1. Get the default adapter, as described in [Bluetooth setup](https://developer.android.com/develop/connectivity/bluetooth/setup).
2. Set up a [`BluetoothProfile.ServiceListener`](https://developer.android.com/reference/android/bluetooth/BluetoothProfile.ServiceListener). This listener notifies [`BluetoothProfile`](https://developer.android.com/reference/android/bluetooth/BluetoothProfile) clients when they have been connected to or disconnected from the service.
3. Use [`getProfileProxy()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getProfileProxy(android.content.Context,%20android.bluetooth.BluetoothProfile.ServiceListener,%20int)) to establish a connection to the profile proxy object associated with the profile. In the following example, the profile proxy object is an instance of `BluetoothHeadset`.
4. In [`onServiceConnected()`](https://developer.android.com/reference/android/bluetooth/BluetoothProfile.ServiceListener#onServiceConnected(int,%20android.bluetooth.BluetoothProfile)), get a handle to the profile proxy object.
5. Once you have the profile proxy object, use it to monitor the state of the connection and perform other operations that are relevant to that profile.

The following code snippet shows how to connect to a `BluetoothHeadset` proxy
object so that you can control the Headset profile:

### Kotlin

```kotlin
var bluetoothHeadset: BluetoothHeadset? = null

// Get the default adapter
val bluetoothAdapter: BluetoothAdapter? = BluetoothAdapter.getDefaultAdapter()

private val profileListener = object : BluetoothProfile.ServiceListener {

    override fun onServiceConnected(profile: Int, proxy: BluetoothProfile) {
        if (profile == BluetoothProfile.HEADSET) {
            bluetoothHeadset = proxy as BluetoothHeadset
        }
    }

    override fun onServiceDisconnected(profile: Int) {
        if (profile == BluetoothProfile.HEADSET) {
            bluetoothHeadset = null
        }
    }
}

// Establish connection to the proxy.
bluetoothAdapter?.getProfileProxy(context, profileListener, BluetoothProfile.HEADSET)

// ... call functions on bluetoothHeadset

// Close proxy connection after use.
bluetoothAdapter?.closeProfileProxy(BluetoothProfile.HEADSET, bluetoothHeadset)
```

### Java

```java
BluetoothHeadset bluetoothHeadset;

// Get the default adapter
BluetoothAdapter bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

private BluetoothProfile.ServiceListener profileListener = new BluetoothProfile.ServiceListener() {
    public void onServiceConnected(int profile, BluetoothProfile proxy) {
        if (profile == BluetoothProfile.HEADSET) {
            bluetoothHeadset = (BluetoothHeadset) proxy;
        }
    }
    public void onServiceDisconnected(int profile) {
        if (profile == BluetoothProfile.HEADSET) {
            bluetoothHeadset = null;
        }
    }
};

// Establish connection to the proxy.
bluetoothAdapter.getProfileProxy(context, profileListener, BluetoothProfile.HEADSET);

// ... call functions on bluetoothHeadset

// Close proxy connection after use.
bluetoothAdapter.closeProfileProxy(bluetoothHeadset);
```

### Vendor-specific AT commands

Apps can register to receive system broadcasts of predefined vendor-specific AT
commands sent by headsets (such as a Plantronics +XEVENT command). For example,
an app could receive broadcasts that indicate a connected device's battery level
and could notify the user or take other action as needed. Create a broadcast
receiver for the
[`ACTION_VENDOR_SPECIFIC_HEADSET_EVENT`](https://developer.android.com/reference/android/bluetooth/BluetoothHeadset#ACTION_VENDOR_SPECIFIC_HEADSET_EVENT)
intent to handle vendor-specific AT commands for the headset.

## Health Device Profile

Android supports the Bluetooth Health Device Profile (HDP). The Bluetooth Health
API includes the classes
[`BluetoothHealth`](https://developer.android.com/reference/android/bluetooth/BluetoothHealth),
[`BluetoothHealthCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothHealthCallback),
and
[`BluetoothHealthAppConfiguration`](https://developer.android.com/reference/android/bluetooth/BluetoothHealthAppConfiguration),
which are described in [Key classes and
interfaces](https://developer.android.com/develop/connectivity/bluetooth#key-classes).

> [!CAUTION]
> **Caution:** The Health Device Profile (HDP) and MCAP protocols are no longer used. New apps should use Bluetooth Low Energy based solutions such as [`BluetoothGatt`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt), [`BluetoothAdapter.listenUsingL2capChannel()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#listenUsingL2capChannel()), or [`BluetoothDevice#createL2capChannel(int)`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#createL2capChannel(int)).

When using the Bluetooth Health API, it's helpful to understand these key HDP
concepts:

Source
:   A health device, such as a weight scale, glucose meter, or thermometer, which
    transmits medical data to a smart device, such as an Android phone or tablet.

Sink
:   The smart device that receives the medical data. In an HDP app, the
    sink is represented by a `BluetoothHealthAppConfiguration` object.

Registration
:   The process used to register a sink for communicating with a particular health
    device.

Connection
:   The process used to open a channel between a health device (source) and a
    smart device (sink).

### Create an HDP app

Here are the basic steps involved in creating an HDP app:

1. Get a reference to the `BluetoothHealth` proxy object. As with regular
   headset and A2DP profile devices, you must call `getProfileProxy()` with a
   `BluetoothProfile.ServiceListener` and the
   [`HEALTH`](https://developer.android.com/reference/android/bluetooth/BluetoothProfile#HEALTH) profile type
   to establish a connection with the profile proxy object.

2. Create a `BluetoothHealthCallback` and register an app configuration
   (`BluetoothHealthAppConfiguration`) that acts as a health sink.

3. Establish a connection to a health device.

   > [!NOTE]
   > **Note:** Some devices initiate the connection automatically. It is unnecessary to carry out this step for those devices.

4. When connected successfully to a health device, read and write to the health
   device using the file descriptor. The received data needs to be interpreted
   using a health manager, which implements the [IEEE 11073
   specifications](https://standards.ieee.org/standard/11073-10207-2017.html).

5. When done, close the health channel and unregister the app. The channel also
   closes when there is extended inactivity.