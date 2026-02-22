---
title: https://developer.android.com/media/camera/camerax/configuration
url: https://developer.android.com/media/camera/camerax/configuration
source: md.txt
---

You configure each CameraX use case to control different aspects of the use
case's operations.

For example, with the image capture use case, you can set a target aspect ratio
and a flash mode. The following code shows one example:  

### Kotlin

```kotlin
val imageCapture = ImageCapture.Builder()
    .setFlashMode(...)
    .setTargetAspectRatio(...)
    .build()
```

### Java

```java
ImageCapture imageCapture =
    new ImageCapture.Builder()
        .setFlashMode(...)
        .setTargetAspectRatio(...)
        .build();
```

In addition to configuration options, some use cases expose APIs to dynamically
alter settings after the use case has been created. For information about
configuration that is specific to the individual use cases, see [Implement a
preview](https://developer.android.com/training/camerax/preview), [Analyze
images](https://developer.android.com/training/camerax/analyze), and [Image
capture](https://developer.android.com/training/camerax/take-photo).

## CameraXConfig

For simplicity, CameraX has default configurations such as internal executors
and handlers that are suitable for most usage scenarios. However, if your
application has special requirements or prefers to customize those
configurations, [`CameraXConfig`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig)
is the interface for that purpose.

With `CameraXConfig`, an application can do the following:

- Optimize startup latency with [`setAvailableCameraLimiter()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setAvailableCamerasLimiter(androidx.camera.core.CameraSelector)).
- Provide the application's executor to CameraX with [`setCameraExecutor()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setCameraExecutor(java.util.concurrent.Executor)).
- Replace the default scheduler handler with [`setSchedulerHandler()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setSchedulerHandler(android.os.Handler)).
- Change the logging level with [`setMinimumLoggingLevel()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setMinimumLoggingLevel(int)).

### Usage Model

The following procedure describes how to use `CameraXConfig`:

1. Create a `CameraXConfig` object with your customized configurations.
2. Implement the [`CameraXConfig.Provider`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Provider) interface in your [`Application`](https://developer.android.com/reference/android/app/Application), and return your `CameraXConfig` object in [`getCameraXConfig()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Provider#getCameraXConfig()).
3. Add your `Application` class to your `AndroidManifest.xml` file, as described [here](https://developer.android.com/reference/android/app/Application).

For example, the following code sample restricts CameraX logging to error
messages only:  

### Kotlin

```kotlin
class CameraApplication : Application(), CameraXConfig.Provider {
   override fun getCameraXConfig(): CameraXConfig {
       return CameraXConfig.Builder.fromConfig(Camera2Config.defaultConfig())
           .setMinimumLoggingLevel(Log.ERROR).build()
   }
}
```

Keep a local copy of the `CameraXConfig` object if your application needs to
know the CameraX configuration after setting it.

### Camera Limiter

During the first invocation of
[`ProcessCameraProvider.getInstance()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#getInstance(android.content.Context)),
CameraX enumerates and queries characteristics of the cameras available on the
device. Because CameraX needs to communicate with hardware components, this
process can take a non-trivial amount of time for each camera, particularly on
low-end devices. If your application only uses specific cameras on the device,
such as the default front camera, you can set CameraX to ignore other cameras,
which can reduce startup latency for the cameras your application uses.

If the [`CameraSelector`](https://developer.android.com/reference/androidx/camera/core/CameraSelector) passed
to
[`CameraXConfig.Builder.setAvailableCamerasLimiter()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setAvailableCamerasLimiter(androidx.camera.core.CameraSelector))
filters out a camera, CameraX behaves as if that camera doesn't exist. For
example, the following code limits the application to only use the device's
default back camera:  

### Kotlin

```kotlin
class MainApplication : Application(), CameraXConfig.Provider {
   override fun getCameraXConfig(): CameraXConfig {
       return CameraXConfig.Builder.fromConfig(Camera2Config.defaultConfig())
              .setAvailableCamerasLimiter(CameraSelector.DEFAULT_BACK_CAMERA)
              .build()
   }
}
```

### Threads

Many of the platform APIs on which CameraX is built require blocking
interprocess communication (IPC) with hardware that can sometimes take hundreds
of milliseconds to respond. For this reason, CameraX only calls these APIs from
background threads, so that the main thread isn't blocked and the UI
remains fluid. CameraX internally manages these background threads so that this
behavior appears transparent. However, some applications require strict control
of threads. `CameraXConfig` lets an application set the background threads
that are used through
[`CameraXConfig.Builder.setCameraExecutor()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setCameraExecutor(java.util.concurrent.Executor))
and
[`CameraXConfig.Builder.setSchedulerHandler()`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setSchedulerHandler(android.os.Handler)).
| **Note:** When providing a custom executor or scheduler handler, use one that doesn't execute code on the main thread.

### Camera Executor

The camera executor is used for all internal Camera platform API calls, as well
as for callbacks from these APIs. CameraX allocates and manages an internal
[`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor) to perform these tasks.
However, if your application requires stricter control of threads, use
`CameraXConfig.Builder.setCameraExecutor()`.

### Scheduler Handler

The scheduler handler is used to schedule internal tasks at fixed intervals,
such as retrying opening the camera when it isn't available. This handler does
not execute jobs, and only dispatches them to the camera executor. It is also
sometimes used on the legacy API platforms that require a
[`Handler`](https://developer.android.com/reference/android/os/Handler) for callbacks. In these cases, the
callbacks are still only dispatched directly to the camera executor. CameraX
allocates and manages an internal
[`HandlerThread`](https://developer.android.com/reference/android/os/HandlerThread) to perform these tasks,
but you can overridde it with `CameraXConfig.Builder.setSchedulerHandler()`.

### Logging

CameraX logging lets applications filter logcat messages, as it can be good
practice to avoid verbose messages in your production code. CameraX supports
four logging levels, from the most verbose to the most severe:

- `Log.DEBUG` (default)
- `Log.INFO`
- `Log.WARN`
- `Log.ERROR`

Refer to the [Android Log documentation](https://developer.android.com/reference/android/util/Log#DEBUG)
for detailed descriptions of these log levels. Use
[`CameraXConfig.Builder.setMinimumLoggingLevel(int)`](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setMinimumLoggingLevel(int))
to set the appropriate logging level for your application.

## Automatic selection

CameraX automatically provides functionality that is specific to the device that
your app is running on. For example, CameraX automatically determines the
best resolution to use if you don't specify a resolution, or if the resolution
you specify is unsupported. All of this is handled by the library, eliminating
the need for you to write device-specific code.

CameraX's goal is to successfully initialize a camera session. This means
CameraX compromises on resolution and aspect ratios based on device capability.
The compromise can happen because:

- The device doesn't support the requested resolution.
- The device has compatibility issues, such as legacy devices that require certain resolutions to operate correctly.
- On some devices, certain formats are only available at certain aspect ratios.
- The device has a preference for a "nearest mod16" for JPEG or video encoding. For more information, see [`SCALER_STREAM_CONFIGURATION_MAP`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SCALER_STREAM_CONFIGURATION_MAP).

Although CameraX creates and manages the session, always check the
returned image sizes on the use case output in your code and adjust accordingly.

## Rotation

By default, the camera rotation is set to match the default display's rotation
during the creation of the use case. In this default case, CameraX produces
outputs to let the app match what you expect to see in the
preview. You can change the rotation to a custom value to support multi-display
devices by passing in the current display orientation when configuring use case
objects or dynamically after they have been created.

Your app can set the target rotation using configuration settings. It can then
update rotation settings by using the methods from the use case APIs (such as
[`ImageAnalysis.setTargetRotation()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#setTargetRotation(int))),
even while the lifecycle is in a running state. You might use this when the app
is locked to portrait mode---and so no reconfiguration occurs on
rotation---but the photo or analysis use case needs to be aware of the
current rotation of the device. For example, rotation awareness might be needed
so
faces are oriented correctly for face detection, or photos are set to landscape
or portrait.

Data for captured images might be stored without rotation information. Exif data
contains rotation information so that gallery applications can show the image in
the correct orientation after saving.

To display preview data with the correct orientation, you can use the metadata
output from
[`Preview.PreviewOutput()`](https://developer.android.com/reference/androidx/camera/core/Preview.PreviewOutput)
to create transforms.

The following code sample shows how to set the rotation on an orientation event:  

### Kotlin

```kotlin
override fun onCreate() {
    val imageCapture = ImageCapture.Builder().build()

    val orientationEventListener = object : OrientationEventListener(this as Context) {
        override fun onOrientationChanged(orientation : Int) {
            // Monitors orientation values to determine the target rotation value
            val rotation : Int = when (orientation) {
                in 45..134 -> Surface.ROTATION_270
                in 135..224 -> Surface.ROTATION_180
                in 225..314 -> Surface.ROTATION_90
                else -> Surface.ROTATION_0
            }

            imageCapture.targetRotation = rotation
        }
    }
    orientationEventListener.enable()
}
```

### Java

```java
@Override
public void onCreate() {
    ImageCapture imageCapture = new ImageCapture.Builder().build();

    OrientationEventListener orientationEventListener = new OrientationEventListener((Context)this) {
       @Override
       public void onOrientationChanged(int orientation) {
           int rotation;

           // Monitors orientation values to determine the target rotation value
           if (orientation >= 45 && orientation < 135) {
               rotation = Surface.ROTATION_270;
           } else if (orientation >= 135 && orientation < 225) {
               rotation = Surface.ROTATION_180;
           } else if (orientation >= 225 && orientation < 315) {
               rotation = Surface.ROTATION_90;
           } else {
               rotation = Surface.ROTATION_0;
           }

           imageCapture.setTargetRotation(rotation);
       }
    };

    orientationEventListener.enable();
}
```

Based on the set rotation, each use case either rotates the image data
directly or provides rotation metadata to the consumers of the non-rotated image
data.

- **Preview** : Metadata output is provided so that the rotation of the target resolution is known using [`Preview.getTargetRotation()`](https://developer.android.com/reference/androidx/camera/core/Preview#getTargetRotation()).
- **ImageAnalysis**: Metadata output is provided so that image buffer coordinates are known relative to display coordinates.
- **ImageCapture**: The image Exif metadata, buffer, or both the buffer and metadata are altered to note the rotation setting. The value altered depends upon the HAL implementation.

## Crop rect

By default, the crop rect is the full buffer rect. You can customize it with
[`ViewPort`](https://developer.android.com/reference/androidx/camera/core/ViewPort) and
[`UseCaseGroup`](https://developer.android.com/reference/androidx/camera/core/UseCaseGroup). By grouping use
cases and setting the viewport, CameraX guarantees that the crop rects of all
the use cases in the group point to the same area in the camera sensor.

The following code snippet shows how to use these two classes:  

### Kotlin

```kotlin
val viewPort =  ViewPort.Builder(Rational(width, height), display.rotation).build()
val useCaseGroup = UseCaseGroup.Builder()
    .addUseCase(preview)
    .addUseCase(imageAnalysis)
    .addUseCase(imageCapture)
    .setViewPort(viewPort)
    .build()
cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, useCaseGroup)
```

### Java

```java
ViewPort viewPort = new ViewPort.Builder(
         new Rational(width, height),
         getDisplay().getRotation()).build();
UseCaseGroup useCaseGroup = new UseCaseGroup.Builder()
    .addUseCase(preview)
    .addUseCase(imageAnalysis)
    .addUseCase(imageCapture)
    .setViewPort(viewPort)
    .build();
cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, useCaseGroup);
```

`ViewPort` defines the buffer rect visible to end users. Then CameraX calculates
the largest possible crop rect based on the properties of the viewport and the
attached use cases. Usually, to achieve a WYSIWYG effect, you can configure
the viewport based on the preview use case. A simple way to get the viewport is
to use [`PreviewView`](https://developer.android.com/training/camerax/preview#implementation).

The following code snippets shows how to get the `ViewPort` object:  

### Kotlin

```kotlin
val viewport = findViewById<PreviewView>(R.id.preview_view).viewPort
```

### Java

```java
ViewPort viewPort = ((PreviewView)findViewById(R.id.preview_view)).getViewPort();
```

In the preceding example, what the app gets from `ImageAnalysis` and
`ImageCapture` matches what the end user sees in `PreviewView`, assuming the
`PreviewView`'s scale type is set to the default, `FILL_CENTER`. After applying
the crop rect and rotation to the output buffer, the image from all use cases
is the same, though possibly with different resolutions. For more
information about how to apply the transformation info, see [transform
output](https://developer.android.com/training/camerax/transform-output).

## Camera selection

CameraX automatically selects the best camera device for your application's
requirements and use cases. If you wish to use a different device than the one
selected for you, there are a few options:

- Request the default front facing camera with [`CameraSelector.DEFAULT_FRONT_CAMERA`](https://developer.android.com/reference/androidx/camera/core/CameraSelector#DEFAULT_FRONT_CAMERA).
- Request the default rear facing camera with [`CameraSelector.DEFAULT_BACK_CAMERA`](https://developer.android.com/reference/androidx/camera/core/CameraSelector#DEFAULT_BACK_CAMERA).
- Filter the list of available devices by their [`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics) with [`CameraSelector.Builder.addCameraFilter()`](https://developer.android.com/reference/androidx/camera/core/CameraSelector.Builder#addCameraFilter(androidx.camera.core.CameraFilter)).

| **Note:** Camera devices must be recognized by the system and appear in `CameraManager.getCameraIdList()` before they can be used.
|
| Additionally, each OEM is responsible for choosing whether to support external camera devices. So be sure to check that `PackageManager.FEATURE_CAMERA_EXTERNAL` is enabled before attempting to use any external cameras.

The following code sample illustrates how to create a `CameraSelector` to
influence device selection:  

### Kotlin

```kotlin
fun selectExternalOrBestCamera(provider: ProcessCameraProvider):CameraSelector? {
   val cam2Infos = provider.availableCameraInfos.map {
       Camera2CameraInfo.from(it)
   }.sortedByDescending {
       // HARDWARE_LEVEL is Int type, with the order of:
       // LEGACY < LIMITED < FULL < LEVEL_3 < EXTERNAL
       it.getCameraCharacteristic(CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL)
   }

   return when {
       cam2Infos.isNotEmpty() -> {
           CameraSelector.Builder()
               .addCameraFilter {
                   it.filter { camInfo ->
                       // cam2Infos[0] is either EXTERNAL or best built-in camera
                       val thisCamId = Camera2CameraInfo.from(camInfo).cameraId
                       thisCamId == cam2Infos[0].cameraId
                   }
               }.build()
       }
       else -> null
    }
}

// create a CameraSelector for the USB camera (or highest level internal camera)
val selector = selectExternalOrBestCamera(processCameraProvider)
processCameraProvider.bindToLifecycle(this, selector, preview, analysis)
```

## Select multiple cameras concurrently

Starting with CameraX 1.3, you can also select multiple cameras concurrently.
For example, you can bind to a front and back camera to take photos or record
videos from both perspectives simultaneously.

When using the Concurrent Camera feature, the device can operate two cameras
with different-facing lenses at the same time, or operate two back cameras at
the same time. The following code block shows how to set two cameras when
calling `bindToLifecycle`, and how to get both Camera objects from the returned
`ConcurrentCamera` object.  

### Kotlin

```kotlin
// Build ConcurrentCameraConfig
val primary = ConcurrentCamera.SingleCameraConfig(
    primaryCameraSelector,
    useCaseGroup,
    lifecycleOwner
)

val secondary = ConcurrentCamera.SingleCameraConfig(
    secondaryCameraSelector,
    useCaseGroup,
    lifecycleOwner
)

val concurrentCamera = cameraProvider.bindToLifecycle(
    listOf(primary, secondary)
)

val primaryCamera = concurrentCamera.cameras[0]
val secondaryCamera = concurrentCamera.cameras[1]
```

### Java

```java
// Build ConcurrentCameraConfig
SingleCameraConfig primary = new SingleCameraConfig(
    primaryCameraSelector,
    useCaseGroup,
    lifecycleOwner
);

SingleCameraConfig secondary = new SingleCameraConfig(
    primaryCameraSelector,
    useCaseGroup,
    lifecycleOwner
);

ConcurrentCamera concurrentCamera =  
    mCameraProvider.bindToLifecycle(Arrays.asList(primary, secondary));

Camera primaryCamera = concurrentCamera.getCameras().get(0);
Camera secondaryCamera = concurrentCamera.getCameras().get(1);
```

## Camera resolution

You can choose to let CameraX set the image resolution based on a combination
of the device capabilities, device's supported [hardware
level](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL),
use case, and provided aspect ratio. Alternatively, you can set a specific
target resolution or a specific aspect ratio in use cases that support that
configuration.

### Automatic resolution

CameraX can automatically determine the best resolution settings based on the
use cases specified in `cameraProcessProvider.bindToLifecycle()`. Whenever
possible, specify all the use cases needed to run concurrently in a single
session in a single `bindToLifecycle()` call. CameraX determines resolutions
based on the set of use cases bound by considering the device's supported
hardware level and by accounting for device-specific variance (where a device
exceeds or doesn't meet the [stream configurations
available](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(android.hardware.camera2.params.SessionConfiguration))).
The intent is to let the application run on a wide variety of devices while
minimizing device-specific code paths.

The default aspect ratio for image capture and image analysis use cases is 4:3.

Use cases have a configurable aspect ratio to let the application specify
the desired aspect ratio based on UI design. CameraX output is produced to
match the aspect ratios requested as closely as the device supports. If there is
no exact-match resolution supported, the one that fulfills the most conditions
is selected. Thus, the application dictates how the camera appears in the
app, and CameraX determines the best camera resolution settings to satisfy that
on different devices.

For example, an app can do any of the following:

- Specify a target resolution of 4:3 or 16:9 for a use case
- Specify a custom resolution, which CameraX attempts to find the closest match to
- Specify a cropping aspect ratio for `ImageCapture`

CameraX chooses the internal Camera2 surface resolutions automatically. The
following table shows the resolutions:

| **Use case** | **Internal surface resolution** | **Output data resolution** |
|---|---|---|
| Preview | **Aspect Ratio:** The resolution that best fits the target to the setting. | Internal surface resolution. Metadata is provided to let a View crop, scale, and rotate for the target aspect ratio. |
| Preview | **Default resolution:** Highest preview resolution, or highest device-preferred resolution that matches the Preview's aspect ratio. | Internal surface resolution. Metadata is provided to let a View crop, scale, and rotate for the target aspect ratio. |
| Preview | **Max resolution:** Preview size, which refers to the best size match to the device's screen resolution, or to 1080p (1920x1080), whichever is smaller. | Internal surface resolution. Metadata is provided to let a View crop, scale, and rotate for the target aspect ratio. |
| Image analysis | **Aspect ratio:** The resolution that best fits the target to the setting. | Internal surface resolution. |
| Image analysis | **Default resolution:** The default target resolution setting is 640x480. Adjusting both target resolution and corresponding aspect ratio results in a best-supported resolution. | Internal surface resolution. |
| Image analysis | **Max resolution:** The camera device's maximum output resolution of YUV_420_888 format which is retrieved from [`StreamConfigurationMap.getOutputSizes()`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputSizes(int)). The target resolution is set as 640x480 by default, so if you want a resolution larger than 640x480, you must use [`setTargetResolution()`](https://developer.android.com/reference/kotlin/androidx/camera/core/ImageAnalysis.Builder#settargetresolution) and [`setTargetAspectRatio()`](https://developer.android.com/reference/kotlin/androidx/camera/core/ImageAnalysis.Builder#settargetaspectratio) to get the closest one from the supported resolutions. | Internal surface resolution. |
| Image capture | **Aspect ratio:** Aspect ratio that best fits the setting. | Internal surface resolution. |
| Image capture | **Default resolution:** Highest resolution available, or highest device-preferred resolution that matches the ImageCapture's aspect ratio. | Internal surface resolution. |
| Image capture | **Max resolution:** The camera device's maximum output resolution in a JPEG format. Use [`StreamConfigurationMap.getOutputSizes()`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputSizes(int)) to retrieve this. | Internal surface resolution. |

### Specify a resolution

You can set specific resolutions when building use cases using the
`setTargetResolution(Size resolution)` method, as shown in the following code
sample:  

### Kotlin

```kotlin
val imageAnalysis = ImageAnalysis.Builder()
    .setTargetResolution(Size(1280, 720))
    .build()
```

### Java

```java
ImageAnalysis imageAnalysis =
  new ImageAnalysis.Builder()
    .setTargetResolution(new Size(1280, 720))
    .build();
```

You can't set both target aspect ratio and target resolution on the same use
case. Doing so throws an `IllegalArgumentException` when building the configuration
object.

Express the resolution [`Size`](https://developer.android.com/reference/android/util/Size) in the coordinate
frame after rotating the supported sizes by the target rotation. For example, a
device with portrait natural orientation in natural target rotation requesting a
portrait image can specify 480x640, and the same device, rotated 90 degrees and
targeting landscape orientation can specify 640x480.

The target resolution attempts to establish a minimum bound for the image
resolution. The actual image resolution is the closest available resolution
in size that isn't smaller than the target resolution, as determined by the
Camera implementation.

However, if no resolution exists that is equal to or
larger than the target resolution, the nearest available resolution smaller than
the target resolution is chosen. Resolutions with the same aspect ratio of
the provided `Size` are given higher priority than resolutions of different
aspect ratios.

CameraX applies the best suitable resolution based on the requests. If the
primary need is to satisfy aspect ratio, specify only `setTargetAspectRatio`,
and CameraX determines a specific resolution suitable based on the device.
If the primary need of the app is to specify a resolution in order to make image
processing more efficient (for example a small or mid-sized image based on
device processing capability), use `setTargetResolution(Size resolution)`.
| **Note:** If you use `setTargetResolution()`, then you can receive a buffer whose aspect ratio doesn't match other use cases. If the aspect ratios must match, check the dimensions of the buffers returned by both use cases and crop or scale one of them to match the other.

If your app requires an exact resolution, see the table within
[`createCaptureSession()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#regular-capture)
to determine what maximum resolutions are supported by each hardware level. To
check for the specific resolutions supported by the current device, see
[`StreamConfigurationMap.getOutputSizes(int)`](https://developer.android.com/reference/android/hardware/camera2/params/StreamConfigurationMap#getOutputSizes(int)).

If your app is running on Android 10 or higher, you can use
[`isSessionConfigurationSupported()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#isSessionConfigurationSupported(android.hardware.camera2.params.SessionConfiguration))
to verify a specific `SessionConfiguration`.

## Control camera output

In addition to letting you configure the camera output as-needed for each
individual use case, CameraX also implements the following interfaces to support
camera operations common to all bound use cases:

- [`CameraControl`](https://developer.android.com/reference/androidx/camera/core/CameraControl) lets you configure common camera features.
- [`CameraInfo`](https://developer.android.com/reference/androidx/camera/core/CameraInfo) lets you query the states of those common camera features.

These are the supported camera features with CameraControl:

- Zoom
- Torch
- Focus and Metering (tap-to-focus)
- Exposure Compensation

### Get instances of CameraControl and CameraInfo

Retrieve instances of `CameraControl` and `CameraInfo` using the
[`Camera`](https://developer.android.com/reference/androidx/camera/core/Camera) object returned by
[`ProcessCameraProvider.bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider).
The following code shows an example:  

### Kotlin

```kotlin
val camera = processCameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)

// For performing operations that affect all outputs.
val cameraControl = camera.cameraControl
// For querying information and states.
val cameraInfo = camera.cameraInfo
```

### Java

```java
Camera camera = processCameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)

// For performing operations that affect all outputs.
CameraControl cameraControl = camera.getCameraControl()
// For querying information and states.
CameraInfo cameraInfo = camera.getCameraInfo()
```

For example, you can submit zoom and other `CameraControl` operations after
calling `bindToLifecycle()`. After you stop or destroy the activity used to bind
the camera instance, `CameraControl` can no longer execute operations and
returns a failed `ListenableFuture`.
| **Note:** All changes to the state of zoom, torch, focus and metering, and exposure compensation controls revert to their default values after the `Camera` is closed, which happens when the [`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner) is stopped or destroyed.

### Zoom

CameraControl offers two methods for changing the zoom level:

- [`setZoomRatio()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#setZoomRatio(float))
  sets the zoom by the zoom ratio.

  The ratio must be within the range of
  `CameraInfo.getZoomState().getValue().getMinZoomRatio()` and
  `CameraInfo.getZoomState().getValue().getMaxZoomRatio()`. Otherwise the
  function returns a failed `ListenableFuture`.
- [`setLinearZoom()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#setLinearZoom(float))
  sets the current zoom with a linear zoom value ranging from 0 to 1.0.

  The advantage of linear zoom is that it makes the field of view (FOV)
  scale with changes in zoom. This makes it ideal for use with a
  [`Slider`](https://developer.android.com/reference/com/google/android/material/slider/Slider) view.

[`CameraInfo.getZoomState()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getZoomState())
returns a LiveData of the current zoom state. The value changes when the camera
is initialized or if the zoom level is set using `setZoomRatio()` or
`setLinearZoom()`. Calling either method sets the values backing
[`ZoomState.getZoomRatio()`](https://developer.android.com/reference/androidx/camera/core/ZoomState#getZoomRatio())
and
[`ZoomState.getLinearZoom()`](https://developer.android.com/reference/androidx/camera/core/ZoomState#getLinearZoom()).
This is helpful if you want to display zoom ratio text alongside a slider.
Simply observe the `ZoomState` `LiveData` to update both without needing to do a
conversion.

The `ListenableFuture` returned by both APIs offers the option for applications
to be notified when a repeating request with the specified zoom value is
completed. In addition, if you set a new zoom value while the previous operation
is still executing, the previous zoom operation's `ListenableFuture` fails
immediately.

### Torch

[`CameraControl.enableTorch(boolean)`](https://developer.android.com/reference/androidx/camera/core/CameraControl#enableTorch(boolean))
enables or disables the torch (also known as the flashlight).

[`CameraInfo.getTorchState()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getTorchState())
can be used to query the current torch state. You can check the value returned
by
[`CameraInfo.hasFlashUnit()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#hasFlashUnit())
to determine whether a torch is available. If not, calling
`CameraControl.enableTorch(boolean)` causes the returned `ListenableFuture` to
complete immediately with a failed result and sets the torch state to
`TorchState.OFF`.

When the torch is enabled, it remains on during photo and video capture
regardless of the flashMode setting. The
[`flashMode`](https://developer.android.com/reference/android/hardware/Camera.Parameters#getFlashMode()) in
`ImageCapture` works only when the torch is disabled.

### Focus and Metering

[`CameraControl.startFocusAndMetering()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#setExposureCompensationIndex(int))
triggers autofocus and exposure metering by setting AF/AE/AWB metering regions
based on the given FocusMeteringAction. This is often used to implement the "tap
to focus" feature in many camera applications.

#### MeteringPoint

To begin, create a
[`MeteringPoint`](https://developer.android.com/reference/androidx/camera/core/MeteringPoint) using
[`MeteringPointFactory.createPoint(float x, float y, float
size)`](https://developer.android.com/reference/androidx/camera/core/MeteringPointFactory#createPoint(float,%20float,%20float)).
A `MeteringPoint` represents a single point on the camera
[`Surface`](https://developer.android.com/reference/android/view/Surface). It's stored in a normalized form
so that it can be easily converted to sensor coordinates for specifying
AF/AE/AWB regions.

The size of the `MeteringPoint` ranges from 0 to 1, with a default size of
0.15f. When calling `MeteringPointFactory.createPoint(float x, float y, float
size)`, CameraX creates a rectangle region centered at `(x, y)` for the provided
`size`.

The following code demonstrates how to create a `MeteringPoint`:  

### Kotlin

```kotlin
// Use PreviewView.getMeteringPointFactory if PreviewView is used for preview.
previewView.setOnTouchListener((view, motionEvent) ->  {
val meteringPoint = previewView.meteringPointFactory
    .createPoint(motionEvent.x, motionEvent.y)
...
}

// Use DisplayOrientedMeteringPointFactory if SurfaceView / TextureView is used for
// preview. Please note that if the preview is scaled or cropped in the View,
// it's the application's responsibility to transform the coordinates properly
// so that the width and height of this factory represents the full Preview FOV.
// And the (x,y) passed to create MeteringPoint might need to be adjusted with
// the offsets.
val meteringPointFactory = DisplayOrientedMeteringPointFactory(
     surfaceView.display,
     camera.cameraInfo,
     surfaceView.width,
     surfaceView.height
)

// Use SurfaceOrientedMeteringPointFactory if the point is specified in
// ImageAnalysis ImageProxy.
val meteringPointFactory = SurfaceOrientedMeteringPointFactory(
     imageWidth,
     imageHeight,
     imageAnalysis)
```

#### startFocusAndMetering and FocusMeteringAction

To invoke
[`startFocusAndMetering()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#startFocusAndMetering(androidx.camera.core.FocusMeteringAction)),
applications must build a
[`FocusMeteringAction`](https://developer.android.com/reference/androidx/camera/core/FocusMeteringAction),
which consists of one or more `MeteringPoints` with optional metering mode
combinations from
[`FLAG_AF`](https://developer.android.com/reference/androidx/camera/core/FocusMeteringAction#FLAG_AF),
[`FLAG_AE`](https://developer.android.com/reference/androidx/camera/core/FocusMeteringAction#FLAG_AE),
[`FLAG_AWB`](https://developer.android.com/reference/androidx/camera/core/FocusMeteringAction#FLAG_AWB). The
follow code demonstrates this usage:  

### Kotlin

```kotlin
val meteringPoint1 = meteringPointFactory.createPoint(x1, x1)
val meteringPoint2 = meteringPointFactory.createPoint(x2, y2)
val action = FocusMeteringAction.Builder(meteringPoint1) // default AF|AE|AWB
      // Optionally add meteringPoint2 for AF/AE.
      .addPoint(meteringPoint2, FLAG_AF | FLAG_AE)
      // The action is canceled in 3 seconds (if not set, default is 5s).
      .setAutoCancelDuration(3, TimeUnit.SECONDS)
      .build()

val result = cameraControl.startFocusAndMetering(action)
// Adds listener to the ListenableFuture if you need to know the focusMetering result.
result.addListener({
   // result.get().isFocusSuccessful returns if the auto focus is successful or not.
}, ContextCompat.getMainExecutor(this)
```

As shown in the preceding code,
[`startFocusAndMetering()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#startFocusAndMetering(androidx.camera.core.FocusMeteringAction))
takes a `FocusMeteringAction` consisting of one `MeteringPoint` for AF/AE/AWB
metering regions and another MeteringPoint for AF and AE only.

Internally, CameraX converts it into Camera2
[`MeteringRectangles`](https://developer.android.com/reference/android/hardware/camera2/params/MeteringRectangle)
and sets the corresponding
[`CONTROL_AF_REGIONS`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AF_REGIONS)
/
[`CONTROL_AE_REGIONS`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AE_REGIONS)
/
[`CONTROL_AWB_REGIONS`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AWB_REGIONS)
parameters to the capture request.

Since not every device supports AF/AE/AWB and multiple regions, CameraX executes
the `FocusMeteringAction` with best effort. CameraX uses the maximum number
of MeteringPoints supported, in the order that points were added. All
MeteringPoints added after the maximum count are ignored. For example, if a
`FocusMeteringAction` is supplied with 3 MeteringPoints on a platform supporting
just 2, only the first 2 MeteringPoints are used. The final `MeteringPoint` is
ignored by CameraX.

#### Exposure Compensation

Exposure compensation is useful when applications need to fine-tune exposure
values (EV) beyond the auto exposure (AE) output result. Exposure compensation
values are combined in the following way to determine the necessary exposure for
current image conditions:

`Exposure = ExposureCompensationIndex * ExposureCompensationStep`

CameraX provides the
[`Camera.CameraControl.setExposureCompensationIndex()`](https://developer.android.com/reference/androidx/camera/core/CameraControl#setExposureCompensationIndex(int))
function for setting the exposure compensation as an index value.

Positive index values make the image brighter, while negative values dim the
image. Applications can query the supported range by
[`CameraInfo.ExposureState.exposureCompensationRange()`](https://developer.android.com/reference/androidx/camera/core/ExposureState#getExposureCompensationRange())
described in the next section. If the value is supported, the returned
`ListenableFuture` completes when the value is successfully enabled in the
capture request; if the specified index is out of the supported range,
`setExposureCompensationIndex()` causes the returned `ListenableFuture` to
complete immediately with a failed result.

CameraX keeps only the latest outstanding `setExposureCompensationIndex()`
request, and calling the function multiple times before the previous request
gets executed results in its cancellation.

The following snippet sets an exposure compensation index and registers a
callback for when the exposure change request has been executed:  

### Kotlin

```kotlin
camera.cameraControl.setExposureCompensationIndex(exposureCompensationIndex)
   .addListener({
      // Get the current exposure compensation index, it might be
      // different from the asked value in case this request was
      // canceled by a newer setting request.
      val currentExposureIndex = camera.cameraInfo.exposureState.exposureCompensationIndex
      ...
   }, mainExecutor)
```

- [`Camera.CameraInfo.getExposureState()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getExposureState())
  retrieves the current
  [`ExposureState`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getExposureState())
  including:

  - The supportability of exposure compensation control.
  - The current exposure compensation index.
  - The exposure compensation index range.
  - The exposure compensation step used in exposure compensation value calculation.

For example, the following code initializes the settings for an exposure
[`SeekBar`](https://developer.android.com/reference/android/widget/SeekBar) with current `ExposureState`
values:  

### Kotlin

```kotlin
val exposureState = camera.cameraInfo.exposureState
binding.seekBar.apply {
   isEnabled = exposureState.isExposureCompensationSupported
   max = exposureState.exposureCompensationRange.upper
   min = exposureState.exposureCompensationRange.lower
   progress = exposureState.exposureCompensationIndex
}
```

## Additional resources

To learn more about CameraX, consult the following additional resources.

### Codelab


- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- 
- [CameraX sample apps](https://github.com/android/camera-samples/)

### Developer community

- [Android CameraX Discussion Group](http://g.co/camerax/developers)