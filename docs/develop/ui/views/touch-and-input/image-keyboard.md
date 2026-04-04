---
title: Image keyboard support  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/touch-and-input/image-keyboard
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Image keyboard support Stay organized with collections Save and categorize content based on your preferences.




Users often want to communicate using emoji, stickers, and other kinds of rich
content. In previous versions of Android, soft keyboards—also known as
[input method editors](/guide/topics/text/creating-input-method), or
IMEs—could send only Unicode emoji to apps. For rich content, apps built
app-specific APIs that couldn't be used in other apps or used workarounds like
sending images through [simple share action](/training/sharing/shareaction)
or the clipboard.

![An image showing a keyboard that support image search](/static/images/guide/topics/text/image-keyboard-sample.png)


**Figure 1.** Example of image keyboard support.

Starting with Android 7.1 (API level 25), the Android SDK includes the Commit
Content API, which provides a universal way for IMEs to send images and other
rich content directly to a text editor in an app. The API is also available in
the v13 Support Library as of revision 25.0.0. We recommend using the Support
Library because it contains helper methods that simplify implementation.

With this API, you can build messaging apps that accept rich content from any
keyboard as well as keyboards that can send rich content to any app. The [Google
Keyboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)
and apps like [Messages by
Google](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging)
support the Commit Content API in Android 7.1, as shown in figure 1.

This document shows how to implement the Commit Content API in both IMEs and
apps.

## How it works

Keyboard image insertion requires participation from the IME and the app. The
following sequence describes each step in the image insertion process:

1. When the user taps an [`EditText`](/reference/android/widget/EditText),
   the editor sends a list of MIME content types that it accepts in
   [`EditorInfo.contentMimeTypes`](/reference/android/view/inputmethod/EditorInfo#contentMimeTypes).
2. The IME reads the list of supported types and displays content in the soft
   keyboard that the editor can accept.
3. When the user selects an image, the IME calls
   [`commitContent()`](/reference/android/view/inputmethod/InputConnection#commitContent(android.view.inputmethod.InputContentInfo,%20int,%20android.os.Bundle))
   and sends an
   [`InputContentInfo`](/reference/android/view/inputmethod/InputContentInfo)
   to the editor. The `commitContent()` call is analogous to the
   [`commitText()`](/reference/android/view/inputmethod/InputConnection#commitText(java.lang.CharSequence,%0Aint)) call, but for rich content. `InputContentInfo` contains an URI that
   identifies the content in a [content
   provider](/guide/topics/providers/content-providers).

This process is depicted in figure 2:

![An image showing the sequence from Application to IME and back to Application](/static/images/guide/topics/text/image-keyboard-diagram.png)


**Figure 2.** Application to IME to application flow.

## Add image support to apps

**Important:** For editable `TextView` objects, follow the implementation steps in
the [Receive rich content](/guide/topics/input/receive-rich-content)
documentation to quickly add support for accepting rich content from IMEs in
your app. This section describes how to accept rich content for `View` objects
that don't yet support the
[`OnReceiveContentListener`](/reference/android/view/OnReceiveContentListener).

To accept rich content from IMEs, an app must tell IMEs what content types it
accepts and specify a callback method that is executed when content is received.
The following example demonstrates how to create an `EditText` that accepts PNG
images:

### Kotlin

```
var editText: EditText = object : EditText(this) {
    override fun onCreateInputConnection(outAttrs: EditorInfo): InputConnection {
        var ic = super.onCreateInputConnection(outAttrs)
        EditorInfoCompat.setContentMimeTypes(outAttrs, arrayOf("image/png"))
        val mimeTypes = ViewCompat.getOnReceiveContentMimeTypes(this)
        if (mimeTypes != null) {
            EditorInfoCompat.setContentMimeTypes(outAttrs, mimeTypes)
            ic = InputConnectionCompat.createWrapper(this, ic, outAttrs)
        }
        return ic
    }
}
```

### Java

```
EditText editText = new EditText(this) {
    @Override
    public InputConnection onCreateInputConnection(EditorInfo outAttrs) {
        InputConnection ic = super.onCreateInputConnection(outAttrs);
        EditorInfoCompat.setContentMimeTypes(outAttrs, new String[]{"image/png"});
        String[] mimeTypes = ViewCompat.getOnReceiveContentMimeTypes(this);
        if (mimeTypes != null) {
            EditorInfoCompat.setContentMimeTypes(outAttrs, mimeTypes);
            ic = InputConnectionCompat.createWrapper(this, ic, outAttrs);
        }
        return ic;
    }
};
```

The following is further explanation:

* This example uses the Support Library, so there are some references to
  [`android.support.v13.view.inputmethod`](/reference/android/support/v13/view/inputmethod/package-summary)
  instead of
  [`android.view.inputmethod`](/reference/android/view/inputmethod/package-summary).
* This example creates an `EditText` and overrides its
  [`onCreateInputConnection(EditorInfo)`](/reference/android/widget/TextView#onCreateInputConnection(android.view.inputmethod.EditorInfo))
  method to modify the
  [`InputConnection`](/reference/android/view/inputmethod/InputConnection).
  The `InputConnection` is the communication channel between an IME and the
  app that is receiving its input.
* The call
  [`super.onCreateInputConnection()`](/reference/android/widget/TextView#onCreateInputConnection(android.view.inputmethod.EditorInfo))
  preserves the built-in behavior—sending and receiving text—and
  gives you a reference to the `InputConnection`.
* [`setContentMimeTypes()`](/reference/androidx/core/view/inputmethod/EditorInfoCompat#setContentMimeTypes(android.view.inputmethod.EditorInfo,java.lang.String%5B%5D))
  adds a list of supported MIME types to the
  [`EditorInfo`](/reference/android/view/inputmethod/EditorInfo). Call
  `super.onCreateInputConnection()` before `setContentMimeTypes()`.
* `callback` is executed whenever the IME commits content. The method
  [`onCommitContent()`](/reference/androidx/core/view/inputmethod/InputConnectionCompat.OnCommitContentListener#onCommitContent(androidx.core.view.inputmethod.InputContentInfoCompat,int,android.os.Bundle))
  has a reference to
  [`InputContentInfoCompat`](/reference/androidx/core/view/inputmethod/InputContentInfoCompat),
  which contains a content URI.

  + Request and release permissions if your app is running on API level 25
    or higher and the
    [`INPUT_CONTENT_GRANT_READ_URI_PERMISSION`](/reference/androidx/core/view/inputmethod/InputConnectionCompat#INPUT_CONTENT_GRANT_READ_URI_PERMISSION())
    flag is set by the IME. Otherwise, you already have access to the content
    URI because it is granted by the IME or because the content provider
    doesn't restrict access. For more information, see [Add image support to
    IMEs](#imes).
* [`createWrapper()`](/reference/androidx/core/view/inputmethod/InputConnectionCompat#createWrapper(android.view.View,android.view.inputmethod.InputConnection,android.view.inputmethod.EditorInfo))
  wraps the `InputConnection`, the modified `EditorInfo`, and the callback
  into a new `InputConnection` and returns it.

The following are recommended practices:

* Editors that don't support rich content don't call
  [`setContentMimeTypes()`](/reference/androidx/core/view/inputmethod/EditorInfoCompat#setContentMimeTypes(android.view.inputmethod.EditorInfo,%0Ajava.lang.String%5B%5D)), and they leave their `EditorInfo.contentMimeTypes` set
  to `null`.
* Editors ignore the content if the MIME type specified in `InputContentInfo`
  doesn't match any of the types they accept.
* Rich content doesn't affect and isn't affected by the position of the text
  cursor. Editors can ignore cursor position when working with content.
* In the editor's
  [`OnCommitContentListener.onCommitContent()`](/reference/androidx/core/view/inputmethod/InputConnectionCompat.OnCommitContentListener#onCommitContent(android.support.v13.view.inputmethod.InputContentInfoCompat,%0Aint,%20android.os.Bundle)) method, you can return `true` asynchronously, even
  before loading the content.
* Unlike text, which can be edited in the IME before being committed, rich
  content is committed immediately. If you want to let users edit or delete
  content, implement the logic yourself.

To test your app, make sure your device or emulator has a keyboard that can send
rich content. You can use the Google Keyboard in Android 7.1 or higher.

## Add image support to IMEs

IMEs that want to send rich content to apps must implement the Commit Content
API, as shown in the following example:

* Override
  [`onStartInput()`](/reference/android/inputmethodservice/InputMethodService#onStartInput(android.view.inputmethod.EditorInfo,%0Aboolean)) or
  [`onStartInputView()`](/reference/android/inputmethodservice/InputMethodService#onStartInputView(android.view.inputmethod.EditorInfo,%0Aboolean)) and read the list of supported content types from the target
  editor. The following code snippet shows how to check whether the target
  editor accepts GIF images.

### Kotlin

```
override fun onStartInputView(editorInfo: EditorInfo, restarting: Boolean) {
    val mimeTypes: Array<String> = EditorInfoCompat.getContentMimeTypes(editorInfo)

    val gifSupported: Boolean = mimeTypes.any {
        ClipDescription.compareMimeTypes(it, "image/gif")
    }

    if (gifSupported) {
        // The target editor supports GIFs. Enable the corresponding content.
    } else {
        // The target editor doesn't support GIFs. Disable the corresponding
        // content.
    }
}
```

### Java

```
@Override
public void onStartInputView(EditorInfo info, boolean restarting) {
    String[] mimeTypes = EditorInfoCompat.getContentMimeTypes(editorInfo);

    boolean gifSupported = false;
    for (String mimeType : mimeTypes) {
        if (ClipDescription.compareMimeTypes(mimeType, "image/gif")) {
            gifSupported = true;
        }
    }

    if (gifSupported) {
        // The target editor supports GIFs. Enable the corresponding content.
    } else {
        // The target editor doesn't support GIFs. Disable the corresponding
        // content.
    }
}
```

* Commit content to the app when the user selects an image. Avoid calling
  [`commitContent()`](/reference/android/view/inputmethod/InputConnection#commitContent(android.view.inputmethod.InputContentInfo,%0Aint,%20android.os.Bundle)) when there is any text being composed, because it
  might cause the editor to lose focus. The following code snippet shows how
  to commit a GIF image.

### Kotlin

```
// Commits a GIF image.

// @param contentUri = Content URI of the GIF image to be sent.
// @param imageDescription = Description of the GIF image to be sent.

fun commitGifImage(contentUri: Uri, imageDescription: String) {
    val inputContentInfo = InputContentInfoCompat(
            contentUri,
            ClipDescription(imageDescription, arrayOf("image/gif")),
            null
    )
    val inputConnection = currentInputConnection
    val editorInfo = currentInputEditorInfo
    var flags = 0
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N_MR1) {
        flags = flags or InputConnectionCompat.INPUT_CONTENT_GRANT_READ_URI_PERMISSION
    }
    InputConnectionCompat.commitContent(inputConnection, editorInfo, inputContentInfo, flags, null)
}
```

### Java

```
// Commits a GIF image.

// @param contentUri = Content URI of the GIF image to be sent.
// @param imageDescription = Description of the GIF image to be sent.

public static void commitGifImage(Uri contentUri, String imageDescription) {
    InputContentInfoCompat inputContentInfo = new InputContentInfoCompat(
            contentUri,
            new ClipDescription(imageDescription, new String[]{"image/gif"}),
            null
    );
    InputConnection inputConnection = getCurrentInputConnection();
    EditorInfo editorInfo = getCurrentInputEditorInfo();
    Int flags = 0;
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N_MR1) {
        flags |= InputConnectionCompat.INPUT_CONTENT_GRANT_READ_URI_PERMISSION;
    }
    InputConnectionCompat.commitContent(
            inputConnection, editorInfo, inputContentInfo, flags, null);
}
```

As an IME author, you most likely have to implement your own content provider to
respond to content URI requests. The exception is if your IME supports content
from existing content providers like
[`MediaStore`](/reference/android/provider/MediaStore). For information on
building content providers, see the [content
provider](/guide/topics/providers/content-providers) and [file
provider](/training/secure-file-sharing/setup-sharing) documentation.

If you are building your own content provider, we recommend you don't export it
by setting
[`android:exported`](/guide/topics/manifest/provider-element#exported) to
`false`. Instead, enable permission granting in the provider by setting
[`android:grantUriPermission`](/guide/topics/manifest/provider-element#gprmsn)
to `true`. Then, your IME can grant permissions to access the content URI when
the content is committed. There are two ways to do this:

* On Android 7.1 (API level 25) and higher, when calling `commitContent()`,
  set the flag parameter to
  [`INPUT_CONTENT_GRANT_READ_URI_PERMISSION`](/reference/androidx/core/view/inputmethod/InputConnectionCompat#INPUT_CONTENT_GRANT_READ_URI_PERMISSION()).
  Then, the `InputContentInfo` object that the app receives can request and
  release temporary read permissions by calling
  [`requestPermission()`](/reference/android/view/inputmethod/InputContentInfo#requestPermission())
  and
  [`releasePermission()`](/reference/android/view/inputmethod/InputContentInfo#releasePermission()).
* On Android 7.0 (API level 24) and lower,
  `INPUT_CONTENT_GRANT_READ_URI_PERMISSION` is ignored, so manually grant
  permission to the content. One way to do this is with
  [`grantUriPermission()`](/reference/android/content/Context#grantUriPermission(java.lang.String,%0Aandroid.net.Uri,%20int)), but you can implement your own mechanism that
  satisfies your own requirements.

To test your IME, make sure your device or emulator has an app that can receive
rich content. You can use the Google Messenger app in Android 7.1 or higher.