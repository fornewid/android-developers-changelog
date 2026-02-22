---
title: https://developer.android.com/media/implement/playback-app
url: https://developer.android.com/media/implement/playback-app
source: md.txt
---

Jetpack Media3 defines a `Player` interface that outlines basic functionality
for playback of video and audio files. `ExoPlayer` is the default implementation
of this interface in Media3. We recommend using ExoPlayer, as it provides a
comprehensive set of features that cover most playback use-cases and is
customizable to handle any additional use-cases you might have. ExoPlayer also
abstracts away device and OS fragmentation so your code works consistently
across the entire Android ecosystem. ExoPlayer includes:

- Support for [playlists](https://developer.android.com/guide/topics/media/exoplayer/playlists)
- Support for a variety of progressive and adaptive streaming [formats](https://developer.android.com/guide/topics/media/exoplayer/supported-formats)
- Support for both client-side and server-side [ad insertion](https://developer.android.com/guide/topics/media/exoplayer/ad-insertion)
- Support for [DRM-protected playback](https://developer.android.com/guide/topics/media/exoplayer/drm)

This page walks you through some of the key steps in building a playback
app, and for more details you can head to our full guides on
[Media3 ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer).

## Getting started

To get started, add a dependency on the ExoPlayer, UI, and Common modules of
Jetpack Media3:  

```groovy
implementation "androidx.media3:media3-exoplayer:1.9.2"
implementation "androidx.media3:media3-ui:1.9.2"
implementation "androidx.media3:media3-common:1.9.2"
```

Depending on your use-case, you may also need additional modules from Media3,
such as `exoplayer-dash` to play streams in the DASH format.

Make sure to replace `1.9.2` with your preferred version of the
library. You can refer to the [release notes](https://github.com/androidx/media/tree/release/RELEASENOTES.md)
to see the latest version.

## Creating a media player

With Media3, you can either use the included implementation of the `Player`
interface, `ExoPlayer`, or you can build your own custom implementation.

### Creating an ExoPlayer

The simplest way to create an `ExoPlayer` instance is as follows:  

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context).build();
```

You can create your media player in the `onCreate()` lifecycle method of the
`Activity`, `Fragment`, or `Service` where it lives.

The [`Builder`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder) includes
a range of customization options you may be interested in, such as:

- [`setAudioAttributes()`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder#setAudioAttributes(androidx.media3.common.AudioAttributes,boolean)) to configure [audio focus](https://developer.android.com/media/optimize/audio-focus) handling
- [`setHandleAudioBecomingNoisy()`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder#setHandleAudioBecomingNoisy(boolean)) to configure playback behavior when an audio output device is disconnected
- [`setTrackSelector()`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder#setTrackSelector(androidx.media3.exoplayer.trackselection.TrackSelector)) to configure [track selection](https://developer.android.com/guide/topics/media/exoplayer/track-selection)

Media3 provides a `PlayerView` UI component that you can include in your app's
layout file. This component encapsulates a `PlayerControlView` for playback
controls, `SubtitleView` for displaying subtitles, and `Surface` for rendering
video.

### Preparing the player

Add [media items](https://developer.android.com/guide/topics/media/exoplayer/media-items) to a playlist for
playback with methods like
[`setMediaItem()`](https://developer.android.com/reference/androidx/media3/common/Player#setMediaItem(androidx.media3.common.MediaItem))
and [`addMediaItem()`](https://developer.android.com/reference/androidx/media3/common/Player#addMediaItem(androidx.media3.common.MediaItem)).
Then, call [`prepare()`](https://developer.android.com/reference/androidx/media3/common/Player#prepare()) to
start loading media and acquire the necessary resources.

You shouldn't perform these steps before the app is in the foreground. If your
player is in an `Activity` or `Fragment`, this means preparing the player in the
`onStart()` lifecycle method on API level 24 and higher or the `onResume()`
lifecycle method on API level 23 and below. For a player that's in a `Service`,
you can prepare it in `onCreate()`. Refer to the [Exoplayer codelab](https://developer.android.com/codelabs/exoplayer-intro#playeractivity.kt_4) for an
example of how to implement lifecycle methods.

### Control the player

After the player has been prepared, you can control playback by calling methods
on the player such as:

- [`play()`](https://developer.android.com/reference/androidx/media3/common/Player#play()) and [`pause()`](https://developer.android.com/reference/androidx/media3/common/Player#pause()) to start and pause playback
- [`seekTo()`](https://developer.android.com/reference/androidx/media3/common/Player#seekTo(long)) to seek to a position within the current media item
- [`seekToNextMediaItem()`](https://developer.android.com/reference/androidx/media3/common/Player#seekToNextMediaItem()) and [`seekToPreviousMediaItem()`](https://developer.android.com/reference/androidx/media3/common/Player#seekToPreviousMediaItem()) to navigate through the playlist

UI components such as the `PlayerView` or `PlayerControlView` will update
accordingly when bound to a player.

### Release the player

Playback can require resources that are in limited supply, such as video
decoders, so it's important to call [`release()`](https://developer.android.com/reference/androidx/media3/common/Player#release())
on your player to free up resources when the player is no longer needed.

If your player is in an `Activity` or `Fragment`, release the player in the
`onStop()` lifecycle method on API level 24 and higher or the `onPause()`
method on API level 23 and below. For a player that's in a `Service`, you can
release it in `onDestroy()`. Refer to the [Exoplayer codelab](https://developer.android.com/codelabs/exoplayer-intro#playeractivity.kt_6) for an
example of how to implement lifecycle methods.

## Managing playback with a media session

On Android, media sessions provide a standardized way to interact with a media
player across process boundaries. Connecting a media session to your player
allows you to advertise your media playback externally and to receive playback
commands from external sources, for example to integrate with
[system media controls](https://developer.android.com/media/implement/surfaces/mobile) on mobile and large
screen devices.

To use media sessions, add a dependency on the Media3 Session module:  

```groovy
implementation "androidx.media3:media3-session:1.9.2"
```

### Create a media session

You can create a `MediaSession` after initializing a player as follows:  

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context).build()
val mediaSession = MediaSession.Builder(context, player).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context).build();
MediaSession mediaSession = new MediaSession.Builder(context, player).build();
```

Media3 automatically syncs the state of the `Player` with the state of the
`MediaSession`. This works with any `Player` implementation, including
`ExoPlayer`, [`CastPlayer`](https://developer.android.com/reference/androidx/media3/cast/CastPlayer), or a
custom implementation.

### Grant control to other clients

Client apps can implement a [media controller](https://developer.android.com/reference/androidx/media3/session/MediaController)
to control playback of your media session. To receive these requests, set a
[callback](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback) object when
building your `MediaSession`.

When a controller is about to connect to your media session, the
[`onConnect()`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onConnect(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo))
method is called. You can use the provided [`ControllerInfo`](https://developer.android.com/reference/androidx/media3/session/MediaSession.ControllerInfo)
to decide whether to [accept](https://developer.android.com/reference/androidx/media3/session/MediaSession.ConnectionResult#accept(androidx.media3.session.SessionCommands,androidx.media3.common.Player.Commands))
or [reject](https://developer.android.com/reference/androidx/media3/session/MediaSession.ConnectionResult#reject())
the request. See an example of this in the [Media3 Session demo app](https://github.com/androidx/media/blob/release/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L104).

Once connected, a controller can send playback commands to the session. The
session then delegates those commands down to the player. Playback and playlist
commands defined in the `Player` interface are automatically handled by the
session.

Other callback methods allow you to handle, for example, requests for
[custom playback commands](https://developer.android.com/guide/topics/media/media3/getting-started/mediasession#adding-custom)
and [modifying the playlist](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onAddMediaItems(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,java.util.List%3Candroidx.media3.common.MediaItem%3E)). These callbacks similarly include a `ControllerInfo` object so you
can determine access control on a request-by-request basis.
| **Note:** If you want to allow controllers to add media items to the player, implement the [`onAddMediaItems()`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onAddMediaItems(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,java.util.List%3Candroidx.media3.common.MediaItem%3E)) callback. In addition to handling `setMediaItems()` and `addMediaItems()` requests from a Media3 `MediaController`, this method is backward compatible with legacy APIs such as `TransportControls.prepareFrom*` and `TransportControls.playFrom*`. A sample implementation of `onAddMediaItems()` can be found in the [`PlaybackService`](https://github.com/androidx/media/blob/main/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L205) of the session demo app.

## Playing media in the background

To continue playing media when your app is not in the foreground, for example
to play music, audiobooks, or podcasts even when the user doesn't have your app
open, your `Player` and `MediaSession` should be encapsulated in a
[foreground service](https://developer.android.com/develop/background-work/services/fgs). Media3 provides
the `MediaSessionService` interface for this purpose.

### Implementing a `MediaSessionService`

Create a class that extends `MediaSessionService` and instantiate your
`MediaSession` in the `onCreate()` lifecycle method.  

### Kotlin

```kotlin
class PlaybackService : MediaSessionService() {
    private var mediaSession: MediaSession? = null

    // Create your Player and MediaSession in the onCreate lifecycle event
    override fun onCreate() {
        super.onCreate()
        val player = ExoPlayer.Builder(this).build()
        mediaSession = MediaSession.Builder(this, player).build()
    }

    // Remember to release the player and media session in onDestroy
    override fun onDestroy() {
        mediaSession?.run {
            player.release()
            release()
            mediaSession = null
        }
        super.onDestroy()
    }
}
```

### Java

```java
public class PlaybackService extends MediaSessionService {
    private MediaSession mediaSession = null;

    @Override
    public void onCreate() {
        super.onCreate();
        ExoPlayer player = new ExoPlayer.Builder(this).build();
        mediaSession = new MediaSession.Builder(this, player).build();
    }

    @Override
    public void onDestroy() {
        mediaSession.getPlayer().release();
        mediaSession.release();
        mediaSession = null;
        super.onDestroy();
    }
}
```

In your manifest, add your `Service` class with a `MediaSessionService` intent
filter and request the `FOREGROUND_SERVICE` permission to run a foreground
service:  

    <service
        android:name=".PlaybackService"
        android:foregroundServiceType="mediaPlayback"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.media3.session.MediaSessionService"/>
        </intent-filter>
    </service>

    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />

Lastly, in the class you created, override the `onGetSession()` method to control
client access to your media session. Return a `MediaSession` to accept the
connection request, or return `null` to reject the request.  

### Kotlin

```kotlin
// This example always accepts the connection request
override fun onGetSession(
    controllerInfo: MediaSession.ControllerInfo
): MediaSession? = mediaSession
```

### Java

```java
@Override
public MediaSession onGetSession(MediaSession.ControllerInfo controllerInfo) {
  // This example always accepts the connection request
  return mediaSession;
}
```

### Connecting to your UI

Now that your media session is in a `Service` separate from the `Activity` or
`Fragment` where your player UI lives, you can use a `MediaController` to link
them together. In the `onStart()` method of the `Activity` or `Fragment` with your
UI, create a `SessionToken` for your `MediaSession`, then use the `SessionToken`
to build a `MediaController`. Building a `MediaController` happens
asynchronously.  

### Kotlin

```kotlin
override fun onStart() {
  val sessionToken = SessionToken(this, ComponentName(this, PlaybackService::class.java))
  val controllerFuture = MediaController.Builder(this, sessionToken).buildAsync()
  controllerFuture.addListener(
    {
        // Call controllerFuture.get() to retrieve the MediaController.
        // MediaController implements the Player interface, so it can be
        // attached to the PlayerView UI component.
        playerView.setPlayer(controllerFuture.get())
      },
    MoreExecutors.directExecutor()
  )
}
```

### Java

```java
@Override
public void onStart() {
  SessionToken sessionToken =
    new SessionToken(this, new ComponentName(this, PlaybackService.class));
  ListenableFuture<MediaController> controllerFuture =
    new MediaController.Builder(this, sessionToken).buildAsync();
  controllerFuture.addListener(() -> {
    // Call controllerFuture.get() to retrieve the MediaController.
    // MediaController implements the Player interface, so it can be
    // attached to the PlayerView UI component.
    playerView.setPlayer(controllerFuture.get());
  }, MoreExecutors.directExecutor())
}
```

`MediaController` implements the `Player` interface, so you can use the same
methods such as `play()` and `pause()` to control playback. Similar to other
components, remember to release the `MediaController` when it is no longer
needed, such as the `onStop()` lifecycle method of an `Activity`, by calling
[`MediaController.releaseFuture()`](https://developer.android.com/reference/androidx/media3/session/MediaController#releaseFuture(java.util.concurrent.Future%3C?%20extends%20androidx.media3.session.MediaController%3E)).

### Publishing a notification

Foreground services are required to publish a notification while active. A
`MediaSessionService` will automatically create a
[`MediaStyle` notification](https://developer.android.com/reference/android/app/Notification.MediaStyle) for
you in the form of a [`MediaNotification`](https://developer.android.com/reference/androidx/media3/session/MediaNotification).
To provide a custom notification, create a
[`MediaNotification.Provider`](https://developer.android.com/reference/androidx/media3/session/MediaNotification.Provider)
with [`DefaultMediaNotificationProvider.Builder`](https://developer.android.com/reference/androidx/media3/session/DefaultMediaNotificationProvider)
or by creating a custom implementation of the provider interface. Add your
provider to your `MediaSession` with
[`setMediaNotificationProvider`](https://developer.android.com/reference/androidx/media3/session/MediaSessionService#setMediaNotificationProvider(androidx.media3.session.MediaNotification.Provider)).

## Advertising your content library

A `MediaLibraryService` builds on a `MediaSessionService` by allowing client
apps to browse the media content provided by your app. Client apps implement a
[`MediaBrowser`](https://developer.android.com/reference/androidx/media3/session/MediaBrowser) to interact
with your `MediaLibraryService`.

Implementing a `MediaLibraryService` is similar to implementing a
`MediaSessionService`, except that in `onGetSession()` you should return a
`MediaLibrarySession` instead of a `MediaSession`. Compared to a
`MediaSession.Callback`, the `MediaLibrarySession.Callback` includes additional
methods that allow a browser client to navigate the content offered by your
library service.

Similar to the `MediaSessionService`, declare the `MediaLibraryService` in your
manifest and request the `FOREGROUND_SERVICE` permission to run a foreground
service:  

    <service
        android:name=".PlaybackService"
        android:foregroundServiceType="mediaPlayback"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.media3.session.MediaLibraryService"/>
            <action android:name="android.media.browse.MediaBrowserService"/>
        </intent-filter>
    </service>

    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />

The example above includes an intent filter for both the `MediaLibraryService`
and, for backward compatibility, the legacy `MediaBrowserService`. The
additional intent filter enables client apps using the `MediaBrowserCompat` API
to recognize your `Service`.

A `MediaLibrarySession` lets you serve your content library in a tree
structure, with a single root `MediaItem`. Each `MediaItem` in the tree can have
any number of children `MediaItem` nodes. You can serve a different root, or a
different tree, based on the client app's request. For example, the tree you
return to a client looking for a list of recommended media items might only
contain the root `MediaItem` and a single level of children `MediaItem` nodes,
whereas the tree you return to a different client app may represent a more
complete library of content.

### Creating a `MediaLibrarySession`

A [`MediaLibrarySession`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.MediaLibrarySession)
extends the `MediaSession` API to add content browsing APIs. Compared to the
[`MediaSession` callback](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback),
the [`MediaLibrarySession` callback](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.MediaLibrarySession.Callback)
adds methods such as:

- [`onGetLibraryRoot()`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.MediaLibrarySession.Callback#onGetLibraryRoot(androidx.media3.session.MediaLibraryService.MediaLibrarySession,androidx.media3.session.MediaSession.ControllerInfo,androidx.media3.session.MediaLibraryService.LibraryParams)) for when a client requests the root `MediaItem` of a content tree
- [`onGetChildren()`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.MediaLibrarySession.Callback#onGetChildren(androidx.media3.session.MediaLibraryService.MediaLibrarySession,androidx.media3.session.MediaSession.ControllerInfo,java.lang.String,int,int,androidx.media3.session.MediaLibraryService.LibraryParams)) for when a client requests the children of a `MediaItem` in the content tree
- [`onGetSearchResult()`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.MediaLibrarySession.Callback#onGetSearchResult(androidx.media3.session.MediaLibraryService.MediaLibrarySession,androidx.media3.session.MediaSession.ControllerInfo,java.lang.String,int,int,androidx.media3.session.MediaLibraryService.LibraryParams)) for when a client requests search results from the content tree for a given query

Relevant callback methods will include a [`LibraryParams`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.LibraryParams)
object with additional signals about the type of content tree that a client app
is interested in.