---
title: https://developer.android.com/develop/ui/compose/components/dialog
url: https://developer.android.com/develop/ui/compose/components/dialog
source: md.txt
---

The [`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/package-summary#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)) component displays dialog messages or requests user input on a
layer above the main app content. It creates an interruptive UI experience to
capture user attention.

Among the use cases for a dialog are the following:

- Confirming user action, such as when deleting a file.
- Requesting user input, such as in a to-do list app.
- Presenting a list of options for user selection, like choosing a country in a profile setup.

![A dialog populated with text and icons.](https://developer.android.com/static/develop/ui/compose/images/components/dialog.svg) **Figure 1.** An example of a dialog populated with text and icons.

## Alert dialog

The [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AlertDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.window.DialogProperties)) composable provides a convenient API for creating a
Material Design themed dialog. `AlertDialog` has specific parameters for
handling particular elements of the dialog. Among them are the following:

- `title`: The text that appears along the top of the dialog.
- `text`: The text that appears centered within the dialog.
- `icon`: The graphic that appears at the top of the dialog.
- `onDismissRequest`: The function called when the user dismisses the dialog, such as by tapping outside of it.
- `dismissButton`: A composable that serves as the dismiss button.
- `confirmButton`: A composable that serves as the confirm button.

The following example implements two buttons in an alert dialog, one that
dismisses the dialog, and another that confirms its request.


```kotlin
@Composable
fun AlertDialogExample(
    onDismissRequest: () -> Unit,
    onConfirmation: () -> Unit,
    dialogTitle: String,
    dialogText: String,
    icon: ImageVector,
) {
    AlertDialog(
        icon = {
            Icon(icon, contentDescription = "Example Icon")
        },
        title = {
            Text(text = dialogTitle)
        },
        text = {
            Text(text = dialogText)
        },
        onDismissRequest = {
            onDismissRequest()
        },
        confirmButton = {
            TextButton(
                onClick = {
                    onConfirmation()
                }
            ) {
                Text("Confirm")
            }
        },
        dismissButton = {
            TextButton(
                onClick = {
                    onDismissRequest()
                }
            ) {
                Text("Dismiss")
            }
        }
    )
}
```

<br />

This implementation implies a parent composable that passes arguments to the
child composable in this way:


```kotlin
@Composable
fun DialogExamples() {
    // ...
    val openAlertDialog = remember { mutableStateOf(false) }

    // ...
        when {
            // ...
            openAlertDialog.value -> {
                AlertDialogExample(
                    onDismissRequest = { openAlertDialog.value = false },
                    onConfirmation = {
                        openAlertDialog.value = false
                        println("Confirmation registered") // Add logic here to handle confirmation.
                    },
                    dialogTitle = "Alert dialog example",
                    dialogText = "This is an example of an alert dialog with buttons.",
                    icon = Icons.Default.Info
                )
            }
        }
    }
}
```

<br />

This implementation appears as follows:
![An open alert dialog that has both a dismiss and confirm button.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-alert.png) **Figure 2.** An alert dialog with buttons.

> [!NOTE]
> **Note:** When the user clicks either of the buttons, the dialog closes. When the user clicks confirm, it calls a function that also handles the confirmation. In this example, those functions are `onDismissRequest()` and `onConfirmRequest()`.

> [!NOTE]
> **Note:** In cases where your dialog requires a more complex set of buttons, you may benefit from using the `Dialog` composable and populating it in a more freeform manner.

## Dialog composable

[`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/package-summary#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)) is a basic composable that doesn't provide any styling or
predefined slots for content. It is a relatively straightforward container that
you should populate with a container such as `Card`. The following are some of
the key parameters of a dialog:

- **`onDismissRequest`**: The lambda called when the user closes the dialog.
- **`properties`** : An instance of [`DialogProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/DialogProperties) that provides some additional scope for customization.

> [!CAUTION]
> **Caution:** Unlike the example of `AlertDialog` in the preceding section, you need to manually specify the size and shape of `Dialog`. You also need to provide an inner container.

### Basic example

The following example is a basic implementation of the `Dialog` composable. Note
that it uses a `Card` as the secondary container. Without the `Card`, the `Text`
component would appear alone above the main app content.


```kotlin
@Composable
fun MinimalDialog(onDismissRequest: () -> Unit) {
    Dialog(onDismissRequest = { onDismissRequest() }) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .height(200.dp)
                .padding(16.dp),
            shape = RoundedCornerShape(16.dp),
        ) {
            Text(
                text = "This is a minimal dialog",
                modifier = Modifier
                    .fillMaxSize()
                    .wrapContentSize(Alignment.Center),
                textAlign = TextAlign.Center,
            )
        }
    }
}
```

<br />

This implementation appears as follows. Note that when the dialog is open, the
main app content beneath it appears darkened and grayed out:
![A dialog that contains nothing other than a label.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-minimal.png) **Figure 3.** Minimal dialog.

### Advanced example

The following is a more advanced implemented of the `Dialog` composable. In this
case, the component manually implements a similar interface to the `AlertDialog`
example above.

> [!CAUTION]
> **Caution:** If you only need to display a two-button dialog as in this example, you should use `AlertDialog` and its more convenient API. However, if you want to create a more complex dialog, perhaps with forms and multiple buttons, you should use `Dialog` with custom content, as in the following example.


```kotlin
@Composable
fun DialogWithImage(
    onDismissRequest: () -> Unit,
    onConfirmation: () -> Unit,
    painter: Painter,
    imageDescription: String,
) {
    Dialog(onDismissRequest = { onDismissRequest() }) {
        // Draw a rectangle shape with rounded corners inside the dialog
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .height(375.dp)
                .padding(16.dp),
            shape = RoundedCornerShape(16.dp),
        ) {
            Column(
                modifier = Modifier
                    .fillMaxSize(),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally,
            ) {
                Image(
                    painter = painter,
                    contentDescription = imageDescription,
                    contentScale = ContentScale.Fit,
                    modifier = Modifier
                        .height(160.dp)
                )
                Text(
                    text = "This is a dialog with buttons and an image.",
                    modifier = Modifier.padding(16.dp),
                )
                Row(
                    modifier = Modifier
                        .fillMaxWidth(),
                    horizontalArrangement = Arrangement.Center,
                ) {
                    TextButton(
                        onClick = { onDismissRequest() },
                        modifier = Modifier.padding(8.dp),
                    ) {
                        Text("Dismiss")
                    }
                    TextButton(
                        onClick = { onConfirmation() },
                        modifier = Modifier.padding(8.dp),
                    ) {
                        Text("Confirm")
                    }
                }
            }
        }
    }
}
```

<br />

This implementation appears as follows:
![A dialog with a photo of Mount Feathertop, Victoria. Below the image are a dismiss button and a confirm button.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-image.png) **Figure 4.** A dialog that includes an image.

## Additional resources

- [Material UI docs](https://m3.material.io/components/dialogs/overview)