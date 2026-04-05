---
title: Manage calls using the Telecom API  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Manage calls using the Telecom API Stay organized with collections Save and categorize content based on your preferences.




This guide covers how to route audio for Bluetooth devices using the
[Telecom API](/develop/connectivity/telecom) and set the connection for
VoIP calls. Read the
[Build a calling app](/develop/connectivity/telecom/selfManaged) guide
before continuing.

By using the [`ConnectionService`](/reference/android/telecom/ConnectionService)
and [`Connection`](/reference/android/telecom/Connection) classes, you can access
the audio state and a list of available Bluetooth devices, and can route
audio to a selected Bluetooth device.

## VoIP Connection and ConnectionService

Create a `VoIPConnection` class that extends from
[`Connection`](/reference/android/telecom/Connection). This class controls the state of the current call. As the
[Build a calling app](/develop/connectivity/telecom/selfManaged) guide
states, make this a self-managed application and set the audio mode for a VoIP
application.

### Kotlin

```
class VoIPConnection : Connection() {
  init {
    setConnectionProperties(PROPERTY_SELF_MANAGED)
    setAudioModeIsVoip(true)
  }
}
```

### Java

```
public class VoIPConnection extends Connection {
  public VoIPConnection() {
    setConnectionProperties(PROPERTY_SELF_MANAGED);
    setAudioModeIsVoip(true);
  }
}
```

Next, return an instance of this class in
[`ConnectionService`](/reference/android/telecom/ConnectionService) when an
incoming or outgoing call occurs.

### Kotlin

```
class VoIPConnectionService : ConnectionService() {
  override fun onCreateOutgoingConnection(
    connectionManagerPhoneAccount: PhoneAccountHandle,
    request: ConnectionRequest,
  ): Connection {
    return VoIPConnection()
  }
}
```

### Java

```
public class VoIPConnectionService extends ConnectionService {
  @Override
  public Connection onCreateOutgoingConnection(PhoneAccountHandle connectionManagerPhoneAccount, ConnectionRequest request) {
    return new VoIPConnection();
  }
}
```

Ensure the manifest correctly points to the `VoIPConnectionService` class.

```
<service android:name=".voip.TelegramConnectionService" android:permission="android.permission.BIND_TELECOM_CONNECTION_SERVICE">
  <intent-filter>
    <action android:name="android.telecom.ConnectionService"/>
  </intent-filter>
</service>
```

With these custom [`Connection`](/reference/android/telecom/Connection) and
[`ConnectionService`](/reference/android/telecom/ConnectionService) classes, you
can control which device and what type of audio routing you wish to use during a
call.

## Get the current audio state

To get the current audio state, call
[`getCallAudioState()`](/reference/android/telecom/Connection#getCallAudioState()).
[`getCallAudioState()`](/reference/android/telecom/Connection#getCallAudioState())
returns if the device is streaming using Bluetooth, Earpiece, Wired, or
Speaker.

```
mAudioState = connection.getCallAudioState()
```

## On State Changed

Subscribe to changes in CallAudioState by overriding
[`onCallAudioStateChanged()`](/reference/android/telecom/Connection#onCallAudioStateChanged(android.telecom.CallAudioState)).
This alerts you of any changes to the state.

### Kotlin

```
fun onCallAudioStateChanged(audioState: CallAudioState) {
  mAudioState = audioState
}
```

### Java

```
@Override
public void onCallAudioStateChanged(CallAudioState audioState) {
  mAudioState = audioState;
}
```

## Get the current device

Get the current active device using
[`CallAudioState.getActiveBluetoothDevice()`](/reference/android/telecom/CallAudioState#getActiveBluetoothDevice()).
This function returns the active Bluetooth device.

**Note:** This feature is only available in API level 28 and higher.

### Kotlin

```
val activeDevice: BluetoothDevice = mAudioState.getActiveBluetoothDevice()
```

### Java

```
BluetoothDevice activeDevice = mAudioState.getActiveBluetoothDevice();
```

## Get Bluetooth devices

Get a list of Bluetooth devices that are available for call audio routing using
[`CallAudioState.getSupportedBluetoothDevices()`](/reference/android/telecom/CallAudioState#getSupportedBluetoothDevices()).

### Kotlin

```
val availableBluetoothDevices: Collection =
  mAudioState.getSupportedBluetoothDevices()
```

### Java

```
Collection availableBluetoothDevices = mAudioState.getSupportedBluetoothDevices();
```

## Route the call audio

### Using API level 28 and higher (recommended)

Route the call audio to an available Bluetooth device using
[`requestBluetoothAudio(BluetoothDevice)`](/reference/android/telecom/Connection#requestBluetoothAudio(android.bluetooth.BluetoothDevice)):

```
requestBluetoothAudio(availableBluetoothDevices[0]);
```

### Using API level 23 and higher

Enable
[`ROUTE_BLUETOOTH`](/reference/android/telecom/CallAudioState#ROUTE_BLUETOOTH)
without specifying the device using
[`setAudioRoute(int)`](/reference/android/telecom/Connection#setAudioRoute(int)).
This defaults routing to current, active bluetooth devices on Android 9 and higher.

```
setAudioRoute(CallAudioState.ROUTE_BLUETOOTH);
```

**Note:** This step isn’t required if the app already knows which Bluetooth device
to route audio to.