---
title: https://developer.android.com/media/media3/exoplayer/hls
url: https://developer.android.com/media/media3/exoplayer/hls
source: md.txt
---

ExoPlayer supports HLS with multiple container formats. The contained audio and
video sample formats must also be supported (see the [sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats)
section for details). We strongly encourage HLS content producers to generate
high quality HLS streams, as described [in this blog post](https://medium.com/google-exoplayer/hls-playback-in-exoplayer-a33959a47be7).

| Feature | Supported | Comments |
|---|---|---|
| **Containers** |   |   |
| MPEG-TS | YES |   |
| FMP4/CMAF | YES |   |
| ADTS (AAC) | YES |   |
| MP3 | YES |   |
| **Closed captions /** **subtitles** |   |   |
| CEA-608 | YES |   |
| CEA-708 | YES |   |
| WebVTT | YES |   |
| **Metadata** |   |   |
| ID3 | YES |   |
| SCTE-35 | NO |   |
| **Content protection** |   |   |
| AES-128 | YES |   |
| Sample AES-128 | NO |   |
| Widevine | YES | API 19+ ("cenc" scheme) and 25+ ("cbcs" scheme) |
| PlayReady SL2000 | YES | Android TV only |
| **Server control** |   |   |
| Delta updates | YES |   |
| Blocking playlist reload | YES |   |
| Blocking load of preload hints | YES | Except for byteranges with undefined lengths |
| **Ad insertion** |   |   |
| Server-guided ad insertion (Interstitials) | Partially | Only VOD with `X-ASSET-URI`. Live streams and `X-ASSET-LIST` will be added later. |
| IMA server-side and client-side ads | YES | [Ad insertion guide](https://developer.android.com/media/media3/exoplayer/ad-insertion) |
| **Live playback** |   |   |
| Regular live playback | YES |   |
| Low-latency HLS (Apple) | YES |   |
| Low-latency HLS (Community) | NO |   |
| **Common Media Client Data** **CMCD** | YES | [CMCD integration guide](https://developer.android.com/media/media3/exoplayer/cmcd) |

## Using MediaItem

To play an HLS stream, you need to depend on the HLS module.

### Kotlin

```kotlin
implementation("androidx.media3:media3-exoplayer-hls:1.9.2")
```

### Groovy

```groovy
implementation "androidx.media3:media3-exoplayer-hls:1.9.2"
```

You can then create a `MediaItem` for an HLS playlist URI and pass it to the
player.

### Kotlin

```kotlin
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(hlsUri))
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(hlsUri));
// Prepare the player.
player.prepare();
```

If your URI doesn't end with `.m3u8`, you can pass `MimeTypes.APPLICATION_M3U8`
to `setMimeType` of `MediaItem.Builder` to explicitly indicate the type of the
content.

The URI of the media item may point to either a media playlist or a multivariant
playlist. If the URI points to a multivariant playlist that declares multiple
`#EXT-X-STREAM-INF` tags, then ExoPlayer will automatically adapt between
variants, taking into account both available bandwidth and device capabilities.

## Using HlsMediaSource

For more customization options, you can create a `HlsMediaSource` and pass it
directly to the player instead of a `MediaItem`.

### Kotlin

```kotlin
// Create a data source factory.
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSource.Factory()
// Create a HLS media source pointing to a playlist uri.
val hlsMediaSource =
  HlsMediaSource.Factory(dataSourceFactory).createMediaSource(MediaItem.fromUri(hlsUri))
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the HLS media source as the playlist with a single media item.
player.setMediaSource(hlsMediaSource)
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a data source factory.
DataSource.Factory dataSourceFactory = new DefaultHttpDataSource.Factory();
// Create a HLS media source pointing to a playlist uri.
HlsMediaSource hlsMediaSource =
    new HlsMediaSource.Factory(dataSourceFactory).createMediaSource(MediaItem.fromUri(hlsUri));
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the HLS media source as the playlist with a single media item.
player.setMediaSource(hlsMediaSource);
// Prepare the player.
player.prepare();
```

## Accessing the manifest

You can retrieve the current manifest by calling `Player.getCurrentManifest`.
For HLS, you should cast the returned object to `HlsManifest`. The
`onTimelineChanged` callback of `Player.Listener` is also called whenever
the manifest is loaded. This will happen once for on-demand content and
possibly many times for live content. The following code snippet shows how an app
can do something whenever the manifest is loaded.

### Kotlin

```kotlin
player.addListener(
  object : Player.Listener {
    override fun onTimelineChanged(
      timeline: Timeline,
      @Player.TimelineChangeReason reason: Int,
    ) {
      val manifest = player.currentManifest
      if (manifest is HlsManifest) {
        // Do something with the manifest.
      }
    }
  }
)
```

### Java

```java
player.addListener(
    new Player.Listener() {
      @Override
      public void onTimelineChanged(
          Timeline timeline, @Player.TimelineChangeReason int reason) {
        Object manifest = player.getCurrentManifest();
        if (manifest != null) {
          HlsManifest hlsManifest = (HlsManifest) manifest;
          // Do something with the manifest.
        }
      }
    });
```

## Play HLS streams with interstitials

The HLS specification defines HLS interstitials which can be used to include
interstitial information in a media playlist. ExoPlayer by default ignores these
interstitials. Support can be added by using `HlsInterstitialsAdsLoader`. We
don't support all features of the spec from the start. If you miss support for
your stream, let us know by [filing an issue on GitHub](https://github.com/androidx/media/issues/new?template=feature_request.md) and send us your
stream URI, so we can add support for your stream.

### Use a `MediaItem` with the playlist API

The most convenient way to play HLS streams with interstitials is building an
ExoPlayer instance with a `HlsInterstitialsAdsLoader.AdsMediaSourceFactory`.
This allows to use the `MediaItem` based [playlist API](https://developer.android.com/media/media3/exoplayer/playlists) of the `Player`
interface to play HLS interstitials.

The `MediaSource.Factory` of `ExoPlayer` can be injected into the builder when
building the player instance:

### Kotlin

```kotlin
val hlsInterstitialsAdsLoader = HlsInterstitialsAdsLoader(context)
// Create a MediaSource.Factory for HLS streams with interstitials.
val hlsMediaSourceFactory =
  HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
    hlsInterstitialsAdsLoader,
    playerView,
    DefaultMediaSourceFactory(context),
  )

// Build player with interstitials media source factory
val player = ExoPlayer.Builder(context).setMediaSourceFactory(hlsMediaSourceFactory).build()

// Set the player on the ads loader.
hlsInterstitialsAdsLoader.setPlayer(player)
playerView.setPlayer(player)
```

### Java

```java
HlsInterstitialsAdsLoader hlsInterstitialsAdsLoader = new HlsInterstitialsAdsLoader(context);
// Create a MediaSource.Factory for HLS streams with interstitials.
MediaSource.Factory hlsMediaSourceFactory =
    new HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
        hlsInterstitialsAdsLoader, playerView, new DefaultMediaSourceFactory(context));

// Build player with interstitials media source factory
ExoPlayer player =
    new ExoPlayer.Builder(context).setMediaSourceFactory(hlsMediaSourceFactory).build();

// Set the player on the ads loader.
hlsInterstitialsAdsLoader.setPlayer(player);
playerView.setPlayer(player);
```

With such a player setup, playing HLS interstitials is just about setting a
media item with an `AdsConfiguration` on the player:

### Kotlin

```kotlin
// Build an HLS media item with ads configuration to be played.
player.setMediaItem(
  MediaItem.Builder()
    .setUri("https://www.example.com/media.m3u8")
    .setAdsConfiguration(
      MediaItem.AdsConfiguration.Builder("hls://interstitials".toUri())
        .setAdsId("ad-tag-0") // must be unique within playlist
        .build()
    )
    .build()
)

player.prepare()
player.play()
```

### Java

```java
// Build an HLS media item with ads configuration to be played.
player.setMediaItem(
    new MediaItem.Builder()
        .setUri("https://www.example.com/media.m3u8")
        .setAdsConfiguration(
            new AdsConfiguration.Builder(Uri.parse("hls://interstitials"))
                .setAdsId("ad-tag-0") // must be unique within playlist
                .build())
        .build());
player.prepare();
player.play();
```

> [!NOTE]
> **Note:** The `HlsInterstitialsAdsLoader.AdsMediaSourceFactory` can be used for any HLS stream. If the ads configuration is omitted, the source is played as if it was created with `HlsMediaSource.Factory` directly.

### Use the media source based API

Alternatively, the ExoPlayer instance can be built without overriding the
default media source factory. To support interstitials, an app can then
use `HlsInterstitialsAdsLoader.AdsMediaSourceFactory` directly to create a
`MediaSource` and provide it to ExoPlayer using the media source based playlist
API:

### Kotlin

```kotlin
val hlsInterstitialsAdsLoader = HlsInterstitialsAdsLoader(context)
// Create a MediaSource.Factory for HLS streams with interstitials.
val hlsMediaSourceFactory =
  HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
    hlsInterstitialsAdsLoader,
    playerView,
    context,
  )

// Build player with default media source factory.
val player = ExoPlayer.Builder(context).build()

// Create an media source from an HLS media item with ads configuration.
val mediaSource =
  hlsMediaSourceFactory.createMediaSource(
    MediaItem.Builder()
      .setUri("https://www.example.com/media.m3u8")
      .setAdsConfiguration(
        MediaItem.AdsConfiguration.Builder("hls://interstitials".toUri())
          .setAdsId("ad-tag-0")
          .build()
      )
      .build()
  )

// Set the media source on the player.
player.setMediaSource(mediaSource)
player.prepare()
player.play()
```

### Java

```java
HlsInterstitialsAdsLoader hlsInterstitialsAdsLoader = new HlsInterstitialsAdsLoader(context);
// Create a MediaSource.Factory for HLS streams with interstitials.
MediaSource.Factory hlsMediaSourceFactory =
    new HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
        hlsInterstitialsAdsLoader, playerView, context);

// Build player with default media source factory.
ExoPlayer player = new ExoPlayer.Builder(context).build();

// Create an media source from an HLS media item with ads configuration.
MediaSource mediaSource =
    hlsMediaSourceFactory.createMediaSource(
        new MediaItem.Builder()
            .setUri("https://www.example.com/media.m3u8")
            .setAdsConfiguration(
                new MediaItem.AdsConfiguration.Builder(Uri.parse("hls://interstitials"))
                    .setAdsId("ad-tag-0")
                    .build())
            .build());

// Set the media source on the player.
player.setMediaSource(mediaSource);
player.prepare();
player.play();
```

### Listen to ad events

A `Listener` can be added to `HlsInterstitialsAdsLoader` to monitor events
regarding status changes concerning HLS interstitials playback. This allows an
app or SDK to track ads played, asset lists being loaded, ad media sources being
prepared or detect asset list load and ad preparation errors. Further, metadata
emitted by ad media sources can be received for fine-grained ad playback
verification or to track ad playback progress.

> [!NOTE]
> **Note:** A conventional `Player.Listener` can be used to track (ad) playback in more detail (see [Listening to player events](https://developer.android.com/media/media3/exoplayer/listening-to-player-events)).

### Kotlin

```kotlin
class AdsLoaderListener : HlsInterstitialsAdsLoader.Listener {

  override fun onStart(mediaItem: MediaItem, adsId: Any, adViewProvider: AdViewProvider) {
    // Do something when HLS media item with interstitials is started.
  }

  override fun onMetadata(
    mediaItem: MediaItem,
    adsId: Any,
    adGroupIndex: Int,
    adIndexInAdGroup: Int,
    metadata: Metadata,
  ) {
    // Do something with metadata that is emitted by the ad media source of the given ad.
  }

  override fun onAdCompleted(
    mediaItem: MediaItem,
    adsId: Any,
    adGroupIndex: Int,
    adIndexInAdGroup: Int,
  ) {
    // Do something when ad completed playback.
  }

  // ... See JavaDoc for further callbacks of HlsInterstitialsAdsLoader.Listener.

  override fun onStop(mediaItem: MediaItem, adsId: Any, adPlaybackState: AdPlaybackState) {
    // Do something with the resulting ad playback state when stopped.
  }
}
```

### Java

```java
@OptIn(markerClass = UnstableApi.class)
private static class AdsLoaderListener implements HlsInterstitialsAdsLoader.Listener {

  // implement HlsInterstitialsAdsLoader.Listener
  @Override
  public void onStart(MediaItem mediaItem, Object adsId, AdViewProvider adViewProvider) {
    // Do something when HLS media item with interstitials is started.
  }

  @Override
  public void onMetadata(
      MediaItem mediaItem,
      Object adsId,
      int adGroupIndex,
      int adIndexInAdGroup,
      Metadata metadata) {
    // Do something with metadata that is emitted by the ad media source of the given ad.
  }

  @Override
  public void onAdCompleted(
      MediaItem mediaItem, Object adsId, int adGroupIndex, int adIndexInAdGroup) {
    // Do something when ad completed playback.
  }

  // ... See JavaDoc for further callbacks

  @Override
  public void onStop(MediaItem mediaItem, Object adsId, AdPlaybackState adPlaybackState) {
    // Do something with the resulting ad playback state when stopped.
  }
}
```

See the [JavaDoc of `HlsInterstitialsAdsLoader.Listener`](https://developer.android.com/reference/androidx/media3/exoplayer/hls/HlsInterstitialsAdsLoader.Listener) for the detailed
documentation of all available callbacks.

The listener can then be added to the ads loader:

### Kotlin

```kotlin
val listener = AdsLoaderListener()
// Add the listener to the ads loader to receive ad loader events.
hlsInterstitialsAdsLoader.addListener(listener)
```

### Java

```java
AdsLoaderListener listener = new AdsLoaderListener();
// Add the listener to the ads loader to receive ad loader events.
hlsInterstitialsAdsLoader.addListener(listener);
```

### `HlsInterstitialsAdsLoader` lifecycle

An instance of `HlsInterstitialsAdsLoader` or
`HlsInterstitialsAdsLoader.AdsMediaSourceFactory` can be reused for multiple
player instances that create multiple media sources for which ads have to be
loaded.

An instance can be created for example in the `onCreate` method of an `Activity`
and then be re-used for multiple player instances. This works as long as it is
in use by a single player instance at the same time. This is useful for the
common use case when the app is taken into the background, the player instance
is destroyed and then a new instance is created when the app is foregrounded
again.

#### Playback resumption with an ad playback state

To avoid users having to re-watch ads, the ad playback state can be saved and
restored when the player is recreated. This is done by calling
`getAdsResumptionStates()` when the player is about to be released and storing
the returned `AdsResumptionState` objects. When the player is recreated, the
state can be restored by calling `addAdResumptionState()` on the ads loader
instance. `AdsResumptionState` is bundleable, so it can be stored in an
`Activity`'s `onSaveInstanceState` bundle. Note that ad resumption is only
supported for VOD streams

### Kotlin

```kotlin
class HlsInterstitialsActivity : Activity() {

  companion object {
    const val ADS_RESUMPTION_STATE_KEY = "ads_resumption_state"
  }

  private var hlsInterstitialsAdsLoader: HlsInterstitialsAdsLoader? = null
  private var playerView: PlayerView? = null
  private var player: ExoPlayer? = null
  private var adsResumptionStates: List<HlsInterstitialsAdsLoader.AdsResumptionState>? = null

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Create the ads loader instance.
    hlsInterstitialsAdsLoader = HlsInterstitialsAdsLoader(this)
    // Restore ad resumption states.
    savedInstanceState?.getParcelableArrayList<Bundle>(ADS_RESUMPTION_STATE_KEY)?.let { bundles ->
      adsResumptionStates =
        bundles.map { HlsInterstitialsAdsLoader.AdsResumptionState.fromBundle(it) }
    }
  }

  override fun onStart() {
    super.onStart()
    // Build a player and set it on the ads loader.
    initializePlayer()
    hlsInterstitialsAdsLoader?.setPlayer(player)
    // Add any stored ad resumption states to the ads loader.
    adsResumptionStates?.forEach { hlsInterstitialsAdsLoader?.addAdResumptionState(it) }
    adsResumptionStates = null // Consume the states
  }

  override fun onStop() {
    super.onStop()
    // Get ad resumption states.
    adsResumptionStates = hlsInterstitialsAdsLoader?.adsResumptionStates
    releasePlayer()
  }

  override fun onDestroy() {
    // Release the ads loader when not used anymore.
    hlsInterstitialsAdsLoader?.release()
    hlsInterstitialsAdsLoader = null
    super.onDestroy()
  }

  override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    // Store the ad resumption states.
    adsResumptionStates?.let {
      outState.putParcelableArrayList(
        ADS_RESUMPTION_STATE_KEY,
        ArrayList(it.map(HlsInterstitialsAdsLoader.AdsResumptionState::toBundle)),
      )
    }
  }

  fun initializePlayer() {
    if (player == null) {
      // Create a media source factory for HLS streams.
      val hlsMediaSourceFactory =
        HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
          checkNotNull(hlsInterstitialsAdsLoader),
          playerView!!,
          /* context= */ this,
        )
      // Build player with interstitials media source
      player =
        ExoPlayer.Builder(/* context= */ this)
          .setMediaSourceFactory(hlsMediaSourceFactory)
          .build()
      // Set the player on the ads loader.
      hlsInterstitialsAdsLoader?.setPlayer(player)
      playerView?.player = player
    }

    // Use a media item with an HLS stream URI, an ad tag URI and ads ID.
    player?.setMediaItem(
      MediaItem.Builder()
        .setUri("https://www.example.com/media.m3u8")
        .setMimeType(MimeTypes.APPLICATION_M3U8)
        .setAdsConfiguration(
          MediaItem.AdsConfiguration.Builder("hls://interstitials".toUri())
            .setAdsId("ad-tag-0") // must be unique within ExoPlayer playlist
            .build()
        )
        .build()
    )
    player?.prepare()
    player?.play()
  }

  fun releasePlayer() {
    player?.release()
    player = null
    hlsInterstitialsAdsLoader?.setPlayer(null)
    playerView?.player = null
  }
}
```

### Java

```java
@OptIn(markerClass = UnstableApi.class)
public static class HlsInterstitialsActivity extends Activity {

  public static final String ADS_RESUMPTION_STATE_KEY = "ads_resumption_state";

  @Nullable private HlsInterstitialsAdsLoader hlsInterstitialsAdsLoader;
  @Nullable private PlayerView playerView;
  @Nullable private ExoPlayer player;

  private List<HlsInterstitialsAdsLoader.AdsResumptionState> adsResumptionStates;

  @Override
  protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // Create the ads loader instance.
    hlsInterstitialsAdsLoader = new HlsInterstitialsAdsLoader(this);
    // Restore ad resumption states.
    if (savedInstanceState != null) {
      ArrayList<Bundle> bundles =
          savedInstanceState.getParcelableArrayList(ADS_RESUMPTION_STATE_KEY);
      if (bundles != null) {
        adsResumptionStates = new ArrayList<>();
        for (Bundle bundle : bundles) {
          adsResumptionStates.add(
              HlsInterstitialsAdsLoader.AdsResumptionState.fromBundle(bundle));
        }
      }
    }
  }

  @Override
  protected void onStart() {
    super.onStart();
    // Build a player and set it on the ads loader.
    initializePlayer();
    // Add any stored ad resumption states to the ads loader.
    if (adsResumptionStates != null) {
      for (HlsInterstitialsAdsLoader.AdsResumptionState state : adsResumptionStates) {
        hlsInterstitialsAdsLoader.addAdResumptionState(state);
      }
      adsResumptionStates = null; // Consume the states
    }
  }

  @Override
  protected void onStop() {
    super.onStop();
    // Get ad resumption states before releasing the player.
    if (hlsInterstitialsAdsLoader != null) {
      adsResumptionStates = hlsInterstitialsAdsLoader.getAdsResumptionStates();
    }
    releasePlayer();
  }

  @Override
  protected void onDestroy() {
    // Release the ads loader when not used anymore.
    if (hlsInterstitialsAdsLoader != null) {
      hlsInterstitialsAdsLoader.release();
      hlsInterstitialsAdsLoader = null;
    }
    super.onDestroy();
  }

  @Override
  protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    // Store the ad resumption states.
    if (adsResumptionStates != null) {
      ArrayList<Bundle> bundles = new ArrayList<>();
      for (HlsInterstitialsAdsLoader.AdsResumptionState state : adsResumptionStates) {
        bundles.add(state.toBundle());
      }
      outState.putParcelableArrayList(ADS_RESUMPTION_STATE_KEY, bundles);
    }
  }

  private void initializePlayer() {
    if (player == null) {
      // Create a media source factory for HLS streams.
      MediaSource.Factory hlsMediaSourceFactory =
          new HlsInterstitialsAdsLoader.AdsMediaSourceFactory(
              checkNotNull(hlsInterstitialsAdsLoader), playerView, /* context= */ this);
      // Build player with interstitials media source
      player =
          new ExoPlayer.Builder(/* context= */ this)
              .setMediaSourceFactory(hlsMediaSourceFactory)
              .build();
      // Set the player on the ads loader.
      hlsInterstitialsAdsLoader.setPlayer(player);
      playerView.setPlayer(player);
    }

    // Use a media item with an HLS stream URI, an ad tag URI and ads ID.
    player.setMediaItem(
        new MediaItem.Builder()
            .setUri("https://www.example.com/media.m3u8")
            .setMimeType(MimeTypes.APPLICATION_M3U8)
            .setAdsConfiguration(
                new MediaItem.AdsConfiguration.Builder(Uri.parse("hls://interstitials"))
                    .setAdsId("ad-tag-0") // must be unique within ExoPlayer playlist
                    .build())
            .build());
    player.prepare();
    player.play();
  }

  private void releasePlayer() {
    if (player != null) {
      player.release();
      player = null;
    }
    if (hlsInterstitialsAdsLoader != null) {
      hlsInterstitialsAdsLoader.setPlayer(null);
    }
    if (playerView != null) {
      playerView.setPlayer(null);
    }
  }
}
```

## Customizing playback

ExoPlayer provides multiple ways for you to tailor playback experience to your
app's needs. See the [Customization page](https://developer.android.com/guide/topics/media/exoplayer/customization) for examples.

### Disabling chunkless preparation

By default, ExoPlayer will use chunkless preparation. This means that ExoPlayer
will only use the information in the multivariant playlist to prepare the
stream, which works if the `#EXT-X-STREAM-INF` tags contain the `CODECS`
attribute.

You may need to disable this feature if your media segments contain muxed
closed-caption tracks that are not declared in the multivariant playlist with a
`#EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS` tag. Otherwise, these closed-caption tracks
won't be detected and played. You can disable chunkless preparation in the
`HlsMediaSource.Factory` as shown in the following snippet. Note that this
will increase start up time as ExoPlayer needs to download a media segment to
discover these additional tracks and it is preferable to declare the
closed-caption tracks in the multivariant playlist instead.

### Kotlin

```kotlin
val hlsMediaSource =
  HlsMediaSource.Factory(dataSourceFactory)
    .setAllowChunklessPreparation(false)
    .createMediaSource(MediaItem.fromUri(hlsUri))
```

### Java

```java
HlsMediaSource hlsMediaSource =
    new HlsMediaSource.Factory(dataSourceFactory)
        .setAllowChunklessPreparation(false)
        .createMediaSource(MediaItem.fromUri(hlsUri));
```

## Creating high quality HLS content

In order to get the most out of ExoPlayer, there are certain guidelines you can
follow to improve your HLS content. Read our [Medium post about HLS playback in
ExoPlayer](https://medium.com/google-exoplayer/hls-playback-in-exoplayer-a33959a47be7) for a full explanation. The main points are:

- Use precise segment durations.
- Use a continuous media stream; avoid changes in the media structure across segments.
- Use the `#EXT-X-INDEPENDENT-SEGMENTS` tag.
- Prefer demuxed streams, as opposed to files that include both video and audio.
- Include all information you can in the Multivariant Playlist.

The following guidelines apply specifically for live streams:

- Use the `#EXT-X-PROGRAM-DATE-TIME` tag.
- Use the `#EXT-X-DISCONTINUITY-SEQUENCE` tag.
- Provide a long live window. One minute or more is great.