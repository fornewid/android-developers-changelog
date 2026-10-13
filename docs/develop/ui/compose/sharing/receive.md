---
title: https://developer.android.com/develop/ui/compose/sharing/receive
url: https://developer.android.com/develop/ui/compose/sharing/receive
source: md.txt
---

Just as an app can send data to other apps, it can also receive data from other
apps. Think about how users interact with your application and what data types
you want to receive from other applications. For example, a social networking
application might be interested in receiving text content, like an interesting
web URL, from another app.

In an app using Compose Navigation, receiving data sent by another app is a
three-step process:

1. Declare an `<intent-filter>` in the manifest: You must still add an intent
   filter to your activity in the `AndroidManifest.xml` file. This tells the
   Android OS that your application is capable of receiving specific actions
   (like `ACTION_SEND`) and MIME types (like `text/plain`).

2. Define a `navDeepLink` in your Compose Navigation graph: Attach a
   `navDeepLink` that matches the action and MIME type directly to the
   composable destination that should display the content. The `NavController`
   automatically intercepts the incoming intent and routes the user directly to
   that screen.

3. Extract the incoming data payload: In your destination screen, access the
   intent extras (such as `EXTRA_TEXT` or `EXTRA_STREAM`) to retrieve
   the shared content and update your UI state.

Direct Share targets are deep links into a specific activity within your app.
They often represent a person or a group, and the Android Sharesheet shows them.
For example, a messaging app can provide a Direct Share target for a person that
deep links directly into a conversation with that person. See [Provide Direct
Share targets](https://developer.android.com/develop/ui/compose/sharing/direct-share-targets) for detailed instructions.

## Support MIME types

Ideally, an app must be able to receive the widest possible range of MIME types.
For example, a messaging app designed for sending text, images, and video
ideally supports receiving `text/*`, `image/*` and `video/*`. Here are a few
common MIME types for sending and receiving data in Android.

| Receivers register for | Senders send |
|---|---|
| `text/*` | - `text/plain` - `text/rtf` - `text/html` - `text/json` |
| `image/*` | - `image/jpg` - `image/png` - `image/gif` |
| `video/*` | - `video/mp4` - `video/3gp` |
| Supported file extensions | `application/pdf` |

See the [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) official registry of MIME media types.

> [!CAUTION]
> **Caution:** Although you can receive a MIME type of `*/*`, avoid doing so unless your app is fully capable of handling any type of incoming content.

## Make great share targets

When users tap a share target associated with a specific activity, let them
confirm and edit the shared content before your app uses it. This is especially
important for text data.

## Receive data in your app

Receiving shared data in an app using Compose involves declaring intent filters
in your manifest, routing incoming intents to the proper screen with deep links,
and extracting the payload from the intent to update your UI.

### Update your manifest

Intent filters inform the system which intents an app component accepts. Similar
to how you constructed an intent with an `ACTION_SEND` action in the [Sending
data to other apps](https://developer.android.com/develop/ui/compose/sharing/send) lesson, you create intent filters to receive
intents with this action. You define an intent filter in your manifest using the
`<intent-filter>` element. For example, if your app handles receiving text
content, a manifest that includes one or more images of any type would look like
the following snippet:

    <activity android:name=".ui.MyActivity" android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.SEND" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="image/*" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action.SEND" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="text/plain" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action.SEND_MULTIPLE" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="image/*" />
        </intent-filter>
    </activity>

When another app tries to share any of these things by constructing an intent
and passing it to [`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)), your application is listed
as an option in the Android Sharesheet or intent resolver. If the user selects
your app, this starts the corresponding activity (`.ui.MyActivity` in the
preceding example). It's then up to you to handle the content appropriately
within your code and UI.

> [!NOTE]
> **Note:** For more information about intent filters and intent resolution, read [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters#Receiving).

### Define a deep link in your navigation graph

In Compose Navigation, attach a `navDeepLink` directly to the composable
destination that should display the content. When another app shares data that
matches your intent filter, Compose Navigation routes the user directly to this
destination:


```kotlin
composable(
    route = "incoming_share",
    deepLinks = listOf(
        navDeepLink {
            action = Intent.ACTION_SEND
            mimeType = "text/plain"
        },
        navDeepLink {
            action = Intent.ACTION_SEND
            mimeType = "image/*"
        },
        navDeepLink {
            action = Intent.ACTION_SEND_MULTIPLE
            mimeType = "image/*"
        }
    )
) {
    SharesheetHandler()
}
```

<br />

The `navDeepLink` matches on the action and MIME type of the incoming intent to
navigate to the correct destination screen. Once on that destination, your
handler inspects the intent to determine which payload was received (such as a
single image versus multiple images) and extracts the corresponding extras.

### Handle the incoming content

To retrieve the content delivered by an [`Intent`](https://developer.android.com/reference/android/content/Intent), read the current
activity from [`LocalActivity.current`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#LocalActivity()) within your composable,
then examine the intent to determine what to do next. If this activity can be
started from other parts of the system (such as the launcher), take this into
consideration when examining the intent.

Take extra care to check incoming data: the wrong MIME type might be set, or an
image being sent might be extremely large. Process binary data or heavy I/O
operations (such as decoding large images or writing files) asynchronously using
coroutines (such as `Dispatchers.IO`) rather than on the main UI thread.


```kotlin
@Composable
fun SharesheetHandler() {
    val activity = LocalActivity.current
    val intent = activity?.intent

    when (intent?.action) {
        Intent.ACTION_SEND -> {
            if (intent.type == "text/plain") {
                handleSendText(intent) // Handle text being sent
            } else if (intent.type?.startsWith("image/") == true) {
                handleSendImage(intent) // Handle single image being sent
            }
        }

        Intent.ACTION_SEND_MULTIPLE -> {
            if (intent.type?.startsWith("image/") == true) {
                handleSendMultipleImages(intent) // Handle multiple images being sent
            }
        }

        else -> {
            // Handle other intents, such as being started from the home screen
        }
    }
}

private fun handleSendText(intent: Intent) {
    intent.getStringExtra(Intent.EXTRA_TEXT)?.let {
        // Update UI state with the shared text
    }
}

private fun handleSendImage(intent: Intent) {
    val imageUri = IntentCompat.getParcelableExtra(intent, Intent.EXTRA_STREAM, Uri::class.java)
    imageUri?.let {
        // Update UI state with the shared image
    }
}

private fun handleSendMultipleImages(intent: Intent) {
    val imageUris =
        IntentCompat.getParcelableArrayListExtra(intent, Intent.EXTRA_STREAM, Uri::class.java)
    imageUris?.let {
        // Update UI state with the shared images
    }
}
```

<br />

When extracting binary data or URIs from intent extras (such as `EXTRA_STREAM`),
use [`IntentCompat.getParcelableExtra()`](https://developer.android.com/reference/androidx/core/content/IntentCompat#getparcelableextra) or
[`IntentCompat.getParcelableArrayListExtra()`](https://developer.android.com/reference/androidx/core/content/IntentCompat#getparcelablearraylistextra)
from the AndroidX Core library, as shown in the preceding `handleSendImage` and
`handleSendMultipleImages` functions. Android 13 (API level 33) deprecates the
unparameterized `Intent.getParcelableExtra(String)` method in favor of type-safe
methods that take the expected class type.

Updating the UI after receiving the data can be as straightforward as updating
state to populate a [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable), or as complex as applying a filter
to an image. It's up to your app what happens next.

#### Screenshot URL sharing

When taking a screenshot, you can share the screenshot and any associated URL.
This provides a richer user experience. When receiving a URL, make sure to get
the `EXTRA_TEXT` field from the intent, as shown in the following example:


```kotlin
IntentCompat.getParcelableExtra(intent, Intent.EXTRA_STREAM, Uri::class.java).let {
    // Handle the EXTRA_TEXT as well
    val extraText = intent.getCharSequenceExtra(Intent.EXTRA_TEXT)
    // Update UI state with the shared image and the EXTRA_TEXT if available
}
```

<br />

### Ensure users recognize your app

Your app is represented by its [icon](https://developer.android.com/guide/topics/manifest/application-element#icon) and
[label](https://developer.android.com/guide/topics/manifest/application-element#label) in the Android Sharesheet and intent resolver. These
are both defined in the manifest. You can set activity or intent filter labels
to provide more context.

As of Android 10 (API level 29), the Android Sharesheet only uses icons set in the
manifest on your `application` tag. Android ignores icons set on `intent-filter`
and `activity` tags.

> [!NOTE]
> **Note:** Effective share targets don't need a label and icon in the associated activity or intent filter. The receiving app's name and icon alone must be enough for a user to understand what happens when they share.

## Receive rich content

While `ACTION_SEND` intents enable receiving data from the Android Sharesheet
and intent resolver at the activity or navigation level, apps can also receive
rich content (such as images, videos, audio files, and styled text) through
direct UI interactions. These mechanisms include:

- Pasting from the clipboard (touch \& hold menu)
- Inserting media directly from the software keyboard (IME), such as stickers or GIFs
- Dragging and dropping content from another app in multi-window or split-screen mode

In View-based UIs, Android 12 (API level 31) and AndroidX Core 1.7 introduce the
unified [`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener) API. This
listener consolidates content handling from the clipboard, keyboard, and
drag-and-drop into a single callback. For detailed instructions on implementing
this in Views, see [Receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content).

In Jetpack Compose, you can handle receiving rich content inserted into UI
components (such as text fields) using the
[`Modifier.contentReceiver`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/content/package-summary#(androidx.compose.ui.Modifier).contentReceiver(androidx.compose.foundation.content.ReceiveContentListener)) modifier or
drag-and-drop modifiers.