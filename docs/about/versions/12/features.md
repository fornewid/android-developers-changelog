---
title: https://developer.android.com/about/versions/12/features
url: https://developer.android.com/about/versions/12/features
source: md.txt
---

Android 12 introduces great new features and APIs for developers.
The sections below help you learn about features for your apps and get started
with the related APIs.

For a detailed list of new, modified, and removed APIs, read the [API diff
report](https://developer.android.com/sdk/api_diff/s-dp1/changes). For details on new APIs visit the [Android
API reference](https://developer.android.com/reference) --- new APIs are highlighted for visibility. Also, to
learn about areas where platform changes may affect your apps, be sure to check
out Android 12 behavior changes [for apps that target
Android 12](https://developer.android.com/about/versions/12/behavior-changes-12) and [for all
apps](https://developer.android.com/about/versions/12/behavior-changes-all).

## User experience

### Material You

Android 12 introduces a new design language called [Material
You](https://material.io/blog/announcing-material-you), helping you to build
more personalized, beautiful apps. To bring all of the latest Material Design 3
updates into your apps, try an alpha version of [Material Design
Components](https://github.com/material-components/material-components-android/releases).

![Material You](https://developer.android.com/static/images/about/versions/12/material-you.jpeg)

### Widgets improvements

Android 12 revamps the existing Widgets API to improve the user and developer
experience in the platform and launchers. We've created a guide to help you
ensure your widget is compatible with Android 12 and to refresh it with new
features.

See [Android 12 widgets improvements](https://developer.android.com/about/versions/12/features/widgets) for
more information.

### Rich content insertion

Android 12 introduces a new unified API that lets your app
receive rich content from any available source: clipboard, keyboard, or drag and
drop.

For more information, see [Receive rich
content](https://developer.android.com/guide/topics/input/receive-rich-content).

### App splash screens API

Android 12 introduces a new app launch animation for all apps that includes an
into-app motion from the point of launch, a splash screen showing the app icon,
and a transition to the app itself. See the [splash screens developer
guide](https://developer.android.com/guide/topics/ui/splash-screen) for more details.

### Rounded corner APIs

Android 12 introduces [`RoundedCorner`](https://developer.android.com/reference/android/view/RoundedCorner)
and [`WindowInsets.getRoundedCorner(int
position)`](https://developer.android.com/reference/android/view/WindowInsets#getRoundedCorner(int)),
which provide the radius and center point for rounded corners.

For more information, see [Rounded corners](https://developer.android.com/guide/topics/ui/look-and-feel/rounded-corners).

### Rich haptic experiences

Android 12 expands the tools for creating informative haptic feedback for UI
events, immersive and delightful effects for gaming, and attentional haptics for
productivity.

#### Actuator effects

Android 12 adds expressive effects like [low
tick](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_LOW_TICK) that
take advantage of the broader frequency bandwidth of the latest actuators. Game
developers can now access [multiple, different
actuators](https://developer.android.com/reference/android/os/VibratorManager) independently in game
controllers to deliver the same effect synchronously or different haptic effects
on multiple actuators. For developers, we recommend using the
[constants](https://developer.android.com/reference/android/view/HapticFeedbackConstants) and
[primitives](https://developer.android.com/reference/android/os/VibrationEffect.Composition#summary) as
building blocks for rich haptic effects - constants to enhance UI events and
[haptic composer](https://developer.android.com/reference/android/os/VibrationEffect.Composition) to sequence
primitives for more complex effects. These APIs are available to try on Pixel 4
devices, and we're continuing to work with our device-maker partners to bring
the latest in haptics support to users across the ecosystem.

#### Audio-coupled haptic effects

Android 12 apps can generate haptic feedback derived from an audio session using
the phone's vibrator. This provides an opportunity for more immersive game and
audio experiences. For example, haptic-enhanced ringtones can help identify
callers, or a driving game could simulate the feeling of rough terrain.

See the [`HapticGenerator`](https://developer.android.com/reference/android/media/audiofx/HapticGenerator)
reference documentation for more information.

### AppSearch

Android 12 introduces AppSearch, a high-performance on-device search engine,
as a system service. AppSearch allows applications to index structured data
and search over it with built-in full-text search capabilities. Furthermore,
AppSearch supports native search features, like highly-efficient indexing
and retrieval, multi-language support, and relevancy ranking.
![Diagram illustrating indexing and searching within AppSearch](https://developer.android.com/static/images/about/versions/12/appsearch.png)

AppSearch comes in two flavors: a local index for your application to use
that's compatible with older versions of Android, or a central index
maintained for the entire system in Android 12. Using the central index, your
application can allow its data to be displayed on system UI surfaces by the
system's pre-installed intelligence component. Exactly which data gets
displayed on system UI surfaces is dependent on the OEM. Additionally, your
application can securely share data with other applications, to allow them
to search over that data as well.

Learn more about AppSearch in the
[developer guide](https://developer.android.com/guide/topics/search/appsearch), and begin using it with
the [AppSearch Jetpack library](https://developer.android.com/jetpack/androidx/releases/appsearch), which
provides a developer-friendly API surface as well as annotation processor
support.

### Game Mode

The [Game Mode API](https://developer.android.com/games/gamemode/gamemode-api) and [Game Mode
interventions](https://developer.android.com/games/gamemode/gamemode-interventions) allow you to optimize
gameplay by prioritizing characteristics, such as performance or battery life
based on users settings or game specific configurations.

For more information, see [Game Mode](https://developer.android.com/games/gamemode).

### Picture-in-picture (PiP) recommendations and improvements

Android 12 introduces the following improvements for PiP mode:

#### Support for new PiP gestures

Android 12 now supports [stashing and pinch-to-zoom
gestures](https://developer.android.com/develop/ui/views/picture-in-picture#gestures) for the PiP
window:

- To stash the window, the user can drag the window to the left or right
  edge. To unstash the window, the user can either tap the visible part of
  the stashed window or drag it out.

- The user can now resize the PiP window using pinch-to-zoom.

#### Recommended new features that support a polished PiP transition experience

Android 12 added [significant cosmetic improvements](https://developer.android.com/develop/ui/views/picture-in-picture#smoother-transition)
to the animated
transitions between fullscreen and PiP windows. We strongly recommend
implementing all applicable changes; once you've done so, these changes
automatically scale to large screens such as foldables and tablets without
any further required work.

These features are the following:

- [A new API flag for smoother transition to PiP mode with gesture navigation](https://developer.android.com/develop/ui/views/picture-in-picture#setautoenterenabled)

  Use the [`setAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParamsBuilder#setAutoEnterEnabled(boolean))
  flag to provide smoother transitions to PiP mode when swiping up to home in
  gesture navigation mode. Previously, Android waited for the swipe-up-to-home
  animation to finish before fading in the PiP window.
- [Smoother animations when entering and exiting out of PiP mode](https://developer.android.com/develop/ui/views/picture-in-picture#set-sourcerecthint)

  The [`SourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect))
  flag is now reused to implement smoother animation when entering and exiting
  PiP mode.
- [A new API flag to disable seamless resizing for non-video content](https://developer.android.com/develop/ui/views/picture-in-picture#seamless-resizing)

  The [`SeamlessResizeEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSeamlessResizeEnabled(boolean))
  flag provides a much smoother cross-fading animation when resizing non-video
  content in the PiP window. Previously, resizing non-video content in a PiP
  window could create jarring visual artifacts.

### New phone call notifications allowing for ranking importance of incoming calls

Android 12 adds the new notification style
[`Notification.CallStyle`](https://developer.android.com/reference/android/app/Notification.CallStyle)
for phone calls. Using this template lets your app indicate the importance of
active calls by displaying a prominent chip that shows the time of the call in
the status bar; the user can tap this chip to return to their call.

Because incoming and ongoing calls are the most critical to users, these
notifications are given top ranking in the shade. This ranking also allows the
system to potentially forward these prioritized calls to other devices.

Implement the following code for all types of calls.

### Kotlin

```kotlin
// Create a new call with the user as caller.
val incoming_caller = Person.Builder()
    .setName("Jane Doe")
    .setImportant(true)
    .build()
```

### Java

```java
// Create a new call with the user as caller.
Person incoming_caller = new Person.Builder()
    .setName("Jane Doe")
    .setImportant(true)
    .build();
```

Use [`forIncomingCall()`](https://developer.android.com/reference/android/app/Notification.CallStyle#forIncomingCall(android.app.Person,%20android.app.PendingIntent,%20android.app.PendingIntent))
to create a call style notification for an incoming call.

### Kotlin

```kotlin
// Create a call style notification for an incoming call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forIncomingCall(caller, declineIntent, answerIntent))
    .addPerson(incoming_caller)
```

### Java

```java
// Create a call style notification for an incoming call.
Notification.Builder builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forIncomingCall(caller, declineIntent, answerIntent))
    .addPerson(incoming_caller);
```

Use [`forOngoingCall()`](https://developer.android.com/reference/android/app/Notification.CallStyle#forOngoingCall(android.app.Person,%20android.app.PendingIntent))
to create a call style notification for an ongoing call.

### Kotlin

```kotlin
// Create a call style notification for an ongoing call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forOnGoingCall(caller, hangupIntent))
    .addPerson(second_caller)
```

### Java

```java
// Create a call style notification for an ongoing call.
Notification.Builder builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forOnGoingCall(caller, hangupIntent))
    .addPerson(second_caller);
```

Use [`forScreeningCall()`](https://developer.android.com/reference/android/app/Notification.CallStyle#forScreeningCall(android.app.Person,%20android.app.PendingIntent,%20android.app.PendingIntent))
to create a call style notification for screening a call.

### Kotlin

```kotlin
// Create a call style notification for screening a call.
val builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
         Notification.CallStyle.forScreeningCall(caller, hangupIntent, answerIntent))
    .addPerson(second_caller)
```

### Java

```java
Notification.Builder builder = Notification.Builder(context, CHANNEL_ID)
    .setContentIntent(contentIntent)
    .setSmallIcon(smallIcon)
    .setStyle(
        Notification.CallStyle.forScreeningCall(caller, hangupIntent, answerIntent))
    .addPerson(second_caller);
```

### Enriched image support for notifications

In Android 12, you can now enrich your app's notification experience by
providing animated images in [`MessagingStyle()`](https://developer.android.com/reference/android/app/Notification.MessagingStyle#MessagingStyle(android.app.Person))
and [`BigPictureStyle()`](https://developer.android.com/reference/android/app/Notification.BigPictureStyle#BigPictureStyle())
notifications. Also, your app can now enable users to send image messages when
they reply to messages from the notification shade.

### Immersive mode improvements for gesture navigation

Android 12 consolidates existing behavior to make it easier for users to
[perform gesture navigation commands while in immersive
mode](https://developer.android.com/training/system-ui/immersive#immersive-consolidated-behavior). In
addition, Android 12 provides [backward compatibility behavior for sticky
immersive
mode](https://developer.android.com/training/system-ui/immersive#sticky-immersive-compat-android11-lower).

### Recents URL sharing (Pixel only)

On Pixel devices, users can now share links to recently viewed web content
directly from the Recents screen. After visiting the content in an app, the user
can swipe to the Recents screen and find the app where they viewed the content,
then tap on the link button to copy or share the URL.

For more information, see [Enable recents URL
sharing](https://developer.android.com/guide/components/activities/recents#url-sharing).

## Security and privacy

### Privacy Dashboard

![A vertical timeline shows the different apps that have
accessed location information, and at what time the accesses occurred](https://developer.android.com/static/images/about/versions/12/privacy-dashboard.svg) **Figure 1.** Location usage screen, part of the Privacy Dashboard.

On supported devices that run Android 12 or higher, a Privacy
Dashboard screen appears in system settings. On this screen, users can access
separate screens that show when apps access location, camera, and microphone
information. Each screen shows a timeline of when different apps have accessed a
particular type of data. Figure 1 shows the data access timeline for location
information.

Your app can [provide a rationale for
users](https://developer.android.com/training/permissions/explaining-access#privacy-dashboard-show-rationale)
to help them understand why your app accesses location, camera, or microphone
information. This rationale can appear on the new Privacy Dashboard screen, your
app's permissions screen, or both.

### Bluetooth permissions

Android 12 introduces the
[`BLUETOOTH_SCAN`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN),
[`BLUETOOTH_ADVERTISE`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE),
and
[`BLUETOOTH_CONNECT`](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT)
permissions. These permissions make it easier for apps that target
Android 12 to [interact with Bluetooth
devices](https://developer.android.com/guide/topics/connectivity/bluetooth), especially for apps that don't
require access to device location.

> [!NOTE]
> **Note:** The [Companion Device
> Manager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) provides a more streamlined method of connecting to companion devices. The system provides the pairing UI on behalf of your app. If you want more control over the pairing and connecting experience, use the Bluetooth permissions introduced in Android 12.

#### Update your app's Bluetooth permission declarations

To prepare your device for targeting Android 12 or higher, update
your app's logic. Instead of declaring a [legacy set of Bluetooth
permissions](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#declare-android11-or-lower),
declare a [more modern set of Bluetooth
permissions](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions#declare-android12-or-higher).

### Permission group lookup

On Android 12 or higher, you can query how the system organizes
platform-provided [permissions](https://developer.android.com/guide/topics/permissions/overview) into
permission groups:

- To determine the permission group into which the system has placed a platform-defined permission, call [`getGroupOfPlatformPermission()`](https://developer.android.com/reference/android/content/pm/PackageManager#getGroupOfPlatformPermission(java.lang.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.lang.String%3E)).
- To determine the platform-defined permissions that the system has placed into a particular permission group, call [`getPlatformPermissionsForGroup()`](https://developer.android.com/reference/android/content/pm/PackageManager#getPlatformPermissionsForGroup(java.lang.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.util.List%3Cjava.lang.String%3E%3E)).

> [!NOTE]
> **Note:** One of the [basic principles](https://developer.android.com/training/permissions/requesting#principles) of using Android permissions is to not assume system behavior. Don't assume that a particular permission is in a particular group. Instead, use the APIs described in this section.

### Hide application overlay windows

To give developers more control over what users see when they interact with the
developer's app, Android 12 introduces the ability to hide
overlay windows that are drawn by apps that have the
[`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
permission.

After declaring the
[`HIDE_OVERLAY_WINDOWS`](https://developer.android.com/reference/android/Manifest.permission#HIDE_OVERLAY_WINDOWS)
permission, an app can call
[`setHideOverlayWindows()`](https://developer.android.com/reference/android/view/Window#setHideOverlayWindows(boolean))
to indicate that all windows of type
[`TYPE_APPLICATION_OVERLAY`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY)
should be hidden when the app's own window is visible. Apps might choose to do
this when displaying sensitive screens, such as transaction confirmation flows.

Apps that show windows of type `TYPE_APPLICATION_OVERLAY` should consider
alternatives that may be more appropriate for their use case, such as
[picture-in-picture](https://developer.android.com/guide/topics/ui/picture-in-picture) or
[bubbles](https://developer.android.com/guide/topics/ui/bubbles).

### Known signers permission protection flag

Starting in Android 12, the
[`knownCerts`](https://developer.android.com/reference/android/R.attr#knownCerts) attribute for
[signature-level permissions](https://developer.android.com/guide/topics/permissions/overview#signature)
allows you to refer to the digests of known [signing
certificates](https://developer.android.com/studio/publish/app-signing#certificates-keystores) at declaration
time.

Your app can declare this attribute and use the `knownSigner` flag to allow
devices and apps to [grant signature permissions to other
apps](https://developer.android.com/guide/topics/permissions/defining#grant-signature-permissions), without
having to sign the apps at the time of device manufacturing and shipment.

### Device properties attestation

Android 12 expands the set of apps that can verify the device properties that
are in an [attestation
certificate](https://source.android.com/security/keystore/attestation#attestation-certificate)
when these apps generate a new key.

As of Android 9 (API level 28), [device policy
owners (DPOs)](https://developer.android.com/work/device-admin) that use
[Keymaster 4.0](https://source.android.com/security/keystore) or higher can
verify the device properties in these attestation certificates. Starting in
Android 12, any app that targets Android 12 (API level 31) or higher can perform
this verification using the
[`setDevicePropertiesAttestationIncluded()`](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setDevicePropertiesAttestationIncluded(boolean))
method.

The generated device properties include the following
[`Build`](https://developer.android.com/reference/android/os/Build) fields:

- `BRAND`
- `DEVICE`
- `MANUFACTURER`
- `MODEL`
- `PRODUCT`

### Secure lockscreen notification actions

Starting in Android 12, the `Notification.Action.Builder` class
supports the
[`setAuthenticationRequired()`](https://developer.android.com/reference/android/app/Notification.Action.Builder#setAuthenticationRequired(boolean))
method, which allows your app to [require that a device is
unlocked](https://developer.android.com/guide/topics/ui/notifiers/notifications#ActionsRequireUnlockedDevice)
before your app invokes a given notification action. This method helps add an
extra layer of security to notifications on locked devices.

### Localizable strings for BiometricPrompt

Android 12 introduces new APIs to help you improve your app's biometric
authentication user experience. The new [`BiometricManager.Strings`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings)
nested class includes the [`getButtonLabel()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings#getButtonLabel()),
[`getPromptMessage()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings#getPromptMessage()),
and [`getSettingName()`](https://developer.android.com/reference/android/hardware/biometrics/BiometricManager.Strings#getSettingName())
methods, which let your app retrieve a user-readable and localized button label,
prompt message, or app setting name. Use these labels to create more precise
user-facing instructions that are specific to the biometric authentication
methods used, such as "Use face unlock" or "Use your fingerprint to continue".

## Media

### Compatible media transcoding

Starting in Android 12 (API level 31), the system can automatically transcode
[HEVC(H.265)](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) and
[HDR](https://en.wikipedia.org/wiki/High-dynamic-range_video) (HDR10 and HDR10+)
videos recorded on the device to AVC (H.264), a format which is widely
compatible with standard players. This takes advantage of modern codecs when
they are available without sacrificing compatibility with older applications.

See [compatible media transcoding](https://developer.android.com/guide/topics/media-apps/video-app/compatible-media-transcoding) for more details.

### Performance class

Android 12 introduces a standard called *performance class*. A
performance class specifies hardware capabilities beyond Android's baseline
requirements. Each Android device declares the performance class that it
supports. Developers can check the device's performance class at runtime and
provide upgraded experiences that take full advantage of the device's
capabilities.

See [Performance class](https://developer.android.com/topic/performance/performance-class)
for more details.

### Video encoding improvements

Android 12 defines a standard set of keys for controlling the
quantization parameter (QP) value for video encoding, allowing developers to
avoid vendor-specific code.

The new keys are available in the
[`MediaFormat`](https://developer.android.com/reference/android/media/MediaFormat#KEY_VIDEO_QP_B_MAX) API
and also in the
[NDK Media library](https://developer.android.com/ndk/reference/group/media).

Starting with Android 12 video encoders enforce a minimum quality
threshold. This guarantees that users don't experience extremely low quality
when encoding videos with high scene complexity.

### Audio focus

Starting with Android 12 (API level 31), when an app requests audio focus while
another app has the focus and is playing, the system fades out the playing app.

See [Audio focus in Android 12 and higher](https://developer.android.com/media/optimize/audio-focus#audio-focus-12)
for more details.

### MediaDrm updates

In order to determine whether a secure decoder component is required with the
current `MediaDrm` APIs, you must follow these steps:

1. Create a `MediaDrm`.
2. Open a session to obtain a session id.
3. Create a `MediaCrypto` using the session id.
4. Call `MediaCrypto.requiresSecureDecoderComponent(mimeType)`.

With the new methods `requiresSecureDecoder(@NonNull String mime)` and
`requiresSecureDecoder(@NonNull String mime, @SecurityLevel int level)`
you can determine this as soon as you create a `MediaDrm`.

## Camera

### Camera2 vendor extensions

Many of our device manufacturer partners have built custom camera extensions---such
as Bokeh, HDR, Night mode, and others---that they want apps to use to create
differentiated experiences on their devices. The [CameraX
library](https://developer.android.com/training/camerax/extensions-api) already supports
these custom vendor extensions. In Android 12, these
vendor extensions are now exposed directly in the platform.

This addition helps apps that have complex
[`Camera2`](https://developer.android.com/reference/android/hardware/camera2/package-summary)
implementations take advantage of vendor extensions without having to make
significant changes to legacy code. The Camera2 Extension APIs expose exactly
the [same set of
extensions](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics) as
in CameraX, and those are already supported on [many different
devices](https://developer.android.com/training/camerax/devices), so you can use them without any
additional configuration.

For more information, see
[`CameraExtensionCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics).

### Quad bayer camera sensor support

Many Android devices today ship with ultra high-resolution camera sensors,
typically with Quad or Nona Bayer patterns, and these offer great flexibility in
terms of image quality and low-light performance. Android 12 introduces new
platform APIs that let third-party apps take full advantage of these versatile
sensors. The [new APIs](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_ULTRA_HIGH_RESOLUTION_SENSOR)
support the unique behavior of these sensors and take into account that they
might support different stream configurations and combinations when operating in
full resolution or 'maximum resolution' mode vs 'default' mode.

## Graphics and images

### Provide apps direct access to tombstone traces

Starting in Android 12, you can access your app's native crash tombstone as a
[protocol buffer](https://developers.google.com/protocol-buffers/) through the
[`ApplicationExitInfo.getTraceInputStream()`](https://developer.android.com/reference/android/app/ApplicationExitInfo#getTraceInputStream())
method. The protocol buffer is serialized using [this schema](https://android.googlesource.com/platform/system/core/+/refs/heads/master/debuggerd/proto/tombstone.proto).
Previously, the only way to get access to this information was through the
[Android Debug Bridge](https://developer.android.com/studio/command-line/adb) (adb).

For more information, see [Provide apps direct access to tombstone traces](https://developer.android.com/ndk/guides/debug#tombstone-traces)

### AVIF image support

Android 12 introduces support for images that use the AV1 Image File Format
(AVIF). AVIF is a container format for images and sequences of images encoded
using AV1. AVIF takes advantage of the intra-frame encoded content from video
compression. This dramatically improves image quality for the same file size
when compared to older image formats, such as JPEG. For an in-depth look at the
advantages of this format, see Jake Archibald's [blog
post](https://jakearchibald.com/2020/avif-has-landed/).

### Easier blurs, color filters, and other effects

Android 12 adds the new [`RenderEffect`](https://developer.android.com/reference/android/graphics/RenderEffect)
that applies common graphics effects such as blurs, color filters, Android shader
effects, and more to [`View`](https://developer.android.com/reference/android/view/View)s
and rendering hierarchies. Effects can be combined as either chain effects
(which compose an inner and outer effect) or blended effects. Different Android
devices may or may not support the feature due to limited processing power.

Effects can also be applied to the underlying [`RenderNode`](https://developer.android.com/reference/android/graphics/RenderNode)
for `View`s by calling [`View.setRenderEffect(RenderEffect)`](https://developer.android.com/reference/android/view/View#setRenderEffect(android.graphics.RenderEffect)).

To implement a `RenderEffect`:

    view.setRenderEffect(RenderEffect.createBlurEffect(radiusX, radiusY, SHADER_TILE_MODE))

### Native animated image decoding

In Android 12, the NDK
[`ImageDecoder`](https://developer.android.com/ndk/reference/group/image-decoder) API has been expanded
to decode all frames and timing data from images
that use the animated [GIF](https://en.wikipedia.org/wiki/GIF) and
animated [WebP](https://developers.google.com/speed/webp) file formats. When it
was introduced in Android 11, this API decoded only the first image from
animations in these formats.

Use `ImageDecoder` instead of third-party libraries to further [decrease APK
size](https://developer.android.com/topic/performance/reduce-apk-size#minimize)
and benefit from future updates related to security and performance.

For more details on the API, refer to the [API reference](https://developer.android.com/ndk/reference/group/image-decoder) and the [sample on GitHub](https://github.com/android/ndk-samples/tree/develop/webp/image-decoder).

## Connectivity

### Keeping companion apps awake

To support the need of companion apps to stay running to manage the device,
Android 12 introduces APIs that do the following:

- Enable you to wake an app when a companion device is within range.
- Guarantee that the process will continue running while the device stays within range.

To use the APIs, your devices must be connected using [Companion Device
Manager](https://developer.android.com/reference/android/companion/CompanionDeviceManager). For more
information, see
[`CompanionDeviceManager.startObservingDevicePresence()`](https://developer.android.com/reference/android/companion/CompanionDeviceManager#startObservingDevicePresence(java.lang.String))
and
[`CompanionDeviceService.onDeviceAppeared()`](https://developer.android.com/reference/android/companion/CompanionDeviceService#onDeviceAppeared(java.lang.String)).

### Companion Device Manager profiles

![](https://developer.android.com/static/images/about/versions/12/companion-device-profile.png) A permissions dialog that uses a companion device profile to request multiple permissions in a single request.

Partner apps on Android 12 (API level 31) and higher can use companion device
profiles when connecting to a watch. Using a profile simplifies the enrollment
process by bundling the granting of a device-type-specific set of permissions
into one step.

The bundled permissions are granted to the companion app once the device
connects, and last only while the device is associated. Deleting the app or
removing the association removes the permissions.

For more information, see
[`AssociationRequest.Builder.setDeviceProfile()`](https://developer.android.com/reference/android/companion/AssociationRequest.Builder#setDeviceProfile(java.lang.String)).


### Bandwidth estimation improvements

In Android 12, the bandwidth estimation capabilities provided by
[`getLinkDownstreamBandwidthKbps()`](https://developer.android.com/reference/android/net/NetworkCapabilities#getLinkDownstreamBandwidthKbps())
and
[`getLinkUpstreamBandwidthKbps()`](https://developer.android.com/reference/android/net/NetworkCapabilities#getLinkUpstreamBandwidthKbps())
are improved for both Wi-Fi and cellular connectivity. The values returned now
represent the user's all-time weighted average throughput per carrier or WiFi
SSID, network type, and signal level, across all applications on the device.
This can return a more-accurate and realistic estimate of expected throughput,
provide estimates on a cold start of your application, and requires fewer cycles
when compared to using other throughput estimation methods.

### Wi-Fi Aware (NAN) enhancements

Android 12 adds some enhancements to Wi-Fi Aware:

- On devices running Android 12 (API level 31) and higher, you can use the [`onServiceLost()`](https://developer.android.com/reference/android/net/wifi/aware/DiscoverySessionCallback#onServiceLost(android.net.wifi.aware.PeerHandle,%20int)) callback to be alerted when your app has lost a discovered service due to the service stopping or moving out of range.
- The way that multiple data-paths (NAN Data Paths) are set up is changing to be more efficient. Earlier versions used L2 messaging to exchange peer information of the initiators, which introduced latency. On devices running Android 12 and higher, the responder (server) can be configured to accept any peer---that is, it doesn't need to know the initiator information upfront. This speeds up datapath bringup and enables multiple point-to-point links with only one network request.
- To prevent the framework from rejecting discovery or connection requests due to running out of resources, on devices running Android 12 and higher, you can call [`WifiAwareManager.getAvailableAwareResources()`](https://developer.android.com/reference/android/net/wifi/aware/WifiAwareManager#getAvailableAwareResources()). This method's return value lets you get the number of available data paths, the number of available publish sessions, and the number of available subscribe sessions.

### Concurrent Peer-to-Peer + Internet Connection

When devices targeting Android 12 (API level 31) and higher run on devices with
hardware support, using [Peer-to-peer
connections](https://developer.android.com/guide/topics/connectivity/wifi-bootstrap) will not disconnect your
existing Wi-Fi connection when creating the connection to the peer device. To
check for support for this feature, use
[`WifiManager.isMultiStaConcurrencySupported()`](https://developer.android.com/reference/android/net/wifi/WifiManager#isMultiStaConcurrencySupported()).

### Enable screen off for NFC payments

In apps that target Android 12 and higher, you can enable NFC
payments without the device's screen on by setting
[`requireDeviceScreenOn`](https://developer.android.com/reference/android/R.attr#requireDeviceScreenOn) to
`false`. For more information about NFC payments with screen off or locked, see
[Screen off and lock-screen
behavior](https://developer.android.com/guide/topics/connectivity/nfc/hce#screen-off-12-higher).

## Storage

Android 12 introduces the following storage management
capabilities:

- Media store support for `MediaDocumentsProvider` when your app [retrieves a
  media URI that is equivalent to a given documents provider
  URI](https://developer.android.com/training/data-storage/shared/documents-files#retrieve-equivalent-media-uri).
- A directory for [voice
  recordings](https://developer.android.com/training/data-storage/shared/media#well-defined-collections).
- The [`MANAGE_MEDIA`](https://developer.android.com/reference/android/Manifest.permission#MANAGE_MEDIA) permission, which allows an app to [perform media management
  operations](https://developer.android.com/training/data-storage/shared/media#management-permission) without showing a confirmation dialog to the user for each operation.
- Apps that have both the [`MANAGE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE) permission and the [`QUERY_ALL_PACKAGES`](https://developer.android.com/reference/android/Manifest.permission#QUERY_ALL_PACKAGES) permission---such as file management apps---can [invoke a custom
  activity](https://developer.android.com/training/data-storage/manage-all-files#invoke-storage-management-activity) for managing another app's storage space, provided that the other app [creates
  the custom activity](https://developer.android.com/training/data-storage/app-specific#create-storage-management-activity).

## Core functionality

### Automatic app updates

Android 12 introduces the
[`setRequireUserAction()`](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequireUserAction(int))
method for apps that use the
[`PackageInstaller`](https://developer.android.com/reference/android/content/pm/PackageInstaller) API.
This method allows installer apps to perform app updates without requiring the
user to confirm the action.

### Device chipset information

Android 12 adds two constants to `android.os.Build` that expose
the SoC chipset vendor and model information via the SDK. You can retrieve this
information by calling `Build.SOC_MANUFACTURER` and `Build.SOC_MODEL`
respectively.

### Updates to core Java APIs

Based on requests and collaboration with developers, we've added the following
core libraries in Android 12:

| **Class** | **APIs** |
|---|---|
| `java.lang.Deprecated` | - [`forRemoval()`](https://developer.android.com/reference/java/lang/Deprecated#forRemoval()) - [`since()`](https://developer.android.com/reference/java/lang/Deprecated#since()) |
| `java.lang.Byte` | - [Constructors deprecated](https://developer.android.com/reference/java/lang/Byte#public-constructors_1) - [`compareUnsigned()`](https://developer.android.com/reference/java/lang/Byte#compareUnsigned(byte,%20byte)) |
| `java.lang.Short` | - [Constructors deprecated](https://developer.android.com/reference/java/lang/Short#public-constructors_1) - [`compareUnsigned()`](https://developer.android.com/reference/java/lang/Short#compareUnsigned(short,%20short)) |
| `java.lang.Math` | - [`floorDiv()`](https://developer.android.com/reference/java/lang/Math#floorDiv(long,%20int)) - [`floorMod()`](https://developer.android.com/reference/java/lang/Math#floorMod(long,%20int)) - [`multiplyExact()`](https://developer.android.com/reference/java/lang/Math#multiplyExact(long,%20int)) - [`multiplyFull()`](https://developer.android.com/reference/java/lang/Math#multiplyFull(int,%20int)) - [`multiplyHigh()`](https://developer.android.com/reference/java/lang/Math#multiplyHigh(long,%20long)) |
| `java.lang.StrictMath` | - [`floorDiv()`](https://developer.android.com/reference/java/lang/StrictMath#floorDiv(long,%20int)) - [`floorMod()`](https://developer.android.com/reference/java/lang/StrictMath#floorMod(long,%20int)) - [`multiplyExact()`](https://developer.android.com/reference/java/lang/StrictMath#multiplyExact(long,%20int)) - [`multiplyFull()`](https://developer.android.com/reference/java/lang/StrictMath#multiplyFull(int,%20int)) - [`multiplyHigh()`](https://developer.android.com/reference/java/lang/StrictMath#multiplyHigh(long,%20long)) |
| `java.util.Set` | [`copyOf()`](https://developer.android.com/reference/java/util/Set#copyOf(java.util.Collection%3C?%20extends%20E%3E)) |
| `java.util.Map` | [`copyOf()`](https://developer.android.com/reference/java/util/Map#copyOf(java.util.Map%3C?%20extends%20K,%20?%20extends%20V%3E)) |
| `java.util.List` | [`copyOf()`](https://developer.android.com/reference/java/util/List#copyOf(java.util.Collection%3C?%20extends%20E%3E)) |
| `java.time.Duration` | - [`dividedBy()`](https://developer.android.com/reference/java/time/Duration#dividedBy(java.time.Duration)) - [`toDaysPart()`](https://developer.android.com/reference/java/time/Duration#toDaysPart()) - [`toHoursPart()`](https://developer.android.com/reference/java/time/Duration#toHoursPart()) - [`toMillisPart()`](https://developer.android.com/reference/java/time/Duration#toMillisPart()) - [`toMinutesPart()`](https://developer.android.com/reference/java/time/Duration#toMinutesPart()) - [`toNanosPart()`](https://developer.android.com/reference/java/time/Duration#toNanosPart()) - [`toSecondsPart()`](https://developer.android.com/reference/java/time/Duration#toSecondsPart()) - [`truncatedTo()`](https://developer.android.com/reference/java/time/Duration#truncatedTo(java.time.temporal.TemporalUnit)) |
| `java.time.LocalTime` | - [`ofInstant()`](https://developer.android.com/reference/java/time/LocalTime#ofInstant(java.time.Instant,%20java.time.ZoneId)) - [`toEpochSecond()`](https://developer.android.com/reference/java/time/LocalTime#toEpochSecond(java.time.LocalDate,%20java.time.ZoneOffset)) |