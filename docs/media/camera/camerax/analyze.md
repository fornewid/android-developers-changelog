---
title: https://developer.android.com/media/camera/camerax/analyze
url: https://developer.android.com/media/camera/camerax/analyze
source: md.txt
---

# Image analysis

The[image analysis](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer#analyze(androidx.camera.core.ImageProxy))use case provides your app with a CPU-accessible image on which you can perform image processing, computer vision, or machine learning inference. The application implements an[`analyze()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer#analyze(androidx.camera.core.ImageProxy))method that is run on each frame.

To learn how to integrate Google's ML Kit with your CameraX app, see[ML Kit Analyzer](https://developer.android.com/training/camerax/mlkitanalyzer).

## Operating Modes

When the application's analysis pipeline can't keep up with CameraX's frame rate requirements, CameraX can be configured to drop frames in one of the following ways:

- ***non-blocking*** (default): In this mode, the executor always caches the latest image into an image buffer (similar to a queue with a depth of one) while the application analyzes the previous image. If CameraX receives a new image before the application finishes processing, the new image is saved to the same buffer, overwriting the previous image. Note that`ImageAnalysis.Builder.setImageQueueDepth()`has no effect in this scenario, and the buffer contents are always overwritten. You can enable this non-blocking mode by calling`setBackpressureStrategy()`with[`STRATEGY_KEEP_ONLY_LATEST`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#STRATEGY_KEEP_ONLY_LATEST). For more information on executor implications, see the reference documentation for[`STRATEGY_KEEP_ONLY_LATEST`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#STRATEGY_KEEP_ONLY_LATEST).

- ***blocking*** : In this mode, the internal executor can add multiple images to the internal image queue and begins dropping frames only when the queue is full. The blocking occurs across the entire camera device scope: if the camera device has multiple bound use cases, those uses cases will all be blocked while CameraX is processing these images. For example, when both preview and image analysis are bound to a Camera device, then preview would also be blocked while CameraX is processing the images. You can enable blocking mode is enabled by passing[`STRATEGY_BLOCK_PRODUCER`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#strategy_block_producer)to[`setBackpressureStrategy()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setBackpressureStrategy(int)). You can also configure the image queue depth by using[ImageAnalysis.Builder.setImageQueueDepth()](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setImageQueueDepth(int)).

With a low latency and high performance analyzer where the total time to analyze an image is less than the duration of a CameraX frame (16ms for 60fps, for example), either operating mode provides a smooth overall experience. Blocking mode can still be helpful in some scenarios, such as when dealing with very brief system jitters.

With a high latency and high performance analyzer, blocking mode with a longer queue is necessary to compensate for latency. Note, however, that the application can still process all frames.

With a high latency and time-consuming analyzer (analyzer is unable to process all frames), a non-blocking mode might be a more appropriate choice, as frames have to be dropped for analysis path, but other concurrent bound use cases can still see all frames.

## Implementation

To use image analysis in your application, follow those steps:

- Build an[`ImageAnalysis`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis)use case.
- Create an[`ImageAnalysis.Analyzer`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer).
- [Set your analyzer](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#setAnalyzer(java.util.concurrent.Executor,%20androidx.camera.core.ImageAnalysis.Analyzer))to your`ImageAnalysis`.
- [Bind](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...))your lifecycle owner, camera selector, and`ImageAnalysis`use case to the lifecycle.

Immediately after binding, CameraX sends images to your registered analyzer. After completing analysis, call[`ImageAnalysis.clearAnalyzer()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#clearAnalyzer())or unbind the`ImageAnalysis`use case to stop analysis.

### Build ImageAnalysis use case

[`ImageAnalysis`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis)connects your analyzer (an image consumer) to CameraX, which is an image producer. Applications can use[`ImageAnalysis.Builder`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder)to build an`ImageAnalysis`object. With the`ImageAnalysis.Builder`, application can configure the following:

- Image output parameters:
  - Format: CameraX supports[`YUV_420_888`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#OUTPUT_IMAGE_FORMAT_YUV_420_888)and[`RGBA_8888`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#OUTPUT_IMAGE_FORMAT_RGBA_8888)through[`setOutputImageFormat(int)`](https://developer.android.com/reference/kotlin/androidx/camera/core/ImageAnalysis.Builder#setOutputImageFormat(kotlin.Int)). The default format is`YUV_420_888`.
  - [Resolution](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setTargetResolution(android.util.Size))and[AspectRatio](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setTargetAspectRatio(int)): You can set either of these parameters, but note that you can't set both values at the same time.
  - [Rotation](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setTargetRotation(int)).
  - [Target Name](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setTargetName(java.lang.String)): Use this parameter for debugging purposes.
- Image flow controls:
  - [Background executor](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setBackgroundExecutor(java.util.concurrent.Executor))
  - [Image queue (between analyzer and CamaraX) depth](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setImageQueueDepth(int))
  - [Back pressure strategy](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setBackpressureStrategy(int))

Applications can set either the resolution or the aspect ratio, but not both. The exact output resolution depends on the application's requested size (or aspect ratio) and hardware capabilities and might differ from the requested size or ratio. For information about the resolution matching algorithm, see the documentation for[`setTargetResolution()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Builder#setTargetResolution(android.util.Size))

An application can configure the output image pixels to be in YUV (default) or RGBA color spaces. When setting an RGBA output format, CameraX internally converts images from YUV to RGBA color space and packs image bits into the[`ByteBuffer`](https://developer.android.com/reference/androidx/camera/core/ImageProxy.PlaneProxy#getBuffer())of the ImageProxy's first plane (the other two planes are not used) with the following sequence:  

    ImageProxy.getPlanes()[0].buffer[0]: alpha
    ImageProxy.getPlanes()[0].buffer[1]: red
    ImageProxy.getPlanes()[0].buffer[2]: green
    ImageProxy.getPlanes()[0].buffer[3]: blue
    ...

When performing complicated image analysis where the device can't keep up with the frame rate, you can configure CameraX to drop frames with the strategies described in[Operating Modes](https://developer.android.com/media/camera/camerax/analyze#operating_modes)section of this topic.

### Create your analyzer

Applications can create analyzers by implementing the[`ImageAnalysis.Analyzer`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer)interface and overriding[`analyze(ImageProxy image)`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer#analyze(androidx.camera.core.ImageProxy)). In each analyzer, applications receive an[`ImageProxy`](https://developer.android.com/reference/androidx/camera/core/ImageProxy), which is a wrapper for[Media.Image](https://developer.android.com/reference/android/media/Image). The image format can be queried with[`ImageProxy.getFormat()`](https://developer.android.com/reference/androidx/camera/core/ImageProxy#getFormat()). The format is one of the following values that the application provides with the`ImageAnalysis.Builder`:

- `ImageFormat.RGBA_8888`if the app requested`OUTPUT_IMAGE_FORMAT_RGBA_8888`.
- `ImageFormat.YUV_420_888`if the app requested`OUTPUT_IMAGE_FORMAT_YUV_420_888`.

See the[Build ImageAnalysis use case](https://developer.android.com/training/camerax/analyze#build_imageanalysis_use_case)for color space configurations and where the pixel bytes can be retrieved.

Inside an analyzer, the application should do the following:

1. Analyze a given frame as quickly as possible, preferably within the given frame rate time limit (for example, less than 32ms for 30 fps case). If the application can't analyze a frame quickly enough, consider one of the[supported frame dropping mechanisms](https://developer.android.com/training/camerax/analyze#operating_modes).
2. Release the`ImageProxy`to CameraX by calling[`ImageProxy.close()`](https://developer.android.com/reference/androidx/camera/core/ImageProxy#close()). Note that you shouldn't call the wrapped Media.Image's close function (`Media.Image.close()`).

Applications can use the wrapped`Media.Image`inside ImageProxy directly. Just do not call`Media.Image.close()`on the wrapped image as this would break the image sharing mechanism inside CameraX; instead, use[`ImageProxy.close()`](https://developer.android.com/reference/androidx/camera/core/ImageProxy#close())to release the underlying`Media.Image`to CameraX.

### Configure your analyzer for ImageAnalysis

Once you've created an analyzer, use[`ImageAnalysis.setAnalyzer()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#setAnalyzer(java.util.concurrent.Executor,%20androidx.camera.core.ImageAnalysis.Analyzer))to register it to begin analysis. Once you're finished with analysis, use[`ImageAnalysis.clearAnalyzer()`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#clearAnalyzer())to remove the registered analyzer.

Only one active analyzer can be configured for image analysis. Calling`ImageAnalysis.setAnalyzer()`replaces the registered analyzer if it already exists. Applications can set a new analyzer at any time, before or after binding the use case.

### Bind the ImageAnalysis to a Lifecycle

| **Note:** This step is common to all CameraX use cases. See the[CameraX API model](https://developer.android.com/training/camerax/architecture#api-model)for more information about binding and lifecycle customization.

It is highly recommended to bind the your`ImageAnalysis`to an existing AndroidX lifecycle with the[`ProcessCameraProvider.bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...))function. Note that the`bindToLifecycle()`function returns the selected[`Camera`](https://developer.android.com/reference/androidx/camera/core/Camera)device, which can be used to fine tune advanced settings such as exposure and others. See[this guide](https://developer.android.com/training/camerax/configuration#camera-output)for more information about controlling camera output.

The following example combines everything from the previous steps, binding CameraX`ImageAnalysis`and`Preview`use cases to a`lifeCycle`owner:  

### Kotlin

```kotlin
val imageAnalysis = ImageAnalysis.Builder()
    // enable the following line if RGBA output is needed.
    // .setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
    .setTargetResolution(Size(1280, 720))
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .build()
imageAnalysis.setAnalyzer(executor, ImageAnalysis.Analyzer { imageProxy ->
    val rotationDegrees = imageProxy.imageInfo.rotationDegrees
    // insert your code here.
    ...
    // after done, release the ImageProxy object
    imageProxy.close()
})

cameraProvider.bindToLifecycle(this as LifecycleOwner, cameraSelector, imageAnalysis, preview)
```

### Java

```java
ImageAnalysis imageAnalysis =
    new ImageAnalysis.Builder()
        // enable the following line if RGBA output is needed.
        //.setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
        .setTargetResolution(new Size(1280, 720))
        .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
        .build();

imageAnalysis.setAnalyzer(executor, new ImageAnalysis.Analyzer() {
    @Override
    public void analyze(@NonNull ImageProxy imageProxy) {
        int rotationDegrees = imageProxy.getImageInfo().getRotationDegrees();
            // insert your code here.
            ...
            // after done, release the ImageProxy object
            imageProxy.close();
        }
    });

cameraProvider.bindToLifecycle((LifecycleOwner) this, cameraSelector, imageAnalysis, preview);
```

## Additional resources

To learn more about CameraX, see the following additional resources.

### Codelab

<br />

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX sample apps](https://github.com/android/camera-samples/)