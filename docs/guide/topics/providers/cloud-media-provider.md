---
title: https://developer.android.com/guide/topics/providers/cloud-media-provider
url: https://developer.android.com/guide/topics/providers/cloud-media-provider
source: md.txt
---

# Create a cloud media provider for Android

A cloud media provider provides additional cloud media content to the[Android photo picker](https://developer.android.com/training/data-storage/shared/photopicker). Users are able to select photos or videos supplied by the cloud media provider when an app uses`ACTION_PICK_IMAGES`or`ACTION_GET_CONTENT`to request media files from the user. A cloud media provider can also give information about*albums*, which can be browsed in the Android photo picker.

## Before you begin

Take the following items into consideration before you begin building your cloud media provider.

### Eligibility

Android is running a pilot program to allow OEM-nominated apps to become cloud media providers.**Only apps nominated by OEMs are eligible to participate in this program to become a cloud media provider for Android at this time**. Each OEM can nominate up to 3 apps. Once approved, these apps become accessible as cloud media providers on any GMS Android-powered device on which they are installed.

Android maintains a server-side list of all eligible cloud providers. Each OEM can choose a default cloud provider using a[configurable overlay](https://source.android.com/docs/core/runtime/rros#static-rros). Nominated apps must meet all technical requirements and pass all quality tests. To learn more about the OEM cloud media provider pilot program's process and requirements,[complete the inquiry form](https://docs.google.com/forms/d/1MGECQc2N-UnYFF5DIxeRq7AjrJ9bh_3KmoWsK8dq9ZM/edit).

### Decide if you need to create a cloud media provider

Cloud media providers are intended to be apps or services that act as a users' primary source for backing up and retrieving photos and videos from the cloud. If your app has a library of useful content, but it is not typically used as a photo storage solution, you should consider creating a[document provider](https://developer.android.com/guide/topics/providers/create-document-provider)instead.

### One active cloud provider per profile

There can be at most one active cloud media provider at a time for each[Android profile](https://source.android.com/docs/devices/admin/multi-user#general_defs). Users might remove or change their selected cloud media provider app at any time from photo picker settings.

By default, the Android photo picker will attempt to choose a cloud provider automatically.

- If there is only one eligible cloud provider on the device, that app will be selected as the current provider automatically.
- If there are more than one eligible cloud providers on the device and one of them matches the OEM chosen default, then the OEM-chosen app will be selected.

- If there are more than one eligible cloud providers on the device, and none of them match the OEM chosen default, no app will be selected.

## Build your cloud media provider

The following diagram illustrates the sequence of events both before and during a photo selection session between the Android app, the Android photo picker, the local device's`MediaProvider`, and a`CloudMediaProvider`.
![Sequence diagram showing flow from photo picker to a cloud media provider](https://developer.android.com/static/guide/topics/providers/images/cloud-media-provider-sequence.svg)**Figure 1:**Event sequence diagram during a photo selection session.

1. The system initializes the user's preferred cloud provider and periodically syncs media metadata into the Android photo picker backend.
2. When an Android app launches the photo picker, before showing a merged local or cloud item grid to the user, the photo picker performs a latency-sensitive incremental sync with the cloud provider to ensure results are as up-to-date as possible. After receiving a response, or when the deadline is reached, the photo picker grid now displays all accessible photos, combining those stored locally on your device with those synced from the cloud.
3. While the user scrolls, the photo picker fetches media thumbnails from the cloud media provider to display in the UI.
4. When the user completes the session and the results include a cloud media item, the photo picker requests file descriptors for the content, generates a URI, and grants access to the file to the calling application.
5. The app is now able to open the URI and has read-only access to the media contents. By default, sensitive metadata is redacted. The photo picker leverages the FUSE file system to coordinate data exchange between the Android app and the cloud media provider.

## Common Issues

Here are some important considerations to keep in mind when considering your implementation:

### Avoid duplicate files

Since the Android photo picker has no way of inspecting the cloud media state, the`CloudMediaProvider`needs to provide the`MEDIA_STORE_URI`in the cursor row of any file that exists both in the cloud and on the local device, or the user will see duplicate files in the photo picker.

### Optimize image sizes for preview display

It's very important that the file returned from`onOpenPreview`is not the full resolution image, and adheres to the`Size`being requested. Too large an image will incur loading times in the UI, and too small an image might be pixelated or blurry based on the screen size of the device.

### Handle correct orientation

If thumbnails returned in`onOpenPreview`do not contain their EXIF data, they should be returned in the correct orientation to avoid thumbnails being rotated incorrectly in the preview grid.

### Prevent unauthorized access

Check for the`MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION`before returning data to the caller from the ContentProvider. This will prevent unauthorized apps from accessing cloud data.

## The CloudMediaProvider class

Derived from`android.content.ContentProvider`, the[`CloudMediaProvider`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider)class includes methods like the ones shown in the following example:  

### Kotlin

    abstract class CloudMediaProvider : ContentProvider() {

        @NonNull
        abstract override fun onGetMediaCollectionInfo(@NonNull bundle: Bundle): Bundle

        @NonNull
        override fun onQueryAlbums(@NonNull bundle: Bundle): Cursor = TODO("Implement onQueryAlbums")

        @NonNull
        abstract override fun onQueryDeletedMedia(@NonNull bundle: Bundle): Cursor

        @NonNull
        abstract override fun onQueryMedia(@NonNull bundle: Bundle): Cursor

        @NonNull
        abstract override fun onOpenMedia(
            @NonNull string: String,
            @Nullable bundle: Bundle?,
            @Nullable cancellationSignal: CancellationSignal?
        ): ParcelFileDescriptor

        @NonNull
        abstract override fun onOpenPreview(
            @NonNull string: String,
            @NonNull point: Point,
            @Nullable bundle: Bundle?,
            @Nullable cancellationSignal: CancellationSignal?
        ): AssetFileDescriptor

        @Nullable
        override fun onCreateCloudMediaSurfaceController(
            @NonNull bundle: Bundle,
            @NonNull callback: CloudMediaSurfaceStateChangedCallback
        ): CloudMediaSurfaceController? = null
    }

### Java

    public abstract class CloudMediaProvider extends android.content.ContentProvider {

      @NonNull
      public abstract android.os.Bundle onGetMediaCollectionInfo(@NonNull android.os.Bundle);

      @NonNull
      public android.database.Cursor onQueryAlbums(@NonNull android.os.Bundle);

      @NonNull
      public abstract android.database.Cursor onQueryDeletedMedia(@NonNull android.os.Bundle);

      @NonNull
      public abstract android.database.Cursor onQueryMedia(@NonNull android.os.Bundle);

      @NonNull
      public abstract android.os.ParcelFileDescriptor onOpenMedia(@NonNull String, @Nullable android.os.Bundle, @Nullable android.os.CancellationSignal) throws java.io.FileNotFoundException;

      @NonNull
      public abstract android.content.res.AssetFileDescriptor onOpenPreview(@NonNull String, @NonNull android.graphics.Point, @Nullable android.os.Bundle, @Nullable android.os.CancellationSignal) throws java.io.FileNotFoundException;

      @Nullable
      public android.provider.CloudMediaProvider.CloudMediaSurfaceController onCreateCloudMediaSurfaceController(@NonNull android.os.Bundle, @NonNull android.provider.CloudMediaProvider.CloudMediaSurfaceStateChangedCallback);
    }

## The CloudMediaProviderContract class

In addition to the primary`CloudMediaProvider`implementation class, the Android photo picker incorporates a[`CloudMediaProviderContract`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract)class. This class outlines the interoperability between the photo picker and the cloud media provider, encompassing aspects such as`MediaCollectionInfo`for synchronization operations, anticipated`Cursor`columns, and`Bundle`extras.  

### Kotlin

    object CloudMediaProviderContract {

        const val EXTRA_ALBUM_ID = "android.provider.extra.ALBUM_ID"
        const val EXTRA_LOOPING_PLAYBACK_ENABLED = "android.provider.extra.LOOPING_PLAYBACK_ENABLED"
        const val EXTRA_MEDIA_COLLECTION_ID = "android.provider.extra.MEDIA_COLLECTION_ID"
        const val EXTRA_PAGE_SIZE = "android.provider.extra.PAGE_SIZE"
        const val EXTRA_PAGE_TOKEN = "android.provider.extra.PAGE_TOKEN"
        const val EXTRA_PREVIEW_THUMBNAIL = "android.provider.extra.PREVIEW_THUMBNAIL"
        const val EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED = "android.provider.extra.SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED"
        const val EXTRA_SYNC_GENERATION = "android.provider.extra.SYNC_GENERATION"
        const val MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION = "com.android.providers.media.permission.MANAGE_CLOUD_MEDIA_PROVIDERS"
        const val PROVIDER_INTERFACE = "android.content.action.CLOUD_MEDIA_PROVIDER"

        object MediaColumns {
            const val DATE_TAKEN_MILLIS = "date_taken_millis"
            const val DURATION_MILLIS = "duration_millis"
            const val HEIGHT = "height"
            const val ID = "id"
            const val IS_FAVORITE = "is_favorite"
            const val MEDIA_STORE_URI = "media_store_uri"
            const val MIME_TYPE = "mime_type"
            const val ORIENTATION = "orientation"
            const val SIZE_BYTES = "size_bytes"
            const val STANDARD_MIME_TYPE_EXTENSION = "standard_mime_type_extension"
            const val STANDARD_MIME_TYPE_EXTENSION_ANIMATED_WEBP = 3 // 0x3
            const val STANDARD_MIME_TYPE_EXTENSION_GIF = 1 // 0x1
            const val STANDARD_MIME_TYPE_EXTENSION_MOTION_PHOTO = 2 // 0x2
            const val STANDARD_MIME_TYPE_EXTENSION_NONE = 0 // 0x0
            const val SYNC_GENERATION = "sync_generation"
            const val WIDTH = "width"
        }

        object AlbumColumns {
            const val DATE_TAKEN_MILLIS = "date_taken_millis"
            const val DISPLAY_NAME = "display_name"
            const val ID = "id"
            const val MEDIA_COUNT = "album_media_count"
            const val MEDIA_COVER_ID = "album_media_cover_id"
        }

        object MediaCollectionInfo {
            const val ACCOUNT_CONFIGURATION_INTENT = "account_configuration_intent"
            const val ACCOUNT_NAME = "account_name"
            const val LAST_MEDIA_SYNC_GENERATION = "last_media_sync_generation"
            const val MEDIA_COLLECTION_ID = "media_collection_id"
        }
    }

### Java

    public final class CloudMediaProviderContract {

      public static final String EXTRA_ALBUM_ID = "android.provider.extra.ALBUM_ID";
      public static final String EXTRA_LOOPING_PLAYBACK_ENABLED = "android.provider.extra.LOOPING_PLAYBACK_ENABLED";
      public static final String EXTRA_MEDIA_COLLECTION_ID = "android.provider.extra.MEDIA_COLLECTION_ID";
      public static final String EXTRA_PAGE_SIZE = "android.provider.extra.PAGE_SIZE";
      public static final String EXTRA_PAGE_TOKEN = "android.provider.extra.PAGE_TOKEN";
      public static final String EXTRA_PREVIEW_THUMBNAIL = "android.provider.extra.PREVIEW_THUMBNAIL";
      public static final String EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED = "android.provider.extra.SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED";
      public static final String EXTRA_SYNC_GENERATION = "android.provider.extra.SYNC_GENERATION";
      public static final String MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION = "com.android.providers.media.permission.MANAGE_CLOUD_MEDIA_PROVIDERS";
      public static final String PROVIDER_INTERFACE = "android.content.action.CLOUD_MEDIA_PROVIDER";
    }

    // Columns available for every media item
    public static final class CloudMediaProviderContract.MediaColumns {

      public static final String DATE_TAKEN_MILLIS = "date_taken_millis";
      public static final String DURATION_MILLIS = "duration_millis";
      public static final String HEIGHT = "height";
      public static final String ID = "id";
      public static final String IS_FAVORITE = "is_favorite";
      public static final String MEDIA_STORE_URI = "media_store_uri";
      public static final String MIME_TYPE = "mime_type";
      public static final String ORIENTATION = "orientation";
      public static final String SIZE_BYTES = "size_bytes";
      public static final String STANDARD_MIME_TYPE_EXTENSION = "standard_mime_type_extension";
      public static final int STANDARD_MIME_TYPE_EXTENSION_ANIMATED_WEBP = 3; // 0x3
      public static final int STANDARD_MIME_TYPE_EXTENSION_GIF = 1; // 0x1 
      public static final int STANDARD_MIME_TYPE_EXTENSION_MOTION_PHOTO = 2; // 0x2 
      public static final int STANDARD_MIME_TYPE_EXTENSION_NONE = 0; // 0x0 
      public static final String SYNC_GENERATION = "sync_generation";
      public static final String WIDTH = "width";
    }

    // Columns available for every album item
    public static final class CloudMediaProviderContract.AlbumColumns {

      public static final String DATE_TAKEN_MILLIS = "date_taken_millis";
      public static final String DISPLAY_NAME = "display_name";
      public static final String ID = "id";
      public static final String MEDIA_COUNT = "album_media_count";
      public static final String MEDIA_COVER_ID = "album_media_cover_id";
    }

    // Media Collection metadata that is cached by the OS to compare sync states.
    public static final class CloudMediaProviderContract.MediaCollectionInfo {

      public static final String ACCOUNT_CONFIGURATION_INTENT = "account_configuration_intent";
      public static final String ACCOUNT_NAME = "account_name";
      public static final String LAST_MEDIA_SYNC_GENERATION = "last_media_sync_generation";
      public static final String MEDIA_COLLECTION_ID = "media_collection_id";
    }

### onGetMediaCollectionInfo

The[`onGetMediaCollectionInfo()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#ongetmediacollectioninfo)method is used by the operating system to assess the validity of its cached cloud media items and determine necessary synchronization with the cloud media provider. Due to the potential for frequent calls by the operating system,`onGetMediaCollectionInfo()`is considered performance-critical; it is crucial to avoid long-running operations or side effects that could negatively impact performance. The operating system caches previous responses from this method and compares them with subsequent responses to determine the appropriate actions.  

### Kotlin

    abstract fun onGetMediaCollectionInfo(extras: Bundle): Bundle

### Java

    @NonNull
    public abstract Bundle onGetMediaCollectionInfo(@NonNull Bundle extras);

The returned[`MediaCollectionInfo`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.MediaCollectionInfo)bundle includes the following constants:

- [`MEDIA_COLLECTION_ID`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.MediaCollectionInfo#MEDIA_COLLECTION_ID:kotlin.String)
- [`LAST_MEDIA_SYNC_GENERATION`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.MediaCollectionInfo#LAST_MEDIA_SYNC_GENERATION:kotlin.String)
- [`ACCOUNT_NAME`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.MediaCollectionInfo#ACCOUNT_NAME:kotlin.String)
- [`ACCOUNT_CONFIGURATION_INTENT`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.MediaCollectionInfo#ACCOUNT_CONFIGURATION_INTENT:kotlin.String)

### onQueryMedia

The[`onQueryMedia()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#onquerymedia)method is used to populate the main photo grid in photo picker in a variety of views. These calls might be latency sensitive, and can be called as part of a background proactive sync, or during photo picker sessions when a full or incremental sync state is required. The photo picker user interface won't wait indefinitely for a response to display results, and might time out these requests for user interface purposes. The returned cursor will still attempt to be processed into the photo picker's database for future sessions.

This method returns a`Cursor`representing all media items in the media collection optionally filtered by the provided extras and sorted in reverse chronological order of`MediaColumns#DATE_TAKEN_MILLIS`(most recent items first).

The returned[`CloudMediaProviderContract`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract)bundle includes the following constants:

- [`EXTRA_ALBUM_ID`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_album_id)
- [`EXTRA_LOOPING_PLAYBACK_ENABLED`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_looping_playback_enabled)
- [`EXTRA_MEDIA_COLLECTION_ID`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_media_collection_id)
- [`EXTRA_PAGE_SIZE`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_page_size)
- [`EXTRA_PAGE_TOKEN`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_page_token)
- [`EXTRA_PREVIEW_THUMBNAIL`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_preview_thumbnail)
- [`EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_surface_controller_audio_mute_enabled)
- [`EXTRA_SYNC_GENERATION`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#extra_sync_generation)
- [`MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#manage_cloud_media_providers_permission)
- [`PROVIDER_INTERFACE`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract#provider_interface)

The cloud media provider must set`CloudMediaProviderContract#EXTRA_MEDIA_COLLECTION_ID`as part of the returned`Bundle`. Not setting this is an error and invalidates the returned`Cursor`. If the cloud media provider handled any filters in the provided extras, it must add the key to the`ContentResolver#EXTRA_HONORED_ARGS`as part of the returned`Cursor#setExtras`.

### onQueryDeletedMedia

The[`onQueryDeletedMedia()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#onquerydeletedmedia)method is used to ensure deleted items in the cloud account are correctly removed from the photo picker user interface. Due to their potential latency sensitivity, these calls might be initiated as part of:

- Background proactive synchronization
- Photo picker sessions (when a full or incremental sync state is required)

The photo picker's user interface prioritizes a responsive user experience and will not wait indefinitely for a response. To maintain smooth interactions, timeouts might occur. Any returned`Cursor`will still attempt to be processed into the photo picker's database for future sessions.

This method returns a`Cursor`representing all deleted media items in the entire media collection within the current provider version as returned by`onGetMediaCollectionInfo()`. These items can be optionally filtered by extras. The cloud media provider must set the`CloudMediaProviderContract#EXTRA_MEDIA_COLLECTION_ID`as part of the returned`Cursor#setExtras`Not setting this is an error and invalidates the`Cursor`. If the provider handled any filters in the provided extras, it must add the key to the`ContentResolver#EXTRA_HONORED_ARGS`.

### onQueryAlbums

The[`onQueryAlbums()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#onqueryalbums)method is used to fetch a list of Cloud albums that are available in the cloud provider, and their associated metadata. See[`CloudMediaProviderContract.AlbumColumns`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProviderContract.AlbumColumns)for additional details.

This method returns a`Cursor`representing all album items in the media collection optionally filtered by the provided extras and sorted in reverse chronological order of`AlbumColumns#DATE_TAKEN_MILLIS`, most recent items first. The cloud media provider must set the`CloudMediaProviderContract#EXTRA_MEDIA_COLLECTION_ID`as part of the returned`Cursor`. Not setting this is an error and invalidates the returned`Cursor`. If the provider handled any filters in the provided extras, it must add the key to the`ContentResolver#EXTRA_HONORED_ARGS`as part of the returned`Cursor`.

### onOpenMedia

The[`onOpenMedia()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#onopenmedia)method should return the full size media identified by the provided`mediaId`. If this method blocks while downloading content to the device, you should periodically check the provided`CancellationSignal`to abort abandoned requests.

### onOpenPreview

The[`onOpenPreview()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#onopenpreview)method should return a thumbnail of the provided`size`for the item of the provided mediaId. The thumbnail should be in the original`CloudMediaProviderContract.MediaColumns#MIME_TYPE`and is expected to be much lower resolution than the item returned by`onOpenMedia`. If this method is blocked while downloading content to the device, you should periodically check the provided`CancellationSignal`to abort abandoned requests.

### onCreateCloudMediaSurfaceController

The[`onCreateCloudMediaSurfaceController()`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider#oncreatecloudmediasurfacecontroller)method should return a`CloudMediaSurfaceController`used for rendering the preview of media items, or`null`if preview rendering is not supported.

The`CloudMediaSurfaceController`manages rendering the preview of media items on given instances of`Surface`. The methods of this class are meant to be asynchronous, and should not block by performing any heavy operation. A single`CloudMediaSurfaceController`instance is responsible for rendering multiple media items associated with multiple surfaces.

The`CloudMediaSurfaceController`has support for the following list of lifecycle callbacks:

- [`onConfigChange`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onconfigchange)
- [`onDestroy`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onDestroy)
- [`onMediaPause`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onMediaPause)
- [`onMediaPlay`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onMediaPlay)
- [`onMediaSeekTo`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onMediaSeekTo)
- [`onPlayerCreate`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onPlayerCreate)
- [`onPlayerRelease`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onPlayerRelease)
- [`onSurfaceChanged`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onSurfaceChanged)
- [`onSurfaceCreated`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onSurfaceCreated)
- [`onSurfaceDestroyed`](https://developer.android.com/reference/kotlin/android/provider/CloudMediaProvider.CloudMediaSurfaceController#onSurfaceDestroyed)