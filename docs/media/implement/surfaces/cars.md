---
title: https://developer.android.com/media/implement/surfaces/cars
url: https://developer.android.com/media/implement/surfaces/cars
source: md.txt
---

Bring your app to vehicles running either Android Auto or Android Automotive OS.
Use one app architecture that works for both cases so every user can enjoy your
app.

## What is Android for Cars?

A media app for cars can
provide a way for users to connect their digital lives seamlessly with their
cars. By extending the same apps for phone to be available for automobiles, you
create a better user experience. You can accomplish this by integrating with
Android Auto, or Android Automotive OS.

Android apps for cars must avoid driver distraction above all else. You can
minimize distractions by following best practices such as using voice commands
and a very practical visual design. In this way, your media app can show
timely information to the driver only when it's relevant and use predictable
patterns for common tasks.

### Android Auto

Android Auto provides a driver-optimized app experience for users who have an
Android phone with the Android Auto app and a compatible car or aftermarket
stereo system. They can use your app directly on their car's display by
connecting their phone. You enable Android Auto to connect with your phone app
by creating services that Android Auto uses to display a driver-optimized
interface to the driver.
| **Note:** Android Auto is only compatible with phones running Android 9 (API level 28) or higher.

### Android Automotive OS

Android Automotive OS is an Android-based infotainment system that is built into
vehicles. The car's system is a standalone Android-powered device that is
optimized for driving. With Android Automotive OS, users install your app
directly onto the car instead of their phones.

### Supported app categories

| **Important:** Media and video apps are considered separate categories for cars, which is explained further in the [Apps category table](https://developer.android.com/training/cars#supported-app-categories). For details on apps that play video, see [Video category](https://developer.android.com/training/cars#video).

Media apps let users browse and play music, radio, audiobooks, and other audio
content in the car. For more information, see
[Build audio playback apps for cars](https://developer.android.com/media/implement/surfaces/cars#build_audio_playback_apps_for_cars). Further information is also available at
[Build media apps for cars](https://developer.android.com/training/cars/media).

Media apps are built using [`MediaLibraryService`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService)
and [`MediaSession`](https://developer.android.com/reference/androidx/media3/session/MediaSession).
On Android
Automotive OS, you can also build sign-in and settings screens (for use while
parked) using Views or Compose.

Video apps let users view streaming videos while the car is parked. The core
purpose of these apps is to display streaming videos. These apps are built
using Views or Compose. For more information, see
[Build video playback apps for Android Automotive OS](https://developer.android.com/media/implement/surfaces/cars#build_video_playback_apps_for_Android_Automotive_OS). Further information
is available at
[Build video apps for Android Automotive OS](https://developer.android.com/training/cars/parked/video).

## Build audio playback apps for cars

This guide assumes you have a basic media playback app already. If you don't,
to get started, go to
[Create a basic media player app](https://developer.android.com/media/implement/playback-app#getting_started).

This guide gives you information on what you need to do, including links to
further resources with specific guidance.

#### Playback components

Media3 offers several key components for playback use-cases. The classes
that make up these components are familiar to you if you have worked with
previous Android media libraries.

The following diagram demonstrates how these components come together in a
typical app.
![The different components of a media app that uses Media3 connect
together in several simple ways owing to their sharing of interfaces
and classes.](https://developer.android.com/static/media/images/cars_media3_diagram.svg) **Figure 1**: Media app components **Important:** One of the primary characteristics that distinguishes Media3 from previous media APIs is that there is no longer a need for connectors between components. The new `MediaSession` class takes any class that implements the `Player` interface, as can the UI. Both `ExoPlayer` and `MediaController` are classes which implement that interface. This facilitates much better interaction between the components.

For more information,
see [Playback components](https://developer.android.com/guide/topics/media/media3#components).

### Implement a `MediaLibraryService` and `MediaLibrarySession`

A [`MediaLibraryService`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService)
provides a standardized API to serve and allow access to your media library.
This is required when adding support for Android Auto or Android Automotive
OS to your media app, since these platforms provide their own driver-safe UI
for your media library. For more information about implementing and using a
`MediaLibraryService`, see
[Serve content with MediaLibraryService](https://developer.android.com/guide/topics/media/session/medialibraryservice).

For playback controls, use a media session. The `MediaSession` API provides a
universal way of interacting with an audio or video player. The Jetpack Media3
library includes `MediaLibrarySession`, which extends `MediaSession` to add
content browsing APIs.

Connecting a media session to a player lets an app
advertise media playback externally and to receive playback commands from
external sources such as Android Auto, Android Automotive OS, or Google
Assistant. For more information, see
[Control and advertise playback using a MediaSession](https://developer.android.com/guide/topics/media/session/mediasession)
and [Use a MediaLibrarySession](https://developer.android.com/guide/topics/media/session/medialibraryservice#use).

At minimum, your media session should declare support for the following player
commands:

- [`COMMAND_PLAY_PAUSE`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_PLAY_PAUSE())

- [`COMMAND_STOP`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_STOP())

- [`COMMAND_SET_MEDIA_ITEM`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SET_MEDIA_ITEM())

- [`COMMAND_PREPARE`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_PREPARE())

The [Enable playback controls](https://developer.android.com/training/cars/media/enable-playback) guide
describes the ways you can customize your playback controls in cars.

When Android Auto or Android Automotive OS connect to your app, they request a
content library to display, which triggers the `onGetLibraryRoot()` callback
method. You can quickly return a root media item to allow access to your
library. The `onGetChildren()` callback method is called when Android Auto or
Android Automotive OS are trying to browse deeper levels of your content
library.

These platforms enforce additional
[limits](https://developer.android.com/training/cars/media#root-menu-structure) on how your content library
is structured. For details on customizing how your content library is displayed,
see the
[Create your media browser service](https://developer.android.com/training/cars/media#implement_browser)
guide.

### Declare support for Android Auto

Use the following manifest entry to declare that your phone app supports
Android Auto:  

    <application>
        ...
        <meta-data android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to an XML file that declares what automotive
capabilities your app supports. To indicate that you have a media app, add an
XML file named `automotive_app_desc.xml` to the `res/xml/` directory in your
project. This file should include the following content:  

    <automotiveApp>
        <uses name="media"/>
    </automotiveApp>

### Declare support for Android Automotive OS

You need to create an automotive module as not all of the logic in your app can
be shared with an automotive app. Some components of Android Automotive OS, such
as the manifest, have platform-specific requirements. Create a module that can
keep the code for these components separate from other code in your project,
such as the code used for your mobile app.

Follow these steps to add an automotive module to your project:

1. In Android Studio, click **File \> New \> New Module**.
2. Select **Automotive Module** , then click **Next**.
3. Enter an **Application/Library name**. This is the name that users see for your app on Android Automotive OS.
4. Enter a **Module name**.
5. Adjust the **Package name** to match your app.
6. Select **API 28: Android 9.0 (Pie)** for the **Minimum SDK** , and then click
   **Next**.

   All cars that support Android Automotive OS run on Android 9 (API level 28) or
   higher, so selecting this value targets all
   compatible cars.
7. Select **No Activity** , and then click **Finish**.

After creating your module in Android Studio, open the `AndroidManifest.xml` in
your new automotive module:  

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.media">

        <application
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            android:roundIcon="@mipmap/ic_launcher_round"
            android:supportsRtl="true"
            android:theme="@style/AppTheme" />

        <uses-feature
            android:name="android.hardware.type.automotive"
            android:required="true" />

    </manifest>

The [`application`](https://developer.android.com/guide/topics/manifest/application-element)
element has some standard app information as well as a
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element)
element that declares support for Android Automotive OS. Note that there
are no activities declared in the manifest.

If you implement [settings or sign-in activities](https://developer.android.com/training/cars/media/automotive-os#settings-sign-in),
add them here. These activities are triggered by the system using explicit
intents and are the only activities you declare within the manifest for your
Android Automotive OS app.

After adding any settings or sign-in activities, complete your manifest file by
setting the `android:appCategory="audio"` attribute in the `application` element
and adding the following `uses-feature` elements:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.media">

    <application
        android:allowBackup="true"
        android:appCategory="audio"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme" />

    <uses-feature
        android:name="android.hardware.type.automotive"
        android:required="true" />

    <uses-feature
        android:name="android.hardware.wifi"
        android:required="false" />
    <uses-feature
        android:name="android.hardware.screen.portrait"
        android:required="false" />
    <uses-feature
        android:name="android.hardware.screen.landscape"
        android:required="false" />

</manifest>
```

Explicitly setting these features to `required="false"` ensures that
your app doesn't conflict with available hardware features in Automotive OS
devices.

Use the following manifest entry to declare that your app supports Android
Automotive OS:  

    <application>
        ...
        <meta-data android:name="com.android.automotive"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>

This manifest entry refers to an XML file that declares the automotive
capabilities that your app supports.

To indicate that you have a media app, add an XML file named
`automotive_app_desc.xml` to the `res/xml/` directory in your project. Include
the following content in this file:  

    <automotiveApp>
        <uses name="media"/>
    </automotiveApp>

| **Note:** Don't include any references to the `com.google.android.gms.car.application` attribute that is required for Android Auto in your Android Automotive OS app.

#### Intent filters

Android Automotive OS uses explicit intents to trigger activities in your media
app. Don't include any activities that have
[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)
or [`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) intent
filters in the manifest file.

Activities like the one in the following example usually target a phone or some
other mobile device. Declare these activities in the module that builds the
phone app, not in the module that builds your Android Automotive OS app.  

    <activity android:name=".MyActivity">
    <intent-filter>
    <!-- You can't use either of these intents for Android Automotive OS -->
    <action android:name="android.intent.action.MAIN" />
    <category android:name="android.intent.category.LAUNCHER" />
    <!--
    In their place, you can include other intent filters for any activities
    that your app needs for Android Automotive OS, such as settings or
    sign-in activities.
    -->
    </intent-filter>
    </activity>

### Further steps

Now that you have an app for Android Auto and Android Automotive OS, you might
want to take additional steps to optimize your app to be more safely used while
driving. For more recommendations to help ensure a safe and convenient user
experience, see the technical guides for
[Voice actions](https://developer.android.com/training/cars/media#support_voice),
[Distraction safeguards](https://developer.android.com/training/cars/media#implement_distraction_safeguards),
and [Error handling](https://developer.android.com/training/cars/media#errors).

## Build video playback apps for Android Automotive OS

Since video apps are categorized separately from media apps in cars, you need to
be aware of some specific requirements for video apps, as described in
[Build parked apps for cars](https://developer.android.com/training/cars/parked), and
[Build video apps for Android Automotive OS](https://developer.android.com/training/cars/parked/video).
You need to use the following instructions.
| **Design guidelines:** Refer to [Adapt video apps](https://developers.google.com/cars/design/create-apps/parked-passenger-apps/overview) for UX guidance specific to video apps.
| **Important:** Google takes driver distraction very seriously. Your app must meet specific criteria before it can be listed on Google Play for Android Automotive OS. By adhering to these requirements, you can make it more efficient to build and test your app. For more information, see [Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=video).

### Mark your app as a video app

To indicate that your app supports video, add an XML file named
`automotive_app_desc.xml` to the res/xml/ directory in your project. In this
file, include the following content:  

    <automotiveApp>
        <uses name="video"/>
    </automotiveApp>

| **Note:** You might see a lint error in Android Studio that says "Expecting one of media, notification, sms, or template for the name attribute in uses tag." This can be safely ignored by adding `tools:ignore="InvalidUsesTagAttribute"` to the `uses` element.

Then, within the `application` element of your manifest, add the following
`meta-data` element referencing the XML file:  

    <meta-data android:name="com.android.automotive"
        android:resource="@xml/automotive_app_desc"/>