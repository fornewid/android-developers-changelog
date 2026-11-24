---
title: https://developer.android.com/agents/skills/profilers/android-profiler/references/perfetto/sql
url: https://developer.android.com/agents/skills/profilers/android-profiler/references/perfetto/sql
source: md.txt
---

How to get data out of a trace (`.pftrace`, `.perfetto-trace`, `.pb`,
systrace, ftrace text, Chrome JSON) with `trace_processor` and PerfettoSQL.
`trace_processor` must be on the `PATH` (see
`$SKILL_ROOT/references/perfetto/setup.md`).

## 1. Load once, query many

Parsing is the slow part (seconds to minutes for large traces), so load
the trace into a named background session and run every query against it
with `--remote`:

```bash
trace_processor server unix --name mysession --daemonize TRACE_FILE
trace_processor query --remote mysession "SELECT s.ts, s.dur, s.name FROM slice AS s WHERE s.dur > 5e8 LIMIT 5"
trace_processor query --remote mysession -f queries.sql   # long SQL from a file
trace_processor server kill mysession                     # when completely done
```

- Session state persists between calls: a `CREATE PERFETTO TABLE` or `INCLUDE PERFETTO MODULE` done once is available in the next call.
- Several `;`-separated statements per call are fine. Each result set is printed, separated by a blank line: CSV by default, or markdown tables when `trace_processor` detects a coding agent (`--format csv` forces CSV).
- Trace-loading flags (`--full-sort`, `--add-sql-package`, ...) go on the `server unix` invocation, not on `query --remote`.
- `TRACE_FILE` may be a local path, an `http(s)://` URL or a Perfetto UI share link; gzipped traces load directly.
- Idle sessions are reaped after 30 minutes; kill yours when done.
- `trace_processor query TRACE_FILE "..."` without a session re-parses on every call. Use it only for a single quick question.
- A session is shared by every client that names it: tables created in it and `server kill` affect them all. Pick a unique name (for example, derived from the trace file), and never reuse or kill another agent's session.
- `--daemonize` is POSIX-only. On Windows, omit it and run the `server unix` command as a background process; `query --remote` and `server kill` work unchanged.

## 2. Discover, don't guess

Never guess column names: check the columns of every table, view or query
you use with `SELECT * FROM ... LIMIT 0` before you write the query.

```sql
-- Exact columns of any table, view or query (no rows scanned):
SELECT * FROM slice LIMIT 0;

-- Search the standard library (tables, views, functions, macros) by keyword:
SELECT o.qualified_name, o.object_type, o.short_description
FROM __intrinsic_stdlib_objects AS o
WHERE o.exposed = 1 AND regexp('startup|launch', o.summary, 'i')
LIMIT 20;

-- Full documentation of one object (arguments, columns, description):
SELECT o.summary FROM __intrinsic_stdlib_objects AS o
WHERE o.qualified_name = 'android.startup.startups.android_startups';

-- Then load its module and use it:
INCLUDE PERFETTO MODULE android.startup.startups;
SELECT s.package, s.startup_type, s.dur / 1e6 AS ms FROM android_startups AS s;
```

The standard library has ready-made tables for most common questions, and
its views already join threads and processes onto events. Prefer it over
hand-written joins on raw tables. If a query fails with "no such table",
newer `trace_processor` builds name the module to `INCLUDE` in the error;
otherwise search for the name as above. (`__intrinsic_stdlib_objects` is
an implementation detail: fine to use interactively, do not bake it into
committed scripts.)

Raw tables worth knowing: `slice` (anything with a duration), `thread`,
`process`, `thread_state` (Running / Runnable / Sleeping per thread),
`sched` (on-CPU intervals per CPU), `counter`, `track`, `args`.

Modules that answer most questions:

| Question | Module (`INCLUDE PERFETTO MODULE ...`) | Main table |
|---|---|---|
| Slices with thread/process names | `slices.with_context` | `thread_slice`, `process_slice`, `thread_or_process_slice` |
| CPU time per thread/process | `sched.with_context` | `sched_with_thread_process` |
| CPU time inside each slice | `slices.cpu_time` | `thread_slice_cpu_time` |
| App startups and their phases | `android.startup.startups`, `android.startup.startup_breakdowns` | `android_startups`, `android_startup_opinionated_breakdown` |
| Frames and jank | `android.frames.timeline` | `android_frames` |
| ANRs | `android.anrs` | `android_anrs` |
| Binder transactions | `android.binder` | `android_binder_txns`, `android_binder_metrics_by_process` |
| Process importance (foreground, background, cached) | `android.oom_adjuster` | `android_oom_adj_intervals` |
| Low-memory kills, process RSS | `android.memory.lmk`, `linux.memory.process` | `android_lmk_events`, `memory_rss_and_swap_per_process` |
| CPU frequency, clusters | `linux.cpu.frequency`, `android.cpu.cluster_type` | `cpu_frequency_counters`, `android_cpu_cluster_mapping` |
| Java heap retained sizes | `android.memory.heap_graph.dominator_tree` | `heap_graph_dominator_tree` |
| CPU sampling stacks | `stacks.cpu_profiling` | `cpu_profiling_samples` |
| Interval overlap / intersection | `intervals.intersect`, `intervals.overlap` | `_interval_intersect!`, `interval_merge_overlapping!`, `intervals_overlap_count!` |

Static references: <https://perfetto.dev/docs/analysis/stdlib-docs>,
<https://perfetto.dev/docs/analysis/sql-tables>.

## 3. PerfettoSQL rules of thumb

- Join on `utid` / `upid` (unique for the trace), not `tid` / `pid` (the OS recycles them). Ids like `id`, `utid`, `track_id` are fine as join keys but unstable across runs: report names (`thread.name`, `process.name`, `slice.name`) to the user.
- Qualify every column: give every table, view, CTE and subquery an alias, and write every column as `{alias}.{column}`, including inside subqueries and `ON`, `WHERE` and `IN(...)` clauses. SQLite resolves an unqualified column that a subquery's own tables lack to a same-named column of the outer query, without an error; qualified names fail fast with `no such column` instead of returning wrong rows.
- `dur = -1` means the slice was still open at trace end; `dur = 0` is an instant. When summing or bounding, use `IIF(dur = -1, trace_end() - ts, dur)`.
- Match strings with `=`, `GLOB '*Render*'` or `regexp('render', name, 'i')`, not `LIKE` (slow, and `_` is a wildcard).
- Aggregate (`COUNT`, `SUM`, `GROUP BY`, `LIMIT`) instead of dumping raw rows; a trace can have millions.
- Make statements re-runnable: `CREATE OR REPLACE PERFETTO TABLE|VIEW|FUNCTION|MACRO`. Virtual tables (`SPAN_JOIN`) do not support it: `DROP TABLE IF EXISTS x;` first.
- Materialise expensive intermediates with `CREATE PERFETTO TABLE`.
- For interval intersection prefer the `intervals.*` modules or `SPAN_JOIN`. `SPAN_JOIN` needs integer `PARTITIONED` columns, and overlapping spans within a partition silently produce wrong rows. Nested slices overlap even within one `track_id`: use `depth = 0` only, or flatten them first with `interval_merge_overlapping_partitioned!` (`intervals.overlap`). Only fall back to manual arithmetic (`overlap iff start1 < end2 AND start2 < end1`, `dur = MIN(end1, end2) - MAX(start1, start2)`) when neither applies.
- Event properties: `EXTRACT_ARG(arg_set_id, 'key')` rather than joining `args` by hand.
- Slow query? On `slice`, `counter`, `sched` and `thread_state`, `id` and `ts` are sorted, and `slice.track_id`, `slice.parent_id` and `sched.utid` are indexed; filters on other columns of these tables scan.
- Per-row `CREATE PERFETTO FUNCTION` calls are expensive; prefer plain SQL, CTEs and stdlib views.

## 4. Working loop

1. State the question and which tables/modules should answer it; search the stdlib before writing custom joins.
2. Check the schema (`LIMIT 0`) of every table you will use, then draft the query and run it against the session.
3. On an error, read the hint in the message, fix the query and re-run. Do not water down the question to make a query pass (for example, replacing an intersection with two independent totals).
4. Present the validated SQL alongside the result and explain what the numbers mean. Distinguish what the trace shows from what you infer.

## More

- Language tour: <https://perfetto.dev/docs/analysis/perfetto-sql-getting-started>
- Trace processor reference: <https://perfetto.dev/docs/analysis/trace-processor>