---
title: https://developer.android.com/social-and-messaging/guides/media-sharing
url: https://developer.android.com/social-and-messaging/guides/media-sharing
source: md.txt
---

# About media sharing

Whether it's a funny image, an informative video, or a captivating audio clip, enabling users to share content enriches their experience and promotes engagement. This document explores the essentials of sharing media on Android, including the APIs and techniques you need to integrate this capability.

## Designed for sharing

Android's design promotes interoperability between apps using a system based on*Intents*. An Intent is an abstract description of an operation to be performed. Intents allow apps to communicate with each other without having to know specifics about each other.

When an app wants to share data or initiate an action, it creates an Intent that specifies the type of content and operation. The Android system presents a list of relevant apps that can handle that Intent, allowing the user to choose which app to use. This approach fosters a collaborative ecosystem.

Sharing text involves just a few lines of code:  

    val sendIntent: Intent = Intent().apply {
        action = Intent.ACTION_SEND
        putExtra(Intent.EXTRA_TEXT, "This is my text to share.")
        type = "text/plain"
    }

    val shareIntent = Intent.createChooser(sendIntent, null)
    startActivity(shareIntent)

The[`createChooser`](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent,%20java.lang.CharSequence,%20android.content.IntentSender))line displays the[Android Sharesheet](https://developer.android.com/training/sharing/send#why-to-use-system-sharesheet)UI, which lets users share information with people --- including relevant app suggestions --- with a single tap. Other things you can do with the Android Sharesheet include:

- [Find out when your users complete a share and to where](https://developer.android.com/training/sharing/send#share-interaction-data)
- [Provide rich text content previews, starting in Android 10 (API level 29)](https://developer.android.com/training/sharing/send#adding-rich-content-previews)

See[Send simple data to other apps](https://developer.android.com/training/sharing/send)for more information about Android Sharesheets and how to use them.

[Provide Direct Share targets](https://developer.android.com/training/sharing/direct-share-targets)to make it easier and faster for users of other apps to share URLs, images, or other kinds of data with your app.[Direct Share](https://developer.android.com/codelabs/android-direct-share)works by presenting contacts from messaging and social apps directly on the Android Sharesheet, without users having to select the app and then search for the contact.

Support[receiving rich content](https://developer.android.com/develop/ui/views/receive-rich-content)through an[`OnReceiveContentListener`](https://developer.android.com/reference/kotlin/androidx/core/view/OnReceiveContentListener). This API provides a single place for your code to handle receiving all content, from plain and styled text to markup, images, videos, audio files, and others. The content can come from image keyboards, drag and drop, or the clipboard.

## Share media files

Intents can only contain a small amount of data, so Android provides a way for Intents to contain a secure handle to files. Sharing media files securely from your app involves:

- [Configure your app to offer a secure handle to the file](https://developer.android.com/training/secure-file-sharing/setup-sharing)--- in the form of a content URI --- using the Android`FileProvider`component.
- [Specify sharable directories](https://developer.android.com/training/secure-file-sharing/setup-sharing#DefineMetaData)in your manifest.
- Use[`getUriForFile`](https://developer.android.com/reference/androidx/core/content/FileProvider#getUriForFile(android.content.Context,%20java.lang.String,%20java.io.File))to create a content URL that functions as a secure handle to the file.
- Create an Intent that[grants permissions](https://developer.android.com/training/secure-file-sharing/share-file#GrantPermissions)to the file.

See[About sharing files](https://developer.android.com/training/secure-file-sharing)for more information about how to securely share files.

## Optimize media for sharing

Whether you're sharing media to other users in your app, or sharing media to another app, you want to make sure you share media that offers a high quality sharing experience.

### Striking the balance between quality and size

Large media files can quickly consume bandwidth and storage, leading to frustrating delays and potential data overage charges for your users. Compression is your best friend here.

- **Image compression** :[Utilize modern image compression formats](https://developer.android.com/develop/ui/views/graphics/reduce-image-sizes)like WebP and AVIF, which offer superior compression ratios compared to traditional JPEGs without significant quality loss. Experiment with different quality settings to find the sweet spot.
- **Video compression** :[Leverage the power of AV1 or H.265 (HEVC)](https://developer.android.com/media/platform/transcoding)video compression to provide better compression efficiency while maintaining excellent visual quality. You can check for the presence of hardware encoding on Android 10+ devices, as well as the[`mediaPerformanceClass`](https://developer.android.com/topic/performance/performance-class)to help determine what your device can best support. Consider offering different resolution options to cater to varying user preferences and network conditions.

    fun hasHardwareEncodingSupportFor(mimeType: String): Boolean {
        val codecList = MediaCodecList(REGULAR_CODECS)
        val codecInfos = codecList.codecInfos
        for ( codecInfo in codecInfos ) {
            if (!codecInfo.isEncoder()) {
                continue;
            }
            if (!codecInfo.isHardwareAccelerated()) {
                continue;
            }
            val types: Array<String> = codecInfo.getSupportedTypes()
            for (j in types.indices) {
                if (types[j].equals(mimeType, ignoreCase = true)) {
                    return true
                }
            }
        }
        return false
    }
    // test for AV1 hardware encoding support
    val hasAV1 = hasHardwareEncodingSupportFor("video/av01")

### Adapting media

Social media platforms often enforce specific dimensions and aspect ratios for shared media. By[proactively resizing and cropping media files before sharing](https://developer.android.com/media/optimize/sharing#resolution_cropping_and_scaling), you can avoid unexpected distortion or formatting issues when users post to their favorite platforms.

Provide clear instructions and guidance on how users can optimize their media before sharing. This could include tips on adjusting[encoding bitrates](https://developer.android.com/media/optimize/sharing#bitrate), setting[quantization parameters](https://developer.android.com/media/optimize/sharing#quantization_parameter_qp),[choosing the video format](https://developer.android.com/media/media3/transformer/transformations#transcode), selecting appropriate file sizes, or understanding the impact of different sharing options.

### Enhancing media discoverability

Adding relevant metadata, such as titles, descriptions, and tags to your media files can improve their discoverability. Encourage users to add their own descriptions and captions when sharing, further personalizing the experience.

#### Add metadata to images

The[Jetpack ExifInterface](https://developer.android.com/reference/androidx/exifinterface/media/ExifInterface)class writes metadata into JPEG, PNG, and WebP images in the form of Exif tags.  

    // sets the title of the image in the form of Exif data
    val exif = ExifInterface(imageFile)
    exif.setAttribute(ExifInterface.TAG_IMAGE_DESCRIPTION, "Beautiful sunset")
    exif.saveAttributes()