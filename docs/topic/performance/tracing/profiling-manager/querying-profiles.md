---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles
url: https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles
source: md.txt
---

<br />

Querying `ProfilingManager` profiles is similar to querying regular Perfetto
profiles. Therefore, review [Getting Started with PerfettoSQL](https://perfetto.dev/docs/analysis/perfetto-sql-getting-started) for a guide on
how to query profiles.

An important distinction between regular Perfetto traces and `ProfilingManager`
traces is that `ProfilingManager` traces pass through a trace redactor. This
redactor removes information about other processes unrelated to your app for
privacy reasons.

Some queries from the Perfetto standard library are not usable on redacted
traces. This is because `ProfilingManager` only collects profiling data for your
app, not other processes. As a result, the queries you can use with
`ProfilingManager` are a smaller set than those for full system profiles
recorded using local Perfetto.

Even though the querying space is reduced, you can still use many PerfettoSQL
queries and tables from the [Perfetto Standard Library](https://perfetto.dev/docs/analysis/stdlib-docs) as-is, so we
encourage you to try them.

We also recommend that you review [Analyzing Android Traces](https://perfetto.dev/docs/getting-started/android-trace-analysis) to find
ready-to-use queries that provide useful performance data without modification.

## ProfilingManager sample queries

To simplify the querying journey, this section provides a list of queries that
work with `ProfilingManager`. You can use these queries directly or as examples
to build other queries.

### Find the most duplicated slices

This query finds repeated slices in a trace and sorts them by how often they
appear, showing the most duplicated ones first.

Finding duplicated work is a common way to find unnecessary work in a trace.

> [!NOTE]
> **Note:** This query defines a Perfetto function that lets you use any GLOB pattern to find duplicates, making it easier to reuse. For more information on functions, checkout [Perfetto SQL Syntax docs](https://perfetto.dev/docs/analysis/perfetto-sql-syntax#defining-functions).

    -- You only need to call this once in the session to create the function
    DROP TABLE IF EXISTS find_duplicates;
    CREATE PERFETTO FUNCTION find_duplicates(pattern STRING) RETURNS
    TABLE(name STRING, count_slice LONG) AS SELECT name, COUNT(dur) as count_slice FROM slice WHERE name GLOB $pattern GROUP BY name HAVING COUNT(name) >= 2 ORDER BY count_slice DESC;

    -- Subsequent calls can just use the function to find dupes
    SELECT * FROM find_duplicates('*Text*')

### Jank queries

#### Find slow frames

This query finds frames where your app takes too long to generate a frame,
assuming an expected frame rate of 60 Hz (16.6 ms). The `dur` is set to
16,660,000 because slice durations in Perfetto tables are stored in nanoseconds.

    INCLUDE PERFETTO module android.frames.timeline;
    SELECT * FROM android_frames WHERE dur > 16660000;

#### Find jank-causing frames

    INCLUDE PERFETTO module android.frames.timeline;
    SELECT * FROM actual_frame_timeline_slice WHERE jank_type = 'App Deadline Missed';

This query is useful to find locations where jank occurs in the trace because
the app takes too long to generate a frame. This means that the UI thread failed
to generate a frame. Under extreme circumstances, this could precede an ANR.

> [!NOTE]
> **Note:** Jank detection in this query depends on the device refresh rate. A higher refresh rate means less tolerance for jank.

### Find most duplicated objects

You can also query memory-related profiles, such as heap dumps, to perform more
complex memory analyses.

    INCLUDE PERFETTO MODULE android.memory.heap_graph.heap_graph_class_aggregation;

    SELECT * FROM android_heap_graph_class_aggregation WHERE obj_count >= 2
    ORDER BY obj_count DESC LIMIT 100

This query returns the top 100 duplicated objects. This can help you find
objects that are instantiated multiple times, which might reveal opportunities
for caching them or identify unintended duplicates.

### Cold startup latency

You can also query for startups. This section provides a more elaborate query to
estimate cold startup time in a trace.

    -- This function finds slices that match the given GLOB $pattern
    CREATE OR REPLACE FUNCTION find_slices(pattern STRING) RETURNS
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

This query generates a slice that represents the time between two slices that
define the startup time: `bindApplication` (typically found at the start of a
cold app launch) and the first `Choreographer#doFrame` slice (the first
generated frame). This metric effectively estimates cold startup TTFF (time to
first frame).