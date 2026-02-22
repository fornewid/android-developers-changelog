---
title: https://developer.android.com/training/tv/playback/audio-capabilities
url: https://developer.android.com/training/tv/playback/audio-capabilities
source: md.txt
---

Android TV devices can have multiple audio outputs connected at the same time:
TV speakers, HDMI-connected home cinema, Bluetooth headphones, and so on.
These audio output devices can support different audio capabilities,
like encodings (Dolby Digital+, DTS, and PCM), sample rate, and channels.
For example, HDMI-connected TVs have support for a multitude of encodings
while connected Bluetooth headphones usually support just PCM.

The list of available audio devices and the routed audio device can also change
by hot-plugging HDMI devices, connecting or disconnecting Bluetooth headphones,
or the user changing audio settings. Since the audio output capabilities can
change even when apps are playing media, apps need to gracefully adapt to these
changes and continue playback on the new routed audio device and its
capabilities. Outputting the wrong audio format can result in errors or
no sound playing.

Apps have the capability to output the same content in multiple encodings
to offer the user the best audio experience depending on audio device
capabilities. For example, a Dolby Digital encoded audio stream is played
if the TV supports it, while a more widely-supported PCM audio stream is
chosen when there is no support for Dolby Digital. The list of built-in Android
decoders used to transform an audio stream into PCM can be found in
[Supported media formats](https://developer.android.com/guide/topics/media/media-formats).

At playback time, the streaming app should create an
[`AudioTrack`](https://developer.android.com/reference/android/media/AudioTrack) with the best
[`AudioFormat`](https://developer.android.com/reference/android/media/AudioFormat) supported by the output
audio device.

## Create a track with the right format

Apps should create an `AudioTrack`, start playing it, and call
[`getRoutedDevice()`](https://developer.android.com/reference/android/media/AudioRouting#getRoutedDevice())
to determine the default audio device from which to play sound.
This can be, for example, a safe short silence PCM encoded track used only to
determine the routed device and its audio capabilities.

### Get supported encodings

Use
[`getAudioProfiles()`](https://developer.android.com/reference/android/media/AudioDeviceInfo#getAudioProfiles())
(API level 31 and higher) or
[`getEncodings()`](https://developer.android.com/reference/android/media/AudioDeviceInfo#getEncodings())
(API level 23 and higher) to determine the audio formats available on the
default audio device.

### Check supported audio profiles and formats

Use [`AudioProfile`](https://developer.android.com/reference/android/media/AudioProfile)
(API level 31 and higher) or
[`isDirectPlaybackSupported()`](https://developer.android.com/reference/android/media/AudioTrack#isDirectPlaybackSupported(android.media.AudioFormat,%20android.media.AudioAttributes))
(API level 29 and higher) to check supported combinations of format,
channel count, and sample rate.

Some Android devices are capable of supporting encodings beyond the ones
supported by the output audio device. These additional formats should be
detected through `isDirectPlaybackSupported()`. In these cases the audio data
is re-encoded to a format that is supported by the output audio device. Use
`isDirectPlaybackSupported()` to properly check support for the desired format
even if it is not present in the list returned by `getEncodings()`.
| **Note:** Before API level 33, `isDirectPlaybackSupported()` considers all available audio output paths, even those which are not currently routed. For example, consider what occurs when you have connected both HDMI that supports direct playback and Bluetooth headphones that do not. Here, the function returns true, even though audio might play only on the Bluetooth headphones and creation of a direct `AudioTrack` fails. You can create a direct AudioTrack by setting the [`FLAG_HW_AV_SYNC`](https://developer.android.com/reference/android/media/AudioAttributes#FLAG_HW_AV_SYNC). For API level 33 and higher this only considers the currently active audio routing.

### Anticipatory audio route

Android 13 (API level 33) introduced anticipatory audio routes. You can
anticipate device audio attribute support and prepare tracks for the active
audio device. You can use
[`getDirectPlaybackSupport()`](https://developer.android.com/reference/android/media/AudioManager#getDirectPlaybackSupport(android.media.AudioFormat,%20android.media.AudioAttributes))
to check whether direct playback is supported on the currently routed audio
device for a given format and attributes:  

### Kotlin

```kotlin
val format = AudioFormat.Builder()
    .setEncoding(AudioFormat.ENCODING_E_AC3)
    .setChannelMask(AudioFormat.CHANNEL_OUT_5POINT1)
    .setSampleRate(48000)
    .build()
val attributes = AudioAttributes.Builder()
    .setUsage(AudioAttributes.USAGE_MEDIA)
    .build()

if (AudioManager.getDirectPlaybackSupport(format, attributes) !=
    AudioManager.DIRECT_PLAYBACK_NOT_SUPPORTED
) {
    // The format and attributes are supported for direct playback
    // on the currently active routed audio path
} else {
    // The format and attributes are NOT supported for direct playback
    // on the currently active routed audio path
}
```

### Java

```java
AudioFormat format = new AudioFormat.Builder()
        .setEncoding(AudioFormat.ENCODING_E_AC3)
        .setChannelMask(AudioFormat.CHANNEL_OUT_5POINT1)
        .setSampleRate(48000)
        .build();
AudioAttributes attributes = new AudioAttributes.Builder()
        .setUsage(AudioAttributes.USAGE_MEDIA)
        .build();

if (AudioManager.getDirectPlaybackSupport(format, attributes) !=
        AudioManager.DIRECT_PLAYBACK_NOT_SUPPORTED) {
    // The format and attributes are supported for direct playback
    // on the currently active routed audio path
} else {
    // The format and attributes are NOT supported for direct playback
    // on the currently active routed audio path
}
```

Alternatively, you can query which profiles are supported for direct media
playback through the currently routed audio device. This excludes any profiles
that are unsupported or would be, for instance, transcoded by the Android
framework:  

### Kotlin

```kotlin
private fun findBestAudioFormat(audioAttributes: AudioAttributes): AudioFormat {
    val preferredFormats = listOf(
        AudioFormat.ENCODING_E_AC3,
        AudioFormat.ENCODING_AC3,
        AudioFormat.ENCODING_PCM_16BIT,
        AudioFormat.ENCODING_DEFAULT
    )
    val audioProfiles = audioManager.getDirectProfilesForAttributes(audioAttributes)
    val bestAudioProfile = preferredFormats.firstNotNullOf { format ->
        audioProfiles.firstOrNull { it.format == format }
    }
    val sampleRate = findBestSampleRate(bestAudioProfile)
    val channelMask = findBestChannelMask(bestAudioProfile)
    return AudioFormat.Builder()
        .setEncoding(bestAudioProfile.format)
        .setSampleRate(sampleRate)
        .setChannelMask(channelMask)
        .build()
}
```

### Java

```java
private AudioFormat findBestAudioFormat(AudioAttributes audioAttributes) {
    Stream<Integer> preferredFormats = Stream.<Integer>builder()
            .add(AudioFormat.ENCODING_E_AC3)
            .add(AudioFormat.ENCODING_AC3)
            .add(AudioFormat.ENCODING_PCM_16BIT)
            .add(AudioFormat.ENCODING_DEFAULT)
            .build();
    Stream<AudioProfile> audioProfiles =
            audioManager.getDirectProfilesForAttributes(audioAttributes).stream();
    AudioProfile bestAudioProfile = (AudioProfile) preferredFormats.map(format ->
            audioProfiles.filter(profile -> profile.getFormat() == format)
                    .findFirst()
                    .orElseThrow(NoSuchElementException::new)
    );
    Integer sampleRate = findBestSampleRate(bestAudioProfile);
    Integer channelMask = findBestChannelMask(bestAudioProfile);
    return new AudioFormat.Builder()
            .setEncoding(bestAudioProfile.getFormat())
            .setSampleRate(sampleRate)
            .setChannelMask(channelMask)
            .build();
}
```

In this example, `preferredFormats` is a list of
[`AudioFormat`](https://developer.android.com/reference/android/media/AudioFormat) instances. It is ordered
with the most preferred first in the list, and the least preferred last.
[`getDirectProfilesForAttributes()`](https://developer.android.com/reference/android/media/AudioManager#getDirectProfilesForAttributes(android.media.AudioAttributes))
returns a list of supported
[`AudioProfile`](https://developer.android.com/reference/android/media/AudioProfile) objects for the
currently routed audio device with the supplied
[`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes). The list of
preferred `AudioFormat` items is iterated through until a matching supported
`AudioProfile` is found. This `AudioProfile` is stored as `bestAudioProfile`.
Optimum sample rates and channel masks are determined from `bestAudioProfile`.
Finally, an appropriate [`AudioFormat`](https://developer.android.com/reference/android/media/AudioFormat)
instance is created.

### Create audio track

Apps should use this information to create an `AudioTrack` for the
highest-quality `AudioFormat` supported by the default audio device
(and available for the selected content).

## Intercept audio device changes

To intercept and react to audio device changes, apps should:

- For API levels equal to or greater than 24, add an [`OnRoutingChangedListener`](https://developer.android.com/reference/android/media/AudioRouting.OnRoutingChangedListener) to monitor audio device changes (HDMI, Bluetooth, and so on).
- For API level 23, register an [`AudioDeviceCallback`](https://developer.android.com/reference/android/media/AudioDeviceCallback) to receive changes in the available audio device list.
- For API levels 21 and 22, monitor for [HDMI plug events](https://developer.android.com/reference/android/media/AudioManager#ACTION_HDMI_AUDIO_PLUG) and use the extra data from the broadcasts.
- Also register a `BroadcastReceiver` to monitor [`BluetoothDevice`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice) state changes for devices lower than API 23, since [`AudioDeviceCallback`](https://developer.android.com/reference/android/media/AudioDeviceCallback) is not yet supported.

When an audio device change has been detected for the `AudioTrack`, the app
should check the updated audio capabilities and, if needed, recreate
the `AudioTrack` with a different `AudioFormat`. Do this if a higher-quality
encoding is now supported or the previously-used encoding is
no-longer-supported.
| **Note:** Writing data to an `AudioTrack` in a no-longer-supported format can trigger errors from the framework (such as "Error -32 during AudioTrack native read"). These can happen even before the changing audio routing callback is called. Intercept them and recreate the `AudioTrack` according to the capabilities of the new routed-to device.

## Sample code

### Kotlin

```kotlin
// audioPlayer is a wrapper around an AudioTrack
// which calls a callback for an AudioTrack write error
audioPlayer.addAudioTrackWriteErrorListener {
    // error code can be checked here,
    // in case of write error try to recreate the audio track
    restartAudioTrack(findDefaultAudioDeviceInfo())
}

audioPlayer.audioTrack.addOnRoutingChangedListener({ audioRouting ->
    audioRouting?.routedDevice?.let { audioDeviceInfo ->
        // use the updated audio routed device to determine
        // what audio format should be used
        if (needsAudioFormatChange(audioDeviceInfo)) {
            restartAudioTrack(audioDeviceInfo)
        }
    }
}, handler)
```

### Java

```java
// audioPlayer is a wrapper around an AudioTrack
// which calls a callback for an AudioTrack write error
audioPlayer.addAudioTrackWriteErrorListener(new AudioTrackPlayer.AudioTrackWriteError() {
    @Override
    public void audioTrackWriteError(int errorCode) {
        // error code can be checked here,
        // in case of write error try to recreate the audio track
        restartAudioTrack(findDefaultAudioDeviceInfo());
    }
});

audioPlayer.getAudioTrack().addOnRoutingChangedListener(new AudioRouting.OnRoutingChangedListener() {
    @Override
    public void onRoutingChanged(AudioRouting audioRouting) {
        if (audioRouting != null && audioRouting.getRoutedDevice() != null) {
            AudioDeviceInfo audioDeviceInfo = audioRouting.getRoutedDevice();
            // use the updated audio routed device to determine
            // what audio format should be used
            if (needsAudioFormatChange(audioDeviceInfo)) {
                restartAudioTrack(audioDeviceInfo);
            }
        }
    }
}, handler);
```