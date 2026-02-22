---
title: https://developer.android.com/about/versions/13/features
url: https://developer.android.com/about/versions/13/features
source: md.txt
---

Android 13 introduces great new features and APIs for developers. The sections
below help you learn about features for your apps and get started with the
related APIs.

For a detailed list of new, modified, and removed APIs, read the
[API diff report](https://developer.android.com/sdk/api_diff/t-dp1/changes). For details on new APIs
visit the [Android API reference](https://developer.android.com/reference) --- new APIs are highlighted for
visibility. Also, to learn about areas where platform changes may
affect your apps, be sure to check out Android 13 behavior changes [for apps
that target Android 13](https://developer.android.com/about/versions/13/behavior-changes-13) and [for all
apps](https://developer.android.com/about/versions/13/behavior-changes-all).

## Developer productivity and tools

### Themed app icons

![User opting into themed app icons](https://developer.android.com/static/images/about/versions/13/themed-app-icons.gif) Opting in to themed app icons on Android 13

Starting with Android 13, you can opt in to themed app icons. With this
feature, app icons in supported Android launchers are tinted to inherit the
coloring of the user's chosen wallpaper and other themes.

To support this feature, your app must provide both an
[adaptive icon](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) and a
monochromatic app icon, and point to the monochromatic app icon from the
`<adaptive-icon>` element in the manifest. If a user has enabled themed app
icons (in other words, turned on the **Themed icons** toggle in system settings),
and the launcher supports this feature, the system uses the coloring of the
user's chosen wallpaper and theme to determine the tint color, which it then
applies to the monochromatic app icon.

The home screen does NOT display the themed app icon---and instead displays
the adaptive or standard app icon---in any of the following scenarios:

- If the user hasn't enabled themed app icons
- If your app doesn't provide a monochromatic app icon
- If the launcher doesn't support themed app icons

For more details and instructions, see [Adaptive icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive).

### Per-app language preferences

![](https://developer.android.com/static/images/about/versions/13/app-languages.png) Per-app languages in system settings

In many cases, multilingual users set their system language to one language---such
as English---but they want to select other languages for specific apps, such as
Dutch, Chinese, or Hindi. To help apps provide a better experience for these
users, Android 13 introduces the following features for apps that support
multiple languages:

- **System settings**: A centralized location where users can select a
  preferred language for each app.

  Your app must declare the `android:localeConfig` attribute in your app's
  manifest to tell the system that it supports multiple languages. To learn
  more, see the instructions for
  [creating a resource file and declaring it in your app's manifest file](https://developer.android.com/guide/topics/resources/app-languages#app-language-settings).
- **Additional APIs** : These public APIs, such as the
  [`setApplicationLocales()`](https://developer.android.com/reference/android/app/LocaleManager#setApplicationLocales(android.os.LocaleList))
  and
  [`getApplicationLocales()`](https://developer.android.com/reference/android/app/LocaleManager#getApplicationLocales())
  methods in [`LocaleManager`](https://developer.android.com/reference/android/app/LocaleManager), let apps
  set a different language from the system language at runtime.

  These APIs automatically sync with system settings; therefore, apps that use these APIs to create custom in-app language pickers will ensure
  their users have a consistent user experience regardless of where they select
  their language preferences. The public APIs also help you reduce the amount
  of boilerplate code, they support split APKs, and they support
  [Auto Backup for Apps](https://developer.android.com/guide/topics/data/autobackup) to store app-level
  user language settings.

  For backward compatibility with previous Android versions, equivalent APIs
  are also available in AndroidX. We recommend using
  [the APIs](https://developer.android.com/guide/topics/resources/app-languages#api-implementation)
  added in [Appcompat 1.6.0-beta01](https://developer.android.com/jetpack/androidx/releases/appcompat#1.6.0-beta01)
  or higher.

Apps that don't support multiple languages are not impacted by these changes.

### Improved text and language support

Android 13 includes several features text and language improvements that help
you deliver a more polished experience, which the following sections describe:

#### Faster hyphenation

Hyphenation makes wrapped text easier to read and helps make your UI more
adaptive. Starting in Android 13, hyphenation performance is optimized by as
much as 200% so you can enable it in your `TextView` with almost no impact on
rendering performance. To enable faster hyphenation, use the
[`fullFast`](https://developer.android.com/reference/android/widget/TextView#attr_android:hyphenationFrequency)
or
[`normalFast`](https://developer.android.com/reference/android/widget/TextView#attr_android:hyphenationFrequency)
frequencies in
[`setHyphenationFrequency()`](https://developer.android.com/reference/android/widget/TextView#setHyphenationFrequency(int)).

#### Text Conversion APIs

People who speak languages like Japanese and Chinese use phonetic lettering
input methods, which often slow down searching and features like auto-
completion. In Android 13, apps can call the new [text conversion
API](https://developer.android.com/reference/android/view/inputmethod/TextAttribute) so users can find what
they're looking for faster and easier. Previously, for example, searching
required a Japanese user to do these steps:

1. Input Hiragana as the phonetic pronunciation of their search term (such as a place or an app name)
2. Use the keyboard to convert the Hiragana characters to Kanji
3. Re-search using the Kanji characters
4. Finally get their search results

With the new text conversion API, Japanese users can type in Hiragana and
immediately see Kanji search results live, skipping steps 2 and 3.

#### Improved line heights for non-latin scripts

Android 13 improves the display of non-Latin scripts (such as Tamil, Burmese,
Telugu, and Tibetan) by using a line height that's adapted for each language.
The new line heights prevent clipping and improve the positioning of characters.
Your app can take advantage of these improvements just by targeting Android 13.
Make sure to test your apps when using the new line spacing because the changes
might affect your UI in non-Latin languages.
![](https://developer.android.com/static/images/about/versions/13/line-heights.png) Line heights that were clipped in Android 12 (above) that are now positioned better and not clipped in Android 13 (below).

#### Improved Japanese text wrapping

Starting in Android 13, TextViews can wrap text by Bunsetsu (the smallest unit of words that sounds
natural) or phrases, instead of by character, for more polished and readable
Japanese applications. You can take advantage of this wrapping by using
[`android:lineBreakWordStyle="phrase"`](https://developer.android.com/reference/android/R.attr#lineBreakWordStyle)
with TextViews.
![](https://developer.android.com/static/images/about/versions/13/japanese-text-wrapping.png) Japanese text wrapping with phrase style enabled (below) and without (above).

#### Unicode library updates

Android 13 adds the latest improvements, fixes, and changes that are included in
[Unicode ICU 70](http://blog.unicode.org/2021/10/icu-70-released.html),
[Unicode CLDR 40](http://blog.unicode.org/2021/10/unicode-cldr-v40-now-available.html),
and [Unicode 14.0](http://blog.unicode.org/2021/09/announcing-unicode-standard-version-140.html).

Here are a couple notable changes:

- English (Canada) `en‑CA` and English (Republic of the Philippines) `en‑PH` both use English (United States) `en` translation resources when there are no translation resources available instead of English (United Kingdom) `en‑GB`.
- The `many` plural category has been introduced for Spanish `es`, Italian `it`, Portuguese `pt`, and Portuguese (Portugal) `pt‑PT`. Similar to French introduced in [CLDR v38](https://cldr.unicode.org/index/downloads/cldr-38#h.6nnr48ppi2p3), this is used for large numbers.

### Color vector fonts

![](https://developer.android.com/static/images/about/versions/13/color-vector-fonts.png) COLRv1 vector emoji (left) and bitmap emoji (right)

Starting in Android 13, the system includes rendering support for COLR version 1
(COLRv1) fonts and updates system emoji to the COLRv1 format. COLRv1 is a highly
compact font format that renders quickly and crisply at any size.

For most apps, the system handles everything and COLRv1 just works. However,
if your app implements its own text rendering and uses the system's fonts, we
recommend testing emoji rendering.

To learn more about COLRv1, see the following resources:

- [Chrome Developers blog announcement](https://developer.chrome.com/blog/colrv1-fonts/)
- [Shipping COLRv1 Color Vector Fonts in Chrome (Video)](https://www.youtube.com/watch?v=BmqYm5Wwz8M)
- [COLR table specification](https://docs.microsoft.com/en-us/typography/opentype/spec/colr)

### Quick Settings placement API

Quick Settings in the notification shade is a convenient way for users to change
settings or take quick actions without leaving the context of an app. For apps
that provide [custom tiles](https://developer.android.com/reference/android/service/quicksettings/TileService),
we're making it easier for users to discover and add your tiles to Quick
Settings. Using a new
[tile placement API](https://developer.android.com/reference/android/app/StatusBarManager#requestAddTileService(android.content.ComponentName,%20java.lang.CharSequence,%20android.graphics.drawable.Icon,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.lang.Integer%3E)), your app can now prompt the user to directly add your custom tile to the
set of active Quick Settings tiles. A new system dialog lets the user add the
tile in one step, without leaving your app, rather than having to go to Quick
Settings to add the tile.

![A dialog asking the user whether they want to add a tile to their
Quick Settings.](https://developer.android.com/static/images/about/versions/13/quick-settings.png)

### Clipboard preview

Starting in Android 13, the system displays a standard visual confirmation when
content is added to the clipboard. The new confirmation does the following:

- Confirms the content was successfully copied.
- Provides a preview of the copied content.

This feature standardizes the various notifications shown by apps after copying
and offers users more control over their clipboard. For additional information,
visit the [Copy and Paste](https://developer.android.com/guide/topics/text/copy-paste#Feedback) feature
page.  
![Copy/Paste widget](https://developer.android.com/static/images/about/versions/13/new-copy-paste-UI.gif) New UI shown when content enters the clipboard.

<br />

### Predictive back gesture

Android 13 introduces a predictive back gesture for Android devices such as
phones, large screens, and foldables. Supporting this feature requires you to
update your app.

To see detailed documentation, see [Update your app to support a predictive back
gesture](https://developer.android.com/about/versions/13/features/predictive-back-gesture). You can also try
out [our codelab](https://codelabs.developers.google.com/handling-gesture-back-navigation).

### Bluetooth LE Audio

Low Energy (LE) Audio is wireless audio built to replace
Bluetooth classic and enable certain use cases and connection topologies. It
allows users to share and broadcast their audio to friends and family, or
subscribe to public broadcasts for information, entertainment, or accessibility.
It's designed to ensure that users can receive high fidelity audio without
sacrificing battery life, and can seamlessly switch between different use
cases that are not possible with Bluetooth Classic. Starting in Android 13, the
system includes built-in support for LE Audio, so developers receive these
capabilities for free on compatible devices.

### MIDI 2.0

Starting in Android 13, the system includes support for the MIDI 2.0 standard,
including the ability to connect MIDI 2.0 hardware through USB. This standard
offers features such as increased resolution for controllers, better support for
non-Western intonation, and more expressive performance using per-note
controllers.

### Splash screen efficiency improvements

Android 13 improves the efficiency of animated splash screens in the Splash
Screen API:

- The system infers the animation duration directly from the
  `AnimatedVectorDrawable`. Prior to Android 13, it was necessary to set the
  `windowSplashScreenAnimationDuration` directly.

- Use the new `windowSplashScreenBehavior` attribute for more control over
  whether your app always displays the icon on the splash screen in Android 13
  and higher.

To see detailed documentation, see [Splash Screens](https://developer.android.com/guide/topics/ui/splash-screen).

### ART optimizations

In Android 13 (API level 33) and higher, ART makes switching to and from native
code much faster, with JNI calls now up to 2.5x faster. Runtime reference
processing was also reworked to make it mostly non-blocking, which further
reduces jank. In addition, you can use the
[`Reference.refersTo()`](https://developer.android.com/reference/java/lang/ref/Reference#refersTo(T))
public API to reclaim unreachable objects sooner, and you'll notice the
interpreter is now faster thanks to optimized class and method lookups. ART also
performs more byte-code verification at install time, avoiding the expense of
verification at runtime and keeping app startup times fast.

## Privacy and security

### Safer exporting of context-registered receivers

To help make runtime receivers safer, Android 13 introduces the
ability for your app to specify whether a
[registered broadcast receiver](https://developer.android.com/guide/components/broadcasts#context-registered-receivers)
should be exported and visible to other apps on the device. On previous versions
of Android, any app on the device could send an unprotected broadcast to a
dynamically-registered receiver unless that receiver was guarded by a
[signature permission](https://developer.android.com/guide/topics/permissions/overview#signature).

This exporting configuration is available on apps that do at least one of the
following:

- Use the [`ContextCompat`](https://developer.android.com/reference/androidx/core/content/ContextCompat) class from version 1.9.0 or higher of the [AndroidX Core library](https://developer.android.com/jetpack/androidx/releases/core).
- Target Android 13 or higher.

### Photo picker

Android 13 (API level 33) and higher includes a
[photo picker](https://developer.android.com/training/data-storage/shared/photopicker)
experience. When your app launches the
photo picker, users select specific images and videos to share with your app,
such as profile pictures, instead of giving your app access to view the entire
media library. This is the recommended way to access the user's photos and
videos.

The photo picker provides enhanced privacy for users because your app doesn't
need to declare any runtime permissions. In addition, the photo picker provides
a built-in, standardized UI for apps, which creates a more consistent user
experience.

### New runtime permission for nearby Wi-Fi devices

Android 13 (API level 33) introduces a new
[runtime permission](https://developer.android.com/guide/topics/permissions/overview#runtime) in the
`NEARBY_DEVICES` permission group for apps that manage a device's connections to
nearby access points over Wi-Fi. These apps must declare the new permission,
[`NEARBY_WIFI_DEVICES`](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES),
when they
[call several different Wi-Fi APIs](https://developer.android.com/about/versions/13/features/nearby-wifi-devices-permission#check-for-apis-that-require-permission).
In addition, as long as apps don't derive physical location from the Wi-Fi
APIs, they don't need to declare the
[`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)
permission when they target Android 13 or higher.

Learn more about the
[nearby Wi-Fi devices permission](https://developer.android.com/about/versions/13/features/nearby-wifi-devices-permission).

### New permission to use exact alarms

If your app targets Android 13 or higher, you can use the
[`USE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)
permission, which is automatically granted to your app. In order for your app to
use this permission, however, it must satisfy at least one of the following
criteria:

- Your app is an alarm clock app or a timer app.
- Your app is a calendar app that shows notifications for upcoming events.

| **Note:** An upcoming [Google Play policy](https://support.google.com/googleplay/android-developer/answer/12253906#exact_alarm_preview) will prevent apps from using the `USE_EXACT_ALARM` permission unless they satisfy one of the cases shown in the previous list.

If your app sets exact alarms but doesn't satisfy either case shown in the
previous list, continue to declare the
[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)
permission instead, and be prepared for the situation where the user denies
access to your app.

### Developer downgradable permissions

Starting in Android 13, your app can [revoke access to unused
runtime permissions](https://developer.android.com/training/permissions/requesting#remove-access). This API
allows your app to perform privacy-enhancing tasks such as the following:

- Remove unused permissions.
- Adhere to permissions best practices, which improves user trust. You may want to consider showing the users a dialog displaying the permissions you have proactively revoked.

### APK Signature Scheme v3.1

Android 13 adds support for APK Signature Scheme v3.1, which
improves upon the existing
[APK Signature Scheme v3](https://source.android.com/security/apksigning/v3).
This scheme
[addresses some of the known issues](https://source.android.com/docs/security/features/apksigning/v3-1)
with APK Signature Scheme v3 regarding rotation. In particular, the v3.1
signature scheme supports SDK version targeting, which allows rotation to
target a later release of the platform.

The v3.1 signature scheme uses a block ID that isn't recognized on
12L or lower. Therefore, the platform applies the
following signer behavior:

- Devices that run Android 13 or higher use the rotated signer in the v3.1 block.
- Devices that run older versions of Android ignore the rotated signer and instead use the original signer in the v3.0 block.

Apps that haven't yet rotated their signing key don't require any additional
action. Whenever these apps choose to rotate, the system applies the v3.1
signature scheme by default.

Apps that have already rotated and want to continue using their rotated signing
key in the v3.0 signing block need to update their
[`apksigner`](https://developer.android.com/studio/command-line/apksigner)
invocation:  

```
apksigner sign --ks keystore.jks |
  --key key.pk8 --cert cert.x509.pem
  --rotation-min-sdk-version <var translate="no">API_LEVEL</var>
  [signer_options] app-name.apk
```

...where `API_LEVEL` is 32 or lower.

### Better error reporting in Keystore and KeyMint

For apps that generate keys, Keystore and KeyMint now provide more detailed and
accurate error indicators. We've added an exception class hierarchy under
`java.security.ProviderException`, with Android-specific exceptions that include
[Keystore/KeyMint error codes](https://developer.android.com/reference/android/security/KeyStoreException),
and whether the error is retryable. You can also modify the methods for key
generation and use (signing, encryption) to throw the new exceptions. The
improved error reporting is not limited to key generation and should now give
you what you need to retry key generation.

## Tablet and large screen support

Android 13 builds on the tablet optimizations introduced in Android 12 and the
12L feature drop---including optimizations for the system UI, better multitasking,
and improved compatibility modes. As part of your testing, make sure your apps
look their best on tablets and other large-screen devices.

For more information about what's new and what to test, see the
[Tablet and large-screens support](https://developer.android.com/about/versions/13/features/large-screens)
page.

## Graphics

### Programmable shaders

![](https://developer.android.com/static/images/about/versions/13/agsl-shader.gif) An AGSL animated shader, adapted from this [GLSL Shader](https://twitter.com/notargs/status/1250468645030858753).

Starting in Android 13, the system includes support for programmable
[`RuntimeShader`](https://developer.android.com/reference/android/graphics/RuntimeShader) objects, with
behavior defined using the Android Graphics Shading Language
([AGSL](https://developer.android.com/guide/topics/graphics/agsl)). AGSL shares
much of its syntax with GLSL, but works within the Android rendering engine to
customize painting within Android's canvas as well as filtering of View content.
Android internally uses these shaders to implement
[ripple effects](https://cs.android.com/android/platform/superproject/+/master:frameworks/base/graphics/java/android/graphics/drawable/RippleShader.java;l=24?q=RippleShader&sq),
[blur](https://cs.android.com/android/platform/superproject/+/master:frameworks/native/libs/renderengine/skia/filters/BlurFilter.cpp?q=RuntimeShader&ss=android/platform/superproject&start=21),
and
[stretch overscroll](https://cs.android.com/android/platform/superproject/+/master:frameworks/base/tests/HwAccelerationTest/src/com/android/test/hwui/StretchShaderActivity.java?q=RuntimeShader&ss=android/platform/superproject&start=11).
Android 13 and higher enable you to create similar advanced effects for your
app.

### Choreographer improvements

Android 13 introduces public API methods to
[`Choreographer`](https://developer.android.com/ndk/reference/group/choreographer) and
[`ASurfaceControl`](https://developer.android.com/ndk/reference/group/native-activity#asurfacecontrol) that
provide apps with more information about the possible frame timelines and add
more context to
[`SurfaceFlinger`](https://source.android.com/devices/graphics/surfaceflinger-windowmanager)
about the frame lifecycle. Similar to before, apps can
[post a callback](https://developer.android.com/ndk/reference/group/choreographer#achoreographer_postvsynccallback)
to `Choreographer` and receive frame timeline information. In Android 13 (API
level 33), `Choreographer` returns multiple possible presentation times and
their corresponding frame deadlines. Apps can choose the presentation time and
subsequently
[notify `SurfaceFlinger`](https://developer.android.com/ndk/reference/group/native-activity#asurfacetransaction_setframetimeline)
of the choice. `SurfaceFlinger` then doesn't attempt to apply transactions or
latch buffers before the desired presentation time.
![](https://developer.android.com/static/images/about/versions/13/13-choreographer.png) If your app uses the new Choreographer and SurfaceControl methods, you can view the app's frame lifecycle in a Perfetto trace.

## Camera

### HDR video capture

Starting in Android 13, the
[Camera2 APIs](https://developer.android.com/reference/android/hardware/camera2/package-summary)
support High Dynamic Range (HDR) video capture, which enables you to preview
and record HDR video content using your camera. Compared to Standard Dynamic
Range (SDR), HDR offers a wider range of colors and increases the dynamic range
of the luminance component (from the current 100 cd/m2 to 1000s of cd/m2).
This results in video quality that more closely matches real life, with richer
colors, brighter highlights, and darker shadows.

To learn more about HDR video capture, see the
[HDR video capture](https://developer.android.com/training/camera2/hdr-video-capture) documentation.

## Media

### Spatial audio

Spatial audio is an immersive audio experience that makes media content sound
more realistic for your users. See our [Spatial audio](https://developer.android.com/guide/topics/media/spatial-audio)
documentation for details on how to integrate with this feature.

### Anticipatory audio routing

To help media apps identify how their audio is going to be routed, Android 13
introduces audio route APIs in the
[`AudioManager`](https://developer.android.com/reference/android/media/AudioManager) class. The
[`getAudioDevicesForAttributes()`](https://developer.android.com/reference/android/media/AudioManager#getAudioDevicesForAttributes(android.media.AudioAttributes))
API allows you to retrieve a list of devices that may be used to play the
specified audio, and the
[`getDirectProfilesForAttributes()`](https://developer.android.com/reference/android/media/AudioManager#getDirectProfilesForAttributes(android.media.AudioAttributes))
API helps you understand whether your audio stream can be played directly. Use
these APIs to determine the best
[`AudioFormat`](https://developer.android.com/reference/android/media/AudioFormat) to use for your audio
track.

## Accessibility

### Audio description

Android 13 (API level 33) introduces a new system-wide accessibility preference
that allows users to enable audio descriptions across all apps. An audio
description is an additional narration track that consists of a narrator talking
through the presentation, describing what is happening on the screen during
natural pauses in the audio.
Apps can follow the user's preference for audio description tracks by
querying it with [`isAudioDescriptionRequested()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#isAudioDescriptionRequested()),
as shown in the following code snippet:  

### Kotlin

```kotlin
private lateinit var accessibilityManager: AccessibilityManager

// In onCreate():
accessibilityManager = getSystemService(AccessibilityManager::class.java)

// Where your media player is initialized
if (accessibilityManager.isAudioDescriptionRequested) {
    // User has requested to enable audio descriptions
}
```

### Java

```java
private AccessibilityManager accessibilityManager;

// In onCreate():
accessibilityManager = getSystemService(AccessibilityManager.class);

// Where your media player is initialized
if(accessibilityManager.isAudioDescriptionRequested()) {
    // User has requested to enable audio descriptions
}
```

Apps can monitor user's preference change by adding a listener to
[`AccessbilityManager`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager):  

### Kotlin

```kotlin
private val listener =
    AccessibilityManager.AudioDescriptionRequestedChangeListener { enabled ->
        // Preference changed; reflect its state in your media player
    }

override fun onStart() {
    super.onStart()

    accessibilityManager.addAudioDescriptionRequestedChangeListener(mainExecutor, listener)
}

override fun onStop() {
    super.onStop()

    accessibilityManager.removeAudioDescriptionRequestedChangeListener(listener)
}
```

### Java

```java
private AccessibilityManager.AudioDescriptionRequestedChangeListener listener = enabled -> {
    // Preference changed; reflect its state in your media player
};

@Override
protected void onStart() {
    super.onStart();

    accessibilityManager.addAudioDescriptionRequestedChangeListener(getMainExecutor(), listener);
}

@Override
protected void onStop() {
    super.onStop();

    accessibilityManager.removeAudioDescriptionRequestedChangeListener(listener);
}
```

## Core functionality

### OpenJDK 11 updates

Android 13 starts the work of refreshing Android's core libraries to align with
the OpenJDK 11 LTS release with both library updates and Java 11 language
support for application and platform developers. The core library changes
introduced in Android 13 will also be available to Android 12 devices through a
Google Play system update to the ART Mainline Module.

Android 13 includes the following changes to core libraries:

- Support for the `var` keyword for local variables and as parameters lambdas.
- New methods in the String class:

  - `isBlank()`
  - `lines()`
  - `repeat()`
  - `strip()`
  - `stripLeading()`
  - `stripTrailing()`
- Support for `Collection.toArray(IntFunction)` to make it easier to adapt a
  collection to an array.

- Support for `ifPresentOrElse()`, `isEmpty()`, `orElseThrow()`, and `stream()`
  in `java.util` classes `Optional`, `OptionalDouble`, `OptionalInt`, and
  `OptionalLong`.

- Extended support for `SocketOptions` including re-use of sockets.

- `NullReader`, `NullWriter`, `InputStream`, `OutputStream`, and `transferTo()`
  `Reader` functionality which transfer read characters to a `Writer`.

- Added functionality for URL encoding and decoding using `Charsets`.

- `Charset` functionality for `FileReader`, `FileWriter`, `PrintStream`, and
  `PrintWriter`.

- New `transferTo()`, `readNBytes()`, `readAllBytes()`, and `writeBytes()`
  functions for `ByteArrayInput` or `OutputStream` and `Input` or
  `OutputStream`.

- Runtime and compiler support for `java.lang.invoke.VarHandle`.

- Updates `java.util.concurrent` to OpenJDK 11 API using `VarHandle` internally.

*Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its
affiliates.*