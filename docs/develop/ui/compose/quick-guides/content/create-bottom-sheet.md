---
title: Create a bottom sheet  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-bottom-sheet
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a bottom sheet Stay organized with collections Save and categorize content based on your preferences.




A bottom sheet shows secondary content, anchored to the bottom of the screen.

## Results

![](/static/develop/ui/compose/images/layouts/material/m3-bottom-sheet.png)


**Figure 1.** A standard bottom sheet (left) and a modal bottom sheet (right).

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Implement a bottom sheet

To implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), use the [`ModalBottomSheet`](/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable)
composable:

## Expand and collapse the sheet

To expand and collapse the sheet, use [`SheetState`](/reference/kotlin/androidx/compose/material3/SheetState):

### Key points

* Use the `content` slot, which uses a [`ColumnScope`](/reference/kotlin/androidx/compose/foundation/layout/ColumnScope) to lay out sheet
  content composables in a column.
* Use [`rememberSheetState`](/reference/kotlin/androidx/compose/material3/package-summary#rememberSheetState(kotlin.Boolean,kotlin.Function1)) to create an instance of `SheetState` that you
  pass to `ModalBottomSheet` with the `sheetState` parameter.
* `SheetState` provides access to the [`show`](/reference/kotlin/androidx/compose/material3/SheetState#show()) and [`hide`](/reference/kotlin/androidx/compose/material3/SheetState#hide()) functions
  and to properties related to the current sheet state. These functions
  require a `CoroutineScope` — for example, [`rememberCoroutineScope`](/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope) —
  and can be called in response to UI events.
* Make sure to remove the `ModalBottomSheet` from composition when you hide
  the bottom sheet.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)