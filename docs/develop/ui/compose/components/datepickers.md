---
title: https://developer.android.com/develop/ui/compose/components/datepickers
url: https://developer.android.com/develop/ui/compose/components/datepickers
source: md.txt
---

[Date pickers](https://m3.material.io/components/date-pickers/overview) let users select a date, a date range, or both. They use a
calendar dialog or text input to let users select dates.

## Types

There are three types of date pickers:

- **Docked**: Appears inline within the layout. It's suitable for compact layouts where a dedicated dialog might feel intrusive.
- **Modal**: Appears as a dialog overlaying the app's content. This provides a clear focus on date selection.
- **Modal input**: Combines a text field with a modal date picker.

You can implement these date pickers in your app using the following
composables:

- [`DatePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePicker(androidx.compose.material3.DatePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)): General composable for a date picker. The container you use determines whether it is docked or model.
- [`DatePickerDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.material3.DatePickerColors,androidx.compose.ui.window.DialogProperties,kotlin.Function1)): The container for both modal and modal input date pickers.
- [`DateRangePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DateRangePicker(androidx.compose.material3.DateRangePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)): For any date picker where the user can select a range with a start and end date.

> [!NOTE]
> **Note:** `DatePicker`, `DatePickerDialog`, and `DateRangePicker` are experimental. File any issues on the [issue tracker](https://issuetracker.google.com/issues/new?component=742043&template=1590761&pli=1).

## State

The key parameter that the different date picker composables share in common is
`state`, which takes either a [`DatePickerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerState(androidx.compose.material3.CalendarLocale,kotlin.Long,kotlin.Long,kotlin.ranges.IntRange,androidx.compose.material3.DisplayMode,androidx.compose.material3.SelectableDates)) or
[`DateRangePickerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DateRangePickerState) object. Their properties capture information about
the user's selection using the date picker, such as the current selected date.

For more information on how you can make use of the selected date, see the [Use
selected date section](https://developer.android.com/develop/ui/compose/components/datepickers#selected-date).

## Docked date picker

In the following example, there is a text field that prompts the user to input
their date of birth. When they click the calendar icon in the field, it opens a
docked date picker below the input field.


```kotlin
@Composable
fun DatePickerDocked() {
    var showDatePicker by remember { mutableStateOf(false) }
    val datePickerState = rememberDatePickerState()
    val selectedDate = datePickerState.selectedDateMillis?.let {
        convertMillisToDate(it)
    } ?: ""

    Box(
        modifier = Modifier.fillMaxWidth()
    ) {
        OutlinedTextField(
            value = selectedDate,
            onValueChange = { },
            label = { Text("DOB") },
            readOnly = true,
            trailingIcon = {
                IconButton(onClick = { showDatePicker = !showDatePicker }) {
                    Icon(
                        imageVector = Icons.Default.DateRange,
                        contentDescription = "Select date"
                    )
                }
            },
            modifier = Modifier
                .fillMaxWidth()
                .height(64.dp)
        )

        if (showDatePicker) {
            Popup(
                onDismissRequest = { showDatePicker = false },
                alignment = Alignment.TopStart
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .offset(y = 64.dp)
                        .shadow(elevation = 4.dp)
                        .background(MaterialTheme.colorScheme.surface)
                        .padding(16.dp)
                ) {
                    DatePicker(
                        state = datePickerState,
                        showModeToggle = false
                    )
                }
            }
        }
    }
}

@Composable
fun DatePickerFieldToModal(modifier: Modifier = Modifier) {
    var selectedDate by remember { mutableStateOf<Long?>(null) }
    var showModal by remember { mutableStateOf(false) }

    OutlinedTextField(
        value = selectedDate?.let { convertMillisToDate(it) } ?: "",
        onValueChange = { },
        label = { Text("DOB") },
        placeholder = { Text("MM/DD/YYYY") },
        trailingIcon = {
            Icon(Icons.Default.DateRange, contentDescription = "Select date")
        },
        modifier = modifier
            .fillMaxWidth()
            .pointerInput(selectedDate) {
                awaitEachGesture {
                    // Modifier.clickable doesn't work for text fields, so we use Modifier.pointerInput
                    // in the Initial pass to observe events before the text field consumes them
                    // in the Main pass.
                    awaitFirstDown(pass = PointerEventPass.Initial)
                    val upEvent = waitForUpOrCancellation(pass = PointerEventPass.Initial)
                    if (upEvent != null) {
                        showModal = true
                    }
                }
            }
    )

    if (showModal) {
        DatePickerModal(
            onDateSelected = { selectedDate = it },
            onDismiss = { showModal = false }
        )
    }
}

fun convertMillisToDate(millis: Long): String {
    val formatter = SimpleDateFormat("MM/dd/yyyy", Locale.getDefault())
    return formatter.format(Date(millis))
}
```

<br />

> [!NOTE]
> **Note:** This example is self-contained. For how you can expose the selected date to a parent composable, see the other examples.

### Key points about the code

- The date picker appears when the user clicks the `IconButton`.
  - The icon button serves as the argument for the `OutlinedTextField`'s `trailingIcon` parameter.
  - The `showDatePicker` state variable controls the visibility of the docked date picker.
- The date picker's container is a `Popup` composable, which overlays the content without affecting the layout of other elements.
- `selectedDate` captures the value of the selected date from the `DatePickerState` object and formats it using the `convertMillisToDate` function.
- The selected date appears in the text field.
- The docked date picker is positioned below the text field using an `offset` modifier.
- A `Box` is used as the root container to allow proper layering of the text field and the date picker.

### Results

After clicking the calendar icon, this implementation appears as follows:
![Docked date picker example.](https://developer.android.com/static/develop/ui/compose/images/components/datepicker-docked.png) **Figure 1.** A docked date picker.

## Modal date picker

A modal date picker displays a dialog that floats over the screen. To implement
it, create a [`DatePickerDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.material3.DatePickerColors,androidx.compose.ui.window.DialogProperties,kotlin.Function1)) and pass it a [`DatePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePicker(androidx.compose.material3.DatePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)).


```kotlin
@Composable
fun DatePickerModal(
    onDateSelected: (Long?) -> Unit,
    onDismiss: () -> Unit
) {
    val datePickerState = rememberDatePickerState()

    DatePickerDialog(
        onDismissRequest = onDismiss,
        confirmButton = {
            TextButton(onClick = {
                onDateSelected(datePickerState.selectedDateMillis)
                onDismiss()
            }) {
                Text("OK")
            }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) {
                Text("Cancel")
            }
        }
    ) {
        DatePicker(state = datePickerState)
    }
}
```

<br />

### Key points about the code

- The `DatePickerModal` composable function displays a modal date picker.
- The `onDateSelected` lambda expression executes when the user selects a date.
  - It exposes the selected date to the parent composable.
- The `onDismiss` lambda expression executes when the user dismisses the dialog.

### Results

This implementation appears as follows:
![Modal date picker example.](https://developer.android.com/static/develop/ui/compose/images/components/datepicker-modal.png) **Figure 2.** A modal date picker.

## Input modal date picker

A modal date picker with input displays a dialog that floats over the screen and
allows the user to input a date.


```kotlin
@Composable
fun DatePickerModalInput(
    onDateSelected: (Long?) -> Unit,
    onDismiss: () -> Unit
) {
    val datePickerState = rememberDatePickerState(initialDisplayMode = DisplayMode.Input)

    DatePickerDialog(
        onDismissRequest = onDismiss,
        confirmButton = {
            TextButton(onClick = {
                onDateSelected(datePickerState.selectedDateMillis)
                onDismiss()
            }) {
                Text("OK")
            }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) {
                Text("Cancel")
            }
        }
    ) {
        DatePicker(state = datePickerState)
    }
}
```

<br />

### Key points about the code

This is very much the same as the [modal date picker example](https://developer.android.com/develop/ui/compose/components/datepickers#modal). The primary
difference is the following:

- The `initialDisplayMode` parameter sets the initial display mode to `DisplayMode.Input`.

![Modal date picker with input.](https://developer.android.com/static/develop/ui/compose/images/components/datepicker-modal-input.png) **Figure 3.** A modal date picker with input.

## Date picker with range

You can create a date picker that lets the user select a range between a start
and end date. To do so, use [`DateRangePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DateRangePicker(androidx.compose.material3.DateRangePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)).

The use of `DateRangePicker` is essentially the same as `DatePicker`. You can
use it for a [docked picker](https://developer.android.com/develop/ui/compose/components/datepickers#docked) as a child of `PopUp`, or you can use it as a
[modal picker](https://developer.android.com/develop/ui/compose/components/datepickers#modal) and pass it to `DatePickerDialog`. The primary difference is
that you use [`DateRangePickerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DateRangePickerState) instead of [`DatePickerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerState(androidx.compose.material3.CalendarLocale,kotlin.Long,kotlin.Long,kotlin.ranges.IntRange,androidx.compose.material3.DisplayMode,androidx.compose.material3.SelectableDates)).

The following snippet demonstrates how to create a modal date picker with a
range:


```kotlin
@Composable
fun DateRangePickerModal(
    onDateRangeSelected: (Pair<Long?, Long?>) -> Unit,
    onDismiss: () -> Unit
) {
    val dateRangePickerState = rememberDateRangePickerState()

    DatePickerDialog(
        onDismissRequest = onDismiss,
        confirmButton = {
            TextButton(
                onClick = {
                    onDateRangeSelected(
                        Pair(
                            dateRangePickerState.selectedStartDateMillis,
                            dateRangePickerState.selectedEndDateMillis
                        )
                    )
                    onDismiss()
                }
            ) {
                Text("OK")
            }
        },
        dismissButton = {
            TextButton(onClick = onDismiss) {
                Text("Cancel")
            }
        }
    ) {
        DateRangePicker(
            state = dateRangePickerState,
            title = {
                Text(
                    text = "Select date range"
                )
            },
            showModeToggle = false,
            modifier = Modifier
                .fillMaxWidth()
                .height(500.dp)
                .padding(16.dp)
        )
    }
}
```

<br />

### Key points about the code

- The `onDateRangeSelected` parameter is a callback that receives a `Pair<Long?, Long?>` that represents the selected start and end dates. This gives the parent composable access to the selected range.
- `rememberDateRangePickerState()` creates the state for the date range picker.
- The `DatePickerDialog` creates a modal dialog container.
- In the confirm button's `onClick` handler, `onDateRangeSelected` passes up the selected range to the parent composable.
- The `DateRangePicker` composable serves as the dialog content.

### Results

This implementation appears as follows:
![Modal range date picker example.](https://developer.android.com/static/develop/ui/compose/images/components/datepicker-range.png) **Figure 4.** A modal date picker with a selected range.

## Use selected date

To capture the selected date, track it in the parent composable as a `Long` and
pass the value to the `DatePicker` in `onDateSelected`. The following snippet
demonstrates this, though you can see the full implementation in the [official
snippets app](https://github.com/android/snippets/tree/main/compose/snippets/src/main/java/com/example/compose/snippets).


```kotlin
// ...
    var selectedDate by remember { mutableStateOf<Long?>(null) }
// ...
        if (selectedDate != null) {
            val date = Date(selectedDate!!)
            val formattedDate = SimpleDateFormat("MMM dd, yyyy", Locale.getDefault()).format(date)
            Text("Selected date: $formattedDate")
        } else {
            Text("No date selected")
        }
// ...
        DatePickerModal(
            onDateSelected = {
                selectedDate = it
                showModal = false
            },
            onDismiss = { showModal = false }
        )
    }
// ...https://github.com/android/snippets/blob/bbf4e1ff2570641546d50270b121493ef1965774/compose/snippets/src/main/java/com/example/compose/snippets/components/DatePickers.kt#L74-L163
```

<br />

Essentially the same applies for [range date pickers](https://developer.android.com/develop/ui/compose/components/datepickers#range), though you need to
use a `Pair<Long?, Long?>` or a data class to capture the start and end values.

> [!IMPORTANT]
> **Important:** Instead of using a `Long` for the selected date, you could pass the state object itself from the parent composable to the child. Doing so would let you capture the full state in the parent.

## See also

- [Material Design date pickers](https://m3.material.io/components/date-pickers/overview)
- [Time pickers](https://developer.android.com/develop/ui/compose/components/time-pickers)