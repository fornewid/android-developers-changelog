---
title: https://developer.android.com/media/grow/ultra-hdr/edit
url: https://developer.android.com/media/grow/ultra-hdr/edit
source: md.txt
---

The [Ultra HDR image format](https://developer.android.com/guide/topics/media/platform/hdr-image-format) encodes luminosity information
that lets devices display brighter
images with more intense colors. When your app edits an Ultra HDR image, you
want to make sure to preserve that luminosity information. This is important even if the
user's device doesn't support displaying an Ultra HDR image at full
intensity. After all, the user might share their image to someone with a device
that supports Ultra HDR, or they might save that image and look at it again on a
new device years later.

The good news is most Android methods for editing bitmaps support the Ultra HDR
image format. If you're making basic edits to an image, like cropping or
rotating it, the standard Android methods do the job---you'll end up with an
ultra HDR image with the new dimensions or orientation.

The job is trickier if you're modifying the contents of the image. In those
cases, the standard editing methods preserve the luminosity information of the
*old* image, which might not be what you want. In those cases, you might need to
edit or remove the gain map (which encodes the image's luminosity information)
to get the right result.

### Ultra HDR format overview

The Ultra HDR image format is described in detail in the [Ultra HDR Image
specification](https://developer.android.com/guide/topics/media/platform/hdr-image-format). The most important thing to understand is an
Ultra HDR image contains both a *primary image* and a *gain map*.

- The *primary image* has the color information for each pixel of the image.
- The *gain map* is a standard JPEG image with the same proportions as the primary image, though not necessarily the same pixel dimensions. Each pixel of the gain map specifies the luminance of the corresponding part of the primary image.

The gain map can be either grayscale or color. If the gain map is in color, each
color channel on the gain map specifies the luminance of that color channel on
the corresponding part of the primary image. If the gain map is grayscale, each
pixel of the gain map specifies the luminance of all three color channels on
that portion of the primary image.

The gain map must have the same proportions as the primary image, but it does
not have to have the same pixel dimensions. In fact, when the Android platform
creates Ultra HDR images, it creates a gain map with a smaller width and height
than the primary image; doing so makes the file size significantly smaller, but
still encodes enough information for a good result. This means that each pixel
in the gain map might store the luminance information for several pixels in the
primary image.

### Basic Ultra HDR edits

If you use the Android [`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap) APIs to make
basic transformations to an Ultra HDR image, the methods make the appropriate
changes to the gain map. The following `Bitmap` operations are supported:

- **Rotate:** If you rotate an Ultra HDR image, the method rotates the gain map too.
- **Crop:** If you crop an Ultra HDR image, the method crops the gain map appropriately.
- **Scale:** If you scale an Ultra HDR image, the method scales the gain map so it has half the width and half the height of the resized primary image.

In each case, the luminosity information is preserved.

### Advanced Ultra HDR edits

If you make more elaborate edits to an Ultra HDR image, the gain map is
preserved unchanged, which may not give you the results you want.

Common edits that might result in this situation include:

- **Adding stickers or emoji:** The added sticker would have the same luminosity and color vividness values as the area it was pasted on.
- **Overlaying a second image:** The new image would use the luminosity and color vividness information of the content it's overlaying.
- **Adding filters:** The old gain map's information might not be appropriate for the modified primary image.

In each case, the old luminosity and color vividness information is preserved,
but it might not be appropriate for the modified image.

If the original gain map is appropriate for the edited image, you don't have to
do anything. If you *do* want to modify the gain map, the usual workflow is:

1. **Fetch the image's current gain map** by calling [`Bitmap.getGainmap()`](https://developer.android.com/reference/android/graphics/Bitmap#getGainmap()) and cache it.
2. **Modify the primary image as desired.**
3. **Make corresponding edits to the cached gain map.** For example, if you
   pasted an emoji onto the primary image, you might set the corresponding
   portion of the gain map to a neutral value, like [`Color.GRAY`](https://developer.android.com/reference/android/graphics/Color#GRAY).

   | **Important:** The gain map might not have the same pixel dimensions as the primary image. For this reason, you need to calculate the appropriate pixels on the gain map that correspond to the edited areas on the primary image. For example, suppose the primary image is 8,000×4,000 pixels, and the gain map is 2,000×1,000 pixels. If you edit pixel (500,600) on the primary image, the corresponding pixel on the gain map would be at location (125,150).
4. **Apply the modified gain map back to the image** by calling
   [`Bitmap.setGainmap()`](https://developer.android.com/reference/android/graphics/Bitmap#setGainmap(android.graphics.Gainmap))).

### Additional resources

To learn more about Ultra HDR images, see the following additional resources:

- [Ultra HDR image format specification](https://developer.android.com/guide/topics/media/platform/hdr-image-format)