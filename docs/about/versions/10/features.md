---
title: https://developer.android.com/about/versions/10/features
url: https://developer.android.com/about/versions/10/features
source: md.txt
---

Android 10 introduces great features and capabilities for users and
developers. This document highlights what's available for developers.

To learn about the APIs, read the
[API diff report](https://developer.android.com/sdk/api_diff/29/changes) or visit the
[Android API reference](https://developer.android.com/reference) --- look for APIs that were "added in
API level 29". Also be sure to check out Android 10 behavior
changes (for [apps targeting API level 29](https://developer.android.com/about/versions/10/behavior-changes-10) and for
[all apps](https://developer.android.com/about/versions/10/behavior-changes-all)), as well as [privacy
changes](https://developer.android.com/about/versions/10/privacy), to learn about areas where platform changes may
affect your apps.

## Security enhancements

Android 10 introduces a number of security features, which the
following sections summarize.

### Improved biometric authentication dialogs

Android 10 introduces the following improvements to
[biometric authentication](https://developer.android.com/training/sign-in/biometric-auth) support:

- A check for the biometric authentication capability.
- A fallback mechanism that allows a user to authenticate using their device PIN, pattern, or password if they cannot authenticate using their biometric input.
- A hint that tells the system not to require user confirmation after the user has authenticated using an implicit biometric modality. For example, you could tell the system that no further confirmation should be required after a user has authenticated using face authentication.

### Run embedded DEX code directly from APK

As of Android 10, you can tell the platform to run embedded DEX
code directly from your app's APK file. This option can help prevent an attack
if an attacker ever managed to tamper with the locally compiled code on the
device.

For more information, see
[Run embedded DEX code directly from APK](https://developer.android.com/topic/security/dex).

### TLS 1.3 support

Android 10 adds support for
[TLS 1.3](https://www.ietf.org/blog/tls13/). TLS 1.3 is a major revision to the
TLS standard that includes performance benefits and enhanced security. Our
benchmarks indicate that secure connections can be established as much as 40%
faster with TLS 1.3 compared to TLS 1.2.

For more details about our implementation of TLS 1.3, see the [TLS section
within the behavior changes for all apps
page](https://developer.android.com/about/versions/10/behavior-changes-all#tls-1.3).

### Public Conscrypt API

As of Android 10, the Conscrypt security provider includes a
public API for TLS functionality.

The collection of classes under
[`android.net.ssl`](https://developer.android.com/reference/android/net/ssl/package-summary) contain static
methods to access functionality that isn't available from the generic
`javax.net.ssl` APIs. The names for these classes can be inferred as the plural
of the corresponding `javax.net.ssl` class. For example, code that operates on
instances of `javax.net.ssl.SSLSocket` can instead use methods from
[`SSLSockets`](https://developer.android.com/reference/android/net/ssl/SSLSockets).
| **Caution:** If you're still accessing TLS functionality using reflection, change to using the public API. This is because of planned further [restrictions on
| non-SDK
| interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).

## Connectivity features

Android 10 includes several improvements related to networking and connectivity.

### Wi-Fi network connection API

Android 10 adds support for peer-to-peer connections. This
feature enables your app to prompt the user to change the access point that the
device is connected to by using
[`WifiNetworkSpecifier`](https://developer.android.com/reference/android/net/wifi/WifiNetworkSpecifier)
to describe properties of a requested network. The peer-to-peer connection is
used for non-network-providing purposes, such as bootstrapping configuration for
secondary devices like Chromecast and Google Home hardware.

For more information, see [Wi-Fi Network Request API for peer-to-peer
connectivity](https://developer.android.com/guide/topics/connectivity/wifi-bootstrap).

### Wi-Fi network suggestion API

Android 10 adds support for your app to prompt the user to connect
to a Wi-Fi access point. You can supply suggestions for which network to connect
to. The platform will ultimately choose which access point to accept based on
the input from your and other apps.

For more information about this feature, see
[Wi-Fi suggest](https://developer.android.com/guide/topics/connectivity/wifi-suggest).

### Improvements to Wi-Fi high-performance and low-latency modes

Android 10 allows you to provide a hint to the underlying modem to minimize
latency.

Android 10 extends the Wi-Fi lock API to effectively support high-performance
mode and low-latency mode. Wi-Fi power save is disabled for high-performance and
low-latency mode, and further latency optimization may be enabled in low-latency
mode, depending on modem support.

Low-latency mode is only enabled when the application acquiring the lock is
running in the foreground and the screen is on. The low-latency mode is
especially helpful for real-time mobile gaming applications.

### Specialized lookups in DNS resolver

Android 10 adds native support for specialized DNS lookups using
both cleartext lookups and DNS-over-TLS mode. Previously, the platform DNS
resolver supported only A and AAAA records, which allow looking up only the IP
addresses associated with a name, but did not support any other record types.
The [`DnsResolver`](https://developer.android.com/reference/android/net/DnsResolver) API provides generic,
asynchronous resolution, enabling you to look up `SRV`, `NAPTR`, and other
record types. Note that parsing the response is left to the app to perform.

For NDK-based apps, see
[`android_res_nsend`](https://developer.android.com/ndk/reference/group/networking#android_res_nsend).

### Wi-Fi Easy Connect

Android 10 enables you to use Easy Connect to provision Wi-Fi
credentials to a peer device, as a replacement of WPS which has been deprecated.
Apps can integrate Easy Connect into their setup and provisioning flow by using
the
[`ACTION_PROCESS_WIFI_EASY_CONNECT_URI`](https://developer.android.com/reference/android/provider/Settings#ACTION_PROCESS_WIFI_EASY_CONNECT_URI)
intent.

For more information on this feature, see
[Wi-Fi Easy Connect](https://developer.android.com/guide/topics/connectivity/wifi-easy).

### Wi-Fi Direct connection API

The `WifiP2pConfig` and `WifiP2pManager` API classes have updates in Android 10
to support fast connection establishment capabilities to Wi-Fi Direct using
predetermined information. This information is shared via a side channel, such
as Bluetooth or NFC.

The following code sample shows how to create a group using predetermined
information:  

### Kotlin

```kotlin
val manager = getSystemService(Context.WIFI_P2P_SERVICE) as WifiP2pManager
val channel = manager.initialize(this, mainLooper, null)

// prefer 5G band for this group
val config = WifiP2pConfig.Builder()
    .setNetworkName("networkName")
    .setPassphrase("passphrase")
    .enablePersistentMode(false)
    .setGroupOperatingBand(WifiP2pConfig.GROUP_OWNER_BAND_5GHZ)
    .build()

// create a non-persistent group on 5GHz
manager.createGroup(channel, config, null)
```

### Java

```java
WifiP2pManager manager = (WifiP2pManager) getSystemService(Context.WIFI_P2P_SERVICE);
Channel channel = manager.initialize(this, getMainLooper(), null);

// prefer 5G band for this group
WifiP2pConfig config = new WifiP2pConfig.Builder()
.setNetworkName("networkName")
.setPassphrase("passphrase")
.enablePersistentMode(false)
.setGroupOperatingBand(WifiP2pConfig.GROUP_OWNER_BAND_5GHZ)
.build();

// create a non-persistent group on 5GHz
manager.createGroup(channel, config, null);
```

To join a group using credentials, replace `manager.createGroup()` with the
following:  

### Kotlin

```kotlin
manager.connect(channel, config, null)
```

### Java

```java
manager.connect(channel, config, null);
```

### Bluetooth LE Connection Oriented Channels (CoC)

Android 10 enables your app to use BLE CoC connections to transfer larger data
streams between two BLE devices. This interface abstracts Bluetooth and
connectivity mechanics to simplify implementation.

## Telephony features

Android 10 includes several improvements related to telephony.

### Call quality improvements

Android 10 adds the ability to collect information about the quality of ongoing
IP Multimedia Subsystem (IMS) calls, including quality to and from the network,
on devices that support the feature.

### Call screening and caller ID

Android 10 provides your app with a means to identify calls not
in the user's address book as potential spam calls, and to have spam calls
silently rejected on behalf of the user. Information about these blocked calls
is logged as blocked calls in the call log to provide greater transparency to
the user when they are missing calls. Use of this API eliminates the requirement
to obtain `READ_CALL_LOG` permissions from the user to provide call screening
and caller ID functionality.

### Call redirection service API

Android 10 changes how call intents are handled. The
`NEW_OUTGOING_CALL` broadcast is deprecated and is replaced with the
`CallRedirectionService` API. The `CallRedirectionService` API provides
interfaces for you to modify outgoing calls made by the Android platform. For
example, third-party apps might cancel calls and reroute them over VoIP.

## Improvements in creating files on external storage

In addition to introducing [scoped
storage](https://developer.android.com/training/data-storage/files/external-scoped),
Android 10 adds the following capabilities related to external
storage:

- You can use the [`IS_PENDING`
  flag](https://developer.android.com/training/data-storage/files/media#pending-media-files) to give your app exclusive access to a media file as it's written to disk.
- If you're aware of a specific location where files should be stored, you can [provide the system a hint](https://developer.android.com/training/data-storage/files/media#provide-hint) for where to store the newly-written files.
- Each external storage device has a [unique volume
  name](https://developer.android.com/training/data-storage/files/external#unique-volume-names).

## Media and graphics

Android 10 introduces the following new media and graphics features and APIs:

### Sharing audio input

Android 10 adds the ability for two apps to share the audio input simultaneously.
For full information, see [Sharing audio input](https://developer.android.com/guide/topics/media/sharing-audio-input).

### Audio playback capture

Android 10 gives an app the ability to capture audio playback from other apps.
For full information, see [Playback capture](https://developer.android.com/guide/topics/media/playback-capture).

### Seekbar in MediaStyle notifications

Starting with Android 10, `MediaStyle` notifications display a seekbar. The seekbar shows
the playback progress from
[`PlaybackState.getPosition()`](https://developer.android.com/reference/android/media/session/PlaybackState#getPosition()),
and in some cases the seekbar can be used to seek to a location in the playing
program. The seekbar appearance and behavior is controlled by these rules:

- The seekbar appears if there is an active `MediaSession` and its duration (specified by `MediaMetadata.METADATA_KEY_DURATION`) is greater than zero. This means that the bar does not appear for indeterminate streams like livestreams and radio broadcasts.
- If the session implements `ACTION_SEEK_TO` the user can drag the seekbar to control the playback location.

### Native MIDI API

The Android Native MIDI API *(AMidi)* gives application developers the ability
to send and receive MIDI data with C/C++code, integrating more closely with
their C/C++ audio/control logic and minimizing the need for JNI.

For more information, see [Android Native MIDI API](https://developer.android.com/ndk/guides/audio/midi).

### MediaCodecInfo improvements

Android 10 adds methods to
[`MediaCodecInfo`](https://developer.android.com/reference/android/media/MediaCodecInfo) that reveal more
information about a codec.

For more information, see [Media codecs](https://developer.android.com/guide/topics/media/media-codecs).

## Thermal API

When devices get too warm, they may throttle the CPU and/or GPU, and this can
affect apps and games in unexpected ways. Apps using complex graphics, heavy
computation, or sustained network activity are more likely to hit issues, and
those can vary across devices based on chipset and core frequencies, levels of
integration, and also device packaging and form factor.

In Android 10, apps and games can use a thermal API to monitor changes on
the device and take action to maintain lower power usage to restore normal
temperature. Apps [register a listener](https://developer.android.com/reference/android/os/PowerManager#addThermalStatusListener(android.os.PowerManager.OnThermalStatusChangedListener))
in [PowerManager](https://developer.android.com/reference/android/os/PowerManager), through which the system
reports ongoing thermal status ranging from light and moderate to severe,
critical, emergency, and shutdown.

When the device reports thermal stress, apps and games can help by backing off
ongoing activities to reduce power usage on various ways. For example,
streaming apps could reduce resolution/bit rate or network traffic, a camera
app could disable flash or intensive image enhancement, a game could reduce
frame rate or polygon tesselation, a media app could reduce speaker volume,
and a maps app could turn off GPS.

The thermal API requires a new device HAL layer---it's currently supported
on Pixel devices running Android 10 and we're working with our device-maker
partners to bring broad support to the ecosystem as quickly as possible.

## Camera and images

Android 10 introduces the following new camera- and image-related features:

### Monochrome camera support

Android 9 (API level 28) first introduced monochrome camera capability.
Android 10 adds several enhancements to monochrome camera support:

- Y8 stream format support to improve memory efficiency.
- Support for monochrome raw DNG capture.
- Introduction of MONO and NIR CFA enumerations to distinguish between regular monochrome camera and near infrared cameras.

You may use this feature to capture a native monochrome image. A logical
multi-camera device may use a monochrome camera as a physical sub-camera to
achieve better low-light image quality.

### Dynamic Depth Format

Starting in Android 10, cameras can store the depth data for an image in a
separate file, using a new schema called Dynamic Depth Format (DDF). Apps can
request both the JPG image and its depth metadata, using that information to
apply any blur they want in post-processing without modifying the original
image data.

To read the specification for this format, see
[Dynamic Depth Format](https://developer.android.com/static/training/camera2/Dynamic-depth-v1.0.pdf).

### High Efficiency Image File format

High Efficiency Image File (HEIF) format is a standard image and video format
that introduces higher-quality encoding and smaller file size when compared to
other file formats.

For more information about the file format, see
[HEIC](https://developer.android.com/reference/android/graphics/ImageFormat#HEIC).

### Improvements in multi-camera

Android 10 improves the fusing of multiple cameras into a single logical camera,
a feature introduced in Android 9 (API level 28). The following were added to
the
[Camera2 API](https://developer.android.com/reference/android/hardware/camera2/package-summary):

- [`isSessionConfigurationSupported(SessionConfiguration sessionConfig)`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#isSessionConfigurationSupported(android.hardware.camera2.params.SessionConfiguration))---enables you to query whether or not the passed session
  configuration can be used to create a camera capture session.

- [`LOGICAL_MULTI_CAMERA_ACTIVE_PHYSICAL_ID`](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#LOGICAL_MULTI_CAMERA_ACTIVE_PHYSICAL_ID)---enables
  you to determine the ID of the active physical camera backing a logical
  camera device. You can use the IDs returned to request logical streams and
  physical subcamera streams to achieve better power efficiency.

## Accessibility services API

Android 10 introduces the following new accessibility service
features and APIs:

### AccessibilityNodeInfo entry key flag

As of Android 10, you can call
[`isTextEntryKey()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#isTextEntryKey())
to determine whether a given `AccessibilityNodeInfo` represents a text entry key
that's part of a keyboard or keypad.

### Accessibility dialog spoken feedback

In case where users need to perform the accessibility shortcut to start an
accessibility service, Android 10 allows the dialog to be
accompanied by a text-to-speech prompt if the service requests it.

### Accessibility shortcut when gesture navigation enabled

When the [gesture navigation](https://developer.android.com/guide/navigation/gesturenav) feature is enabled
in Android 10, the [accessibility
button](https://support.google.com/accessibility/android/answer/7650693) isn't
visible or selectable. To access the accessibility services menu, users must
perform one of the following gestures:

- Two-finger swipe up.
- Two-finger swipe up and hold.

### Accessibility shortcut for physical keyboards

In Android 10, users can trigger the accessibility shortcut on a
physical keyboard by pressing <kbd>Control+Alt+Z</kbd>.

### Soft keyboard controller enhancement

In Android 10, accessibility services can request that the soft
keyboard be displayed even when the device detects a hard keyboard attached.
Users can override this behavior.

### User-defined accessibility timeouts

Android 10 introduces the
[`getRecommendedTimeoutMillis()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#getRecommendedTimeoutMillis(int,%20int))
API. This method provides support for user-defined timeouts for interactive and
non-interactive UI elements. The return value is influenced by both user
preferences and accessibility service APIs.

## Autofill improvements

Android 10 contains the following improvements to the autofill service.

### Compatibility-related autofill requests

You can use the
[`FillRequest.FLAG_COMPATIBILITY_MODE_REQUEST`](https://developer.android.com/reference/android/service/autofill/FillRequest#FLAG_COMPATIBILITY_MODE_REQUEST)
flag to determine whether an autofill request was generated via compatibility
mode.

### Save username and password simultaneously

You can support cases where an application uses multiple activities to
display username, password, and other fields by using the
[`SaveInfo.FLAG_DELAY_SAVE`](https://developer.android.com/reference/android/service/autofill/SaveInfo#FLAG_DELAY_SAVE)
flag.

### User interaction with the Save UI

You can show and hide a password field in a save dialog by setting an action
listener on the dialog and changing the visibility of the corresponding password
remote view.

### Support for updating datasets

Autofill can update existing passwords. For example, if a user has already
stored a password, and they save a new password, Autofill prompts the user to
update the existing password instead of saving a new one.

### Field Classification improvements

Android 10 contains the following improvements to the Field Classification API.

#### UserData.Builder constructor

The
[`UserData.Builder`](https://developer.android.com/reference/android/service/autofill/UserData.Builder)
constructor has changed to better align to the `Builder` pattern.

#### Allow a Value to be mapped to multiple types of Category IDs

When using
[`UserData.Builder`](https://developer.android.com/reference/android/service/autofill/UserData.Builder) in
Android 10, you can now map a value to multiple types of category IDs. In
previous releases, an exception was thrown if a value was added more than once.

#### Improved support for credit card numbers

Field classification can now detect four-digit numbers as the last four digits
of a credit card number.

#### Support for app-specific field classification

Android 10 adds
[`FillResponse.setUserData()`](https://developer.android.com/reference/android/service/autofill/FillResponse#setUserData(android.service.autofill.UserData)),
which allows you to set app-specific user data for the duration of the session.
This helps the autofill service detect types for fields with app-specific
content.

## UI and system controls

Android 10 provides the following user-interface improvements:

### Support JVMTI PopFrame caps

Android 10 adds support for the
[`can_pop_frames`](https://docs.oracle.com/javase/7/docs/platform/jvmti/jvmti.html#PopFrame)
capability in the Android JVMTI implementation. When debugging, this feature
allows you to re-run functions after pausing at a breakpoint and adjusting
locals, globals, or implementation of a function. For more information, see
Oracle's [Pop Frame reference page](https://docs.oracle.com/javase/7/docs/platform/jvmti/jvmti.html#PopFrame).

### Surface control API

Android 10 provides a
[`SurfaceControl`](https://developer.android.com/reference/android/view/SurfaceControl) API
for low-level access to the system-compositor
([`SurfaceFlinger`](https://source.android.com/devices/graphics/arch-sf-hwc)). For
most users, SurfaceView is the correct way to leverage the compositor. The
`SurfaceControl` API can be useful in certain cases, for example:

- Synchronization of multiple surfaces
- Cross-process surface embedding
- Lower-level lifetime management

The `SurfaceControl` API is available in both
[SDK](https://developer.android.com/reference/android/view/SurfaceControl) and NDK bindings.
The NDK implementation includes an API for manual exchange of buffers with the
compositor. This provides an alternative for users who have run up against the
limitations of
[`BufferQueue`](https://source.android.com/devices/graphics/arch-bq-gralloc).

### WebView hung renderer detection

Android 10 introduces the
[`WebViewRenderProcessClient`](https://developer.android.com/reference/android/webkit/WebViewRenderProcessClient)
abstract class, which apps can use to detect if a
[`WebView`](https://developer.android.com/reference/android/webkit/WebView) has become unresponsive. To
use this class:

1. Define your own subclass and implement its [`onRenderProcessResponsive()`](https://developer.android.com/reference/android/webkit/WebViewRenderProcessClient#onRenderProcessResponsive(android.webkit.WebView,%20android.webkit.WebViewRenderProcess)) and [`onRenderProcessUnresponsive()`](https://developer.android.com/reference/android/webkit/WebViewRenderProcessClient#onRenderProcessUnresponsive(android.webkit.WebView,%20android.webkit.WebViewRenderProcess)) methods.
2. Attach an instance of your `WebViewRenderProcessClient` to one or more `WebView` objects.
3. If the `WebView` becomes unresponsive, the system calls the client's `onRenderProcessUnresponsive()` method, passing the `WebView` and `WebViewRenderProcess`. (If the `WebView` is single-process, the `WebViewRenderProcess` parameter is null.) Your app can take appropriate action, such as showing a dialog box to the user asking if they want to halt the rendering process.

If the `WebView` remains unresponsive, the system calls `onRenderProcessUnresponsive()`
periodically (no more than once every five seconds), but takes no other action.
If the `WebView` becomes responsive
again, the system calls `onRenderProcessResponsive()` just once.

### Settings panels

Android 10 introduces *Settings Panels* , an API which allows apps to show
settings to users in the context of their app. This prevents users from needing
to go into **Settings** to change things like **NFC** or **Mobile data** in
order to use the app.
![](https://developer.android.com/static/images/about/versions/10/settings-wifi-part1.png) **Figure 1.** The user tries to open a web page while the device is not connected to the network. Chrome pops up the **Internet Connectivity** settings panel...

<br />

<br />

<br />

![](https://developer.android.com/static/images/about/versions/10/settings-wifi-part2.png) **Figure 2.** The user can turn on Wi-Fi and select a network without leaving the Chrome app.

For example, suppose a user opens a web browser while their device is in
airplane mode. Prior to Android 10, the app could only display a generic message
asking the user to open **Settings** to restore connectivity. With Android 10,
the browser app can display an inline panel showing key connectivity settings
such as airplane mode, Wi-Fi (including nearby networks), and mobile data. With
this panel, users can restore connectivity without leaving the app.

To display a settings panel, fire an intent with the one of the following
[`Settings.Panel`](https://developer.android.com/reference/android/provider/Settings.Panel) actions:  

### Kotlin

```kotlin
val panelIntent = Intent(Settings.Panel.settings_panel_type)
startActivityForResult(panelIntent)
```

### Java

```java
Intent panelIntent = new Intent(Settings.Panel.settings_panel_type);
startActivityForResult(panelIntent);
```

<var translate="no"><code translate="no" dir="ltr">settings_panel_type</code></var> can be one of:

[`ACTION_INTERNET_CONNECTIVITY`](https://developer.android.com/reference/android/provider/Settings.Panel#ACTION_INTERNET_CONNECTIVITY)
:   Shows settings related to internet connectivity, such as Airplane mode, Wi-Fi,
    and Mobile Data.

[`ACTION_WIFI`](https://developer.android.com/reference/android/provider/Settings.Panel#ACTION_WIFI)
:   Shows Wi-Fi settings, but *not* the other connectivity settings. This is
    useful for apps that need a Wi-Fi connection to perform large uploads or
    downloads.

[`ACTION_NFC`](https://developer.android.com/reference/android/provider/Settings.Panel#ACTION_NFC)
:   Shows all settings related to near-field communication *(NFC).*

[`ACTION_VOLUME`](https://developer.android.com/reference/android/provider/Settings.Panel#ACTION_VOLUME)
:   Shows volume settings for all audio streams.

### Sharing improvements

Android 10 provides a number of improvements to sharing:

#### Sharing Shortcuts API

The [Sharing Shortcuts API](https://developer.android.com/training/sharing/receive#sharing-shortcuts-api)
replaces the [Direct Share
APIs](https://developer.android.com/about/versions/marshmallow/android-6.0#direct-share).

Instead of retrieving results reactively on demand, the Sharing Shortcuts API
lets apps publish direct share targets in advance. This is how
the [`ShortcutManager`](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts) works.
Since the two APIs are similar, we have expanded the [`ShortcutInfo`
API](https://developer.android.com/reference/android/content/pm/ShortcutInfo) to make using both
features easier. With the Sharing Shortcuts API, you can directly assign
categories or people to a share target. The share targets persist in the system
until the same app updates them or the app is uninstalled.

The older Direct Share mechanism still works, but apps that use it have a lower
priority than apps using the Sharing Shortcuts API.

[`ShortcutInfo.Builder`](https://developer.android.com/reference/android/content/pm/ShortcutInfo.Builder)
adds and enhances methods to provide additional info about the share target.

#### Direct share targets

You can publish a dynamic shortcut as a Direct Share Target.
See [Publish direct share targets](https://developer.android.com/training/sharing/receive#publish-direct-share-targets).

[`ShortcutManagerCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat)
is a new AndroidX API that provides backwards compatibility with the old DirectShare API. This
is the preferred way to publish share targets.

#### Previewing text

When an app shares text content, it can show an optional preview of
the content in the Sharesheet UI.

See [Adding rich text previews](https://developer.android.com/training/sharing/send#adding-rich-content-previews)

#### Learn more

For more information on how apps can share data,
see [Sending simple data to other apps](https://developer.android.com/training/sharing/send) and
[Receiving simple data from other apps](https://developer.android.com/training/sharing/receive)

### Dark theme

Android 10 offers a Dark theme that applies to both the Android
system UI and apps running on the device. For full information,
see [Dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme).

## Foreground service types

Android 10 introduces the
[`foregroundServiceType`](https://developer.android.com/reference/android/R.attr#foregroundServiceType)
XML manifest attribute, which you include in the definition of several specific
services. It's possible, though rarely appropriate, to assign multiple
foreground service types to a particular service.

The following table shows the different foreground service types and the
services where it's appropriate to declare a specific type:

| Foreground service type | Example use case for a service that should declare this type |
|---|---|
| `connectedDevice` | Monitor a wearable fitness tracker |
| `dataSync` | Download files from a network |
| `location` | [Continue a user-initiated action](https://developer.android.com/training/location/request-updates#continuation-user-initiated-action) |
| `mediaPlayback` | Play an audio book, podcast, or music |
| `mediaProjection` | Record a video of the device's display over a short period of time |
| `phoneCall` | Handle ongoing phone call |

## Kotlin

Android 10 includes the following updates for Kotlin development.

### Nullability annotations for libcore APIs

Android 10 improves the coverage of nullability annotations in
the SDK for libcore APIs. These annotations enable app developers who are using
either Kotlin or Java nullability analysis in Android Studio to get nullness
information when interacting with these APIs.

Normally, nullability contract violations in Kotlin result in compilation
errors. To ensure compatibility with your existing code, only the
`@RecentlyNullable` and `@RecentlyNonNull` annotations are added. This means
that nullability violations result in warnings instead of errors.

In addition, any `@RecentlyNullable` or `@RecentlyNonNull` annotations that were
added in Android 9 are changing to `@Nullable` and `@NonNull`, respectively.
This means that, in Android 10 and higher, nullability violations
lead to errors instead of warnings.

For more information about annotation changes, see
[Android Pie SDK is now more Kotlin-friendly](https://android-developers.googleblog.com/2018/08/android-pie-sdk-is-now-more-kotlin.html)
on the Android Developers Blog.

## NDK

Android 10 includes the following NDK changes.

### Improved debugging of file descriptor ownership

Android 10 adds fdsan, which helps you find and fix file descriptor ownership
issues more easily.

Bugs related to mishandling of file descriptor ownership, which tend to manifest
as *use-after-close* and *double-close* , are analogous to the memory allocation
*use-after-free* and *double-free* bugs, but tend to be much more difficult to
diagnose and fix. *fdsan* attempts to detect and/or prevent file descriptor
mismanagement by enforcing file descriptor ownership.

For more information about crashes related to these issues, see
[Error detected by fdsan](https://source.android.com/devices/tech/debug/native-crash#fdsan).
For more information about fdsan, see the
[Googlesource page on fdsan](https://android.googlesource.com/platform/bionic/+/master/docs/fdsan.md).

### ELF TLS

Applications built using the NDK with a minimum API level 29 can use ELF TLS
instead of `emutls`. Dynamic and static linker support has been added to support
this method of handling thread-local variables.

For apps built for API level 28 and lower, improvements have been implemented
for `libgcc/compiler-rt` to work around some `emutls` issues.

For more information, see
[Android changes for NDK developers](https://android.googlesource.com/platform/bionic/+/master/android-changes-for-ndk-developers.md).

## Runtime

Android 10 includes the following runtime change.

### Mallinfo-based garbage collection triggering

When small platform Java objects reference huge objects in the C++ heap, the
C++ objects can often be reclaimed only when the Java object is collected and,
for example, finalized. In previous releases, the platform estimated the sizes
of many C++ objects associated with Java objects. This estimation was not always
accurate and occasionally resulted in greatly increased memory usage, as the
platform failed to garbage collect when it should have.

In Android 10, the garbage collector (GC) tracks the total size
of the heap allocated by system `malloc()`, ensuring that large `malloc()`
allocations are always included in GC-triggering calculations. Apps interleaving
large numbers of C++ allocations with Java execution might see an increase in
garbage collection frequency as a result. Other apps might see a small decrease.

## Testing and debugging

Android 10 includes the following improvements for testing and debugging.

### Improvements for on-device system tracing

As of Android 10, you can specify limits for the size and
duration of a trace when you perform an
[on-device system trace](https://developer.android.com/topic/performance/tracing/on-device). When you specify
either value, the system performs a long trace, periodically copying the trace
buffer to the destination file while the trace is recorded. The trace completes
when the size or duration limits that you specified are reached.

Use these additional parameters to test different use cases than you would test
with a standard trace. For example, you might be diagnosing a performance bug
that only occurs after your app has been running for a long period of time. In
this case, you could record a long trace over an entire day, and then analyze
the CPU scheduler, disk activity, app threads, and other data in the report to
help you determine the cause of the bug.

In Android 10 and higher, trace files are saved in a format that
can be opened with [Perfetto](https://ui.perfetto.dev/#!/), an
open-source project for performance instrumentation and tracing. You can
[convert Perfetto trace files to the Systrace
format](https://docs.perfetto.dev/#/traceconv.md).

## TextClassifier improvements

Android 10 provides additional text classification functionality in the
[`TextClassifier`](https://developer.android.com/reference/android/view/textclassifier/TextClassifier)
interface.

### Language detection

The
[`detectLanguage()`](https://developer.android.com/reference/android/view/textclassifier/TextClassifier#detectLanguage(android.view.textclassifier.TextLanguage.Request))
method works similarly to previously-existing classification methods. It
receives a
[`TextLanguage.Request`](https://developer.android.com/reference/android/view/textclassifier/TextLanguage.Request)
object and returns a
[`TextLanguage`](https://developer.android.com/reference/android/view/textclassifier/TextLanguage)
object.

`TextLanguage` objects consist of a list of ordered pairs. Each pair
contains a locale and a corresponding confidence score for the classification.

### Suggested conversation actions

The
[`suggestConversationActions()`](https://developer.android.com/reference/android/view/textclassifier/TextClassifier#suggestConversationActions(android.view.textclassifier.ConversationActions.Request))
method works similarly to existing classification methods. It receives a
[`ConversationActions.Request`](https://developer.android.com/reference/android/view/textclassifier/ConversationActions.Request)
object and returns a
[`ConversationActions`](https://developer.android.com/reference/android/view/textclassifier/ConversationActions)
object.

[`ConversationActions`](https://developer.android.com/reference/android/view/textclassifier/ConversationActions)
objects consist of a list of
[`ConversationAction`](https://developer.android.com/reference/android/view/textclassifier/ConversationAction)
objects. Each `ConversationAction` object includes a potential
suggested action and its confidence score.

## Smart replies/actions in notifications

Android 9 introduced the ability to display suggested replies within a notification. Android 10 expands on this with the ability to include suggested intent-based actions. Furthermore, the platform is able to generate these suggestions automatically. Apps can still provide their own suggestions, or opt out of system-generated suggestions.

<br />

The API used to generate these replies is part of
[`TextClassifier`](https://developer.android.com/reference/android/view/textclassifier/TextClassifier),
and has also been directly exposed to developers in Android 10.
Please read [the section on TextClassifier improvements](https://developer.android.com/about/versions/10/features#textclass)
for more information.

If your app provides its own suggestions, the platform doesn't generate any
automatic suggestions. If you don't want your app's notifications to display
any suggested replies or actions, you can opt out of system-generated replies
and actions by using
[`setAllowGeneratedReplies()`](https://developer.android.com/reference/android/app/Notification.Action.Builder#setAllowGeneratedReplies(boolean))
and
[`setAllowSystemGeneratedContextualActions()`](https://developer.android.com/reference/android/app/Notification.Builder#setAllowSystemGeneratedContextualActions(boolean)).