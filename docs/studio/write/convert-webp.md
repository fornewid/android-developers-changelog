---
title: https://developer.android.com/studio/write/convert-webp
url: https://developer.android.com/studio/write/convert-webp
source: md.txt
---

# Create WebP images

[WebP](https://developers.google.com/speed/webp/)is an image file format from Google that provides lossy compression (like JPEG) as well as transparency (like PNG) but can provide better compression than either JPEG or PNG. Lossy WebP images are supported in Android 4.0 (API level 14) and higher, and lossless and transparent WebP images are supported in Android 4.3 (API level 18) and higher. This page shows how to convert images to WebP format and how to convert WebP images to PNG format.
| **Note:** Because support for lossless and transparent WebP images is only available in Android 4.3 and higher, your project must declare a`minSdkVersion`of 18 or higher to create lossless or transparent WebP images using Android Studio.

For more information about selecting the correct image format to improve download speed, see[Reduce image download sizes](https://developer.android.com/topic/performance/network-xfer#webp).

## Convert images to WebP

Android Studio can convert PNG, JPG, BMP, or static GIF images to WebP format. You can convert individual images or folders of images.

To convert an image or folder of images, proceed as follows:

1. Right-click an image file or a folder containing image files, and then click**Convert to WebP**.
2. The**Converting Images to WebP** dialog opens. The default settings depend on the`minSdkVersion`setting for the current module.

   <br />

   ![The Converting Images to WebP dialog](https://developer.android.com/static/studio/images/write/webp-convertimage_2x.png)**Figure 1.**The Converting Images to WebP dialog.
3. Select either lossy or lossless encoding.

   Lossless encoding is only available if your`minSdkVersion`is set to 18 or higher.

   If you select lossy encoding, set the encoding quality and choose whether to preview each converted image before saving.

   You can also choose to skip the conversion of any files where the encoded version would be larger than the original or any files with transparency or an alpha channel. Because Android Studio only lets you create transparent WebP images if your`minSdkVersion`is set to 18 or higher, the**Skip images with transparency/alpha channel** checkbox is automatically selected if your`minSdkVersion`is lower than 18.

   **Note:**9-patch files can't be converted to WebP images. The converter tool always automatically skips 9-patch images.
4. Click**OK**to begin the conversion.

   If you are converting more than one image, the conversion is a single step, and can be undone to revert all the images you converted at once.

   If you selected lossless conversion, the conversion happens immediately. Your images are converted in their original location. If you selected lossy conversion, continue to the next step.
5. If you selected lossy conversion and you chose to preview each converted image before saving, Android Studio shows you each image during the conversion so you can inspect the conversion result. During the preview step, you can adjust the quality setting for each image individually, as shown in figure 2.

   If you did not choose to preview the converted images, Android Studio skips this step and converts your images immediately.
   ![Converting a JPG to WebP format at 75% quality](https://developer.android.com/static/studio/images/write/webp-convertqualitydefault_2x.png)**Figure 2.**Previewing the conversion of a JPG image to WebP format at 75% quality.

   Figure 2 shows the original JPG image on the left and the lossy-encoded WebP image on the right. The dialog shows the file size for the original and the converted image. You can drag the slider left or right to change the quality setting and immediately see the effect on the encoded image and the file size.

   The middle area shows the pixels that differ between the original image and the encoded image. In figure 2, with the quality set to 75%, there's almost no difference between the two images. Figure 3 shows the same image encoded with the quality set to 0%.
   ![Converting a JPG to WebP format at 0% quality](https://developer.android.com/static/studio/images/write/webp-convertqualitylow_2x.png)**Figure 3.**Previewing the conversion of a JPG image to WebP format at 0% quality.

   **Note:** If you set the quality to 100% and the`minSdkVersion`is set to 18 or higher, Android Studio automatically switches to lossless encoding instead.

   Select a quality setting for each image you review. If you are converting more than one image, click**Next**to advance to the next image.
6. Click**Finish**. Your images are converted in their original location.

## Convert WebP images to PNG

If you want to use a WebP image from your project for another purpose---for example, in a web page that needs to correctly display images in a browser without WebP support---you can use Android Studio to convert WebP images to PNG format.

To convert a WebP image to PNG, proceed as follows:

1. Right-click a WebP image in Android Studio, and then click**Convert to PNG**.
2. A dialog appears, asking whether you would like to delete the original WebP file after conversion or keep the original WebP file as well as the new PNG file.

   Click**Yes** to delete the original WebP file or**No**to retain the WebP file in addition to the PNG file. Your image is converted immediately.