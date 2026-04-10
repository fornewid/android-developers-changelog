---
title: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls
url: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls
source: md.txt
---

This guide covers how to route audio for Bluetooth devices using the
[Telecom API](https://developer.android.com/develop/connectivity/telecom) and set the connection for
VoIP calls. Read the
[Build a calling app](https://developer.android.com/develop/connectivity/telecom/selfManaged) guide
before continuing.

By using the [`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService)
and [`Connection`](https://developer.android.com/reference/android/telecom/Connection) classes, you can access
the audio state and a list of available Bluetooth devices, and can route
audio to a selected Bluetooth device.

## VoIP Connection and ConnectionService

Create a `VoIPConnection` class that extends from
[`Connection`](https://developer.android.com/reference/android/telecom/Connection). This class controls the state of the current call. As the
[Build a calling app](https://developer.android.com/develop/connectivity/telecom/selfManaged) guide
states, make this a self-managed application and set the audio mode for a VoIP
application.

### Kotlin

```kotlin
class VoIPConnection : Connection() {
  init {
    setConnectionProperties(PROPERTY_SELF_MANAGED)
    setAudioModeIsVoip(true)
  }
}
```

### Java

```java
public class VoIPConnection extends Connection {
  public VoIPConnection() {
    setConnectionProperties(PROPERTY_SELF_MANAGED);
    setAudioModeIsVoip(true);
  }
}
```

Next, return an instance of this class in
[`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService) when an
incoming or outgoing call occurs.

### Kotlin

```kotlin
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

```java
public class VoIPConnectionService extends ConnectionService {
  @Override
  public Connection onCreateOutgoingConnection(PhoneAccountHandle connectionManagerPhoneAccount, ConnectionRequest request) {
    return new VoIPConnection();
  }
}
```

Ensure the manifest correctly points to the `VoIPConnectionService` class.

    <service android:name=".voip.TelegramConnectionService" android:permission="android.permission.BIND_TELECOM_CONNECTION_SERVICE">
      <intent-filter>
        <action android:name="android.telecom.ConnectionService"/>
      </intent-filter>
    </service>

With these custom [`Connection`](https://developer.android.com/reference/android/telecom/Connection) and
[`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService) classes, you
can control which device and what type of audio routing you wish to use during a
call.

## Get the current audio state

To get the current audio state, call
[`getCallAudioState()`](https://developer.android.com/reference/android/telecom/Connection#getCallAudioState()).
[`getCallAudioState()`](https://developer.android.com/reference/android/telecom/Connection#getCallAudioState())
returns if the device is streaming using Bluetooth, Earpiece, Wired, or
Speaker.

    mAudioState = connection.getCallAudioState()

## On State Changed

Subscribe to changes in CallAudioState by overriding
[`onCallAudioStateChanged()`](https://developer.android.com/reference/android/telecom/Connection#onCallAudioStateChanged(android.telecom.CallAudioState)).
This alerts you of any changes to the state.

### Kotlin

```kotlin
fun onCallAudioStateChanged(audioState: CallAudioState) {
  mAudioState = audioState
}
```

### Java

```java
@Override
public void onCallAudioStateChanged(CallAudioState audioState) {
  mAudioState = audioState;
}
```

## Get the current device

Get the current active device using
[`CallAudioState.getActiveBluetoothDevice()`](https://developer.android.com/reference/android/telecom/CallAudioState#getActiveBluetoothDevice()).
This function returns the active Bluetooth device.

> [!NOTE]
> **Note:** This feature is only available in API level 28 and higher.

### Kotlin

```kotlin
val activeDevice: BluetoothDevice = mAudioState.getActiveBluetoothDevice()
```

### Java

```java
BluetoothDevice activeDevice = mAudioState.getActiveBluetoothDevice();
```

## Get Bluetooth devices

Get a list of Bluetooth devices that are available for call audio routing using
[`CallAudioState.getSupportedBluetoothDevices()`](https://developer.android.com/reference/android/telecom/CallAudioState#getSupportedBluetoothDevices()).

### Kotlin

```kotlin
val availableBluetoothDevices: Collection =
  mAudioState.getSupportedBluetoothDevices()
```

### Java

```java
Collection availableBluetoothDevices = mAudioState.getSupportedBluetoothDevices();
```

## Route the call audio

### Using API level 28 and higher (recommended)

Route the call audio to an available Bluetooth device using
[`requestBluetoothAudio(BluetoothDevice)`](https://developer.android.com/reference/android/telecom/Connection#requestBluetoothAudio(android.bluetooth.BluetoothDevice)):

    requestBluetoothAudio(availableBluetoothDevices[0]);

### Using API level 23 and higher

Enable
[`ROUTE_BLUETOOTH`](https://developer.android.com/reference/android/telecom/CallAudioState#ROUTE_BLUETOOTH)
without specifying the device using
[`setAudioRoute(int)`](https://developer.android.com/reference/android/telecom/Connection#setAudioRoute(int)).
This defaults routing to current, active bluetooth devices on Android 9 and higher.

    setAudioRoute(CallAudioState.ROUTE_BLUETOOTH);

> [!NOTE]
> **Note:** This step isn't required if the app already knows which Bluetooth device to route audio to.