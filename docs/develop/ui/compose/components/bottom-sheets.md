---
title: https://developer.android.com/develop/ui/compose/components/bottom-sheets
url: https://developer.android.com/develop/ui/compose/components/bottom-sheets
source: md.txt
---

![An example of a Material Design 3 modal bottom sheet.](https://developer.android.com/static/develop/ui/compose/images/layouts/material/m3-bottom-sheet.png)

If you want to implement a [bottom sheet](https://m3.material.io/components/bottom-sheets/overview), you can use the
[`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.ModalBottomSheetProperties,kotlin.Function1)) composable.

You can use the `content` slot, which uses a [`ColumnScope`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/ColumnScope) to layout sheet
content composables in a column:


```kotlin
ModalBottomSheet(onDismissRequest = { /* Executed when the sheet is dismissed */ }) {
    // Sheet content
}
```

<br />

## Control sheet state programmatically

To programmatically expand and collapse the sheet, use
[`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState). You can use [`rememberModalBottomSheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#rememberModalBottomSheetState(kotlin.Boolean,kotlin.Function1)) to create
an instance of `SheetState` that must be passed to `ModalBottomSheet` with
the `sheetState` parameter. `SheetState` provides access to the [`show`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState#show())
and [`hide`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState#hide()) functions, as well as properties related to the current sheet
state. These suspending functions require a `CoroutineScope` --- for example,
using [`rememberCoroutineScope`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope) --- and you can call them in response to UI
events. Make sure to remove the `ModalBottomSheet` from composition upon hiding
the bottom sheet.


```kotlin
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
```

<br />

![A modal bottom sheet in Jetpack Compose showing content.](https://developer.android.com/static/develop/ui/compose/images/layouts/material/modal_bottom_sheet.png)