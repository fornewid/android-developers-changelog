---
title: https://developer.android.com/training/wearables/watch-faces/designing
url: https://developer.android.com/training/wearables/watch-faces/designing
source: md.txt
---

# Design watch faces

Custom watch faces leverage a dynamic, digital canvas that can include colors, animations, and contextual information.

Creating a watch face for Wear OS involves visualizing time clearly, just as you would for a traditional watch face. Wear devices provide advanced capabilities for watch faces that you can leverage in your designs, such as vibrant colors, dynamic backgrounds, animations, and data integration. However, there are also many design considerations to take into account.

To design a watch face without coding, see[Watch Face Studio](https://developer.samsung.com/watch-face-studio/user-guide).

To begin designing a watch face, review other examples of watch faces. Download the[Wear OS companion app](https://play.google.com/store/apps/details?id=com.google.android.wearable.app)to browse a large selection of watch faces.

## Plan the implementation of the watch face

After you finalize the design for your watch face, you need to determine how to obtain any necessary data and draw the watch face on the wearable device. Most implementations consist of the following components:

- One or more background images.
- Application code that retrieves the required data.
- Application code that draws text and shapes over the background images.

Apps typically show different background images for the interactive and ambient modes. It can be difficult to create a good-looking image for ambient mode. Therefore, ambient mode backgrounds are often completely black or grey with no image.

Background images for Wear devices with a screen density of hdpi should be 320 by 320 pixels in size. The corners of the background image aren't visible on round devices. In your code, you can detect the size of the device screen and scale down the background image if the device has a lower resolution than your image. To improve performance, scale the background image only once and store the resulting bitmap.

Run the application code to retrieve contextual data only as often as required and store the results to reuse the data every time you draw the watch face. For example, you don't need to fetch weather updates every minute.

Keep the application code that draws your watch face in ambient mode relatively simple to increase battery life. You usually draw outlines of shapes using a limited set of colors in this mode. In interactive mode, you can use full color, complex shapes, gradients, and animations to draw your watch face.

The remaining lessons in this class show you how to implement watch faces in detail.

## Related resources

Refer to the following related resources:

- [WatchFace sample](https://github.com/android/wear-os-samples)