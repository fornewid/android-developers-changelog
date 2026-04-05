---
title: https://developer.android.com/training/tv/tif/time-shifting
url: https://developer.android.com/training/tv/tif/time-shifting
source: md.txt
---

# Support time-shifting

Use time-shifting APIs in your TV input service to let users pause, rewind, and fast-forward live programs in your service channels. If your app supports time-shifting, users gain flexibility in how they watch your content:

- Users can pause programs while handling a short-term interruption, so they never miss key moments.
- Users can fast-forward through content they've already seen or content that doesn't interest them.
- Users can rewind and rewatch favorite moments in program content.

![](https://developer.android.com/static/images/training/tv/tif/time-shift.png)

**Figure 1.**Android TV playback controls used for time-shifting.

Time-shifting uses short, temporary, recorded segments of program data to implement the ability to playback live programs. Users can't play these time-shifting recordings outside of the current playback session. This means they can't use time-shifting to pause a program to watch the next day or pause a program to watch later while they switch to a different channel.

Use the[TV recording APIs](https://developer.android.com/training/tv/tif/content-recording)if you want to let your users record program content to watch outside of the current playback session.

## Add time-shifting support

To add time-shifting support to your TV input service, you need to implement the time-shifting APIs in your[TvInputService.Session](https://developer.android.com/reference/android/media/tv/TvInputService.Session)class, handle recording and playback of time-shifting recordings in your app, and notify the system that your input service provides time-shifting support.

TheTvInputService.Sessionmethods that you implement are the following:

- [onTimeShiftGetCurrentPosition()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftGetCurrentPosition()): called by the system to get the current playback position in milliseconds. For more details, see the[Track playback times](https://developer.android.com/training/tv/tif/time-shifting#track-playback-times)section.
- [onTimeShiftGetStartPosition()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftGetStartPosition()): called by the system to get the start position of the current time-shift recording in milliseconds. For more details, see the[Track playback times](https://developer.android.com/training/tv/tif/time-shifting#track-playback-times)section.
- [onTimeShiftPause()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftPause()): called when the user pauses playback.
- [onTimeShiftResume()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftResume()): called when the user resumes playback.
- [onTimeShiftSeekTo(long)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftSeekTo(long)): called when the system needs to seek a new time position. Normally, the new position is between the start position and the current position.
- [onTimeShiftSetPlaybackParams(PlaybackParams)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftSetPlaybackParams(android.media.PlaybackParams)): called by the system to provide playback parameters, such as playback speed, for the current session. For more details, see the[Support playback parameters](https://developer.android.com/training/tv/tif/time-shifting#support-playback-parameters)section.

For more information about how to inform the system that your input service supports time-shifting, see the[Notify the system about time-shifting status](https://developer.android.com/training/tv/tif/time-shifting#notify-about-timeshift-status)section.

If you're using the TIF Companion Library to implement yourTvInputService.Sessionclass, you automatically get an implementation of time-shifting that uses ExoPlayer. You can use this implementation or override the time-shifting API methods in`BaseTvInputService.Session`and provide your own implementation. For more information on using the TIF Companion Library, see[Create a TV input service using the TIF Companion Library](https://developer.android.com/training/tv/tif/tvinput#TIFCompanion).

## Record content when a session starts

A user can pause, rewind, and fast-forward program content by accessing the playback controls for the channel, either by pressing**Select**while watching content and then navigating to the playback controls or by using dedicated playback controls on a remote device.

Because the user can use time-shifting at any time while watching program content, your TV input service must begin recording time-shifting content as soon as the user tunes to a channel in your[onTune()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTune(android.net.Uri))implementation. You also need to inform the system that you are capable of recording by calling[notifyTimeShiftStatusChanged(int)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#notifyTimeShiftStatusChanged(int)), as described in the[Notify the system about time-shifting status](https://developer.android.com/training/tv/tif/time-shifting#notify-about-timeshift-status)section.

## Manage recorded content storage

Your TV input service is responsible for storing time-shifting recordings in your app's private app storage and playing back content when the system calls your time-shifting methods, such as[onTimeShiftResume()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftResume()). If your content is already stored in the cloud and your app can manage time-shifting recordings in the cloud, you can use cloud storage instead of app storage.

If your content uses protected content, your TV input service is responsible for proper encryption of recorded content and decryption of content during playback.

Since recorded video content can require a large amount of storage, you need to carefully manage recorded content during session playback. If the playback session time exceeds the amount of time you can record and store for time-shifting, adjust your time-shifting recording to maintain the current buffer but ensure the current time is captured. For example, if the user has been playing content for 31 minutes and your maximum time-shifting recording size is 30 minutes, adjust your recording and start time to contain content from minute 1 to minute 31.

If your TV input service can't support time-shifting due to lack of storage, you must inform the system. For more details on how to notify the system about time-shifting support restrictions, see the[Notify the system about time-shifting status](https://developer.android.com/training/tv/tif/time-shifting#notify-about-timeshift-status)section.

When the user switches to a different channel or otherwise ends their playback session, delete your recorded time-shifting data.

## Notify the system about time-shifting status

If your TV input service supports time-shifting, call[notifyTimeShiftStatusChanged(TvInputManager.TIME_SHIFT_STATUS_AVAILABLE)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#notifyTimeShiftStatusChanged(int))in your implementation of[onTune()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTune(android.net.Uri))when a user tunes to a channel.

To inform the system if any time-shifting capabilities of your input service change, use[notifyTimeShiftStatusChanged(int)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#notifyTimeShiftStatusChanged(int)). For example, if your TV input service cannot support time-shifting due to storage space restrictions or other reasons, call[notifyTimeShiftStatusChanged(TvInputManager.TIME_SHIFT_STATUS_UNAVAILABLE)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#notifyTimeShiftStatusChanged(int)).

If your TV input service can't support time-shifting at all, call[notifyTimeShiftStatusChanged(TvInputManager.TIME_SHIFT_STATUS_UNSUPPORTED)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#notifyTimeShiftStatusChanged(int))when a playback session is created. The system treats any input service that never calls`notifyTimeShiftStatusChanged()`as an input service that can't support time-shifting. This covers input services using API Level 22 and earlier.

## Track playback times

The start position of a time-shifting recording is the earliest absolute time position, in milliseconds since the epoch, that the user can seek to. This is usually the time when the video playback starts after[onTune()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTune(android.net.Uri))is called. However, when the user watches an amount of content that exceeds what your app can record, you need to start recording a new segment for time-shifting and update your start time accordingly.

The current position of a time-shifting recording is the current playback position, in milliseconds since the epoch. This position changes continuously during playback. Typically, you can use your playback engine to determine this value, as shown in the following example:  

### Kotlin

```kotlin
override fun onTimeShiftGetCurrentPosition(): Long =
        tvPlayer?.run {
            currentProgram?.let { program ->
                currentPosition + program.startTimeUtcMillis
            }
        } ?: TvInputManager.TIME_SHIFT_INVALID_TIME
```

### Java

```java
@Override
public long onTimeShiftGetCurrentPosition() {
  if (getTvPlayer() != null && currentProgram != null) {
    return getTvPlayer().getCurrentPosition() +
      currentProgram.getStartTimeUtcMillis();
  }
  return TvInputManager.TIME_SHIFT_INVALID_TIME;
}
```

Ensure that the start time you provide when the system calls your[onTimeShiftGetStartPosition()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftGetStartPosition())is never greater than the current time position you provide in[onTimeShiftGetCurrentPosition()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftGetCurrentPosition()). The system uses these calls to update the time-shifting duration in the playback controls UI.

## Support playback parameters

To change playback speed during time-shifting, the system uses playback parameters. For example, if the user decides to rewind the current playback, new playback parameters are passed to your app with a negative playback speed. Time-shifting also supports several different levels, 2x or 3x, of playback speed for rewinding or fast-forwarding.

The system calls your[onTimeShiftSetPlaybackParams(PlaybackParams)](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTimeShiftSetPlaybackParams(android.media.PlaybackParams))method with a[PlaybackParams](https://developer.android.com/reference/android/media/PlaybackParams)object that contains parameters for the current session. Use this information to configure your media playback engine appropriately.

If your playback engine does not support a parameter, emulate the expected behavior as best you can. For example, if your playback engine doesn't support 2x speed, use repeated seek operations on your playback engine to achieve an approximately double playback speed.

After the parameters are set, don't change the settings unless the user either issues a playback command that requires a different parameter or switches to a new channel.