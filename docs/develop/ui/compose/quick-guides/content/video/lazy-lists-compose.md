---
title: Lazy lists in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/lazy-lists-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Lazy lists in Compose Stay organized with collections Save and categorize content based on your preferences.



Compose gives you a simpler and more performant way to create scrolling lists,
using fewer lines of code than [`RecyclerView`](/reference/androidx/recyclerview/widget/RecyclerView). Learn how to use lazy
layouts to create lists that let you add content to lists, on demand.

## Key points

* Use lazy layouts to add content on demand for a significant number of items
  or large datasets, increasing your app's performance and responsiveness.
* This approach lets you focus on describing your item content while lazy
  lists handle everything else.
* You can describe one item using the [`item()`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#item(kotlin.Any,kotlin.Any,kotlin.Function1)) block or multiple items
  with the [`items()`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) block.
* [`LazyListState`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListState) is an important state object that stores the scroll
  position and contains useful information on your list.

## Resources

* [Codelab: Basic layouts in Compose](/codelabs/jetpack-compose-layouts#0)

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