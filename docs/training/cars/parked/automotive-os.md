---
title: https://developer.android.com/training/cars/parked/automotive-os
url: https://developer.android.com/training/cars/parked/automotive-os
source: md.txt
---

# Add support for Android Automotive OS to your parked app

When distributing your app to Android Automotive OS devices, there are some considerations unique to the form factor that you should be aware of. This guide explains those considerations.

## Test your existing app on an Android Automotive OS emulator

To begin building your app for Android Automotive OS, first test your existing app on an Android Automotive OS emulator. To set up an emulator, follow the steps in[Test using the Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator). You can then run the app by following the instructions in[Run your app on the emulator](https://developer.android.com/studio/run/emulator#runningapp).

When running your app, watch for compatibility issues, such as the following:

- Infotainment screens have fixed orientations. To meet the[car app quality guidelines](https://developer.android.com/docs/quality-guidelines/car-app-quality#display-orientation), apps must support both portrait and landscape orientations.
- APIs available on other devices might not be available on Android Automotive OS. For example, some Google Play services APIs are not available on Android Automotive OS. See the[Disable features](https://developer.android.com/training/cars/parked/automotive-os#disable-features)section for details on how to handle these issues.

<br />

## Configure your app's manifest file

To target Android Automotive OS devices, your app must have certain manifest entries. After you've opted-in to distributing to Android Automotive OS devices, compatible apps are put through a manual review process to help ensure that they're safe for use in a car. See[Distribute to cars](https://developer.android.com/training/cars/distribute)for more details.

### Required Android Automotive OS features

All apps built for Android Automotive OS must meet certain requirements to be distributed using Google Play. See[Meet Google Play feature requirements](https://developer.android.com/training/cars/platforms/automotive-os#play-feature-requirements)for more information.
| **Warning:** If your app does not meet these requirements, it will be rejected upon submission to the Google Play.

### Category-specific manifest entries

In addition to the preceding requirements, which apply to all parked apps, the video and games categories have additional requirements:

- For video apps, see[Mark your app as a video app](https://developer.android.com/training/cars/parked/video#mark-video).
- For games, see[Mark your app as a game](https://developer.android.com/training/cars/parked/games#mark-game).

## Meet driver distraction requirements

Avoiding driver distraction is critical when bringing your app to cars. For parked apps, this is primarily accomplished by preventing your app from being used or playing audio while[user experience (UX) restrictions](https://developer.android.com/training/cars/platforms/automotive-os#ux-restrictions)are active, as captured by the[`DD-2`](https://developer.android.com/docs/quality-guidelines/car-app-quality#DD-2)and[`DD-3`](https://developer.android.com/docs/quality-guidelines/car-app-quality#DD-3)quality guidelines.
| **Note:** The exception to this rule is video apps, which can[support audio while driving](https://developer.android.com/training/cars/parked/video#audio-while-driving)on supported devices to let users continue playing content while UX restrictions are active.

### Prevent use while user experience restrictions are active

By default, activities cannot be used or launched while UX restrictions are active. To ensure this behavior applies to your app, it must not include the following`<meta-data>`element in any[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)element within your manifest:  

    <!-- NOT ALLOWED -->
    <meta-data
      android:name="distractionOptimized"
      android:value="true"/>

If an activity in your app is*Resumed*when UX restrictions become active, it is obscured by an activity owned by the OS.

At the minimum, your app's activity transitions to the[*Paused*lifecycle state](https://developer.android.com/guide/components/activities/activity-lifecycle#onpause). This happens as an`onPause()`lifecycle callback during which you must pause both video and audio playback from your app.

On devices that include the[Android Automotive OS compatibility mode](https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode#activity-lifecycle), the system blocking causes your app's activities to transition through the*Paused* state to the[*Stopped*state](https://developer.android.com/guide/components/activities/activity-lifecycle#onstop).

### Stop playback and prevent playback resumption

For some apps, pausing playback during`onPause()`and tracking state to prevent playback resumption until`onResume()`is sufficient to meet driver distraction requirements.

If reacting to lifecycle callbacks isn't sufficient for your app, you can listen to UX restriction state directly as described in the following section. For example, apps that support[picture-in-picture](https://developer.android.com/develop/ui/compose/system/picture-in-picture)may prefer to listen directly rather than have conditional checks in lifecycle callbacks.

#### Listen to user experience restrictions

To listen to UX restrictions, first add a dependency on the[`android.car`](https://developer.android.com/reference/android/car/classes)library in your app module's`build.gradle`file. This is an extension to the Android SDK that provides APIs that are specific to Android Automotive OS.  

    android {
        ...
        useLibrary("android.car")
    }

Use the[`CarUxRestrictionsManager`](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictionsManager)to read UX restriction state. Don't attempt to determine the UX restriction state from other hardware state such as gear or speed, because UX restrictions may vary from display to display within a vehicle.  

    val car = Car.createCar(context)
    val carUxRestrictionsManager =
        car.getCarManager(Car.CAR_UX_RESTRICTION_SERVICE) as CarUxRestrictionsManager

    // You can either read the state directly ...
    val currentUxRestrictions = carUxRestrictionsManager.currentUxRestrictions

    // or listen to state changes
    carUxRestrictionsManager.registerListener { carUxRestrictions: CarUxRestrictions -> ...}

    // Don't forget to teardown and release resources when they're no longer needed
    carUxRestrictionsManager.unregisterListener()
    car.disconnect()

| **Tip:** You can use a runtime check to support both Android Automotive OS and other form factors with the same code by only calling`Car.createCar()`on Android Automotive OS devices.

The only value provided by[`CarUxRestrictions`](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictions)that your app should reference is the return value of[`isRequiresDistractionOptimization()`](https://developer.android.com/reference/android/car/drivingstate/CarUxRestrictions#isRequiresDistractionOptimization()). Other values are only relevant for activities that are marked as distraction optimized.

### Test your implementation

Validate that your app meets driver distraction requirements using the following procedure:

1. Install your app on a[system image](https://developer.android.com/training/cars/testing/emulator#generic-images)without the Google Play Store or Compatibility mode.
2. With the launcher app grid open,[simulate driving](https://developer.android.com/training/cars/testing/emulator#simulate-driving)and verify that your app cannot be opened.
3. Stop simulating driving and open your app to a playback screen and begin playback.
4. Simulate driving again and verify that playback pauses.
   1. If your app supports integrates with`MediaSession`, use`adb shell cmd media_session dispatch play`and verify that playback doesn't resume.

| **Caution:** To verify that your app pauses playback on all devices and not just those that support compatibility mode, make sure to test on a device that**doesn't** include the compatibility mode. See[Test using the Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator#generic-images)for information on which emulators do or don't include the compatibility mode.

## Optimize your app for Android Automotive OS

To give your users the best experience possible in cars, keep the following in mind while building your app for Android Automotive OS:

### Work with window insets and display cutouts

As with other form factors, Android Automotive OS includes system UI elements, such as status and navigation bars, and support for non-rectangular displays.

By default, apps draw in an area that doesn't overlap with system bars or display cutouts. However, you might want your app to hide the system bars, draw content behind them, or show content in a display cutout as described in[Lay out your app within window insets](https://developer.android.com/develop/ui/views/layout/insets). If your app does any of these, refer to the following subsections for details on how to let your app work well across the ecosystem of Android Automotive OS devices.
| **Caution:** Navigation bars may or may not include a back affordance on Android Automotive OS, and gesture navigation isn't supported. Car app quality guideline[`AN-1`](https://developer.android.com/docs/quality-guidelines/car-app-quality#AN-1)requires that your app be navigable by users without a system or hardware back affordance.

#### System bars, immersive mode, and edge-to-edge rendering

System bars in cars may be sized and positioned differently than on other form factors. For example, navigation bars may be positioned on the left, right, or bottom of the screen. Even in the case that there is a status bar on top and a navigation bar on the bottom (as is the case with most phones and tablets), the size of these elements will likely be much greater in cars.

Additionally, Android Automotive OS allows OEMs to control whether or not apps can[show or hide the system bars to enter and exit immersive mode](https://developer.android.com/develop/ui/views/layout/immersive). For example, by preventing apps from hiding the system bars, OEMs can ensure that vehicle controls, such as climate controls, are always accessible on screen. If an OEM has prevented apps from controlling system bars, nothing happens when an app calls the[`WindowInsetsController`](https://developer.android.com/reference/android/view/WindowInsetsController)(or[`WindowInsetsControllerCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat)) APIs to show or hide system bars. Refer to the documentation of`show`and`hide`to learn more about how to detect if your app was able to modify the insets.

Likewise, OEMs can also control whether or not apps can set the color and translucency of system bars to ensure that the bars and the elements contained within them are clearly visible at all times. If your app draws edge-to-edge, check that only non-critical content is drawn behind system bars. This content may not be visible if the device OEM prevents setting the color or translucency of the bars.  

    <!-- Depending on OEM configuration, these style declarations
         (and the corresponding runtime calls) may be ignored -->
    <style name="...">
      <item name="android:statusBarColor">...</item>
      <item name="android:navigationBarColor">...</item>
      <item name="android:windowTranslucentStatus">...</item>
      <item name="android:windowTranslucentNavigation">...</status>
    </style>

If your app goes edge-to-edge, don't make assumptions about the size, number, type, or location of system bars. Instead, use the window insets APIs to lay out your app's content relative to the system bars. See[Display content edge-to-edge in your app](https://developer.android.com/develop/ui/views/layout/edge-to-edge)for more details on how to use these APIs. Hard-coded padding values are never recommended for any form factor, but in cars they likely won't work to keep content in the safe area at all.
| **Tip:** For details on how to test how your app handles these various configurations, see[Test using the configurable emulator](https://developer.android.com/training/cars/testing/emulator/configurable).

#### Adapt to irregularly shaped displays

In addition to rectangular displays, some vehicles may have irregularly shaped screens, such as shown in**Figure 1**:
![A diagram of an Android Automotive OS device with a display that's curved on the right side.](https://developer.android.com/static/images/training/cars/aaos-curved.png)**Figure 1**: An Android Automotive OS device with a display that's curved on the right side. The green area is the safe rectangle that doesn't overlap with the bounding box of the curve's display cutout.

If your app doesn't render edge-to-edge, you don't need to do anything for it to render within the safe area.

If your app renders edge-to-edge, you can choose how you'd like it to behave with respect to display cutouts. You can accomplish this using resources by setting the[`android:windowLayoutInDisplayCutoutMode`](https://developer.android.com/reference/android/R.attr#windowLayoutInDisplayCutoutMode)attribute for your app's[theme](https://developer.android.com/develop/ui/views/theming/themes)or at runtime by modifying the window's[`layoutInDisplayCutoutMode`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#layoutInDisplayCutoutMode)attribute.

Because the types of display cutouts present on Android Automotive OS devices are different than those on mobile devices, don't use the[`LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT)or[`LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES), which have behavior optimized for the cutouts found on mobile devices. Instead, use[`LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER)or[`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS)to either always avoid or always enter the cutout. When choosing the latter, see[Support display cutouts](https://developer.android.com/develop/ui/views/layout/display-cutout)for more details on the APIs related to display cutouts.

If your app renders into the display cutout area and you'd like to have different behavior between Android Automotive OS and mobile, see[Disable features](https://developer.android.com/training/cars/parked/automotive-os#disable-features)for guidance if your app sets this behavior at runtime and[Use alternate resources](https://developer.android.com/training/cars/parked/automotive-os#alternate-resources)if your app sets this behavior using resource files.
| **Tip:** For details on how to test how your app handles display cutouts, see[Test using the configurable emulator](https://developer.android.com/training/cars/testing/emulator/configurable#emulate-cutouts).

### Disable features

If you are making an existing mobile app available on Android Automotive OS, certain features and functionality might not be relevant or available. For example, cars generally don't provide access to cameras. Additionally, only a subset of Google Play services are available on Android Automotive OS; see[Google Play services for cars](https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services)for more details.

You can use the[`PackageManager.hasSystemFeature`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))API to detect whether the app is running on Android Automotive OS by checking for the[`FEATURE_AUTOMOTIVE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUTOMOTIVE)feature, as shown in the following example:  

### Kotlin

```kotlin
val packageManager: PackageManager = ... // Get a PackageManager from a Context
val isCar = packageManager.hasSystemFeature(PackageManager.FEATURE_AUTOMOTIVE)
if (isCar) {
  // Enable or disable a given feature
}
```

### Java

```java
PackageManager packageManager = ... // Get a PackageManager from a Context
boolean isCar = packageManager.hasSystemFeature(PackageManager.FEATURE_AUTOMOTIVE)
if (isCar) {
  // Enable or disable a given feature
}
```

Alternatively, if your app also has an Android Auto component, you can use the[`CarConnection`](https://developer.android.com/training/cars/apps#car-connection)API from the[Android for Cars App Library](https://developer.android.com/training/cars/apps)to detect whether the app is running on Android Automotive OS or Android Auto---or if it is not connected to a car at all.

For Picture-in-Picture (PiP), follow the established[best practices](https://developer.android.com/guide/topics/ui/picture-in-picture#best)to check whether the feature is available and react appropriately.

### Handle offline scenarios

While cars are becoming increasingly internet connected, apps are recommended to handle running without an internet connection, such as in the following cases:

- Users might opt out of mobile data offered as part of a subscription package from the auto maker.
- Access to mobile data might be limited in certain areas.
- Cars with Wi-Fi radios might be out of Wi-Fi range, or an OEM might turn off Wi-Fi in favor of a mobile network.

Be prepared to handle these scenarios in your app by gracefully degrading functionality that depends on internet access, such as by offering offline content. For more information, see the[best practices for optimizing networking](https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity#network).

### Use alternate resources

To help adapt your app for cars, you can use the[`car`resource qualifier](https://developer.android.com/guide/topics/resources/providing-resources#UiModeQualifier)to[provide alternate resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)when running on an Android Automotive OS vehicle. For example, if you use[Dimension resources](https://developer.android.com/guide/topics/resources/more-resources#Dimension)to store padding values, you could use a larger value for the`car`resource set to make touch targets larger.
| **Important:** The`car`resource qualifier is matched when the mode returned by[`UiModeManager.getCurrentModeType()`](https://developer.android.com/reference/android/app/UiModeManager#getCurrentModeType())is[`UI_MODE_TYPE_CAR`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_TYPE_CAR). This is always the case on Android Automotive OS, but can occasionally be the case on other devices (for example, when an app calls[`UiModeManager.enableCarMode()`](https://developer.android.com/reference/android/app/UiModeManager#enableCarMode(int))itself).