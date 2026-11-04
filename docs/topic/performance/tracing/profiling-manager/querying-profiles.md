---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles
url: https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles
source: md.txt
---

You can query `ProfilingManager` profiles using [PerfettoSQL](https://perfetto.dev/docs/analysis/perfetto-sql-getting-started) and modules
from the [Perfetto Standard Library](https://perfetto.dev/docs/analysis/stdlib-docs). Because `ProfilingManager` [redacts
system traces](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze#visualize-trace) to include only your app's process data, system-wide standard
library queries that depend on other processes aren't supported. However, most
app-scoped queries and standard library modules work without modification. For
additional ready-to-use queries, see [Analyzing Android Traces](https://perfetto.dev/docs/getting-started/android-trace-analysis).

## ProfilingManager sample queries

Use the following sample queries directly or as templates for your own
PerfettoSQL analysis.

### Find the most duplicated slices

Repeated slices often point to redundant work. For details on function syntax,
see [Defining functions in PerfettoSQL](https://perfetto.dev/docs/analysis/perfetto-sql-syntax#defining-functions). The following query defines a
reusable PerfettoSQL function that finds slices matching a `GLOB` pattern and
sorts them by frequency:

    -- You only need to call this once in the session to create or update the function
    CREATE OR REPLACE PERFETTO FUNCTION find_duplicates(pattern STRING) RETURNS
    TABLE(name STRING, count_slice LONG) AS SELECT name, COUNT(dur) as count_slice FROM slice WHERE name GLOB $pattern GROUP BY name HAVING COUNT(name) >= 2 ORDER BY count_slice DESC;

    -- Subsequent calls can just use the function to find dupes
    SELECT * FROM find_duplicates('*Text*')

### Jank queries

Use the following queries to identify slow or janky frames in a system trace.

#### Find slow frames

This query finds frames that take longer than 16.6 ms (60 Hz) to render. Because
Perfetto stores slice durations in nanoseconds, `dur` is compared against
`16660000`:

    INCLUDE PERFETTO module android.frames.timeline;
    SELECT * FROM android_frames WHERE dur > 16660000;

#### Find jank-causing frames

This query uses the frame timeline module to find frames where the app missed
its rendering deadline according to the device's refresh rate:

    INCLUDE PERFETTO module android.frames.timeline;
    SELECT * FROM actual_frame_timeline_slice WHERE jank_type GLOB '*App Deadline Missed*';

### Find most duplicated objects

In a Java heap dump, this query returns the top 100 classes with two or more
instances to help you spot unintended duplicates or caching opportunities:

    INCLUDE PERFETTO MODULE android.memory.heap_graph.heap_graph_class_aggregation;

    SELECT * FROM android_heap_graph_class_aggregation WHERE obj_count >= 2
    ORDER BY obj_count DESC LIMIT 100

### Cold startup latency

This query estimates cold startup time to first frame (TTFF) by measuring the
duration between `bindApplication` and the first `Choreographer#doFrame` slice:

    -- This function finds slices that match the given GLOB $pattern
    CREATE OR REPLACE PERFETTO FUNCTION find_slices(pattern STRING) RETURNS
    TABLE (name STRING, ts LONG, dur LONG) AS
    SELECT name,ts,dur FROM slice WHERE name GLOB $pattern;

    -- This function generates a slice that starts at $startSlicePattern and finishes at the slice matched by $endSlicePattern. If $inclusive is true, then the end slice dur will be added, otherwise, the end slice start time will be used.
    CREATE OR REPLACE PERFETTO FUNCTION generate_start_to_end_slices(startSlicePattern STRING, endSlicePattern STRING, inclusive BOOL) RETURNS
    TABLE(name STRING, ts LONG, dur LONG) AS
    SELECT name, ts, MIN(startToEndDur) as dur
    FROM
      (SELECT S.name as name, S.ts as ts, E.ts + IIF($inclusive, E.dur, 0) - S.ts as startToEndDur
      FROM find_slices($startSlicePattern) as S CROSS JOIN find_slices($endSlicePattern) as E
      WHERE startToEndDur > 0)
    GROUP BY name, ts;

    -- Using these functions we can estimate cold startup time by generating a slice between bindApplication and first frame.
    SELECT * from generate_start_to_end_slices('bindApplication','*Choreographer#doFrame [0-9]*', true)