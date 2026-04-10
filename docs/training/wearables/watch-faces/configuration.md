---
title: https://developer.android.com/training/wearables/watch-faces/configuration
url: https://developer.android.com/training/wearables/watch-faces/configuration
source: md.txt
---

# Provide configuration activities on Wear OS

Some watch faces support configuration parameters to let users customize how the watch face looks and behaves. For example, some watch faces let users pick a custom background color. Other watch faces that tell time for two different time zones let users select which time zones they are interested in.

Watch faces that support configuration parameters let users customize a watch face using an activity. Users can start the wearable configuration activity on the wearable device. They can also start the companion configuration activity from the handheld app, if it has been installed. Additionally, users can configure the watch face in the device companion app for Wear OS 3 devices.

**Note:**Configuration on the device companion app is available on devices that target API level 30 and higher. Configuration on a handheld app is available on all devices.

## Use editor session

We strongly recommend that you support configuration on the smartwatch so that the user can customize their watch face without requiring a companion device.

To support this, a watch face can provide a configuration`Activity`and let the user change settings using an`EditorSession`returned from[`EditorSession.createOnWatchEditorSession`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/editor/EditorSession.Companion#createOnWatchEditorSession(androidx.activity.ComponentActivity)). As the user makes changes, calling[`EditorSession.renderWatchFaceToBitmap`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/editor/EditorSession#renderWatchFaceToBitmap(androidx.wear.watchface.RenderParameters,java.time.Instant,kotlin.collections.Map))provides a live preview of the watch face in the editor`Activity`.

### Specify an intent for configuration activities

If your watch face includes configuration activities and you are configuring your watch face from the device companion app, add the following metadata entries to the service declaration in the manifest file of the wearable app:  

```xml
<service>
    <meta-data
        android:name="com.google.android.wearable.watchface.wearableConfigurationAction"
        android:value="androidx.wear.watchface.editor.action.WATCH_FACE_EDITOR" />
    <meta-data
        android:name="com.google.android.wearable.watchface.companionBuiltinConfigurationEnabled"
        android:value="true" />
</service>
```

Configuration activities register intent filters for this intent, and the system fires this intent when users want to configure your watch face.

If your watch face only includes a companion or a wearable configuration activity, you only need to include the corresponding metadata entry from the prior example.

### Create a wearable configuration activity

Wearable configuration activities provide a limited set of customization choices for a watch face because complex menus are hard to navigate on smaller screens. In your wearable configuration activity, provide binary choices and just a few selections to customize the main aspects of your watch face.

To create a wearable configuration activity, add a new activity to your wearable app module and declare the following intent filter in the manifest file of the wearable app:  

```xml
<activity
    android:name=".DigitalWatchFaceWearableConfigActivity"
    android:label="@string/digital_config_name">
    <intent-filter>
        <action android:name="androidx.wear.watchface.editor.action.WATCH_FACE_EDITOR" />
        <category android:name=
        "com.google.android.wearable.watchface.category.WEARABLE_CONFIGURATION" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

The name of the action in this intent filter must be`androidx.wear.watchface.editor.action.WATCH_FACE_EDITOR`.

In your configuration activity, build a simple UI that provides selections for users to customize your watch face.

## Create a companion configuration activity

Companion configuration activities give users access to the full set of configuration choices for a watch face, because it is easier to interact with complex menus on the larger screen of a handheld device. For example, a configuration activity on a handheld device enables you to present users with elaborate color pickers to select the background color of a watch face.

**Note:**Configuration activities can only be written for handheld devices running Android such as phones, tablets, and foldables.

To create a companion configuration activity, add a new activity to your handheld app module and declare the following intent filter in the manifest file of the handheld app:  

```xml
<activity
    android:name=".DigitalWatchFaceCompanionConfigActivity"
    android:label="@string/app_name">
    <intent-filter>
        <action android:name=
            "com.example.android.wearable.watchface.CONFIG_DIGITAL" />
        <category android:name=
        "com.google.android.wearable.watchface.category.COMPANION_CONFIGURATION" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

In your configuration activity, build a UI that provides options to customize all the configurable elements of your watch face. After users make a selection, use the[Wearable Data Layer API](https://developer.android.com/training/wearables/data-layer)to communicate the configuration change to the watch face activity.

## Related resources

Refer to the following related resources:

- [Wear OS Samples Repository](https://github.com/android/wear-os-samples)