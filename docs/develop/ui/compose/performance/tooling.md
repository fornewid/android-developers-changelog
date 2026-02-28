---
title: https://developer.android.com/develop/ui/compose/performance/tooling
url: https://developer.android.com/develop/ui/compose/performance/tooling
source: md.txt
---

It can be hard to know where a performance issue lies and what code to start
optimizing. Start by using tools to help narrow down where your issue is.

## Layout Inspector

Use the [Layout Inspector](https://developer.android.com/develop/ui/compose/tooling/debug#layout_inspector) to inspect your layout and see recomposition
counts.

If your UI has poor performance, this is often because of a coding error that
forces your UI to be recomposed excessively. On the other hand, some coding
errors can prevent your UI from being recomposed when it needs to be, which
means UI changes aren't showing up on the screen. Tracking recompositions can
help find both of these kinds of problems.

Recomposition in itself is not bad; however, unexpected recomposition can be an
issue.

For more information, see the Layout Inspector [recomposition counts](https://developer.android.com/develop/ui/compose/tooling/debug#recomposition-counts)
documentation.

## Composition tracing

Use [composition tracing](https://developer.android.com/develop/ui/compose/tooling/tracing) to trace your composable functions in a system
trace. Traces are often the best source of information when first looking into a
performance issue. They allow you to form a hypothesis of what the issue is and
where to start looking.

## Additional Resources

- **[App performance guide](https://developer.android.com/topic/performance/overview)**: Discover best practices, libraries, and tools to improve performance on Android.
- **[Inspect Performance](https://developer.android.com/topic/performance/inspecting-overview):** Inspect app performance.
- **[Benchmarking](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview):** Benchmark app performance.
- **[App startup](https://developer.android.com/topic/performance/appstartup/analysis-optimization):** Optimize app startup.
- **[Baseline profiles](https://developer.android.com/baseline-profiles):** Understand baseline profiles.