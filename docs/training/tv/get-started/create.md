---
title: https://developer.android.com/training/tv/get-started/create
url: https://developer.android.com/training/tv/get-started/create
source: md.txt
---

# Create and run a TV app

TV apps use the same structure as apps for phones and tablets. This similarity means you can modify your existing apps to also run on TV devices or create new apps based on what you already know about building apps for Android.

**Important:** Your app must meet specific requirements to qualify as an Android TV app on Google Play. For more information, see the requirements listed in[TV app quality](https://developer.android.com/distribute/essentials/quality/tv).

This guide describes how to prepare your development environment for building TV apps and the minimum required changes to enable an app to run on TV devices.

For information about designing apps for TV, see[Design for TV](https://developer.android.com/design/tv). Also see the sample apps in the[Android TV GitHub repository](https://github.com/android/tv).

## Determine media format support

See the following documentation for information about the codecs, protocols, and formats supported by Android TV:

- [Supported media formats](https://developer.android.com/guide/appendix/media-formats)
- [DRM](https://source.android.com/devices/drm.html)
- [android.drm](https://developer.android.com/reference/android/drm/package-summary)
- [ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)
- [android.media.MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer)

## Set up a TV project

This section discusses how to set up a TV project, whether you are modifying an existing Android app to run on TV devices or creating a new TV app. If you have an existing Android app, adding Android TV support lets you design a user interface for TV while re-using your existing app architecture.
| **Note:** We recommend that you have a single app that supports both mobile devices and TV devices. If you need separate apps for mobile devices and TV devices, you can publish multiple apps under the same listing on Google Play by using multiple APK support. For more information, see[Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks).

There are two main components you use when creating an app that runs on TV devices:

- **Activity for TV:**In your application manifest, declare an activity that is intended to run on TV devices.
- **TV libraries:** Optionally, include one or more of the[androidx libraries](https://developer.android.com/training/tv/get-started/libraries)available for TV devices, which are listed in another section of this guide. These libraries provide widgets for building user interfaces.

### Prerequisites

Before you begin building an app for TV, you must take the following steps:

- **[Update your SDK tools](https://developer.android.com/studio/intro/update#GetTools)to version 24.0.0 or higher.**   
  The updated SDK tools let you build and test apps for TV.
- **Update your SDK with Android 5.0 (API 21) or higher.**   
  The updated platform version provides new APIs for TV apps.
- **[Create](https://developer.android.com/studio/projects/create-project)or update your app project.**   
  To access new APIs for TV devices, create a project or modify an existing project that targets Android 5.0 (API level 21) or higher.

### Declare a TV activity

An application intended to run on TV devices must declare a launcher activity for TV in its manifest. It uses a[CATEGORY_LEANBACK_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER)intent filter to do this. This filter identifies your app as being enabled for TV and lets Google Play identify it as a TV app. When a user selects your app on their TV home screen, this intent identifies which activity to launch.

The following code snippet shows how to include this intent filter in your manifest:  

```xml
<application
  android:banner="@drawable/banner" >
  ...
  <activity
    android:name="com.example.android.MainActivity"
    android:label="@string/app_name" >

    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
  </activity>

  <activity
    android:name="com.example.android.TvActivity"
    android:label="@string/app_name"
    android:theme="@style/Theme.Leanback">

    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LEANBACK_LAUNCHER" />
    </intent-filter>

  </activity>
</application>
```

The second activity manifest entry in this example specifies that it is the activity to launch on a TV device.

**Caution:** If you don't include the`CATEGORY_LEANBACK_LAUNCHER`intent filter in your app, it's not visible to users running Google Play on TV devices. Also, if your app doesn't have this filter when you use developer tools to load it onto a TV device, the app does not appear in the TV user interface.

Your TV app's user interface, or the TV portion of your existing app, must provide a simple interface for easy navigation using a remote control from 10 feet away. If you are modifying an existing app for use on TV, don't use the same activity layout for TV that you use for phones and tablets. For guidelines on designing an app for TV, see[Design for TV](https://developer.android.com/design/tv).

### Declare TV device support

Declare that your app is for built for Android TV by declaring the`android.software.leanback`feature.

If your app runs on both mobile and TV, set the`required`attribute value to`false`. If you set the`required`attribute value to`true`, Google Play will only make your app available on Android TV OS.  

```xml
<manifest>
    <uses-feature android:name="android.software.leanback"
        android:required="false" />
    ...
</manifest>
```

### Declare touchscreen not required

Applications that are intended to run on TV devices don't rely on touchscreens for input. To make this clear, your TV app's manifest must declare that the`android.hardware.touchscreen`feature is not required. This setting identifies your app as being able to work on a TV device, and it is required for your app to be considered a TV app in Google Play. The following code example shows how to include this manifest declaration:  

```xml
<manifest>
    <uses-feature android:name="android.hardware.touchscreen"
              android:required="false" />
    ...
</manifest>
```

**Caution:**In your app manifest, you must declare that a touchscreen is not required, as shown this example code. Otherwise, your app doesn't appear in Google Play on TV devices.

### Provide a home screen icon and banner

Android TV apps must provide both a home screen icon and a banner image for each localization. Depending on the Android TV device, either the icon or banner is used as the app launch point that appears on the home screen in the apps and games rows.

To add these to your app, describe the icon and banner in the manifest as follows:  

```xml
<application
    ...
    android:icon="@mipmap/ic_launcher"
    android:banner="@drawable/banner" >
    ...
</application>
```

#### Home screen icon

Android TV apps, like all Android apps, must provide a home screen icon. For best practices on desiging a great launch point for your app and detailed asset requirements, see the[Android TV app icon and banner guidelines](https://developer.android.com/design/ui/tv/guides/system/tv-app-icon-guidelines).

#### Home screen banner

Use the[`android:banner`](https://developer.android.com/guide/topics/manifest/application-element#banner)attribute with the[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)tag, to supply a default banner for all application activities, or with the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)tag to supply a banner for a specific activity.

For the banner, use an xhdpi resource with a size of 320 x 180 px. Text must be included in the image. If your app is available in more than one language, you must provide separate versions of the banner with text for each supported language.

### Change the launcher color

**Caution:** In Android 12 and higher, custom splash screen animations built using the`SplashScreen`platform API are not supported for Android TV apps.

When a TV app launches, the system displays an animation that resembles an expanding, filled circle. To customize the color of this animation, set the`android:colorPrimary`attribute of your TV app or activity to a specific color. Also, set two transition overlap attributes to`true`as shown in the following snippet from a theme resource XML file:  

```xml
<resources>
    <style ... >
      <item name="android:colorPrimary">@color/primary</item>
      <item name="android:windowAllowReturnTransitionOverlap">true</item>
      <item name="android:windowAllowEnterTransitionOverlap">true</item>
    </style>
</resources>
```

For more information about working with themes and styles, see[Styles and Themes](https://developer.android.com/guide/topics/ui/themes).

## Build an app for Android TV OS

Jetpack includes[androidx](https://developer.android.com/jetpack/androidx)package libraries for use with TV apps.

### Compose for TV

Compose is the recommended way to build apps for Android TV OS. Alongside the core Compose libraries, the Compose for TV libraries provide dedicated components designed specially for the big screen:

- [androidx.tv.foundation](https://developer.android.com/reference/kotlin/androidx/tv/foundation/package-summary)
- [androidx.tv.material](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary)

<br />

Discover how to build a TV app using Compose for TV in[Use Jetpack Compose on Android TV](https://developer.android.com/training/tv/playback/compose).

### Leanback UI toolkit

The Leanback UI toolkit provides APIs and user interface widgets for TV devices:

- [androidx.leanback.app](https://developer.android.com/reference/androidx/leanback/app/package-summary)
- [androidx.leanback.database](https://developer.android.com/reference/androidx/leanback/database/package-summary)
- [androidx.leanback.graphics](https://developer.android.com/reference/androidx/leanback/graphics/package-summary)
- [androidx.leanback.media](https://developer.android.com/reference/androidx/leanback/media/package-summary)
- [androidx.leanback.preference](https://developer.android.com/reference/androidx/leanback/preference/package-summary)
- [androidx.leanback.system](https://developer.android.com/reference/androidx/leanback/system/package-summary)
- [androidx.leanback.widget](https://developer.android.com/reference/androidx/leanback/widget/package-summary)
- [androidx.leanback.widget.picker](https://developer.android.com/reference/androidx/leanback/widget/picker/package-summary)

<br />

Discover how to build a TV app using the Leanback UI toolkit in[Build TV playback apps](https://developer.android.com/training/tv/playback).

## Run TV apps

Running your app is an important part of the development process. You can run your app on TV devices configured to support USB debugging or use virtual TV devices.

### Run on a physical device

Set up your TV device as follows:

1. Use a USB cable to connect your TV device to your development machine. If needed, refer to documentation provided by your device manufacturer.
2. On your TV device, navigate to**Settings**.
3. In the**Device** row, select**About**.
4. Scroll to**Build** and select**Build**several times until you get the message "You are now a developer!"
5. Return to**Settings** . In the**Preferences** row, select**Developer options**.
6. Select**Debugging \> USB debugging** and select**On**.
7. Navigate back to the TV home screen.

To test your application on your TV device:

1. In Android Studio, select your project and click**Run** ![](https://developer.android.com/static/images/tools/as-run.png)from the toolbar.
2. In the**Select Deployment Target** window, select your TV device and click**OK**.

### Run on a virtual device

The AVD Manager in the Android SDK provides device definitions that let you create virtual TV devices for running and testing your applications.

To create a virtual TV device:

1. Start the AVD Manager. For more information, see[Create and manage virtual devices](https://developer.android.com/tools/help/avd-manager).
2. In the AVD Manager dialog, click the**Device Definitions**tab.
3. Select one of the Android TV device definitions and click**Create AVD**.
4. Select the emulator options and click**OK** to create the AVD.

   **Note:** For best performance of the TV emulator device, use the x86 emulator and enable the**Use Host GPU** option. Also use virtual device acceleration when it's available. For more information on the emulator's hardware acceleration, see[Configure hardware acceleration for the Android Emulator](https://developer.android.com/studio/run/emulator-acceleration).

To test your application on the virtual TV device:

1. In Android Studio, select your project and click**Run** ![](https://developer.android.com/static/images/tools/as-run.png)from the toolbar.
2. In the**Select Deployment Target** window, select your virtual TV device and click**OK**.

For more information about using emulators, see[Run apps on the Android Emulator](https://developer.android.com/tools/devices/emulator). For more information on deploying apps from Android Studio to virtual devices, see[Debug your app](https://developer.android.com/studio/debug).

## Enable your TV app to run as an instant experience

[Instant experiences](https://developer.android.com/topic/google-play-instant/overview)make it easy for users to try out your TV app and can help increase adoption.

To set up your TV app to run as an instant app on an Android TV device or emulator, first follow the instructions to[create an instant-enabled app bundle](https://developer.android.com/topic/google-play-instant/getting-started/instant-enabled-app-bundle).

Next, in the`intent-filter`for your TV app's`MainActivity`, be sure that both`LAUNCHER`and`LEANBACK_LAUNCHER`are declared in`AndroidManifest.xml`:  

```xml
<activity
    android:name="com.example.android.MainActivity"
    android:label="@string/app_name" >

    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
      <category android:name="android.intent.category.LEANBACK_LAUNCHER" />
    </intent-filter>
  </activity>
```

Your TV app is now configured to run as an instant experience.

## Prepare your TV app for publication

Review the[TV Apps checklist](https://developer.android.com/training/tv/publishing/checklist)for the next steps to prepare your TV app for publication and distribution.