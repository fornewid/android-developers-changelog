---
title: Partial bottom sheet  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/bottom-sheets-partial
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Partial bottom sheet Stay organized with collections Save and categorize content based on your preferences.




You can partially show a [bottom sheet](/develop/ui/compose/components/bottom-sheets) and then let the user either make it
full screen or dismiss it.

To do so, pass your [`ModalBottomSheet`](/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable) an instance of [`SheetState`](/reference/kotlin/androidx/compose/material3/SheetState)
with `skipPartiallyExpanded` set to `false`.

**Note:** `ModalBottomSheet` is experimental. File any issues on the [issue
tracker](https://issuetracker.google.com/issues/new?component=856989&template=1425922).

## Example

This example demonstrates how you can use the `sheetState` property of
`ModalBottomSheet` to display the sheet only partially at first:

```
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

BottomSheet.kt
```

### Key points about the code

In this example, note the following:

* `showBottomSheet` controls whether the app displays the bottom sheet.
* `sheetState` is an instance of [`SheetState`](/reference/kotlin/androidx/compose/material3/SheetState) where
  `skipPartiallyExpanded` is false.
* [`ModalBottomSheet`](/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable) takes a modifier that ensures it fills the screen
  when fully expanded.
* `ModalBottomSheet` takes `sheetState` as the value for its `sheetState`
  parameter.
  + As a result, the sheet only partially displays when first opened. The
    user can then drag or swipe it to make it full screen or dismiss it.
* The `onDismissRequest` lambda controls what happens when the user tries to
  dismiss the bottom sheet. In this case, it only removes the sheet.

### Results

When the user first presses the button, the sheet displays partially:

![A bottom sheet that initially only fills part of the screen. The user can swipe to fill the screen with it, or dismiss it](/static/develop/ui/compose/images/components/bottom-sheet-partial.png)


**Figure 1.** Partially displayed bottom sheet.

If the user swipes up on the sheet, it fills the screen:

![A bottom sheet that the user has expanded to fill the screen.](/static/develop/ui/compose/images/components/bottom-sheet-fullscreen.png)


**Figure 2.** Full-screen bottom sheet.

**Note:** If you set `skipPartiallyExpanded` to true, the sheet opens immediately to
full screen.

## Additional resources

* [Bottom sheets](/develop/ui/compose/components/bottom-sheets)