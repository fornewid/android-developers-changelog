---
title: https://developer.android.com/media/media3/exoplayer/downloading-media
url: https://developer.android.com/media/media3/exoplayer/downloading-media
source: md.txt
---

> [!NOTE]
> **Note:** ExoPlayer also supports on-the-fly caching for streamed media, see [Caching media](https://developer.android.com/media/media3/exoplayer/network-stacks#caching).

ExoPlayer provides functionality to download media for offline playback. In most
use cases, it's desirable for downloads to continue even when your app is in the
background. For these use cases, your app should subclass `DownloadService` and
send commands to the service to add, remove, and control the downloads. The
following diagram shows the main classes that are involved.

![Classes for downloading media. The arrow directions indicate the flow of data.](https://developer.android.com/static/guide/topics/media/exoplayer/images/downloading.svg)

- `DownloadService`: Wraps a `DownloadManager` and forwards commands to it. The service allows the `DownloadManager` to keep running even when the app is in the background.
- `DownloadManager`: Manages multiple downloads, loading (and storing) their states from (and to) a `DownloadIndex`, starting and stopping downloads based on requirements such as network connectivity, and so on. To download the content, the manager will typically read the data being downloaded from a `HttpDataSource`, and write it into a `Cache`.
- `DownloadIndex`: Persists the states of the downloads.

## Creating a DownloadService

To create a `DownloadService`, subclass it and implement its
abstract methods:

- `getDownloadManager()`: Returns the `DownloadManager` to be used.
- `getScheduler()`: Returns an optional `Scheduler`, which can restart the service when requirements needed for pending downloads to progress are met. ExoPlayer provides these implementations:
  - `PlatformScheduler`, which uses [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler) (Minimum API is 21). See the [PlatformScheduler](https://developer.android.com/reference/androidx/media3/scheduler/PlatformScheduler) javadocs for app permission requirements.
  - `WorkManagerScheduler`, which uses [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager).
- `getForegroundNotification()`: Returns a notification to be displayed when the service is running in the foreground. You can use `DownloadNotificationHelper.buildProgressNotification` to create a notification in default style.

Finally, define the service in your `AndroidManifest.xml` file:

    <uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC"/>
    <application>
      <service android:name="com.myapp.MyDownloadService"
          android:exported="false"
          android:foregroundServiceType="dataSync">
        <!-- This is needed for Scheduler -->
        <intent-filter>
          <action android:name="androidx.media3.exoplayer.downloadService.action.RESTART"/>
          <category android:name="android.intent.category.DEFAULT"/>
        </intent-filter>
      </service>
    </application>

See [`DemoDownloadService`](https://github.com/androidx/media/tree/release/demos/main/src/main/java/androidx/media3/demo/main/DemoDownloadService.java) and [`AndroidManifest.xml`](https://github.com/androidx/media/tree/release/demos/main/src/main/AndroidManifest.xml) in the ExoPlayer
demo app for a concrete example.

## Creating a DownloadManager

The following code snippet demonstrates how to instantiate a `DownloadManager`,
which can be returned by `getDownloadManager()` in your `DownloadService`:

### Kotlin

```kotlin
// Note: This should be a singleton in your app.
val databaseProvider = StandaloneDatabaseProvider(context)

// A download cache should not evict media, so should use a NoopCacheEvictor.
val downloadCache = SimpleCache(downloadDirectory, NoOpCacheEvictor(), databaseProvider)

// Create a factory for reading the data from the network.
val dataSourceFactory = DefaultHttpDataSource.Factory()

// Choose an executor for downloading data. Using Runnable::run will cause each download task to
// download data on its own thread. Passing an executor that uses multiple threads will speed up
// download tasks that can be split into smaller parts for parallel execution. Applications that
// already have an executor for background downloads may wish to reuse their existing executor.
val downloadExecutor = Executor(Runnable::run)

// Create the download manager.
val downloadManager =
  DownloadManager(context, databaseProvider, downloadCache, dataSourceFactory, downloadExecutor)

// Optionally, properties can be assigned to configure the download manager.
downloadManager.requirements = requirements
downloadManager.maxParallelDownloads = 3
```

### Java

```java
// Note: This should be a singleton in your app.
databaseProvider = new StandaloneDatabaseProvider(context);

// A download cache should not evict media, so should use a NoopCacheEvictor.
downloadCache = new SimpleCache(downloadDirectory, new NoOpCacheEvictor(), databaseProvider);

// Create a factory for reading the data from the network.
dataSourceFactory = new DefaultHttpDataSource.Factory();

// Choose an executor for downloading data. Using Runnable::run will cause each download task to
// download data on its own thread. Passing an executor that uses multiple threads will speed up
// download tasks that can be split into smaller parts for parallel execution. Applications that
// already have an executor for background downloads may wish to reuse their existing executor.
Executor downloadExecutor = Runnable::run;

// Create the download manager.
downloadManager =
    new DownloadManager(
        context, databaseProvider, downloadCache, dataSourceFactory, downloadExecutor);

// Optionally, setters can be called to configure the download manager.
downloadManager.setRequirements(requirements);
downloadManager.setMaxParallelDownloads(3);
```

See [`DemoUtil`](https://github.com/androidx/media/tree/release/demos/main/src/main/java/androidx/media3/demo/main/DemoUtil.java) in the demo app for a concrete example.

## Adding a download

To add a download, create a `DownloadRequest` and send it to your
`DownloadService`. For adaptive streams, [use `DownloadHelper` to help
build a `DownloadRequest`](https://developer.android.com/media/media3/exoplayer/downloading-media#dl-play-adaptive-streams). The following
example shows how to create a download request:

### Kotlin

```kotlin
val downloadRequest = DownloadRequest.Builder(contentId, contentUri).build()
```

### Java

```java
DownloadRequest downloadRequest = new DownloadRequest.Builder(contentId, contentUri).build();
```

In this example, `contentId` is a unique identifier for the content. In simple cases, the
`contentUri` can often be used as the `contentId`, however apps are free to use
whatever ID scheme best suits their use case. `DownloadRequest.Builder` also has
some optional setters. For example, `setKeySetId` and `setData` can be used to
set DRM and custom data that the app wishes to associate with the download,
respectively. The content's MIME type can also be specified using `setMimeType`,
as a hint for cases where the content type cannot be inferred from `contentUri`.

Once created, the request can be sent to the `DownloadService` to add the
download:

### Kotlin

```kotlin
DownloadService.sendAddDownload(
  context,
  MyDownloadService::class.java,
  downloadRequest,
  /* foreground= */ false,
)
```

### Java

```java
DownloadService.sendAddDownload(
    context, MyDownloadService.class, downloadRequest, /* foreground= */ false);
```

In this example, `MyDownloadService` is the app's `DownloadService` subclass, and the
`foreground` parameter controls whether the service will be started in the
foreground. If your app is already in the foreground, then the `foreground`
parameter should normally be set to `false` because the `DownloadService` will
put itself in the foreground if it determines that it has work to do.

## Removing downloads

A download can be removed by sending a remove command to the `DownloadService`,
where `contentId` identifies the download to be removed:

### Kotlin

```kotlin
DownloadService.sendRemoveDownload(
  context,
  MyDownloadService::class.java,
  contentId,
  /* foreground= */ false,
)
```

### Java

```java
DownloadService.sendRemoveDownload(
    context, MyDownloadService.class, contentId, /* foreground= */ false);
```

You can also remove all downloaded data with
`DownloadService.sendRemoveAllDownloads`.

## Starting and stopping downloads

A download will only progress if four conditions are met:

- The download doesn't have a stop reason.
- Downloads aren't paused.
- The requirements for downloads to progress are met. Requirements can specify constraints on the allowed network types, as well as whether the device should be idle or connected to a charger.
- The maximum number of parallel downloads is not exceeded.

All of these conditions can be controlled by sending commands to your
`DownloadService`.

#### Setting and clearing download stop reasons

It's possible to set a reason for one or all downloads being stopped:

### Kotlin

```kotlin
// Set the stop reason for a single download.
DownloadService.sendSetStopReason(
  context,
  MyDownloadService::class.java,
  contentId,
  stopReason,
  /* foreground= */ false,
)

// Clear the stop reason for a single download.
DownloadService.sendSetStopReason(
  context,
  MyDownloadService::class.java,
  contentId,
  Download.STOP_REASON_NONE,
  /* foreground= */ false,
)
```

### Java

```java
// Set the stop reason for a single download.
DownloadService.sendSetStopReason(
    context, MyDownloadService.class, contentId, stopReason, /* foreground= */ false);

// Clear the stop reason for a single download.
DownloadService.sendSetStopReason(
    context,
    MyDownloadService.class,
    contentId,
    Download.STOP_REASON_NONE,
    /* foreground= */ false);
```

`stopReason` can be any non-zero value (`Download.STOP_REASON_NONE = 0` is
a special value meaning that the download is not stopped). Apps that have
multiple reasons for stopping downloads can use different values to keep track
of why each download is stopped. Setting and clearing the stop reason for all
downloads works the same way as setting and clearing the stop reason for a
single download, except that `contentId` should be set to `null`.

> [!NOTE]
> **Note:** Setting a stop reason does not remove a download. The partial download will be retained, and clearing the stop reason will cause the download to continue.

When a download has a non-zero stop reason, it will be in the
`Download.STATE_STOPPED` state. Stop reasons are persisted in the
`DownloadIndex`, and so are retained if the application process is killed and
later restarted.

#### Pausing and resuming all downloads

All downloads can be paused and resumed as follows:

### Kotlin

```kotlin
// Pause all downloads.
DownloadService.sendPauseDownloads(
  context,
  MyDownloadService::class.java,
  /* foreground= */ false,
)

// Resume all downloads.
DownloadService.sendResumeDownloads(
  context,
  MyDownloadService::class.java,
  /* foreground= */ false,
)
```

### Java

```java
// Pause all downloads.
DownloadService.sendPauseDownloads(context, MyDownloadService.class, /* foreground= */ false);

// Resume all downloads.
DownloadService.sendResumeDownloads(context, MyDownloadService.class, /* foreground= */ false);
```

When downloads are paused, they will be in the `Download.STATE_QUEUED` state.
Unlike [setting stop reasons](https://developer.android.com/media/media3/exoplayer/downloading-media#setting-and-clearing-download-stop-reasons), this approach does not persist any state
changes. It only affects the runtime state of the `DownloadManager`.

#### Setting the requirements for downloads to progress

[`Requirements`](https://developer.android.com/reference/androidx/media3/exoplayer/scheduler/Requirements) can be used to specify constraints that must be met for
downloads to proceed. The requirements can be set by calling
`DownloadManager.setRequirements()` when creating the `DownloadManager`, as in
the example [above](https://developer.android.com/media/media3/exoplayer/downloading-media#creating-a-downloadmanager). They can also be changed dynamically by sending a command
to the `DownloadService`:

### Kotlin

```kotlin
// Set the download requirements.
DownloadService.sendSetRequirements(
  context,
  MyDownloadService::class.java,
  requirements,
  /* foreground= */ false,
)
```

### Java

```java
// Set the download requirements.
DownloadService.sendSetRequirements(
    context, MyDownloadService.class, requirements, /* foreground= */ false);
```

When a download cannot proceed because the requirements are not met, it
will be in the `Download.STATE_QUEUED` state. You can query the not met
requirements with `DownloadManager.getNotMetRequirements()`.

#### Setting the maximum number of parallel downloads

The maximum number of parallel downloads can be set by calling
`DownloadManager.setMaxParallelDownloads()`. This would normally be done when
creating the `DownloadManager`, as in the example [above](https://developer.android.com/media/media3/exoplayer/downloading-media#creating-a-downloadmanager).

When a download cannot proceed because the maximum number of parallel downloads
are already in progress, it will be in the `Download.STATE_QUEUED` state.

## Querying downloads

The `DownloadIndex` of a `DownloadManager` can be queried for the state of all
downloads, including those that have completed or failed. The `DownloadIndex`
can be obtained by calling `DownloadManager.getDownloadIndex()`. A cursor that
iterates over all downloads can then be obtained by calling
`DownloadIndex.getDownloads()`. Alternatively, the state of a single download
can be queried by calling `DownloadIndex.getDownload()`.

`DownloadManager` also provides `DownloadManager.getCurrentDownloads()`, which
returns the state of current (i.e. not completed or failed) downloads only. This
method is useful for updating notifications and other UI components that display
the progress and status of current downloads.

## Listening to downloads

You can add a listener to `DownloadManager` to be informed when current
downloads change state:

### Kotlin

```kotlin
downloadManager.addListener(
  object : DownloadManager.Listener { // Override methods of interest here.
  }
)
```

### Java

```java
downloadManager.addListener(
    new DownloadManager.Listener() {
      // Override methods of interest here.
    });
```

See `DownloadManagerListener` in the demo app's [`DownloadTracker`](https://github.com/androidx/media/tree/release/demos/main/src/main/java/androidx/media3/demo/main/DownloadTracker.java) class for
a concrete example.

> [!NOTE]
> **Note:** Download progress updates do not trigger calls on `DownloadManager.Listener`. To update a UI component that shows download progress, you should periodically query the `DownloadManager` at your desired update rate. [`DownloadService`](https://github.com/androidx/media/tree/release/libraries/exoplayer/src/main/java/androidx/media3/exoplayer/offline/DownloadService.java) contains an example of this, which periodically updates the service foreground notification.

## Playing downloaded content

Playing downloaded content is similar to playing online content, except that
data is read from the download `Cache` instead of over the network.

> [!NOTE]
> **Note:** It's important that you do not try and read files directly from the download directory. Instead, use ExoPlayer library classes as described below.

To play downloaded content, create a `CacheDataSource.Factory` using the same
`Cache` instance that was used for downloading, and inject it into
`DefaultMediaSourceFactory` when building the player:

### Kotlin

```kotlin
// Create a read-only cache data source factory using the download cache.
val cacheDataSourceFactory: DataSource.Factory =
  CacheDataSource.Factory()
    .setCache(downloadCache)
    .setUpstreamDataSourceFactory(httpDataSourceFactory)
    .setCacheWriteDataSinkFactory(null) // Disable writing.

val player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setDataSourceFactory(cacheDataSourceFactory)
    )
    .build()
```

### Java

```java
// Create a read-only cache data source factory using the download cache.
DataSource.Factory cacheDataSourceFactory =
    new CacheDataSource.Factory()
        .setCache(downloadCache)
        .setUpstreamDataSourceFactory(httpDataSourceFactory)
        .setCacheWriteDataSinkFactory(null); // Disable writing.

ExoPlayer player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context).setDataSourceFactory(cacheDataSourceFactory))
        .build();
```

If the same player instance will also be used to play non-downloaded content
then the `CacheDataSource.Factory` should be configured as read-only to avoid
downloading that content as well during playback.

Once the player has been configured with the `CacheDataSource.Factory`, it will
have access to the downloaded content for playback. Playing a download is then
as simple as passing the corresponding `MediaItem` to the player. A `MediaItem`
can be obtained from a `Download` using `Download.request.toMediaItem`, or
directly from a `DownloadRequest` using `DownloadRequest.toMediaItem`.

### MediaSource configuration

The preceding example makes the download cache available for playback of all
`MediaItem`s. You can also make the download cache available for
individual `MediaSource` instances, which can be passed directly to the player:

### Kotlin

```kotlin
val mediaSource =
  ProgressiveMediaSource.Factory(cacheDataSourceFactory)
    .createMediaSource(MediaItem.fromUri(contentUri))
player.setMediaSource(mediaSource)
player.prepare()
```

### Java

```java
ProgressiveMediaSource mediaSource =
    new ProgressiveMediaSource.Factory(cacheDataSourceFactory)
        .createMediaSource(MediaItem.fromUri(contentUri));
player.setMediaSource(mediaSource);
player.prepare();
```

## Downloading and playing adaptive streams

Adaptive streams (e.g. DASH, SmoothStreaming and HLS) normally contain multiple
media tracks. There are often multiple tracks that contain the same content in
different qualities (e.g. SD, HD and 4K video tracks). There may also be
multiple tracks of the same type containing different content (e.g. multiple
audio tracks in different languages).

For streaming playbacks, a track selector can be used to choose which of the
tracks are played. Similarly, for downloading, a `DownloadHelper` can be used to
choose which of the tracks are downloaded. Typical usage of a `DownloadHelper`
follows these steps:

1. Build a `DownloadHelper` using a `DownloadHelper.Factory` instance. Prepare the helper and wait for the callback.
2. Optionally, inspect the default selected tracks using `getMappedTrackInfo` and `getTrackSelections`, and make adjustments using `clearTrackSelections`, `replaceTrackSelections` and `addTrackSelection`.
3. Create a `DownloadRequest` for the selected tracks by calling `getDownloadRequest`. The request can be passed to your `DownloadService` to add the download, as described above.
4. Release the helper using `release()`.

### Kotlin

```kotlin
val downloadHelper =
  DownloadHelper.Factory()
    .setRenderersFactory(DefaultRenderersFactory(context))
    .setDataSourceFactory(dataSourceFactory)
    .create(MediaItem.fromUri(contentUri))
downloadHelper.prepare(callback)
```

### Java

```java
DownloadHelper downloadHelper =
    new DownloadHelper.Factory()
        .setRenderersFactory(new DefaultRenderersFactory(context))
        .setDataSourceFactory(dataSourceFactory)
        .create(MediaItem.fromUri(contentUri));
downloadHelper.prepare(callback);
```

Playback of downloaded adaptive content requires configuring the player and
passing the corresponding `MediaItem`, as described above.

When building the `MediaItem`, `MediaItem.localConfiguration.streamKeys` must be
set to match those in the `DownloadRequest` so that the player only tries to
play the subset of tracks that have been downloaded. Using
`Download.request.toMediaItem` and `DownloadRequest.toMediaItem` to build the
`MediaItem` will take care of this for you.

> [!NOTE]
> **Note:** If you see data being requested from the network when trying to play downloaded adaptive content, the most likely cause is that the player is trying to adapt to a track that was not downloaded. Ensure you've set the stream keys correctly.