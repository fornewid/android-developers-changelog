---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-bottom-sheet
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-bottom-sheet
source: md.txt
---

<br />

A bottom sheet shows secondary content, anchored to the bottom of the screen.

## Results

![](https://developer.android.com/static/develop/ui/compose/images/layouts/material/m3-bottom-sheet.png)
**Figure 1.** A standard bottom sheet (left) and a modal bottom sheet (right).

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_2519fd3fbb696c8d700357eb8e799d84d0caaa5d9a7dd3ddcb421fcba3615386.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a bottom sheet

To implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), use the [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable)
composable:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_ff93f255856d962265ac6052f686a21397955d08af2ac9678a8f8c5c9af4be01.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Expand and collapse the sheet

To expand and collapse the sheet, use [`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_ba9c6b4932148827a5cc61a891aeff0eb29ab2ee69a89cd85db4e0ae23a790a9.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points

- Use the `content` slot, which uses a [`ColumnScope`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/ColumnScope) to lay out sheet content composables in a column.
- Use [`rememberSheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#rememberSheetState(kotlin.Boolean,kotlin.Function1)) to create an instance of `SheetState` that you pass to `ModalBottomSheet` with the `sheetState` parameter.
- `SheetState` provides access to the [`show`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState#show()) and [`hide`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState#hide()) functions
  and to properties related to the current sheet state. These functions
  require a `CoroutineScope` --- for example, [`rememberCoroutineScope`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope) ---
  and can be called in response to UI events.

- Make sure to remove the `ModalBottomSheet` from composition when you hide
  the bottom sheet.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)