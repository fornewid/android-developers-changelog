---
title: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls
url: https://developer.android.com/develop/connectivity/bluetooth/ble-audio/telecom-api-managed-calls
source: md.txt
---

> Documentation index: https://developer.android.com/develop/connectivity/bluetooth/llms.txt

This guide covers how to route audio for Bluetooth devices using the
[Telecom API](https://developer.android.com/develop/connectivity/telecom.md.txt) and set the connection for VoIP calls. Read the
[Build a calling app](https://developer.android.com/develop/connectivity/telecom/selfManaged) guide before continuing.

By using the [`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService.md.txt) and [`Connection`](https://developer.android.com/reference/android/telecom/Connection.md.txt) classes, you can
access the audio state and a list of available Bluetooth devices, and can route
audio to a selected Bluetooth device.

## VoIP Connection and ConnectionService

Create a `VoIPConnection` class that extends from [`Connection`](https://developer.android.com/reference/android/telecom/Connection.md.txt). This class
controls the state of the current call. As the [Build a calling app](https://developer.android.com/develop/connectivity/telecom/selfManaged) guide
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

Next, return an instance of this class in [`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService.md.txt) when an
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

```xml
<service android:name=".voip.TelegramConnectionService" android:permission="android.permission.BIND_TELECOM_CONNECTION_SERVICE">
  <intent-filter>
    <action android:name="android.telecom.ConnectionService"/>
  </intent-filter>
</service>
```

With these custom [`Connection`](https://developer.android.com/reference/android/telecom/Connection.md.txt) and [`ConnectionService`](https://developer.android.com/reference/android/telecom/ConnectionService.md.txt) classes, you
can control which device and what type of audio routing you want to use during
a call.

## Get the current audio state

To get the current audio state, call [`getCallAudioState`](https://developer.android.com/reference/android/telecom/Connection.md.txt#getCallAudioState()).
[`getCallAudioState`](https://developer.android.com/reference/android/telecom/Connection.md.txt#getCallAudioState()) returns whether the device is streaming using
Bluetooth, an earpiece, a wired headset, or a speaker.

```java
mAudioState = connection.getCallAudioState()
```

## On state changed

Subscribe to changes in CallAudioState by overriding
[`onCallAudioStateChanged()`](https://developer.android.com/reference/android/telecom/Connection.md.txt#onCallAudioStateChanged(android.telecom.CallAudioState)). This alerts you of any changes to the state.

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
[`CallAudioState.getActiveBluetoothDevice()`](https://developer.android.com/reference/android/telecom/CallAudioState.md.txt#getActiveBluetoothDevice()). This function returns the
active Bluetooth device.

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
[`CallAudioState.getSupportedBluetoothDevices()`](https://developer.android.com/reference/android/telecom/CallAudioState.md.txt#getSupportedBluetoothDevices()).

### Kotlin

```kotlin
val availableBluetoothDevices: Collection<BluetoothDevice> =
  mAudioState.getSupportedBluetoothDevices()
```

### Java

```java
Collection<BluetoothDevice> availableBluetoothDevices = mAudioState.getSupportedBluetoothDevices();
```

## Route the call audio

### Using API level 28 and higher (recommended)

Route the call audio to an available Bluetooth device using
[`requestBluetoothAudio(BluetoothDevice)`](https://developer.android.com/reference/android/telecom/Connection.md.txt#requestBluetoothAudio(android.bluetooth.BluetoothDevice)):

```java
requestBluetoothAudio(availableBluetoothDevices[0]);
```

### Using API level 23 and higher

Enable [`ROUTE_BLUETOOTH`](https://developer.android.com/reference/android/telecom/CallAudioState.md.txt#ROUTE_BLUETOOTH) without specifying the device using
[`setAudioRoute(int)`](https://developer.android.com/reference/android/telecom/Connection.md.txt#setAudioRoute(int)). This defaults routing to current, active Bluetooth
devices on Android 9 and higher.

```java
setAudioRoute(CallAudioState.ROUTE_BLUETOOTH);
```

> [!NOTE]
> **Note:** This step isn't required if the app already knows which Bluetooth device to route audio to.