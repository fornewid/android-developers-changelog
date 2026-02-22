---
title: https://developer.android.com/media/media3/session/background-playback
url: https://developer.android.com/media/media3/session/background-playback
source: md.txt
---

It is often desirable to play media while an app is not in the foreground. For
example, a music player generally keeps playing music when the user has locked
their device or is using another app. The Media3 library provides a series of
interfaces that allow you to support background playback.
| **Note:** The following instructions for `MediaSessionService` equally apply to `MediaLibraryService`, which should be used instead of `MediaSessionService` when [serving a content library](https://developer.android.com/media/media3/session/serve-content).

## Use a MediaSessionService

To enable background playback, you should contain the `Player` and
`MediaSession` inside a separate [Service](https://developer.android.com/guide/components/services).
This allows the device to continue serving media even while your app is not in
the foreground.
![The MediaSessionService allows the media session to run separately
from the app's activity](https://developer.android.com/static/guide/topics/media/images/mediasessionservice.png) **Figure 1** : The `MediaSessionService` allows the media session to run separately from the app's activity

When hosting a player inside a Service, you should use a `MediaSessionService`.
To do this, create a class that extends `MediaSessionService` and create your
media session inside of it.

Using `MediaSessionService` makes it possible for external clients like Google
Assistant, system media controls, media buttons on peripheral devices, or
companion devices like Wear OS to discover your service, connect to it, and
control playback, all without accessing your app's UI activity at all. In fact,
there can be multiple client apps connected to the same `MediaSessionService` at
the same time, each app with its own `MediaController`.

### Implement the service lifecycle

You need to implement two lifecycle methods of your service:

- `onCreate()` is called when the first controller is about to connect and the service is instantiated and started. It's the best place to build `Player` and `MediaSession`.
- `onDestroy()` is called when the service is being stopped. All resources including player and session need to be released.

You can optionally override `onTaskRemoved(Intent)` to customize what happens
when the user dismisses the app from the recent tasks. By default, the service
is left running if playback is ongoing and is stopped otherwise.
**Note:** You can [implement playback resumption](https://developer.android.com/media/media3/session/background-playback#resumption) to allow a user to restart the service lifecycle and resume playback from where it was left off.  

### Kotlin

```kotlin
class PlaybackService : MediaSessionService() {
  private var mediaSession: MediaSession? = null

  // Create your player and media session in the onCreate lifecycle event
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

  // Create your Player and MediaSession in the onCreate lifecycle event
  @Override
  public void onCreate() {
    super.onCreate();
    ExoPlayer player = new ExoPlayer.Builder(this).build();
    mediaSession = new MediaSession.Builder(this, player).build();
  }

  // Remember to release the player and media session in onDestroy
  @Override
  public void onDestroy() {
    mediaSession.getPlayer().release();
    mediaSession.release();
    mediaSession = null;
    super.onDestroy();
  }
}
```

<br />

As an alternative of keeping playback ongoing in the background, you can
stop the service in any case when the user dismisses the app:  

### Kotlin

```kotlin
override fun onTaskRemoved(rootIntent: Intent?) {
  pauseAllPlayersAndStopSelf()
}
```

### Java

```java
@Override
public void onTaskRemoved(@Nullable Intent rootIntent) {
  pauseAllPlayersAndStopSelf();
}
```

<br />

For any other manual implementation of `onTaskRemoved`, you can use
`isPlaybackOngoing()` to check if the playback is considered ongoing and the
foreground service is started.

### Provide access to the media session

Override the `onGetSession()` method to give other clients access to your media
session that was built when the service was created.  

### Kotlin

```kotlin
class PlaybackService : MediaSessionService() {
  private var mediaSession: MediaSession? = null
  // [...] lifecycle methods omitted

  override fun onGetSession(controllerInfo: MediaSession.ControllerInfo): MediaSession? =
    mediaSession
}
```

### Java

```java
public class PlaybackService extends MediaSessionService {
  private MediaSession mediaSession = null;
  // [...] lifecycle methods omitted

  @Override
  public MediaSession onGetSession(MediaSession.ControllerInfo controllerInfo) {
    return mediaSession;
  }
}
```

<br />

### Declare the service in the manifest

An app requires the `FOREGROUND_SERVICE` and `FOREGROUND_SERVICE_MEDIA_PLAYBACK`
permissions to run a playback foreground service:  

    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

You must also declare your `Service` class in the manifest with an intent filter
of `MediaSessionService` and a [`foregroundServiceType`](https://developer.android.com/guide/topics/manifest/service-element#foregroundservicetype) that includes
`mediaPlayback`.  

    <service
        android:name=".PlaybackService"
        android:foregroundServiceType="mediaPlayback"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.media3.session.MediaSessionService"/>
            <action android:name="android.media.browse.MediaBrowserService"/>
        </intent-filter>
    </service>

| **Note:** If you would like your `MediaLibraryService` to be compatible with client apps using the platform `MediaBrowserService`, you need to include `<action android:name="android.media.browse.MediaBrowserService"/>` in the `intent-filter` element.

## Control playback using a `MediaController`

In the Activity or Fragment containing your player UI, you can establish a link
between the UI and your media session using a `MediaController`. Your UI uses
the media controller to send commands from your UI to the player within the
session. See the
[Create a `MediaController`](https://developer.android.com/guide/topics/media/session/mediacontroller#create-controller)
guide for details on creating and using a `MediaController`.

### Handle `MediaController` commands

The `MediaSession` receives commands from the controller through its
`MediaSession.Callback`. Initializing a `MediaSession` creates a default
implementation of `MediaSession.Callback` that automatically handles all
commands a `MediaController` sends to your player.
| **Note:** A `MediaSession.ControllerInfo` is passed as an argument to the functions within the `MediaSession.Callback` interface. This allows you to see the caller package with `controllerInfo.packageName` and tailor how your app reacts accordingly. For example, you may wish to handle a command differently if it came from Android Auto or a Bluetooth headset (`com.android.bluetooth`). Also refer to the [control playback](https://developer.android.com/media/media3/session/control-playback#controller-for-current-request) page for more details on how to identify the caller for `Player` methods.

## Notification

A `MediaSessionService` automatically creates a `MediaNotification` for you that
should work in most cases. By default, the published notification is a
[`MediaStyle` notification](https://developer.android.com/reference/androidx/media3/session/MediaStyleNotificationHelper.MediaStyle) that stays updated with the latest
information from your media session and displays playback controls. The
`MediaNotification` is aware of your session and can be used to control playback
for any other apps that are connected to the same session.

For example, a music streaming app using a `MediaSessionService` would create a
`MediaNotification` that displays the title, artist, and album art for the
current media item being played alongside playback controls based on your
`MediaSession` configuration.

The required metadata can be provided in the media or declared as part of the
media item as in the following snippet:  

### Kotlin

```kotlin
val mediaItem =
    MediaItem.Builder()
      .setMediaId("media-1")
      .setUri(mediaUri)
      .setMediaMetadata(
        MediaMetadata.Builder()
          .setArtist("David Bowie")
          .setTitle("Heroes")
          .setArtworkUri(artworkUri)
          .build()
      )
      .build()

mediaController.setMediaItem(mediaItem)
mediaController.prepare()
mediaController.play()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setMediaId("media-1")
        .setUri(mediaUri)
        .setMediaMetadata(
            new MediaMetadata.Builder()
                .setArtist("David Bowie")
                .setTitle("Heroes")
                .setArtworkUri(artworkUri)
                .build())
        .build();

mediaController.setMediaItem(mediaItem);
mediaController.prepare();
mediaController.play();
```

<br />

### Notification lifecycle

The notification is created as soon as the `Player` has `MediaItem` instances
in its playlist.

All notification updates happen automatically based on the `Player` and
`MediaSession` state.

The notification cannot be removed while the foreground service is running. To
immediately remove the notification, you must call `Player.release()` or clear
the playlist using `Player.clearMediaItems()`.

If the player is paused, stopped or failed for more than 10 minutes without
further user interactions, the service is automatically transitioned out of the
foreground service state so it can be destroyed by the system. You can
[implement playback resumption](https://developer.android.com/media/media3/session/background-playback#resumption) to allow a user to restart the
service lifecycle and resume playback at a later point in time.

### Notification customization

The metadata about the currently playing item can be customized by modifying
the `MediaItem.MediaMetadata`. If you want to update the metadata of an existing
item, you can use `Player.replaceMediaItem` to update the metadata without
interrupting playback.

You can also customize some of the buttons shown in the notification by setting
custom media button preferences for the Android Media controls.
[Read more about customizing Android Media controls](https://developer.android.com/media/implement/surfaces/mobile#config-action-buttons).

To further customize the notification itself, create a
[`MediaNotification.Provider`](https://developer.android.com/reference/androidx/media3/session/MediaNotification.Provider)
with [`DefaultMediaNotificationProvider.Builder`](https://developer.android.com/reference/androidx/media3/session/DefaultMediaNotificationProvider)
or by creating a custom implementation of the provider interface. Add your
provider to your `MediaSessionService` with
[`setMediaNotificationProvider`](https://developer.android.com/reference/androidx/media3/session/MediaSessionService#setMediaNotificationProvider(androidx.media3.session.MediaNotification.Provider)).
| **Warning:** Starting with API 33, the System UI media notification is populated from the data in the media session. We advise against modifications using `MediaNotification.Provider` as these only take effect before API 33. Instead, change the state of the `MediaItem.MediaMetadata` and the session's media button preferences.

## Playback resumption

After the `MediaSessionService` has been terminated, and even after the device
has been rebooted, it is possible to offer playback resumption to let users
restart the service and resume playback where they left off. By default,
playback resumption is turned off. This means the user can't resume playback
when your service isn't running. To opt-in to this feature, you need to declare
a media button receiver and implement the `onPlaybackResumption` method.

### Declare the Media3 media button receiver

Start by declaring the `MediaButtonReceiver` in your manifest:  

    <receiver android:name="androidx.media3.session.MediaButtonReceiver"
      android:exported="true">
      <intent-filter>
        <action android:name="android.intent.action.MEDIA_BUTTON" />
      </intent-filter>
    </receiver>

| **Important:** If you add the `MediaButtonReceiver`, you **must** implement `MediaSession.Callback.onPlaybackResumption()` as a second step.

### Implement playback resumption callback

When playback resumption is requested by either a Bluetooth device or the
Android System UI [resumption feature](https://developer.android.com/media/implement/surfaces/mobile#supporting-media),
the [`onPlaybackResumption()`](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaSession.Callback#onPlaybackResumption(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,boolean)) callback method is
called.
**Note:** The Android System UI resumption notification is only available if you implement a `MediaLibraryService` to [serve a content library](https://developer.android.com/media/media3/session/serve-content).  

### Kotlin

```kotlin
override fun onPlaybackResumption(
    mediaSession: MediaSession,
    controller: ControllerInfo,
    isForPlayback: Boolean,
): ListenableFuture<MediaItemsWithStartPosition> {
  val settable = SettableFuture.create<MediaItemsWithStartPosition>()
  scope.launch {
    // Your app is responsible for storing the playlist, metadata (like title
    // and artwork) of the current item and the start position to use here.
    val resumptionPlaylist = restorePlaylist()
    settable.set(resumptionPlaylist)
  }
  return settable
}
```

### Java

```java
@Override
public ListenableFuture<MediaItemsWithStartPosition> onPlaybackResumption(
    MediaSession mediaSession,
    ControllerInfo controller,
    boolean isForPlayback
) {
  SettableFuture<MediaItemsWithStartPosition> settableFuture = SettableFuture.create();
  settableFuture.addListener(() -> {
    // Your app is responsible for storing the playlist, metadata (like title
    // and artwork) of the current item and the start position to use here.
    MediaItemsWithStartPosition resumptionPlaylist = restorePlaylist();
    settableFuture.set(resumptionPlaylist);
  }, MoreExecutors.directExecutor());
  return settableFuture;
}
```

<br />

| **Important:** You should aim to complete the `ListenableFuture` as quickly as possible to keep startup latency low.

If you've stored other parameters such as playback speed, repeat mode, or
shuffle mode, `onPlaybackResumption()` is a good place to configure the player
with these parameters before Media3 prepares the player and starts playback when
the callback completes.

This method is called during boot time to create the Android System UI
resumption notification after a reboot of the device with `isForPlayback` set to
`false`. For a rich notification, it is recommended to fill in `MediaMetadata`
fields like `title` and `artworkData` or `artworkUri` of the current item with
locally available values, as network access may not yet be available. You can
also add `MediaConstants.EXTRAS_KEY_COMPLETION_STATUS` and
`MediaConstants.EXTRAS_KEY_COMPLETION_PERCENTAGE` to the `MediaMetadata.extras`
to indicate the resumption playback position.

## Advanced controller configuration and backward compatibility

A common scenario is using a `MediaController` in the app UI for controlling
playback and displaying the playlist. At the same time, the session is exposed
to external clients like Android media controls and Assistant on mobile or TV,
Wear OS for watches and Android Auto in cars. The Media3 [session demo app](https://github.com/androidx/media/tree/release/demos/session)
is an example of an app that implements such a scenario.

These external clients may use APIs like `MediaControllerCompat` of the legacy
AndroidX library or `android.media.session.MediaController` of the Android
platform. Media3 is fully backward compatible with the legacy library and
provides interoperability with the Android platform API.

### Identify trusted controllers

Any app can attempt to connect to your media session or library. If you want to
restrict access to system controllers, controllers with media content control
permission, and your own app, you can use `ControllerInfo.isTrusted()` for a
basic access check. Alternatively, you can identify more specific controllers
like the media notification controller or Android Auto controllers as described
in the following sections.

### Use the media notification controller

It's important to understand that these legacy and platform controllers share
the same state and visibility can't be customized by controller (for example the
available `PlaybackState.getActions()` and `PlaybackState.getCustomActions()`).
You can can use the [media notification controller](https://developer.android.com/reference/androidx/media3/session/MediaSession#getMediaNotificationControllerInfo()) to
configure the state set in the platform media session for compatibility to these
legacy and platform controllers.

For example, an app can provide an implementation of
`MediaSession.Callback.onConnect()` to set available commands and
media button preferences specifically for the platform session as follows:  

### Kotlin

```kotlin
override fun onConnect(
  session: MediaSession,
  controller: MediaSession.ControllerInfo
): ConnectionResult {
  if (session.isMediaNotificationController(controller)) {
    val playerCommands =
      ConnectionResult.DEFAULT_PLAYER_COMMANDS.buildUpon()
        .remove(COMMAND_SEEK_TO_PREVIOUS)
        .remove(COMMAND_SEEK_TO_PREVIOUS_MEDIA_ITEM)
        .remove(COMMAND_SEEK_TO_NEXT)
        .remove(COMMAND_SEEK_TO_NEXT_MEDIA_ITEM)
        .build()
    // Custom button preferences and commands to configure the platform session.
    return AcceptedResultBuilder(session)
      .setMediaButtonPreferences(
        listOf(seekBackButton, seekForwardButton)
      )
      .setAvailablePlayerCommands(playerCommands)
      .build()
  }
  // Default commands with default button preferences for all other controllers.
  return AcceptedResultBuilder(session).build()
}
```

### Java

```java
@Override
public ConnectionResult onConnect(
    MediaSession session, MediaSession.ControllerInfo controller) {
  if (session.isMediaNotificationController(controller)) {
    Player.Commands playerCommands =
        ConnectionResult.DEFAULT_PLAYER_COMMANDS
            .buildUpon()
            .remove(COMMAND_SEEK_TO_PREVIOUS)
            .remove(COMMAND_SEEK_TO_PREVIOUS_MEDIA_ITEM)
            .remove(COMMAND_SEEK_TO_NEXT)
            .remove(COMMAND_SEEK_TO_NEXT_MEDIA_ITEM)
            .build();
    // Custom button preferences and commands to configure the platform session.
    return new AcceptedResultBuilder(session)
        .setMediaButtonPreferences(
            ImmutableList.of(seekBackButton, seekForwardButton))
        .setAvailablePlayerCommands(playerCommands)
        .build();
  }
  // Default commands with default button preferences for all other controllers.
  return new AcceptedResultBuilder(session).build();
}
```

<br />

| **Caution:** Rejecting an attempt of the media notification controller to connect, causes your app to not work properly.

### Authorize Android Auto to send custom commands

When using a [`MediaLibraryService`](https://developer.android.com/guide/topics/media/session/medialibraryservice)
and to support Android Auto with the mobile app, the Android Auto controller
requires appropriate available commands, otherwise Media3 would deny
incoming custom commands from that controller:  

### Kotlin

```kotlin
override fun onConnect(
  session: MediaSession,
  controller: MediaSession.ControllerInfo
): ConnectionResult {
  val sessionCommands =
    ConnectionResult.DEFAULT_SESSION_AND_LIBRARY_COMMANDS.buildUpon()
      .add(customCommand)
      .build()
  if (session.isMediaNotificationController(controller)) {
    // [...] See above.
  } else if (session.isAutoCompanionController(controller)) {
    // Available session commands to accept incoming custom commands from Auto.
    return AcceptedResultBuilder(session)
      .setAvailableSessionCommands(sessionCommands)
      .build()
  }
  // Default commands for all other controllers.
  return AcceptedResultBuilder(session).build()
}
```

### Java

```java
@Override
public ConnectionResult onConnect(
    MediaSession session, MediaSession.ControllerInfo controller) {
  SessionCommands sessionCommands =
      ConnectionResult.DEFAULT_SESSION_COMMANDS
          .buildUpon()
          .add(customCommand)
          .build();
  if (session.isMediaNotificationController(controller)) {
    // [...] See above.
  } else if (session.isAutoCompanionController(controller)) {
    // Available commands to accept incoming custom commands from Auto.
    return new AcceptedResultBuilder(session)
        .setAvailableSessionCommands(sessionCommands)
        .build();
  }
  // Default commands for all other controllers.
  return new AcceptedResultBuilder(session).build();
}
```

<br />

The session demo app has an
[automotive module](https://github.com/androidx/media/tree/main/demos/session_automotive),
that demonstrates support for Automotive OS that requires a separate APK.