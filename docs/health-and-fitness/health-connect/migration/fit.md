---
title: Fit migration guide  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-connect/migration/fit
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Health Connect Guides](https://developer.android.com/health-and-fitness/health-connect)

# Fit migration guide Stay organized with collections Save and categorize content based on your preferences.




The Google Fit APIs will be deprecated in 2026. Google offers several health
and wellness products and services to help your users continue to achieve their
goals after deprecation.

The following guidelines show you which service to migrate to based on how
you're using Google Fit Android APIs.

We will keep this page updated with the latest information and guidance.

## Fit API integrations

If you use one or more Fit APIs but **don't** include a direct link to the Fit
app in your UI, these guidelines are for you. If you surface Fit in your UI,
reference the
[Fit app integrations guidelines](/health-and-fitness/guides/health-connect/migrate/migration-guide#fit_app_integrations).

### Apps using the Fit Recording API for recording steps

The [Fit Recording API](https://developers.google.com/fit/android/record) lets your app request automated
storage of sensor data in a battery-efficient manner by creating subscriptions.
Each subscription connects an Android app to a particular fitness data type or
data source, and the `Step` data type is commonly used for recording steps.

Follow these steps to migrate from the Fit Recording API:

*Table 1: Migration steps from Fit Recording API*

| **Phone** | **Wear** |
| 1. To show a total step count,    [add Health Connect to your app](/health-and-fitness/guides/health-connect/develop/get-started). The total includes    [mobile steps](/health-and-fitness/guides/health-connect/develop/steps#read-mobile-steps) (Android 14 or higher) and steps from other apps and    devices. 2. To continue showing local steps data in your app, implement data capture    using the    [Recording API on mobile](/health-and-fitness/guides/recording-api). | Use Health Services:   * PassiveMonitoringClient * ExerciseClient   See the [Health Services documentation](/training/wearables/health-services) for more on the differences between the two. |

### Apps using the History API to read or write data to the fitness store

The [History API](https://developers.google.com/fit/android/history) lets your app perform bulk operations on the
fitness store. These operations include reading, inserting, updating, and
deleting historical health and wellness data.

Follow these steps to migrate from the History API:

*Table 2: Migration steps from Fit History API*

| **Phone** | **Wear** |
| [Add Health Connect to your app](/health-and-fitness/guides/health-connect/develop/get-started). | Not applicable. Use Health Connect from your mobile app and not the wearable. |

### Apps using the Sensor API to display real-time fitness data

The [Sensor API](https://developers.google.com/fit/android/sensors) lets you read raw sensor data in your app in real
time. The Sensor API does the following:

* Lists data sources that are available on the device and on companion devices.
* Registers listeners to receive raw sensor data.
* Unregisters listeners so that they no longer receive raw sensor data.

Follow these steps to migrate from the Sensor API:

*Table 3: Migration steps from Fit Sensor API*

| **Phone** | **Wear** |
| Use [Sensors](/develop/sensors-and-location/sensors/sensors_overview), [Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider) | Use [Health Services](/health-and-fitness/guides/health-services) on Wear OS:   * `PassiveMonitoringClient` * `MeasureClient` * `ExerciseClient` Or use `SensorManager`, `FusedLocationProvider` |

### Apps using the Session API to provide activity summaries

Sessions represent a time interval during which users perform a fitness
activity.

The [Session API](https://developers.google.com/fit/android/using-sessions) lets your app create sessions in the fitness
store.

Follow these steps to migrate from the Session API:

*Table 4: Migration steps from Fit Session API*

| **Phone** | **Wear** |
| Start/stop: Not applicable. The application should track the state of ongoing sessions internally.  Read/write: [Add Health Connect to your app](/health-and-fitness/guides/health-connect/develop/get-started). | Start/stop: Use Health Services (ExerciseClient)  Read/write: Use Health Connect with your mobile app.  *For specific workflows, we advise the following:*   * Inserting a session: Developers should use Health Connect with their   mobile app and either insert an `ExerciseSessionRecord` or a   `SleepSessionRecord` accordingly. |

### Apps using the Goals API

Goals are targets in the Google Fit app that users can set for their metrics
like steps and heart points. The Fit platform records their goals and tracks
their daily activity against these using the [Goals API](https://developers.google.com/fit/android/using-goals).

*Table 5: Migration guidance for Fit Goals API*

| **Phone** | **Wear** |
| No replacement API available. | No replacement API available. |

### Apps using the BLE API

Your app can find available Bluetooth Low Energy (BLE) devices and insert
sensor data into the Google Fit platform using the [BLE API](https://developers.google.com/fit/android/ble-sensors).

**Follow these steps to migrate from BLE API:**

*Table 6: Migration steps from Fit BLE API*

| **Phone** | **Wear** |
| Use Android Bluetooth APIs directly. | Use Android Bluetooth APIs directly. |

## Fit app integrations

The following shows you how to integrate your Fit app depending if you have
existing users or new users for your app.

### Existing users of your app

If your app UI includes a way for users to connect to Google Fit (or if your
app is included on the list of [Works with Google Fit apps](https://play.google.com/store/apps/collection/promotion_3000e6f_googlefit_all)), you can
continue to maintain your Fit app integration for current users.

We will keep this section updated with information on when to deprecate your
Fit app integration, and what your best options are for maintaining your user
experience. In the meantime, you can [connect with us](/health-and-fitness#connect-with-us).

*Table 7: Recommendations for existing users with Fit app integrations*

| check**Do this** | close**Don't do this** |
| [Offer Health Connect](/health-and-fitness/guides/health-connect/design/ui-guidelines#promote-health-connect) as a new option in your app. Focus on user benefits like richer data and insights, privacy, and security.  Sync with Health Connect | Ask users to disconnect from Google Fit.  Disconnect from Health Connect |

### New users of your app

To offer a similar experience to new users of your app, we recommend
[building a Health Connect integration](/health-and-fitness/guides/health-connect/develop/get-started).

Health Connect offers you access to new data sources and types to provide a
richer experience for users. Data is stored on-device and is shared securely
between apps that the user allows, making it private, and secure.

*Table 8: Recommendations for new users with Fit app integrations*

| check**Do this** | close**Don't do this** |
| Include Health Connect in your app's [setup flow](/health-and-fitness/guides/health-connect/design/ui-guidelines#app-setup-flow). | Offer Fit as an app that users can connect to once Health Connect is available. |