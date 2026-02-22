---
title: https://developer.android.com/media/media3/session/serve-content
url: https://developer.android.com/media/media3/session/serve-content
source: md.txt
---

Media apps often contain collections of media items, organized in a hierarchy.
For example, songs in an album or TV episodes in a playlist. This hierarchy of
media items is known as a media library.
![Examples of media content arranged in a hierarchy](https://developer.android.com/static/guide/topics/media/images/media-library-examples.svg) **Figure 1**: Examples of media item hierarchies that form a media library.

A `MediaLibraryService` provides a standardized API to serve and access your
media library. This can be helpful, for example, when adding support for
[Android Auto](https://developer.android.com/training/cars/media) to your media app, which provides its own
driver-safe UI for your media library.

## Build a `MediaLibraryService`

Implementing a `MediaLibraryService` is similar to
[implementing a `MediaSessionService`](https://developer.android.com/guide/topics/media/session/mediasessionservice#provide-access),
except that in the `onGetSession()` method, you should
return a `MediaLibrarySession` instead of a `MediaSession`.  

### Kotlin

```kotlin
class PlaybackService : MediaLibraryService() {
  var mediaLibrarySession: MediaLibrarySession? = null
  var callback: MediaLibrarySession.Callback = object : MediaLibrarySession.Callback {...}

  // If desired, validate the controller before returning the media library session
  override fun onGetSession(controllerInfo: MediaSession.ControllerInfo): MediaLibrarySession? =
    mediaLibrarySession

  // Create your player and media library session in the onCreate lifecycle event
  override fun onCreate() {
    super.onCreate()
    val player = ExoPlayer.Builder(this).build()
    mediaLibrarySession = MediaLibrarySession.Builder(this, player, callback).build()
  }

  // Remember to release the player and media library session in onDestroy
  override fun onDestroy() {
    mediaLibrarySession?.run { 
      player.release()
      release()
      mediaLibrarySession = null
    }
    super.onDestroy()
  }
}
```

### Java

```java
class PlaybackService extends MediaLibraryService {
  MediaLibrarySession mediaLibrarySession = null;
  MediaLibrarySession.Callback callback = new MediaLibrarySession.Callback() {...};

  @Override
  public MediaLibrarySession onGetSession(MediaSession.ControllerInfo controllerInfo) {
    // If desired, validate the controller before returning the media library session
    return mediaLibrarySession;
  }

  // Create your player and media library session in the onCreate lifecycle event
  @Override
  public void onCreate() {
    super.onCreate();
    ExoPlayer player = new ExoPlayer.Builder(this).build();
    mediaLibrarySession = new MediaLibrarySession.Builder(this, player, callback).build();
  }

  // Remember to release the player and media library session in onDestroy
  @Override
  public void onDestroy() {
    if (mediaLibrarySession != null) {
      mediaLibrarySession.getPlayer().release();
      mediaLibrarySession.release();
      mediaLibrarySession = null;
    }
    super.onDestroy();
  }
}
```

<br />

Remember to declare your `Service` and required permissions in the manifest file
as well:  

    <service
        android:name=".PlaybackService"
        android:foregroundServiceType="mediaPlayback"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.media3.session.MediaSessionService"/>
            <action android:name="android.media.browse.MediaBrowserService"/>
        </intent-filter>
    </service>

    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

| **Note:** For compatibility with clients using the platform media session APIs, it is recommended to include `<action android:name="android.media.browse.MediaBrowserService"/>` in the `intent-filter` element.

## Use a `MediaLibrarySession`

The `MediaLibraryService` API expects your media library to be structured in a
tree format, with a single root node and children nodes that may be
[playable](https://developer.android.com/reference/kotlin/androidx/media3/common/MediaMetadata#isPlayable())
or further [browsable](https://developer.android.com/reference/kotlin/androidx/media3/common/MediaMetadata#isBrowsable()).

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

## Command buttons for media items

A session app can declare command buttons that are supported by a `MediaItem` in
the `MediaMetadata`. This allows to assign one or more `CommandButton` entries
to a media item that a controller can display and use for sending the custom
command for the item to the session in a convenient way.

### Setup command buttons on the session side

When building the session, a session app declares the set of command buttons
that a session can handle as custom commands:  

### Kotlin

```kotlin
val allCommandButtons =
  listOf(
    CommandButton.Builder(CommandButton.ICON_PLAYLIST_ADD)
      .setDisplayName(context.getString(R.string.add_to_playlist))
      .setSessionCommand(SessionCommand(COMMAND_PLAYLIST_ADD, Bundle.EMPTY))
      .setExtras(playlistAddExtras)
      .build(),
    CommandButton.Builder(CommandButton.ICON_RADIO)
      .setDisplayName(context.getString(R.string.radio_station))
      .setSessionCommand(SessionCommand(COMMAND_RADIO, Bundle.EMPTY))
      .setExtras(radioExtras)
      .build(),
    // possibly more here
  )

// Add all command buttons for media items supported by the session.
val session =
  MediaSession.Builder(context, player)
    .setCommandButtonsForMediaItems(allCommandButtons)
    .build()
```

### Java

```java
ImmutableList<CommandButton> allCommandButtons =
    ImmutableList.of(
        new CommandButton.Builder(CommandButton.ICON_PLAYLIST_ADD)
            .setDisplayName(context.getString(R.string.add_to_playlist))
            .setSessionCommand(new SessionCommand(COMMAND_PLAYLIST_ADD, Bundle.EMPTY))
            .setExtras(playlistAddExtras)
            .build(),
        new CommandButton.Builder(CommandButton.ICON_RADIO)
            .setDisplayName(context.getString(R.string.radio_station))
            .setSessionCommand(new SessionCommand(COMMAND_RADIO, Bundle.EMPTY))
            .setExtras(radioExtras)
            .build());

// Add all command buttons for media items supported by the session.
MediaSession session =
    new MediaSession.Builder(context, player)
        .setCommandButtonsForMediaItems(allCommandButtons)
        .build();
```
| **Note:** The [Android media controls](https://developer.android.com/media/implement/surfaces/mobile#config-action-buttons) that are available through the media notification aren't using command buttons for media items. Use [media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) to declare preferences for these media controls.

When building a media item, a session app can add a set of supported command IDs
that reference session commands of command buttons that have been setup when
building the session:  

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setMediaMetadata(
      MediaMetadata.Builder()
        .setSupportedCommands(listOf(COMMAND_PLAYLIST_ADD, COMMAND_RADIO))
        .build())
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setMediaMetadata(
            new MediaMetadata.Builder()
                .setSupportedCommands(ImmutableList.of(COMMAND_PLAYLIST_ADD, COMMAND_RADIO))
                .build())
        .build();
```
| **Note:** A controller only sees the command buttons for which the session has also made the corresponding [session command available to the controller](https://developer.android.com/media/media3/session/control-playback#available-commands).

When a controller or browser connects or calls another method of the session
`Callback`, the session app can inspect the `ControllerInfo` passed to the
callback to get the maximum number of command buttons a controller or browser
can display. The `ControllerInfo` passed into a callback method provides a
getter to access this value conveniently. By default the value is set to 0 which
indicates that the browser or controller doesn't support this feature:  

### Kotlin

```kotlin
override fun onGetItem(
  session: MediaLibrarySession,
  browser: MediaSession.ControllerInfo,
  mediaId: String,
): ListenableFuture<LibraryResult<MediaItem>> {

  val settableFuture = SettableFuture.create<LibraryResult<MediaItem>>()

  val maxCommandsForMediaItems = browser.maxCommandsForMediaItems
  scope.launch {
    loadMediaItem(settableFuture, mediaId, maxCommandsForMediaItems)
  }

  return settableFuture
}
```

### Java

```java
@Override
public ListenableFuture<LibraryResult<MediaItem>> onGetItem(
    MediaLibraryService.MediaLibrarySession session, ControllerInfo browser, String mediaId) {

  SettableFuture<LibraryResult<MediaItem>> settableFuture = SettableFuture.create();

  int maxCommandsForMediaItems = browser.getMaxCommandsForMediaItems();
  loadMediaItemAsync(settableFuture, mediaId, maxCommandsForMediaItems);

  return settableFuture;
}
```

When handling a custom action that has been sent for a media item, the session
app can get the media item ID from the arguments `Bundle` passed into
`onCustomCommand`:  

### Kotlin

```kotlin
override fun onCustomCommand(
  session: MediaSession,
  controller: MediaSession.ControllerInfo,
  customCommand: SessionCommand,
  args: Bundle,
): ListenableFuture<SessionResult> {
  val mediaItemId = args.getString(MediaConstants.EXTRA_KEY_MEDIA_ID)
  return if (mediaItemId != null)
    handleCustomCommandForMediaItem(controller, customCommand, mediaItemId, args)
  else handleCustomCommand(controller, customCommand, args)
}
```

### Java

```java
@Override
public ListenableFuture<SessionResult> onCustomCommand(
    MediaSession session,
    ControllerInfo controller,
    SessionCommand customCommand,
    Bundle args) {
  String mediaItemId = args.getString(MediaConstants.EXTRA_KEY_MEDIA_ID);
  return mediaItemId != null
      ? handleCustomCommandForMediaItem(controller, customCommand, mediaItemId, args)
      : handleCustomCommand(controller, customCommand, args);
}
```

### Use command buttons as a browser or controller

On the `MediaController` side, an app can declare the maximum number of command
buttons it supports for a media item when building the `MediaController` or
`MediaBrowser`:  

### Kotlin

```kotlin
val browserFuture =
  MediaBrowser.Builder(context, sessionToken)
    .setMaxCommandsForMediaItems(3)
    .buildAsync()
```

### Java

```java
ListenableFuture<MediaBrowser> browserFuture =
    new MediaBrowser.Builder(context, sessionToken)
        .setMaxCommandsForMediaItems(3)
        .buildAsync();
```
| **Note:** By default, the number of commands is set to 0 (zero) which advises the session app to not advertise command buttons for that browser or controller.

When connected to the session, the controller app can receive the
command buttons that are supported by the media item and for which the
controller has the [available command granted by the session app](https://developer.android.com/media/media3/session/control-playback#available-commands):  

### Kotlin

```kotlin
val commandButtonsForMediaItem: List<CommandButton> =
  controller.getCommandButtonsForMediaItem(mediaItem)
```

### Java

```java
ImmutableList<CommandButton> commandButtonsForMediaItem =
    controller.getCommandButtonsForMediaItem(mediaItem);
```
| **Note:** The returned command buttons are the intersection of all buttons that have been set up by the session, the supported commands set on the media item and the available commands of the controller.

For convenience a `MediaController` can send media item specific custom commands
with `MediaController.sendCustomCommand(SessionCommand, MediaItem, Bundle)`:  

### Kotlin

```kotlin
controller.sendCustomCommand(addToPlaylistButton.sessionCommand!!, mediaItem, Bundle.EMPTY)
```

### Java

```java
controller.sendCustomCommand(
    checkNotNull(addToPlaylistButton.sessionCommand), mediaItem, Bundle.EMPTY);
```

<br />