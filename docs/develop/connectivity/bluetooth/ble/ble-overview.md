---
title: https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview
url: https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview
source: md.txt
---

# Bluetooth Low Energy

Android provides built-in platform support for Bluetooth Low Energy (BLE) in the central role and provides APIs that apps can use to discover devices, query for services, and transmit information.

Common use cases include the following:

- Transferring small amounts of data between nearby devices.
- Interacting with proximity sensors to give users a customized experience based on their current location.

In contrast to[classic Bluetooth](https://developer.android.com/develop/connectivity/bluetooth), BLE is designed for significantly lower power consumption. This allows apps to communicate with BLE devices that have stricter power requirements, such as proximity sensors, heart rate monitors, and fitness devices.  
**Caution:** When a user pairs their device with another device using BLE, the data that's communicated between the two devices is accessible to**all**apps on the user's device.

For this reason, if your app captures sensitive data, you should implement app-layer security to protect the privacy of that data.

## The basics

For BLE-enabled devices to transmit data between each other, they must first form a channel of communication. Use of the Bluetooth LE APIs requires you to[declare several permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)in your manifest file. Once your app has permission to use Bluetooth, your app needs to access the`BluetoothAdapter`and[determine if Bluetooth is available on the device](https://developer.android.com/develop/connectivity/bluetooth/setup)If Bluetooth is available, the device will[scan for nearby BLE devices](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices). Once a device is found, the capabilities of the BLE device are discovered by[connecting to the GATT server on the BLE device](https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server). Once a connection is made,[data can be transferred with the connected device](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data)based on the available services and characteristics.

## Key terms and concepts

The following is a summary of key BLE terms and concepts:

-

  **Generic Attribute Profile (GATT)**
  :   The GATT profile is a general specification for sending and receiving short pieces of data known as "attributes" over a BLE link. All current BLE application profiles are based on GATT. Review the[Android BluetoothLeGatt sample](https://github.com/android/platform-samples/tree/main/samples/connectivity/bluetooth/ble/src/main/java/com/example/platform/connectivity/bluetooth/ble)on GitHub to learn more.
-

  **Profiles**
  :   The**Bluetooth SIG** defines many[profiles](https://www.bluetooth.org/en-us/specification/adopted-specifications)for BLE devices. A profile is a specification for how a device works in a particular application. Note that a device can implement more than one profile. For example, a device could contain a heart rate monitor and a battery level detector.
-

  **Attribute Protocol (ATT)**
  :   GATT is built on top of the Attribute Protocol (ATT). This is also referred to as GATT/ATT. ATT is optimized to run on BLE devices. To this end, it uses as few bytes as possible. Each attribute is uniquely identified by a Universally Unique Identifier (UUID), which is a standardized 128-bit format for a string ID used to uniquely identify information. The*attributes* transported by ATT are formatted as*characteristics* and*services*.
-

  **Characteristic**
  :   A characteristic contains a single value and 0-n descriptors that describe the characteristic's value. A characteristic can be thought of as a type, analogous to a class.
-

  **Descriptor**
  :   Descriptors are defined attributes that describe a characteristic value. For example, a descriptor might specify a human-readable description, an acceptable range for a characteristic's value, or a unit of measure that is specific to a characteristic's value.
-

  **Service**
  :   A service is a collection of characteristics. For example, you could have a service called "Heart Rate Monitor" that includes characteristics such as "heart rate measurement." You can find a list of existing GATT-based profiles and services on[bluetooth.org](https://www.bluetooth.org/en-us/specification/adopted-specifications).

### Roles and responsibilities

When a device interacts with a BLE device, roles and responsibilities are divided in two different ways:

- **Central versus peripheral.**This applies to the BLE connection itself---the device in the central role scans, looking for advertisement, and the device in the peripheral role advertises. Two devices that only support the peripheral role can't talk to each other, and neither can two devices that only support the central role.

- **GATT server versus GATT client.**This determines how the two devices talk to each other after they've established the connection. The device in the client role sends requests for data, and the device in the server role fulfills them.

To understand the distinction between the central-peripheral and server-client role divisions, consider an example where you have an Android phone and a BLE-enabled activity tracker that reports sensor data back to the phone.

- The phone---the*central* device---actively scans for BLE devices. The activity tracker---the*peripheral*device---advertises and waits to receive a request for connection.

- After the phone and the activity tracker have established a connection, they start transferring GATT metadata to each other. In this case, the app running on the phone sends requests for data, so it acts as the*GATT client* . The activity tracker fulfills those requests, so it acts as the*GATT server*.

An alternative design of the app might involve the phone playing the GATT server role instead. See[`BluetoothGattServer`](https://developer.android.com/reference/android/bluetooth/BluetoothGattServer)for more information.