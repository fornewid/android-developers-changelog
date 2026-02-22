---
title: Background audio hardening  |  Android Developers
url: https://developer.android.com/about/versions/17/changes/bg-audio
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Background audio hardening Stay organized with collections Save and categorize content based on your preferences.




Starting in Android 17, the audio framework enforces restrictions on background
audio interactions including audio playback, [audio focus](/media/optimize/audio-focus) requests, and
[volume change](/reference/android/media/AudioManager#adjustStreamVolume(int,%20int,%20int)) APIs to ensure that these changes are started intentionally
by the user.

If an app developer intends to control audio without a visible activity, they
should ensure that the app has a foreground service (that is not of type
`SHORT_SERVICE`) which was started with [while-in-use](/develop/background-work/services/fgs/restrictions-bg-start#wiu-restrictions-exemptions) (WIU) capabilities. A
foreground service is granted WIU capabilities if it is started in response to a
`MediaSessionEvent` or while the app is visible to the user.

If the app tries to call audio APIs while the app is not in a valid lifecycle,
the audio playback and volume change APIs fail silently without throwing an
exception or providing a failure message. The audio focus API fails with the
result code `AUDIOFOCUS_REQUEST_FAILED`.

The intention of introducing these restrictions is to reduce unintentional
background audio buggy experiences. Some examples include:

* Apps playing audio without a foreground service can be frozen. When the app
  is eventually unfrozen, it unexpectedly resumes audio playback, potentially
  hours later.
* Apps playing audio without a foreground service faced varied run
  restrictions which result in choppy audio performance.
* Playback detached from the activity lifecycle, which could result in a
  leaked playback session or leaked focus events which continue with no way
  for the user to stop playback.

We encourage developers to test their apps and provide feedback to the behavior
change if there's any intentional audio use cases negatively impacted.
Please report any issues using this [Android 17 app compat issue
tracker](/about/versions/17/report-issue-appcompat).

## Identify impacted background audio use cases

Audit your audio playback implementation and identify if your app intends to
provide background audio interaction functionality even in conditional
circumstances.

If your app only intends to play audio or utilize audio APIs while it is showing
an activity which is visible to the user, including using [Picture in Picture
(PiP) mode](/design/ui/mobile/guides/home-screen/picture-in-picture), then it is not affected by any of these changes.

If your app provides VOIP functionality, including video calling apps, then it
must already meet the requirements being introduced for playback (typically
through utilizing the recommended [telecom APIs](/develop/connectivity/telecom#integrate-a-calling-solution))) to successfully record
audio, and it is thus unlikely to be impacted.

If your app intends to continue audio playback while the screen is off or while
the user has fully dismissed your activity, which is most commonly seen in music
streaming apps or podcast apps, then your app is considered to provide
background audio functionality and must meet the new requirements.

## Background audio scenarios that are likely to see impact

If your app doesn't follow the model of continuing an audio interaction
initiated while your app was open, or in response to an explicit user trigger,
it is likely that your app's functionality will be suppressed silently.

For example, if your app starts a foreground service in response to
`BOOT_COMPLETE` and attempts to interact with audio, it will be suppressed.

## Best background audio practices to mitigate impact

* Use the [media3](/media/media3) jetpack library's [`MediaSessionService`](/reference/androidx/media3/session/MediaSessionService) component to
  manage background audio playback.

  If you do so, your app is not likely to be impacted by the background
  hardening due to the library assisting in managing the playback lifecycle.
* If you're not leveraging the media3 library, you will need to manually start
  a `mediaPlayback` FGS. Always start a foreground service while the app is in
  the foreground if background audio may occur.

  For example, if your app is a video streaming app which typically is
  foreground-only but contains a user affordance to continue playing while the
  screen is off, then when the user-initiated playback trigger occurs, your
  app should still start a foreground service.

  Doing this ensures that the foreground service is started with WIU
  capabilities.
* Keep the `mediaPlayback` FGS active during transient failures of under 10
  minutes.

  If your app has a transient failure, such as an issue with buffering due to
  network activity, or there is an expected transient interruption such as
  `AUDIOFOCUS_LOSS_TRANSIENT`, the intent to play should continue. Thus your
  FGS should remain active.
* Stop the foreground service at the end of playback and restart playback only
  if the user explicitly resumes the playback.

  In the case of a permanent signal to end playback (for example, content is
  complete with no auto-play, an `AUDIOFOCUS_LOSS`, a pause event from the
  UMO, or a media key event) or an unrecoverable failure, your app should
  cease the audio interaction, stop the foreground service, and end the media
  session. Doing all of this corresponds to the user's conception of
  "finishing" the desired background audio interaction. After doing this, your
  app no longer has background audio interaction capabilities.

  Subsequently, if the user explicitly resumes playback for example through
  your app's UI or through the Universal Media Object play button, the intent
  to start audio playback should return, resulting in a newly started FGS.
* Test audio playback behavior with adb shell commands.

## Testing changes on Android 16 and Android 17

The feature is already implemented at the "warning" level from
Android 16 onwards. This means apps can use `adb shell cmd audio
set-enable-hardening` to manually test background audio hardening enforcement.

To enable enforcement on devices running Android 16, run the following
command:

```
adb shell cmd audio set-enable-hardening 1
```

To disable enforcement on devices running Android 17, run the following
command:

```
adb shell cmd audio set-enable-hardening 0
```

We also recommend using `logcat` or the adb command `adb dumpsys audio` to
identify if the app
encountered silent failures due to audio hardening enforcement. If it did, the
log will have an entry prefixed by `AudioHardening` with your package name.

## Understanding FGS with while-in-use capability

Generally, foreground services (FGS) must be launched while an app is in the
foreground to extend user-initiated operations. [In some specific cases](/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions),
apps are allowed to launch a foreground service while the app is in the
background. However, these foreground services are usually not granted
While-In-Use (WIU) capabilities.

WIU acts as a security gate–it prevents FGS started from the background from
engaging in certain sensitive behaviors when the user might not be aware of the
app's activity. It prevents the app from accessing sensitive data like location,
camera, or microphone, and beginning in Android 17, it also blocks audio APIs
that typically require a visible UI context.

Here's a handy reference:

* Standard FGS: Services started while the app is visible or granted
  [background activity launch capability](/guide/components/activities/background-starts#exceptions) are granted WIU access.
* Background-Started FGS (BFSL): Most do not grant WIU access. The [primary
  exceptions](/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions) that grant WIU are interactions involving explicit user
  intent for example, notification clicks, widget interactions, or media key
  events from an external device.
* System started FGS: FGS started using system-server delegation (for example,
  by using Telecom jetpack library) are granted WIU access.

Read more in [Restrictions on starting a foreground service from the
background](/develop/background-work/services/fgs/restrictions-bg-start).

## Full list of Audio APIs impacted

|  |  |  |
| --- | --- | --- |
| Audio function | Result | Impacted APIs |
| Audio playback | Playback is silenced  No exceptions, no failure message provided by any API | [`AudioTrack.write()`](/reference/android/media/AudioTrack#write(float[],%20int,%20int,%20int))  (NDK) [`AAudioStream_write`](/ndk/reference/group/audio#group___audio_1ga052d406b198490072eb04b5f2074c9a3)  [OpenSL ES for Android](/ndk/guides/audio/opensl/opensl-for-android)  Any client side media libraries that manage playback such as media3, Exoplayer and Oboe could also be impacted. |
| Audio focus request | Returns `AUDIOFOCUS_REQUEST_FAILED`  No effect on audio playback of other apps, no focus acquired | [`AudioManager.requestAudioFocus()`](/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioFocusRequest)) |
| Volume and ringer mode APIs | No effect on ringer mode or volume (method call is silently ignored)  No exceptions, no failure message provided by any API | [`AudioManager.setStreamVolume()`](/reference/android/media/AudioManager#setStreamVolume(int,%20int,%20int))  [`AudioManager.setStreamMute()`](/reference/android/media/AudioManager#setStreamMute(int,%20boolean))  [`AudioManager.adjustStreamVolume()`](/reference/android/media/AudioManager#adjustStreamVolume(int,%20int,%20int))  [`AudioManager.adjustVolume()`](/reference/android/media/AudioManager#adjustVolume(int,%20int))  [`AudioManager.adjustSuggestedStreamVolume()`](/reference/android/media/AudioManager#adjustSuggestedStreamVolume(int,%20int,%20int))  [`AudioManager.setRingerMode()`](/reference/android/media/AudioManager#setRingerMode(int)) |