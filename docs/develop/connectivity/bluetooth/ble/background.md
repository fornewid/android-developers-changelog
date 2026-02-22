---
title: https://developer.android.com/develop/connectivity/bluetooth/ble/background
url: https://developer.android.com/develop/connectivity/bluetooth/ble/background
source: md.txt
---

# Communicate in the background

This guide provides an overview of how to support key use cases for communicating with peripheral devices when your app is running in the background:

- [Find a device](https://developer.android.com/develop/connectivity/bluetooth/ble/background#find-device)
- [Connect to a device](https://developer.android.com/develop/connectivity/bluetooth/ble/background#connect-device)
- [Stay connected to a device](https://developer.android.com/develop/connectivity/bluetooth/ble/background#stay-connected)

There are multiple options to support each of these use cases. Each one has benefits and drawbacks that might make it more or less suitable for your specific needs.

The following diagram shows a simplified view of the guidance on this page:

![](https://developer.android.com/static/images/develop/connectivity/bluetooth/ble-background.png)
| **Note:** The[general guidance for background work](https://developer.android.com/develop/background-work/background-tasks)on Android applies for Bluetooth-related work too.

## Find a device

First, your app needs to find a device to connect to. To find a BLE device you can use either of the following APIs:

- [`BluetoothLeScanner`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner)as described in[Find BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices). ([Sample](https://github.com/android/platform-samples/blob/main/samples/connectivity/bluetooth/ble/src/main/java/com/example/platform/connectivity/bluetooth/ble/FindBLEDevicesSample.kt))
- [`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager)as described in[Companion device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing#implement). ([Sample](https://github.com/android/platform-samples/blob/main/samples/connectivity/bluetooth/companion/src/main/java/com/example/platform/connectivity/bluetooth/cdm/CompanionDeviceManagerSample.kt))

| **Note:** `CompanionDeviceManager`has certain limitations (such as limited filtering and no support for random MAC addresses) that might not satisfy your needs depending on the implementation of the peripheral device.

### In the background

There is no limitation on using either of these APIs while the app is not visible, but they do both need your app process to be alive. If the app process is not running, you can use the following workarounds:

- For`BluetoothLeScanner`: Call[`startScan()`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner#startScan(java.util.List%3Candroid.bluetooth.le.ScanFilter%3E,%20android.bluetooth.le.ScanSettings,%20android.app.PendingIntent))with a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)object instead of a[`ScanCallback`](https://developer.android.com/reference/android/bluetooth/le/ScanCallback)object to get notified when a device matching your filter is scanned. ([Sample](https://github.com/android/platform-samples/blob/main/samples/connectivity/bluetooth/ble/src/main/java/com/example/platform/connectivity/bluetooth/ble/BLEScanIntentSample.kt#L163))
- For`CompanionDeviceManager`: Follow the guidance in[Keep companion apps awake](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing#keep-awake)to wake the app and keep it awake while a previously associated device is in range. ([Sample](https://github.com/android/platform-samples/blob/main/samples/connectivity/bluetooth/companion/src/main/java/com/example/platform/connectivity/bluetooth/cdm/CompanionDeviceSampleService.kt#L40))

| **Note:** Scheduling periodic scans to find devices is discouraged. That approach is less efficient because it starts the app process periodically regardless of whether a device is in range. The methods described in this guide ensure that a device is in range before waking up the app process.

## Connect to a device

To connect to a device after you have found it, you need to get a[`BluetoothDevice`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice)instance for the device from one of the following sources:

- A`BluetoothLeScanner`scan result as described in the[previous section](https://developer.android.com/develop/connectivity/bluetooth/ble/background#find-device).
- The bonded device list retrieved from[`BluetoothAdapter.getBondedDevices()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getBondedDevices()).
- The`BluetoothAdapter`cache, using[`BluetoothAdapter.getRemoteLeDevice()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getRemoteLeDevice(java.lang.String,%20int)).

After you have a`BluetoothDevice`instance, you can start a connection request to the corresponding device by calling one of the[`connectGatt()`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#connectGatt(android.content.Context,%20boolean,%20android.bluetooth.BluetoothGattCallback))methods. The value that you pass into the`autoConnect`boolean defines which of the following two connection modes the GATT client uses:

- **Direct connect** (`autoconnect = false`): Try to connect to the peripheral device directly, and fail if the device isn't available. In case of disconnection, the GATT client doesn't automatically try to reconnect.
- **Auto connect** (`autoconnect = true`): Try to automatically connect to the peripheral device whenever it's available. In case of a disconnection initiated by the peripheral or because the peripheral is out of range, the GATT client automatically tries to reconnect when the peripheral is available.

| **Note:** Android versions below 10 allow only one connection request at a time and queue all subsequent requests. In Android 10 and higher, the system groups connection requests for batched execution.

### In the background

There is no restriction on connecting to a device while the app is in the background, although the connection is closed if your process is killed. In addition there are[restrictions on starting activities](https://developer.android.com/guide/components/activities/background-starts)(in Android 10 and higher) or[foreground services](https://developer.android.com/about/versions/12/behavior-changes-12#foreground-service-launch-restrictions)(in Android 12 and higher) from the background.

Thus, to perform a connection while in the background, apps can use the following solutions:

- Use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)to connect to your device.
  - You can set a[`PeriodicWorkRequest`](https://developer.android.com/reference/androidx/work/PeriodicWorkRequest)or a[`OneTimeWorkRequest`](https://developer.android.com/reference/androidx/work/OneTimeWorkRequest)to perform a defined action, although[app restrictions might apply](https://developer.android.com/topic/performance/appstandby).
  - Additionally, you can benefit from WorkManager features like[work constraints](https://developer.android.com/topic/libraries/architecture/workmanager#constraints),[expedited work](https://developer.android.com/topic/libraries/architecture/workmanager#expedited),[retry policy](https://developer.android.com/topic/libraries/architecture/workmanager#flexible), and more.
  - If the connection needs to be kept alive as long as possible to perform a task, such as data syncing or polling from the peripheral devices, you need to start a foreground service following the guidance in[Support for long-running workers](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running#long-running). However,[foreground service launch restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)apply starting in Android 12.
- Start a foreground service with the`connectedDevice`type.
  - If the connection needs to be kept alive as long as possible to perform a task, such as data syncing or polling from the peripheral devices, you need to start a foreground service following the guidance in[Support for long-running workers](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/long-running#long-running). However,[foreground service launch restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)apply starting in Android 12.
- Call`startScan()`with a`PendingIntent`object as described in[Find a device](https://developer.android.com/develop/connectivity/bluetooth/ble/background#find-device)to wake your process up when the device is present. The peripheral device must be advertising.
  - We recommend that you start a Worker and a Job. This might be interrupted by the system and thus it can only support short duration communication.
  - In versions lower than Android 12 you can start a foreground service directly from the`PendingIntent`object.
- Use[`CompanionDeviceService`](https://developer.android.com/reference/android/companion/CompanionDeviceService)and either of the[`REQUEST_COMPANION_RUN_IN_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)or[`REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)permissions to start the service from the background.

## Stay connected to a device

Ideally, apps should maintain connections to peripheral devices only as long as necessary, and disconnect once the task is completed. However, there are two cases where an app might need to keep a connection alive indefinitely:

- [While switching between apps](https://developer.android.com/develop/connectivity/bluetooth/ble/background#while-switching).
- [While listening to peripheral notifications](https://developer.android.com/develop/connectivity/bluetooth/ble/background#while-listening).

In both cases, the following options are available:

- Use[`CompanionDeviceService`](https://developer.android.com/reference/android/companion/CompanionDeviceService)with the[`REQUEST_COMPANION_RUN_IN_BACKGROUND`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)permission and the[`CompanionDeviceManager.startObservingDevicePresence()`](https://developer.android.com/reference/android/companion/CompanionDeviceManager#startObservingDevicePresence(android.companion.ObservingDevicePresenceRequest))method.
- [Start a foreground service](https://developer.android.com/develop/background-work/services/fgs/launch)while the app is in the foreground (or within one of the[exemptions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions)) with the[`connectedDevice`](https://developer.android.com/about/versions/14/changes/fgs-types-required#connected-device)foreground type.

### While switching between apps

Finding a device, connecting to it, and transferring data is time consuming and resource intensive. To avoid losing connection and having to perform the full process every time the user switches between apps or performs simultaneous tasks, you should keep the connection alive until the operation finishes. You can use either a foreground service with the`connectedDevice`type or the[companion device presence API](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing#keep-awake).

### While listening to peripheral notifications

To listen to peripheral notifications the app must call[`setCharacteristicNotification()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#setCharacteristicNotification(android.bluetooth.BluetoothGattCharacteristic,%20boolean)), listen to callbacks using[`onCharacteristicChanged()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onCharacteristicChanged(android.bluetooth.BluetoothGatt,%20android.bluetooth.BluetoothGattCharacteristic,%20byte[])), and keep the connection alive. For most apps, it's best to support this use case with`CompanionDeviceService`because the app will likely need to keep listening for long periods of time. However, you can also use a foreground service.

In either case, you can reconnect after a terminated process by following the instructions in the[Connect to a device](https://developer.android.com/develop/connectivity/bluetooth/ble/background#connect-device)section.