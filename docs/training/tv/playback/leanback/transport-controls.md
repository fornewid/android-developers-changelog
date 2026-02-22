---
title: https://developer.android.com/training/tv/playback/leanback/transport-controls
url: https://developer.android.com/training/tv/playback/leanback/transport-controls
source: md.txt
---

# Use transport controls

Build better with Compose  
Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.  
[Compose for TV →](https://developer.android.com/training/tv/playback/compose)  
![](https://developer.android.com/static/images/android-compose-tv-logo.png)
| **Warning:** The Leanback library is deprecated. Use[Jetpack Compose for Android TV OS](https://developer.android.com/training/tv/playback/compose)instead.

The Leanback UI toolkit has playback controls that provide an improved user experience. For video apps, the transport controls support video scrubbing with the forward and backward controls. While scrubbing the display shows thumbnails to help navigate through the video.

The library includes abstract classes as well as prebuilt, out-of-the-box implementations that provide more granular control for developers. Using the prebuilt implementations, you can quickly build a feature-rich app without much coding. If you need more customization, you can extend any of the library's prebuilt components.

## Controls and player

The Leanback UI toolkit separates the transport controls UI from the player that plays back video. This is accomplished with two components: a*playback support fragment* for displaying the transport controls (and optionally the video) and a*player adapter*to encapsulate a media player.

### Playback fragment

Your app's UI Activity should use a[PlaybackSupportFragment](https://developer.android.com/reference/androidx/leanback/app/PlaybackSupportFragment)or a[VideoSupportFragment](https://developer.android.com/reference/androidx/leanback/app/VideoSupportFragment). Both contain the leanback transport controls:

- A[PlaybackSupportFragment](https://developer.android.com/reference/androidx/leanback/app/PlaybackSupportFragment)animates its transport controls to hide/show them as needed.
- A[VideoSupportFragment](https://developer.android.com/reference/androidx/leanback/app/VideoSupportFragment)extends`PlaybackSupportFragment`and has a[SurfaceView](https://developer.android.com/reference/android/view/SurfaceView)to render video.

You can customize a fragment's[ObjectAdapter](https://developer.android.com/reference/androidx/leanback/widget/ObjectAdapter)to enhance the UI. For example, use[setAdapter()](https://developer.android.com/reference/androidx/leanback/app/PlaybackSupportFragment#setAdapter(androidx.leanback.widget.ObjectAdapter))to add a "related videos" row.

### PlayerAdapter

[PlayerAdapter](https://developer.android.com/reference/androidx/leanback/media/PlayerAdapter)is an abstract class that controls the underlying media player. Developers can choose the pre-built[MediaPlayerAdapter](https://developer.android.com/reference/androidx/leanback/media/MediaPlayerAdapter)implementation, or write their own implementation of this class.

## Glueing the pieces together

You must use some "control glue" to connect the playback fragment to the player. The leanback library provides two kinds of glue:

- [PlaybackBannerControlGlue](https://developer.android.com/reference/androidx/leanback/media/PlaybackBannerControlGlue)draws the transport controls in the playback fragment in the "old style", placing them inside an opaque background. (`PlaybackBannerControlGlue`replaces[PlaybackControlGlue](https://developer.android.com/reference/androidx/leanback/media/PlaybackControlGlue), which has been deprecated.)
- [PlaybackTransportControlGlue](https://developer.android.com/reference/androidx/leanback/media/PlaybackTransportControlGlue)uses "new style" controls with a transparent background.

![leanback transport control glue](https://developer.android.com/training/tv/playback/images/glue_side_by_side.png)

If you want your app to support video scrubbing you must use[PlaybackTransportControlGlue](https://developer.android.com/reference/androidx/leanback/media/PlaybackTransportControlGlue).

You also need to specify a "glue host" that binds the glue to the playback fragment, draws the transport controls in the UI and maintains their state, and passes transport control events back to the glue. The host must match the playback fragment type. Use[PlaybackSupportFragmentGlueHost](https://developer.android.com/reference/androidx/leanback/app/PlaybackSupportFragmentGlueHost)with a`PlaybackFragment`, and[VideoSupportFragmentGlueHost](https://developer.android.com/reference/androidx/leanback/app/VideoSupportFragmentGlueHost)with a`VideoFragment`.

Here's an illustration showing how the pieces of a leanback transport control fit together:

![leanback transport control glue](https://developer.android.com/training/tv/playback/images/leanback-control-glue.png)

The code that glues your app together should be inside the`PlaybackSupportFragment`or`VideoSupportFragment`that defines the UI.

In the following example, the app constructs an instance of`PlaybackTransportControlGlue`, naming it`playerGlue`, and connects its`VideoSupportFragment`to a newly-created`MediaPlayerAdapter`. Since this is a`VideoSupportFragment`the setup code calls`setHost()`to attach a`VideoSupportFragmentGlueHost`to`playerGlue`. The code is included inside the class that extends the`VideoSupportFragment`.  

### Kotlin

```kotlin
class MyVideoFragment : VideoSupportFragment() {

  fun onCreate(savedInstanceState: Bundle) {
      super.onCreate(savedInstanceState)
      val playerGlue = PlaybackTransportControlGlue(getActivity(),
          MediaPlayerAdapter(getActivity()))
      playerGlue.setHost(VideoSupportFragmentGlueHost(this))
      playerGlue.addPlayerCallback(object : PlaybackGlue.PlayerCallback() {
          override fun onPreparedStateChanged(glue: PlaybackGlue) {
              if (glue.isPrepared()) {
                  playerGlue.seekProvider = MySeekProvider()
                  playerGlue.play()
              }
          }
      })
      playerGlue.setSubtitle("Leanback artist")
      playerGlue.setTitle("Leanback team at work")
      val uriPath = "android.resource://com.example.android.leanback/raw/video"
      playerGlue.getPlayerAdapter().setDataSource(Uri.parse(uriPath))
  }
}
```

### Java

```java
public class MyVideoFragment extends VideoSupportFragment {

  @Override
  public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      final PlaybackTransportControlGlue<MediaPlayerAdapter> playerGlue =
              new PlaybackTransportControlGlue(getActivity(),
                      new MediaPlayerAdapter(getActivity()));
      playerGlue.setHost(new VideoSupportFragmentGlueHost(this));
      playerGlue.addPlayerCallback(new PlaybackGlue.PlayerCallback() {
          @Override
          public void onPreparedStateChanged(PlaybackGlue glue) {
              if (glue.isPrepared()) {
                  playerGlue.setSeekProvider(new MySeekProvider());
                  playerGlue.play();
              }
          }
      });
      playerGlue.setSubtitle("Leanback artist");
      playerGlue.setTitle("Leanback team at work");
      String uriPath = "android.resource://com.example.android.leanback/raw/video";
      playerGlue.getPlayerAdapter().setDataSource(Uri.parse(uriPath));
  }
}
```

Note that the setup code also defines a[PlayerAdapter.Callback](https://developer.android.com/reference/androidx/leanback/media/PlayerAdapter.Callback)to handle events from the media player.

## Customizing the UI glue

You can customize the`PlaybackBannerControlGlue`and`PlaybackTransportControlGlue`to change the[PlaybackControlsRow](https://developer.android.com/reference/androidx/leanback/widget/PlaybackControlsRow).

### Customizing the title and description

To customize the title and description at the top of the playback controls, override[onCreateRowPresenter()](https://developer.android.com/reference/androidx/leanback/media/PlaybackTransportControlGlue#onCreateRowPresenter()):  

### Kotlin

```kotlin
override fun onCreateRowPresenter(): PlaybackRowPresenter {
    return super.onCreateRowPresenter().apply {
        (this as? PlaybackTransportRowPresenter)
                ?.setDescriptionPresenter(MyCustomDescriptionPresenter())
    }
}
```

### Java

```java
@Override
protected PlaybackRowPresenter onCreateRowPresenter() {
  PlaybackTransportRowPresenter presenter = (PlaybackTransportRowPresenter) super.onCreateRowPresenter();
  presenter.setDescriptionPresenter(new MyCustomDescriptionPresenter());
  return presenter;
}
```

### Adding controls

The control glue displays controls for actions in a[PlaybackControlsRow](https://developer.android.com/reference/androidx/leanback/widget/PlaybackControlsRow).

The actions in the`PlaybackControlsRow`are assigned to two groups:*primary actions* and*secondary actions*. Controls for the primary group appear above the seek bar and controls for the secondary group appear below the seek bar. Initially, there is only a single primary action for the play/pause button, and no secondary actions.

You can add actions to the primary and secondary groups by overriding[onCreatePrimaryActions()](https://developer.android.com/reference/androidx/leanback/media/PlaybackControlGlue#onCreatePrimaryActions(androidx.leanback.widget.SparseArrayObjectAdapter))and[onCreateSecondaryActions()](https://developer.android.com/reference/androidx/leanback/media/PlaybackControlGlue#onCreateSecondaryActions(androidx.leanback.widget.ArrayObjectAdapter)).  

### Kotlin

```kotlin
private lateinit var repeatAction: PlaybackControlsRow.RepeatAction
private lateinit var pipAction: PlaybackControlsRow.PictureInPictureAction
private lateinit var thumbsUpAction: PlaybackControlsRow.ThumbsUpAction
private lateinit var thumbsDownAction: PlaybackControlsRow.ThumbsDownAction
private lateinit var skipPreviousAction: PlaybackControlsRow.SkipPreviousAction
private lateinit var skipNextAction: PlaybackControlsRow.SkipNextAction
private lateinit var fastForwardAction: PlaybackControlsRow.FastForwardAction
private lateinit var rewindAction: PlaybackControlsRow.RewindAction

override fun onCreatePrimaryActions(primaryActionsAdapter: ArrayObjectAdapter) {
    // Order matters, super.onCreatePrimaryActions() will create the play / pause action.
    // Will display as follows:
    // play/pause, previous, rewind, fast forward, next
    //   > /||      |<        <<        >>         >|
    super.onCreatePrimaryActions(primaryActionsAdapter)
    primaryActionsAdapter.apply {
        add(skipPreviousAction)
        add(rewindAction)
        add(fastForwardAction)
        add(skipNextAction)
    }
}

override fun onCreateSecondaryActions(adapter: ArrayObjectAdapter?) {
    super.onCreateSecondaryActions(adapter)
    adapter?.apply {
        add(thumbsDownAction)
        add(thumbsUpAction)
    }
}
```

### Java

```java
private PlaybackControlsRow.RepeatAction repeatAction;
private PlaybackControlsRow.PictureInPictureAction pipAction;
private PlaybackControlsRow.ThumbsUpAction thumbsUpAction;
private PlaybackControlsRow.ThumbsDownAction thumbsDownAction;
private PlaybackControlsRow.SkipPreviousAction skipPreviousAction;
private PlaybackControlsRow.SkipNextAction skipNextAction;
private PlaybackControlsRow.FastForwardAction fastForwardAction;
private PlaybackControlsRow.RewindAction rewindAction;

@Override
protected void onCreatePrimaryActions(ArrayObjectAdapter primaryActionsAdapter) {
    // Order matters, super.onCreatePrimaryActions() will create the play / pause action.
    // Will display as follows:
    // play/pause, previous, rewind, fast forward, next
    //   > /||      |<        <<        >>         >|
    super.onCreatePrimaryActions(primaryActionsAdapter);
    primaryActionsAdapter.add(skipPreviousAction);
    primaryActionsAdapter.add(rewindAction);
    primaryActionsAdapter.add(fastForwardAction);
    primaryActionsAdapter.add(skipNextAction);
}

@Override
protected void onCreateSecondaryActions(ArrayObjectAdapter adapter) {
    super.onCreateSecondaryActions(adapter);
    adapter.add(thumbsDownAction);
    adapter.add(thumbsUpAction);
}
```

You must override[onActionClicked()](https://developer.android.com/reference/androidx/leanback/widget/OnActionClickedListener#onActionClicked(androidx.leanback.widget.Action))to handle the new actions.  

### Kotlin

```kotlin
override fun onActionClicked(action: Action) {
    when(action) {
        rewindAction -> {
            // Handle Rewind
        }
        fastForwardAction -> {
            // Handle FastForward
        }
        thumbsDownAction -> {
            // Handle ThumbsDown
        }
        thumbsUpAction -> {
            // Handle ThumbsUp
        }
        else ->
            // The superclass handles play/pause and delegates next/previous actions to abstract methods,
            // so those two methods should be overridden rather than handling the actions here.
            super.onActionClicked(action)
    }
}

override fun next() {
    // Skip to next item in playlist.
}

override fun previous() {
    // Skip to previous item in playlist.
}
```

### Java

```java
@Override
public void onActionClicked(Action action) {
    if (action == rewindAction) {
        // Handle Rewind
    } else if (action == fastForwardAction ) {
        // Handle FastForward
    } else if (action == thumbsDownAction) {
        // Handle ThumbsDown
    } else if (action == thumbsUpAction) {
        // Handle ThumbsUp
    } else {
        // The superclass handles play/pause and delegates next/previous actions to abstract methods,
        // so those two methods should be overridden rather than handling the actions here.
        super.onActionClicked(action);
    }
}

@Override
public void next() {
    // Skip to next item in playlist.
}

@Override
public void previous() {
    // Skip to previous item in playlist.
}
```

In special cases, you might want to implement your own[PlaybackTransportRowPresenter](https://developer.android.com/reference/androidx/leanback/widget/PlaybackTransportRowPresenter)to render custom controls and respond to seek actions using the[PlaybackSeekUi](https://developer.android.com/reference/androidx/leanback/widget/PlaybackSeekUi).

## Video scrubbing

If your app uses a`VideoSupportFragment`and you want to support video scrubbing.

![scrubbing](https://developer.android.com/training/tv/playback/images/leanback-scrubbing.gif)

You need to provide an implementation of[PlaybackSeekDataProvider](https://developer.android.com/reference/androidx/leanback/widget/PlaybackSeekDataProvider). This component provides the video thumbnails used when scrolling. You must implement your own provider by extending[PlaybackSeekDataProvider](https://developer.android.com/reference/androidx/leanback/widget/PlaybackSeekDataProvider). See the example in the[Leanback Showcase app](https://github.com/android/tv-samples/tree/main/LeanbackShowcase). .