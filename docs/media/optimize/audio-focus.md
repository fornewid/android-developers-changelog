---
title: https://developer.android.com/media/optimize/audio-focus
url: https://developer.android.com/media/optimize/audio-focus
source: md.txt
---

| **Note:** If you use ExoPlayer, consider letting ExoPlayer automatically manage audio focus by calling [`setAudioAttributes`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer#setAudioAttributes(androidx.media3.common.AudioAttributes,boolean)) with `true` for the `handleAudioFocus` parameter. With this behavior enabled, your app shouldn't include any code for requesting or responding to audio focus changes.

Two or more Android apps can play audio to the same output stream
simultaneously, and the system mixes everything together. While this is
technically impressive, it can be very aggravating to a user. To avoid every
music app playing at the same time, Android introduces the idea of *audio
focus*. Only one app can hold audio focus at a time.

When your app needs to output audio, it should request audio focus. When it has
focus, it can play sound. However, after you acquire audio focus you may not be
able to keep it until you're done playing. Another app can request focus, which
preempts your hold on audio focus. If that happens, your app should pause
playing or lower its volume to let users hear the new audio source more easily.

Before Android 12 (API level 31), audio focus is not managed by the system. So,
while app developers are encouraged to comply with the audio focus guidelines,
if an app continues to play loudly even after losing audio focus on a device
running Android 11 (API level 30) or lower, the system can't prevent it.
However, this app behavior leads to a bad user experience and can often lead
users to uninstall the misbehaving app.

A well-designed audio app should manage audio focus according to these general
guidelines:

- Call `requestAudioFocus()` immediately before starting to play and verify that
  the call returns
  [`AUDIOFOCUS_REQUEST_GRANTED`](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_REQUEST_GRANTED).
  Make the call to
  `requestAudioFocus()` in the `onPlay()` callback of your media session.

- When another app gains audio focus, stop or pause playing, or duck (that is,
  reduce) the volume.

- When playback stops (for example, when the app has nothing left to play),
  abandon audio focus. Your app doesn't have to abandon audio focus if the user
  pauses playback but might resume playback later.

- Use [`AudioAttributes`](https://developer.android.com/reference/android/media/AudioAttributes) to describe
  the type of audio your app is playing. For example, for apps that play speech,
  specify
  [`CONTENT_TYPE_SPEECH`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SPEECH).

Audio focus is handled differently depending on the version of Android that
is running:

[Android 12 (API level 31) or later](https://developer.android.com/media/optimize/audio-focus#audio-focus-12)
:   Audio focus is managed by the system. The system forces audio playback from an
    app to fade out when another app requests audio focus. The system
    also mutes audio playback when an incoming call is received.

[Android 8.0 (API level 26) through Android 11 (API level 30)](https://developer.android.com/media/optimize/audio-focus#audio-focus-8-0)
:   Audio focus is not managed by the system, but includes some changes that were
    introduced starting in Android 8.0 (API level 26).

[Android 7.1 (API level 25) and lower](https://developer.android.com/media/optimize/audio-focus#audio-focus-7-1)
:   Audio focus is not managed by the system, and apps manage audio focus using
    the [`requestAudioFocus()`](https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener,%20int,%20int))
    and
    [`abandonAudioFocus()`](https://developer.android.com/reference/android/media/AudioManager#abandonAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener)).

## Audio focus in Android 12 and higher

| **Note:** If an app targets Android 15 (API level 35) or higher, it cannot request audio focus unless it's the top app or running a foreground service. This requirement is similar to the [existing requirements for audio
| playback](https://developer.android.com/media/media3/session/background-playback#service-declaration). If an app requests audio focus when it does not meet these requirements, the method returns [`AUDIOFOCUS_REQUEST_FAILED`](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_REQUEST_FAILED).

A media or game app that uses audio focus shouldn't play audio after it loses
focus. In Android 12 (API level 31) and higher, the system enforces this
behavior. When an app requests audio focus while another app has the focus and
is playing, the system forces the playing app to fade out. The addition of the
fade-out provides a smoother transition when going from one app to another.

This fade out behavior happens when the following conditions are met:

1. The first, currently playing app meets all of these criteria:

   - The app has either the [`AudioAttributes.USAGE_MEDIA`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_MEDIA) or [`AudioAttributes.USAGE_GAME`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_GAME) usage attribute.
   - The app successfully requested audio focus with [`AudioManager.AUDIOFOCUS_GAIN`](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_GAIN).
   - The app is not playing audio with content type [`AudioAttributes.CONTENT_TYPE_SPEECH`](https://developer.android.com/reference/android/media/AudioAttributes#CONTENT_TYPE_SPEECH).
2. A second app requests audio focus with `AudioManager.AUDIOFOCUS_GAIN`.

When these conditions are met, the audio system fades out the first app. At the
end of the fade out, the system notifies the first app of focus loss. The app's
players remain muted until the app requests audio focus again.

### Existing audio focus behaviors

You should also be aware of these other cases that involve a switch in audio
focus.

#### Automatic ducking

Automatic ducking (temporarily reducing the audio level of one app so that
another can be heard clearly) was introduced in Android 8.0 (API level 26).

By having the system implement ducking, you don't have to implement ducking in
your app.

Automatic ducking also occurs when an audio notification grabs the focus
from a playing app. The start of the notification playback is synchronized
with the end of the ducking ramp.

Automatic ducking happens when the following conditions are met:

1. The first, currently-playing app meets all of these criteria:

   - The app successfully requested audio focus with any type of [focus
     gain](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_GAIN).
   - The app is not playing audio with content type `AudioAttributes.CONTENT_TYPE_SPEECH`.
   - The app did not set [`AudioFocusRequest.Builder.setWillPauseWhenDucked(true)`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setWillPauseWhenDucked(boolean)).
2. A second app requests audio focus with
   [`AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`](https://developer.android.com/reference/android/media/AudioManager#AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK).

When these conditions are met, the audio system ducks all the active players of
the first app while the second app has focus. When the second app abandons
focus, it unducks them. The first app is not notified when it loses focus,
so it doesn't have to do anything.

Note that automatic ducking is not performed when the user is listening to
speech content, because the user might miss some of the program. For example,
voice guidance for driving directions are not ducked.

#### Mute current audio playback for incoming phone calls

Some apps don't behave properly and continue playing audio during phone calls.
This situation forces the user to find and mute or quit the offending app in
order to hear their call. To prevent this, the system can mute audio from other
apps while there is an incoming call. The system invokes this feature when an
a incoming phone call is received and an app meets these conditions:

- The app has either the `AudioAttributes.USAGE_MEDIA` or `AudioAttributes.USAGE_GAME` usage attribute.
- The app successfully requested audio focus (any focus gain) and is playing audio.

If an app continues playing during the call, its playback is muted until the
call ends. However, if an app starts playing during the call, that player is not
muted on the assumption that the user started playback intentionally.

## Audio focus in Android 8.0 through Android 11

Beginning with Android 8.0 (API level 26), when you call
[`requestAudioFocus()`](https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioFocusRequest))
you must supply an `AudioFocusRequest` parameter. The `AudioFocusRequest`
contains information about the audio context and capabilities of your app. The
system uses this information to manage the gain and loss of audio focus
automatically. To release audio focus, call the method
[`abandonAudioFocusRequest()`](https://developer.android.com/reference/android/media/AudioManager#abandonAudioFocusRequest(android.media.AudioFocusRequest))
which also takes an `AudioFocusRequest` as its argument. Use the same
`AudioFocusRequest` instance both when you request and abandon focus.

To create an [`AudioFocusRequest`](https://developer.android.com/reference/android/media/AudioFocusRequest), use an
[`AudioFocusRequest.Builder`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder). Since a focus request must
always specify the type of the request, the type is included in the constructor
for the builder. Use the builder's methods to set the other fields of the
request.

The `FocusGain` field is required; all the other fields are optional.

<br />

| Method | Notes |
|---|---|
| [setFocusGain()](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setFocusGain(int)) | This field is required in every request. It takes the same values as the `durationHint` used in the pre-Android 8.0 call to `requestAudioFocus()`: `AUDIOFOCUS_GAIN`, `AUDIOFOCUS_GAIN_TRANSIENT`, `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`, or `AUDIOFOCUS_GAIN_TRANSIENT_EXCLUSIVE`. |
| [setAudioAttributes()](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setAudioAttributes(android.media.AudioAttributes)) | [AudioAttributes](https://developer.android.com/reference/android/media/AudioAttributes) describes the use case for your app. The system looks at them when an app gains and loses audio focus. Attributes supersede the notion of stream type. In Android 8.0 (API level 26) and later, stream types for any operation other than volume controls are deprecated. Use the same attributes in the focus request that you use in your audio player (as shown in the example following this table). <br /> Use an [AudioAttributes.Builder](https://developer.android.com/reference/android/media/AudioAttributes.Builder) to specify the attributes first, then use this method to assign the attributes to the request. <br /> If not specified, `AudioAttributes` defaults to `AudioAttributes.USAGE_MEDIA`. |
| [setWillPauseWhenDucked()](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setWillPauseWhenDucked(boolean)) | When another app requests focus with `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`, the app that has focus does not usually receive an [onAudioFocusChange()](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener#onAudioFocusChange(int)) callback because the system can [do the ducking by itself](https://developer.android.com/media/optimize/audio-focus#automatic-ducking). When you need to pause playback rather than duck the volume, call `setWillPauseWhenDucked(true)` and create and set an `OnAudioFocusChangeListener`, as described in [automatic ducking](https://developer.android.com/media/optimize/audio-focus#automatic-ducking). |
| [setAcceptsDelayedFocusGain()](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setAcceptsDelayedFocusGain(boolean)) | A request for audio focus can fail when the focus is locked by another app. This method enables [delayed focus gain](https://developer.android.com/media/optimize/audio-focus#delayed-focus-gain): the ability to asynchronously acquire focus when it becomes available. <br /> Note that delayed focus gain only works if you also specify an [AudioManager.OnAudioFocusChangeListener](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener) in the audio request, since your app needs to receive the callback in order to know that focus was granted. <br /> |
| [setOnAudioFocusChangeListener()](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setOnAudioFocusChangeListener(android.media.AudioManager.OnAudioFocusChangeListener, android.os.Handler)) | An `OnAudioFocusChangeListener` is only required if you also specify `willPauseWhenDucked(true)` or `setAcceptsDelayedFocusGain(true)` in the request. <br /> There are two methods for setting the listener: one with and one without a handler argument. The handler is the thread on which the listener runs. If you do not specify a handler, the handler associated with the main [Looper](https://developer.android.com/reference/android/os/Looper) is used. <br /> |

<br />

The following example shows how to use an `AudioFocusRequest.Builder` to build
an `AudioFocusRequest` and request and abandon audio focus:  

### Kotlin

```kotlin
// initializing variables for audio focus and playback management
audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
focusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN).run {
    setAudioAttributes(AudioAttributes.Builder().run {
        setUsage(AudioAttributes.USAGE_GAME)
        setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
        build()
    })
    setAcceptsDelayedFocusGain(true)
    setOnAudioFocusChangeListener(afChangeListener, handler)
    build()
}
val focusLock = Any()

var playbackDelayed = false
var playbackNowAuthorized = false

// requesting audio focus and processing the response
val res = audioManager.requestAudioFocus(focusRequest)
synchronized(focusLock) {
    playbackNowAuthorized = when (res) {
        AudioManager.AUDIOFOCUS_REQUEST_FAILED -> false
        AudioManager.AUDIOFOCUS_REQUEST_GRANTED -> {
            playbackNow()
            true
        }
        AudioManager.AUDIOFOCUS_REQUEST_DELAYED -> {
            playbackDelayed = true
            false
        }
        else -> false
    }
}

// implementing OnAudioFocusChangeListener to react to focus changes
override fun onAudioFocusChange(focusChange: Int) {
    when (focusChange) {
        AudioManager.AUDIOFOCUS_GAIN ->
            if (playbackDelayed || resumeOnFocusGain) {
                synchronized(focusLock) {
                    playbackDelayed = false
                    resumeOnFocusGain = false
                }
                playbackNow()
            }
        AudioManager.AUDIOFOCUS_LOSS -> {
            synchronized(focusLock) {
                resumeOnFocusGain = false
                playbackDelayed = false
            }
            pausePlayback()
        }
        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
            synchronized(focusLock) {
                // only resume if playback is being interrupted
                resumeOnFocusGain = isPlaying()
                playbackDelayed = false
            }
            pausePlayback()
        }
        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK -> {
            // ... pausing or ducking depends on your app
        }
    }
}
```

### Java

```java
// initializing variables for audio focus and playback management
audioManager = (AudioManager) Context.getSystemService(Context.AUDIO_SERVICE);
playbackAttributes = new AudioAttributes.Builder()
        .setUsage(AudioAttributes.USAGE_GAME)
        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
        .build();
focusRequest = new AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
        .setAudioAttributes(playbackAttributes)
        .setAcceptsDelayedFocusGain(true)
        .setOnAudioFocusChangeListener(afChangeListener, handler)
        .build();
final Object focusLock = new Object();

boolean playbackDelayed = false;
boolean playbackNowAuthorized = false;

// requesting audio focus and processing the response
int res = audioManager.requestAudioFocus(focusRequest);
synchronized(focusLock) {
    if (res == AudioManager.AUDIOFOCUS_REQUEST_FAILED) {
        playbackNowAuthorized = false;
    } else if (res == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
        playbackNowAuthorized = true;
        playbackNow();
    } else if (res == AudioManager.AUDIOFOCUS_REQUEST_DELAYED) {
        playbackDelayed = true;
        playbackNowAuthorized = false;
    }
}

// implementing OnAudioFocusChangeListener to react to focus changes
@Override
public void onAudioFocusChange(int focusChange) {
    switch (focusChange) {
        case AudioManager.AUDIOFOCUS_GAIN:
            if (playbackDelayed || resumeOnFocusGain) {
                synchronized(focusLock) {
                    playbackDelayed = false;
                    resumeOnFocusGain = false;
                }
                playbackNow();
            }
            break;
        case AudioManager.AUDIOFOCUS_LOSS:
            synchronized(focusLock) {
                resumeOnFocusGain = false;
                playbackDelayed = false;
            }
            pausePlayback();
            break;
        case AudioManager.AUDIOFOCUS_LOSS_TRANSIENT:
            synchronized(focusLock) {
                // only resume if playback is being interrupted
                resumeOnFocusGain = isPlaying();
                playbackDelayed = false;
            }
            pausePlayback();
            break;
        case AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK:
            // ... pausing or ducking depends on your app
            break;
        }
    }
}
```

### Automatic ducking

In Android 8.0 (API level 26), when another app requests focus with
`AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK` the system can duck and restore the volume
without invoking the app's `onAudioFocusChange()` callback.

While automatic ducking is acceptable behavior for music and video playback
apps, it isn't useful when playing spoken content, such as in an
audio book app. In this case, the app should pause instead.

If you want your app to pause when asked to duck rather than decrease its volume, create an `OnAudioFocusChangeListener` with
an `onAudioFocusChange()` callback method that implements the desired pause/resume behavior.
Call [`setOnAudioFocusChangeListener()`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setOnAudioFocusChangeListener(android.media.AudioManager.OnAudioFocusChangeListener,%20android.os.Handler)) to register the listener, and call
[`setWillPauseWhenDucked(true)`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setWillPauseWhenDucked(boolean))
to tell the system to use your callback rather than perform automatic ducking.

### Delayed focus gain

Sometimes the system cannot grant a request for audio focus because the focus is
"locked" by another app, such as during a phone call. In this case,
`requestAudioFocus()` returns `AUDIOFOCUS_REQUEST_FAILED`. When this happens,
your app should not proceed with audio playback because it did not gain
focus.

The method, [`setAcceptsDelayedFocusGain(true)`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setAcceptsDelayedFocusGain(boolean)), that lets your app handle a request for focus
asynchronously. With this flag set, a request made when the focus is locked
returns `AUDIOFOCUS_REQUEST_DELAYED`. When the condition that locked the audio
focus no longer exists, such as when a phone call ends, the system
grants the pending focus request and calls `onAudioFocusChange()` to notify your
app.

In order to handle the delayed gain of focus, you must create an
`OnAudioFocusChangeListener` with an `onAudioFocusChange()` callback method that
implements the desired behavior and register the listener by calling
[`setOnAudioFocusChangeListener()`](https://developer.android.com/reference/android/media/AudioFocusRequest.Builder#setOnAudioFocusChangeListener(android.media.AudioManager.OnAudioFocusChangeListener,%20android.os.Handler)).

## Audio focus in Android 7.1 and lower

When you call
[`requestAudioFocus()`](https://developer.android.com/reference/android/media/AudioManager#requestAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener,%20int,%20int))
you must specify a duration hint, which may
be honored by another app that is currently holding focus and playing:

- Request permanent audio focus (`AUDIOFOCUS_GAIN`) when you plan to play audio for the foreseeable future (for example, when playing music) and you expect the previous holder of audio focus to stop playing.
- Request transient focus (`AUDIOFOCUS_GAIN_TRANSIENT`) when you expect to play audio for only a short time and you expect the previous holder to pause playing.
- Request transient focus with *ducking* (`AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`) to indicate that you expect to play audio for only a short time and that it's OK for the previous focus owner to keep playing if it "ducks" (lowers) its audio output. Both audio outputs are mixed into the audio stream. Ducking is particularly suitable for apps that use the audio stream intermittently, such as for audible driving directions.

The `requestAudioFocus()` method also requires an [`AudioManager.OnAudioFocusChangeListener`](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener). This listener should be
created in the same activity or service that owns your media session. It
implements the callback `onAudioFocusChange()` that your app receives when
some other app acquires or abandons audio focus.

The following snippet requests permanent audio focus on the stream
`STREAM_MUSIC` and registers an `OnAudioFocusChangeListener` to handle
subsequent changes in audio focus. (The change listener is discussed in
[Responding to an audio focus change](https://developer.android.com/media/optimize/audio-focus#audio-focus-change).)  

### Kotlin

```kotlin
audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
lateinit var afChangeListener AudioManager.OnAudioFocusChangeListener

...
// Request audio focus for playback
val result: Int = audioManager.requestAudioFocus(
        afChangeListener,
        // Use the music stream.
        AudioManager.STREAM_MUSIC,
        // Request permanent focus.
        AudioManager.AUDIOFOCUS_GAIN
)

if (result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
    // Start playback
}
```

### Java

```java
AudioManager audioManager = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
AudioManager.OnAudioFocusChangeListener afChangeListener;

...
// Request audio focus for playback
int result = audioManager.requestAudioFocus(afChangeListener,
                             // Use the music stream.
                             AudioManager.STREAM_MUSIC,
                             // Request permanent focus.
                             AudioManager.AUDIOFOCUS_GAIN);

if (result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
    // Start playback
}
```

When you finish playback, call
[`abandonAudioFocus()`](https://developer.android.com/reference/android/media/AudioManager#abandonAudioFocus(android.media.AudioManager.OnAudioFocusChangeListener)).  

### Kotlin

```kotlin
audioManager.abandonAudioFocus(afChangeListener)
```

### Java

```java
// Abandon audio focus when playback complete
audioManager.abandonAudioFocus(afChangeListener);
```

This notifies the system that you no longer require focus and unregisters the
associated `OnAudioFocusChangeListener`. If you requested transient focus,
this will notify an app that paused or ducked that it may continue playing or
restore its volume.

## Responding to an audio focus change

When an app acquires audio focus, it must be able to release it when another app
requests audio focus for itself. When this happens, your app
receives a call to the
[`onAudioFocusChange()`](https://developer.android.com/reference/android/media/AudioManager.OnAudioFocusChangeListener#onAudioFocusChange(int))
method in the `AudioFocusChangeListener`
that you specified when the app called `requestAudioFocus()`.

The `focusChange` parameter passed to `onAudioFocusChange()` indicates the kind
of change that's happening. It corresponds
to the duration hint used by the app that's acquiring focus. Your app should
respond appropriately.

<br />

Transient loss of focus
:
    If the focus change is transient (`AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK` or
    `AUDIOFOCUS_LOSS_TRANSIENT`), your app should duck (if you are not relying
    on [automatic ducking](https://developer.android.com/media/optimize/audio-focus#automatic-ducking)) or pause playing but
    otherwise maintain the same state.

    <br />


    During a transient loss of audio focus, you should continue to monitor changes
    in audio focus and be prepared to resume normal playback when you regain the
    focus. When the blocking app abandons focus, you receive a callback
    (`AUDIOFOCUS_GAIN`). At this point, you can restore the volume to normal level
    or restart playback.


    <br />

Permanent loss of focus
:
    If the audio focus loss is permanent (`AUDIOFOCUS_LOSS`), another app is
    playing audio. Your app should pause playback immediately, as it won't ever
    receive an `AUDIOFOCUS_GAIN` callback. To restart playback, the user
    must take an explicit action, like pressing the play transport control
    in a notification or app UI.

    <br />


    <br />

<br />

The following code snippet demonstrates how to implement the
`OnAudioFocusChangeListener` and its `onAudioFocusChange()` callback. Notice the
use of a `Handler` to delay the stop callback on a permanent loss of audio
focus.  

### Kotlin

```kotlin
private val handler = Handler()
private val afChangeListener = AudioManager.OnAudioFocusChangeListener { focusChange ->
    when (focusChange) {
        AudioManager.AUDIOFOCUS_LOSS -> {
            // Permanent loss of audio focus
            // Pause playback immediately
            mediaController.transportControls.pause()
            // Wait 30 seconds before stopping playback
            handler.postDelayed(delayedStopRunnable, TimeUnit.SECONDS.toMillis(30))
        }
        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
            // Pause playback
        }
        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK -> {
            // Lower the volume, keep playing
        }
        AudioManager.AUDIOFOCUS_GAIN -> {
            // Your app has been granted audio focus again
            // Raise volume to normal, restart playback if necessary
        }
    }
}
```

### Java

```java
private Handler handler = new Handler();
AudioManager.OnAudioFocusChangeListener afChangeListener =
  new AudioManager.OnAudioFocusChangeListener() {
    public void onAudioFocusChange(int focusChange) {
      if (focusChange == AudioManager.AUDIOFOCUS_LOSS) {
        // Permanent loss of audio focus
        // Pause playback immediately
        mediaController.getTransportControls().pause();
        // Wait 30 seconds before stopping playback
        handler.postDelayed(delayedStopRunnable,
          TimeUnit.SECONDS.toMillis(30));
      }
      else if (focusChange == AudioManager.AUDIOFOCUS_LOSS_TRANSIENT) {
        // Pause playback
      } else if (focusChange == AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK) {
        // Lower the volume, keep playing
      } else if (focusChange == AudioManager.AUDIOFOCUS_GAIN) {
        // Your app has been granted audio focus again
        // Raise volume to normal, restart playback if necessary
      }
    }
  };
```

The handler uses a `Runnable` that looks like this:  

### Kotlin

```kotlin
private var delayedStopRunnable = Runnable {
    mediaController.transportControls.stop()
}
```

### Java

```java
private Runnable delayedStopRunnable = new Runnable() {
    @Override
    public void run() {
        getMediaController().getTransportControls().stop();
    }
};
```

To ensure the delayed stop does not kick in if the user restarts playback, call
`mHandler.removeCallbacks(mDelayedStopRunnable)` in response to any state
changes. For example, call `removeCallbacks()` in your Callback's `onPlay()`,
`onSkipToNext()`, etc. You should also call this method in your service's
`onDestroy()` callback when cleaning up the resources used by your service.