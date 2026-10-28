---
title: Tooling  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/performance/tooling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Tooling Stay organized with collections Save and categorize content based on your preferences.





It can be hard to know where a performance issue lies and what code to start
optimizing. Start by using tools to help narrow down where your issue is.

## Layout Inspector

Use the [Layout Inspector](/develop/ui/compose/tooling/debug#layout_inspector) to inspect your layout and see recomposition
counts.

If your UI has poor performance, this is often because of a coding error that
forces your UI to be recomposed excessively. On the other hand, some coding
errors can prevent your UI from being recomposed when it needs to be, which
means UI changes aren't showing up on the screen. Tracking recompositions can
help find both of these kinds of problems.

Recomposition in itself is not bad; however, unexpected recomposition can be an
issue. Keep in mind that recomposition counts aren't a substitute for
benchmarks: skipping a composable has slot table and parameter comparison
overhead, and once composition is scheduled, skipping a single intermediate
composable saves little time compared to deferring rapidly changing state reads
to the Layout or Draw phases. Always verify performance changes using
[composition tracing](/develop/ui/compose/tooling/tracing) and Macrobenchmark.

For more information, see the Layout Inspector [recomposition counts](/develop/ui/compose/tooling/debug#recomposition-counts)
documentation.

## Composition tracing

Use [composition tracing](/develop/ui/compose/tooling/tracing) to trace your composable functions in a system
trace. Traces are often the best source of information when first looking into a
performance issue. They allow you to form a hypothesis of what the issue is and
where to start looking.

## Additional resources

* **[App performance guide](/topic/performance/overview):** Discover best
  practices, libraries, and tools to improve performance on Android.
* **[Inspect Performance](/topic/performance/inspecting-overview):** Inspect app performance.
* **[Benchmarking](/topic/performance/benchmarking/benchmarking-overview):** Benchmark app performance.
* **[App startup](/topic/performance/appstartup/analysis-optimization):** Optimize app startup.
* **[Baseline profiles](/baseline-profiles):** Understand baseline profiles.