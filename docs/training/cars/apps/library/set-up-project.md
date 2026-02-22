---
title: https://developer.android.com/training/cars/apps/library/set-up-project
url: https://developer.android.com/training/cars/apps/library/set-up-project
source: md.txt
---

This page describes how to install the Car App library and now to configure
the manifest file for your app.

## Install the Car App library

To add the library to your app, see the Jetpack library [release page](https://developer.android.com/jetpack/androidx/releases/car-app#declaring_dependencies).
| **Important:** When depending on alpha and beta releases of the library, take extra caution when using newly introduced or experimental APIs. Specifically, new APIs in alpha releases and APIs that are annotated as experimental can change --- and potentially break --- your app when the hosts are updated. \*\*We strongly recommend that you don't refer to these categories of APIs in your production APKs.

## Configure your app's manifest files

Before you can create your car app, you must configure your app's
[manifest files](https://developer.android.com/guide/topics/manifest/manifest-intro).

### Declare your CarAppService

The host connects to your app through your [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) implementation.
You declare this service in your manifest to let the host discover and connect
to your app.

You also need to declare your app's category in the [`<category>`](https://developer.android.com/guide/topics/manifest/category-element) element of
your app's intent filter. See the list of [supported app categories](https://developer.android.com/training/cars/apps/library/set-up-project#supported-app-categories) for the
values allowed for this element.

The following code snippet shows how to declare a car app service for a point of
interest app in your manifest:  

    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService"/>
            <category android:name="androidx.car.app.category.POI"/>
          </intent-filter>
        </service>

        ...
    <application>

| **Caution:** You might see a lint warning because the service is exported, but doesn't require a [permission](https://developer.android.com/guide/topics/manifest/service-element#prmsn). It's generally safe to ignore this warning because you must override the [`createHostValidator()`](https://developer.android.com/reference/androidx/car/app/CarAppService#createHostValidator()) method, which gives you more granular control over which host apps can connect to your app.

### Supported app categories

When you declare your `CarAppService` as described in
[Declare your CarAppService](https://developer.android.com/training/cars/apps/library/set-up-project#declare-carappservice), you must also declare your app's category by
adding one or more of these values in the intent filter.

- `androidx.car.app.category.NAVIGATION`: Provides turn-by-turn navigation
  instructions. See [Build navigation apps for cars](https://developer.android.com/training/cars/apps/navigation).

- `androidx.car.app.category.POI`: Provides functionality relevant
  to finding points of interest such as parking spots, charging stations, and
  gas stations. See [Build point of interest apps for cars](https://developer.android.com/training/cars/apps/poi).

- `androidx.car.app.category.IOT`: Enables users to take relevant actions on
  connected devices from within the car. See
  [Build internet of things apps for cars](https://developer.android.com/training/cars/apps/iot).

- `androidx.car.app.category.WEATHER`: Lets users see relevant weather
  information related to their current location or along their route.
  See [Build weather apps for cars](https://developer.android.com/training/cars/apps/weather).

- `androidx.car.app.category.MEDIA`: Lets users browse and play music, radio,
  audiobooks, and other audio content in the car. See
  [Build templated media apps for cars](https://developer.android.com/training/cars/apps/media).

- `androidx.car.app.category.MESSAGING`: Lets users communicate
  with short-form text messages. See
  [Build templated messaging experiences for Android Auto](https://developer.android.com/training/cars/communication/messaging).

- `androidx.car.app.category.CALLING`: Lets users communicate
  with voice calling. See
  [Build calling experiences for Android Auto](https://developer.android.com/training/cars/communication/calling).

| **Important:** The categories listed here are those that are built using the Car App Library. For a complete list of app categories supported in cars, see the [Android for Cars Overview](https://developer.android.com/training/cars#supported-app-categories).

For detailed descriptions of each category and the criteria required to qualify
for a category, see [Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality).
| **Note:** The car app category isn't tied to the [category you choose for listing your app in Google Play](https://support.google.com/googleplay/android-developer/answer/9859673), which is used to help users discover the most relevant apps in the Play Store.

### Specify the app name and icon

To represent your app in the system UI, `carPermissionActivityLayout` must
specify an app name and an icon for the host. Use the [`label`](https://developer.android.com/guide/topics/manifest/service-element#label) and
[`icon`](https://developer.android.com/guide/topics/manifest/service-element#icon) attributes of your [`CarAppService`](https://developer.android.com/guide/topics/manifest/manifest-intro) to specify the app name and
icon used by the host to represent your app:  

    ...
    <service
       android:name=".MyCarAppService"
       android:exported="true"
       android:label="@string/my_app_name"
       android:icon="@drawable/my_app_icon">
       ...
    </service>
    ...

If you don't declare a label or icon in the [`<service>`](https://developer.android.com/guide/topics/manifest/service-element) element, the host
falls back to values specified by the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element.

### Set a custom theme

To set a custom theme for your car app:

1. Add a [`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element) element in your manifest file:

       <meta-data
           android:name="androidx.car.app.theme"
           android:resource="@style/<var translate="no">MyCarAppTheme</var> />

2. Declare your [style resource](https://developer.android.com/guide/topics/resources/style-resource) to set the attributes for your custom car
   app theme:

       <resources>
         <style name="<var translate="no">MyCarAppTheme</var>">
           <item name="carColorPrimary">@color/<var translate="no">my_primary_car_color</var></item>
           <item name="carColorPrimaryDark">@color/<var translate="no">my_primary_dark_car_color</var></item>
           <item name="carColorSecondary">@color/<var translate="no">my_secondary_car_color</var></item>
           <item name="carColorSecondaryDark">@color/<var translate="no">my_secondary_dark_car_color</var></item>
           <item name="carPermissionActivityLayout">@layout/<var translate="no">my_custom_background</var></item>
         </style>
       </resources>