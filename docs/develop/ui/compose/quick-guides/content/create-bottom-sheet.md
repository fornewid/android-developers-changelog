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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a bottom sheet

To implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), use the [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ModalBottomSheetProperties,kotlin.Function1))
composable:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_2f061b9d033015d5186dcf1939411220e6848eb00aa9bd8e50e8782dab7ea959.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Expand and collapse the sheet

To expand and collapse the sheet, use [`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-bottom-sheet_b6b4cbd60237f7b6c23783d6b52ad193b92f525a7724d590127cfa3041939f11.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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