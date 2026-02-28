---
title: https://developer.android.com/develop/devices/assistant/cars
url: https://developer.android.com/develop/devices/assistant/cars
source: md.txt
---

<br />

[Video](https://www.youtube.com/watch?v=MI40lmJmp7w)

<br />

Voice control enables drivers perform to tasks without taking their hands off
the wheel or their eyes off the road. With App Actions for car apps, drivers can
use Google Assistant to control Android apps on their infotainment system by
saying things like, *"Hey Google, find street parking on ExampleApp"*.

App Actions works with [point of interest (POI)](https://developer.android.com/training/cars/apps/poi) car apps. This guide covers the
specific requirements and limitations for integrating App Actions into your POI
app.

## How it works

App Actions extend your in-app functionality to Assistant, enabling users to
access app features by using their voice. When a user invokes an App Action,
Assistant matches the query to a built-in intent ([BII](https://developer.android.com/guide/app-actions/intents)) declared in your app's
`shortcuts.xml` resource, and launches your app at the requested screen.

You declare support for BIIs in your app using Android [`capability`](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities#define_capabilities_in_shortcutsxml) elements.
When you upload your app using the Google Play console, Google registers the
capabilities declared in your app and makes them available for users to access
from Assistant.

![Chart showing car fulfillment.](https://developer.android.com/static/guide/app-actions/images/app-actions-car.png)

1. A user triggers Assistant and makes a voice request for a specific app.
2. Assistant matches the request to a pre-trained model (BII), and extracts any parameters supported by the BII.
3. In this example, Assistant matches the query to the [`GET_CHARGING_STATION`](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-charging-station) BII, extracts the location parameter "SFO", and translates the location to its geo coordinates.
4. The app is triggered via its fulfillment definition for this BII.
5. The app processes the fulfillment, displaying charging station options in the driver's infotainment system.

## Limitations

Car implementations of App Actions carry the following limitations:

- Car App Actions must be fulfilled using Android [deep links](https://developer.android.com/training/app-links/deep-linking). For information
  on App Actions fulfillments, see
  [Provide fulfillment details for built-in intents](https://developer.android.com/guide/app-actions/get-started#fulfillment).

- Car implementations only support the following BIIs:

  - Parking - [`GET_PARKING_FACILITY`](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-parking-facility)
  - Charging - [`GET_CHARGING_STATION`](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-charging-station)

## Requirements

> [!NOTE]
> **Note:** App Actions fulfillment is only available for car apps that implement the Car App Library and [declare support](https://developer.android.com/training/cars/apps#supported-app-categories) for the POI app category.

Perform the following steps to prepare your car app for App Actions:

- Fulfill the general Android app [requirements](https://developer.android.com/guide/app-actions/get-started#requirements) for App Actions.
- Include the Car App Library dependency. For details, see [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/car-app#declaring_dependencies).

## Determine your intent and fulfillment

The first step to voice enabling a car app with App Actions is to determine
which user voice commands, or *intents*, your app supports. You then define a
fulfillment for each intent to specify how your app should satisfy the request.

- **Which intents does your car app support?**

  App Actions provides pre-trained voice models, called built-in intents (BII),
  which can understand and interpret a user's voice commands when they say,
  *"Hey Google"* . To respond to voice requests, you simply declare to Assistant
  the BIIs that your app supports. For example, if you want your app to assist
  in finding a parking facility, you implement the [`GET_PARKING_FACILITY`](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-parking-facility)
  BII. Or, implement[`GET_CHARGING_STATION`](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-charging-station) BII to help users find electric
  car charging stations.
- **How should your app fulfill each intent?**

  Your app fulfills the voice request by launching itself to the appropriate
  screen. App Actions provides your fulfillment with parameters extracted from
  the user request, enabling you to tailor your response to the user's needs.

## Integrate App Actions

After determining your fulfillment strategy, follow these steps to voice enable
your car app:

1. Open your main activity `AndroidManifest.xml` and declare support for Android
   shortcuts. You use `capability` shortcut elements to declare to Assistant
   the BIIs that your app supports. For more information, see
   [Add capabilities](https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities).

        <!-- AndroidManifest.xml -->
        <meta-data
            android:name="android.app.shortcuts"
            android:resource="@xml/shortcuts" />

2. Next, add an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) element to `AndroidManifest.xml`. This
   enables Assistant to use deep links to connect to your app's content.

   - For Android Auto fulfillment, the [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) is the same as your
     mobile app.

   - For Android Automotive OS, your app's [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) session triggers
     Assistant. To allow a session to trigger your deep link, specify an
     [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) in the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) element of `AndroidManifest.xml`.

       <!-- AndroidManifest.xml -->
       <activity
         ...
         android:name="androidx.car.app.activity.CarAppActivity">
         ...
         <intent-filter>
             <action android:name="android.intent.action.VIEW" />
             <category android:name="android.intent.category.DEFAULT" />
             <category android:name="android.intent.category.BROWSABLE" />
             <data
               android:scheme="YOUR_SCHEME"
               android:host="YOUR_HOST" />
         </intent-filter>
       </activity>

3. If you don't already have a `shortcuts.xml` file your app's `res/xml`
   directory, create a new one. For information about how App Actions uses
   Android shortcuts, see [Create shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema).

   In `shortcuts.xml`, implement a [`capability`](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities#define_capabilities_in_shortcutsxml) for your chosen BII. Next,
   add a nested `<intent>` to define the app fulfillment.

       <!-- shortcuts.xml -->
       <?xml version="1.0" encoding="utf-8"?>
       <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">

         <capability android:name="actions.intent.GET_PARKING_FACILITY">
           <intent>
             <url-template
             android:value="YOUR_SCHEME://YOUR_HOST{?name,address,disambiguatingDescription,latitude,longitude}">

             <!-- Facility name, e.g. "Googleplex" -->
             <parameter
               android:name="parkingFacility.name"
               android:key="name"/>
             <!-- Address, e.g. "1600 Amphitheatre Pkwy, Mountain View, CA 94043" -->
             <parameter
               android:name="parkingFacility.address"
               android:key="address"/>
             <!-- Disambiguate the type of service, e.g. "valet" -->
             <parameter
               android:name="parkingFacility.disambiguatingDescription"
               android:key="disambiguatingDescription"/>
             <!-- Latitude, e.g. "37.3861" -->
             <parameter
               android:name="parkingFacility.geo.latitude"
               android:key="latitude"/>
             <!-- Longitude, e.g. "-122.084" -->
             <parameter
               android:name="parkingFacility.geo.longitude"
               android:key="longitude"/>
           </intent>
         </capability>
       </shortcuts>

4. Finally, update your car app's [`Session()`](https://developer.android.com/reference/androidx/car/app/Session(android.content.Intent)) logic to handle the incoming App
   Actions fulfillment. The following samples demonstrate intent handling for
   [`Session.onCreateScreen()`](https://developer.android.com/reference/androidx/car/app/Session#onCreateScreen(android.content.Intent)), and [`Session.onNewIntent()`](https://developer.android.com/reference/androidx/car/app/Session#onNewIntent(android.content.Intent)).

   **onCreateScreen()**

   ### Kotlin

   ```kotlin
   @Override
   fun onCreateScreen(@NonNull intent: Intent): Screen {
     if (intent.getData() != null) {
         val uri: Uri = intent.getData()
         // uri = "YOUR_SCHEME://YOUR_HOST?name=Levis%20center"
         // Build your Templates with parsed uri parameters
     ...
    }
   }
   ```

   ### Java

   ```java
   @Override
   public Screen onCreateScreen(@NonNull Intent intent) {
   if (intent.getData() != null) {
     Uri uri = intent.getData();
     // uri = "YOUR_SCHEME://YOUR_HOST?name=Levis%20center"
     // Build your Templates with parsed uri parameters
   ...
   }
   }
   ```

   <br />

   **onNewIntent()**

   ### Kotlin

   ```kotlin
   @Override
   fun onNewIntent(@NonNull intent: Intent): Screen {
     if (intent.getData() != null) {
         val uri: Uri = intent.getData()
         // uri = "YOUR_SCHEME://YOUR_HOST?name=Levis%20center"
         // Build your Templates with parsed uri parameters
         ...
     }
   }
   ```

   ### Java

   ```java
   @Override
   public void onNewIntent(@NonNull Intent intent) {
   if (intent.getData() != null) {
    Uri uri = intent.getData();
    // uri = "YOUR_SCHEME://YOUR_HOST?name=Levis%20center"
    // Build your Templates with parsed uri parameters
    ...
   }
   }
   ```

## Preview, test, and publish your app

App Actions provides tools to preview and test your app. Visit the
[App Actions overview](https://developer.android.com/guide/app-actions/get-started#preview_your_app_actions) for information about this tooling, and for details on
how to publish your voice-enabled car app to the Play Store.

*** ** * ** ***