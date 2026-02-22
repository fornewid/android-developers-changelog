---
title: https://developer.android.com/topic/google-play-instant/guides/analytics
url: https://developer.android.com/topic/google-play-instant/guides/analytics
source: md.txt
---

# Add Google Analytics for Firebase to your instant app

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Tracking the success of an app, instant or installed, is important to each developer. Several analytics libraries are compatible with Google Play Instant, including[Fabric Answers](https://fabric.io/kits/android/answers),[Localytics](https://docs.localytics.com/dev/android.html#android), and[Mixpanel](https://mixpanel.com/help/reference/android).

If your current analytics solution isn't listed or if you find that it doesn't work with Google Play Instant, consider using Google Analytics for Firebase as your telemetry solution. This page describes how to set up Google Analytics for Firebase in an instant app project.

## Adding Google Analytics for Firebase to an instant app project

1. Add the Firebase SDK to your app by following the instructions described in the[Getting started guide for Google Analytics for Firebase](https://firebase.google.com/docs/analytics/android/start/).
2. Use the latest version of the google-services plugin.
3. Place the`google-services.json`file in each module.
4. Add the following line to each module's`build.gradle`file:

   <br />

   ### Groovy

   ```groovy
   // android { ... }
   // dependencies { ... }
   plugins {
       id 'com.google.gms.google-services'
   }
   ```

   ### Kotlin

   ```kotlin
   // android { ... }
   // dependencies { ... }
   plugins {
       id("com.google.gms.google-services")
   }
   ```

   <br />

Once you have added Google Analytics for Firebase to your instant app project, you can use the Google Analytics for Firebase APIs as you might in an installable app project.

For more information about how to use the Google Analytics for Firebase APIs, see the[getting started documentation for Google Analytics for Firebase](https://firebase.google.com/docs/analytics/android/start/).

## Differentiating between installed and instant app data

Because both your installed and your instant app share a package name, you may want to differentiate the events and data collected from each. To differentiate your instant and installed apps in Analytics, set a`app_type`user property, with the value "instant" for the instant app and "installed" for the installed app.
| **Note:** Both the instant app and the installed app need to implement the`app_type`user property. Further, you must publish the installed app that contains`app_type`before the instant app. Otherwise, Analytics logs installed app events to the instant app when users install the app.

The following code snippet shows an activity that gets an Analytics instance and then sets a user property. Notice that the code uses[`PackageManagerCompat.isInstantApp()`](https://developers.google.com/android/reference/com/google/android/gms/instantapps/PackageManagerCompat.html#isInstantApp())in the[onCreate(android.os.Bundle)](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method to determine the app's context.  

### Kotlin

```kotlin
val STATUS_INSTALLED = "installed"
val STATUS_INSTANT = "instant"
val ANALYTICS_USER_PROP = "app_type"

private lateinit var firebaseAnalytics: FirebaseAnalytics

protected fun onCreate(savedInstanceState: Bundle?) {
    ...

    firebaseAnalytics = FirebaseAnalytics.getInstance(this)

    // Determine the current app context, either installed or instant, then
    // set the corresponding user property for Google Analytics.
    if (InstantApps.getPackageManagerCompat(this).isInstantApp()) {
        firebaseAnalytics.setUserProperty(ANALYTICS_USER_PROP, STATUS_INSTANT)
    } else {
        firebaseAnalytics.setUserProperty(ANALYTICS_USER_PROP, STATUS_INSTALLED)
    }
}
```

### Java

```java
final String STATUS_INSTALLED = "installed";
final String STATUS_INSTANT = "instant";
final String ANALYTICS_USER_PROP = "app_type";

private FirebaseAnalytics firebaseAnalytics;

@Override
protected void onCreate(Bundle savedInstanceState) {
    ...

    firebaseAnalytics = FirebaseAnalytics.getInstance(this);

    // Determine the current app context, either installed or instant, then
    // set the corresponding user property for Google Analytics.
    if (InstantApps.getPackageManagerCompat(this).isInstantApp()) {
        firebaseAnalytics.setUserProperty(ANALYTICS_USER_PROP, STATUS_INSTANT);
    } else {
        firebaseAnalytics.setUserProperty(ANALYTICS_USER_PROP, STATUS_INSTALLED);
    }

}
```

Once you set the`app_type`user property, you can select an event in the Analytics console's**Events** tab and then filter the event by the`app_type`value. The resulting data projection gives you a count for the specified event in your instant or installed app.

For more information about how to log and view events in Google Analytics for Firebase, see[Log Events](https://firebase.google.com/docs/analytics/android/events).

## Interpreting Analytics events

Analytics allows you to track a variety of metrics valuable to an instant app. The following table describes relevant metrics for your instant app, including the corresponding event name or property in Analytics.

|        Name         |                                                                             Analytics value                                                                             |                                                                                                                                         Definition                                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Visits              | `session_start`                                                                                                                                                         | Session started. This event is automatically tracked.                                                                                                                                                                                                                                      |
| Physical purchases  | [`Firebase.Event.ECOMMERCE_PURCHASE`](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event.html#ECOMMERCE_PURCHASE) | Physical purchases. You must explicitly track this event in your code.                                                                                                                                                                                                                     |
| Digital purchases   | `in_app_purchase`                                                                                                                                                       | Digital in-app purchases. This event is automatically tracked.                                                                                                                                                                                                                             |
| Time in app         | `user_engagement`                                                                                                                                                       | Amount of time that the app spends in the foreground. This event is automatically tracked.                                                                                                                                                                                                 |
| Instant app context | `app_type`                                                                                                                                                              | Events raised from the app running in the instant or installed context. You must explicitly track this event in your code. See[Differentiating between installed and instant app data](https://developer.android.com/topic/google-play-instant/guides/analytics#analytics-implement)above. |
| Return visitors     | `session_start.count`and`app_type`                                                                                                                                      | Audience of users who visit twice or more. You must explicitly track the`app_type`event;`session_start`is tracked for you. See[Differentiating between installed and instant app data](https://developer.android.com/topic/google-play-instant/guides/analytics#analytics-implement)above. |

For more information about the constants for events that you can collect in Analytics, see[FirebaseAnalytics.Event](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event.html).