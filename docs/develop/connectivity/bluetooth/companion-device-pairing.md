---
title: Companion device pairing  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Companion device pairing Stay organized with collections Save and categorize content based on your preferences.



On devices running Android 8.0 (API level 26) and higher, companion device
pairing performs a Bluetooth or Wi-Fi scan of nearby devices on behalf of your
app without requiring the
[`ACCESS_FINE_LOCATION`](/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission. This helps maximize user privacy protections. Use this method to
perform the initial configuration of the companion device, such as a BLE-capable
smart watch. In addition, companion device pairing requires Location Services to
be enabled.

Companion device pairing doesn't create connections on its own nor enable
continuous scanning. Apps can use Bluetooth or Wi-Fi connectivity APIs to
establish connections.

After the device is paired, the device can use the
[`REQUEST_COMPANION_RUN_IN_BACKGROUND`](/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)
and
[`REQUEST_COMPANION_USE_DATA_IN_BACKGROUND`](/reference/android/Manifest.permission#REQUEST_COMPANION_USE_DATA_IN_BACKGROUND)
permissions to start the app from background. Apps can also use
[`REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND`](/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)
permission to start a foreground service from background.

A user can select a device from a list and grant the app permissions to access
the device. These permissions are revoked if you uninstall the app or call
[`disassociate()`](/reference/android/companion/CompanionDeviceManager#disassociate(java.lang.String)).
The companion app is responsible for clearing its own associations if the user
no longer needs them, such as when they log out or remove bound devices.

## Implement companion device pairing

This section explains how use the [`CompanionDeviceManager`](/reference/android/companion/CompanionDeviceManager) to pair your
app with companion devices over Bluetooth, BLE, and Wi-Fi.

### Specify companion devices

The following code sample shows how to add the
[`<uses-feature>`](/guide/topics/manifest/uses-feature-element) flag to a
manifest file. This tells the system that your app intends to set up companion
devices.

```
<uses-feature android:name="android.software.companion_device_setup"/>
```

### List devices by [`DeviceFilter`](/reference/android/companion/DeviceFilter)

You can display all in-range companion devices that match the
[`DeviceFilter`](/reference/android/companion/DeviceFilter)
you provide (shown in figure 1). If you want to limit the scanning to only one
device, you can
[`setSingleDevice()`](/reference/android/companion/AssociationRequest.Builder#setSingleDevice(boolean))
to `true` (shown in figure 2).

![Companion devices pairing](/static/images/develop/connectivity/companion-device-pairing-1.png)


**Figure 1.** Companion devices pairing


![Single device pairing](/static/images/develop/connectivity/companion-device-pairing-2.png)


**Figure 2.** Single device pairing

The following are the subclasses of [`DeviceFilter`](/reference/android/companion/DeviceFilter) that
can be specified in [`AssociationRequest`](/reference/android/companion/AssociationRequest):

* [`BluetoothDeviceFilter`](/reference/android/companion/BluetoothDeviceFilter)
* [`BluetoothLeDeviceFilter`](/reference/android/companion/BluetoothLeDeviceFilter)
* [`WifiDeviceFilter`](/reference/android/companion/WifiDeviceFilter)

All three subclasses have builders that streamline the configuration of filters.
In the following example, a device scans for a Bluetooth device with a
[`BluetoothDeviceFilter`](/reference/android/companion/BluetoothDeviceFilter).

### Kotlin

```
val deviceFilter: BluetoothDeviceFilter = BluetoothDeviceFilter.Builder()
        // Match only Bluetooth devices whose name matches the pattern.
        .setNamePattern(Pattern.compile("My device"))
        // Match only Bluetooth devices whose service UUID matches this pattern.
        .addServiceUuid(ParcelUuid(UUID(0x123abcL, -1L)), null)
        .build()
```

### Java

```
BluetoothDeviceFilter deviceFilter = new BluetoothDeviceFilter.Builder()
        // Match only Bluetooth devices whose name matches the pattern.
        .setNamePattern(Pattern.compile("My device"))
        // Match only Bluetooth devices whose service UUID matches this pattern.
        .addServiceUuid(new ParcelUuid(new UUID(0x123abcL, -1L)), null)
        .build();
```

Set a [`DeviceFilter`](/reference/android/companion/DeviceFilter) to an [`AssociationRequest`](/reference/android/companion/AssociationRequest) so
[`CompanionDeviceManager`](/reference/android/companion/CompanionDeviceManager) can determine what type of devices to seek.

### Kotlin

```
val pairingRequest: AssociationRequest = AssociationRequest.Builder()
        // Find only devices that match this request filter.
        .addDeviceFilter(deviceFilter)
        // Stop scanning as soon as one device matching the filter is found.
        .setSingleDevice(true)
        .build()
```

### Java

```
AssociationRequest pairingRequest = new AssociationRequest.Builder()
        // Find only devices that match this request filter.
        .addDeviceFilter(deviceFilter)
        // Stop scanning as soon as one device matching the filter is found.
        .setSingleDevice(true)
        .build();
```

After your app initializes an [`AssociationRequest`](/reference/android/companion/AssociationRequest), run the
[`associate()`](/reference/android/companion/CompanionDeviceManager#associate(android.companion.AssociationRequest,%20java.util.concurrent.Executor,%20android.companion.CompanionDeviceManager.Callback))
function on the [`CompanionDeviceManager`](/reference/android/companion/CompanionDeviceManager). The [`associate()`](/reference/android/companion/CompanionDeviceManager#associate(android.companion.AssociationRequest,%20java.util.concurrent.Executor,%20android.companion.CompanionDeviceManager.Callback)) function
takes in an [`AssociationRequest`](/reference/android/companion/AssociationRequest) and a [`Callback`](/reference/android/companion/CompanionDeviceManager.Callback).

The [`Callback`](/reference/android/companion/CompanionDeviceManager.Callback) returns an
[`IntentSender`](/reference/android/content/IntentSender) in the
[`onAssociationPending`](/reference/android/companion/CompanionDeviceManager.Callback#onAssociationPending(android.content.IntentSender)) when [`CompanionDeviceManager`](/reference/android/companion/CompanionDeviceManager) locates a device
and it's ready to launch a user consent dialog.
After the user confirms the device, an [`AssociationInfo`](/reference/android/companion/AssociationInfo)
of the device is returned in [`onAssociationCreated`](/reference/android/companion/CompanionDeviceManager.Callback#onAssociationCreated(android.companion.AssociationInfo)).
If your app doesn't find any devices, the callback returns [`onFailure`](/reference/android/companion/CompanionDeviceManager.Callback#onFailure(java.lang.CharSequence))
with an error message.

On devices running Android 13 (API level 33) and higher:

### Kotlin

```
val deviceManager =
  requireContext().getSystemService(Context.COMPANION_DEVICE_SERVICE)

val executor: Executor =  Executor { it.run() }

deviceManager.associate(pairingRequest,
    executor,
    object : CompanionDeviceManager.Callback() {
    // Called when a device is found. Launch the IntentSender so the user
    // can select the device they want to pair with.
    override fun onAssociationPending(intentSender: IntentSender) {
        intentSender?.let {
             startIntentSenderForResult(it, SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0)
        }
    }

    override fun onAssociationCreated(associationInfo: AssociationInfo) {
        // An association is created.
    }

    override fun onFailure(errorMessage: CharSequence?) {
        // To handle the failure.
     }
})
```

### Java

```
CompanionDeviceManager deviceManager =
        (CompanionDeviceManager) getSystemService(Context.COMPANION_DEVICE_SERVICE);

Executor executor = new Executor() {
            @Override
            public void execute(Runnable runnable) {
                runnable.run();
            }
        };
deviceManager.associate(pairingRequest, new CompanionDeviceManager.Callback() {
    executor,
    // Called when a device is found. Launch the IntentSender so the user can
    // select the device they want to pair with.
    @Override
    public void onDeviceFound(IntentSender chooserLauncher) {
        try {
            startIntentSenderForResult(
                    chooserLauncher, SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0
            );
        } catch (IntentSender.SendIntentException e) {
            Log.e("MainActivity", "Failed to send intent");
        }
    }

    @Override
    public void onAssociationCreated(AssociationInfo associationInfo) {
        // An association is created.
    }

    @Override
    public void onFailure(CharSequence errorMessage) {
        // To handle the failure.
    });
```

On devices running Android 12L (API level 32) or lower (deprecated):

### Kotlin

```
val deviceManager =
      requireContext().getSystemService(Context.COMPANION_DEVICE_SERVICE)

deviceManager.associate(pairingRequest,
    object : CompanionDeviceManager.Callback() {
        // Called when a device is found. Launch the IntentSender so the user
        // can select the device they want to pair with.
        override fun onDeviceFound(chooserLauncher: IntentSender) {
            startIntentSenderForResult(chooserLauncher,
                SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0)
        }

        override fun onFailure(error: CharSequence?) {
            // To handle the failure.
        }
    }, null)
```

### Java

```
CompanionDeviceManager deviceManager =
        (CompanionDeviceManager) getSystemService(Context.COMPANION_DEVICE_SERVICE);
deviceManager.associate(pairingRequest, new CompanionDeviceManager.Callback() {
    // Called when a device is found. Launch the IntentSender so the user can
    // select the device they want to pair with.
    @Override
    public void onDeviceFound(IntentSender chooserLauncher) {
        try {
            startIntentSenderForResult(
                    chooserLauncher, SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0
            );
        } catch (IntentSender.SendIntentException e) {
            Log.e("MainActivity", "Failed to send intent");
        }
    }

    @Override
    public void onFailure(CharSequence error) {
        // To handle the failure.
    }
}, null);
```

The result of user selection is sent back to the fragment in the
[`onActivityResult()`](/reference/android/app/Activity#onActivityResult(int,%20int,%20android.content.Intent))
of your activity. You can then access the selected device.

When the user selects a Bluetooth device, expect a
[`BluetoothDevice`](/reference/android/bluetooth/BluetoothDevice).
When the user selects a Bluetooth LE device, expect a
[`android.bluetooth.le.ScanResult`](/reference/android/bluetooth/le/ScanResult).
When the user selects a Wi-Fi device, expect a
[`android.net.wifi.ScanResult`](/reference/android/net/wifi/ScanResult).

### Kotlin

```
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    when (requestCode) {
        SELECT_DEVICE_REQUEST_CODE -> when(resultCode) {
            Activity.RESULT_OK -> {
                // The user chose to pair the app with a Bluetooth device.
                val deviceToPair: BluetoothDevice? =
data?.getParcelableExtra(CompanionDeviceManager.EXTRA_DEVICE)
                deviceToPair?.let { device ->
                    device.createBond()
                    // Continue to interact with the paired device.
                }
            }
        }
        else -> super.onActivityResult(requestCode, resultCode, data)
    }
}
```

### Java

```
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    if (resultCode != Activity.RESULT_OK) {
        return;
    }
    if (requestCode == SELECT_DEVICE_REQUEST_CODE && data != null) {
        BluetoothDevice deviceToPair =
data.getParcelableExtra(CompanionDeviceManager.EXTRA_DEVICE);
        if (deviceToPair != null) {
            deviceToPair.createBond();
            // Continue to interact with the paired device.
        }
    } else {
        super.onActivityResult(requestCode, resultCode, data);
    }
}
```

See the complete example:

On devices running Android 13 (API level 33) and higher:

### Kotlin

```
private const val SELECT_DEVICE_REQUEST_CODE = 0

class MainActivity : AppCompatActivity() {

    private val deviceManager: CompanionDeviceManager by lazy {
        getSystemService(Context.COMPANION_DEVICE_SERVICE) as CompanionDeviceManager
    }
    val mBluetoothAdapter: BluetoothAdapter by lazy {
        val java = BluetoothManager::class.java
        getSystemService(java)!!.adapter }
    val executor: Executor =  Executor { it.run() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // To skip filters based on names and supported feature flags (UUIDs),
        // omit calls to setNamePattern() and addServiceUuid()
        // respectively, as shown in the following  Bluetooth example.
        val deviceFilter: BluetoothDeviceFilter = BluetoothDeviceFilter.Builder()
            .setNamePattern(Pattern.compile("My device"))
            .addServiceUuid(ParcelUuid(UUID(0x123abcL, -1L)), null)
            .build()

        // The argument provided in setSingleDevice() determines whether a single
        // device name or a list of them appears.
        val pairingRequest: AssociationRequest = AssociationRequest.Builder()
            .addDeviceFilter(deviceFilter)
            .setSingleDevice(true)
            .build()

        // When the app tries to pair with a Bluetooth device, show the
        // corresponding dialog box to the user.
        deviceManager.associate(pairingRequest,
            executor,
            object : CompanionDeviceManager.Callback() {
                // Called when a device is found. Launch the IntentSender so the user
                // can select the device they want to pair with.
                override fun onAssociationPending(intentSender: IntentSender) {
                intentSender?.let {
                    startIntentSenderForResult(it, SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0)
              }
            }

             override fun onAssociationCreated(associationInfo: AssociationInfo) {
                 // AssociationInfo object is created and get association id and the
                 // macAddress.
                 var associationId: int = associationInfo.id
                 var macAddress: MacAddress = associationInfo.deviceMacAddress
             }
             override fun onFailure(errorMessage: CharSequence?) {
                // Handle the failure.
            }
    )

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        when (requestCode) {
            SELECT_DEVICE_REQUEST_CODE -> when(resultCode) {
                Activity.RESULT_OK -> {
                    // The user chose to pair the app with a Bluetooth device.
                    val deviceToPair: BluetoothDevice? =
                        data?.getParcelableExtra(CompanionDeviceManager.EXTRA_DEVICE)
                    deviceToPair?.let { device ->
                        device.createBond()
                        // Maintain continuous interaction with a paired device.
                    }
                }
            }
            else -> super.onActivityResult(requestCode, resultCode, data)
        }
    }
}
```

### Java

```
class MainActivityJava extends AppCompatActivity {

    private static final int SELECT_DEVICE_REQUEST_CODE = 0;
    Executor executor = new Executor() {
        @Override
        public void execute(Runnable runnable) {
            runnable.run();
        }
    };

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CompanionDeviceManager deviceManager =
            (CompanionDeviceManager) getSystemService(
                Context.COMPANION_DEVICE_SERVICE
            );

        // To skip filtering based on name and supported feature flags,
        // do not include calls to setNamePattern() and addServiceUuid(),
        // respectively. This example uses Bluetooth.
        BluetoothDeviceFilter deviceFilter =
            new BluetoothDeviceFilter.Builder()
                .setNamePattern(Pattern.compile("My device"))
                .addServiceUuid(
                    new ParcelUuid(new UUID(0x123abcL, -1L)), null
                )
                .build();

        // The argument provided in setSingleDevice() determines whether a single
        // device name or a list of device names is presented to the user as
        // pairing options.
        AssociationRequest pairingRequest = new AssociationRequest.Builder()
            .addDeviceFilter(deviceFilter)
            .setSingleDevice(true)
            .build();

        // When the app tries to pair with the Bluetooth device, show the
        // appropriate pairing request dialog to the user.
        deviceManager.associate(pairingRequest, new CompanionDeviceManager.Callback() {
            executor,
           // Called when a device is found. Launch the IntentSender so the user can
           // select the device they want to pair with.
           @Override
           public void onDeviceFound(IntentSender chooserLauncher) {
               try {
                   startIntentSenderForResult(
                       chooserLauncher, SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0
                   );
               } catch (IntentSender.SendIntentException e) {
                   Log.e("MainActivity", "Failed to send intent");
               }
           }

          @Override
          public void onAssociationCreated(AssociationInfo associationInfo) {
                 // AssociationInfo object is created and get association id and the
                 // macAddress.
                 int associationId = associationInfo.getId();
                 MacAddress macAddress = associationInfo.getDeviceMacAddress();
          }

          @Override
          public void onFailure(CharSequence errorMessage) {
             // Handle the failure.
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        if (resultCode != Activity.RESULT_OK) {
            return;
        }
        if (requestCode == SELECT_DEVICE_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK && data != null) {
                BluetoothDevice deviceToPair = data.getParcelableExtra(
                    CompanionDeviceManager.EXTRA_DEVICE
                );

                if (deviceToPair != null) {
                    deviceToPair.createBond();
                    // ... Continue interacting with the paired device.
                }
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}
```

On devices running Android 12L (API level 32) or lower (deprecated):

### Kotlin

```
private const val SELECT_DEVICE_REQUEST_CODE = 0

class MainActivity : AppCompatActivity() {

    private val deviceManager: CompanionDeviceManager by lazy {
        getSystemService(Context.COMPANION_DEVICE_SERVICE) as CompanionDeviceManager
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // To skip filters based on names and supported feature flags (UUIDs),
        // omit calls to setNamePattern() and addServiceUuid()
        // respectively, as shown in the following  Bluetooth example.
        val deviceFilter: BluetoothDeviceFilter = BluetoothDeviceFilter.Builder()
            .setNamePattern(Pattern.compile("My device"))
            .addServiceUuid(ParcelUuid(UUID(0x123abcL, -1L)), null)
            .build()

        // The argument provided in setSingleDevice() determines whether a single
        // device name or a list of them appears.
        val pairingRequest: AssociationRequest = AssociationRequest.Builder()
            .addDeviceFilter(deviceFilter)
            .setSingleDevice(true)
            .build()

        // When the app tries to pair with a Bluetooth device, show the
        // corresponding dialog box to the user.
        deviceManager.associate(pairingRequest,
            object : CompanionDeviceManager.Callback() {

                override fun onDeviceFound(chooserLauncher: IntentSender) {
                    startIntentSenderForResult(chooserLauncher,
                        SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0)
                }

                override fun onFailure(error: CharSequence?) {
                    // Handle the failure.
                }
            }, null)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        when (requestCode) {
            SELECT_DEVICE_REQUEST_CODE -> when(resultCode) {
                Activity.RESULT_OK -> {
                    // The user chose to pair the app with a Bluetooth device.
                    val deviceToPair: BluetoothDevice? =
                        data?.getParcelableExtra(CompanionDeviceManager.EXTRA_DEVICE)
                    deviceToPair?.let { device ->
                        device.createBond()
                        // Maintain continuous interaction with a paired device.
                    }
                }
            }
            else -> super.onActivityResult(requestCode, resultCode, data)
        }
    }
}
```

### Java

```
class MainActivityJava extends AppCompatActivity {

    private static final int SELECT_DEVICE_REQUEST_CODE = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CompanionDeviceManager deviceManager =
            (CompanionDeviceManager) getSystemService(
                Context.COMPANION_DEVICE_SERVICE
            );

        // To skip filtering based on name and supported feature flags,
        // don't include calls to setNamePattern() and addServiceUuid(),
        // respectively. This example uses Bluetooth.
        BluetoothDeviceFilter deviceFilter =
            new BluetoothDeviceFilter.Builder()
                .setNamePattern(Pattern.compile("My device"))
                .addServiceUuid(
                    new ParcelUuid(new UUID(0x123abcL, -1L)), null
                )
                .build();

        // The argument provided in setSingleDevice() determines whether a single
        // device name or a list of device names is presented to the user as
        // pairing options.
        AssociationRequest pairingRequest = new AssociationRequest.Builder()
            .addDeviceFilter(deviceFilter)
            .setSingleDevice(true)
            .build();

        // When the app tries to pair with the Bluetooth device, show the
        // appropriate pairing request dialog to the user.
        deviceManager.associate(pairingRequest,
            new CompanionDeviceManager.Callback() {
                @Override
                public void onDeviceFound(IntentSender chooserLauncher) {
                    try {
                        startIntentSenderForResult(chooserLauncher,
                            SELECT_DEVICE_REQUEST_CODE, null, 0, 0, 0);
                    } catch (IntentSender.SendIntentException e) {
                        // failed to send the intent
                    }
                }

                @Override
                public void onFailure(CharSequence error) {
                    // handle failure to find the companion device
                }
            }, null);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        if (requestCode == SELECT_DEVICE_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK && data != null) {
                BluetoothDevice deviceToPair = data.getParcelableExtra(
                    CompanionDeviceManager.EXTRA_DEVICE
                );

                if (deviceToPair != null) {
                    deviceToPair.createBond();
                    // ... Continue interacting with the paired device.
                }
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}
```

### Companion device profiles

On Android 12 (API level 31) and higher, companion apps that manage devices like
watches can use companion device profiles to streamline the setup process by
granting necessary permissions when pairing. For more information, see
[Companion Device Profiles](https://source.android.com/docs/core/connect/companion-device-profile).

### Keep companion apps awake

Starting with Android 16 (API level 36),

[`CompanionDeviceManager.startObservingDevicePresence(String)`](/reference/android/companion/CompanionDeviceManager#startObservingDevicePresence(java.lang.String))
and
[`CompanionDeviceService.onDeviceAppeared()`](/reference/android/companion/CompanionDeviceService#onDeviceAppeared(java.lang.String))
are deprecated.

* You should use
  [`CompanionDeviceManager.startObservingDevicePresence
  (ObservingDevicePresenceRequest)`](/reference/android/companion/CompanionDeviceManager#startObservingDevicePresence(android.companion.ObservingDevicePresenceRequest)) to automatically
  manage the binding of your implemented [`CompanionDeviceService`](/reference/android/companion/CompanionDeviceService).

  + The binding state of your [`CompanionDeviceService`](/reference/android/companion/CompanionDeviceService) is automatically
    managed based on the presence status of its associated companion device:
    1. The service is bound when the companion device is within BLE range or
       connected using Bluetooth.
    2. The service becomes unbound when the companion device moves
       out of BLE range or its Bluetooth connection is terminated.
* App will receives callback based on various of [`DevicePresenceEvent`](/reference/android/companion/CompanionDeviceService#onDevicePresenceEvent(android.companion.DevicePresenceEvent)).

  For details, see
  [`CompanionDeviceService.onDeviceEvent()`](/reference/android/companion/DevicePresenceEvent).