---
title: https://developer.android.com/training/tv/playback/media-session
url: https://developer.android.com/training/tv/playback/media-session
source: md.txt
---

# Implement a media session

Create a[`MediaSession`](https://developer.android.com/reference/android/media/session/MediaSession#MediaSession(android.content.Context,%20java.lang.String))when your app is preparing to play media. The following code snippet is an example of how to set the appropriate callback and flags:  

### Kotlin

```kotlin
session = MediaSession(this, "MusicService").apply {
    setCallback(MediaSessionCallback())
    setFlags(
            MediaSession.FLAG_HANDLES_MEDIA_BUTTONS or MediaSession.FLAG_HANDLES_TRANSPORT_CONTROLS
    )
}
```

### Java

```java
session = new MediaSession(this, "MusicService");
session.setCallback(new MediaSessionCallback());
session.setFlags(MediaSession.FLAG_HANDLES_MEDIA_BUTTONS |
        MediaSession.FLAG_HANDLES_TRANSPORT_CONTROLS);
```

## Start a media session

Be sure to also call[`setActive(true)`](https://developer.android.com/reference/android/media/session/MediaSession#setActive(boolean))when playback begins. Your app must also request audio focus, as described in[Manage audio focus](https://developer.android.com/media/optimize/audio-focus). These steps are shown in the following example:  

### Kotlin

```kotlin
private fun handlePlayRequest() {

    tryToGetAudioFocus()

    if (!session.isActive) {
        session.isActive = true
    }
    ...
}
```

### Java

```java
private void handlePlayRequest() {

    tryToGetAudioFocus();

    if (!session.isActive()) {
        session.setActive(true);
    }
    ...
}
```

## Update the playback state

Update the playback state in the[`MediaSession`](https://developer.android.com/reference/android/media/session/MediaSession)to reflect the state of the current media:  

### Kotlin

```kotlin
private fun updatePlaybackState() {
    val position: Long =
            mediaPlayer
                    ?.takeIf { it.isPlaying }
                    ?.currentPosition?.toLong()
                    ?: PlaybackState.PLAYBACK_POSITION_UNKNOWN

    val stateBuilder = PlaybackState.Builder()
            .setActions(getAvailableActions()).apply {
                setState(mState, position, 1.0f)
            }
    session.setPlaybackState(stateBuilder.build())
}

private fun getAvailableActions(): Long {
    var actions = (PlaybackState.ACTION_PLAY_PAUSE
            or PlaybackState.ACTION_PLAY_FROM_MEDIA_ID
            or PlaybackState.ACTION_PLAY_FROM_SEARCH)

    playingQueue?.takeIf { it.isNotEmpty() }?.apply {
        actions = if (mState == PlaybackState.STATE_PLAYING) {
            actions or PlaybackState.ACTION_PAUSE
        } else {
            actions or PlaybackState.ACTION_PLAY
        }
        if (currentIndexOnQueue > 0) {
            actions = actions or PlaybackState.ACTION_SKIP_TO_PREVIOUS
        }
        if (currentIndexOnQueue < size - 1) {
            actions = actions or PlaybackState.ACTION_SKIP_TO_NEXT
        }
    }
    return actions
}
```

### Java

```java
private void updatePlaybackState() {
    long position = PlaybackState.PLAYBACK_POSITION_UNKNOWN;
    if (mediaPlayer != null && mediaPlayer.isPlaying()) {
        position = mediaPlayer.getCurrentPosition();
    }
    PlaybackState.Builder stateBuilder = new PlaybackState.Builder()
            .setActions(getAvailableActions());
    stateBuilder.setState(mState, position, 1.0f);
    session.setPlaybackState(stateBuilder.build());
}

private long getAvailableActions() {
    long actions = PlaybackState.ACTION_PLAY_PAUSE |
            PlaybackState.ACTION_PLAY_FROM_MEDIA_ID |
            PlaybackState.ACTION_PLAY_FROM_SEARCH;
    if (playingQueue == null || playingQueue.isEmpty()) {
        return actions;
    }
    if (mState == PlaybackState.STATE_PLAYING) {
        actions |= PlaybackState.ACTION_PAUSE;
    } else {
        actions |= PlaybackState.ACTION_PLAY;
    }
    if (currentIndexOnQueue > 0) {
        actions |= PlaybackState.ACTION_SKIP_TO_PREVIOUS;
    }
    if (currentIndexOnQueue < playingQueue.size() - 1) {
        actions |= PlaybackState.ACTION_SKIP_TO_NEXT;
    }
    return actions;
}
```

## Update the media metadata

Set the[`MediaMetadata`](https://developer.android.com/reference/android/media/MediaMetadata)with the[`setMetadata()`](https://developer.android.com/reference/android/media/session/MediaSession#setMetadata(android.media.MediaMetadata))method. This method is only called once per object that is played. It lets you provide information to the media session about the media, including its title, subtitle, artist, artwork, etc. The following example is tailored toward music and assumes the track's data is stored in a custom data class,`MediaData`:  

### Kotlin

```kotlin
private fun updateMetadata(myData: MediaData) {
    val metadataBuilder = MediaMetadata.Builder().apply {
        // To provide most control over how an item is displayed set the
        // display fields in the metadata
        putString(MediaMetadata.METADATA_KEY_DISPLAY_TITLE, myData.displayTitle)
        putString(MediaMetadata.METADATA_KEY_DISPLAY_SUBTITLE, myData.displaySubtitle)
        putString(MediaMetadata.METADATA_KEY_DISPLAY_ICON_URI, myData.artUri)
        // And at minimum the title and artist for legacy support
        putString(MediaMetadata.METADATA_KEY_TITLE, myData.title)
        putString(MediaMetadata.METADATA_KEY_ARTIST, myData.artist)
        // A small bitmap for the artwork is also recommended
        putBitmap(MediaMetadata.METADATA_KEY_ART, myData.artBitmap)
        // Add any other fields you have for your data as well
    }
    session.setMetadata(metadataBuilder.build())
}
```

### Java

```java
private void updateMetadata(MediaData myData) {
    MediaMetadata.Builder metadataBuilder = new MediaMetadata.Builder();
    // To provide most control over how an item is displayed set the
    // display fields in the metadata
    metadataBuilder.putString(MediaMetadata.METADATA_KEY_DISPLAY_TITLE,
            myData.displayTitle);
    metadataBuilder.putString(MediaMetadata.METADATA_KEY_DISPLAY_SUBTITLE,
            myData.displaySubtitle);
    metadataBuilder.putString(MediaMetadata.METADATA_KEY_DISPLAY_ICON_URI,
            myData.artUri);
    // And at minimum the title and artist for legacy support
    metadataBuilder.putString(MediaMetadata.METADATA_KEY_TITLE,
            myData.title);
    metadataBuilder.putString(MediaMetadata.METADATA_KEY_ARTIST,
            myData.artist);
    // A small bitmap for the artwork is also recommended
    metadataBuilder.putBitmap(MediaMetadata.METADATA_KEY_ART,
            myData.artBitmap);
    // Add any other fields you have for your data as well
    session.setMetadata(metadataBuilder.build());
}
```