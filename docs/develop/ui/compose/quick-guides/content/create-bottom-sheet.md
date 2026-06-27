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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_90b94f6fc49da5d289b5455639aac6e3fffc24699727c9148b981cb0dd1fe670.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a bottom sheet

To implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), use the [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable)
composable:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_afe9265af7da129f6092e2517134f9220cffe0a8ea56993956b4e50f012c0805.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Expand and collapse the sheet

To expand and collapse the sheet, use [`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_a166ede9c8a3a55b458df78aad0ec9ea00ac7b2eded854648d0fe77055303857.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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