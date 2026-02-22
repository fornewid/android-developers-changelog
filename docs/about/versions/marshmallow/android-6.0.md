---
title: https://developer.android.com/about/versions/marshmallow/android-6.0
url: https://developer.android.com/about/versions/marshmallow/android-6.0
source: md.txt
---

# Android 6.0 APIs

Android 6.0 ([M](https://developer.android.com/reference/android/os/Build.VERSION_CODES#M)) offers new features for users and app developers. This document provides an introduction to the most notable APIs.

### Start developing

To start building apps for Android 6.0, you must first[get the Android SDK](https://developer.android.com/studio). Then use the[SDK Manager](https://developer.android.com/tools/help/sdk-manager)to download the Android 6.0 SDK Platform and System Images.

### Update your target API level

To better optimize your app for devices running Android , set your[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)to`"23"`, install your app on an Android system image, test it, then publish the updated app with this change.

You can use Android APIs while also supporting older versions by adding conditions to your code that check for the system API level before executing APIs not supported by your[`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min). To learn more about maintaining backward compatibility, read[Supporting Different Platform Versions](https://developer.android.com/training/basics/supporting-devices/platforms).

For more information about how API levels work, read[What is API Level?](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

## Fingerprint Authentication

This release offers new APIs to let you authenticate users by using their fingerprint scans on supported devices, Use these APIs in conjunction with the[Android Keystore system](https://developer.android.com/training/articles/keystore).

To authenticate users via fingerprint scan, get an instance of the new[FingerprintManager](https://developer.android.com/reference/android/hardware/fingerprint/FingerprintManager)class and call the[authenticate()](https://developer.android.com/reference/android/hardware/fingerprint/FingerprintManager#authenticate(android.hardware.fingerprint.FingerprintManager.CryptoObject, android.os.CancellationSignal, int, android.hardware.fingerprint.FingerprintManager.AuthenticationCallback, android.os.Handler))method. Your app must be running on a compatible device with a fingerprint sensor. You must implement the user interface for the fingerprint authentication flow on your app, and use the standard Android fingerprint icon in your UI. The Android fingerprint icon (`c_fp_40px.png`) is included in the[Biometric Authentication sample](https://github.com/android/security-samples/tree/main/BiometricAuthentication/#readme). If you are developing multiple apps that use fingerprint authentication, note that each app must authenticate the user's fingerprint independently.

To use this feature in your app, first add the[USE_FINGERPRINT](https://developer.android.com/reference/android/Manifest.permission#USE_FINGERPRINT)permission in your manifest.  

```xml
<uses-permission
        android:name="android.permission.USE_FINGERPRINT" />
```
![Mobile showing fingerprint authentication functionality](https://developer.android.com/static/images/android-6.0/fingerprint-screen.png)

To see an app implementation of fingerprint authentication, refer to the[Biometric Authentication sample](https://github.com/android/security-samples/tree/main/BiometricAuthentication/#readme). For a demonstration of how you can use these authentication APIs in conjunction with other Android APIs, see the video[Fingerprint and Payment APIs](https://www.youtube.com/watch?v=VOn7VrTRlA4).

If you are testing this feature, follow these steps:

1. Install Android SDK Tools Revision 24.3, if you have not done so.
2. Enroll a new fingerprint in the emulator by going to**Settings \> Security \> Fingerprint**, then follow the enrollment instructions.
3. Use an emulator to emulate fingerprint touch events with the following command. Use the same command to emulate fingerprint touch events on the lockscreen or in your app.  

   ```
   adb -e emu finger touch <finger_id>
   ```

   On Windows, you may have to run`telnet 127.0.0.1 <emulator-id>`followed by`finger touch <finger_id>`.

## Confirm Credential

Your app can authenticate users based on how recently they last unlocked their device. This feature frees users from having to remember additional app-specific passwords, and avoids the need for you to implement your own authentication user interface. Your app should use this feature in conjunction with a public or secret key implementation for user authentication.

To set the timeout duration for which the same key can be re-used after a user is successfully authenticated, call the new[setUserAuthenticationValidityDurationSeconds()](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUserAuthenticationValidityDurationSeconds(int))method when you set up a[KeyGenerator](https://developer.android.com/reference/javax/crypto/KeyGenerator)or[KeyPairGenerator](https://developer.android.com/reference/java/security/KeyPairGenerator).

Avoid showing the re-authentication dialog excessively -- your apps should try using the cryptographic object first and if the timeout expires, use the[createConfirmDeviceCredentialIntent()](https://developer.android.com/reference/android/app/KeyguardManager#createConfirmDeviceCredentialIntent(java.lang.CharSequence, java.lang.CharSequence))method to re-authenticate the user within your app.

## App Linking

This release enhances Android's intent system by providing more powerful app linking. This feature allows you to associate an app with a web domain you own. Based on this association, the platform can determine the default app to use to handle a particular web link and skip prompting users to select an app. To learn how to implement this feature, see[Handling App Links](https://developer.android.com/training/app-links).

## Auto Backup for Apps

The system now performs automatic full data backup and restore for apps. Your app must target Android 6.0 (API level 23) to enable this behavior; you do not need to add any additional code. If users delete their Google accounts, their backup data is deleted as well. To learn how this feature works and how to configure what to back up on the file system, see[Configuring Auto Backup for Apps](https://developer.android.com/training/backup/autosyncapi).

## Direct Share

![Bottom portion of a mobile displaying Direct Share functionality](https://developer.android.com/static/images/android-6.0/direct-share-screen.png)

This release provides you with APIs to make sharing intuitive and quick for users. You can now define*direct share targets* that launch a specific activity in your app. These direct share targets are exposed to users via the*Share*menu. This feature allows users to share content to targets, such as contacts, within other apps. For example, the direct share target might launch an activity in another social network app, which lets the user share content directly to a specific friend or community in that app.

To enable direct share targets you must define a class that extends the[ChooserTargetService](https://developer.android.com/reference/android/service/chooser/ChooserTargetService)class. Declare your service in the manifest. Within that declaration, specify the[BIND_CHOOSER_TARGET_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CHOOSER_TARGET_SERVICE)permission and an intent filter using the[SERVICE_INTERFACE](https://developer.android.com/reference/android/service/chooser/ChooserTargetService#SERVICE_INTERFACE)action.

The following example shows how you might declare the[ChooserTargetService](https://developer.android.com/reference/android/service/chooser/ChooserTargetService)in your manifest.  

```xml
<service android:name=".ChooserTargetService"
        android:label="@string/service_name"
        android:permission="android.permission.BIND_CHOOSER_TARGET_SERVICE">
    <intent-filter>
        <action android:name="android.service.chooser.ChooserTargetService" />
    </intent-filter>
</service>
```

For each activity that you want to expose to[ChooserTargetService](https://developer.android.com/reference/android/service/chooser/ChooserTargetService), add a`<meta-data>`element with the name`"android.service.chooser.chooser_target_service"`in your app manifest.  

```xml
<activity android:name=".MyShareActivity”
        android:label="@string/share_activity_label">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
    </intent-filter>
<meta-data
        android:name="android.service.chooser.chooser_target_service"
        android:value=".ChooserTargetService" />
</activity>
```

## Voice Interactions

This release provides a new voice interaction API which, together with[Voice Actions](https://developers.google.com/voice-actions/), allows you to build conversational voice experiences into your apps. Call the[isVoiceInteraction()](https://developer.android.com/reference/android/app/Activity#isVoiceInteraction())method to determine if a voice action triggered your activity. If so, your app can use the[VoiceInteractor](https://developer.android.com/reference/android/app/VoiceInteractor)class to request a voice confirmation from the user, select from a list of options, and more.

Most voice interactions originate from a user voice action. A voice interaction activity can also, however, start without user input. For example, another app launched through a voice interaction can also send an intent to launch a voice interaction. To determine if your activity launched from a user voice query or from another voice interaction app, call the[isVoiceInteractionRoot()](https://developer.android.com/reference/android/app/Activity#isVoiceInteractionRoot())method. If another app launched your activity, the method returns`false`. Your app may then prompt the user to confirm that they intended this action.

To learn more about implementing voice actions, see the[Voice Actions developer site](https://developers.google.com/voice-actions/interaction/).

## Assist API

This release offers a new way for users to engage with your apps through an assistant. To use this feature, the user must enable the assistant to use the current context. Once enabled, the user can summon the assistant within any app, by long-pressing on the**Home**button.

Your app can elect to not share the current context with the assistant by setting the[FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)flag. In addition to the standard set of information that the platform passes to the assistant, your app can share additional information by using the new[AssistContent](https://developer.android.com/reference/android/app/assist/AssistContent)class.

To provide the assistant with additional context from your app, follow these steps:

1. Implement the[Application.OnProvideAssistDataListener](https://developer.android.com/reference/android/app/Application.OnProvideAssistDataListener)interface.
2. Register this listener by using[registerOnProvideAssistDataListener()](https://developer.android.com/reference/android/app/Application#registerOnProvideAssistDataListener(android.app.Application.OnProvideAssistDataListener)).
3. In order to provide activity-specific contextual information, override the[onProvideAssistData()](https://developer.android.com/reference/android/app/Activity#onProvideAssistData(android.os.Bundle))callback and, optionally, the new[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent))callback.

## Adoptable Storage Devices

With this release, users can*adopt* external storage devices such as SD cards. Adopting an external storage device encrypts and formats the device to behave like internal storage. This feature allows users to move both apps and private data of those apps between storage devices. When moving apps, the system respects the[`android:installLocation`](https://developer.android.com/guide/topics/manifest/manifest-element#install)preference in the manifest.

If your app accesses the following APIs or fields, be aware that the file paths they return will dynamically change when the app is moved between internal and external storage devices. When building file paths, it is strongly recommended that you always call these APIs dynamically. Don't use hardcoded file paths or persist fully-qualified file paths that were built previously.

- [Context](https://developer.android.com/reference/android/content/Context)methods:
  - [getFilesDir()](https://developer.android.com/reference/android/content/Context#getFilesDir())
  - [getCacheDir()](https://developer.android.com/reference/android/content/Context#getCacheDir())
  - [getCodeCacheDir()](https://developer.android.com/reference/android/content/Context#getCodeCacheDir())
  - [getDatabasePath()](https://developer.android.com/reference/android/content/Context#getDatabasePath(java.lang.String))
  - [getDir()](https://developer.android.com/reference/android/content/Context#getDir(java.lang.String, int))
  - [getNoBackupFilesDir()](https://developer.android.com/reference/android/content/Context#getNoBackupFilesDir())
  - [getFileStreamPath()](https://developer.android.com/reference/android/content/Context#getFileStreamPath(java.lang.String))
  - [getPackageCodePath()](https://developer.android.com/reference/android/content/Context#getPackageCodePath())
  - [getPackageResourcePath()](https://developer.android.com/reference/android/content/Context#getPackageResourcePath())
- [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)fields:
  - [dataDir](https://developer.android.com/reference/android/content/pm/ApplicationInfo#dataDir)
  - [sourceDir](https://developer.android.com/reference/android/content/pm/ApplicationInfo#sourceDir)
  - [nativeLibraryDir](https://developer.android.com/reference/android/content/pm/ApplicationInfo#nativeLibraryDir)
  - [publicSourceDir](https://developer.android.com/reference/android/content/pm/ApplicationInfo#publicSourceDir)
  - [splitSourceDirs](https://developer.android.com/reference/android/content/pm/ApplicationInfo#splitSourceDirs)
  - [splitPublicSourceDirs](https://developer.android.com/reference/android/content/pm/ApplicationInfo#splitPublicSourceDirs)

To debug this feature, you can enable adoption of a USB drive that is connected to an Android device through a USB On-The-Go (OTG) cable, by running this command:  

```
$ adb shell sm set-force-adoptable true
```

## Notifications

This release adds the following API changes for notifications:

- New[INTERRUPTION_FILTER_ALARMS](https://developer.android.com/reference/android/app/NotificationManager#INTERRUPTION_FILTER_ALARMS)filter level that corresponds to the new*Alarms only*do not disturb mode.
- New[CATEGORY_REMINDER](https://developer.android.com/reference/android/app/Notification#CATEGORY_REMINDER)category value that is used to distinguish user-scheduled reminders from other events ([CATEGORY_EVENT](https://developer.android.com/reference/android/app/Notification#CATEGORY_EVENT)) and alarms ([CATEGORY_ALARM](https://developer.android.com/reference/android/app/Notification#CATEGORY_ALARM)).
- New[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon)class that you can attach to your notifications via the[setSmallIcon()](https://developer.android.com/reference/android/app/Notification.Builder#setSmallIcon(android.graphics.drawable.Icon))and[setLargeIcon()](https://developer.android.com/reference/android/app/Notification.Builder#setLargeIcon(android.graphics.drawable.Icon))methods. Similarly, the[addAction()](https://developer.android.com/reference/android/app/Notification.Builder#addAction(int, java.lang.CharSequence, android.app.PendingIntent))method now accepts an[Icon](https://developer.android.com/reference/android/graphics/drawable/Icon)object instead of a drawable resource ID.
- New[getActiveNotifications()](https://developer.android.com/reference/android/app/NotificationManager#getActiveNotifications())method that allows your apps to find out which of their notifications are currently alive.

## Bluetooth Stylus Support

This release provides improved support for user input using a Bluetooth stylus. Users can pair and connect a compatible Bluetooth stylus with their phone or tablet. While connected, position information from the touch screen is fused with pressure and button information from the stylus to provide a greater range of expression than with the touch screen alone. Your app can listen for stylus button presses and perform secondary actions, by registering[View.OnContextClickListener](https://developer.android.com/reference/android/view/View.OnContextClickListener)and[GestureDetector.OnContextClickListener](https://developer.android.com/reference/android/view/GestureDetector.OnContextClickListener)objects in your activity.

Use the[MotionEvent](https://developer.android.com/reference/android/view/MotionEvent)methods and constants to detect stylus button interactions:

- If the user touches a stylus with a button on the screen of your app, the[getTooltype()](https://developer.android.com/reference/android/view/MotionEvent#getToolType(int))method returns[TOOL_TYPE_STYLUS](https://developer.android.com/reference/android/view/MotionEvent#TOOL_TYPE_STYLUS).
- For apps targeting Android 6.0 (API level 23), the[getButtonState()](https://developer.android.com/reference/android/view/MotionEvent#getButtonState())method returns[BUTTON_STYLUS_PRIMARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_STYLUS_PRIMARY)when the user presses the primary stylus button. If the stylus has a second button, the same method returns[BUTTON_STYLUS_SECONDARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_STYLUS_SECONDARY)when the user presses it. If the user presses both buttons simultaneously, the method returns both values OR'ed together ([BUTTON_STYLUS_PRIMARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_STYLUS_PRIMARY)\|[BUTTON_STYLUS_SECONDARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_STYLUS_SECONDARY)).
- For apps targeting a lower platform version, the[getButtonState()](https://developer.android.com/reference/android/view/MotionEvent#getButtonState())method returns[BUTTON_SECONDARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_SECONDARY)(for primary stylus button press),[BUTTON_TERTIARY](https://developer.android.com/reference/android/view/MotionEvent#BUTTON_TERTIARY)(for secondary stylus button press), or both.

## Improved Bluetooth Low Energy Scanning

If your app performs performs Bluetooth Low Energy scans, use the new[setCallbackType()](https://developer.android.com/reference/android/bluetooth/le/ScanSettings.Builder#setCallbackType(int))method to specify that you want the system to notify callbacks when it first finds, or sees after a long time, an advertisement packet matching the set[ScanFilter](https://developer.android.com/reference/android/bluetooth/le/ScanFilter). This approach to scanning is more power-efficient than what's provided in the previous platform version.

## Hotspot 2.0 Release 1 Support

This release adds support for the Hotspot 2.0 Release 1 spec on Nexus 6 and Nexus 9 devices. To provision Hotspot 2.0 credentials in your app, use the new methods of the[WifiEnterpriseConfig](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig)class, such as[setPlmn()](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setPlmn(java.lang.String))and[setRealm()](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setRealm(java.lang.String)). In the[WifiConfiguration](https://developer.android.com/reference/android/net/wifi/WifiConfiguration)object, you can set the[FQDN](https://developer.android.com/reference/android/net/wifi/WifiConfiguration#FQDN)and the[providerFriendlyName](https://developer.android.com/reference/android/net/wifi/WifiConfiguration#providerFriendlyName)fields. The new[isPasspointNetwork()](https://developer.android.com/reference/android/net/wifi/ScanResult#isPasspointNetwork())method indicates if a detected network represents a Hotspot 2.0 access point.

## 4K Display Mode

The platform now allows apps to request that the display resolution be upgraded to 4K rendering on compatible hardware. To query the current physical resolution, use the new[Display.Mode](https://developer.android.com/reference/android/view/Display.Mode)APIs. If the UI is drawn at a lower logical resolution and is upscaled to a larger physical resolution, be aware that the physical resolution the[getPhysicalWidth()](https://developer.android.com/reference/android/view/Display.Mode#getPhysicalWidth())method returns may differ from the logical resolution reported by[getSize()](https://developer.android.com/reference/android/view/Display#getSize(android.graphics.Point)).

You can request the system to change the physical resolution in your app as it runs, by setting the[preferredDisplayModeId](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#preferredDisplayModeId)property of your app's window. This feature is useful if you want to switch to 4K display resolution. While in 4K display mode, the UI continues to be rendered at the original resolution (such as 1080p) and is upscaled to 4K, but[SurfaceView](https://developer.android.com/reference/android/view/SurfaceView)objects may show content at the native resolution.

## Themeable ColorStateLists

Theme attributes are now supported in[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList)for devices running on Android 6.0 (API level 23). The[Resources.getColorStateList()](https://developer.android.com/reference/android/content/res/Resources#getColorStateList(int))and[Resources.getColor()](https://developer.android.com/reference/android/content/res/Resources#getColor(int))methods have been deprecated. If you are calling these APIs, call the new[Context.getColorStateList()](https://developer.android.com/reference/android/content/Context#getColorStateList(int))or[Context.getColor()](https://developer.android.com/reference/android/content/Context#getColor(int))methods instead. These methods are also available in the v4 appcompat library via[ContextCompat](https://developer.android.com/reference/android/support/v4/content/ContextCompat).

## Audio Features

This release adds enhancements to audio processing on Android, including:

- Support for the[MIDI](https://en.wikipedia.org/wiki/MIDI)protocol, with the new[android.media.midi](https://developer.android.com/reference/android/media/midi/package-summary)APIs. Use these APIs to send and receive MIDI events.
- New[AudioRecord.Builder](https://developer.android.com/reference/android/media/AudioRecord.Builder)and[AudioTrack.Builder](https://developer.android.com/reference/android/media/AudioTrack.Builder)classes to create digital audio capture and playback objects respectively, and configure audio source and sink properties to override the system defaults.
- API hooks for associating audio and input devices. This is particularly useful if your app allows users to start a voice search from a game controller or remote control connected to Android TV. The system invokes the new[onSearchRequested()](https://developer.android.com/reference/android/app/Activity#onSearchRequested(android.view.SearchEvent))callback when the user starts a search. To determine if the user's input device has a built-in microphone, retrieve the[InputDevice](https://developer.android.com/reference/android/view/InputDevice)object from that callback, then call the new[hasMicrophone()](https://developer.android.com/reference/android/view/InputDevice#hasMicrophone())method.
- New[getDevices()](https://developer.android.com/reference/android/media/AudioManager#getDevices(int))method which lets you retrieve a list of all audio devices currently connected to the system. You can also register an[AudioDeviceCallback](https://developer.android.com/reference/android/media/AudioDeviceCallback)object if you want the system to notify your app when an audio device connects or disconnects.

## Video Features

This release adds new capabilities to the video processing APIs, including:

- New[MediaSync](https://developer.android.com/reference/android/media/MediaSync)class which helps applications to synchronously render audio and video streams. The audio buffers are submitted in non-blocking fashion and are returned via a callback. It also supports dynamic playback rate.
- New[EVENT_SESSION_RECLAIMED](https://developer.android.com/reference/android/media/MediaDrm#EVENT_SESSION_RECLAIMED)event, which indicates that a session opened by the app has been reclaimed by the resource manager. If your app uses DRM sessions, you should handle this event and make sure not to use a reclaimed session.
- New[ERROR_RECLAIMED](https://developer.android.com/reference/android/media/MediaCodec.CodecException#ERROR_RECLAIMED)error code, which indicates that the resource manager reclaimed the media resource used by the codec. With this exception, the codec must be released, as it has moved to terminal state.
- New[getMaxSupportedInstances()](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities#getMaxSupportedInstances())interface to get a hint for the max number of the supported concurrent codec instances.
- New[setPlaybackParams()](https://developer.android.com/reference/android/media/MediaPlayer#setPlaybackParams(android.media.PlaybackParams))method to set the media playback rate for fast or slow motion playback. It also stretches or speeds up the audio playback automatically in conjunction with the video.

## Camera Features

This release includes the following new APIs for accessing the camera's flashlight and for camera reprocessing of images:

### Flashlight API

If a camera device has a flash unit, you can call the[setTorchMode()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#setTorchMode(java.lang.String, boolean))method to switch the flash unit's torch mode on or off without opening the camera device. The app does not have exclusive ownership of the flash unit or the camera device. The torch mode is turned off and becomes unavailable whenever the camera device becomes unavailable, or when other camera resources keeping the torch on become unavailable. Other apps can also call[setTorchMode()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#setTorchMode(java.lang.String, boolean))to turn off the torch mode. When the last app that turned on the torch mode is closed, the torch mode is turned off.

You can register a callback to be notified about torch mode status by calling the[registerTorchCallback()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#registerTorchCallback(android.hardware.camera2.CameraManager.TorchCallback, android.os.Handler))method. The first time the callback is registered, it is immediately called with the torch mode status of all currently known camera devices with a flash unit. If the torch mode is turned on or off successfully, the[onTorchModeChanged()](https://developer.android.com/reference/android/hardware/camera2/CameraManager.TorchCallback#onTorchModeChanged(java.lang.String, boolean))method is invoked.

### Reprocessing API

The[Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary)API is extended to support YUV and private opaque format image reprocessing. To determine if these reprocessing capabilities are available, call[getCameraCharacteristics()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics(java.lang.String))and check for the[REPROCESS_MAX_CAPTURE_STALL](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#REPROCESS_MAX_CAPTURE_STALL)key. If a device supports reprocessing, you can create a reprocessable camera capture session by calling[`createReprocessableCaptureSession()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createReprocessableCaptureSession(android.hardware.camera2.params.InputConfiguration, java.util.List<android.view.Surface>, android.hardware.camera2.CameraCaptureSession.StateCallback, android.os.Handler)), and create requests for input buffer reprocessing.

Use the[ImageWriter](https://developer.android.com/reference/android/media/ImageWriter)class to connect the input buffer flow to the camera reprocessing input. To get an empty buffer, follow this programming model:

1. Call the[dequeueInputImage()](https://developer.android.com/reference/android/media/ImageWriter#dequeueInputImage())method.
2. Fill the data into the input buffer.
3. Send the buffer to the camera by calling the[queueInputImage()](https://developer.android.com/reference/android/media/ImageWriter#queueInputImage(android.media.Image))method.

If you are using a[ImageWriter](https://developer.android.com/reference/android/media/ImageWriter)object together with an[PRIVATE](https://developer.android.com/reference/android/graphics/ImageFormat#PRIVATE)image, your app cannot access the image data directly. Instead, pass the[PRIVATE](https://developer.android.com/reference/android/graphics/ImageFormat#PRIVATE)image directly to the[ImageWriter](https://developer.android.com/reference/android/media/ImageWriter)by calling the[queueInputImage()](https://developer.android.com/reference/android/media/ImageWriter#queueInputImage(android.media.Image))method without any buffer copy.

The[ImageReader](https://developer.android.com/reference/android/media/ImageReader)class now supports[PRIVATE](https://developer.android.com/reference/android/graphics/ImageFormat#PRIVATE)format image streams. This support allows your app to maintain a circular image queue of[ImageReader](https://developer.android.com/reference/android/media/ImageReader)output images, select one or more images, and send them to the[ImageWriter](https://developer.android.com/reference/android/media/ImageWriter)for camera reprocessing.

## Android for Work Features

This release includes the following new APIs for Android for Work:

- **Enhanced controls for Corporate-Owned, Single-Use devices:** The Device Owner can now control the following settings to improve management of Corporate-Owned, Single-Use (COSU) devices:
  - Disable or re-enable the keyguard with the[setKeyguardDisabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setKeyguardDisabled(android.content.ComponentName, boolean))method.
  - Disable or re-enable the status bar (including quick settings, notifications, and the navigation swipe-up gesture that launches Google Now) with the[setStatusBarDisabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setStatusBarDisabled(android.content.ComponentName, boolean))method.
  - Disable or re-enable safe boot with the[UserManager](https://developer.android.com/reference/android/os/UserManager)constant[DISALLOW_SAFE_BOOT](https://developer.android.com/reference/android/os/UserManager#DISALLOW_SAFE_BOOT).
  - Prevent the screen from turning off while plugged in with the[STAY_ON_WHILE_PLUGGED_IN](https://developer.android.com/reference/android/provider/Settings.Global#STAY_ON_WHILE_PLUGGED_IN)constant.
- **Silent install and uninstall of apps by Device Owner:** A Device Owner can now silently install and uninstall applications using the[PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller)APIs, independent of Google Play for Work. You can now provision devices through a Device Owner that fetches and installs apps without user interaction. This feature is useful for enabling one-touch provisioning of kiosks or other such devices without activating a Google account.
- **Silent enterprise certificate access:** When an app calls[choosePrivateKeyAlias()](https://developer.android.com/reference/android/security/KeyChain#choosePrivateKeyAlias(android.app.Activity, android.security.KeyChainAliasCallback, java.lang.String[], java.security.Principal[], java.lang.String, int, java.lang.String)), prior to the user being prompted to select a certificate, the Profile or Device Owner can now call the[onChoosePrivateKeyAlias()](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onChoosePrivateKeyAlias(android.content.Context, android.content.Intent, int, android.net.Uri, java.lang.String))method to provide the alias silently to the requesting application. This feature lets you grant managed apps access to certificates without user interaction.
- **Auto-acceptance of system updates.** By setting a system update policy with[setSystemUpdatePolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setSystemUpdatePolicy(android.content.ComponentName, android.app.admin.SystemUpdatePolicy)), a Device Owner can now auto-accept a system update, for instance in the case of a kiosk device, or postpone the update and prevent it being taken by the user for up to 30 days. Furthermore, an administrator can set a daily time window in which an update must be taken, for example during the hours when a kiosk device is not in use. When a system update is available, the system checks if the device policy controller app has set a system update policy, and behaves accordingly.
- **Delegated certificate installation:** A Profile or Device Owner can now grant a third-party app the ability to call these[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)certificate management APIs:
  - [getInstalledCaCerts()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getInstalledCaCerts(android.content.ComponentName))
  - [hasCaCertInstalled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#hasCaCertInstalled(android.content.ComponentName, byte[]))
  - [installCaCert()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installCaCert(android.content.ComponentName, byte[]))
  - [uninstallCaCert()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#uninstallCaCert(android.content.ComponentName, byte[]))
  - [uninstallAllUserCaCerts()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#uninstallAllUserCaCerts(android.content.ComponentName))
  - [installKeyPair()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#installKeyPair(android.content.ComponentName, java.security.PrivateKey, java.security.cert.Certificate, java.lang.String))
![Mobile displaying the work status notification feature within Android for Work](https://developer.android.com/static/images/android-6.0/work-profile-screen.png)
- **Data usage tracking.** A Profile or Device Owner can now query for the data usage statistics visible in**Settings \> Data** usage by using the new[NetworkStatsManager](https://developer.android.com/reference/android/app/usage/NetworkStatsManager)methods. Profile Owners are automatically granted permission to query data on the profile they manage, while Device Owners get access to usage data of the managed primary user.
- **Runtime permission management:**

  A Profile or Device Owner can set a permission policy for all runtime requests of all applications using[setPermissionPolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermissionPolicy(android.content.ComponentName, int)), to either prompt the user to grant the permission or automatically grant or deny the permission silently. If the latter policy is set, the user cannot modify the selection made by the Profile or Device Owner within the app's permissions screen in**Settings**.
- **VPN in Settings:** VPN apps are now visible in**Settings \> More \> VPN**. Additionally, the notifications that accompany VPN usage are now specific to how that VPN is configured. For Profile Owner, the notifications are specific to whether the VPN is configured for a managed profile, a personal profile, or both. For a Device Owner, the notifications are specific to whether the VPN is configured for the entire device.
- **Work status notification:**A status bar briefcase icon now appears whenever an app from the managed profile has an activity in the foreground. Furthermore, if the device is unlocked directly to the activity of an app in the managed profile, a toast is displayed notifying the user that they are within the work profile.