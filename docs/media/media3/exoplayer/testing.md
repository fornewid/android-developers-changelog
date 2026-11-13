---
title: https://developer.android.com/media/media3/exoplayer/testing
url: https://developer.android.com/media/media3/exoplayer/testing
source: md.txt
---

> Documentation index: https://developer.android.com/media/media3/exoplayer/llms.txt

Media3 provides dedicated testing artifacts (`media3-test-utils` and
`media3-test-utils-robolectric`) to help you test media playback, player state
transitions, UI components, and custom media sources in both local JVM tests
and device instrumentation tests.

This page outlines recommended practices for testing apps that use `ExoPlayer`
and shows how to use Media3's testing utilities in each test environment.

## Testing recommendations

When writing automated tests for media playback, follow these core principles:

- **Prefer real components or Media3 fakes over mocks** : Avoid mocking [`Player`](https://developer.android.com/reference/androidx/media3/common/Player.md.txt) or [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.md.txt) with frameworks such as Mockito. `Player` has state invariants and listener contracts that mocks don't enforce, which can make tests brittle or hide bugs. Instead, use a real `ExoPlayer` instance, [`FakePlayer`](https://developer.android.com/reference/androidx/media3/test/utils/FakePlayer.md.txt), or fakes such as [`FakeMediaSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeMediaSource.md.txt) and [`FakeDataSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeDataSource.md.txt). Reserve mocks for verifying custom callback invocations when needed.
- **Wait deterministically instead of sleeping** : `ExoPlayer` performs media loading and playback asynchronously on an internal thread. Avoid arbitrary `Thread.sleep` calls, which make tests slow and flaky. Use [`TestPlayerRunHelper`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.md.txt) in Robolectric tests and suspending `Player` extensions or [`PlayerFence`](https://developer.android.com/reference/androidx/media3/test/utils/PlayerFence.md.txt) in instrumentation tests. These helpers wait for explicit player conditions and fail immediately if a playback error occurs.
- **Access the player on its application thread** : `ExoPlayer` instances and waiting helpers must be called on the player's application `Looper` thread (typically the main thread). For more information, see the [ExoPlayer
  threading requirements](https://developer.android.com/media/media3/exoplayer/hello-world#a-note-on-threading).

### Choose the right test environment

Different layers of your media integration benefit from different test
environments:

| Test target | Recommended environment | Key Media3 utilities |
|---|---|---|
| UI components (`PlayerView`, Compose UI), ViewModels, or `MediaSession` callbacks | Local Robolectric tests (`src/test`) or instrumented UI tests (`src/androidTest`) | [`FakePlayer`](https://developer.android.com/reference/androidx/media3/test/utils/FakePlayer.md.txt) |
| `ExoPlayer` integration, playlist transitions, analytics, and custom `MediaSource` or `DataSource` logic | Local Robolectric tests (`src/test`) | [`TestExoPlayerBuilder`](https://developer.android.com/reference/androidx/media3/test/utils/TestExoPlayerBuilder.md.txt), [`TestPlayerRunHelper`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.md.txt), [`FakeMediaSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeMediaSource.md.txt) |
| Real hardware `MediaCodec` decoding, `Surface` rendering, audio output, and DRM | Instrumentation tests on physical devices (`src/androidTest`) | [`ExoPlayer.Builder`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder.md.txt), `Player.await*` extensions, [`PlayerFence`](https://developer.android.com/reference/androidx/media3/test/utils/PlayerFence.md.txt) |

Where possible, run instrumentation playback tests on physical devices rather
than emulators, because emulator media stack implementations vary. For more
information about emulator support, see the [supported devices
guide](https://developer.android.com/media/media3/exoplayer/supported-devices#emulators).

## Add testing dependencies

Add the Media3 test artifacts to the `dependencies` block of your module's
`build.gradle.kts` or `build.gradle` file using the same version as your other
Media3 modules:

### Kotlin

```kotlin
testImplementation("androidx.media3:media3-test-utils:1.11.1")
testImplementation("androidx.media3:media3-test-utils-robolectric:1.11.1")
androidTestImplementation("androidx.media3:media3-test-utils:1.11.1")
```

### Groovy

```groovy
testImplementation "androidx.media3:media3-test-utils:1.11.1"
testImplementation "androidx.media3:media3-test-utils-robolectric:1.11.1"
androidTestImplementation "androidx.media3:media3-test-utils:1.11.1"
```

The two modules divide responsibilities by runtime environment:

- `media3-test-utils`: Cross-environment utilities for both local and instrumented tests, including [`TestExoPlayerBuilder`](https://developer.android.com/reference/androidx/media3/test/utils/TestExoPlayerBuilder.md.txt), [`PlayerFence`](https://developer.android.com/reference/androidx/media3/test/utils/PlayerFence.md.txt) (and Kotlin `Player.await*` extensions), [`FakePlayer`](https://developer.android.com/reference/androidx/media3/test/utils/FakePlayer.md.txt), [`FakeClock`](https://developer.android.com/reference/androidx/media3/test/utils/FakeClock.md.txt), [`FakeMediaSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeMediaSource.md.txt), [`FakeDataSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeDataSource.md.txt), [`DataSourceContractTest`](https://developer.android.com/reference/androidx/media3/test/utils/DataSourceContractTest.md.txt), and [`Media3FlagsRule`](https://developer.android.com/reference/androidx/media3/test/utils/Media3FlagsRule.md.txt).
- `media3-test-utils-robolectric`: Utilities for [Robolectric](https://developer.android.com/training/testing/local-tests/robolectric.md.txt) tests on the local JVM, including [`TestPlayerRunHelper`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.md.txt), [`RobolectricUtil`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/RobolectricUtil.md.txt), [`ShadowMediaCodecConfig`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/ShadowMediaCodecConfig.md.txt), [`CapturingRenderersFactory`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/CapturingRenderersFactory.md.txt), and [`PlaybackOutput`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/PlaybackOutput.md.txt).

Make sure your module also includes the test framework dependencies for your
test environments:

- Robolectric: `org.robolectric:robolectric`. Set `android.testOptions.unitTests.isIncludeAndroidResources = true` when loading local assets.
- [AndroidX Test](https://developer.android.com/training/testing/instrumented-tests.md.txt): `androidx.test:runner`, `androidx.test:core`, and `androidx.test.ext:junit`.
- Kotlin coroutines on the main thread: `org.jetbrains.kotlinx:kotlinx-coroutines-android`.

### Opt in to unstable testing APIs

Classes and methods in `media3-test-utils` and `media3-test-utils-robolectric`
are annotated with [`@UnstableApi`](https://developer.android.com/reference/androidx/media3/common/util/UnstableApi.md.txt). Although Media3 aims to keep
widely used test helpers ergonomic across releases, test utilities don't follow
the same binary compatibility stability rules as production playback APIs.

In your test source sets, annotate test classes or methods with
`@androidx.annotation.OptIn`, add a `package-info` opt-in for your test
packages, or configure `lint.xml` for test sources. For more information, see
the [unstable API lint troubleshooting notes](https://developer.android.com/media/media3/exoplayer/troubleshooting.md.txt#unstable-api-lint-errors).

## Local tests with Robolectric

Local [Robolectric](https://developer.android.com/training/testing/local-tests/robolectric.md.txt) tests run on your development machine's JVM
without a physical device or emulator. Robolectric doesn't provide
`MediaCodec` implementations, and it keeps the main `Looper` paused until
explicitly pumped, so a default `ExoPlayer` instance can't decode media or
deliver state updates on its own.

### Build a test player and advance playback

Use [`TestExoPlayerBuilder`](https://developer.android.com/reference/androidx/media3/test/utils/TestExoPlayerBuilder.md.txt) to create an `ExoPlayer`
configured for Robolectric tests. By default, `TestExoPlayerBuilder` configures
the following components:

- An auto-advancing [`FakeClock`](https://developer.android.com/reference/androidx/media3/test/utils/FakeClock.md.txt) (`isAutoAdvancing = true`) that coordinates time progression between `ExoPlayer`'s background playback thread and Robolectric's paused main `Looper`.
- Fake video and audio renderers ([`FakeVideoRenderer`](https://developer.android.com/reference/androidx/media3/test/utils/FakeVideoRenderer.md.txt) and [`FakeAudioRenderer`](https://developer.android.com/reference/androidx/media3/test/utils/FakeAudioRenderer.md.txt)) that consume media samples according to their timestamps without requiring `MediaCodec` decoders.

To progress playback and assert outcomes on the main thread (with a player using
`Looper.getMainLooper`, the default in Robolectric), use the static
`advance(player)` or `play(player)` methods on
[`TestPlayerRunHelper`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.md.txt) (`play(player)` calls
`player.play` before waiting). For most conditions, the helper pumps
Robolectric's main `Looper` until the target condition is met and throws an
exception if a fatal or nonfatal playback error occurs:


### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
@OptIn(UnstableApi::class)
class PlaybackRobolectricTest {

  private lateinit var player: ExoPlayer

  @After
  fun tearDown() {
    if (::player.isInitialized) {
      player.release()
    }
  }

  @Test
  fun play_sampleMediaItem_reachesEndedState() {
    val context = ApplicationProvider.getApplicationContext<Context>()
    player = TestExoPlayerBuilder(context).build()
    player.setMediaItem(MediaItem.fromUri("asset:///media/mp4/sample.mp4"))
    player.prepare()

    play(player).untilState(Player.STATE_ENDED)

    assertThat(player.playbackState).isEqualTo(Player.STATE_ENDED)
  }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@OptIn(markerClass = UnstableApi.class)
public static class PlaybackRobolectricTest {

  private @Nullable ExoPlayer player;

  @After
  public void tearDown() {
    if (player != null) {
      player.release();
    }
  }

  @Test
  public void play_sampleMediaItem_reachesEndedState() throws Exception {
    Context context = ApplicationProvider.getApplicationContext();
    player = new TestExoPlayerBuilder(context).build();
    player.setMediaItem(MediaItem.fromUri("asset:///media/mp4/sample.mp4"));
    player.prepare();

    play(player).untilState(Player.STATE_ENDED);

    assertThat(player.getPlaybackState()).isEqualTo(Player.STATE_ENDED);
  }
}
```

<br />

In this example, `asset:///media/mp4/sample.mp4` refers to a sample media file
placed in your module's `src/test/assets/` (or `src/main/assets/`) directory.

When passed an `ExoPlayer` reference, `advance(player)` and `play(player)`
return an [`ExoPlayerRunResult`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.ExoPlayerRunResult.md.txt) (or
[`PlayerRunResult`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.PlayerRunResult.md.txt) when passed a `Player`). These result
types provide methods for waiting on playback states, positions, playlist
transitions, rendered frames, pending commands, and expected playback errors, or
ignoring nonfatal errors. For more information about waiting conditions, see the
[`TestPlayerRunHelper`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/TestPlayerRunHelper.md.txt) API reference.

### Test with fake sources and simulated codecs

Many integration tests verify playlist navigation, track selection, timeline
updates, or retry behavior and don't need real media files. You can feed
synthetic timelines and data into a `TestExoPlayerBuilder` player using
[`FakeMediaSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeMediaSource.md.txt), [`FakeTimeline`](https://developer.android.com/reference/androidx/media3/test/utils/FakeTimeline.md.txt),
[`FakeDataSource`](https://developer.android.com/reference/androidx/media3/test/utils/FakeDataSource.md.txt), or
[`WebServerDispatcher`](https://developer.android.com/reference/androidx/media3/test/utils/WebServerDispatcher.md.txt) (with OkHttp `MockWebServer`):


### Kotlin

```kotlin
val player = TestExoPlayerBuilder(context).build()
val fakeMediaSource = FakeMediaSource(FakeTimeline(/* windowCount= */ 2))
player.setMediaSource(fakeMediaSource)
player.prepare()

play(player).untilMediaItemIndex(/* mediaItemIndex= */ 1)

assertThat(player.currentMediaItemIndex).isEqualTo(1)
player.release()
```

### Java

```java
ExoPlayer player = new TestExoPlayerBuilder(context).build();
FakeMediaSource fakeMediaSource = new FakeMediaSource(new FakeTimeline(/* windowCount= */ 2));
player.setMediaSource(fakeMediaSource);
player.prepare();

play(player).untilMediaItemIndex(/* mediaItemIndex= */ 1);

assertThat(player.getCurrentMediaItemIndex()).isEqualTo(1);
player.release();
```

<br />

`TestExoPlayerBuilder` uses fake renderers by default. If your Robolectric test
needs `MediaCodec` interactions instead, configure simulated codecs and output
capture as follows:

1. Add `withAllDefaultSupportedCodecs` from [`ShadowMediaCodecConfig`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/ShadowMediaCodecConfig.md.txt) as a JUnit `@Rule` to register Robolectric's simulated codecs.
2. Pass a [`CapturingRenderersFactory`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/CapturingRenderersFactory.md.txt) built with the builder's `Clock` (`CapturingRenderersFactory(context,
   builder.getClock())`) to `builder.setRenderersFactory`.
3. When testing video tracks, attach a `Surface` (such as `Surface(SurfaceTexture(1))`) with `player.setVideoSurface` so `MediaCodecVideoRenderer` renders decoded frames instead of skipping them.
4. To verify rendered output, call `register(player,
   capturingRenderersFactory)` on [`PlaybackOutput`](https://developer.android.com/reference/androidx/media3/test/utils/robolectric/PlaybackOutput) before starting playback.
5. After playback finishes, release the player and surface, and then inspect the formatted output from [`Dumper`](https://developer.android.com/reference/androidx/media3/test/utils/Dumper.md.txt) (`Dumper().add(playbackOutput).toString()`).

## Instrumentation tests on devices

Local Robolectric tests don't execute real platform decoders, audio tracks, DRM
sessions, or `Surface` rendering. To verify end-to-end playback behavior on
devices that run Android, write [instrumented tests](https://developer.android.com/training/testing/instrumented-tests.md.txt) in
`src/androidTest` using a real `ExoPlayer` built with `ExoPlayer.Builder`.

In JUnit instrumentation tests, `@Test` methods run on an instrumentation
thread rather than the application's main thread. Always create, control, and
release `ExoPlayer` on its application `Looper` thread, for example by using
`runBlocking(Dispatchers.Main)` in Kotlin or
`InstrumentationRegistry.getInstrumentation().runOnMainSync` in Java.

### Wait for player states with PlayerFence and coroutines

In instrumentation tests, the main `Looper` runs in real time on the device.
Don't include Robolectric or `media3-test-utils-robolectric` in
`androidTestImplementation` dependencies. To wait for playback states and
events, `media3-test-utils` provides the following helpers:

- **Kotlin** : Suspending extension functions on `Player` (such as [`awaitPlaybackState`](https://developer.android.com/reference/kotlin/androidx/media3/test/utils/package-summary.md.txt#(androidx.media3.common.Player).awaitPlaybackState(kotlin.Int,kotlin.Boolean,kotlin.time.Duration)), [`awaitIsPlaying`](https://developer.android.com/reference/kotlin/androidx/media3/test/utils/package-summary.md.txt#(androidx.media3.common.Player).awaitIsPlaying(kotlin.Boolean,kotlin.Boolean,kotlin.time.Duration)), [`awaitFirstFrameRendered`](https://developer.android.com/reference/kotlin/androidx/media3/test/utils/package-summary.md.txt#(androidx.media3.common.Player).awaitFirstFrameRendered(kotlin.Boolean,kotlin.time.Duration)), and [`awaitContentPositionAtLeast`](https://developer.android.com/reference/kotlin/androidx/media3/test/utils/package-summary.md.txt#(androidx.media3.common.Player).awaitContentPositionAtLeast(kotlin.Long,kotlin.Boolean,kotlin.time.Duration))).
- **Java** : The static `futureWhen(player)` method on [`PlayerFence`](https://developer.android.com/reference/androidx/media3/test/utils/PlayerFence.md.txt), which returns a `PlayerFence` whose condition methods (such as `entersPlaybackState` and `isPlaying`) must be called on the player's `Looper` thread and return a `ListenableFuture` that the test thread can block on with `get`.

Both APIs supervise the player while waiting. If a fatal playback error (or, by
default, a nonfatal error) occurs, or if the wait exceeds its timeout (10
seconds by default, or 30 seconds on an emulator), the call fails immediately
instead of hanging:


### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
@OptIn(UnstableApi::class)
class PlaybackInstrumentationTest {

  private lateinit var player: ExoPlayer

  @After
  fun tearDown() =
    runBlocking(Dispatchers.Main) {
      if (::player.isInitialized) {
        player.release()
      }
    }

  @Test
  fun play_sampleMediaItem_advancesAndEnds() =
    runBlocking(Dispatchers.Main) {
      val context = ApplicationProvider.getApplicationContext<Context>()
      player = ExoPlayer.Builder(context).build()
      player.setMediaItem(MediaItem.fromUri("asset:///media/mp4/sample.mp4"))
      player.prepare()

      player.play()
      player.awaitIsPlaying(true)
      player.awaitContentPositionAtLeast(500)
      player.awaitPlaybackState(Player.STATE_ENDED)

      assertThat(player.playbackState).isEqualTo(Player.STATE_ENDED)
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@OptIn(markerClass = UnstableApi.class)
public static class PlaybackInstrumentationTest {

  private @Nullable ExoPlayer player;

  @After
  public void tearDown() {
    InstrumentationRegistry.getInstrumentation()
        .runOnMainSync(() -> {
          if (player != null) {
            player.release();
          }
        });
  }

  @Test
  public void play_sampleMediaItem_advancesAndEnds() throws Exception {
    SettableFuture<Void> playbackStarted = SettableFuture.create();
    SettableFuture<Void> positionPassed = SettableFuture.create();
    SettableFuture<Void> playbackEnded = SettableFuture.create();
    InstrumentationRegistry.getInstrumentation()
        .runOnMainSync(() -> {
          Context context = ApplicationProvider.getApplicationContext();
          player = new ExoPlayer.Builder(context).build();
          player.setMediaItem(MediaItem.fromUri("asset:///media/mp4/sample.mp4"));
          playbackStarted.setFuture(futureWhen(player).isPlaying(true));
          positionPassed.setFuture(futureWhen(player).passesContentPosition(500));
          playbackEnded.setFuture(futureWhen(player).entersPlaybackState(Player.STATE_ENDED));
          player.prepare();
          player.play();
        });

    playbackStarted.get();
    positionPassed.get();
    playbackEnded.get();

    InstrumentationRegistry.getInstrumentation()
        .runOnMainSync(() -> assertThat(player.getPlaybackState()).isEqualTo(Player.STATE_ENDED));
  }
}
```

<br />

When building `ExoPlayer` with `ApplicationProvider.getApplicationContext` in
an app module (`com.android.application`), `asset:///` URIs resolve against the
target app's assets (such as `src/debug/assets/` or `src/main/assets/`, rather
than `src/androidTest/assets/`).

### Transient events and custom supervision

In addition to checking current player state (where waits return immediately if
the condition is already met), the helpers in `media3-test-utils` support
one-off events and custom listener conditions:

- **Transient events such as first rendered frame** : Attach a video output (such as a `Surface` or `PlayerView`) to the player, and start waiting with `awaitFirstFrameRendered` or `rendersFirstFrame` before calling `player.prepare` so an early one-off frame event isn't missed.
- **Custom conditions** : Wrap custom listener or coroutine waits inside [`awaitSupervised`](https://developer.android.com/reference/kotlin/androidx/media3/test/utils/package-summary.md.txt#(androidx.media3.common.Player).awaitSupervised(kotlin.Boolean,kotlin.time.Duration,kotlin.coroutines.SuspendFunction1)) on `player` in Kotlin, or pass a custom `ListenableFuture` to `futureWhen(player).withSupervision(future)` in Java. When testing recovery from nonfatal errors, pass `failOnNonFatalErrors = false` (Kotlin) or call `ignoringNonFatalErrors` (Java), and customize timeouts with `timeout` or `withTimeoutMs(timeoutMs)`.

The following example waits for a transient first-frame event and supervises a
custom metadata listener:


### Kotlin

```kotlin
// Start awaiting transient events (with a video surface attached) before prepare().
coroutineScope {
  val firstFrameDeferred =
    async(start = CoroutineStart.UNDISPATCHED) { player.awaitFirstFrameRendered() }
  player.setMediaItem(mediaItem)
  player.prepare()
  player.play()
  firstFrameDeferred.await()
}

// Supervise a custom listener condition while still failing fast on player errors.
val metadataTitle = player.awaitSupervised {
  player.mediaMetadata.title?.let {
    return@awaitSupervised it
  }
  val titleDeferred = CompletableDeferred<CharSequence>()
  val listener =
    object : Player.Listener {
      override fun onMediaMetadataChanged(mediaMetadata: MediaMetadata) {
        mediaMetadata.title?.let { titleDeferred.complete(it) }
      }
    }
  player.addListener(listener)
  try {
    titleDeferred.await()
  } finally {
    player.removeListener(listener)
  }
}
```

### Java

```java
SettableFuture<Void> firstFrameFuture = SettableFuture.create();
SettableFuture<CharSequence> metadataTitleFuture = SettableFuture.create();
SettableFuture<CharSequence> supervisedTitleFuture = SettableFuture.create();
Player.Listener metadataListener =
    new Player.Listener() {
      @Override
      public void onMediaMetadataChanged(MediaMetadata mediaMetadata) {
        if (mediaMetadata.title != null) {
          metadataTitleFuture.set(mediaMetadata.title);
        }
      }
    };

try {
  InstrumentationRegistry.getInstrumentation()
      .runOnMainSync(() -> {
        // Register transient event fences (with a video surface attached) before prepare().
        firstFrameFuture.setFuture(futureWhen(player).rendersFirstFrame());

        // Supervise a custom ListenableFuture so player errors fail fast.
        player.addListener(metadataListener);
        supervisedTitleFuture.setFuture(
            futureWhen(player).withSupervision(metadataTitleFuture));

        player.setMediaItem(mediaItem);
        if (player.getMediaMetadata().title != null) {
          metadataTitleFuture.set(player.getMediaMetadata().title);
        }
        player.prepare();
        player.play();
      });

  firstFrameFuture.get();
  CharSequence title = supervisedTitleFuture.get();
} finally {
  InstrumentationRegistry.getInstrumentation()
      .runOnMainSync(() -> {
        player.removeListener(metadataListener);
        firstFrameFuture.cancel(/* mayInterruptIfRunning= */ true);
        supervisedTitleFuture.cancel(/* mayInterruptIfRunning= */ true);
      });
}
```

<br />

## Test UI and app components with FakePlayer

When testing UI components such as `PlayerView` or `media3-ui-compose`
composables, ViewModels, or `MediaSession` callbacks, creating a full
`ExoPlayer` is often unnecessary. [`FakePlayer`](https://developer.android.com/reference/androidx/media3/test/utils/FakePlayer.md.txt) in
`media3-test-utils` extends [`SimpleBasePlayer`](https://developer.android.com/reference/androidx/media3/common/SimpleBasePlayer.md.txt) to
simulate playlists, playback states, positions, video sizes, cues, and errors on
the calling thread's `Looper`. This `Looper` is available automatically in
Robolectric tests with `@RunWith(AndroidJUnit4::class)` and on the main thread
in instrumented tests.

By default, `FakePlayer` simulates a 100 ms buffering delay on `prepare` and
`seekTo`; pass `bufferingDelayMs = 0` in Kotlin or set states directly with
`setPlaybackState`:


### Kotlin

```kotlin
val fakePlayer = FakePlayer(bufferingDelayMs = 0)
fakePlayer.setMediaItem(MediaItem.fromUri("https://example.com/media.mp4"))
fakePlayer.prepare()
fakePlayer.play()

assertThat(fakePlayer.isPlaying).isTrue()

// Drive state transitions directly to test UI or session listeners.
fakePlayer.setPosition(30_000)
fakePlayer.setPlaybackState(Player.STATE_ENDED)
fakePlayer.release()
```

### Java

```java
FakePlayer fakePlayer = new FakePlayer();
fakePlayer.setMediaItem(MediaItem.fromUri("https://example.com/media.mp4"));
// Drive state transitions directly (prepare() simulates a 100 ms buffering delay by default).
fakePlayer.setPlaybackState(Player.STATE_READY);
fakePlayer.play();

assertThat(fakePlayer.isPlaying()).isTrue();

fakePlayer.setPosition(30_000);
fakePlayer.setPlaybackState(Player.STATE_ENDED);
fakePlayer.release();
```

<br />

## Additional testing utilities

`media3-test-utils` includes specialized helpers for other testing scenarios:

- **Feature flags and Canary mode** : Use [`Media3FlagsRule`](https://developer.android.com/reference/androidx/media3/test/utils/Media3FlagsRule.md.txt) together with [`@BindFlag`](https://developer.android.com/reference/androidx/media3/test/utils/BindFlag.md.txt) and [`@BindCanaryMode`](https://developer.android.com/reference/androidx/media3/test/utils/BindCanaryMode.md.txt) to reset flag overrides after each test and run parameterized tests across flag states. For more information, see [testing with feature
  flags](https://developer.android.com/media/media3/exoplayer/flags#testing-with-flags).
- **Custom `DataSource` contract tests** : Subclass [`DataSourceContractTest`](https://developer.android.com/reference/androidx/media3/test/utils/DataSourceContractTest.md.txt) to verify that custom `DataSource` or `HttpDataSource` implementations conform to Media3's contract expectations across range requests, error handling, and transfer listeners. For more information, see [integrating other network
  stacks](https://developer.android.com/media/media3/exoplayer/network-stacks#other-network).