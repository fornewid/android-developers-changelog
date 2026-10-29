---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-dialog
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A [`SpatialDialog`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/SpatialDialog.composable) is a [spatialized component](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components) that appears on top of
the content at the base elevation level.

### Show a spatial dialog

The following example shows a spatial dialog that opens after a short delay.
When `SpatialDialog` is used, the dialog appears at the same z-depth as the
spatial panel, and the panel is pushed back by 125dp when spatialization is
enabled. `SpatialDialog` can also be used when spatialization isn't enabled, in
which case `SpatialDialog` falls back to its 2D counterpart, [`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/Dialog.composable).


```kotlin
@Composable
fun DelayedDialog() {
    var showDialog by remember { mutableStateOf(false) }
    LaunchedEffect(Unit) {
        delay(3000.milliseconds)
        showDialog = true
    }
    if (showDialog) {
        SpatialDialog(
            onDismissRequest = { showDialog = false },
            SpatialDialogProperties(
                dismissOnBackPress = true
            )
        ) {
            Box(
                Modifier
                    .height(150.dp)
                    .width(150.dp)
            ) {
                Button(onClick = { showDialog = false }) {
                    Text("OK")
                }
            }
        }
    }
}
```

<br />

### Key points about the code

- This is an example of [`SpatialDialog`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/SpatialDialog.composable), but using [`SpatialPopup`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/SpatialPopup.composable) and [`SpatialElevation`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/SpatialElevation.composable) is very similar. For more information, see our [API reference](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary).