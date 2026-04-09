---
title: https://developer.android.com/media/camera/camerax/extensions-api
url: https://developer.android.com/media/camera/camerax/extensions-api
source: md.txt
---

# CameraX Extensions API

CameraX provides an Extensions API for accessing[extensions](https://developer.android.com/training/camera/camera-extensions)that device manufacturers have implemented on various Android devices. For a list of supported extension modes, see[Camera extensions](https://developer.android.com/training/camera/camera-extensions).

For a list of devices that support extensions, see[Supported devices](https://developer.android.com/training/camera/supported-devices).

## Extensions architecture

The following image shows the camera extensions architecture.
![](https://developer.android.com/static/images/training/camera/camerax/camerax-camera-extensions-architecture.png)**Figure 1.**Camera Extensions architecture

A CameraX application can use extensions through the CameraX Extensions API. The CameraX Extensions API manages querying for available extensions, configuring an extension camera session, and communicating with the Camera Extensions OEM library. This allows your application to use capabilities like Night, HDR, Auto, Bokeh, or Face Retouch.

## Enable an extension for image capture and preview

Before using the extensions API, retrieve an`ExtensionsManager`instance using the[ExtensionsManager#getInstanceAsync(Context, CameraProvider)](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager#getInstanceAsync(android.content.Context,%20androidx.camera.core.CameraProvider))method. This will allow you to query the extension availability information. Then retrieve an extension enabled`CameraSelector`. The extension mode will be applied on the image capture and preview use cases when calling the[bindToLifecycle()](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...))method with the`CameraSelector`extension enabled.
| **Note:** Enabling extensions on`ImageCapture`and`Preview`may limit the number of cameras that you can select when you use`ImageCapture`and`Preview`as parameters to[`bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...)).`ExtensionsManager#getExtensionEnabledCameraSelector()`will throw an exception if no cameras are found that support the extension.

To implement the extension for the image capture and preview use cases, refer to the following code sample:  

### Kotlin

```kotlin
import androidx.camera.extensions.ExtensionMode
import androidx.camera.extensions.ExtensionsManager

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    val lifecycleOwner = this

    val cameraProviderFuture = ProcessCameraProvider.getInstance(applicationContext)
    cameraProviderFuture.addListener({
        // Obtain an instance of a process camera provider
        // The camera provider provides access to the set of cameras associated with the device.
        // The camera obtained from the provider will be bound to the activity lifecycle.
        val cameraProvider = cameraProviderFuture.get()

        val extensionsManagerFuture =
            ExtensionsManager.getInstanceAsync(applicationContext, cameraProvider)
        extensionsManagerFuture.addListener({
            // Obtain an instance of the extensions manager
            // The extensions manager enables a camera to use extension capabilities available on
            // the device.
            val extensionsManager = extensionsManagerFuture.get()

            // Select the camera
            val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

            // Query if extension is available.
            // Not all devices will support extensions or might only support a subset of
            // extensions.
            if (extensionsManager.isExtensionAvailable(cameraSelector, ExtensionMode.NIGHT)) {
                // Unbind all use cases before enabling different extension modes.
                try {
                    cameraProvider.unbindAll()

                    // Retrieve a night extension enabled camera selector
                    val nightCameraSelector =
                        extensionsManager.getExtensionEnabledCameraSelector(
                            cameraSelector,
                            ExtensionMode.NIGHT
                        )

                    // Bind image capture and preview use cases with the extension enabled camera
                    // selector.
                    val imageCapture = ImageCapture.Builder().build()
                    val preview = Preview.Builder().build()
                    // Connect the preview to receive the surface the camera outputs the frames
                    // to. This will allow displaying the camera frames in either a TextureView
                    // or SurfaceView. The SurfaceProvider can be obtained from the PreviewView.
                    preview.setSurfaceProvider(surfaceProvider)

                    // Returns an instance of the camera bound to the lifecycle
                    // Use this camera object to control various operations with the camera
                    // Example: flash, zoom, focus metering etc.
                    val camera = cameraProvider.bindToLifecycle(
                        lifecycleOwner,
                        nightCameraSelector,
                        imageCapture,
                        preview
                    )
                } catch (e: Exception) {
                    Log.e(TAG, "Use case binding failed", e)
                }
            }
        }, ContextCompat.getMainExecutor(this))
    }, ContextCompat.getMainExecutor(this))
}
```

### Java

```java
import androidx.camera.extensions.ExtensionMode;
import androidx.camera.extensions.ExtensionsManager;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    final LifecycleOwner lifecycleOwner = this;

    final ListenableFuture cameraProviderFuture =
            ProcessCameraProvider.getInstance(getApplicationContext());

    cameraProviderFuture.addListener(() -> {
      try {
          // Obtain an instance of a process camera provider
          // The camera provider provides access to the set of cameras associated with the
          // device. The camera obtained from the provider will be bound to the activity
          // lifecycle.
          final ProcessCameraProvider cameraProvider = cameraProviderFuture.get();

          final ListenableFuture extensionsManagerFuture =
                  ExtensionsManager.getInstanceAsync(getApplicationContext(), cameraProvider);
          extensionsManagerFuture.addListener(() -> {
              // Obtain an instance of the extensions manager
              // The extensions manager enables a camera to use extension capabilities available
              // on the device.
              try {
                  final ExtensionsManager extensionsManager = extensionsManagerFuture.get();

                  // Select the camera
                  final CameraSelector cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA;

                  // Query if extension is available.
                  // Not all devices will support extensions or might only support a subset of
                  // extensions.
                  if (extensionsManager.isExtensionAvailable(
                          cameraSelector,
                          ExtensionMode.NIGHT
                  )) {
                      // Unbind all use cases before enabling different extension modes.
                      cameraProvider.unbindAll();

                      // Retrieve extension enabled camera selector
                      final CameraSelector nightCameraSelector = extensionsManager
                              .getExtensionEnabledCameraSelector(cameraSelector, ExtensionMode.NIGHT);

                      // Bind image capture and preview use cases with the extension enabled camera
                      // selector.
                      final ImageCapture imageCapture = new ImageCapture.Builder().build();
                      final Preview preview = new Preview.Builder().build();
                      // Connect the preview to receive the surface the camera outputs the frames
                      // to. This will allow displaying the camera frames in either a TextureView
                      // or SurfaceView. The SurfaceProvider can be obtained from the PreviewView.
                      preview.setSurfaceProvider(surfaceProvider);

                      cameraProvider.bindToLifecycle(
                              lifecycleOwner,
                              nightCameraSelector,
                              imageCapture,
                              preview
                      );
                  }
              } catch (ExecutionException | InterruptedException e) {
                  throw new RuntimeException(e);
              }
          }, ContextCompat.getMainExecutor(this));

      } catch (ExecutionException | InterruptedException e) {
          throw new RuntimeException(e);
      }

  }, ContextCompat.getMainExecutor(this));
}
```

## Disable the extension

To disable vendor extensions, unbind all use cases and rebind the image capture and preview use cases with a normal camera selector. For example, rebind to the back camera using`CameraSelector.DEFAULT_BACK_CAMERA`.

## Dependencies

The CameraX Extensions API is implemented in the`camera-extensions`library. The extensions depend on the CameraX core modules (`core`,`camera2`,`lifecycle`).
**Note:** To ensure compatibility, you must use the version of the extensions library that is found in the same[release package](https://developer.android.com/jetpack/androidx/releases/camera)as the corresponding core camera modules. For example, to use`camera-extensions:1.0.0-alpha28`, you must also include version`1.1.0-alpha28`for the`camera-lifecycle`,`camera-core`, and`camera-camera2`, as these modules were all released together.  

### Groovy

```groovy
dependencies {
  def camerax_version = "1.2.0-rc01"
  implementation "androidx.camera:camera-core:${camerax_version}"
  implementation "androidx.camera:camera-camera2:${camerax_version}"
  implementation "androidx.camera:camera-lifecycle:${camerax_version}"
  //the CameraX Extensions library
  implementation "androidx.camera:camera-extensions:${camerax_version}"
    ...
}
```

### Kotlin

```kotlin
dependencies {
  val camerax_version = "1.2.0-rc01"
  implementation("androidx.camera:camera-core:${camerax_version}")
  implementation("androidx.camera:camera-camera2:${camerax_version}")
  implementation("androidx.camera:camera-lifecycle:${camerax_version}")
  // the CameraX Extensions library
  implementation("androidx.camera:camera-extensions:${camerax_version}")
    ...
}
```

## Legacy API removal

With the new Extensions API released in`1.0.0-alpha26`, the legacy Extensions API released in August 2019 is now deprecated. Starting with version`1.0.0-alpha28`, the legacy Extensions API has been removed from the library. Applications using the new Extensions API must now acquire an extension-enabled[`CameraSelector`](https://developer.android.com/reference/androidx/camera/core/CameraSelector)and use it to bind the use cases.

Applications using the legacy Extensions API should migrate to the new Extensions API to ensure future compatibility with upcoming CameraX releases.

## Additional resources

To learn more about CameraX, consult the following additional resources.

### Codelab

<br />

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX Extensions Sample App](https://github.com/android/camera-samples/tree/main/CameraXExtensions)

### Other references

- [CameraX Vendor Extensions](https://source.android.com/devices/camera/camerax-vendor-extensions)
- [CameraX Vendor Extensions Validation Tool](https://source.android.com/devices/camera/camerax-vendor-extensions-validation-tool)