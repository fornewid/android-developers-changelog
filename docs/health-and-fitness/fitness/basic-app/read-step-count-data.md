---
title: https://developer.android.com/health-and-fitness/fitness/basic-app/read-step-count-data
url: https://developer.android.com/health-and-fitness/fitness/basic-app/read-step-count-data
source: md.txt
---

| **Note:** This guide uses `SensorManager` for retrieving steps data. We recommend using the [Recording API on mobile](https://developer.android.com/health-and-fitness/guides/recording-api) for recording steps in a power-efficient way.

Use Sensor Manager to populate steps data in a mobile app, as described in this
guide. For more information about how to design and manage an exercise app UI,
refer to [Build a basic fitness app](https://developer.android.com/health-and-fitness/guides/basic-fitness-app/overview).

## Getting started

To get started with measuring the steps of your basic step counter from your
mobile device, you will need to add the dependencies to your app module
`build.gradle` file. Verify that you use the latest versions of dependencies.
Also, when you extend your app's support to other form factors, such as Wear OS,
add the dependencies that these form factors require.

The following are a few examples of some of the UI dependencies. For a complete
list, refer to this [UI Elements](https://developer.android.com/jetpack/androidx/releases/compose-ui) guide.  

    implementation(platform("androidx.compose:compose-bom:2023.10.01"))
    implementation("androidx.activity:activity-compose")
    implementation("androidx.compose.foundation:foundation")
    implementation("androidx.compose.material:material")

## Obtain the step counter sensor

After the user has granted the necessary [activity recognition permission](https://developer.android.com/health-and-fitness/guides/basic-fitness-app/overview#request-permissions),
you can access the step counter sensor:

1. Obtain the `SensorManager` object from `getSystemService()`.
2. Acquire the step counter sensor from the `SensorManager`:

    private val sensorManager by lazy {
            getSystemService(Context.SENSOR_SERVICE) as SensorManager }
    private val sensor: Sensor? by lazy {
            sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER) }

Some devices don't have the step counter sensor. You should check for the sensor
and show an error message if the device doesn't have one:  

    if (sensor == null) {
        Text(text = "Step counter sensor is not present on this device")
    }

## Create your foreground service

In a basic fitness app, you might have a [button](https://developer.android.com/jetpack/compose/components/button)
to receive start and stop events from the user for tracking steps.

Keep in mind sensor [best practices](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview#sensors-practices).
In particular, the step counter sensor should only count steps while the sensor
listener is registered. By associating sensor registration with a foreground
service, the sensor is registered as long as it's needed, and the sensor can
remain registered when the app is not in the foreground.

Use the following snippet to unregister the sensor in the `onPause()` method of
your foreground service:  

    override fun onPause() {
        super.onPause()
        sensorManager.unregisterListener(this)
    }

## Analyze data for events

To access the sensor data, implement the `SensorEventListener` interface. Note
that you should associate sensor registration with your foreground service's
lifecycle, unregistering the sensor when the service is paused or ended. The
following snippet shows how to implement the `SensorEventListener` interface
for `Sensor.TYPE_STEP_COUNTER`:  

    private const val TAG = "STEP_COUNT_LISTENER"

    context(Context)
    class StepCounter {
        private val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        private val sensor: Sensor? = sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER)

        suspend fun steps() = suspendCancellableCoroutine { continuation ->
            Log.d(TAG, "Registering sensor listener... ")

            val listener: SensorEventListener by lazy {
                object : SensorEventListener {
                    override fun onSensorChanged(event: SensorEvent?) {
                        if (event == null) return

                        val stepsSinceLastReboot = event.values[0].toLong()
                        Log.d(TAG, "Steps since last reboot: $stepsSinceLastReboot")

                        if (continuation.isActive) {
                            continuation.resume(stepsSinceLastReboot)
                        }
                    }

                    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {
                          Log.d(TAG, "Accuracy changed to: $accuracy")
                    }
                }
           }

            val supportedAndEnabled = sensorManager.registerListener(listener,
                    sensor, SensorManager.SENSOR_DELAY_UI)
            Log.d(TAG, "Sensor listener registered: $supportedAndEnabled")
        }
    }

## Create a database for the sensor events

Your app might show a screen where the user can view their steps over time.
To provide this capability in your app, use the [Room persistence library](https://developer.android.com/training/data-storage/room).

The following snippet creates a table that contains a set of step count
measurements, along with the time when your app accessed each measurement:  

    @Entity(tableName = "steps")
    data class StepCount(
      @ColumnInfo(name = "steps") val steps: Long,
      @ColumnInfo(name = "created_at") val createdAt: String,
    )

Create a [data access object (DAO)](https://developer.android.com/training/data-storage/room/accessing-data)
to read and write the data:  

    @Dao
    interface StepsDao {
        @Query("SELECT * FROM steps")
        suspend fun getAll(): List<StepCount>

        @Query("SELECT * FROM steps WHERE created_at >= date(:startDateTime) " +
                "AND created_at < date(:startDateTime, '+1 day')")
        suspend fun loadAllStepsFromToday(startDateTime: String): Array<StepCount>

        @Insert
        suspend fun insertAll(vararg steps: StepCount)

        @Delete
        suspend fun delete(steps: StepCount)
    }

To instantiate the DAO, create a `RoomDatabase` object:  

    @Database(entities = [StepCount::class], version = 1)
    abstract class AppDatabase : RoomDatabase() {
        abstract fun stepsDao(): StepsDao
    }

### Store the sensor data into the database

The ViewModel uses the new StepCounter class, so you can store the steps as soon
as you read them:  

    viewModelScope.launch {
        val stepsFromLastBoot = stepCounter.steps()
        repository.storeSteps(stepsFromLastBoot)
    }

The `repository` class would look like this:  

    class Repository(
        private val stepsDao: StepsDao,
    ) {

        suspend fun storeSteps(stepsSinceLastReboot: Long) = withContext(Dispatchers.IO) {
            val stepCount = StepCount(
                steps = stepsSinceLastReboot,
                createdAt = Instant.now().toString()
            )
            Log.d(TAG, "Storing steps: $stepCount")
            stepsDao.insertAll(stepCount)
        }

        suspend fun loadTodaySteps(): Long = withContext(Dispatchers.IO) {
            printTheWholeStepsTable() // DEBUG

            val todayAtMidnight = (LocalDateTime.of(LocalDate.now(), LocalTime.MIDNIGHT).toString())
            val todayDataPoints = stepsDao.loadAllStepsFromToday(startDateTime = todayAtMidnight)
            when {
                todayDataPoints.isEmpty() -> 0
                else -> {
                    val firstDataPointOfTheDay = todayDataPoints.first()
                    val latestDataPointSoFar = todayDataPoints.last()

                    val todaySteps = latestDataPointSoFar.steps - firstDataPointOfTheDay.steps
                    Log.d(TAG, "Today Steps: $todaySteps")
                    todaySteps
                }
            }
        }
    }


## Periodically retrieving sensor data

If you use a foreground service, you don't need to configure `WorkManager`
because, during the time when your app is actively tracking the user's steps,
the updated total step count should appear in your app.

If you want to batch your steps records, however, you can use `WorkManager` to
measure steps at a specific interval, such as once every 15 minutes.
`WorkManager` is the component that performs the background
work for reliable execution. Learn more in the [WorkManager codelab](https://developer.android.com/codelabs/basic-android-kotlin-compose-workmanager#0).

To configure the `Worker` object to retrieve the data, override the `doWork()`
method, as shown in the following code snippet:  

    private const val TAG = " StepCounterWorker"

    @HiltWorker
    class StepCounterWorker @AssistedInject constructor(
        @Assisted appContext: Context,
        @Assisted workerParams: WorkerParameters,
        val repository: Repository,
        val stepCounter: StepCounter
    ) : CoroutineWorker(appContext, workerParams) {

        override suspend fun doWork(): Result {
            Log.d(TAG, "Starting worker...")

            val stepsSinceLastReboot = stepCounter.steps().first()
            if (stepsSinceLastReboot == 0L) return Result.success()

            Log.d(TAG, "Received steps from step sensor: $stepsSinceLastReboot")
            repository.storeSteps(stepsSinceLastReboot)

            Log.d(TAG, "Stopping worker...")
            return Result.success()
        }
    }

To set up `WorkManager` to store the current step count every 15 minutes, do
the following:

1. Extend the `Application` class to implement the `Configuration.Provider` interface.
2. In the `onCreate()` method, enqueue a `PeriodicWorkRequestBuilder`.

This process appears in the following code snippet:  

    @HiltAndroidApp
    @RequiresApi(Build.VERSION_CODES.S)
    internal class PulseApplication : Application(), Configuration.Provider {

        @Inject
        lateinit var workerFactory: HiltWorkerFactory

        override fun onCreate() {
            super.onCreate()

            val myWork = PeriodicWorkRequestBuilder<StepCounterWorker>(
                    15, TimeUnit.MINUTES).build()

            WorkManager.getInstance(this)
                .enqueueUniquePeriodicWork("MyUniqueWorkName",
                        ExistingPeriodicWorkPolicy.UPDATE, myWork)
        }

        override val workManagerConfiguration: Configuration
            get() = Configuration.Builder()
                .setWorkerFactory(workerFactory)
                .setMinimumLoggingLevel(android.util.Log.DEBUG)
                .build()
    }

To initialize the content provider that controls access to your app's step
counter database immediately upon app startup, add the following element to
your app's manifest file:  

    <provider
        android:name="androidx.startup.InitializationProvider"
        android:authorities="${applicationId}.androidx-startup"
        tools:node="remove" />