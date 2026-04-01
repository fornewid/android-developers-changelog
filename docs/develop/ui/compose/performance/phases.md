---
title: https://developer.android.com/develop/ui/compose/performance/phases
url: https://developer.android.com/develop/ui/compose/performance/phases
source: md.txt
---

When Compose updates a frame, it goes through three phases:

- **Composition:** Compose determines *what* to show. It runs composable functions and builds the UI tree.
- **Layout:** Compose determines the size and placement of each element in the UI tree.
- **Drawing:** Compose actually *renders* the individual UI elements.

Compose can intelligently skip any of those phases if they aren't needed. For
example, suppose a single graphic element swaps between two icons of the same
size. Since this element isn't changing size, and no elements of the UI tree are
being added or removed, Compose can skip over the composition and layout phases
and redraw this one element.

However, coding mistakes can make it hard for Compose to know which phases it
can safely skip, in which case Compose runs all three phases, which can slow
down your UI. So, many of the performance best practices are to help Compose
skip the phases it doesn't need to do.

For more information, see the [Jetpack Compose Phases](https://developer.android.com/develop/ui/compose/phases) guide.

## General principles

There are a couple of broad principles to follow that can improve performance in
general:

- **Whenever possible, move calculations out of your composable functions.** Composable functions might need to be rerun whenever the UI changes. Any code you put in the composable gets re-executed, potentially for every frame of an animation. Limit the composable's code to only what it needs to build the UI.
- **Defer state reads for as long as possible.** By moving state reading to a child composable or a later phase, you can minimize recomposition or skip the composition phase entirely. You can do this by passing lambda functions instead of the state value for frequently changing state and by preferring lambda-based modifiers when you pass in frequently changing state. You can see an example of this technique in the [Defer reads as long as possible](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads) section of [Follow best practices](https://developer.android.com/develop/ui/compose/performance/bestpractices).

## Additional Resources

- **[App performance guide](https://developer.android.com/topic/performance/overview)**: Discover best practices, libraries, and tools to improve performance on Android.
- **[Inspect Performance](https://developer.android.com/topic/performance/inspecting-overview):** Inspect app performance.
- **[Benchmarking](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview):** Benchmark app performance.
- **[App startup](https://developer.android.com/topic/performance/appstartup/analysis-optimization):** Optimize app startup.
- **[Baseline profiles](https://developer.android.com/baseline-profiles):** Understand baseline profiles.