---
title: https://developer.android.com/about/versions/11/privacy/storage
url: https://developer.android.com/about/versions/11/privacy/storage
source: md.txt
---

Android 11 (API level 30) further enhances the platform, giving better
protection to app and user data on external storage. This release introduces
several enhancements, such as raw file path access, batch edit
operations for media, and an updated UI for the Storage Access Framework.

The release also offers improvements to [scoped
storage](https://developer.android.com/training/data-storage#scoped-storage), which makes it easier for
developers to fulfill their [storage use
cases](https://developer.android.com/training/data-storage/use-cases) after they migrate to using this
storage model.

## Scoped storage enforcement

Apps that run on Android 11 but target Android 10
(API level 29) can still request the
[`requestLegacyExternalStorage`](https://developer.android.com/reference/android/R.attr#requestLegacyExternalStorage)
attribute. This flag allows apps to [temporarily opt out of the
changes](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage) associated
with scoped storage, such as granting access to different directories and
different types of media files. After you update your app to target
Android 11, the system ignores the `requestLegacyExternalStorage`
flag.

### Maintain compatibility with Android 10

If your app opts out of scoped storage when running on Android 10 devices, it's
recommended that you continue to set `requestLegacyExternalStorage` to `true` in
your app's manifest file. That way, your app can continue to behave as expected
on devices that run Android 10.

### Migrate data to directories that are visible when using scoped storage

If your app uses the legacy storage model and previously targeted Android 10 or
lower, you might be storing data in a directory that your app cannot access when
the [scoped storage](https://developer.android.com/training/data-storage#scoped-storage) model is enabled.
Before you target Android 11, [migrate
data](https://developer.android.com/training/data-storage/use-cases#migrate-legacy-storage) to a directory
that's compatible with scoped storage.

### Test scoped storage

To enable scoped storage in your app, regardless of your app's target SDK
version and manifest flag values, enable the following app compatibility flags:

- [`DEFAULT_SCOPED_STORAGE`](https://developer.android.com/about/versions/11/reference/compat-framework-changes#default_scoped_storage) (enabled for all apps by default)
- [`FORCE_ENABLE_SCOPED_STORAGE`](https://developer.android.com/about/versions/11/reference/compat-framework-changes#force_enable_scoped_storage) (disabled for all apps by default)

To **disable** scoped storage and use the legacy storage model instead,
**unset** both flags.

## Manage device storage

Starting in Android 11, apps that use the scoped storage model
can access only their own app-specific cache files. If your app needs to manage
device storage, follow the instructions on how to [query free
space](https://developer.android.com/training/data-storage/app-specific#query-free-space).

1. Check for free space by invoking the [`ACTION_MANAGE_STORAGE`](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager#action_manage_storage) intent action.
2. If there isn't enough free space on the device, prompt the user to give your
   app consent to clear all caches. To do so, invoke the
   [`ACTION_CLEAR_APP_CACHE`](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager#action_clear_app_cache) intent action.

   | **Caution:** The `ACTION_CLEAR_APP_CACHE` intent action can substantially affect device battery life and might remove a large number of files from the device.

## App-specific directory on external storage

Starting in Android 11, apps cannot create their own
[app-specific directory on external storage](https://developer.android.com/training/data-storage/app-specific#external). To
access the directory that the system provides for your app, call
[`getExternalFilesDirs()`](https://developer.android.com/reference/android/content/Context#getExternalFilesDirs(java.lang.String)).

## Media file access

To make it easier to access media while retaining user privacy,
Android 11 adds the following capabilities.

### Perform batch operations

For consistency across devices and added user convenience,
Android 11 adds several methods that make it easier to [manage
groups of media files](https://developer.android.com/training/data-storage/shared/media#manage-groups-files).

### Access files using direct file paths and native libraries

To help your app work more smoothly with third-party media libraries,
Android 11 allows you to use APIs other than the
[`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore) API to access
media files from shared storage using [direct file
paths](https://developer.android.com/training/data-storage/shared/media#direct-file-paths). These APIs
include the following:

- The [`File`](https://developer.android.com/reference/java/io/File) API.
- Native libraries, such as `fopen()`.

## Access to data from other apps

To protect user privacy, on devices that run Android 11 or
higher, the system further restricts your app's access to other apps' private
directories.

### Access to data directories on internal storage

Android 9 (API level 28) started to restrict which apps could make the files in
their [data directories on internal
storage](https://developer.android.com/training/data-storage/app-specific#internal) world-accessible to other
apps. Apps that target Android 9 or higher [cannot make the files in their data
directories
world-accessible](https://developer.android.com/about/versions/pie/android-9.0-changes-28#per-app-selinux).

Android 11 expands upon this restriction. If your app targets
Android 11, it cannot access the files in any other app's data
directory, even if the other app targets Android 8.1 (API level 27) or lower and
has made the files in its data directory world-readable.

### Access to app-specific directories on external storage

On Android 11, apps can no longer access files in *any* other
app's [dedicated, app-specific
directory](https://developer.android.com/training/data-storage/app-specific#external) within external
storage.

## Document access restrictions

To give developers time for testing, the following changes related to the
Storage Access Framework (SAF) take effect only if your app targets
Android 11 or higher.

### Access to directories

You can no longer use the
[`ACTION_OPEN_DOCUMENT_TREE`](https://developer.android.com/training/data-storage/shared/documents-files#grant-access-directory)
intent action to request access to the following directories:

- The root directory of the internal storage volume.
- The root directory of each SD card volume that the device manufacturer considers to be *reliable*, regardless of whether the card is emulated or removable. A reliable volume is one that an app can successfully access most of the time.
- The `Download` directory.

### Access to files

You can no longer use the
[`ACTION_OPEN_DOCUMENT_TREE`](https://developer.android.com/training/data-storage/shared/documents-files#grant-access-directory)
or the
[`ACTION_OPEN_DOCUMENT`](https://developer.android.com/training/data-storage/shared/documents-files#open-file)
intent action to request that the user select individual files from the
following directories:

- The `Android/data/` directory and all subdirectories.
- The `Android/obb/` directory and all subdirectories.

### Test the change

To test this behavior change, do the following:

1. Invoke an intent with the `ACTION_OPEN_DOCUMENT` action. Check that the `Android/data/` and `Android/obb/` directories both don't appear.
2. Do one of the following:
   - Enable the [`RESTRICT_STORAGE_ACCESS_FRAMEWORK`](https://developer.android.com/about/versions/11/reference/compat-framework-changes#restrict_storage_access_framework) app compatibility flag.
   - Target Android 11 or higher.
3. Invoke an intent with the `ACTION_OPEN_DOCUMENT_TREE` action. Check that the `Download` directory appears and the action button associated with the directory is grayed out.

## Permissions

Android 11 introduces the following changes related to storage
permissions.

### Target any version

![The first dialog presents a link called Allow in settings](https://developer.android.com/static/images/about/versions/11/request-external-storage.svg) **Figure 1.** Dialog shown when an app uses scoped storage and requests the `READ_EXTERNAL_STORAGE` permission.

The following changes take effect in Android 11, regardless of your app's target SDK version:

- The **Storage** runtime permission is renamed to **Files \&
  Media**.
- If your app hasn't opted out of
  [scoped storage](https://developer.android.com/training/data-storage#scoped-storage) and
  requests the
  [`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
  permission, users see a different dialog compared to Android 10. The dialog
  indicates that your app is requesting access to photos and media, as shown in
  Figure 1.

  Users can see which apps have the `READ_EXTERNAL_STORAGE`
  permission in system settings. On the **Settings \> Privacy \>
  Permission manager \> Files and media** page, each app that has the
  permission is listed under **Allowed for all files** . If your app targets
  Android 11, keep in mind that this access to "all files" is
  read-only. To read **and write** to all files in
  [shared storage](https://developer.android.com/training/data-storage/shared) using this app, you
  need to have the [all files
  access](https://developer.android.com/about/versions/11/privacy/storage#all-files-access) permission.

### Target Android 11

If your app targets Android 11, both the
`WRITE_EXTERNAL_STORAGE` permission and the `WRITE_MEDIA_STORAGE` privileged
permission no longer provide any additional access.

Keep in mind that, on devices that run Android 10 (API level 29) or higher, your
app can contribute to well-defined media collections such as
`MediaStore.Downloads` without requesting any storage-related permissions. Learn
more about how to [request only the necessary
permissions](https://developer.android.com/training/data-storage/shared/media#request-permissions) when
working with media files in your app.

## All files access

The majority of apps that require shared storage access can follow the best
practices for [sharing media
files](https://developer.android.com/training/data-storage/use-cases#share-media-all) and [sharing non-media
files](https://developer.android.com/training/data-storage/use-cases#sharing-non-media-files). However, some
apps have a core use case that requires broad access of files on a device, but
cannot do so efficiently using the privacy-friendly storage best practices.
Android provides a special app access called *All files access* for these
situations. To learn more, see the guide on how to [manage all
files](https://developer.android.com/training/data-storage/manage-all-files) on a storage device.
| **Note:** If you publish your app to Google Play, carefully read the [notice](https://developer.android.com/training/data-storage/manage-all-files#all-files-access-google-play). If you target Android 11 and declare *All files access*, it can affect your ability to publish and update your app on Google Play.

## Additional resources

For more information about changes to storage in Android 11, view the following
materials:

### Blog posts

- [Android 11 Storage
  FAQ](https://medium.com/androiddevelopers/android-11-storage-faq-78cefea52b7c)

### Videos

- [How to perform storage access in
  Android 11](https://www.youtube.com/watch?v=RjyYCUW-9tY)