---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai
url: https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai
source: md.txt
---

Because [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) profiles use the standard Perfetto format and
can be [queried with PerfettoSQL](https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles), you can pair an AI coding agent with the
[Perfetto AI skill](https://perfetto.dev/docs/getting-started/using-ai) to automate root-cause analysis directly in your
workspace instead of manually navigating timelines in the [Perfetto UI](https://ui.perfetto.dev/)
or writing custom queries against the [Perfetto Standard Library](https://perfetto.dev/docs/analysis/stdlib-docs):

1. **Load the profile** : The agent opens the collected profile using Perfetto's `trace_processor`.
2. **Execute diagnostic queries** : Guided by the Perfetto AI skill, the agent queries standard library modules (such as `android.frames.timeline` for jank or `android.memory.heap_graph.dominator_tree` for memory leaks) and iteratively refines its queries.
3. **Correlate with source code**: The agent maps custom trace slices, sampled call stacks, or retaining class names in the profile directly to your Kotlin or Java source files and proposes a fix.

> [!TIP]
> **Tip:** Treat the agent's initial report as the starting point of an interactive investigation. Ask follow-up questions to explore how specific metrics or retention paths relate to your architecture, or prompt the agent to keep querying the profile to uncover secondary bottlenecks and memory inefficiencies beyond the primary issue.

## Set up the Perfetto AI skill

The open source [Perfetto AI skill](https://perfetto.dev/docs/getting-started/using-ai) teaches coding agents how to run
`trace_processor`, write PerfettoSQL, and follow guided workflows for Android
memory and CPU analysis. Each install bundles a `trace_processor` wrapper, so
you don't need to install `trace_processor` separately:

- **Install with AI**: Run the following prompt in any AI coding agent:

      Following instructions from https://perfetto.dev/docs/getting-started/using-ai set up the Perfetto AI skill to be usable by any agent

- **Install manually** : Follow the setup instructions in [Using AI with
  Perfetto](https://perfetto.dev/docs/getting-started/using-ai) for your agent (such as Claude Code, Codex, Cursor,
  Antigravity, or OpenCode).

> [!NOTE]
> **Note:** You can also use the [Android profiler skill](https://developer.android.com/topic/performance/issues/memory-usage#skill-title_android-profiler) (`android skills add android-profiler`), which comes built-in with the [Android CLI](https://developer.android.com/tools/agents/android-cli). Choose the **Android profiler skill** if you use the Android CLI and want an integrated workflow to both record new profiles from a connected device and analyze them. Choose the **Perfetto AI skill** if you already have captured `.perfetto-trace` or `.perfetto-java-heap-dump` files (such as production profiles from `ProfilingManager`) and want a standalone `trace_processor` wrapper with guided PerfettoSQL analysis workflows in any agent.

## Workflow examples

Place one or more captured profiles in your workspace and prompt your AI agent
to investigate. You can analyze a single profile to diagnose an individual issue
or pass multiple profiles to compare patterns and regressions in bulk.

### Analyze Java heap dumps and OOMs

When you provide a Java heap dump captured directly with
[`PROFILING_TYPE_JAVA_HEAP_DUMP`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_JAVA_HEAP_DUMP) or automatically through the
[`TRIGGER_TYPE_OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM) trigger, an AI agent using the Perfetto AI skill can
help you identify:

- **Memory leaks** : Objects, such as destroyed `Activity` or `Fragment` instances, that remain reachable from GC roots when they should have been reclaimed.
- **Heavily duplicated objects**: Classes with an unexpectedly high instance count that collectively consume a large share of the heap.
- **Memory inefficiencies**: Oversized caches, redundant data structures, or single dominator objects retaining a disproportionate amount of memory.

To investigate an `OutOfMemoryError` heap dump and correlate it with your app's
source code, run a prompt like the following:

    Analyze the Perfetto OOM heap dump at </path/to/profile>, which corresponds to
    the codebase located at </path/to/codebase> using the Perfetto AI skill and find
    the root cause of the OutOfMemoryError.

To see a complete example of the report this prompt generates, including the
dominator tree retention path, source-code root cause, and proposed fix, see
[Automate the OOM investigation with an AI agent](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-oom-example#analyze-with-ai) in [Case study: Debug an
OOM crash](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-oom-example).

### Analyze system traces and ANRs

When you provide a system trace captured directly with
[`PROFILING_TYPE_SYSTEM_TRACE`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_SYSTEM_TRACE) or automatically through the
[`TRIGGER_TYPE_ANR`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANR) trigger, an AI agent using the Perfetto AI skill can
help you identify:

- **Blocking main-thread operations**: Long-running trace slices or synchronous calls that prevent the UI thread from processing input events or drawing frames before the ANR threshold.
- **Thread state bottlenecks** : Intervals where the main thread is stuck in `Sleeping` (such as blocking network I/O or `Thread.sleep` timeouts), `Blocked` (lock contention), or `Runnable` (CPU scheduling delays) states.
- **Main-thread CPU spikes**: Expensive computations or tight loops executing directly on the UI thread instead of a background thread.

To investigate an ANR system trace and correlate it with your app's source code,
run a prompt like the following:

    Analyze the Perfetto system trace at </path/to/trace.perfetto-trace>, which
    corresponds to an ANR trace, and find the root cause of the ANR using the
    Perfetto AI skill. The codebase is located at </path/to/codebase>.

To see a complete example of the report this prompt generates, including the
main-thread slice breakdown, `thread_state` interval reconstruction, and
source-code mapping, see [Automate the ANR investigation with an AI agent](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-anr-example#analyze-with-ai)
in [Case study: Debug an ANR](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-anr-example).