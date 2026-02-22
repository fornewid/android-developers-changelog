---
title: https://developer.android.com/media/media3/exoplayer/troubleshooting
url: https://developer.android.com/media/media3/exoplayer/troubleshooting
source: md.txt
---

- [Fixing "Cleartext HTTP traffic not permitted" errors](https://developer.android.com/media/media3/exoplayer/troubleshooting#fixing-cleartext-http-traffic-not-permitted-errors)
- [Fixing "SSLHandshakeException", "CertPathValidatorException" and "ERR_CERT_AUTHORITY_INVALID" errors](https://developer.android.com/media/media3/exoplayer/troubleshooting#fixing-sslhandshakeexception-certpathvalidatorexception-and-err_cert_authority_invalid-errors)
- [Why are some media files not seekable?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-are-some-media-files-not-seekable)
- [Why is seeking inaccurate in some MP3 files?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-is-seeking-inaccurate-in-some-mp3-files)
- [Why is seeking in my video slow?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-is-seeking-in-my-video-slow)
- [Why do some MPEG-TS files fail to play?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-do-some-mpeg-ts-files-fail-to-play)
- [Why are subtitles not found in some MPEG-TS files?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-are-subtitles-not-found-in-some-mpeg-ts-files)
- [Why do some MP4/FMP4 files play incorrectly?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-do-some-mp4fmp4-files-play-incorrectly)
- [Why do some streams fail with HTTP response code 301 or 302?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-do-some-streams-fail-with-http-response-code-301-or-302)
- [Why do some streams fail with UnrecognizedInputFormatException?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-do-some-streams-fail-with-unrecognizedinputformatexception)
- [Why doesn't setPlaybackParameters work properly on some devices?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-doesnt-setplaybackparameters-work-properly-on-some-devices)
- [What do "Player is accessed on the wrong thread" errors mean?](https://developer.android.com/media/media3/exoplayer/troubleshooting#what-do-player-is-accessed-on-the-wrong-thread-errors-mean)
- [How can I fix "Unexpected status line: ICY 200 OK"?](https://developer.android.com/media/media3/exoplayer/troubleshooting#how-can-i-fix-unexpected-status-line-icy-200-ok)
- [How can I query whether the stream being played is a live stream?](https://developer.android.com/media/media3/exoplayer/troubleshooting#how-can-i-query-whether-the-stream-being-played-is-a-live-stream)
- [How do I keep audio playing when my app is backgrounded?](https://developer.android.com/media/media3/exoplayer/troubleshooting#how-do-i-keep-audio-playing-when-my-app-is-backgrounded)
- [Why does ExoPlayer support my content but the ExoPlayer Cast library doesn't?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-does-exoplayer-support-my-content-but-the-exoplayer-cast-library-doesnt)
- [Why does content fail to play, but no error is surfaced?](https://developer.android.com/media/media3/exoplayer/troubleshooting#why-does-content-fail-to-play-but-no-error-is-surfaced)
- [How can I get a decoding library to load and be used for playback?](https://developer.android.com/media/media3/exoplayer/troubleshooting#how-can-i-get-a-decoding-library-to-load-and-be-used-for-playback)
- [Can I play YouTube videos directly with ExoPlayer?](https://developer.android.com/media/media3/exoplayer/troubleshooting#can-i-play-youtube-videos-directly-with-exoplayer)
- [Video playback is stuttering](https://developer.android.com/media/media3/exoplayer/troubleshooting#video-playback-is-stuttering)
- [Unstable API lint errors](https://developer.android.com/media/media3/exoplayer/troubleshooting#unstable-api-lint-errors)

*** ** * ** ***

#### Fixing "Cleartext HTTP traffic not permitted" errors

This error will occur if your app requests cleartext HTTP traffic (that is,
`http://` rather than `https://`) when its Network Security Configuration does
not permit it. If your app targets Android 9 (API level 28) or higher, cleartext
HTTP traffic is disabled by the default configuration.

If your app needs to work with cleartext HTTP traffic, then you need to use a
Network Security Configuration that permits it. See Android's
[network security documentation](https://developer.android.com/training/articles/security-config)
for details. To enable all cleartext HTTP traffic, you can simply add
`android:usesCleartextTraffic="true"` to the `application` element of your app's
`AndroidManifest.xml`.

The ExoPlayer demo app uses the default Network Security Configuration, and so
it does not allow cleartext HTTP traffic. You can enable it using the instructions
above.

#### Fixing "SSLHandshakeException", "CertPathValidatorException" and "ERR_CERT_AUTHORITY_INVALID" errors

`SSLHandshakeException`, `CertPathValidatorException` and
`ERR_CERT_AUTHORITY_INVALID` all indicate a problem with the server's SSL
certificate. These errors are not ExoPlayer specific. See
[Android's SSL documentation](https://developer.android.com/training/articles/security-ssl#CommonProblems)
for more details.

#### Why are some media files not seekable?

By default, ExoPlayer does not support seeking in media where the only method for
performing accurate seek operations is for the player to scan and index the
entire file. ExoPlayer considers such files as unseekable. Most modern media
container formats include metadata for seeking (such as a sample index), have a
well defined seek algorithm (for example, interpolated bisection search for Ogg), or
indicate that their content is constant bitrate. Efficient seek operations are
possible and supported by ExoPlayer in these cases.

If you require seeking but have unseekable media, we suggest converting your
content to use a more appropriate container format. For MP3, ADTS and AMR files,
you can also enable seeking under the assumption that the files have a constant
bitrate, as described
[here](https://developer.android.com/media/media3/exoplayer/customization#enabling-constant-bitrate-seeking).

#### Why is seeking inaccurate in some MP3 files?

Variable bitrate (VBR) MP3 files are fundamentally unsuitable for use cases that
require exact seeking. There are two reasons for this:

1. For exact seeking, a container format will ideally provide a precise time-to-byte mapping in a header. This mapping allows a player to map a requested seek time to the corresponding byte offset, and start requesting, parsing and playing media from that offset. The headers available for specifying this mapping in MP3 (such as XING headers) are, unfortunately, often imprecise.
2. For container formats that don't provide a precise time-to-byte mapping (or any time-to-byte mapping at all), it's still possible to perform an exact seek if the container includes absolute sample timestamps in the stream. In this case a player can map the seek time to a best guess of the corresponding byte offset, start requesting media from that offset, parse the first absolute sample timestamp, and effectively perform a guided binary search into the media until it finds the right sample. Unfortunately MP3 does not include absolute sample timestamps in the stream, so this approach is not possible.

For these reasons, the only way to perform an exact seek into a VBR MP3 file is
to scan the entire file and manually build up a time-to-byte mapping in the
player. This strategy can be enabled by using [`FLAG_ENABLE_INDEX_SEEKING`](https://developer.android.com/reference/androidx/media3/extractor/mp3/Mp3Extractor#FLAG_ENABLE_INDEX_SEEKING),
which can be [set on a `DefaultExtractorsFactory`](https://developer.android.com/guide/topics/media/exoplayer/customization#customizing-extractor-flags) using
[`setMp3ExtractorFlags`](https://developer.android.com/reference/androidx/media3/extractor/DefaultExtractorsFactory#setMp3ExtractorFlags(int)). Note that it doesn't scale well to large MP3 files,
particularly if the user tries to seek to near the end of the stream shortly
after starting playback, which requires the player to wait until it's downloaded
and indexed the entire stream before performing the seek. In ExoPlayer, we
decided to optimize for speed over accuracy in this case and
[`FLAG_ENABLE_INDEX_SEEKING`](https://developer.android.com/reference/androidx/media3/extractor/mp3/Mp3Extractor#FLAG_ENABLE_INDEX_SEEKING) is therefore disabled by default.

If you control the media you're playing, we strongly advise that you use a more
appropriate container format, such as MP4. There are no use cases we're aware of
where MP3 is the best choice of media format.

#### Why is seeking in my video slow?

When the player seeks to a new playback position in a video it needs to do two
things:

1. Load the data corresponding to the new playback position into the buffer (this may not be necessary if this data is already buffered).
2. Flush the video decoder and start decoding from the I-frame (keyframe) before the new playback position, due to the [intra-frame coding](https://en.wikipedia.org/wiki/Intra-frame_coding) used by most video compression formats. In order to ensure the seek is *accurate* (that is, playback starts exactly at the seek position), all frames between the preceding I-frame and the seek position need to be decoded and immediately discarded (without being shown on the screen).

The latency introduced by (1) can be mitigated by either increasing the amount
of data buffered in memory by the player, or [pre-caching the data to disk](https://developer.android.com/guide/topics/media/exoplayer/downloading-media).

The latency introduced by (2) can be mitigated by either reducing the accuracy
of the seek using [`ExoPlayer.setSeekParameters`](https://developer.android.com/reference/androidx/media3/ExoPlayer#setSeekParameters(androidx.media3.exoplayer.SeekParameters)), or re-encoding the video
to have more frequent I-frames (which will result in a larger output file).

#### Why do some MPEG-TS files fail to play?

Some MPEG-TS files do not contain access unit delimiters (AUDs). By default,
ExoPlayer relies on AUDs to cheaply detect frame boundaries. Similarly, some
MPEG-TS files do not contain IDR keyframes. By default, these are the only type
of keyframes considered by ExoPlayer.

ExoPlayer will appear to be stuck in the buffering state when asked to play an
MPEG-TS file that lacks AUDs or IDR keyframes. If you need to play such files,
you can do so using [`FLAG_DETECT_ACCESS_UNITS`](https://developer.android.com/reference/androidx/media3/extractor/ts/DefaultTsPayloadReaderFactory#FLAG_DETECT_ACCESS_UNITS) and
[`FLAG_ALLOW_NON_IDR_KEYFRAMES`](https://developer.android.com/reference/androidx/media3/extractor/ts/DefaultTsPayloadReaderFactory#FLAG_ALLOW_NON_IDR_KEYFRAMES) respectively. These flags can be [set on a
`DefaultExtractorsFactory`](https://developer.android.com/guide/topics/media/exoplayer/customization#customizing-extractor-flags) using [`setTsExtractorFlags`](https://developer.android.com/reference/androidx/media3/extractor/DefaultExtractorsFactory#setTsExtractorFlags(int)) or on a
`DefaultHlsExtractorFactory` using the
[constructor](https://developer.android.com/reference/androidx/media3/exoplayer/hls/DefaultHlsExtractorFactory#DefaultHlsExtractorFactory-int-boolean-).
Use of `FLAG_DETECT_ACCESS_UNITS` has no side effects other than being
computationally expensive relative to AUD based frame boundary detection. Use of
`FLAG_ALLOW_NON_IDR_KEYFRAMES` may result in temporary visual corruption at the
start of playback and immediately after seeks when playing some MPEG-TS files.

#### Why are subtitles not found in some MPEG-TS files?

Some MPEG-TS files include CEA-608 tracks but don't declare them in the
container metadata, so ExoPlayer is unable to detect them. You can manually
specify any subtitle tracks by providing a list of expected
subtitle formats to the `DefaultExtractorsFactory`, including the accessibility
channels that can be used to identify them in the MPEG-TS stream:

### Kotlin

```kotlin
val extractorsFactory =
  DefaultExtractorsFactory()
    .setTsSubtitleFormats(
      listOf(
        Format.Builder()
          .setSampleMimeType(MimeTypes.APPLICATION_CEA608)
          .setAccessibilityChannel(accessibilityChannel)
          // Set other subtitle format info, such as language.
          .build()
      )
    )
val player: Player =
  ExoPlayer.Builder(context, DefaultMediaSourceFactory(context, extractorsFactory)).build()
```

### Java

```java
DefaultExtractorsFactory extractorsFactory =
    new DefaultExtractorsFactory()
        .setTsSubtitleFormats(
            ImmutableList.of(
                new Format.Builder()
                    .setSampleMimeType(MimeTypes.APPLICATION_CEA608)
                    .setAccessibilityChannel(accessibilityChannel)
                    // Set other subtitle format info, such as language.
                    .build()));
Player player =
    new ExoPlayer.Builder(context, new DefaultMediaSourceFactory(context, extractorsFactory))
        .build();
```

#### Why do some MP4/FMP4 files play incorrectly?

Some MP4/FMP4 files contain edit lists that rewrite the media timeline by
skipping, moving, or repeating lists of samples. ExoPlayer has partial support
for applying edit lists. For example, it can delay or repeat groups of samples
starting on a synchronization sample, but it does not truncate audio samples or
preroll media for edits that don't start on a synchronization sample.

If you are seeing that part of the media is unexpectedly missing or repeated,
try setting [`Mp4Extractor.FLAG_WORKAROUND_IGNORE_EDIT_LISTS`](https://developer.android.com/reference/androidx/media3/extractor/mp4/Mp4Extractor#FLAG_WORKAROUND_IGNORE_EDIT_LISTS) or
[`FragmentedMp4Extractor.FLAG_WORKAROUND_IGNORE_EDIT_LISTS`](https://developer.android.com/reference/androidx/media3/extractor/mp4/FragmentedMp4Extractor#FLAG_WORKAROUND_IGNORE_EDIT_LISTS), which will cause
the extractor to ignore edit lists entirely. These can be [set on a
`DefaultExtractorsFactory`](https://developer.android.com/guide/topics/media/exoplayer/customization#customizing-extractor-flags) using [`setMp4ExtractorFlags`](https://developer.android.com/reference/androidx/media3/extractor/DefaultExtractorsFactory#setMp4ExtractorFlags(int)) or
[`setFragmentedMp4ExtractorFlags`](https://developer.android.com/reference/androidx/media3/extractor/DefaultExtractorsFactory#setFragmentedMp4ExtractorFlags(int)).

#### Why do some streams fail with HTTP response code 301 or 302?

HTTP response codes 301 and 302 both indicate redirection. Brief descriptions
can be found on [Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). When ExoPlayer makes a request and receives a
response with status code 301 or 302, it will normally follow the redirect
and start playback as normal. The one case where this does not happen by default
is for cross-protocol redirects. A cross-protocol redirect is one that redirects
from HTTPS to HTTP or vice-versa (or less commonly, between another pair of
protocols). You can test whether a URL causes a cross-protocol redirect using
the [wget](https://www.gnu.org/software/wget/manual/wget.html) command line tool as follows:

```
wget "https://yourserver.example.com/test.mp3" 2>&1  | grep Location
```

The output should look something like this:

    Location: https://secondserver.example.net/test.mp3 [following]
    Location: http://thirdserver.example.org/test.mp3 [following]

In this example, there are two redirects. The first redirect is from
`https://yourserver.example.com/test.mp3` to
`https://secondserver.example.net/test.mp3`. Both are HTTPS, and so this is not
a cross-protocol redirect. The second redirect is from
`https://secondserver.example.net/test.mp3` to
`http://thirdserver.example.org/test.mp3`. This redirects from HTTPS to HTTP and
so is a cross-protocol redirect. ExoPlayer will not follow this redirect in its
default configuration, meaning playback will fail.

If you need to, you can configure ExoPlayer to follow cross-protocol redirects
when instantiating [`DefaultHttpDataSource.Factory`](https://developer.android.com/reference/androidx/media3/datasource/DefaultHttpDataSource.Factory) instances used in your
application. Learn about selecting and configuring the network stack
[here](https://developer.android.com/guide/topics/media/exoplayer/customization#configuring-the-network-stack).

#### Why do some streams fail with UnrecognizedInputFormatException?

This question relates to playback failures of the following form:

    UnrecognizedInputFormatException: None of the available extractors
    (MatroskaExtractor, FragmentedMp4Extractor, ...) could read the stream.

There are two possible causes of this failure. The most common cause is that
you're trying to play DASH (mpd), HLS (m3u8), or SmoothStreaming (ism, isml)
content, but the player tries to play it as a progressive stream. To play such
streams, you must depend on the respective [ExoPlayer module](https://developer.android.com/guide/topics/media/exoplayer/hello-world#add-exoplayer-modules). In cases where
the stream URI doesn't end with the standard file extension, you can also pass
`MimeTypes.APPLICATION_MPD`, `MimeTypes.APPLICATION_M3U8` or
`MimeTypes.APPLICATION_SS` to `setMimeType` of `MediaItem.Builder` to explicitly
specify the type of stream.

The second, less-common cause, is that ExoPlayer doesn't support the container
format of the media that you're trying to play. In this case, the failure is
working as intended, however feel free to submit a feature request to our
[issue tracker](https://github.com/androidx/media/issues), including details of the container format and a test stream.
Please search for an existing feature request before submitting a new one.

#### Why doesn't setPlaybackParameters work properly on some devices?

When running a debug build of your app on Android M and earlier, you may
experience choppy performance, audible artifacts and high CPU utilization when
using the [`setPlaybackParameters`](https://developer.android.com/reference/androidx/media3/common/Player#setPlaybackParameters(androidx.media3.common.PlaybackParameters)) API. This is because an optimization
that's important to this API is disabled for debug builds running on these
versions of Android.

It's important to note that this issue affects debug builds only. It does *not*
affect release builds, for which the optimization is always enabled. Hence the
releases you provide to end users should not be affected by this issue.

#### What do "Player is accessed on the wrong thread" errors mean?

See [A note on threading](https://developer.android.com/guide/topics/media/exoplayer/hello-world#a-note-on-threading) on the getting started page.

#### How can I fix "Unexpected status line: ICY 200 OK"?

This problem can occur if the server response includes an ICY status line,
rather than one that's HTTP compliant. ICY status lines are deprecated and
should not be used, so if you control the server you should update it to provide
an HTTP compliant response. If you're unable to do this then using the
[ExoPlayer OkHttp library](https://github.com/androidx/media/tree/release/libraries/datasource_okhttp) will resolve the problem, since it's able to handle ICY
status lines correctly.

#### How can I query whether the stream being played is a live stream?

You can query the player's [`isCurrentWindowLive`](https://developer.android.com/reference/androidx/media3/common/Player#isCurrentWindowLive()) method. In addition, you
can check [`isCurrentWindowDynamic`](https://developer.android.com/reference/androidx/media3/common/Player#isCurrentWindowDynamic()) to find out whether the window is dynamic
(that is, still updating over time).

#### How do I keep audio playing when my app is backgrounded?

Follow these steps to ensure continued playback of audio when your app is in
the background:

1. You need to have a running [foreground service](https://developer.android.com/guide/components/services#Foreground). This prevents the system from killing your process to free up resources.
2. You need to hold a [`WifiLock`](https://developer.android.com/reference/android/net/wifi/WifiManager.WifiLock) and a [`WakeLock`](https://developer.android.com/reference/android/os/PowerManager.WakeLock). These ensure that the system keeps the WiFi radio and CPU awake. This can be easily done if using [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) by calling [`setWakeMode`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer#setWakeMode(int)), which will automatically acquire and release the required locks at the correct times.

It's important that you release the locks (if not using `setWakeMode`) and stop
the service as soon as audio is no longer being played.

#### Why does ExoPlayer support my content but the ExoPlayer Cast library doesn't?

It's possible that the content that you are trying to play is not
[CORS enabled](https://www.w3.org/wiki/CORS_Enabled). The [Cast framework](https://developers.google.com/cast/docs/chrome_sender/advanced#cors_requirements) requires content to be CORS enabled in
order to play it.

#### Why does content fail to play, but no error is surfaced?

It's possible that the device on which you are playing the content does not
support a specific media sample format. This can be easily confirmed by adding
an [`EventLogger`](https://developer.android.com/guide/topics/media/exoplayer/debug-logging) as a listener to your player, and looking for a line
similar to this one in Logcat:

    [ ] Track:x, id=x, mimeType=mime/type, ... , supported=NO_UNSUPPORTED_TYPE

`NO_UNSUPPORTED_TYPE` means that the device is not able to decode the media
sample format specified by the `mimeType`. See the [Android media formats
documentation](https://developer.android.com/guide/topics/media/media-formats#core) for information about supported sample formats. [How can I get
a decoding library to load and be used for playback?](https://developer.android.com/media/media3/exoplayer/troubleshooting#how-can-i-get-a-decoding-library-to-load-and-be-used-for-playback) may also be useful.

#### How can I get a decoding library to load and be used for playback?

- Most decoder libraries have manual steps to check out and build the dependencies, so make sure you've followed the steps in the README for the relevant library. For example, for the ExoPlayer FFmpeg library it's necessary to follow the instructions in [libraries/decoder_ffmpeg/README.md](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg/README.md), including passing configuration flags to [enable decoders](https://developer.android.com/guide/topics/media/exoplayer/supported-formats#ffmpeg-library) for any formats you want to play.
- For libraries that have native code, make sure you're using the correct version of the Android NDK as specified in the README, and look out for any errors that appear during configuration and building. You should see `.so` files appear in the `libs` subdirectory of the library's path for each supported architecture after following the steps in the README.
- To try out playback using the library in the [demo application](https://developer.android.com/guide/topics/media/exoplayer/demo-application), see [enabling bundled decoders](https://developer.android.com/guide/topics/media/exoplayer/demo-application#enabling-bundled-decoders). See the README for the library for instructions on using the library from your own app.
- If you're using [`DefaultRenderersFactory`](https://developer.android.com/reference/androidx/media3/exoplayer/DefaultRenderersFactory), you should see an info-level log line like "Loaded FfmpegAudioRenderer" in Logcat when the decoder loads. If that's missing, make sure the application has a dependency on the decoding library.
- If you see warning-level logs from [`LibraryLoader`](https://developer.android.com/reference/androidx/media3/common/util/LibraryLoader) in Logcat, this indicates that loading the native component of the library failed. If this happens, check you've followed the steps in the library's README correctly and that no errors were output while following the instructions.

If you're still experiencing problems using decoding libraries, please check the
Media3 [issue tracker](https://github.com/androidx/media/issues) for any relevant recent issues. If you need to file
a new issue and it relates to building the native part of the library, please
include full command line output from running README instructions, to help us
diagnose the issue.

#### Can I play YouTube videos directly with ExoPlayer?

No, ExoPlayer cannot play videos from YouTube, such as URLs of the form
`https://www.youtube.com/watch?v=...`. Instead, you should use the [YouTube
IFrame Player API](https://developers.google.com/youtube/iframe_api_reference),
which is the official way to play YouTube videos on Android.

#### Video playback is stuttering

The device may not be able to decode the content fast enough if, for example,
the content bitrate or resolution exceeds the device capabilities. You may need
to use lower quality content to obtain good performance on such devices.

If you're experiencing video stuttering on a device running a version of Android
from Android 6.0 (API level 23) up to and including Android 11 (API level 30),
particularly when playing DRM protected or high-frame-rate content, you can try
[enabling asynchronous buffer queueing](https://developer.android.com/guide/topics/media/exoplayer/customization#enabling-asynchronous-buffer-queueing).

#### Unstable API lint errors

Media3 guarantees binary compatibility for a subset of the API surface. The
parts that **don't** guarantee binary compatibility are marked with
[`@UnstableApi`](https://developer.android.com/reference/androidx/media3/common/util/UnstableApi). In order to make this distinction clear, usages of unstable
API symbols generate a lint error unless they are annotated with `@OptIn`.

The `@UnstableApi` annotation implies nothing about the quality or performance of an API, only the fact that it is not "API-frozen."

You have two choices to handle unstable API lint errors:

- Switch to using a stable API that achieves the same result.
- Continue using the unstable API and annotate the usage with `@OptIn`, as shown later.

##### Add the `@OptIn` annotation

Android Studio can help you add the annotation:
![Screenshot: How to add the Optin annotation](https://developer.android.com/static/media/media3/exoplayer/images/unstable-api.png) **Figure 2**: Adding an @androidx.annotations.OptIn annotation with Android Studio.

You can also manually annotate specific usage sites:

### Kotlin

    import androidx.annotation.OptIn
    import androidx.media3.common.util.UnstableApi

    @OptIn(UnstableApi::class)
    fun functionUsingUnstableApi() { ... }

### Java

    import androidx.annotation.OptIn;
    import androidx.media3.common.util.UnstableApi;

    @OptIn(markerClass = UnstableApi.class)
    private void methodUsingUnstableApis() { ... }

Whole packages can be opted-in by adding a `package-info` file:

### Kotlin

    // In your package-info.kt
    @OptIn(UnstableApi::class)
    package name.of.your.package

    import androidx.annotation.OptIn
    import androidx.media3.common.util.UnstableApi

### Java

    // In your package-info.java
    @OptIn(markerClass = UnstableApi.class)
    package name.of.your.package;

    import androidx.annotation.OptIn;
    import androidx.media3.common.util.UnstableApi;

Whole projects can be opted-in by suppressing the specific lint error in their
[`lint.xml` file](https://developer.android.com/studio/write/lint#pref):

     <?xml version="1.0" encoding="utf-8"?>
     <lint>
       <issue id="UnsafeOptInUsageError">
         <option name="opt-in" value="androidx.media3.common.util.UnstableApi" />
       </issue>
     </lint>

There is a `kotlin.OptIn` annotation as well that shouldn't be used. It's
important to use the `androidx.annotation.OptIn` annotation.