---
title: https://developer.android.com/training/data-storage/use-cases
url: https://developer.android.com/training/data-storage/use-cases
source: md.txt
---

To give users more control over their files and limit file clutter,
Android 10 introduced a new storage paradigm for apps called
[scoped storage](https://developer.android.com/training/data-storage#scoped-storage). Scoped storage changes
the way apps store and access files on a device's external storage. To help you
migrate your app to support scoped storage, follow the best practices for common
storage use cases that are outlined in this guide. The use cases are organized
into two categories: [handling media files](https://developer.android.com/training/data-storage/use-cases#handle-media-files) and [handling
non-media files](https://developer.android.com/training/data-storage/use-cases#handle-non-media-files).

In many cases, your app creates files that other apps don't need to access, or
shouldn't access. The system provides
[app-specific storage locations](https://developer.android.com/training/data-storage/use-cases#handle-app-specific-files) to manage such
files.

To learn more about how to store and access files on Android, see the [storage
training guides](https://developer.android.com/training/data-storage).

## Handle media files

This section describes some of the common use cases for handling media files
(video, image, and audio files) and explains the high-level approach that your
app can use. The following table summarizes each of these use cases, and links
to the each of sections that contain further details.

| Use case | Summary |
|---|---|
| [Show all image or video files](https://developer.android.com/training/data-storage/use-cases#show-all-files-media) | Use the same approach for all versions of Android. |
| [Show images or videos from a particular folder](https://developer.android.com/training/data-storage/use-cases#show-all-folder) | Use the same approach for all versions of Android. |
| [Access location information from photos](https://developer.android.com/training/data-storage/use-cases#access-photo-locations) | Use one approach if your app uses scoped storage. Use a different approach if your app opts out of scoped storage. |
| [Define storage location for new downloads](https://developer.android.com/training/data-storage/use-cases#download-media-files) | Use one approach if your app uses scoped storage. Use a different approach if your app opts out of scoped storage. |
| [Export user media files to a device](https://developer.android.com/training/data-storage/use-cases#export-media-files-to-device) | Use the same approach for all versions of Android. |
| [Modify or delete multiple media files in a single operation](https://developer.android.com/training/data-storage/use-cases#modify-delete-media) | Use one approach for Android 11. For Android 10, opt out of scoped storage and use the approach for Android 9 and lower instead. |
| [Import a single image that already exists](https://developer.android.com/training/data-storage/use-cases#import-image-media) | Use the same approach for all versions of Android. |
| [Capture a single image](https://developer.android.com/training/data-storage/use-cases#capture-image-media) | Use the same approach for all versions of Android. |
| [Share media files with other apps](https://developer.android.com/training/data-storage/use-cases#share-media-all) | Use the same approach for all versions of Android. |
| [Share media files with a specific app](https://developer.android.com/training/data-storage/use-cases#share-media-specific) | Use the same approach for all versions of Android. |
| [Access files from code or libraries that use direct file paths](https://developer.android.com/training/data-storage/use-cases#access-file-paths) | Use one approach for Android 11. For Android 10, opt out of scoped storage and use the approach for Android 9 and lower instead. |

### Show image or video files from multiple folders

[Query a media collection](https://developer.android.com/training/data-storage/shared/media#query-collection)
using the [`query()`](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri,%20java.lang.String%5B%5D,%20java.lang.String,%20java.lang.String%5B%5D,%20java.lang.String,%20android.os.CancellationSignal))
API. To filter or sort the media files, adjust the `projection`, `selection`,
`selectionArgs`, and `sortOrder` parameters.

### Show images or videos from a particular folder

Use this approach:

1. Following the best practices outlined in [Request App Permissions](https://developer.android.com/training/permissions/requesting), request the [`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE) permission.
2. Retrieve media files based on the value of [`MediaColumns.DATA`](https://developer.android.com/reference/kotlin/android/provider/MediaStore.MediaColumns#data), which contains the absolute filesystem path to the media item on disk.

**Note:** When you access an existing media file, you can use the value
of the [`DATA`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#DATA)
column in your logic. That's because this value has a valid file path.
However, don't assume that the file is always available. Be prepared to handle
any file-based I/O errors that could occur.

To create or update a media file, on the other hand, don't use the
`DATA` column. Instead, use the `DISPLAY_NAME` and
`RELATIVE_PATH` columns.

### Access location information from photos

If your app uses scoped storage, follow the steps in the [Location information
in photographs](https://developer.android.com/training/data-storage/shared/media#location-info-photos)
section of the media storage guide.

> [!NOTE]
> **Note:** As described on the [Access media files from shared
> storage](https://developer.android.com/training/data-storage/shared/media#media-location-permission) page, apps that target Android 10 or higher need the [`ACCESS_MEDIA_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION) permission to read unredacted location information in images accessed using the [`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API.

### Define storage location for new downloads

If your app uses scoped storage, be mindful of the location where you choose to
store media files that you download.

If other apps require access to files, consider using [well-defined media
collections](https://developer.android.com/training/data-storage/shared/media#well-defined-collections) for downloads or document collections.

> [!NOTE]
> **Note:** Files stored in an [app-specific directory on external storage](https://developer.android.com/training/data-storage/app-specific#external) aren't accessible to other apps on Android 11 or higher, regardless of target SDK level.

On Android 11 and higher, the files inside of your external app-specific
directory aren't accessible to other apps, even if you use [`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager) to
fetch these files.

### Export user media files to a device

Define a proper default location to store user media
files:

- Allow users to choose whether to make their media files readable by other apps or not, using [app-specific-storage](https://developer.android.com/training/data-storage/app-specific) or [shared storage](https://developer.android.com/training/data-storage/shared/media).
- Allow users to export files from [app-specific directories](https://developer.android.com/reference/android/content/Context#getExternalFilesDirs(java.lang.String)) to a more generally accessible location. Use [MediaStore's images, video, and audio collections](https://developer.android.com/training/data-storage/shared/media#well-defined-collections) to export media files to the device's gallery.

> [!NOTE]
> **Note:** To avoid cluttering, use generally accessible locations like [`externalStoragePublicDirectory()`](https://developer.android.com/reference/android/os/Environment#getExternalStoragePublicDirectory(java.lang.String)) or [`externalMediaDirs()`](https://developer.android.com/reference/android/content/Context#getExternalMediaDirs()).

### Modify or delete multiple media files in a single operation

Incorporate logic based on the Android versions that your app runs on.

#### Running on Android 11

Use this approach:

1. Create a pending intent for your app's write or delete request using [`MediaStore.createWriteRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createWriteRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E)) or [`MediaStore.createTrashRequest()`](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest(android.content.ContentResolver,%20java.util.Collection%3Candroid.net.Uri%3E,%20boolean)) and then prompt the user for permission to edit a set of files by invoking that intent.
2. Evaluate the user's response:

   - If the permission was granted, proceed with the modify or delete operation.
   - If the permission wasn't granted, explain to the user why the feature in your app needs the permission.

Learn more about how to [manage groups of media
files](https://developer.android.com/training/data-storage/shared/media#manage-groups-files) using these
methods that are available on Android 11 and higher.

#### Running on Android 10

If your app targets Android 10 (API level 29), [opt-out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) and continue using the approach for Android 9
and lower to perform this operation.

#### Running on Android 9 or lower

Use this approach:

1. Following the best practices outlined in [Request App Permissions](https://developer.android.com/training/permissions/requesting), request the [`WRITE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE) permission.
2. Use the [`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API to modify or delete the media files.

### Import a single image that already exists

When you want to import a single image that already exists (for example, to use
as the photo for a user's profile), your app can either use its own UI for the
operation, or it can use the system picker.

#### Present your own user interface

Use this approach:

1. Following the best practices outlined in [Request App Permissions](https://developer.android.com/training/permissions/requesting), request the [`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE) permission.
2. Use the [`query()`](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri,%20java.lang.String%5B%5D,%20java.lang.String,%20java.lang.String%5B%5D,%20java.lang.String,%20android.os.CancellationSignal)) API to [query a media collection](https://developer.android.com/training/data-storage/shared/media#query-collection).
3. Display the results in your app's custom UI.

#### Use the system picker

Use the [`ACTION_GET_CONTENT`](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)
intent, which asks the user to pick an image to import.

If you want to filter the types of images that the system picker presents to the
user to choose from, you can use
[`setType()`](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String))
or [`EXTRA_MIME_TYPES`](https://developer.android.com/reference/android/content/Intent#EXTRA_MIME_TYPES).

### Capture a single image

When you want to capture a single image to use in your app (for example, to use
as the photo for a user's profile), use the
[`ACTION_IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE)
intent to ask the user to take a photo using the device's camera. The system
stores the captured photo in the
[`MediaStore.Images`](https://developer.android.com/reference/android/provider/MediaStore.Images) table.

### Share media files with other apps

Use the
[`insert()`](https://developer.android.com/reference/android/content/ContentResolver#insert(android.net.Uri,%20android.content.ContentValues))
method to add records directly into the MediaStore. For more information, see
the [Add an item](https://developer.android.com/training/data-storage/shared/media#add-item) section of the
media storage guide.

### Share media files with a specific app

Use the Android `FileProvider` component, as described in the [Setting up file
sharing](https://developer.android.com/training/secure-file-sharing/setup-sharing) guide.

### Access files from code or libraries that use direct file paths

Incorporate logic based on the Android versions that your app runs on.

#### Running on Android 11

Use this approach:

1. Following the best practices outlined in [Request App Permissions](https://developer.android.com/training/permissions/requesting), request the [`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE) permission.
2. Access the files using direct file paths.

For more information, see the section about how to open media files using
[direct file paths](https://developer.android.com/training/data-storage/shared/media#direct-file-paths).

#### Running on Android 10

If your app targets Android 10 (API level 29), [opt-out of scoped
storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) and continue using the approach for Android 9
and lower to perform this operation.

#### Running on Android 9 or lower

Use this approach:

1. Following the best practices outlined in [Request App Permissions](https://developer.android.com/training/permissions/requesting), request the [`WRITE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE) permission.
2. Access the files using direct file paths.

## Handle non-media files

This section describes some of the common use cases for handling non-media files
and explains the high-level approach that your app can use. The following table
summarizes each of these use cases, and links to the each of sections that
contain further details.

| Use case | Summary |
|---|---|
| [Open a document file](https://developer.android.com/training/data-storage/use-cases#open-document) | Use the same approach for all versions of Android. |
| [Write to files on secondary storage volumes](https://developer.android.com/training/data-storage/use-cases#write-files-secondary-storage-volumes) | Use one approach for Android 11. Use a different approach for earlier versions of Android. |
| [Migrate existing files from a legacy storage location](https://developer.android.com/training/data-storage/use-cases#migrate-legacy-storage) | Migrate your files to scoped storage when possible. Opt out of scoped storage for Android 10 when necessary. |
| [Share content with other apps](https://developer.android.com/training/data-storage/use-cases#sharing-non-media-files) | Use the same approach for all versions of Android. |
| [Cache non-media files](https://developer.android.com/training/data-storage/use-cases#cache-non-media) | Use the same approach for all versions of Android. |
| [Export non-media files to a device](https://developer.android.com/training/data-storage/use-cases#export-files-to-device) | Use one approach if your app uses scoped storage. Use a different approach if your app opts out of scoped storage. |

### Open a document file

Use the [`ACTION_OPEN_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT)
intent to ask the user to pick a file to open using the system picker. If you
want to filter the types of files that the system picker will present to the
user to choose from, you can use
[`setType()`](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String))
or [`EXTRA_MIME_TYPES`](https://developer.android.com/reference/android/content/Intent#EXTRA_MIME_TYPES).

For example, you could find all PDF, ODT, and TXT files using the following
code:

### Kotlin

```kotlin
startActivityForResult(
        Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
            addCategory(Intent.CATEGORY_OPENABLE)
            type = "*/*"
            putExtra(Intent.EXTRA_MIME_TYPES, arrayOf(
                    "application/pdf", // .pdf
                    "application/vnd.oasis.opendocument.text", // .odt
                    "text/plain" // .txt
            ))
        },
        REQUEST_CODE
      )
```

### Java

```java
Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[] {
                "application/pdf", // .pdf
                "application/vnd.oasis.opendocument.text", // .odt
                "text/plain" // .txt
        });
        startActivityForResult(intent, REQUEST_CODE);
```

### Write to files on secondary storage volumes

Secondary storage volumes include SD cards. You can access information about a
given storage volume using the
[`StorageVolume`](https://developer.android.com/reference/android/os/storage/StorageVolume) class.

Incorporate logic based on the Android version that your app runs on.

#### Running on Android 11

> [!NOTE]
> **Note:** The following approach provides access only to *reliable* volumes, which are volumes that an app can successfully access most of the time.

Use this approach:

1. Use the [scoped storage](https://developer.android.com/training/data-storage#scoped-storage) model.
2. Target Android 10 (API level 29) or lower.
3. Declare the [`WRITE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE) permission.
4. Perform one of the following types of access:
   - File access using the `MediaStore` API.
   - Direct file path access using APIs such as [`File`](https://developer.android.com/reference/java/io/File) or `fopen()`.

#### Running on older versions

Use the [Storage Access
Framework](https://developer.android.com/training/data-storage/shared/documents-files), which allows users to
select the location on a secondary storage volume where your app can write the
file.

### Migrate existing files from a legacy storage location

A directory is considered a *legacy storage location* if it isn't an
app-specific directory or a public shared directory. If your app creates or
consumes files in a legacy storage location, we recommend that you migrate your
app's files to locations that are accessible with scoped storage and make any
necessary app changes to work with files in scoped storage.

#### Maintain access to the legacy storage location for data migration

Your app needs to maintain access to the legacy storage location in order to
migrate any app files to locations that are accessible with scoped storage. The
approach you should use depends on your app's target API level.

##### If your app targets Android 11

1. Set the
   [`preserveLegacyExternalStorage`](https://developer.android.com/reference/android/R.attr#preserveLegacyExternalStorage)
   flag to `true` to [preserve the legacy storage
   model](https://developer.android.com/about/versions/11/privacy/storage#migrate-data-for-scoped-storage) so
   that your app can migrate a user's data when they upgrade to the new version of
   your app that targets Android 11.

   > [!NOTE]
   > **Note:** If you set `preserveLegacyExternalStorage` to `true`, the legacy storage model remains in effect only until the user uninstalls your app. If the user installs or reinstalls your app on a device that runs Android 11, then your app cannot opt out the scoped storage model, regardless of the value of `preserveLegacyExternalStorage`.

2. Continue to [opt out of scoped storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) so that
   your app can continue to access your files in the legacy storage location on
   Android 10 devices.

##### If your app targets Android 10

[Opt out of scoped storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) to make it easier to
maintain your app's behavior across Android versions.

#### Migrate app data

When your app is ready to migrate, use the following approach:

1. Target Android 10 or lower.
2. [Opt out of scoped storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) so that your app has access to the files that you need to migrate.
3. Deploy code that uses the `File` API to move files from their
   current location under `/sdcard/` to a location that's accessible
   with scoped storage:

   1. Move any private app files to the directory that is returned by the [`getExternalFilesDir()`](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)) method.
   2. Move any shared non-media files to an app-dedicated subdirectory of the `Downloads/` directory.
4. Remove your app's legacy storage directories from the `/sdcard/` directory.

After users install the new version of your app, they complete the data
migration process on their devices. You can monitor the migration process across
your user base by creating an analytics event.

After users have migrated their data, publish another update to your app, where
you target Android 11.

### Share content with other apps

To share your app's files with a single other app, [use a
`FileProvider`](https://developer.android.com/training/secure-file-sharing). For apps that all need to share
files between each other, we recommend [using a content
provider](https://developer.android.com/guide/topics/providers/content-provider-basics) for each app, and
then syncing the data as apps are added to the collection.

### Cache non-media files

The approach that you should use depends on the type of files that you need
to cache.

- **Small files or files that contain sensitive information** : Use [`Context#getCacheDir()`](https://developer.android.com/reference/android/content/Context#getCacheDir()).
- **Large files or files that do not contain sensitive information** : Use [`Context#getExternalCacheDir()`](https://developer.android.com/reference/android/content/Context#getExternalCacheDir()).

### Export non-media files to a device

Define a proper default location to store non-media
files. Allow users to export files from
[app-specific directories](https://developer.android.com/reference/android/content/Context#getExternalFilesDirs(java.lang.String)) to a more generally accessible location.
Use [MediaStore's downloads or document collections](https://developer.android.com/training/data-storage/shared/documents-files) to export non-media files to
the device.

> [!NOTE]
> **Note:** To avoid cluttering, use generally accessible locations like [`externalStoragePublicDirectory()`](https://developer.android.com/reference/android/os/Environment#getExternalStoragePublicDirectory(java.lang.String)) or [`externalMediaDirs()`](https://developer.android.com/reference/android/content/Context#getExternalMediaDirs()).

## Handle App-specific Files

In case your app creates files that other apps don't need to access, or
shouldn't access, you can store these files in
[app-specific storage locations](https://developer.android.com/training/data-storage/app-specific).

### Internal storage directories

The system prevents other apps from accessing these locations, and
on Android 10 (API level 29) and higher, these locations are encrypted. These locations
are a good place to store sensitive data that only your app can access.

### External storage directories

If internal storage doesn't provide enough space to store app-specific files,
consider using external storage instead. Although it's possible for another app
to [access these directories](https://developer.android.com/training/data-storage/app-specific#external)
if that app has the proper permissions, the files stored in these directories
are meant for use only by your app.

On Android 4.4 (API level 19) or higher, your app doesn't need to request any
storage-related permissions to access app-specific directories within external
storage.

When the user uninstalls your app, the files saved in app-specific storage are
removed, and hence, you shouldn't use this storage to save
anything that the user expects to persist independently of your app.

## Temporarily opt-out of scoped storage

Before your app is fully compatible with scoped storage, you can temporarily opt
out, both in [your tests](https://developer.android.com/training/data-storage/use-cases#opt-out-in-tests) and in your [production
app](https://developer.android.com/training/data-storage/use-cases#opt-out-in-production-app).

### Opt out in your tests

On Android 10 (API level 29) and higher, your app's tests run in a storage
sandbox by default. This sandbox prevents your app from accessing files outside
of the app-specific directory and publicly-shared directories.

If a test outputs files for the host---such as screenshots, debugging data,
coverage data, or performance metrics---you can write these files to global
directories. To do so, add the following flag to the relevant harness that
invokes `am instrument`:

```
-e no-isolated-storage 1
```

This flag affects all behavior of the instrumented test case, and it affects all
invoked test code. Therefore, when you use this flag, you can't validate your
app's compatibility with scoped storage. For test output, it's better to instead
write to app-scoped storage that's readable by the shell. You can then pull that
app-scoped directory. To determine which directory to pull from, call
[`getExternalMediaDirs()`](https://developer.android.com/reference/android/content/Context#getExternalMediaDirs()).

> [!NOTE]
> **Note:** The files in app-scoped storage don't persist after your app is uninstalled.

### Opt out in your production app

If your app targets Android 10 (API level 29) or lower, you can temporarily opt
out of scoped storage in your production app. If you target
Android 10, however, you need to set the value of
`requestLegacyExternalStorage` to `true` in your app's manifest file:

```xml
<manifest ... >
  <!-- This attribute is "false" by default on apps targeting
       Android 10. -->
  <application android:requestLegacyExternalStorage="true" ... >
    ...
  </application>
</manifest>
```

> [!CAUTION]
> **Caution:** After you update your app to target Android 11 (API level 30), [the
> system ignores the `requestLegacyExternalStorage`
> attribute](https://developer.android.com/about/versions/11/privacy/storage#scoped-storage) when your app is running on Android 11 devices, so your app must be ready to support scoped storage and to [migrate app data](https://developer.android.com/training/data-storage/use-cases#migrate-legacy-storage) for users on those devices.

To test how an app targeting Android 10 or lower behaves when
using scoped storage, you can opt in to the behavior by setting the value of
`requestLegacyExternalStorage` to `false`. If you are testing on a device that
runs Android 11, you can also [use app compatibility
flags](https://developer.android.com/about/versions/11/privacy/storage#test-scoped-storage) to test your
app's behavior with or without scoped storage.

## Additional resources

For more information about Android storage, view the following materials:

### Blog posts

- [Bringing modern storage to Viber's
  users](https://android-developers.googleblog.com/2020/07/bringing-modern-storage-to-vibers-users.html)