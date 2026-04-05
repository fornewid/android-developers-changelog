---
title: Retrieving file information  |  App data and files  |  Android Developers
url: https://developer.android.com/training/secure-file-sharing/retrieve-info
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Retrieving file information Stay organized with collections Save and categorize content based on your preferences.



Before a client app tries to work with a file for which it has a content URI, the app can
request information about the file from the server app, including the file's data type and
file size. The data type helps the client app to determine if it can handle the file, and the
file size helps the client app set up buffering and caching for the file.

This lesson demonstrates how to query the server app's
`FileProvider` to retrieve a file's MIME type and size.

## Retrieve a file's MIME type

A file's data type indicates to the client app how it should handle the file's contents. To get
the data type of a shared file given its content URI, the client app calls
`ContentResolver.getType()`. This method returns
the file's MIME type. By default, a
`FileProvider` determines the file's MIME type from its
filename extension.

The following code snippet demonstrates how a client app retrieves the MIME type of a file once
the server app has returned the content URI to the client:

### Kotlin

```
    ...
    /*
     * Get the file's content URI from the incoming Intent, then
     * get the file's MIME type
     */
    val mimeType: String? = returnIntent.data?.let { returnUri ->
        contentResolver.getType(returnUri)
    }
    ...
```

### Java

```
    ...
    /*
     * Get the file's content URI from the incoming Intent, then
     * get the file's MIME type
     */
    Uri returnUri = returnIntent.getData();
    String mimeType = getContentResolver().getType(returnUri);
    ...
```

## Retrieve a file's name and size

The `FileProvider` class has a default implementation of the
`query()` method that returns the
name and size of the file associated with a content URI in a
`Cursor`. The default implementation returns two columns:

`DISPLAY_NAME`
:   The file's name, as a `String`. This value is the same as the value returned
    by `File.getName()`.

`SIZE`
:   The size of the file in bytes, as a `long` This value is the same as the value
    returned by `File.length()`

The client app can get both the `DISPLAY_NAME` and `SIZE` for a file by setting all
of the arguments of `query()` to
`null` except for the content URI. For example, this code snippet retrieves a file's
`DISPLAY_NAME` and
`SIZE` and displays each one in separate
`TextView`:

### Kotlin

```
    /*
     * Get the file's content URI from the incoming Intent,
     * then query the server app to get the file's display name
     * and size.
     */
    returnIntent.data?.let { returnUri ->
        contentResolver.query(returnUri, null, null, null, null)
    }?.use { cursor ->
        /*
         * Get the column indexes of the data in the Cursor,
         * move to the first row in the Cursor, get the data,
         * and display it.
         */
        val nameIndex = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME)
        val sizeIndex = cursor.getColumnIndex(OpenableColumns.SIZE)
        cursor.moveToFirst()
        findViewById<TextView>(R.id.filename_text).text = cursor.getString(nameIndex)
        findViewById<TextView>(R.id.filesize_text).text = cursor.getLong(sizeIndex).toString()
        ...
    }
```

### Java

```
    ...
    /*
     * Get the file's content URI from the incoming Intent,
     * then query the server app to get the file's display name
     * and size.
     */
    Uri returnUri = returnIntent.getData();
    Cursor returnCursor =
            getContentResolver().query(returnUri, null, null, null, null);
    /*
     * Get the column indexes of the data in the Cursor,
     * move to the first row in the Cursor, get the data,
     * and display it.
     */
    int nameIndex = returnCursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
    int sizeIndex = returnCursor.getColumnIndex(OpenableColumns.SIZE);
    returnCursor.moveToFirst();
    TextView nameView = (TextView) findViewById(R.id.filename_text);
    TextView sizeView = (TextView) findViewById(R.id.filesize_text);
    nameView.setText(returnCursor.getString(nameIndex));
    sizeView.setText(Long.toString(returnCursor.getLong(sizeIndex)));
    ...
```

For additional related information, refer to:

* [Retrieving Data from the Provider](/guide/topics/providers/content-provider-basics#SimpleQuery)

[Previous

arrow\_back

Requesting a shared file](/training/secure-file-sharing/request-file)