---
title: https://developer.android.com/training/cars/parked/auto
url: https://developer.android.com/training/cars/parked/auto
source: md.txt
---

# Add support for Android Auto to your parked app

On devices running Android 15 or higher, Android Auto supports running apps in[supported parked app categories](https://developer.android.com/training/cars#parked)directly on the head unit. See[Parked apps](https://developer.android.com/training/cars/platforms/android-auto#parked-apps)for more information about the parked app user experience on Android Auto.

## Declare Android Auto support

To declare that your app supports Android Auto, you must include the following`<category>`element in the intent filter of an activity in your app's manifest:  

    <activity ...>
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            ...
            <category android:name="android.intent.category.CAR_LAUNCHER" />
        </intent-filter>
    </activity>

Generally, the`android.intent.category.CAR_LAUNCHER`category element can be placed in the same intent filter as the`android.intent.category.LAUNCHER`element, but it can be in a different one if preferred.
| **Caution:** Be careful not to promote builds that support Android Auto to track types other than those listed in[Supported app categories](https://developer.android.com/training/cars#parked), or your submission will be rejected[during review](https://developer.android.com/training/cars/distribute#understand-review).

### Category-specific manifest entries

In addition to the preceding requirement, games have an additional requirement. See[Mark your app as a game](https://developer.android.com/training/cars/parked/games#mark-game).
| **Important:** Games are the only parked app category supported by Android Auto at this time.

## Support common Android Auto screen sizes

For the best user experience, we recommend making your app[fully adaptive](https://developer.android.com/develop/ui/compose/build-adaptive-apps)to different screen sizes. At the minimum, to ensure a high quality experience in the variety of cars that support Android Auto, apps**must not** be significantly pillarboxed on landscape screens, as captured by the[`DO-2`](https://developer.android.com/docs/quality-guidelines/car-app-quality#DO-2)car app quality guideline.

For example, if an app runs in a portrait aspect ratio with pillarboxing on a landscape screen, it will be rejected during Play Store review. An app running in a landscape aspect ratio with minimal pillarboxing on a landscape screen is acceptable, as is an app running in a landscape aspect ratio with letterboxing on a portrait screen.
| **Tip:** See[Support large screen resizability](https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability)for game-specific guidance on adapting to different screen sizes.

### Test against canonical screen sizes

When building and testing your app for Android Auto, you can use the following[Desktop Head Unit (DHU) configurations](https://developer.android.com/training/cars/testing/dhu#configure-dhu)to verify that your app meets the preceding requirements:  

### Small Landscape

    [general]
    resolution = 800x480
    dpi = 160
    ...

| **Tip:** This is the default configuration used when running the DHU, and represents the most common configuration for cars that support Android Auto.

### Wide Landscape

    [general]
    resolution = 1920x1080
    dpi = 160
    marginheight = 596
    normalizedpi = true
    cropmargins = true
    ...

### Portrait

    [general]
    resolution = 1920x1080
    dpi = 160
    marginwidth = 878
    normalizedpi = true
    cropmargins = true
    ...

## Detect usage on Android Auto

If you'd like to detect when your app is being used through Android Auto (such as for analytics purposes), you can look at two signals:

- The connection state reported by the[`CarConnection`](https://developer.android.com/training/cars/apps#car-connection)API. When Android Auto is connected, this will be[`CONNECTION_TYPE_PROJECTION`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#CONNECTION_TYPE_PROJECTION).
- The display ID of the active display. When your app is running on a display other than a built-in screen, such as when used through Android Auto, this is a value other than[`DEFAULT_DISPLAY`](https://developer.android.com/reference/android/view/Display#DEFAULT_DISPLAY).

The following snippet shows how to combine these signals to detect usage through Android Auto:  

    val connectionType = ...
    val displayId = context.display.displayId
    isRunningOnAndroidAuto = connectionType == CONNECTION_TYPE_PROJECTION and displayId != DEFAULT_DISPLAY

| **Caution:** This method might not always be accurate. A device could be connected to both Android Auto and another display, and your app might be running on that other display.