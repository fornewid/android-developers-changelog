---
title: https://developer.android.com/media/media3/session/control-playback
url: https://developer.android.com/media/media3/session/control-playback
source: md.txt
---

Media sessions provide a universal way of interacting with an audio or video
player. In Media3, the default player is the `ExoPlayer` class, which implements
the `Player` interface. Connecting the media session to the player allows an app
to advertise media playback externally and to receive playback commands from
external sources.

Commands may originate from physical buttons such as the play button on a
headset or TV remote control. They might also come from client apps that have a
media controller, such as instructing "pause" to Google Assistant. The media
session delegates these commands to the media app's player.

## When to choose a media session

When you implement `MediaSession`, you allow users to control playback:

- Through their **headphones**. There are often buttons or touch interactions a user can perform on their headphones to play or pause media or go to the next or previous track.
- By talking to the **Google Assistant** . A common pattern is to say *"OK
  Google, pause"* to pause any media that is currently playing on the device.
- Through their **Wear OS watch**. This allows for easier access to the most common playback controls while playing on their phone.
- Through the **Media controls**. This carousel shows controls for each running media session.
- On **TV**. Allows actions with physical playback buttons, platform playback control, and power management (for example if the TV, soundbar or A/V receiver switches off or the input is switched, playback should stop in the app).
- Through the **Android Auto** media controls. This allows for safe playback control while driving.
- And any other external processes that need to influence playback.

This is great for many use cases. In particular, you should strongly consider
using `MediaSession` when:

- You're streaming **long-form video content**, such as movies or live TV.
- You're streaming **long-form audio content**, such as podcasts or music playlists.
- You're building a **TV app**.

However, not all use cases fit well with the `MediaSession`. You might want to
use just the `Player` in the following cases:

- You're showing **short-form content**, where no external control or background playback is needed.
- There isn't a single active video, such as user is scrolling through a list and **multiple videos are displayed** on screen at the same time.
- You're playing a **one-off introduction or explanation video**, which you expect your user to actively watch without needing external playback controls.
- Your content is **privacy-sensitive** and you don't want external processes to access the media metadata (for example incognito mode in a browser).

If your use case does not fit any of those listed above, consider whether you're
okay with your app continuing playback when the user is not actively engaging
with the content. If the answer is yes, you probably want to choose
`MediaSession`. If the answer is no, you probably want to use the `Player`
instead.

## Create a media session

A media session lives alongside the player that it manages. You can construct a
media session with a `Context` and a `Player` object. You should create and
initialize a media session when it is needed, such as the `onStart()` or
`onResume()` lifecycle method of the `Activity` or `Fragment`, or `onCreate()`
method of the `Service` that owns the media session and its associated player.

To create a media session, initialize a `Player` and supply it to
`MediaSession.Builder` like this:  

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

<br />

### Automatic state handling

The Media3 library automatically updates the media session using the
player's state. As such, you don't need to manually handle the mapping from
player to session.

This is different from the platform media session where you needed to create and
maintain a `PlaybackState` independently from the player itself, for example to
indicate any [errors](https://developer.android.com/media/media3/session/control-playback#error-handling).

### Unique session ID

By default, `MediaSession.Builder` creates a session with an empty string as
the session ID. This is sufficient if an app intends to only create a single
session instance, which is the most common case.

If an app wants to manage multiple session instances at the same time, the app
has to ensure that the session ID of each session is unique. The session ID can
be set when building the session with `MediaSession.Builder.setId(String id)`.

If you see an `IllegalStateException` crashing your app with the error
message `IllegalStateException: Session ID must be unique. ID=` then it is
likely that a session has been unexpectedly created before a previously created
instance with the same ID has been released. To avoid sessions to be leaked by a
programming error, such cases are detected and notified by throwing an
exception.

## Grant control to other clients

The media session is the key to controlling playback. It enables you to route
commands from external sources to the player that does the work of playing your
media. These sources can be physical buttons such as the play button on a
headset or TV remote control, or indirect commands such as instructing "pause"
to Google Assistant. Likewise, you may wish to grant access to the Android
system to facilitate notification and lock screen controls, or to a Wear OS
watch so that you can control playback from the watchface. External clients can
use a media controller to issue playback commands to your media app. These are
received by your media session, which ultimately delegates commands to the
media player.
![A diagram demonstrating the interaction between a MediaSession and MediaController.](https://developer.android.com/static/guide/topics/media/images/backgroundcontrols.png) **Figure 1**: The media controller facilitates passing commands from external sources to the media session. **Note:** When playing media in the background, your MediaSession and the player need to be housed within a `MediaSessionService` or `MediaLibraryService` that runs as a foreground service. For more information, see [Background
| playback with a `MediaSessionService`](https://developer.android.com/guide/topics/media/session/mediasessionservice).

When a controller is about to connect to your media session, the
[`onConnect()`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onConnect(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo))
method is called. You can use the provided [`ControllerInfo`](https://developer.android.com/reference/androidx/media3/session/MediaSession.ControllerInfo)
to decide whether to [accept](https://developer.android.com/reference/androidx/media3/session/MediaSession.ConnectionResult#accept(androidx.media3.session.SessionCommands,androidx.media3.common.Player.Commands))
or [reject](https://developer.android.com/reference/androidx/media3/session/MediaSession.ConnectionResult#reject())
the request. See an example of accepting a connection request in the [Declare
custom commands](https://developer.android.com/media/media3/session/control-playback#available-commands) section.

After connecting, a controller can send playback commands to the session. The
session then delegates those commands down to the player. Playback and playlist
commands defined in the `Player` interface are automatically handled by the
session.

Other callback methods allow you to handle, for example, requests for [custom
commands](https://developer.android.com/media/media3/session/control-playback#available-commands) and [modifying the playlist](https://developer.android.com/media/media3/session/control-playback#modify-playlist). These
callbacks similarly include a `ControllerInfo` object so you can modify how you
respond to each request on a per-controller basis.

## Modify the playlist

A media session can directly modify the playlist of its player as explained in
the
[ExoPlayer guide for playlists](https://developer.android.com/guide/topics/media/exoplayer/playlists#modifying-playlist).
Controllers are also able to modify the playlist if either
`COMMAND_SET_MEDIA_ITEM` or `COMMAND_CHANGE_MEDIA_ITEMS` is available to the
controller.

When adding new items to the playlist, the player typically requires `MediaItem`
instances with a
[defined URI](https://developer.android.com/reference/androidx/media3/common/MediaItem.Builder#setUri(java.lang.String))
to make them playable. By default, newly added items are automatically forwarded
to player methods like `player.addMediaItem` if they have a URI defined.

If you want to customize the `MediaItem` instances added to the player, you can
override
[`onAddMediaItems()`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onAddMediaItems(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,java.util.List%3Candroidx.media3.common.MediaItem%3E)).
This step is needed when you want to support controllers that request media
without a defined URI. Instead, the `MediaItem` typically has
one or more of the following fields set to describe the requested media:

- `MediaItem.id`: A generic ID identifying the media.
- `MediaItem.RequestMetadata.mediaUri`: A request URI that may use a custom schema and is not necessarily directly playable by the player.
- `MediaItem.RequestMetadata.searchQuery`: A textual search query, for example from Google Assistant.
- `MediaItem.MediaMetadata`: Structured metadata like 'title' or 'artist'.

For more customization options for completely new playlists, you can
additionally override
[`onSetMediaItems()`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Callback#onSetMediaItems(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,java.util.List%3Candroidx.media3.common.MediaItem%3E,int,long))
that lets you define the start item and position in the playlist. For example,
you can expand a single requested item to an entire playlist and instruct the
player to start at the index of the originally requested item. A
[sample implementation of `onSetMediaItems()`](https://github.com/androidx/media/blob/4bcb60d31d8c8996a93c6703ee934f62a50a837a/demos/session_service/src/main/java/androidx/media3/demo/session/DemoMediaLibrarySessionCallback.kt#L163)
with this feature can be found in the session demo app.

## Manage media button preferences

Every controller, for example System UI, Android Auto, or Wear OS, can make its
own decisions about which buttons to show to the user. To indicate which
playback controls you want to expose to the user, you can specify *media button
preferences* on the `MediaSession`. These preferences consist of an ordered list
of `CommandButton` instances, each defining a preference for a button in the
user interface.

### Define command buttons

`CommandButton` instances are used to define media button preferences. Every
button defines three aspects of the desired UI element:

1. The **Icon** , defining the visual appearance. The icon must be set to one of the predefined constants when creating a `CommandButton.Builder`. Note that this isn't an actual Bitmap or image resource. A generic constant helps controllers to choose an appropriate resource for a consistent look and feel within their own UI. If none of the predefined icon constants fit your use case, you can use `setCustomIconResId` instead.
2. The **Command** , defining the action triggered when the user interacts with the button. You can use `setPlayerCommand` for a `Player.Command`, or `setSessionCommand` for a predefined or custom `SessionCommand`.
3. The **Slot** , defining where the button should be placed in the controller UI. This field is optional and automatically set based on the *Icon* and *Command*. For example, it allows to specify that a button should be displayed in the 'forward' navigation area of the UI instead of the default 'overflow' area.

### Kotlin

```kotlin
val button =
  CommandButton.Builder(CommandButton.ICON_SKIP_FORWARD_15)
    .setPlayerCommand(Player.COMMAND_SEEK_FORWARD)
    .setSlots(CommandButton.SLOT_FORWARD)
    .build()
```

### Java

```java
CommandButton button =
    new CommandButton.Builder(CommandButton.ICON_SKIP_FORWARD_15)
        .setPlayerCommand(Player.COMMAND_SEEK_FORWARD)
        .setSlots(CommandButton.SLOT_FORWARD)
        .build();
```

<br />

| **Note:** Some commands like `COMMAND_SET_REPEAT_MODE` need additional parameters to be fully functional. You can specify these parameters as a second argument in `setPlayerCommand`. Refer to the documentation of [`CommandButton.executeAction`](https://developer.android.com/reference/androidx/media3/session/CommandButton#executeAction(androidx.media3.session.MediaController)) for a complete list of supported commands.

When media button preferences are resolved, the following algorithm is applied:

1. For each `CommandButton` in the *media button preferences* , place the button in the first available and allowed *slot*.
2. If any of the central, forward and backward *slots* are not filled with a button, add default buttons for this *slot*.

You can use `CommandButton.DisplayConstraints` to generate a preview of how
the media button preferences will be resolved depending on the UI display
constraints.

### Set media button preferences

The easiest way to set the media button preferences is to define the list when
building the `MediaSession`. Alternatively, you can override
`MediaSession.Callback.onConnect` to customize the media button preferences for
each connected controller.  

### Kotlin

```kotlin
val mediaSession =
  MediaSession.Builder(context, player)
    .setMediaButtonPreferences(ImmutableList.of(likeButton, favoriteButton))
    .build()
```

### Java

```java
MediaSession mediaSession =
  new MediaSession.Builder(context, player)
      .setMediaButtonPreferences(ImmutableList.of(likeButton, favoriteButton))
      .build();
```

<br />

### Update media button preferences after a user interaction

After handling an interaction with your player, you may want to update the
buttons displayed in the controller UI. A typical example is a toggle button
that changes its icon and action after triggering the action associated with
this button. To update the media button preferences, you can use
`MediaSession.setMediaButtonPreferences` to either update the preferences for
all controllers or a specific controller:  

### Kotlin

```kotlin
// Handle "favoritesButton" action, replace by opposite button
mediaSession.setMediaButtonPreferences(
  ImmutableList.of(likeButton, removeFromFavoritesButton))
```

### Java

```java
// Handle "favoritesButton" action, replace by opposite button
mediaSession.setMediaButtonPreferences(
    ImmutableList.of(likeButton, removeFromFavoritesButton));
```

<br />

## Add custom commands and customize default behavior

The available player commands can be extended by custom commands and it's also
possible to intercept incoming player commands and media buttons to change the
default behavior.

### Declare and handle custom commands

Media applications can define custom commands that for instance can be used in
the [media button preferences](https://developer.android.com/media/media3/session/control-playback#command-buttons). For example, you may
want to implement buttons that allow the user to save a media item to a list of
favorite items. The `MediaController` sends custom commands and the
`MediaSession.Callback` receives them.
| **Caution:** You must implement custom commands as a completely new behavior. Don't use a custom command to replace one of the standard controls defined in the `Player` interface.

To define custom commands, you need to override
`MediaSession.Callback.onConnect()` to set the available custom commands for
each connected controller.  

### Kotlin

```kotlin
private class CustomMediaSessionCallback: MediaSession.Callback {
  // Configure commands available to the controller in onConnect()
  override fun onConnect(
    session: MediaSession,
    controller: MediaSession.ControllerInfo
  ): ConnectionResult {
    val sessionCommands = ConnectionResult.DEFAULT_SESSION_COMMANDS.buildUpon()
        .add(SessionCommand(SAVE_TO_FAVORITES, Bundle.EMPTY))
        .build()
    return AcceptedResultBuilder(session)
        .setAvailableSessionCommands(sessionCommands)
        .build()
  }
}
```

### Java

```java
class CustomMediaSessionCallback implements MediaSession.Callback {
  // Configure commands available to the controller in onConnect()
  @Override
  public ConnectionResult onConnect(
    MediaSession session,
    ControllerInfo controller) {
    SessionCommands sessionCommands =
        ConnectionResult.DEFAULT_SESSION_COMMANDS.buildUpon()
            .add(new SessionCommand(SAVE_TO_FAVORITES, new Bundle()))
            .build();
    return new AcceptedResultBuilder(session)
        .setAvailableSessionCommands(sessionCommands)
        .build();
  }
}
```

<br />

To receive custom command requests from a `MediaController`, override the
`onCustomCommand()` method in the `Callback`.  

### Kotlin

```kotlin
private class CustomMediaSessionCallback: MediaSession.Callback {
  ...
  override fun onCustomCommand(
    session: MediaSession,
    controller: MediaSession.ControllerInfo,
    customCommand: SessionCommand,
    args: Bundle
  ): ListenableFuture<SessionResult> {
    if (customCommand.customAction == SAVE_TO_FAVORITES) {
      // Do custom logic here
      saveToFavorites(session.player.currentMediaItem)
      return Futures.immediateFuture(
        SessionResult(SessionResult.RESULT_SUCCESS)
      )
    }
    ...
  }
}
```

### Java

```java
class CustomMediaSessionCallback implements MediaSession.Callback {
  ...
  @Override
  public ListenableFuture<SessionResult> onCustomCommand(
    MediaSession session, 
    ControllerInfo controller,
    SessionCommand customCommand,
    Bundle args
  ) {
    if(customCommand.customAction.equals(SAVE_TO_FAVORITES)) {
      // Do custom logic here
      saveToFavorites(session.getPlayer().getCurrentMediaItem());
      return Futures.immediateFuture(
        new SessionResult(SessionResult.RESULT_SUCCESS)
      );
    }
    ...
  }
}
```

<br />

You can track which media controller is making a request by using the
`packageName` property of the `MediaSession.ControllerInfo` object that is
passed into `Callback` methods. This allows you to tailor your app's
behavior in response to a given command if it originates from the system, your
own app, or other client apps.

### Customize default player commands

All default commands and state handling is delegated to the `Player` that is on
the `MediaSession`. To customize the behavior of a command defined in the
`Player` interface, such as `play()` or `seekToNext()`, wrap your `Player` in a
`ForwardingSimpleBasePlayer` before passing it to `MediaSession`:  

### Kotlin

```kotlin
val player = (logic to build a Player instance)

val forwardingPlayer = object : ForwardingSimpleBasePlayer(player) {
  // Customizations
}

val mediaSession = MediaSession.Builder(context, forwardingPlayer).build()
```

### Java

```java
ExoPlayer player = (logic to build a Player instance)

ForwardingSimpleBasePlayer forwardingPlayer =
    new ForwardingSimpleBasePlayer(player) {
      // Customizations
    };

MediaSession mediaSession =
  new MediaSession.Builder(context, forwardingPlayer).build();
```

<br />

For more information about `ForwardingSimpleBasePlayer`, see the ExoPlayer guide
on
[Customization](https://developer.android.com/guide/topics/media/exoplayer/customization#player-operations).

### Identify the requesting controller of a player command

When a call to a `Player` method is originated by a `MediaController`, you can
identify the source of origin with `MediaSession.controllerForCurrentRequest`
and acquire the `ControllerInfo` for the current request:  

### Kotlin

```kotlin
class CallerAwarePlayer(player: Player) :
  ForwardingSimpleBasePlayer(player) {

  override fun handleSeek(
    mediaItemIndex: Int,
    positionMs: Long,
    seekCommand: Int,
  ): ListenableFuture<*> {
    Log.d(
      "caller",
      "seek operation from package ${session.controllerForCurrentRequest?.packageName}",
    )
    return super.handleSeek(mediaItemIndex, positionMs, seekCommand)
  }
}
```

### Java

```java
public class CallerAwarePlayer extends ForwardingSimpleBasePlayer {
  public CallerAwarePlayer(Player player) {
    super(player);
  }

  @Override
  protected ListenableFuture<?> handleSeek(
        int mediaItemIndex, long positionMs, int seekCommand) {
    Log.d(
        "caller",
        "seek operation from package: "
            + session.getControllerForCurrentRequest().getPackageName());
    return super.handleSeek(mediaItemIndex, positionMs, seekCommand);
  }
}
```

<br />

### Customize media button handling

Media buttons are hardware buttons found on Android devices and other peripheral
devices, such as the play/pause button on a Bluetooth headset. Media3 handles
media button events for you when they arrive at the session and calls the
appropriate `Player` method on the [session player](https://developer.android.com/reference/androidx/media3/session/MediaSession#getPlayer()).

It is recommended to handle all incoming media button events in the
corresponding `Player` method. For more advanced use cases, the media button
events can be intercepted in `MediaSession.Callback.onMediaButtonEvent(Intent)`.

## Error handling and reporting

There are two types of errors that a session emits and reports to controllers.
Fatal errors report a technical playback failure of the session
player that interrupts playback. Fatal errors are reported to the controller
automatically when they occur. Nonfatal errors are non-technical or policy
errors that don't interrupt playback and are sent to controllers by the
application manually.

### Fatal playback errors

A fatal playback error is reported to the session by the player and then
reported to controllers to call through
`Player.Listener.onPlayerError(PlaybackException)` and
`Player.Listener.onPlayerErrorChanged(@Nullable PlaybackException)`.

In such a case, the playback state is transitioned to `STATE_IDLE` and
`MediaController.getPlaybackError()` returns the `PlaybackException` that caused
the transition. A controller can inspect the `PlayerException.errorCode` to get
information about the reason for the error.
| **Note:** For interoperability, a fatal error is replicated to the platform session by transitioning its state to `STATE_ERROR` and setting error code and message according to the `PlaybackException`.

#### Setting a custom player error

In addition to fatal errors reported by the player, an application can
set a custom `PlaybackException` on the MediaSession level using
`MediaSession.setPlaybackException(PlaybackException)`. This allows the
application to signal an error state to connected controllers. The exception can
be set for all connected controllers or for a specific `ControllerInfo`.

When an app sets a `PlaybackException` using this API:

- Connected `MediaController` instances will be notified. The
  `Listener.onPlayerError(PlaybackException)` and
  `Listener.onPlayerErrorChanged(@Nullable PlaybackException)`
  callbacks on the controller will be invoked with the provided exception.

- The `MediaController.getPlayerError()` method will return the
  `PlaybackException` set by the application.

- The playback state for the affected controllers will change to
  `Player.STATE_IDLE`.

- Available commands will be removed and only reading commands like
  `COMMAND_GET_TIMELINE` are left in case they are already granted. The state of
  the `Timeline`, for example, is frozen to the state when the exception was
  applied to the controller. Commands that attempt to change the state of the
  player, like `COMMAND_PLAY`, are removed until the playback exception for the
  given controller is removed by the app.

| **Note:** If a controller connects while the session has a `PlaybackException` set, the controller's initial state will be `Player.STATE_IDLE` and `getPlayerError()` will return the session-level exception.

To clear a previously set custom `PlaybackException` and restore the normal
player state reporting, an app can call
`MediaSession.setPlaybackException(/* playbackException= */ null)` or
`MediaSession.setPlaybackException(ControllerInfo,
/* playbackException= */ null)`.

#### Customization of fatal errors

To provide localized and meaningful information to the user, you can customize
the error code, the error message, and error extras of a fatal playback error
coming from the actual player. It can be achieved by using a `ForwardingPlayer`
when building the session:  

### Kotlin

```kotlin
val forwardingPlayer = ErrorForwardingPlayer(player)
val session = MediaSession.Builder(context, forwardingPlayer).build()
```

### Java

```java
Player forwardingPlayer = new ErrorForwardingPlayer(player);
MediaSession session =
    new MediaSession.Builder(context, forwardingPlayer).build();
```

<br />

The forwarding player can use `ForwardingSimpleBasePlayer` to intercept the
error and customize the error code, message or extras. In the same way, you can
also generate new errors that don't exist in the original player:  

### Kotlin

```kotlin
class ErrorForwardingPlayer (private val context: Context, player: Player) :
    ForwardingSimpleBasePlayer(player) {

  override fun getState(): State {
    var state = super.getState()
    if (state.playerError != null) {
      state =
        state.buildUpon()
          .setPlayerError(customizePlaybackException(state.playerError!!))
          .build()
    }
    return state
  }

  fun customizePlaybackException(error: PlaybackException): PlaybackException {
    val buttonLabel: String
    val errorMessage: String
    when (error.errorCode) {
      PlaybackException.ERROR_CODE_BEHIND_LIVE_WINDOW -> {
        buttonLabel = context.getString(R.string.err_button_label_restart_stream)
        errorMessage = context.getString(R.string.err_msg_behind_live_window)
      }
      else -> {
        buttonLabel = context.getString(R.string.err_button_label_ok)
        errorMessage = context.getString(R.string.err_message_default)
      }
    }
    val extras = Bundle()
    extras.putString("button_label", buttonLabel)
    return PlaybackException(errorMessage, error.cause, error.errorCode, extras)
  }
}
```

### Java

```java
class ErrorForwardingPlayer extends ForwardingSimpleBasePlayer {

  private final Context context;

  public ErrorForwardingPlayer(Context context, Player player) {
    super(player);
    this.context = context;
  }

  @Override
  protected State getState() {
    State state = super.getState();
    if (state.playerError != null) {
      state =
          state.buildUpon()
              .setPlayerError(customizePlaybackException(state.playerError))
              .build();
    }
    return state;
  }

  private PlaybackException customizePlaybackException(PlaybackException error) {
    String buttonLabel;
    String errorMessage;
    switch (error.errorCode) {
      case PlaybackException.ERROR_CODE_BEHIND_LIVE_WINDOW:
        buttonLabel = context.getString(R.string.err_button_label_restart_stream);
        errorMessage = context.getString(R.string.err_msg_behind_live_window);
        break;
      default:
        buttonLabel = context.getString(R.string.err_button_label_ok);
        errorMessage = context.getString(R.string.err_message_default);
        break;
    }
    Bundle extras = new Bundle();
    extras.putString("button_label", buttonLabel);
    return new PlaybackException(errorMessage, error.getCause(), error.errorCode, extras);
  }
}
```

<br />

### Nonfatal errors

Nonfatal errors that do *not* originate from a technical exception can be sent
by an app to all or to a specific controller:  

### Kotlin

```kotlin
val sessionError = SessionError(
  SessionError.ERROR_SESSION_AUTHENTICATION_EXPIRED,
  context.getString(R.string.error_message_authentication_expired),
)

// Option 1: Sending a nonfatal error to all controllers.
mediaSession.sendError(sessionError)

// Option 2: Sending a nonfatal error to the media notification controller only
// to set the error code and error message in the playback state of the platform
// media session.
mediaSession.mediaNotificationControllerInfo?.let {
  mediaSession.sendError(it, sessionError)
}
```

### Java

```java
SessionError sessionError = new SessionError(
    SessionError.ERROR_SESSION_AUTHENTICATION_EXPIRED,
    context.getString(R.string.error_message_authentication_expired));

// Option 1: Sending a nonfatal error to all controllers.
mediaSession.sendError(sessionError);

// Option 2: Sending a nonfatal error to the media notification controller only
// to set the error code and error message in the playback state of the platform
// media session.
ControllerInfo mediaNotificationControllerInfo =
    mediaSession.getMediaNotificationControllerInfo();
if (mediaNotificationControllerInfo != null) {
  mediaSession.sendError(mediaNotificationControllerInfo, sessionError);
}
```

When a nonfatal error is sent to the media notification controller, the error
code and error message is replicated to the platform media session, while
`PlaybackState.state` is not changed to `STATE_ERROR`.

#### Receive nonfatal errors

A `MediaController` receives a nonfatal error by implementing
`MediaController.Listener.onError`:  

### Kotlin

```kotlin
val future = MediaController.Builder(context, sessionToken)
  .setListener(object : MediaController.Listener {
    override fun onError(controller: MediaController, sessionError: SessionError) {
      // Handle nonfatal error.
    }
  })
  .buildAsync()
```

### Java

```java
MediaController.Builder future =
    new MediaController.Builder(context, sessionToken)
        .setListener(
            new MediaController.Listener() {
              @Override
              public void onError(MediaController controller, SessionError sessionError) {
                // Handle nonfatal error.
              }
            });
```

<br />