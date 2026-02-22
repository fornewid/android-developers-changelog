---
title: https://developer.android.com/media/media3/exoplayer/network-stacks
url: https://developer.android.com/media/media3/exoplayer/network-stacks
source: md.txt
---

ExoPlayer is commonly used for streaming media over the internet. It supports
multiple network stacks for making its underlying network requests. Your choice
of network stack can have a significant impact on streaming performance.

This page outlines how to configure ExoPlayer to use your network stack of
choice, lists the available options, provides some guidance on how to choose
a network stack for your app, and explains how to enable caching for streamed
media.

## Configuring ExoPlayer to use a specific network stack

ExoPlayer loads data through `DataSource` components, which it obtains from
`DataSource.Factory` instances that are injected from app code.

If your app only needs to play http(s) content, selecting a network
stack is as simple as updating any `DataSource.Factory` instances that your
app injects to be instances of the `HttpDataSource.Factory`
that corresponds to the network stack you wish to use. If your app also
needs to play non-http(s) content, such as local files, use
`DefaultDataSource.Factory`:

### Kotlin

```kotlin
DefaultDataSource.Factory(
  context,
  /* baseDataSourceFactory= */ PreferredHttpDataSource.Factory(context),
)
```

### Java

```java
new DefaultDataSource.Factory(
    context, /* baseDataSourceFactory= */ new PreferredHttpDataSource.Factory(context));
```

In this example, `PreferredHttpDataSource.Factory` is the factory corresponding to your
preferred network stack. The `DefaultDataSource.Factory` layer adds in support
for non-http(s) sources such as local files.

The following example shows how to build an `ExoPlayer` that will use the Cronet
network stack and also support playback of non-http(s) content.

### Kotlin

```kotlin
// Given a CronetEngine and Executor, build a CronetDataSource.Factory.
val cronetDataSourceFactory = CronetDataSource.Factory(cronetEngine, executor)

// Wrap the CronetDataSource.Factory in a DefaultDataSource.Factory, which adds
// in support for requesting data from other sources (such as files, resources,
// etc).
val dataSourceFactory =
  DefaultDataSource.Factory(context, /* baseDataSourceFactory= */ cronetDataSourceFactory)

// Inject the DefaultDataSource.Factory when creating the player.
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setDataSourceFactory(dataSourceFactory)
    )
    .build()
```

### Java

```java
// Given a CronetEngine and Executor, build a CronetDataSource.Factory.
CronetDataSource.Factory cronetDataSourceFactory =
    new CronetDataSource.Factory(cronetEngine, executor);

// Wrap the CronetDataSource.Factory in a DefaultDataSource.Factory, which adds
// in support for requesting data from other sources (such as files, resources,
// etc).
DefaultDataSource.Factory dataSourceFactory =
    new DefaultDataSource.Factory(
        context, /* baseDataSourceFactory= */ cronetDataSourceFactory);

// Inject the DefaultDataSource.Factory when creating the player.
ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context).setDataSourceFactory(dataSourceFactory))
        .build();
```

## Supported network stacks

ExoPlayer provides direct support for HttpEngine, Cronet, OkHttp, and Android's
built-in default network stack. ExoPlayer can also be extended to support any
other network stack that works on Android.

### HttpEngine

[`HttpEngine`](https://developer.android.com/reference/android/net/http/HttpEngine)
is the recommended default network stack on Android from API 34 (or S
extensions 7). In most cases, it is using the Cronet network stack internally,
supporting HTTP, HTTP/2, and HTTP/3 over QUIC protocols.

ExoPlayer supports `HttpEngine` with its `HttpEngineDataSource.Factory`. You can
inject this data source factory as described in [Configuring ExoPlayer to use a
specific network stack](https://developer.android.com/media/media3/exoplayer/network-stacks#configuring-exoplayer).

### Cronet

[Cronet](https://developer.android.com/guide/topics/connectivity/cronet) is the
Chromium network stack made available to Android apps as a library. Cronet takes
advantage of multiple technologies that reduce the latency and increase the
throughput of the network requests that your app needs to work, including those
made by ExoPlayer. It natively supports the HTTP, HTTP/2, and HTTP/3 over QUIC
protocols. Cronet is used by some of the world's biggest streaming apps,
including YouTube.

ExoPlayer supports Cronet via its
[Cronet library](https://github.com/androidx/media/tree/main/libraries/datasource_cronet).
See the library's `README.md` for detailed instructions on how to use
it. Note that the Cronet library is able to use three underlying Cronet
implementations:

1. **Google Play Services:** We recommend using this implementation in most cases, and falling back to Android's built-in network stack (`DefaultHttpDataSource`) if Google Play Services is not available.
2. **Cronet Embedded:** May be a good choice if a large percentage of your users are in markets where Google Play Services is not widely available, or if you want to control the exact version of the Cronet implementation being used. The major disadvantage of Cronet Embedded is that it adds approximately 8MB to your app.
3. **Cronet Fallback:** The fallback implementation of Cronet implements Cronet's API as a wrapper around Android's built-in network stack. It should not be used with ExoPlayer, since using Android's built-in network stack directly (by using `DefaultHttpDataSource`) is more efficient.

### OkHttp

[OkHttp](https://square.github.io/okhttp/) is another modern network stack that
is widely used by many popular Android apps. It supports HTTP and
HTTP/2, but does not yet support HTTP/3 over QUIC.

ExoPlayer supports OkHttp through its
[OkHttp library](https://github.com/androidx/media/tree/main/libraries/datasource_okhttp).
See the library's `README.md` for detailed instructions on how to use
it. When using the OkHttp library, the network stack is embedded within the
app. This is similar to Cronet Embedded, however OkHttp is significantly
smaller, adding under 1MB to your app.

### Android's built-in network stack

> [!NOTE]
> **Note:** On API 34 (or S extensions 7) and above, the recommended built-in network stack is [HttpEngine](https://developer.android.com/media/media3/exoplayer/network-stacks#httpengine).

ExoPlayer supports use of Android's built-in network stack with
`DefaultHttpDataSource` and `DefaultHttpDataSource.Factory`, which are part of
the core ExoPlayer library.

The exact network stack implementation depends on the software running on the
underlying device. On most devices only HTTP is supported (that is,
HTTP/2 and HTTP/3 over QUIC are not supported).

### Other network stacks

Apps can also integrate other network stacks with ExoPlayer.
To do this, implement an `HttpDataSource` that wraps the network stack,
together with a corresponding `HttpDataSource.Factory`. ExoPlayer's Cronet and
OkHttp libraries are good examples of how to do this.

When integrating with a pure Java network stack, it's a good idea to implement a
`DataSourceContractTest` to check that your `HttpDataSource` implementation
behaves correctly. `OkHttpDataSourceContractTest` in the OkHttp library is a
good example of how to do this.

## Choosing a network stack

The following table outlines the pros and cons of the network stacks supported by
ExoPlayer.

| Network stack | Protocols | APK size impact | Notes |
|---|---|---|---|
| HttpEngine | HTTP HTTP/2 HTTP/3 over QUIC | None | Only available on API 34, or S Extensions 7 |
| Cronet (Google Play Services) | HTTP HTTP/2 HTTP/3 over QUIC | Small (\<100KB) | Requires Google Play Services. Cronet version updated automatically |
| Cronet (Embedded) | HTTP HTTP/2 HTTP/3 over QUIC | Large (\~8MB) | Cronet version controlled by app developer |
| Cronet (Fallback) | HTTP (varies by device) | Small (\<100KB) | Not recommended for ExoPlayer |
| OkHttp | HTTP HTTP/2 | Small (\<1MB) |   |
| Built-in network stack | HTTP (varies by device) | None | Implementation varies by device |

The HTTP/2 and HTTP/3 over QUIC protocols can significantly improve media
streaming performance. In particular, when streaming adaptive media that is
distributed using a content distribution network (CDN), there are cases for
which use of these protocols can allow CDNs to operate much more efficiently.
For this reason, HttpEngine's and Cronet's support for both HTTP/2 and HTTP/3
over QUIC (and OkHttp's support for HTTP/2), is a major benefit compared to
using Android's built-in network stack, provided the servers on which the
content is hosted also support these protocols.

When considering media streaming in isolation, we recommend use of HttpEngine or
Cronet provided by Google Play Services falling back to `DefaultHttpDataSource`
if Google Play Services is unavailable. This recommendation strikes a good
balance between enabling use of HTTP/2 and HTTP/3 over QUIC on most devices, and
avoiding a significant increase in APK size. There are exceptions to this
recommendation. For cases where Google Play Services is likely to be unavailable
on a significant fraction of devices that will be running your app,
using Cronet Embedded or OkHttp may be more appropriate. Use of the built-in
network stack may be acceptable if APK size is a critical concern, or if media
streaming is only a minor part of your app's functionality.

Beyond just media, it's normally a good idea to choose a single network stack
for all of the networking performed by your app. This allows resources
(such as sockets) to be efficiently pooled and shared between ExoPlayer and other
app components.

> [!NOTE]
> **Note:** To assist with resource sharing, it's recommended to use a single `HttpEngine`, `CronetEngine` or `OkHttpClient` instance throughout your app, when using HttpEngine, Cronet or OkHttp respectively.

Because your app will most likely need to perform networking not related
to media playback, your choice of network stack should ultimately factor in our
recommendations above for media streaming in isolation, the requirements of any
other components that perform networking, and their relative importance to your
app.

## Caching media

ExoPlayer supports caching loaded bytes to disk to prevent repeatedly loading
the same bytes from network. This is useful when seeking back in the current
media or repeating the same item.

> [!NOTE]
> **Note:** You can also download media more permanently outside of playback as explained in [Downloading Media](https://developer.android.com/media/media3/exoplayer/downloading-media).

Caching requires a `SimpleCache` instance pointing to a dedicated cache
directory and a `CacheDataSource.Factory`:

### Kotlin

```kotlin
// Note: This should be a singleton in your app.
val databaseProvider = StandaloneDatabaseProvider(context)

// An on-the-fly cache should evict media when reaching a maximum disk space limit.
val cache =
  SimpleCache(downloadDirectory, LeastRecentlyUsedCacheEvictor(maxBytes), databaseProvider)

// Configure the DataSource.Factory with the cache and factory for the desired HTTP stack.
val cacheDataSourceFactory =
  CacheDataSource.Factory().setCache(cache).setUpstreamDataSourceFactory(httpDataSourceFactory)

// Inject the DefaultDataSource.Factory when creating the player.
val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setDataSourceFactory(cacheDataSourceFactory)
    )
    .build()
```

### Java

```java
// Note: This should be a singleton in your app.
DatabaseProvider databaseProvider = new StandaloneDatabaseProvider(context);

// An on-the-fly cache should evict media when reaching a maximum disk space limit.
Cache cache =
    new SimpleCache(
        downloadDirectory, new LeastRecentlyUsedCacheEvictor(maxBytes), databaseProvider);

// Configure the DataSource.Factory with the cache and factory for the desired HTTP stack.
DataSource.Factory cacheDataSourceFactory =
    new CacheDataSource.Factory()
        .setCache(cache)
        .setUpstreamDataSourceFactory(httpDataSourceFactory);

// Inject the DefaultDataSource.Factory when creating the player.
ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context).setDataSourceFactory(cacheDataSourceFactory))
        .build();
```