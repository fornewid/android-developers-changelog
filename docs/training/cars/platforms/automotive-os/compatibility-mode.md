---
title: https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode
url: https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode
source: md.txt
---

# Android Automotive OS compatibility mode

To simplify the process of bringing mobile apps to Android Automotive OS devices, certain cars come with a compatibility mode that addresses common issues faced when bringing existing mobile apps into cars.

While this compatibility mode is used by the[Car ready mobile apps](https://developer.android.com/training/cars/car-ready-mobile-apps)program, apps that are not part of that program can also run in it.

## Understand compatibility mode

Android Automotive OS compatibility mode is a software feature available on[some vehicles](https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode#determine-support)to improve the user experience of apps built for mobile devices when run on Android Automotive OS.

### Back navigation

Unlike other form factors, there is no requirement for Android Automotive OS devices to have a hardware or software back affordance. The compatibility mode addresses this by requiring a system-provided back affordance, such as a hardware button, software button, or gesture. This means that apps don't need to provide their own back navigation controls when targeting only devices with compatibility mode.  
![](https://developer.android.com/static/training/cars/images/nav-with-compat.png)  
check_circle

### With compatibility mode

The user can navigate back to the previous screen even though the app doesn't provide a back affordance in its UI.  
![](https://developer.android.com/static/training/cars/images/nav-without-compat.png)  
cancel

### Without compatibility mode

The user cannot navigate back to the previous screen.

### Safe area rendering

In cars, software and hardware elements such as[system bars and display cutouts](https://developer.android.com/training/cars/parked/automotive-os#insets-and-cutouts)can invalidate assumptions made when developing apps primarily for mobile devices. The compatibility mode addresses this by rendering apps within a safe area.

### Density scaling

Because the interaction distance in cars is greater than with other large screen devices, touch targets and font sizes are often smaller than recommended when running on a car. The compatibility mode addresses this by allowing OEMs to specify a DPI scaling factor used when rendering apps.

### Activity lifecycle

As described in[Add support for Android Automotive OS to your parked app](https://developer.android.com/training/cars/parked/automotive-os#driver-distraction), the OS blocks your app's activities automatically when the car enters driving mode to reduce distractions for the driver. On devices with compatibility mode, the OEM's blocking UI must not be transparent, so your app is no longer visible and transitions to the[*Stopped*lifecycle state](https://developer.android.com/guide/components/activities/activity-lifecycle#onstop)when blocked.
| **Caution:** This behavior applies to*all*applications running on a device that supports compatibility mode, not just the apps that run in compatibility mode.

## Configure compatibility mode

By default, your app's activities are run in compatibility mode when the device supports it. Activities**aren't** run in compatibility mode when a`<uses-feature>`element for the`android.hardware.type.automotive`feature is present in the manifest:  

    <manifest ...>
      ...
      <uses-feature android:name="android.hardware.type.automotive" ...>
      ...
    </manifest>

If you'd prefer for your activities to be run in display compatibility mode, irrespective of the`<uses-feature>`element described earlier, you can add the following`<meta-data>`element in your app's manifest:  

    <application ...>
      ...
      <meta-data android:name="android.software.car.display_compatibility" android:value="true"/>
      ...
    </application>

## Test your app in compatibility mode

To test your app in compatibility mode, you can use the[generic system images with compatibility mode](https://developer.android.com/training/cars/testing/emulator?filter=compatibility-mode#generic-images)or[Android Automotive OS on Pixel Tablet](https://developer.android.com/training/cars/testing/aaos-on-pixel)system images.

## Determine device support

Devices that support the Android Automotive OS compatibility mode must declare the`android.software.car.display_compatibility`system feature. To discover which devices support this feature, you can use the Play Console's[Device catalog](https://play.google.com/console/about/devicecatalog).