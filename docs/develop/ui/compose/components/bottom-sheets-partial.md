---
title: https://developer.android.com/develop/ui/compose/components/bottom-sheets-partial
url: https://developer.android.com/develop/ui/compose/components/bottom-sheets-partial
source: md.txt
---

You can partially show a [bottom sheet](https://developer.android.com/develop/ui/compose/components/bottom-sheets.md.txt) and then let the user either make it
full screen or dismiss it.

To do so, pass your [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable.md.txt) an instance of [`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState.md.txt)
with `skipPartiallyExpanded` set to `false`.

> [!NOTE]
> **Note:** `ModalBottomSheet` is experimental. File any issues on the [issue
> tracker](https://issuetracker.google.com/issues/new?component=856989&template=1425922).

## Example

This example demonstrates how you can use the `sheetState` property of
`ModalBottomSheet` to display the sheet only partially at first:


```kotlin
@Composable
fun PartialBottomSheet() {
    var showBottomSheet by remember { mutableStateOf(false) }
    val sheetState = rememberModalBottomSheetState(
        skipPartiallyExpanded = false,
    )

    Column(
        modifier = Modifier.fillMaxWidth(),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Button(
            onClick = { showBottomSheet = true }
        ) {
            Text("Display partial bottom sheet")
        }

        if (showBottomSheet) {
            ModalBottomSheet(
                modifier = Modifier.fillMaxHeight(),
                sheetState = sheetState,
                onDismissRequest = { showBottomSheet = false }
            ) {
                Text(
                    "Swipe up to open sheet. Swipe down to dismiss.",
                    modifier = Modifier.padding(16.dp)
                )
            }
        }
    }
}
```

<br />

### Key points about the code

In this example, note the following:

- `showBottomSheet` controls whether the app displays the bottom sheet.
- `sheetState` is an instance of [`SheetState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SheetState.md.txt) where `skipPartiallyExpanded` is false.
- [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable.md.txt) takes a modifier that ensures it fills the screen when fully expanded.
- `ModalBottomSheet` takes `sheetState` as the value for its `sheetState` parameter.
  - As a result, the sheet only partially displays when first opened. The user can then drag or swipe it to make it full screen or dismiss it.
- The `onDismissRequest` lambda controls what happens when the user tries to dismiss the bottom sheet. In this case, it only removes the sheet.

### Results

When the user first presses the button, the sheet displays partially:
![A modal bottom sheet partially expanded over the lower half of the screen, with a drag handle and the text 'Swipe up to open sheet. Swipe down to dismiss.', below a dimmed 'Display partial bottom sheet' button.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_partialbottomsheet.png) **Figure 1.** Partially displayed bottom sheet.

> [!NOTE]
> **Note:** If you set `skipPartiallyExpanded` to true, the sheet opens immediately to full screen.

## Additional resources

- [Bottom sheets](https://developer.android.com/develop/ui/compose/components/bottom-sheets.md.txt)