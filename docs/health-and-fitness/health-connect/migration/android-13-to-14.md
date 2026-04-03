---
title: https://developer.android.com/health-and-fitness/health-connect/migration/android-13-to-14
url: https://developer.android.com/health-and-fitness/health-connect/migration/android-13-to-14
source: md.txt
---

Health Connect will be packaged with Android 14 as a common data storage layer
for consumer health and fitness data, protected by granular permissions and
accessible as an Android system app (referred to throughout this document as the
'framework' module).

Developers should consider the Health Connect APK (Android 13) as a backwards
compatibility layer for the framework model. The framework model will retain
100% feature parity with its APK predecessor.

During the transition from Android 13 to 14, it's vitally important that the
user experience remains as smooth and intuitive as possible.

This document outlines the migration plan, provides some example migration
scenarios, and lists changes to the Jetpack SDK, which facilitates access to the
Health Connect API.

## Migration plan

1. Once Android 14 is released, Google will switch to providing Health Connect as an Android system app.
2. Data will then be backfilled from the APK once feature parity is achieved.
3. All entry points will target the system app UI.
4. Data migration will commence. Whilst the migration is progressing, the module APIs will be suspended with a 'Migration in Process' status. This will also be visible within the Health Connect UI.
5. Once migration is complete, the APK can be uninstalled.

| **Note:** Data migration is not expected to exceed 2 hours.

### Example migration scenarios

Here are some example scenarios that explain the migration process for both
`interval` and `series` data types:

#### Example 1 - Running (interval data)

A user has collected 10 years of running records for 1 hour every day. This
equates to:

- Exercise Session Records: 365 \* 10 \* 1
- Steps: 365 \* 10 \* 1
- Calories: 365 \* 10 \* 1
- Total = 365 \* 10 \* 3 (365 \* 30) = 10,950

Given that 1 chunk equates to 3,000 records, the data totals around 4 chunks.

Our internal testing has confirmed that a typical chunk takes approximately a
second to insert, so the data in the example would be migrated in approximately
4 seconds.

#### Example 2 - Heart rate (series data)

A user has collected 5 years of heart rate data (with a record created every
minute) totalling 2,628,000 records.

At 3,000 records per chunk, the data is distributed across 876 chunks. Given
that 1 chunk takes approximately a second to insert, the data would be migrated
in under 15 minutes.

## Proposed migration flow

We've decided to opt for an **instant migration**. In practical terms, this
means that the APK will become inactive as soon as the device is upgraded to
Android 14, with minimal user intervention.

Here's the high-level migration flow:

1. The user upgrades their device to Android 14.
2. Jetpack 14 routes the user to the module APIs, and blocks them whilst the migration is in progress.
3. The migration process starts when the module version is feature compatible with the APK - in other words, the module version contains the same feature set, or more. Once the migration process has commenced, the APK migrates permissions and data.
   1. If both versions are not feature compatible, the module version will need to be upgraded. Once the upgrade is complete, the migration process will commence.
4. Once the migration has completed, the state is changed to 'Migration Complete', and the module APIs are unblocked.
5. The APK can now be uninstalled.

### Migration UI elements

The following screens are displayed by the framework module for user education
purposes, both before and during migration:

**Figure 1.** If the Health Connect APK is not 'migration aware', a prompt
is displayed instructing the user to update the APK. If the user declines the
update, the module continues to function and starts accumulating permissions
and data.
![Figure of Phone update required](https://developer.android.com/static/health-and-fitness/health-connect/images/phone_update_needed.png) **Figure 1**: Prompt to update the Health Connect APK.

**Figure 2.** If the framework module requires an update for it to become
feature compatible, a prompt is displayed asking the user to perform the update
and reboot their device. If the user declines the update, the module continues
to function and starts accumulating permissions and data.
![Figure of APK update needed](https://developer.android.com/static/health-and-fitness/health-connect/images/apk_update_needed.png) **Figure 2**: Prompt to update the framework module.

**Figure 3.** A spinner is displayed during the migration process, with text to
explain that data is syncing.
![Figure of Data Syncing](https://developer.android.com/static/health-and-fitness/health-connect/images/migration_in_process.png) **Figure 3**: Data migration in progress.

## Deduped data

If the framework module has started to acquire data and permissions
*before* any migration or cloud-based restore has taken place, the following
rules apply.

### Permissions

If permissions are present within the framework module, any duplicate
permissions acquired from the APK are ignored during the migration process.

### Data

During migration, duplicate data originating from the APK is ignored. More
recent data from the module is given preference.

The data is deduped on `clientRecordId` if the record ID is provided by the
client. If it isn't, time intervals (`startTime` and `endTime` for internal
records, and `time` for instant records) are treated as key, along with the data
type and package name of the app.

## Changes in Jetpack SDK

The Jetpack SDK serves as the common integration point for both the Health
Connect APK, and the Health Connect framework APIs.

OEMs can start integrating with Jetpack 13 so that when Jetpack 14 becomes
available, you are able to appropriate the new library and compile it within
Android 14.

We'll be releasing a new version of the SDK that supports the transition to
Android 14. You will need to make some changes to your existing integration to
ensure a smooth transition.

### Permission declaration

In Android 13, you declare permissions using a custom permissions format, in a
resource file that is linked to the manifest:

    #AndroidManifest.xml

    <activity>
        android:name=".RationaleActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE"/>
        </intent-filter>
        <meta-data
            android:name="health_permissions"
            android:resource="@array/health_permissions"/>
    </activity>

    <queries>
        <package android:name="com.google.android.apps.healthdata" />
    </queries>

    #health_permissions.xml

    <resources>
      <array name="health_permissions">
        <item>androidx.health.permission.SleepSession.READ</item>
        <item>androidx.health.permission.SleepStage.READ</item>
        <item>androidx.health.permission.Weight.READ</item>
        <item>androidx.health.permission.Weight.WRITE</item>
      </array>
    </resources>

To support Android 14, developers need to move to the standard permissions
format:

    #AndroidManifest.xml

    <uses-permission android:name="android.permission.health.READ_SLEEP" />
    <uses-permission android:name="android.permission.health.READ_WEIGHT" />
    <uses-permission android:name="android.permission.health.WRITE_WEIGHT" />

    <activity>
        android:name=".RationaleActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE" />
        </intent-filter>
    </activity>

    <queries>
        <package android:name="com.google.android.apps.healthdata"/>
    </queries>

### Open Health Connect

Most third-party apps feature a button that opens the Health Connect app, such
as the 'Manage Access' button in Fitbit.

In Android 13, you either open the Health Connect app using the package name, or
using the `androidx.health.ACTION_HEALTH_CONNECT_SETTINGS` action.

In Android 14, you need to use an intent action, specified in the Jetpack SDK,
which has different values based on the Android version it's acting on:

`@get:JvmName("getHealthConnectSettingsAction")` `@JvmStatic val
ACTION_HEALTH_CONNECT_SETTINGS`

### Getting the Health Connect client

We've created [a single API](https://developer.android.com/jetpack/androidx/releases/health-connect#1.0.0-alpha11) called `sdkStatus`, available in Jetpack 11, to
replace two other deprecated APIs - `IsSdkSupported()` and
`isProviderAvailable()`.

### Session record API changes

Four `ExerciseSession` subtypes have been deleted as part of the alpha10
release:

- `ExerciseEvent`
- `ExerciseLaps`
- `ExerciseRepetitions`
- `SwimmingStrokes`

| **Important:** If any data exists for these types, it will be deleted during a cleanup. You should stop using these data types.

As with `ExerciseSessionRecord`, `SleepStage` will become a subtype of
`SleepSession`.

Both the `ExerciseSessionRecord` subtypes and `SleepSession` changes will be
released as part of the April SDK update.

### Exercise session type update

The following exercise session types will no longer be supported, and instead
added as segment types at a later date:

- `EXERCISE_TYPE_BACK_EXTENSION`
- `EXERCISE_TYPE_BARBELL_SHOULDER_PRESS`
- `EXERCISE_TYPE_BENCH_PRESS`
- `EXERCISE_TYPE_BENCH_SIT_UP`
- `EXERCISE_TYPE_BURPEE`
- `EXERCISE_TYPE_CRUNCH`
- `EXERCISE_TYPE_DEADLIFT`
- `EXERCISE_TYPE_DUMBBELL_CURL_LEFT_ARM`
- `EXERCISE_TYPE_DUMBBELL_CURL_RIGHT_ARM`
- `EXERCISE_TYPE_DUMBBELL_FRONT_RAISE`
- `EXERCISE_TYPE_DUMBBELL_LATERAL_RAISE`
- `EXERCISE_TYPE_DUMBBELL_TRICEPS_EXTENSION_LEFT_ARM`
- `EXERCISE_TYPE_DUMBBELL_TRICEPS_EXTENSION_RIGHT_ARM`
- `EXERCISE_TYPE_DUMBBELL_TRICEPS_EXTENSION_TWO_ARM`
- `EXERCISE_TYPE_FORWARD_TWIST`
- `EXERCISE_TYPE_JUMPING_JACK`
- `EXERCISE_TYPE_JUMP_ROPE`
- `EXERCISE_TYPE_LAT_PULL_DOWN`
- `EXERCISE_TYPE_LUNGE`
- `EXERCISE_TYPE_PLANK`
- `EXERCISE_TYPE_SQUAT`
- `EXERCISE_TYPE_UPPER_TWIST`

Replacement types:

- `EXERCISE_TYPE_HIGH_INTENSITY_INTERVAL_TRAINING`
- `EXERCISE_TYPE_STRENGTH_TRAINING`
- `EXERCISE_TYPE_CALISTHENICS`

### Changelog handling

Changelogs won't be migrated as part of the switch from APK to Android 14.

After migration is complete, you will start to receive `TOKEN_EXPIRED` or
`TOKEN_INVALID` exceptions. These should be handled in the following ways (in
order of preference):

**1. Read and dedupe all data since the 'last read' timestamp, or for the last
30 days**

Store a timestamp of when an app last read data from Health Connect. On token
expiry, data should be re-read either from this value, or the previous 30 days
(whichever equates to the minimum), and dedupe it against previously read data
using the UUID.

**2. Read data since the 'last read' timestamp**

Establish a timestamp that indicates when data was last read from Health Connect
, and upon token expiry, read all data *after* that value.

**3. Delete and re-read data for the last 30 days**

Delete all data read from Health Connect from the previous 30 days, and read all
of that data again (e.g. as is done when apps first integrate with Health
Connect).

**4. Do nothing (i.e. re-read data for the last 30 days and don't dedupe)**

This should be used as a last resort, with an associated risk of displaying
duplicate data. Developers should instead explore options 1-3, given that UUIDs
should already be in place.

### Testing Android 14 APIs with Jetpack SDK

The Android 14 Jetpack SDK is set to be released on June 7 2023, along with the
Beta 3 release of Android 14. You will need to start compiling your app against
Android 14 to be able to use the Android 14 Jetpack SDK.

If you want to test your solution against the Android Developer Preview builds
ahead of June 7th, contact your Google POC for assistance.

If you want to test your solution against the Beta 3 release, you should make
the following changes in your APK:

1. Set `compileSDKPreview = UpsideDownCake`.
2. Update the manifest to include an intent for Android 14:

    # AndroidManifest.xml

    <uses-permission android:name="android.permission.health.READ_SLEEP"/>
    <uses-permission android:name="android.permission.health.READ_WEIGHT"/>
    <uses-permission android:name="android.permission.health.WRITE_WEIGHT"/>

    <activity>
        android:name=".RationaleActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.health.ACTION_SHOW_PERMISSIONS_RATIONALE"/>
        </intent-filter>
    </activity>

    <activity-alias>
          android:name="AndroidURationaleActivity"
          android:exported="true"
          android:targetActivity=".RationaleActivity"
          android:permission="android.permission.START_VIEW_PERMISSION_USAGE">
          <intent-filter>
            <action android:name="android.intent.action.VIEW_PERMISSION_USAGE" />
            <category android:name="android.intent.category.HEALTH_PERMISSIONS" />
          </intent-filter>
    </activity-alias>

    <queries>
        <package android:name="com.google.android.apps.healthdata" />
    </queries>

## OEM customization

In Android 14, Health Connect privacy \& data management controls are located
within System Settings.

To make data management and permissions screens look and feel like part of the
device, Health Connect offers OEM theming through the use of custom overlays.

For documentation on OEM styling, consult [Health Connect Google Mobile Services
documentation](https://docs.partner.android.com/gms/building/apps/productivity/android-14-integration). You may be required to log into Google
Developers to view the page.