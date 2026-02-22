---
title: https://developer.android.com/health-and-fitness/health-connect/get-started
url: https://developer.android.com/health-and-fitness/health-connect/get-started
source: md.txt
---

<br />

> This guide is compatible with Health Connect version [1.1.0-alpha12](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-alpha12).

This guide shows you how you can begin using Health Connect on your app.

## Step 1: Prepare the Health Connect app

The Health Connect app is responsible for handling all the requests that your
application sends through the Health Connect SDK. These requests include storing
data and managing its read and write access.

Access to Health Connect depends on the Android version installed on the phone.
The following sections outline how to handle several recent versions of Android.

### Android 14

Starting Android 14 (API Level 34), Health Connect is part of the
Android Framework. This version of Health Connect is a *framework module*. With
that, there's no setup necessary.

### Android 13 and lower

On Android 13 (API Level 33) and lower versions, Health Connect is not part of
the Android Framework. With that, you need to install the
[Health Connect app](https://play.google.com/store/apps/details?id=com.google.android.apps.healthdata) from the Google Play Store.

If you have integrated your app with Health Connect on Android 13 and lower, and
would like to migrate on Android 14, refer to
[Migrate from Android 13 to 14](https://developer.android.com/health-and-fitness/guides/health-connect/migrate/migrate-from-android-13-to-14).

### Open the Health Connect app

Health Connect no longer appears on the Home screen by default. You can open
Health Connect through **Settings**, though the path varies depending on the
Android version:

- **On Android 14 and higher:** Go to **Settings \> Security and Privacy \> Privacy Controls \> Health Connect** , or search for **Health Connect** in Settings.
- **On Android 13 and lower:** Go to **Settings \> Apps \> Health Connect** , or add Health Connect to your **Quick Settings** menu.

## Step 2: Add the Health Connect SDK to your app

The Health Connect SDK is responsible for using the Health Connect API to
send requests in performing operations against the datastore in the Health
Connect app.

Add the Health Connect SDK dependency in your module-level `build.gradle` file:  

    dependencies {
      ...
      implementation "androidx.health.connect:connect-client:1.2.0-alpha02"
      ...
    }

Refer to the [Health Connect releases](https://developer.android.com/jetpack/androidx/releases/health-connect) for the latest version.
| **Note:** The Health Connect SDK supports Android 8 (API level 26) or higher, while the Health Connect app is only compatible with Android 9 (API level 28) or higher. This means that third-party apps can support users with Android 8, but only users with Android 9 or higher can use Health Connect.

## Step 3: Configure your app

The following sections explain how to configure your app to integrate to
Health Connect.

### Check feature availability

When new features are added to Health Connect, users may not always update their
version of Health Connect. The Feature Availability API is a way to check if a
feature in Health Connect is available on your user's device and decide what
action to take.

The main function to check for feature availability is
[`getFeatureStatus()`](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability#perform-check). This returns integer constants
`FEATURE_STATUS_AVAILABLE` or `FEATURE_STATUS_UNAVAILABLE`:  

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_READ_HEALTH_DATA_IN_BACKGROUND
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
      ...
    } else {
      // Feature is not available
      ...
    }

| **Note:** If a feature isn't available, ask the user to update Health Connect. Features tied to the system module remain unavailable on Android 13 and lower, even with the APK.

### Declare permissions

Access to health and fitness data is sensitive. Health Connect implements a
layer of security to read and write operations, maintaining user trust.

In your app, declare read and write permissions in the `AndroidManifest.xml`
file based on those required data types, which should match the ones you
declared access to in the Play Console.

Health Connect uses the standard Android permission declaration format.
Assign permissions with the `<uses-permission>` tags. Nest them within the
`<manifest>` tags.  

    <manifest>
      <uses-permission android:name="android.permission.health.READ_HEART_RATE"/>
      <uses-permission android:name="android.permission.health.WRITE_HEART_RATE"/>
      <uses-permission android:name="android.permission.health.READ_STEPS"/>
      <uses-permission android:name="android.permission.health.WRITE_STEPS"/>

      <application>
      ...
      </application>
    </manifest>

For the full list of permissions and their corresponding data types, see
[List of data types](https://developer.android.com/guide/health-and-fitness/health-connect/plan/data-types#alpha10).

### Show your app's privacy policy dialog

Your Android manifest needs to have an Activity that displays your app's
privacy policy, which is your app's rationale of the requested permissions,
describing how the user's data is used and handled.

Declare this activity to handle the `ACTION_SHOW_PERMISSIONS_RATIONALE`
intent where it is sent to the app when the user clicks on the
**privacy policy** link in the Health Connect permissions screen.  

    ...
    <application>
      ...
      <!-- For supported versions through Android 13, create an activity to show the rationale
           of Health Connect permissions once users click the privacy policy link. -->
      <activity
          android:name=".PermissionsRationaleActivity"
          android:exported="true">
        <intent-filter>
          <action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE" />
        </intent-filter>
      </activity>

      <!-- For versions starting Android 14, create an activity alias to show the rationale
           of Health Connect permissions once users click the privacy policy link. -->
      <activity-alias
          android:name="ViewPermissionUsageActivity"
          android:exported="true"
          android:targetActivity=".PermissionsRationaleActivity"
          android:permission="android.permission.START_VIEW_PERMISSION_USAGE">
        <intent-filter>
          <action android:name="android.intent.action.VIEW_PERMISSION_USAGE" />
          <category android:name="android.intent.category.HEALTH_PERMISSIONS" />
        </intent-filter>
      </activity-alias>
      ...
    </application>
    ...

| **Note:** The activity must display the same privacy policy you provide for your app in the [Google Play Console](https://support.google.com/googleplay/android-developer/answer/9859455).

### Get a Health Connect client

[`HealthConnectClient`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient) is an entry point to the Health Connect API.
It allows the app to use the datastore in the Health Connect app. It
automatically manages its connection to the underlying storage layer and handles
all IPC and serialization of outgoing requests and incoming responses.

To get a client instance, declare the Health Connect package name in your
Android manifest first.  

    <application> ... </application>
    ...
    <!-- Check if Health Connect is installed -->
    <queries>
        <package android:name="com.google.android.apps.healthdata" />
    </queries>

Then in your Activity, check if Health Connect is installed
using [`getSdkStatus`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#getSdkStatus(android.content.Context,kotlin.String)). If it is, obtain a
`HealthConnectClient` instance.  

    val availabilityStatus = HealthConnectClient.getSdkStatus(context, providerPackageName)
    if (availabilityStatus == HealthConnectClient.SDK_UNAVAILABLE) {
      return // early return as there is no viable integration
    }
    if (availabilityStatus == HealthConnectClient.SDK_UNAVAILABLE_PROVIDER_UPDATE_REQUIRED) {
      // Optionally redirect to package installer to find a provider, for example:
      val uriString = "market://details?id=$providerPackageName&url=healthconnect%3A%2F%2Fonboarding"
      context.startActivity(
        Intent(Intent.ACTION_VIEW).apply {
          setPackage("com.android.vending")
          data = Uri.parse(uriString)
          putExtra("overlay", true)
          putExtra("callerId", context.packageName)
        }
      )
      return
    }
    val healthConnectClient = HealthConnectClient.getOrCreate(context)
    // Issue operations with healthConnectClient

## Step 4: Request permissions from the user

After creating a client instance, your app needs to request permissions from
the user. Users must be allowed to grant or deny permissions at any time.

To do so, create a set of permissions for the required data types.
Make sure that the permissions in the set are declared in your Android
manifest first.  

    // Create a set of permissions for required data types
    val PERMISSIONS =
        setOf(
      HealthPermission.getReadPermission(HeartRateRecord::class),
      HealthPermission.getWritePermission(HeartRateRecord::class),
      HealthPermission.getReadPermission(StepsRecord::class),
      HealthPermission.getWritePermission(StepsRecord::class)
    )

Use [`getGrantedPermissions`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#getGrantedPermissions()) to see if your app already has the
required permissions granted. If not, use
[`createRequestPermissionResultContract`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController#createRequestPermissionResultContract(kotlin.String)) to request
those permissions. This displays the Health Connect permissions screen.  

    // Create the permissions launcher
    val requestPermissionActivityContract = PermissionController.createRequestPermissionResultContract()

    val requestPermissions = registerForActivityResult(requestPermissionActivityContract) { granted ->
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions successfully granted
      } else {
        // Lack of required permissions
      }
    }

    suspend fun checkPermissionsAndRun(healthConnectClient: HealthConnectClient) {
      val granted = healthConnectClient.permissionController.getGrantedPermissions()
      if (granted.containsAll(PERMISSIONS)) {
        // Permissions already granted; proceed with inserting or reading data
      } else {
        requestPermissions.launch(PERMISSIONS)
      }
    }

Because users can grant or revoke permissions at any time, your app needs to
periodically check for granted permissions and handle scenarios where
permission is lost.

### Onboard users

Many apps have a custom onboarding flow such as feature education or asking user
consent. To enable Health Connect to launch your onboarding flow, add the
following to your manifest:  

    <!-- Required to support pre-Android 14 devices with APK Health Connect -->
    <activity
      android:name=".OnboardingActivity"
      android:exported="true"
      android:permission="com.google.android.apps.healthdata.permission.START_ONBOARDING">
      <intent-filter>
        <action android:name="androidx.health.ACTION_SHOW_ONBOARDING"/>
      </intent-filter>
    </activity>
    <!-- Required to support Android 14+ devices with platform Health Connect -->
    <activity-alias
      android:name="UAndAboveOnboardingActivity"
      android:exported="true"
      android:targetActivity=".OnboardingActivity"
      android:permission="android.permission.health.START_ONBOARDING">
      <intent-filter>
        <action android:name="android.health.connect.action.SHOW_ONBOARDING" />
      </intent-filter>
    </activity-alias>

Users may initiate the connection to your app directly from the Health
Connect app, rather than from within your app. If your app requires any
additional interaction beyond being granted permission to read or write data,
provide an onboarding activity.

Note that the onboarding activity may be launched more than once, for example if
the user later revokes permissions to your app and then reconnects it.

## Step 5: Perform operations

Now that everything is set, perform read and write operations in your app.

### Write data

Structure your data into a record. Check out the list of
[data types](https://developer.android.com/guide/health-and-fitness/health-connect/plan/data-types#alpha10) available in Health Connect.  

    val stepsRecord = StepsRecord(
        count = 120,
        startTime = START_TIME,
        endTime = END_TIME,
        startZoneOffset = START_ZONE_OFFSET,
        endZoneOffset = END_ZONE_OFFSET,
    )

Then write your record using [`insertRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#insertRecords(kotlin.collections.List)).  

    suspend fun insertSteps(healthConnectClient: HealthConnectClient) {
        val endTime = Instant.now()
        val startTime = endTime.minus(Duration.ofMinutes(15))
        try {
            val stepsRecord = StepsRecord(
                count = 120,
                startTime = startTime,
                endTime = endTime,
                startZoneOffset = ZoneOffset.UTC,
                endZoneOffset = ZoneOffset.UTC,
                metadata = Metadata.autoRecorded(
                    device = Device(type = Device.TYPE_WATCH)
                ),
            )
            healthConnectClient.insertRecords(listOf(stepsRecord))
        } catch (e: Exception) {
            // Run error handling here
        }
    }

### Read data

You can read your data individually using [`readRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#readRecords(androidx.health.connect.client.request.ReadRecordsRequest)).
| **Note:** For cumulative types like `StepsRecord`, use `aggregate()` instead of `readRecords()` to avoid double counting from multiple sources and improve accuracy. See [Read aggregated
data](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary) for more information.  

    suspend fun readHeartRateByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.readRecords(
                ReadRecordsRequest(
                    HeartRateRecord::class,
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            for (record in response.records) {
                // Process each record
            }
        } catch (e: Exception) {
            // Run error handling here
        }
    }

You can also read your data in an aggregated manner using
[`aggregate`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/aggregate/package-summary).  

    suspend fun aggregateSteps(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            val response = healthConnectClient.aggregate(
                AggregateRequest(
                    metrics = setOf(StepsRecord.COUNT_TOTAL),
                    timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
                )
            )
            // The result may be null if no data is available in the time range
            val stepCount = response[StepsRecord.COUNT_TOTAL]
        } catch (e: Exception) {
            // Run error handling here
        }
    }

| **Important:** Health Connect can read data for up to 30 days prior to the time permission was granted. If you would like your app to read records beyond 30 days, use the `PERMISSION_READ_HEALTH_DATA_HISTORY` permission. See [Read restrictions](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-restriction) for more information.

## Video tutorials

Watch these videos that explain more about the Health Connect features, as well
as best practice guidelines for achieving a smooth integration:

- [Managing permissions in Health Connect](https://www.youtube.com/watch?v=C2I4OymO3S4)
- [Reading and writing in Health Connect](https://www.youtube.com/watch?v=NAx7Gv_Hk7E)
- [Tips for a great Health Connect integration](https://www.youtube.com/watch?v=yGAlBTTX9R4)

## Resources

Check out the following resources that help with
development later on.

- **Health Connect SDK (available on Jetpack):** Include this [SDK](https://developer.android.com/jetpack/androidx/releases/health-connect) in your application to use the Health Connect API.
- **API reference:** Take a look at the [Jetpack reference](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/package-summary) for the Health Connect API.
- **Declare use of data types:** In the Play Console, [declare access to the Health Connect data types](https://developer.android.com/health-and-fitness/guides/health-connect/publish/declare-access) that your app reads from and writes to.
- **Optional GitHub code sample and codelab:** See the GitHub code sample [repository](https://github.com/android/health-samples/tree/main/health-connect/HealthConnectSample) and the [codelab](https://developer.android.com/codelabs/health-connect) exercise to help you get started.

| **Note:** If you are applying for another request in case your app requires new data types, you need to include both new and existing data types, and exclude any data types you no longer need. If you only need to remove access to certain data types, include all of your existing data types but exclude the data types you no longer need.

## Next steps

Check out **Common workflows** to learn how to perform operations in
Health Connect such as:

- [Write data](https://developer.android.com/guide/health-and-fitness/health-connect/develop/write-data)
- [Read raw data](https://developer.android.com/guide/health-and-fitness/health-connect/develop/read-data)
- [Read aggregated data](https://developer.android.com/guide/health-and-fitness/health-connect/develop/aggregate-data)