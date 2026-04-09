---
title: https://developer.android.com/health-and-fitness/fitness/basic-app/integrate-wear-os
url: https://developer.android.com/health-and-fitness/fitness/basic-app/integrate-wear-os
source: md.txt
---

Enhance your app's health and fitness experience by expanding it onto wearable
devices powered by [Wear OS](https://developer.android.com/wear).

## Add a Wear OS module

Android Studio provides a handy wizard to add a Wear OS module to your app. In
the **File \> New Module** menu, select **Wear OS**, as shown in the following
image:
![Wear OS module wizard in Android Studio](https://developer.android.com/static/health-and-fitness/fitness/basic-app/images/basic_fitness_app_img_8.png) **Figure 1**: Create a Wear OS module

It's important to note that the **Minimum SDK** must be **API 30** or higher
to let you use the latest version of Health Services. Health Services
makes it easier to track metrics and record data by configuring health
sensors automatically.

After you complete the wizard, sync your project. The following **Run**
configuration appears:
![An image showing the Wear OS app run button](https://developer.android.com/static/health-and-fitness/fitness/basic-app/images/basic_fitness_app_img_5.png) **Figure 2**: Run button for the new Wear OS module

This lets you run the Wear OS module on a wearable device. You have two options:

- Run on an [emulator](https://developer.android.com/training/wearables/get-started/creating#run-emulator).

- Run on a [real device](https://developer.android.com/training/wearables/get-started/creating#run-watch).

Running the configuration deploys the app to the Wear OS emulator or
device and shows a "hello world" experience. This is the basic UI setup, using
Compose for Wear OS, to get started with your app.

## Add Health Services and Hilt

Integrate the following libraries into your Wear OS module:

- **[Health Services](https://developer.android.com/health-and-fitness/guides/health-services):** makes accessing sensors and data on the watch very convenient and more power-efficient.
- **[Hilt](https://developer.android.com/training/dependency-injection/hilt-android):** Allows for effective dependency injection and management.

## Create the Health Services Manager

To make using [Health Services](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService) a bit more convenient, and expose a smaller
and smoother API, you can create a wrapper like this:  

    private const val TAG = "WATCHMAIN"

    class HealthServicesManager(context: Context) {
        private val measureClient = HealthServices.getClient(context).measureClient

        suspend fun hasHeartRateCapability() = runCatching {
            val capabilities = measureClient.getCapabilities()
            (DataType.HEART_RATE_BPM in capabilities.supportedDataTypesMeasure)
        }.getOrDefault(false)

        /**
         * Returns a cold flow. When activated, the flow will register a callback for heart rate data
         * and start to emit messages. When the consuming coroutine is canceled, the measure callback
         * is unregistered.
         *
         * [callbackFlow] creates a  bridge between a callback-based API and Kotlin flows.
         */
        @ExperimentalCoroutinesApi
        fun heartRateMeasureFlow(): Flow<MeasureMessage> = callbackFlow {
            val callback = object : MeasureCallback {
                override fun onAvailabilityChanged(dataType: DeltaDataType<*, *>, availability: Availability) {
                    // Only send back DataTypeAvailability (not LocationAvailability)
                    if (availability is DataTypeAvailability) {
                        trySendBlocking(MeasureMessage.MeasureAvailability(availability))
                    }
                }

                override fun onDataReceived(data: DataPointContainer) {
                    val heartRateBpm = data.getData(DataType.HEART_RATE_BPM)
                    Log.d(TAG, "💓 Received heart rate: ${heartRateBpm.first().value}")
                    trySendBlocking(MeasureMessage.MeasureData(heartRateBpm))
                }
            }

            Log.d(TAG, "⌛ Registering for data...")
            measureClient.registerMeasureCallback(DataType.HEART_RATE_BPM, callback)

            awaitClose {
                Log.d(TAG, "👋 Unregistering for data")
                runBlocking {
                    measureClient.unregisterMeasureCallback(DataType.HEART_RATE_BPM, callback)
                }
            }
        }
    }

    sealed class MeasureMessage {
        class MeasureAvailability(val availability: DataTypeAvailability) : MeasureMessage()
        class MeasureData(val data: List<SampleDataPoint<Double>>) : MeasureMessage()
    }

Once you have created the Hilt module to manage it, using the following snippet:  

    @Module
    @InstallIn(SingletonComponent::class)
    internal object DataModule {
        @Provides
        @Singleton
        fun provideHealthServices(@ApplicationContext context: Context): HealthServicesManager = HealthServicesManager(context)
    }

you can inject the `HealthServicesManager` as any other Hilt dependency.

The new `HealthServicesManager` provides a `heartRateMeasureFlow()` method that
registers a listener for the heart monitor and emits the received data.

## Enable data updates on wearable devices

Fitness-related data updates require the `BODY_SENSORS` permission. If you
haven't done so already, declare the `BODY_SENSORS` permission in your
app's manifest file. Then, request the permission, as shown in this snippet:  

    val permissionState = rememberPermissionState(
        permission = Manifest.permission.BODY_SENSORS,
        onPermissionResult = { granted -> /* do something */ }
    )

    [...]

    if (permissionState.status.isGranted) {
        // do something
    } else {
        permissionState.launchPermissionRequest()
    }

If you test your app on a physical device, data should start updating.

Starting in Wear OS 4, emulators also show test data automatically. On previous
versions, you can simulate the data stream from the sensor. In a terminal
window, run this ADB command:  

    adb shell am broadcast \
    -a "whs.USE_SYNTHETIC_PROVIDERS" \
    com.google.android.wearable.healthservices

To see different heart rate values, try simulating different exercises.
This command simulates walking:  

    adb shell am broadcast \
    -a "whs.synthetic.user.START_WALKING" \
    com.google.android.wearable.healthservices

This command simulates running:  

    adb shell am broadcast \
    -a "whs.synthetic.user.START_RUNNING" \
    com.google.android.wearable.healthservices

To stop simulating the data, run this command:  

    adb shell am broadcast -a \
    "whs.USE_SENSOR_PROVIDERS" \
    com.google.android.wearable.healthservices

## Read heart rate data

With the `BODY_SENSORS` permission granted, you can read the user's heart rate
(`heartRateMeasureFlow()`) in the `HealthServicesManager`. In the Wear OS app's
UI, the current heart rate value appears, being measured by the sensor on the
wearable device.

In your `ViewModel`, start collecting data using the heart rate flow object,
as shown in the following snippet:  

    val hr: MutableState<Double> = mutableStateOf(0.0)

    [...]

    healthServicesManager
        .heartRateMeasureFlow()
        .takeWhile { enabled.value }
        .collect { measureMessage ->
            when (measureMessage) {
                is MeasureData -> {
                    val latestHeartRateValue = measureMessage.data.last().value
                    hr.value = latestHeartRateValue
                }

                is MeasureAvailability -> availability.value =
                        measureMessage.availability
            }
        }

Use a composable object similar to the following to display the live data in
your app's UI:  

    val heartRate by viewModel.hr

    Text(
      text = "Heart Rate: $heartRate",
      style = MaterialTheme.typography.display1
    )

## Send data to a handheld device

To send health and fitness data to a handheld device, use the `DataClient`
class in Health Services. The following code snippet shows how to send heart
rate data that your app previously collected:  

    class HealthServicesManager(context: Context) {
        private val dataClient by lazy { Wearable.getDataClient(context) }

    [...]

        suspend fun sendToHandheldDevice(heartRate: Int) {
            try {
                val result = dataClient
                    .putDataItem(PutDataMapRequest
                        .create("/heartrate")
                        .apply { dataMap.putInt("heartrate", heartRate) }
                        .asPutDataRequest()
                        .setUrgent())
                    .await()

                Log.d(TAG, "DataItem saved: $result")
            } catch (cancellationException: CancellationException) {
                throw cancellationException
            } catch (exception: Exception) {
                Log.d(TAG, "Saving DataItem failed: $exception")
            }
        }
    }

## Receive the data on the phone

To receive the data on the phone, create a
[`WearableListenerService`](https://developers.google.com/android/reference/com/google/android/gms/wearable/WearableListenerService):  

    @AndroidEntryPoint
    class DataLayerListenerService : WearableListenerService() {

        @Inject
        lateinit var heartRateMonitor: HeartRateMonitor

        override fun onDataChanged(dataEvents: DataEventBuffer) {

            dataEvents.forEach { event ->
                when (event.type) {
                    DataEvent.TYPE_CHANGED -> {
                        event.dataItem.run {
                            if (uri.path?.compareTo("/heartrate") == 0) {
                                val heartRate = DataMapItem.fromDataItem(this)
                                        .dataMap.getInt(HR_KEY)
                                Log.d("DataLayerListenerService",
                                        "New heart rate value received: $heartRate")
                                heartRateMonitor.send(heartRate)
                            }
                        }
                    }

                    DataEvent.TYPE_DELETED -> {
                        // DataItem deleted
                    }
                }
            }
        }
    }

Upon completion of this step, notice a few interesting details:

- The `@AndroidEntryPoint` annotation lets us use Hilt in this class
- The `@Inject lateinit var heartRateMonitor: HeartRateMonitor` will indeed inject a dependency in this class
- The class implements `onDataChanged()` and receives a collection of events that you can parse and use

The following `HeartRateMonitor` logic lets you send the received heart rate
values to another part of your app's codebase:  

    class HeartRateMonitor {
        private val datapoints = MutableSharedFlow<Int>(extraBufferCapacity = 10)

        fun receive(): SharedFlow<Int> = datapoints.asSharedFlow()

        fun send(hr: Int) {
            datapoints.tryEmit(hr)
        }
    }

A data bus receives the events from the `onDataChanged()` method and makes them
available to data observers using a `SharedFlow`.

The final bit is the declaration of the `Service` in the phone application
`AndroidManifest.xml`:  

    <service
        android:name=".DataLayerListenerService"
        android:exported="true">
        <intent-filter>
            <!-- listeners receive events that match the action and data filters -->
            <action android:name="com.google.android.gms.wearable.DATA_CHANGED" />
            <data
                android:host="*"
                android:pathPrefix="/heartrate"
                android:scheme="wear" />
        </intent-filter>
    </service>

## Show real-time data on a handheld device

In the part of your app that runs on a handheld device, inject the
`HeartRateMonitor` into your view model's constructor. This `HeartRateMonitor`
object observes the heart rate data and emits UI updates as needed.