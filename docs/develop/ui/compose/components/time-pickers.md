---
title: https://developer.android.com/develop/ui/compose/components/time-pickers
url: https://developer.android.com/develop/ui/compose/components/time-pickers
source: md.txt
---

[Time pickers](https://m3.material.io/components/time-pickers/overview) provide a way for users to select a time. You can
use the [`TimePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType)) and [`TimeInput`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimeInput(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors)) composables to implement a time
picker in your app.

> [!NOTE]
> **Note:** `TimePicker` and `TimeInput` are experimental. File any issues on the [issue tracker](https://issuetracker.google.com/issues/new?component=856989&template=1425922).

## Types

There are two types of time picker:

- **Dial**: Lets users set a time by moving a handle around a dial.
- **Input**: Lets users set a time using their keyboard.

The following image provides an example of a dial time picker on the left, and
an input time picker on the right:
![A dial and an input time picker.](https://developer.android.com/static/develop/ui/compose/images/components/timepickers.png) **Figure 1.** A dial and an input time picker.

## API surface

To implement a time picker, use either the `TimePicker` or `TimeInput`
composable:

- [`TimePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType)): Implements a dial time picker.
- [`TimeInput`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimeInput(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors)): Implements an input time picker.

> [!NOTE]
> **Note:** While they display different components, `TimePicker` and `TimeInput` are very similar composables in terms of their parameters. They are therefore largely interchangeable.

### State

For both `TimePicker` and `TimeInput`, you must also pass a
[`TimePickerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TimePickerState). This lets you set the default selected time that appears
on the picker. It also captures the time that the user has selected using the
picker.

### Dialog

Time pickers appear in dialogs. The examples in this guide don't use dialogs.
For examples that do use dialogs, see the [Dialogs for time pickers](https://developer.android.com/develop/ui/compose/components/time-pickers-dialogs) guide.

## Dial time picker

This snippet demonstrates how to implement a basic dial time picker.


```kotlin
@Composable
fun DialExample(
    onConfirm: () -> Unit,
    onDismiss: () -> Unit,
) {
    val currentTime = Calendar.getInstance()

    val timePickerState = rememberTimePickerState(
        initialHour = currentTime.get(Calendar.HOUR_OF_DAY),
        initialMinute = currentTime.get(Calendar.MINUTE),
        is24Hour = true,
    )

    Column {
        TimePicker(
            state = timePickerState,
        )
        Button(onClick = onDismiss) {
            Text("Dismiss picker")
        }
        Button(onClick = onConfirm) {
            Text("Confirm selection")
        }
    }
}
```

<br />

Consider the following in this snippet:

- `Calendar.getInstance()` initializes the `TimePickerState` with the current time.
  - This example uses `java.util.Calendar`. Enable [Java
    8+ API desugaring](https://developer.android.com/studio/write/java8-support#library-desugaring) in your project to alternatively use `java.time.LocalTime` on all Android versions.
- The `TimePicker` composable displays the time picker, taking `timePickerState` as a parameter.
- The implementation includes two buttons: one to confirm the selection and another to dismiss the picker.

This implementation appears as follows:
![A dial time picker. The user can select a time using the dial.](https://developer.android.com/static/develop/ui/compose/images/components/timepicker-dial.png) **Figure 2.** A dial time picker.

## Input time picker

This snippet demonstrates how to implement a basic input style time picker.


```kotlin
@Composable
fun InputExample(
    onConfirm: () -> Unit,
    onDismiss: () -> Unit,
) {
    val currentTime = Calendar.getInstance()

    val timePickerState = rememberTimePickerState(
        initialHour = currentTime.get(Calendar.HOUR_OF_DAY),
        initialMinute = currentTime.get(Calendar.MINUTE),
        is24Hour = true,
    )

    Column {
        TimeInput(
            state = timePickerState,
        )
        Button(onClick = onDismiss) {
            Text("Dismiss picker")
        }
        Button(onClick = onConfirm) {
            Text("Confirm selection")
        }
    }
}
```

<br />

Key points to note in this implementation:

- The structure is essentially the same the dial time picker, with the main difference being the use of `TimeInput` instead of `TimePicker`.
- The `is24Hour` parameter for `timePickerState` is explicitly set to `true`. By default, this value is `false`.

This implementation appears as follows:
![An input time picker. The user can enter a time using text fields.](https://developer.android.com/static/develop/ui/compose/images/components/timepicker-input.png) **Figure 3.** An input time picker.

## Use the state

To make use of the time that the user has selected in a time picker, pass the
appropriate `TimePickerState` to your `onConfirm` function. The parent
composable can then access the selected time through `TimePickerState.hour` and
`TimePickerState.minute`.

The following snippet demonstrates how to do this:


```kotlin
@Composable
fun DialUseStateExample(
    onConfirm: (TimePickerState) -> Unit,
    onDismiss: () -> Unit,
) {
    val currentTime = Calendar.getInstance()

    val timePickerState = rememberTimePickerState(
        initialHour = currentTime.get(Calendar.HOUR_OF_DAY),
        initialMinute = currentTime.get(Calendar.MINUTE),
        is24Hour = true,
    )

    Column {
        TimePicker(
            state = timePickerState,
        )
        Button(onClick = onDismiss) {
            Text("Dismiss picker")
        }
        Button(onClick = { onConfirm(timePickerState) }) {
            Text("Confirm selection")
        }
    }
}
```

<br />

You could then call the composable like this:

    var selectedTime: TimePickerState? by remember { mutableStateOf(null) }

    // ...

    DialUseStateExample(
        onDismiss = {
            showDialExample = false
        },
        onConfirm = {
                time ->
            selectedTime = time
            showDialExample = false
        },
    )

    // ...

    if (selectedTime != null) {
        val cal = Calendar.getInstance()
        cal.set(Calendar.HOUR_OF_DAY, selectedTime!!.hour)
        cal.set(Calendar.MINUTE, selectedTime!!.minute)
        cal.isLenient = false
        Text("Selected time = ${formatter.format(cal.time)}")
    } else {
        Text("No time selected.")
    }

For more detail, see the [full implementation in the snippets
app](https://github.com/android/snippets/blob/main/compose/snippets/src/main/java/com/example/compose/snippets/components/TimePickers.kt).

## Additional resources

- [`TimePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType))
- [Material Design - Time Pickers](https://m3.material.io/components/time-pickers/overview)