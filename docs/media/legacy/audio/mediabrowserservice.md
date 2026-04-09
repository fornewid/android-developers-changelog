---
title: https://developer.android.com/media/legacy/audio/mediabrowserservice
url: https://developer.android.com/media/legacy/audio/mediabrowserservice
source: md.txt
---

Your app must declare the `MediaBrowserService` with an intent-filter in its manifest. You can choose your own service name; in the following example, it is "MediaPlaybackService."  

    <service android:name=".MediaPlaybackService">
      <intent-filter>
        <action android:name="android.media.browse.MediaBrowserService" />
      </intent-filter>
    </service>

<br />

**Note:** The recommended implementation of `MediaBrowserService`
is [MediaBrowserServiceCompat](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat).
which is defined in the
[media-compat support library](https://developer.android.com/topic/libraries/support-library/features.html#v4-media-compat).
Throughout this page the term "MediaBrowserService" refers to an instance of
of `MediaBrowserServiceCompat`.

<br />

## Initialize the media session

When the service receives the `onCreate()` lifecycle callback method it should perform these steps:

- Create and [initialize the media session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session#init-session)
- Set the media session callback
- Set the media session token

The `onCreate()` code below demonstrates these steps:  

### Kotlin

```kotlin
private const val MY_MEDIA_ROOT_ID = "media_root_id"
private const val MY_EMPTY_MEDIA_ROOT_ID = "empty_root_id"

class MediaPlaybackService : MediaBrowserServiceCompat() {

    private var mediaSession: MediaSessionCompat? = null
    private lateinit var stateBuilder: PlaybackStateCompat.Builder

    override fun onCreate() {
        super.onCreate()

        // Create a MediaSessionCompat
        mediaSession = MediaSessionCompat(baseContext, LOG_TAG).apply {

            // Enable callbacks from MediaButtons and TransportControls
            setFlags(MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS
                    or MediaSessionCompat.FLAG_HANDLES_TRANSPORT_CONTROLS
            )

            // Set an initial PlaybackState with ACTION_PLAY, so media buttons can start the player
            stateBuilder = PlaybackStateCompat.Builder()
                    .setActions(PlaybackStateCompat.ACTION_PLAY
                                    or PlaybackStateCompat.ACTION_PLAY_PAUSE
                    )
            setPlaybackState(stateBuilder.build())

            // MySessionCallback() has methods that handle callbacks from a media controller
            setCallback(MySessionCallback())

            // Set the session's token so that client activities can communicate with it.
            setSessionToken(sessionToken)
        }
    }
}
```

### Java

```java
public class MediaPlaybackService extends MediaBrowserServiceCompat {
    private static final String MY_MEDIA_ROOT_ID = "media_root_id";
    private static final String MY_EMPTY_MEDIA_ROOT_ID = "empty_root_id";

    private MediaSessionCompat mediaSession;
    private PlaybackStateCompat.Builder stateBuilder;

    @Override
    public void onCreate() {
        super.onCreate();

        // Create a MediaSessionCompat
        mediaSession = new MediaSessionCompat(context, LOG_TAG);

        // Enable callbacks from MediaButtons and TransportControls
        mediaSession.setFlags(
              MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS |
              MediaSessionCompat.FLAG_HANDLES_TRANSPORT_CONTROLS);

        // Set an initial PlaybackState with ACTION_PLAY, so media buttons can start the player
        stateBuilder = new PlaybackStateCompat.Builder()
                            .setActions(
                                PlaybackStateCompat.ACTION_PLAY |
                                PlaybackStateCompat.ACTION_PLAY_PAUSE);
        mediaSession.setPlaybackState(stateBuilder.build());

        // MySessionCallback() has methods that handle callbacks from a media controller
        mediaSession.setCallback(new MySessionCallback());

        // Set the session's token so that client activities can communicate with it.
        setSessionToken(mediaSession.getSessionToken());
    }
}
```

## Manage client connections

A `MediaBrowserService` has two methods that handle client connections:
[onGetRoot()](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onGetRoot(java.lang.String, int, android.os.Bundle)) controls
access to the service, and
[onLoadChildren()](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String, android.support.v4.media.MediaBrowserServiceCompat.Result<java.util.List<android.support.v4.media.MediaBrowserCompat.MediaItem>>))
provides the ability for a client to build and display a menu of the `MediaBrowserService`'s content hierarchy.

### Controlling client connections with `onGetRoot()`

The `onGetRoot()` method returns the root node of the content hierarchy. If the
method returns null, the connection is refused.

To allow clients to connect to your service and browse its media content,
onGetRoot() must return a non-null BrowserRoot which is a root ID that
represents your content hierarchy.

To allow clients to connect to your MediaSession without browsing, onGetRoot()
must still return a non-null BrowserRoot, but the root ID should represent an
empty content hierarchy.

A typical implementation of `onGetRoot()` might look like this:  

### Kotlin

```kotlin
override fun onGetRoot(
        clientPackageName: String,
        clientUid: Int,
        rootHints: Bundle?
): MediaBrowserServiceCompat.BrowserRoot {

    // (Optional) Control the level of access for the specified package name.
    // You'll need to write your own logic to do this.
    return if (allowBrowsing(clientPackageName, clientUid)) {
        // Returns a root ID that clients can use with onLoadChildren() to retrieve
        // the content hierarchy.
        MediaBrowserServiceCompat.BrowserRoot(MY_MEDIA_ROOT_ID, null)
    } else {
        // Clients can connect, but this BrowserRoot is an empty hierarchy
        // so onLoadChildren returns nothing. This disables the ability to browse for content.
        MediaBrowserServiceCompat.BrowserRoot(MY_EMPTY_MEDIA_ROOT_ID, null)
    }
}
```

### Java

```java
@Override
public BrowserRoot onGetRoot(String clientPackageName, int clientUid,
    Bundle rootHints) {

    // (Optional) Control the level of access for the specified package name.
    // You'll need to write your own logic to do this.
    if (allowBrowsing(clientPackageName, clientUid)) {
        // Returns a root ID that clients can use with onLoadChildren() to retrieve
        // the content hierarchy.
        return new BrowserRoot(MY_MEDIA_ROOT_ID, null);
    } else {
        // Clients can connect, but this BrowserRoot is an empty hierarchy
        // so onLoadChildren returns nothing. This disables the ability to browse for content.
        return new BrowserRoot(MY_EMPTY_MEDIA_ROOT_ID, null);
    }
}
```
| **Note:** The `onGetRoot()` method should quickly return a non-null value. User authentication and other slow processes should not run in `onGetRoot()`. Most business logic should be handled in the `onLoadChildren()` method, described in the next section.

In some cases, you might want to control who can connect
to your `MediaBrowserService`. One way is to use an access control list (ACL)
that specifies which connections are allowed, or alternatively enumerates
which connections should be forbidden. For an example of how to implement an ACL
that allows specific connections, see the
[PackageValidator](https://github.com/android/uamp/blob/890ad26978f30125578b2502037025d48d4304f6/common/src/main/java/com/example/android/uamp/media/PackageValidator.kt)
class in the [Universal Android Music Player](https://github.com/android/uamp)
sample app.
| **Note:** If you build an ACL, consider collecting telemetry when a forbidden client attempts to connect to the `MediaBrowserService`. Such telemetry could indicate if an allowed client inadvertently becomes forbidden due to a bug in the ACL logic.

You should consider providing different content hierarchies depending on
what type of client is making the query. In particular, Android Auto limits how
users interact with audio apps. For more information, see [Playing Audio for
Auto](https://developer.android.com/training/auto/audio/index.html#build_hierarchy). You
can look at the `clientPackageName` at connection time to determine the client
type, and return a different `BrowserRoot` depending on the client (or `rootHints`
if any).

### Communicating content with `onLoadChildren()`

After the client connects, it can traverse the content hierarchy by making repeated calls to `MediaBrowserCompat.subscribe()` to build a local representation of the UI. The `subscribe()` method sends the callback `onLoadChildren()` to the service, which returns a list of [MediaBrowser.MediaItem](https://developer.android.com/reference/android/media/browse/MediaBrowser.MediaItem) objects.

Each MediaItem has a unique ID string, which is an opaque token. When a client wants to open a submenu or play an item, it passes the ID. Your service is responsible for associating the ID with the appropriate menu node or content item.

A simple implementation of `onLoadChildren()` might look like this:  

### Kotlin

```kotlin
override fun onLoadChildren(
        parentMediaId: String,
        result: MediaBrowserServiceCompat.Result<List<MediaBrowserCompat.MediaItem>>
) {
    //  Browsing not allowed
    if (MY_EMPTY_MEDIA_ROOT_ID == parentMediaId) {
        result.sendResult(null)
        return
    }

    // Assume for example that the music catalog is already loaded/cached.

    val mediaItems = emptyList<MediaBrowserCompat.MediaItem>()

    // Check if this is the root menu:
    if (MY_MEDIA_ROOT_ID == parentMediaId) {
        // Build the MediaItem objects for the top level,
        // and put them in the mediaItems list...
    } else {
        // Examine the passed parentMediaId to see which submenu we're at,
        // and put the children of that menu in the mediaItems list...
    }
    result.sendResult(mediaItems)
}
```

### Java

```java
@Override
public void onLoadChildren(final String parentMediaId,
    final Result<List<MediaItem>> result) {

    //  Browsing not allowed
    if (TextUtils.equals(MY_EMPTY_MEDIA_ROOT_ID, parentMediaId)) {
        result.sendResult(null);
        return;
    }

    // Assume for example that the music catalog is already loaded/cached.

    List<MediaItem> mediaItems = new ArrayList<>();

    // Check if this is the root menu:
    if (MY_MEDIA_ROOT_ID.equals(parentMediaId)) {
        // Build the MediaItem objects for the top level,
        // and put them in the mediaItems list...
    } else {
        // Examine the passed parentMediaId to see which submenu we're at,
        // and put the children of that menu in the mediaItems list...
    }
    result.sendResult(mediaItems);
}
```

<br />

**Note:** `MediaItem` objects delivered by the MediaBrowserService
should not contain icon bitmaps. Use a `Uri` instead by calling
[setIconUri()](https://developer.android.com/reference/android/media/MediaDescription.Builder#setIconUri(android.net.Uri))
when you build the [MediaDescription](https://developer.android.com/reference/android/media/MediaDescription) for each item.

<br />

For an example of how to implement `onLoadChildren()`, see the [Universal Android Music Player](https://github.com/android/uamp) sample app.

## The media browser service lifecycle

The behavior of an Android [service](https://developer.android.com/guide/components/services.html) depends on whether it is *started* or *bound* to one or more clients. After a service is created, it can be started, bound, or both. In all of these states, it is fully functional and can perform the work it's designed to do. The difference is how long the service will exist. A bound service is not destroyed until all its bound clients unbind. A started service can be explicitly stopped and destroyed (assuming it is no longer bound to any clients).

When a `MediaBrowser` running in another activity connects to a `MediaBrowserService`, it binds the activity to the service, making the service bound (but not started). This default behavior is built into the `MediaBrowserServiceCompat` class.

A service that is only bound (and not started) is destroyed when all of its clients unbind. If your UI activity disconnects at this point, the service is destroyed. This isn't a problem if you haven't played any music yet. However, when playback starts, the user probably expects to continue listening even after switching apps. You don't want to destroy the player when you unbind the UI to work with another app.

For this reason, you need to be sure that the service is started when it begins
to play by calling [startService()](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)). A
started service must be explicitly stopped, whether or not it's bound. This
ensures that your player continues to perform even if the controlling UI
activity unbinds.

To stop a started service, call [Context.stopService()](https://developer.android.com/reference/android/content/Context#stopService(android.content.Intent)) or [stopSelf()](https://developer.android.com/reference/android/app/Service#stopSelf()). The system stops and destroys the service as soon as possible. However, if one or more clients are still bound to the service, the call to stop the service is delayed until all its clients unbind.

The lifecycle of the `MediaBrowserService` is controlled by the way it is created, the number of clients that are bound to it, and the calls it receives from media session callbacks. To summarize:

- The service is created when it is started in response to a media button or when an activity binds to it (after connecting via its `MediaBrowser`).
- The media session `onPlay()` callback should include code that calls `startService()`. This ensures that the service starts and continues to run, even when all UI `MediaBrowser` activities that are bound to it unbind.
- The `onStop()` callback should call `stopSelf()`. If the service was started, this stops it. In addition, the service is destroyed if there are no activities bound to it. Otherwise, the service remains bound until all its activities unbind. (If a subsequent `startService()` call is received before the service is destroyed, the pending stop is cancelled.)

The following flowchart demonstrates how the lifecycle of a service is managed. The variable counter tracks the number of bound clients:

![Service Lifecycle](https://developer.android.com/static/guide/topics/media/images/service-lifecycle.png "service lifecycle")

## Using MediaStyle notifications with a foreground service

When a service is playing, it should be running in the foreground. This lets the system know that the service is performing a useful function and should not be killed if the system is low on memory. A foreground service must display a notification so the user knows about it and can optionally control it. The `onPlay()` callback should put the service in the foreground. (Note that this is a special meaning of "foreground." While Android considers the service in the foreground for purposes of process management, to the user the player is playing in the background while some other app is visible in the "foreground" on the screen.)

When a service runs in the foreground, it must display a [notification](https://developer.android.com/develop/ui/views/notifications), ideally with one or more transport controls. The notification should also include useful information from the session's metadata.

Build and display the notification when the player starts playing. The best place to do this is inside the `MediaSessionCompat.Callback.onPlay()` method.

The example below uses the
[NotificationCompat.MediaStyle](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle),
which is designed for media apps. It shows how to build a notification that displays metadata and transport controls. The convenience method
[getController()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#getController())
allows you to create a media controller directly from your media session.  

### Kotlin

```kotlin
// Given a media session and its context (usually the component containing the session)
// Create a NotificationCompat.Builder

// Get the session's metadata
val controller = mediaSession.controller
val mediaMetadata = controller.metadata
val description = mediaMetadata.description

val builder = NotificationCompat.Builder(context, channelId).apply {
    // Add the metadata for the currently playing track
    setContentTitle(description.title)
    setContentText(description.subtitle)
    setSubText(description.description)
    setLargeIcon(description.iconBitmap)

    // Enable launching the player by clicking the notification
    setContentIntent(controller.sessionActivity)

    // Stop the service when the notification is swiped away
    setDeleteIntent(
            MediaButtonReceiver.buildMediaButtonPendingIntent(
                    context,
                    PlaybackStateCompat.ACTION_STOP
            )
    )

    // Make the transport controls visible on the lockscreen
    setVisibility(NotificationCompat.VISIBILITY_PUBLIC)

    // Add an app icon and set its accent color
    // Be careful about the color
    setSmallIcon(R.drawable.notification_icon)
    color = ContextCompat.getColor(context, R.color.primaryDark)

    // Add a pause button
    addAction(
            NotificationCompat.Action(
                    R.drawable.pause,
                    getString(R.string.pause),
                    MediaButtonReceiver.buildMediaButtonPendingIntent(
                            context,
                            PlaybackStateCompat.ACTION_PLAY_PAUSE
                    )
            )
    )

    // Take advantage of MediaStyle features
    setStyle(android.support.v4.media.app.NotificationCompat.MediaStyle()
            .setMediaSession(mediaSession.sessionToken)
            .setShowActionsInCompactView(0)

            // Add a cancel button
            .setShowCancelButton(true)
            .setCancelButtonIntent(
                    MediaButtonReceiver.buildMediaButtonPendingIntent(
                            context,
                            PlaybackStateCompat.ACTION_STOP
                    )
            )
    )
}

// Display the notification and place the service in the foreground
startForeground(id, builder.build())
```

### Java

```java
// Given a media session and its context (usually the component containing the session)
// Create a NotificationCompat.Builder

// Get the session's metadata
MediaControllerCompat controller = mediaSession.getController();
MediaMetadataCompat mediaMetadata = controller.getMetadata();
MediaDescriptionCompat description = mediaMetadata.getDescription();

NotificationCompat.Builder builder = new NotificationCompat.Builder(context, channelId);

builder
    // Add the metadata for the currently playing track
    .setContentTitle(description.getTitle())
    .setContentText(description.getSubtitle())
    .setSubText(description.getDescription())
    .setLargeIcon(description.getIconBitmap())

    // Enable launching the player by clicking the notification
    .setContentIntent(controller.getSessionActivity())

    // Stop the service when the notification is swiped away
    .setDeleteIntent(MediaButtonReceiver.buildMediaButtonPendingIntent(context,
       PlaybackStateCompat.ACTION_STOP))

    // Make the transport controls visible on the lockscreen
    .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)

    // Add an app icon and set its accent color
    // Be careful about the color
    .setSmallIcon(R.drawable.notification_icon)
    .setColor(ContextCompat.getColor(context, R.color.primaryDark))

    // Add a pause button
    .addAction(new NotificationCompat.Action(
        R.drawable.pause, getString(R.string.pause),
        MediaButtonReceiver.buildMediaButtonPendingIntent(context,
            PlaybackStateCompat.ACTION_PLAY_PAUSE)))

    // Take advantage of MediaStyle features
    .setStyle(new MediaStyle()
        .setMediaSession(mediaSession.getSessionToken())
        .setShowActionsInCompactView(0)

        // Add a cancel button
       .setShowCancelButton(true)
       .setCancelButtonIntent(MediaButtonReceiver.buildMediaButtonPendingIntent(context,
           PlaybackStateCompat.ACTION_STOP)));

// Display the notification and place the service in the foreground
startForeground(id, builder.build());
```

When using MediaStyle notifications, be aware of the behavior of these
NotificationCompat settings:

- When you use [setContentIntent()](https://developer.android.com/reference/android/app/Notification.Builder#setContentIntent(android.app.PendingIntent)), your service starts automatically when the notification is clicked, a handy feature.
- In an "untrusted" situation like the lockscreen, the default visibility for notification contents is [VISIBILITY_PRIVATE](https://developer.android.com/reference/android/app/Notification#VISIBILITY_PRIVATE). You probably want to see the transport controls on the lockscreen, so [VISIBILITY_PUBLIC](https://developer.android.com/reference/android/app/Notification#VISIBILITY_PUBLIC) is the way to go.
- Be careful when you set the background color. In an ordinary notification in Android version 5.0 or later, the color is applied only to the background of the small app icon. But for MediaStyle notifications prior to Android 7.0, the color is used for the entire notification background. Test your background color. Go gentle on the eyes and avoid extremely bright or fluorescent colors.

These settings are available only when you are using NotificationCompat.MediaStyle:

- Use [setMediaSession()](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle#setMediaSession(android.support.v4.media.session.MediaSessionCompat.Token)) to associate the notification with your session. This allows third-party apps and companion devices to access and control the session.
- Use [setShowActionsInCompactView()](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle#setShowActionsInCompactView(int...)) to add up to 3 actions to be shown in the notification's standard-sized contentView. (Here the pause button is specified.)
- In Android 5.0 (API level 21) and later you can swipe away a notification to stop the player once the service is no longer running in the foreground. You can't do this in earlier versions. To allow users to remove the notification and stop playback before Android 5.0 (API level 21), you can add a cancel button in the upper-right corner of the notification by calling [setShowCancelButton(true)](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle#setShowCancelButton(boolean)) and [setCancelButtonIntent()](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle#setCancelButtonIntent(android.app.PendingIntent)).

When you add the pause and cancel buttons, you'll need a PendingIntent to attach
to the playback action. The method [MediaButtonReceiver.buildMediaButtonPendingIntent()](https://developer.android.com/reference/androidx/media/session/MediaButtonReceiver#buildMediaButtonPendingIntent(android.content.Context, long)) does the job of converting
a PlaybackState action into a PendingIntent.