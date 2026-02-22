---
title: https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data
url: https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data
source: md.txt
---

# Transfer BLE data

Once you have[connected to a BLE GATT server](https://developer.android.com/develop/connectivity/bluetooth/connect-gatt-server), you can use the connection to find out what services are available on the device, query data from the device, and request notifications when a certain GATT characteristic changes.

## Discover services

The first thing to do once you connect to the GATT Server on the BLE device is to perform service discovery. This provides information about the services available on the remote device as well as the service characteristics and their descriptors. In the following example, once the service successfully connects to the device (indicated by the appropriate call to the[`onConnectionStateChange()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onConnectionStateChange(android.bluetooth.BluetoothGatt,%20int,%20int))function of the[`BluetoothGattCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback)), the[`discoverServices()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#discoverServices())function queries the information from the BLE device.

The service needs to override the[`onServicesDiscovered()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onServicesDiscovered(android.bluetooth.BluetoothGatt,%20int))function in the[`BluetoothGattCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback). This function is called when the device reports on its available services.  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

private val bluetoothGattCallback = object : BluetoothGattCallback() {
    override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
        if (newState == BluetoothProfile.STATE_CONNECTED) {
            // successfully connected to the GATT Server
            broadcastUpdate(ACTION_GATT_CONNECTED)
            connectionState = STATE_CONNECTED
            // Attempts to discover services after successful connection.
            bluetoothGatt?.discoverServices()
        } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
            // disconnected from the GATT Server
            broadcastUpdate(ACTION_GATT_DISCONNECTED)
            connectionState = STATE_DISCONNECTED
        }
    }

    override fun onServicesDiscovered(gatt: BluetoothGatt?, status: Int) {
        if (status == BluetoothGatt.GATT_SUCCESS) {
            broadcastUpdate(ACTION_GATT_SERVICES_DISCOVERED)
        } else {
            Log.w(BluetoothLeService.TAG, "onServicesDiscovered received: $status")
        }
    }
}

...

companion object {
  const val ACTION_GATT_CONNECTED = "com.example.bluetooth.le.ACTION_GATT_CONNECTED"
  const val ACTION_GATT_DISCONNECTED =
              "com.example.bluetooth.le.ACTION_GATT_DISCONNECTED"
  const val ACTION_GATT_SERVICES_DISCOVERED =
              "com.example.bluetooth.le.ACTION_GATT_SERVICES_DISCOVERED"

  private const val STATE_DISCONNECTED = 0
  private const val STATE_CONNECTED = 2
}
```

### Java

```java
class BluetoothLeService extends Service {

    public final static String ACTION_GATT_SERVICES_DISCOVERED =
            "com.example.bluetooth.le.ACTION_GATT_SERVICES_DISCOVERED";

    ...

    private final BluetoothGattCallback bluetoothGattCallback = new BluetoothGattCallback() {
        @Override
        public void onConnectionStateChange(BluetoothGatt gatt, int status, int newState) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                // successfully connected to the GATT Server
                connectionState = STATE_CONNECTED;
                broadcastUpdate(ACTION_GATT_CONNECTED);
                // Attempts to discover services after successful connection.
                bluetoothGatt.discoverServices();
            } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                // disconnected from the GATT Server
                connectionState = STATE_DISCONNECTED;
                broadcastUpdate(ACTION_GATT_DISCONNECTED);
            }
        }

        @Override
        public void onServicesDiscovered(BluetoothGatt gatt, int status) {
            if (status == BluetoothGatt.GATT_SUCCESS) {
                broadcastUpdate(ACTION_GATT_SERVICES_DISCOVERED);
            } else {
                Log.w(TAG, "onServicesDiscovered received: " + status);
            }
        }
    };
}
```

The service uses[broadcasts](https://developer.android.com/guide/components/broadcasts)to notify the activity. Once the services have been discovered, the service can call[`getServices()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#getServices())to get the reported data.  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

  fun getSupportedGattServices(): List<BluetoothGattService?>? {
      return bluetoothGatt?.services
  }
}
```

### Java

```java
class BluetoothLeService extends Service {

...

    public List<BluetoothGattService> getSupportedGattServices() {
        if (bluetoothGatt == null) return null;
        return bluetoothGatt.getServices();
    }
}
```

The activity can then call this function when it receives the broadcast intent, indicating that service discovery has finished.  

### Kotlin

```kotlin
class DeviceControlActivity : AppCompatActivity() {

...

    private val gattUpdateReceiver: BroadcastReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context, intent: Intent) {
            when (intent.action) {
                BluetoothLeService.ACTION_GATT_CONNECTED -> {
                    connected = true
                    updateConnectionState(R.string.connected)
                }
                BluetoothLeService.ACTION_GATT_DISCONNECTED -> {
                    connected = false
                    updateConnectionState(R.string.disconnected)
                        }
                BluetoothLeService.ACTION_GATT_SERVICES_DISCOVERED -> {
                    // Show all the supported services and characteristics on the user interface.
                    displayGattServices(bluetoothService?.getSupportedGattServices())
                }
            }
        }
    }
}
```

### Java

```java
class DeviceControlsActivity extends AppCompatActivity {

...

    private final BroadcastReceiver gattUpdateReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();
            if (BluetoothLeService.ACTION_GATT_CONNECTED.equals(action)) {
                connected = true;
                updateConnectionState(R.string.connected);
            } else if (BluetoothLeService.ACTION_GATT_DISCONNECTED.equals(action)) {
                connected = false;
                updateConnectionState(R.string.disconnected);
            } else if (BluetoothLeService.ACTION_GATT_SERVICES_DISCOVERED.equals(action)) {
                // Show all the supported services and characteristics on the user interface.
                displayGattServices(bluetoothService.getSupportedGattServices());
            }
        }
    };
}
```

## Read BLE characteristics

Once your app has connected to a GATT server and discovered services, it can read and write attributes, where supported. For example, the following snippet iterates through the server's services and characteristics and displays them in the UI:  

### Kotlin

```kotlin
class DeviceControlActivity : Activity() {

    // Demonstrates how to iterate through the supported GATT
    // Services/Characteristics.
    // In this sample, we populate the data structure that is bound to the
    // ExpandableListView on the UI.
    private fun displayGattServices(gattServices: List<BluetoothGattService>?) {
        if (gattServices == null) return
        var uuid: String?
        val unknownServiceString: String = resources.getString(R.string.unknown_service)
        val unknownCharaString: String = resources.getString(R.string.unknown_characteristic)
        val gattServiceData: MutableList<HashMap<String, String>> = mutableListOf()
        val gattCharacteristicData: MutableList<ArrayList<HashMap<String, String>>> =
                mutableListOf()
        mGattCharacteristics = mutableListOf()

        // Loops through available GATT Services.
        gattServices.forEach { gattService ->
            val currentServiceData = HashMap<String, String>()
            uuid = gattService.uuid.toString()
            currentServiceData[LIST_NAME] = SampleGattAttributes.lookup(uuid, unknownServiceString)
            currentServiceData[LIST_UUID] = uuid
            gattServiceData += currentServiceData

            val gattCharacteristicGroupData: ArrayList<HashMap<String, String>> = arrayListOf()
            val gattCharacteristics = gattService.characteristics
            val charas: MutableList<BluetoothGattCharacteristic> = mutableListOf()

            // Loops through available Characteristics.
            gattCharacteristics.forEach { gattCharacteristic ->
                charas += gattCharacteristic
                val currentCharaData: HashMap<String, String> = hashMapOf()
                uuid = gattCharacteristic.uuid.toString()
                currentCharaData[LIST_NAME] = SampleGattAttributes.lookup(uuid, unknownCharaString)
                currentCharaData[LIST_UUID] = uuid
                gattCharacteristicGroupData += currentCharaData
            }
            mGattCharacteristics += charas
            gattCharacteristicData += gattCharacteristicGroupData
        }
    }
}
```

### Java

```java
public class DeviceControlActivity extends Activity {
    ...
    // Demonstrates how to iterate through the supported GATT
    // Services/Characteristics.
    // In this sample, we populate the data structure that is bound to the
    // ExpandableListView on the UI.
    private void displayGattServices(List<BluetoothGattService> gattServices) {
        if (gattServices == null) return;
        String uuid = null;
        String unknownServiceString = getResources().
                getString(R.string.unknown_service);
        String unknownCharaString = getResources().
                getString(R.string.unknown_characteristic);
        ArrayList<HashMap<String, String>> gattServiceData =
                new ArrayList<HashMap<String, String>>();
        ArrayList<ArrayList<HashMap<String, String>>> gattCharacteristicData
                = new ArrayList<ArrayList<HashMap<String, String>>>();
        mGattCharacteristics =
                new ArrayList<ArrayList<BluetoothGattCharacteristic>>();

        // Loops through available GATT Services.
        for (BluetoothGattService gattService : gattServices) {
            HashMap<String, String> currentServiceData =
                    new HashMap<String, String>();
            uuid = gattService.getUuid().toString();
            currentServiceData.put(
                    LIST_NAME, SampleGattAttributes.
                            lookup(uuid, unknownServiceString));
            currentServiceData.put(LIST_UUID, uuid);
            gattServiceData.add(currentServiceData);

            ArrayList<HashMap<String, String>> gattCharacteristicGroupData =
                    new ArrayList<HashMap<String, String>>();
            List<BluetoothGattCharacteristic> gattCharacteristics =
                    gattService.getCharacteristics();
            ArrayList<BluetoothGattCharacteristic> charas =
                    new ArrayList<BluetoothGattCharacteristic>();
           // Loops through available Characteristics.
            for (BluetoothGattCharacteristic gattCharacteristic :
                    gattCharacteristics) {
                charas.add(gattCharacteristic);
                HashMap<String, String> currentCharaData =
                        new HashMap<String, String>();
                uuid = gattCharacteristic.getUuid().toString();
                currentCharaData.put(
                        LIST_NAME, SampleGattAttributes.lookup(uuid,
                                unknownCharaString));
                currentCharaData.put(LIST_UUID, uuid);
                gattCharacteristicGroupData.add(currentCharaData);
            }
            mGattCharacteristics.add(charas);
            gattCharacteristicData.add(gattCharacteristicGroupData);
         }
    ...
    }
...
}
```

The GATT service provides a list of characteristics you can read from the device. In order to query the data, call the[`readCharacteristic()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#readCharacteristic(android.bluetooth.BluetoothGattCharacteristic))function on the[`BluetoothGatt`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt), passing in the[`BluetoothGattCharacteristic`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCharacteristic)you want to read.  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

    fun readCharacteristic(characteristic: BluetoothGattCharacteristic) {
        bluetoothGatt?.let { gatt ->
            gatt.readCharacteristic(characteristic)
        } ?: run {
            Log.w(TAG, "BluetoothGatt not initialized")
            Return
        }
    }
}
```

### Java

```java
class BluetoothLeService extends Service {

...

    public void readCharacteristic(BluetoothGattCharacteristic characteristic) {
        if (bluetoothGatt == null) {
            Log.w(TAG, "BluetoothGatt not initialized");
            return;
        }
        bluetoothGatt.readCharacteristic(characteristic);
    }
}
```

In this example, the service implements a function to call[`readCharacteristic()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#readCharacteristic(android.bluetooth.BluetoothGattCharacteristic)). This is an asynchronous call. The results are sent to the[`BluetoothGattCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback)function[`onCharacteristicRead()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onCharacteristicRead(android.bluetooth.BluetoothGatt,%20android.bluetooth.BluetoothGattCharacteristic,%20int)).  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

    private val bluetoothGattCallback = object : BluetoothGattCallback() {

        ...

        override fun onCharacteristicRead(
            gatt: BluetoothGatt,
            characteristic: BluetoothGattCharacteristic,
            status: Int
            ) {
                if (status == BluetoothGatt.GATT_SUCCESS) {
                broadcastUpdate(BluetoothLeService.ACTION_DATA_AVAILABLE, characteristic)
            }
        }
    }
}
```

### Java

```java
class BluetoothLeService extends Service {

...

    private final BluetoothGattCallback bluetoothGattCallback = new BluetoothGattCallback() {

    ...

        @Override
        public void onCharacteristicRead(
        BluetoothGatt gatt,
        BluetoothGattCharacteristic characteristic,
        int status
        ) {
            if (status == BluetoothGatt.GATT_SUCCESS) {
                broadcastUpdate(ACTION_DATA_AVAILABLE, characteristic);
            }
        }
    };
}
```

When a particular callback is triggered, it calls the appropriate`broadcastUpdate()`helper method and passes it an action. Note that the data parsing in this section is performed in accordance with the Bluetooth Heart Rate Measurement profile specifications.  

### Kotlin

```kotlin
private fun broadcastUpdate(action: String, characteristic: BluetoothGattCharacteristic) {
    val intent = Intent(action)

    // This is special handling for the Heart Rate Measurement profile. Data
    // parsing is carried out as per profile specifications.
    when (characteristic.uuid) {
        UUID_HEART_RATE_MEASUREMENT -> {
            val flag = characteristic.properties
            val format = when (flag and 0x01) {
                0x01 -> {
                    Log.d(TAG, "Heart rate format UINT16.")
                    BluetoothGattCharacteristic.FORMAT_UINT16
                }
                else -> {
                    Log.d(TAG, "Heart rate format UINT8.")
                    BluetoothGattCharacteristic.FORMAT_UINT8
                }
            }
            val heartRate = characteristic.getIntValue(format, 1)
            Log.d(TAG, String.format("Received heart rate: %d", heartRate))
            intent.putExtra(EXTRA_DATA, (heartRate).toString())
        }
        else -> {
            // For all other profiles, writes the data formatted in HEX.
            val data: ByteArray? = characteristic.value
            if (data?.isNotEmpty() == true) {
                val hexString: String = data.joinToString(separator = " ") {
                    String.format("%02X", it)
                }
                intent.putExtra(EXTRA_DATA, "$data\n$hexString")
            }
        }
    }
    sendBroadcast(intent)
}
```

### Java

```java
private void broadcastUpdate(final String action,
                             final BluetoothGattCharacteristic characteristic) {
    final Intent intent = new Intent(action);

    // This is special handling for the Heart Rate Measurement profile. Data
    // parsing is carried out as per profile specifications.
    if (UUID_HEART_RATE_MEASUREMENT.equals(characteristic.getUuid())) {
        int flag = characteristic.getProperties();
        int format = -1;
        if ((flag & 0x01) != 0) {
            format = BluetoothGattCharacteristic.FORMAT_UINT16;
            Log.d(TAG, "Heart rate format UINT16.");
        } else {
            format = BluetoothGattCharacteristic.FORMAT_UINT8;
            Log.d(TAG, "Heart rate format UINT8.");
        }
        final int heartRate = characteristic.getIntValue(format, 1);
        Log.d(TAG, String.format("Received heart rate: %d", heartRate));
        intent.putExtra(EXTRA_DATA, String.valueOf(heartRate));
    } else {
        // For all other profiles, writes the data formatted in HEX.
        final byte[] data = characteristic.getValue();
        if (data != null && data.length > 0) {
            final StringBuilder stringBuilder = new StringBuilder(data.length);
            for(byte byteChar : data)
                stringBuilder.append(String.format("%02X ", byteChar));
            intent.putExtra(EXTRA_DATA, new String(data) + "\n" +
                    stringBuilder.toString());
        }
    }
    sendBroadcast(intent);
}
```

## Receive GATT notifications

It's common for BLE apps to ask to be notified when a particular characteristic changes on the device. In the following example, the service implements a function to call the[`setCharacteristicNotification()`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#setCharacteristicNotification(android.bluetooth.BluetoothGattCharacteristic,%20boolean))method:  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

    fun setCharacteristicNotification(
    characteristic: BluetoothGattCharacteristic,
    enabled: Boolean
    ) {
        bluetoothGatt?.let { gatt ->
        gatt.setCharacteristicNotification(characteristic, enabled)

        // This is specific to Heart Rate Measurement.
        if (BluetoothLeService.UUID_HEART_RATE_MEASUREMENT == characteristic.uuid) {
            val descriptor = characteristic.getDescriptor(UUID.fromString(SampleGattAttributes.CLIENT_CHARACTERISTIC_CONFIG))
            descriptor.value = BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE
            gatt.writeDescriptor(descriptor)
        }
        } ?: run {
            Log.w(BluetoothLeService.TAG, "BluetoothGatt not initialized")
        }
    }
}
```

### Java

```java
class BluetoothLeService extends Service {

...

    public void setCharacteristicNotification(BluetoothGattCharacteristic characteristic,boolean enabled) {
        if (bluetoothGatt == null) {
            Log.w(TAG, "BluetoothGatt not initialized");
            Return;
        }
        bluetoothGatt.setCharacteristicNotification(characteristic, enabled);

        // This is specific to Heart Rate Measurement.
        if (UUID_HEART_RATE_MEASUREMENT.equals(characteristic.getUuid())) {
            BluetoothGattDescriptor descriptor = characteristic.getDescriptor(UUID.fromString(SampleGattAttributes.CLIENT_CHARACTERISTIC_CONFIG));
            descriptor.setValue(BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE);
            bluetoothGatt.writeDescriptor(descriptor);
        }
    }
}
```

Once notifications are enabled for a characteristic, an[`onCharacteristicChanged()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onCharacteristicChanged(android.bluetooth.BluetoothGatt,%20android.bluetooth.BluetoothGattCharacteristic))callback is triggered if the characteristic changes on the remote device:  

### Kotlin

```kotlin
class BluetoothLeService : Service() {

...

    private val bluetoothGattCallback = object : BluetoothGattCallback() {
        ...

        override fun onCharacteristicChanged(
        gatt: BluetoothGatt,
        characteristic: BluetoothGattCharacteristic
        ) {
            broadcastUpdate(ACTION_DATA_AVAILABLE, characteristic)
        }
    }
}
```

### Java

```java
class BluetoothLeService extends Service {

...

    private final BluetoothGattCallback bluetoothGattCallback = new BluetoothGattCallback() {
    ...

        @Override
        public void onCharacteristicChanged(
        BluetoothGatt gatt,
        BluetoothGattCharacteristic characteristic
        ) {
            broadcastUpdate(ACTION_DATA_AVAILABLE, characteristic);
        }
    };
}
```