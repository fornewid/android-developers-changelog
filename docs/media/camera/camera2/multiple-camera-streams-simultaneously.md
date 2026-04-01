---
title: https://developer.android.com/media/camera/camera2/multiple-camera-streams-simultaneously
url: https://developer.android.com/media/camera/camera2/multiple-camera-streams-simultaneously
source: md.txt
---

**Note:** This page refers to the [Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary) package. Unless your app requires specific, low-level features from Camera2, we recommend using [CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

A camera application can use more than one stream of frames simultaneously. In
some cases, different streams even require a different frame resolution or pixel
format. Some typical use cases include:

- **Video recording**: one stream for preview, another being encoded and saved into a file.
- **Barcode scanning**: one stream for preview, another for barcode detection.
- **Computational photography**: one stream for preview, another for face/scene detection.

There is a non-trivial performance cost when processing frames, and the cost is
multiplied when doing parallel stream or pipeline processing.

Resources like CPU, GPU, and DSP might be able to take advantage of the
framework's [reprocessing](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#setRepeatingRequest%28android.hardware.camera2.CaptureRequest,%20android.hardware.camera2.CameraCaptureSession.CaptureCallback,%20android.os.Handler%29)
capabilities, but resources like memory will grow linearly.

## Multiple targets per request

Multiple camera streams can be combined into a single
[`CameraCaptureRequest`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest).
The following code snippet illustrates how to set up a camera session with one
stream for camera preview and another stream for image processing:  

### Kotlin

```kotlin
val session: CameraCaptureSession = ...  // from CameraCaptureSession.StateCallback

// You will use the preview capture template for the combined streams
// because it is optimized for low latency; for high-quality images, use
// TEMPLATE_STILL_CAPTURE, and for a steady frame rate use TEMPLATE_RECORD
val requestTemplate = CameraDevice.TEMPLATE_PREVIEW
val combinedRequest = session.device.createCaptureRequest(requestTemplate)

// Link the Surface targets with the combined request
combinedRequest.addTarget(previewSurface)
combinedRequest.addTarget(imReaderSurface)

// In this simple case, the SurfaceView gets updated automatically. ImageReader
// has its own callback that you have to listen to in order to retrieve the
// frames so there is no need to set up a callback for the capture request
session.setRepeatingRequest(combinedRequest.build(), null, null)
```

### Java

```java
CameraCaptureSession session = ...;  // from CameraCaptureSession.StateCallback

// You will use the preview capture template for the combined streams
// because it is optimized for low latency; for high-quality images, use
// TEMPLATE_STILL_CAPTURE, and for a steady frame rate use TEMPLATE_RECORD
        CaptureRequest.Builder combinedRequest = session.getDevice().createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);

// Link the Surface targets with the combined request
        combinedRequest.addTarget(previewSurface);
        combinedRequest.addTarget(imReaderSurface);

// In this simple case, the SurfaceView gets updated automatically. ImageReader
// has its own callback that you have to listen to in order to retrieve the
// frames so there is no need to set up a callback for the capture request
        session.setRepeatingRequest(combinedRequest.build(), null, null);
```

If you configure the target surfaces correctly, this code will produce only
streams that meet the minimum FPS determined by
[`StreamComfigurationMap.GetOutputMinFrameDuration(int, Size)`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputMinFrameDuration%28int,%20android.util.Size%29)
and
[`StreamComfigurationMap.GetOutputStallDuration(int, Size)`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputStallDuration%28int,%20android.util.Size%29).
Actual performance varies from device to device, though Android provides some
guarantees for supporting specific combinations depending on three variables:
*output type* , *output size* , and *hardware level*.

Using an unsupported combination of variables may work at a low frame rate; if
it does not, it will trigger one of the failure callbacks.
The documentation for [`createCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession%28java.util.List%3Candroid.view.Surface%3E,%20android.hardware.camera2.CameraCaptureSession.StateCallback,%20android.os.Handler%29)
describes what is guaranteed to work.

## Output type

*Output type* refers to the format in which the frames are encoded. The
possible values are PRIV, YUV, JPEG and RAW. The documentation for
[`createCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(java.util.List%3Candroid.view.Surface%3E,%20android.hardware.camera2.CameraCaptureSession.StateCallback,%20android.os.Handler))
describes them.

When choosing your application's output type, if the goal is to maximize
compatibility, then use
[`ImageFormat.YUV_420_888`](https://developer.android.com/reference/android/graphics/ImageFormat#YUV_420_888)
for frame analysis and
[`ImageFormat.JPEG`](https://developer.android.com/reference/android/graphics/ImageFormat#JPEG) for still
images. For preview and recording scenarios, you will likely be using a
[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView),
[`TextureView`](https://developer.android.com/reference/android/view/TextureView),
[`MediaRecorder`](https://developer.android.com/reference/android/media/MediaRecorder),
[`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec), or
[`RenderScript.Allocation`](https://developer.android.com/reference/android/renderscript/Allocation). In
those cases, do not specify an image format. For compatibility, it will count as
[`ImageFormat.PRIVATE`](https://developer.android.com/reference/android/graphics/ImageFormat#PRIVATE),
regardless of the actual format used internally. To query the formats supported
by a device given its
[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics),
use the following code:  

### Kotlin

```kotlin
val characteristics: CameraCharacteristics = ...
val supportedFormats = characteristics.get(
    CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP).outputFormats
```

### Java

```java
CameraCharacteristics characteristics = ...;
        int[] supportedFormats = characteristics.get(
CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP).getOutputFormats();
```

## Output size

All available *output sizes* are listed by
[`StreamConfigurationMap.getOutputSizes()`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputSizes%28int%29),
but only two are related to compatibility: `PREVIEW` and `MAXIMUM`. The sizes
act as upper bounds. If something of size `PREVIEW` works, then anything with a
size smaller than `PREVIEW` will also work. The same is true for `MAXIMUM`. The
documentation for
[`CameraDevice`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice)
explains these sizes.

The available output sizes depend on the choice of format. Given the
[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics)
and a format, you can query for the available output sizes like this:  

### Kotlin

```kotlin
val characteristics: CameraCharacteristics = ...
val outputFormat: Int = ...  // such as ImageFormat.JPEG
val sizes = characteristics.get(
    CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
    .getOutputSizes(outputFormat)
```

### Java

```java
CameraCharacteristics characteristics = ...;
        int outputFormat = ...;  // such as ImageFormat.JPEG
Size[] sizes = characteristics.get(
                CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
                .getOutputSizes(outputFormat);
```

In the camera preview and recording use cases, use the target class to determine
supported sizes. The format will be handled by the camera framework itself:  

### Kotlin

```kotlin
val characteristics: CameraCharacteristics = ...
val targetClass: Class <T> = ...  // such as SurfaceView::class.java
val sizes = characteristics.get(
    CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
    .getOutputSizes(targetClass)
```

### Java

```java
CameraCharacteristics characteristics = ...;
   int outputFormat = ...;  // such as ImageFormat.JPEG
   Size[] sizes = characteristics.get(
                CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)
                .getOutputSizes(outputFormat);
```

To get the `MAXIMUM` size, sort the output sizes by area and return the largest
one:  

### Kotlin

```kotlin
fun <T>getMaximumOutputSize(
    characteristics: CameraCharacteristics, targetClass: Class <T>, format: Int? = null):
    Size {
  val config = characteristics.get(
      CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)

  // If image format is provided, use it to determine supported sizes; or else use target class
  val allSizes = if (format == null)
    config.getOutputSizes(targetClass) else config.getOutputSizes(format)
  return allSizes.maxBy { it.height * it.width }
}
```

### Java

```java
 @RequiresApi(api = Build.VERSION_CODES.N)
    <T> Size getMaximumOutputSize(CameraCharacteristics characteristics,
                                            Class <T> targetClass,
                                            Integer format) {
        StreamConfigurationMap config = characteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP);

        // If image format is provided, use it to determine supported sizes; else use target class
        Size[] allSizes;
        if (format == null) {
            allSizes = config.getOutputSizes(targetClass);
        } else {
            allSizes = config.getOutputSizes(format);
        }
        return Arrays.stream(allSizes).max(Comparator.comparing(s -> s.getHeight() * s.getWidth())).get();
    }
```

`PREVIEW` refers to the best size match to the device's screen resolution or to
1080p (1920x1080), whichever is smaller. The aspect ratio may not match the
screen's aspect ratio exactly, so you may need to apply letter-boxing or
cropping to the stream to display it in full screen mode. To get the right
preview size, compare the available output sizes with the display size while
taking into account that the display may be rotated.

The following code defines a helper class, `SmartSize`, that will make size
comparisons a little easier:  

### Kotlin

```kotlin
/** Helper class used to pre-compute shortest and longest sides of a [Size] */
class SmartSize(width: Int, height: Int) {
    var size = Size(width, height)
    var long = max(size.width, size.height)
    var short = min(size.width, size.height)
    override fun toString() = "SmartSize(${long}x${short})"
}

/** Standard High Definition size for pictures and video */
val SIZE_1080P: SmartSize = SmartSize(1920, 1080)

/** Returns a [SmartSize] object for the given [Display] */
fun getDisplaySmartSize(display: Display): SmartSize {
    val outPoint = Point()
    display.getRealSize(outPoint)
    return SmartSize(outPoint.x, outPoint.y)
}

/**
 * Returns the largest available PREVIEW size. For more information, see:
 * https://d.android.com/reference/android/hardware/camera2/CameraDevice
 */
fun <T>getPreviewOutputSize(
        display: Display,
        characteristics: CameraCharacteristics,
        targetClass: Class <T>,
        format: Int? = null
): Size {

    // Find which is smaller: screen or 1080p
    val screenSize = getDisplaySmartSize(display)
    val hdScreen = screenSize.long >= SIZE_1080P.long || screenSize.short >= SIZE_1080P.short
    val maxSize = if (hdScreen) SIZE_1080P else screenSize

    // If image format is provided, use it to determine supported sizes; else use target class
    val config = characteristics.get(
            CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!
    if (format == null)
        assert(StreamConfigurationMap.isOutputSupportedFor(targetClass))
    else
        assert(config.isOutputSupportedFor(format))
    val allSizes = if (format == null)
        config.getOutputSizes(targetClass) else config.getOutputSizes(format)

    // Get available sizes and sort them by area from largest to smallest
    val validSizes = allSizes
            .sortedWith(compareBy { it.height * it.width })
            .map { SmartSize(it.width, it.height) }.reversed()

    // Then, get the largest output size that is smaller or equal than our max size
    return validSizes.first { it.long <= maxSize.long && it.short <= maxSize.short }.size
}
```

### Java

```java
/** Helper class used to pre-compute shortest and longest sides of a [Size] */
    class SmartSize {
        Size size;
        double longSize;
        double shortSize;

        public SmartSize(Integer width, Integer height) {
            size = new Size(width, height);
            longSize = max(size.getWidth(), size.getHeight());
            shortSize = min(size.getWidth(), size.getHeight());
        }

        @Override
        public String toString() {
            return String.format("SmartSize(%sx%s)", longSize, shortSize);
        }
    }

    /** Standard High Definition size for pictures and video */
    SmartSize SIZE_1080P = new SmartSize(1920, 1080);

    /** Returns a [SmartSize] object for the given [Display] */
    SmartSize getDisplaySmartSize(Display display) {
        Point outPoint = new Point();
        display.getRealSize(outPoint);
        return new SmartSize(outPoint.x, outPoint.y);
    }

    /**
     * Returns the largest available PREVIEW size. For more information, see:
     * https://d.android.com/reference/android/hardware/camera2/CameraDevice
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    <T> Size getPreviewOutputSize(
            Display display,
            CameraCharacteristics characteristics,
            Class <T> targetClass,
            Integer format
    ){

        // Find which is smaller: screen or 1080p
        SmartSize screenSize = getDisplaySmartSize(display);
        boolean hdScreen = screenSize.longSize >= SIZE_1080P.longSize || screenSize.shortSize >= SIZE_1080P.shortSize;
        SmartSize maxSize;
        if (hdScreen) {
            maxSize = SIZE_1080P;
        } else {
            maxSize = screenSize;
        }

        // If image format is provided, use it to determine supported sizes; else use target class
        StreamConfigurationMap config = characteristics.get(
                CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP);
        if (format == null)
            assert(StreamConfigurationMap.isOutputSupportedFor(targetClass));
        else
            assert(config.isOutputSupportedFor(format));
        Size[] allSizes;
        if (format == null) {
            allSizes = config.getOutputSizes(targetClass);
        } else {
            allSizes = config.getOutputSizes(format);
        }

        // Get available sizes and sort them by area from largest to smallest
        List <Size> sortedSizes = Arrays.asList(allSizes);
        List <SmartSize> validSizes =
                sortedSizes.stream()
                        .sorted(Comparator.comparing(s -> s.getHeight() * s.getWidth()))
                        .map(s -> new SmartSize(s.getWidth(), s.getHeight()))
                        .sorted(Collections.reverseOrder()).collect(Collectors.toList());

        // Then, get the largest output size that is smaller or equal than our max size
        return validSizes.stream()
                .filter(s -> s.longSize <= maxSize.longSize && s.shortSize <= maxSize.shortSize)
                .findFirst().get().size;
    }
```

## Check the supported hardware level

To determine the available capabilities at runtime, check the supported hardware
level using
[`CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL).

With a
[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics)
object, you can retrieve the hardware level with a single statement:  

### Kotlin

```kotlin
val characteristics: CameraCharacteristics = ...

// Hardware level will be one of:
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_EXTERNAL,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_LIMITED,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_FULL,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_3
val hardwareLevel = characteristics.get(
        CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL)
```

### Java

```java
CameraCharacteristics characteristics = ...;

// Hardware level will be one of:
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_EXTERNAL,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_LIMITED,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_FULL,
// - CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_3
Integer hardwareLevel = characteristics.get(
                CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL);
```

## Putting all the pieces together

With output type, output size, and hardware level, you can determine which
combinations of streams are valid. The following chart is a snapshot of the
configurations supported by a `CameraDevice` with
[`LEGACY`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY)
hardware level.

| Target 1 || Target 2 || Target 3 || Sample use case(s) |
| Type | Max size | Type | Max size | Type | Max size | Sample use case(s) |
|---|---|---|---|---|---|---|
| `PRIV` | `MAXIMUM` |   |   |   |   | Simple preview, GPU video processing, or no-preview video recording. |
| `JPEG` | `MAXIMUM` |   |   |   |   | No-viewfinder still image capture. |
| `YUV` | `MAXIMUM` |   |   |   |   | In-application video/image processing. |
| `PRIV` | `PREVIEW` | `JPEG` | `MAXIMUM` |   |   | Standard still imaging. |
| `YUV` | `PREVIEW` | `JPEG` | `MAXIMUM` |   |   | In-app processing plus still capture. |
| `PRIV` | `PREVIEW` | `PRIV` | `PREVIEW` |   |   | Standard recording. |
| `PRIV` | `PREVIEW` | `YUV` | `PREVIEW` |   |   | Preview plus in-app processing. |
| `PRIV` | `PREVIEW` | `YUV` | `PREVIEW` | `JPEG` | `MAXIMUM` | Still capture plus in-app processing. |

`LEGACY` is the lowest possible hardware level. This table shows that every
device that supports Camera2 (API level 21 and higher) can output up to three
simultaneous streams using the right configuration and if there isn't too much
overhead  limiting performance, such as memory, CPU, or thermal constraints.

Your app also needs to configure targeting output buffers. For example, to
target a device with `LEGACY` hardware level, you could set up two target output
surfaces, one using `ImageFormat.PRIVATE` and another using
`ImageFormat.YUV_420_888`. This is a supported combination while using the
`PREVIEW` size. Using the function defined earlier in this topic, getting the
required preview sizes for a camera ID requires the following code:  

### Kotlin

```kotlin
val characteristics: CameraCharacteristics = ...
val context = this as Context  // assuming you are inside of an activity

val surfaceViewSize = getPreviewOutputSize(
    context, characteristics, SurfaceView::class.java)
val imageReaderSize = getPreviewOutputSize(
    context, characteristics, ImageReader::class.java, format = ImageFormat.YUV_420_888)
```

### Java

```java
CameraCharacteristics characteristics = ...;
        Context context = this; // assuming you are inside of an activity

        Size surfaceViewSize = getPreviewOutputSize(
                context, characteristics, SurfaceView.class);
        Size imageReaderSize = getPreviewOutputSize(
                context, characteristics, ImageReader.class, format = ImageFormat.YUV_420_888);
```

It requires waiting until `SurfaceView` is ready using the provided callbacks:  

### Kotlin

```kotlin
val surfaceView = findViewById <SurfaceView>(...)
surfaceView.holder.addCallback(object : SurfaceHolder.Callback {
  override fun surfaceCreated(holder: SurfaceHolder) {
    // You do not need to specify image format, and it will be considered of type PRIV
    // Surface is now ready and you could use it as an output target for CameraSession
  }
  ...
})
```

### Java

```java
SurfaceView surfaceView = findViewById <SurfaceView>(...);

surfaceView.getHolder().addCallback(new SurfaceHolder.Callback() {
            @Override
            public void surfaceCreated(@NonNull SurfaceHolder surfaceHolder) {
                // You do not need to specify image format, and it will be considered of type PRIV
                // Surface is now ready and you could use it as an output target for CameraSession
            }
            ...
        });
```

You can force the `SurfaceView` to match the camera output size by calling
[`SurfaceHolder.setFixedSize()`](https://developer.android.com/reference/android/view/SurfaceHolder#setFixedSize%28int,%20int%29)
or you can take an approach similar to
[`AutoFitSurfaceView`](https://github.com/android/camera-samples/blob/3d1a254eb018a51ff39ae78d39a9e9e7942a027b/Common/src/main/java/com/example/android/camera2/common/AutoFitSurfaceView.kt) from the [Common
module](https://github.com/android/camera-samples/tree/3d1a254eb018a51ff39ae78d39a9e9e7942a027b/Common)
of the camera samples on GitHub, which sets an absolute size, taking into
consideration both the aspect ratio and the available space, while automatically
adjusting when activity changes are triggered.

Setting up the other surface from
[`ImageReader`](https://developer.android.com/reference/android/media/ImageReader) with the desired format is
easier, since there are no callbacks to wait for:  

### Kotlin

```kotlin
val frameBufferCount = 3  // just an example, depends on your usage of ImageReader
val imageReader = ImageReader.newInstance(
    imageReaderSize.width, imageReaderSize.height, ImageFormat.YUV_420_888,
    frameBufferCount)
```

### Java

```java
int frameBufferCount = 3;  // just an example, depends on your usage of ImageReader
ImageReader imageReader = ImageReader.newInstance(
                imageReaderSize.width, imageReaderSize.height, ImageFormat.YUV_420_888,
                frameBufferCount);
```

When using a blocking target buffer like `ImageReader`, discard the frames after
using them:  

### Kotlin

```kotlin
imageReader.setOnImageAvailableListener({
  val frame =  it.acquireNextImage()
  // Do something with "frame" here
  it.close()
}, null)
```

### Java

```java
imageReader.setOnImageAvailableListener(listener -> {
            Image frame = listener.acquireNextImage();
            // Do something with "frame" here
            listener.close();
        }, null);
```

`LEGACY` hardware level targets the lowest common denominator  devices. You can
add conditional branching and use `RECORD` size for one of the output target
surfaces in devices with `LIMITED` hardware level, or even increase it to
`MAXIMUM` size for devices with `FULL` hardware level.