---
title: https://developer.android.com/media/platform/sharing-audio-input
url: https://developer.android.com/media/platform/sharing-audio-input
source: md.txt
---

Audio input usually comes from the built-in mic, an external mic, or an
audio interface attached to the device. Audio input can also come from
a phone conversation.

Sometimes two or more apps might both want to "capture" the same audio input.
They may be performing different tasks.
For example, some apps that receive audio might be "recording," like a simple voice recorder,
while other apps might be "listening," like the Google Assistant or an accessibility service that
respond to voice commands.

In either case, these apps want to receive audio input.
Throughout this page, we use the term "capture" regardless of whether an
app is recording or just listening.

If two or more apps want to capture audio at the same time, there can be a problem
delivering the audio signal from the same source to all of them. This page describes
how the Android system shares audio input between multiple apps that capture audio.

## Pre-Android 10 behavior

Before Android 10 the input audio stream could only be captured by one app at a
time. If some app was already recording or listening to audio, your app could
create an `AudioRecord` object, but an error would be returned when you called
[`AudioRecord.startRecording()`](https://developer.android.com/reference/android/media/AudioRecord#startRecording(android.media.MediaSyncEvent))
and the recording would not start.

One exception to this rule was when a privileged app (like Google Assistant or an
accessibility service) had the permission
`android.permission.CAPTURE_AUDIO_HOTWORD` and used an audio source of type
`HOTWORD`. In this case another app could start recording. When that happened the
privileged app terminated and the new app captured the input.

One more change was added in Android 9: only apps running in the foreground (or
a foreground service) could capture the audio input. When an app without a
foreground service or foreground UI component started to capture, the app
continued running but received silence, even if it was the only app capturing
audio at the time.

## Android 10 behavior

The behavior prior to Android 10 is "first come, first served."
Once an app starts to capture audio, no other apps can access the
audio input until the app that is capturing audio stops.

Android 10 imposes a priority scheme that can switch the input audio stream
between apps while they are running. In most cases, if a new app acquires the audio input,
the previously capturing app continues to run, but receives silence. In some
cases the system can continue to deliver audio to both apps. The various
[sharing scenarios](https://developer.android.com/media/platform/sharing-audio-input#sharing_scenarios) are explained below.

This scheme is similar to the way audio focus handles multiple apps
contending for the use of the audio output. However, audio focus is managed by
programmatic requests to gain and release focus, while the input switching
scheme described here is based on a prioritization policy that's applied
automatically whenever a new app starts to capture audio.

For the purpose of capturing audio, Android distinguishes two kinds of apps:

- "Ordinary" apps are installed by the user.
- "Privileged" apps come pre-installed on the device. These include the Google Assistant, and all accessibility services.

In addition, an app is treated differently
if it uses a "privacy-sensitive" audio source:
[`CAMCORDER`](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#CAMCORDER)
or [`VOICE_COMMUNICATION`](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#VOICE_COMMUNICATION).

The prioritization rules for using and sharing audio input are as follows:

- Privileged apps have higher priority than ordinary apps.
- Apps with visible foreground UIs have higher priority than background apps.
- Apps capturing audio from a privacy-sensitive source have higher priority than apps that are not.
- Two ordinary apps can never capture audio at the same time.
- In some situations, a privileged app can share audio input with another app.
- If two background apps of same priority are capturing audio, the last one started has higher priority.

### Sharing scenarios

When two apps are trying to capture audio,
they both may be able to receive the input signal, or one of them may receive
silence.

There are four main scenarios:

- Assistant + ordinary app
- Accessibility service + ordinary app
- Two ordinary apps
- Voice call + ordinary app

#### Assistant + ordinary app

The Assistant is a privileged app because it is pre-installed and it holds the
role [`RoleManager.ROLE_ASSISTANT`](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_ASSISTANT).
Any other pre-installed app with this role is treated similarly.

Android shares the input audio according to these rules:

- The Assistant can receive audio (no matter whether it's in the foreground or background)
  unless another app using a privacy-sensitive audio source is already capturing.

- The app receives audio unless the Assistant has a visible UI
  component on top of the screen.

Note that both apps receive audio only when the Assistant is in the background
and the other app is not capturing from a privacy-sensitive audio source.

#### Accessibility service + ordinary app

An [`AccessibilityService`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
requires a strict [declaration](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#declaration).

Android shares the input audio according to these rules:

- If the service's UI is on top, both the service and the app receive
  audio input. This behavior offers functionality like controlling a voice call or video
  capture with voice commands.

- If the service is not on top, this case is treated like the ordinary two-app case below.

#### Two ordinary apps

When two apps are capturing concurrently, only one app receives audio and the other gets silence.

Android shares the input audio according to these rules:

- If neither app is privacy-sensitive, the app with a UI on top receives audio. If neither app has a UI, the one that started capture the most recently receives audio.
- If one of the apps is privacy-sensitive, it receives audio and the other app gets silence even if it has a UI on top or started capturing more recently.
- If both apps are privacy-sensitive, the app which started capturing most recently receives audio and the other gets silence.

#### Voice call + ordinary app

A voice call is active if the audio mode returned by
[`AudioManager.getMode()`](https://developer.android.com/reference/android/media/AudioManager#getMode()) is
[`MODE_IN_CALL`](https://developer.android.com/reference/android/media/AudioManager#MODE_IN_CALL) or
[`MODE_IN_COMMUNICATION`](https://developer.android.com/reference/android/media/AudioManager#MODE_IN_COMMUNICATION).

Android shares the input audio according to these rules:

- The call always receives audio.
- The app can capture audio if it is an [accessibility service](https://developer.android.com/media/platform/sharing-audio-input#accessibility_service_ordinary_app).
- The app can capture the voice call if it is a privileged
  (pre-installed) app with permission
  [`CAPTURE_AUDIO_OUTPUT`](https://developer.android.com/reference/android/Manifest.permission#CAPTURE_AUDIO_OUTPUT).

  To capture the voice call's uplink (TX), downlink (RX), or both, the app must
  specify the audio sources
  [`MediaRecorder.AudioSource.VOICE_UPLINK`](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#VOICE_UPLINK) or
  [`MediaRecorder.AudioSource.VOICE_DOWNLINK`](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#VOICE_DOWNLINK),
  and/or the device [`AudioDeviceInfo.TYPE_TELEPHONY`](https://developer.android.com/reference/android/media/AudioDeviceInfo#TYPE_TELEPHONY).

## Android 11 behavior

Android 11 (API level 30) observes the Android 10 priority scheme
described above. It also provides new methods in `AudioRecord`, `MediaRecorder`, and
`AAudioStream` that enable and disable the ability to capture audio concurrently,
regardless of the selected use case.

The new methods are:

- [`AudioRecord.Builder.setPrivacySensitive()`](https://developer.android.com/reference/android/media/AudioRecord.Builder#setPrivacySensitive(boolean))
- [`AudioRecord.isPrivacySensitive()`](https://developer.android.com/reference/android/media/AudioRecord#isPrivacySensitive())
- [`MediaRecorder.setPrivacySensitive()`](https://developer.android.com/reference/android/media/MediaRecorder#setPrivacySensitive(boolean))
- [`MediaRecorder.isPrivacySensitive()`](https://developer.android.com/reference/android/media/MediaRecorder#isPrivacySensitive())
- [`AAudioStreamBuilder_setPrivacySensitive()`](https://developer.android.com/ndk/reference/group/audio#aaudiostreambuilder_setprivacysensitive)
- [`AAudioStream_isPrivacySensitive()`](https://developer.android.com/ndk/reference/group/audio#aaudiostream_isprivacysensitive)

When `setPrivacySensitive()` is `true`, the capture use case is private and even
a privileged Assistant cannot capture concurrently. This setting overrides the
default behavior that depends on the audio source. For instance,
`VOICE_COMMUNICATION` is private by default but `UNPROCESSED` is not.

## Configuration changes

When several apps are capturing audio simultaneously, only one or two them are
"active" (receiving audio); the others are muted (receiving silence). When the
active apps change, the audio framework might reconfigure the audio paths
according to these rules:

- The audio input device for each active app might change (for example, from the built-in microphone to an attached bluetooth headset).
- The preprocessing associated with the highest-priority active app is enabled. All other preprocessing is ignored.

Since an active app might be silenced when a higher-priority app becomes active,
you can register an
[AudioManager.AudioRecordingCallback](https://developer.android.com/reference/android/media/AudioManager.AudioRecordingCallback)
on the [`AudioRecord`](https://developer.android.com/reference/android/media/AudioRecord)
or [`MediaRecorder`](https://developer.android.com/reference/android/media/MediaRecorder)
object to be notified when the configuration changes.
The possible changes could be:

- Capture silenced or unsilenced
- Device changed
- Preprocessing changed
- Stream properties changed (sampling rate, channel mask, sample format)

You must call
[`AudioRecord.registerAudioRecordingCallback()`](https://developer.android.com/reference/android/media/AudioRecord#registerAudioRecordingCallback(java.util.concurrent.Executor,%2520android.media.AudioManager.AudioRecordingCallback))
before the capture is started.
The callback is executed only when the app is receiving audio and a change occurs.

The method [`onRecordingConfigChanged()`](https://developer.android.com/reference/android/media/AudioManager.AudioRecordingCallback#onRecordingConfigChanged(java.util.List%3Candroid.media.AudioRecordingConfiguration%3E)) returns an [`AudioRecordingConfiguration`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration) containing the current audio capture state. Use the following
methods to learn about the change:

[`isClientSilenced()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#isClientSilenced())
:   Returns true if the audio returned to the client is currently being silenced due to the capture policy.

[`getAudioDevice()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#getAudioDevice())
:   Returns the active audio device.

[`getEffects()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#getEffects())
:   Returns the active preprocessing effect. Note that the active effect might not be the same as those returned by [`getClientEffects()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#getClientEffects()) if the client is not the highest-priority active app.

[`getFormat()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#getFormat())
:   Returns the stream properties. Note that the actual audio data received by the client always respects the required format returned by [`getClientFormat()`](https://developer.android.com/reference/android/media/AudioRecordingConfiguration#getClientFormat()). The framework automatically performs the necessary resampling, channel, and format conversion from the format used at the hardware interface to the format specified by the client.

[`AudioRecord.getActiveRecordingConfiguration()`](https://developer.android.com/reference/android/media/AudioRecord#getActiveRecordingConfiguration()).
:   Returns the active recording configuration.

You can get a general view of all active recordings on the device by calling
[`AudioManager.getActiveRecordingConfigurations()`](https://developer.android.com/reference/android/media/AudioManager#getActiveRecordingConfigurations()).