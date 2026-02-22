---
title: https://developer.android.com/media/media3/exoplayer/mappings
url: https://developer.android.com/media/media3/exoplayer/mappings
source: md.txt
---

The following tables outline how the various class, package,
module, and Gradle dependency names differ between `exoplayer2`
and the new `media3` implementation.
| **Note:** This page covers ExoPlayer version **`2.19.1`** and Media3 version **`1.1.1`**.

When migrating to Media3, consider reading our AndroidX Media3
[migration guide](https://developer.android.com/guide/topics/media/media3/getting-started/migration-guide).

## Package mappings

| **exoplayer2 package name** | **media3 package name** |
|---|---|
| com.google.android.exoplayer2 | androidx.media3.exoplayer |
| com.google.android.exoplayer2.analytics | androidx.media3.exoplayer.analytics |
| com.google.android.exoplayer2.audio | androidx.media3.exoplayer.audio |
| com.google.android.exoplayer2.castdemo | androidx.media3.demo.cast |
| com.google.android.exoplayer2.database | androidx.media3.database |
| com.google.android.exoplayer2.decoder | androidx.media3.decoder |
| com.google.android.exoplayer2.demo | androidx.media3.demo.main |
| com.google.android.exoplayer2.drm | androidx.media3.exoplayer.drm |
| com.google.android.exoplayer2.ext.av1 | androidx.media3.decoder.av1 |
| com.google.android.exoplayer2.ext.cast | androidx.media3.cast |
| com.google.android.exoplayer2.ext.cronet | androidx.media3.datasource.cronet |
| com.google.android.exoplayer2.ext.ffmpeg | androidx.media3.decoder.ffmpeg |
| com.google.android.exoplayer2.ext.flac | androidx.media3.decoder.flac |
| com.google.android.exoplayer2.ext.ima | androidx.media3.exoplayer.ima |
| com.google.android.exoplayer2.ext.leanback | androidx.media3.ui.leanback |
| com.google.android.exoplayer2.ext.okhttp | androidx.media3.datasource.okhttp |
| com.google.android.exoplayer2.ext.opus | androidx.media3.decoder.opus |
| com.google.android.exoplayer2.ext.rtmp | androidx.media3.datasource.rtmp |
| com.google.android.exoplayer2.ext.vp9 | androidx.media3.decoder.vp9 |
| com.google.android.exoplayer2.ext.workmanager | androidx.media3.exoplayer.workmanager |
| com.google.android.exoplayer2.extractor | androidx.media3.extractor |
| com.google.android.exoplayer2.gldemo | androidx.media3.demo.gl |
| com.google.android.exoplayer2.mediacodec | androidx.media3.exoplayer.mediacodec |
| com.google.android.exoplayer2.metadata | androidx.media3.extractor.metadata |
| com.google.android.exoplayer2.offline | androidx.media3.exoplayer.offline |
| com.google.android.exoplayer2.playbacktests | androidx.media3.test.exoplayer.playback |
| com.google.android.exoplayer2.robolectric | androidx.media3.test.utils.robolectric |
| com.google.android.exoplayer2.scheduler | androidx.media3.exoplayer.scheduler |
| com.google.android.exoplayer2.source | androidx.media3.exoplayer.source |
| com.google.android.exoplayer2.source.rtsp | androidx.media3.exoplayer.rtsp |
| com.google.android.exoplayer2.source.dash | androidx.media3.exoplayer.dash |
| com.google.android.exoplayer2.source.smoothstreaming | androidx.media3.exoplayer.smoothstreaming |
| com.google.android.exoplayer2.source.hls | androidx.media3.exoplayer.hls |
| com.google.android.exoplayer2.surfacedemo | androidx.media3.demo.surface |
| com.google.android.exoplayer2.testdata | androidx.media3.test.data |
| com.google.android.exoplayer2.testutil | androidx.media3.test.utils |
| com.google.android.exoplayer2.text | androidx.media3.extractor.text |
| com.google.android.exoplayer2.trackselection | androidx.media3.exoplayer.trackselection |
| com.google.android.exoplayer2.transformer | androidx.media3.transformer |
| com.google.android.exoplayer2.transformerdemo | androidx.media3.demo.transformer |
| com.google.android.exoplayer2.ui | androidx.media3.ui |
| com.google.android.exoplayer2.upstream.crypto | androidx.media3.exoplayer.upstream.crypto |
| com.google.android.exoplayer2.upstream.cache | androidx.media3.datasource.cache |
| com.google.android.exoplayer2.upstream | androidx.media3.datasource |
| com.google.android.exoplayer2.util | androidx.media3.exoplayer.util |
| com.google.android.exoplayer2.util | androidx.media3.common.util |
| com.google.android.exoplayer2.video | androidx.media3.exoplayer.video |

## Class renamings

| **exoplayer2 class name** | **media3 package name** | **media3 class names** |
|---|---|---|
| com.google.android.exoplayer2.ExoPlayerLibraryInfo | androidx.media3.common | MediaLibraryInfo |
| com.google.android.exoplayer2.SimpleExoPlayer | androidx.media3.exoplayer | ExoPlayer |
| com.google.android.exoplayer2.ui.StyledPlayerView | androidx.media3.ui | PlayerView |
| com.google.android.exoplayer2.ui.StyledPlayerControlView | androidx.media3.ui | PlayerControlView |

## Class moved to other packages

| **exoplayer2 package name** | **media3 package name** | **media3 class names** |
|---|---|---|
| com.google.android.exoplayer2 | androidx.media3.exoplayer | FormatHolder, PlayerMessage |
| com.google.android.exoplayer2 | androidx.media3.common | BasePlayer, BundleListRetriever, Bundleable, ControlDispatcher, C, DefaultControlDispatcher, DeviceInfo, ErrorMessageProvider, ExoPlayerLibraryInfo, Format, ForwardingPlayer, HeartRating, IllegalSeekPositionException, MediaItem, MediaMetadata, ParserException, PercentageRating, PlaybackException, PlaybackParameters, Player, PositionInfo, Rating, StarRating, ThumbRating, Timeline, TracksInfo |
| com.google.android.exoplayer2.audio | androidx.media3.extractor | AacUtil, Ac3Util, Ac4Util, DtsUtil, MpegAudioUtil, OpusUtil, WavUtil |
| com.google.android.exoplayer2.audio | androidx.media3.common | AudioAttribute, AuxEffectInfo |
| com.google.android.exoplayer2.decoder | androidx.media3.exoplayer | DecoderCounters, DecoderReuseEvaluation |
| com.google.android.exoplayer2.drm | androidx.media3.common | DrmInitData |
| com.google.android.exoplayer2.metadata | androidx.media3.exoplayer.metadata | MetadataDecoderFactor, MetadataOutput, MetadataRenderer |
| com.google.android.exoplayer2.metadata | androidx.media3.common | Metadata |
| com.google.android.exoplayer2.offline | androidx.media3.common | StreamKey |
| com.google.android.exoplayer2.source.ads | androidx.media3.common | AdPlaybackState |
| com.google.android.exoplayer2.source | androidx.media3.common | MediaPeriodId, TrackGroup |
| com.google.android.exoplayer2.trackselection | androidx.media3.common | TrackSelectionParameter, TrackSelectionOverride |
| com.google.android.exoplayer2.text | androidx.media3.common.text | Cue |
| com.google.android.exoplayer2.text | androidx.media3.exoplayer.text | ExoplayerCuesDecode, SubtitleDecoderFactor, TextOutput, TextRenderer |
| com.google.android.exoplayer2.text.span | androidx.media3.common.text | HorizontalTextInVerticalContextSpan, LanguageFeatureSpa, RubySpa, SpanUti, TextAnnotation, TextEmphasisSpan |
| com.google.android.exoplayer2.ui | androidx.media3.common | AdOverlayInf, AdViewProvider |
| com.google.android.exoplayer2.ui | androidx.media3.exoplayer.offline | DownloadNotificationHelper |
| com.google.android.exoplayer2.upstream | androidx.media3.common | DataReader |
| com.google.android.exoplayer2.upstream | androidx.media3.exoplayer.upstream | Allocation, Allocator, BandwidthMeter, CachedRegionTracker, DefaultAllocator, DefaultBandwidthMeter, DefaultLoadErrorHandlingPolicy, Loader, LoaderErrorThrower, ParsingLoadable, SlidingPercentile, TimeToFirstByteEstimator |
| com.google.android.exoplayer2.upstream.crypto | androidx.media3.datasource | AesCipherDataSource, AesCipherDataSink, AesFlushingCipher |
| com.google.android.exoplayer2.util | androidx.media3.common | ErrorMessageProvider, FlagSet, FileType, MimeType, PriorityTaskManager |
| com.google.android.exoplayer2.util | androidx.media3.common.util | AtomicFile, Assertion, BundleableUtil, BundleUtil, Clock, ClosedSource, CodecSpecificDataUtil, ColorParser, ConditionVariable, Consumer, CopyOnWriteMultise, EGLSurfaceTexture, GlProgram, GlUtil, HandlerWrapper, LibraryLoader, ListenerSet, Log, LongArray, MediaFormatUtil, NetworkTypeObserver, NonNullApi, NotificationUtil, ParsableBitArray, ParsableByteArray, RepeatModeUtil, RunnableFutureTask, SystemCloc, SystemHandlerWrapper, TimedValueQueue, TimestampAdjuster, TraceUtil, UnknownNull, UnstableApi, UriUtil, Util, XmlPullParserUtil |
| com.google.android.exoplayer2.util | androidx.media3.extractor | NalUnitUtil, ParsableNalUnitBitArray |
| com.google.android.exoplayer2.util | androidx.media3.exoplayer | MediaClock, StandaloneMediaClock |
| com.google.android.exoplayer2.video | androidx.media3.common | ColorInfo, VideoSize |
| com.google.android.exoplayer2.video | androidx.media3.extractor | AvcConfig, DolbyVisionConfig, HevcConfig |

## Dependency mappings

| **exoplayer2 module name** | **media3 module name** |
|---|---|
| exoplayer | media3-exoplayer |
| exoplayer-database | media3-database |
| exoplayer-datasource | media3-datasource |
| exoplayer-decoder | media3-decoder |
| exoplayer-common | media3-common |
| exoplayer-core | media3-exoplayer |
| exoplayer-dash | media3-exoplayer-dash |
| exoplayer-extractor | media3-extractor |
| exoplayer-hls | media3-exoplayer-hls |
| exoplayer-robolectricutils | media3-test-utils-robolectric |
| exoplayer-rtsp | media3-exoplayer-rtsp |
| exoplayer-smoothstreaming | media3-exoplayer-smoothstreaming |
| exoplayer-testutils | media3-test-utils |
| exoplayer-transformer | media3-transformer |
| exoplayer-ui | media3-ui |
| extension-cast | media3-cast |
| extension-cronet | media3-datasource-cronet |
| extension-ima | media3-exoplayer-ima |
| extension-leanback | media3-ui-leanback |
| extension-okhttp | media3-datasource-okhttp |
| extension-rtmp | media3-datasource-rtmp |
| extension-workmanager | media3-exoplayer-workmanager |