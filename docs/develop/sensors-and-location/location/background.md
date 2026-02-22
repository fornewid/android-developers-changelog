---
title: https://developer.android.com/develop/sensors-and-location/location/background
url: https://developer.android.com/develop/sensors-and-location/location/background
source: md.txt
---

# Access location in the background

As described on the[request location permissions](https://developer.android.com/training/location/permissions)and[privacy best practices](https://developer.android.com/privacy/best-practices)pages, apps should only ask for the type of location permission that's critical to the user-facing feature, and properly disclose this to users. The majority of use cases only require location when the user is engaging with the app. If your app requires background location, such as when implementing geofencing, make sure that it's critical to the core functionality of the app, offers clear benefits to the user, and is done in a way that's obvious to them.  
**Note:**The Google Play store has updated its policy concerning device location, restricting background location access to apps that need it for their core functionality and meet related policy requirements. Adopting these best practices doesn't guarantee Google Play approves your app's usage of location in the background.

Learn more about the[policy changes](https://support.google.com/googleplay/android-developer/answer/9799150)related to device location.

## Background location access checklist

Use the following checklist to identify potential location access logic in the background:

- In your app's manifest, check for the[`ACCESS_COARSE_LOCATION`permission](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)and the[`ACCESS_FINE_LOCATION`permission](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION). Verify that your app requires these location permissions.

  - If your app targets Android 10 (API level 29) or higher, also check for the[`ACCESS_BACKGROUND_LOCATION`permission](https://developer.android.com/training/location/receive-location-updates#request-background-location). Verify that your app has a feature that requires it.
- Look for use of location access APIs, such as the[Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider),[Geofencing API](https://developers.google.com/location-context/geofencing), or[LocationManager API](https://developer.android.com/reference/android/location/LocationManager), within your code such as in the following constructs:

  - [Background services](https://developer.android.com/training/run-background-service/create-service)
  - [`JobIntentService`](https://developer.android.com/reference/kotlin/androidx/core/app/JobIntentService)objects
  - [`WorkManager`](https://developer.android.com/reference/kotlin/androidx/work/WorkManager)or[`JobScheduler`](https://developer.android.com/reference/kotlin/android/app/job/JobScheduler)tasks
  - [`AlarmManager`](https://developer.android.com/reference/kotlin/android/app/AlarmManager)operations
  - Pending intents that are invoked from an[app widget](https://developer.android.com/guide/topics/appwidgets)
- If your app uses an SDK or library that accesses location, this access is attributed to your app. To determine whether an SDK or library needs location access, consult the library's documentation.

## Evaluate background location access

If you find that your app accesses location in the background, consider taking the following actions:

- Evaluate whether background location access is critical to the core functionality of the app.
- If you don't need location access in the background, remove it.

  If your app targets Android 10 (API level 29) or higher, remove the[`ACCESS_BACKGROUND_LOCATION`permission](https://developer.android.com/training/location/receive-location-updates#request-background-location)from your app's manifest. When you remove this permission, all-the-time access to location isn't an option for the app on devices that run Android 10.
- Make sure the user is aware that your app is accessing location in the background. This is especially important for cases that aren't obvious to users.

- If possible,[refactor your location access logic](https://developer.android.com/about/versions/oreo/background-location-limits#tuning-behavior)so that you request location only when your app's activity is visible to users.

## Limited updates to background location

If background location access is essential for your app, keep in mind that Android preserves device battery life by setting*background location limits* on devices that run Android 8.0 (API level 26) and higher. On these versions of Android, if your app is running in the background, it can receive location updates only a few times each hour. Learn more about[background location limits](https://developer.android.com/about/versions/oreo/background-location-limits).

## Additional resources

To learn more about background location usage, view the following materials:

### Videos

[How to find possible background location usage](https://www.youtube.com/watch?v=xTVeFJZQ28c)

### Samples

[Sample](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/bglocationaccess)to demonstrate best practices for accessing location when app is in background.