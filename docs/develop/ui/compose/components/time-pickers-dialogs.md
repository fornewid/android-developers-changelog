---
title: https://developer.android.com/develop/ui/compose/components/time-pickers-dialogs
url: https://developer.android.com/develop/ui/compose/components/time-pickers-dialogs
source: md.txt
---

[Time pickers](https://developer.android.com/develop/ui/compose/components/time-pickers) often appear in dialogs. You can use a relatively generic and
minimal implementation of a dialog, or you can implement a custom dialog with
more flexibility.

For more information on dialogs in general, including how to use the time picker
state, see the [Time pickers guide](https://developer.android.com/develop/ui/compose/components/time-pickers).

## Basic example

The most straightforward way to create a dialog for your time picker is to
create a composable that implements [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AlertDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.window.DialogProperties)). The following snippet
provides an example of a relatively minimal dialog using this approach:


```kotlin
@Composable
fun DialWithDialogExample(
    onConfirm: (TimePickerState) -> Unit,
    onDismiss: () -> Unit,
) {
    val currentTime = Calendar.getInstance()

    val timePickerState = rememberTimePickerState(
        initialHour = currentTime.get(Calendar.HOUR_OF_DAY),
        initialMinute = currentTime.get(Calendar.MINUTE),
        is24Hour = true,
    )

    TimePickerDialog(
        onDismiss = { onDismiss() },
        onConfirm = { onConfirm(timePickerState) }
    ) {
        TimePicker(
            state = timePickerState,
        )
    }
}

@Composable
fun TimePickerDialog(
    onDismiss: () -> Unit,
    onConfirm: () -> Unit,
    content: @Composable () -> Unit
) {
    AlertDialog(
        onDismissRequest = onDismiss,
        dismissButton = {
            TextButton(onClick = { onDismiss() }) {
                Text("Dismiss")
            }
        },
        confirmButton = {
            TextButton(onClick = { onConfirm() }) {
                Text("OK")
            }
        },
        text = { content() }
    )
}
```

<br />

Note the key points in this snippet:

1. The `DialWithDialogExample` composable wraps [`TimePicker`](https://developer.android.com/develop/ui/compose/components/time-pickers) in a dialog.
2. `TimePickerDialog` is a custom composable that creates an `AlertDialog` with the following parameters:
   - `onDismiss`: A function called when the user dismisses the dialog (via the dismiss button or navigation back).
   - `onConfirm`: A function called when the user clicks the "OK" button.
   - `content`: A composable that displays the time picker within the dialog.
3. The `AlertDialog` includes:
   - A dismiss button labeled "Dismiss".
   - A confirm button labeled "OK".
   - The time picker content passed as the `text` parameter.
4. The `DialWithDialogExample` initializes the `TimePickerState` with the current time and passes it to both the `TimePicker` and the `onConfirm` function.

![A time picker in an AlertDialog that implements a title, a mode toggle, and dismiss and confirm buttons.](https://developer.android.com/static/develop/ui/compose/images/components/timepicker-basic.png) **Figure 1.** A time picker in an AlertDialog.

## Advanced example

This snippet demonstrates an advanced implementation of a customizable time
picker dialog in Jetpack Compose.


```kotlin
@Composable
fun AdvancedTimePickerExample(
    onConfirm: (TimePickerState) -> Unit,
    onDismiss: () -> Unit,
) {

    val currentTime = Calendar.getInstance()

    val timePickerState = rememberTimePickerState(
        initialHour = currentTime.get(Calendar.HOUR_OF_DAY),
        initialMinute = currentTime.get(Calendar.MINUTE),
        is24Hour = true,
    )

    /** Determines whether the time picker is dial or input */
    var showDial by remember { mutableStateOf(true) }

    /** The icon used for the icon button that switches from dial to input */
    val toggleIcon = if (showDial) {
        Icons.Filled.EditCalendar
    } else {
        Icons.Filled.AccessTime
    }

    AdvancedTimePickerDialog(
        onDismiss = { onDismiss() },
        onConfirm = { onConfirm(timePickerState) },
        toggle = {
            IconButton(onClick = { showDial = !showDial }) {
                Icon(
                    imageVector = toggleIcon,
                    contentDescription = "Time picker type toggle",
                )
            }
        },
    ) {
        if (showDial) {
            TimePicker(
                state = timePickerState,
            )
        } else {
            TimeInput(
                state = timePickerState,
            )
        }
    }
}

@Composable
fun AdvancedTimePickerDialog(
    title: String = "Select Time",
    onDismiss: () -> Unit,
    onConfirm: () -> Unit,
    toggle: @Composable () -> Unit = {},
    content: @Composable () -> Unit,
) {
    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(usePlatformDefaultWidth = false),
    ) {
        Surface(
            shape = MaterialTheme.shapes.extraLarge,
            tonalElevation = 6.dp,
            modifier =
            Modifier
                .width(IntrinsicSize.Min)
                .height(IntrinsicSize.Min)
                .background(
                    shape = MaterialTheme.shapes.extraLarge,
                    color = MaterialTheme.colorScheme.surface
                ),
        ) {
            Column(
                modifier = Modifier.padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Text(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 20.dp),
                    text = title,
                    style = MaterialTheme.typography.labelMedium
                )
                content()
                Row(
                    modifier = Modifier
                        .height(40.dp)
                        .fillMaxWidth()
                ) {
                    toggle()
                    Spacer(modifier = Modifier.weight(1f))
                    TextButton(onClick = onDismiss) { Text("Cancel") }
                    TextButton(onClick = onConfirm) { Text("OK") }
                }
            }
        }
    }
}
```

<br />

Note the key points in this snippet:

1. The `AdvancedTimePickerExample` composable creates a customizable time picker dialog.
2. It uses a [`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/package-summary#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)) composable for more flexibility than `AlertDialog`.
3. The dialog includes a customizable title and a toggle button to switch between dial and input modes.
4. `Surface` applies shape and elevation to the dialog, with `IntrinsicSize.Min` for both width and height.
5. `Column` and `Row` layout provide the dialog's structure components.
6. The example tracks the picker mode using `showDial`.
   - An `IconButton` toggles between modes, updating the icon accordingly.
   - The dialog content switches between `TimePicker` and `TimeInput` based on the `showDial` state.

This advanced implementation provides a highly customizable and reusable time
picker dialog that can adapt to different use cases in your app.

This implementation appears as follows:
![A time picker in a custom dialog that implements a title, a mode toggle, and dismiss and confirm buttons.](https://developer.android.com/static/develop/ui/compose/images/components/timepicker-advanced.png) **Figure 2.** A time picker in a custom dialog.

## Additional resources

- [Time pickers guide](https://developer.android.com/develop/ui/compose/components/time-pickers)
- [Material Design - Time Pickers](https://m3.material.io/components/time-pickers/overview)