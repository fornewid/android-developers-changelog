---
title: https://developer.android.com/media/grow/ultra-hdr/display
url: https://developer.android.com/media/grow/ultra-hdr/display
source: md.txt
---

The [Ultra HDR image format](https://developer.android.com/guide/topics/media/platform/hdr-image-format) lets images store more information
about the intensity of light, resulting in more detailed highlights and shadows,
and more intense colors. Android provides support for Ultra HDR images beginning
with Android 14 (API level 34). If your app is running on those versions, it's
important to configure your app to display these images properly. On the other
hand, if your app isn't displaying Ultra HDR images, you can save device
resources by not enabling Ultra HDR display. This page explains how to check
whether graphics support Ultra HDR, and how to display them properly.

## Check for the presence of a gain map

Ultra HDR images contain a [*gain map*](https://developer.android.com/guide/topics/media/platform/hdr-image-format#gain_map-generation). The gain map is
used to determine the increased brightness of each pixel in the image. To verify
if an image is in the Ultra HDR format, convert the image or drawable into a
[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap) and call [`Bitmap.hasGainMap()`](https://developer.android.com/reference/android/graphics/Bitmap#hasGainmap())
(available since Android 14) to check if it has a gain map.

## Configure your window to display Ultra HDR

To display Ultra HDR images with the full dynamic range, set the window's color
mode to [`ActivityInfo.COLOR_MODE_HDR`](https://developer.android.com/reference/android/content/pm/ActivityInfo#COLOR_MODE_HDR). Do this by calling the
window's [`setColorMode()`](https://developer.android.com/reference/android/view/Window#setColorMode(int)) method. (These APIs are
available from Android 8; however, images are not displayed in Ultra HDR unless
the device is running Android 14 or higher.)
| **Note:** You can set a window's color mode in the Android manifest, but we don't recommend doing this. For optimum device performance, you should dynamically change a window's color mode to HDR when you're displaying an Ultra HDR image.
| **Note:** Android takes screenshots in SDR. HDR content is tonemapped to SDR in screenshots.

## Putting it all together

The following code shows how the whole process looks. This code assumes an image
is loaded into a Bitmap, and checks if the image has a gain map. If it does, the
code switches the window's color mode to [`COLOR_MODE_HDR`](https://developer.android.com/reference/android/content/pm/ActivityInfo#COLOR_MODE_HDR). If
the image does not have a gain map, the code switches the window to the default
color mode.  

### Kotlin

```kotlin
val bitmap = /* Get Bitmap from Image Resource */
binding.imageContainer.setImageBitmap(bitmap)

// Set color mode of the activity to the correct color mode.
requireActivity().window.colorMode =
   if (bitmap.hasGainmap()) ActivityInfo.COLOR_MODE_HDR else ActivityInfo.COLOR_MODE_DEFAULT
```

### Java

```java
final Bitmap bitmap = /* Get Bitmap from Image Resource */
binding.imageContainer.setImageBitmap(bitmap);

// Set color mode of the activity to the correct color mode.
int colorMode = ActivityInfo.COLOR_MODE_DEFAULT;
if (bitmap.hasGainmap()) colorMode = ActivityInfo.COLOR_MODE_HDR;
requireActivity().getWindow().setColorMode(colorMode);
```

## Additional resources

To learn more about Ultra HDR images, see the following additional resources:

- Video: [Creating high-quality Android media
  experiences](https://www.youtube.com/watch?v=sv9ICtooWBc&t=284s)
- Sample app: [Displaying Ultra HDR](https://github.com/android/platform-samples/blob/main/samples/graphics/ultrahdr/src/main/java/com/example/platform/graphics/ultrahdr/display/DisplayingUltraHDR.kt)
- [Ultra HDR image format specification](https://developer.android.com/guide/topics/media/platform/hdr-image-format)
- Video: [Android Developer Story: Instagram's early adoption of Ultra HDR transforms UX in only 3 months](https://www.youtube.com/watch?v=gGFHVi3NPWM)