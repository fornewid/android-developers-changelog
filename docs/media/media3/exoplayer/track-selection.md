---
title: https://developer.android.com/media/media3/exoplayer/track-selection
url: https://developer.android.com/media/media3/exoplayer/track-selection
source: md.txt
---

When a media item contains multiple tracks, track selection is the process that
determines which of them are chosen for playback. The track selection process is
configured by [`TrackSelectionParameters`](https://developer.android.com/reference/androidx/media3/common/TrackSelectionParameters), which allows many different
constraints and overrides influencing track selection to be specified.

## Querying the available tracks

You can listen to `Player.Listener.onTracksChanged` to be notified about changes
to tracks, including:

- The available tracks becoming known when preparation of the media item being played completes. Note that the player needs to prepare a media item to know what tracks it contains.
- The available tracks changing due to playback transitioning from one media item to another.
- Changes to the selected tracks.

### Kotlin

```kotlin
player.addListener(
  object : Player.Listener {
    override fun onTracksChanged(tracks: Tracks) {
      // Update UI using current tracks.
    }
  }
)
```

### Java

```java
player.addListener(
    new Player.Listener() {
      @Override
      public void onTracksChanged(Tracks tracks) {
        // Update UI using current tracks.
      }
    });
```

You can also query the current tracks by calling `player.getCurrentTracks()`.
The returned `Tracks` contains a list of `Tracks.Group` objects, where tracks
within a single `Group` present the same content but in different formats.

As an example of how tracks can be grouped, consider an adaptive playback where
a main video feed is provided in five bitrates, and an alternative video feed
(for example, a different camera angle in a sports match) is provided in two bitrates.
In this case there will be two video track groups, one corresponding to the main
video feed containing five tracks, and a second for the alternative video feed
containing two tracks.

Audio tracks whose languages differ are not grouped, because content in
different languages is not considered to be the same. Conversely, audio tracks
in the same language that only differ in properties such as bitrate, sampling
rate, channel count and so on can be grouped. This also applies to text tracks.

Each `Group` can be queried to determine which tracks are supported for
playback, which are currently selected, and what `Format` each track uses:

### Kotlin

```kotlin
for (trackGroup in tracks.groups) {
  // Group level information.
  val trackType = trackGroup.type
  val trackInGroupIsSelected = trackGroup.isSelected
  val trackInGroupIsSupported = trackGroup.isSupported
  for (i in 0 until trackGroup.length) {
    // Individual track information.
    val isSupported = trackGroup.isTrackSupported(i)
    val isSelected = trackGroup.isTrackSelected(i)
    val trackFormat = trackGroup.getTrackFormat(i)
  }
}
```

### Java

```java
for (Tracks.Group trackGroup : tracks.getGroups()) {
  // Group level information.
  @C.TrackType int trackType = trackGroup.getType();
  boolean trackInGroupIsSelected = trackGroup.isSelected();
  boolean trackInGroupIsSupported = trackGroup.isSupported();
  for (int i = 0; i < trackGroup.length; i++) {
    // Individual track information.
    boolean isSupported = trackGroup.isTrackSupported(i);
    boolean isSelected = trackGroup.isTrackSelected(i);
    Format trackFormat = trackGroup.getTrackFormat(i);
  }
}
```

- A track is *supported* if the `Player` is able to decode and render its samples. Note that even if multiple track groups of the same type (for example multiple audio track groups) are supported, it only means that they are supported individually and the player is not necessarily able to play them at the same time.
- A track is *selected* if it has been chosen for playback given the current `TrackSelectionParameters`. If multiple tracks within one track group are selected, the player uses these tracks for adaptive playback (for example, multiple video tracks with different bitrates). Note that only one of these tracks will be played at any one time.

## Modifying track selection parameters

The track selection process can be configured using
`Player.setTrackSelectionParameters`. You can do this both before and during
playback. The following example demonstrates how to obtain the current
`TrackSelectionParameters` from the player, modify them, and update the `Player`
with the modified result:

### Kotlin

```kotlin
player.trackSelectionParameters =
  player.trackSelectionParameters
    .buildUpon()
    .setMaxVideoSizeSd()
    .setPreferredAudioLanguage("hu")
    .build()
```

### Java

```java
player.setTrackSelectionParameters(
    player
        .getTrackSelectionParameters()
        .buildUpon()
        .setMaxVideoSizeSd()
        .setPreferredAudioLanguage("hu")
        .build());
```

### Constraint-based track selection

Most options in `TrackSelectionParameters` allow you to specify constraints,
which are independent of the tracks that are actually available. Available
constraints include:

- Maximum and minimum video width, height, frame rate, and bitrate.
- Maximum audio channel count and bitrate.
- Preferred MIME types for video and audio.
- Preferred audio languages and role flags.
- Preferred text languages and role flags.

ExoPlayer uses sensible defaults for these constraints, for example restricting
video resolution to the display size and preferring the audio language that
matches the user's system Locale setting.

There are several benefits to using constraint-based track selection rather than
selecting specific tracks from those that are available:

- You can specify constraints before knowing what tracks a media item provides. This means that constraints can be specified before the player has prepared a media item, whereas selecting specific tracks requires application code to wait until the available tracks become known.
- Constraints are applied for all media items in a playlist, even when those items have different available tracks. For example, a preferred audio language constraint will be automatically applied for all media items, even if the `Format` of the track in that language varies from one media item to the next. This is not the case when selecting specific tracks, as described below.

### Selecting specific tracks

It's possible to select specific tracks using `TrackSelectionParameters`. First,
the player's currently available tracks should be queried using
`Player.getCurrentTracks`. Second, having identified which tracks to select,
they can be set on `TrackSelectionParameters` using a `TrackSelectionOverride`.
For example, to select the first track from a specific `audioTrackGroup`:

### Kotlin

```kotlin
player.trackSelectionParameters =
  player.trackSelectionParameters
    .buildUpon()
    .setOverrideForType(
      TrackSelectionOverride(audioTrackGroup.mediaTrackGroup, /* trackIndex= */ 0)
    )
    .build()
```

### Java

```java
player.setTrackSelectionParameters(
    player
        .getTrackSelectionParameters()
        .buildUpon()
        .setOverrideForType(
            new TrackSelectionOverride(
                audioTrackGroup.getMediaTrackGroup(), /* trackIndex= */ 0))
        .build());
```

A `TrackSelectionOverride` will only apply to media items that contain a
`TrackGroup` exactly matching the one specified in the override. Hence an
override may not apply to a subsequent media item if that item contains
different tracks.

### Disabling track types or groups

Track types like video, audio or text, can be disabled completely using
`TrackSelectionParameters.Builder.setTrackTypeDisabled`. A disabled track type
will be disabled for all media items:

### Kotlin

```kotlin
player.trackSelectionParameters =
  player.trackSelectionParameters
    .buildUpon()
    .setTrackTypeDisabled(C.TRACK_TYPE_VIDEO, /* disabled= */ true)
    .build()
```

### Java

```java
player.setTrackSelectionParameters(
    player
        .getTrackSelectionParameters()
        .buildUpon()
        .setTrackTypeDisabled(C.TRACK_TYPE_VIDEO, /* disabled= */ true)
        .build());
```

Alternatively, it's possible to prevent the selection of tracks from a specific
`TrackGroup` by specifying an empty override for that group:

### Kotlin

```kotlin
player.trackSelectionParameters =
  player.trackSelectionParameters
    .buildUpon()
    .addOverride(
      TrackSelectionOverride(disabledTrackGroup.mediaTrackGroup, /* trackIndices= */ listOf())
    )
    .build()
```

### Java

```java
player.setTrackSelectionParameters(
    player
        .getTrackSelectionParameters()
        .buildUpon()
        .addOverride(
            new TrackSelectionOverride(
                disabledTrackGroup.getMediaTrackGroup(),
                /* trackIndices= */ ImmutableList.of()))
        .build());
```

## Customizing the track selector

Track selection is the responsibility of a `TrackSelector`, an instance
of which can be provided whenever an `ExoPlayer` is built and later obtained
with `ExoPlayer.getTrackSelector()`.

### Kotlin

```kotlin
val trackSelector = DefaultTrackSelector(context)
val player = ExoPlayer.Builder(context).setTrackSelector(trackSelector).build()
```

### Java

```java
DefaultTrackSelector trackSelector = new DefaultTrackSelector(context);
ExoPlayer player = new ExoPlayer.Builder(context).setTrackSelector(trackSelector).build();
```

`DefaultTrackSelector` is a flexible `TrackSelector` suitable for most use
cases. It uses the `TrackSelectionParameters` set in the `Player`, but also
provides some advanced customization options that can be specified in the
`DefaultTrackSelector.ParametersBuilder`:

### Kotlin

```kotlin
trackSelector.setParameters(
  trackSelector.buildUponParameters().setAllowVideoMixedMimeTypeAdaptiveness(true)
)
```

### Java

```java
trackSelector.setParameters(
    trackSelector.buildUponParameters().setAllowVideoMixedMimeTypeAdaptiveness(true));
```

### Tunneling

Tunneling may help with efficient video playback of high-resolution streams on
some TV devices. See the [battery consumption](https://developer.android.com/media/media3/exoplayer/battery-consumption) page for further notes and
details.

You can set a preference for tunneled playback to enable it in cases where the
combination of renderers and selected tracks supports it. To do this, use
`DefaultTrackSelector.ParametersBuilder.setTunnelingEnabled(true)`.

### Audio Offload

Audio offload may help to save power, in particular for longer playbacks with
the screen turned off. See the [battery consumption](https://developer.android.com/media/media3/exoplayer/battery-consumption) page for further notes
and details.

You can set preferences for offloaded audio playback to enable it in cases where
the combination of renderers and selected tracks supports it. To do this,
specify [`AudioOffloadModePreferences`](https://developer.android.com/reference/androidx/media3/common/TrackSelectionParameters.AudioOffloadPreferences) in your `TrackSelectionParameters`.

### Kotlin

```kotlin
val audioOffloadPreferences =
  AudioOffloadPreferences.Builder()
    .setAudioOffloadMode(AudioOffloadPreferences.AUDIO_OFFLOAD_MODE_ENABLED)
    // Add additional options as needed
    .setIsGaplessSupportRequired(true)
    .build()
player.trackSelectionParameters =
  player.trackSelectionParameters
    .buildUpon()
    .setAudioOffloadPreferences(audioOffloadPreferences)
    .build()
```

### Java

```java
AudioOffloadPreferences audioOffloadPreferences =
    new AudioOffloadPreferences.Builder()
        .setAudioOffloadMode(AudioOffloadPreferences.AUDIO_OFFLOAD_MODE_ENABLED)
        // Add additional options as needed
        .setIsGaplessSupportRequired(true)
        .build();
player.setTrackSelectionParameters(
    player
        .getTrackSelectionParameters()
        .buildUpon()
        .setAudioOffloadPreferences(audioOffloadPreferences)
        .build());
```