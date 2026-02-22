---
title: https://developer.android.com/training/data-storage/shared/photo-picker
url: https://developer.android.com/training/data-storage/shared/photo-picker
source: md.txt
---

![Photo picker dialog appears with media files on your device. Select a photo to share with the app.](https://developer.android.com/static/images/training/data-storage/kotlin-picker.gif) **Figure 1.** The photo picker provides an intuitive UI for sharing photos with your app.

The photo picker provides a browsable interface that presents the
user with their media library, sorted by date from newest to oldest. As shown in
the [privacy best practices codelab](https://developer.android.com/codelabs/android-privacy-codelab), the
photo picker provides a safe, built-in way for users to grant your app access to
only selected images and videos, instead of their entire media library.

Users who have eligible cloud media providers on their device are also able to
select from photos and videos stored remotely. [Learn more about cloud media
providers](https://developer.android.com/guide/topics/providers/cloud-media-provider).

The tool updates automatically, offering expanded functionality to your app's
users over time without requiring any code changes.

## Use Jetpack Activity contracts

To simplify photo picker integration, include version 1.7.0 or higher of the
[`androidx.activity`](https://developer.android.com/jetpack/androidx/releases/activity#1.7.0) library.

Use the following activity result contracts to launch the photo picker:

- [`PickVisualMedia`](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia) to [select a single image or video](https://developer.android.com/training/data-storage/shared/photo-picker#select-single-item).
- [`PickMultipleVisualMedia`](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.PickMultipleVisualMedia) to [select multiple images or videos](https://developer.android.com/training/data-storage/shared/photo-picker#select-multiple-items).

If the photo picker isn't available on a device, the library
automatically invokes the
[`ACTION_OPEN_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#action_open_document)
intent action instead. This intent is supported on devices that run Android 4.4
(API level 19) or higher. You can verify whether the photo picker is available
on a given device by calling
[`isPhotoPickerAvailable()`](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia#isPhotoPickerAvailable(android.content.Context)).

### Select a single media item

To select a single media item, use the `PickVisualMedia` activity result
contract, as shown in the following code snippet:  

### Views

```kotlin
// Registers a photo picker activity launcher in single-select mode.
val pickMedia = registerForActivityResult(PickVisualMedia()) { uri ->
    // Callback is invoked after the user selects a media item or closes the
    // photo picker.
    if (uri != null) {
        Log.d("PhotoPicker", "Selected URI: $uri")
    } else {
        Log.d("PhotoPicker", "No media selected")
    }
}

// Include only one of the following calls to launch(), depending on the types
// of media that you want to let the user choose from.

// Launch the photo picker and let the user choose images and videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))

// Launch the photo picker and let the user choose only images.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageOnly))

// Launch the photo picker and let the user choose only videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.VideoOnly))

// Launch the photo picker and let the user choose only images/videos of a
// specific MIME type, such as GIFs.
val mimeType = "image/gif"
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.SingleMimeType(mimeType)))
```

### Views

```java
// Registers a photo picker activity launcher in single-select mode.
ActivityResultLauncher<PickVisualMediaRequest> pickMedia =
        registerForActivityResult(new PickVisualMedia(), uri -> {
    // Callback is invoked after the user selects a media item or closes the
    // photo picker.
    if (uri != null) {
        Log.d("PhotoPicker", "Selected URI: " + uri);
    } else {
        Log.d("PhotoPicker", "No media selected");
    }
});

// Include only one of the following calls to launch(), depending on the types
// of media that you want to let the user choose from.

// Launch the photo picker and let the user choose images and videos.
pickMedia.launch(new PickVisualMediaRequest.Builder()
        .setMediaType(PickVisualMedia.ImageAndVideo.INSTANCE)
        .build());

// Launch the photo picker and let the user choose only images.
pickMedia.launch(new PickVisualMediaRequest.Builder()
        .setMediaType(PickVisualMedia.ImageOnly.INSTANCE)
        .build());

// Launch the photo picker and let the user choose only videos.
pickMedia.launch(new PickVisualMediaRequest.Builder()
        .setMediaType(PickVisualMedia.VideoOnly.INSTANCE)
        .build());

// Launch the photo picker and let the user choose only images/videos of a
// specific MIME type, such as GIFs.
String mimeType = "image/gif";
pickMedia.launch(new PickVisualMediaRequest.Builder()
        .setMediaType(new PickVisualMedia.SingleMimeType(mimeType))
        .build());
```

### Compose

```kotlin
// Registers a photo picker activity launcher in single-select mode.
val pickMedia = rememberLauncherForActivityResult(PickVisualMedia()) { uri ->
    // Callback is invoked after the user selects a media item or closes the
    // photo picker.
    if (uri != null) {
        Log.d("PhotoPicker", "Selected URI: $uri")
    } else {
        Log.d("PhotoPicker", "No media selected")
    }
}

// Include only one of the following calls to launch(), depending on the types
// of media that you want to let the user choose from.

// Launch the photo picker and let the user choose images and videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))

// Launch the photo picker and let the user choose only images.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageOnly))

// Launch the photo picker and let the user choose only videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.VideoOnly))

// Launch the photo picker and let the user choose only images/videos of a
// specific MIME type, such as GIFs.
val mimeType = "image/gif"
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.SingleMimeType(mimeType)))
```
| **Note:** When using `PickVisualMedia`, the photo picker opens in half-screen mode.

### Select multiple media items

To select multiple media items, set a maximum number of selectable media files,
as shown in the following code snippet.  

### Views

```kotlin
// Registers a photo picker activity launcher in multi-select mode.
// In this example, the app lets the user select up to 5 media files.
val pickMultipleMedia =
        registerForActivityResult(PickMultipleVisualMedia(5)) { uris ->
    // Callback is invoked after the user selects media items or closes the
    // photo picker.
    if (uris.isNotEmpty()) {
        Log.d("PhotoPicker", "Number of items selected: ${uris.size}")
    } else {
        Log.d("PhotoPicker", "No media selected")
    }
}

// For this example, launch the photo picker and let the user choose images
// and videos. If you want the user to select a specific type of media file,
// use the overloaded versions of launch(), as shown in the section about how
// to https://developer.android.com/training/data-storage/shared/photo-picker#select-single-item.
pickMultipleMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))
```

### Views

```java
// Registers a photo picker activity launcher in multi-select mode.
// In this example, the app lets the user select up to 5 media files.
ActivityResultLauncher<PickVisualMediaRequest> pickMultipleMedia =
        registerForActivityResult(new PickMultipleVisualMedia(5), uris -> {
    // Callback is invoked after the user selects media items or closes the
    // photo picker.
    if (!uris.isEmpty()) {
        Log.d("PhotoPicker", "Number of items selected: " + uris.size());
    } else {
        Log.d("PhotoPicker", "No media selected");
    }
});

// For this example, launch the photo picker and let the user choose images
// and videos. If you want the user to select a specific type of media file,
// use the overloaded versions of launch(), as shown in the section about how
// to https://developer.android.com/training/data-storage/shared/photo-picker#select-single-item.
pickMultipleMedia.launch(new PickVisualMediaRequest.Builder()
        .setMediaType(PickVisualMedia.ImageAndVideo.INSTANCE)
        .build());
```

### Compose

```kotlin
// Registers a photo picker activity launcher in multi-select mode.
// In this example, the app lets the user select up to 5 media files.
val pickMultipleMedia =
        rememberLauncherForActivityResult(PickMultipleVisualMedia(5)) { uris ->
    // Callback is invoked after the user selects media items or closes the
    // photo picker.
    if (uris.isNotEmpty()) {
        Log.d("PhotoPicker", "Number of items selected: ${uris.size}")
    } else {
        Log.d("PhotoPicker", "No media selected")
    }
}

// For this example, launch the photo picker and let the user choose images
// and videos. If you want the user to select a specific type of media file,
// use the overloaded versions of launch(), as shown in the section about how
// to https://developer.android.com/training/data-storage/shared/photo-picker#select-single-item.
pickMultipleMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))
```

The platform limits the maximum number of files that you can ask the user to
select in the photo picker. To access this limit, call
[`getPickImagesMaxLimit()`](https://developer.android.com/reference/android/provider/MediaStore#getPickImagesMaxLimit()).
On devices where the photo picker isn't supported, this limit is ignored.
| **Note:** If the photo picker isn't available and the support library invokes the `ACTION_OPEN_DOCUMENT` intent action, the system ignores the specified maximum number of selectable media files.

## Device availability

The photo picker is available on devices that meet the following criteria:

- Run Android 11 (API level 30) or higher
- Receive changes to [Modular System Components](https://source.android.com/devices/architecture/modular-system) through [Google System Updates](https://support.google.com/product-documentation/answer/11412553)

Older devices that run Android 4.4 (API level 19) through Android 10 (API level 29)
and Android Go devices running Android 11 or 12 that support
Google Play services can install a backported version of the photo picker. To
enable the automatic installation of the backported photo picker module through
Google Play services, add the following entry to the `<application>` tag in your
app's manifest file:  

    <!-- Trigger Google Play services to install the backported photo picker module. -->
    <service android:name="com.google.android.gms.metadata.ModuleDependencies"
             android:enabled="false"
             android:exported="false"
             tools:ignore="MissingClass">
        <intent-filter>
            <action android:name="com.google.android.gms.metadata.MODULE_DEPENDENCIES" />
        </intent-filter>
        <meta-data android:name="photopicker_activity:0:required" android:value="" />
    </service>

## Persist media file access

By default, the system grants your app access to media files until the device is
restarted or until your app stops. If your app performs long-running work, such
as uploading a large file in the background, you might need this access to be
persisted for a longer period of time. To do so, call the
[`takePersistableUriPermission()`](https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission(android.net.Uri,%20int))
method:  

### Kotlin

```kotlin
val flag = Intent.FLAG_GRANT_READ_URI_PERMISSION
context.contentResolver.takePersistableUriPermission(uri, flag)
```

### Java

```java
int flag = Intent.FLAG_GRANT_READ_URI_PERMISSION;
context.contentResolver.takePersistableUriPermission(uri, flag);
```
| **Note:** An app can only have up to 5,000 media grants at any one time. For every additional photo or video access granted after 5,000 have been selected, the system removes the first grant on the list to accommodate this request.

## Handle HDR video with transcoding

Android 13 (API 33) introduced the capability to capture **High Dynamic Range
(HDR) videos** . While HDR offers a richer visual experience, some older apps
might not be equipped to handle these newer formats, leading to issues like
unnatural color rendition during playback (such as green-tinted faces). To
address this compatibility gap, the photo picker offers a transcoding feature
that can automatically convert HDR videos to **Standard Dynamic Range (SDR)**
format before providing them to the requesting app.

The primary goal of photo picker transcoding is to ensure a consistent and
visually accurate media experience across a wider range of applications, even
those that don't yet have explicit HDR support. By transcoding HDR video to SDR,
photo picker aims to improve app compatibility and provide a seamless user
experience.

### How photo picker transcoding works

Photo picker HDR transcoding is not enabled by default. To enable this feature,
your app needs to explicitly declare its media format handling capabilities when
launching the photo picker.

Your app provides its media processing capabilities to the photo picker. This is
done when launching the photo picker using the AndroidX Activity library by
adding `mediaCapabilities` to the `PickVisualMediaRequest.Builder`. A new API,
`setMediaCapabilitiesForTranscoding(capabilities: MediaCapabilities?)`, has been
added to the `PickVisualMediaRequest.Builder` to facilitate this.

You can control HDR transcoding behavior using the `MediaCapabilities` class.
Provide a `MediaCapabilities` object specifying exactly which HDR types your app
supports (e.g., `TYPE_HLG10`, `TYPE_HDR10`, `TYPE_HDR10_PLUS`,
`TYPE_DOLBY_VISION`).

To disable transcoding entirely, pass `null` for
`MediaCapabilities`. Any HDR type *not* explicitly listed in your provided
capabilities will be considered unsupported. This API is supported on **Android
13 (API level 33) and higher** and is annotated with
`@RequiresApi(Build.VERSION_CODES.TIRAMISU)`.  

    import androidx.activity.result.PickVisualMediaRequest
    import androidx.activity.result.contract.ActivityResultContracts.PickVisualMedia
    import androidx.annotation.RequiresApi
    import android.os.Build
    import android.util.Log
    import android.provider.MediaStore

    // Registers a photo picker activity launcher.
    val pickMedia = registerForActivityResult(PickVisualMedia()) { uri ->
        // Callback invoked after media selected or picker activity closed.
        if (uri != null) {
            Log.d("photo picker", "Selected URI: $uri")
        } else {
            Log.d("photo picker", "No media selected")
        }
    }

    @RequiresApi(Build.VERSION_CODES.TIRAMISU)
    fun launchPhotoPickerWithTranscodingSupport() {
        val mediaCapabilities = MediaCapabilities.Builder()
            .addSupportedHdrType(MediaCapabilities.HdrType.TYPE_HLG10)
            .build()

        // Launch the photo picker and let the user choose only videos with
        // transcoding enabled.
        pickMedia.launch(PickVisualMediaRequest.Builder()
            .setMediaType(PickVisualMedia.VideoOnly)
            .setMediaCapabilitiesForTranscoding(mediaCapabilities)
            .build())
    }

The transcoding by photo picker is based on both the app's media capabilities
and the chosen video. A URI to the transcoded video is returned if transcoding
is performed.

### Important considerations for HDR transcoding

- **Performance and storage:** Transcoding takes processing time and creates a new file, which consumes storage space.
- **Video length limit:** To balance user experience and storage constraints, there is a 1 minute limit on video length.
- **Cached file management:** Cached transcoded files are periodically cleared during idle maintenance to prevent excessive storage usage.
- **Device availability:** Photo picker transcoding is supported on **Android 13
  (API level 33) and later**.
- **AndroidX activity integration:** Ensure you are using version 1.11.0-alpha01 or a later alpha/beta/RC/stable release of the AndroidX Activity library, as this includes the necessary `setMediaCapabilitiesForTranscoding` API.