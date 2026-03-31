---
title: Bottom sheets  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/bottom-sheets
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Bottom sheets Stay organized with collections Save and categorize content based on your preferences.




![An example of a Material Design 3 modal bottom sheet.](/static/develop/ui/compose/images/layouts/material/m3-bottom-sheet.png)

If you want to implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), you can use the
[`ModalBottomSheet`](/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable) composable.

You can use the `content` slot, which uses a [`ColumnScope`](/reference/kotlin/androidx/compose/foundation/layout/ColumnScope) to layout sheet
content composables in a column:

```
ModalBottomSheet(onDismissRequest = { /* Executed when the sheet is dismissed */ }) {
    // Sheet content
}

MaterialLayoutSnippets.kt
```

## Control sheet state programmatically

To programmatically expand and collapse the sheet, use
[`SheetState`](/reference/kotlin/androidx/compose/material3/SheetState). You can use [`rememberModalBottomSheetState`](/reference/kotlin/androidx/compose/material3/rememberModalBottomSheetState.composable#rememberModalBottomSheetState(kotlin.Boolean,kotlin.Function1)) to create
an instance of `SheetState` that must be passed to `ModalBottomSheet` with
the `sheetState` parameter. `SheetState` provides access to the [`show`](/reference/kotlin/androidx/compose/material3/SheetState#show())
and [`hide`](/reference/kotlin/androidx/compose/material3/SheetState#hide()) functions, as well as properties related to the current sheet
state. These suspending functions require a `CoroutineScope` — for example,
using [`rememberCoroutineScope`](/reference/kotlin/androidx/compose/runtime/rememberCoroutineScope.composable) — and you can call them in response to UI
events. Make sure to remove the `ModalBottomSheet` from composition upon hiding
the bottom sheet.

```
val sheetState = rememberModalBottomSheetState()
val scope = rememberCoroutineScope()
var showBottomSheet by remember { mutableStateOf(false) }
Scaffold(
    floatingActionButton = {
        ExtendedFloatingActionButton(
            text = { Text("Show bottom sheet") },
            icon = { Icon(Icons.Filled.Add, contentDescription = "") },
            onClick = {
                showBottomSheet = true
            }
        )
    }
) { contentPadding ->
    // Screen content

    if (showBottomSheet) {
        ModalBottomSheet(
            onDismissRequest = {
                showBottomSheet = false
            },
            sheetState = sheetState
        ) {
            // Sheet content
            Button(onClick = {
                scope.launch { sheetState.hide() }.invokeOnCompletion {
                    if (!sheetState.isVisible) {
                        showBottomSheet = false
                    }
                }
            }) {
                Text("Hide bottom sheet")
            }
        }
    }
}

MaterialLayoutSnippets.kt
```

![A modal bottom sheet in Jetpack Compose showing content.](/static/develop/ui/compose/images/layouts/material/modal_bottom_sheet.png)