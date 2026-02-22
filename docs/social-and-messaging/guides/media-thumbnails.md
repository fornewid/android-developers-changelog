---
title: https://developer.android.com/social-and-messaging/guides/media-thumbnails
url: https://developer.android.com/social-and-messaging/guides/media-thumbnails
source: md.txt
---

# Generate media thumbnails

Media thumbnails provide users with a quick visual preview of images and videos, allowing for faster browsing while making the app interface more visually appealing and engaging. Because thumbnails are smaller than full-sized media, they help to save memory, storage space, and bandwidth while improving the media browsing performance.

Depending on the file type and the file access you have in your application and your media assets, you can create thumbnails in a variety of different ways.

## Create a thumbnail using an image loading library

Image loading libraries do a lot of the heavy lifting for you; they can handle caching along with the logic to fetch the source media from the local or network resource based upon a[Uri](https://developer.android.com/reference/android/net/Uri). The following code demonstrates the use of the[Coil](https://coil-kt.github.io/coil/)image loading library works for both images and videos, and works on a local or network resource.  

    // Use Coil to create and display a thumbnail of a video or image with a specific height
    // ImageLoader has its own memory and storage cache, and this one is configured to also
    // load frames from videos
    val videoEnabledLoader = ImageLoader.Builder(context)
        .components {
            add(VideoFrameDecoder.Factory())
        }.build()
    // Coil requests images that match the size of the AsyncImage composable, but this allows
    // for precise control of the height
    val request = ImageRequest.Builder(context)
        .data(mediaUri)
        .size(Int.MAX_VALUE, THUMBNAIL_HEIGHT)
        .build()
    AsyncImage(
        model = request,
        imageLoader = videoEnabledLoader,
        modifier = Modifier
            .clip(RoundedCornerShape(20))    ,
        contentDescription = null
    )

**If at all possible, create thumbnails server-side** . See[Loading images](https://developer.android.com/develop/ui/compose/graphics/images/loading)for detail on how to load images using Compose, and[Loading large bitmaps efficiently](https://developer.android.com/topic/performance/graphics/load-bitmap)for guidance on how to work with large images.

## Create a thumbnail from a local image file

Getting thumbnail images involves efficient downscaling while preserving visual quality, avoiding excessive memory usage, dealing with a variety of image formats, and making correct use of[Exif](https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface)data.

The[`createImageThumbnail`](https://developer.android.com/reference/android/media/ThumbnailUtils#createImageThumbnail(java.io.File,%20android.util.Size,%20android.os.CancellationSignal))method does all of these, providing you have access to the path of the image file.  

    val bitmap = ThumbnailUtils.createImageThumbnail(File(file_path), Size(640, 480), null)

If you only have the`Uri`, you can use the[`loadThumbnail`](https://developer.android.com/reference/android/content/ContentResolver#loadThumbnail(android.net.Uri,%20android.util.Size,%20android.os.CancellationSignal))method in[ContentResolver](https://developer.android.com/reference/android/content/ContentResolver)starting with Android 10, API level 29.  

    val thumbnail: Bitmap =
            applicationContext.contentResolver.loadThumbnail(
            content-uri, Size(640, 480), null)

The[ImageDecoder](https://developer.android.com/reference/android/graphics/ImageDecoder), available starting with Android 9, API level 28, has some solid options to resample the image as you decode it to prevent extra memory use.  

    class DecodeResampler(val size: Size, val signal: CancellationSignal?) : OnHeaderDecodedListener {
        private val size: Size

       override fun onHeaderDecoded(decoder: ImageDecoder, info: ImageInfo, source:
           // sample down if needed.
            val widthSample = info.size.width / size.width
            val heightSample = info.size.height / size.height
            val sample = min(widthSample, heightSample)
            if (sample > 1) {
                decoder.setTargetSampleSize(sample)
            }
        }
    }

    val resampler = DecoderResampler(size, null)
    val source = ImageDecoder.createSource(context.contentResolver, imageUri)
    val bitmap = ImageDecoder.decodeBitmap(source, resampler);

You can use[BitmapFactory](https://developer.android.com/reference/android/graphics/BitmapFactory)to create thumbnails for apps targeting earlier Android releases.[BitmapFactory.Options](https://developer.android.com/reference/android/graphics/BitmapFactory.Options)has a setting to decode just the bounds of an image for the purpose of resampling.

First, decode just the bounds of the bitmap into the`BitmapFactory.Options`:  

    private fun decodeResizedBitmap(context: Context, uri: Uri, size: Size): Bitmap?{
        val boundsStream = context.contentResolver.openInputStream(uri)
        val options = BitmapFactory.Options()
        options.inJustDecodeBounds = true
        BitmapFactory.decodeStream(boundsStream, null, options)
        boundsStream?.close()

Use the`width`and`height`from`BitmapFactory.Options`to set the sample size:  

    if ( options.outHeight != 0 ) {
            // we've got bounds
            val widthSample = options.outWidth / size.width
            val heightSample = options.outHeight / size.height
            val sample = min(widthSample, heightSample)
            if (sample > 1) {
                options.inSampleSize = sample
            }
        }

Decode the stream. The size of the resulting image is sampled by powers of two based upon the`inSampleSize`.  

        options.inJustDecodeBounds = false
        val decodeStream = context.contentResolver.openInputStream(uri)
        val bitmap =  BitmapFactory.decodeStream(decodeStream, null, options)
        decodeStream?.close()
        return bitmap
    }

## Create a thumbnail from a local video file

Getting video thumbnail images involves many of the same challenges as with getting image thumbnails, but the file sizes can be much larger and getting a representative video frame isn't always as straightforward as picking the first frame of the video.

The[`createVideoThumbnail`](https://developer.android.com/reference/android/media/ThumbnailUtils#createVideoThumbnail(java.io.File,%20android.util.Size,%20android.os.CancellationSignal))method is a solid choice if you have access to the path of the video file.  

    val bitmap = ThumbnailUtils.createVideoThumbnail(File(file_path), Size(640, 480), null)

If you only have access to a content Uri, you can use[`MediaMetadataRetriever`](https://developer.android.com/reference/android/media/MediaMetadataRetriever).

First, check to see if the video has an embedded thumbnail, and use that if possible:  

    private suspend fun getVideoThumbnailFromMediaMetadataRetriever(context: Context, uri: Uri, size: Size): Bitmap? {
        val mediaMetadataRetriever = MediaMetadataRetriever()
        mediaMetadataRetriever.setDataSource(context, uri)
        val thumbnailBytes = mediaMetadataRetriever.embeddedPicture
        val resizer = Resizer(size, null)
        ImageDecoder.createSource(context.contentResolver, uri)
        // use a built-in thumbnail if the media file has it
        thumbnailBytes?.let {
            return ImageDecoder.decodeBitmap(ImageDecoder.createSource(it));
        }

Fetch the width and height of the video from the`MediaMetadataRetriever`to calculate the scaling factor:  

    val width = mediaMetadataRetriever.extractMetadata(MediaMetadataRetriever.METADATA_KEY_VIDEO_WIDTH)
                ?.toFloat() ?: size.width.toFloat()
        val height = mediaMetadataRetriever.extractMetadata(MediaMetadataRetriever.METADATA_KEY_VIDEO_HEIGHT)
                ?.toFloat() ?: size.height.toFloat()
        val widthRatio = size.width.toFloat() / width
        val heightRatio = size.height.toFloat() / height
        val ratio = max(widthRatio, heightRatio)

On Android 9+ (API level 28), the`MediaMetadataRetriever`can return a scaled frame:  

    if (ratio > 1) {
            val requestedWidth = width * ratio
            val requestedHeight = height * ratio
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                val frame = mediaMetadataRetriever.getScaledFrameAtTime(
                    -1, OPTION_PREVIOUS_SYNC,
                    requestedWidth.toInt(), requestedHeight.toInt())
                mediaMetadataRetriever.close()
                return frame
            }
        }

Otherwise, return the first frame unscaled:  

        // consider scaling this after the fact
        val frame = mediaMetadataRetriever.frameAtTime
        mediaMetadataRetriever.close()
        return frame
    }