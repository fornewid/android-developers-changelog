---
title: https://developer.android.com/media/grow/ultra-hdr
url: https://developer.android.com/media/grow/ultra-hdr
source: md.txt
---

# Support Ultra HDR

The[Ultra HDR image format](https://developer.android.com/guide/topics/media/platform/hdr-image-format)lets images store more information about the intensity of light, resulting in more detailed highlights and shadows and more intense colors. This section provides information to help your apps properly support Ultra HDR images.
![A graphic showing a simulation of the difference between standard dynamic range and high dynamic range. The graphic shows a landscape with a cloudy sky. The right half, simulating HDR, has brighter highlights, darker shadows, and clearer colors.](https://developer.android.com/static/media/images/grow/ultrahdr-simulation.png)**Key Point:** Ultra HDR was introduced with Android 14, but it is**fully backward compatible**. Your apps can start supporting it right away. That way, they'll take full advantage of the capabilities of whatever device they're running on.

- Devices can**display** Ultra HDR images in their full intensity if they're running**Android 14 or higher**and have screens that support HDR. On other devices, the images still display, but they're shown in standard dynamic range.
- Devices can**capture** Ultra HDR images if they're running**Android 14 or higher**and have cameras that support HDR.
- All Android devices can**share**Ultra HDR images, even if the device doesn't otherwise support Ultra HDR. For example, if a user has a phone running Android 13 and they're sent an Ultra HDR image in chat, and they forward that image to a friend with a device running Android 14 that supports HDR, that friend can view the image in its full intensity.

## Documentation

This section contains the following documentation on supporting Ultra HDR images:

- [Display Ultra HDR images](https://developer.android.com/media/grow/ultra-hdr/display): How to properly display Ultra HDR images when your app is running on a device that supports them
- [Edit Ultra HDR images](https://developer.android.com/media/grow/ultra-hdr/edit): How to edit Ultra HDR images while preserving their full intensity

| **Note:** Android OEMs might have different consumer-facing branding for HDR image features. The information in these pages applies to these features when they conform to the Ultra HDR format. For example,**Super HDR for images**on Samsung devices uses the Ultra HDR image format.
|
| As developers, your existing code will support this format, as the underlying format is the same Ultra HDR.

## Additional resources

To learn more about Ultra HDR images, see the following additional resources:

### Documentation

- [Ultra HDR format specification](https://developer.android.com/guide/topics/media/platform/hdr-image-format)

### Videos

- [Creating high-quality Android media experiences](https://www.youtube.com/watch?v=sv9ICtooWBc&t=284s)

### Code samples

#### Capture

- [Capturing an Ultra HDR image](https://github.com/android/platform-samples/pull/56)

#### Display

- [Ultra HDR: Default render](https://github.com/android/platform-samples/pull/65)
- [Visualizing the gain map](https://github.com/android/platform-samples/pull/51)
- [Compressing an Ultra HDR image](https://github.com/android/platform-samples/pull/117)
- [Displaying an Ultra HDR image in Compose](https://github.com/android/platform-samples/pull/89)
- [Using image loading libraries with Ultra HDR images](https://github.com/android/platform-samples/pull/65)

#### Edit

- [Spatial operations (rotate, scale, crop)](https://github.com/android/platform-samples/pull/88)

#### Other

- [Converting Ultra HDR images to video](https://github.com/android/platform-samples/pull/83)