---
title: https://developer.android.com/media/media3/exoplayer/customization
url: https://developer.android.com/media/media3/exoplayer/customization
source: md.txt
---

At the core of the ExoPlayer library is the `Player` interface. A `Player`
exposes traditional high-level media player functionality such as the ability to
buffer media, play, pause and seek. The default implementation `ExoPlayer` is
designed to make few assumptions about (and hence impose few restrictions on)
the type of media being played, how and where it is stored, and how it is
rendered. Rather than implementing the loading and rendering of media directly,
`ExoPlayer` implementations delegate this work to components that are injected
when a player is created or when new media sources are passed to the player.
Components common to all `ExoPlayer` implementations are:

- `MediaSource` instances that define media to be played, load the media, and from which the loaded media can be read. A `MediaSource` instance is created from a `MediaItem` by a `MediaSource.Factory` inside the player. They can also be passed directly to the player using the [media source based playlist API](https://developer.android.com/guide/topics/media/exoplayer/media-sources#media-source-based-playlist-api).
- A `MediaSource.Factory` instances that converts a `MediaItem` to a `MediaSource`. The `MediaSource.Factory` is injected when the player is created.
- `Renderer` instances that render individual components of the media. These are injected when the player is created.
- A `TrackSelector` that selects tracks provided by the `MediaSource` to be consumed by each available `Renderer`. A `TrackSelector` is injected when the player is created.
- A `LoadControl` that controls when the `MediaSource` buffers more media, and how much media is buffered. A `LoadControl` is injected when the player is created.
- A `LivePlaybackSpeedControl` that controls the playback speed during live playbacks to allow the player to stay close to a configured live offset. A `LivePlaybackSpeedControl` is injected when the player is created.

The concept of injecting components that implement pieces of player
functionality is present throughout the library. The default implementations of
some components delegate work to further injected components. This allows many
sub-components to be individually replaced with implementations that are
configured in a custom way.

## Player customization

Some common examples of customizing the player by injecting components are
described below.

### Configuring the network stack

We have a page about [customizing the network stack used by ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer/network-stacks).

### Caching data loaded from the network

See the guides for
[temporary on-the-fly caching](https://developer.android.com/media/media3/exoplayer/network-stacks#caching)
and [downloading media](https://developer.android.com/media/media3/exoplayer/downloading-media).

### Customizing server interactions

Some apps may want to intercept HTTP requests and responses. You may want to
inject custom request headers, read the server's response headers, modify the
requests' URIs, etc. For example, your app may authenticate itself by injecting
a token as a header when requesting the media segments.

The following example demonstrates how to implement these behaviors by
injecting a custom `DataSource.Factory` into the `DefaultMediaSourceFactory`:

### Kotlin

```kotlin
val dataSourceFactory =
  DataSource.Factory {
    val dataSource = httpDataSourceFactory.createDataSource()
    // Set a custom authentication request header.
    dataSource.setRequestProperty("Header", "Value")
    dataSource
  }
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setDataSourceFactory(dataSourceFactory)
    )
    .build()
```

### Java

```java
DataSource.Factory dataSourceFactory =
    () -> {
      HttpDataSource dataSource = httpDataSourceFactory.createDataSource();
      // Set a custom authentication request header.
      dataSource.setRequestProperty("Header", "Value");
      return dataSource;
    };

ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context).setDataSourceFactory(dataSourceFactory))
        .build();
```

In the code snippet above, the injected `HttpDataSource` includes the header
`"Header: Value"` in every HTTP request. This behavior is *fixed* for every
interaction with an HTTP source.

For a more granular approach, you can inject just-in-time behavior using a
`ResolvingDataSource`. The following code snippet shows how to inject
request headers just before interacting with an HTTP source:

### Kotlin

```kotlin
val dataSourceFactory: DataSource.Factory =
  ResolvingDataSource.Factory(httpDataSourceFactory) { dataSpec: DataSpec ->
    // Provide just-in-time request headers.
    dataSpec.withRequestHeaders(getCustomHeaders(dataSpec.uri))
  }
```

### Java

```java
DataSource.Factory dataSourceFactory =
    new ResolvingDataSource.Factory(
        httpDataSourceFactory,
        // Provide just-in-time request headers.
        dataSpec -> dataSpec.withRequestHeaders(getCustomHeaders(dataSpec.uri)));
```

You may also use a `ResolvingDataSource` to perform
just-in-time modifications of the URI, as shown in the following snippet:

### Kotlin

```kotlin
val dataSourceFactory: DataSource.Factory =
  ResolvingDataSource.Factory(httpDataSourceFactory) { dataSpec: DataSpec ->
    // Provide just-in-time URI resolution logic.
    dataSpec.withUri(resolveUri(dataSpec.uri))
  }
```

### Java

```java
DataSource.Factory dataSourceFactory =
    new ResolvingDataSource.Factory(
        httpDataSourceFactory,
        // Provide just-in-time URI resolution logic.
        dataSpec -> dataSpec.withUri(resolveUri(dataSpec.uri)));
```

### Customizing error handling

Implementing a custom [`LoadErrorHandlingPolicy`](https://developer.android.com/reference/androidx/media3/exoplayer/upstream/LoadErrorHandlingPolicy) allows apps to customize the
way ExoPlayer reacts to load errors. For example, an app may want to fail fast
instead of retrying many times, or may want to customize the back-off logic that
controls how long the player waits between each retry. The following snippet
shows how to implement custom back-off logic:

### Kotlin

```kotlin
val loadErrorHandlingPolicy: LoadErrorHandlingPolicy =
  object : DefaultLoadErrorHandlingPolicy() {
    override fun getRetryDelayMsFor(
      loadErrorInfo: LoadErrorHandlingPolicy.LoadErrorInfo
    ): Long {
      // Implement custom back-off logic here.
      return 0
    }
  }
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setLoadErrorHandlingPolicy(loadErrorHandlingPolicy)
    )
    .build()
```

### Java

```java
LoadErrorHandlingPolicy loadErrorHandlingPolicy =
    new DefaultLoadErrorHandlingPolicy() {
      @Override
      public long getRetryDelayMsFor(LoadErrorHandlingPolicy.LoadErrorInfo loadErrorInfo) {
        // Implement custom back-off logic here.
        return 0;
      }
    };

ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context)
                .setLoadErrorHandlingPolicy(loadErrorHandlingPolicy))
        .build();
```

The `LoadErrorInfo` argument contains more information about the failed load to
customize the logic based on the error type or the failed request.

### Customizing extractor flags

Extractor flags can be used to customize how individual formats are extracted
from progressive media. They can be set on the `DefaultExtractorsFactory` that's
provided to the `DefaultMediaSourceFactory`. The following example passes a flag
that enables index-based seeking for MP3 streams.

### Kotlin

```kotlin
val extractorsFactory =
  DefaultExtractorsFactory().setMp3ExtractorFlags(Mp3Extractor.FLAG_ENABLE_INDEX_SEEKING)
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(DefaultMediaSourceFactory(context, extractorsFactory))
    .build()
```

### Java

```java
DefaultExtractorsFactory extractorsFactory =
    new DefaultExtractorsFactory().setMp3ExtractorFlags(Mp3Extractor.FLAG_ENABLE_INDEX_SEEKING);

ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(new DefaultMediaSourceFactory(context, extractorsFactory))
        .build();
```

### Enabling constant bitrate seeking

For MP3, ADTS and AMR streams, you can enable approximate seeking using a
constant bitrate assumption with `FLAG_ENABLE_CONSTANT_BITRATE_SEEKING` flags.
These flags can be set for individual extractors using the individual
`DefaultExtractorsFactory.setXyzExtractorFlags` methods as described above. To
enable constant bitrate seeking for all extractors that support it, use
`DefaultExtractorsFactory.setConstantBitrateSeekingEnabled`.

### Kotlin

```kotlin
val extractorsFactory = DefaultExtractorsFactory().setConstantBitrateSeekingEnabled(true)
```

### Java

```java
DefaultExtractorsFactory extractorsFactory =
    new DefaultExtractorsFactory().setConstantBitrateSeekingEnabled(true);
```

The `ExtractorsFactory` can then be injected via `DefaultMediaSourceFactory` as
described for customizing extractor flags above.

### Enabling asynchronous buffer queueing

Asynchronous buffer queueing is an enhancement in ExoPlayer's rendering
pipeline, which operates `MediaCodec` instances in [asynchronous mode](https://developer.android.com/reference/android/media/MediaCodec#asynchronous-processing-using-buffers) and
uses additional threads to schedule decoding and rendering of data. Enabling it
can reduce dropped frames and audio underruns.

Asynchronous buffer queueing is enabled by default on devices running Android 12
(API level 31) and above, and can be enabled manually starting with Android 6.0 (API level 23).
Consider enabling the feature for specific devices on which you observe dropped
frames or audio underruns, particularly when playing DRM protected or high-frame-rate
content.

In the simplest case, you need to inject a `DefaultRenderersFactory` to the
player as follows:

### Kotlin

```kotlin
val renderersFactory =
  DefaultRenderersFactory(context).forceEnableMediaCodecAsynchronousQueueing()
val exoPlayer = ExoPlayer.Builder(context, renderersFactory).build()
```

### Java

```java
DefaultRenderersFactory renderersFactory =
    new DefaultRenderersFactory(context).forceEnableMediaCodecAsynchronousQueueing();
ExoPlayer exoPlayer = new ExoPlayer.Builder(context, renderersFactory).build();
```

If you're instantiating renderers directly, pass
`new DefaultMediaCodecAdapter.Factory(context).forceEnableAsynchronous()` to the
`MediaCodecVideoRenderer` and `MediaCodecAudioRenderer` constructors.

### Customizing operations with `ForwardingSimpleBasePlayer`

You can customize some of the behavior of a `Player` instance by wrapping it in
a subclass of `ForwardingSimpleBasePlayer`. This class lets you intercept
specific 'operations', rather than directly having to implement `Player`
methods. This ensures consistent behaviour of, for example, `play()`, `pause()`
and `setPlayWhenReady(boolean)`. It also ensures all state changes are correctly
propagated to registered `Player.Listener` instances. For most customization
use-cases `ForwardingSimpleBasePlayer` should be preferred to the more
error-prone `ForwardingPlayer` due to these consistency guarantees.

For example, to add some custom logic when playback is started or stopped:

### Kotlin

```kotlin
class PlayerWithCustomPlay(player: Player) : ForwardingSimpleBasePlayer(player) {
  override fun handleSetPlayWhenReady(playWhenReady: Boolean): ListenableFuture<*> {
    // Add custom logic
    return super.handleSetPlayWhenReady(playWhenReady)
  }
}
```

### Java

```java
public static final class PlayerWithCustomPlay extends ForwardingSimpleBasePlayer {

  public PlayerWithCustomPlay(Player player) {
    super(player);
  }

  @Override
  protected ListenableFuture<?> handleSetPlayWhenReady(boolean playWhenReady) {
    // Add custom logic
    return super.handleSetPlayWhenReady(playWhenReady);
  }
}
```

Or to disallow the `SEEK_TO_NEXT` command (and ensure `Player.seekToNext` is a
no-op):

### Kotlin

```kotlin
class PlayerWithoutSeekToNext(player: Player) : ForwardingSimpleBasePlayer(player) {
  override fun getState(): State {
    val state = super.getState()
    return state
      .buildUpon()
      .setAvailableCommands(
        state.availableCommands.buildUpon().remove(COMMAND_SEEK_TO_NEXT).build()
      )
      .build()
  }

  // We don't need to override handleSeek, because it is guaranteed not to be called for
  // COMMAND_SEEK_TO_NEXT since we've marked that command unavailable.
}
```

### Java

```java
public static final class PlayerWithoutSeekToNext extends ForwardingSimpleBasePlayer {

  public PlayerWithoutSeekToNext(Player player) {
    super(player);
  }

  @Override
  protected State getState() {
    State state = super.getState();
    return state
        .buildUpon()
        .setAvailableCommands(
            state.availableCommands.buildUpon().remove(COMMAND_SEEK_TO_NEXT).build())
        .build();
  }

  // We don't need to override handleSeek, because it is guaranteed not to be called for
  // COMMAND_SEEK_TO_NEXT since we've marked that command unavailable.
}
```

## MediaSource customization

The examples above inject customized components for use during playback of all
`MediaItem` objects that are passed to the player. Where fine-grained customization is
required, it's also possible to inject customized components into individual
`MediaSource` instances, which can be passed directly to the player. The example
below shows how to customize a `ProgressiveMediaSource` to use a custom
`DataSource.Factory`, `ExtractorsFactory` and `LoadErrorHandlingPolicy`:

### Kotlin

```kotlin
val mediaSource =
  ProgressiveMediaSource.Factory(customDataSourceFactory, customExtractorsFactory)
    .setLoadErrorHandlingPolicy(customLoadErrorHandlingPolicy)
    .createMediaSource(MediaItem.fromUri(streamUri))
```

### Java

```java
ProgressiveMediaSource mediaSource =
    new ProgressiveMediaSource.Factory(customDataSourceFactory, customExtractorsFactory)
        .setLoadErrorHandlingPolicy(customLoadErrorHandlingPolicy)
        .createMediaSource(MediaItem.fromUri(streamUri));
```

## Creating custom components

The library provides default implementations of the components listed at the top
of this page for common use cases. An `ExoPlayer` can use these components, but
may also be built to use custom implementations if non-standard behaviors are
required. Some use cases for custom implementations are:

- `Renderer` -- You may want to implement a custom `Renderer` to handle a media type not supported by the default implementations provided by the library.
- `TrackSelector` -- Implementing a custom `TrackSelector` allows an app developer to change the way in which tracks exposed by a `MediaSource` are selected for consumption by each of the available `Renderer`s.
- `LoadControl` -- Implementing a custom `LoadControl` allows an app developer to change the player's buffering policy.
- `Extractor` -- If you need to support a container format not currently supported by the library, consider implementing a custom `Extractor` class.
- `MediaSource` -- Implementing a custom `MediaSource` class may be appropriate if you wish to obtain media samples to feed to renderers in a custom way, or if you wish to implement custom `MediaSource` compositing behavior.
- `MediaSource.Factory` -- Implementing a custom `MediaSource.Factory` allows an application to customize the way in which a `MediaSource` is created from a `MediaItem`.
- `DataSource` -- ExoPlayer's upstream package already contains a number of `DataSource` implementations for different use cases. You may want to implement you own `DataSource` class to load data in another way, such as over a custom protocol, using a custom HTTP stack, or from a custom persistent cache.

When building custom components, we recommend the following:

- If a custom component needs to report events back to the app, we recommend that you do so using the same model as existing ExoPlayer components, for example using `EventDispatcher` classes or passing a `Handler` together with a listener to the constructor of the component.
- We recommended that custom components use the same model as existing ExoPlayer components to allow reconfiguration by the app during playback. To do this, custom components should implement `PlayerMessage.Target` and receive configuration changes in the `handleMessage` method. Application code should pass configuration changes by calling ExoPlayer's `createMessage` method, configuring the message, and sending it to the component using `PlayerMessage.send`. Sending messages to be delivered on the playback thread ensures that they are executed in order with any other operations being performed on the player.