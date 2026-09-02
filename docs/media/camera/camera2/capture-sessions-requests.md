---
title: https://developer.android.com/media/camera/camera2/capture-sessions-requests
url: https://developer.android.com/media/camera/camera2/capture-sessions-requests
source: md.txt
---

# Camera capture sessions and requests

<br />

**Note:** This page refers to the[Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary)package. Unless your app requires specific, low-level features from Camera2, we recommend using[CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

A single Android-powered device can have multiple cameras. Each camera is a[`CameraDevice`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice), and a`CameraDevice`can output more than one stream simultaneously.

One reason to do this is so that one stream, sequential camera frames coming from a`CameraDevice`, is optimized for a specific task, such as displaying a viewfinder, while others might be used to take a photo or to make a video recording.The streams act as parallel pipelines that process raw frames coming out of the camera,one frame at a time:
![](https://developer.android.com/static/images/training/camera/camera2/capture-sessions-requests-1.png)**Figure 1.**Illustration from Building a Universal Camera App (Google I/O '18)

Parallel processing suggests that there can be performance limits depending on the available processing power from the CPU, GPU, or other processor. If a pipeline can't keep up with the incoming frames, it starts dropping them.

Each pipeline has its own output format. The raw data coming in is automatically transformed into the appropriate[output format](https://developer.android.com/reference/android/graphics/PixelFormat)by implicit logic associated with each pipeline. The`CameraDevice`used throughout this page's code samples is non-specific, so you first[enumerate](https://developer.android.com/training/camera2/camera-enumeration)all available cameras before proceeding.

You can use the`CameraDevice`to create a[`CameraCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession), which is specific to that`CameraDevice`. A`CameraDevice`must receive a frame configuration for each raw frame using the`CameraCaptureSession`. The configuration specifies camera attributes such as autofocus, aperture, effects, and exposure. Due to hardware constraints, only a single configuration is active in the camera sensor at any given time, which is called the*active*configuration.

However, Stream Use Cases enhance and extend previous ways to use`CameraDevice`to stream capture sessions, which lets you optimize the camera stream for your particular use case. For example, it can improve battery life when optimizing video calls.

A`CameraCaptureSession`describes all the possible pipelines bound to the`CameraDevice`. When a session is created, you cannot add or remove pipelines. The`CameraCaptureSession`maintains a queue of[`CaptureRequest`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest)s, which become the active configuration.

A`CaptureRequest`adds a configuration to the queue and selects one, more than one, or all of the available pipelines to receive a frame from the`CameraDevice`. You can send many capture requests over the life of a capture session. Each request can change the active configuration and set of output pipelines that receive the raw image.

## Use Stream Use Cases for better performance

Stream Use Cases are a way to improve the performance of Camera2 capture sessions. They give the hardware device more information to tune parameters, which provides a better camera experience for your specific task.

This allows the camera device to optimize camera hardware and software pipelines based on user scenarios for each stream. For more information about Stream Use Cases, see[`setStreamUseCase`](https://developer.android.com/reference/android/hardware/camera2/params/OutputConfiguration#setStreamUseCase(long)).

Stream Use Cases let you specify how a particular camera stream is used in greater detail, in addition to setting a template in`CameraDevice.createCaptureRequest()`. This lets the camera hardware optimize parameters, such as tuning, sensor mode, or camera sensor settings, based on quality or latency tradeoffs suitable for specific use cases.

Stream Use Cases include:

- `DEFAULT`: Covers all existing application behavior. It's equivalent to not setting any Stream Use Case.

- `PREVIEW`: Recommended for Viewfinder or in-app image analysis.

- `STILL_CAPTURE`: Optimized for high-quality high-resolution capture, and not expected to maintain preview-like frame rates.

- `VIDEO_RECORD`: Optimized for high-quality video capture, including high-quality image stabilization, if supported by the device and enabled by the application. This option might produce output frames with a substantial lag from real time, to allow for highest-quality stabilization or other processing.

- `VIDEO_CALL`: Recommended for long-running camera uses where power drain is a concern.

- `PREVIEW_VIDEO_STILL`: Recommended for social media apps or single stream use cases. It's a multipurpose stream.

- `VENDOR_START`: Used for OEM-defined use cases.

## Create a CameraCaptureSession

To create a camera session, provide it with one or more output buffers your app can write output frames to. Each buffer represents a pipeline. You must do this before you start using the camera so that the framework can configure the device's internal pipelines and allocate memory buffers for sending frames to the needed output targets.

The following code snippet shows how you can prepare a camera session with two output buffers, one belonging to a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)and another to an[`ImageReader`](https://developer.android.com/reference/android/media/ImageReader). Adding[`PREVIEW`](https://developer.android.com/training/camerax/preview#scale-type)Stream Use Case to`previewSurface`and[`STILL_CAPTURE`](https://developer.android.com/training/camerax/take-photo#set-up-image-capture)Stream Use Case to`imReaderSurface`lets the device hardware optimize these streams even further.  

### Kotlin

```kotlin
// Retrieve the target surfaces, which might be coming from a number of places:
// 1. SurfaceView, if you want to display the image directly to the user
// 2. ImageReader, if you want to read each frame or perform frame-by-frame
// analysis
// 3. OpenGL Texture or TextureView, although discouraged for maintainability
      reasons
// 4. RenderScript.Allocation, if you want to do parallel processing
val surfaceView = findViewById<SurfaceView>(...)
val imageReader = ImageReader.newInstance(...)

// Remember to call this only *after* SurfaceHolder.Callback.surfaceCreated()
val previewSurface = surfaceView.holder.surface
val imReaderSurface = imageReader.surface
val targets = listOf(previewSurface, imReaderSurface)

// Create a capture session using the predefined targets; this also involves
// defining the session state callback to be notified of when the session is
// ready
// Setup Stream Use Case while setting up your Output Configuration.
@RequiresApi(Build.VERSION_CODES.TIRAMISU)
fun configureSession(device: CameraDevice, targets: List<Surface>){
    val configs = mutableListOf<OutputConfiguration>()
    val streamUseCase = CameraMetadata
        .SCALER_AVAILABLE_STREAM_USE_CASES_PREVIEW_VIDEO_STILL

    targets.forEach {
        val config = OutputConfiguration(it)
        config.streamUseCase = streamUseCase.toLong()
        configs.add(config)
    }
    ...
    device.createCaptureSession(session)
}
```

### Java

```java
// Retrieve the target surfaces, which might be coming from a number of places:
// 1. SurfaceView, if you want to display the image directly to the user
// 2. ImageReader, if you want to read each frame or perform frame-by-frame
      analysis
// 3. RenderScript.Allocation, if you want to do parallel processing
// 4. OpenGL Texture or TextureView, although discouraged for maintainability
      reasons
Surface surfaceView = findViewById<SurfaceView>(...);
ImageReader imageReader = ImageReader.newInstance(...);

// Remember to call this only *after* SurfaceHolder.Callback.surfaceCreated()
Surface previewSurface = surfaceView.getHolder().getSurface();
Surface imageSurface = imageReader.getSurface();
List<Surface> targets = Arrays.asList(previewSurface, imageSurface);

// Create a capture session using the predefined targets; this also involves defining the
// session state callback to be notified of when the session is ready
private void configureSession(CameraDevice device, List<Surface> targets){
    ArrayList<OutputConfiguration> configs= new ArrayList()
    String streamUseCase=  CameraMetadata
        .SCALER_AVAILABLE_STREAM_USE_CASES_PREVIEW_VIDEO_STILL

    for(Surface s : targets){
        OutputConfiguration config = new OutputConfiguration(s)
        config.setStreamUseCase(String.toLong(streamUseCase))
        configs.add(config)
}

device.createCaptureSession(session)
}
```

At this point, you have not defined the camera's active configuration. When the session is configured, you can create and dispatch capture requests to do that.

The transformation applied to inputs as they are written to their buffer is determined by the type of each target, which must be a[`Surface`](https://developer.android.com/reference/android/view/Surface). The Android framework knows how to convert a raw image in the active configuration into a format appropriate for each target. The conversion is controlled by the pixel format and size of the particular`Surface`.

The framework tries to do its best, but some`Surface`configuration combinations might not work, causing issues such as the session not being created, throwing a runtime error when you dispatch a request, or performance degradation. The framework provides guarantees for specific combinations of device, surface, and request parameters. The documentation for[`createCaptureSession()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(android.hardware.camera2.params.SessionConfiguration))provides more information.

## Single CaptureRequests

The configuration used for each frame is encoded in a`CaptureRequest`, which is sent to the camera. To create a capture request, you can use one of the predefined[templates](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#constants_1), or you can use`TEMPLATE_MANUAL`for full control. When you choose a template, you need to provide one or more output buffers to be used with the request. You can only use buffers that were already defined on the capture session you intend to use.

Capture requests use a[builder pattern](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest.Builder)and give developers the opportunity to set[many different options](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#fields_1)including[auto-exposure](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AE_MODE),[auto-focus](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AF_MODE), and[lens aperture](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#LENS_APERTURE). Before setting a field, make sure that the specific option is available for the device by calling[`CameraCharacteristics.getAvailableCaptureRequestKeys()`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#getAvailableCaptureRequestKeys())and that the desired value is supported by checking the appropriate camera characteristic, such as the[available auto-exposure modes](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#CONTROL_AE_AVAILABLE_MODES).

To create a capture request for a`SurfaceView`using the template designed for preview without any modifications, use[`CameraDevice.TEMPLATE_PREVIEW`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#TEMPLATE_PREVIEW):  

### Kotlin

```kotlin
val session: CameraCaptureSession = ...  // from CameraCaptureSession.StateCallback
val captureRequest = session.device.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW)
captureRequest.addTarget(previewSurface)
```

### Java

```java
CameraCaptureSession session = ...;  // from CameraCaptureSession.StateCallback
CaptureRequest.Builder captureRequest =
    session.getDevice().createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);
captureRequest.addTarget(previewSurface);
```

With a capture request defined, you can now[dispatch](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#capture%28android.hardware.camera2.CaptureRequest,%20android.hardware.camera2.CameraCaptureSession.CaptureCallback,%20android.os.Handler%29)it to the camera session:  

### Kotlin

```kotlin
val session: CameraCaptureSession = ...  // from CameraCaptureSession.StateCallback
val captureRequest: CaptureRequest = ...  // from CameraDevice.createCaptureRequest()

// The first null argument corresponds to the capture callback, which you
// provide if you want to retrieve frame metadata or keep track of failed capture
// requests that can indicate dropped frames; the second null argument
// corresponds to the Handler used by the asynchronous callback, which falls
// back to the current thread's looper if null
session.capture(captureRequest.build(), null, null)
```

### Java

```java
CameraCaptureSession session = ...;  // from CameraCaptureSession.StateCallback
CaptureRequest captureRequest = ...;  // from CameraDevice.createCaptureRequest()

// The first null argument corresponds to the capture callback, which you
// provide if you want to retrieve frame metadata or keep track of failed
// capture
// requests that can indicate dropped frames; the second null argument
// corresponds to the Handler used by the asynchronous callback, which falls
// back to the current thread's looper if null
session.capture(captureRequest.build(), null, null);
```

When an output frame is put into the specific buffer, a[capture callback](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession.CaptureCallback)is triggered. In many cases additional callbacks, such as[`ImageReader.OnImageAvailableListener`](https://developer.android.com/reference/android/media/ImageReader.OnImageAvailableListener), is triggered when the frame it contains is processed. It is at this point that you can retrieve image data out of the specified buffer.

## Repeat CaptureRequests

Single camera requests are straightforward to do, but for displaying a live preview, or video, they aren't very useful. In that case, you need to receive a continuous stream of frames, not just a single one. The following code snippet shows how to add a[repeating request](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#setRepeatingRequest%28android.hardware.camera2.CaptureRequest,%20android.hardware.camera2.CameraCaptureSession.CaptureCallback,%20android.os.Handler%29)to the session:  

### Kotlin

```kotlin
val session: CameraCaptureSession = ...  // from CameraCaptureSession.StateCallback
val captureRequest: CaptureRequest = ...  // from CameraDevice.createCaptureRequest()

// This keeps sending the capture request as frequently as possible until
// the
// session is torn down or session.stopRepeating() is called
// session.setRepeatingRequest(captureRequest.build(), null, null)
```

### Java

```java
CameraCaptureSession session = ...;  // from CameraCaptureSession.StateCallback
CaptureRequest captureRequest = ...;  // from CameraDevice.createCaptureRequest()

// This keeps sending the capture request as frequently as possible until the
// session is torn down or session.stopRepeating() is called
// session.setRepeatingRequest(captureRequest.build(), null, null);
```

A repeating capture request makes the camera device continually capture images using the settings in the provided`CaptureRequest`. The Camera2 API also lets users capture video from the camera by sending repeating`CaptureRequests`as seen in this[Camera2 sample](https://github.com/android/camera-samples/tree/master/Camera2Video)repository on GitHub. It can also render slow motion video by capturing a high-speed (slow motion) video using repeating burst`CaptureRequests`as showcased in the[Camera2 slow motion video sample app](https://github.com/android/camera-samples/tree/master/Camera2SlowMotion)on GitHub.

## Interleave CaptureRequests

To send a second capture request while the repeating capture request is active, such as to display a viewfinder and let users capture a photo, you don't need to stop the ongoing repeating request. Instead, you issue a non-repeating capture request while the repeating request continues to run.

Any output buffer used needs to be configured as part of the camera session when the session is first created. Repeating requests have lower priority than single-frame or burst requests, which enable the following sample to work:  

### Kotlin

```kotlin
val session: CameraCaptureSession = ...  // from CameraCaptureSession.StateCallback

// Create the repeating request and dispatch it
val repeatingRequest = session.device.createCaptureRequest(
CameraDevice.TEMPLATE_PREVIEW)
repeatingRequest.addTarget(previewSurface)
session.setRepeatingRequest(repeatingRequest.build(), null, null)

// Some time later...

// Create the single request and dispatch it
// NOTE: This can disrupt the ongoing repeating request momentarily
val singleRequest = session.device.createCaptureRequest(
CameraDevice.TEMPLATE_STILL_CAPTURE)
singleRequest.addTarget(imReaderSurface)
session.capture(singleRequest.build(), null, null)
```

### Java

```java
CameraCaptureSession session = ...;  // from CameraCaptureSession.StateCallback

// Create the repeating request and dispatch it
CaptureRequest.Builder repeatingRequest =
session.getDevice().createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);
repeatingRequest.addTarget(previewSurface);
session.setRepeatingRequest(repeatingRequest.build(), null, null);

// Some time later...

// Create the single request and dispatch it
// NOTE: This can disrupt the ongoing repeating request momentarily
CaptureRequest.Builder singleRequest =
session.getDevice().createCaptureRequest(CameraDevice.TEMPLATE_STILL_CAPTURE);
singleRequest.addTarget(imReaderSurface);
session.capture(singleRequest.build(), null, null);
```

There is a drawback with this approach, though: you don't know exactly when the single request occurs. In the following figure, if**A** is the repeating capture request and**B**is the single-frame capture request, this is how the session processes the request queue:
![](https://developer.android.com/static/images/training/camera/camera2/capture-sessions-requests-2.png)**Figure 2.**Illustration of a request queue for the ongoing camera session

There are no guarantees for the latency between the last repeating request from**A** before request**B** activates and the next time that**A**is being used again, so you might experience some skipped frames. There are some things you can do to mitigate this problem:

- Add the output targets from request**A** to request**B** . That way, when**B** 's frame is ready, it is copied into**A** 's output targets. For example, this is essential when doing video snapshots to maintain a steady frame rate. In the preceding code, you add`singleRequest.addTarget(previewSurface)`before building the request.

- Use a combination of templates designed to work for this particular scenario, such as zero-shutter-lag.