---
title: Building a media browser client  |  Legacy media APIs  |  Android Developers
url: https://developer.android.com/media/legacy/audio/mediabrowser
source: html-scrape
---

These guides discuss the MediaCompat APIs, which are no longer updated. We strongly recommend using the [Jetpack Media3](/guide/topics/media/media3) library instead.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Building a media browser client Stay organized with collections Save and categorize content based on your preferences.



To complete the client/server design, you must build an activity component that contains your UI code, an associated MediaController, and a MediaBrowser.

The MediaBrowser performs two important functions: It connects to a MediaBrowserService, and upon connecting it creates the MediaController for your UI.

**Note:** The recommended implementation of MediaBrowser
is `MediaBrowserCompat`,
which is defined in the
[Media-Compat support library](https://developer.android.com/topic/libraries/support-library/features.html#v4-media-compat).
Throughout this page the term "MediaBrowser" refers to an instance
of MediaBrowserCompat.

## Connect to the MediaBrowserService

When your client activity is created, it connects to the MediaBrowserService. There's a little handshake and dance involved.
Modify the activity's lifecycle callbacks as follows:

* `onCreate()` constructs a MediaBrowserCompat. Pass in the name of your MediaBrowserService and the MediaBrowserCompat.ConnectionCallback that you've defined.
* `onStart()` connects to the MediaBrowserService. Here's where the magic of MediaBrowserCompat.ConnectionCallback comes in. If the connection is successful, the onConnect() callback creates the media controller, links it to the media session, links your UI controls to the MediaController, and registers the controller to receive callbacks from the media session.
* `onResume()` sets the audio stream so your app responds to the volume control on the device.
* `onStop()` disconnects your MediaBrowser and unregisters the MediaController.Callback when your activity stops.

### Kotlin

```
class MediaPlayerActivity : AppCompatActivity() {

    private lateinit var mediaBrowser: MediaBrowserCompat

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // ...
        // Create MediaBrowserServiceCompat
        mediaBrowser = MediaBrowserCompat(
                this,
                ComponentName(this, MediaPlaybackService::class.java),
                connectionCallbacks,
                null // optional Bundle
        )
    }

    public override fun onStart() {
        super.onStart()
        mediaBrowser.connect()
    }

    public override fun onResume() {
        super.onResume()
        volumeControlStream = AudioManager.STREAM_MUSIC
    }

    public override fun onStop() {
        super.onStop()
        // (see "stay in sync with the MediaSession")
        MediaControllerCompat.getMediaController(this)?.unregisterCallback(controllerCallback)
        mediaBrowser.disconnect()
    }
}
```

### Java

```
public class MediaPlayerActivity extends AppCompatActivity {
  private MediaBrowserCompat mediaBrowser;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // ...
    // Create MediaBrowserServiceCompat
    mediaBrowser = new MediaBrowserCompat(this,
      new ComponentName(this, MediaPlaybackService.class),
        connectionCallbacks,
        null); // optional Bundle
  }

  @Override
  public void onStart() {
    super.onStart();
    mediaBrowser.connect();
  }

  @Override
  public void onResume() {
    super.onResume();
    setVolumeControlStream(AudioManager.STREAM_MUSIC);
  }

  @Override
  public void onStop() {
    super.onStop();
    // (see "stay in sync with the MediaSession")
    if (MediaControllerCompat.getMediaController(MediaPlayerActivity.this) != null) {
      MediaControllerCompat.getMediaController(MediaPlayerActivity.this).unregisterCallback(controllerCallback);
    }
    mediaBrowser.disconnect();

  }
}
```

## Customize MediaBrowserCompat.ConnectionCallback

When your activity constructs MediaBrowserCompat, you must create an instance of ConnectionCallback. Modify its `onConnected()` method to retrieve the media session token from the MediaBrowserService and use the token to create a MediaControllerCompat.

Use the convenience method
`MediaControllerCompat.setMediaController()`
to save a link to the controller. This enables handling of [media buttons](/guide/topics/media-apps/mediabuttons). It also allows you to call
`MediaControllerCompat.getMediaController()` to retrieve the controller when building the transport controls.

The following code sample shows how to modify the `onConnected()` method.

### Kotlin

```
private val connectionCallbacks = object : MediaBrowserCompat.ConnectionCallback() {
    override fun onConnected() {

        // Get the token for the MediaSession
        mediaBrowser.sessionToken.also { token ->

            // Create a MediaControllerCompat
            val mediaController = MediaControllerCompat(
                    this@MediaPlayerActivity, // Context
                    token
            )

            // Save the controller
            MediaControllerCompat.setMediaController(this@MediaPlayerActivity, mediaController)
        }

        // Finish building the UI
        buildTransportControls()
    }

    override fun onConnectionSuspended() {
        // The Service has crashed. Disable transport controls until it automatically reconnects
    }

    override fun onConnectionFailed() {
        // The Service has refused our connection
    }
}
```

### Java

```
private final MediaBrowserCompat.ConnectionCallback connectionCallbacks =
  new MediaBrowserCompat.ConnectionCallback() {
    @Override
    public void onConnected() {

      // Get the token for the MediaSession
      MediaSessionCompat.Token token = mediaBrowser.getSessionToken();

      // Create a MediaControllerCompat
      MediaControllerCompat mediaController =
        new MediaControllerCompat(MediaPlayerActivity.this, // Context
        token);

      // Save the controller
      MediaControllerCompat.setMediaController(MediaPlayerActivity.this, mediaController);

      // Finish building the UI
      buildTransportControls();
    }

    @Override
    public void onConnectionSuspended() {
      // The Service has crashed. Disable transport controls until it automatically reconnects
    }

    @Override
    public void onConnectionFailed() {
      // The Service has refused our connection
    }
  };
```

## Connect your UI to the media controller

In the ConnectionCallback sample code above, includes a call to `buildTransportControls()` to flesh out your UI. You'll need to set onClickListeners for the UI elements that control the player. Choose the appropriate
`MediaControllerCompat.TransportControls` method for each one.

Your code will look something like this, with an onClickListener for each button:

### Kotlin

```
fun buildTransportControls() {
    val mediaController = MediaControllerCompat.getMediaController(this@MediaPlayerActivity)
    // Grab the view for the play/pause button
    playPause = findViewById<ImageView>(R.id.play_pause).apply {
        setOnClickListener {
            // Since this is a play/pause button, you'll need to test the current state
            // and choose the action accordingly

            val pbState = mediaController.playbackState.state
            if (pbState == PlaybackStateCompat.STATE_PLAYING) {
                mediaController.transportControls.pause()
            } else {
                mediaController.transportControls.play()
            }
        }
    }

    // Display the initial state
    val metadata = mediaController.metadata
    val pbState = mediaController.playbackState

    // Register a Callback to stay in sync
    mediaController.registerCallback(controllerCallback)
}
```

### Java

```
void buildTransportControls()
{
  // Grab the view for the play/pause button
  playPause = (ImageView) findViewById(R.id.play_pause);

  // Attach a listener to the button
  playPause.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
      // Since this is a play/pause button, you'll need to test the current state
      // and choose the action accordingly

      int pbState = MediaControllerCompat.getMediaController(MediaPlayerActivity.this).getPlaybackState().getState();
      if (pbState == PlaybackStateCompat.STATE_PLAYING) {
        MediaControllerCompat.getMediaController(MediaPlayerActivity.this).getTransportControls().pause();
      } else {
        MediaControllerCompat.getMediaController(MediaPlayerActivity.this).getTransportControls().play();
      }
  });

  MediaControllerCompat mediaController = MediaControllerCompat.getMediaController(MediaPlayerActivity.this);

  // Display the initial state
  MediaMetadataCompat metadata = mediaController.getMetadata();
  PlaybackStateCompat pbState = mediaController.getPlaybackState();

  // Register a Callback to stay in sync
  mediaController.registerCallback(controllerCallback);
}
}
```

The TransportControls methods send callbacks to your service's media session. Make sure you've defined a corresponding
`MediaSessionCompat.Callback` method for each control.

## Stay in sync with the media session

The UI should display the current state of the media session, as described by its PlaybackState and Metadata. When you create the transport controls, you can grab the current state of the session, display it in your UI, and enable and disable transport controls based on the state and its available actions.

To receive callbacks from the media session every time its state or metadata changes, define a
`MediaControllerCompat.Callback`, with these two methods:

### Kotlin

```
private var controllerCallback = object : MediaControllerCompat.Callback() {

    override fun onMetadataChanged(metadata: MediaMetadataCompat?) {}

    override fun onPlaybackStateChanged(state: PlaybackStateCompat?) {}
}
```

### Java

```
MediaControllerCompat.Callback controllerCallback =
  new MediaControllerCompat.Callback() {
    @Override
    public void onMetadataChanged(MediaMetadataCompat metadata) {}

    @Override
    public void onPlaybackStateChanged(PlaybackStateCompat state) {}
  };
```

Register the callback when you build the transport controls (see the `buildTransportControls()` method) and unregister it when the activity stops (in the activity's `onStop()` lifecycle method).

## Disconnect when the media session is destroyed

If the media session becomes invalid, the
[`onSessionDestroyed()`](/reference/android/support/v4/media/session/MediaControllerCompat.Callback#onSessionDestroyed())
callback is issued. When that happens, the session cannot become functional
again within the lifetime of the `MediaBrowserService`. Although functions
related to `MediaBrowser` might continue to work, a user cannot view or control
playback from a destroyed media session, which will likely diminish the value of
your application.

Therefore, when the session is destroyed, you *must* disconnect from the
`MediaBrowserService` by calling
[`disconnect()`](/reference/android/support/v4/media/MediaBrowserCompat#disconnect()).
This ensures that the browser service has no bound clients and
[can be destroyed by the
OS](/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#service-lifecycle).
If you need to reconnect to the `MediaBrowserService` later (for example, if
your application wants to maintain a persistent connection to the media app),
create a *new* instance of `MediaBrowser` rather than reusing the old one.

The following code snippet demonstrates a callback implementation that
disconnects from the browser service when the media session is destroyed:

### Kotlin

```
private var controllerCallback = object : MediaControllerCompat.Callback() {
    override fun onSessionDestroyed() {
      mediaBrowser.disconnect()
      // maybe schedule a reconnection using a new MediaBrowser instance
    }
}
```

### Java

```
MediaControllerCompat.Callback controllerCallback =
  new MediaControllerCompat.Callback() {
    @Override
    public void onSessionDestroyed() {
      mediaBrowser.disconnect();
      // maybe schedule a reconnection using a new MediaBrowser instance
    }
  };
```