---
title: https://developer.android.com/games/develop/vulkan/detect-rendering-api
url: https://developer.android.com/games/develop/vulkan/detect-rendering-api
source: md.txt
---

While developing or optimizing Android games, it can often be helpful to
understand which graphics pipeline your engine is using; engines may choose
Vulkan or GLES without clearly developer-accessible signals. Unfortunately,
there are situations where relying on `logcat` to verify whether a game is
running on Vulkan or has silently fallen back to OpenGL ES can be unreliable.

This guide shows you how to use the [Android Performance Analyzer](https://developer.android.com/android-performance-analyzer) (APA) and
custom Perfetto SQL queries to definitively identify a game's active rendering
API.

## Limitations of log-based verification

- **Stripped logs**: Production builds often hide initialization and driver-loading footprints.
- **False positives**: Some game engines load both Vulkan and OpenGL ES libraries during startup, printing initialization logs for both, even if one eventually fails and triggers a fallback.
- **Silent fallbacks**: If Vulkan initialization fails due to device-specific driver issues, engines frequently fall back to OpenGL ES without throwing critical errors.

## Measure using APA

Using the Android Performance Analyzer, you can record a system trace
and precisely analyze frame data through SQL queries. Follow these steps to
measure your use of Vulkan and GLES:

1. **Capture the trace with APA**: Run your game and use APA to capture a
   system trace during the segment you want to analyze, such as a point during
   gameplay where you suspect frame drops. After the device is connected and
   the trace recording is complete, the trace data loads in the APA interface.

2. **Click the SQL tab in APA** : When the trace analysis screen is open, in the
   navigation menu of the UI, click the **SQL** tab to open the
   trace processor environment, where you can query the data directly.

3. **Paste the following SQL query in the APA SQL tab** : Copy the following SQL
   query and paste it into the query input field. This query scans the trace
   for drawing API events, such as `eglSwapBuffers`, `QueuePresentKHR`, and
   `vkQueuePresentKHR`. It groups them by process name and calculates the
   rendering API counts and percentage distribution of Vulkan versus OpenGL ES
   rendering calls:

       WITH raw_slices AS (
         -- 1. Map each slice (API call) to its corresponding process or package via UTID and UPID
         SELECT
           p.name AS process_name,
           s.name AS slice_name
         FROM slice s
         JOIN thread_track tt ON s.track_id = tt.id
         JOIN thread t USING (utid)
         JOIN process p USING (upid)
         WHERE (s.name LIKE 'eglSwapBuffers%'
           OR s.name IN ('QueuePresentKHR', 'vkQueuePresentKHR'))
           -- Optional: To isolate your game, uncomment the following and filter by package name and thread name:
           -- AND p.name = 'com.example.mygame'
           -- AND t.name = 'RenderThread'
       ),
       process_stats AS (
         -- 2. Aggregate counts per individual process
         SELECT
           process_name,
           SUM(CASE WHEN slice_name LIKE 'eglSwapBuffers%' THEN 1 ELSE 0 END) AS egl_count,
           SUM(CASE WHEN slice_name IN ('QueuePresentKHR', 'vkQueuePresentKHR') THEN 1 ELSE 0 END) AS vulkan_count
         FROM raw_slices
         GROUP BY process_name
       ),
       process_totals AS (
         -- 3. Calculate total counts for denominator calculation
         SELECT
           process_name,
           egl_count,
           vulkan_count,
           (egl_count + vulkan_count) AS total_count
         FROM process_stats
       )
       -- 4. Calculate final percentage shares per row, preventing division by zero errors
       SELECT
         process_name,
         egl_count,
         vulkan_count,
         total_count,
         ROUND(CAST(egl_count AS REAL) * 100 / NULLIF(total_count, 0), 2) AS "egl_percentage(%)",
         ROUND(CAST(vulkan_count AS REAL) * 100 / NULLIF(total_count, 0), 2) AS "vulkan_percentage(%)"
       FROM process_totals
       ORDER BY total_count DESC;

4. **Run the query** : Click the **Run Query** button near the input field.
   After the query runs, a table appears in the results pane showing the
   process name (`process_name`), OpenGL ES presentation count (`egl_count`),
   Vulkan presentation count (`vulkan_count`), total presentation count
   (`total_count`), and the percentage of each API used (`egl_percentage(%)`
   and `vulkan_percentage(%)`).

   ![](https://developer.android.com/static/images/games/vulkan_apa.png) Screen showing the executed SQL query and the resulting rendering API metrics displayed in a table

## Common pitfalls

- **Avoid `SurfaceFlinger` confusion** : Always scope your search to your
  game's application thread (`RenderThread`). System-wide compositor processes
  like `SurfaceFlinger` might show Vulkan or EGL tracks that represent system
  UI rendering, not your game's internal rendering pipeline. To isolate
  your game, uncomment the optional filters in the main SQL query's `WHERE`
  clause and replace `'com.example.mygame'` with your game's package name:

      -- AND p.name = 'com.example.mygame'
      -- AND t.name = 'RenderThread'

- **Warm-up period** : Always record the trace *after* the game's main 3D scene
  has fully loaded. Capturing during splash screens or loading transitions
  might result in misleading initializations.

## LevelUp Exemption Trace Requirements

If you are using the Android Performance Analyzer (APA) to capture a trace to
qualify for a Google Play Games LevelUp exemption, there are specific hardware
requirements for the trace to be valid.

It is highly preferred that you capture your trace using one of the targeted
[Level Up reference devices](https://developer.android.com/games/guidelines#referencedevice).

Furthermore, to ensure accurate validation, your trace must not be taken on a
device utilizing an ANGLE GPU. Specifically, you cannot use the following
devices to capture your [LevelUp exemption](https://developer.android.com/games/guidelines#exemptions-13) trace:

- Any device where the GPU vendor is SLSI (Samsung), which uses AMD Xclipse GPUs
- The Pixel 11