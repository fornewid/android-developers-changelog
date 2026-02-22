---
title: https://developer.android.com/training/data-storage/shared/media
url: https://developer.android.com/training/data-storage/shared/media
source: md.txt
---

To provide a more enriched user experience, many apps let users contribute
and access media that's available on an external storage volume. The framework
provides an optimized index into media collections, called the *media store*,
that lets users retrieve and update these media files more easily. Even
after your app is uninstalled, these files remain on the user's device.
| **Note:** If your app works with media files that provide value to the user only within your app, it's best to store them in [app-specific directories within
| external storage](https://developer.android.com/training/data-storage/app-specific#media).

## Photo picker

As an alternative to using the media store, the Android photo picker tool
provides a safe, built-in way for users to select media files without needing
to grant your app access to their entire media library. This is only available
on supported devices. For more information, see the
[photo picker](https://developer.android.com/training/data-storage/shared/photopicker) guide.

## Media store

To interact with the media store abstraction, use a
[`ContentResolver`](https://developer.android.com/reference/android/content/ContentResolver) object that you
retrieve from your app's context:  

### Kotlin

```kotlin
val projection = arrayOf(media-database-columns-to-retrieve)
val selection = sql-where-clause-with-placeholder-variables
val selectionArgs = values-of-placeholder-variables
val sortOrder = sql-order-by-clause

applicationContext.contentResolver.query(
    MediaStore.media-type.Media.EXTERNAL_CONTENT_URI,
    projection,
    selection,
    selectionArgs,
    sortOrder
)?.use { cursor ->
    while (cursor.moveToNext()) {
        // Use an ID column from the projection to get
        // a URI representing the media item itself.
    }
}
```

### Java

```java
String[] projection = new String[] {
        media-database-columns-to-retrieve
};
String selection = sql-where-clause-with-placeholder-variables;
String[] selectionArgs = new String[] {
        values-of-placeholder-variables
};
String sortOrder = sql-order-by-clause;

Cursor cursor = getApplicationContext().getContentResolver().query(
    MediaStore.media-type.Media.EXTERNAL_CONTENT_URI,
    projection,
    selection,
    selectionArgs,
    sortOrder
);

while (cursor.moveToNext()) {
    // Use an ID column from the projection to get
    // a URI representing the media item itself.
}
```

The system automatically scans an external storage volume and adds media files
to the following well-defined collections:

- **Images,** including photographs and screenshots, which are stored in the `DCIM/` and `Pictures/` directories. The system adds these files to the [`MediaStore.Images`](https://developer.android.com/reference/android/provider/MediaStore.Images) table.
- **Videos,** which are stored in the `DCIM/`, `Movies/`, and `Pictures/` directories. The system adds these files to the [`MediaStore.Video`](https://developer.android.com/reference/android/provider/MediaStore.Video) table.
- **Audio files,** which are stored in the `Alarms/`, `Audiobooks/`, `Music/`, `Notifications/`, `Podcasts/`, and `Ringtones/` directories. Additionally, the system recognizes audio playlists that are in the `Music/` or `Movies/` directories as well as voice recordings that are in the `Recordings/` directory. The system adds these files to the [`MediaStore.Audio`](https://developer.android.com/reference/android/provider/MediaStore.Audio) table. *The `Recordings/` directory isn't available on Android 11 (API level 30) and
  lower.*
- **Downloaded files,** which are stored in the `Download/` directory. On devices that run Android 10 (API level 29) and higher, these files are stored in the [`MediaStore.Downloads`](https://developer.android.com/reference/android/provider/MediaStore.Downloads) table. *This table isn't available on Android 9 (API level 28) and lower.*

The media store also includes a collection called
[`MediaStore.Files`](https://developer.android.com/reference/android/provider/MediaStore.Files). Its contents
depend on whether your app uses [scoped
storage](https://developer.android.com/training/data-storage#scoped-storage), available on apps that target
Android 10 or higher.

- If scoped storage is enabled, the collection shows only the photos, videos, and audio files that your app has created. Most developers don't need to use `MediaStore.Files` to view media files from other apps, but if you have a specific requirement to do so, you can declare the `READ_EXTERNAL_STORAGE` permission. We recommend, however, that you use the `MediaStore` APIs to [open files](https://developer.android.com/training/data-storage/shared/media#open-file) that your app hasn't created.
- If scoped storage is unavailable or not being used, the collection shows all types of media files.

## Request necessary permissions

Before performing operations on media files, make sure your app has declared the
permissions that it needs to access these files. Be careful, however, not to
declare permissions that your app doesn't need or use.

### Storage permissions

Whether your app needs permissions to access storage depends on whether it accesses
only its own media files or files created by other apps.

#### Access your own media files

On devices that run Android 10 or higher, you don't need
storage-related permissions to access and modify media files that
[your app owns](https://developer.android.com/training/data-storage/shared/media#app-attribution), including files in the `MediaStore.Downloads`
collection. If you're developing a camera app, for example, you don't need to
request storage-related permissions to access the photos it takes, because your
app owns the images that you're writing to the media store.

#### Access other apps' media files

To access media files that other apps create, you must declare the
appropriate storage-related permissions, and the files must reside in one of the
following media collections:

- [`MediaStore.Images`](https://developer.android.com/reference/android/provider/MediaStore.Images)
- [`MediaStore.Video`](https://developer.android.com/reference/android/provider/MediaStore.Video)
- [`MediaStore.Audio`](https://developer.android.com/reference/android/provider/MediaStore.Audio)

As long as a file is viewable from the `MediaStore.Images`,
`MediaStore.Video`, or `MediaStore.Audio` queries, it's also viewable using the
[`MediaStore.Files`](https://developer.android.com/reference/android/provider/MediaStore.Files) query.

The following code snippet demonstrates how to declare the appropriate storage
permissions:  

```xml
<!-- Required only if your app needs to access images or photos
     that other apps created. -->
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />

<!-- Required only if your app needs to access videos
     that other apps created. -->
<uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />

<!-- Required only if your app needs to access audio files
     that other apps created. -->
<uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />

<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>

<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
                 android:maxSdkVersion="29" />
```
| **Note:** If you request both the `READ_MEDIA_IMAGES` permission and the `READ_MEDIA_VIDEO` permission at the same time, the system shows a single runtime permission dialog that mentions both permissions.

#### Extra permissions needed for apps running on legacy devices

If your app is used on a device that runs Android 9 or lower, or if
your app has temporarily [opted out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage), you must
request the
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
permission to access any media file. If you want to modify media files, you must
request the
[`WRITE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)
permission, as well.

#### Storage Access Framework required for accessing other apps' downloads

If your app wants to access a file within the `MediaStore.Downloads` collection
that your app didn't create, you must use the Storage Access Framework. To learn
more about how to use this framework, see [Access documents and other files from
shared storage](https://developer.android.com/training/data-storage/shared/documents-files).

### Media location permission

If your app targets Android 10 (API level 29) or higher and needs
to retrieve unredacted EXIF metadata from photos, you need to declare the
[`ACCESS_MEDIA_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION)
permission in your app's manifest, then request this permission at runtime.
| **Caution:** Because you request the `ACCESS_MEDIA_LOCATION` permission at runtime, there is no guarantee that your app has access to unredacted EXIF metadata from photos. Your app requires explicit user consent to gain access to this information.

## Check for updates to the media store

To access media files more reliably, particularly if your app caches URIs or
data from the media store, check whether the media store version has changed
compared to when you last synced your media data. To perform this check for
updates, call
[`getVersion()`](https://developer.android.com/reference/android/provider/MediaStore#getVersion(android.content.Context,%20java.lang.String)).
The returned version is a unique string that changes whenever the media store
changes substantially. If the returned version is different from the last synced
version, rescan and resync your app's media cache.

Complete this check at app process startup time. There's no need to check the
version each time you query the media store.

Don't assume any implementation details regarding the version number.
| **Note:** The media store version number doesn't change as a result of app-side changes, such as when an app [adds a media file](https://developer.android.com/training/data-storage/shared/media#add-item). There's a separate method to help you [detect updates to media files](https://developer.android.com/training/data-storage/shared/media#detect-updates-media-files).

## Query a media collection

To find media that satisfies a particular set of conditions, such as a duration
of 5 minutes or longer, use a SQL-like selection statement similar to the one
shown in the following code snippet:  

### Kotlin

```kotlin
// Need the READ_EXTERNAL_STORAGE permission if accessing video files that your
// app didn't create.

// Container for information about each video.
data class Video(val uri: Uri,
    val name: String,
    val duration: Int,
    val size: Int
)
val videoList = mutableListOf<Video>()

val collection =
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        MediaStore.Video.Media.getContentUri(
            MediaStore.VOLUME_EXTERNAL
        )
    } else {
        MediaStore.Video.Media.EXTERNAL_CONTENT_URI
    }

val projection = arrayOf(
    MediaStore.Video.Media._ID,
    MediaStore.Video.Media.DISPLAY_NAME,
    MediaStore.Video.Media.DURATION,
    MediaStore.Video.Media.SIZE
)

// Show only videos that are at least 5 minutes in duration.
val selection = "${MediaStore.Video.Media.DURATION} >= ?"
val selectionArgs = arrayOf(
    TimeUnit.MILLISECONDS.convert(5, TimeUnit.MINUTES).toString()
)

// Display videos in alphabetical order based on their display name.
val sortOrder = "${MediaStore.Video.Media.DISPLAY_NAME} ASC"

val query = ContentResolver.query(
    collection,
    projection,
    selection,
    selectionArgs,
    sortOrder
)
query?.use { cursor ->
    // Cache column indices.
    val idColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media._ID)
    val nameColumn =
            cursor.getColumnIndexOrThrow(MediaStore.Video.Media.DISPLAY_NAME)
    val durationColumn =
            cursor.getColumnIndexOrThrow(MediaStore.Video.Media.DURATION)
    val sizeColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media.SIZE)

    while (cursor.moveToNext()) {
        // Get values of columns for a given video.
        val id = cursor.getLong(idColumn)
        val name = cursor.getString(nameColumn)
        val duration = cursor.getInt(durationColumn)
        val size = cursor.getInt(sizeColumn)

        val contentUri: Uri = ContentUris.withAppendedId(
            MediaStore.Video.Media.EXTERNAL_CONTENT_URI,
            id
        )

        // Stores column values and the contentUri in a local object
        // that represents the media file.
        videoList += Video(contentUri, name, duration, size)
    }
}
```

### Java

```java
// Need the READ_EXTERNAL_STORAGE permission if accessing video files that your
// app didn't create.

// Container for information about each video.
class Video {
    private final Uri uri;
    private final String name;
    private final int duration;
    private final int size;

    public Video(Uri uri, String name, int duration, int size) {
        this.uri = uri;
        this.name = name;
        this.duration = duration;
        this.size = size;
    }
}
List<Video> videoList = new ArrayList<Video>();

Uri collection;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    collection = MediaStore.Video.Media.getContentUri(MediaStore.VOLUME_EXTERNAL);
} else {
    collection = MediaStore.Video.Media.EXTERNAL_CONTENT_URI;
}

String[] projection = new String[] {
    MediaStore.Video.Media._ID,
    MediaStore.Video.Media.DISPLAY_NAME,
    MediaStore.Video.Media.DURATION,
    MediaStore.Video.Media.SIZE
};
String selection = MediaStore.Video.Media.DURATION +
        " >= ?";
String[] selectionArgs = new String[] {
    String.valueOf(TimeUnit.MILLISECONDS.convert(5, TimeUnit.MINUTES));
};
String sortOrder = MediaStore.Video.Media.DISPLAY_NAME + " ASC";

try (Cursor cursor = getApplicationContext().getContentResolver().query(
    collection,
    projection,
    selection,
    selectionArgs,
    sortOrder
)) {
    // Cache column indices.
    int idColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media._ID);
    int nameColumn =
            cursor.getColumnIndexOrThrow(MediaStore.Video.Media.DISPLAY_NAME);
    int durationColumn =
            cursor.getColumnIndexOrThrow(MediaStore.Video.Media.DURATION);
    int sizeColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media.SIZE);

    while (cursor.moveToNext()) {
        // Get values of columns for a given video.
        long id = cursor.getLong(idColumn);
        String name = cursor.getString(nameColumn);
        int duration = cursor.getInt(durationColumn);
        int size = cursor.getInt(sizeColumn);

        Uri contentUri = ContentUris.withAppendedId(
                MediaStore.Video.Media.EXTERNAL_CONTENT_URI, id);

        // Stores column values and the contentUri in a local object
        // that represents the media file.
        videoList.add(new Video(contentUri, name, duration, size));
    }
}
```

When performing such a query in your app, keep the following in mind:

- Call the `query()` method in a worker thread.
- Cache the column indices so that you don't need to call [`getColumnIndexOrThrow()`](https://developer.android.com/reference/android/database/Cursor#getColumnIndexOrThrow(java.lang.String)) each time you process a row from the query result.
- Append the ID to the content URI as shown in this example.
- Devices that run Android 10 and higher require [column
  names that are defined](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns) in the `MediaStore` API. If a dependent library within your app expects a column name that's undefined in the API, such as `"MimeType"`, use [`CursorWrapper`](https://developer.android.com/reference/android/database/CursorWrapper) to dynamically translate the column name in your app's process.

## Load file thumbnails

If your app shows multiple media files and requests that the user choose one of
these files, it's more efficient to load preview
versions---or *thumbnails*---of the
files instead of the files themselves.

To load the thumbnail for a given media file, use
[`loadThumbnail()`](https://developer.android.com/reference/android/content/ContentResolver#loadThumbnail(android.net.Uri,%2520android.util.Size,%2520android.os.CancellationSignal))
and pass in the size of the thumbnail that you want to load, as shown in the
following code snippet:  

### Kotlin

```kotlin
// Load thumbnail of a specific media item.
val thumbnail: Bitmap =
        applicationContext.contentResolver.loadThumbnail(
        content-uri, Size(640, 480), null)
```

### Java

```java
// Load thumbnail of a specific media item.
Bitmap thumbnail =
        getApplicationContext().getContentResolver().loadThumbnail(
        content-uri, new Size(640, 480), null);
```

## Open a media file

The specific logic that you use to open a media file depends on whether the
media content is best represented as a file descriptor, a file stream, or a
direct file path.

### File descriptor

To open a media file using a file descriptor, use logic similar to that shown in
the following code snippet:  

### Kotlin

```kotlin
// Open a specific media item using ParcelFileDescriptor.
val resolver = applicationContext.contentResolver

// "rw" for read-and-write.
// "rwt" for truncating or overwriting existing file contents.
val readOnlyMode = "r"
resolver.openFileDescriptor(content-uri, readOnlyMode).use { pfd ->
    // Perform operations on "pfd".
}
```

### Java

```java
// Open a specific media item using ParcelFileDescriptor.
ContentResolver resolver = getApplicationContext()
        .getContentResolver();

// "rw" for read-and-write.
// "rwt" for truncating or overwriting existing file contents.
String readOnlyMode = "r";
try (ParcelFileDescriptor pfd =
        resolver.openFileDescriptor(content-uri, readOnlyMode)) {
    // Perform operations on "pfd".
} catch (IOException e) {
    e.printStackTrace();
}
```

### File stream

To open a media file using a file stream, use logic similar to that shown in
the following code snippet:  

### Kotlin

```kotlin
// Open a specific media item using InputStream.
val resolver = applicationContext.contentResolver
resolver.openInputStream(content-uri).use { stream ->
    // Perform operations on "stream".
}
```

### Java

```java
// Open a specific media item using InputStream.
ContentResolver resolver = getApplicationContext()
        .getContentResolver();
try (InputStream stream = resolver.openInputStream(content-uri)) {
    // Perform operations on "stream".
}
```

### Direct file paths

To help your app work more smoothly with third-party media libraries,
Android 11 (API level 30) and higher let you use APIs other than the
[`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API to access
media files from shared storage. You can instead access media files directly
using either of the following APIs:

- The [`File`](https://developer.android.com/reference/java/io/File) API
- Native libraries, such as `fopen()`

If you don't have any storage-related permissions, you can access files in your
[app-specific directory](https://developer.android.com/training/data-storage/app-specific) as well as [media
files that are attributed to your app](https://developer.android.com/training/data-storage/shared/media#app-attribution) using the `File` API.

If your app tries to access a file using the `File` API and it doesn't have the
necessary permissions, a
[`FileNotFoundException`](https://developer.android.com/reference/java/io/FileNotFoundException) occurs.

To access other files in shared storage on a device that runs Android 10 (API
level 29), we recommend that you [temporarily opt out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) by setting
[`requestLegacyExternalStorage`](https://developer.android.com/reference/kotlin/android/R.attr#requestLegacyExternalStorage:kotlin.Int)
to `true` in your app's manifest file. To access media files using
native files methods on Android 10, you must also request the
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
permission.

## Considerations when accessing media content

When accessing media content, keep in mind the considerations discussed in the
following sections.

### Cached data

If your app caches URIs or data from the media store, periodically [check for
updates to the media store](https://developer.android.com/training/data-storage/shared/media#check-for-updates). This check lets your
app-side, cached data stay in sync with the system-side, provider data.

### Performance

When you perform sequential reads of media files using direct file paths, the
performance is comparable to that of the
[`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API.

When you perform random reads and writes of media files using direct file paths,
however, the process can be up to twice as slow. In these situations, we
recommend using the `MediaStore` API instead.

### DATA column

When you access an existing media file, you can use the value of the
[`DATA`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DATA) column in
your logic. That's because this value has a valid file path. However, don't
assume that the file is always available. Be prepared to handle any file-based
I/O errors that occur.

To create or update a media file, on the other hand, don't use the value of the
`DATA` column. Instead, use the values of the
[`DISPLAY_NAME`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DISPLAY_NAME)
and
[`RELATIVE_PATH`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#RELATIVE_PATH)
columns.

### Storage volumes

Apps that target Android 10 or higher can access the unique name
that the system assigns to each external storage volume. This naming system
helps you efficiently organize and index content, and it gives you control over
where new media files are stored.

The following volumes are particularly useful to keep in mind:

- The [`VOLUME_EXTERNAL`](https://developer.android.com/reference/android/provider/MediaStore#VOLUME_EXTERNAL) volume provides a view of all shared storage volumes on the device. You can read the contents of this synthetic volume, but you cannot modify the contents.
- The [`VOLUME_EXTERNAL_PRIMARY`](https://developer.android.com/reference/android/provider/MediaStore#VOLUME_EXTERNAL_PRIMARY) volume represents the primary shared storage volume on the device. You can read and modify the contents of this volume.

You can discover other volumes by calling
[`MediaStore.getExternalVolumeNames()`](https://developer.android.com/reference/android/provider/MediaStore#getExternalVolumeNames(android.content.Context)):  

### Kotlin

```kotlin
val volumeNames: Set<String> = MediaStore.getExternalVolumeNames(context)
val firstVolumeName = volumeNames.iterator().next()
```

### Java

```java
Set<String> volumeNames = MediaStore.getExternalVolumeNames(context);
String firstVolumeName = volumeNames.iterator().next();
```

### Location where media was captured

Some photographs and videos contain location information in their metadata,
which shows the place where a photograph was taken or where a video was
recorded.

How you access this location information in your app depends on whether you
need to access location information for a photograph or for a video.

#### Photographs

If your app uses [scoped storage](https://developer.android.com/training/data-storage#scoped-storage), the
system hides location information by default. To access this information,
complete the following steps:

1. Request the [`ACCESS_MEDIA_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION) permission in your app's manifest.
2. From your `MediaStore` object, get the exact bytes of the photograph by
   calling
   [`setRequireOriginal()`](https://developer.android.com/reference/android/provider/MediaStore#setRequireOriginal(android.net.Uri))
   and passing in the URI of the photograph, as shown in the following code snippet:

   ### Kotlin

   ```kotlin
   val photoUri: Uri = Uri.withAppendedPath(
           MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
           cursor.getString(idColumnIndex)
   )

   // Get location data using the https://developer.android.com/jetpack/androidx/releases/exifinterface.
   // Exception occurs if ACCESS_MEDIA_LOCATION permission isn't granted.
   photoUri = MediaStore.setRequireOriginal(photoUri)
   contentResolver.openInputStream(photoUri)?.use { stream ->
       ExifInterface(stream).run {
           // If lat/long is null, fall back to the coordinates (0, 0).
           val latLong = latLong ?: doubleArrayOf(0.0, 0.0)
       }
   }
   ```

   ### Java

   ```java
   Uri photoUri = Uri.withAppendedPath(
           MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
           cursor.getString(idColumnIndex));

   final double[] latLong;

   // Get location data using the https://developer.android.com/jetpack/androidx/releases/exifinterface.
   // Exception occurs if ACCESS_MEDIA_LOCATION permission isn't granted.
   photoUri = MediaStore.setRequireOriginal(photoUri);
   InputStream stream = getContentResolver().openInputStream(photoUri);
   if (stream != null) {
       ExifInterface exifInterface = new ExifInterface(stream);
       double[] returnedLatLong = exifInterface.getLatLong();

       // If lat/long is null, fall back to the coordinates (0, 0).
       latLong = returnedLatLong != null ? returnedLatLong : new double[2];

       // Don't reuse the stream associated with
       // the instance of "ExifInterface".
       stream.close();
   } else {
       // Failed to load the stream, so return the coordinates (0, 0).
       latLong = new double[2];
   }
   ```

#### Videos

To access location information within a video's metadata, use the
[`MediaMetadataRetriever`](https://developer.android.com/reference/android/media/MediaMetadataRetriever)
class, as shown in the following code snippet. Your app doesn't need to request
any additional permissions to use this class.  

### Kotlin

```kotlin
val retriever = MediaMetadataRetriever()
val context = applicationContext

// Find the videos that are stored on a device by https://developer.android.com/training/data-storage/shared/media#query-collection.
val query = ContentResolver.query(
    collection,
    projection,
    selection,
    selectionArgs,
    sortOrder
)
query?.use { cursor ->
    val idColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media._ID)
    while (cursor.moveToNext()) {
        val id = cursor.getLong(idColumn)
        val videoUri: Uri = ContentUris.withAppendedId(
            MediaStore.Video.Media.EXTERNAL_CONTENT_URI,
            id
        )
        extractVideoLocationInfo(videoUri)
    }
}

private fun extractVideoLocationInfo(videoUri: Uri) {
    try {
        retriever.setDataSource(context, videoUri)
    } catch (e: RuntimeException) {
        Log.e(APP_TAG, "Cannot retrieve video file", e)
    }
    // Metadata uses a https://developer.android.com/reference/android/media/MediaMetadataRetriever#METADATA_KEY_LOCATION.
    val locationMetadata: String? =
            retriever.extractMetadata(MediaMetadataRetriever.METADATA_KEY_LOCATION)
}
```

### Java

```java
MediaMetadataRetriever retriever = new MediaMetadataRetriever();
Context context = getApplicationContext();

// Find the videos that are stored on a device by https://developer.android.com/training/data-storage/shared/media#query-collection.
try (Cursor cursor = context.getContentResolver().query(
    collection,
    projection,
    selection,
    selectionArgs,
    sortOrder
)) {
    int idColumn = cursor.getColumnIndexOrThrow(MediaStore.Video.Media._ID);
    while (cursor.moveToNext()) {
        long id = cursor.getLong(idColumn);
        Uri videoUri = ContentUris.withAppendedId(
                MediaStore.Video.Media.EXTERNAL_CONTENT_URI, id);
        extractVideoLocationInfo(videoUri);
    }
}

private void extractVideoLocationInfo(Uri videoUri) {
    try {
        retriever.setDataSource(context, videoUri);
    } catch (RuntimeException e) {
        Log.e(APP_TAG, "Cannot retrieve video file", e);
    }
    // Metadata uses a https://developer.android.com/reference/android/media/MediaMetadataRetriever#METADATA_KEY_LOCATION.
    String locationMetadata = retriever.extractMetadata(
            MediaMetadataRetriever.METADATA_KEY_LOCATION);
}
```

### Sharing

Some apps let users share media files with each other. For example, social
media apps let users share photos and videos with friends.

To share media files, use a `content://` URI, as recommended in the [guide to
creating a content provider](https://developer.android.com/guide/topics/providers/content-provider-creating).

### App attribution of media files

When [scoped storage](https://developer.android.com/training/data-storage#scoped-storage) is enabled for an
app that targets Android 10 or higher, the system *attributes* an
app to each media file, which determines the files that your app can access when
it hasn't requested any storage permissions. Each file can be attributed to only
one app. Therefore, if your app creates a media file that's stored in the
photos, videos, or audio files media collection, your app has access to the
file.

If the user uninstalls and reinstalls your app, however, you must request
[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
to access the files that your app originally created. This permission request is
required because the system considers the file to be attributed to the
previously installed version of the app, rather than the newly installed one.

When prompted for photo and video permissions by an app targeting SDK 36 or
higher on devices running Android 16 or higher, users who choose to limit access
to selected media will see any photos owned by the app pre-selected in the photo
picker. Users can deselect any of these pre-selected items, which will revoke
the app's access to those photos and videos.

## Add an item

To add a media item to an existing collection, use code similar to the
following. This code snippet accesses the `VOLUME_EXTERNAL_PRIMARY` volume
on devices that run Android 10 or higher. That's because, on these devices, you
can only modify the contents of a volume if it's the primary volume, as
described in the [Storage volumes](https://developer.android.com/training/data-storage/shared/media#storage-volume) section.  

### Kotlin

```kotlin
// Add a specific media item.
val resolver = applicationContext.contentResolver

// Find all audio files on the primary external storage device.
val audioCollection =
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        MediaStore.Audio.Media.getContentUri(
            MediaStore.VOLUME_EXTERNAL_PRIMARY
        )
    } else {
        MediaStore.Audio.Media.EXTERNAL_CONTENT_URI
    }

// Publish a new song.
val newSongDetails = ContentValues().apply {
    put(MediaStore.Audio.Media.DISPLAY_NAME, "My Song.mp3")
}

// Keep a handle to the new song's URI in case you need to modify it
// later.
val myFavoriteSongUri = resolver
        .insert(audioCollection, newSongDetails)
```

### Java

```java
// Add a specific media item.
ContentResolver resolver = getApplicationContext()
        .getContentResolver();

// Find all audio files on the primary external storage device.
Uri audioCollection;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    audioCollection = MediaStore.Audio.Media
            .getContentUri(MediaStore.VOLUME_EXTERNAL_PRIMARY);
} else {
    audioCollection = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
}

// Publish a new song.
ContentValues newSongDetails = new ContentValues();
newSongDetails.put(MediaStore.Audio.Media.DISPLAY_NAME,
        "My Song.mp3");

// Keep a handle to the new song's URI in case you need to modify it
// later.
Uri myFavoriteSongUri = resolver
        .insert(audioCollection, newSongDetails);
```

### Toggle pending status for media files

If your app performs potentially time-consuming operations, such as writing to
media files, it's useful to have exclusive access to the file as it's being
processed. On devices that run Android 10 or higher, your app can
get this exclusive access by setting the value of the
[`IS_PENDING`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#IS_PENDING)
flag to 1. Only your app can view the file until your app changes the value of
`IS_PENDING` back to 0.

The following code snippet builds on the previous code snippet. This
snippet shows how to use the `IS_PENDING` flag when storing a long song in the
directory corresponding to the `MediaStore.Audio` collection:  

### Kotlin

```kotlin
// Add a media item that other apps don't see until the item is
// fully written to the media store.
val resolver = applicationContext.contentResolver

// Find all audio files on the primary external storage device.
val audioCollection =
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        MediaStore.Audio.Media.getContentUri(
            MediaStore.VOLUME_EXTERNAL_PRIMARY
        )
    } else {
        MediaStore.Audio.Media.EXTERNAL_CONTENT_URI
    }

val songDetails = ContentValues().apply {
    put(MediaStore.Audio.Media.DISPLAY_NAME, "My Workout Playlist.mp3")
    put(MediaStore.Audio.Media.IS_PENDING, 1)
}

val songContentUri = resolver.insert(audioCollection, songDetails)

// "w" for write.
resolver.openFileDescriptor(songContentUri, "w", null).use { pfd ->
    // Write data into the pending audio file.
}

// Now that you're finished, release the "pending" status and let other apps
// play the audio track.
songDetails.clear()
songDetails.put(MediaStore.Audio.Media.IS_PENDING, 0)
resolver.update(songContentUri, songDetails, null, null)
```

### Java

```java
// Add a media item that other apps don't see until the item is
// fully written to the media store.
ContentResolver resolver = getApplicationContext()
        .getContentResolver();

// Find all audio files on the primary external storage device.
Uri audioCollection;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    audioCollection = MediaStore.Audio.Media
            .getContentUri(MediaStore.VOLUME_EXTERNAL_PRIMARY);
} else {
    audioCollection = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
}

ContentValues songDetails = new ContentValues();
songDetails.put(MediaStore.Audio.Media.DISPLAY_NAME,
        "My Workout Playlist.mp3");
songDetails.put(MediaStore.Audio.Media.IS_PENDING, 1);

Uri songContentUri = resolver
        .insert(audioCollection, songDetails);

// "w" for write.
try (ParcelFileDescriptor pfd =
        resolver.openFileDescriptor(songContentUri, "w", null)) {
    // Write data into the pending audio file.
}

// Now that you're finished, release the "pending" status and let other apps
// play the audio track.
songDetails.clear();
songDetails.put(MediaStore.Audio.Media.IS_PENDING, 0);
resolver.update(songContentUri, songDetails, null, null);
```

### Give a hint for file location

When your app stores media on a device running Android 10, by
default the media is organized based on its type. For example, by default new
image files are placed in the
[`Environment.DIRECTORY_PICTURES`](https://developer.android.com/reference/android/os/Environment#DIRECTORY_PICTURES)
directory, which corresponds to the
[`MediaStore.Images`](https://developer.android.com/reference/android/provider/MediaStore.Images) collection.

If your app is aware of a specific location where files can be stored, such
as a photo album called `Pictures/MyVacationPictures`, you can set
[`MediaColumns.RELATIVE_PATH`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#RELATIVE_PATH)
to provide the system a hint for where to store the newly written files.
| **Note:** Although it's possible to store general-purpose files in either the `Documents/` folder or the `Download/` folder, including non-media files, it's better to use the Storage Access Framework for these use cases.

## Update an item

To update a media file that your app owns, use code similar to the following:  

### Kotlin

```kotlin
// Updates an existing media item.
val mediaId = // MediaStore.Audio.Media._ID of item to update.
val resolver = applicationContext.contentResolver

// When performing a single item update, prefer using the ID.
val selection = "${MediaStore.Audio.Media._ID} = ?"

// By using selection + args you protect against improper escaping of // values.
val selectionArgs = arrayOf(mediaId.toString())

// Update an existing song.
val updatedSongDetails = ContentValues().apply {
    put(MediaStore.Audio.Media.DISPLAY_NAME, "My Favorite Song.mp3")
}

// Use the individual song's URI to represent the collection that's
// updated.
val numSongsUpdated = resolver.update(
        myFavoriteSongUri,
        updatedSongDetails,
        selection,
        selectionArgs)
```

### Java

```java
// Updates an existing media item.
long mediaId = // MediaStore.Audio.Media._ID of item to update.
ContentResolver resolver = getApplicationContext()
        .getContentResolver();

// When performing a single item update, prefer using the ID.
String selection = MediaStore.Audio.Media._ID + " = ?";

// By using selection + args you protect against improper escaping of
// values. Here, "song" is an in-memory object that caches the song's
// information.
String[] selectionArgs = new String[] { getId().toString() };

// Update an existing song.
ContentValues updatedSongDetails = new ContentValues();
updatedSongDetails.put(MediaStore.Audio.Media.DISPLAY_NAME,
        "My Favorite Song.mp3");

// Use the individual song's URI to represent the collection that's
// updated.
int numSongsUpdated = resolver.update(
        myFavoriteSongUri,
        updatedSongDetails,
        selection,
        selectionArgs);
```

If scoped storage is unavailable or not enabled, the process shown in the
preceding code snippet also works for files that your app doesn't own.
| **Note:** You can move files on disk during a call to [`update()`](https://developer.android.com/reference/android/content/ContentResolver#update(android.net.Uri,%2520android.content.ContentValues,%2520java.lang.String,%2520java.lang.String%5B%5D)) by changing `MediaColumns.RELATIVE_PATH` or [`MediaColumns.DISPLAY_NAME`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DISPLAY_NAME).

### Update in native code

If you need to write media files using native libraries, pass the file's
associated file descriptor from your Java-based or Kotlin-based code into your
native code.

The following code snippet shows how to pass a media object's file descriptor
into your app's native code:  

### Kotlin

```kotlin
val contentUri: Uri = ContentUris.withAppendedId(
        MediaStore.Audio.Media.EXTERNAL_CONTENT_URI,
        cursor.getLong(BaseColumns._ID))
val fileOpenMode = "r"
val parcelFd = resolver.openFileDescriptor(contentUri, fileOpenMode)
val fd = parcelFd?.detachFd()
// Pass the integer value "fd" into your native code. Remember to call
// close(2) on the file descriptor when you're done using it.
```

### Java

```java
Uri contentUri = ContentUris.withAppendedId(
        MediaStore.Audio.Media.EXTERNAL_CONTENT_URI,
        cursor.getLong(Integer.parseInt(BaseColumns._ID)));
String fileOpenMode = "r";
ParcelFileDescriptor parcelFd =
        resolver.openFileDescriptor(contentUri, fileOpenMode);
if (parcelFd != null) {
    int fd = parcelFd.detachFd();
    // Pass the integer value "fd" into your native code. Remember to call
    // close(2) on the file descriptor when you're done using it.
}
```

### Update other apps' media files

If your app uses [scoped storage](https://developer.android.com/training/data-storage#scoped-storage), it
ordinarily can't update a media file that a different app contributed to the
media store.

You can get user consent to modify the file, however, by catching
the [`RecoverableSecurityException`](https://developer.android.com/reference/android/app/RecoverableSecurityException)
that the platform throws. You can then request that the user grant your app
write access to that specific item, as shown in the following code snippet:  

### Kotlin

```kotlin
// Apply a grayscale filter to the image at the given content URI.
try {
    // "w" for write.
    contentResolver.openFileDescriptor(image-content-uri, "w")?.use {
        setGrayscaleFilter(it)
    }
} catch (securityException: SecurityException) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        val recoverableSecurityException = securityException as?
            RecoverableSecurityException ?:
            throw RuntimeException(securityException.message, securityException)

        val intentSender =
            recoverableSecurityException.userAction.actionIntent.intentSender
        intentSender?.let {
            startIntentSenderForResult(intentSender, image-request-code,
                    null, 0, 0, 0, null)
        }
    } else {
        throw RuntimeException(securityException.message, securityException)
    }
}
```

### Java

```java
try {
    // "w" for write.
    ParcelFileDescriptor imageFd = getContentResolver()
            .openFileDescriptor(image-content-uri, "w");
    setGrayscaleFilter(imageFd);
} catch (SecurityException securityException) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        RecoverableSecurityException recoverableSecurityException;
        if (securityException instanceof RecoverableSecurityException) {
            recoverableSecurityException =
                    (RecoverableSecurityException)securityException;
        } else {
            throw new RuntimeException(
                    securityException.getMessage(), securityException);
        }
        IntentSender intentSender =recoverableSecurityException.getUserAction()
                .getActionIntent().getIntentSender();
        startIntentSenderForResult(intentSender, image-request-code,
                null, 0, 0, 0, null);
    } else {
        throw new RuntimeException(
                securityException.getMessage(), securityException);
    }
}
```

Complete this process each time your app needs to modify a media file that it
didn't create.

Alternatively, if your app runs on Android 11 or higher, you can
let users grant your app write access to a group of media files. Use the
[`createWriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createWriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E))
method, as described in the section about how to [manage groups of media
files](https://developer.android.com/training/data-storage/shared/media#manage-groups-files).

If your app has another use case that isn't covered by scoped storage, [file a
feature request](https://source.android.com/setup/contribute/report-bugs) and
[temporarily opt out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage).

## Remove an item

To remove an item that your app no longer needs in the media store, use logic
similar to what's shown in the following code snippet:  

### Kotlin

```kotlin
// Remove a specific media item.
val resolver = applicationContext.contentResolver

// URI of the image to remove.
val imageUri = "..."

// WHERE clause.
val selection = "..."
val selectionArgs = "..."

// Perform the actual removal.
val numImagesRemoved = resolver.delete(
        imageUri,
        selection,
        selectionArgs)
```

### Java

```java
// Remove a specific media item.
ContentResolver resolver = getApplicationContext()
        getContentResolver();

// URI of the image to remove.
Uri imageUri = "...";

// WHERE clause.
String selection = "...";
String[] selectionArgs = "...";

// Perform the actual removal.
int numImagesRemoved = resolver.delete(
        imageUri,
        selection,
        selectionArgs);
```

If scoped storage is unavailable or isn't enabled, you can use the preceding
code snippet to remove files that other apps own. If scoped storage is enabled,
however, you need to catch a `RecoverableSecurityException` for each file that
your app wants to remove, as described in the section about [updating media
items](https://developer.android.com/training/data-storage/shared/media#update-item).

If your app runs on Android 11 or higher, you can let users
choose a group of media files to remove. Use the [`createTrashRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean))
method or the
[`createDeleteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createDeleteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E))
method, as described in the section about how to [manage groups of media
files](https://developer.android.com/training/data-storage/shared/media#manage-groups-files).

If your app has another use case that isn't covered by scoped storage, [file a
feature request](https://source.android.com/setup/contribute/report-bugs) and
[temporarily opt out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage).

## Detect updates to media files

Your app might need to identify storage volumes containing media files that apps
added or modified, compared to a previous point in time. To detect these changes
most reliably, pass the storage volume of interest into
[`getGeneration()`](https://developer.android.com/reference/android/provider/MediaStore#getGeneration(android.content.Context,%20java.lang.String)).
As long as the media store version doesn't change, the return value of this
method monotonically increases over time.

In particular, `getGeneration()` is more robust than the dates in media columns,
such as
[`DATE_ADDED`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DATE_ADDED)
and [`DATE_MODIFIED`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DATE_MODIFIED).
That's because those media column values can change when an app calls
[`setLastModified()`](https://developer.android.com/reference/java/io/File#setLastModified(long)) or when
the user changes the system clock.
| **Caution:** Before you rely on the value of `getGeneration()`, [check the media
| store for updates](https://developer.android.com/training/data-storage/shared/media#check-for-updates). If the media store version has changed, perform a full synchronization pass.

## Manage groups of media files

On Android 11 and higher, you can ask the user to select a group
of media files, then update these media files in a single operation. These
methods offer better consistency across devices, and the methods make it easier
for users to manage their media collections.

The methods that provide this "batch update" functionality include the
following:

[`createWriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createWriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E))
:   Request that the user grant your app write access to the specified group of
    media files.

[`createFavoriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createFavoriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean))
:   Request that the user mark the specified media files as some of their
    "favorite" media on the device. Any app that has read access to this file can
    see that the user has marked the file as a "favorite."

[`createTrashRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean))

:   Request that the user place the specified media files in the device's trash.
    Items in the trash are permanently deleted after a system-defined time
    period.

    | **Note:** If your app is the device OEM's preinstalled gallery app, you can place files in the trash without showing a dialog. To do so, set [`IS_TRASHED`](https://developer.android.com/reference/kotlin/android/provider/MediaStore.MediaColumns#is_trashed) to `1` directly.

[`createDeleteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createDeleteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E))

:   Request that the user permanently delete the specified media files
    immediately, without placing them in the trash beforehand.

After calling any of these methods, the system builds a
[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) object. After your app
invokes this intent, users see a dialog that requests their consent for your app
to update or delete the specified media files.

For example, here is how to structure a call to `createWriteRequest()`:  

### Kotlin

```kotlin
val urisToModify = /* A collection of content URIs to modify. */
val editPendingIntent = MediaStore.createWriteRequest(contentResolver,
        urisToModify)

// Launch a system prompt requesting user permission for the operation.
startIntentSenderForResult(editPendingIntent.intentSender, EDIT_REQUEST_CODE,
    null, 0, 0, 0)
```

### Java

```java
List<Uri> urisToModify = /* A collection of content URIs to modify. */
PendingIntent editPendingIntent = MediaStore.createWriteRequest(contentResolver,
                  urisToModify);

// Launch a system prompt requesting user permission for the operation.
startIntentSenderForResult(editPendingIntent.getIntentSender(),
    EDIT_REQUEST_CODE, null, 0, 0, 0);
```

Evaluate the user's response. If the user provided consent, proceed with the
media operation. Otherwise, explain to the user why your app needs the
permission:  

### Kotlin

```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int,
                 data: Intent?) {
    ...
    when (requestCode) {
        EDIT_REQUEST_CODE ->
            if (resultCode == Activity.RESULT_OK) {
                /* Edit request granted; proceed. */
            } else {
                /* Edit request not granted; explain to the user. */
            }
    }
}
```

### Java

```java
@Override
protected void onActivityResult(int requestCode, int resultCode,
                   @Nullable Intent data) {
    ...
    if (requestCode == EDIT_REQUEST_CODE) {
        if (resultCode == Activity.RESULT_OK) {
            /* Edit request granted; proceed. */
        } else {
            /* Edit request not granted; explain to the user. */
        }
    }
}
```

You can use this same general pattern with
[`createFavoriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createFavoriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean)),
[`createTrashRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean)),
and
[`createDeleteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createDeleteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E)).

### Media management permission

Users might trust a particular app to perform media management, such as making
frequent edits to media files. If your app targets
Android 11 or higher and isn't the device's default gallery app,
you must show a confirmation dialog to the user each time your app attempts to
modify or delete a file.

If your app targets Android 12 (API level 31) or higher, you can request that
users grant your app access to the *media management* special permission. This
permission lets your app do each of the following without needing to prompt
the user for each file operation:

- Modify files, using [`createWriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createWriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E)).
- Move files into and out of the trash, using [`createTrashRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean)).
- Delete files, using [`createDeleteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createDeleteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E)).

To do so, complete the following steps:

1. Declare the
   [`MANAGE_MEDIA`](https://developer.android.com/reference/android/Manifest.permission#MANAGE_MEDIA) permission
   and the
   [`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
   permission in your app's manifest file.

   To call `createWriteRequest()` without showing a confirmation
   dialog, declare the
   [`ACCESS_MEDIA_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION)
   permission as well.
2. In your app, show a UI to the user to explain why they might want to grant
   media management access to your app.

3. Invoke the
   [`ACTION_REQUEST_MANAGE_MEDIA`](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_MANAGE_MEDIA)
   intent action. This takes users to the **Media management apps** screen in
   system settings. From here, users can grant the special app access.

## Use cases that require an alternative to media store

If your app primarily performs one of the following roles, consider an
alternative to the `MediaStore` APIs.

### Working with other types of files

If your app works with documents and files that don't exclusively contain media
content, such as files that use the EPUB or PDF file extension, use the
`ACTION_OPEN_DOCUMENT` intent action, as described in the guide to [storing
and accessing documents and other
files](https://developer.android.com/training/data-storage/shared/documents-files).

### File sharing in companion apps

In cases where you provide a suite of companion apps, such as a messaging app and
a profile app, [set up file sharing](https://developer.android.com/training/secure-file-sharing/setup-sharing)
using `content://` URIs. We also recommend this workflow as a [security best
practice](https://developer.android.com/topic/security/best-practices#permissions-share-data).

## Additional resources

For more information about how to store and access media, consult the following
resources.

### Samples

- [MediaStore](https://github.com/android/storage-samples/tree/main/MediaStore), available on GitHub

### Videos

- [Preparing for Scoped Storage (Android Dev Summit
  '19)](https://www.youtube.com/watch?v=UnJ3amzJM94)