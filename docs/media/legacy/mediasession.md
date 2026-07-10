---
title: https://developer.android.com/media/legacy/mediasession
url: https://developer.android.com/media/legacy/mediasession
source: md.txt
---

# Using a media session

Media sessions provide a universal way of interacting with an audio or video player. By informing Android that media is playing in an app, playback controls can be delegated to the app. Integrating with the media session allows an app to advertise media playback externally and to receive playback commands from external sources. These sources can be physical buttons (such as the play button on a headset or TV remote control) or indirect commands (such as instructing "pause" to Google Assistant). The media session then delegates these commands to the app that applies them to the media player for which it is transparent where the commands originated.

A media session lives alongside the player that it manages. You should create and initialize a media session in the`onCreate()`method of the activity or service that owns the media session and its associated player.
| **Note:** The best practice for writing a media app is to use the[media-compat library](https://developer.android.com/guide/topics/media-apps/media-apps-overview#compat-library). On this page the term "media session" means an instance of[MediaSessionCompat](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat), and "media controller" means an instance of[MediaControllerCompat](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat).

## Initialize the media session

A newly-created media session has no capabilities. You must initialize the session by performing these steps:

- Set flags so that the media session can receive callbacks from media controllers and media buttons.
- Create and initialize an instance of`PlaybackStateCompat`and assign it to the session. The playback state changes throughout the session, so we recommend caching the`PlaybackStateCompat.Builder`for reuse.
- Create an instance of`MediaSessionCompat.Callback`and assign it to the session (more on callbacks below).

You should create and initialize a media session in the`onCreate()`method of the[activity](https://developer.android.com/guide/topics/media-apps/video-app/building-a-video-player-activity)or[service](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#init-session)that owns the session.

In order for[media buttons](https://developer.android.com/guide/topics/media-apps/mediabuttons)to work when your app is newly initialized (or stopped), its`PlaybackState`must contain a play action matching the intent that the media button sends. This is why`ACTION_PLAY`is assigned to the session state during initialization. For more information, see[Responding to Media Buttons](https://developer.android.com/guide/topics/media-apps/mediabuttons).
| **Note:** If you are integrating with the[ExoPlayer MediaSession extension](https://github.com/google/ExoPlayer/tree/release-v2/extensions/mediasession), you don't need to implement your own`MediaSessionCompat.Callback`. The`MediaSessionConnector`takes care of mapping the player state to the media session and delegating events received from the media session.

## Maintain the playback state and metadata

There are two classes that represent the state of a media session.

The[PlaybackStateCompat](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat)class describes the current operational state of the player. This includes:

- The transport state (whether the player is playing/paused/buffering, etc. See[getState()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getState()))
- An error code and optional error message, when applicable. (See[getErrorCode()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getErrorCode())and read[States and errors](https://developer.android.com/media/legacy/mediasession#errors), below.)
- The player position
- The valid controller actions that can be handled in the present state

The[MediaMetadataCompat](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat)class describes the material that is playing:

- The name of the artist, album, and track
- The track duration
- Album artwork for display on the lock screen. The image is a bitmap with a maximum size of 320x320dp (if larger, it's scaled down).
- An instance of[ContentUris](https://developer.android.com/reference/android/content/ContentUris)that points to a larger version of the artwork

The player state and metadata can change over the life of a media session. Every time the state or metadata changes, you must use the corresponding builder for each class,`PlaybackStateCompat.Builder()`or`MediaMetadataCompat.Builder()`, and then pass the new instance to the media session by calling[setPlaybackState()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setPlaybackState(android.support.v4.media.session.PlaybackStateCompat))or[setMetaData()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setMetadata(android.support.v4.media.MediaMetadataCompat)). To reduce overall memory consumption from these frequent operations, it's a good idea to create the builders once and to reuse them throughout the life of the session.

### States and errors

Note that`PlaybackState`is an object that contains separate values for the*playback state of the session* ([getState()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getState())) and, when necessary, an associated*error code* ([getErrorCode()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getErrorCode())). Errors can be fatal or non-fatal:

Whenever playback is interrupted, you should generate a fatal error: Set the transport state to`STATE_ERROR`and specify an associated error with[setErrorMessage(int, CharSequence)](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage(int, java.lang.CharSequence)). As long as playback is blocked by the error, the`PlaybackState`should continue to report`STATE_ERROR`and the error.

A non-fatal error occurs when your app cannot handle a request, but can continue to play: The transport remains in a "normal" state (such as`STATE_PLAYING`) but the`PlaybackState`holds an error code. For example, if the last song is playing and the user requests a skip to next song, playback can continue, but you should create a new`PlaybackState`with the error code`ERROR_CODE_END_OF_QUEUE`and then call`setPlaybackState()`. Media Controllers attached to the session will receive the callback[onPlaybackStateChanged()](https://developer.android.com/reference/android/support/v4/media/session/MediaControllerCompat.Callback#onPlaybackStateChanged(android.support.v4.media.session.PlaybackStateCompat))and explain to the user what happened. A non-fatal error should only be reported once, at the time it occurs. The next time the session updates the`PlaybackState`do not set the same non-fatal error again (unless the error occurred in response to a new request).

## Media session lock screens

Starting with Android 4.0 (API level 14) the system can access a media session's playback state and metadata. This is how the lock screen can display media controls and artwork. The behavior varies depending on the Android version.

### Album artwork

In Android 4.0 (API level 14) through Android 10 (API level 29), the background of the lock screen displays your album artwork - but only if the media session metadata includes a background bitmap.

### Transport controls

In Android 4.0 (API level 14) through Android 4.4 (API level 19), when a media session is active and the media session metadata includes a background bitmap the lock screen automatically displays transport controls.

In Android 5.0 (API level 21) or greater the system does not provide transport controls on the lock screen. Instead, you should use a[MediaStyle notification](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#mediastyle-notifications)to display transport controls.

### Add custom actions

Media applications can define custom actions; for example: thumbs up, like, or rewind 30 seconds. A custom action should implement completely new behavior. Do not use a custom action to replace one of the standard transport control actions defined in[PlaybackStateCompat](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#constants_1).

Add custom actions with[addCustomAction()](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#addCustomAction(android.support.v4.media.session.PlaybackStateCompat.CustomAction)). The following example shows how to add a control for a thumbs-up action:  

### Kotlin

```kotlin
stateBuilder.addCustomAction(
        PlaybackStateCompat.CustomAction.Builder(
                CUSTOM_ACTION_THUMBS_UP,
                resources.getString(R.string.thumbs_up),
                thumbsUpIcon
        ).run {
            setExtras(customActionExtras)
            build()
        }
)
```

### Java

```java
stateBuilder.addCustomAction(new PlaybackStateCompat.CustomAction.Builder(
    CUSTOM_ACTION_THUMBS_UP, resources.getString(R.string.thumbs_up), thumbsUpIcon)
    .setExtras(customActionExtras)
    .build());
```

See the[Universal Music Player](https://github.com/android/uamp/blob/f3154af7ac972ee9b7b1fd32ca3c935e02268a18/mobile/src/main/java/com/example/android/uamp/playback/PlaybackManager.java#L150-L171)for a complete example.

You respond to the action with[onCustomAction()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onCustomAction(java.lang.String, android.os.Bundle)).  

### Kotlin

```kotlin
override fun onCustomAction(action: String, extras: Bundle?) {
    when(action) {
        CUSTOM_ACTION_THUMBS_UP -> {
            ...
        }
    }
}
```

### Java

```java
@Override
public void onCustomAction(@NonNull String action, Bundle extras) {
    if (CUSTOM_ACTION_THUMBS_UP.equals(action)) {
        ...
    }
}
```

Also see the[Universal Music Player](https://github.com/android/uamp/blob/f3154af7ac972ee9b7b1fd32ca3c935e02268a18/mobile/src/main/java/com/example/android/uamp/playback/PlaybackManager.java#L328-L346).

## Media session callbacks

The main media session callback methods are`onPlay()`,`onPause()`, and`onStop()`. This is where you add the code that controls your player.

Since you instantiate and set the session's callback at runtime (in`onCreate()`), your app can define alternative callbacks that use different players and choose the appropriate callback/player combination depending on the device and/or system level. You can change the player without changing the rest of the app. For example, you could use[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)when running on Android 4.1 (API level 16) or greater and use[`MediaPlayer`](https://developer.android.com/guide/topics/media/mediaplayer)on earlier systems.

Besides controlling the player and managing the media session state transitions, callbacks also enable and disable features of your app and control the way it interacts with other apps and the device hardware. (See[Controlling Audio Output](https://developer.android.com/guide/topics/media-apps/volume-and-earphones)).

The implementation of the media session callback methods depends on the structure of your app. See the separate pages that describe how to use callbacks in[audio apps](https://developer.android.com/guide/topics/media-apps/audio-app/mediasession-callbacks)and[video apps](https://developer.android.com/guide/topics/media-apps/video-app/mediasession-callbacks), describe how the callbacks should be implemented for each kind of app.