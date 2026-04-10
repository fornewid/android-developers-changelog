---
title: https://developer.android.com/media/platform/output
url: https://developer.android.com/media/platform/output
source: md.txt
---

# Handling changes in audio output

Users expect to be able to control the volume of an audio app. Standard behavior
includes the ability to use the volume controls (either buttons or knobs on the
device or sliders in the UI), and to avoid suddenly playing out loud if a
peripheral like headphones is disconnected while in use.

## Using the volume controls

When a user presses a volume key in a game or music app the volume should
change, even if the player is paused between songs or there's no music for the
current game location.

Android uses separate audio streams for playing music, alarms,
notifications, the incoming call ringer, system sounds, in-call volume, and DTMF
tones. This allows users to control the volume of each stream independently.

By default, pressing the volume control modifies the volume of the active audio
stream. If your app isn't currently playing anything, hitting the volume keys
adjusts the music volume (or the ringer volume before Android 9).

Unless your app is an alarm clock, you should play audio with usage
[AudioAttributes.USAGE_MEDIA](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA).

To ensure that volume controls adjust
the correct stream, you should call
[setVolumeControlStream()](https://developer.android.com/reference/android/app/Activity#setVolumeControlStream(int))
passing in the stream type matching your attributes that you can retrieve from
[AudioAttributes.getVolumeControlStream](https://developer.android.com/reference/android/media/AudioAttributes#getVolumeControlStream()).  

### Kotlin

```kotlin
setVolumeControlStream(AudioManager.STREAM_MUSIC)
```

### Java

```java
setVolumeControlStream(AudioManager.STREAM_MUSIC);
```

Make this call in your app's lifecycle, typically from the `onResume()`
method of the activity or fragment that controls your media. This connects
the volume controls to `STREAM_MUSIC` whenever the target activity or fragment
is visible.

### Controlling stream volume programmatically

In rare cases, you can set the volume of an audio stream programmatically. For
example, when your app replaces an existing UI. This is not recommended because
the Android `AudioManager` mixes all audio streams of the same type together.
These methods change the volume of every app that uses the stream. Avoid using
them:

- [adjustStreamVolume()](https://developer.android.com/reference/android/media/AudioManager#adjustStreamVolume(int, int, int))
- [adjustSuggestedStreamVolume()](https://developer.android.com/reference/android/media/AudioManager#adjustSuggestedStreamVolume(int, int, int))
- [adjustVolume()](https://developer.android.com/reference/android/media/AudioManager#adjustVolume(int, int))
- [setStreamVolume()
  setStreamVolume()](https://developer.android.com/reference/android/media/AudioManager#setStreamVolume(int, int, int))
- [setStreamSolo()](https://developer.android.com/reference/android/media/AudioManager#setStreamSolo(int, boolean))
- [setStreamMute()](https://developer.android.com/reference/android/media/AudioManager#setStreamMute(int, boolean))

## Working with fixed-volume devices

Some devices (like Chromebooks and Android Automotive OS cars) have volume
controls but don't allow apps to use the `AudioManager` methods described
earlier to change the level of an audio stream. These are called *fixed-volume*
devices. You can discover if your app is running on a fixed-volume device by
calling [`isVolumeFixed()`](https://developer.android.com/reference/android/media/AudioManager#isVolumeFixed()).

An audio app should provide the ability to balance
its output volume with other apps that might be playing on the same stream.
On *fixed-volume* devices, the app should connect its own volume controls to the
appropriate `setVolume()` method:

|   Player    |                                                             Method                                                              |
|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| AudioTrack  | [AudioTrack.setVolume()](https://developer.android.com/reference/android/media/AudioTrack#setVolume(float))                     |
| MediaPlayer | [MediaPlayer.setVolume()](https://developer.android.com/reference/android/media/MediaPlayer#setVolume(float, float))            |
| ExoPlayer   | Use `SimpleExoPlayer.setVolume()` which sets the volume of the underlying AudioTrack.                                           |
| Web         | Set the [`volume`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volume) property of the `HTMLMediaElement` |

## Don't be noisy

Users have a number of alternatives when it comes to enjoying the audio from
their Android devices. Most devices have a built-in speaker, headphone jacks for
wired headsets, and many also feature Bluetooth connectivity and support for
A2DP audio.

When a headset is unplugged or a Bluetooth device disconnected, the audio stream
automatically reroutes to the built-in speaker. If you listen to music at a high
volume, this can be a noisy surprise.

Users usually expect apps that include a music player with onscreen playback
controls to pause playback in this case. Other apps, like games that don't
include controls, should keep playing. The user can adjust the volume with the
device's hardware controls.

When audio output switches back to the built-in speaker the system broadcasts an [ACTION_AUDIO_BECOMING_NOISY](https://developer.android.com/reference/android/media/AudioManager#ACTION_AUDIO_BECOMING_NOISY)
intent. You should create a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)
that listens for this intent whenever you're playing audio. Your receiver should look like this:  

### Kotlin

```kotlin
private class BecomingNoisyReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == AudioManager.ACTION_AUDIO_BECOMING_NOISY) {
            // Pause the playback
        }
    }
}
```

### Java

```java
private class BecomingNoisyReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
      if (AudioManager.ACTION_AUDIO_BECOMING_NOISY.equals(intent.getAction())) {
          // Pause the playback
      }
    }
}
```

Register the receiver when you begin playback, and unregister it when you stop.
If you design your app as we describe in this guide, these calls should appear
in the `onPlay()` and `onStop()` media session callbacks.  

### Kotlin

```kotlin
private val intentFilter = IntentFilter(AudioManager.ACTION_AUDIO_BECOMING_NOISY)
private val myNoisyAudioStreamReceiver = BecomingNoisyReceiver()

private val callback = object : MediaSessionCompat.Callback() {

    override fun onPlay() {
        registerReceiver(myNoisyAudioStreamReceiver, intentFilter)
    }

    override fun onStop() {
        unregisterReceiver(myNoisyAudioStreamReceiver)
    }
}
```

### Java

```java
private IntentFilter intentFilter = new IntentFilter(AudioManager.ACTION_AUDIO_BECOMING_NOISY);
private BecomingNoisyReceiver myNoisyAudioStreamReceiver = new BecomingNoisyReceiver();

MediaSessionCompat.Callback callback = new
MediaSessionCompat.Callback() {
  @Override
  public void onPlay() {
    registerReceiver(myNoisyAudioStreamReceiver, intentFilter);
  }

  @Override
  public void onStop() {
    unregisterReceiver(myNoisyAudioStreamReceiver);
  }
}
```