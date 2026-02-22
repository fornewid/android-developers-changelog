---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The spatial audio features in Jetpack SceneCore empower you to craft immersive
audio experiences within your Android XR applications.

Spatial audio simulates how users perceive sound in a 3D environment. It creates
the sensation of sound emanating from all directions, including above and below
the user. The system does this by simulating one or more "virtual speakers" at
specific locations in 3D space.

Existing apps that haven't been designed for or modified for Android XR have
their audio automatically spatialized in Android XR. As the user moves around
their space, all app audio will be emitted from the panel which the app's UI is
rendered onto. For example, if a timer goes off from a clock app, the audio
would sound like it's coming from the app panel position. Android XR will
automatically alter the sound for positional realism. For example, the perceived
distance between the app panel and the user will subtly impact the audio volume
for a greater sense of realism.

For more information on how existing apps render spatial audio, read [Add stereo
and surround sound to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio#add-stereo) on this page.

> [!NOTE]
> **Note:** The user can choose to disable spatial audio effects on an app or system level and choose stereo instead.

If you are optimizing your app for XR, Jetpack SceneCore provides tools for
advanced spatial audio customization. You can precisely position sounds in the
3D environment, use ambisonic audio for realistic sound fields, and take
advantage of built-in surround sound integration.

## Types of spatial audio available in Android XR

Android XR supports positional, stereo, surround sound, and ambisonic audio.

### Positional audio

A positional audio can be positioned to play from a specific point in 3D space.
For example, you can have a [3D model](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models) of a dog barking at the corner of your
virtual environment. You can have multiple entities emitting sound from each of
their respective positions. To render positional audio, files must be mono or
stereo.

### Spatialized stereo and surround sound

All [Android media formats](https://developer.android.com/media/platform/supported-formats#audio-formats) are supported for positional, stereo, and
surround sound. In addition to these formats, Android XR devices may support
[Dolby Atmos](https://professional.dolby.com/content-creation/Dolby-Atmos-for-content-creators/), [Dolby Digital](https://professional.dolby.com/tv/dolby-digital/), and [Dolby Digital+](https://professional.dolby.com/technologies/dolby-digital-plus/) audio formats.

Stereo audio refers to audio formats with two channels and surround sound refers
to audio formats with more than two channels, such as [5.1 surround
sound](https://en.wikipedia.org/wiki/5.1_surround_sound) or [7.1 surround sound](https://en.wikipedia.org/wiki/7.1_surround_sound)
configurations. Each channel's sound data is associated with one speaker. For
example, when playing music in stereo, the left speaker channel may emit
different instrument tracks than the right.

Surround sound is often used in movies and television shows to enhance realism
and immersion through the use of multiple speaker channels. For example,
dialogue often plays from a center speaker channel while the sound of a
helicopter flying may use different channels in sequence to give the sense that
the helicopter is flying around your 3D space.

### Ambisonic audio

[Ambisonic](https://en.wikipedia.org/wiki/Ambisonics) audio (or ambisonics) is like a skybox for audio,
providing an immersive soundscape for your users. Use ambisonics for background
environmental sounds or other scenarios where you want to replicate a
full-spherical sound field that surrounds the listener. Android XR supports the
[AmbiX](https://github.com/iem-projects/ambix) ambisonic audio format in first-, second- and third-order
ambisonics. We recommend the [Opus](https://www.opus-codec.org/) (`.ogg`) and
[PCM/Wave](https://en.wikipedia.org/wiki/WAV) (`.wav`) file types.

## Use spatial audio with Jetpack SceneCore

Implementing spatial audio with Jetpack SceneCore involves checking for spatial
capabilities and choosing an API for loading spatial audio.

### Check for spatial capabilities

Before using spatial audio features, check that the [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session) supports
spatial audio. In all of the code snippets in the following sections,
capabilities are checked before attempting to play spatialized audio.

> [!NOTE]
> **Note:** If your app uses the same code for form factors other than Android XR, the [traditional check for spatial capabilities](https://developer.android.com/media/grow/spatial-audio#query) always returns true in Android XR.

### Load spatial audio

You can use any of the following APIs to load spatial audio for use in Jetpack
SceneCore.

- [`SoundPool`](https://developer.android.com/reference/android/media/SoundPool): Ideal for short sound effects that are less than 1 MB in size, they are loaded ahead of time and the sounds can be used repeatedly. This is a great way to load audio for positional audio.
- [`ExoPlayer`](https://developer.android.com/media/media3/exoplayer): Ideal for loading stereo and surround sound content such as music and video. Also allows for background media playback.
- [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer): Provides the simplest way to load ambisonic audio.
- [`AudioTrack`](https://developer.android.com/reference/android/media/AudioTrack): Provides the most control over how to load audio data. Allows for directly writing buffers of audio or if you synthesized or decoded your own audio files.

### Check for media format support

Some media formats are [supported by the Android platform](https://developer.android.com/media/platform/supported-formats#audio-formats). However, a
particular Android XR device might support additional formats, such as
[Dolby Atmos](https://professional.dolby.com/content-creation/Dolby-Atmos-for-content-creators/). To query for media format support, use ExoPlayer's
[`AudioCapabilities`](https://developer.android.com/reference/kotlin/androidx/media3/exoplayer/audio/AudioCapabilities):


```kotlin
val audioCapabilities = AudioCapabilities.getCapabilities(context, androidx.media3.common.AudioAttributes.DEFAULT, null)
if (audioCapabilities.supportsEncoding(C.ENCODING_AC3)) {
    // Device supports playback of the Dolby Digital media format.
}
if (audioCapabilities.supportsEncoding(C.ENCODING_E_AC3)) {
    // Device supports playback of the Dolby Digital Plus media format.
}
if (audioCapabilities.supportsEncoding(C.ENCODING_E_AC3_JOC)) {
    // Device supports playback of the Dolby Digital Plus with Dolby Atmos media format.
}
```

<br />

Checking for these capabilities may potentially involve blocking calls, and
[should not be called on the main thread](https://developer.android.com/topic/performance/threads).

> [!NOTE]
> **Note:** If you are using ExoPlayer, it will automatically attempt to select audio formats with higher track counts, such as Dolby Digital or Dolby Digital Plus, and object-based formats like Dolby Atmos, when supported by the device and audio output routing.

### Add positional audio to your app

Positional sound sources are defined by [`PointSourceParams`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PointSourceParams) and an
associated [`Entity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Entity). The position and orientation of the `Entity` dictates
where the `PointSourceParams` is rendered in 3D space.

> [!IMPORTANT]
> **Important:** To properly render positional audio, the files must be mono or stereo and the Usage in [`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes) must not be [`USAGE_MEDIA`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA), nor can the ContentType be [`CONTENT_TYPE_MOVIE`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MOVIE), [`CONTENT_TYPE_MUSIC`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MUSIC), or [`CONTENT_TYPE_SPEECH`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SPEECH).

#### Positional audio example

The following example loads a sound effect audio file into a sound pool and
plays it back at the position of the `Entity`.


```kotlin
// Check spatial capabilities before using spatial audio
if (session.scene.spatialCapabilities.contains(SpatialCapability.SPATIAL_AUDIO)
) { // The session has spatial audio capabilities
    val maxVolume = 1F
    val lowPriority = 0
    val infiniteLoop = -1
    val normalSpeed = 1F

    val soundPool = SoundPool.Builder()
        .setAudioAttributes(
            AudioAttributes.Builder()
                .setContentType(CONTENT_TYPE_SONIFICATION)
                .setUsage(USAGE_ASSISTANCE_SONIFICATION)
                .build()
        )
        .build()

    val pointSource = PointSourceParams(entity)

    val soundEffect = appContext.assets.openFd("sounds/tiger_16db.mp3")
    val pointSoundId = soundPool.load(soundEffect, lowPriority)

    soundPool.setOnLoadCompleteListener { soundPool, sampleId, status ->
        // wait for the sound file to be loaded into the soundPool
        if (status == 0) {
            SpatialSoundPool.play(
                session = session,
                soundPool = soundPool,
                soundID = pointSoundId,
                params = pointSource,
                volume = maxVolume,
                priority = lowPriority,
                loop = infiniteLoop,
                rate = normalSpeed
            )
        }
    }
} else {
    // The session does not have spatial audio capabilities
}
```

<br />

**Key points about the code**

- The first step is to check if Spatial Audio capabilities are currently available by using [`spatialCapabilities`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene#spatialCapabilities()).
- Setting the contentType to [`CONTENT_TYPE_SONIFICATION`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SONIFICATION) and usage to [`USAGE_ASSISTANCE_SONIFICATION`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANCE_SONIFICATION) lets the system treat this audio file as a sound effect.
- The preceding example loads the audio file into the pool immediately before using it to keep the code together for simplicity. Ideally, you should load all of your sound effects asynchronously as you load your app so all the audio files are available in the pool when you need it.

### Add stereo and surround sound to your app

The recommended way to add stereo and surround sound to your app is by using
`Exoplayer`. For more information on how to use Spatial Audio with `Exoplayer`,
refer to the [Spatial Audio guide](https://developer.android.com/media/grow/spatial-audio).

> [!IMPORTANT]
> **Important:** To properly render Stereo or Surround sound, the files must have two or more channels and the Usage in [`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes) must be [`USAGE_MEDIA`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA) or the ContentType must be [`CONTENT_TYPE_MOVIE`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MOVIE), [`CONTENT_TYPE_MUSIC`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_MUSIC), or [`CONTENT_TYPE_SPEECH`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SPEECH).

#### Stereo and surround sound speaker positioning

With surround sound speaker positioning, the virtual surround sound speakers are
positioned and oriented relative to a center speaker, around the user in a
standard [ITU configuration](https://en.wikipedia.org/wiki/5.1_surround_sound#Speaker_placement).

By default, the center channel speaker is placed on the app's
[`mainPanelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene#mainPanelEntity()). This includes mobile apps that have their audio
spatialized automatically by Android XR.

For stereo, speaker placement is similar to surround sound, except with only the
left and right channels positioned on the left and right side of the panel,
respectively.

If you have multiple panels and you want to choose which panel emits audio, or
if you want the stereo or surround audio to render relative to another `Entity`,
you can use the `PointSourceAttributes` to define the location of the center
channel. The remaining channels will be placed as mentioned previously. In these
situations, you must also use [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer).

As the user moves around their space, the stereo and surround sound virtual
speakers will move and adjust to ensure that the speakers are always in an
optimal position.

If you have configured the [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer) or [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) to continue
playing stereo or surround sound from the background, virtual speaker
positioning will be altered when the app is backgrounded. Because there's no
panel or other point in space to anchor the sound to, the spatial audio moves
with the user (in other words, it's "head-locked").

#### Surround sound example

The following example loads a 5.1 audio file using `MediaPlayer` and sets the
center channel of the file to be an `Entity`.


```kotlin
// Check spatial capabilities before using spatial audio
if (session.scene.spatialCapabilities.contains(SpatialCapability.SPATIAL_AUDIO)) {
    // The session has spatial audio capabilities

    val pointSourceAttributes = PointSourceParams(session.scene.mainPanelEntity)

    val mediaPlayer = MediaPlayer()

    val fivePointOneAudio = appContext.assets.openFd("sounds/aac_51.ogg")
    mediaPlayer.reset()
    mediaPlayer.setDataSource(fivePointOneAudio)

    val audioAttributes =
        AudioAttributes.Builder()
            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
            .setUsage(AudioAttributes.USAGE_MEDIA)
            .build()

    SpatialMediaPlayer.setPointSourceParams(
        session,
        mediaPlayer,
        pointSourceAttributes
    )

    mediaPlayer.setAudioAttributes(audioAttributes)
    mediaPlayer.prepare()
    mediaPlayer.start()
} else {
    // The session does not have spatial audio capabilities
}
```

<br />

**Key points about the code**

- Like in the [positional audio example](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio#positional-audio-example), the first step is to check if spatial audio capabilities are available by using [`spatialCapabilities`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene#spatialCapabilities()).
- Setting the `contentType` to [`AudioAttributes.CONTENT_TYPE_MUSIC`](https://developer.android.com/reference/android/media/AudioAttributes) and usage to [`AudioAttributes.USAGE_MEDIA`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA) lets the system treat this audio file as surround sound.

### Add ambisonic sound fields to your app

The simplest way to play back ambisonic sound fields is by loading the file with
a `MediaPlayer`. Since ambisonic sound applies to the entire soundscape, you do
not need to specify an `Entity` to provide a position. Instead, you create an
instance of the [`SoundFieldAttributes`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SoundFieldAttributes) with the appropriate ambisonic
order specifying the number of channels.

#### Ambionics example

The following example plays an ambisonic sound field using `MediaPlayer`.


```kotlin
// Check spatial capabilities before using spatial audio
if (session.scene.spatialCapabilities.contains(SpatialCapability.SPATIAL_AUDIO)) {
    // The session has spatial audio capabilities

    val soundFieldAttributes =
        SoundFieldAttributes(SpatializerConstants.AmbisonicsOrder.FIRST_ORDER)

    val mediaPlayer = MediaPlayer()

    val soundFieldAudio = appContext.assets.openFd("sounds/foa_basketball_16bit.wav")

    mediaPlayer.reset()
    mediaPlayer.setDataSource(soundFieldAudio)

    val audioAttributes =
        AudioAttributes.Builder()
            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
            .setUsage(AudioAttributes.USAGE_MEDIA)
            .build()

    SpatialMediaPlayer.setSoundFieldAttributes(
        session,
        mediaPlayer,
        soundFieldAttributes
    )

    mediaPlayer.setAudioAttributes(audioAttributes)
    mediaPlayer.prepare()
    mediaPlayer.start()
} else {
    // The session does not have spatial audio capabilities
}
```

<br />

**Key points about the code**

- As with the previous snippets, the first step is to check if Spatial Audio capabilities are available using [`hasCapability()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities#hasCapability(kotlin.Int)).
- The `contentType` and usage are purely informational.
- The [`AMBISONICS_ORDER_FIRST_ORDER`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatializerConstants#AMBISONICS_ORDER_FIRST_ORDER()) signals to SceneCore that the sound field file defines four channels.