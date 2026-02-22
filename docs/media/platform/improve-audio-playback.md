---
title: https://developer.android.com/media/platform/improve-audio-playback
url: https://developer.android.com/media/platform/improve-audio-playback
source: md.txt
---

# Improve audio playback

When you try to directly access the USB audio peripheral using the USB APIs, problems arise. These problems can include: security issues, limiting media playback from other apps, and loss of alarms, notifications, and ringtones over USB devices.

To improve audio playback, instead configure the mixer attributes.

### Configure mixer attributes

By using the[`AudioMixerAttributes`](https://developer.android.com/reference/android/media/AudioMixerAttributes)APIs, you can configure your app with preferred mixer attributes over USB.

When your app playback matches the encoding format, channel mask, and sample rate of the preferred mixer attributes, the playback is attached to the audio output stream whose mixer is configured with the preferred mixer attributes.

Your app can stream at any configuration to the hardware abstraction layer (HAL), and to the device, as long as the USB device supports the configuration.

The two allowed mixer behaviors in`AudioMixerAttributes`are`DEFAULT`and`BIT_PERFECT`. When the mixer behavior is`DEFAULT`, it indicates that audio data from different sources is mixed.

When the mixer behavior is`BIT_PERFECT`, no audio mixing, volume adjustment, or audio processed effect is applied to the playback. The data is sent as is to the HAL and finally down to the USB device.

Using`BIT_PERFECT`lets you direct stream digital (DSD) over pulse code modulation (PCM) on Android-powered devices. The following code sample shows how this can be accomplished:  

### Kotlin

```kotlin
val EXPECTED_FORMAT: AudioFormat = AudioFormat.Builder()
  .setEncoding(AudioFormat.ENCODING_PCM_24BIT_PACKED)
  .setChannelMask(AudioFormat.CHANNEL_OUT_STEREO)
  .setSampleRate(44100)
  .build()

fun startPlayback() {
  // Query all supported mixer attributes
  val mixerAttributesList: List<AudioMixerAttributes?> =
    mAudioManager.getSupportedMixerAttributes(usbDevice)

  // Find the wanted mixer attributes
  val mixerAttributes = mixerAttributesList.stream()
    .filter { mixerAttr: AudioMixerAttributes? ->
      EXPECTED_FORMAT.equals(
        mixerAttr!!.format
      )
    }
    .findAny()
    .orElse(null)

  // Register a listener to mixer attributes changed
  val listener = MyPreferredMixerAttributesChangedListener()
  mAudioManager.addOnPreferredMixerAttributesChangedListener(
    Executors.newSingleThreadExecutor(), listener
  )

  // Currently, only media usage over USB devices will be allowed
  val attr: AudioAttributes = AudioAttributes.Builder()
    .setUsage(AudioAttributes.USAGE_MEDIA).build()
  // Set preferred mixer attributes
  mAudioManager.setPreferredMixerAttributes(
    attr, usbDevice, mixerAttributes
  )

  // Start playback, note the playback and the audio format must
  // match what is set when calling `setPreferredMixerAttriutes`
  // API.
  val audioTrack = AudioTrack.Builder()
    .setAudioAttributes(attr)
    .setAudioFormat(mixerAttributes!!.format)
    .build()

  // Clear all preferred mixer attributes related stuff when
  // playback task is completed
  mAudioManager.clearPreferredMixerAttributes(attr, usbDevice)
  mAudioManager.removeOnPreferredMixerAttributesChangedListener(listener)
}

private class MyPreferredMixerAttributesChangedListener :
  AudioManager.OnPreferredMixerAttributesChangedListener {
  override fun onPreferredMixerAttributesChanged(
    attributes: AudioAttributes,
    device: AudioDeviceInfo,
    mixerAttributes: AudioMixerAttributes?,
  ) {
    // Do something when preferred mixer attributes changed
  }
}
```

### Java

```java
final AudioFormat EXPECTED_FORMAT = new AudioFormat.Builder()
        .setEncoding(AudioFormat.ENCODING_PCM_24BIT_PACKED)
        .setChannelMask(AudioFormat.CHANNEL_OUT_STEREO)
        .setSampleRate(44100)
        .build();

void startPlayback() {
    // Query all supported mixer attributes
    List<AudioMixerAttributes> mixerAttributesList =
    mAudioManager.getSupportedMixerAttributes(usbDevice);

    // Find the wanted mixer attributes
    AudioMixerAttributes mixerAttributes =
        mixerAttributesList.stream()
            .filter(mixerAttr -> EXPECTED_FORMAT.equals(mixerAttr.getFormat()))
            .findAny()
            .orElse(null);

    // Register a listener to mixer attributes changed
    MyPreferredMixerAttributesChangedListener listener =
        new MyPreferredMixerAttributesChangedListener();
    mAudioManager.addOnPreferredMixerAttributesChangedListener(
            Executors.newSingleThreadExecutor(), listener);

    // Currently, only media usage over USB devices will be allowed
    AudioAttributes attr = new AudioAttributes.Builder()
           .setUsage(AudioAttributes.USAGE_MEDIA).build();
    // Set preferred mixer attributes
    mAudioManager.setPreferredMixerAttributes(
            attr, usbDevice, mixerAttributes);

    // Start playback, note the playback and the audio format must
    // match what is set when calling `setPreferredMixerAttriutes`
    // API.
    AudioTrack audioTrack = new AudioTrack.Builder()
            .setAudioAttributes(attr)
            .setAudioFormat(mixerAttributes.getFormat())
            .build();

    // Clear all preferred mixer attributes related stuff when
    // playback task is completed
    mAudioManager.clearPreferredMixerAttributes(attr, usbDevice);
    mAudioManager.removeOnPreferredMixerAttributesChangedListener(
            listener);
}

private class MyPreferredMixerAttributesChangedListener
        implements AudioManager.OnPreferredMixerAttributesChangedListener {
    @Override
    public void onPreferredMixerAttributesChanged(
        AudioAttributes attributes,
        AudioDeviceInfo device,
        AudioMixerAttributes mixerAttributes) {
        // Do something when preferred mixer attributes changed
    }
}
```