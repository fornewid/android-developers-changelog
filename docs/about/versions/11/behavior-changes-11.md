---
title: https://developer.android.com/about/versions/11/behavior-changes-11
url: https://developer.android.com/about/versions/11/behavior-changes-11
source: md.txt
---

Like earlier releases, Android 11 includes behavior changes that may
affect your app. The following behavior changes apply exclusively to apps
that are targeting Android 11 or higher. If your app sets
`targetSdkVersion` to `30`, you should modify your app to
support these behaviors properly, where applicable.

Be sure to also review the list of [behavior changes that affect all apps
running on Android 11](https://developer.android.com/about/versions/11/behavior-changes-all).

## Privacy

Android 11 introduces changes and restrictions to enhance user
privacy, including the following:

- **[Scoped storage enforcement](https://developer.android.com/about/versions/11/privacy/storage#scoped-storage):** Access into external storage directories is limited to an app-specific directory and specific types of media that the app has created.
- **[Permissions auto-reset](https://developer.android.com/about/versions/11/privacy/permissions#auto-reset):** If users haven't interacted with an app for a few months, the system auto-resets the app's sensitive permissions.
- **[Background location
  access](https://developer.android.com/about/versions/11/privacy/location#background-location):** Users must be directed to system settings in order to grant the background location permission to apps.
- **[Package visibility](https://developer.android.com/about/versions/11/privacy/package-visibility):** When an app queries for the list of installed apps on the device, the returned list is filtered.

To learn more, see the [Privacy](https://developer.android.com/about/versions/11/privacy) page.

## Security

### Heap pointer tagging

### Change details

**Change Name** : `NATIVE_HEAP_POINTER_TAGGING`

**Change ID** : `135754954`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (135754954|NATIVE_HEAP_POINTER_TAGGING) PACKAGE_NAME
    adb shell am compat disable (135754954|NATIVE_HEAP_POINTER_TAGGING) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

Heap pointers now have a non-zero tag in the most significant byte (MSB).
Applications that use pointers incorrectly, including those that modify the MSB,
can now crash or experience other issues. This change is necessary to support
future hardware with ARM Memory Tagging Extension (MTE) enabled. To learn more, see
[Tagged Pointers](https://source.android.com/devices/tech/debug/tagged-pointers).

To disable this feature, see the [`allowNativeHeapPointerTagging`](https://developer.android.com/guide/topics/manifest/application-element#allowNativeHeapPointerTagging)
manifest documentation.

### Updates to toasts

#### Custom toasts from the background are blocked

For security reasons and to maintain a good user experience, the system blocks
toasts that contain custom views if those toasts are sent from the background by
an app that targets Android 11 or higher. Note that text toasts
are still allowed; these are toasts created using
[`Toast.makeText()`](https://developer.android.com/reference/kotlin/android/widget/Toast#maketext) that
don't call [`setView()`](https://developer.android.com/reference/kotlin/android/widget/Toast#setview).

If your app tries to post a toast containing a custom view from the background
anyway, the system doesn't show the message to the user. Instead, the system
logs the following message in logcat:

```
W/NotificationService: Blocking custom toast from package \
  <package> due to package not in the foreground
```

#### Toast callbacks

If you want to be notified when a toast (text or custom) appears or disappears,
use the
[`addCallback()`](https://developer.android.com/reference/android/widget/Toast#addCallback(android.widget.Toast.Callback))
method, which was added in Android 11.

#### Text toast API changes

Apps that target Android 11 or higher see the following side
effects for text toasts:

- The [`getView()`](https://developer.android.com/reference/kotlin/android/widget/Toast#getview) method returns `null`.
- The return values of the following methods don't reflect the actual values, so you shouldn't rely on them in your app:
  - [`getHorizontalMargin()`](https://developer.android.com/reference/android/widget/Toast#getHorizontalMargin())
  - [`getVerticalMargin()`](https://developer.android.com/reference/android/widget/Toast#getVerticalMargin())
  - [`getGravity()`](https://developer.android.com/reference/android/widget/Toast#getGravity())
  - [`getXOffset()`](https://developer.android.com/reference/android/widget/Toast#getXOffset())
  - [`getYOffset()`](https://developer.android.com/reference/android/widget/Toast#getYOffset())
- The following methods are no-ops, so your app shouldn't use them:
  - [`setMargin()`](https://developer.android.com/reference/android/widget/Toast#setMargin(float,%20float))
  - [`setGravity()`](https://developer.android.com/reference/android/widget/Toast#setGravity(int,%20int,%20int))

## Connectivity

### Restricted read access to APN database

### Change details

**Change Name** : `APN_READING_PERMISSION_CHANGE_ID`

**Change ID** : `124107808`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (124107808|APN_READING_PERMISSION_CHANGE_ID) PACKAGE_NAME
    adb shell am compat disable (124107808|APN_READING_PERMISSION_CHANGE_ID) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

Apps that target Android 11 now require the
[`Manifest.permission.WRITE_APN_SETTINGS`](https://developer.android.com/reference/android/Manifest.permission#WRITE_APN_SETTINGS)
privileged permission to read or access the [Telephony](https://developer.android.com/reference/android/provider/Telephony)
provider APN database. Attempting to access the APN database without this
permission generates a security exception.

## Accessibility

### Declare interaction with TTS engines in manifest file

Because of changes to [package
visibility](https://developer.android.com/about/versions/11/privacy/package-visibility), apps that target
Android 11 and interact with a text-to-speech (TTS) engine need
to add the following `<queries>` element to their manifest files:

```xml
<queries>
  <intent>
    <action
       android:name="android.intent.action.TTS_SERVICE" />
  </intent>
</queries>
```

### Declare accessibility button usage in metadata file

### Change details

**Change Name** : `REQUEST_ACCESSIBILITY_BUTTON_CHANGE`

**Change ID** : `136293963`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (136293963|REQUEST_ACCESSIBILITY_BUTTON_CHANGE) PACKAGE_NAME
    adb shell am compat disable (136293963|REQUEST_ACCESSIBILITY_BUTTON_CHANGE) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

Starting in Android 11, your accessibility service cannot make
a runtime declaration that it has an [association with the system's
accessibility button](https://developer.android.com/guide/topics/ui/accessibility/service#button). If you
append `AccessibilityServiceInfo.FLAG_REQUEST_ACCESSIBILITY_BUTTON` to the
`flags` property of an `AccessibilityServiceInfo` object, the framework doesn't
pass accessibility button callback events to your service.

To receive accessibility callback events in your accessibility service, use your
accessibility service metadata file to declare your service's association with
the accessibility button. Include the `flagRequestAccessibilityButton` value in
your definition of the
[`accessibilityFlags`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityServiceInfo#android:accessibilityflags)
attribute. A common location for the accessibility service metadata file is
`res/raw/accessibilityservice.xml`.

## Camera

### Media intent actions require system default camera

Starting in Android 11, only pre-installed system camera apps can
respond to the following intent actions:

- [`android.media.action.VIDEO_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_VIDEO_CAPTURE)
- [`android.media.action.IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE)
- [`android.media.action.IMAGE_CAPTURE_SECURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE_SECURE)

If more than one pre-installed system camera app is available, the system
presents a dialog for the user to select an app. If you want your app to use a
specific third-party camera app to capture images or videos on its behalf, you
can make these intents explicit by setting a package name or component for the
intent.

## App packaging and installation

### Compressed resource files

### Change details

**Change Name** : `RESOURCES_ARSC_COMPRESSED`

**Change ID** : `132742131`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (132742131|RESOURCES_ARSC_COMPRESSED) PACKAGE_NAME
    adb shell am compat disable (132742131|RESOURCES_ARSC_COMPRESSED) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

Apps that target Android 11 (API level 30) or higher can't be installed if they
contain a *compressed* `resources.arsc` file or if this file is not aligned on
a 4-byte boundary. This file can't be memory-mapped by the system if either of
these conditions is present. Resources tables that can't be memory-mapped must
be read into a buffer in RAM, resulting in unnecessary memory pressure on the
system and greatly-increased RAM usage on the device.

If you were previously using a compressed `resources.arsc` file, try alternative
strategies instead, such as [shrinking app
resources](https://developer.android.com/studio/build/shrink-code#shrink-resources) or other methods to
[shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code).

### APK Signature Scheme v2 now required

Apps that target Android 11 (API level 30) that are currently only signed using
APK Signature Scheme v1 must now also be signed using [APK
Signature Scheme v2](https://source.android.com/security/apksigning/v2) or
higher. Users can't install or update apps that are only signed with APK
Signature Scheme v1 on devices that run Android 11.

To verify that your app is being signed with APK Signature Scheme v2 or higher,
you can use either [Android Studio](https://developer.android.com/studio/publish/app-signing#sign_release),
or the [`apksigner`](https://developer.android.com/studio/command-line/apksigner) tool on the command line.

> [!CAUTION]
> **Caution:** To support devices that run older versions of Android, you should continue to sign your APKs using APK Signature Scheme v1, in addition to signing your APK with APK Signature Scheme v2 or higher.

## Firebase

### Firebase JobDispatcher and GCMNetworkManager

If your app targets API level 30 or higher, Firebase
JobDispatcher and GcmNetworkManager API calls are disabled on devices
running Android 6.0 (API level 23) or higher. For migration information, see
[Migrating from Firebase JobDispatcher to
WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/migrating-fb) and
[Migrating from GCMNetworkManager to
WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager/migrating-gcm).

## Speech recognition

Because of changes to [package
visibility](https://developer.android.com/about/versions/11/privacy/package-visibility), apps that target
Android 11 and interact with a speech recognition service need
to add the following `<queries>` element to their manifest files:

```xml
<queries>
  <intent>
    <action
       android:name="android.speech.RecognitionService" />
  </intent>
</queries>
```

## Callback changes for OnSharedPreferenceChangeListener

### Change details

**Change Name** : `CALLBACK_ON_CLEAR_CHANGE`

**Change ID** : `119147584`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (119147584|CALLBACK_ON_CLEAR_CHANGE) PACKAGE_NAME
    adb shell am compat disable (119147584|CALLBACK_ON_CLEAR_CHANGE) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

For apps targeting Android 11 (API level 30), whenever
[`Editor.clear`](https://developer.android.com/reference/android/content/SharedPreferences.Editor#clear())
is called, a callback is now made to
[`OnSharedPreferenceChangeListener.onSharedPreferenceChanged`](https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener#onSharedPreferenceChanged(android.content.SharedPreferences,%20java.lang.String))
with a `null` key.

## Non-SDK interface restrictions

Android 11 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 11, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

To learn more about the changes in this release of Android, see [Updates to
non-SDK interface restrictions in Android 11](https://developer.android.com/about/versions/11/non-sdk-11). To learn more
about non-SDK interfaces generally, see [Restrictions on non-SDK
interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).