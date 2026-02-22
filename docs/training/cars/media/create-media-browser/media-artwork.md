---
title: https://developer.android.com/training/cars/media/create-media-browser/media-artwork
url: https://developer.android.com/training/cars/media/create-media-browser/media-artwork
source: md.txt
---

Artwork for media items must be passed as a local URI using either
[`ContentResolver.SCHEME_CONTENT`](https://developer.android.com/reference/android/content/ContentResolver#SCHEME_CONTENT) or
[`ContentResolver.SCHEME_ANDROID_RESOURCE`](https://developer.android.com/reference/android/content/ContentResolver#SCHEME_ANDROID_RESOURCE). This local URI must resolve to
either a bitmap or a vector drawable.

- For `MediaDescriptionCompat` objects representing items in the [content
  hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy#onLoadChildren), pass the URI through [`setIconUri`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat.Builder#setIconUri(android.net.Uri)).

  | **Warning:** Don't provide artwork using [`setIconBitmap`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat.Builder#setIconUri(android.net.Uri)). While this method is supported on Android Auto, it isn't supported on Android Automotive OS (AAOS). Additionally, including many bitmaps in a result can cause you to exceed the [1MB binder size limit](https://developer.android.com/guide/components/activities/parcelables-and-bundles#sdbp), causing your app to be unresponsive.
- For `MediaMetadataCompat` objects representing the [playing item](https://developer.android.com/media/legacy/mediasession#maintain-state),
  use any of these keys to pass the URI through [`putString`](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat.Builder#putString(java.lang.String,%20java.lang.String)):

  - [`MediaMetadataCompat.METADATA_KEY_DISPLAY_ICON_URI`](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat#METADATA_KEY_DISPLAY_ICON_URI())
  - [`MediaMetadataCompat.METADATA_KEY_ART_URI`](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat#METADATA_KEY_ART_URI())
  - [`MediaMetadataCompat.METADATA_KEY_ALBUM_ART_URI`](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat#METADATA_KEY_ALBUM_ART_URI())

## Provide artwork from your app's resources

To provide drawables from your [app's resources](https://developer.android.com/guide/topics/resources/providing-resources), pass a URI in the
following format:  

    android.resource://<var translate="no">PACKAGE_NAME</var>/<var translate="no">RESOURCE_TYPE</var>/<var translate="no">RESOURCE_NAME</var>

    // Example URI - note that there is no file extension at the end of the URI
    android.resource://com.example.app/drawable/example_drawable

This snippet demonstrates how to create a URI of this format from a resource ID:  

    val resources = context.resources
    val resourceId: Int = R.drawable.example_drawable

    Uri.Builder()
        .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
        .authority(resources.getResourcePackageName(resourceId))
        .appendPath(resources.getResourceTypeName(resourceId))
        .appendPath(resources.getResourceEntryName(resourceId))
        .build()

## Provide artwork using a content provider

These steps describe how to download art from a web URI and expose it through a
local URI using a [content provider](https://developer.android.com/guide/topics/providers/content-provider-creating). For a complete example, see the
[implementation](https://github.com/android/uamp/blob/99e44c1c5106218c62eff552b64bbc12f1883a22/common/src/main/java/com/example/android/uamp/media/library/AlbumArtContentProvider.kt#L52) of [`openFile`](https://developer.android.com/reference/android/content/ContentProvider#openFile(android.net.Uri,%20java.lang.String)) and the surrounding methods in the
Universal Android Music Player sample app.

1. Build a `content://` URI corresponding to the web URI. The media browser
   service and media session pass this content URI to Android Auto and
   AAOS.

   ### Kotlin

       fun Uri.asAlbumArtContentURI(): Uri {
             return Uri.Builder()
               .scheme(ContentResolver.SCHEME_CONTENT)
               .authority(CONTENT_PROVIDER_AUTHORITY)
               .appendPath(this.getPath()) // Make sure you trust the URI
               .build()
         }

   ### Java

       public static Uri asAlbumArtContentURI(Uri webUri) {
             return new Uri.Builder()
               .scheme(ContentResolver.SCHEME_CONTENT)
               .authority(CONTENT_PROVIDER_AUTHORITY)
               .appendPath(webUri.getPath()) // Make sure you trust the URI!
               .build();
        }

2. In your implementation of `ContentProvider.openFile`, check if a file exists
   for the corresponding URI. If not, download and cache the image file. This
   code snippet uses [Glide](https://github.com/bumptech/glide).

   ### Kotlin

       override fun openFile(uri: Uri, mode: String): ParcelFileDescriptor? {
             val context = this.context ?: return null
             val file = File(context.cacheDir, uri.path)
             if (!file.exists()) {
               val remoteUri = Uri.Builder()
                   .scheme("https")
                   .authority("my-image-site")
                   .appendPath(uri.path)
                   .build()
               val cacheFile = Glide.with(context)
                   .asFile()
                   .load(remoteUri)
                   .submit()
                   .get(DOWNLOAD_TIMEOUT_SECONDS, TimeUnit.SECONDS)

               cacheFile.renameTo(file)
                file = cacheFile
             }
             return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
        }

   ### Java

       @Nullable
         @Override
         public ParcelFileDescriptor openFile(@NonNull Uri uri, @NonNull String mode)
               throws FileNotFoundException {
             Context context = this.getContext();
             File file = new File(context.getCacheDir(), uri.getPath());
             if (!file.exists()) {
               Uri remoteUri = new Uri.Builder()
                   .scheme("https")
                   .authority("my-image-site")
                   .appendPath(uri.getPath())
                   .build();
               File cacheFile = Glide.with(context)
                   .asFile()
                   .load(remoteUri)
                   .submit()
                   .get(DOWNLOAD_TIMEOUT_SECONDS, TimeUnit.SECONDS);

               cacheFile.renameTo(file);
               file = cacheFile;
             }
             return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
         }

| **Note:** The content URI should be quickly constructed and sent to Android Auto and AAOS, as demonstrated in the previous example. This is true even when the file isn't downloaded. Android Auto and AAOS show a loading UI for the images when waiting for the content provider to respond. Consider optimizing your app to quickly fetch images and to minimize the time needed to load the UI. Consider preloading and caching images.