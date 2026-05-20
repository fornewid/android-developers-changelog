---
title: https://developer.android.com/develop/ui/compose/first
url: https://developer.android.com/develop/ui/compose/first
source: md.txt
---

![](https://developer.android.com/static/develop/ui/compose/images/compose-first.png)

Jetpack Compose is Android's declarative UI toolkit, built for modern user
interfaces, with dynamic data, rich graphics, and
beautiful animations. It's replacing the View toolkit, which has served
Android development well for years, but was not designed for the latest demands
and best practices.

## Why Compose-first

We first announced Jetpack Compose in 2019 and have been adding to its features,
performance, and tooling since then. Jetpack Compose now has
everything you need to build premium, native Android applications.

- **Rich feature set**

  With a powerful library of layouts, input, graphics, animation APIs, and the
  latest Material Design components, Compose empowers you to build anything that
  you can imagine.
- **Highly performant**

  Out of the box, Compose offers native performance, delivering a delightful
  experience to your users.
- **Adaptive**

  Compose offers the easiest way to build adaptive apps that work across the
  range of Android form factors.
- **Productive**

  With powerful tools like Previews and Live Edit and the full expressiveness of
  Kotlin, teams tell us that they move much faster when building with Jetpack
  Compose, reducing the time to market.

[Learn more](https://developer.android.com/develop/ui/compose/adopt) about how Compose can accelerate development.

## What does Compose-first mean?

When building new Android development tools and content, such as Jetpack
libraries, samples, documentation, and training content, we'll design them
with Jetpack Compose users in mind. We understand that adopting a new UI
framework takes some time, so we'll continue to support traditional Views for
some time. We'll also continue supporting [interop APIs](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis) to allow you to
adopt Compose at your own pace.

### Android Views

We now consider the View toolkit (for example, classes in `android.widget`
such as `TextView` and `ListView`) to be in **maintenance mode** --- this means
that it will only receive highly critical fixes. The `android.view` package is
still supported as the plumbing necessary for Compose and other UI toolkits.

### View-based Jetpack libraries

The following View-based libraries are also in **maintenance mode** and will
not receive significant updates beyond critical fixes:

- [`CardView`](https://developer.android.com/jetpack/androidx/releases/cardview)
- [`ConstraintLayout`](https://developer.android.com/jetpack/androidx/releases/constraintlayout)
- [`CoordinatorLayout`](https://developer.android.com/jetpack/androidx/releases/coordinatorlayout)
- [`CustomView`](https://developer.android.com/jetpack/androidx/releases/customview)
- [`Databinding`](https://developer.android.com/jetpack/androidx/releases/databinding)
- [`DragAndDrop`](https://developer.android.com/jetpack/androidx/releases/draganddrop)
- [`DrawerLayout`](https://developer.android.com/jetpack/androidx/releases/drawerlayout)
- [`DynamicAnimation`](https://developer.android.com/jetpack/androidx/releases/dynamicanimation)
- [`Emoji`](https://developer.android.com/jetpack/androidx/releases/emoji)
- [`Fragment`](https://developer.android.com/jetpack/androidx/releases/fragment)
- [`GridLayout`](https://developer.android.com/jetpack/androidx/releases/gridlayout)
- [`Interpolator`](https://developer.android.com/jetpack/androidx/releases/interpolator)
- [`Loader`](https://developer.android.com/jetpack/androidx/releases/loader)
- [`Navigation`](https://developer.android.com/jetpack/androidx/releases/navigation)
- [`PercentLayout`](https://developer.android.com/jetpack/androidx/releases/percentlayout)
- [`Preference`](https://developer.android.com/jetpack/androidx/releases/preference)
- [`RecyclerView`](https://developer.android.com/jetpack/androidx/releases/recyclerview)
- [`SlidingPaneLayout`](https://developer.android.com/jetpack/androidx/releases/slidingpanelayout)
- [`SwipeRefreshLayout`](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout)
- [`Transition`](https://developer.android.com/jetpack/androidx/releases/transition)
- [`VectorDrawable`](https://developer.android.com/jetpack/androidx/releases/vectordrawable)
- [`ViewPager`](https://developer.android.com/jetpack/androidx/releases/viewpager)
- [`ViewPager2`](https://developer.android.com/jetpack/androidx/releases/viewpager2)
- [Material Design Components (Views)](https://m3.material.io/develop/android/mdc-android)

### Tools

Any new Android Studio UI tools will be built for Jetpack Compose only. Existing
tools (such as the Navigation Editor and Layout Editor) are now in
**maintenance mode** and will not receive new features.

### Guidance

Documentation, codelabs, and samples will focus on building UI with Jetpack
Compose. You can still find Views-specific documentation linked from pages that
contain generic and Compose information, where relevant.

We're currently updating all relevant documentation across
[developer.android.com](http://developer.android.com) to be Compose-first.

## Happy Composing

Follow the [quick start guide](https://developer.android.com/develop/ui/compose/setup) to add Jetpack Compose to your applications,
[migrate](https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose) your apps to Compose using our Android [migration skill on
GitHub](https://github.com/android/skills), and, finally, take a look at our [sample apps on
GitHub](https://github.com/android/compose-samples) to see Compose in action.