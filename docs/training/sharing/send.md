---
title: https://developer.android.com/training/sharing/send
url: https://developer.android.com/training/sharing/send
source: md.txt
---

Android uses intents and their associated extras to let users share information quickly and
easily using their favorite apps.

Android provides two ways for users to share data between apps:

- The Android Sharesheet is primarily designed for sending content outside your app and/or directly to another user. For example, sharing a URL with a friend.
- The Android intent resolver is best suited for passing data to the next stage of a well-defined task. For example, opening a PDF from your app and letting users pick their preferred viewer.

When you construct an intent, you specify the action you want the intent to perform.
Android uses the action [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)
to send data from one activity to another,
even across process boundaries. You need to specify
the data and its type. The system automatically identifies the compatible activities
that can receive the data and displays them to the user. In the case of the intent resolver,
if only one activity can handle the intent, that activity immediately starts.

## Why use the Android Sharesheet

![](https://developer.android.com/static/images/training/sharing/sharesheet.png)

We strongly recommend using the Android Sharesheet to create consistency for your users across
apps. Don't display your app's own list of share targets or create your own
Sharesheet variations.

The Android Sharesheet lets users share information with the
right person, with relevant app suggestions, all with a single tap.
The Sharesheet can suggest targets unavailable to custom solutions and uses a consistent ranking.
This is because the Sharesheet can take into account information about app and user activity
that is only available to the system.

The Android Sharesheet also has many handy features for developers. For example, you can
do the following:

- [Find out when your users complete a share and to where](https://developer.android.com/training/sharing/send#share-interaction-data)
- [Add a custom `ChooserTarget` and app targets](https://developer.android.com/training/sharing/send#adding-custom-targets)
- [Provide rich text content previews, starting in Android 10 (API level 29)](https://developer.android.com/training/sharing/send#adding-rich-content-previews)
- [Exclude targets matching specific component names](https://developer.android.com/training/sharing/send#excluding-specific-targets-by-component)

## Use the Android Sharesheet

For all types of sharing, create an intent and set its action to
[Intent.ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND).
To display the Android Sharesheet, call
[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent, java.lang.CharSequence)),
passing it your [Intent](https://developer.android.com/reference/android/content/Intent) object.
It returns a version of your intent that always displays the Android Sharesheet.

### Send text content

The most straightforward and common use of the Android Sharesheet is to send text content from
one activity to another. For example, most browsers can share the URL of the currently displayed
page as text with another app. This is useful for sharing an article or website with friends through
email or social networking. Here's an example of how to do this:  

### Kotlin

```kotlin
val sendIntent: Intent = Intent().apply {
    action = Intent.ACTION_SEND
    putExtra(Intent.EXTRA_TEXT, "This is my text to send.")
    type = "text/plain"
}

val shareIntent = Intent.createChooser(sendIntent, null)
startActivity(shareIntent)
```

### Java

```java
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.putExtra(Intent.EXTRA_TEXT, "This is my text to send.");
sendIntent.setType("text/plain");

Intent shareIntent = Intent.createChooser(sendIntent, null);
startActivity(shareIntent);
```

Optionally, you can add extras to include more information, such as email recipients
([EXTRA_EMAIL](https://developer.android.com/reference/android/content/Intent#EXTRA_EMAIL),
[EXTRA_CC](https://developer.android.com/reference/android/content/Intent#EXTRA_CC),
[EXTRA_BCC](https://developer.android.com/reference/android/content/Intent#EXTRA_BCC)),
the email subject
([EXTRA_SUBJECT](https://developer.android.com/reference/android/content/Intent#EXTRA_SUBJECT)), etc.

**Note:** Some email apps, such as Gmail, expect a
[String[]](https://developer.android.com/reference/java/lang/String) for extras like
`EXTRA_EMAIL` and `EXTRA_CC`. Use
[putExtra(String, String[])](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String, java.lang.String[]))
to add these to your intent.

### Send binary content

Share binary data using the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) action.
Set the appropriate MIME type and place a URI to the data in the extra
[EXTRA_STREAM](https://developer.android.com/reference/android/content/Intent#EXTRA_STREAM), as
shown in the following example.
This is commonly used to share an image but can be used to share any type of binary content.  

### Kotlin

```kotlin
val shareIntent: Intent = Intent().apply {
    action = Intent.ACTION_SEND
    // Example: content://com.google.android.apps.photos.contentprovider/...
    putExtra(Intent.EXTRA_STREAM, uriToImage)
    type = "image/jpeg"
}
startActivity(Intent.createChooser(shareIntent, null))
```

### Java

```java
Intent shareIntent = new Intent();
shareIntent.setAction(Intent.ACTION_SEND);
// Example: content://com.google.android.apps.photos.contentprovider/...
shareIntent.putExtra(Intent.EXTRA_STREAM, uriToImage);
shareIntent.setType("image/jpeg");
startActivity(Intent.createChooser(shareIntent, null));
```

The receiving application needs permission to access the data the [Uri](https://developer.android.com/reference/android/net/Uri)
points to. There are two recommended ways to do this:

- Store the data in your own [ContentProvider](https://developer.android.com/reference/android/content/ContentProvider), making sure that other apps have the correct permission to access your provider. The preferred mechanism for providing access is to use [per-URI permissions](https://developer.android.com/training/permissions/restrict-interactions#uri), which are temporary and only grant access to the receiving application. An easy way to create a `ContentProvider` like this is to use the [FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider) helper class.
- Use the system [MediaStore](https://developer.android.com/reference/android/provider/MediaStore). The `MediaStore` is primarily for video, audio, and image MIME types. However, beginning with Android 3.0 (API level 11), it can also store non-media types. For more information, see [MediaStore.Files](https://developer.android.com/reference/android/provider/MediaStore.Files). Files can be inserted into the `MediaStore` using [scanFile()](https://developer.android.com/reference/android/media/MediaScannerConnection#scanFile(android.content.Context, java.lang.String[], java.lang.String[], android.media.MediaScannerConnection.OnScanCompletedListener)), after which a `content://`-style [Uri](https://developer.android.com/reference/android/net/Uri) suitable for sharing is passed to the provided [onScanCompleted()](https://developer.android.com/reference/android/media/MediaScannerConnection.OnScanCompletedListener#onScanCompleted(java.lang.String, android.net.Uri)) callback. Note that once added to the system `MediaStore`, the content is accessible to any app on the device.

### Use the right MIME type

Provide the most specific MIME type available for the data you're
sending. For example, use `text/plain` when sharing plain text. Here are a few
common MIME types when sending simple data in Android:

| Receivers register for | Senders send |
|---|---|
| `text/*` | - `text/plain` - `text/rtf` - `text/html` - `text/json` |
| ```image/*``` | - `image/jpg` - `image/png` - `image/gif` |
| `video/*` | - `video/mp4` - `video/3gp` |
| Supported file extensions | `application/pdf` |

| **Caution:** Although you can use a MIME type of `*/*`, we strongly discourage doing so because most receiving apps aren't able to receive any kind of content. Ideally, your app must match activities that can handle generic data streams.

For more information about MIME types, see the
[IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)
official registry of MIME media types.

The Android Sharesheet might show a content preview, depending on the provided MIME type. Some
preview features are only available for specific types.

### Share multiple pieces of content

To share multiple pieces of content, use the [ACTION_SEND_MULTIPLE](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE)
action together with a list of URIs pointing to the content. The MIME type varies according to the
mix of content you're sharing. For example, if you share three JPEG images, you use the type
`"image/jpg"`. For a mixture of image types, use `"image/*"` to match an
activity that handles any type of image. While it's possible to share a mix of types, we highly
discourage this, because it's
unclear to the receiver what is intended to be sent. If it's necessary to send multiple types, use
`"*/*"`. It's up to the receiving application to parse
and process your data. Here's an example:  

### Kotlin

```kotlin
val imageUris: ArrayList<Uri> = arrayListOf(
        // Add your image URIs here
        imageUri1,
        imageUri2
)

val shareIntent = Intent().apply {
    action = Intent.ACTION_SEND_MULTIPLE
    putParcelableArrayListExtra(Intent.EXTRA_STREAM, imageUris)
    type = "image/*"
}
startActivity(Intent.createChooser(shareIntent, null))
```

### Java

```java
ArrayList<Uri> imageUris = new ArrayList<Uri>();
imageUris.add(imageUri1); // Add your image URIs here
imageUris.add(imageUri2);

Intent shareIntent = new Intent();
shareIntent.setAction(Intent.ACTION_SEND_MULTIPLE);
shareIntent.putParcelableArrayListExtra(Intent.EXTRA_STREAM, imageUris);
shareIntent.setType("image/*");
startActivity(Intent.createChooser(shareIntent, null));
```

Be sure the provided [Uri](https://developer.android.com/reference/android/net/Uri) objects point
to data that a receiving application can access.

### Add rich content to text previews

Starting in Android 10 (API level 29), the Android Sharesheet shows a preview of text being
shared. In some cases, text that's being shared can be hard to understand. Consider sharing a
complicated URL like `https://www.google.com/search?ei=2rRVXcLkJajM0PEPoLy7oA4`. A richer
preview can reassure your users what is being shared.

If you are previewing text, you can set a title, a thumbnail image, or both. Add a description to
`Intent.EXTRA_TITLE` before calling `Intent.createChooser()`, and add a
relevant thumbnail using `ClipData`.

**Note:** The image content URI is provided from a
`FileProvider`, usually from a configured `<cache-path>`.
For more information, see [Sharing files](https://developer.android.com/training/secure-file-sharing). Be sure to give
Sharesheet the right permissions to read any image you want use as a thumbnail. For more information,
see [Intent.FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION).

Here's an example:  

### Kotlin

```kotlin
 val share = Intent.createChooser(Intent().apply {
      action = Intent.ACTION_SEND
      putExtra(Intent.EXTRA_TEXT, "https://developer.android.com/training/sharing/")

      // (Optional) Here you're setting the title of the content
      putExtra(Intent.EXTRA_TITLE, "Introducing content previews")

      // (Optional) Here you're passing a content URI to an image to be displayed
      data = contentUri
      flags = Intent.FLAG_GRANT_READ_URI_PERMISSION
  }, null)
  startActivity(share)
```

### Java

```java
Intent sendIntent = new Intent(Intent.ACTION_SEND);
sendIntent.putExtra(Intent.EXTRA_TEXT, "https://developer.android.com/training/sharing/");

// (Optional) Here you're setting the title of the content
sendIntent.putExtra(Intent.EXTRA_TITLE, "Introducing content previews");

// (Optional) Here you're passing a content URI to an image to be displayed
sendIntent.setData(contentUri);
sendIntent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);

// Show the Sharesheet
startActivity(Intent.createChooser(sendIntent, null));
```

The preview looks something like this:  
![](https://developer.android.com/static/images/training/sharing/sharing_content_preview.png)

### Add custom actions to the sharesheet

![](https://developer.android.com/static/images/training/sharing/sharesheet_custom_actions.png)

Screenshot of custom actions on the Android Sharesheet.

On Android 14 (API Level 34) and above, apps can add custom actions to the Android Sharesheet.
The custom actions are shown as small action icons at the top of the Android Sharesheet, and apps
can specify any `Intent` as the action invoked when the icon is clicked.

To add custom actions on the Android Sharesheet, first create a
[ChooserAction](https://developer.android.com/reference/android/service/chooser/ChooserAction)
with
[ChooserAction.Builder](https://developer.android.com/training/sharing/reference/android/service/chooser/ChooserAction.Builder).
You can specify a `PendingIntent` as the action invoked when the icon is clicked. Create
an array containing all of your custom actions and specify it as
[EXTRA_CHOOSER_CUSTOM_ACTIONS](https://developer.android.com/reference/android/content/Intent#EXTRA_CHOOSER_CUSTOM_ACTIONS)
of the share `Intent`.  

### Kotlin

```kotlin
val sendIntent = Intent(Intent.ACTION_SEND)
    .setType("text/plain")
    .putExtra(Intent.EXTRA_TEXT, text)
val shareIntent = Intent.createChooser(sendIntent, null)
val customActions = arrayOf(
    ChooserAction.Builder(
        Icon.createWithResource(context, R.drawable.ic_custom_action),
        "Custom",
        PendingIntent.getBroadcast(
            context,
            1,
            Intent(Intent.ACTION_VIEW),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_CANCEL_CURRENT
        )
    ).build()
)
shareIntent.putExtra(Intent.EXTRA_CHOOSER_CUSTOM_ACTIONS, customActions)
context.startActivity(shareIntent)
```

### Java

```java
Intent sendIntent = new Intent(Intent.ACTION_SEND)
        .setType("text.plain")
        .putExtra(Intent.EXTRA_TEXT, text);
Intent shareIntent = Intent.createChooser(sendIntent, null);
ChooserAction[] actions = new ChooserAction[]{
        new ChooserAction.Builder(
                Icon.createWithResource(context, R.drawable.ic_custom_action),
                "Custom",
                PendingIntent.getBroadcast(
                        context,
                        1,
                        new Intent(Intent.ACTION_VIEW),
                        PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_CANCEL_CURRENT
                )
        ).build()
};
shareIntent.putExtra(Intent.EXTRA_CHOOSER_CUSTOM_ACTIONS, actions);
context.startActivity(shareIntent);
```

### Add custom targets

The Android Sharesheet lets you specify up to two [ChooserTarget](https://developer.android.com/reference/android/service/chooser/ChooserTarget) objects that
are shown before the sharing shortcuts and chooser targets loaded from `ChooserTargetServices`. You can also
specify up to two intents pointing to activities that are listed
before the app suggestions:
![](https://developer.android.com/static/images/training/sharing/customshare.png)

Add `Intent.EXTRA_CHOOSER_TARGETS` and `Intent.EXTRA_INITIAL_INTENTS` to
your share Intent *after* calling
[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent,%20java.lang.CharSequence)):  

### Kotlin

```kotlin
val share = Intent.createChooser(myShareIntent, null).apply {
    putExtra(Intent.EXTRA_CHOOSER_TARGETS, myChooserTargetArray)
    putExtra(Intent.EXTRA_INITIAL_INTENTS, myInitialIntentArray)
}
```

### Java

```java
Intent shareIntent = Intent.createChooser(sendIntent, null);
share.putExtra(Intent.EXTRA_CHOOSER_TARGETS, myChooserTargetArray);
share.putExtra(Intent.EXTRA_INITIAL_INTENTS, myInitialIntentArray);
```

Use this feature with care. Every custom `Intent`
and `ChooserTarget` that you add reduces the number the system suggests. We generally
discourage adding custom targets. A common appropriate example of adding
`Intent.EXTRA_INITIAL_INTENTS` is to provide additional actions users can take on shared
content. For example, a user shares images and `Intent.EXTRA_INITIAL_INTENTS` is used to
let them send a link instead. A common appropriate example of adding `Intent.EXTRA_CHOOSER_TARGETS`
is to surface relevant people or devices that your app provides.

### Exclude specific targets by component

You can exclude specific targets by providing `Intent.EXTRA_EXCLUDE_COMPONENTS`.
Only do this to remove targets you have control over. A common use case is to hide your
app's share targets when your users share from within your app, as their intent is likely to share
outside your app.

Add `Intent.EXTRA_EXCLUDE_COMPONENTS` to your intent after calling `Intent.createChooser()`:  

### Kotlin

```kotlin
  val share = Intent.createChooser(Intent(), null).apply {
    // Only use for components you have control over
    val excludedComponentNames = arrayOf(ComponentName("com.example.android", "ExampleClass"))
    putExtra(Intent.EXTRA_EXCLUDE_COMPONENTS, excludedComponentNames)
  }
```

### Java

```java
  Intent shareIntent = Intent.createChooser(new Intent(), null);
  // Only use for components you have control over
  ComponentName[] excludedComponentNames = {
          new ComponentName("com.example.android", "ExampleClass")
  };
  shareIntent.putExtra(Intent.EXTRA_EXCLUDE_COMPONENTS, excludedComponentNames);
```

### Get information about sharing

It can be useful to know when your users are sharing and what target they select. The
Android Sharesheet lets you get this information by providing the `ComponentName` of
targets your users select using an `IntentSender`.

First create a `PendingIntent` for a `BroadcastReceiver` and supply its
`IntentSender` in `Intent.createChooser()`:  

### Kotlin

```kotlin
var share = Intent(Intent.ACTION_SEND)
// ...
val pi = PendingIntent.getBroadcast(
    myContext, requestCode,
    Intent(myContext, MyBroadcastReceiver::class.java),
    PendingIntent.FLAG_MUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
share = Intent.createChooser(share, null, pi.intentSender)
```

### Java

```java
Intent share = new Intent(ACTION_SEND);
...
PendingIntent pi = PendingIntent.getBroadcast(myContext, requestCode,
        new Intent(myContext, MyBroadcastReceiver.class),
        PendingIntent.FLAG_MUTABLE | PendingIntent.FLAG_UPDATE_CURRENT);
share = Intent.createChooser(share, null, pi.getIntentSender());
```

Receive the callback in `MyBroadcastReceiver` and look in
`Intent.EXTRA_CHOOSER_RESULT`:  

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
  ...
  val chooserResult: ChooserResult? = IntentCompat.getParcelableExtra(
      intent,
      Intent.EXTRA_CHOOSER_RESULT,
      ChooserResult::class.java,
  )
  chooserResult?.let {
      Log.i(
          TAG,
          "Share callback: isShortcut: ${it.isShortcut}, type: ${typeToString(it.type)}, componentName: ${it.selectedComponent}",
      )
  } ?: Log.i(TAG, "chooserResult is null")
}
```

### Java

```java
@Override public void onReceive(Context context, Intent intent) {
  ...
  ChooserResult chooserResult = intent.getParcelableExtra(EXTRA_CHOOSER_RESULT);
  Log.i(
      TAG,
      "Share callback: isShortcut: "
          + chooserResult.isShortcut()
          + ", type: "
          + chooserResult.getType()
          + ", componentName: "
          + chooserResult.getSelectedComponent()
  );
}
```
See the [platform share sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/share) for more information:

### Add custom actions to the sharesheet

On Android 14 (API Level 34) and above, apps can add custom actions to the Android Sharesheet.
Create a [ChooserAction](https://developer.android.com/reference/android/service/chooser/ChooserAction)
with
[ChooserAction.Builder](https://developer.android.com/training/sharing/reference/android/service/chooser/ChooserAction.Builder).
You can specify a `PendingIntent` as the action invoked when the icon is clicked. Create
an array containing all of your custom actions and specify it as
[EXTRA_CHOOSER_CUSTOM_ACTIONS](https://developer.android.com/reference/android/content/Intent#EXTRA_CHOOSER_CUSTOM_ACTIONS)
of the share `Intent`.  

### Kotlin

```kotlin
val sendIntent = Intent(Intent.ACTION_SEND)
    .setType("text/plain")
    .putExtra(Intent.EXTRA_TEXT, text)
val shareIntent = Intent.createChooser(sendIntent, null)
val customActions = arrayOf(
    ChooserAction.Builder(
        Icon.createWithResource(context, R.drawable.ic_custom_action),
        "Custom",
        PendingIntent.getBroadcast(
            context,
            1,
            Intent(Intent.ACTION_VIEW),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_CANCEL_CURRENT
        )
    ).build()
)
shareIntent.putExtra(Intent.EXTRA_CHOOSER_CUSTOM_ACTIONS, customActions)
context.startActivity(shareIntent)
```

### Java

```java
Intent sendIntent = new Intent(Intent.ACTION_SEND)
        .setType("text.plain")
        .putExtra(Intent.EXTRA_TEXT, text);
Intent shareIntent = Intent.createChooser(sendIntent, null);
ChooserAction[] actions = new ChooserAction[]{
        new ChooserAction.Builder(
                Icon.createWithResource(context, R.drawable.ic_custom_action),
                "Custom",
                PendingIntent.getBroadcast(
                        context,
                        1,
                        new Intent(Intent.ACTION_VIEW),
                        PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_CANCEL_CURRENT
                )
        ).build()
};
shareIntent.putExtra(Intent.EXTRA_CHOOSER_CUSTOM_ACTIONS, actions);
context.startActivity(shareIntent);
```

## Use the Android intent resolver

![](https://developer.android.com/static/images/training/sharing/send_intent.png)

Screenshot of [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) intent resolver.

The Android intent resolver is best used when sending data to another app as part of a well-defined task flow.

To use the Android intent resolver, create an intent and add extras as you would to call
the Android Sharesheet. However, *don't* call
[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent, java.lang.CharSequence)).

If there are multiple installed applications with filters that match
[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)
and the MIME type, the system displays a disambiguation dialog called the *intent resolver*
that lets the user choose a target to share to. If a single application
matches, it runs.

Here is an example of how to use the Android intent resolver to send text:  

### Kotlin

```kotlin
val sendIntent: Intent = Intent().apply {
    action = Intent.ACTION_SEND
    putExtra(Intent.EXTRA_TEXT, "This is my text to send.")
    type = "text/plain"
}
startActivity(sendIntent)
```

### Java

```java
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.putExtra(Intent.EXTRA_TEXT, "This is my text to send.");
sendIntent.setType("text/plain");
startActivity(sendIntent);
```

## Learn more

For more information about sending data, see
[Intents and Intent Filters.](https://developer.android.com/guide/components/intents-filters)