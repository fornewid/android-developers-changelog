---
title: https://developer.android.com/training/data-storage/shared/documents-files
url: https://developer.android.com/training/data-storage/shared/documents-files
source: md.txt
---

On devices that run Android 4.4 (API level 19) and higher, your app can interact
with a [documents provider](https://developer.android.com/guide/topics/providers/create-document-provider),
including external storage volumes and cloud-based storage, using the Storage
Access Framework. This framework allows users to interact with a system picker
to choose a documents provider and select specific documents and other files for
your app to create, open, or modify.

Because the user is involved in selecting the files or directories that your app
can access, this mechanism doesn't require any [system
permissions](https://developer.android.com/guide/topics/permissions/overview), and user control and privacy
is enhanced. Additionally, these files, which are stored outside of an
app-specific directory and outside of the media store, remain on the device
after your app is uninstalled.

Using the framework involves the following steps:

1. An app invokes an intent that contains a storage-related action. This action corresponds to a specific [use case](https://developer.android.com/training/data-storage/shared/documents-files#use-cases) that the framework makes available.
2. The user sees a system picker, allowing them to browse a documents provider and choose a location or document where the storage-related action takes place.
3. The app gains read and write access to a URI that represents the user's chosen location or document. Using this URI, the app can [perform operations on
   the chosen location](https://developer.android.com/training/data-storage/shared/documents-files#perform-operations).

> [!NOTE]
> **Note:** If your app accesses media files, consider using the [photo picker](https://developer.android.com/training/data-storage/shared/photopicker), which provides a convenient interface for accessing photos and videos.

To support media file access on devices that run Android 9 (API level 28) or
lower, declare the
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
permission and set the `maxSdkVersion` to `28`.

This guide explains the different use cases that the framework supports for
working with files and other documents. It also explains how to perform
operations on the user-selected location.

## Use cases for accessing documents and other files

The Storage Access Framework supports the following use cases for accessing
files and other documents.

[Create a new file](https://developer.android.com/training/data-storage/shared/documents-files#create-file)
:   The
    [`ACTION_CREATE_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT)
    intent action allows users to save a file in a specific location.

[Open a document or file](https://developer.android.com/training/data-storage/shared/documents-files#open-file)
:   The
    [`ACTION_OPEN_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT)
    intent action allows users to select a specific document or file to open.

[Grant access to a directory's contents](https://developer.android.com/training/data-storage/shared/documents-files#grant-access-directory)
:   The
    [`ACTION_OPEN_DOCUMENT_TREE`](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT_TREE)
    intent action, available on Android 5.0 (API level 21) and higher, allows users
    to select a specific directory, granting your app access to all of the files and
    sub-directories within that directory.

The following sections provide guidance on how to configure each use case.

## Create a new file

Use the
[`ACTION_CREATE_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT)
intent action to load the system file picker and allow the user to choose a
location where to write the contents of a file. This process is similar to the
one used in the "save as" dialogs that other operating systems use.
**Note:** `ACTION_CREATE_DOCUMENT` cannot overwrite an
existing file. If your app tries to save a file with the same name, the system
appends a number in parentheses at the end of the file name.

For example, if your app tries to save a file called
`confirmation.pdf` in a directory that already has a file with that
name, the system saves the new file with the name
`confirmation(1).pdf`.

When configuring the intent, specify the file's name and MIME type, and
optionally specify the URI of the file or directory that the file picker should
display when it first loads by using the
[`EXTRA_INITIAL_URI`](https://developer.android.com/reference/android/provider/DocumentsContract#EXTRA_INITIAL_URI)
intent extra.

The following code snippet shows how to create and invoke the intent for
creating a file:

### Kotlin

```kotlin
// Request code for creating a PDF document.
const val CREATE_FILE = 1

private fun createFile(pickerInitialUri: Uri) {
    val intent = Intent(Intent.ACTION_CREATE_DOCUMENT).apply {
        addCategory(Intent.CATEGORY_OPENABLE)
        type = "application/pdf"
        putExtra(Intent.EXTRA_TITLE, "invoice.pdf")

        // Optionally, specify a URI for the directory that should be opened in
        // the system file picker before your app creates the document.
        putExtra(DocumentsContract.EXTRA_INITIAL_URI, pickerInitialUri)
    }
    startActivityForResult(intent, CREATE_FILE)
}
```

### Java

```java
// Request code for creating a PDF document.
private static final int CREATE_FILE = 1;

private void createFile(Uri pickerInitialUri) {
    Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
    intent.addCategory(Intent.CATEGORY_OPENABLE);
    intent.setType("application/pdf");
    intent.putExtra(Intent.EXTRA_TITLE, "invoice.pdf");

    // Optionally, specify a URI for the directory that should be opened in
    // the system file picker when your app creates the document.
    intent.putExtra(DocumentsContract.EXTRA_INITIAL_URI, pickerInitialUri);

    startActivityForResult(intent, CREATE_FILE);
}
```

## Open a file

Your app might use documents as the unit of storage in which users enter data
that they might want to share with peers or import into other documents. Several
examples include a user opening a productivity document or opening a book that's
saved as an EPUB file.

In these cases, allow the user to choose the file to open by invoking the
[`ACTION_OPEN_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT)
intent, which opens the system's file picker app. To show only the types of
files that your app supports, specify a MIME type. Also, you can optionally
specify the URI of the file that the file picker should display when it first
loads by using the
[`EXTRA_INITIAL_URI`](https://developer.android.com/reference/android/provider/DocumentsContract#EXTRA_INITIAL_URI)
intent extra.

The following code snippet shows how to create and invoke the intent for opening
a PDF document:

### Kotlin

```kotlin
// Request code for selecting a PDF document.
const val PICK_PDF_FILE = 2

fun openFile(pickerInitialUri: Uri) {
    val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
        addCategory(Intent.CATEGORY_OPENABLE)
        type = "application/pdf"

        // Optionally, specify a URI for the file that should appear in the
        // system file picker when it loads.
        putExtra(DocumentsContract.EXTRA_INITIAL_URI, pickerInitialUri)
    }

    startActivityForResult(intent, PICK_PDF_FILE)
}
```

### Java

```java
// Request code for selecting a PDF document.
private static final int PICK_PDF_FILE = 2;

private void openFile(Uri pickerInitialUri) {
    Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
    intent.addCategory(Intent.CATEGORY_OPENABLE);
    intent.setType("application/pdf");

    // Optionally, specify a URI for the file that should appear in the
    // system file picker when it loads.
    intent.putExtra(DocumentsContract.EXTRA_INITIAL_URI, pickerInitialUri);

    startActivityForResult(intent, PICK_PDF_FILE);
}
```

### Access restrictions

On Android 11 (API level 30) and higher, you cannot use the
`ACTION_OPEN_DOCUMENT` intent action to request that the user select individual
files from the following directories:

- The `Android/data/` directory and all subdirectories.
- The `Android/obb/` directory and all subdirectories.

## Grant access to a directory's contents

> [!NOTE]
> **Note:** The intent action that's discussed in this section is available on Android 5.0 (API level 21) and higher.

File management and media-creation apps typically manage groups of files in a
directory hierarchy. To provide this capability in your app, use the
[`ACTION_OPEN_DOCUMENT_TREE`](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT_TREE)
intent action, which allows the user to grant access to an entire directory
tree, with some exceptions starting in Android 11 (API level 30). Your app can
then access any file in the selected directory and any of its sub-directories.

When using `ACTION_OPEN_DOCUMENT_TREE`, your app gains access only to the
files in the directory that the user selects. You don't have access to other
apps' files that reside outside this user-selected directory. This
user-controlled access allows users to choose exactly what content they're
comfortable sharing with your app.

Optionally, you can specify the URI of the directory that the file picker should
display when it first loads by using the
[`EXTRA_INITIAL_URI`](https://developer.android.com/reference/android/provider/DocumentsContract#EXTRA_INITIAL_URI)
intent extra.

The following code snippet shows how to create and invoke the intent for opening
a directory:

### Kotlin

```kotlin
fun openDirectory(pickerInitialUri: Uri) {
    // Choose a directory using the system's file picker.
    val intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE).apply {
        // Optionally, specify a URI for the directory that should be opened in
        // the system file picker when it loads.
        putExtra(DocumentsContract.EXTRA_INITIAL_URI, pickerInitialUri)
    }

    startActivityForResult(intent, your-request-code)
}
```

### Java

```java
public void openDirectory(Uri uriToLoad) {
    // Choose a directory using the system's file picker.
    Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE);

    // Optionally, specify a URI for the directory that should be opened in
    // the system file picker when it loads.
    intent.putExtra(DocumentsContract.EXTRA_INITIAL_URI, uriToLoad);

    startActivityForResult(intent, your-request-code);
}
```

> [!CAUTION]
> **Caution:** If you iterate through a large number of files within the directory that's accessed using `ACTION_OPEN_DOCUMENT_TREE`, your app's performance might be reduced.

### Access restrictions

On Android 11 (API level 30) and higher, you cannot use the
`ACTION_OPEN_DOCUMENT_TREE` intent action to request access to the following
directories:

- The root directory of the internal storage volume.
- The root directory of each SD card volume that the device manufacturer considers to be *reliable*, regardless of whether the card is emulated or removable. A reliable volume is one that an app can successfully access most of the time.
- The `Download` directory.

Furthermore, on Android 11 (API level 30) and higher, you cannot use the
`ACTION_OPEN_DOCUMENT_TREE` intent action to request that the user select
individual files from the following directories:

- The `Android/data/` directory and all subdirectories.
- The `Android/obb/` directory and all subdirectories.

## Perform operations on chosen location

After the user has selected a file or directory using the system's file picker,
you can retrieve the selected item's URI using the following code in
[`onActivityResult()`](https://developer.android.com/reference/android/app/Activity#onActivityResult(int,%20int,%20android.content.Intent)):

### Kotlin

```kotlin
override fun onActivityResult(
        requestCode: Int, resultCode: Int, resultData: Intent?) {
    if (requestCode == your-request-code
            && resultCode == Activity.RESULT_OK) {
        // The result data contains a URI for the document or directory that
        // the user selected.
        resultData?.data?.also { uri ->
            // Perform operations on the document using its URI.
        }
    }
}
```

### Java

```java
@Override
public void onActivityResult(int requestCode, int resultCode,
        Intent resultData) {
    if (requestCode == your-request-code
            && resultCode == Activity.RESULT_OK) {
        // The result data contains a URI for the document or directory that
        // the user selected.
        Uri uri = null;
        if (resultData != null) {
            uri = resultData.getData();
            // Perform operations on the document using its URI.
        }
    }
}
```

By getting a reference to the selected item's URI, your app can perform several
operations on the item. For example, you can access the item's metadata, edit
the item in place, and delete the item.

The following sections show how to complete actions on the files that the user
selects.

### Determine operations that a provider supports

Different content providers allow for different operations to be performed on
documents---such as copying the document or viewing a document's thumbnail. To
determine which operations a given provider supports, check the value of
[`Document.COLUMN_FLAGS`](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS).
Your app's UI can then show only the options that the provider supports.

### Persist permissions

When your app opens a file for reading or writing, the system gives your app a
URI permission grant for that file, which lasts until the user's device
restarts. Suppose, however, that your app is an image-editing app, and you want
users to be able to access the 5 images that they most recently edited, directly
from your app. If the user's device has restarted, you'd have to send the user
back to the system picker to find the files.

To preserve access to files across device restarts and create a better user
experience, your app can "take" the persistable URI permission grant that the
system offers, as shown in the following code snippet:

### Kotlin

```kotlin
val contentResolver = applicationContext.contentResolver

val takeFlags: Int = Intent.FLAG_GRANT_READ_URI_PERMISSION or
        Intent.FLAG_GRANT_WRITE_URI_PERMISSION
// Check for the freshest data.
contentResolver.takePersistableUriPermission(uri, takeFlags)
```

### Java

```java
final int takeFlags = intent.getFlags()
            & (Intent.FLAG_GRANT_READ_URI_PERMISSION
            | Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
// Check for the freshest data.
getContentResolver().takePersistableUriPermission(uri, takeFlags);
```

> [!CAUTION]
> **Caution:** Even after calling `takePersistableUriPermission()`, your app doesn't retain access to the URI if the associated document is moved or deleted. In those cases, you need to ask permission again to regain access to the URI.

### Examine document metadata

When you have the URI for a document, you gain access to its metadata. This
snippet grabs the metadata for a document specified by the URI, and logs it:

### Kotlin

```kotlin
val contentResolver = applicationContext.contentResolver

fun dumpImageMetaData(uri: Uri) {

    // The query, because it only applies to a single document, returns only
    // one row. There's no need to filter, sort, or select fields,
    // because we want all fields for one document.
    val cursor: Cursor? = contentResolver.query(
            uri, null, null, null, null, null)

    cursor?.use {
        // moveToFirst() returns false if the cursor has 0 rows. Very handy for
        // "if there's anything to look at, look at it" conditionals.
        if (it.moveToFirst()) {

            // Note it's called "Display Name". This is
            // provider-specific, and might not necessarily be the file name.
            val displayName: String =
                    it.getString(it.getColumnIndex(OpenableColumns.DISPLAY_NAME))
            Log.i(TAG, "Display Name: $displayName")

            val sizeIndex: Int = it.getColumnIndex(OpenableColumns.SIZE)
            // If the size is unknown, the value stored is null. But because an
            // int can't be null, the behavior is implementation-specific,
            // and unpredictable. So as
            // a rule, check if it's null before assigning to an int. This will
            // happen often: The storage API allows for remote files, whose
            // size might not be locally known.
            val size: String = if (!it.isNull(sizeIndex)) {
                // Technically the column stores an int, but cursor.getString()
                // will do the conversion automatically.
                it.getString(sizeIndex)
            } else {
                "Unknown"
            }
            Log.i(TAG, "Size: $size")
        }
    }
}
```

### Java

```java
public void dumpImageMetaData(Uri uri) {

    // The query, because it only applies to a single document, returns only
    // one row. There's no need to filter, sort, or select fields,
    // because we want all fields for one document.
    Cursor cursor = getActivity().getContentResolver()
            .query(uri, null, null, null, null, null);

    try {
        // moveToFirst() returns false if the cursor has 0 rows. Very handy for
        // "if there's anything to look at, look at it" conditionals.
        if (cursor != null && cursor.moveToFirst()) {

            // Note it's called "Display Name". This is
            // provider-specific, and might not necessarily be the file name.
            String displayName = cursor.getString(
                    cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME));
            Log.i(TAG, "Display Name: " + displayName);

            int sizeIndex = cursor.getColumnIndex(OpenableColumns.SIZE);
            // If the size is unknown, the value stored is null. But because an
            // int can't be null, the behavior is implementation-specific,
            // and unpredictable. So as
            // a rule, check if it's null before assigning to an int. This will
            // happen often: The storage API allows for remote files, whose
            // size might not be locally known.
            String size = null;
            if (!cursor.isNull(sizeIndex)) {
                // Technically the column stores an int, but cursor.getString()
                // will do the conversion automatically.
                size = cursor.getString(sizeIndex);
            } else {
                size = "Unknown";
            }
            Log.i(TAG, "Size: " + size);
        }
    } finally {
        cursor.close();
    }
}
```

### Open a document

By having a reference to a document's URI, you can open a document for further
processing. This section shows examples for opening a bitmap and an input
stream.

#### Bitmap

The following code snippet shows how to open a
[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap) file given its URI:

### Kotlin

```kotlin
val contentResolver = applicationContext.contentResolver

@Throws(IOException::class)
private fun getBitmapFromUri(uri: Uri): Bitmap {
    val parcelFileDescriptor: ParcelFileDescriptor =
            contentResolver.openFileDescriptor(uri, "r")
    val fileDescriptor: FileDescriptor = parcelFileDescriptor.fileDescriptor
    val image: Bitmap = BitmapFactory.decodeFileDescriptor(fileDescriptor)
    parcelFileDescriptor.close()
    return image
}
```

### Java

```java
private Bitmap getBitmapFromUri(Uri uri) throws IOException {
    ParcelFileDescriptor parcelFileDescriptor =
            getContentResolver().openFileDescriptor(uri, "r");
    FileDescriptor fileDescriptor = parcelFileDescriptor.getFileDescriptor();
    Bitmap image = BitmapFactory.decodeFileDescriptor(fileDescriptor);
    parcelFileDescriptor.close();
    return image;
}
```

> [!NOTE]
> **Note:** You should complete this operation on a background thread, not the UI thread.

After you open the bitmap, you can display it in an
[`ImageView`](https://developer.android.com/reference/android/widget/ImageView).

#### Input stream

The following code snippet shows how to open an InputStream object given its
URI. In this snippet, the lines of the file are being read into a string:

### Kotlin

```kotlin
val contentResolver = applicationContext.contentResolver

@Throws(IOException::class)
private fun readTextFromUri(uri: Uri): String {
    val stringBuilder = StringBuilder()
    contentResolver.openInputStream(uri)?.use { inputStream ->
        BufferedReader(InputStreamReader(inputStream)).use { reader ->
            var line: String? = reader.readLine()
            while (line != null) {
                stringBuilder.append(line)
                line = reader.readLine()
            }
        }
    }
    return stringBuilder.toString()
}
```

### Java

```java
private String readTextFromUri(Uri uri) throws IOException {
    StringBuilder stringBuilder = new StringBuilder();
    try (InputStream inputStream =
            getContentResolver().openInputStream(uri);
            BufferedReader reader = new BufferedReader(
            new InputStreamReader(Objects.requireNonNull(inputStream)))) {
        String line;
        while ((line = reader.readLine()) != null) {
            stringBuilder.append(line);
        }
    }
    return stringBuilder.toString();
}
```

### Edit a document

You can use the Storage Access Framework to edit a text document in place.

> [!NOTE]
> **Note:** The `DocumentFile` class's [`canWrite()`](https://developer.android.com/reference/androidx/documentfile/provider/DocumentFile#canWrite()) method doesn't necessarily indicate that your app can edit a document. That's because this method returns `true` if [`Document.COLUMN_FLAGS`](https://developer.android.com/training/data-storage/shared/(/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS)) contains *either* `FLAG_SUPPORTS_DELETE` or `FLAG_SUPPORTS_WRITE`. To determine whether your app can edit a given document, query the value of `FLAG_SUPPORTS_WRITE` directly.

The following code snippet overwrites the contents of the document represented
by the given URI:

### Kotlin

```kotlin
val contentResolver = applicationContext.contentResolver

private fun alterDocument(uri: Uri) {
    try {
        contentResolver.openFileDescriptor(uri, "w")?.use {
            FileOutputStream(it.fileDescriptor).use {
                it.write(
                    ("Overwritten at ${System.currentTimeMillis()}\n")
                        .toByteArray()
                )
            }
        }
    } catch (e: FileNotFoundException) {
        e.printStackTrace()
    } catch (e: IOException) {
        e.printStackTrace()
    }
}
```

### Java

```java
private void alterDocument(Uri uri) {
    try {
        ParcelFileDescriptor pfd = getActivity().getContentResolver().
                openFileDescriptor(uri, "w");
        FileOutputStream fileOutputStream =
                new FileOutputStream(pfd.getFileDescriptor());
        fileOutputStream.write(("Overwritten at " + System.currentTimeMillis() +
                "\n").getBytes());
        // Let the document provider know you're done by closing the stream.
        fileOutputStream.close();
        pfd.close();
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### Delete a document

If you have the URI for a document and the document's
[`Document.COLUMN_FLAGS`](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS)
contains
[`SUPPORTS_DELETE`](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_DELETE),
you can delete the document. For example:

### Kotlin

```kotlin
DocumentsContract.deleteDocument(applicationContext.contentResolver, uri)
```

### Java

```java
DocumentsContract.deleteDocument(applicationContext.contentResolver, uri);
```

### Retrieve an equivalent media URI

The
[`getMediaUri()`](https://developer.android.com/reference/android/provider/MediaStore#getMediaUri(android.content.Context,%20android.net.Uri))
method provides a media store URI that is equivalent to the given documents
provider URI. The 2 URIs refer to the same underlying item. Using the media
store URI, you can more easily [access media files from shared
storage](https://developer.android.com/training/data-storage/shared/media).

> [!NOTE]
> **Note:** This method doesn't grant any new permissions. Your app must already have the necessary permissions to access a given document provider URI, such as by [opening the document](https://developer.android.com/training/data-storage/shared/documents-files#open).

The `getMediaUri()` method supports `ExternalStorageProvider` URIs. On
Android 12 (API level 31) and higher, the method also supports
`MediaDocumentsProvider` URIs.

### Open a virtual file

On Android 7.0 (API level 25) and higher, your app can make use of virtual files
that the Storage Access Framework makes available. Even though virtual files
don't have a binary representation, your app can open their contents by coercing
them into a different file type or by viewing those files by using the
[`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW) intent
action.

To open virtual files, your client app needs to include special logic to handle
them. If you want to get a byte representation of the file---to preview the file,
for example---you need to request for an alternate MIME type from the documents
provider.

> [!NOTE]
> **Note:** Because an app cannot directly open a virtual file by using the [`openInputStream()`](https://developer.android.com/reference/android/content/ContentResolver#openInputStream(android.net.Uri)) method, don't use the [`CATEGORY_OPENABLE`](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE) category when creating the intent that contains the `ACTION_OPEN_DOCUMENT` or `ACTION_OPEN_DOCUMENT_TREE` action.

After the user makes a selection, use the URI in the results data to determine
whether the file is virtual, as shown in the following code snippet:

### Kotlin

```kotlin
private fun isVirtualFile(uri: Uri): Boolean {
    if (!DocumentsContract.isDocumentUri(this, uri)) {
        return false
    }

    val cursor: Cursor? = contentResolver.query(
            uri,
            arrayOf(DocumentsContract.Document.COLUMN_FLAGS),
            null,
            null,
            null
    )

    val flags: Int = cursor?.use {
        if (cursor.moveToFirst()) {
            cursor.getInt(0)
        } else {
            0
        }
    } ?: 0

    return flags and DocumentsContract.Document.FLAG_VIRTUAL_DOCUMENT != 0
}
```

### Java

```java
private boolean isVirtualFile(Uri uri) {
    if (!DocumentsContract.isDocumentUri(this, uri)) {
        return false;
    }

    Cursor cursor = getContentResolver().query(
        uri,
        new String[] { DocumentsContract.Document.COLUMN_FLAGS },
        null, null, null);

    int flags = 0;
    if (cursor.moveToFirst()) {
        flags = cursor.getInt(0);
    }
    cursor.close();

    return (flags & DocumentsContract.Document.FLAG_VIRTUAL_DOCUMENT) != 0;
}
```

After you verify that the document is a virtual file, you can then coerce the
file into an alternative MIME type, such as `"image/png"`. The following code
snippet shows how to check whether a virtual file can be represented as an
image, and if so, gets an input stream from the virtual file:

### Kotlin

```kotlin
@Throws(IOException::class)
private fun getInputStreamForVirtualFile(
        uri: Uri, mimeTypeFilter: String): InputStream {

    val openableMimeTypes: Array<String>? =
            contentResolver.getStreamTypes(uri, mimeTypeFilter)

    return if (openableMimeTypes?.isNotEmpty() == true) {
        contentResolver
                .openTypedAssetFileDescriptor(uri, openableMimeTypes[0], null)
                .createInputStream()
    } else {
        throw FileNotFoundException()
    }
}
```

### Java

```java
private InputStream getInputStreamForVirtualFile(Uri uri, String mimeTypeFilter)
    throws IOException {

    ContentResolver resolver = getContentResolver();

    String[] openableMimeTypes = resolver.getStreamTypes(uri, mimeTypeFilter);

    if (openableMimeTypes == null ||
        openableMimeTypes.length < 1) {
        throw new FileNotFoundException();
    }

    return resolver
        .openTypedAssetFileDescriptor(uri, openableMimeTypes[0], null)
        .createInputStream();
}
```

## Additional resources

For more information about how to store and access documents and other files,
consult the following resources.

### Samples

- [ActionOpenDocument](https://github.com/android/storage-samples/tree/main/ActionOpenDocument), available on GitHub.
- [ActionOpenDocumentTree](https://github.com/android/storage-samples/tree/main/ActionOpenDocumentTree), available on GitHub.

### Videos

- [Preparing for Scoped Storage (Android Dev Summit
  '19)](https://www.youtube.com/watch?v=UnJ3amzJM94)