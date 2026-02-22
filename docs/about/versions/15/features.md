---
title: https://developer.android.com/about/versions/15/features
url: https://developer.android.com/about/versions/15/features
source: md.txt
---

Android 15 introduces great features and APIs for developers. The following
sections summarize these features to help you get started with the related APIs.

For a detailed list of added, modified, and removed APIs, read the [API diff
report](https://developer.android.com/sdk/api_diff/35/changes). For details on added APIs visit the [Android API reference](https://developer.android.com/reference) --- for
Android 15, look for APIs that were added in API level 35. To learn about areas
where platform changes might affect your apps, be sure to check out Android 15
behavior changes [for apps that target Android 15](https://developer.android.com/about/versions/15/behavior-changes-15) and [for all apps](https://developer.android.com/about/versions/15/behavior-changes-all).

## Camera and media

Android 15 includes a variety of features that improve the camera and media
experience and that give you access to tools and hardware to support creators in
bringing their vision to life on Android.

For more on the latest features and developer solutions for Android media and
camera, see the [Building modern Android media and camera
experiences](https://io.google/2024/explore/25ff7e80-ca0b-4b3b-aa89-aa796618b3af/) talk from Google I/O.

### Low Light Boost

Android 15 introduces *Low Light Boost* , an auto-exposure mode available to
both [Camera 2](https://developer.android.com/media/camera/camera2) and the
[night mode camera extension](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT). Low Light Boost adjusts the
exposure of the Preview stream in low-light conditions. This is different from
how the night mode camera extension creates still images, because night mode
combines a burst of photos to create a single, enhanced image. While night mode
works very well for creating a still image, it can't create a continuous stream
of frames, but Low Light Boost can. Thus, Low Light Boost enables camera
capabilities, such as:

- Providing an enhanced image preview, so users are better able to frame their low-light pictures
- Scanning QR codes in low light

If you enable Low Light Boost, it automatically turns on when there's a low
light level, and turns off when there's more light.

Apps can record off the Preview stream in low-light conditions to save a
brightened video.
| **Note:** Because Low Light Boost uses a different mechanism than night mode still capture, the two images won't look identical. Night mode still capture provides a better result when you just want to capture a single image, but Low Light Boost is able to show you enhanced images in real time.

For more information, see [Low Light Boost](https://developer.android.com/media/camera/lowlight/hw-low-light-boost).

### In-app camera controls

Android 15 adds an extension for more control over the camera hardware and its
algorithms on supported devices:

- **Advanced flash strength adjustments** enabling precise control of flash intensity in both [`SINGLE`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#FLASH_SINGLE_STRENGTH_DEFAULT_LEVEL) and [`TORCH`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#FLASH_TORCH_STRENGTH_DEFAULT_LEVEL) modes while capturing images.

### HDR headroom control

Android 15 chooses HDR headroom that is appropriate for the underlying device
capabilities and bit-depth of the panel. For pages that have lots of SDR
content, such as a messaging app displaying a single HDR thumbnail, this
behavior can end up adversely influencing the perceived brightness of the SDR
content. Android 15 lets you control the HDR headroom with
[`setDesiredHdrHeadroom`](https://developer.android.com/reference/kotlin/android/view/Window#setdesiredhdrheadroom) to strike a balance between SDR
and HDR content.
![](https://developer.android.com/static/about/versions/15/images/hdr-headroom.png) The brightness of SDR UI elements on the left screen appears to be more uniform than the brightness on the right screen, which simulates possible headroom issues when HDR and SDR content are mixed. By adjusting the HDR headroom, you can achieve a better balance between the SDR and HDR content.

### Loudness control

![](https://developer.android.com/static/images/shared/bot-headphones-512px.png)

Android 15 introduces support for the
[CTA-2075](https://shop.cta.tech/products/loudness-standard-for-over-the-top-television-and-online-video-distribution-for-mobile-and-fixed-devices-ansi-cta-2075) loudness standard to help you
avoid audio loudness inconsistencies and ensure users don't have to constantly
adjust volume when switching between content. The system leverages known
characteristics of the output devices (headphones and speaker) along with
loudness metadata available in AAC audio content to intelligently adjust the
audio loudness and dynamic range compression levels.

To enable this feature, you need to ensure loudness metadata is available in
your AAC content and enable the platform feature in your app. For this, you
instantiate a [`LoudnessCodecController`](https://developer.android.com/reference/android/media/LoudnessCodecController) object by
calling its [create](https://developer.android.com/reference/android/media/LoudnessCodecController#create(int)) factory method with the audio
session ID from the associated [`AudioTrack`](https://developer.android.com/reference/android/media/AudioTrack); this
automatically starts applying audio updates. You can pass an
[`OnLoudnessCodecUpdateListener`](https://developer.android.com/reference/android/media/LoudnessCodecController.OnLoudnessCodecUpdateListener) to modify or filter
loudness parameters before they are applied on the
[`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec).  

    // Media contains metadata of type MPEG_4 OR MPEG_D
    val mediaCodec = ...
    val audioTrack = AudioTrack.Builder()
                                    .setSessionId(sessionId)
                                    .build()
    ...
    // Create new loudness controller that applies the parameters to the MediaCodec
    try {
       val lcController = LoudnessCodecController.create(mSessionId)
       // Starts applying audio updates for each added MediaCodec
    }

AndroidX media3 ExoPlayer will also be updated to use the
`LoudnessCodecController` APIs for a seamless app integration.

### Virtual MIDI 2.0 devices

Android 13 added support for connecting to
[MIDI 2.0 devices using USB](https://developer.android.com/reference/android/media/midi/package-summary), which communicate using
Universal MIDI Packets (UMP). Android 15 extends [UMP support to virtual MIDI
apps](https://developer.android.com/reference/android/media/midi/MidiUmpDeviceService), enabling composition apps to control synthesizer apps
as a virtual MIDI 2.0 device just like they would with an USB MIDI 2.0 device.

### More efficient AV1 software decoding

![dav1d logo](https://developer.android.com/static/about/versions/15/images/dav1d.png)

[dav1d](https://code.videolan.org/videolan/dav1d), the popular AV1 software decoder from VideoLAN
is available for Android devices that don't support AV1 decode in hardware.
dav1d is up to 3x more performant than the legacy AV1 software decoder, enabling
HD AV1 playback for more users, including some low and mid tier devices.

Your app needs to opt-in to using dav1d by invoking it by name
`"c2.android.av1-dav1d.decoder"`. dav1d will be made the default AV1 software
decoder in a subsequent update. This support is standardized and backported to
Android 11 devices that receive Google Play system updates.

## Developer productivity and tools

While most of our work to improve your productivity centers around tools like
[Android Studio](https://developer.android.com/studio), [Jetpack Compose](https://developer.android.com/jetpack/compose), and the [Android Jetpack](https://developer.android.com/jetpack)
libraries, we always look for ways in the platform to help you more easily
realize your vision.

### OpenJDK 17 updates

Android 15 continues the work of refreshing Android's core libraries to align
with the features in the latest OpenJDK LTS releases.

The following key features and improvements are included:

- Quality-of-life improvements around [NIO buffers](https://developer.android.com/reference/java/nio/ByteBuffer#get%28int,%20byte%5B%5D%29)
- [Streams](https://developer.android.com/reference/java/util/stream/DoubleStream.DoubleMapMultiConsumer)
- Additional [`math`](https://developer.android.com/sdk/api_diff/35-incr/changes/java.lang.Math) and [`strictmath`](https://developer.android.com/sdk/api_diff/35-incr/changes/java.lang.StrictMath) methods
- [`util`](https://developer.android.com/sdk/api_diff/35-incr/changes/pkg_java.util) package updates including sequenced [`collection`](https://developer.android.com/reference/java/util/SequencedCollection), [`map`](https://developer.android.com/reference/java/util/SequencedMap), and [`set`](https://developer.android.com/reference/java/util/SequencedSet)
- [`ByteBuffer` support in `Deflater`](https://developer.android.com/sdk/api_diff/35-incr/changes/java.util.zip.Deflater)
- Security updates such as [`X500PrivateCredential`](https://developer.android.com/reference/javax/security/auth/x500/X500PrivateCredential) and [security key updates](https://developer.android.com/sdk/api_diff/35-incr/changes/pkg_java.security.spec)

These APIs are updated on [over a billion devices running Android 12 (API level
31) and higher through Google Play System updates](https://android-developers.googleblog.com/2023/11/the-secret-to-androids-improved-memory-latest-android-runtime-update.html), so you can
target the latest programming features.

### PDF improvements

Android 15 includes substantial improvements to the [`PdfRenderer`](https://developer.android.com/reference/android/graphics/pdf/PdfRenderer)
APIs. Apps can incorporate advanced features such as rendering
[password-protected files](https://developer.android.com/reference/android/graphics/pdf/LoadParams), annotations, [form editing](https://developer.android.com/reference/android/graphics/pdf/models/FormEditRecord),
[searching](https://developer.android.com/reference/android/graphics/pdf/PdfRenderer.Page#searchText(java.lang.String)), and [selection](https://developer.android.com/reference/android/graphics/pdf/PdfRenderer.Page#selectContent(android.graphics.pdf.models.selection.SelectionBoundary,%20android.graphics.pdf.models.selection.SelectionBoundary,%20boolean)) with copy. Linearized PDF
optimizations are supported to speed local PDF viewing and reduce resource use.
The [Jetpack PDF library](https://developer.android.com/jetpack/androidx/releases/pdf) uses these APIs to simplify adding PDF
viewing capabilities to your app.
![](https://developer.android.com/static/about/versions/15/images/pdf-rendering.png) The latest updates to PDF rendering include features such as searching an embedded PDF file.

The `PdfRenderer` has been moved to a module that can be updated using Google
Play system updates independent of the platform release, and we're supporting
these changes back to Android 11 (API level 30) by creating a compatible
pre-Android 15 version of the API surface, called
[`PdfRendererPreV`](https://developer.android.com/reference/android/graphics/pdf/PdfRendererPreV).

### Automatic language switching refinements

Android 14 added on-device, multi-language recognition in audio with automatic
switching between languages, but this can cause words to get dropped,
especially when languages switch with less of a pause between the two
utterances. Android 15 adds additional controls to help apps tune this switching
to their use case.
[`EXTRA_LANGUAGE_SWITCH_INITIAL_ACTIVE_DURATION_TIME_MILLIS`](https://developer.android.com/reference/android/speech/RecognizerIntent#EXTRA_LANGUAGE_SWITCH_INITIAL_ACTIVE_DURATION_TIME_MILLIS)
confines the automatic switching to the beginning of the audio session, while
[`EXTRA_LANGUAGE_SWITCH_MATCH_SWITCHES`](https://developer.android.com/reference/android/speech/RecognizerIntent#EXTRA_LANGUAGE_SWITCH_MAX_SWITCHES) deactivates the
language switching after a defined number of switches. These options are
particularly useful if you expect that there will be a single language spoken
during the session that should be autodetected.

### Improved OpenType Variable Font API

Android 15 improves the usability of the OpenType variable font. You can create
a [`FontFamily`](https://developer.android.com/reference/android/graphics/fonts/FontFamily) instance from a variable font without specifying weight axes
with the [`buildVariableFamily`](https://developer.android.com/reference/android/graphics/fonts/FontFamily.Builder#buildVariableFamily()) API. The text renderer overrides the value
of `wght` axis to match the displaying text.

Using the API simplifies the code for creating a [`Typeface`](https://developer.android.com/reference/android/graphics/Typeface) considerably:  

### Kotlin

```kotlin
val newTypeface = Typeface.CustomFallbackBuilder(
            FontFamily.Builder(
                Font.Builder(assets, "RobotoFlex.ttf").build())
                    .buildVariableFamily())
    .build()
```

### Java

```java
Typeface newTypeface = Typeface.CustomFallbackBuilder(
            new FontFamily.Builder(
                new Font.Builder(assets, "RobotoFlex.ttf").build())
                    .buildVariableFamily())
    .build();
```

Previously, to create the same `Typeface`, you would need much more code:  

### Kotlin

```kotlin
val oldTypeface = Typeface.CustomFallbackBuilder(
            FontFamily.Builder(
                Font.Builder(assets, "RobotoFlex.ttf")
                    .setFontVariationSettings("'wght' 400")
                    .setWeight(400)
                    .build())
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 100")
                        .setWeight(100)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 200")
                        .setWeight(200)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 300")
                        .setWeight(300)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 500")
                        .setWeight(500)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 600")
                        .setWeight(600)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 700")
                        .setWeight(700)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 800")
                        .setWeight(800)
                        .build()
                )
                .addFont(
                    Font.Builder(assets, "RobotoFlex.ttf")
                        .setFontVariationSettings("'wght' 900")
                        .setWeight(900)
                        .build()
                ).build()
        ).build()
```

### Java

```java
Typeface oldTypeface = new Typeface.CustomFallbackBuilder(
    new FontFamily.Builder(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 400")
            .setWeight(400)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 100")
            .setWeight(100)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 200")
            .setWeight(200)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 300")
            .setWeight(300)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 500")
            .setWeight(500)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 600")
            .setWeight(600)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 700")
            .setWeight(700)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 800")
            .setWeight(800)
            .build()
    )
    .addFont(
        new Font.Builder(assets, "RobotoFlex.ttf")
            .setFontVariationSettings("'wght' 900")
            .setWeight(900)
            .build()
    )
    .build()
).build();
```

Here's an example of how a `Typeface` created with both the old and new APIs
renders:

![An example of how Typeface rendering differs using new and old
APIs](https://developer.android.com/static/about/versions/15/images/opentype-variable-font.png)

In this example, the `Typeface` created with the old API doesn't have the
capability to create accurate font weights for the 350, 450, 550 and 650
[`Font`](https://developer.android.com/reference/android/graphics/fonts/Font) instances, so the renderer falls back to the closest weight. So in
this case, 300 is rendered instead of 350, 400 is rendered instead of 450, and
so on. By contrast, the `Typeface` created with the new APIs dynamically creates
a `Font` instance for a given weight, so accurate weights are rendered for 350,
450, 550, and 650 as well.

### Granular line break controls

Starting in Android 15, a [`TextView`](https://developer.android.com/reference/android/widget/TextView) and the underlying
line breaker can preserve the given portion of text in the same line to improve
readability. You can take advantage of this line break customization by using
the `<nobreak>` tag in string resources or
[`createNoBreakSpan`](https://developer.android.com/reference/android/text/style/LineBreakConfigSpan#createNoBreakSpan()). Similarly, you can preserve words from
hyphenation by using the `<nohyphen>` tag or
[`createNoHyphenationSpan`](https://developer.android.com/reference/android/text/style/LineBreakConfigSpan#createNoHyphenationSpan()).

For example, the following string resource doesn't include a line break, and
renders with the text "Pixel 8 Pro." breaking in an undesirable place:  

    <resources>
        <string name="pixel8pro">The power and brains behind Pixel 8 Pro.</string>
    </resources>

In contrast, this string resource includes the `<nobreak>` tag, which wraps the
phrase "Pixel 8 Pro." and prevents line breaks:  

    <resources>
        <string name="pixel8pro">The power and brains behind <nobreak>Pixel 8 Pro.</nobreak></string>
    </resources>

The difference in how these strings are rendered is shown in the following
images:  
![](https://developer.android.com/static/about/versions/15/images/line-breaks-none.png)  
Layout for a line of text where the phrase "Pixel 8 Pro." isn't wrapped using a `<nobreak>` tag.  
![](https://developer.android.com/static/about/versions/15/images/line-breaks-included.png)  
Layout for the same line of text where the phrase "Pixel 8 Pro." is wrapped using a `<nobreak>` tag.

### App archiving

[Android and Google Play announced support for app archiving last
year](https://android-developers.googleblog.com/2023/04/reduce-uninstalls-for-your-app-with-auto-archive.html), allowing users to free up space by partially removing
infrequently used apps from the device that were published using Android App
Bundle on Google Play. Android 15 includes OS level support for app archiving
and unarchiving, making it easier for all app stores to implement it.

Apps with the [`REQUEST_DELETE_PACKAGES`](https://developer.android.com/reference/android/Manifest.permission#REQUEST_DELETE_PACKAGES) permission can call the
`PackageInstaller` [`requestArchive`](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.String,%20android.content.IntentSender)) method to request archiving an
installed app package, which removes the APK and any cached files, but persists
user data. Archived apps are returned as displayable apps through the
[`LauncherApps`](https://developer.android.com/reference/android/content/pm/LauncherApps) APIs; users will see a UI treatment to highlight that those
apps are archived. If a user taps on an archived app, the responsible installer
will get a request to [unarchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestUnarchive(java.lang.String,%20android.content.IntentSender)) it, and the restoration process can be
monitored by the [`ACTION_PACKAGE_ADDED`](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_ADDED) broadcast.

### Enable 16 KB mode on a device using developer options

![](https://developer.android.com/static/images/guide/practices/16-kb-dev-option.png)

Toggle the **Boot with 16KB page size** developer
option to boot a device in 16 KB mode.

In QPR versions of Android 15, you can
[use the developer option](https://source.android.com/docs/core/architecture/16kb-page-size/16kb-developer-option#use_16kb_toggle) that's available on certain
devices to boot the device in 16 KB mode and perform on-device testing.
Before using the developer option, go to **Settings \> System \> Software
updates** and apply any updates that are available.

This developer option is available on the following devices:

- Pixel 8 and 8 Pro (with Android 15 QPR1 or higher)

- Pixel 8a (with Android 15 QPR1 or higher)

- Pixel 9, 9 Pro, and 9 Pro XL (with Android 15 QPR2 or higher)

- Pixel 9a (with Android 16 or higher)

<br />

## Graphics

Android 15 brings the latest graphics improvements, including ANGLE and
additions to the Canvas graphics system.

### Modernizing Android's GPU access

![Vulkan logo](https://developer.android.com/static/about/versions/15/images/vulkan.svg)

Android hardware has evolved quite a bit from the early days where the core OS
would run on a single CPU and GPUs were accessed using APIs based on
fixed-function pipelines. The [Vulkan® graphics API](https://developer.android.com/ndk/guides/graphics) has been available in the
[NDK](https://developer.android.com/ndk) since Android 7.0 (API level 24) with a lower-level abstraction that
better reflects modern GPU hardware, scales better to support multiple CPU
cores, and offers reduced CPU driver overhead --- leading to improved app
performance. Vulkan is supported by all modern game engines.

Vulkan is Android's preferred interface to the GPU. Therefore, Android 15
includes [ANGLE](https://chromium.googlesource.com/angle/angle) as an optional layer for running OpenGL® ES on
top of Vulkan. Moving to ANGLE will standardize the Android OpenGL
implementation for improved compatibility, and, in some cases, improved
performance. You can test out your OpenGL ES app stability and performance with
ANGLE by enabling the developer option in
**Settings -\> System -\> Developer Options -\> Experimental: Enable ANGLE** on
Android 15.

#### The Android ANGLE on Vulkan roadmap

![Roadmap of upcoming changes to the Android GPU APIs.](https://developer.android.com/static/about/versions/15/images/angle-vulkan-roadmap.png)

As part of streamlining our GPU stack, going forward we will be shipping ANGLE
as the GL system driver on more new devices, with the future expectation that
OpenGL/ES will be only available through ANGLE. That being said, we plan to
**continue support for OpenGL ES on all devices**.

#### Recommended next steps

Use the developer options to select the ANGLE driver for OpenGL ES and test your
app. For new projects, we strongly encourage using Vulkan for C/C++.

### Improvements for Canvas

Android 15 continues our modernization of Android's Canvas graphics system with
additional capabilities:

- [`Matrix44`](https://developer.android.com/reference/android/graphics/Matrix44) provides a 4x4 matrix for transforming coordinates that should be used when you want to manipulate the canvas in 3D.
- [`clipShader`](https://developer.android.com/reference/android/graphics/Canvas#clipShader(android.graphics.Shader)) intersects the current clip with the specified shader, while [`clipOutShader`](https://developer.android.com/reference/android/graphics/Canvas#clipOutShader(android.graphics.Shader)) sets the clip to the difference of the current clip and the shader, each treating the shader as an alpha mask. This supports the drawing of complex shapes efficiently.

## Performance and battery

Android continues its focus on helping you improve the performance and quality
of your apps. Android 15 introduces APIs that help make tasks in your app
more efficient to execute, optimize app performance, and gather insights about
your apps.

For battery-efficient best practices, debugging network and power usage, and
detail on how we're improving battery efficiency of background work in Android
15 and recent versions of Android, see the [Improving battery efficiency of
background work on Android](https://io.google/2024/explore/4ad3e7fe-ca50-4c24-8c48-5c04ee39e4d0/)
talk from Google I/O.

### ApplicationStartInfo API

In previous versions of Android, app startup has been a bit of a mystery. It was
challenging to determine within your app whether it started from a cold, warm,
or hot state. It was also difficult to know how long your app spent during the
various launch phases: forking the process, calling `onCreate`, drawing the
first frame, and more. When your `Application` class was instantiated, you had no
way of knowing whether the app started from a broadcast, a content provider, a
job, a backup, boot complete, an alarm, or an `Activity`.

The [`ApplicationStartInfo`](https://developer.android.com/reference/android/app/ApplicationStartInfo) API on Android 15 provides
all of this and more. You can even choose to add your own timestamps into the
flow to help collect timing data in one place. In addition to collecting
metrics, you can use `ApplicationStartInfo` to help directly optimize app
startup; for example, you can eliminate the costly instantiation of UI-related
libraries within your `Application` class when your app is starting up due to a
broadcast.

### Detailed app size information

Since Android 8.0 (API level 26), Android has included the
[`StorageStats.getAppBytes`](https://developer.android.com/reference/android/app/usage/StorageStats#getAppBytes()) API that summarizes the installed
size of an app as a single number of bytes, which is a sum of the APK size, the
size of files extracted from the APK, and files that were generated on the
device such as ahead-of-time (AOT) compiled code. This number is not very
insightful in terms of how your app is using storage.

Android 15 adds the
[`StorageStats.getAppBytesByDataType([type])`](https://developer.android.com/reference/android/app/usage/StorageStats#getAppBytesByDataType(int)) API, which lets
you get insight into how your app is using up all that space, including APK file
splits, AOT and speedup related code, dex metadata, libraries, and guided
profiles.

### App-managed profiling

Android 15 includes the [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) class,
which lets you collect profiling information from within your app such as heap
dumps, heap profiles, stack sampling, and more. It provides a callback to your
app with a supplied tag to identify the output file, which is delivered to your
app's files directory. The API does rate limiting to minimize the performance
impact.

To simplify constructing profiling requests in your app, we recommend using the
corresponding [`Profiling`](https://developer.android.com/reference/androidx/core/os/Profiling) AndroidX API, available
in [Core 1.15.0-rc01](https://developer.android.com/jetpack/androidx/releases/core#1.15.0-rc01) or higher.

### SQLite database improvements

Android 15 introduces SQLite APIs that expose advanced features from the
underlying SQLite engine that target specific performance issues that can
manifest in apps. These APIs are included with the [update of SQLite to version
3.44.3](https://developer.android.com/reference/android/database/sqlite/package-summary).

Developers should consult [best practices for SQLite performance](https://developer.android.com/topic/performance/sqlite-performance-best-practices)
to get the most out of their SQLite database, especially when working with large
databases or when running latency-sensitive queries.

- **Read-only deferred transactions** : when issuing transactions that are read-only (don't include write statements), use [`beginTransactionReadOnly()`](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase#begintransactionreadonly) and [`beginTransactionWithListenerReadOnly(SQLiteTransactionListener)`](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase#begintransactionreadonly) to issue read-only `DEFERRED` transactions. Such transactions can run concurrently with each other, and if the database is in WAL mode, they can run concurrently with `IMMEDIATE` or `EXCLUSIVE` transactions.
- **Row counts and IDs** : APIs were added to retrieve the count of changed rows or the last inserted row ID without issuing an additional query. [`getLastChangedRowCount()`](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase#getlastchangedrowcount) returns the number of rows that were inserted, updated, or deleted by the most recent SQL statement within the current transaction, while [`getTotalChangedRowCount()`](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase#gettotalchangedrowcount) returns the count on the current connection. [`getLastInsertRowId()`](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase#getlastinsertrowid) returns the `rowid` of the last row to be inserted on the current connection.
- **Raw statements**: issue a raw SQlite statement, bypassing convenience wrappers and any additional processing overhead that they may incur.

### Android Dynamic Performance Framework updates

Android 15 continues our investment in the [Android Dynamic Performance
Framework (ADPF)](https://developer.android.com/games/optimize/adpf), a set of APIs that allow games and
performance intensive apps to interact more directly with power and thermal
systems of Android devices. On supported devices, Android 15 adds ADPF
capabilities:

- A [power-efficiency mode](https://developer.android.com/reference/android/os/PerformanceHintManager.Session#setPreferPowerEfficiency%28boolean%29) for hint sessions to indicate that their associated threads should prefer power saving over performance, great for long-running background workloads.
- GPU and CPU work durations can both be [reported](https://developer.android.com/reference/android/os/PerformanceHintManager.Session#reportActualWorkDuration%28android.os.WorkDuration%29) in hint sessions, allowing the system to adjust CPU and GPU frequencies together to best meet workload demands.
- [Thermal headroom thresholds](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroomThresholds%28%29) to interpret possible thermal throttling status based on headroom prediction.

To learn more about how to use ADPF in your apps and games, [head over to the
documentation](https://developer.android.com/games/optimize/adpf).

## Privacy

Android 15 includes a variety of features that help app developers protect user
privacy.

### Screen recording detection

Android 15 adds [support for apps](https://developer.android.com/reference/android/view/WindowManager#addScreenRecordingCallback(java.util.concurrent.Executor,%20java.util.function.Consumer%3Cjava.lang.Integer%3E)) to detect that
they are being recorded. A callback is invoked whenever the app transitions
between being visible or invisible within a screen recording. An app is
considered visible if activities owned by the registering process's UID are
being recorded. This way, if your app is performing a sensitive operation, you
can inform the user that they're being recorded.  

    val mCallback = Consumer<Int> { state ->
      if (state == SCREEN_RECORDING_STATE_VISIBLE) {
        // We're being recorded
      } else {
        // We're not being recorded
      }
    }

    override fun onStart() {
       super.onStart()
       val initialState =
          windowManager.addScreenRecordingCallback(mainExecutor, mCallback)
       mCallback.accept(initialState)
    }

    override fun onStop() {
        super.onStop()
        windowManager.removeScreenRecordingCallback(mCallback)
    }

### Expanded IntentFilter capabilities

Android 15 builds in support for more precise `Intent` resolution through
[`UriRelativeFilterGroup`](https://developer.android.com/reference/android/content/UriRelativeFilterGroup), which contains a set of
[`UriRelativeFilter`](https://developer.android.com/reference/android/content/UriRelativeFilter) objects that form a set of `Intent`
matching rules that must each be satisfied, including URL query parameters, URL
fragments, and blocking or exclusion rules.

These rules can be defined in the `AndroidManifest` XML file with the
`<uri-relative-filter-group>` tag, which can optionally include an
`android:allow` tag. These tags can contain `<data>` tags that use existing data
tag attributes as well as the `android:query` and `android:fragment`
attributes.

Here's an example of the `AndroidManifest` syntax:  

    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.BROWSABLE" />
      <category android:name="android.intent.category.DEFAULT" />
      <data android:scheme="http" />
      <data android:scheme="https" />
      <data android:host="astore.com" />
      <uri-relative-filter-group>
        <data android:pathPrefix="/auth" />
        <data android:query="region=na" />
      </uri-relative-filter-group>
      <uri-relative-filter-group android:allow="false">
        <data android:pathPrefix="/auth" />
        <data android:query="mobileoptout=true" />
      </uri-relative-filter-group>
      <uri-relative-filter-group android:allow="false">
        <data android:pathPrefix="/auth" />
        <data android:fragmentPrefix="faq" />
      </uri-relative-filter-group>
    </intent-filter>

### Private space

![](https://developer.android.com/static/about/versions/15/images/private-space.png) The private space can be unlocked and locked to show or hide sensitive apps on a device.

Private space lets users create a separate space on their device where they can
keep sensitive apps away from prying eyes, under an additional layer of
authentication. The private space uses a separate user profile. The user can
choose to use the device lock or a separate lock factor for the private space.

Apps in the private space show up in a separate container in the launcher, and
are hidden from the recents view, notifications, settings, and from other apps
when the private space is locked. User-generated and downloaded content (such as
media or files) and accounts are separated between the private space and the
main space. The [system sharesheet](https://developer.android.com/training/sharing/send) and the
[photo picker](https://developer.android.com/training/data-storage/shared/photopicker) can be used to give apps access to content
across spaces when the private space is unlocked.

Users can't move existing apps and their data into the private space. Instead,
users select an install option in the private space to install an app using
whichever app store they prefer. Apps in the private space are installed as
separate copies from any apps in the main space (new copies of the same app).

When a user locks the private space, the profile is stopped. While the profile
is stopped, apps in the private space are no longer active and can't perform
foreground or background activities, including showing notifications.

We recommend that you test your app with private space to make sure your app
works as expected, especially if your app falls into one of the following
categories:

- [Apps with logic for work profiles](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-work-profiles) that assumes that any installed copies of their app that aren't in the main profile are in the work profile.
- [Medical apps](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-medical-apps)
- [Launcher apps](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-launcher-apps)
- [App store apps](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-app-store-apps)

### Query most-recent user selection for Selected Photos Access

Apps can now highlight only the most-recently-selected photos and videos when
[partial access](https://developer.android.com/about/versions/14/changes/partial-photo-video-access) to media permissions is granted. This feature can improve
the user experience for apps that frequently request access to photos and
videos. To use this feature in your app, enable the
[`QUERY_ARG_LATEST_SELECTION_ONLY`](https://developer.android.com/reference/android/provider/MediaStore#QUERY_ARG_LATEST_SELECTION_ONLY) argument when querying [`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore)
through [`ContentResolver`](https://developer.android.com/reference/android/content/ContentResolver).  

### Kotlin

```kotlin
val externalContentUri = MediaStore.Files.getContentUri("external")

val mediaColumns = arrayOf(
   FileColumns._ID,
   FileColumns.DISPLAY_NAME,
   FileColumns.MIME_TYPE,
)

val queryArgs = bundleOf(
   // Return only items from the last selection (selected photos access)
   QUERY_ARG_LATEST_SELECTION_ONLY to true,
   // Sort returned items chronologically based on when they were added to the device's storage
   QUERY_ARG_SQL_SORT_ORDER to "${FileColumns.DATE_ADDED} DESC",
   QUERY_ARG_SQL_SELECTION to "${FileColumns.MEDIA_TYPE} = ? OR ${FileColumns.MEDIA_TYPE} = ?",
   QUERY_ARG_SQL_SELECTION_ARGS to arrayOf(
       FileColumns.MEDIA_TYPE_IMAGE.toString(),
       FileColumns.MEDIA_TYPE_VIDEO.toString()
   )
)
```

### Java

```java
Uri externalContentUri = MediaStore.Files.getContentUri("external");

String[] mediaColumns = {
    FileColumns._ID,
    FileColumns.DISPLAY_NAME,
    FileColumns.MIME_TYPE
};

Bundle queryArgs = new Bundle();
queryArgs.putBoolean(MediaStore.QUERY_ARG_LATEST_SELECTION_ONLY, true);
queryArgs.putString(MediaStore.QUERY_ARG_SQL_SORT_ORDER, FileColumns.DATE_ADDED + " DESC");
queryArgs.putString(MediaStore.QUERY_ARG_SQL_SELECTION, FileColumns.MEDIA_TYPE + " = ? OR " + FileColumns.MEDIA_TYPE + " = ?");
queryArgs.putStringArray(MediaStore.QUERY_ARG_SQL_SELECTION_ARGS, new String[] {
    String.valueOf(FileColumns.MEDIA_TYPE_IMAGE),
    String.valueOf(FileColumns.MEDIA_TYPE_VIDEO)
});
```

### Privacy Sandbox on Android

Android 15 includes the latest Android Ad Services extensions, incorporating the
latest version of the [Privacy Sandbox on Android](https://developer.android.com/design-for-safety/privacy-sandbox). This
addition is part of our work to develop technologies that improve user privacy
and enable effective, personalized advertising experiences for mobile apps. Our
[privacy sandbox page](https://developer.android.com/design-for-safety/privacy-sandbox/program-overview) has more information about the
Privacy Sandbox on Android developer preview and beta programs to help you get
started.

### Health Connect

Android 15 integrates the latest extensions around
[Health Connect by Android](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started), a secure and centralized
platform to manage and share app-collected health and fitness data. This update
adds support for additional data types across [fitness](https://developer.android.com/reference/android/health/connect/datatypes/StepsCadenceRecord#STEPS_CADENCE_RATE_AVG),
[nutrition](https://developer.android.com/reference/android/health/connect/datatypes/NutritionRecord#TRANS_FAT_TOTAL), skin temperature, training plans, and more.

Skin temperature tracking allows users to store and share more accurate
temperature data from a wearable or other tracking device.

Training plans are structured workout plans to help a user achieve their fitness
goals. Training plans support includes a variety of completion and performance
goals:

- Completion goals around [calories burned](https://developer.android.com/reference/android/health/connect/datatypes/ExerciseCompletionGoal.ActiveCaloriesBurnedGoal), [distance](https://developer.android.com/reference/android/health/connect/datatypes/ExerciseCompletionGoal.DistanceGoal), [duration](https://developer.android.com/reference/android/health/connect/datatypes/ExerciseCompletionGoal.DurationGoal), [repetition](https://developer.android.com/reference/android/health/connect/datatypes/ExerciseCompletionGoal.RepetitionsGoal), and [steps](https://developer.android.com/reference/android/health/connect/datatypes/ExerciseCompletionGoal.StepsGoal).
- Performance goals around as [many repetitions as possible (AMRAP)](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.AmrapGoal), [cadence](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.CadenceGoal), [heart rate](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.HeartRateGoal), [power](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.PowerGoal), [perceived rate of exertion](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.RateOfPerceivedExertionGoal), and [speed](https://developer.android.com/reference/android/health/connect/datatypes/ExercisePerformanceGoal.SpeedGoal).

Learn more about the latest updates to Health Connect in Android in the
[Building adaptable experiences with Android
Health](https://io.google/2024/explore/2e00e987-fa84-4cf9-9c4b-8b67b84456e3/) talk from Google I/O.

### App screen sharing

Android 15 supports app screen sharing so users can share or record just an
app window rather than the entire device screen. This feature, first enabled in
Android 14 QPR2, includes
[`MediaProjection` callbacks](https://developer.android.com/about/versions/14/features/app-screen-sharing#media_projection_callbacks) that allow your app
to customize the app screen sharing experience. Note that for apps targeting
Android 14 (API level 34) or higher,
[user consent is required](https://developer.android.com/about/versions/14/behavior-changes-14#media-projection-consent) for each
[`MediaProjection`](https://developer.android.com/reference/android/media/projection/MediaProjection) capture session.

## User experience and system UI

Android 15 gives app developers and users more control and flexibility for
configuring their device to fit their needs.

To learn more about how to use the latest improvements in Android 15 to improve
your app's user experience, see the [Improve the user experience of your Android
app](https://io.google/2024/explore/3d552a80-acee-4243-8995-c491272800a1/)
talk from Google I/O.

### Richer widget previews with Generated Previews API

Before Android 15, the only way to provide widget picker previews was to specify
a static [image or layout resource](https://developer.android.com/develop/ui/views/appwidgets#preview). These previews often differ
significantly from the look of the actual widget when it is placed on the home
screen. Also, static resources can't be created with Jetpack Glance, so a Glance
developer had to screenshot their widget or create an XML layout to have a
widget preview.

Android 15 adds support for generated previews. This means that app widget
providers can generate [`RemoteViews`](https://developer.android.com/reference/android/widget/RemoteViews) to use as the picker preview, instead
of a static resource.
![](https://developer.android.com/static/about/versions/15/images/generated-previews.png) Apps can provide Remote Views to the Widget Picker, so they can update the content in the picker to be more representative of what the user will see.

#### Push API

Apps can provide generated previews through a push API. Apps can provide
previews at any point in their lifecycle, and don't receive an explicit request
from the host to provide previews. Previews are persisted in `AppWidgetService`,
and hosts can request them on-demand. The following example loads an XML widget
layout resource and sets it as the preview:  

    AppWidgetManager.getInstance(appContext).setWidgetPreview(
       ComponentName(
           appContext,
           SociaLiteAppWidgetReceiver::class.java
       ),
       AppWidgetProviderInfo.WIDGET_CATEGORY_HOME_SCREEN,
       RemoteViews("com.example", R.layout.widget_preview)
    )

The expected flow is:

1. At any time, the widget provider calls [`setWidgetPreview`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#setWidgetPreview(android.content.ComponentName,%20int,%20android.widget.RemoteViews)). The provided previews are persisted in `AppWidgetService` with other provider info.
2. `setWidgetPreview` notifies hosts of an updated preview through the [`AppWidgetHost.onProvidersChanged`](https://developer.android.com/reference/android/appwidget/AppWidgetHost#onProvidersChanged()) callback. In response, the widget host reloads all of its provider information.
3. When displaying a widget preview, the host checks [`AppWidgetProviderInfo.generatedPreviewCategories`](https://developer.android.com/reference/android/appwidget/AppWidgetProviderInfo#generatedPreviewCategories), and if the chosen category is available, calls [`AppWidgetManager.getWidgetPreview`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#getWidgetPreview(android.content.ComponentName,%20android.os.UserHandle,%20int)) to return the saved preview for this provider.

#### When to call `setWidgetPreview`

Because there is no callback to provide previews, apps can choose to send
previews at any point when they are running. How often to update the preview
depends on the widget's use case.

The following list describes the two main categories of preview use cases:

- Providers that show real data in their widget previews, such as personalized or recent information. These providers can set the preview once the user has signed in or has done initial configuration in their app. After this, they can set up a periodic task to update the previews at their chosen cadence. Examples of this type of widget could be a photo, calendar, weather or news widget.
- Providers that show static information in previews or quick-action widgets that don't display any data. These providers can set previews once, when the app first launches. Examples of this type of widget include a drive quick actions widget or chrome shortcuts widget.

Some providers might show static previews on the hub mode picker, but real
information on the homescreen picker. These providers should follow the guidance
for both of these use cases to set previews.

### Picture-in-Picture

Android 15 introduces changes in Picture-in-Picture (PiP) ensuring an even
smoother transition when entering into PiP mode. This will be beneficial for
apps having UI elements overlaid on top of their main UI, which goes into PiP.

Developers use the [`onPictureInPictureModeChanged`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureModeChanged(boolean,%20android.content.res.Configuration)) callback to define logic
that toggles the visibility of the overlaid UI elements. This callback is
triggered when the PiP enter or exit animation is completed. Beginning in
Android 15, the [`PictureInPictureUiState`](https://developer.android.com/reference/android/app/PictureInPictureUiState) class includes another state.

With this UI state, apps targeting Android 15 (API level 35) will observe the
[`Activity#onPictureInPictureUiStateChanged`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureUiStateChanged(android.app.PictureInPictureUiState)) callback being invoked with
[`isTransitioningToPip()`](https://developer.android.com/reference/android/app/PictureInPictureUiState#isTransitioningToPip()) as soon as the PiP animation starts. There are
many UI elements that are not relevant for the app when it is in PiP mode, for
example views or layout that include information such as suggestions, upcoming
video, ratings, and titles. When the app goes to PiP mode, use the
`onPictureInPictureUiStateChanged` callback to hide these UI elements. When the
app goes to full screen mode from the PiP window, use
`onPictureInPictureModeChanged` callback to unhide these elements, as shown in
the following examples:  

    override fun onPictureInPictureUiStateChanged(pipState: PictureInPictureUiState) {
            if (pipState.isTransitioningToPip()) {
              // Hide UI elements
            }
        }

    override fun onPictureInPictureModeChanged(isInPictureInPictureMode: Boolean) {
            if (isInPictureInPictureMode) {
              // Unhide UI elements
            }
        }

This quick visibility toggle of irrelevant UI elements (for a PiP window) helps
ensure a smoother and flicker-free PiP enter animation.

### Improved Do Not Disturb rules

[`AutomaticZenRule`](https://developer.android.com/reference/android/app/AutomaticZenRule) lets apps customize Attention
Management (Do Not Disturb) rules and decide when to activate or deactivate
them. Android 15 greatly enhances these rules with the goal of improving the
user experience. The following enhancements are included:

- Adding types to `AutomaticZenRule`, allowing the system to apply special treatment to some rules.
- Adding an icon to `AutomaticZenRule`, helping to make the modes be more recognizable.
- Adding a `triggerDescription` string to `AutomaticZenRule` that describes the conditions on which the rule should become active for the user.
- Added [`ZenDeviceEffects`](https://developer.android.com/reference/android/service/notification/ZenDeviceEffects) to `AutomaticZenRule`, allowing rules to trigger things like grayscale display, night mode, or dimming the wallpaper.

### Set VibrationEffect for notification channels

Android 15 supports setting rich vibrations for incoming notifications by
channel using [`NotificationChannel.setVibrationEffect`](https://developer.android.com/reference/android/app/NotificationChannel#setVibrationEffect(android.os.VibrationEffect)), so
your users can distinguish between different types of notifications without
having to look at their device.

### Media projection status bar chip and auto stop

| **Note:** This feature is included on devices running [Android 15
| QPR1](https://developer.android.com/about/versions/15/release-notes) or higher.

Media projection can expose private user information. A new, prominent status
bar chip makes users aware of any ongoing screen projection. Users can tap the
chip to stop screen casting, sharing, or recording. Also, for a more intuitive
user experience, any in‑progress screen projection now automatically stops
when the device screen is locked.
![](https://developer.android.com/static/media/images/grow/media_projection_status_bar_chip.png) Status bar chip for screen sharing, casting, and recording.

## Large screens and form factors

Android 15 gives your apps the support to get the most out of Android's form
factors, including large screens, flippables, and foldables.

### Improved large screen multitasking

![Users can save their favorite split-screen app combinations for
quick access](https://developer.android.com/static/about/versions/15/images/save-app-pairs.png)

Android 15 gives users better ways to multitask on large screen devices. For
example, users can save their favorite split-screen app combinations for quick
access and pin the taskbar on screen to quickly switch between apps. This means
that making sure your app is adaptive is more important than ever.

Google I/O has sessions on [Building adaptive Android
apps](https://io.google/2024/explore/d16737ba-e336-4b68-8928-24692a88e644/) and [Building UI with the Material 3
adaptive library](https://io.google/2024/explore/2dff9b4c-4069-4bde-ab9a-c5f53dc0fdb8/)
that can help, and our documentation has more to help you [Design for large
screens](https://developer.android.com/design/ui/large-screens).

### Cover screen support

Your app can [declare a property](https://developer.android.com/reference/android/view/WindowManager#COMPAT_SMALL_COVER_SCREEN_OPT_IN) that Android 15 uses to
allow your `Application` or `Activity` to be presented on the small cover
screens of supported flippable devices. These screens are too small to be
considered as compatible targets for Android apps to run on, but your app can
opt in to supporting them, making your app available in more places.

## Connectivity

Android 15 updates the platform to give your app access to the latest advances
in communication and wireless technologies.

### Satellite support

Android 15 continues to extend platform support for satellite connectivity and
includes some UI elements to ensure a consistent user experience across the
satellite connectivity landscape.

Apps can use [`ServiceState.isUsingNonTerrestrialNetwork()`](https://developer.android.com/reference/android/telephony/ServiceState#isUsingNonTerrestrialNetwork()) to
detect when a device is connected to a satellite, giving them more awareness of
why full network services might be unavailable. Additionally, Android 15
provides support for SMS and MMS apps as well as preloaded RCS apps to use
satellite connectivity for sending and receiving messages.
![](https://developer.android.com/static/about/versions/15/images/satellite-notification.png) A notification appears when the device connects to a satellite.

### Smoother NFC experiences

Android 15 is working to make the tap to pay experience more seamless and
reliable while continuing to support Android's robust NFC app ecosystem. On
supported devices, apps can request the [`NfcAdapter`](https://developer.android.com/reference/android/nfc/NfcAdapter) to enter
[observe mode](https://developer.android.com/reference/android/nfc/NfcAdapter#setObserveModeEnabled(boolean)), where the device listens but doesn't respond to NFC
readers, sending the app's NFC service [`PollingFrame`](https://developer.android.com/reference/android/nfc/cardemulation/HostApduService#processPollingFrames(java.util.List%3Candroid.nfc.cardemulation.PollingFrame%3E))
[objects](https://developer.android.com/reference/android/nfc/cardemulation/HostApduService#processPollingFrames(java.util.List%3Candroid.nfc.cardemulation.PollingFrame%3E)) to process. The `PollingFrame` objects can be used to auth
ahead of the first communication to the NFC reader, allowing for a one tap
transaction in many cases.

In addition, apps can [register a filter](https://developer.android.com/reference/android/nfc/cardemulation/CardEmulation#registerPollingLoopPatternFilterForService(android.content.ComponentName,%20java.lang.String,%20boolean)) on supported devices so
they can be notified of polling loop activity, which allows for smooth operation
with multiple NFC-aware applications.

### Wallet role

Android 15 introduces a Wallet role that allows tighter integration with the
user's preferred wallet app. This role replaces the NFC default contactless
payment setting. Users can manage the Wallet role holder by navigating to
**Settings \> Apps \> Default Apps**.

The Wallet role is used when routing NFC taps for AIDs registered in the payment
category. Taps always go to the Wallet role holder unless another app that is
registered for the same AID is running in the foreground.

This role is also used to determine where the Wallet Quick Access tile should go
when activated. When the role is set to "None", the Quick Access tile isn't
available and payment category NFC taps are only delivered to the foreground
app.

## Security

Android 15 helps you enhance your app's security, protect your app's data, and
gives users more transparency and control over their data. See the [Safeguarding
user security on Android](https://io.google/2024/explore/f757438a-844f-4c59-8dd4-9a5580a5e23d/)
talk from Google I/O for more of what we're doing to improve user safeguards and
protect your app against new threats.

### Integrate Credential Manager with autofill

Starting with Android 15, developers can [link specific views like username or
password fields with Credential Manager requests](https://developer.android.com/identity/autofill/credential-manager-autofill), making it
easier to provide a tailored user experience during the sign-in process. When
the user focuses on one of these views, a corresponding request is sent to
Credential Manager. The resulting credentials are aggregated across providers
and displayed in autofill fallback UIs, such as inline suggestions or drop-down
suggestions. The Jetpack androidx.credentials library is the preferred endpoint
for developers to use and will soon be available to further enhance this feature
in Android 15 and higher.

### Integrate single tap sign-up and sign-in with biometric prompts

Credential Manager [integrates biometric prompts into the credential creation
and sign-in processes](https://developer.android.com/identity/sign-in/single-tap-biometric), eliminating the need for providers to manage
biometric prompts. As a result, credential providers only need to focus on the
results of the create and get flows, augmented with the biometric flow result.
This simplified process creates a more efficient and streamlined credential
creation and retrieval process.

### Key management for end-to-end encryption

We are introducing the [`E2eeContactKeysManager`](https://developer.android.com/reference/android/provider/E2eeContactKeysManager) in Android 15, which
facilitates end-to-end encryption (E2EE) in your Android apps by providing an
OS-level API for the storage of cryptographic public keys.

The `E2eeContactKeysManager` is designed to integrate with the platform
contacts app to give users a centralized way to manage and verify their
contacts' public keys.

### Permission checks on content URIs

Android 15 introduces a set of APIs that perform permission checks on content
URIs:

- [`Context.checkContentUriPermissionFull`](https://developer.android.com/reference/android/content/Context#checkContentUriPermissionFull(android.net.Uri,%20int,%20int,%20int)): This performs a full permission check on content URIs.
- `Activity` manifest attribute [`requireContentUriPermissionFromCaller`](https://developer.android.com/guide/topics/manifest/activity-element#requireContentUriPermissionFromCaller): This enforces specified permissions on the provided content URIs at activity launch.
- [`ComponentCaller` class](https://developer.android.com/reference/android/app/ComponentCaller) for `Activity` callers: This represents the app that launched the activity.

## Accessibility

Android 15 adds features that improve accessibility for users.

### Better Braille

In Android 15, we've made it possible for [TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback) to support Braille
displays that are using the HID standard over both USB and secure Bluetooth.

This standard, much like the one used by mice and keyboards, will help Android
support a wider range of Braille displays over time.

## Internationalization

Android 15 adds features and capabilities that complement the user experience
when a device is used in different languages.

### CJK variable font

Starting with Android 15, the font file for Chinese, Japanese, and Korean (CJK)
languages, NotoSansCJK, is now a variable font. Variable fonts open up
possibilities for creative typography in CJK languages. Designers can explore a
broader range of styles and create visually striking layouts that were
previously difficult or impossible to achieve.
![](https://developer.android.com/static/about/versions/15/images/cjk-variable-font.png) How the variable font for Chinese, Japanese, and Korean (CJK) languages appears with different font widths.

### Inter-character justification

Starting with Android 15, text can be justified utilizing letter spacing by
using [`JUSTIFICATION_MODE_INTER_CHARACTER`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_INTER_CHARACTER). Inter-word justification was
first introduced in Android 8.0 (API level 26), and inter-character
justification provides similar capabilities for languages that use the
whitespace character for segmentation, such as Chinese, Japanese, and others.  
![](https://developer.android.com/static/about/versions/15/images/none-japanese.png)  
Layout for Japanese text using [`JUSTIFICATION_MODE_NONE`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_NONE).  
![](https://developer.android.com/static/about/versions/15/images/none-english.png)  
Layout for English text using [`JUSTIFICATION_MODE_NONE`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_NONE).

<br />

![](https://developer.android.com/static/about/versions/15/images/inter-word-japanese.png)  
Layout for Japanese text using [`JUSTIFICATION_MODE_INTER_WORD`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_INTER_WORD).  
![](https://developer.android.com/static/about/versions/15/images/inter-word-english.png)  
Layout for English text using [`JUSTIFICATION_MODE_INTER_WORD`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_INTER_WORD).

<br />

![](https://developer.android.com/static/about/versions/15/images/inter-character-japanese.png)  
Layout for Japanese text using the [`JUSTIFICATION_MODE_INTER_CHARACTER`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_INTER_CHARACTER).  
![](https://developer.android.com/static/about/versions/15/images/inter-character-english.png)  
Layout for English text using the [`JUSTIFICATION_MODE_INTER_CHARACTER`](https://developer.android.com/reference/android/text/Layout#JUSTIFICATION_MODE_INTER_CHARACTER).

### Automatic line break configuration

Android started supporting phrase-based line breaks for Japanese and Korean in
Android 13 (API level 33). However, while phrase-based line breaks improve the
readability of short lines of text, they don't work well for long lines of text.
In Android 15, apps can apply phrase-based line breaks only for short lines
of text, using the [`LINE_BREAK_WORD_STYLE_AUTO`](https://developer.android.com/reference/kotlin/android/graphics/text/LineBreakConfig#line_break_style_auto)
option. This option selects the best word style option for the text.

For short lines of text, phrase-based line breaks are used, functioning the same
as [`LINE_BREAK_WORD_STYLE_PHRASE`](https://developer.android.com/reference/kotlin/android/graphics/text/LineBreakConfig#line_break_word_style_phrase), as shown in the
following image:
![](https://developer.android.com/static/about/versions/15/images/line-break-auto-short.png) For short lines of text, `LINE_BREAK_WORD_STYLE_AUTO` applies phrase-based line breaks to improve the readability of the text. This is the same as applying `LINE_BREAK_WORD_STYLE_PHRASE`.

For longer lines of text, `LINE_BREAK_WORD_STYLE_AUTO` uses a no
line-break word style, functioning the same as
[`LINE_BREAK_WORD_STYLE_NONE`](https://developer.android.com/reference/kotlin/android/graphics/text/LineBreakConfig#line_break_word_style_none), as shown in the
following image:
![](https://developer.android.com/static/about/versions/15/images/line-break-auto-long.png) For long lines of text, `LINE_BREAK_WORD_STYLE_AUTO` applies no line-break word style to improve the readability of the text. This is the same as applying `LINE_BREAK_WORD_STYLE_NONE`.

### Additional Japanese Hentaigana Font

In Android 15, a font file for old Japanese Hiragana (known as Hentaigana)
is bundled by default. The unique shapes of Hentaigana characters can add a
distinctive flair to artwork or design while also helping to preserve accurate
transmission and understanding of ancient Japanese documents.
![](https://developer.android.com/static/about/versions/15/images/hentaigana-font.png) Character and text style for the Japanese Hentaigana font.

*** ** * ** ***

*VideoLAN cone Copyright (c) 1996-2010 VideoLAN. This logo or a modified version
may be used or modified by anyone to refer to the VideoLAN project or any
product developed by the VideoLAN team, but does not indicate endorsement by the
project.*

*Vulkan and the Vulkan logo are registered trademarks of the Khronos Group Inc.*

*OpenGL is a registered trademark and the OpenGL ES logo is a trademark of
Hewlett Packard Enterprise used by permission by Khronos.*