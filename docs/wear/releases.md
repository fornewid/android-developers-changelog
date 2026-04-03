---
title: https://developer.android.com/wear/releases
url: https://developer.android.com/wear/releases
source: md.txt
---

# Wear OS release notes

This page contains information about Wear OS releases, such as the Wearable SDK and Wearable Support Library.
| **Note:** The Wearable Support Library doesn't send user data to a backend service of any kind. Integrating the Wearable Support Library into your app has no impact on your app's Data safety form in the Play console. For more information, see[Review how your app collects and shares user data](https://developer.android.com/guide/topics/data/collect-share).

## 2024-November-21 Wearable SDK 19.0.0

Wearable SDK version 19.0.0 includes minor SDK updates. Updates include:

- Updated library dependencies to latest versions.
- Removed an unsupported`sendMessage()`API variant that included a`MessageOptions`parameter.

## 2023-August-31 Wearable SDK 18.1.0

Wearable SDK version 18.1.0 includes minor API updates to support the next Wearable Support Library release. Updates include:

- Phone Switching Support, see[`NodeClient.OnNodeMigratedListener`](https://developers.google.com/android/reference/com/google/android/gms/wearable/NodeClient)for more details.
- Additional documentation for[`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient)send and reply messaging.
- Updated links in API descriptions.

## 2022-September-20 Wearable SDK 18.0.0

Wearable SDK version 18.0.0 includes minor API updates to support the next Wearable Support Library release. Updates include:

- `WearableListenerService`support for apps targeting Android 13---issue[235538840](https://issuetracker.google.com/235538840).
- New`MessageClient.sendRequest()`method.

## 2022-February-16 Wearable Support Library v2.9.0

Version 2.9.0 of the Wearable Support Library deprecates all remaining classes. Use the[Wear OS Jetpack libraries](https://developer.android.com/jetpack/androidx/releases/wear)instead.

## 2021-October-29 Wear OS Jetpack Library

The[Wear OS Jetpack libraries](https://developer.android.com/jetpack/androidx/releases/wear)are replacements for the Wearable Support Libraries, and they aren't designed to be used together. The Wearable Support Library does not work on Wear OS 3.

## 2021-April-27 Wearable SDK 17.1.0

Wearable SDK version 17.1.0 includes minor API updates to support the next Wearable Support Library release.

## 2020-September-28 Wearable Support Library v2.8.1

Version 2.8.1 of the Wearable Support Library includes the following change.

### Permit disabling of Jetifier when using the Watch Face template

The Android Studio Watch Face template now uses AndroidX dependencies to permit Jetifier to be disabled. These fixes apply when using the Watch Face template with Android Studio 4.2 or higher.

## 2020-September-24 Wearable Support Library v2.8.0

Version 2.8.0 of the Wearable Support Library includes the following changes.

### Fallback capability for specifying default non-system complication providers

Watch faces can now use`setDefaultComplicationProviderWithFallbacks`to specify one or more non-system complication providers to be used by default. If none of the specified non-system providers are installed, the system falls back to using the default system provider.

### WearableActivity deprecated

[`WearableActivity`](https://developer.android.com/reference/android/support/wearable/activity/WearableActivity)is deprecated. Use[`AmbientModeSupport`](https://developer.android.com/reference/androidx/wear/ambient/AmbientModeSupport)instead.

### SKIP_CONFIRMATION_UI deprecated

[`ActionConfirmationActivity.SKIP_CONFIRMATION_UI`](https://developer.android.com/reference/android/support/wearable/input/RemoteInputIntent)is deprecated. This extra has been unused since the release of Wear 2.0.

## 2020-May-15 Wearable Support Library v2.7.0

Version 2.7.0 of the Wearable Support Library includes the following feature.

### Hardware acceleration for watch faces

You can now ask for a hardware-accelerated canvas when using the`CanvasWatchFaceService`class. Take advantage of hardware acceleration to improve the performance of your watch face and to access more UI performance data.

For more information, see[Improve your watch face performance with hardware acceleration](https://developer.android.com/training/wearables/watch-faces/hardware-acceleration).

## 2020-April-21 Wearable Support Library v2.6.0

Version 2.6.0 of the Wearable Support Library includes the following improvement.

### Migration to Android Jetpack

The Wearable Support Library has been migrated to[Android Jetpack](https://developer.android.com/jetpack). Existing libraries are now mapped and accessible in[AndroidX](https://developer.android.com/jetpack/androidx)using the`androidx`namespace, and all dependencies on the[deprecated Support Library](https://developer.android.com/topic/libraries/support-library)have been removed.

This change also lets you use the Wearable Support libraries in Android Studio 4.0 and higher, which resolves issues like[issue #147972079](https://issuetracker.google.com/147972079).

## 2019-August-28 Wearable Support Library v2.5.0

Version 2.5.0 of the Wearable Support Library includes the following improvement.

### Fix for Complication Drawable when TYPE_NO_PERMISSION complication type is used

[`ComplicationDrawable`](https://developer.android.com/reference/android/support/wearable/complications/rendering/ComplicationDrawable)now includes a`NEW_TASK`flag that ensures that`startActivity()`calls that originate from a[`WatchFaceService`](https://developer.android.com/reference/android/support/wearable/watchface/WatchFaceService)include[`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)to avoid an`android.util.AndroidRuntimeException`.

This change lets the[`TYPE_NO_PERMISSION`](https://developer.android.com/reference/android/support/wearable/complications/ComplicationData#TYPE_NO_PERMISSION)complication type properly launch the permission request activity rather than crashing the watch face.

## 2018-September-25 Wearable SDK 16.0.0

Wearable SDK version 16.0.0 lowers the required version of Google Play services from version 12.4 to version 8.6. This change lets existing apps update to the latest version of the Wearable SDK without requiring an update to the Google Play services APK.

## 2018-June-11 Update to Wear OS Developer Preview 2

A recent[over-the-air](https://source.android.com/devices/tech/ota)update to the[Wear OS Developer Preview 2](https://developer.android.com/wear/releases#May-8-2018-release)has re-enabled alarms and jobs for background apps.

While this policy change supports increased flexibility in app development, background alarms and jobs continue to be subject to other Android P restrictions, including the ones that pertain to[App Standby Buckets](https://developer.android.com/about/versions/pie/power#buckets). Follow the[best practices](https://developer.android.com/about/versions/pie/power#buckets)to ensure your apps behave well, whichever bucket the apps are in.

This update also strengthens[user input and data privacy](https://developer.android.com/about/versions/pie/android-9.0-changes-all#bg-sensor-access)by limiting a background app's access to user input and sensor data. Depending on an app's requirements, you might need to use a foreground service to enable continual access to sensor data.

## 2018-May-8 Wear OS Developer Preview 2

Wear OS Developer Preview 2 has features such as an[improved Google Assistant experience](https://developer.android.com/wear/releases#google-assistant-on-wear).

Submit any bugs or feedback using the[Wear OS by Google issue tracker](https://issuetracker.google.com/issues/new?component=192711&template=840908). The earlier you submit them, the higher the likelihood that the fixes are included in the final release.

### Known issues

This section contains known issues for the Preview 2 release.

#### Issues for the Wear OS image

- When you are in any app and you press the power button on the side of the watch, you might be returned to the previous screen rather than to the watch face.

#### Issues for the Wear OS for China image

- When you are in any app and you press the power button on the side of the watch, you might be returned to the previous screen rather than to the watch face.

- Volume-related sound settings are not persisted. For example, an incoming call results in audible rings on the watch, even if the sound on the watch is set to off. And if you adjust the Alarm Volume, the change has no effect.

- Multiple ongoing notifications might not display correctly. For example, if both a timer and a stopwatch are set, notifications are not displayed. We recommend that you test your app with one ongoing notification rather than with more than one.

- The Wear app store in the China version does not work. Developers can't update or install new apps using that channel. We recommend using`adb`as a workaround to side-load your application for testing.

#### Issues for the Wear emulator

- An incoming phone call to a companion phone is not shown, or*mirrored*, as an incoming call in the paired emulator.

- When you use the[SDK manager](https://developer.android.com/tools/help/sdk-manager)to install or confirm that you have the latest installation of Android P or the China version, the checkboxes next to those selections can become unselected after you select them. If they become unselected, select them a second time.

- When the emulator performs a cold boot, the following error might be displayed: "There's an internal problem with your device. Contact the manufacturer for details." This does not affect functionality. Click**OK**to begin testing your app.

- Voice reply might not work on the emulator. For example, if you receive a notification for a Google Hangouts message on the Wear emulator and you try to reply to the message by voice, a "Google keeps stopping" error message occurs and you are prevented from replying by voice.

- Instant Run might be incompatible with the Wear emulator.

- Taking a screenshot programmatically, such as using`adb`or by taking a bug report, might not work. As a workaround, click the camera button on the emulator toolbar to capture a screenshot.

#### Issues for the China version of the Wear emulator

- An incoming phone call to a companion phone might not be shown, or*mirrored*, as an incoming call in the paired emulator. Accordingly, notifications of missed calls might not be shown in the emulator. Additionally, you might not be able to answer a call from the emulator, in which case the call continues to ring.

- When you use the[SDK manager](https://developer.android.com/tools/help/sdk-manager)to install or confirm that you have the latest installation of Android P or the China version, the checkboxes next to those selections can become unselected after you select them. If they become unselected, select them a second time.

- When the emulator performs a cold boot, the following error might display: "There's an internal problem with your device. Contact the manufacturer for details." This does not affect functionality. Click**OK**to begin testing your app.

- Instant Run might be incompatible with the Wear emulator.

- Taking a screenshot programmatically, such as using`adb`or by taking a bug report, might not work. As a workaround, click the camera button on the emulator toolbar to capture a screenshot.

### Google Assistant on Wear

Enhanced support for the Assistant on Wear OS lets you build a wearable-ready experience without writing Android code. Specifically, you can build for the Actions on Google platform, helping your users get things done with your products and services.

Additionally, Wear OS now supports faster interactions by voice and touch. Suggestion chips are also supported. They do the following:

- Help users complete interactions quickly

- Give users hints about your Action's capability

Moreover, Wear OS now supports more visual cards, as well as lists and carousels.

Thus, you can use[`DialogFlow`](https://developers.google.com/actions/dialogflow/first-app),[templates](https://developers.google.com/actions/templates/first-app), or the[Actions SDK](https://developers.google.com/actions/sdk/create-a-project)to create Actions on Google for Wear OS. You can also take advantage of new response templates that are specific to a watch. Best practices for Actions on Google include:

- Short, concise dialog

- Enabling both visual and vocal feedback

These enhancements for the Assistant on Wear OS don't depend on Android P and are rolling out to all Wear 2.0 users. For an introduction to building Actions on Google, see[Integrate with Google Assistant](https://developers.google.com/actions/extending-the-assistant).

### Battery Savings in Developer Preview 2

As described in the following in section, power-related features are available to increase battery life. The information in this Developer Preview 2 section supersedes the power-related information for Developer Preview 1.

#### New mode: Enhanced battery saver

While a watch is in the enhanced battery saver mode, a default power-optimised watch face displays. All of the following are turned off:

- Radios

- The touchscreen

- The tilt-to-wake feature

Users can see the time by short-pressing the side button. A long press lets the user switch back to a fully operational mode and perform tasks, such as paying with NFC or replying to a message. Assume that apps, watch faces, and complication data providers are unavailable in enhanced battery saver mode.

#### Limited background activity

To improve power management, apps in the background can no longer start alarms and jobs unless the watch is on the charger. Exceptions include watch faces and active complications.
| **Note:** If your app must always run, such as for background monitoring, we recommend that you use a foreground service by using the[`startForegroundService()`](https://developer.android.com/reference/android/content/Context#startForegroundService(android.content.Intent))method. See[Background service limitations](https://developer.android.com/about/versions/oreo/background#services)for more details. Using a foreground service is appropriate for exceptional use cases such as health monitoring.

### Improved app compatibility

To improve app compatibility, Android P has begun implementing certain[restrictions on the use of non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#determine-list). Make plans to migrate away from non-SDK methods and fields. If no public equivalent is available for your use case,[let us know](https://issuetracker.google.com/issues/new?component=328403&template=1027267).

### Dark UI system theme

Since the beginning of 2018, Wear OS has switched to a default UI theme that has a darker background for the notifications stream and system launcher. This change is intended to improve glanceability for your apps; check your app's accessibility with this new UI theme.

### Updated codelabs are available

To help you explore important ways to develop with Wear OS, updated[codelabs](https://codelabs.developers.google.com/)are available. For example, try the new Kotlin-based watch face codelab to experiment with Kotlin domain-specific language, or DSL.

## 2018-March-27 Wear OS Developer Preview 1

This section contains information about Developer Preview 1 of Wear OS by Google. Several updates to this preview are expected before the final production release. Submit any bugs you find using the[Wear OS by Google issue tracker](https://issuetracker.google.com/issues/new?component=192711&template=840908). The earlier you submit them, the higher the likelihood that we can include the fixes in the final release.

#### Known issues

- In the Wear OS companion app, tapping**Report wearable bug** appears to work, but no bug report is actually generated. Use`adb bugreport`as a workaround.
- Accepting a phone call using the watch does not always succeed. If it does not succeed, the user needs to accept the call from the phone directly.
- A "Detected problems with API compatibility" error sometimes appears after pairing or launching a preloaded app. That error message disappears after a short time and does not impact usability.
- In the Settings menu on the watch and in the emulator, the**Take bug report**option displays twice. To take a bug report, try using each of the two options, because only one is functional. When you tap the functional option, a toast displays, showing that a bug report is being generated.
- In the China version, voice input causes an app to crash. For example, this occurs with voice search or when you use voice to add a reminder because this functionality uses voice input APIs. For testing, use keyboard or handwriting input instead of voice input.
- The Wear app store in the China version does not work. Developers can't update or install new apps using that channel. We recommend using`adb`as a workaround to side-load your application for testing.

### Highlights in this developer preview

Developer Preview 1 includes the following features for app testing:

- **Limited background activity:** To improve power management, apps in the background can no longer use alarms and jobs. Exceptions include watch faces and complications that the user has selected. This feature will be rolled out gradually in the developer previews, so you might not see it immediately on your watch. Note: If your app must always run, modify it to make it a foreground service using the[`startForegroundService()`](https://developer.android.com/reference/android/content/Context#startForegroundService(android.content.Intent))method. See[Background service limitations](https://developer.android.com/about/versions/oreo/background#services)for further details.
- **Restrictions on apps' use of non-SDK interfaces:** To improve app compatibility, Android P has begun implementing certain[restrictions on the use of non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#determine-list). Make plans to migrate away from non-SDK methods and fields. If no public equivalent is available for your use case,[let us know](https://issuetracker.google.com/issues/new?component=328403&template=1027267).
- **Dark UI system theme:**Since the beginning of 2018, Wear OS has switched to a default UI theme that has a darker background for the notifications stream and system launcher. This change is intended to improve glanceability for your apps; check your app's accessibility with this new UI theme.
- **Radios are off when the watch is off the body** : To improve power management, the Bluetooth radio, Wi-Fi radio, and cellular radio are off when the watch is detected as off the body for an extended period. This feature will be rolled out gradually in the developer previews, so you might not initially see it on your watch. If this feature causes challenges in your development process, you can disable the feature using`adb`using the following command:`adb shell settings put global
  off_body_radios_off_for_small_battery_enabled 0`
- **Wi-Fi is off when Bluetooth is disconnected:**To improve power management, the watch no longer automatically connects to Wi-Fi when the watch disconnects from Bluetooth. Exceptions include the case of an app requesting a high bandwidth network, and the case of the watch attached to a charger. This feature will be rolled out gradually in the developer previews, so you might not initially see it on your watch.

### Updates to the Wearable Support Library, v2.3.0

The[v2.3.0 documentation update](https://developer.android.com/reference/android/support/wearable/classes)for the Wearable Support Library includes[rebranding](https://developer.android.com/wear/releases#rebrand-to-wear-os)updates.

Additionally, v2.3.0 of the library includes updates related to[`ComplicationDrawable`](https://developer.android.com/reference/android/support/wearable/complications/rendering/ComplicationDrawable)and[`TextRenderer`](https://developer.android.com/reference/android/support/wearable/complications/rendering/TextRenderer)for text that has markup objects attached to text ranges. These classes have improved handling of[spanned](https://developer.android.com/reference/android/text/Spanned)texts. Only a certain subset of spans can be rendered---see the[`setText`](https://developer.android.com/reference/android/support/wearable/complications/rendering/TextRenderer#setText(java.lang.CharSequence))method for the span types that can be drawn---so the spans don't look out-of-place when rendered in a watch face.

## 2018-March-15 Rebrand of Wear

This section contains information about Wear OS features.

### New name for Android Wear

Android Wear is renamed to Wear OS by Google.

## 2018-Feb-27 Ambient mode update

This section contains information about new Android Wear features.

### New class for supporting ambient mode

The[27.1.0 version](https://developer.android.com/topic/libraries/support-library/revisions)of the Android Support Library contains a new class,[`AmbientModeSupport`](https://developer.android.com/reference/androidx/wear/ambient/AmbientModeSupport), which replaces the now-deprecated[`AmbientMode`](https://developer.android.com/reference/androidx/wear/ambient/AmbientMode)class. Updates to samples are planned in upcoming weeks.

## 2018-Jan-25 Final emulator and more

This section contains information about new Android Wear features.

### Android Emulator: Update for Wear

The final Wear-related update to the[Android emulator](https://developer.android.com/studio/run/emulator)is available for testing apps based on API version 26.

### Enhancements in the Wearable Support Library, v2.2.0

The[2.2.0 version](https://developer.android.com/reference/android/support/wearable/classes)of the Wearable Support Library includes the updates described in the following section.

#### A new unread notification indicator

Because users want to be aware of unread notifications, a new indicator is provided: a circled dot at the bottom of the watch face. If you prefer to manage notifications on your own, you can use[`setHideNotificationIndicator`](https://developer.android.com/reference/android/support/wearable/watchface/WatchFaceStyle.Builder#setHideNotificationIndicator(boolean))to hide the default indicator and display your own or[`setShowUnreadCountIndicator`](https://developer.android.com/reference/android/support/wearable/watchface/WatchFaceStyle.Builder#setShowUnreadCountIndicator(boolean))to display a notification count in the status bar.

Customize the color of the outer ring of the unread notification indicator with the[`setAccentColor`](https://developer.android.com/reference/android/support/wearable/watchface/WatchFaceStyle.Builder#setAccentColor(int))method.
| **Note:** The unread notifications indicator is not enabled in the production version of Wear 2.8.0. Test your implementation using the latest Wear emulator instead. Starting with the next consumer release of Wear (version 2.9.0), the unread notifications indicator will be displayed by default.

#### Enhancements to the ComplicationDrawable class

The[`ComplicationDrawable`](https://developer.android.com/reference/android/support/wearable/complications/rendering/ComplicationDrawable)class starts a permission request for a watch face that is tapped when the system indicates a value of[`TYPE_NO_PERMISSION`](https://developer.android.com/reference/android/support/wearable/complications/ComplicationData#TYPE_NO_PERMISSION), indicating that the watch face lacks permission to get the complication data.

Additionally, the`ComplicationDrawable`class invalidates itself when it finishes loading images or when a tap highlight expires. To respond to this invalidation---such as to redraw your watch face---add a[`Drawable.Callback`](https://developer.android.com/reference/android/graphics/drawable/Drawable.Callback).

### Known issues

- If you activate Theater mode in the emulator, as described in[Change screen \& brightness settings](https://support.google.com/androidwear/answer/6056890), the emulator can remain stuck on Theater mode. Fixing the issue requires clearing the emulator data; see[Run and stop an emulator and clear data](https://developer.android.com/studio/run/managing-avds#emulator).

- Within the window of an emulator for API level 25 or 26, the power button does not work. Use buttons other than the power button instead. Specifically, to switch to ambient mode---for example, as if a user covered the screen with their palm---use the power button on the emulator toolbar to the right of the display. To start the application launcher in interactive mode, use the Home button on the emulator toolbar.

- On the China version of the emulator, if you use the handwriting input method, the screen can begin flashing. Then, when you click the button for the on-screen keyboard, the keyboard blocks half the screen.

## 2017-Dec-18 New access to Google Play services

This section contains information about new Android Wear features.

### Migrate away from the GoogleApiClient class

Starting with[version 11.8.0](https://developers.google.com/android/guides/releases)of Google Play services, migrate your Wear apps away from the[`GoogleApiClient`](https://developers.google.com/android/guides/google-api-client)class and instead use API client objects that are based on the[`GoogleApi`](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApi)class and the[Tasks API](https://developers.google.com/android/guides/tasks).
| **Note:** This update does not apply to[Android Wear apps for China](https://developer.android.com/training/wearables/apps/creating-app-china), which generally use version 10.2.0 of Google Play services.

For more information, see the following:

- [Migrating Wear Apps to GoogleApi](https://developer.android.com/training/wearables/data-layer/migrate-to-googleapi)
- [Access Google APIs](https://developers.google.com/android/guides/api-client)
- [`Wearable`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Wearable)class documentation

#### New components for connecting with Google Play services

When you use classes that extend the[`GoogleApi`](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApi)class, such as[`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient)and[`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient), the Google Play services SDK manages connections to Google Play services for you. Apps that use these classes no longer need to create and manage[`GoogleApiClient`](https://developers.google.com/android/guides/google-api-client)objects. See the blog post[Moving Past GoogleApiClient](https://android-developers.googleblog.com/2017/11/moving-past-googleapiclient_21.html)for more information.

For the replacements of Wear-related components for connecting to Google Play services, see[Replacements for deprecated components](https://developer.android.com/training/wearables/data-layer/migrate-to-googleapi#deprecation-table). For releases and known issues related to Google Play services, see the[Release Notes for Google Play services](https://developers.google.com/android/guides/releases).
| **Note:** If you compile your app with the latest version of Google Play services, users are prompted to update their devices to that latest version. However, a known issue for apps that target API version 26 might prevent users from being prompted to update their devices. This issue is described in the[Release Notes for Google Play services](https://developers.google.com/android/guides/releases).

## 2017-Oct-25 Ambient mode and more

This section contains information about new Android Wear features.

### Android Support Library, v27.0.0: Features and bug fixes

The[27.0.0 version](https://developer.android.com/topic/libraries/support-library/revisions)of the Android Support Library contains new features for Wear. Review the following section.

#### New, preferred way to support ambient mode

Ambient mode lets a Wear app remain visible to a user when the device goes idle. The Android Support Library has a new, preferred way for your apps to use ambient mode. The Wear team seeks[developer feedback](https://issuetracker.google.com/issues/new?component=192711&template=840908)about this significant change.

Specifically, using the[`AmbientMode`](https://developer.android.com/reference/androidx/wear/ambient/AmbientMode)class offers the following benefits:

- The[`Activity`](https://developer.android.com/reference/android/app/Activity)subclasses in the Android Support Library, such as[`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity). Functionality for support library fragments is available.

- [Architecture components](https://developer.android.com/topic/libraries/architecture), which are[lifecycle aware](https://developer.android.com/topic/libraries/architecture/lifecycle).

- Better support for[Google Sign-In](https://developers.google.com/identity/sign-in/android/sign-in).

#### Manifest metadata constants in the Android Support Library

Constants for Android Wear apps, used in the`meta-data`tag in the Android Manifest file, are now[available in the Android Support Library](https://developer.android.com/reference/androidx/wear/utils/MetadataConstants). To use the constants---for standalone apps, notification bridging mode, and watch face preview images---add a reference to the following in the dependencies section of the app module's`build.gradle`file, which requires the latest version of the Google Repository:

<br />

### Groovy

<br />

    implementation 'com.android.support:wear:27.0.0'

<br />

### Kotlin

<br />

    implementation("com.android.support:wear:27.0.0")

<br />

<br />

#### Action drawer updates

Updates are available to the[`WearableActionDrawerView`](https://developer.android.com/reference/androidx/wear/widget/drawer/WearableActionDrawerView)class, which is used for creating a wearable action drawer. In the latest version:

- When menu items are modified, the action drawer properly updates.

- If set for an action drawer, the title displays correctly.

#### Inflation of the RoundedDrawable class

Assuming an API level of at least 24, the[`RoundedDrawable`](https://developer.android.com/reference/androidx/wear/widget/RoundedDrawable)class can now be inflated from a drawable XML file; see[Custom drawables](https://developer.android.com/reference/android/graphics/drawable/Drawable#Custom).

### Wearable Support Library, v2.1.0: Enhancements and more

The[2.1.0 version](https://developer.android.com/reference/android/support/wearable/classes)of the Wearable Support Library includes the updates described in the following section, and requires Android Support Library version 26.0.2 or higher.

#### Supply burn-in-safe images for ambient mode

The[`ComplicationDrawable`](https://developer.android.com/reference/android/support/wearable/complications/rendering/ComplicationDrawable)class lets you supply burn-in-safe images for ambient mode. Specifically, a[`ComplicationData`](https://developer.android.com/reference/android/support/wearable/complications/ComplicationData)object's*burn-in protection small image* field lets a watch face display a small image in the`SMALL_IMAGE`complication type, in ambient mode, when burn-in protection is enabled.

#### Tap event updates for complications

The[`ComplicationDrawable`](https://developer.android.com/reference/android/support/wearable/complications/rendering/ComplicationDrawable)class has a new`onTap`method that lets your watch face pass tap events to complications. The new method builds on the existing functionality in which a tap on the watch face triggers the[`WatchFaceService.Engine.onTapCommand`](https://developer.android.com/reference/android/support/wearable/watchface/WatchFaceService.Engine#onTapCommand(int,int,%20int,%20long))method.

You can pass the coordinates to a`ComplicationDrawable`with an`onTap`call to launch the action associated with the`ComplicationDrawable`that contains the tap coordinates. When the new`onTap`method is called, you can use a return value of`true`to see whether a`ComplicationDrawable`launched the action associated with it.

Additionally, the`setHighlightDuration`method sets the duration for a complication to remain highlighted after the`onTap`method is called.

#### Progress bar for ranged value complications

If you prefer to draw your own progress bar for ranged value complications in your watch face, use the`setRangedValueProgressHidden`method of the`ComplicationDrawable`class to hide the ranged value progress that's drawn by the`ComplicationDrawable`.

## 2017-Oct-02 Android Wear beta

- Date: 2017-Oct-02
- Build: OWP4.170828.008
- Supported device: LG Watch Sport

This section contains known issues for an Android Wear beta release. For information about the beta program or to enroll, see the[Android beta page](https://www.google.com/android/beta).

### Known issues

- Google Pay and its cards don't function with this Android Wear beta release.
- Even if cellular connectivity is on, it is turned off after the beta is installed. As a workaround, turn on cellular connectivity after the beta is installed by navigating to**Settings \> Connectivity \> Cellular**.
- If notifications are erratic or missing after a beta update, or contacts were not synced, factory-reset your watch.
- In the Wear tutorial, which starts after a watch is set up, some cards behave erratically, but they can be dismissed normally with a swipe.
- On Android 6.0 phones, phone call notifications are not received on the watch.
- Heart rate monitoring sometimes fails after an update. As a workaround, reboot the watch.
- The OTA card in the stream sometimes fails to enable an installation. As a workaround, navigate to**Settings \> System \> About \> System Updates**