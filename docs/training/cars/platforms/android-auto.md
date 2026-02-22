---
title: https://developer.android.com/training/cars/platforms/android-auto
url: https://developer.android.com/training/cars/platforms/android-auto
source: md.txt
---

![Android Auto user interface](https://developer.android.com/static/images/training/cars/android-auto.png) **Figure 1**: Android Auto

Android Auto provides a driver-optimized app experience for users who have an
Android phone with the Android Auto app and a compatible [car or aftermarket
stereo system](https://www.android.com/auto/compatibility/). They
can use your app directly on their car's display by connecting their phone. You
enable Android Auto to connect with your phone app by creating services that
Android Auto uses to display a driver-optimized interface to the driver.
| **Note:** Android Auto is only compatible with phones running Android 9 (API level 28) or higher.

## How apps declare support for Android Auto

Apps declare that they support Android Auto in different ways depending on their
category.

### Media, messaging, and templated apps

Media, messaging, and templated apps declare support for Android Auto by
including the following `<meta-data>` element in their manifest:  

    <application>
        ...
        <meta-data
            android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

The contents of the resource file vary depending on your app's category:  

### Media

```xml
<automotiveApp>
    <uses name="media" />
</automotiveApp>
      
```


See [Add support for
Android Auto to your media app](https://developer.android.com/training/cars/media/auto#manifest-car-app) for more details.

### Messaging

```xml
<automotiveApp>
    <uses name="notification" />
    <!-- Include the following only if your capp can be set as the default SMS handler -->
    <uses name="sms">
</automotiveApp>
      
```


See [Build messaging
apps for Android Auto](https://developer.android.com/training/cars/messaging#manifest-messaging) for more details.

### Templated apps

```xml
<automotiveApp>
    <uses name="template" />
</automotiveApp>
      
```


See [Add support for Android Auto to your templated app](https://developer.android.com/training/cars/apps/auto#declare-android-auto-support) for more details.

### Parked apps

Parked apps declare support for Android Auto by including the following
`<category>` element in the intent-filter of an activity in your app's manifest:  

    <activity ...>
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            ...
            <category android:name="android.intent.category.CAR_LAUNCHER" />
        </intent-filter>
    </activity>

See [Add support for Android Auto to your parked app](https://developer.android.com/training/cars/parked/auto) for more details.

## Parked apps

On devices running Android 15 or higher, Android Auto supports running
activities directly on the head unit while parked. This capability is limited to
apps in the [supported parked app categories](https://developer.android.com/training/cars#parked). For safety purposes, Android
Auto automatically exits an app when vehicle motion is detected.

### User interface

![Android Auto parked app user interface](https://developer.android.com/static/training/cars/images/parked-ui.png) **Figure 2**: An app running on Android Auto with the back and exit controls shown.

Activities run on Android Auto are always run in full screen. Users can swipe
from the top or bottom edge of the Android Auto UI to pull up controls for
navigating back or exiting the current app.

### Behavior differences

Due to restrictions imposed by Android Auto and Android more generally, there
are some notable behavior differences when an app runs on the head unit.

#### Starting other apps

Because only apps in supported categories that have declared support for Android
Auto can have their activities run on the head unit, it is likely that intents
to other apps won't open the other app on the head unit. If the intent is for a
web page or Google Play Store page, the corresponding app will be opened on the
phone instead. All other activity-launching intents are blocked and the user is
notified that the corresponding app can't be opened.

#### Accepting permissions

On devices running Android 15, it isn't possible for users to accept
runtime permissions requests on the head unit. When an app requests a
permission, a dialog appears informing users to accept the permission on their
phone screen.

## Trusted stores

As described in [Test in real vehicles](https://developer.android.com/training/cars/testing#real-vehicles),
apps must be installed from a trusted source to run on a real vehicle. Trusted
sources include the following:

- Google Play
- ONE store

## Frequently asked questions

### How can I detect if Android Auto is running?

To detect whether Android Auto is running on a device, you can use the
`CarConnection` API that is part of the Android for Cars App Library. See
[Connection API](https://developer.android.com/training/cars/apps#car-connection) for more details.
| **Caution:** On devices running Android 12 or higher, Android Auto doesn't change the [UI mode](https://developer.android.com/reference/android/content/res/Configuration#uiMode) of the device when running, so don't rely on it.

### In which vehicles is Android Auto available?

See the list of [compatible vehicles and stereos](https://www.android.com/auto/compatibility/vehicles/).

### In which countries is Android Auto available?

See [Is Android Auto available in my country?](https://www.android.com/auto/#al-faq)