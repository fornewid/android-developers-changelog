---
title: https://developer.android.com/develop/ui/views/receive-rich-content
url: https://developer.android.com/develop/ui/views/receive-rich-content
source: md.txt
---

![](https://developer.android.com/static/images/develop/ui/views/copy-paste-drag-and-drop-in-split-screen.png) **Figure 1.** The unified API provides a single place to handle incoming content regardless of the specific UI mechanism, such as pasting from the touch \& hold menu or using drag-and-drop.

Users love images, videos, and other expressive content, but inserting and
moving this content in apps isn't always easy. To make it simpler for apps to
receive rich content, Android 12 (API level 31) introduces a unified API that
lets your app accept content from any source: clipboard, keyboard, or dragging.

You can attach an interface, such as
[`OnReceiveContentListener`](https://developer.android.com/reference/android/view/OnReceiveContentListener),
to UI components and get a callback when content is inserted through any
mechanism. The callback becomes the single place for your code to handle
receiving all content, from plain and styled text to markup, images, videos,
audio files, and others.

For backward compatibility with previous Android versions, this API is also
available in AndroidX, starting from
[Core 1.7](https://developer.android.com/jetpack/androidx/releases/core#1.7.0) and
[Appcompat 1.4](https://developer.android.com/jetpack/androidx/releases/appcompat#1.4.0),
which we recommend you use when implementing this functionality.

## Overview

With other existing APIs, each UI mechanism---such as the touch \& hold menu
or dragging---has its own corresponding API. This means that you have to
integrate with each API separately, adding similar code for each mechanism that
inserts content:
![An image showing the different actions and the relative API to implement](https://developer.android.com/static/images/develop/ui/views/required-apis-before.svg) **Figure 2.** Previously, apps implemented a different API for each UI mechanism for inserting content.

The `OnReceiveContentListener` API consolidates these different code paths by
creating a single API to implement, so you can focus on your app-specific logic
and let the platform handle the rest:
![An image showing the simplified unified API](https://developer.android.com/static/images/develop/ui/views/required-apis-after.svg) **Figure 3.** The unified API lets you implement a single API that supports all UI mechanisms.

This approach also means that when new ways of inserting content are added to
the platform, you don't need to make additional code changes to enable support
in your app. And if your app needs to implement full customization for a
particular use case, you can still use the existing APIs, which continue to work
the same way.

## Implementation

> [!NOTE]
> **Note:** See the [Drag and Drop sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/draganddrop) for a complete implementation of [`DropHelper`](https://developer.android.com/reference/kotlin/androidx/draganddrop/DropHelper), which implements `OnReceiveContentListener`. For more details, see the guide on [Enabling drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop).

The API is a listener interface with a single method,
[`OnReceiveContentListener`](https://developer.android.com/reference/android/view/OnReceiveContentListener).
To support older versions of the Android platform, we recommend using the
matching
[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener)
interface in the AndroidX Core library.

To use the API, implement the listener by specifying what types of content your
app can handle:

### Kotlin

```kotlin
object MyReceiver : OnReceiveContentListener {
    val MIME_TYPES = arrayOf("image/*", "video/*")
    
    // ...
    
    override fun onReceiveContent(view: View, payload: ContentInfoCompat): ContentInfoCompat? {
        TODO("Not yet implemented")
    }
}
```

### Java

```java
public class MyReceiver implements OnReceiveContentListener {
     public static final String[] MIME_TYPES = new String[] {"image/*", "video/*"};
     // ...
}
```

After specifying all the content MIME types that your app supports, implement
the rest of the listener:

### Kotlin

```kotlin
class MyReceiver : OnReceiveContentListener {
    override fun onReceiveContent(view: View, contentInfo: ContentInfoCompat): ContentInfoCompat {
        val split = contentInfo.partition { item: ClipData.Item -> item.uri != null }
        val uriContent = split.first
        val remaining = split.second
        if (uriContent != null) {
            // App-specific logic to handle the URI(s) in uriContent.
        }
        // Return anything that your app didn't handle. This preserves the
        // default platform behavior for text and anything else that you aren't
        // implementing custom handling for.
        return remaining
    }

    companion object {
        val MIME_TYPES = arrayOf("image/*", "video/*")
    }
}
```

### Java

```java
 public class MyReceiver implements OnReceiveContentListener {
     public static final String[] MIME_TYPES = new String[] {"image/*", "video/*"};

     @Override
     public ContentInfoCompat onReceiveContent(View view, ContentInfoCompat contentInfo) {
         Pair<ContentInfoCompat, ContentInfoCompat> split = contentInfo.partition(
                 item -> item.getUri() != null);
         ContentInfo uriContent = split.first;
         ContentInfo remaining = split.second;
         if (uriContent != null) {
             // App-specific logic to handle the URI(s) in uriContent.
         }
         // Return anything that your app didn't handle. This preserves the
         // default platform behavior for text and anything else that you aren't
         // implementing custom handling for.
         return remaining;
     }
 }
```

If your app already supports sharing with intents, you can reuse your
app-specific logic for handling content URIs. Return any remaining data to
delegate handling of that data to the platform.

After implementing the listener, set it on the appropriate UI elements in
your app:

### Kotlin

```kotlin
class MyActivity : Activity() {
    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // ...
        val myInput = findViewById(R.id.my_input)
        ViewCompat.setOnReceiveContentListener(myInput, MyReceiver.MIME_TYPES, MyReceiver())
    }
}
```

### Java

```java
public class MyActivity extends Activity {
     @Override
     public void onCreate(Bundle savedInstanceState) {
         // ...

         AppCompatEditText myInput = findViewById(R.id.my_input);
         ViewCompat.setOnReceiveContentListener(myInput, MyReceiver.MIME_TYPES, new MyReceiver());
     }
}
```

## URI permissions

Read permissions are granted and released automatically by the platform for any
[content URIs](https://developer.android.com/reference/android/content/ContentResolver#SCHEME_CONTENT) in the
payload passed to the `OnReceiveContentListener`.

Normally, your app processes content URIs in a service or activity. For
long-running processing, use
[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager). When you implement
this, extend permissions to the target service or activity by passing the
content using
[`Intent.setClipData`](https://developer.android.com/reference/android/content/Intent#setClipData(android.content.ClipData))
and [setting](https://developer.android.com/reference/android/content/Intent#addFlags(int)) the flag
[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION).

Alternatively, you can use a background thread within the current context to
process the content. In this case, you must maintain a reference to the
`payload` object received by the listener to help ensure that permissions aren't
revoked prematurely by the platform.

## Custom views

If your app uses a custom `View` subclass, take care to ensure that the
`OnReceiveContentListener` isn't bypassed.

If your `View` class overrides the
[`onCreateInputConnection`](https://developer.android.com/reference/android/widget/TextView#onCreateInputConnection(android.view.inputmethod.EditorInfo))
method, use the Jetpack API
[`InputConnectionCompat.createWrapper`](https://developer.android.com/reference/androidx/core/view/inputmethod/InputConnectionCompat#createWrapper(android.view.View,%20android.view.inputmethod.InputConnection,%20android.view.inputmethod.EditorInfo))
to configure the `InputConnection`.

If your `View` class overrides the
[`onTextContextMenuItem`](https://developer.android.com/reference/android/widget/TextView#onTextContextMenuItem(int))
method, delegate to super when the menu item is
[`R.id.paste`](https://developer.android.com/reference/android/R.id#paste) or
[`R.id.pasteAsPlainText`](https://developer.android.com/reference/android/R.id#pasteAsPlainText).

## Comparison with the keyboard image API

You can think of the `OnReceiveContentListener` API as the next version of the
existing [keyboard image API](https://developer.android.com/guide/topics/text/image-keyboard). This unified
API supports the functionality of the keyboard image API as well as some
additional features. Device and feature compatibility varies depending on
whether you use the Jetpack library or the native APIs from the Android SDK.

| Action or feature | Supported by keyboard image API | Supported by unified API |
|---|---|---|
| Insert from the keyboard | YesYes (API level 13 and higher) | Yes Yes (API level 13 and higher) |
| Insert using paste from the touch \& hold menu | NoNo | Yes Yes |
| Insert using drag-and-drop | NoNo | Yes Yes (API level 24 and higher) |
[**Table 1.** Supported features and API levels for
Jetpack.]

| Action or feature | Supported by keyboard image API | Supported by unified API |
|---|---|---|
| Insert from the keyboard | YesYes (API level 25 and higher) | Yes Yes (Android 12 and higher) |
| Insert using paste from the touch \& hold menu | NoNo | Yes Yes (Android 12 and higher) |
| Insert using drag and drop | NoNo | Yes Yes (Android 12 and higher) |
[**Table 2.** Supported features and API levels for native
APIs.]