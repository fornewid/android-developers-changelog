---
title: Connect to a media app  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/session/connect-to-media-app
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Connect to a media app Stay organized with collections Save and categorize content based on your preferences.



There are two ways to connect to a Media app:

1. `MediaController`
2. `MediaBrowser`

## `MediaController`

A media controller interacts with a media session to query and control a media
app's playback. In Media3, the [`MediaController`](/reference/kotlin/androidx/media3/session/MediaController)
API implements the `Player` interface. Examples of client apps that use a media
controller include:

* [Android system media controls](/media/implement/surfaces/mobile)
* Android Wear OS companion app
* [Android Auto and Automotive OS](/training/cars/media)
* Voice assistants, like [Google Assistant](/media/implement/assistant)
* The [Media Controller Test app](/media/optimize/mct)

A media controller can also be useful within a media app, for example if the
player and media session live in a `Service` separate from the `Activity` or
`Fragment` with the UI.

### Create a `MediaController`

To create a `MediaController`, start by creating a `SessionToken` for the
corresponding `MediaSession`. The `onStart()` method of your `Activity` or
`Fragment` can be a good place for this.

### Kotlin

```
val sessionToken = SessionToken(context, ComponentName(context, PlaybackService::class.java))

ConnectToMediaApp.kt
```

### Java

```
SessionToken sessionToken =
    new SessionToken(context, new ComponentName(context, PlaybackService.class));

ConnectToMediaApp.java
```

Using this `SessionToken` to then build a `MediaController` connects the
controller to the given session. This takes place asynchronously, so you should
listen for the result and use it when available.

### Kotlin

```
val controllerFuture = MediaController.Builder(context, sessionToken).buildAsync()
controllerFuture.addListener(
  {
    // MediaController is available here with controllerFuture.get()
  },
  MoreExecutors.directExecutor(),
)

ConnectToMediaApp.kt
```

### Java

```
ListenableFuture<MediaController> controllerFuture =
    new MediaController.Builder(context, sessionToken).buildAsync();
controllerFuture.addListener(
    () -> {
      // MediaController is available here with controllerFuture.get()
    },
    MoreExecutors.directExecutor());

ConnectToMediaApp.java
```

**Note:** Use `ContextCompat.getMainExecutor()` instead of `MoreExecutors.directExecutor()`
in case you run your service in another process than the UI.**Note:** Apps targeting SDK level 30 or higher must include a `<queries>` element
in their manifest to connect to a different app's `MediaSessionService` (or
similar component). Refer to the [package visibility](/training/package-visibility)
guide for further details.

### Use a `MediaController`

`MediaController` implements the `Player` interface, so you can use the commands
defined in the interface to control playback of the connected `MediaSession`.
This is to say that calling `play()` on a `MediaController` will send the
command to the connected `MediaSession`, which will subsequently delegate the
command to its underlying `Player`.

**Tip:** A media controller implements the `Player` interface, and as such you can
use it within your UI as a `Player`.

You can add a `Player.Listener` to the controller to listen for changes in the
`Player` state. Refer to the [Player events](/guide/topics/media/exoplayer/listening-to-player-events) guide for more details on using a
`Player.Listener`.

The `MediaController.Listener` interface defines additional callbacks for events
and custom commands from the connected `MediaSession`. Examples are
[`onCustomCommand()`](/reference/kotlin/androidx/media3/session/MediaController.Listener#onCustomCommand(androidx.media3.session.MediaController,androidx.media3.session.SessionCommand,android.os.Bundle)) when the session sends a custom command,
[`onAvailableSessionCommandsChanged()`](/reference/kotlin/androidx/media3/session/MediaController.Listener#onAvailableSessionCommandsChanged(androidx.media3.session.MediaController,androidx.media3.session.SessionCommands)) when the session changes the available
session commands or [`onDisconnected()`](/reference/kotlin/androidx/media3/session/MediaController.Listener#onDisconnected(androidx.media3.session.MediaController)) when the controller is disconnected
from the session.

A `MediaController.Listener` can be set when building the controller with a
`Builder`:

### Kotlin

```
val controllerFuture =
  MediaController.Builder(context, sessionToken)
    .setListener(
      object : MediaController.Listener {
        override fun onCustomCommand(
          controller: MediaController,
          command: SessionCommand,
          args: Bundle,
        ): ListenableFuture<SessionResult> {
          // Handle custom command.
          return Futures.immediateFuture(SessionResult(SessionResult.RESULT_SUCCESS))
        }

        override fun onDisconnected(controller: MediaController) {
          // Handle disconnection.
        }
      }
    )
    .buildAsync()

ConnectToMediaApp.kt
```

### Java

```
ListenableFuture<MediaController> controllerFuture =
    new MediaController.Builder(context, sessionToken)
        .setListener(
            new MediaController.Listener() {
              @Override
              public ListenableFuture<SessionResult> onCustomCommand(
                  MediaController controller, SessionCommand command, Bundle args) {
                // Handle custom command.
                return Futures.immediateFuture(new SessionResult(SessionResult.RESULT_SUCCESS));
              }

              @Override
              public void onDisconnected(MediaController controller) {
                // Handle disconnection.
              }
            })
        .buildAsync();

ConnectToMediaApp.java
```

As with other components, remember to release the `MediaController` when it is
no longer needed, such as in the `onStop()` method of an `Activity` or
`Fragment`.

### Kotlin

```
MediaController.releaseFuture(controllerFuture)

ConnectToMediaApp.kt
```

### Java

```
MediaController.releaseFuture(controllerFuture);

ConnectToMediaApp.java
```

Releasing the controller will still deliver all pending commands sent to the
session and only unbind from the session service either once these commands have
been handled or after a timeout period, whichever occurs first.

## `MediaBrowser`

A `MediaBrowser` builds on top of the capabilities offered by a
`MediaController` to also enable browsing the media library offered by a media
app's `MediaLibraryService`.

### Create a `MediaBrowser`

### Kotlin

```
val browserFuture = MediaBrowser.Builder(context, sessionToken).buildAsync()
browserFuture.addListener(
  {
    // MediaBrowser is available here with browserFuture.get()
  },
  MoreExecutors.directExecutor(),
)

ConnectToMediaApp.kt
```

### Java

```
ListenableFuture<MediaBrowser> browserFuture =
    new MediaBrowser.Builder(context, sessionToken).buildAsync();
browserFuture.addListener(
    () -> {
      // MediaBrowser is available here with browserFuture.get()
    },
    MoreExecutors.directExecutor());

ConnectToMediaApp.java
```

### Use a `MediaBrowser`

To start browsing the media app's content library, first retrieve the root node
with `getLibraryRoot()`:

### Kotlin

```
// Get the library root to start browsing the library tree.
val rootFuture = mediaBrowser.getLibraryRoot(/* params= */ null)
rootFuture.addListener(
  {
    // Root node MediaItem is available here with rootFuture.get().value
  },
  MoreExecutors.directExecutor(),
)

ConnectToMediaApp.kt
```

### Java

```
// Get the library root to start browsing the library tree.
ListenableFuture<LibraryResult<MediaItem>> rootFuture =
    mediaBrowser.getLibraryRoot(/* params= */ null);
rootFuture.addListener(
    () -> {
      // Root node MediaItem is available here with rootFuture.get().value
    },
    MoreExecutors.directExecutor());

ConnectToMediaApp.java
```

You can then navigate through the media library by retrieving the children of a
`MediaItem` in the library with `getChildren()`. For example, to retrieve the
children of the root node `MediaItem`:

### Kotlin

```
// Get the library root to start browsing the library tree.
val childrenFuture = mediaBrowser.getChildren(rootMediaItem.mediaId, 0, Int.MAX_VALUE, null)
childrenFuture.addListener(
  {
    // List of children MediaItem nodes is available here with
    // childrenFuture.get().value
  },
  MoreExecutors.directExecutor(),
)

ConnectToMediaApp.kt
```

### Java

```
ListenableFuture<LibraryResult<ImmutableList<MediaItem>>> childrenFuture =
    mediaBrowser.getChildren(rootMediaItem.mediaId, 0, Integer.MAX_VALUE, null);
childrenFuture.addListener(
    () -> {
      // List of children MediaItem nodes is available here with
      // childrenFuture.get().value
    },
    MoreExecutors.directExecutor());

ConnectToMediaApp.java
```

## Display playback controls for another media app

When displaying UI controls with buttons for another media app, it's important
to follow the declared [media button preferences](/media/media3/session/control-playback#commands) of that
app.

To resolve the app's preferences with the constraints and requirements of your
UI, use `CommandButton.DisplayConstraints`. You can define the limits and
restrictions of your UI can do, and the [`resolve`](/reference/kotlin/androidx/media3/session/CommandButton.DisplayConstraints#resolve(java.util.List%3Candroidx.media3.session.CommandButton%3E,androidx.media3.common.Player)) method
provides a definite list of buttons to display with their icon, position and
intended action. If a user clicks one of these buttons, you can use
`CommandButton.executeAction` to trigger the associated action in the media
app.

### Kotlin

```
// Get media button preferences from media app
val mediaButtonPreferences = controller.getMediaButtonPreferences()
// Declare constraints of UI (example: limit overflow button to one)
val displayConstraints =
  DisplayConstraints.Builder().setMaxButtonsForSlot(CommandButton.SLOT_OVERFLOW, 1).build()
// Resolve media app preferences with constraints
val resolvedButtons = displayConstraints.resolve(mediaButtonPreferences, controller)
// Display buttons in UI
for (button in resolvedButtons) {
  generateUiButton(
    uiPosition = button.slots[0],
    icon = getIconRes(button.icon),
    onClick = { button.executeAction(controller) },
  )
}

ConnectToMediaApp.kt
```

### Java

```
// Get media button preferences from media app
List<CommandButton> mediaButtonPreferences = controller.getMediaButtonPreferences();
// Declare constraints of UI (example: limit overflow button to one)
DisplayConstraints displayConstraints =
    new DisplayConstraints.Builder()
        .setMaxButtonsForSlot(CommandButton.SLOT_OVERFLOW, 1)
        .build();
// Resolve media app preferences with constraints
List<CommandButton> resolvedButtons =
    displayConstraints.resolve(mediaButtonPreferences, controller);
// Display buttons in UI
for (CommandButton button : resolvedButtons) {
  generateUiButton(
      /* uiPosition= */ button.slots.get(0),
      /* icon= */ getIconRes(button.icon),
      /* onClick= */ () -> button.executeAction(controller));
}

ConnectToMediaApp.java
```