---
title: https://developer.android.com/media/platform/mediaplayer/drm
url: https://developer.android.com/media/platform/mediaplayer/drm
source: md.txt
---

> Documentation index: https://developer.android.com/media/platform/mediaplayer/llms.txt

Starting with Android 8.0 (API level 26), [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt) includes APIs that
support the playback of DRM-protected material. The MediaPlayer DRM APIs are
similar to the low-level API provided by [`MediaDrm`](https://developer.android.com/reference/android/media/MediaDrm.md.txt), but they operate at a
higher level and don't expose the underlying extractor, DRM, and crypto objects.

Although the MediaPlayer DRM API does not provide the full functionality of
[`MediaDrm`](https://developer.android.com/reference/android/media/MediaDrm.md.txt), it supports the most common use cases. The current
implementation can handle the following content types:

- Widevine-protected local media files
- Widevine-protected remote or streaming media files

The following code snippet demonstrates how to use the new DRM `MediaPlayer`
methods in a synchronous implementation.

To manage DRM-controlled media, you need to include the new methods alongside
the usual flow of MediaPlayer calls, as shown in this example:

### Kotlin

```kotlin
mediaPlayer?.apply {
    setDataSource()
    setOnDrmConfigHelper() // optional, for custom configuration
    prepare()
    drmInfo?.also {
        prepareDrm()
        getKeyRequest()
        provideKeyResponse()
    }

    // MediaPlayer is now ready to use
    start()
    // ...play/pause/resume...
    stop()
    releaseDrm()
}
```

### Java

```java
setDataSource();
setOnDrmConfigHelper(); // optional, for custom configuration
prepare();
if (getDrmInfo() != null) {
  prepareDrm();
  getKeyRequest();
  provideKeyResponse();
}

// MediaPlayer is now ready to use
start();
// ...play/pause/resume...
stop();
releaseDrm();
```

Start by initializing the [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt) object and setting its source using
[`setDataSource()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#setDataSource(android.content.Context,%20android.net.Uri)), as usual. Then, to use DRM, perform these steps:

1. If you want your app to perform custom configuration, define an [`OnDrmConfigHelper`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmConfigHelper.md.txt) interface, and attach it to the player using [`setOnDrmConfigHelper()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#setOnDrmConfigHelper(android.media.MediaPlayer.OnDrmConfigHelper)).
2. Call [`prepare()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepare()).
3. Call [`getDrmInfo()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#getDrmInfo()). If the source has DRM content, the method returns a non-null [`MediaPlayer.DrmInfo`](https://developer.android.com/reference/android/media/MediaPlayer.DrmInfo.md.txt) value.

If [`MediaPlayer.DrmInfo`](https://developer.android.com/reference/android/media/MediaPlayer.DrmInfo.md.txt) exists:

1. Examine the map of available UUIDs and choose one.
2. Prepare the DRM configuration for the current source by calling [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)).
   - If you created and registered an [`OnDrmConfigHelper`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmConfigHelper.md.txt) callback, it is called while [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) is executing. This lets you perform custom configuration of the DRM properties before opening the DRM session. The callback is called synchronously in the thread that called [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)). To access the DRM properties, call [`getDrmPropertyString()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#getDrmPropertyString(java.lang.String)) and [`setDrmPropertyString()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#setDrmPropertyString(java.lang.String,%20java.lang.String)). Avoid performing lengthy operations.
   - If the device has not yet been provisioned, [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) also accesses the provisioning server to provision the device. This can take a variable amount of time, depending on the network connectivity.
3. To get an opaque key request byte array to send to a license server, call [`getKeyRequest()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#getKeyRequest(byte%5B%5D,%20byte%5B%5D,%20java.lang.String,%20int,%20java.util.Map%3Cjava.lang.String,%20java.lang.String%3E)).
4. To inform the DRM engine about the key response received from the license server, call [`provideKeyResponse()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#provideKeyResponse(byte%5B%5D,%20byte%5B%5D)). The result depends on the type of key request:
   - If the response is for an offline key request, the result is a key-set identifier. You can use this key-set identifier with [`restoreKeys()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#restoreKeys(byte%5B%5D)) to restore the keys to a new session.
   - If the response is for a streaming or release request, the result is null.

## Prepare DRM asynchronously

By default, [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) runs synchronously, blocking until preparation
finishes. However, the very first DRM preparation on a new device may also
require provisioning, which [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) handles internally, and may take
some time to finish due to the network operation involved. You can avoid
blocking on [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) by defining and setting a
[`MediaPlayer.OnDrmPreparedListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmPreparedListener.md.txt).

Set an [`OnDrmPreparedListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmPreparedListener.md.txt). [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) performs the
provisioning (if needed) and preparation in the background. When provisioning
and preparation finish, the system calls the listener. Don't make any
assumptions about the calling sequence or the thread in which the listener runs
(unless you register the listener with a handler thread). The system can call
the listener before or after [`prepareDrm()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareDrm(java.util.UUID)) returns.

## Set up DRM asynchronously

You can initialize the DRM asynchronously by creating and registering the
[`MediaPlayer.OnDrmInfoListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmInfoListener.md.txt) for DRM preparation and the
[`MediaPlayer.OnDrmPreparedListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnDrmPreparedListener.md.txt) to start the player. They work in
conjunction with [`prepareAsync()`](https://developer.android.com/reference/android/media/MediaPlayer.md.txt#prepareAsync()), as shown in this example:

### Kotlin

```kotlin
setOnPreparedListener()
setOnDrmInfoListener()
setDataSource()
prepareAsync()
// ...

// If the data source content is protected you receive a call to the onDrmInfo() callback.
override fun onDrmInfo(mediaPlayer: MediaPlayer, drmInfo: MediaPlayer.DrmInfo) {
    mediaPlayer.apply {
        prepareDrm()
        getKeyRequest()
        provideKeyResponse()
    }
}

// When prepareAsync() finishes, you receive a call to the onPrepared() callback.
// If there is a DRM, onDrmInfo() sets it up before executing this callback,
// so you can start the player.
override fun onPrepared(mediaPlayer: MediaPlayer) {
    mediaPlayer.start()
}
```

### Java

```java
setOnPreparedListener();
setOnDrmInfoListener();
setDataSource();
prepareAsync();
// ...

// If the data source content is protected you receive a call to the onDrmInfo() callback.
onDrmInfo() {
  prepareDrm();
  getKeyRequest();
  provideKeyResponse();
}

// When prepareAsync() finishes, you receive a call to the onPrepared() callback.
// If there is a DRM, onDrmInfo() sets it up before executing this callback,
// so you can start the player.
onPrepared() {

start();
}
```

## Handle encrypted media

Starting with Android 8.0 (API level 26) `MediaPlayer` can also decrypt Common
Encryption Scheme (CENC) and HLS sample-level encrypted media
(METHOD=SAMPLE-AES) for the elementary stream types H.264, and AAC. Full-segment
encrypted media (METHOD=AES-128) was previously supported.

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app. [Read
more](https://developer.android.com/media/media3) about it.

These pages cover topics relating to recording, storing, and playing back audio
and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)