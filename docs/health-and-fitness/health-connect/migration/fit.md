---
title: https://developer.android.com/health-and-fitness/health-connect/migration/fit
url: https://developer.android.com/health-and-fitness/health-connect/migration/fit
source: md.txt
---

The Google Fit APIs are deprecated and scheduled for end of service in late
2026. Google offers several health and wellness products and services to help
your users continue to achieve their goals after deprecation.
> **Caution:** The Google Fit API (including the REST API) will only be
> supported until the end of 2026. We recommend migrating to the Google Health API
> for cloud-based integrations or Health Connect for step tracking and
> mobile-first apps.

The following guidelines show you which service to migrate to based on how
you're using Google Fit APIs.

## Recommended Migration Paths

Your choice of API should be based on your application type and specific data
needs.

### By Application Type

| Application Type | Recommended Path | Primary Reason |
|---|---|---|
| Step Tracking App | [Health Connect](https://developer.android.com/health-and-fitness/health-connect) | Mobile-centric reading of aggregated steps data from various sources. |
| Fitness Trackers Companion App | [Google Health API](https://developers.google.com/health) | Web-centric platform requiring OAuth for user integration. |
| Health and Fitness Platform | The [Google Health API](https://developers.google.com/health) \& [Health Connect](https://developer.android.com/health-and-fitness/health-connect) | Use the Google Health API for Fitbit/Google device data and Health Connect for on-device aggregated data. |

### By current integration

| Current Integration | Recommended Path | Availability |
|---|---|---|
| Google Fit (Android \& REST API) | Google Health API | Available |
| Reading mobile steps (with Google Fit Recording API) | Health Connect | Available |
| Fit API on Wear OS | Health Services | Available |
| Fitbit Web API | Google Health API | Available |
| Recording API on Mobile | Health Connect | Available |
| Health Connect | Keep existing integration or add the Google Health API | Available |

## Technical comparisons

The following sections provide a technical comparison between the Google Fit
APIs, the Google Health API, and Health Connect to help you choose the right
migration path.

### Fit API versus Google Health API

Use this path if your app is a web-based platform or requires server-to-server
(S2S) interactions.

| Feature | Fit API (Android/REST) | Google Health API |
|---|---|---|
| Project Setup | [Google Cloud Console](https://console.cloud.google.com/) | [Create Google Cloud project](https://console.cloud.google.com/) |
| OAuth Configuration | Android or Web application type | Web application type |
| Data Architecture | `com.google` prefixed types | Unified Google Health API data types |
| App Registration | Create Google Cloud project | [Create Google Cloud project and enable the Google Health API](https://developers.google.com/health/setup) |

### Fit API versus Health Connect

Use this path for mobile-first Android applications reading local device
metrics.

| Feature | Fit API for Android | Health Connect |
|---|---|---|
| Registration | Google Cloud Console | Play Store project and health apps declaration |
| Authentication | OAuth 2.0 required | No OAuth required (on-device permissions) |
| Data storage | Cloud-centric | Device-centric (on-device) |
| Audience | Legacy Android developers | Modern Android mobile developers |
| Permissions | OAuth scopes | Android manifest permissions |

## Fit API integrations

The following sections provide guidance on migrating from each of the Google
Fit APIs. If your integration also includes UI elements that connect to the
Google Fit app, see [Fit app integrations guidelines](https://developer.android.com/health-and-fitness/health-connect/migration/fit#fit-app-integrations)
for additional guidance.

### Apps using the Fit Recording API for recording steps

The [Fit Recording API](https://developers.google.com/fit/android/record) lets your app request automated
storage of sensor data in a battery-efficient manner by creating subscriptions.
Each subscription connects an Android app to a particular fitness data type or
data source, and the `Step` data type is commonly used for recording steps.

Follow these steps to migrate from the Fit Recording API:

|---|---|
| **Phone** | **Wear** |
| 1. To show a total step count, [add Health Connect to your app](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started). The total includes [mobile steps](https://developer.android.com/health-and-fitness/guides/health-connect/develop/steps#read-mobile-steps) (Android 14 or higher) and steps from other apps and devices. 2. To continue showing local steps data in your app, implement writing data using [Health Connect's write API](https://developer.android.com/health-and-fitness/guides/health-connect/develop/write-data). | Use Health Services: - PassiveMonitoringClient - ExerciseClient See the [Health Services documentation](https://developer.android.com/training/wearables/health-services) for more on the differences between the two. |
[*Table 1: Migration steps from Fit Recording API*]

### Apps using the History API to read or write data to the fitness store

The [History API](https://developers.google.com/fit/android/history) lets your app perform bulk operations on the
fitness store. These operations include reading, inserting, updating, and
deleting historical health and wellness data.

Follow these steps to migrate from the History API:

|---|---|
| **Phone** | **Wear** |
| [Transition to the Google Health API](https://developers.google.com/health). | Not applicable. Use Health Connect from your mobile app and not the wearable. |
[*Table 2: Migration steps from Fit History API*]

### Apps using the Sensor API to display real-time fitness data

The [Sensor API](https://developers.google.com/fit/android/sensors) lets you read raw sensor data in your app in real
time. The Sensor API does the following:

- Lists data sources that are available on the device and on companion devices.
- Registers listeners to receive raw sensor data.
- Unregisters listeners so that they no longer receive raw sensor data.

Follow these steps to migrate from the Sensor API:

|---|---|
| **Phone** | **Wear** |
| Use [Sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview), [Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider) | Use [Health Services](https://developer.android.com/health-and-fitness/guides/health-services) on Wear OS: - `PassiveMonitoringClient` - `MeasureClient` - `ExerciseClient` Or use `SensorManager`, `FusedLocationProvider` |
[*Table 3: Migration steps from Fit Sensor API*]

### Apps using the Session API to provide activity summaries

Sessions represent a time interval during which users perform a fitness
activity.

The [Session API](https://developers.google.com/fit/android/using-sessions) lets your app create sessions in the fitness
store.

Follow these steps to migrate from the Session API:

|---|---|
| **Phone** | **Wear** |
| Start/stop: Not applicable. The application should track the state of ongoing sessions internally. Read/write: [Transition to the Google Health API](https://developers.google.com/health). | Start/stop: Use Health Services (ExerciseClient) Read/write: Use Health Connect with your mobile app. *For specific workflows, we advise the following:* - Inserting a session: Developers should use Health Connect with their mobile app and either insert an `ExerciseSessionRecord` or a `SleepSessionRecord` accordingly. |
[*Table 4: Migration steps from Fit Session API*]

### Apps using the Goals API

Goals are targets in the Google Fit app that users can set for their metrics
like steps and heart points. The Fit platform records their goals and tracks
their daily activity against these using the [Goals API](https://developers.google.com/fit/android/using-goals).

|---|---|
| **Phone** | **Wear** |
| No replacement API available. | No replacement API available. |
[*Table 5: Migration guidance for Fit Goals API*]

### Apps using the BLE API

Your app can find available Bluetooth Low Energy (BLE) devices and insert
sensor data into the Google Fit platform using the [BLE API](https://developers.google.com/fit/android/ble-sensors).

**Follow these steps to migrate from BLE API:**

|---|---|
| **Phone** | **Wear** |
| Use Android Bluetooth APIs directly. | Use Android Bluetooth APIs directly. |
[*Table 6: Migration steps from Fit BLE API*]

### Deprecated features

The following features don't have a direct API replacement. Use the recommended
Android standard APIs:

- **Sensor API**: Use the Android Sensors framework or the Fused Location Provider API for real-time raw data.
- **Goals API**: No replacement API available. Manage goal tracking and daily activity targets within your application logic.
- **Bluetooth Low Energy (BLE) API**: Use the Android Bluetooth APIs directly to communicate with hardware.

## Fit app integrations

If your app connects to Google Fit for data sharing, follow guidance on
migrating existing and new users to Health Connect or the Google Health API in
these sections:

### Existing users of your app

If your app UI includes a way for users to connect to Google Fit (or if your
app is included on the list of [Works with Google Fit apps](https://play.google.com/store/apps/collection/promotion_3000e6f_googlefit_all)), you can
continue to maintain your Fit app integration for current users.

We will keep this section updated with information on when to deprecate your
Fit app integration, and what your best options are for maintaining your user
experience. In the meantime, you can [connect with us](https://developer.android.com/health-and-fitness#connect-with-us).

|---|---|
| check**Do this** | close**Don't do this** |
| [Offer Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect/design/ui-guidelines#promote-health-connect) or the [Google Health API](https://developers.google.com/health) as a new option in your app. Focus on user benefits like richer data and insights, privacy, and security. ![Sync with Health Connect](https://developer.android.com/static/health-and-fitness/health-connect/images/sync-with-hc.png) | Ask users to disconnect from Google Fit. ![Disconnect from Health Connect](https://developer.android.com/static/health-and-fitness/health-connect/images/disconnect-hc.png) |
[*Table 7: Recommendations for existing users with Fit app integrations*]

### New users of your app

To offer a similar experience to new users of your app, we recommend
building an integration with [Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started) or the
[Google Health API](https://developers.google.com/health).

Health Connect offers access to new data sources and types to provide a
richer experience for users, with data stored securely on-device. The Google
Health API provides a web-centric platform for Fitbit and Google device data.

|---|---|
| check**Do this** | close**Don't do this** |
| Include Health Connect or the Google Health API in your app's [setup flow](https://developer.android.com/health-and-fitness/guides/health-connect/design/ui-guidelines#app-setup-flow). | Offer Fit as an app that users can connect to once Health Connect is available. |
[*Table 8: Recommendations for new users with Fit app integrations*]