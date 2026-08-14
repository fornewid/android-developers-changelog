---
title: https://developer.android.com/develop/ui/views/touch-and-input/copy-paste
url: https://developer.android.com/develop/ui/views/touch-and-input/copy-paste
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use copy and paste in Compose. [Copy and paste →](https://developer.android.com/develop/ui/compose/touch-input/copy-and-paste) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Android provides a powerful clipboard-based framework for copying and pasting. It supports simple
and complex data types, including text strings, complex data structures, text and binary stream
data, and application assets. Simple text data is stored directly in the clipboard, while complex
data is stored as a reference that the pasting application resolves with a content provider. Copying
and pasting works both within an application and between applications that implement the
framework.

Since part of the framework uses content providers, this document assumes some familiarity with
the Android Content Provider API, which is described in
[Content providers](https://developer.android.com/guide/topics/providers/content-providers).

Users expect feedback when copying content to the clipboard, so in addition to the framework that
powers copy and paste, Android shows a default UI to users when copying in Android 13 (API level 33)
and higher. Due to this feature, there is a risk of duplicate notification. You can learn more about
this edge case the in the
[Avoid duplicate notifications](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#duplicate-notifications)
section.
![An animation showing Android 13 clipboard notification](https://developer.android.com/static/images/about/versions/13/new-copy-paste-UI.gif) **Figure 1.** UI shown when content enters the clipboard in Android 13 and up.

Manually provide feedback to users when copying in Android 12L (API level 32) and lower. See
[recommendations for this](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Feedback) in this document.

## The clipboard framework

When you use the clipboard framework, put data into a clip object, and then put the clip object
on the system-wide clipboard. The clip object can take one of three forms:

Text
:
    A text string. Put the string directly in the clip object, which you then put on the
    clipboard. To paste the string, get the clip object from the clipboard and copy the
    string into your application's storage.

URI
:
    A `https://developer.android.com/reference/android/net/Uri` object representing any
    form of URI. This is primarily for copying complex data from a content provider. To copy
    data, put a `Uri` object into a clip object and put the clip object onto the
    clipboard. To paste the data, get the clip object, get the `Uri` object,
    resolve it to a data source, such as a content provider, and copy the data from the
    source into your application's storage.

Intent
:
    An `https://developer.android.com/reference/android/content/Intent`. This
    supports copying application shortcuts. To copy data, create an `Intent`, put
    it in a clip object, and put the clip object on the clipboard. To paste the data, get
    the clip object and then copy the `Intent` object into your application's
    memory area.

The clipboard holds only one clip object at a time. When an application puts a clip object on the
clipboard, the previous clip object disappears.

If you want to let users paste data into your application, you don't have to handle all types of
data. You can examine the data on the clipboard before you give users the option to paste it.
Besides having a certain data form, the clip object also contains metadata that tells you what MIME
types are available. This metadata helps you decide whether your application can do something useful
with the clipboard data. For example, if you have an application that primarily handles text, you
might want to ignore clip objects that contain a URI or intent.

You might also want to let users paste text regardless of the form of data on the clipboard. To
do this, force the clipboard data into a text representation, and then paste this text. This is
described in the [Coerce the clipboard to text](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#CoerceToText) section.

## Clipboard classes

This section describes the classes used by the clipboard framework.

### ClipboardManager

The Android system clipboard is represented by the global
`https://developer.android.com/reference/android/content/ClipboardManager` class.
Don't instantiate this class directly. Instead, get a reference to it by invoking
`https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String)`.

### ClipData, ClipData.Item, and ClipDescription

To add data to the clipboard, create a
`https://developer.android.com/reference/android/content/ClipData` object that contains
a description of the data and the data itself. The clipboard holds one `ClipData` at a
time. A `ClipData` contains a
`https://developer.android.com/reference/android/content/ClipDescription` object
and one or more
`https://developer.android.com/reference/android/content/ClipData.Item` objects.

A `ClipDescription` object contains metadata about the clip. In particular, it
contains an array of available MIME types for the clip's data. Additionally, on
Android 12 (API level 31) and higher, the metadata includes information about whether the object
contains
[stylized text](https://developer.android.com/reference/android/content/ClipDescription#isStyledText()) and about the
[type of text in the object](https://developer.android.com/reference/android/content/ClipDescription#getConfidenceScore(java.lang.String)).
When you put a clip on the clipboard, this information is available to pasting applications, which
can examine whether they can handle the clip data.

A `ClipData.Item` object contains the text, URI, or intent data:

Text
:
    A `https://developer.android.com/reference/java/lang/CharSequence`.

URI
:
    A `Uri`. This usually contains a content provider URI, although any URI is
    allowed. The application that provides the data puts the URI on the clipboard. Applications
    that want to paste the data get the URI from the clipboard and use it to access the content
    provider or other data source and retrieve the data.

Intent
:
    An `Intent`. This data type lets you copy an application shortcut to the
    clipboard. Users can then paste the shortcut into their applications for later use.

You can add more than one `ClipData.Item` object to a clip. This lets users copy and
paste multiple selections as a single clip. For example, if you have a list widget that lets the
user select more than one item at a time, you can copy all the items to the clipboard at once. To do
this, create a separate `ClipData.Item` for each list item, and then add the
`ClipData.Item` objects to the `ClipData` object.

### ClipData convenience methods

The `ClipData` class provides static convenience methods for creating a
`ClipData` object with a single `ClipData.Item` object and a simple
`ClipDescription` object:


`https://developer.android.com/reference/android/content/ClipData#newPlainText(java.lang.CharSequence, java.lang.CharSequence)`
:   Returns a `ClipData` object whose single `ClipData.Item` object
    contains a text string. The `ClipDescription` object's label is set to
    `label`. The single MIME type in `ClipDescription` is
    `https://developer.android.com/reference/android/content/ClipDescription#MIMETYPE_TEXT_PLAIN`.

    Use `newPlainText()` to create a clip from a text string.


`https://developer.android.com/reference/android/content/ClipData#newUri(android.content.ContentResolver, java.lang.CharSequence, android.net.Uri)`
:   Returns a `ClipData` object whose single `ClipData.Item` object
    contains a URI. The `ClipDescription` object's label is set to
    `label`. If the URI is a content URI---that is, if
    `https://developer.android.com/reference/android/net/Uri#getScheme()`
    returns `content:`---the method uses the
    `https://developer.android.com/reference/android/content/ContentResolver`
    object provided in `resolver` to retrieve the available MIME types from the
    content provider. It then stores them in `ClipDescription`. For a URI that isn't
    a `content:` URI, the method sets the MIME type to
    `https://developer.android.com/reference/android/content/ClipDescription#MIMETYPE_TEXT_URILIST`.

    Use `newUri()` to create a clip from a URI---particularly a
    `content:` URI.


`https://developer.android.com/reference/android/content/ClipData#newIntent(java.lang.CharSequence, android.content.Intent)`
:   Returns a `ClipData` object whose single `ClipData.Item` object
    contains an `Intent`. The `ClipDescription` object's label is set to
    `label`. The MIME type is set to
    `https://developer.android.com/reference/android/content/ClipDescription#MIMETYPE_TEXT_INTENT`.

    Use `newIntent()` to create a clip from an `Intent` object.

### Coerce the clipboard data to text

Even if your application only handles text, you can copy non-text data from the clipboard by
converting it with the
`https://developer.android.com/reference/android/content/ClipData.Item#coerceToText(android.content.Context)`
method.

This method converts the data in `ClipData.Item` to text and returns a
`CharSequence`. The value that `ClipData.Item.coerceToText()` returns is based
on the form of data in `ClipData.Item`:

Text
:
    If `ClipData.Item` is text---that is, if
    `https://developer.android.com/reference/android/content/ClipData.Item#getText()`
    isn't null---coerceToText() returns the text.

URI
:
    If `ClipData.Item` is a URI---that is, if
    `https://developer.android.com/reference/android/content/ClipData.Item#getUri()`
    isn't null---`coerceToText()` tries to use it as a content URI.

    - If the URI is a content URI and the provider can return a text stream, `coerceToText()` returns a text stream.
    - If the URI is a content URI but the provider doesn't offer a text stream, `coerceToText()` returns a representation of the URI. The representation is the same as that returned by `https://developer.android.com/reference/android/net/Uri#toString()`.
    - If the URI isn't a content URI, `coerceToText()` returns a representation of the URI. The representation is the same as that returned by `Uri.toString()`.

Intent
:   If `ClipData.Item` is an `Intent`---that is, if
    `https://developer.android.com/reference/android/content/ClipData.Item#getIntent()`
    isn't null---`coerceToText()` converts it to an Intent URI and returns it.
    The representation is the same as that returned by
    `https://developer.android.com/reference/android/content/Intent#toUri(int)`.

The clipboard framework is summarized in figure 2. To copy data, an application puts a
`ClipData` object on the `ClipboardManager` global clipboard. The
`ClipData` contains one or more `ClipData.Item` objects and one
`ClipDescription` object. To paste data, an application gets the `ClipData`,
gets its MIME type from the `ClipDescription`, and gets the data from the
`ClipData.Item` or from the content provider referred to by
`ClipData.Item`.
![An image showing a block diagram of the copy and paste framework](https://developer.android.com/static/images/ui/clipboard/copy_paste_framework.png) **Figure 2.** The Android clipboard framework.

## Copy to the clipboard

To copy data to the clipboard, get a handle to the global `ClipboardManager` object,
create a `ClipData` object, and add a `ClipDescription` and one or more
`ClipData.Item` objects to it. Then, add the finished `ClipData` object to the
`ClipboardManager` object. This is described further in the following procedure:

1. If you are copying data using a content URI, set up a content provider.
2. Get the system clipboard:

   ### Kotlin

   ```kotlin
   when(menuItem.itemId) {
       ...
       R.id.menu_copy -> { // if the user selects copy
           // Gets a handle to the clipboard service.
           val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
       }
   }
   ```

   ### Java

   ```java
   ...
   // If the user selects copy.
   case R.id.menu_copy:

   // Gets a handle to the clipboard service.
   ClipboardManager clipboard = (ClipboardManager)
           getSystemService(Context.CLIPBOARD_SERVICE);
   ```
3.
   Copy the data to a new `ClipData` object:

   - **For text**

     ### Kotlin

     ```kotlin
     // Creates a new text clip to put on the clipboard.
     val clip: ClipData = ClipData.newPlainText("simple text", "Hello, World!")
     ```

     ### Java

     ```java
     // Creates a new text clip to put on the clipboard.
     ClipData clip = ClipData.newPlainText("simple text", "Hello, World!");
     ```
   - **For a URI**

     This snippet constructs a URI by encoding a record ID onto the content URI for
     the provider. This technique is covered in more detail in the
     [Encoding an identifier on the URI](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Encoding) section.

     ### Kotlin

     ```kotlin
     // Creates a Uri using a base Uri and a record ID based on the contact's last
     // name. Declares the base URI string.
     const val CONTACTS = "content://com.example.contacts"

     // Declares a path string for URIs, used to copy data.
     const val COPY_PATH = "/copy"

     // Declares the Uri to paste to the clipboard.
     val copyUri: Uri = Uri.parse("$CONTACTS$COPY_PATH/$lastName")
     ...
     // Creates a new URI clip object. The system uses the anonymous
     // getContentResolver() object to get MIME types from provider. The clip object's
     // label is "URI", and its data is the Uri previously created.
     val clip: ClipData = ClipData.newUri(contentResolver, "URI", copyUri)
     ```

     ### Java

     ```java
     // Creates a Uri using a base Uri and a record ID based on the contact's last
     // name. Declares the base URI string.
     private static final String CONTACTS = "content://com.example.contacts";

     // Declares a path string for URIs, used to copy data.
     private static final String COPY_PATH = "/copy";

     // Declares the Uri to paste to the clipboard.
     Uri copyUri = Uri.parse(CONTACTS + COPY_PATH + "/" + lastName);
     ...
     // Creates a new URI clip object. The system uses the anonymous
     // getContentResolver() object to get MIME types from provider. The clip object's
     // label is "URI", and its data is the Uri previously created.
     ClipData clip = ClipData.newUri(getContentResolver(), "URI", copyUri);
     ```
   - **For an intent**

     This snippet constructs an `Intent` for an application and then puts
     it in the clip object:

     ### Kotlin

     ```kotlin
     // Creates the Intent.
     val appIntent = Intent(this, com.example.demo.myapplication::class.java)
     ...
     // Creates a clip object with the Intent in it. Its label is "Intent"
     // and its data is the Intent object created previously.
     val clip: ClipData = ClipData.newIntent("Intent", appIntent)
     ```

     ### Java

     ```java
     // Creates the Intent.
     Intent appIntent = new Intent(this, com.example.demo.myapplication.class);
     ...
     // Creates a clip object with the Intent in it. Its label is "Intent"
     // and its data is the Intent object created previously.
     ClipData clip = ClipData.newIntent("Intent", appIntent);
     ```
4. Put the new clip object on the clipboard:

   ### Kotlin

   ```kotlin
   // Set the clipboard's primary clip.
   clipboard.setPrimaryClip(clip)
   ```

   ### Java

   ```java
   // Set the clipboard's primary clip.
   clipboard.setPrimaryClip(clip);
   ```

### Provide feedback when copying to the clipboard

Users expect visual feedback when an app copies content to the clipboard. This is done
automatically for users in Android 13 and higher, but it must be manually implemented in prior
versions.

Starting in Android 13, the system displays a standard visual confirmation when content is added
to the clipboard. The new confirmation does the following:

- Confirms the content was successfully copied.
- Provides a preview of the copied content.

<br />

![An animation showing Android 13 clipboard notification](https://developer.android.com/static/images/about/versions/13/new-copy-paste-UI.gif) **Figure 3.** UI shown when content enters the clipboard in Android 13 and up.

In Android 12L (API level 32) and lower, users might be unsure whether they successfully copied
content or what they copied. This feature standardizes the various notifications shown by apps after
copying and offers users more control over the clipboard.

### Avoid duplicate notifications

In Android 12L (API level 32) and lower, we recommend alerting users when they successfully copy
by issuing visual, in-app feedback, using a widget like a `Toast` or
a `Snackbar`, after copying.

To avoid duplicate displays of information, we strongly recommend removing toasts
or snackbars shown after an in-app copy for Android 13 and higher.
![Post snackbar after an in-app copy.](https://developer.android.com/static/images/about/versions/13/snackbar-overlap.png) **Figure 4.** If you show a copy confirmation snackbar in Android 13, the user sees duplicate messages. ![Post toast after an in-app copy.](https://developer.android.com/static/images/about/versions/13/toast-overlap.png) **Figure 5.** If you show a copy confirmation toast in Android 13, the user sees duplicate messages.


Here's an example of how to implement this:

```kotlin
fun textCopyThenPost(textCopied:String) {
    val clipboardManager = getSystemService(CLIPBOARD_SERVICE) as ClipboardManager
    // When setting the clipboard text.
    clipboardManager.setPrimaryClip(ClipData.newPlainText   ("", textCopied))
    // Only show a toast for Android 12 and lower.
    if (Build.VERSION.SDK_INT <= Build.VERSION_CODES.S_V2)
        Toast.makeText(context, "Copied", Toast.LENGTH_SHORT).show()
}
```

### Add sensitive content to the clipboard

If your app lets users copy sensitive content to the clipboard, such as passwords or credit
card information, you must add a flag to `ClipDescription` in `ClipData`
before calling `ClipboardManager.setPrimaryClip()`. Adding this flag prevents sensitive
content from appearing in the visual confirmation of copied content in Android 13 and higher.
![Copied text preview without flagging sensitive content](https://developer.android.com/static/images/about/versions/13/sensitive-content-before.png) **Figure 6.** Copied text preview without a sensitive content flag. ![Copied text preview flagging sensitive content.](https://developer.android.com/static/images/about/versions/13/sensitive-content-after.png) **Figure 7.** Copied text preview with a sensitive content flag.


To flag sensitive content, add a boolean extra to the `ClipDescription`. All apps must do
this, regardless of the targeted API level.

```kotlin
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
```

## Paste from the clipboard

As described previously, paste data from the clipboard by getting the global clipboard object,
getting the clip object, looking at its data, and if possible copying the data from the clip object
to your own storage. This section explains in detail how to paste the three forms of clipboard
data.
**Important:** For editable `TextView` objects, follow the [Receive rich content](https://developer.android.com/guide/topics/input/receive-rich-content) document to add support for pasting any type of content. The following section describes how to develop a custom UI for pasting content.

### Paste plain text

To paste plain text, get the global clipboard and verify that it can return plain text. Then get
the clip object and copy its text to your own storage using `getText()`, as described in
the following procedure:

1. Get the global `ClipboardManager` object using `getSystemService(CLIPBOARD_SERVICE)`. Also, declare a global variable to contain the pasted text:

   ### Kotlin

   ```kotlin
   var clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
   var pasteData: String = ""
   ```

   ### Java

   ```java
   ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
   String pasteData = "";
   ```
2. Determine whether you need to enable or disable the "paste" option in the current activity. Verify that the clipboard contains a clip and that you can handle the type of data represented by the clip:

   ### Kotlin

   ```kotlin
   // Gets the ID of the "paste" menu item.
   val pasteItem: MenuItem = menu.findItem(R.id.menu_paste)

   // If the clipboard doesn't contain data, disable the paste menu item.
   // If it does contain data, decide whether you can handle the data.
   pasteItem.isEnabled = when {
       !clipboard.hasPrimaryClip() -> {
           false
       }
       !(clipboard.primaryClipDescription.hasMimeType(MIMETYPE_TEXT_PLAIN)) -> {
           // Disables the paste menu item, since the clipboard has data but it
           // isn't plain text.
           false
       }
       else -> {
           // Enables the paste menu item, since the clipboard contains plain text.
           true
       }
   }
   ```

   ### Java

   ```java
   // Gets the ID of the "paste" menu item.
   MenuItem pasteItem = menu.findItem(R.id.menu_paste);

   // If the clipboard doesn't contain data, disable the paste menu item.
   // If it does contain data, decide whether you can handle the data.
   if (!(clipboard.hasPrimaryClip())) {

       pasteItem.setEnabled(false);

   } else if (!(clipboard.getPrimaryClipDescription().hasMimeType(MIMETYPE_TEXT_PLAIN))) {

       // Disables the paste menu item, since the clipboard has data but
       // it isn't plain text.
       pasteItem.setEnabled(false);
   } else {

       // Enables the paste menu item, since the clipboard contains plain text.
       pasteItem.setEnabled(true);
   }
   ```
3. Copy the data from the clipboard. This point in the code is only reachable if the "paste" menu item is enabled, so you can assume that the clipboard contains plain text. You don't yet know if it contains a text string or a URI that points to plain text. The following code snippet tests this, but it only shows the code for handling plain text:

   ### Kotlin

   ```kotlin
   when (menuItem.itemId) {
       ...
       R.id.menu_paste -> {    // Responds to the user selecting "paste".
           // Examines the item on the clipboard. If getText() doesn't return null,
           // the clip item contains the text. Assumes that this application can only
           // handle one item at a time.
           val item = clipboard.primaryClip.getItemAt(0)

           // Gets the clipboard as text.
           pasteData = item.text

           return if (pasteData != null) {
               // If the string contains data, then the paste operation is done.
               true
           } else {
               // The clipboard doesn't contain text. If it contains a URI,
               // attempts to get data from it.
               val pasteUri: Uri? = item.uri

               if (pasteUri != null) {
                   // If the URI contains something, try to get text from it.

                   // Calls a routine to resolve the URI and get data from it.
                   // This routine isn't presented here.
                   pasteData = resolveUri(pasteUri)
                   true
               } else {

                   // Something is wrong. The MIME type was plain text, but the
                   // clipboard doesn't contain text or a Uri. Report an error.
                   Log.e(TAG,"Clipboard contains an invalid data type")
                   false
               }
           }
       }
   }
   ```

   ### Java

   ```java
   // Responds to the user selecting "paste".
   case R.id.menu_paste:

   // Examines the item on the clipboard. If getText() does not return null,
   // the clip item contains the text. Assumes that this application can only
   // handle one item at a time.
    ClipData.Item item = clipboard.getPrimaryClip().getItemAt(0);

   // Gets the clipboard as text.
   pasteData = item.getText();

   // If the string contains data, then the paste operation is done.
   if (pasteData != null) {
       return true;

   // The clipboard doesn't contain text. If it contains a URI, attempts to get
   // data from it.
   } else {
       Uri pasteUri = item.getUri();

       // If the URI contains something, try to get text from it.
       if (pasteUri != null) {

           // Calls a routine to resolve the URI and get data from it.
           // This routine isn't presented here.
           pasteData = resolveUri(Uri);
           return true;
       } else {

           // Something is wrong. The MIME type is plain text, but the
           // clipboard doesn't contain text or a Uri. Report an error.
           Log.e(TAG, "Clipboard contains an invalid data type");
           return false;
       }
   }
   ```

### Paste data from a content URI

If the `ClipData.Item` object contains a content URI and you determine that you can
handle one of its MIME types, create a `ContentResolver` and call the appropriate content
provider method to retrieve the data.

The following procedure describes how to get data from a content provider based on a content URI
on the clipboard. It checks whether a MIME type that the application can use is available from the
provider.

1. Declare a global variable to contain the MIME type:

   ### Kotlin

   ```kotlin
   // Declares a MIME type constant to match against the MIME types offered
   // by the provider.
   const val MIME_TYPE_CONTACT = "vnd.android.cursor.item/vnd.example.contact"
   ```

   ### Java

   ```java
   // Declares a MIME type constant to match against the MIME types offered by
   // the provider.
   public static final String MIME_TYPE_CONTACT = "vnd.android.cursor.item/vnd.example.contact";
   ```
2. Get the global clipboard. Also get a content resolver so you can access the content provider:

   ### Kotlin

   ```kotlin
   // Gets a handle to the Clipboard Manager.
   val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager

   // Gets a content resolver instance.
   val cr = contentResolver
   ```

   ### Java

   ```java
   // Gets a handle to the Clipboard Manager.
   ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);

   // Gets a content resolver instance.
   ContentResolver cr = getContentResolver();
   ```
3. Get the primary clip from the clipboard and get its contents as a URI:

   ### Kotlin

   ```kotlin
   // Gets the clipboard data from the clipboard.
   val clip: ClipData? = clipboard.primaryClip

   clip?.run {

       // Gets the first item from the clipboard data.
       val item: ClipData.Item = getItemAt(0)

       // Tries to get the item's contents as a URI.
       val pasteUri: Uri? = item.uri
   ```

   ### Java

   ```java
   // Gets the clipboard data from the clipboard.
   ClipData clip = clipboard.getPrimaryClip();

   if (clip != null) {

       // Gets the first item from the clipboard data.
       ClipData.Item item = clip.getItemAt(0);

       // Tries to get the item's contents as a URI.
       Uri pasteUri = item.getUri();
   ```
4. Test whether the URI is a content URI by calling `https://developer.android.com/reference/android/content/ContentResolver#getType(android.net.Uri)`. This method returns null if `Uri` doesn't point to a valid content provider.

   ### Kotlin

   ```kotlin
       // If the clipboard contains a URI reference...
       pasteUri?.let {

           // ...is this a content URI?
           val uriMimeType: String? = cr.getType(it)
   ```

   ### Java

   ```java
       // If the clipboard contains a URI reference...
       if (pasteUri != null) {

           // ...is this a content URI?
           String uriMimeType = cr.getType(pasteUri);
   ```
5. Test whether the content provider supports a MIME type that the application understands. If it does, call `https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String)` to get the data. The return value is a `https://developer.android.com/reference/android/database/Cursor`.

   ### Kotlin

   ```kotlin
           // If the return value isn't null, the Uri is a content Uri.
           uriMimeType?.takeIf {

               // Does the content provider offer a MIME type that the current
               // application can use?
               it == MIME_TYPE_CONTACT
           }?.apply {

               // Get the data from the content provider.
               cr.query(pasteUri, null, null, null, null)?.use { pasteCursor ->

                   // If the Cursor contains data, move to the first record.
                   if (pasteCursor.moveToFirst()) {

                       // Get the data from the Cursor here.
                       // The code varies according to the format of the data model.
                   }

                   // Kotlin `use` automatically closes the Cursor.
               }
           }
       }
   }
   ```

   ### Java

   ```java
           // If the return value isn't null, the Uri is a content Uri.
           if (uriMimeType != null) {

               // Does the content provider offer a MIME type that the current
               // application can use?
               if (uriMimeType.equals(MIME_TYPE_CONTACT)) {

                   // Get the data from the content provider.
                   Cursor pasteCursor = cr.query(uri, null, null, null, null);

                   // If the Cursor contains data, move to the first record.
                   if (pasteCursor != null) {
                       if (pasteCursor.moveToFirst()) {

                       // Get the data from the Cursor here.
                       // The code varies according to the format of the data model.
                       }
                   }

                   // Close the Cursor.
                   pasteCursor.close();
                }
            }
        }
   }
   ```

### Paste an Intent

To paste an intent, first get the global clipboard. Examine the `ClipData.Item` object
to see whether it contains an `Intent`. Then call `getIntent()` to copy the
intent to your own storage. The following snippet demonstrates this:

### Kotlin

```kotlin
// Gets a handle to the Clipboard Manager.
val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager

// Checks whether the clip item contains an Intent by testing whether
// getIntent() returns null.
val pasteIntent: Intent? = clipboard.primaryClip?.getItemAt(0)?.intent

if (pasteIntent != null) {

    // Handle the Intent.

} else {

    // Ignore the clipboard, or issue an error if
    // you expect an Intent to be on the clipboard.
}
```

### Java

```java
// Gets a handle to the Clipboard Manager.
ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);

// Checks whether the clip item contains an Intent, by testing whether
// getIntent() returns null.
Intent pasteIntent = clipboard.getPrimaryClip().getItemAt(0).getIntent();

if (pasteIntent != null) {

    // Handle the Intent.

} else {

    // Ignore the clipboard, or issue an error if
    // you expect an Intent to be on the clipboard.
}
```

## System notification shown when your app accesses clipboard data

On Android 12 (API level 31) and higher, the system usually shows a toast message when your app
calls
[`getPrimaryClip()`](https://developer.android.com/reference/android/content/ClipboardManager#getPrimaryClip()).
The text inside the message contains the following format:

```
APP pasted from your clipboard
```

The system doesn't show a toast message when your app does one of the following:

- Accesses [`ClipData`](https://developer.android.com/reference/android/content/ClipData) from your own app.
- Repeatedly accesses `ClipData` from a specific app. The toast appears only when your app accesses the data from that app for the first time.
- Retrieves metadata for the clip object, such as by calling [`getPrimaryClipDescription()`](https://developer.android.com/reference/android/content/ClipboardManager#getPrimaryClipDescription()) instead of `getPrimaryClip()`.

## Use content providers to copy complex data

Content providers support copying complex data such as database records or file streams. To copy
the data, put a content URI on the clipboard. Pasting applications then get this URI from the
clipboard and use it to retrieve database data or file stream descriptors.

Since the pasting application only has the content URI for your data, it needs to know which
piece of data to retrieve. You can provide this information by encoding an identifier for the data
on the URI itself, or you can provide a unique URI that returns the data you want to copy. Which
technique you choose depends on the organization of your data.

The following sections describe how to set up URIs, provide complex data, and provide file
streams. The descriptions assume you are familiar with the general principles of content provider
design.

### Encode an identifier on the URI

A useful technique for copying data to the clipboard with a URI is to encode an identifier for
the data on the URI itself. Your content provider can then get the identifier from the URI and use
it to retrieve the data. The pasting application doesn't have to know that the identifier exists. It
just has to get your "reference"---the URI plus the identifier---from the
clipboard, give it your content provider, and get back the data.

You usually encode an identifier onto a content URI by concatenating it to the end of the URI.
For example, suppose you define your provider URI as the following string:

```
"content://com.example.contacts"
```

If you want to encode a name onto this URI, use the following code snippet:

### Kotlin

```kotlin
val uriString = "content://com.example.contacts/Smith"

// uriString now contains content://com.example.contacts/Smith.

// Generates a uri object from the string representation.
val copyUri = Uri.parse(uriString)
```

### Java

```java
String uriString = "content://com.example.contacts" + "/" + "Smith";

// uriString now contains content://com.example.contacts/Smith.

// Generates a uri object from the string representation.
Uri copyUri = Uri.parse(uriString);
```

If you are already using a content provider, you might want to add a new URI path that indicates
the URI is for copying. For example, suppose you already have the following URI paths:

```
"content://com.example.contacts/people"
"content://com.example.contacts/people/detail"
"content://com.example.contacts/people/images"
```

You can add another path that for copying URIs:

```
"content://com.example.contacts/copying"
```

You can then detect a "copy" URI by pattern-matching and handle it with code that is
specific for copying and pasting.

You normally use the encoding technique if you're already using a content provider, internal
database, or internal table to organize your data. In these cases, you have multiple pieces of data
you want to copy, and presumably a unique identifier for each piece. In response to a query from the
pasting application, you can look up the data by its identifier and return it.

If you don't have multiple pieces of data, then you probably don't need to encode an identifier.
You can use a URI that is unique to your provider. In response to a query, your provider returns the
data it currently contains.

### Copy data structures

Set up a content provider for copying and pasting complex data as a subclass of the
`https://developer.android.com/reference/android/content/ContentProvider`
component. Encode the URI you put on the clipboard so that it points to the exact record you want to
provide. In addition, consider the existing state of your application:

- If you already have a content provider, you can add to its functionality. You might only need to modify its `query()` method to handle URIs coming from applications that want to paste data. You probably want to modify the method to handle a "copy" URI pattern.
- If your application maintains an internal database, you might want to move this database into a content provider to facilitate copying from it.
- If you aren't using a database, you can implement a simple content provider whose sole purpose is to offer data to applications that are pasting from the clipboard.

In the content provider, override at least the following methods:


`https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String)`
:   Pasting applications assume they can get your data by using this method with the URI you
    put on the clipboard. To support copying, have this method detect URIs containing a special
    "copy" path. Your application can then create a "copy" URI to put on the
    clipboard, containing the copy path and a pointer to the exact record you want to copy.


`https://developer.android.com/reference/android/content/ContentProvider#getType(android.net.Uri)`
:   This method must return the MIME types for the data you intend to copy. The method
    `https://developer.android.com/reference/android/content/ClipData#newUri(android.content.ContentResolver, java.lang.CharSequence, android.net.Uri)`
    calls `getType()` to put the MIME types into the new `ClipData`
    object.

    MIME types for complex data are described in
    [Content providers](https://developer.android.com/guide/topics/providers/content-providers).

You don't need to have any of the other content provider methods, such as
`https://developer.android.com/reference/android/content/ContentProvider#insert(android.net.Uri, android.content.ContentValues)`
or
`https://developer.android.com/reference/android/content/ContentProvider#update(android.net.Uri, android.content.ContentValues, java.lang.String, java.lang.String[])`.
A pasting application only needs to get your supported MIME types and copy data from your provider.
If you already have these methods, they won't interfere with copy operations.

The following snippets demonstrate how to set up your application to copy complex data:

1. In the global constants for your application, declare a base URI string and a path that
   identifies URI strings you are using to copy data. Also declare a MIME type for the copied
   data.

   ### Kotlin

   ```kotlin
   // Declares the base URI string.
   private const val CONTACTS = "content://com.example.contacts"

   // Declares a path string for URIs that you use to copy data.
   private const val COPY_PATH = "/copy"

   // Declares a MIME type for the copied data.
   const val MIME_TYPE_CONTACT = "vnd.android.cursor.item/vnd.example.contact"
   ```

   ### Java

   ```java
   // Declares the base URI string.
   private static final String CONTACTS = "content://com.example.contacts";

   // Declares a path string for URIs that you use to copy data.
   private static final String COPY_PATH = "/copy";

   // Declares a MIME type for the copied data.
   public static final String MIME_TYPE_CONTACT = "vnd.android.cursor.item/vnd.example.contact";
   ```
2. In the activity users copy data from, set up the code to copy data to the clipboard. In response to a copy request, put the URI on the clipboard.

   ### Kotlin

   ```kotlin
   class MyCopyActivity : Activity() {
       ...
   when(item.itemId) {
       R.id.menu_copy -> { // The user has selected a name and is requesting a copy.
           // Appends the last name to the base URI.
           // The name is stored in "lastName".
           uriString = "$CONTACTS$COPY_PATH/$lastName"

           // Parses the string into a URI.
           val copyUri: Uri? = Uri.parse(uriString)

           // Gets a handle to the clipboard service.
           val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager

           val clip: ClipData = ClipData.newUri(contentResolver, "URI", copyUri)

           // Sets the clipboard's primary clip.
           clipboard.setPrimaryClip(clip)
       }
   }
   ```

   ### Java

   ```java
   public class MyCopyActivity extends Activity {
       ...
   // The user has selected a name and is requesting a copy.
   case R.id.menu_copy:

       // Appends the last name to the base URI.
       // The name is stored in "lastName".
       uriString = CONTACTS + COPY_PATH + "/" + lastName;

       // Parses the string into a URI.
       Uri copyUri = Uri.parse(uriString);

       // Gets a handle to the clipboard service.
       ClipboardManager clipboard = (ClipboardManager)
           getSystemService(Context.CLIPBOARD_SERVICE);

       ClipData clip = ClipData.newUri(getContentResolver(), "URI", copyUri);

       // Sets the clipboard's primary clip.
       clipboard.setPrimaryClip(clip);
   ```
3. In the global scope of your content provider, create a URI matcher and add a URI pattern that
   matches URIs you put on the clipboard.

   ### Kotlin

   ```kotlin
   // A Uri Match object that simplifies matching content URIs to patterns.
   private val sUriMatcher = UriMatcher(UriMatcher.NO_MATCH).apply {

       // Adds a matcher for the content URI. It matches.
       // "content://com.example.contacts/copy/*"
       addURI(CONTACTS, "names/*", GET_SINGLE_CONTACT)
   }

   // An integer to use in switching based on the incoming URI pattern.
   private const val GET_SINGLE_CONTACT = 0
   ...
   class MyCopyProvider : ContentProvider() {
       ...
   }
   ```

   ### Java

   ```java
   public class MyCopyProvider extends ContentProvider {
       ...
   // A Uri Match object that simplifies matching content URIs to patterns.
   private static final UriMatcher sURIMatcher = new UriMatcher(UriMatcher.NO_MATCH);

   // An integer to use in switching based on the incoming URI pattern.
   private static final int GET_SINGLE_CONTACT = 0;
   ...
   // Adds a matcher for the content URI. It matches
   // "content://com.example.contacts/copy/*"
   sUriMatcher.addURI(CONTACTS, "names/*", GET_SINGLE_CONTACT);
   ```
4. Set up the
   `https://developer.android.com/reference/android/content/ContentProvider#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String)`
   method. This method can handle different URI patterns, depending on how you code it, but only
   the pattern for the clipboard copying operation shows.

   ### Kotlin

   ```kotlin
   // Sets up your provider's query() method.
   override fun query(
           uri: Uri,
           projection: Array<out String>?,
           selection: String?,
           selectionArgs: Array<out String>?,
           sortOrder: String?
   ): Cursor? {
       ...
       // When based on the incoming content URI:
       when(sUriMatcher.match(uri)) {

           GET_SINGLE_CONTACT -> {

               // Queries and returns the contact for the requested name. Decodes
               // the incoming URI, queries the data model based on the last name,
               // and returns the result as a Cursor.
           }
       }
       ...
   }
   ```

   ### Java

   ```java
   // Sets up your provider's query() method.
   public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs,
       String sortOrder) {
       ...
       // Switch based on the incoming content URI.
       switch (sUriMatcher.match(uri)) {

       case GET_SINGLE_CONTACT:

           // Queries and returns the contact for the requested name. Decodes the
           // incoming URI, queries the data model based on the last name, and
           // returns the result as a Cursor.
       ...
   }
   ```
5. Set up the `getType()` method to return an appropriate MIME type for copied
   data:

   ### Kotlin

   ```kotlin
   // Sets up your provider's getType() method.
   override fun getType(uri: Uri): String? {
       ...
       return when(sUriMatcher.match(uri)) {
           GET_SINGLE_CONTACT -> MIME_TYPE_CONTACT
           ...
       }
   }
   ```

   ### Java

   ```java
   // Sets up your provider's getType() method.
   public String getType(Uri uri) {
       ...
       switch (sUriMatcher.match(uri)) {
       case GET_SINGLE_CONTACT:
           return (MIME_TYPE_CONTACT);
       ...
       }
   }
   ```

The [Paste data from a content URI](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#PasteContentUri) section describes how to get a
content URI from the clipboard and use it to get and paste data.

### Copy data streams

You can copy and paste large amounts of text and binary data as streams. The data can have forms
such as the following:

- Files stored on the actual device
- Streams from sockets
- Large amounts of data stored in a provider's underlying database system

A content provider for data streams provides access to its data with a file descriptor object,
such as
`https://developer.android.com/reference/android/content/res/AssetFileDescriptor`,
instead of a `Cursor` object. The pasting application reads the data stream using this
file descriptor.

To set up your application to copy a data stream with a provider, follow these steps:

1. Set up a content URI for the data stream you are putting on the clipboard. Options for doing this include the following:
   - Encode an identifier for the data stream onto the URI, as described in the [Encode an identifier on the URI](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Encoding) section, and then maintain a table in your provider that contains identifiers and the corresponding stream name.
   - Encode the stream name directly on the URI.
   - Use a unique URI that always returns the current stream from the provider. If you use this option, remember to update your provider to point to a different stream whenever you copy the stream to the clipboard using the URI.
2. Provide a MIME type for each type of data stream you plan to offer. Pasting applications need this information to determine whether they can paste the data on the clipboard.
3. Implement one of the `ContentProvider` methods that returns a file descriptor for a stream. If you encode identifiers on the content URI, use this method to determine which stream to open.
4. To copy the data stream to the clipboard, construct the content URI and place it on the clipboard.

To paste a data stream, an application gets the clip from the clipboard, gets the URI, and uses
it in a call to a `ContentResolver` file descriptor method that opens the stream. The
`ContentResolver` method calls the corresponding `ContentProvider` method,
passing it the content URI. Your provider returns the file descriptor to the
`ContentResolver` method. The pasting application then has the responsibility to read the
data from the stream.

The following list shows the most important file descriptor methods for a content provider. Each
of these has a corresponding `ContentResolver` method with the string
"Descriptor" appended to the method name. For example, the `ContentResolver`
analog of
`https://developer.android.com/reference/android/content/ContentProvider#openAssetFile(android.net.Uri, java.lang.String)`
is
`https://developer.android.com/reference/android/content/ContentResolver#openAssetFileDescriptor(android.net.Uri, java.lang.String)`.


`https://developer.android.com/reference/android/content/ContentProvider#openTypedAssetFile(android.net.Uri, java.lang.String, android.os.Bundle)`

:   This method returns an asset file descriptor, but only if the provided MIME type is
    supported by the provider. The caller---the application doing the pasting---provides
    a MIME type pattern. The content provider of the application that copies a URI to the
    clipboard returns an `AssetFileDescriptor` file handle if it can provide that
    MIME type and throws an exception if it can't.

    This method handles subsections of files. You can use it to read assets that the
    content provider has copied to the clipboard.


`https://developer.android.com/reference/android/content/ContentProvider#openAssetFile(android.net.Uri, java.lang.String)`
:
    This method is a more general form of `openTypedAssetFile()`. It doesn't filter
    for allowed MIME types, but it can read subsections of files.


`https://developer.android.com/reference/android/content/ContentProvider#openFile(android.net.Uri, java.lang.String)`
:
    This is a more general form of `openAssetFile()`. It can't read subsections of
    files.

You can optionally use the
`https://developer.android.com/reference/android/content/ContentProvider#openPipeHelper(android.net.Uri, java.lang.String, android.os.Bundle, T, android.content.ContentProvider.PipeDataWriter<T>)`
method with your file descriptor method. This lets the pasting application read the stream data in a
background thread using a pipe. To use this method, implement the
`https://developer.android.com/reference/android/content/ContentProvider.PipeDataWriter`
interface.

## Design effective copy and paste functionality

To design effective copy and paste functionality for your application, remember these points:

- At any time, there is only one clip on the clipboard. A new copy operation by any application in the system overwrites the previous clip. Since the user might navigate away from your application and copy before returning, you can't assume the clipboard contains the clip that the user previously copied in *your* application.
- The intended purpose of multiple `ClipData.Item` objects per clip is to support copying and pasting of multiple selections rather than different forms of reference to a single selection. You usually want all of the `ClipData.Item` objects in a clip to have the same form. That is, they must all be simple text, content URI, or `Intent`, and not mixed.
- When you provide data, you can offer different MIME representations. Add the MIME types you support to the `ClipDescription`, and then implement the MIME types in your content provider.
- When you get data from the clipboard, your application is responsible for checking the available MIME types and then deciding which one, if any, to use. Even if there is a clip on the clipboard and the user requests a paste, your application isn't required to do the paste. Do the paste if the MIME type is compatible. You might coerce the data on the clipboard to text using `coerceToText()`. If your application supports more than one of the available MIME types, you can let the user pick which one to use.