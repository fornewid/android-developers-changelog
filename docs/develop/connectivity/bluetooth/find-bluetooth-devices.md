---
title: https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices
url: https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices
source: md.txt
---

# Find Bluetooth devices

Using the[`BluetoothAdapter`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter), you can find remote Bluetooth devices either through device discovery or by querying the list of paired devices.

Make sure you have the appropriate[Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)and[set up your app for Bluetooth](https://developer.android.com/develop/connectivity/bluetooth/setup)before attempting to find Bluetooth devices.

Device discovery is a scanning procedure that searches the local area for Bluetooth-enabled devices and requests some information about each one. This process is sometimes referred to as discovering, inquiring, or scanning. A nearby Bluetooth device responds to a discovery request only if it is currently accepting information requests by being discoverable. If a device is discoverable, it responds to the discovery request by sharing some information, such as the device's name, its class, and its unique MAC address. Using this information, the device that is performing the discovery process can then choose to initiate a connection to the discovered device.

Because discoverable devices might reveal information about the user's location, the device discovery process requires location access. If your app is being used on a device that runs Android 8.0 (API level 26) or higher, consider using the[Companion Device Manager API](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing)instead. This API performs device discovery on your app's behalf, so your app doesn't need to[request location permissions](https://developer.android.com/training/location/permissions).

Once a connection is made with a remote device for the first time, a pairing request is automatically presented to the user. When a device is paired, the basic information about that device---such as the device's name, class, and MAC address---is saved and can be read using the Bluetooth APIs. Using the known MAC address for a remote device, a connection can be initiated with it at any time without performing discovery, assuming the device is still within range.

Note that there is a difference between being paired and being connected:

- To be*paired*means that two devices are aware of each other's existence, have a shared link-key that can be used for authentication, and are capable of establishing an encrypted connection with each other.
- To be*connected*means that the devices currently share an RFCOMM channel and are able to transmit data with each other. The current Bluetooth APIs require devices to be paired before an RFCOMM connection can be established. Pairing is automatically performed when you initiate an encrypted connection with the Bluetooth APIs.

The following sections describe how to find devices that have been paired and how to discover new devices using device discovery.
| **Note:** Android-powered devices are not discoverable by default. A user can make the device discoverable for a limited time through the system settings, or an app can request that the user enable discoverability without leaving the app. For more information, see the[enable discoverability](https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices#enable-discoverability)section on this page.

## Query paired devices

Before performing device discovery, it's worth querying the set of paired devices to see if the desired device is already known. To do so, call[`getBondedDevices()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getBondedDevices()). This returns a set of[`BluetoothDevice`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice)objects representing paired devices. For example, you can query all paired devices and get the name and MAC address of each device, as the following code snippet demonstrates:  

### Kotlin

```kotlin
val pairedDevices: Set<BluetoothDevice>? = bluetoothAdapter?.bondedDevices
pairedDevices?.forEach { device ->
   val deviceName = device.name
   val deviceHardwareAddress = device.address // MAC address
}
```

### Java

```java
Set<BluetoothDevice> pairedDevices = bluetoothAdapter.getBondedDevices();

if (pairedDevices.size() > 0) {
   // There are paired devices. Get the name and address of each paired device.
   for (BluetoothDevice device : pairedDevices) {
       String deviceName = device.getName();
       String deviceHardwareAddress = device.getAddress(); // MAC address
   }
}
```

To initiate a connection with a Bluetooth device, all that's needed from the associated`BluetoothDevice`object is the MAC address, which you retrieve by calling[`getAddress()`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#getAddress()). You can learn more about creating a connection in[Connect Bluetooth devices](https://developer.android.com/develop/connectivity/bluetooth/connect-bluetooth-devices).

### Discover devices

To start discovering devices, call[`startDiscovery()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#startDiscovery()). The process is asynchronous and returns a boolean value indicating whether discovery has successfully started. The discovery process usually involves an inquiry scan of about 12 seconds, followed by a page scan of each device found to retrieve its Bluetooth name.

To receive information about each device discovered, your app must register a[`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver)for the[`ACTION_FOUND`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#ACTION_FOUND)intent. The system broadcasts this intent for each device. The intent contains the extra fields[`EXTRA_DEVICE`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#EXTRA_DEVICE)and[`EXTRA_CLASS`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#EXTRA_CLASS), which in turn contain a`BluetoothDevice`and a[`BluetoothClass`](https://developer.android.com/reference/android/bluetooth/BluetoothClass), respectively. The following code snippet shows how you can register to handle the broadcast when devices are discovered:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
   ...

   // Register for broadcasts when a device is discovered.
   val filter = IntentFilter(BluetoothDevice.ACTION_FOUND)
   registerReceiver(receiver, filter)
}

// Create a BroadcastReceiver for ACTION_FOUND.
private val receiver = object : BroadcastReceiver() {

   override fun onReceive(context: Context, intent: Intent) {
       val action: String = intent.action
       when(action) {
           BluetoothDevice.ACTION_FOUND -> {
               // Discovery has found a device. Get the BluetoothDevice
               // object and its info from the Intent.
               val device: BluetoothDevice =
                       intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE)
               val deviceName = device.name
               val deviceHardwareAddress = device.address // MAC address
           }
       }
   }
}

override fun onDestroy() {
   super.onDestroy()
   ...

   // Don't forget to unregister the ACTION_FOUND receiver.
   unregisterReceiver(receiver)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
   ...

   // Register for broadcasts when a device is discovered.
   IntentFilter filter = new IntentFilter(BluetoothDevice.ACTION_FOUND);
   registerReceiver(receiver, filter);
}

// Create a BroadcastReceiver for ACTION_FOUND.
private final BroadcastReceiver receiver = new BroadcastReceiver() {
   public void onReceive(Context context, Intent intent) {
       String action = intent.getAction();
       if (BluetoothDevice.ACTION_FOUND.equals(action)) {
           // Discovery has found a device. Get the BluetoothDevice
           // object and its info from the Intent.
           BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
           String deviceName = device.getName();
           String deviceHardwareAddress = device.getAddress(); // MAC address
       }
   }
};

@Override
protected void onDestroy() {
   super.onDestroy();
   ...

   // Don't forget to unregister the ACTION_FOUND receiver.
   unregisterReceiver(receiver);
}
```

To initiate a connection with a Bluetooth device, you call`getAddress()`on the`BluetoothDevice`to retrieve the associated MAC address.
| **Caution:** Performing device discovery consumes a lot of the Bluetooth adapter's resources. After you have found a device to connect to, be certain that you stop discovery with`cancelDiscovery()`before attempting a connection. Also, you shouldn't perform discovery while connected to a device because the discovery process significantly reduces the bandwidth available for any existing connections.

#### Enable discoverability

To make the local device discoverable to other devices, call[`startActivityForResult(Intent, int)`](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent,%20int))with the[`ACTION_REQUEST_DISCOVERABLE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#ACTION_REQUEST_DISCOVERABLE)intent. This issues a request to enable the system's discoverable mode without having to navigate to the Settings app, which would stop your own app. By default, the device becomes discoverable for two minutes. You can define a different duration, up to five minutes, by adding the[`EXTRA_DISCOVERABLE_DURATION`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#EXTRA_DISCOVERABLE_DURATION)extra.
| **Caution:** If you set the`EXTRA_DISCOVERABLE_DURATION`extra's value to 0, the device is always discoverable. This configuration is insecure and therefore highly discouraged.

The following code snippet sets the device to be discoverable for five minutes:  

### Kotlin

```kotlin
val requestCode = 1;
val discoverableIntent: Intent = Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE).apply {
   putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300)
}
startActivityForResult(discoverableIntent, requestCode)
```

### Java

```java
int requestCode = 1;
Intent discoverableIntent =
       new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
startActivityForResult(discoverableIntent, requestCode);
```

![](https://developer.android.com/static/images/develop/connectivity/bluetooth/enable-discoverability.png)  
**Figure 2:**The enabling discoverability dialog.

A dialog is displayed, requesting the user's permission to make the device discoverable, as shown in figure 2. If the user responds "Allow," then the device becomes discoverable for the specified amount of time. Your activity then receives a call to the[`onActivityResult()`](https://developer.android.com/reference/android/app/Activity#onActivityResult(int,%20int,%20android.content.Intent))callback, with the result code equal to the duration that the device is discoverable. If the user responded "Deny", or if an error occurred, the result code is[`RESULT_CANCELED`](https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED).
| **Note:** If Bluetooth has not been enabled on the device, then making the device discoverable automatically enables Bluetooth.

The device silently remains in discoverable mode for the allotted time. To be notified when the discoverable mode has changed, register a`BroadcastReceiver`for the[`ACTION_SCAN_MODE_CHANGED`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#ACTION_SCAN_MODE_CHANGED)intent. This intent contains the extra fields[`EXTRA_SCAN_MODE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#EXTRA_SCAN_MODE)and[`EXTRA_PREVIOUS_SCAN_MODE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#EXTRA_PREVIOUS_SCAN_MODE), which provide the new and old scan mode, respectively. Possible values for each extra are as follows:

[`SCAN_MODE_CONNECTABLE_DISCOVERABLE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#SCAN_MODE_CONNECTABLE_DISCOVERABLE)
:   The device is in discoverable mode.

[`SCAN_MODE_CONNECTABLE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#SCAN_MODE_CONNECTABLE)
:   The device isn't in discoverable mode but can still receive connections.

[`SCAN_MODE_NONE`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#SCAN_MODE_NONE)
:   The device isn't in discoverable mode and cannot receive connections.

If you are initiating the connection to a remote device, you don't need to enable device discoverability. Enabling discoverability is only necessary when you want your app to host a server socket that accepts incoming connections, as remote devices must be able to discover other devices before initiating connections to those other devices.