---
title: https://developer.android.com/develop/xr/openxr/get-started
url: https://developer.android.com/develop/xr/openxr/get-started
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg)XR Headsets[](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg)Wired XR Glasses[](https://developer.android.com/develop/xr/devices#xr-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Before you start building with supported OpenXR extensions or with a supported engine, review the information and complete any tasks in the following sections to make sure your app is configured for immersive XR development.

## Configure your app's manifest file

As with other Android app projects, your Android XR app must have an`AndroidManifest.xml`file with specific manifest settings. The manifest file describes essential information about your app to the Android build tools, the Android operating system, and Google Play. See the[app manifest overview guide](https://developer.android.com/guide/topics/manifest/manifest-intro)for more information.
| **Note:** While Unity apps for Android XR build on top of OpenXR, you don't need to add these manifest elements or attributes manually if you use one of the[Android XR packages for Unity](https://developer.android.com/develop/xr/unity). The Unity packages create the manifest for your app based on your project and build settings.

For[XR differentiated apps](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated), your manifest file must contain the following elements and attributes:

### PROPERTY_XR_ACTIVITY_START_MODE property

The`android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"`property lets the system know that an activity should be launched in a specific mode when the activity is started.

This property has the following values:

- `XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED`(OpenXR only)

#### XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED

Apps built with OpenXR launch in Full Space and must use`XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED`start mode. Unmanaged Full Space signals to Android XR the app uses OpenXR.
**Note:** If you use one of the[Android XR packages for Unity](https://developer.android.com/develop/xr/unity), your app will also launch in Full Space. However, you don't need to add this to your manifest manually. The Unity packages create the manifest for your app based on your project and build settings.  


    <manifest ... >

       <application ... >
           <property
               android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
               android:value="XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED" />
           <activity
               android:name="com.example.myapp.MainActivity" ... >

               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />

                   <category android:name="android.intent.category.LAUNCHER" />
               </intent-filter>
           </activity>
       </application>
    </manifest>

### PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED property

The`android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"`property indicates that the application should be launched with a specific type of boundary. Your app needs to specify[`XR_BOUNDARY_TYPE_LARGE`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_LARGE())if it's designed to let users move around their physical space. Specifying[`XR_BOUNDARY_TYPE_NO_RECOMMENDATION`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_NO_RECOMMENDATION())provides no recommendations for the type of safety boundary, so the system uses the type that is already in use.  

    <manifest ... >

       <application ... >
           <property
               android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"
               android:value="XR_BOUNDARY_TYPE_LARGE" />
       </application>
    </manifest>

### \<uses-native-library\> OpenXR

OpenXR applications must declare the use of the native OpenXR library to successfully load its runtime. Without this[declaration](https://developer.android.com/guide/topics/manifest/uses-native-library-element), the runtime fails to load.  

    <manifest ... >

        <application ... >

        <uses-native-library android:name="libopenxr.google.so" android:required="false" />

           <activity
               android:name="com.example.myapp.MainActivity" ... >

               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />

                   <category android:name="android.intent.category.LAUNCHER" />
               </intent-filter>
            </activity>
        </application>
    </manifest>

### PackageManager features for XR apps

When you[distribute apps through the Google Play Store](https://developer.android.com/develop/xr/package-and-distribute), you can specify required hardware or software features in the app manifest. The[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element allows the Play Store to appropriately filter apps shown to users.

The following features are specific to XR-differentiated apps.

#### android.software.xr.api.openxr

Apps that target the Android XR platform and are built with OpenXR or Unity must include this feature in the app manifest with the`android:required`attribute set to`true`.

Apps that use the[Android XR Extensions Package for Unity](https://developer.android.com/develop/xr/unity#android-xr-extensions-unity)version 1.0.0 or higher or the[Unity OpenXR: Android XR Package](https://developer.android.com/develop/xr/unity#unity-openxr)version 0.5.0-exp.1 or higher don't have to add this element manually to the app manifest. These two packages will inject this element into the app manifest for you.

Devices may specify a version for this feature, which indicates the highest version of OpenXR supported by the device. The higher 16 bits represent the major number, and the lower 16 bits represent the minor number. For example, to specify OpenXR version 1.1, the value would be set to`"0x00010001"`.

Apps can use the feature version to indicate a minimum version of OpenXR that the app requires. For example, if your app requires OpenXR version 1.1 support, declare the following feature:  

    <uses-feature android:name="android.software.xr.api.openxr"
        android:version="0x00010001"
        android:required="true" />

#### android.hardware.xr.input.controller

This feature indicates that the app requires input from a high precision, 6DoF (degrees of freedom) motion controller to function correctly. If your app supports controllers and can't function without them, set the value to`true`. If your app supports controllers but can operate without them, set it to`false`.
**Note:** 6DoF motion controllers are a pair of hardware controllers, one for each hand. Each controller is tracked independently in space through six degrees of freedom - both linear and rotational movements. These controllers typically have several hardware buttons, including a trigger as well as haptic feedback.  

    <!-- Sets android:required to true, indicating that your app can't function on devices without controllers. -->
    <uses-feature android:name="android.hardware.xr.input.controller" android:required="true" />

#### android.hardware.xr.input.hand_tracking

This flag indicates that the app requires high fidelity hand tracking to function correctly, including position, orientation, and velocity of joints in the user's hand. If your app supports hand tracking and can't function without it, set the value to`true`. If your app supports hand tracking, but can operate without it, set it to`false`.
**Note:** This flag is not required for detecting basic gestures such as pinching, poking, aiming, and gripping.  

    <!-- Sets android:required to true, indicating that your app can't function on devices without hand tracking. -->
    <uses-feature android:name="android.hardware.xr.input.hand_tracking" android:required="true" />

#### android.hardware.xr.input.eye_tracking

This flag indicates that the app requires high-fidelity eye tracking for input to function correctly. If your app supports eye tracking for input and can't function without it, set the value to`true`. If your app supports eye tracking for input, but can operate without it, set it to`false`.  

    <!-- Sets android:required to true, indicating that your app can't function on devices without eye tracking. -->
    <uses-feature android:name="android.hardware.xr.input.eye_tracking" android:required="true" />

| **Note:** Hand tracking and eye tracking are privacy-sensitive input methods and require the apps to request special permissions. See[Understand permissions for XR](https://developer.android.com/develop/xr/permissions)on this page for more information on declaring permissions.

## Next steps

Now that you've finished configuring your app's manifest and reviewing important information, explore ways that you can build with OpenXR:

- [Build with supported OpenXR extensions](https://developer.android.com/develop/xr/openxr/extensions)
- [Build with supported engines](https://developer.android.com/develop/xr/openxr#supported-engines)