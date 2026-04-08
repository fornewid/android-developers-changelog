---
title: https://developer.android.com/guide/topics/providers/create-document-provider
url: https://developer.android.com/guide/topics/providers/create-document-provider
source: md.txt
---

# Create a custom document provider

If you're developing an app that provides storage services for files (such as a cloud save service), you can make your files available through the Storage Access Framework (SAF) by writing a custom document provider. This page describes how to create a custom document provider.

For more information about how the Storage Access Framework works, see the[Storage Access Framework overview](https://developer.android.com/guide/topics/providers/document-provider#overview).

## Manifest

To implement a custom document provider, add the following to your application's manifest:

- A target of API level 19 or higher.
- A`<provider>`element that declares your custom storage provider.
- The attribute`android:name`set to the name of your[DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider)subclass, which is its class name, including package name:

  `com.example.android.storageprovider.MyCloudProvider`.
- The attribute`android:authority`attribute, which is your package name (in this example,`com.example.android.storageprovider`) plus the type of content provider (`documents`).
- The attribute`android:exported`set to`"true"`. You must export your provider so that other apps can see it.
- The attribute`android:grantUriPermissions`set to`"true"`. This setting allows the system to grant other apps access to content in your provider. For a discussion about how these other apps can persist their access to content from your provider, see[Persist permissions](https://developer.android.com/training/data-storage/shared/documents-files#persist-permissions).
- The`MANAGE_DOCUMENTS`permission. By default a provider is available to everyone. Adding this permission restricts your provider to the system. This restriction is important for security.
- An intent filter that includes the`android.content.action.DOCUMENTS_PROVIDER`action, so that your provider appears in the picker when the system searches for providers.

Here are excerpts from a sample manifest that includes a provider:  

```xml
<manifest... >
    ...
    <uses-sdk
        android:minSdkVersion="19"
        android:targetSdkVersion="19" />
        ....
        <provider
            android:name="com.example.android.storageprovider.MyCloudProvider"
            android:authorities="com.example.android.storageprovider.documents"
            android:grantUriPermissions="true"
            android:exported="true"
            android:permission="android.permission.MANAGE_DOCUMENTS">
            <intent-filter>
                <action android:name="android.content.action.DOCUMENTS_PROVIDER" />
            </intent-filter>
        </provider>
    </application>

</manifest>
```

### Supporting devices running Android 4.3 and lower

The[ACTION_OPEN_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT)intent is only available on devices running Android 4.4 and higher. If you want your application to support[ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)to accommodate devices that are running Android 4.3 and lower, you should disable the[ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)intent filter in your manifest for devices running Android 4.4 or higher. A document provider and[ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)should be considered mutually exclusive. If you support both of them simultaneously, your app appears twice in the system picker UI, offering two different ways of accessing your stored data. This is confusing for users.

Here is the recommended way of disabling the[ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)intent filter for devices running Android version 4.4 or higher:

1. In your`bool.xml`resources file under`res/values/`, add this line:  

   ```xml
   <bool name="atMostJellyBeanMR2">true</bool>
   ```
2. In your`bool.xml`resources file under`res/values-v19/`, add this line:  

   ```xml
   <bool name="atMostJellyBeanMR2">false</bool>
   ```
3. Add an[activity alias](https://developer.android.com/guide/topics/manifest/activity-alias-element)to disable the[ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)intent filter for versions 4.4 (API level 19) and higher. For example:  

   ```xml
   <!-- This activity alias is added so that GET_CONTENT intent-filter
        can be disabled for builds on API level 19 and higher. -->
   <activity-alias android:name="com.android.example.app.MyPicker"
           android:targetActivity="com.android.example.app.MyActivity"
           ...
           android:enabled="@bool/atMostJellyBeanMR2">
       <intent-filter>
           <action android:name="android.intent.action.GET_CONTENT" />
           <category android:name="android.intent.category.OPENABLE" />
           <category android:name="android.intent.category.DEFAULT" />
           <data android:mimeType="image/*" />
           <data android:mimeType="video/*" />
       </intent-filter>
   </activity-alias>
   ```

## Contracts

Usually when you write a custom content provider, one of the tasks is implementing contract classes, as described in the[Content providers](https://developer.android.com/guide/topics/providers/content-provider-creating#ContractClass)developers guide. A contract class is a`public final`class that contains constant definitions for the URIs, column names, MIME types, and other metadata that pertain to the provider. The SAF provides these contract classes for you, so you don't need to write your own:

- [DocumentsContract.Document](https://developer.android.com/reference/android/provider/DocumentsContract.Document)
- [DocumentsContract.Root](https://developer.android.com/reference/android/provider/DocumentsContract.Root)

For example, here are the columns you might return in a cursor when your document provider is queried for documents or the root:  

### Kotlin

```kotlin
private val DEFAULT_ROOT_PROJECTION: Array<String> = arrayOf(
        DocumentsContract.Root.COLUMN_ROOT_ID,
        DocumentsContract.Root.COLUMN_MIME_TYPES,
        DocumentsContract.Root.COLUMN_FLAGS,
        DocumentsContract.Root.COLUMN_ICON,
        DocumentsContract.Root.COLUMN_TITLE,
        DocumentsContract.Root.COLUMN_SUMMARY,
        DocumentsContract.Root.COLUMN_DOCUMENT_ID,
        DocumentsContract.Root.COLUMN_AVAILABLE_BYTES
)
private val DEFAULT_DOCUMENT_PROJECTION: Array<String> = arrayOf(
        DocumentsContract.Document.COLUMN_DOCUMENT_ID,
        DocumentsContract.Document.COLUMN_MIME_TYPE,
        DocumentsContract.Document.COLUMN_DISPLAY_NAME,
        DocumentsContract.Document.COLUMN_LAST_MODIFIED,
        DocumentsContract.Document.COLUMN_FLAGS,
        DocumentsContract.Document.COLUMN_SIZE
)
```

### Java

```java
private static final String[] DEFAULT_ROOT_PROJECTION =
        new String[]{Root.COLUMN_ROOT_ID, Root.COLUMN_MIME_TYPES,
        Root.COLUMN_FLAGS, Root.COLUMN_ICON, Root.COLUMN_TITLE,
        Root.COLUMN_SUMMARY, Root.COLUMN_DOCUMENT_ID,
        Root.COLUMN_AVAILABLE_BYTES,};
private static final String[] DEFAULT_DOCUMENT_PROJECTION = new
        String[]{Document.COLUMN_DOCUMENT_ID, Document.COLUMN_MIME_TYPE,
        Document.COLUMN_DISPLAY_NAME, Document.COLUMN_LAST_MODIFIED,
        Document.COLUMN_FLAGS, Document.COLUMN_SIZE,};
```

Your cursor for the root needs to include certain required columns. These columns are:

- [COLUMN_ROOT_ID](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_ROOT_ID)
- [COLUMN_ICON](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_ICON)
- [COLUMN_TITLE](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_TITLE)
- [COLUMN_FLAGS](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_FLAGS)
- [COLUMN_DOCUMENT_ID](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_DOCUMENT_ID)

<br />

The cursor for documents needs to include the following required columns:

- [COLUMN_DOCUMENT_ID](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_DOCUMENT_ID)
- [COLUMN_DISPLAY_NAME](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_DISPLAY_NAME)
- [COLUMN_MIME_TYPE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_MIME_TYPE)
- [COLUMN_FLAGS](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS)
- [COLUMN_SIZE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_SIZE)
- [COLUMN_LAST_MODIFIED](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_LAST_MODIFIED)

<br />

## Create a subclass of DocumentsProvider

The next step in writing a custom document provider is to subclass the abstract class[DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider). At minimum, you must implement the following methods:

- [queryRoots()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRoots(java.lang.String[]))
- [queryChildDocuments()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryChildDocuments(java.lang.String, java.lang.String[], android.os.Bundle))
- [queryDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryDocument(java.lang.String, java.lang.String[]))
- [openDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#openDocument(java.lang.String, java.lang.String, android.os.CancellationSignal))

These are the only methods you are strictly required to implement, but there are many more you might want to. See[DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider)for details.

### Define a root

Your implementation of[queryRoots()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRoots(java.lang.String[]))needs to return a[Cursor](https://developer.android.com/reference/android/database/Cursor)pointing to all the root directories of your document provider, using columns defined in[DocumentsContract.Root](https://developer.android.com/reference/android/provider/DocumentsContract.Root).

In the following snippet, the`projection`parameter represents the specific fields the caller wants to get back. The snippet creates a new cursor and adds one row to it---one root, a top level directory, like Downloads or Images. Most providers only have one root. You might have more than one, for example, in the case of multiple user accounts. In that case, just add a second row to the cursor.  

### Kotlin

```kotlin
override fun queryRoots(projection: Array<out String>?): Cursor {
    // Use a MatrixCursor to build a cursor
    // with either the requested fields, or the default
    // projection if "projection" is null.
    val result = MatrixCursor(resolveRootProjection(projection))

    // If user is not logged in, return an empty root cursor.  This removes our
    // provider from the list entirely.
    if (!isUserLoggedIn()) {
        return result
    }

    // It's possible to have multiple roots (e.g. for multiple accounts in the
    // same app) -- just add multiple cursor rows.
    result.newRow().apply {
        add(DocumentsContract.Root.COLUMN_ROOT_ID, ROOT)

        // You can provide an optional summary, which helps distinguish roots
        // with the same title. You can also use this field for displaying an
        // user account name.
        add(DocumentsContract.Root.COLUMN_SUMMARY, context.getString(R.string.root_summary))

        // FLAG_SUPPORTS_CREATE means at least one directory under the root supports
        // creating documents. FLAG_SUPPORTS_RECENTS means your application's most
        // recently used documents will show up in the "Recents" category.
        // FLAG_SUPPORTS_SEARCH allows users to search all documents the application
        // shares.
        add(
            DocumentsContract.Root.COLUMN_FLAGS,
            DocumentsContract.Root.FLAG_SUPPORTS_CREATE or
                DocumentsContract.Root.FLAG_SUPPORTS_RECENTS or
                DocumentsContract.Root.FLAG_SUPPORTS_SEARCH
        )

        // COLUMN_TITLE is the root title (e.g. Gallery, Drive).
        add(DocumentsContract.Root.COLUMN_TITLE, context.getString(R.string.title))

        // This document id cannot change after it's shared.
        add(DocumentsContract.Root.COLUMN_DOCUMENT_ID, getDocIdForFile(baseDir))

        // The child MIME types are used to filter the roots and only present to the
        // user those roots that contain the desired type somewhere in their file hierarchy.
        add(DocumentsContract.Root.COLUMN_MIME_TYPES, getChildMimeTypes(baseDir))
        add(DocumentsContract.Root.COLUMN_AVAILABLE_BYTES, baseDir.freeSpace)
        add(DocumentsContract.Root.COLUMN_ICON, R.drawable.ic_launcher)
    }

    return result
}
```

### Java

```java
@Override
public Cursor queryRoots(String[] projection) throws FileNotFoundException {

    // Use a MatrixCursor to build a cursor
    // with either the requested fields, or the default
    // projection if "projection" is null.
    final MatrixCursor result =
            new MatrixCursor(resolveRootProjection(projection));

    // If user is not logged in, return an empty root cursor.  This removes our
    // provider from the list entirely.
    if (!isUserLoggedIn()) {
        return result;
    }

    // It's possible to have multiple roots (e.g. for multiple accounts in the
    // same app) -- just add multiple cursor rows.
    final MatrixCursor.RowBuilder row = result.newRow();
    row.add(Root.COLUMN_ROOT_ID, ROOT);

    // You can provide an optional summary, which helps distinguish roots
    // with the same title. You can also use this field for displaying an
    // user account name.
    row.add(Root.COLUMN_SUMMARY, getContext().getString(R.string.root_summary));

    // FLAG_SUPPORTS_CREATE means at least one directory under the root supports
    // creating documents. FLAG_SUPPORTS_RECENTS means your application's most
    // recently used documents will show up in the "Recents" category.
    // FLAG_SUPPORTS_SEARCH allows users to search all documents the application
    // shares.
    row.add(Root.COLUMN_FLAGS, Root.FLAG_SUPPORTS_CREATE |
            Root.FLAG_SUPPORTS_RECENTS |
            Root.FLAG_SUPPORTS_SEARCH);

    // COLUMN_TITLE is the root title (e.g. Gallery, Drive).
    row.add(Root.COLUMN_TITLE, getContext().getString(R.string.title));

    // This document id cannot change after it's shared.
    row.add(Root.COLUMN_DOCUMENT_ID, getDocIdForFile(baseDir));

    // The child MIME types are used to filter the roots and only present to the
    // user those roots that contain the desired type somewhere in their file hierarchy.
    row.add(Root.COLUMN_MIME_TYPES, getChildMimeTypes(baseDir));
    row.add(Root.COLUMN_AVAILABLE_BYTES, baseDir.getFreeSpace());
    row.add(Root.COLUMN_ICON, R.drawable.ic_launcher);

    return result;
}
```

If your document provider connects to a dynamic set of roots---for example, to a USB device that might be disconnected or an account that the user can sign out from---you can update the document UI to stay in sync with those changes using the[ContentResolver.notifyChange()](https://developer.android.com/reference/android/content/ContentResolver#notifyChange(android.net.Uri, android.database.ContentObserver))method, as shown in the following code snippet.  

### Kotlin

```kotlin
val rootsUri: Uri = DocumentsContract.buildRootsUri(BuildConfig.DOCUMENTS_AUTHORITY)
context.contentResolver.notifyChange(rootsUri, null)
```

### Java

```java
Uri rootsUri = DocumentsContract.buildRootsUri(BuildConfig.DOCUMENTS_AUTHORITY);
context.getContentResolver().notifyChange(rootsUri, null);
```

### List documents in the provider

Your implementation of[queryChildDocuments()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryChildDocuments(java.lang.String, java.lang.String[], android.os.Bundle))must return a[Cursor](https://developer.android.com/reference/android/database/Cursor)that points to all the files in the specified directory, using columns defined in[DocumentsContract.Document](https://developer.android.com/reference/android/provider/DocumentsContract.Document).

This method gets called when the user chooses your root in the picker UI. The method retrieves the children of the document ID specified by[COLUMN_DOCUMENT_ID](https://developer.android.com/reference/android/provider/DocumentsContract.Root#COLUMN_DOCUMENT_ID). The system then calls this method any time the user selects a subdirectory within your documents provider.

This snippet makes a new cursor with the requested columns, then adds information about every immediate child in the parent directory to the cursor. A child can be an image, another directory---any file:  

### Kotlin

```kotlin
override fun queryChildDocuments(
        parentDocumentId: String?,
        projection: Array<out String>?,
        sortOrder: String?
): Cursor {
    return MatrixCursor(resolveDocumentProjection(projection)).apply {
        val parent: File = getFileForDocId(parentDocumentId)
        parent.listFiles()
                .forEach { file ->
                    includeFile(this, null, file)
                }
    }
}
```

### Java

```java
@Override
public Cursor queryChildDocuments(String parentDocumentId, String[] projection,
                              String sortOrder) throws FileNotFoundException {

    final MatrixCursor result = new
            MatrixCursor(resolveDocumentProjection(projection));
    final File parent = getFileForDocId(parentDocumentId);
    for (File file : parent.listFiles()) {
        // Adds the file's display name, MIME type, size, and so on.
        includeFile(result, null, file);
    }
    return result;
}
```

### Get document information

Your implementation of[queryDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryDocument(java.lang.String, java.lang.String[]))must return a[Cursor](https://developer.android.com/reference/android/database/Cursor)that points to the specified file, using columns defined in[DocumentsContract.Document](https://developer.android.com/reference/android/provider/DocumentsContract.Document).

The[queryDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryDocument(java.lang.String, java.lang.String[]))method returns the same information that was passed in[queryChildDocuments()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryChildDocuments(java.lang.String, java.lang.String[], android.os.Bundle)), but for a specific file:  

### Kotlin

```kotlin
override fun queryDocument(documentId: String?, projection: Array<out String>?): Cursor {
    // Create a cursor with the requested projection, or the default projection.
    return MatrixCursor(resolveDocumentProjection(projection)).apply {
        includeFile(this, documentId, null)
    }
}
```

### Java

```java
@Override
public Cursor queryDocument(String documentId, String[] projection) throws
        FileNotFoundException {

    // Create a cursor with the requested projection, or the default projection.
    final MatrixCursor result = new
            MatrixCursor(resolveDocumentProjection(projection));
    includeFile(result, documentId, null);
    return result;
}
```

Your document provider can also provide thumbnails for a document by overriding the[DocumentsProvider.openDocumentThumbnail()](https://developer.android.com/reference/android/provider/DocumentsProvider#openDocumentThumbnail(java.lang.String, android.graphics.Point, android.os.CancellationSignal))method and adding the[FLAG_SUPPORTS_THUMBNAIL](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_THUMBNAIL)flag to the supported files. The following code snippet provides an example of how to implement the[DocumentsProvider.openDocumentThumbnail()](https://developer.android.com/reference/android/provider/DocumentsProvider#openDocumentThumbnail(java.lang.String, android.graphics.Point, android.os.CancellationSignal)).  

### Kotlin

```kotlin
override fun openDocumentThumbnail(
        documentId: String?,
        sizeHint: Point?,
        signal: CancellationSignal?
): AssetFileDescriptor {
    val file = getThumbnailFileForDocId(documentId)
    val pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
    return AssetFileDescriptor(pfd, 0, AssetFileDescriptor.UNKNOWN_LENGTH)
}
```

### Java

```java
@Override
public AssetFileDescriptor openDocumentThumbnail(String documentId, Point sizeHint,
                                                     CancellationSignal signal)
        throws FileNotFoundException {

    final File file = getThumbnailFileForDocId(documentId);
    final ParcelFileDescriptor pfd =
        ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    return new AssetFileDescriptor(pfd, 0, AssetFileDescriptor.UNKNOWN_LENGTH);
}
```

**Caution** : A document provider should not return thumbnail images more than double the size specified by the`sizeHint`parameter.

### Open a document

You must implement[openDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#openDocument(java.lang.String, java.lang.String, android.os.CancellationSignal))to return a[ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor)representing the specified file. Other apps can use the returned[ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor)to stream data. The system calls this method after the user selects a file, and the client app requests access to it by calling[openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String)). For example:  

### Kotlin

```kotlin
override fun openDocument(
        documentId: String,
        mode: String,
        signal: CancellationSignal
): ParcelFileDescriptor {
    Log.v(TAG, "openDocument, mode: $mode")
    // It's OK to do network operations in this method to download the document,
    // as long as you periodically check the CancellationSignal. If you have an
    // extremely large file to transfer from the network, a better solution may
    // be pipes or sockets (see ParcelFileDescriptor for helper methods).

    val file: File = getFileForDocId(documentId)
    val accessMode: Int = ParcelFileDescriptor.parseMode(mode)

    val isWrite: Boolean = mode.contains("w")
    return if (isWrite) {
        val handler = Handler(context.mainLooper)
        // Attach a close listener if the document is opened in write mode.
        try {
            ParcelFileDescriptor.open(file, accessMode, handler) {
                // Update the file with the cloud server. The client is done writing.
                Log.i(TAG, "A file with id $documentId has been closed! Time to update the server.")
            }
        } catch (e: IOException) {
            throw FileNotFoundException(
                    "Failed to open document with id $documentId and mode $mode"
            )
        }
    } else {
        ParcelFileDescriptor.open(file, accessMode)
    }
}
```

### Java

```java
@Override
public ParcelFileDescriptor openDocument(final String documentId,
                                         final String mode,
                                         CancellationSignal signal) throws
        FileNotFoundException {
    Log.v(TAG, "openDocument, mode: " + mode);
    // It's OK to do network operations in this method to download the document,
    // as long as you periodically check the CancellationSignal. If you have an
    // extremely large file to transfer from the network, a better solution may
    // be pipes or sockets (see ParcelFileDescriptor for helper methods).

    final File file = getFileForDocId(documentId);
    final int accessMode = ParcelFileDescriptor.parseMode(mode);

    final boolean isWrite = (mode.indexOf('w') != -1);
    if(isWrite) {
        // Attach a close listener if the document is opened in write mode.
        try {
            Handler handler = new Handler(getContext().getMainLooper());
            return ParcelFileDescriptor.open(file, accessMode, handler,
                        new ParcelFileDescriptor.OnCloseListener() {
                @Override
                public void onClose(IOException e) {

                    // Update the file with the cloud server. The client is done
                    // writing.
                    Log.i(TAG, "A file with id " +
                    documentId + " has been closed! Time to " +
                    "update the server.");
                }

            });
        } catch (IOException e) {
            throw new FileNotFoundException("Failed to open document with id"
            + documentId + " and mode " + mode);
        }
    } else {
        return ParcelFileDescriptor.open(file, accessMode);
    }
}
```

If your document provider streams files or handles complicated data structures, consider implementing the[createReliablePipe()](https://developer.android.com/reference/android/os/ParcelFileDescriptor#createReliablePipe())or[createReliableSocketPair()](https://developer.android.com/reference/android/os/ParcelFileDescriptor#createReliableSocketPair())methods. Those methods allow you to create a pair of[ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor)objects, where you can return one and send the other via an[ParcelFileDescriptor.AutoCloseOutputStream](https://developer.android.com/reference/android/os/ParcelFileDescriptor.AutoCloseOutputStream)or[ParcelFileDescriptor.AutoCloseInputStream](https://developer.android.com/reference/android/os/ParcelFileDescriptor.AutoCloseInputStream).

### Support recent documents and search

You can provide a list of recently modified documents under the root of your document provider by overriding the[queryRecentDocuments()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRecentDocuments(java.lang.String, java.lang.String[]))method and returning[FLAG_SUPPORTS_RECENTS](https://developer.android.com/reference/android/provider/DocumentsContract.Root#FLAG_SUPPORTS_RECENTS), The following code snippet shows an example of how to implement the[queryRecentDocuments()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRecentDocuments(java.lang.String, java.lang.String[]))methods.  

### Kotlin

```kotlin
override fun queryRecentDocuments(rootId: String?, projection: Array<out String>?): Cursor {
    // This example implementation walks a
    // local file structure to find the most recently
    // modified files.  Other implementations might
    // include making a network call to query a
    // server.

    // Create a cursor with the requested projection, or the default projection.
    val result = MatrixCursor(resolveDocumentProjection(projection))

    val parent: File = getFileForDocId(rootId)

    // Create a queue to store the most recent documents,
    // which orders by last modified.
    val lastModifiedFiles = PriorityQueue(
            5,
            Comparator<File> { i, j ->
                Long.compare(i.lastModified(), j.lastModified())
            }
    )

    // Iterate through all files and directories
    // in the file structure under the root.  If
    // the file is more recent than the least
    // recently modified, add it to the queue,
    // limiting the number of results.
    val pending : MutableList<File> = mutableListOf()

    // Start by adding the parent to the list of files to be processed
    pending.add(parent)

    // Do while we still have unexamined files
    while (pending.isNotEmpty()) {
        // Take a file from the list of unprocessed files
        val file: File = pending.removeAt(0)
        if (file.isDirectory) {
            // If it's a directory, add all its children to the unprocessed list
            pending += file.listFiles()
        } else {
            // If it's a file, add it to the ordered queue.
            lastModifiedFiles.add(file)
        }
    }

    // Add the most recent files to the cursor,
    // not exceeding the max number of results.
    for (i in 0 until Math.min(MAX_LAST_MODIFIED + 1, lastModifiedFiles.size)) {
        val file: File = lastModifiedFiles.remove()
        includeFile(result, null, file)
    }
    return result
}
```

### Java

```java
@Override
public Cursor queryRecentDocuments(String rootId, String[] projection)
        throws FileNotFoundException {

    // This example implementation walks a
    // local file structure to find the most recently
    // modified files.  Other implementations might
    // include making a network call to query a
    // server.

    // Create a cursor with the requested projection, or the default projection.
    final MatrixCursor result =
        new MatrixCursor(resolveDocumentProjection(projection));

    final File parent = getFileForDocId(rootId);

    // Create a queue to store the most recent documents,
    // which orders by last modified.
    PriorityQueue lastModifiedFiles =
        new PriorityQueue(5, new Comparator() {

        public int compare(File i, File j) {
            return Long.compare(i.lastModified(), j.lastModified());
        }
    });

    // Iterate through all files and directories
    // in the file structure under the root.  If
    // the file is more recent than the least
    // recently modified, add it to the queue,
    // limiting the number of results.
    final LinkedList pending = new LinkedList();

    // Start by adding the parent to the list of files to be processed
    pending.add(parent);

    // Do while we still have unexamined files
    while (!pending.isEmpty()) {
        // Take a file from the list of unprocessed files
        final File file = pending.removeFirst();
        if (file.isDirectory()) {
            // If it's a directory, add all its children to the unprocessed list
            Collections.addAll(pending, file.listFiles());
        } else {
            // If it's a file, add it to the ordered queue.
            lastModifiedFiles.add(file);
        }
    }

    // Add the most recent files to the cursor,
    // not exceeding the max number of results.
    for (int i = 0; i < Math.min(MAX_LAST_MODIFIED + 1, lastModifiedFiles.size()); i++) {
        final File file = lastModifiedFiles.remove();
        includeFile(result, null, file);
    }
    return result;
}
```

You can get the complete code for the snippet above by downloading the[StorageProvider](https://github.com/android/storage-samples/tree/main/StorageProvider)code sample.

### Support document creation

You can allow client apps to create files within your document provider. If a client app sends an[ACTION_CREATE_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT)intent, your document provider can allow that client app to create new documents within the document provider.

To support document creation, your root needs to have the[FLAG_SUPPORTS_CREATE](https://developer.android.com/reference/android/provider/DocumentsContract.Root#FLAG_SUPPORTS_CREATE)flag. Directories that allow new files to be created within them need to have the[FLAG_DIR_SUPPORTS_CREATE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_DIR_SUPPORTS_CREATE)flag.

Your document provider also needs to implement the[createDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#createDocument(java.lang.String, java.lang.String, java.lang.String))method. When a user selects a directory within your document provider to save a new file, the document provider receives a call to[createDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#createDocument(java.lang.String, java.lang.String, java.lang.String)). Inside the implementation of the[createDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#createDocument(java.lang.String, java.lang.String, java.lang.String))method, you return a new[COLUMN_DOCUMENT_ID](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_DOCUMENT_ID)for the file. The client app can then use that ID to get a handle for the file and, ultimately, call[openDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#openDocument(java.lang.String, java.lang.String, android.os.CancellationSignal))to write to the new file.

The following code snippet demonstrates how to create a new file within a document provider.  

### Kotlin

```kotlin
override fun createDocument(documentId: String?, mimeType: String?, displayName: String?): String {
    val parent: File = getFileForDocId(documentId)
    val file: File = try {
        File(parent.path, displayName).apply {
            createNewFile()
            setWritable(true)
            setReadable(true)
        }
    } catch (e: IOException) {
        throw FileNotFoundException(
                "Failed to create document with name $displayName and documentId $documentId"
        )
    }

    return getDocIdForFile(file)
}
```

### Java

```java
@Override
public String createDocument(String documentId, String mimeType, String displayName)
        throws FileNotFoundException {

    File parent = getFileForDocId(documentId);
    File file = new File(parent.getPath(), displayName);
    try {
        file.createNewFile();
        file.setWritable(true);
        file.setReadable(true);
    } catch (IOException e) {
        throw new FileNotFoundException("Failed to create document with name " +
                displayName +" and documentId " + documentId);
    }
    return getDocIdForFile(file);
}
```

You can get the complete code for the snippet above by downloading the[StorageProvider](https://github.com/android/storage-samples/tree/main/StorageProvider)code sample.

### Support document management features

In addition to opening, creating, and viewing files, your document provider can also allow client apps the ability to rename, copy, move, and delete files. To add document management functionality to your document provider, add a flag to the document's[COLUMN_FLAGS](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS)column to indicate the supported functionality. You also need to implement the corresponding method of the[DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider)class.

The following table provides the[COLUMN_FLAGS](https://developer.android.com/reference/android/provider/DocumentsContract.Document#COLUMN_FLAGS)flag and[DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider)method that a documents provider needs to implement to expose specific features.

|                                Feature                                 |                                                               Flag                                                               |                                                                             Method                                                                              |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delete a file                                                          | [FLAG_SUPPORTS_DELETE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_DELETE) | [deleteDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#deleteDocument(java.lang.String))                                 |
| Rename a file                                                          | [FLAG_SUPPORTS_RENAME](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_RENAME) | [renameDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#renameDocument(java.lang.String, java.lang.String))               |
| Copy a file to a new parent directory within the document provider     | [FLAG_SUPPORTS_COPY](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_COPY)     | [copyDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#copyDocument(java.lang.String, java.lang.String))                   |
| Move a file from one directory to another within the document provider | [FLAG_SUPPORTS_MOVE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_MOVE)     | [moveDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#moveDocument(java.lang.String, java.lang.String, java.lang.String)) |
| Remove a file from its parent directory                                | [FLAG_SUPPORTS_REMOVE](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_SUPPORTS_REMOVE) | [removeDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#removeDocument(java.lang.String, java.lang.String))               |

### Support virtual files and alternate file formats

[Virtual files](https://developer.android.com/guide/topics/providers/document-provider#virtual), a feature introduced in Android 7.0 (API level 24), allows document providers to provide viewing access to files that do not have a direct bytecode representation. To enable other apps to view virtual files, your document provider needs to produce an alternative openable file representation for the virtual files.

For example, imagine a document provider contains a file format that other apps cannot directly open, essentially a virtual file. When a client app sends an[ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)intent without the[CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE)category, then users can select these virtual files within the document provider for viewing. The document provider then returns the virtual file in a different, but openable, file format like an image. The client app can then open the virtual file for the user to view.

To declare that a document in the provider is virtual, you need to add the[FLAG_VIRTUAL_DOCUMENT](https://developer.android.com/reference/android/provider/DocumentsContract.Document#FLAG_VIRTUAL_DOCUMENT)flag to the file returned by the[queryDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryDocument(java.lang.String, java.lang.String[]))method. This flag alerts client apps that the file does not have a direct bytecode representation and cannot be directly opened.

If you declare that a file in your document provider is virtual, it is strongly recommended that you make it available in another MIME type like an image or a PDF. The document provider declares the alternate MIME types that it supports for viewing a virtual file by overriding the[getDocumentStreamTypes()](https://developer.android.com/reference/android/provider/DocumentsProvider#getDocumentStreamTypes(java.lang.String, java.lang.String))method. When client apps call the[getStreamTypes(android.net.Uri, java.lang.String)](https://developer.android.com/reference/android/content/ContentResolver#getStreamTypes(android.net.Uri, java.lang.String))method, the system calls the[getDocumentStreamTypes()](https://developer.android.com/reference/android/provider/DocumentsProvider#getDocumentStreamTypes(java.lang.String, java.lang.String))method of the document provider. The[getDocumentStreamTypes()](https://developer.android.com/reference/android/provider/DocumentsProvider#getDocumentStreamTypes(java.lang.String, java.lang.String))method then returns an array of alternate MIME types that the document provider supports for the file.

After the client determines that the document provider can produce the document in a viewable file format, the client app calls the[openTypedAssetFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openTypedAssetFileDescriptor(android.net.Uri, java.lang.String, android.os.Bundle, android.os.CancellationSignal))method, which internally calls the document provider's[openTypedDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#openTypedDocument(java.lang.String, java.lang.String, android.os.Bundle, android.os.CancellationSignal))method. The document provider returns the file to the client app in the requested file format.

The following code snippet demonstrates a simple implementation of the[getDocumentStreamTypes()](https://developer.android.com/reference/android/provider/DocumentsProvider#getDocumentStreamTypes(java.lang.String, java.lang.String))and[openTypedDocument()](https://developer.android.com/reference/android/provider/DocumentsProvider#openTypedDocument(java.lang.String, java.lang.String, android.os.Bundle, android.os.CancellationSignal))methods.  

### Kotlin

```kotlin
var SUPPORTED_MIME_TYPES : Array<String> = arrayOf("image/png", "image/jpg")
override fun openTypedDocument(
        documentId: String?,
        mimeTypeFilter: String,
        opts: Bundle?,
        signal: CancellationSignal?
): AssetFileDescriptor? {
    return try {
        // Determine which supported MIME type the client app requested.
        when(mimeTypeFilter) {
            "image/jpg" -> openJpgDocument(documentId)
            "image/png", "image/*", "*/*" -> openPngDocument(documentId)
            else -> throw IllegalArgumentException("Invalid mimeTypeFilter $mimeTypeFilter")
        }
    } catch (ex: Exception) {
        Log.e(TAG, ex.message)
        null
    }
}

override fun getDocumentStreamTypes(documentId: String, mimeTypeFilter: String): Array<String> {
    return when (mimeTypeFilter) {
        "*/*", "image/*" -> {
            // Return all supported MIME types if the client app
            // passes in '*/*' or 'image/*'.
            SUPPORTED_MIME_TYPES
        }
        else -> {
            // Filter the list of supported mime types to find a match.
            SUPPORTED_MIME_TYPES.filter { it == mimeTypeFilter }.toTypedArray()
        }
    }
}
```

### Java

```java
public static String[] SUPPORTED_MIME_TYPES = {"image/png", "image/jpg"};

@Override
public AssetFileDescriptor openTypedDocument(String documentId,
    String mimeTypeFilter,
    Bundle opts,
    CancellationSignal signal) {

    try {

        // Determine which supported MIME type the client app requested.
        if ("image/png".equals(mimeTypeFilter) ||
            "image/*".equals(mimeTypeFilter) ||
            "*/*".equals(mimeTypeFilter)) {

            // Return the file in the specified format.
            return openPngDocument(documentId);

        } else if ("image/jpg".equals(mimeTypeFilter)) {
            return openJpgDocument(documentId);
        } else {
            throw new IllegalArgumentException("Invalid mimeTypeFilter " + mimeTypeFilter);
        }

    } catch (Exception ex) {
        Log.e(TAG, ex.getMessage());
    } finally {
        return null;
    }
}

@Override
public String[] getDocumentStreamTypes(String documentId, String mimeTypeFilter) {

    // Return all supported MIME tyupes if the client app
    // passes in '*/*' or 'image/*'.
    if ("*/*".equals(mimeTypeFilter) ||
        "image/*".equals(mimeTypeFilter)) {
        return SUPPORTED_MIME_TYPES;
    }

    ArrayList requestedMimeTypes = new ArrayList&lt;&gt;();

    // Iterate over the list of supported mime types to find a match.
    for (int i=0; i &lt; SUPPORTED_MIME_TYPES.length; i++) {
        if (SUPPORTED_MIME_TYPES[i].equals(mimeTypeFilter)) {
            requestedMimeTypes.add(SUPPORTED_MIME_TYPES[i]);
        }
    }
    return (String[])requestedMimeTypes.toArray();
}
```

## Security

Suppose your document provider is a password-protected cloud storage service and you want to make sure that users are logged in before you start sharing their files. What should your app do if the user is not logged in? The solution is to return zero roots in your implementation of[queryRoots()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRoots(java.lang.String[])). That is, an empty root cursor:  

### Kotlin

```kotlin
override fun queryRoots(projection: Array<out String>): Cursor {
...
    // If user is not logged in, return an empty root cursor.  This removes our
    // provider from the list entirely.
    if (!isUserLoggedIn()) {
        return result
    }
```

### Java

```java
public Cursor queryRoots(String[] projection) throws FileNotFoundException {
...
    // If user is not logged in, return an empty root cursor.  This removes our
    // provider from the list entirely.
    if (!isUserLoggedIn()) {
        return result;
}
```

The other step is to call`getContentResolver().notifyChange()`. Remember the[DocumentsContract](https://developer.android.com/reference/android/provider/DocumentsContract)? We're using it to make this URI. The following snippet tells the system to query the roots of your document provider whenever the user's login status changes. If the user is not logged in, a call to[queryRoots()](https://developer.android.com/reference/android/provider/DocumentsProvider#queryRoots(java.lang.String[]))returns an empty cursor, as shown above. This ensures that a provider's documents are only available if the user is logged into the provider.  

### Kotlin

```kotlin
private fun onLoginButtonClick() {
    loginOrLogout()
    getContentResolver().notifyChange(
        DocumentsContract.buildRootsUri(AUTHORITY),
        null
    )
}
```

### Java

```java
private void onLoginButtonClick() {
    loginOrLogout();
    getContentResolver().notifyChange(DocumentsContract
            .buildRootsUri(AUTHORITY), null);
}
```

For sample code related to this page, refer to:

- [StorageProvider](https://github.com/android/storage-samples/tree/main/StorageProvider)
- [StorageClient](https://github.com/android/storage-samples/tree/main/StorageClient)

For videos related to this page, refer to:

- [DevBytes: Android 4.4 Storage Access Framework: Provider](http://www.youtube.com/watch?v=zxHVeXbK1P4)
- [Storage Access Framework: Building a DocumentsProvider](https://www.youtube.com/watch?v=LaMUvV-gOfE)
- [Virtual Files in the Storage Access Framework](https://www.youtube.com/watch?v=4h7yCZt231Y)

For additional related information, refer to:

- [Building a DocumentsProvider](https://medium.com/google-developers/building-a-documentsprovider-f7f2fb38e86a#.cq3fc969k)
- [Open Files using Storage Access Framework](https://developer.android.com/guide/topics/providers/document-provider)
- [Content Provider Basics](https://developer.android.com/guide/topics/providers/content-provider-basics)