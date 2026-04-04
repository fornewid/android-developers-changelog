---
title: Jetpack Compose Performance  |  Android Developers
url: https://developer.android.com/develop/ui/compose/performance
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Jetpack Compose Performance Stay organized with collections Save and categorize content based on your preferences.




Jetpack Compose delivers excellent performance out of the box. Configure your
app using best practices to avoid common pitfalls and optimize your Compose
application's performance.

## Key concepts

These are some of the key concepts for performance in Compose:

* **[Phases](/develop/ui/compose/performance/phases):** Understanding the composition, layout, and drawing phases
  is crucial for optimizing how Compose updates your UI.
* **[Baseline Profiles](/develop/ui/compose/performance/baseline-profiles):** These profiles precompile essential code,
  leading to faster app launches and smoother interactions.
* **[Stability](/develop/ui/compose/performance/stability):** Increase the stability of your app to more efficiently
  skip unnecessary recompositions, improving performance.

## Properly configure your app

If your app is performing poorly, there might be a configuration problem. A good
first step is to check the following configuration options:

* **Build in Release Mode with R8:** Try running your app in [release
  mode](/studio/run#changing-variant). Debug mode is useful for spotting many problems, but it imposes a
  performance cost and can make it hard to spot other issues. You should also
  [enable optimizing and shrinking](/build/shrink-code#enable) with the R8 compiler to ensure a
  performant and efficient release build.
* **Use Baseline Profiles:** Baseline Profiles improve performance by
  precompiling code for critical user journeys. Compose includes a default
  profile, but ideally, you should create an app-specific one as well. [Learn
  more about Baseline Profiles in the general Android performance docs](/topic/performance/baselineprofiles/overview)

## Tools

Familiarize yourself with the suite of [tools](/develop/ui/compose/performance/tooling) available to help you measure
and analyze your Compose app's performance.

## Best Practices

When developing your app with Compose, keep these best practices in mind:

* **[Avoid expensive calculations](/develop/ui/compose/performance/bestpractices#use-remember):** Use `remember` to cache the results
  of expensive calculations.
* **[Help lazy layouts](/develop/ui/compose/performance/bestpractices#use-lazylist-keys):** Provide stable keys to lazy layouts using the
  `key` parameter to minimize unnecessary recompositions.
* **[Limit unnecessary recompositions](/develop/ui/compose/performance/bestpractices#use-derivedstateof):** Use `derivedStateOf` to limit
  recompositions when rapidly changing state.
* **[Defer state reads](/develop/ui/compose/performance/bestpractices#defer-reads):** Defer state reads as long as possible by
  wrapping them in lambda functions.
* **[Use lambda modifiers for changing state](/develop/ui/compose/performance/bestpractices#defer-reads):** Use lambda-based
  modifiers like `Modifier.offset { ... }` for frequently changing state
  variables.
* **[Avoid backwards writes](/develop/ui/compose/performance/bestpractices#avoid-backwards):** Never write to state that has already been
  read in a composable.

For more details, see the [best practices](/develop/ui/compose/performance/bestpractices) guide.

## Views

If you are working with views instead of Compose, see the dedicated [Improve
layout performance](/develop/ui/views/layout/improving-layouts) guide.

## Additional Resources

* **[App performance guide](/topic/performance/overview)**: Discover best
  practices, libraries, and tools to improve performance on Android.
* **[Inspect Performance](/topic/performance/inspecting-overview):**
  Inspect app performance.
* **[Benchmarking](/topic/performance/benchmarking/benchmarking-overview):**
  Benchmark app performance.
* **[App startup](/topic/performance/appstartup/analysis-optimization):**
  Optimize app startup.
* **[Baseline profiles](/baseline-profiles):** Understand baseline profiles.