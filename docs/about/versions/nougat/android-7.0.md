---
title: https://developer.android.com/about/versions/nougat/android-7.0
url: https://developer.android.com/about/versions/nougat/android-7.0
source: md.txt
---

Android 7.0 Nougat introduces a variety of
new features and capabilities for users and developers.
This document highlights what's new for developers.

Make sure check out the
[Android 7.0 behavior changes](https://developer.android.com/about/versions/nougat/android-7.0-changes) to learn about areas where platform changes
may affect your apps.

To learn more about
the consumer features of Android 7.0, visit [www.android.com](https://www.android.com).

## Multi-window Support

In Android 7.0, we're introducing a new and much-requested
multitasking feature into the platform --- multi-window support.

Users can now pop open two apps on the screen at once.

- On phones and tablets running Android 7.0, users can run two apps side-by-side or one-above-the-other in splitscreen mode. Users can resize the apps by dragging the divider between them.
- On Android TV devices, apps can put themselves in [picture-in-picture
  mode](https://developer.android.com/guide/topics/ui/picture-in-picture), allowing them to continue showing content while the user browses or interacts with other apps.

![Mobile running apps in split screen mode](https://developer.android.com/static/images/android-7.0/mw-portrait.png)


**Figure 1.** Apps running in split-screen mode.

Especially on tablets and other larger-screen devices, multi-window support
gives you new ways to engage users. You can even enable drag-and-drop in
your app to let users conveniently drag content to or from your app --- a great
way to enhance your user experience.

It's straightforward to add multi-window support to your app and configure how it
handles multi-window display. For example, you can specify your activity's
minimum allowable dimensions, preventing users from resizing the activity below
that size. You can also disable multi-window display for your app, which
ensures that the system will only show your app in full-screen mode.


For more information, see the [Multi-Window Support](https://developer.android.com/guide/topics/ui/multi-window)
developer documentation.

## Notification Enhancements

In Android 7.0 we've redesigned notifications to make them easier and
faster to use. Some of the changes include:

- **Template updates**: We're updating notification templates to put a new emphasis on hero image and avatar. Developers will be able to take advantage of the new templates with minimal adjustments in their code.
- **Messaging style customization** : You can customize more of the user interface labels associated with your notifications using the `MessagingStyle` class. You can configure the message, conversation title, and content view.
- **Bundled notifications**: The system can group messages together, for example by message topic, and display the group. A user can take actions, such as Dismiss or Archive, on them in place. If you've implemented notifications for Android Wear, you'll already be familiar with this model.
- **Direct reply**: For real-time communication apps, the Android system supports inline replies so that users can quickly respond to an SMS or text message directly within the notification interface.
- **Custom views**: Two new APIs enable you to leverage system decorations, such as notification headers and actions, when using custom views in notifications.

![Mobile displaying bundled message notifications](https://developer.android.com/static/images/android-7.0/notifications-1.png) ![Mobile displaying single message notification](https://developer.android.com/static/images/android-7.0/notifications-3.png) ![Mobile displaying inline message reply within notification interface](https://developer.android.com/static/images/android-7.0/notifications-2.png)


**Figure 2.** Bundled notifications and direct reply.

To learn how to implement the new features, see the
[Notifications](https://developer.android.com/guide/topics/ui/notifiers/notifications)
guide.

## Profile-guided JIT/AOT Compilation

In Android 7.0, we've added a Just in Time (JIT) compiler with code
profiling to ART, which lets it constantly improve the performance of
Android apps as they run. The JIT compiler complements ART's current
Ahead of Time (AOT) compiler and helps improve runtime performance, save
storage space, and speed up app updates and system updates.

Profile-guided compilation lets ART manage the AOT/JIT compilation for
each app according to its actual usage, as well as conditions on the device.
For example, ART maintains a profile of each app's hot methods and can
precompile and cache those methods for best performance. It leaves other parts
of the app uncompiled until they are actually used.

Besides improving performance for key parts of the app, profile-guided
compilation helps reduce an app's overall RAM footprint, including associated
binaries. This feature is especially important on low-memory devices.

ART manages profile-guided compilation in a way that minimizes impact on the
device battery. It does precompilation only when then the device is idle and
charging, saving time and battery by doing that work in advance.

## Quick Path to App Install

One of the most tangible benefits of ART's JIT compiler is the speed of app
installs and system updates. Even large apps that required several minutes to
optimize and install in Android 6.0 can now install in just a matter of
seconds. System updates are also faster, since there's no more optimizing step.

## Doze on the Go...

Android 6.0 introduced Doze, a system mode that saves battery by deferring
apps' CPU and network activities when the device is idle, such as when it's
sitting on a table or in a drawer.

Now in Android 7.0, Doze takes a step further and saves battery while on the go.
Any time the screen is off for a period of time and the device is unplugged,
Doze applies a subset of the familiar CPU and network restrictions to apps.
This means users can save battery even when carrying their devices in their
pockets.
![Illustration of how Doze applies a first level of system activity restrictions to improve battery life](https://developer.android.com/static/images/android-7.0/doze-diagram-1.png)


**Figure 3.** Doze now applies
restrictions to improve battery life even when the device is not stationary.

A short time after the screen turns off while the device is on battery, Doze
restricts network access and defers jobs and syncs. During brief maintenance
windows, applications are allowed network access and any of their deferred
jobs/syncs are executed. Turning the screen on or plugging in the device brings
the device out of Doze.

When the device is stationary again, with screen off and on battery for a
period of time, Doze applies the full CPU and network restrictions on `https://developer.android.com/reference/android/os/PowerManager.WakeLock`, `https://developer.android.com/reference/android/app/AlarmManager` alarms, and
GPS/Wi-Fi scans.

The best practices for adapting your app to Doze are the same whether the
device is moving or not, so if you already updated your app to gracefully
handle Doze, you're all set. If not, start [adapting
your app to Doze](https://developer.android.com/training/monitoring-device-state/doze-standby#assessing_your_app) now.

## Project Svelte: Background Optimizations

Project Svelte is an ongoing effort to minimize RAM use by system and apps
across the range of Android devices in the ecosystem. In Android 7.0, Project
Svelte is focused on optimizing the way apps run in the background.

Background processing is an essential part of most apps. When handled right, it
can make your user experience amazing --- immediate, fast, and context-aware.
When not handled right, background processing can needlessly consume RAM (and
battery) and affect system performance for other apps.

Since Android 5.0, `https://developer.android.com/reference/android/app/job/JobScheduler` has been the
preferred way of performing background work in a way that's good
for users. Apps can schedule jobs while letting the system optimize based on
memory, power, and connectivity conditions. JobScheduler offers control and
simplicity, and we want all apps to use it.


Another good option is [`GCMNetworkManager`](https://developers.google.com/android/reference/com/google/android/gms/gcm/GcmNetworkManager), part of Google Play Services, which
offers similar job scheduling with compatibility across legacy versions of
Android.

We're continuing to extend `JobScheduler` and
`GCMNetworkManager` to meet more of
your use cases --- for example, in Android 7.0 you can now schedule background
work based on changes in Content Providers. At the same time we're starting to
deprecate some of the older patterns that can reduce system performance,
especially on low-memory devices.

In Android 7.0 we're removing three commonly-used implicit broadcasts ---
`https://developer.android.com/reference/android/net/ConnectivityManager#CONNECTIVITY_ACTION`, `https://developer.android.com/reference/android/hardware/Camera#ACTION_NEW_PICTURE`, and `https://developer.android.com/reference/android/hardware/Camera#ACTION_NEW_VIDEO` --- since those can wake the
background processes of multiple apps at once and strain memory and battery. If
your app is receiving these, take advantage of the Android 7.0 to
migrate to `JobScheduler` and related APIs instead.


Take a look at the [Background
Optimizations](https://developer.android.com/topic/performance/background-optimization) documentation for details.

## SurfaceView


Android 7.0 brings synchronous movement to the `https://developer.android.com/reference/android/view/SurfaceView`
class, which provides better battery performance
than `https://developer.android.com/reference/android/view/TextureView` in certain cases: When rendering video or
3D content, apps with scrolling and animated video position use less power with
`https://developer.android.com/reference/android/view/SurfaceView` than with `https://developer.android.com/reference/android/view/TextureView`.
The `https://developer.android.com/reference/android/view/SurfaceView` class enables more battery-efficient compositing on screen, because it is composited in dedicated hardware, separately from app window content. As a result, it makes fewer intermediate copies than `https://developer.android.com/reference/android/view/TextureView`.

<br />


A `https://developer.android.com/reference/android/view/SurfaceView` object's content position is now updated synchronously
with the containing app content. One result of this change is that simple
translations or scales of a video playing in a `https://developer.android.com/reference/android/view/SurfaceView`
no longer produce black bars alongside the view as it moves.


Starting with Android 7.0, we strongly recommend that you save power by using
`https://developer.android.com/reference/android/view/SurfaceView` instead of `https://developer.android.com/reference/android/view/TextureView`.

## Data Saver

![Data Saver in Settings](https://developer.android.com/static/images/android-7.0/datasaver.png)


**Figure 4.** Data Saver in Settings.

Over the life of a mobile device, the cost of a cellular data plan typically
exceeds the cost of the device itself. For many users, cellular data is an
expensive resource that they want to conserve.

Android 7.0 introduces Data Saver mode, a new system service that helps reduce
cellular data use by apps, whether roaming, near the end of the billing cycle,
or on a small prepaid data pack. Data Saver gives users control over how apps
use cellular data and lets developers provide more efficient service when Data
Saver is on.

When a user enables Data Saver in **Settings** and the device is
on a metered network, the system blocks background data usage and signals apps
to use less data in the foreground wherever possible --- such as by limiting
bit rate for streaming, reducing image quality, deferring optimistic precaching,
and so on. Users can allow specific apps to allow background metered data
usage even when Data Saver is turned on.

Android 7.0 extends the `https://developer.android.com/reference/android/net/ConnectivityManager` to provide apps a
way to [retrieve the
user's Data Saver preferences](https://developer.android.com/training/basics/network-ops/data-saver#status) and [monitor
preference changes](https://developer.android.com/training/basics/network-ops/data-saver#monitor-changes). All apps should check whether the user has enabled Data
Saver and make an effort to limit foreground and background data usage.

## Vulkan API


Android 7.0 integrates [Vulkan™](http://www.khronos.org/vulkan), a new 3D rendering API, into the platform. Like
[OpenGL™
ES](https://www.khronos.org/opengles/), Vulkan is an open standard for 3D graphics and rendering maintained
by the Khronos Group.


Vulkan is designed from the ground up to minimize CPU overhead in the driver,
and allow your application to control GPU operation more directly. Vulkan
also enables better parallelization by allowing multiple threads to perform
work such as command buffer construction at once.


Vulkan development tools and libraries are rolled into the Android 7.0 SDK. They
include:

- Headers
- Validation layers (debug libraries)
- SPIR-V shader compiler
- SPIR-V runtime shader compilation library


Vulkan is only available to apps on devices with Vulkan-capable hardware,
such as Nexus 5X, Nexus 6P, and Nexus Player. We're working closely with our
partners to bring Vulkan to more devices as soon as possible.


For more information, see the [API documentation](https://developer.android.com/ndk/guides/graphics).

## Quick Settings Tile API

![Quick Settings tiles in the notification shade](https://developer.android.com/static/images/android-7.0/quicksettings.png)


**Figure 5.** Quick Settings tiles in the notification shade.

Quick Settings is a popular and simple way to expose key settings and actions,
directly from the notification shade. In Android 7.0, we've expanded the scope of
Quick Settings to make it even more useful and convenient.

We've added more room for additional Quick Settings tiles, which users can
access across a paginated display area by swiping left or right. We've also
given users control over what Quick Settings tiles appear and where they are
displayed --- users can add or move tiles just by dragging and dropping them.

For developers, Android 7.0 also adds a new API that lets you define your own
Quick Settings tiles to give users easy access to key controls and actions in your app.


Quick Settings tiles are reserved for controls or actions that are either
urgently required or frequently used, and should not be used as shortcuts to
launching an app.


Once you've defined your tiles, you can surface them to users, who can add
them to Quick Settings just by drag and drop.


For information about creating an app tile, see the reference documentation
for `https://developer.android.com/reference/android/service/quicksettings/Tile`.

## Number Blocking

Android 7.0 now supports number blocking in the platform and provides a
framework API to let service providers maintain a blocked-number list. The
default SMS app, the default phone app, and carrier apps can read from and
write to the blocked-number list. The list is not accessible to other apps.

By making number blocking a standard feature of the platform, Android provides
a consistent way for apps to support number blocking across a wide range of
devices. Among the other benefits that apps can take advantage of are:

- Numbers blocked on calls are also blocked on texts
- Blocked numbers can persist across resets and devices through the Backup \& Restore feature
- Multiple apps can use the same blocked numbers list

Additionally, carrier app integration through Android means that carriers can
read the blocked numbers list on the device and perform service-side blocking
for the user in order to stop unwanted calls and texts from reaching the user
through any medium, such as a VOIP endpoint or forwarding phones.


For more information, see the reference documentation for
`https://developer.android.com/reference/android/provider/BlockedNumberContract`.

## Call Screening


Android 7.0 allows the default phone app to screen incoming calls. The phone
app does this by implementing the new `CallScreeningService`,
which allows the phone app to perform a number of actions based on an
incoming call's `https://developer.android.com/reference/android/telecom/Call.Details`, such as:

- Reject the incoming call
- Do not allow the call to the call log
- Do not show the user a notification for the call


For more information, see the reference documentation for
`https://developer.android.com/reference/android/telecom/CallScreeningService`.

## Multi-locale Support, More Languages

Android 7.0 now lets users select **multiple locales** in Settings,
to better support bilingual use-cases. Apps can use
a new API to get the user's selected locales and then offer more sophisticated
user experiences for multi-locale users --- such as showing search results in
multiple languages and not offering to translate webpages in a language the
user already knows.

Along with multi-locale support, Android 7.0 also expands the range of languages
available to users. It offers more than 25 variants each for commonly used
languages such as English, Spanish, French, and Arabic. It also adds partial
support for more than 100 new languages.

Apps can get the list of locales set by the user by calling
`LocaleList.GetDefault()`. To support the expanded number of locales, Android 7.0 is
changing the way that it resolves resources. Make sure that you test and verify that your apps
working as expected with the new resource resolution logic.

To learn about the new resource-resolution behavior and the best practices you
should follow, see [Multilingual Support](https://developer.android.com/guide/topics/resources/multilingual-support).

## New Emojis


Android 7.0 introduces additional emojis and emoji-related features including
skin tone emojis and support for variation
selectors. If your app supports emojis,
follow the guidelines below to take advantage of these emoji-related features.

- **Check that a device contains an emoji before inserting it.** To check which emojis are present in the system font, use the `https://developer.android.com/reference/android/graphics/Paint#hasGlyph(java.lang.String)` method.
- **Check that an emoji supports variation selectors.** Variation selectors allow you to present certain emojis in color or in black-and-white. On mobile devices, apps should represent emojis in color rather than black-and-white. However, if your app displays emojis inline with text, then it should use the black-and-white variation. To determine whether an emoji has a variation, use the variation selector. For a complete list of characters with variations, review the *emoji variation sequences* section of the [Unicode documentation on variations](https://www.unicode.org/Public/UNIDATA/StandardizedVariants.txt).
- **Check that an emoji supports skin tone.** Android 7.0 allows users to modify the rendered skin tone of emojis to their preference. Keyboard apps should provide visual indications for emojis that have multiple skin tones and should allow users to select the skin tone that they prefer. To determine which system emojis have skin tone modifiers, use the `https://developer.android.com/reference/android/graphics/Paint#hasGlyph(java.lang.String)` method. You can determine which emojis use skin tones by reading the [Unicode documentation](http://unicode.org/emoji/charts/full-emoji-list.html).

## ICU4J APIs in Android


Android 7.0 now offers a subset of [ICU4J](http://site.icu-project.org/) APIs in the Android framework under
the `android.icu` package. Migration is easy, and mostly entails
simply changing from the `com.java.icu` namespace to
`android.icu`. If you are already using an ICU4J bundle in your
apps, switching to the `android.icu` APIs provided in the Android
framework can produce substantial savings in APK size.


To learn more about the Android ICU4J APIs, see [ICU4J Support](https://developer.android.com/guide/topics/resources/internationalization#nougat).

## WebView

### Chrome + WebView, Together


Starting with Chrome version 51 on Android 7.0 and above, the Chrome APK on your device
is used to provide and render Android System WebViews. This approach improves memory
usage on the device itself and also reduces the bandwidth required to keep
WebView up to date (as the standalone WebView APK will no longer be updated
as long as Chrome remains enabled).


You can choose your WebView provider by enabling Developer Options and
selecting **WebView implementation**. You can use any compatible
Chrome version (Dev, Beta or Stable) that is installed on your device or the
standalone Webview APK to act as the WebView implementation.

### Multiprocess


Starting with Chrome version 51 in Android 7.0, WebView will run web content in a
separate sandboxed process when the developer option "Multiprocess WebView"
is enabled.


We're looking for feedback on compatibility and runtime performance in N
before enabling multiprocess WebView in a future version of Android. In this
version, regressions in startup time, total memory usage and software
rendering performance are expected.


If you find unexpected issues in multiprocess mode we'd like to hear about
them. Please get in touch with the WebView team on the [Chromium bug tracker](https://bugs.chromium.org/p/chromium/issues/entry?template=Webview+Bugs).

### Javascript run before page load


Starting with apps targeting Android 7.0, the Javascript context will be reset
when a new page is loaded. Currently, the context is carried over for the
first page loaded in a new WebView instance.


Developers looking to inject Javascript into the WebView should execute the
script after the page has started to load.

### Geolocation on insecure origins


Starting with apps targeting Android 7.0, the geolocation API will only be
allowed on secure origins (over HTTPS.) This policy is designed to protect
users' private information when they're using an insecure connection.

### Testing with WebView Beta


WebView is updated regularly, so we recommend that you test compatibility
with your app frequently using WebView's beta channel. To get started testing
pre-release versions of WebView on Android 7.0, download and install either
Chrome Dev or Chrome Beta, and select it as the WebView implementation under
developer options as described above. Please report issues via the [Chromium
bug tracker](https://bugs.chromium.org/p/chromium/issues/entry?template=Webview+Bugs) so that we can fix them before a new version of WebView is
released.

## OpenGL™ ES 3.2 API

Android 7.0 adds framework interfaces and platform support for OpenGL ES 3.2, including:

- All extensions from the [Android Extension Pack](https://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt) (AEP) except for `EXT_texture_sRGB_decode`.
- Floating-point framebuffers for HDR and deferred shading.
- BaseVertex draw calls to enable better batching and streaming.
- Robust buffer access control to reduce WebGL overhead.

The framework API for OpenGL ES 3.2 on Android 7.0 is provided with the
`GLES32` class. When using OpenGL ES 3.2, be sure to declare the
requirement in your manifest file, using the `<uses-feature>` tag and
the `android:glEsVersion` attribute.

For information about using OpenGL ES, including how to check a device's
supported OpenGL ES version at runtime, see the [OpenGL ES API guide](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl).

## Android TV Recording

Android 7.0 adds the ability to record and playback content from Android TV input
services via new recording APIs. Building on top of existing time-shifting
APIs, TV input services can control what channel data can be recorded, how
recorded sessions are saved, and manage user interaction with recorded content.

For more information, see [Android TV Recording APIs](https://developer.android.com/training/tv/tif/content-recording).

## Android for Work

Android for Work adds many new features and APIs for devices running Android 7.0.
Some highlights are below --- for a complete list of features, see
[Android Enterprise feature
list](https://developers.google.com/android/work/requirements).

### Work profile security challenge


Profile owners targeting the N SDK
can specify a separate security challenge for apps running in
the work profile. The work challenge is shown when a user attempts to open
any work apps. Successful completion of the security challenge unlocks the
work profile and decrypts it if necessary. For profile owners,
`ACTION_SET_NEW_PASSWORD` prompts the user to set a work
challenge, and `ACTION_SET_NEW_PARENT_PROFILE_PASSWORD` prompts
the user to set a device lock.


Profile owners can set distinct passcode policies for the work challenge
(such as how long the PIN needs to be, or whether a fingerprint can be used
to unlock the profile) using the `setPasswordQuality()`,
`setPasswordMinimumLength()` and related methods. The profile
owner can also set the device lock using the `DevicePolicyManager`
instance returned by the new `getParentProfileInstance()` method.
Additionally, profile owners can customize the credentials screen for the
work challenge using the new `setOrganizationColor()` and
`setOrganizationName()` methods.

### Turn off work

On a device with a work profile, users can toggle work mode. When work mode is
off the managed user is temporarily shut down, which disables work profile
apps, background sync, and notifications. This includes the profile owner
application. When work mode is off, the system displays a persistent status
icon to remind the user that they can't launch work apps. The launcher
indicates that work apps and widgets are not accessible.

### Always on VPN

Device owners and profile owners can ensure that work apps always connect
through a specified VPN. The system automatically starts that VPN after the
device boots.


New `DevicePolicyManager` methods are
`setAlwaysOnVpnPackage()` and
`getAlwaysOnVpnPackage()`.

Because VPN services can be bound directly by the system without app
interaction, VPN clients need to handle new entry points for Always on VPN. As
before, services are indicated to the system by an intent filter matching
action `android.net.VpnService`.


Users can also manually set Always on VPN clients that implement
`VPNService` methods using
**Settings\>More\>Vpn**. The option to enable Always on VPN
from Settings is available only if VPN client targets API level 24.

### Customized provisioning


An application can customize the profile owner and device owner provisioning
flows with corporate colors and logos.
`DevicePolicyManager.EXTRA_PROVISIONING_MAIN_COLOR` customizes
flow color. `DevicePolicyManager.EXTRA_PROVISIONING_LOGO_URI`
customizes the flow with a corporate logo.

## Accessibility Enhancements

Android 7.0 now offers Vision Settings directly on the Welcome screen for new
device setup. This makes it much easier for users to discover and configure
accessibility features on their devices, including magnification gesture, font
size, display size, and TalkBack.

With these accessibility features getting more prominent placement, your users
are more likely to try your app with them enabled. Make sure you test your apps
early with these settings enabled. You can enable them from Settings \>
Accessibility.

Also in Android 7.0, accessibility services can now help users with motor
impairments to touch the screen. The new API allows building services with
features such as face-tracking, eye-tracking, point scanning, and so on, to
meet the needs of those users.

For more information, see the reference documentation for
`https://developer.android.com/reference/android/accessibilityservice/GestureDescription`.

## Direct Boot

Direct boot improves device startup times and lets registered
apps have limited functionality even after an unexpected reboot.
For example, if an encrypted device reboots while the user is sleeping,
registered alarms, messages and incoming calls can now continue to notify
the user as normal. This also means accessibility services can also be
available immediately after a restart.

Direct boot takes advantage of file based encryption in Android 7.0
to enable fine grained encryption policies for both system and app data.
The system uses a device-encrypted store for select system data and explicitly
registered app data. By default a credential-encrypted store is used for all
other system data, user data, apps, and app data.

At boot, the system starts in a restricted mode with access to
device-encrypted data only, and without general access to apps or data.
If you have components that you want to run in this mode, you can register
them by setting a flag in the manifest. After restart, the system activates
registered components by broadcasting the `LOCKED_BOOT_COMPLETED`
intent. The system ensures registered device-encrypted app data is available
before unlock. All other data is unavailable until the User confirms their lock
screen credentials to decrypt it.
For more information, see [Direct Boot](https://developer.android.com/training/articles/direct-boot).

<br />

<br />

## Key Attestation


Android 7.0 introduces *key attestation* , a new security tool that helps
you make sure that the key pairs stored within a device's [*hardware-backed
keystore*](https://source.android.com/security/keystore/) properly protect the sensitive information that your app
uses. By using this tool, you gain additional confidence that your app
interacts with keys that reside in secure hardware, even if the device
running your app is rooted. If you use keys from the hardware-backed keystore
in your apps, you should use this tool, particularly if you use the keys to
verify sensitive information within your app.


Key attestation allows you to verify that an RSA or EC key pair has been
created and stored in a device's hardware-backed keystore within the device's
trusted execution environment (TEE). The tool also allows you to use an
off-device service, such as your app's back-end server, to determine and
strongly verify the uses and validity of the key pair. These features provide
an additional level of security that protects the key pair, even if someone
roots the device or compromises the security of the Android platform running
on the device.


**Note:** Only a small number of devices running Android 7.0
support hardware-level key attestation; all other devices running Android 7.0
use software-level key attestation instead. Before you verify the properties
of a device's hardware-backed keys in a production-level environment, you
should make sure that the device supports hardware-level key attestation. To
do so, you should check that the attestation certificate chain contains a root
certificate that is signed by the Google attestation root key and that the
`attestationSecurityLevel` element within the [key
description](https://developer.android.com/training/articles/security-key-attestation#certificate_schema_keydescription) data structure is set to the TrustedEnvironment security
level.


For more information, see the
[Key Attestation](https://developer.android.com/training/articles/security-key-attestation)
developer documentation.

## Network Security Config

In Android 7.0, apps can customize the behavior of their secure (HTTPS, TLS)
connections safely, without any code modification, by using the declarative
*Network Security Config* instead of using the conventional
error-prone programmatic APIs (e.g. X509TrustManager).

Supported features:

- **Custom trust anchors.** Lets an application customize which Certificate Authorities (CA) are trusted for its secure connections. For example, trusting particular self-signed certificates or a restricted set of public CAs.
- **Debug-only overrides.** Lets an application developer safely debug secure connections of their application without added risk to the installed base.
- **Cleartext traffic opt-out.** Lets an application protect itself from accidental usage of cleartext traffic.
- **Certificate pinning.** An advanced feature that lets an application limit which server keys are trusted for secure connections.

For more information, see [Network security configuration](https://developer.android.com/training/articles/security-config).

## Default Trusted Certificate Authority

By default, apps that target Android 7.0 only trust system-provided certificates
and no longer trust user-added Certificate Authorities (CA). Apps targeting Android 7.0
(API level 24) that wish to trust user-added CAs should use the
[Network security configuration](https://developer.android.com/training/articles/security-config) to
specify how user CAs should be trusted.

## APK Signature Scheme v2


Android 7.0 introduces APK Signature Scheme v2, a new app-signing scheme that
offers faster app install times and more protection against unauthorized
alterations to APK files. By default, Android Studio 2.2 and the Android
Plugin for Gradle 2.2 sign your app using both APK Signature Scheme v2 and
the traditional signing scheme, which uses JAR signing.


Although we recommend applying APK Signature Scheme v2 to your app, this new
scheme is not mandatory. If your app doesn't build properly when using APK
Signature Scheme v2, you can disable the new scheme. The disabling process
causes Android Studio 2.2 and the Android Plugin for Gradle 2.2 to sign your
app using only the traditional signing scheme. To sign with only the
traditional scheme, open the module-level `build.gradle` file, then
add the line `v2SigningEnabled false` to your release signing
configuration:

```text
  android {
    ...
    defaultConfig { ... }
    signingConfigs {
      release {
        storeFile file("myreleasekey.keystore")
        storePassword "password"
        keyAlias "MyReleaseKey"
        keyPassword "password"
        v2SigningEnabled false
      }
    }
  }
```

**Caution:** If you sign your app using APK
Signature Scheme v2 and make further changes to the app, the app's signature
is invalidated. For this reason, use tools such as `zipalign`
before signing your app using APK Signature Scheme v2, not after.


For more information, read the Android Studio documents that describe how to
[sign an app](https://developer.android.com/studio/publish/app-signing#release-mode) in Android Studio and how to [configure
the build file for signing apps](https://developer.android.com/studio/build/build-variants#signing) using the Android Plugin for Gradle.

## Scoped Directory Access

In Android 7.0, apps can use new APIs to request access to specific [external
storage](https://developer.android.com/guide/topics/data/data-storage#filesExternal) directories, including directories on removable media such as SD
cards. The new APIs greatly simplify how your application accesses standard
external storage directories, such as the `Pictures` directory. Apps
like photo apps can use these APIs instead of using
`READ_EXTERNAL_STORAGE`, which grants access to all storage
directories, or the Storage Access Framework, which makes the user navigate to
the directory.

Additionally, the new APIs simplify the steps a user takes to grant external
storage access to your app. When you use the new APIs, the system uses a simple
permissions UI that clearly details what directory the application is
requesting access to.

For more information, see the
[Scoped
Directory Access](https://developer.android.com/training/data-storage) developer documentation.

## Keyboard Shortcuts Helper


In Android 7.0, the user can press **Meta + /** to trigger a
*Keyboard Shortcuts* screen that displays all shortcuts available both
from the system and from the app in focus. The system retrieves these
shortcuts automatically from the app's menu if the shortcuts exist. You can
also provide your own fine-tuned shortcuts lists for the screen. You can do
this by overriding the `https://developer.android.com/reference/android/view/Window.Callback#onProvideKeyboardShortcuts(java.util.List<android.view.KeyboardShortcutGroup>, android.view.Menu, int)` method.


**Note:** The **Meta** key is not present on all
keyboards: on a Macintosh keyboard, it is the **Command** key,
on the Windows keyboard, it is the **Windows** key, and on the
Pixel C and the ChromeOS keyboards, it is the **Search** key.


To trigger Keyboard Shortcuts Helper from anywhere in your app, call
`https://developer.android.com/reference/android/app/Activity#requestShowKeyboardShortcuts()`
from the relevant activity.

## Custom Pointer API


Android 7.0 introduces the Custom Pointer API, which lets you customize the
appearance, visibility, and behavior of the pointer. This capability is
especially useful when a user is using a mouse or touchpad to interact with
UI objects. The default pointer uses a standard icon. This API also includes
advanced functionality such as changing the pointer icon's appearance based
on specific mouse or touchpad movements.


To set a pointer icon, override the `onResolvePointerIcon()`
method of the `View` class. This method uses a
`PointerIcon` object to draw the icon that corresponds to a
specific motion event.

## Sustained Performance API


Performance can fluctuate dramatically for long-running apps, because the
system throttles system-on-chip engines as device components reach their
temperature limits. This fluctuation presents a moving target for app
developers creating high-performance, long-running apps.


To address these limitations, Android 7.0 includes support for
*sustained performance mode*, enabling OEMs to provide hints about
device-performance capabilities for long-running apps. App developers
can use these hints to tune apps for a predictable,
consistent level of device performance over long periods of time.


App developers can try out this new API in Android 7.0 on
Nexus 6P devices only. To use this feature,
set the sustained performance window flag for the window
you want to run in sustained performance mode. Set this flag using the
`Window.setSustainedPerformanceMode()` method. The system automatically
disables this mode when the window is no longer in focus.

## VR Support


Android 7.0 adds platform support and optimizations for a new VR Mode to let developers
build high-quality mobile VR experiences for users. There are a number of performance
enhancements, including access to an exclusive CPU core for VR apps.
Within your apps, you can take advantage of intelligent head-tracking,
and stereo notifications that work for VR. Most importantly, Android 7.0 provides for
very low latency graphics. For complete information about building VR apps for Android 7.0,
see the [Google VR SDK for Android](https://developers.google.com/vr/android/).

## Print Service Enhancements


In Android 7.0, print service developers can now surface additional information
about individual printers and print jobs.


When listing individual printers, a print service can now set per-printer
icons in two ways:

- You can set an icon from a resource ID by calling `https://developer.android.com/reference/android/print/PrinterInfo.Builder#setIconResourceId(int)`.
- You can show an icon from the network by calling `https://developer.android.com/reference/android/print/PrinterInfo.Builder#setHasCustomPrinterIcon(boolean)`, and setting a callback for when the icon is requested using `https://developer.android.com/reference/android/printservice/PrinterDiscoverySession#onRequestCustomPrinterIcon(android.print.PrinterId, android.os.CancellationSignal, android.printservice.CustomPrinterIconCallback)`.


In addition, you can provide a per-printer activity to display additional
information by calling `https://developer.android.com/reference/android/print/PrinterInfo.Builder#setInfoIntent(android.app.PendingIntent)`.


You can indicate the progress and status of print jobs in the print job
notification by calling
`https://developer.android.com/reference/android/printservice/PrintJob#setProgress(float)` and
`https://developer.android.com/reference/android/printservice/PrintJob#setStatus(int)`, respectively.

## Frame Metrics API


The Frame Metrics API allows an app to monitor its UI rendering
performance. The API provides this capability by exposing a streaming Pub/Sub API to transfer frame
timing info for the app's current window. The data returned is
equivalent to that which `https://developer.android.com/tools/help/shell#shellcommands
dumpsys gfxinfo framestats` displays, but is not limited to the past 120 frames.


You can use the Frame Metrics API to measure interaction-level UI
performance in production, without a USB connection. This API
allows collection of data at a much higher granularity than does
`adb shell dumpsys gfxinfo`. This higher granularity is possible because
the system can collect data for particular interactions in the app; the system
need not capture a global summary of the entire app's
performance, or clear any global state. You can use this
capability to gather performance data and catch regressions in UI performance
for real use cases within an app.


To monitor a window, implement the
`https://developer.android.com/reference/android/view/Window.OnFrameMetricsAvailableListener#onFrameMetricsAvailable(android.view.Window, android.view.FrameMetrics, int)`
callback method and register it on that window.


The API provides a `https://developer.android.com/reference/android/view/FrameMetrics` object, which
contains timing data that the rendering subsystem reports for various milestones
in a frame lifecycle. The supported metrics are: `UNKNOWN_DELAY_DURATION`,
`INPUT_HANDLING_DURATION`, `ANIMATION_DURATION`,
`LAYOUT_MEASURE_DURATION`, `DRAW_DURATION`, `SYNC_DURATION`,
`COMMAND_ISSUE_DURATION`, `SWAP_BUFFERS_DURATION`,
`TOTAL_DURATION`, and `FIRST_DRAW_FRAME`.

## Virtual Files


In previous versions of Android, your app could use the Storage Access
Framework to allow users to select files from their cloud storage accounts,
such as Google Drive. However, there was no way to represent files that did
not have a direct bytecode representation; every file was required to provide
an input stream.


Android 7.0 adds the concept of *virtual files* to the Storage Access
Framework. The virtual files feature allows your
`https://developer.android.com/reference/android/provider/DocumentsProvider` to return document URIs that can be
used with an `https://developer.android.com/reference/android/content/Intent#ACTION_VIEW` intent even if they
don't have a direct bytecode representation. Android 7.0 also allows you to
provide alternate formats for user files, virtual or otherwise.


For more information about opening virtual files, see
[Open virtual files in the
Storage Access Frameworks guide](https://developer.android.com/guide/topics/providers/document-provider#virtual).