---
title: https://developer.android.com/media/implement/surfaces/mobile
url: https://developer.android.com/media/implement/surfaces/mobile
source: md.txt
---

Media controls in Android are located near the Quick Settings. Sessions from
multiple apps are arranged in a swipeable carousel. The carousel lists sessions
in this order:

- Streams playing locally on the phone
- Remote streams, such as those detected on external devices or cast sessions
- Previous resumable sessions, in the order they were last played

Starting in Android 13 (API level 33), to ensure that users can access a rich
set of media controls for apps playing media, action buttons on media controls
are derived from the `Player` state.

This way, you can present a consistent set of media controls and a more polished
media control experience across devices.

Figure 1 shows an example of how this looks on a phone and tablet device,
respectively.
![Media controls in terms of how they appear on phone and tablets devices,
using an example of a sample track showing how the buttons may appear](https://developer.android.com/static/images/media/samples/media-controls-android-13.svg) **Figure 1:**Media controls on phone and tablet devices

The system displays up to five action buttons based on the `Player` state as
described in the following table. In compact mode, only the first three action
slots are displayed. This aligns with how media controls are rendered in other
Android platforms such as Auto, Assistant, and Wear OS.

| Slot | Criteria | Action |
|---|---|---|
| 1 | [`playWhenReady`](https://developer.android.com/reference/androidx/media3/common/Player#getPlayWhenReady()) is false or the current [playback state](https://developer.android.com/reference/androidx/media3/common/Player#getPlaybackState()) is `STATE_ENDED`. | Play |
| 1 | [`playWhenReady`](https://developer.android.com/reference/androidx/media3/common/Player#getPlayWhenReady()) is true and the current [playback state](https://developer.android.com/reference/androidx/media3/common/Player#getPlaybackState()) is `STATE_BUFFERING`. | Loading spinner |
| 1 | [`playWhenReady`](https://developer.android.com/reference/androidx/media3/common/Player#getPlayWhenReady()) is true and the current [playback state](https://developer.android.com/reference/androidx/media3/common/Player#getPlaybackState()) is `STATE_READY`. | Pause |
| 2 | The [media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) contain a custom button for `CommandButton.SLOT_BACK` | Custom |
| 2 | Player command [`COMMAND_SEEK_TO_PREVIOUS`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_TO_PREVIOUS()) or [`COMMAND_SEEK_TO_PREVIOUS_MEDIA_ITEM`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_TO_PREVIOUS_MEDIA_ITEM()) is available. | Previous |
| 2 | Neither a custom button nor one of the listed commands is available. | Empty |
| 3 | The [media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) contain a custom button for `CommandButton.SLOT_FORWARD` | Custom |
| 3 | Player command [`COMMAND_SEEK_TO_NEXT`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_TO_NEXT()) or [`COMMAND_SEEK_TO_NEXT_MEDIA_ITEM`](https://developer.android.com/reference/androidx/media3/common/Player#COMMAND_SEEK_TO_NEXT_MEDIA_ITEM()) is available. | Next |
| 3 | Neither a custom button nor one of the listed commands is available. | Empty |
| 4 | The [media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) contain a custom button for `CommandButton.SLOT_OVERFLOW` that hasn't been placed yet. | Custom |
| 5 | The [media button preferences](https://developer.android.com/media/media3/session/control-playback#commands) contain a custom button for `CommandButton.SLOT_OVERFLOW` that hasn't been placed yet. | Custom |

Custom overflow button are placed in the order in which they were added to the
media button preferences.
| **Note:** When the user taps on the notification, the system triggers the session activity `PendingIntent` passed to [`MediaSession.Builder#setSessionActivity`](https://developer.android.com/reference/androidx/media3/session/MediaSession.Builder#setSessionActivity(android.app.PendingIntent)) (which must [launch an activity](https://developer.android.com/reference/android/app/PendingIntent#isActivity())).

## Customize command buttons

To customize system media controls with [Jetpack Media3](https://developer.android.com/guide/topics/media/media3), you can set
the media button preferences of the session and the available commands of
controllers accordingly:

1. Build a [`MediaSession`](https://developer.android.com/media/implement/playback-app#managing_playback_with_a_media_session) and [define the media button
   preferences](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaSession.Builder#setMediaButtonPreferences(java.util.List%3Candroidx.media3.session.CommandButton%3E)) for custom command buttons.

2. In [`MediaSession.Callback.onConnect()`](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaSession.Callback#onConnect(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo)),
   authorize controllers by defining their available commands, including [custom
   commands](https://developer.android.com/media/media3/session/control-playback#available-commands), in the `ConnectionResult`.

3. In [`MediaSession.Callback.onCustomCommand()`](https://developer.android.com/reference/kotlin/androidx/media3/session/MediaSession.Callback#onCustomCommand(androidx.media3.session.MediaSession,androidx.media3.session.MediaSession.ControllerInfo,androidx.media3.session.SessionCommand,android.os.Bundle)),
   respond to the custom command being selected by the user.

### Kotlin

```kotlin
class PlaybackService : MediaSessionService() {
  private val customCommandFavorites = SessionCommand(ACTION_FAVORITES, Bundle.EMPTY)
  private var mediaSession: MediaSession? = null

  override fun onCreate() {
    super.onCreate()
    val favoriteButton =
      CommandButton.Builder(CommandButton.ICON_HEART_UNFILLED)
        .setDisplayName("Save to favorites")
        .setSessionCommand(customCommandFavorites)
        .build()
    val player = ExoPlayer.Builder(this).build()
    // Build the session with a custom layout.
    mediaSession =
      MediaSession.Builder(this, player)
        .setCallback(MyCallback())
        .setMediaButtonPreferences(ImmutableList.of(favoriteButton))
        .build()
  }

  private inner class MyCallback : MediaSession.Callback {
    override fun onConnect(
      session: MediaSession,
      controller: MediaSession.ControllerInfo
    ): ConnectionResult {
    // Set available player and session commands.
    return AcceptedResultBuilder(session)
      .setAvailableSessionCommands(
        ConnectionResult.DEFAULT_SESSION_COMMANDS.buildUpon()
          .add(customCommandFavorites)
          .build()
      )
      .build()
    }

    override fun onCustomCommand(
      session: MediaSession,
      controller: MediaSession.ControllerInfo,
      customCommand: SessionCommand,
      args: Bundle
    ): ListenableFuture {
      if (customCommand.customAction == ACTION_FAVORITES) {
        // Do custom logic here
        saveToFavorites(session.player.currentMediaItem)
        return Futures.immediateFuture(SessionResult(SessionResult.RESULT_SUCCESS))
      }
      return super.onCustomCommand(session, controller, customCommand, args)
    }
  }
}
```

### Java

```java
public class PlaybackService extends MediaSessionService {
  private static final SessionCommand CUSTOM_COMMAND_FAVORITES =
      new SessionCommand("ACTION_FAVORITES", Bundle.EMPTY);
  @Nullable private MediaSession mediaSession;

  public void onCreate() {
    super.onCreate();
    CommandButton favoriteButton =
        new CommandButton.Builder(CommandButton.ICON_HEART_UNFILLED)
            .setDisplayName("Save to favorites")
            .setSessionCommand(CUSTOM_COMMAND_FAVORITES)
            .build();
    Player player = new ExoPlayer.Builder(this).build();
    // Build the session with a custom layout.
    mediaSession =
        new MediaSession.Builder(this, player)
            .setCallback(new MyCallback())
            .setMediaButtonPreferences(ImmutableList.of(favoriteButton))
            .build();
  }

  private static class MyCallback implements MediaSession.Callback {
    @Override
    public ConnectionResult onConnect(
        MediaSession session, MediaSession.ControllerInfo controller) {
      // Set available player and session commands.
      return new AcceptedResultBuilder(session)
          .setAvailableSessionCommands(
              ConnectionResult.DEFAULT_SESSION_COMMANDS.buildUpon()
                .add(CUSTOM_COMMAND_FAVORITES)
                .build())
          .build();
    }

    public ListenableFuture onCustomCommand(
        MediaSession session,
        MediaSession.ControllerInfo controller,
        SessionCommand customCommand,
        Bundle args) {
      if (customCommand.customAction.equals(CUSTOM_COMMAND_FAVORITES.customAction)) {
        // Do custom logic here
        saveToFavorites(session.getPlayer().getCurrentMediaItem());
        return Futures.immediateFuture(new SessionResult(SessionResult.RESULT_SUCCESS));
      }
      return MediaSession.Callback.super.onCustomCommand(
          session, controller, customCommand, args);
    }
  }
}
```

To learn more about configuring your `MediaSession` so that clients like the
system can connect to your media app, see
[Grant control to other clients](https://developer.android.com/media/implement/playback-app#grant_control_to_other_clients).

With Jetpack Media3, when you implement a `MediaSession`, your `PlaybackState`
is automatically kept up-to-date with the media player. Similarly, when you
implement a `MediaSessionService`, the library automatically publishes a
`MediaStyle` [notification](https://developer.android.com/media/implement/playback-app#publishing_a_notification)
for you and keeps it up-to-date.

### Respond to action buttons

When a user taps an action button in the system media controls, the system's
`MediaController` sends a playback command to your `MediaSession`. The
`MediaSession` then delegates those commands down to the player. Commands
defined in Media3's [`Player`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player)
interface are automatically handled by the media
session.

Refer to [Add custom commands](https://developer.android.com/media/media3/session/control-playback#available-commands) for guidance on how
to respond to a custom command.

## Support media resumption

Media resumption allows users to restart previous sessions from the carousel
without having to start the app. When playback begins, the user interacts with
the media controls in the usual way.

The playback resumption feature can be turned on and off using the Settings app,
under the **Sound \> Media** options. The user can also access Settings by
tapping the gear icon that appears after swiping on the expanded carousel.

Media3 offers APIs to make it easier to support media resumption. See the
[Playback resumption with Media3](https://developer.android.com/guide/topics/media/session/mediasessionservice#resumption)
documentation for guidance on implementing this feature.

## Using the legacy media APIs

| **Caution:** We strongly recommend using the Jetpack Media3 APIs as described above.

This section explains how to integrate with the system media controls using
the legacy MediaCompat APIs.

The system retrieves the following information from the
`MediaSession`'s `MediaMetadata`, and displays it when it is available:

- `METADATA_KEY_ALBUM_ART_URI`
- `METADATA_KEY_TITLE`
- `METADATA_KEY_DISPLAY_TITLE`
- `METADATA_KEY_ARTIST`
- `METADATA_KEY_DURATION` (If the duration isn't set the seek bar doesn't show progress)

To ensure you have a valid and accurate media control notification,
set the value of the `METADATA_KEY_TITLE` or `METADATA_KEY_DISPLAY_TITLE`
metadata to the title of the media currently being played.

The media player shows the elapsed time for the currently playing
media, along with a seek bar which is mapped to the `MediaSession`
`PlaybackState`.

The media player shows the progress for the currently playing media, along with
a seek bar which is mapped to the `MediaSession` `PlaybackState`. The seek bar
allows users to change the position and displays the elapsed time for the media
item. In order for the seek bar to be enabled, you must implement
`PlaybackState.Builder#setActions` and include `ACTION_SEEK_TO`.

| Slot | Action | Criteria |
|---|---|---|
| 1 | Play | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is the one of the following: - `STATE_NONE` - `STATE_STOPPED` - `STATE_PAUSED` - `STATE_ERROR` |
| 1 | Loading spinner | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is one of the following: - `STATE_CONNECTING` - `STATE_BUFFERING` |
| 1 | Pause | Current [state](https://developer.android.com/reference/android/media/session/PlaybackState#getState()) of the `PlaybackState` is none of the above. |
| 2 | Previous | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) include `ACTION_SKIP_TO_PREVIOUS`. |
| 2 | Custom | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) don't include `ACTION_SKIP_TO_PREVIOUS` and `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 2 | Empty | `PlaybackState` [extras](https://developer.android.com/reference/android/media/session/PlaybackState#getExtras()) include a `true` boolean value for key [`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV). |
| 3 | Next | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) include `ACTION_SKIP_TO_NEXT`. |
| 3 | Custom | `PlaybackState` [actions](https://developer.android.com/reference/android/media/session/PlaybackState#getActions()) don't include `ACTION_SKIP_TO_NEXT` and `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 3 | Empty | `PlaybackState` [extras](https://developer.android.com/reference/android/media/session/PlaybackState#getExtras()) include a `true` boolean value for key [`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT). |
| 4 | Custom | `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |
| 5 | Custom | `PlaybackState` [custom actions](https://developer.android.com/reference/android/media/session/PlaybackState#getCustomActions()) include a custom action that hasn't been placed yet. |

### Add standard actions

The following code examples illustrate how to add `PlaybackState` standard and
custom actions.

For play, pause, previous, and next, set these actions in
the `PlaybackState` for the media session.  

### Kotlin

```kotlin
val session = MediaSessionCompat(context, TAG)
val playbackStateBuilder = PlaybackStateCompat.Builder()
val style = NotificationCompat.MediaStyle()

// For this example, the media is currently paused:
val state = PlaybackStateCompat.STATE_PAUSED
val position = 0L
val playbackSpeed = 1f
playbackStateBuilder.setState(state, position, playbackSpeed)

// And the user can play, skip to next or previous, and seek
val stateActions = PlaybackStateCompat.ACTION_PLAY
    or PlaybackStateCompat.ACTION_PLAY_PAUSE
    or PlaybackStateCompat.ACTION_SKIP_TO_PREVIOUS
    or PlaybackStateCompat.ACTION_SKIP_TO_NEXT
    or PlaybackStateCompat.ACTION_SEEK_TO // adding the seek action enables seeking with the seekbar
playbackStateBuilder.setActions(stateActions)

// ... do more setup here ...

session.setPlaybackState(playbackStateBuilder.build())
style.setMediaSession(session.sessionToken)
notificationBuilder.setStyle(style)
```

### Java

```java
MediaSessionCompat session = new MediaSessionCompat(context, TAG);
PlaybackStateCompat.Builder playbackStateBuilder = new PlaybackStateCompat.Builder();
NotificationCompat.MediaStyle style = new NotificationCompat.MediaStyle();

// For this example, the media is currently paused:
int state = PlaybackStateCompat.STATE_PAUSED;
long position = 0L;
float playbackSpeed = 1f;
playbackStateBuilder.setState(state, position, playbackSpeed);

// And the user can play, skip to next or previous, and seek
long stateActions = PlaybackStateCompat.ACTION_PLAY
    | PlaybackStateCompat.ACTION_PLAY_PAUSE
    | PlaybackStateCompat.ACTION_SKIP_TO_PREVIOUS
    | PlaybackStateCompat.ACTION_SKIP_TO_NEXT
    | PlaybackStateCompat.ACTION_SEEK_TO; // adding this enables the seekbar thumb
playbackStateBuilder.setActions(stateActions);

// ... do more setup here ...

session.setPlaybackState(playbackStateBuilder.build());
style.setMediaSession(session.getSessionToken());
notificationBuilder.setStyle(style);
```

If you don't want any buttons in the previous or next slots, don't add
`ACTION_SKIP_TO_PREVIOUS` or `ACTION_SKIP_TO_NEXT`, and instead add extras to
the session:  

### Kotlin

```kotlin
session.setExtras(Bundle().apply {
    putBoolean(SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV, true)
    putBoolean(SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT, true)
})
```

### Java

```java
Bundle extras = new Bundle();
extras.putBoolean(SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV, true);
extras.putBoolean(SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT, true);
session.setExtras(extras);
```

### Add custom actions

For other actions you want to show on the media controls, you can create a
[`PlaybackStateCompat.CustomAction`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat.CustomAction)
and add that to the `PlaybackState` instead. These actions are shown in the
order they were added.  

### Kotlin

```kotlin
val customAction = PlaybackStateCompat.CustomAction.Builder(
    "com.example.MY_CUSTOM_ACTION", // action ID
    "Custom Action", // title - used as content description for the button
    R.drawable.ic_custom_action
).build()

playbackStateBuilder.addCustomAction(customAction)
```

### Java

```java
PlaybackStateCompat.CustomAction customAction = new PlaybackStateCompat.CustomAction.Builder(
        "com.example.MY_CUSTOM_ACTION", // action ID
        "Custom Action", // title - used as content description for the button
        R.drawable.ic_custom_action
).build();

playbackStateBuilder.addCustomAction(customAction);
```

### Responding to PlaybackState actions

When a user taps on a button, SystemUI uses
[`MediaController.TransportControls`](https://developer.android.com/reference/android/media/session/MediaController.TransportControls)
to send a command back to the `MediaSession`. You need to register a callback
that can respond properly to these events.  

### Kotlin

```kotlin
val callback = object: MediaSession.Callback() {
    override fun onPlay() {
        // start playback
    }

    override fun onPause() {
        // pause playback
    }

    override fun onSkipToPrevious() {
        // skip to previous
    }

    override fun onSkipToNext() {
        // skip to next
    }

    override fun onSeekTo(pos: Long) {
        // jump to position in track
    }

    override fun onCustomAction(action: String, extras: Bundle?) {
        when (action) {
            CUSTOM_ACTION_1 -> doCustomAction1(extras)
            CUSTOM_ACTION_2 -> doCustomAction2(extras)
            else -> {
                Log.w(TAG, "Unknown custom action $action")
            }
        }
    }

}

session.setCallback(callback)
```

### Java

```java
MediaSession.Callback callback = new MediaSession.Callback() {
    @Override
    public void onPlay() {
        // start playback
    }

    @Override
    public void onPause() {
        // pause playback
    }

    @Override
    public void onSkipToPrevious() {
        // skip to previous
    }

    @Override
    public void onSkipToNext() {
        // skip to next
    }

    @Override
    public void onSeekTo(long pos) {
        // jump to position in track
    }

    @Override
    public void onCustomAction(String action, Bundle extras) {
        if (action.equals(CUSTOM_ACTION_1)) {
            doCustomAction1(extras);
        } else if (action.equals(CUSTOM_ACTION_2)) {
            doCustomAction2(extras);
        } else {
            Log.w(TAG, "Unknown custom action " + action);
        }
    }
};
```

### Media Resumption

To make your player app appear in the quick setting settings area,
you must create a `MediaStyle` notification with a valid `MediaSession` token.

To display the title for the MediaStyle notification, use
`NotificationBuilder.setContentTitle()`.

To display the brand icon for the media player, use
`NotificationBuilder.setSmallIcon()`.

To support playback resumption, apps must implement a `MediaBrowserService`
and `MediaSession`. Your `MediaSession` must implement the `onPlay()` callback.

#### `MediaBrowserService` implementation

After the device boots, the system looks for the five most recently used media
apps, and provides controls that can be used to restart playing from each app.

The system attempts to contact your `MediaBrowserService` with a connection from
SystemUI. Your app must allow such connections, otherwise it cannot support
playback resumption.

Connections from SystemUI can be identified and verified using the package name
`com.android.systemui` and signature. The SystemUI is signed with the platform
signature. An example of how to check against the platform signature can be
found [in the UAMP app](https://github.com/android/uamp/blob/f60b902643407ba234a316abe91410da7c08a4af/common/src/main/java/com/example/android/uamp/media/PackageValidator.kt#L118).

In order to support playback resumption, your `MediaBrowserService` must
implement these behaviors:

- `onGetRoot()` must return a non-null root quickly. Other complex logic should
  be handled in `onLoadChildren()`

- When
  `onLoadChildren()` is called on the root media ID, the result must contain a
  [FLAG_PLAYABLE](https://developer.android.com/reference/android/media/browse/MediaBrowser.MediaItem#FLAG_PLAYABLE)
  child.

- `MediaBrowserService` should return the most recently played media item when
  they receive an
  [EXTRA_RECENT](https://developer.android.com/reference/android/service/media/MediaBrowserService.BrowserRoot#EXTRA_RECENT)
  query. The value returned should be an actual media item rather than generic
  function.

- `MediaBrowserService` must provide an appropriate
  [MediaDescription](https://developer.android.com/reference/android/media/MediaDescription) with a non-empty
  [title](https://developer.android.com/reference/android/media/MediaDescription#getTitle()) and
  [subtitle](https://developer.android.com/reference/android/media/MediaDescription#getSubtitle()).
  It should also set an
  [icon URI](https://developer.android.com/reference/android/media/MediaDescription#getIconUri())
  or an
  [icon bitmap](https://developer.android.com/reference/android/media/MediaDescription#getIconBitmap()).

The following code examples illustrate how to implement `onGetRoot()`.  

### Kotlin

```kotlin
override fun onGetRoot(
    clientPackageName: String,
    clientUid: Int,
    rootHints: Bundle?
): BrowserRoot? {
    ...
    // Verify that the specified package is SystemUI. You'll need to write your 
    // own logic to do this.
    if (isSystem(clientPackageName, clientUid)) {
        rootHints?.let {
            if (it.getBoolean(BrowserRoot.EXTRA_RECENT)) {
                // Return a tree with a single playable media item for resumption.
                val extras = Bundle().apply {
                    putBoolean(BrowserRoot.EXTRA_RECENT, true)
                }
                return BrowserRoot(MY_RECENTS_ROOT_ID, extras)
            }
        }
        // You can return your normal tree if the EXTRA_RECENT flag is not present.
        return BrowserRoot(MY_MEDIA_ROOT_ID, null)
    }
    // Return an empty tree to disallow browsing.
    return BrowserRoot(MY_EMPTY_ROOT_ID, null)
```

### Java

```java
@Override
public BrowserRoot onGetRoot(String clientPackageName, int clientUid,
    Bundle rootHints) {
    ...
    // Verify that the specified package is SystemUI. You'll need to write your
    // own logic to do this.
    if (isSystem(clientPackageName, clientUid)) {
        if (rootHints != null) {
            if (rootHints.getBoolean(BrowserRoot.EXTRA_RECENT)) {
                // Return a tree with a single playable media item for resumption.
                Bundle extras = new Bundle();
                extras.putBoolean(BrowserRoot.EXTRA_RECENT, true);
                return new BrowserRoot(MY_RECENTS_ROOT_ID, extras);
            }
        }
        // You can return your normal tree if the EXTRA_RECENT flag is not present.
        return new BrowserRoot(MY_MEDIA_ROOT_ID, null);
    }
    // Return an empty tree to disallow browsing.
    return new BrowserRoot(MY_EMPTY_ROOT_ID, null);
}
```

### Pre-Android 13 Behavior

For backward compatibility, System UI continues to provide an alternate layout
that uses notification actions for apps that don't update to target Android 13,
or that don't include `PlaybackState` information. The action buttons are
derived from the `Notification.Action` list attached to the `MediaStyle`
notification. The system displays up to five actions in the order in which they
were added. In compact mode, up to three buttons are shown, determined by the
values passed into
[`setShowActionsInCompactView()`](https://developer.android.com/reference/androidx/media3/session/MediaStyleNotificationHelper.MediaStyle#setShowActionsInCompactView(int...)).

Custom actions are placed in the order in which they were added to the
`PlaybackState`.

The following code example illustrates how to add actions to the MediaStyle
notification :  

### Kotlin

```kotlin
import androidx.core.app.NotificationCompat
import androidx.media3.session.MediaStyleNotificationHelper

var notification = NotificationCompat.Builder(context, CHANNEL_ID)
// Show controls on lock screen even when user hides sensitive content.
.setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
.setSmallIcon(R.drawable.ic_stat_player)
// Add media control buttons that invoke intents in your media service
.addAction(R.drawable.ic_prev, "Previous", prevPendingIntent) // #0
.addAction(R.drawable.ic_pause, "Pause", pausePendingIntent) // #1
.addAction(R.drawable.ic_next, "Next", nextPendingIntent) // #2
// Apply the media style template
.setStyle(MediaStyleNotificationHelper.MediaStyle(mediaSession)
.setShowActionsInCompactView(1 /* #1: pause button */))
.setContentTitle("Wonderful music")
.setContentText("My Awesome Band")
.setLargeIcon(albumArtBitmap)
.build()
```

### Java

```java
import androidx.core.app.NotificationCompat;
import androidx.media3.session.MediaStyleNotificationHelper;

NotificationCompat.Builder notification = new NotificationCompat.Builder(context, CHANNEL_ID)
// Show controls on lock screen even when user hides sensitive content.
.setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
.setSmallIcon(R.drawable.ic_stat_player)
// Add media control buttons that invoke intents in your media service
.addAction(R.drawable.ic_prev, "Previous", prevPendingIntent) // #0
.addAction(R.drawable.ic_pause, "Pause", pausePendingIntent) // #1
.addAction(R.drawable.ic_next, "Next", nextPendingIntent) // #2
// Apply the media style template
.setStyle(new MediaStyleNotificationHelper.MediaStyle(mediaSession)
.setShowActionsInCompactView(1 /* #1: pause button */))
.setContentTitle("Wonderful music")
.setContentText("My Awesome Band")
.setLargeIcon(albumArtBitmap)
.build();
```