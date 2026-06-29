---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-user-input
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-user-input
source: md.txt
---

<br />

The [`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/Dialog.composable#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)) component displays pop-up messages or requests user input on a
layer above the main app content. It creates an interruptive UI experience to
capture user attention.

Among the use cases for a dialog are the following:

- Confirming user action, such as when deleting a file.
- Requesting user input, such as in a to-do list app.
- Presenting a list of options for user selection, like choosing a country in a profile setup.

This topic provides the following implementations:

- [Alert](https://developer.android.com/develop/ui/compose/quick-guides/content/display-user-input#alert)
- [Basic dialog](https://developer.android.com/develop/ui/compose/quick-guides/content/display-user-input#basic)
- [Advanced dialog](https://developer.android.com/develop/ui/compose/quick-guides/content/display-user-input#advanced)

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-user-input_90b94f6fc49da5d289b5455639aac6e3fffc24699727c9148b981cb0dd1fe670.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create an Alert dialog

The [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/AlertDialog.composable#AlertDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.window.DialogProperties)) composable provides a convenient API for creating a
Material Design themed dialog. The following example implements two buttons in
an alert dialog, one that dismisses the dialog, and another that confirms its
request:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-user-input_d8da831567d246cb4f5fcb7cf59889a8d142c2dcbec8a38233422b4a23829771.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

This implementation implies a parent composable that passes arguments to the
child composable in this way:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-user-input_39d92462938505d0aa49b9f087cde9ed11602db8ab928896bf3bb8681b1ff08d.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![An open alert dialog that has both a dismiss and confirm button.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-alert.png) **Figure 1.** An alert dialog with buttons.

### Key points

`AlertDialog` has specific parameters for handling particular elements of the
dialog. Among them are the following:

- `title`: The text that appears along the top of the dialog.
- `text`: The text that appears centered within the dialog.
- `icon`: The graphic that appears at the top of the dialog.
- `onDismissRequest`: The function called when the user dismisses the dialog, such as by tapping outside of it.
- `dismissButton`: A composable that serves as the dismiss button.
- `confirmButton`: A composable that serves as the confirm button.

- When the user clicks either of the buttons, the dialog closes. When the user
  clicks confirm, it calls a function that also handles the confirmation. In
  this example, those functions are `onDismissRequest()` and
  `onConfirmRequest()`.

  In cases where your dialog requires a more complex set of buttons, you may
  benefit from using the `Dialog` composable and populating it in a more
  freeform manner.

## Create a dialog

[`Dialog`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/Dialog.composable#Dialog(kotlin.Function0,androidx.compose.ui.window.DialogProperties,kotlin.Function0)) is a basic composable that doesn't provide any styling or
predefined slots for content. It is a straightforward container that you should
populate with a container such as `Card`. The following are some of the key
parameters of a dialog:

- **`onDismissRequest`**: The lambda called when the user closes the dialog.
- **`properties`** : An instance of [`DialogProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/window/DialogProperties) that provides some additional scope for customization.

> [!CAUTION]
> **Caution:** You must manually specify the size and shape of `Dialog`. You also must provide an inner container.

### Create a basic dialog

The following example is a basic implementation of the `Dialog` composable. Note
that it uses a `Card` as the secondary container. Without the `Card`, the `Text`
component would appear alone above the main app content.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-user-input_888adf8185db97c78c73a0362508ca7db20ec7fc6ef31bf715e2239ea3d01335.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Result

Note that when the dialog is open, the main app content beneath it appears
darkened and grayed out:
![A dialog that contains nothing other than a label.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-minimal.png) **Figure 2.** Minimal dialog.

### Create an advanced dialog

The following is a more advanced implemented of the `Dialog` composable. In this
case, the component manually implements a similar interface to the preceding
`AlertDialog` example.

> [!CAUTION]
> **Caution:** If you only need to display a two-button dialog as in this example, you should use `AlertDialog` and its more convenient API. However, if you want to create a more complex dialog, perhaps with forms and multiple buttons, you should use `Dialog` with custom content, as in the following example.

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-user-input_7852eaa9309c4b5209685f2ec98ff392069e53988bfaf789d8ae6393ee2d69d7.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Result

![A dialog with a photo of Mount Feathertop, Victoria. Below the image are a dismiss button and a confirm button.](https://developer.android.com/static/develop/ui/compose/images/components/dialog-image.png) **Figure 3.** A dialog that includes an image.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways you can present text in your app to provide a delightful user experience. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-text) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Request user input

Learn how to implement ways for users to interact with your app by entering text and using other means of input. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/request-user-input) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)