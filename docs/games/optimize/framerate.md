---
title: https://developer.android.com/games/optimize/framerate
url: https://developer.android.com/games/optimize/framerate
source: md.txt
---

## Average FPS

A smooth and stable frame rate is critical to delivering a high-quality
gaming experience on Android devices. When measuring game performance, you
should
measure average FPS as a *baseline* to give a basic understanding of the
experience. You should optimize your game to meet the average frame rate of 60
FPS to ensure a great gaming experience.

## P90 and P99 FPS for stability

With a smooth average 60 FPS, a game can still experience intermittent hitches,
micro-stuttering, and unpredictable input lag, resulting in a poor player
experience.

So frame stability is just as crucial as tracking the average frame rate.
This is where you should measure the P90 and P99 frame rate metrics as
the consistent baseline and the stutter indicator respectively. These
metrics capture the "tail end" of performance for you to optimize the smoothness
of the player experience.

## Metrics

- **Average FPS (baseline)**: This fundamental metric provides a general baseline of your game's performance. While it's a standard benchmark, the average calculation means that intermittent frame drops and micro-stuttering can't be detected, making it insufficient to represent the player experience on its own.
- **P90 FPS (consistent baseline at 10% percentile)**: This indicates that 90% of your frames exceeded this consistent baseline, and only the slowest 10% of frames took longer to render. If your P90 frame rate is high and close to your average, the game is running consistently well for the vast majority of the session.
- **P99 FPS (stutter indicator at 1% percentile)**: This indicates that 99% of your frames exceeded this stutter indicator, specifically isolating the slowest 1% of frames. This metric is essential for catching micro-stutters, asset-loading delays, and sudden asset-heavy rendering spikes that cause visible hitches.

## Examples

By comparing your average FPS against the P90 and P99 metrics, you can
accurately diagnose the underlying behavior of a game.

**Scenario 1: An Optimal Curve (Optimized Game)**

- **Average**: 60 FPS (16.6 ms)
- **P90**: 58 FPS (17.2 ms)
- **P99**: 52 FPS (19.2 ms)
- **Analysis**: The metrics are tightly clustered. The game feels incredibly smooth and consistent. There are no micro-stutters, and even the worst 1% of frames are barely noticeable to the human eye.

**Scenario 2: Load Bottleneck (CPU/GPU Bound)**

- **Average**: 45 FPS (22.2 ms)
- **P90**: 40 FPS (25.0 ms)
- **P99**: 38 FPS (26.3 ms)
- **Analysis**: The average frame rate is lower, but consistently so. P99 does not drop drastically compared to the average. This indicates that the system is essentially overwhelmed by graphical settings or resolution constraints. The game won't feel like it is stuttering, but rather sluggish. Lowering graphics settings will typically uniformly scale up these metrics.

**Scenario 3: An unstable 60 FPS (Shader Compilation / Asset Streaming
Stutters)**

- **Average**: 60 FPS (16.6 ms)
- **P90**: 45 FPS (22.2 ms)
- **P99**: 15 FPS (66.6 ms)
- **Analysis**: This is the worst-case scenario. While the average frame rate appears excellent, the P99 reveals a critical issue. P99 at 66.6 ms means the game is completely freezing for multiple frames at a time. This points to severe outliers---usually caused by CPU bottlenecks, asset streaming delays (for example, slow RAM or storage), or hitches caused by shader compilation.

## Measurement

To effectively measure Average FPS, P90, and P99, you can use the Android
[dumpsys](https://developer.android.com/tools/dumpsys) [surfaceflinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager) timestats command. This tool provides the
average FPS and a `presentToPresent` timing histogram for all layers that are
being rendered. The `presentToPresent` time of a frame is the interval between
the current frame and the previous frame being drawn.

Here are the step-by-step instructions to collect and calculate these metrics
for your game:

1. **Start capturing**: Run the following command with the enable and clear
   flags to start capturing information:

       adb shell dumpsys SurfaceFlinger --timestats -clear -enable

2. **Dump information**: When the game has been played long enough, run the
   command again with the dump flag to output the information:

       adb shell dumpsys SurfaceFlinger --timestats -dump

3. **Filter by layer** : The dumped information provides data for all layers
   rendered by SurfaceFlinger. You must find the section corresponding to your game
   by filtering based on the `layerName` (for example, layerName =
   SurfaceView\[com.example.yourgame...\]).

       layerName = SurfaceView[com.google.test/com.devrel.MainActivity]@0(BLAST)#132833

4. **Identify average FPS**: The Average FPS for each layer is calculated
   automatically and is shown directly in the dump output (for example,
   averageFPS = 30.179).

       ...
       averageFPS = 30.179
       ...

5. **Calculate P90 and P99 FPS** : To find the P90 and P99 metrics, you need to
   analyze the totalFrames and the `presentToPresent` timing histogram provided in
   the dump.

       totalFrames = 1000
       ...
       presentToPresent histogram is as below:
       0ms=0 1ms=0 2ms=0 3ms=0 4ms=0 5ms=0 6ms=0 7ms=0 8ms=0 9ms=0 10ms=0 11ms=0 12ms=0
       13ms=0 14ms=0 15ms=0 16ms=850 17ms=0 18ms=0 19ms=0 20ms=0 21ms=0 22ms=0 23ms=0
       24ms=0 25ms=0 26ms=0 27ms=0 28ms=0 29ms=0 30ms=0 31ms=0 32ms=0 33ms=100 34ms=0
       36ms=0 38ms=0 40ms=0 42ms=0 44ms=0 46ms=0 48ms=0 50ms=35 54ms=0 58ms=0 62ms=0
       66ms=10 70ms=0 74ms=0 78ms=0 82ms=0 86ms=0 90ms=0 94ms=0 98ms=0 102ms=5 106ms=0
       110ms=0 114ms=0 118ms=0 122ms=0 126ms=0 130ms=0 134ms=0 138ms=0 142ms=0 146ms=0
       150ms=0 200ms=0 250ms=0 300ms=0 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0
       650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0

   **A. Conceptual Example (Cumulative Distribution Table)** Assume your game
   session recorded a totalFrames count of 1,000. To find P90 and P99, you
   calculate the millisecond thresholds where the cumulative frame count reaches
   900 frames (90%) and 990 frames (99%) respectively, counting up from the
   lowest millisecond bucket.

   | Frame Time (ms) | Frame Count (Histogram) | Cumulative Frame Count | Percentile Status / Calculation |
   |---|---|---|---|
   | 16ms | 850 | 850 | 85.0% |
   | **33ms** | 100 | 950 | 95.0% (**P90 Target of 900 Reached! → 1000/33 = 30.3 FPS**) |
   | 50ms | 35 | 985 | 98.5% |
   | **66ms** | 10 | 995 | 99.5% (**P99 Target of 990 Reached! → 1000/66 = 15.1 FPS**) |
   | 102ms | 5 | 1,000 | 100% |

   **B. Implementation Logic (Pseudocode)** If you are automating this analysis
   using a Python script or log parser, the logic to extract P90 and P99 values
   from the histogram can be implemented as follows:

       # Define target thresholds based on total frame count
       p90_target = totalFrames * 0.90
       p99_target = totalFrames * 0.99

       cumulative_frames = 0
       p90_fps = None
       p99_fps = None

       # Iterate through the parsed SurfaceFlinger histogram data (sorted by millisecond)
       for ms_bucket, frame_count in present_to_present_histogram:
           cumulative_frames += frame_count

           # Capture P90 when cumulative frames cross the 90% threshold
           if p90_fps is None and cumulative_frames >= p90_target:
               p90_fps = 1000 / ms_bucket

           # Capture P99 when cumulative frames cross the 99% threshold
           if p99_fps is None and cumulative_frames >= p99_target:
               p99_fps = 1000 / ms_bucket
               break # Optimization: stop iterating once both targets are found

6. **Stop capturing**: After collecting all necessary information, you should
   disable the timestats by using the disable flag:

       adb shell dumpsys SurfaceFlinger --timestats -disable

## Slow Sessions

[Slow Sessions](https://developer.android.com/games/optimize/vitals/slow-session) identify widespread real-world performance issues. A session
is "slow" if over 25% of frames drop below a threshold (for example, 20 FPS).
While useful for spotting critical build issues, this metric alone cannot
guarantee a high-quality, sustainable experience. A game might avoid the Slow
Session threshold but still suffer from micro-stuttering that compromises a
smooth 60 FPS experience.

While both derived from frame times, 'Slow Session' and 'Frame Rate' serve
different roles. Average, P90, and P99 FPS metrics measure the quality and
sustainability of performance, detecting instantaneous drops and inconsistent
pacing that the Slow Session metric might overlook.

## Conclusion

Successful performance optimization requires a comprehensive strategy.
Developers should use Slow Sessions as a primary radar to catch severe
performance degradation, and then examine average FPS, P90, and P99 to diagnose
the underlying causes and verify the actual smoothness of the gameplay. By
integrating these metrics, you can ensure your application delivers a
consistently sustainable and exceptional user experience.

## Additional resources

To learn more about advanced profiling techniques, implementing the Frame Pacing
API, and engine-specific optimization strategies, check out the official Android
developer documentation:

- **[Android Vitals: Slow sessions](https://developer.android.com/games/optimize/vitals/slow-session)**: Understand how Google Play measures and reports sustained periods of slow rendering, which directly impacts the user experience. A "slow session" is defined as a user session where more than 25% of the frames are slow (for example, taking more than 50ms, equivalent to 20 FPS).
- **[Android Developers: Optimize Game Performance](https://developer.android.com/games/optimize/gameperformance)** : Explore the central hub for Android game optimization. This comprehensive guide covers best practices, profiling tools (like [Android Performance Analyzer(APA)](https://developer.android.com/android-performance-analyzer) and [Perfetto](https://perfetto.dev/)) to help you maximize your game's overall performance.