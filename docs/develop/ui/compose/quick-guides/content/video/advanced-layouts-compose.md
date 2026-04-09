---
title: Advanced layouts in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/advanced-layouts-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Advanced layouts in Compose Stay organized with collections Save and categorize content based on your preferences.



See how to build complex designs for your Compose layouts, focusing on layout
phase and constraints, subcompose layouts, and intrinsic measurements.

## Key points

* The *layout phase* is the phase of Compose where element sizing and
  positioning is defined.
* During the layout phase, each element in the UI tree measures its children,
  enabling the parent to decide its own size and placing the children in the
  available 2D space.
* To build a custom layout, call the [`Layout`](/reference/kotlin/androidx/compose/ui/layout/Layout.composable#Layout(kotlin.collections.List,androidx.compose.ui.Modifier,androidx.compose.ui.layout.MultiContentMeasurePolicy)) composable, which
  accepts the composable content as its children.
* Subcomposition enables lazy components to add content on demand while
  scrolling.
* Subcomposed layouts can have an impact on performance. Use this
  approach when at least one child's composition depends on the result of
  another child's measurement.
* Intrinsic measurements let you query children before they're measured.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a
visually pleasing form that's easy for users to consume.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)