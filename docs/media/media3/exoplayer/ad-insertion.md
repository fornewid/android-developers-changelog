---
title: https://developer.android.com/media/media3/exoplayer/ad-insertion
url: https://developer.android.com/media/media3/exoplayer/ad-insertion
source: md.txt
---

ExoPlayer can be used for both client-side and server-side ad insertion.

## Client-side ad insertion

In client-side ad insertion, the player switches between loading media from
different URLs as it transitions between playing content and ads. Information
about ads is loaded separately from the media, such as from an XML [VAST](https://www.iab.com/wp-content/uploads/2015/06/VASTv3_0.pdf) or
[VMAP](https://www.iab.com/guidelines/digital-video-multiple-ad-playlist-vmap-1-0-1/) ad tag. This can include ad cue positions relative to the start of the
content, the actual ad media URIs and metadata such as whether a given ad is
skippable.

When using ExoPlayer's `AdsMediaSource` for client-side ad insertion, the player
has information about the ads to be played. This has several benefits:

- The player can expose metadata and functionality relating to ads using its API.
- [ExoPlayer UI components](https://developer.android.com/guide/topics/media/ui/playerview) can show markers for ad positions automatically, and change their behavior depending on whether ad is playing.
- Internally, the player can keep a consistent buffer across transitions between ads and content.

In this setup, the player takes care of switching between ads and content, which
means that apps don't need to take care of controlling multiple separate
background/foreground players for ads and content.

When preparing content videos and ad tags for use with client-side ad insertion,
ads should ideally be positioned at synchronization samples (keyframes) in the
content video so that the player can resume content playback seamlessly.

### Declarative ad support

An ad tag URI can be specified when building a `MediaItem`:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setUri(videoUri)
    .setAdsConfiguration(MediaItem.AdsConfiguration.Builder(adTagUri).build())
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setAdsConfiguration(new MediaItem.AdsConfiguration.Builder(adTagUri).build())
        .build();
```

To enable player support for media items that specify ad tags, it's necessary to
build and inject a `DefaultMediaSourceFactory` configured with an
`AdsLoader.Provider` and an `AdViewProvider` when creating the player:

### Kotlin

```kotlin
val mediaSourceFactory: MediaSource.Factory =
  DefaultMediaSourceFactory(context)
    .setLocalAdInsertionComponents(adsLoaderProvider, playerView)
val player = ExoPlayer.Builder(context).setMediaSourceFactory(mediaSourceFactory).build()
```

### Java

```java
MediaSource.Factory mediaSourceFactory =
    new DefaultMediaSourceFactory(context)
        .setLocalAdInsertionComponents(adsLoaderProvider, /* adViewProvider= */ playerView);
ExoPlayer player =
    new ExoPlayer.Builder(context).setMediaSourceFactory(mediaSourceFactory).build();
```

Internally, `DefaultMediaSourceFactory` will wrap the content media source in an
`AdsMediaSource`. The `AdsMediaSource` will obtain an `AdsLoader` from the
`AdsLoader.Provider` and use it to insert ads as defined by the media item's ad
tag.

ExoPlayer's `PlayerView` implements `AdViewProvider`. The ExoPlayer IMA library
provides an easy to use `AdsLoader`, as described below.

### Playlists with ads

When playing a [playlist](https://developer.android.com/guide/topics/media/exoplayer/playlists) with multiple media items, the default behavior is
to request the ad tag and store ad playback state once for each media ID,
content URI, and ad tag URI combination. This means that users will see ads for
every media item with ads that has a distinct media ID or content URI, even if
the ad tag URIs match. If a media item is repeated, the user will see the
corresponding ads only once (the ad playback state stores whether ads have been
played, so they are skipped after their first occurrence).

It's possible to customize this behavior by passing an opaque ads identifier
with which ad playback state for a given media item is linked, based on object
equality. Here is an example where ad playback state is linked to the ad tag URI
only, rather than the combination of the media ID and ad tag URI, by passing the
ad tag URI as the ads identifier. The effect is that ads will load only once and
the user will not see ads on the second item when playing the playlist from
start to finish.

### Kotlin

```kotlin
// Build the media items, passing the same ads identifier for both items,
// which means they share ad playback state so ads play only once.
val firstItem =
  MediaItem.Builder()
    .setUri(firstVideoUri)
    .setAdsConfiguration(
      MediaItem.AdsConfiguration.Builder(adTagUri).setAdsId(adTagUri).build()
    )
    .build()
val secondItem =
  MediaItem.Builder()
    .setUri(secondVideoUri)
    .setAdsConfiguration(
      MediaItem.AdsConfiguration.Builder(adTagUri).setAdsId(adTagUri).build()
    )
    .build()
player.addMediaItem(firstItem)
player.addMediaItem(secondItem)
```

### Java

```java
// Build the media items, passing the same ads identifier for both items,
// which means they share ad playback state so ads play only once.
MediaItem firstItem =
    new MediaItem.Builder()
        .setUri(firstVideoUri)
        .setAdsConfiguration(
            new MediaItem.AdsConfiguration.Builder(adTagUri).setAdsId(adTagUri).build())
        .build();
MediaItem secondItem =
    new MediaItem.Builder()
        .setUri(secondVideoUri)
        .setAdsConfiguration(
            new MediaItem.AdsConfiguration.Builder(adTagUri).setAdsId(adTagUri).build())
        .build();
player.addMediaItem(firstItem);
player.addMediaItem(secondItem);
```

### Server-guided client-side ad insertion

ExoPlayer comes with `HlsInterstitialsAdsLoader` that supports ads defined in
the HLS playlist to be inserted on the client side automatically. See
the section about `HlsInterstitialsAdsLoader` on the [HLS page](https://developer.android.com/media/media3/exoplayer/hls#interstitials).

### ExoPlayer IMA library

The [ExoPlayer IMA library](https://github.com/androidx/media/tree/release/libraries/exoplayer_ima) provides `ImaAdsLoader`, making it easy to
integrate client-side ad insertion into your app. It wraps the functionality of
the [client-side IMA SDK](https://developers.google.com/interactive-media-ads/docs/sdks/android) to support insertion of VAST/VMAP ads. For
instructions on how to use the library, including how to handle backgrounding
and resuming playback, please see the [README](https://github.com/androidx/media/tree/release/libraries/exoplayer_ima).

The [demo application](https://developer.android.com/guide/topics/media/exoplayer/demo-application) uses the IMA library, and includes several sample
VAST/VMAP ad tags in the sample list.

> [!IMPORTANT]
> **Important:** To improve IMA load times, call the [`ImaSdkFactory.initialize()`](https://developers.google.com/interactive-media-ads/docs/sdks/android/client-side/api/reference/com/google/ads/interactivemedia/v3/api/ImaSdkFactory#initialize(android.content.Context,com.google.ads.interactivemedia.v3.api.ImaSdkSettings)) method as early as possible in the app lifecycle. Calling the method early maximizes the time for IMA to load necessary resources before the first ad request. The `ImaSdkFactory.initialize()` method call accepts an `ImaSdkSettings` instance. Make sure to use the same settings values here, and when you create an `ImaAdsLoader` instance. For more information, see the [Optimize IMA load time guide](https://developers.google.com/interactive-media-ads/docs/sdks/android/client-side/load-time).

#### UI considerations

`PlayerView` hides its transport controls during playback of ads by default, but
apps can toggle this behavior by calling `setControllerHideDuringAds`. The IMA
SDK will show additional views on top of the player while an ad is playing (for
example, a "more info" link and a skip button, if applicable).

> [!NOTE]
> **Note:** Since advertisers expect a consistent experience across apps, the IMA SDK does not allow customization of the views that it shows while an ad is playing. It is therefore not possible to remove or reposition the skip button, change the fonts, or make other customizations to the visual appearance of these views.

The IMA SDK may report whether ads are obscured by application provided views
rendered on top of the player. Apps that need to overlay views that are
essential for controlling playback must register them with the IMA SDK so that
they can be omitted from viewability calculations. When using `PlayerView` as
the `AdViewProvider`, it will automatically register its control overlays. Apps
that use a custom player UI must register overlay views by returning them from
`AdViewProvider.getAdOverlayInfos`.

For more information about overlay views, see [Open Measurement in the IMA
SDK](https://developers.google.com/interactive-media-ads/docs/sdks/android/omsdk).

#### Companion ads

Some ad tags contain additional companion ads that can be shown in 'slots' in an
app UI. These slots can be passed via
`ImaAdsLoader.Builder.setCompanionAdSlots(slots)`. For more information, see
[Adding Companion Ads](https://developers.google.com/interactive-media-ads/docs/sdks/android/companions).

#### Standalone ads

The IMA SDK is designed for inserting ads into media content, not for playing
standalone ads by themselves. Hence playback of standalone ads is not supported
by the IMA library. We recommend using the [Google Mobile Ads SDK](https://developers.google.com/admob/android/quick-start) instead for
this use case.

### Using a third-party ads SDK

If you need to load ads via a third-party ads SDK, it's worth checking whether
it already provides an ExoPlayer integration. If not, implementing a custom
`AdsLoader` that wraps the third-party ads SDK is the recommended approach,
since it provides the benefits of `AdsMediaSource` described above.
`ImaAdsLoader` acts as an example implementation.

Alternatively, you can use ExoPlayer's [playlist support](https://developer.android.com/guide/topics/media/exoplayer/playlists) to build a sequence
of ads and content clips:

### Kotlin

```kotlin
// A pre-roll ad.
val preRollAd = MediaItem.fromUri(preRollAdUri)
// The start of the content.
val contentStart =
  MediaItem.Builder()
    .setUri(contentUri)
    .setClippingConfiguration(
      MediaItem.ClippingConfiguration.Builder().setEndPositionMs(120000).build()
    )
    .build()
// A mid-roll ad.
val midRollAd = MediaItem.fromUri(midRollAdUri)
// The rest of the content
val contentEnd =
  MediaItem.Builder()
    .setUri(contentUri)
    .setClippingConfiguration(
      MediaItem.ClippingConfiguration.Builder().setStartPositionMs(120000).build()
    )
    .build()

// Build the playlist.
player.addMediaItem(preRollAd)
player.addMediaItem(contentStart)
player.addMediaItem(midRollAd)
player.addMediaItem(contentEnd)
```

### Java

```java
// A pre-roll ad.
MediaItem preRollAd = MediaItem.fromUri(preRollAdUri);
// The start of the content.
MediaItem contentStart =
    new MediaItem.Builder()
        .setUri(contentUri)
        .setClippingConfiguration(
            new MediaItem.ClippingConfiguration.Builder().setEndPositionMs(120_000).build())
        .build();
// A mid-roll ad.
MediaItem midRollAd = MediaItem.fromUri(midRollAdUri);
// The rest of the content
MediaItem contentEnd =
    new MediaItem.Builder()
        .setUri(contentUri)
        .setClippingConfiguration(
            new MediaItem.ClippingConfiguration.Builder().setStartPositionMs(120_000).build())
        .build();

// Build the playlist.
player.addMediaItem(preRollAd);
player.addMediaItem(contentStart);
player.addMediaItem(midRollAd);
player.addMediaItem(contentEnd);
```

## Server-side ad insertion

In server-side ad insertion (also called dynamic ad insertion, or DAI), the
media stream contains both ads and content. A DASH manifest may point to both
content and ad segments, possibly in separate periods. For HLS, see the Apple
documentation on [incorporating ads into a playlist](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/incorporating_ads_into_a_playlist).

When using server-side ad insertion, the client may need to resolve the media
URL dynamically to get the stitched stream, it may need to display ads overlays
in the UI or it may need to report events to an ads SDK or ad server.

ExoPlayer's `DefaultMediaSourceFactory` can delegate all these tasks to a
server-side ad insertion `MediaSource` for URIs using the `ssai://` scheme:

### Kotlin

```kotlin
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setServerSideAdInsertionMediaSourceFactory(ssaiFactory)
    )
    .build()
```

### Java

```java
Player player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context)
                .setServerSideAdInsertionMediaSourceFactory(ssaiFactory))
        .build();
```

### ExoPlayer IMA library

The [ExoPlayer IMA library](https://github.com/androidx/media/tree/release/libraries/exoplayer_ima) provides `ImaServerSideAdInsertionMediaSource`,
making it easy to integrate with IMA's server-side inserted ad streams in your
app. It wraps the functionality of the [IMA DAI SDK for Android](https://developers.google.com/interactive-media-ads/docs/sdks/android/dai) and fully
integrates the provided ad metadata into the player. For example, this allows
you to use methods like `Player.isPlayingAd()`, listen to content-ad transitions
and let the player handle ad playback logic like skipping already played ads.

In order to use this class, you need to set up the
`ImaServerSideAdInsertionMediaSource.AdsLoader` and the
`ImaServerSideAdInsertionMediaSource.Factory` and connect them to the player:

### Kotlin

```kotlin
// MediaSource.Factory to load the actual media stream.
val defaultMediaSourceFactory = DefaultMediaSourceFactory(context)
// AdsLoader that can be reused for multiple playbacks.
val adsLoader =
  ImaServerSideAdInsertionMediaSource.AdsLoader.Builder(context, adViewProvider).build()
// MediaSource.Factory to create the ad sources for the current player.
val adsMediaSourceFactory =
  ImaServerSideAdInsertionMediaSource.Factory(adsLoader, defaultMediaSourceFactory)
// Configure DefaultMediaSourceFactory to create both IMA DAI sources and
// regular media sources. If you just play IMA DAI streams, you can also use
// adsMediaSourceFactory directly.
defaultMediaSourceFactory.setServerSideAdInsertionMediaSourceFactory(adsMediaSourceFactory)
// Set the MediaSource.Factory on the Player.
val player = ExoPlayer.Builder(context).setMediaSourceFactory(defaultMediaSourceFactory).build()
// Set the player on the AdsLoader
adsLoader.setPlayer(player)
```

### Java

```java
// MediaSource.Factory to load the actual media stream.
DefaultMediaSourceFactory defaultMediaSourceFactory = new DefaultMediaSourceFactory(context);
// AdsLoader that can be reused for multiple playbacks.
ImaServerSideAdInsertionMediaSource.AdsLoader adsLoader =
    new ImaServerSideAdInsertionMediaSource.AdsLoader.Builder(context, adViewProvider).build();
// MediaSource.Factory to create the ad sources for the current player.
ImaServerSideAdInsertionMediaSource.Factory adsMediaSourceFactory =
    new ImaServerSideAdInsertionMediaSource.Factory(adsLoader, defaultMediaSourceFactory);
// Configure DefaultMediaSourceFactory to create both IMA DAI sources and
// regular media sources. If you just play IMA DAI streams, you can also use
// adsMediaSourceFactory directly.
defaultMediaSourceFactory.setServerSideAdInsertionMediaSourceFactory(adsMediaSourceFactory);
// Set the MediaSource.Factory on the Player.
Player player =
    new ExoPlayer.Builder(context).setMediaSourceFactory(defaultMediaSourceFactory).build();
// Set the player on the AdsLoader
adsLoader.setPlayer(player);
```

Load your IMA asset key, or content source id and video id, by building an URL
with `ImaServerSideAdInsertionUriBuilder`:

### Kotlin

```kotlin
val ssaiUri =
  ImaServerSideAdInsertionUriBuilder()
    .setAssetKey(assetKey)
    .setFormat(C.CONTENT_TYPE_HLS)
    .build()
player.setMediaItem(MediaItem.fromUri(ssaiUri))
```

### Java

```java
Uri ssaiUri =
    new ImaServerSideAdInsertionUriBuilder()
        .setAssetKey(assetKey)
        .setFormat(C.CONTENT_TYPE_HLS)
        .build();
player.setMediaItem(MediaItem.fromUri(ssaiUri));
```

Finally, release your ads loader once it's no longer used:

### Kotlin

```kotlin
adsLoader.release()
```

### Java

```java
adsLoader.release();
```

> [!NOTE]
> **Note:** Currently only a single IMA server-side ad insertion stream is supported in the same playlist. You can combine the stream with other media but not with another IMA server-side ad insertion stream.

#### UI considerations

The same [UI considerations as for client-side ad insertion](https://developer.android.com/media/media3/exoplayer/ad-insertion#ui-considerations) apply to
server-side ad insertion too.

#### Companion ads

Some ad tags contain additional companion ads that can be shown in 'slots' in an
app UI. These slots can be passed via
`ImaServerSideAdInsertionMediaSource.AdsLoader.Builder.setCompanionAdSlots(slots)`.
For more information see [Adding Companion Ads](https://developers.google.com/interactive-media-ads/docs/sdks/android/companions).

### Using a third-party ads SDK

If you need to load ads using a third-party ads SDK, it's worth checking whether
it already provides an ExoPlayer integration. If not, it's recommended to
provide a custom `MediaSource` that accepts URIs with the `ssai://` scheme
similar to `ImaServerSideAdInsertionMediaSource`.

The actual logic of creating the ad structure can be delegated to the general
purpose `ServerSideAdInsertionMediaSource`, which wraps a stream `MediaSource`
and allows the user to set and update the `AdPlaybackState` representing the ad
metadata.

Often, server-side inserted ad streams contain timed events to notify the player
about ad metadata. Please see [supported formats](https://developer.android.com/guide/topics/media/exoplayer/supported-formats) for information on what
timed metadata formats are supported by ExoPlayer. Custom ads SDK `MediaSource`
implementations can listen for timed metadata events from the player using
`Player.Listener.onMetadata`.