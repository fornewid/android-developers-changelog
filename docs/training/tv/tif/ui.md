---
title: Manage TV user interaction  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/tif/ui
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Manage TV user interaction Stay organized with collections Save and categorize content based on your preferences.



In the live TV experience, the user changes channels and is presented with
channel and program information briefly before the information disappears. Other types of information,
such as messages ("DO NOT ATTEMPT AT HOME"), subtitles, or ads may need to persist. As with any TV
app, such information should not interfere with the program content playing on the screen.

![](/static/images/tv/do-not-attempt.png)

**Figure 1.** An overlay message in a live TV app.

Also consider whether certain program content should be presented, given the
content's rating and parental control settings, and how your app behaves and informs the user when
content is blocked or unavailable. This lesson describes how to develop your TV input's user
experience for these considerations.

Try the [TV Input Service](https://github.com/googlesamples/androidtv-sample-inputs) sample app.

## Integrate player with surface

Your TV input must render video onto a `Surface` object, which is passed by
the `TvInputService.Session.onSetSurface()`
method. Here's an example of how to use a `MediaPlayer` instance for playing
content in the `Surface` object:

### Kotlin

```
override fun onSetSurface(surface: Surface?): Boolean {
    player?.setSurface(surface)
    mSurface = surface
    return true
}

override fun onSetStreamVolume(volume: Float) {
    player?.setVolume(volume, volume)
    mVolume = volume
}
```

### Java

```
@Override
public boolean onSetSurface(Surface surface) {
    if (player != null) {
        player.setSurface(surface);
    }
    mSurface = surface;
    return true;
}

@Override
public void onSetStreamVolume(float volume) {
    if (player != null) {
        player.setVolume(volume, volume);
    }
    mVolume = volume;
}
```

Similarly, here's how to do it using [ExoPlayer](/guide/topics/media/exoplayer):

### Kotlin

```
override fun onSetSurface(surface: Surface?): Boolean {
    player?.createMessage(videoRenderer)?.apply {
        type = MSG_SET_SURFACE
        payload = surface
        send()
    }
    mSurface = surface
    return true
}

override fun onSetStreamVolume(volume: Float) {
    player?.createMessage(audioRenderer)?.apply {
        type = MSG_SET_VOLUME
        payload = volume
        send()
    }
    mVolume = volume
}
```

### Java

```
@Override
public boolean onSetSurface(@Nullable Surface surface) {
    if (player != null) {
        player.createMessage(videoRenderer)
                .setType(MSG_SET_SURFACE)
                .setPayload(surface)
                .send();
    }
    mSurface = surface;
    return true;
}

@Override
public void onSetStreamVolume(float volume) {
    if (player != null) {
        player.createMessage(videoRenderer)
                .setType(MSG_SET_VOLUME)
                .setPayload(volume)
                .send();
    }
    mVolume = volume;
}
```

## Use an overlay

Use an overlay to display subtitles, messages, ads or MHEG-5 data broadcasts. By default, the
overlay is disabled. You can enable it when you create the session by calling
`TvInputService.Session.setOverlayViewEnabled(true)`,
as in the following example:

### Kotlin

```
override fun onCreateSession(inputId: String): Session =
        onCreateSessionInternal(inputId).apply {
            setOverlayViewEnabled(true)
            sessions.add(this)
        }
```

### Java

```
@Override
public final Session onCreateSession(String inputId) {
    BaseTvInputSessionImpl session = onCreateSessionInternal(inputId);
    session.setOverlayViewEnabled(true);
    sessions.add(session);
    return session;
}
```

Use a `View` object for the overlay, returned from `TvInputService.Session.onCreateOverlayView()`, as shown here:

### Kotlin

```
override fun onCreateOverlayView(): View =
        (context.getSystemService(LAYOUT_INFLATER_SERVICE) as LayoutInflater).run {
            inflate(R.layout.overlayview, null).apply {
                subtitleView = findViewById<SubtitleView>(R.id.subtitles).apply {
                    // Configure the subtitle view.
                    val captionStyle: CaptionStyleCompat =
                            CaptionStyleCompat.createFromCaptionStyle(captioningManager.userStyle)
                    setStyle(captionStyle)
                    setFractionalTextSize(captioningManager.fontScale)
                }
            }
        }
```

### Java

```
@Override
public View onCreateOverlayView() {
    LayoutInflater inflater = (LayoutInflater) getSystemService(LAYOUT_INFLATER_SERVICE);
    View view = inflater.inflate(R.layout.overlayview, null);
    subtitleView = (SubtitleView) view.findViewById(R.id.subtitles);

    // Configure the subtitle view.
    CaptionStyleCompat captionStyle;
    captionStyle = CaptionStyleCompat.createFromCaptionStyle(
            captioningManager.getUserStyle());
    subtitleView.setStyle(captionStyle);
    subtitleView.setFractionalTextSize(captioningManager.fontScale);
    return view;
}
```

The layout definition for the overlay might look something like this:

```
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"

    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.google.android.exoplayer.text.SubtitleView
        android:id="@+id/subtitles"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|center_horizontal"
        android:layout_marginLeft="16dp"
        android:layout_marginRight="16dp"
        android:layout_marginBottom="32dp"
        android:visibility="invisible"/>
</FrameLayout>
```

## Control content

When the user selects a channel, your TV input handles the `onTune()` callback in the `TvInputService.Session` object. The system TV
app's parental controls determine what content displays, given the content rating.
The following sections describe how to manage channel and program selection using the
`TvInputService.Session` `notify` methods that
communicate with the system TV app.

### Make video unavailable

When the user changes the channel, you want to make sure the screen doesn't display any stray
video artifacts before your TV input renders the content. When you call `TvInputService.Session.onTune()`,
you can prevent the video from being presented by calling `TvInputService.Session.notifyVideoUnavailable()`
and passing the `VIDEO_UNAVAILABLE_REASON_TUNING` constant, as
shown in the following example.

### Kotlin

```
override fun onTune(channelUri: Uri): Boolean {
    subtitleView?.visibility = View.INVISIBLE
    notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_TUNING)
    unblockedRatingSet.clear()

    dbHandler.apply {
        removeCallbacks(playCurrentProgramRunnable)
        playCurrentProgramRunnable = PlayCurrentProgramRunnable(channelUri)
        post(playCurrentProgramRunnable)
    }
    return true
}
```

### Java

```
@Override
public boolean onTune(Uri channelUri) {
    if (subtitleView != null) {
        subtitleView.setVisibility(View.INVISIBLE);
    }
    notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_TUNING);
    unblockedRatingSet.clear();

    dbHandler.removeCallbacks(playCurrentProgramRunnable);
    playCurrentProgramRunnable = new PlayCurrentProgramRunnable(channelUri);
    dbHandler.post(playCurrentProgramRunnable);
    return true;
}
```

Then, when the content is rendered to the `Surface`, you call
`TvInputService.Session.notifyVideoAvailable()`
to allow the video to display, like so:

### Kotlin

```
fun onRenderedFirstFrame(surface:Surface) {
    firstFrameDrawn = true
    notifyVideoAvailable()
}
```

### Java

```
@Override
public void onRenderedFirstFrame(Surface surface) {
    firstFrameDrawn = true;
    notifyVideoAvailable();
}
```

This transition lasts only for fractions of a second, but presenting a blank screen is
visually better than allowing the picture to flash odd blips and jitters.

See also, [Integrate player with surface](#surface) for more information about working
with `Surface` to render video.

### Provide parental control

To determine if a given content is blocked by parental controls and content rating, you check the
`TvInputManager` class methods, `isParentalControlsEnabled()`
and `isRatingBlocked(android.media.tv.TvContentRating)`. You
might also want to make sure the content's `TvContentRating` is included in a
set of currently allowed content ratings. These considerations are shown in the following sample.

### Kotlin

```
private fun checkContentBlockNeeded() {
    currentContentRating?.also { rating ->
        if (!tvInputManager.isParentalControlsEnabled
                || !tvInputManager.isRatingBlocked(rating)
                || unblockedRatingSet.contains(rating)) {
            // Content rating is changed so we don't need to block anymore.
            // Unblock content here explicitly to resume playback.
            unblockContent(null)
            return
        }
    }
    lastBlockedRating = currentContentRating
    player?.run {
        // Children restricted content might be blocked by TV app as well,
        // but TIF should do its best not to show any single frame of blocked content.
        releasePlayer()
    }

    notifyContentBlocked(currentContentRating)
}
```

### Java

```
private void checkContentBlockNeeded() {
    if (currentContentRating == null || !tvInputManager.isParentalControlsEnabled()
            || !tvInputManager.isRatingBlocked(currentContentRating)
            || unblockedRatingSet.contains(currentContentRating)) {
        // Content rating is changed so we don't need to block anymore.
        // Unblock content here explicitly to resume playback.
        unblockContent(null);
        return;
    }

    lastBlockedRating = currentContentRating;
    if (player != null) {
        // Children restricted content might be blocked by TV app as well,
        // but TIF should do its best not to show any single frame of blocked content.
        releasePlayer();
    }

    notifyContentBlocked(currentContentRating);
}
```

Once you have determined if the content should or should not be blocked, notify the system TV
app by calling the
`TvInputService.Session` method `notifyContentAllowed()`
or
`notifyContentBlocked()`
, as shown in the previous example.

Use the `TvContentRating` class to generate the system-defined string for
the `COLUMN_CONTENT_RATING` with the
`TvContentRating.createRating()`
method, as shown here:

### Kotlin

```
val rating = TvContentRating.createRating(
        "com.android.tv",
        "US_TV",
        "US_TV_PG",
        "US_TV_D", "US_TV_L"
)
```

### Java

```
TvContentRating rating = TvContentRating.createRating(
    "com.android.tv",
    "US_TV",
    "US_TV_PG",
    "US_TV_D", "US_TV_L");
```

## Handle track selection

The `TvTrackInfo` class holds information about media tracks such
as the track type (video, audio, or subtitle) and so forth.

The first time your TV input session is able to get track information, it should call
`TvInputService.Session.notifyTracksChanged()` with a list of all tracks to update the system TV app. When there
is a change in track information, call
`notifyTracksChanged()`
again to update the system.

The system TV app provides an interface for the user to select a specific track if more than one
track is available for a given track type; for example, subtitles in different languages. Your TV
input responds to the
`onSelectTrack()`
call from the system TV app by calling
`notifyTrackSelected()`
, as shown in the following example. Note that when `null`
is passed as the track ID, this *deselects* the track.

### Kotlin

```
override fun onSelectTrack(type: Int, trackId: String?): Boolean =
        mPlayer?.let { player ->
            if (type == TvTrackInfo.TYPE_SUBTITLE) {
                if (!captionEnabled && trackId != null) return false
                selectedSubtitleTrackId = trackId
                subtitleView.visibility = if (trackId == null) View.INVISIBLE else View.VISIBLE
            }
            player.trackInfo.indexOfFirst { it.trackType == type }.let { trackIndex ->
                if( trackIndex >= 0) {
                    player.selectTrack(trackIndex)
                    notifyTrackSelected(type, trackId)
                    true
                } else false
            }
        } ?: false
```

### Java

```
@Override
public boolean onSelectTrack(int type, String trackId) {
    if (player != null) {
        if (type == TvTrackInfo.TYPE_SUBTITLE) {
            if (!captionEnabled && trackId != null) {
                return false;
            }
            selectedSubtitleTrackId = trackId;
            if (trackId == null) {
                subtitleView.setVisibility(View.INVISIBLE);
            }
        }
        int trackIndex = -1;
        MediaPlayer.TrackInfo[] trackInfos = player.getTrackInfo();
        for (int index = 0; index < trackInfos.length; index++) {
            MediaPlayer.TrackInfo trackInfo = trackInfos[index];
            if (trackInfo.getTrackType() == type) {
                trackIndex = index;
                break;
            }
        }
        if (trackIndex >= 0) {
            player.selectTrack(trackIndex);
            notifyTrackSelected(type, trackId);
            return true;
        }
    }
    return false;
}
```

[Previous

arrow\_back

Work with channel data](/training/tv/tif/channel)

[Next

Support time-shifting

arrow\_forward](/training/tv/tif/time-shifting)