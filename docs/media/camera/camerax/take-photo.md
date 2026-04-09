---
title: https://developer.android.com/media/camera/camerax/take-photo
url: https://developer.android.com/media/camera/camerax/take-photo
source: md.txt
---

# Capture an image

This page describes how to capture high-quality images with CameraX. You do so with the[`ImageCapture`](https://developer.android.com/reference/androidx/camera/core/ImageCapture)class and its associated methods.
| **Note:** This workflow accommodates the 3A features: auto-white-balance, auto-exposure, and auto-focus. It also supports basic manual camera controls.

## Key concepts

The following are the primary concepts discussed in this document:

- **[Storage method](https://developer.android.com/media/camera/camerax/take-photo#capture):**You can capture images either to an in-memory buffer or directly to a file.
- **[Executors](https://developer.android.com/media/camera/camerax/take-photo#executors):** `ImageCapture`uses executors for handling callbacks and I/O operations. You can customize these executors for better performance and control.
- **[Capture Modes](https://developer.android.com/media/camera/camerax/take-photo/options):**You can configure the capture mode to optimize for either latency or image quality.

### Storage method

There are two ways to capture images with`ImageCapture`. They each use an overload of`ImageCapture.takePicture()`:

- **File:** Use[`takePicture(OutputFileOptions, Executor,
  OnImageSavedCallback)`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#takePicture(androidx.camera.core.ImageCapture.OutputFileOptions,%20java.util.concurrent.Executor,%20androidx.camera.core.ImageCapture.OnImageSavedCallback))to save the captured image directly to a file on disk.

  - This is the most common way to capture photos.
- **In-Memory:** Use[`takePicture(Executor,
  OnImageCapturedCallback)`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#takePicture(java.util.concurrent.Executor,%20androidx.camera.core.ImageCapture.OnImageCapturedCallback))to receive an in-memory buffer of the captured image.

  - This is useful for real-time image processing or analysis.

### Executors

When you call`takePicture`, you pass an[`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor)and either a`OnImageCapturedCallback`or`OnImageSavedCallback`function. The`Executor`runs the callback and handles any resulting IO.
| **Note:** You can set the default executor for IO tasks with[`ImageCapture.Builder.setIoExecutor(Executor)`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder#setIoExecutor(java.util.concurrent.Executor)). If you don't set a default, CameraX uses to an internal IO executor.

## Take photo

To take a photo, you set up the camera and then call`takePicture`.

### Set up the camera

To set up the camera, create a[`CameraProvider`](https://developer.android.com/media/camera/camerax/preview#get-provider). Then, create an`ImageCapture`object. Use[`ImageCapture.Builder()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder):  

### Kotlin

    val imageCapture = ImageCapture.Builder()
        .setTargetRotation(view.display.rotation)
        .build()

    cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, imageCapture, preview)

### Java

    ImageCapture imageCapture =
        new ImageCapture.Builder()
            .setTargetRotation(view.getDisplay().getRotation())
            .build();

    cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, imageCapture, preview);

| **Note:** [`bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...))returns a[`Camera`](https://developer.android.com/reference/androidx/camera/core/Camera)object. See the[Configuration options guide](https://developer.android.com/training/camerax/configuration#camera-output)for more on controlling camera output, such as zoom and exposure.

### Take a picture

After you configure the camera, call`takePicture()`to capture an image. This example demonstrates how to use[`takePicture()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#takePicture(androidx.camera.core.ImageCapture.OutputFileOptions,%20java.util.concurrent.Executor,%20androidx.camera.core.ImageCapture.OnImageSavedCallback))to save an image to disk:  

### Kotlin

    fun onClick() {
        val outputFileOptions = ImageCapture.OutputFileOptions.Builder(File(...)).build()
        imageCapture.takePicture(outputFileOptions, cameraExecutor,
            object : ImageCapture.OnImageSavedCallback {
                override fun onError(error: ImageCaptureException)
                {
                    // insert your code here.
                }
                override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                    // insert your code here.
                }
            })
    }

### Java

    public void onClick() {
        ImageCapture.OutputFileOptions outputFileOptions =
                new ImageCapture.OutputFileOptions.Builder(new File(...)).build();
        imageCapture.takePicture(outputFileOptions, cameraExecutor,
            new ImageCapture.OnImageSavedCallback() {
                @Override
                public void onImageSaved(ImageCapture.OutputFileResults outputFileResults) {
                    // insert your code here.
                }
                @Override
                public void onError(ImageCaptureException error) {
                    // insert your code here.
                }
           }
        );
    }

Here are the key points about this snippet:

- The[`ImageCapture.OutputFileOptions`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.OutputFileOptions)lets you configure save location and metadata.
  - Here, the`OutputFileOptions.Builder()`uses a`File`object to determine the save location.
- The`takePicture()`function captures the image asynchronously using the provided options and executor.
- The[`OnImageSavedCallback`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#takePicture(androidx.camera.core.ImageCapture.OutputFileOptions,%20java.util.concurrent.Executor,%20androidx.camera.core.ImageCapture.OnImageSavedCallback))provides callbacks for success and failure.
  - The`onImageSaved()`callback handles successful image capture and provides access to the[saved image results](https://developer.android.com/reference/androidx/camera/core/ImageCapture.OutputFileResults).
  - The`onError()`callback handles image capture errors.

## Additional options

See the[Configure for optimization, flash, and file format guide](https://developer.android.com/media/camera/camerax/take-photo/options)for extra ways you can configure`ImageCapture`.

## Further resources

To learn more about CameraX, consult the following resources:

### Codelab

<br />

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX sample apps](https://github.com/android/camera-samples/)