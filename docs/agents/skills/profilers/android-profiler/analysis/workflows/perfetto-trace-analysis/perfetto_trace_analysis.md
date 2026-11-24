---
title: https://developer.android.com/agents/skills/profilers/android-profiler/analysis/workflows/perfetto-trace-analysis/perfetto_trace_analysis
url: https://developer.android.com/agents/skills/profilers/android-profiler/analysis/workflows/perfetto-trace-analysis/perfetto_trace_analysis
source: md.txt
---

Analyzes Perfetto traces to find the root cause of performance issues in
user or system Android apps (for example, janks, app startup, memory, or
latency stalls).
keywords:
- perfetto
- trace
- jank
- startup
- latency
- stall
- thread

## - bottleneck

Diagnose Android jank, app startup latency, memory pressure, and thread stalls
from a Perfetto trace.

If the user didn't provide a trace path, URL, or Perfetto UI link, ask for it
before running any commands. Set up `trace_processor` per
`$SKILL_ROOT/references/perfetto/setup.md`, query the trace per
`$SKILL_ROOT/references/perfetto/sql.md`, and apply the diagnosis checks.

## Diagnosis checks

1. **Trace health first:** Before analyzing, check for data loss and memory
   kills, because dropped events leave gaps that hide what happened:

   ```sql
   INCLUDE PERFETTO MODULE android.memory.lmk;
   SELECT
     (SELECT COALESCE(SUM(st.value), 0) FROM stats AS st
      WHERE st.severity IN ('data_loss', 'error')) AS data_loss,
     (SELECT COUNT(*) FROM android_lmk_events) AS lmk_kills;
   ```

   If `data_loss > 0`, inspect `stats` (`value > 0`) and report what was
   dropped. `kswapd` or `kcompactd` activity alone doesn't prove memory
   exhaustion; check `MemAvailable` and report `lmk_kills`. Counter tracks (CPU
   and GPU frequency, memory) record a value only when it changes. On a CPU with
   no frequency track, or before a track's first sample, the value is unknown,
   not nominal. Report it as a data gap instead of assuming.
2. **Blocked threads (`S` and `D`):** For synchronous binder calls, join
   `android_monitor_contention` (`android.monitor_contention`) to
   `android_binder_txns` (`android.binder`) on `binder_reply_id` across all
   calls in the window to find lock contention in the server. For `D`, group by
   `io_wait` and `blocked_function` with prefix `GLOB` (for example,
   `'do_page_fault*'`), because kernel symbols carry compiler suffixes (`NULL`
   if `sched_blocked_reason` wasn't traced). `io_wait = 0` isn't disk I/O (for
   example, `mmap_lock` contention). For either state, the waker is the
   `waker_utid` of the `R` row that starts at the sleep's `ts + dur`. Inspect
   the waker's slices at that time to find what the thread waited for. A
   `Running` row there instead means the wakeup wasn't recorded. With
   `irq_context = 1`, an interrupt woke the thread and `waker_utid` is only the
   thread it interrupted; `NULL` means the trace can't tell.

3. **Runnable (`R` and `R+`):** Runnable time while other CPUs are idle points
   to affinity, cpuset, or scheduling-group limits, not CPU saturation.

4. **Display and GPU (UI, game, or video workloads, even when CPU or `kswapd`
   activity is present):** Query all thread tracks in
   `/system/bin/surfaceflinger` (main, `RenderEngine`, and `GPU completion`).
   Compare composition cycles (`composite *` or `present`, or
   `onMessageInvalidate *` on older Android) against `*drawLayers*` to see how
   often Hardware Composer falls back to GPU composition, and check shader
   compilation and `waiting for GPU completion *`. In those intervals, inspect
   slices at all depths (including `dur = 0` and sub-ms slices, with no minimum
   `dur` filter) to find the layer effects driving the work.

5. **Janky frames:** Count janky frames by `jank_type` (join `android_frames`
   to `actual_frame_timeline_slice` on `actual_frame_timeline_id = id`), not by
   a 16.7 ms duration cutoff. `jank_type` can list several labels, so match
   `GLOB '*App Deadline Missed*'`. Only those frames are late because of the
   app. `Buffer Stuffing` and `Prediction Error` frames aren't.

## Report

Cite the evidence (threads, states, durations, timestamps, and the queries
used). Separate what the trace shows from inferences, and name any data gaps.
For a diagnosis, also give the causal chain, each finding's share of the
symptom, and fixes or follow-up workflows. For example, suggest
`perfetto-trace-recording` when the trace lacks the data.