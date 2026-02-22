---
title: https://developer.android.com/health-and-fitness/health-connect/features/availability
url: https://developer.android.com/health-and-fitness/health-connect/features/availability
source: md.txt
---

When new features are added to Health Connect, users may not always update their
version of Health Connect. The Feature Availability API is a way to check if a
feature in Health Connect is available on your user's device and decide what
action to take.

## Get started

The Feature Availability API shares the same dependency as the Health Connect
SDK. To get started, verify that at least version `1.1.0-alpha08` is in your
`build.gradle` file:

    dependencies {
      implementation("androidx.health.connect:connect-client:1.1.0-alpha08")
    }

## Feature flags

The feature flags available for Health Connect are listed in the following
table. Functionality behind a feature flag won't be available for use if the
user's device doesn't support the feature.

<br />

| Feature flag | Data type | Related guides |
|---|---|---|
| `FEATURE_ACTIVITY_INTENSITY` | Activity intensity |   |
| `FEATURE_EXTENDED_DEVICE_TYPES` | Extended device types | [Metadata requirements](https://developer.android.com/health-and-fitness/guides/health-connect/develop/metadata#device-type) |
| `FEATURE_PERSONAL_HEALTH_RECORD` | Medical records | [Medical Records data format](https://developer.android.com/health-and-fitness/guides/medical-records/data-format) [Write medical data](https://developer.android.com/health-and-fitness/guides/medical-records/write-data) [Read medical data](https://developer.android.com/health-and-fitness/guides/medical-records/read-data) |
| `FEATURE_MINDFULNESS_SESSION` | Mindfulness | [Track mindfulness](https://developer.android.com/health-and-fitness/guides/health-connect/develop/mindfulness) |
| `FEATURE_PLANNED_EXERCISE` | Planned exercise | [Training plans](https://developer.android.com/health-and-fitness/guides/health-connect/develop/training-plans) |
| `FEATURE_READ_HEALTH_DATA_IN_BACKGROUND` | Read data in background | [Background read example](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example) |
| `FEATURE_READ_HEALTH_DATA_HISTORY` | Read historical data | [Read data older than 30 days](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-older-data) |
| `FEATURE_SKIN_TEMPERATURE` | Skin temperature | [Measure skin temperature](https://developer.android.com/health-and-fitness/guides/health-connect/develop/skin-temperature) |
[*Table: Health Connect feature availability flags*]

<br />

## Perform the check

The main function to check for feature availability is `getFeatureStatus()`.
This returns integer constants `FEATURE_STATUS_AVAILABLE` or
`FEATURE_STATUS_UNAVAILABLE`:
To determine whether a user's device supports Read Health Data in Background on Health Connect, check the availability of `FEATURE_READ_HEALTH_DATA_IN_BACKGROUND` on the client:

<br />

    if (healthConnectClient
         .features
         .getFeatureStatus(
           HealthConnectFeatures.FEATURE_READ_HEALTH_DATA_IN_BACKGROUND
         ) == HealthConnectFeatures.FEATURE_STATUS_AVAILABLE) {

      // Feature is available
    } else {
      // Feature isn't available
    }

For a list of all available feature flags, see the [`HealthConnectFeatures`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectFeatures)
reference page.

## Handle lack of feature availability

If a feature isn't available on a user's device, an update may enable it. You
may consider directing the user to update Health Connect if they don't have
the latest supported version on their device. However, users using the APK
(on Android 13 and lower) can't use the system module features that are only
available on devices running Android 14 or higher.

For extended device types, if [`FEATURE_EXTENDED_DEVICE_TYPES`](https://developer.android.com/health-and-fitness/guides/health-connect/develop/metadata#device-type) isn't
available on the user's device, those values are treated as
`Device.TYPE_UNKNOWN`. Provide a sensible fallback in your write and UI logic.