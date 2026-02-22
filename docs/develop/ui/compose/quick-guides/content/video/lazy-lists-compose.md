---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/video/lazy-lists-compose
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/lazy-lists-compose
source: md.txt
---

<br />

Compose gives you a simpler and more performant way to create scrolling lists,
using fewer lines of code than [`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). Learn how to use lazy
layouts to create lists that let you add content to lists, on demand.  

## Key points

- Use lazy layouts to add content on demand for a significant number of items or large datasets, increasing your app's performance and responsiveness.
- This approach lets you focus on describing your item content while lazy lists handle everything else.
- You can describe one item using the [`item()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#item(kotlin.Any,kotlin.Any,kotlin.Function1)) block or multiple items with the [`items()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) block.
- [`LazyListState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState) is an important state object that stores the scroll position and contains useful information on your list.

## Resources

- [Codelab: Basic layouts in Compose](https://developer.android.com/codelabs/jetpack-compose-layouts#0)

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)