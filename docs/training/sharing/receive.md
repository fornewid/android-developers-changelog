---
title: https://developer.android.com/training/sharing/receive
url: https://developer.android.com/training/sharing/receive
source: md.txt
---

Just as an app can send data to other apps, it can also receive data from other
apps as well. Think about how users interact with your application and what data
types you want to receive from other applications. For example, a social
networking application might be interested in receiving text content, like an
interesting web URL, from another app.

Users of other apps frequently send data to your app through the Android
Sharesheet or the intent resolver. Apps that send data to your app must set a
MIME type for that data. Your app can receive data sent by another app in the
following ways:

- An `Activity` with a matching `intent-filter` tag in the manifest
- Sharing Shortcuts published by your app.

Direct Share targets are deep links into a specific Activity within your app.
They often represent a person or a group, and the Android Sharesheet shows them.
For example, a messaging app can provide a Direct Share target for a person that
deep links directly into a conversation with that person. See
[Provide Direct Share targets](https://developer.android.com/training/sharing/direct-share-targets) for detailed
instructions.

## Support MIME types

Ideally, an app must be able to receive the widest possible range of MIME types.
For example, a messaging app designed for sending text, images, and video
ideally supports receiving `text/*`, `image/*` and `video/*`. Here are a few
common MIME types for sending and receiving simple data in Android.

| Receivers register for | Senders send |
|---|---|
| `text/*` | - `text/plain` - `text/rtf` - `text/html` - `text/json` |
| ```image/*``` | - `image/jpg` - `image/png` - `image/gif` |
| `video/*` | - `video/mp4` - `video/3gp` |
| Supported file extensions | `application/pdf` |

Refer to the [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) official registry of MIME media types.
| **Caution:** Although you can receive a MIME type of `*/*`, we strongly discourage doing so unless your app is fully capable of handling any type of incoming content.

## Make great share targets

When a user taps on a share target associated with a specific activity they
should be able to confirm and edit the shared content before using it. This is
especially important for text data.

## Receive data with an activity

Receiving data with an activity involves updating your manifest, handling the
incoming content, and ensuring that the user recognizes your app.

### Update your manifest

Intent filters inform the system which intents an app component accepts.
Similar to how you constructed an intent with an `ACTION_SEND` action in the
[Sending simple data to other apps](https://developer.android.com/training/sharing/send)
lesson, you create intent filters to receive intents with this action. You
define an intent filter in your manifest using the `<intent-filter>` element.
For example, if your app handles receiving text content, a manifest that
includes one or more images of any type would look like the following snippet:  

```xml
<activity android:name=".ui.MyActivity" >
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
```

When another app tries to share any of these things by constructing an
intent and passing it to [`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)), your application
is listed as an option in the Android Sharesheet or intent resolver. If the user
selects your app, this starts the corresponding activity (`.ui.MyActivity` in
the preceding example). It's then up to you to handle the content appropriately
within your code and UI.
| **Note:** For more information about intent filters and intent resolution, read [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters#ifs).

### Handle the incoming content

To handle the content delivered by an [`Intent`](https://developer.android.com/reference/android/content/Intent), call
[`getIntent()`](https://developer.android.com/reference/android/content/Intent#getIntent(java.lang.String)) to get the `Intent` object. Once you have the object,
you can examine its contents to determine what to do next. If this activity can
be started from other parts of the system (such as the launcher), take this
into consideration when examining the intent.

Take extra care to check the incoming data, you never know what some other
application may send you. For example, the wrong MIME type might be set, or the
image being sent might be extremely large. Also, remember to process binary data
in a separate thread rather than the main ("UI") thread.  

### Kotlin

    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        when {
            intent?.action == Intent.ACTION_SEND -> {
                if ("text/plain" == intent.type) {
                    handleSendText(intent) // Handle text being sent
                } else if (intent.type?.startsWith("image/") == true) {
                    handleSendImage(intent) // Handle single image being sent
                }
            }
            intent?.action == Intent.ACTION_SEND_MULTIPLE
                    && intent.type?.startsWith("image/") == true -> {
                    handleSendMultipleImages(intent) // Handle multiple images being sent
            }
            else -> {
                // Handle other intents, such as being started from the home screen
            }
        }
        ...
    }

    private fun handleSendText(intent: Intent) {
        intent.getStringExtra(Intent.EXTRA_TEXT)?.let {
            // Update UI to reflect text being shared
        }
    }

    private fun handleSendImage(intent: Intent) {
        (intent.getParcelableExtra<Parcelable>(Intent.EXTRA_STREAM) as? Uri)?.let {
            // Update UI to reflect image being shared
        }
    }

    private fun handleSendMultipleImages(intent: Intent) {
        intent.getParcelableArrayListExtra<Parcelable>(Intent.EXTRA_STREAM)?.let {
            // Update UI to reflect multiple images being shared
        }
    }

### Java

    void onCreate (Bundle savedInstanceState) {
        ...
        // Get intent, action and MIME type
        Intent intent = getIntent();
        String action = intent.getAction();
        String type = intent.getType();

        if (Intent.ACTION_SEND.equals(action) && type != null) {
            if ("text/plain".equals(type)) {
                handleSendText(intent); // Handle text being sent
            } else if (type.startsWith("image/")) {
                handleSendImage(intent); // Handle single image being sent
            }
        } else if (Intent.ACTION_SEND_MULTIPLE.equals(action) && type != null) {
            if (type.startsWith("image/")) {
                handleSendMultipleImages(intent); // Handle multiple images being sent
            }
        } else {
            // Handle other intents, such as being started from the home screen
        }
        ...
    }

    void handleSendText(Intent intent) {
        String sharedText = intent.getStringExtra(Intent.EXTRA_TEXT);
        if (sharedText != null) {
            // Update UI to reflect text being shared
        }
    }

    void handleSendImage(Intent intent) {
        Uri imageUri = (Uri) intent.getParcelableExtra(Intent.EXTRA_STREAM);
        if (imageUri != null) {
            // Update UI to reflect image being shared
        }
    }

    void handleSendMultipleImages(Intent intent) {
        ArrayList<Uri> imageUris = intent.getParcelableArrayListExtra(Intent.EXTRA_STREAM);
        if (imageUris != null) {
            // Update UI to reflect multiple images being shared
        }
    }

Updating the UI after receiving the data can be as simple as populating an
[`EditText`](https://developer.android.com/reference/android/widget/EditText), or it can be more
complicated like applying an interesting photo filter to an image. It's up to
your app what happens next.

#### Screenshot URL sharing

When taking a screenshot, you can share the screenshot and any associated URL.
This provides a richer user experience. When receiving a URL make sure to get
the `EXTRA_TEXT` field from the intent, as shown in the following example:  

    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        when {
            intent?.action == Intent.ACTION_SEND -> {
                if (intent.type?.startsWith("image/") == true) {
                    handleSendImage(intent)
                }
             }
        ...
    }
    private fun handleSendImage(intent: Intent) {
        (intent.getParcelableExtra<Parcelable>(Intent.EXTRA_STREAM) as? Uri)?.let {
         // Handle the EXTRA_TEXT as well
         intent.getCharSequenceExtra(Intent.EXTRA_TEXT)
        // Update UI to reflect image being shared and the EXTRA_TEXT
        // if available
        }
    }
    ...
    }

### Ensure users recognize your app

Your app is represented by its
[icon](https://developer.android.com/guide/topics/manifest/application-element#icon) and
[label](https://developer.android.com/guide/topics/manifest/application-element#label) in the Android
Sharesheet and intent resolver. These are both defined in the manifest. You can
set activity or intent filter labels to provide more context.

As of Android 10 (API level 29), the Android Sharesheet only uses icons set in
the manifest on your `application` tag. Android ignores icons set on
`intent-filter` and `activity` tags.
| **Note:** Effective share targets don't need a label and icon in the associated activity or intent filter. The receiving app's name and icon alone must be enough for a user to understand what happens when they share.