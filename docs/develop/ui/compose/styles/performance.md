---
title: Performance benefits with Styles  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/styles/performance
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Performance benefits with Styles Stay organized with collections Save and categorize content based on your preferences.




By design, Styles operate in the layout and drawing phase of Compose. This
avoids the need to create lambda-based modifiers as Styles always skips the
composition phase.

![Phases of Compose and where Styles
run](/static/develop/ui/compose/styles/images/phases_compose_styles_skips.png)


**Figure 1.** Phases of Compose and where Styles run.

The performance improvements over modifiers come from three primary
optimizations:

* **Phase shifting**: Styles often target the Draw phase. When a value
  changes, Compose invalidates only the affected phase (e.g., Redraw) instead
  of triggering a full Recomposition or Relayout.
* **Lazy allocation**: Styles defer animation resource allocation until an
  animation actually starts. This reduces the work required during initial
  composition.
* **Reduced object overhead**: Chained modifiers allocate an object for every
  property (e.g., padding, border). Styles use a single lambda to apply
  multiple properties, significantly reducing memory allocations. If a Style
  is defined in a theme, that lambda is shared across all components using
  that theme.

The following table shows illustrative results of an internal [performance
benchmarks](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt) for Compose 1.11.0-alpha06 of Styles, in comparison
to an implementation in Compose without Styles.

The
`basic_box_border_change` test highlights the style system's strength in
avoiding the allocation of multiple modifier objects during property updates,
resulting in a massive ~77% reduction in allocations, and ~59% reduction in
time.

|  |  |  |  |
| --- | --- | --- | --- |
| **Test Method** | **Description** | **Time Change** | **Allocation Change** |
| [basic\_box\_border\_change](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt;l=103) | Toggles the border color of a `Box` to measure update performance. | -59.91% | -77.22% |
| [input\_state\_basic\_box](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt;l=119) | Compares style-based hover/focus/press states vs. manual interaction state collection. | -5.24% | -14.72% |
| [basic\_box](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt;l=114) | Measures initial composition and layout of a `Box` with five chained modifiers. | -4.78% | -6.60% |
| [basic\_text](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt;l=124) | Renders five `BasicText` components with hardcoded strings. | +0.62% | +2.41% |
| [basic\_text\_provided\_color](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/benchmark/src/androidTest/java/androidx/compose/foundation/benchmark/StyleBenchmark.kt;l=129) | Compares setting text color via a style vs. using `CompositionLocalProvider`. | +5.86% | +9.82% |