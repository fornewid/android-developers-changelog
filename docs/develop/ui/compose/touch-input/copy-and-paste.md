---
title: https://developer.android.com/develop/ui/compose/touch-input/copy-and-paste
url: https://developer.android.com/develop/ui/compose/touch-input/copy-and-paste
source: md.txt
---

The Android clipboard-based framework for copying and pasting
supports primitive and complex data types, including:

- Text strings
- Complex data structures
- Text and binary stream data
- Application assets

Simple text data is stored directly in the clipboard,
while complex data is stored as a reference
that the pasting application resolves with a content provider.

Copying and pasting works both within an application and between applications
that implement the framework.

Because part of the framework uses content providers,
this document assumes some familiarity with the [Android Content Provider API](https://developer.android.com/guide/topics/providers/content-providers).

## Work with text

Some components support copying and pasting text out of the box, as shown in
the following table.

| Component | Copying text | Pasting text |
|---|---|---|
| BasicTextField | ✅ | ✅ |
| TextField | ✅ | ✅ |
| SelectionContainer | ✅ |   |

For example, you can copy the text in the card to the clipboard
in the following snippet and paste the copied text to the `TextField`.
You display the menu to paste the text by a
touch \& hold on the `TextField`, or by tapping the cursor handle.  

    val textFieldState = rememberTextFieldState()

    Column {
        Card {
            SelectionContainer {
                Text("You can copy this text")
            }
        }
        BasicTextField(state = textFieldState)
    }

You can paste the text with the following keyboard shortcut:
<kbd>Ctrl</kbd>+<kbd>V</kbd> .
The keyboard shortcut is also available by default.
Refer to [Handle keyboard actions](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands) for details.

### Copy with `ClipboardManager`

You can copy texts to the clipboard with [`ClipboardManager`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ClipboardManager).
Its [setText()](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ClipboardManager#setText(androidx.compose.ui.text.AnnotatedString)) method copies
the passed String object to the clipboard.
The following snippet copies "Hello, clipboard"
to the clipboard when the user clicks the button.  

    // Retrieve a ClipboardManager object
    val clipboardManager = LocalClipboardManager.current

    Button(
        onClick = {
            // Copy "Hello, clipboard" to the clipboard
            clipboardManager.setText("Hello, clipboard")
        }
    ) {
       Text("Click to copy a text")
    }

The following snippet does the same thing, but gives you more granular control.
A common use case is [copying sensitive content](https://developer.android.com/develop/ui/compose/touch-input/copy-and-paste#sensitive_content),
such as password. [`ClipEntry`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ClipEntry) describes an item on the clipboard.
It contains a [`ClipData`](https://developer.android.com/reference/android/content/ClipData) object that describes data on the clipboard.
[`ClipData.newPlainText()`](https://developer.android.com/reference/android/content/ClipData#newPlainText(java.lang.CharSequence,%20java.lang.CharSequence)) method is a convenience method to
create a `ClipData` object from a String object.
You can set the created `ClipEntry` object to clipboard
by calling the [setClip()](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ClipboardManager#setClip(androidx.compose.ui.platform.ClipEntry)) method
over the `ClipboardManager` object.  

    // Retrieve a ClipboardManager object
    val clipboardManager = LocalClipboardManager.current

    Button(
        onClick = {
            val clipData = ClipData.newPlainText("plain text", "Hello, clipboard")
            val clipEntry = ClipEntry(clipData)
            clipboardManager.setClip(clipEntry)
        }
    ) {
       Text("Click to copy a text")
    }

| **Note:** The clipboard can have only one `ClipEntry`.

### Paste with ClipboardManager

You can access the text copied to the clipboard
by calling [`getText()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ClipboardManager#getText()) method
over the `ClipboardManager`.
Its `getText()` method returns an `AnnotatedString` object
when a text is copied in the clipboard.
The following snippet appends text in the clipboard
to the text in the `TextField`.  

    var textFieldState = rememberTextFieldState()

    Column {
        TextField(state = textFieldState)

        Button(
            onClick = {
                // The getText method returns an AnnotatedString object or null
                val annotatedString = clipboardManager.getText()
                if(annotatedString != null) {
                    // The pasted text is placed on the tail of the TextField
                    textFieldState.edit {
                        append(text.toString())
                    }
                }
            }
        ) {
            Text("Click to paste the text in the clipboard")
        }
    }

## Work with rich content

Users love images, videos, and other expressive content.
Your app can enable the user to copy rich content with
`ClipboardManager` and `ClipEntry`.
The [`contentReceiver`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).contentReceiver(androidx.compose.foundation.content.ReceiveContentListener)) modifier helps you to implement pasting rich content.

### Copy rich content

Your app can't copy rich content directly to the clipboard.
Instead, your app passes a `URI` object to the clipboard
and provides access to the content with a [`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider).
The following code snippet shows how to copy a JPEG image to clipboard.
Refer to [Copy data streams](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Streams) for details.  

    // Get a reference to the context
    val context = LocalContext.current

    Button(
        onClick = {
            // URI of the copied JPEG data
            val uri = Uri.parse("content://your.app.authority/0.jpg")
            // Create a ClipData object from the URI value
            // A ContentResolver finds a proper ContentProvider so that ClipData.newUri can set appropriate MIME type to the given URI
            val clipData = ClipData.newUri(context.contentResolver, "Copied", uri)
            // Create a ClipEntry object from the clipData value
            val clipEntry = ClipEntry(clipData)
            // Copy the JPEG data to the clipboard
            clipboardManager.setClip(clipEntry)
        }
    ) {
        Text("Copy a JPEG data")
    }

## Paste a rich content

With the [`contentReceiver`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).contentReceiver(androidx.compose.foundation.content.ReceiveContentListener)) modifier, you can handle pasting rich content
to [`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary#BasicTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.input.TextFieldDecorator,androidx.compose.foundation.ScrollState)) in the modified component.
The following code snippet adds the pasted URI of an image data
to a list of [`Uri`](https://developer.android.com/reference/android/net/Uri) objects.  

    // A URI list of images
    val imageList by remember{ mutableListOf<Uri>() }

    // Remember the ReceiveContentListener object as it is created inside a Composable scope
    val receiveContentListener = remember {
        ReceiveContentListener { transferableContent ->
            // Handle the pasted data if it is image data
            when {
                // Check if the pasted data is an image or not
                transferableContent.hasMediaType(MediaType.Image)) -> {
                    // Handle for each ClipData.Item object
                    // The consume() method returns a new TransferableContent object containging ignored ClipData.Item objects
                    transferableContent.consume { item ->
                        val uri = item.uri
                        if (uri != null) {
                            imageList.add(uri)
                        }
                       // Mark the ClipData.Item object consumed when the retrieved URI is not null
                        uri != null
                    }
                }
                // Return the given transferableContent when the pasted data is not an image
                else -> transferableContent
            }
        }
    }

    val textFieldState = rememberTextFieldState()

    BasicTextField(
        state = textFieldState,
        modifier = Modifier
            .contentReceiver(receiveContentListener)
            .fillMaxWidth()
            .height(48.dp)
    )

The `contentReceiver` modifier takes a [`ReceiveContentListener`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/content/ReceiveContentListener) object
as its argument and calls [`onReceive`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/content/ReceiveContentListener#onReceive(androidx.compose.foundation.content.TransferableContent))
method of the passed object when the user pastes data
to the `BasicTextField` inside the modified component.

A [`TransferableContent`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/content/TransferableContent) object is passed to the onReceive method,
which describes the data that can be transferred between apps
by pasting in this case.
You can access the `ClipEntry` object by referring to the `clipEntry` attribute.

A `ClipEntry` object can have several [`ClipData.Item`](https://developer.android.com/reference/android/content/ClipData.Item) objects
when the user selects several images and copies them to the clipboard
for example.
You should mark consumed or ignored for each `ClipData.Item` object,
and return a `TransferableContent` containing
the ignored `ClipData.Item` objects
so that the closest ancestor `contentReceiver` modifier can receive it.

The [`TransferableContent.hasMediaType()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/content/TransferableContent#(androidx.compose.foundation.content.TransferableContent).hasMediaType(androidx.compose.foundation.content.MediaType)) method can help you determine
whether the `TransferableContent` object can provide an item
with the media type.
For example, the following method call returns `true`
if the `TransferableContent` object can provide an image.  

    transferableContent.hasMediaType(MediaType.Image)

## Work with complex data

You can copy complex data to the clipboard
in the same manner you do for the rich content.
Refer to [Use content providers to copy complex data](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Provider) for details.

You can also handle the pastes of complex data
in the same manner for the rich content.
You can receive a URI of the pasted data.
The actual data can be retrieved from a [`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider).
Refer to [Retrieve data from the provider](https://developer.android.com/guide/topics/providers/content-provider-basics#SimpleQuery) for more information.

## Feedback to copying content

Users expect feedback when they copy content to the clipboard,
so in addition to the framework that powers copy and paste,
Android shows a default UI to users when they copy in Android 13 (API level 33)
and higher. Due to this feature, there is a risk of duplicate notification.
You can learn more about this edge case in [Avoid duplicate notifications](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#duplicate-notifications)).
![An animation showing Android 13 clipboard notification](https://developer.android.com/static/images/about/versions/13/new-copy-paste-UI.gif) **Figure 1.** UI shown when content enters the clipboard in Android 13 and up.

Manually provide feedback to users
when copying in Android 12L (API level 32) and lower.
See the [recommendation](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Feedback).

### Sensitive content

If you choose to have your app let the user copy sensitive content to clipboard,
such as passwords, your app must let the system know
so that the system can avoid displaying the copied sensitive content
in the UI (figure 2).
![Copied text preview flagging sensitive content.](https://developer.android.com/static/images/about/versions/13/sensitive-content-after.png) **Figure 2.** Copied text preview with a sensitive content flag.

You must add a flag to [`ClipDescription`](https://developer.android.com/reference/android/content/ClipDescription) in `ClipData`
before calling `setClip()` method over the `ClipboardManager` object:  

    // If your app is compiled with the API level 33 SDK or higher.
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean(ClipDescription.EXTRA_IS_SENSITIVE, true)
        }
    }

    // If your app is compiled with a lower SDK.
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean("android.content.extra.IS_SENSITIVE", true)
        }
    }