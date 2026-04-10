---
title: https://developer.android.com/training/wearables/watch-faces/performance
url: https://developer.android.com/training/wearables/watch-faces/performance
source: md.txt
---

# Optimize watch faces

A Wear OS watch face runs continuously, so it must use power efficiently.

Optimize the performance of the watch face as much as possible. This page provides best practices for overall watch face optimizations as well as best practices targeted to animations and images.

## Basic optimization

This section contains best practices for improving the overall efficiency of your watch face.

### Watch face color and brightness

Using dark colors in your watch face draws less power from the user's watch. The following are recommendations for setting the watch face background to optimize the watch face's battery use:

- **Color:**whenever possible, use a black background.
- **Brightness:** when a black background is not possible, keep the brightness of the background color at or below 25% on a hue, saturation, value (HSV) or hue, saturation, brightness (HSB) scale. For example, if you use the[`Color`](https://developer.android.com/reference/android/graphics/Color)class to set a background color defined with the HSV scale, use 25 or lower for the value setting, which controls brightness.

### Use dynamic capabilities to interact with the phone

When a watch face requires an operation to run on the phone, execute the code only when the watch face is active. The recommended method for letting the app on the phone learn that the corresponding watch face is active is the[CapabilityClient API](https://developers.google.com/android/reference/com/google/android/gms/wearable/CapabilityClient).

### Monitor power consumption

The[Wear OS companion app](https://play.google.com/store/apps/details?id=com.google.android.wearable.app&hl=en)lets developers and users see how much battery is consumed by different processes on the wearable device. To see this, navigate to**Settings** \>**Watch battery**.

### Register encryption-aware watch faces

Android 7.0 and higher include support for file-based encryption and let[encryption-aware](https://developer.android.com/training/articles/direct-boot)applications run before the user has provided the decryption passcode at bootup. This can reduce the duration of transitioning from boot animation to the watch face by up to 30 seconds.

To enable faster bootup, add`android:directBootAware="true"`to the watch face manifest.

**Note:**Use this feature with watch faces that don't use credential-encrypted storage.

## Best practices for animations

The best practices in this section help reduce the power consumption associated with animations.

### Reduce the frame rate of animations

Animations are often computationally expensive and consume a significant amount of power. Most animations look fluid at 30 frames per second, so avoid running your animations at a higher frame rate. Instead, you can use dynamic frame rates. For more information, see the[Example Canvas Watch Face](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:wear/watchface/watchface/samples/src/main/java/androidx/wear/watchface/samples/ExampleCanvasDigitalWatchFaceService.kt;l=893?q=this.interactiveDrawModeUpdateDelayMillis+%3D).

### Let the CPU sleep between animations

To maximize battery life, use animations sparingly. Even a blinking colon uses battery power with every blink.

Animations and small changes to the contents of the watch face wake up the CPU. Let the CPU sleep between animations by, for example, using short bursts of animation every second in interactive mode and then letting the CPU sleep until the next second. Letting the CPU sleep often, even briefly, can significantly reduce power consumption.

## Best practices for images

The best practices in this section help reduce the power consumption associated with images.

## Reduce the size of your bitmap assets

Many watch faces consist of a background image plus other graphic assets that are transformed and overlaid onto the background image, such as clock hands and other elements that move over time. The larger these graphic assets are, the more computationally expensive it is to transform them. Typically, these graphic elements are rotated, and sometimes scaled, inside the[`Render.CanvasRenderer.render()`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/Renderer.CanvasRenderer#render(android.graphics.Canvas,android.graphics.Rect,java.time.ZonedDateTime))method every time the system redraws the watch face, as described in[Draw a watch face](https://developer.android.com/training/wearables/watch-faces/drawing#Drawing).  
![](https://developer.android.com/static/training/wearables/watch-faces/images/ClockHandFull.png)![](https://developer.android.com/static/training/wearables/watch-faces/images/ClockHandCropped.png)

**Figure 1.**Crop clock hands to remove extra pixels.

Reducing the size of your bitmap assets improves the performance of your animations and saves power. Follow these tips to improve the performance of your watch face:

- Don't use graphic elements that are larger than you need.
- Remove extra transparent pixels around the edges.

For example, the size of the clock hand image on the left in figure 1 can be reduced by 97% by removing the extra transparent pixels, as shown on the right side of the figure.

## Combine bitmap assets

If you have bitmaps that are often drawn together, consider combining them into a single graphic asset. For example, you can often combine the background image in interactive mode with the tick marks to avoid drawing two full-screen bitmaps every time the system redraws the watch face.

## Disable anti-aliasing when drawing scaled bitmaps

When you draw a scaled bitmap on the[Canvas](https://developer.android.com/reference/android/graphics/Canvas)object using the[Canvas.drawBitmap()](https://developer.android.com/reference/android/graphics/Canvas#drawBitmap(android.graphics.Bitmap, float, float, android.graphics.Paint))method, you can provide a[Paint](https://developer.android.com/reference/android/graphics/Paint)instance to configure several options. To improve performance, disable anti-aliasing using the[setAntiAlias()](https://developer.android.com/reference/android/graphics/Paint#setAntiAlias(boolean))method, since this option doesn't have any effect on bitmaps.  
![](https://developer.android.com/static/training/wearables/watch-faces/images/BitmapFilterDisabled.png)![](https://developer.android.com/static/training/wearables/watch-faces/images/BitmapFilterEnabled.png)

**Figure 2.**Example of bitmap filtering disabled (left) and enabled (right).

## Use bitmap filtering

For bitmap assets that you draw on top of other elements, enable bitmap filtering on the same`Paint`instance using the[setFilterBitmap()](https://developer.android.com/reference/android/graphics/Paint#setFilterBitmap(boolean))method. Figure 2 shows a magnified view of a clock hand with and without bitmap filtering.

**Note:**When ambient mode is active, disable bitmap filtering. In low-bit ambient mode, the system does not reliably render the colors in the image for bitmap filtering to process successfully.

## Move expensive operations outside the drawing method

The system calls the`Render.CanvasRenderer.render()`method every time it redraws your watch face. To improve performance, only include operations inside this method that are strictly required to update the watch face.

<br />

When possible, avoid performing the following operations inside the`Render.CanvasRenderer.render()`method:

- Loading images and other resources
- Resizing images
- Allocating objects
- Computations whose results don't change between frames

To analyze the performance of your watch face, use the CPU Profiler. In particular, make sure that the execution time for your`Render.CanvasRenderer.render()`implementation is short and consistent across invocations. For more information, see[Inspect CPU activity with CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler).

## Related resources

The[watch face sample app](https://github.com/android/wear-os-samples)demonstrates the best practices for configuring a watch face.