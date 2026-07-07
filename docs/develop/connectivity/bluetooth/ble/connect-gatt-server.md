---
title: https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server
url: https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server
source: md.txt
---

The first step in interacting with a BLE device is connecting to it. More
specifically, connecting to the GATT server on the device. To connect to a GATT
server on a BLE device, use the
[`connectGatt()`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#connectGatt(android.content.Context,%20boolean,%20android.bluetooth.BluetoothGattCallback))
method. This method takes three parameters: a
[`Context`](https://developer.android.com/reference/android/content/Context) object, `autoConnect` (a boolean
indicating whether to automatically connect to the BLE device as soon as it
becomes available), and a reference to a
[`BluetoothGattCallback`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback):


```kotlin
var bluetoothGatt: BluetoothGatt? = null
// ...
bluetoothGatt = device.connectGatt(this, false, bluetoothGattCallback)
```

<br />

This connects to the GATT server hosted by the BLE device, and returns a
[`BluetoothGatt`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt) instance, which
you can then use to conduct GATT client operations. The caller (the Android app)
is the GATT client. The
`BluetoothGattCallback` is used to deliver results to the client, such as
connection status, as well as any further GATT client operations.

## Set up a bound service

In the following example, the BLE app provides an activity
(`DeviceControlActivity`) to connect to Bluetooth devices, display device data,
and display the GATT services and characteristics supported by the device. Based
on user input, this activity communicates with a
[`Service`](https://developer.android.com/reference/android/app/Service) called `BluetoothLeService`, which
interacts with the BLE device via the BLE API. The communication is
performed using a [bound service](https://developer.android.com/guide/components/bound-services) which allows
the activity to connect to the `BluetoothLeService` and call functions to
connect to the devices. The `BluetoothLeService` needs a
[`Binder`](https://developer.android.com/reference/android/os/Binder) implementation that provides access to
the service for the activity.


```kotlin
class BluetoothLeService : Service() {

    private val binder = LocalBinder()

    override fun onBind(intent: Intent): IBinder? {
        return binder
    }

    inner class LocalBinder : Binder() {
        fun getService(): BluetoothLeService {
            return this@BluetoothLeService
        }
    }
}
```

<br />

The activity can start the service using
[`bindService()`](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent,%20android.content.ServiceConnection,%20int)),
passing in an [`Intent`](https://developer.android.com/reference/android/content/Intent) to start the
service, a [`ServiceConnection`](https://developer.android.com/reference/android/content/ServiceConnection)
implementation to listen for the connection and disconnection events, and a flag
to specify additional connection options.


```kotlin
class DeviceControlActivity : AppCompatActivity() {

    private var bluetoothService: BluetoothLeService? = null
    // Code to manage Service lifecycle.
    private val serviceConnection: ServiceConnection = object : ServiceConnection {
        override fun onServiceConnected(
            componentName: ComponentName,
            service: IBinder
        ) {
            bluetoothService = (service as LocalBinder).getService()
            bluetoothService?.let { bluetooth ->
                // call functions on service to check connection and connect to devices
            }
        }

        override fun onServiceDisconnected(componentName: ComponentName) {
            bluetoothService = null
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.gatt_services_characteristics)

        val gattServiceIntent = Intent(this, BluetoothLeService::class.java)
        bindService(gattServiceIntent, serviceConnection, Context.BIND_AUTO_CREATE)
    }
}
```

<br />

## Set up the BluetoothAdapter

Once the service is bound to, it needs to access the
[`BluetoothAdapter`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter). It should
check that the adapter is available on the device. Read [Set up
Bluetooth](https://developer.android.com/develop/connectivity/bluetooth/setup) for more information on
the `BluetoothAdapter`. The following example wraps this setup code in an
`initialize()` function that returns a `Boolean` value indicating success.


```kotlin
private const val TAG = "BluetoothLeService"

class BluetoothLeService : Service() {

    private var bluetoothAdapter: BluetoothAdapter? = null

    fun initialize(): Boolean {
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
        if (bluetoothAdapter == null) {
            Log.e(TAG, "Unable to obtain a BluetoothAdapter.")
            return false
        }
        return true
    }

    // ...
}
```

<br />

The activity calls this function within its `ServiceConnection` implementation.
Handling a false return value from the `initialize()` function depends on your
application. You could show an error message to the user indicating that the
current device does not support the Bluetooth operation or disable any features
that require Bluetooth to work. In the following example,
[`finish()`](https://developer.android.com/reference/android/app/Activity#finish()) is called on the activity
to send the user back to the previous screen.


```kotlin
class DeviceControlActivity : AppCompatActivity() {

    // Code to manage Service lifecycle.
    private val serviceConnection: ServiceConnection = object : ServiceConnection {
        override fun onServiceConnected(
            componentName: ComponentName,
            service: IBinder
        ) {
            bluetoothService = (service as LocalBinder).getService()
            bluetoothService?.let { bluetooth ->
                if (!bluetooth.initialize()) {
                    Log.e(TAG, "Unable to initialize Bluetooth")
                    finish()
                }
                // perform device connection
            }
        }

        override fun onServiceDisconnected(componentName: ComponentName) {
            bluetoothService = null
        }
    }

    // ...
}
```

<br />

## Connect to a device

Once the `BluetoothLeService` instance is initialized, it can connect to the BLE
device. The activity needs to send the device address to the service so it can
initiate the connection. The service will first call
[`getRemoteDevice()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#getRemoteDevice(java.lang.String))
on the `BluetoothAdapter` to access the device. If the adapter is unable to find
a device with that address, `getRemoteDevice()` throws an
[`IllegalArgumentException`](https://developer.android.com/reference/java/lang/IllegalArgumentException).


```kotlin
fun connect(address: String): Boolean {
    bluetoothAdapter?.let { adapter ->
        try {
            val device = adapter.getRemoteDevice(address)
        } catch (exception: IllegalArgumentException) {
            Log.w(TAG, "Device not found with provided address.")
            return false
        }
        // connect to the GATT server on the device
        return true
    } ?: run {
        Log.w(TAG, "BluetoothAdapter not initialized")
        return false
    }
}
```

<br />

The `DeviceControlActivity` calls this `connect()` function once the service is
initialized. The activity needs to pass in the address of the BLE device. In
the following example, the device address is passed to the activity as an intent
extra.


```kotlin
// Code to manage Service lifecycle.
private val serviceConnection: ServiceConnection = object : ServiceConnection {
    override fun onServiceConnected(
        componentName: ComponentName,
        service: IBinder
    ) {
        bluetoothService = (service as LocalBinder).getService()
        bluetoothService?.let { bluetooth ->
            if (!bluetooth.initialize()) {
                Log.e(TAG, "Unable to initialize Bluetooth")
                finish()
            }
            // perform device connection
            deviceAddress?.let { bluetooth.connect(it) }
        }
    }

    override fun onServiceDisconnected(componentName: ComponentName) {
        bluetoothService = null
    }
}
```

<br />

## Declare GATT callback

Once the activity tells the service which device to connect to and the service
connects to the device, the service needs to connect to the GATT server on the
BLE device. This connection requires a `BluetoothGattCallback` to receive
notifications about the connection state, service discovery, characteristic
reads, and characteristic notifications.

This topic focuses on the connection state notifications. See [Transfer BLE
data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data) for how to perform
service discovery, characteristic reads, and request characteristic
notifications.

The
[`onConnectionStateChange()`](https://developer.android.com/reference/android/bluetooth/BluetoothGattCallback#onConnectionStateChange(android.bluetooth.BluetoothGatt,%20int,%20int))
function is triggered when the connection to the device's GATT server changes.
In the following example, the callback is defined in the `Service` class so it
can be used with the
[`BluetoothDevice`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice) once the
service connects to it.


```kotlin
private val bluetoothGattCallback = object : BluetoothGattCallback() {
    override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
        if (newState == BluetoothProfile.STATE_CONNECTED) {
            // successfully connected to the GATT Server
        } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
            // disconnected from the GATT Server
        }
    }
}
```

<br />

## Connect to GATT service

Once the `BluetoothGattCallback` is declared, the service can use the
`BluetoothDevice` object from the `connect()` function to connect to the GATT
service on the device.

The
[`connectGatt()`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#connectGatt(android.content.Context,%20boolean,%20android.bluetooth.BluetoothGattCallback))
function is used. This requires a `Context` object, an `autoConnect` boolean
flag, and the `BluetoothGattCallback`. In this example, the app is directly
connecting to the BLE device, so `false` is passed for `autoConnect`.

A `BluetoothGatt` property is also added. This allows the service to [close the
connection](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#close()) when it is no
longer needed.


```kotlin
class BluetoothLeService : Service() {

    // ...
    private var bluetoothGatt: BluetoothGatt? = null

    // ...
    fun connect(address: String): Boolean {
        bluetoothAdapter?.let { adapter ->
            try {
                val device = adapter.getRemoteDevice(address)
                // connect to the GATT server on the device
                bluetoothGatt = device.connectGatt(this, false, bluetoothGattCallback)
                return true
            } catch (exception: IllegalArgumentException) {
                Log.w(TAG, "Device not found with provided address.  Unable to connect.")
                return false
            }
        } ?: run {
            Log.w(TAG, "BluetoothAdapter not initialized")
            return false
        }
    }
}
```

<br />

## Broadcast updates

When the server connects or disconnects from the GATT server, it needs to notify
the activity of the new state. There are several ways to accomplish this. The
following example uses [broadcasts](https://developer.android.com/guide/components/broadcasts) to send the
information from the service to activity.

The service declares a function to broadcast the new state. This function takes
in an action string which is passed to an `Intent` object before being broadcast
to the system.


```kotlin
private fun broadcastUpdate(action: String) {
    val intent = Intent(action)
    sendBroadcast(intent)
}
```

<br />

Once the broadcast function is in place, it is used within the
`BluetoothGattCallback` to send information about the connection state with the
GATT server. Constants and the service's current connection state are declared
in the service representing the `Intent` actions.


```kotlin
class BluetoothLeService : Service() {

    private var connectionState = STATE_DISCONNECTED

    private val bluetoothGattCallback = object : BluetoothGattCallback() {
        override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                // successfully connected to the GATT Server
                connectionState = STATE_CONNECTED
                broadcastUpdate(ACTION_GATT_CONNECTED)
            } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                // disconnected from the GATT Server
                connectionState = STATE_DISCONNECTED
                broadcastUpdate(ACTION_GATT_DISCONNECTED)
            }
        }
    }

    // ...
    companion object {
        const val ACTION_GATT_CONNECTED =
            "com.example.bluetooth.le.ACTION_GATT_CONNECTED"
        const val ACTION_GATT_DISCONNECTED =
            "com.example.bluetooth.le.ACTION_GATT_DISCONNECTED"

        private const val STATE_DISCONNECTED = 0
        private const val STATE_CONNECTED = 2
    }
}
```

<br />

## Listen for updates in activity

Once the service broadcasts the connection updates, the activity needs to
implement a [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver).
Register this receiver when setting up the activity, and unregister it when the
activity is leaving the screen. By listening for the events from the service,
the activity is able to update the user interface based on the current
connection state with the BLE device.


```kotlin
class DeviceControlActivity : AppCompatActivity() {

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
            }
        }
    }

    override fun onResume() {
        super.onResume()
        registerReceiver(gattUpdateReceiver, makeGattUpdateIntentFilter())
        bluetoothService?.let { service ->
            deviceAddress?.let { address ->
                val result = service.connect(address)
                Log.d(TAG, "Connect request result=$result")
            }
        }
    }

    override fun onPause() {
        super.onPause()
        unregisterReceiver(gattUpdateReceiver)
    }

    private fun makeGattUpdateIntentFilter(): IntentFilter {
        return IntentFilter().apply {
            addAction(BluetoothLeService.ACTION_GATT_CONNECTED)
            addAction(BluetoothLeService.ACTION_GATT_DISCONNECTED)
        }
    }
}
```

<br />

In [Transfer BLE data](https://developer.android.com/develop/connectivity/bluetooth/ble/transfer-ble-data),
the `BroadcastReceiver` is also used to communicate the service discovery as
well as the characteristic data from the device.

## Close GATT connection

One important step when dealing with Bluetooth connections is to close the
connection when you are finished with it. To do this, call the `close()`
function on the `BluetoothGatt` object. In the following example, the service
holds the reference to the `BluetoothGatt`. When the activity unbinds from the
service, the connection is closed to avoid draining the device battery.


```kotlin
class BluetoothLeService : Service() {

    // ...
    override fun onUnbind(intent: Intent?): Boolean {
        close()
        return super.onUnbind(intent)
    }

    private fun close() {
        bluetoothGatt?.let { gatt ->
            gatt.close()
            bluetoothGatt = null
        }
    }
}
```

<br />