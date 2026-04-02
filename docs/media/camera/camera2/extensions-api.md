---
title: https://developer.android.com/media/camera/camera2/extensions-api
url: https://developer.android.com/media/camera/camera2/extensions-api
source: md.txt
---

# Camera2 Extensions API

<br />

**Note:** This page refers to the[Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary)package. Unless your app requires specific, low-level features from Camera2, we recommend using[CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

Camera2 provides an Extensions API for accessing[extensions](https://developer.android.com/training/camera/camera-extensions)that device manufacturers have implemented on various Android devices. For a list of supported extension modes, see[Camera extensions](https://developer.android.com/training/camera/camera-extensions).

For a list of devices that support extensions, see[Supported devices](https://developer.android.com/training/camera/supported-devices).

## Extensions architecture

The following image shows the camera extensions architecture.
![](https://developer.android.com/static/images/training/camera/camera2/camera2-camera-extensions-architecture.png)**Figure 1.**Camera Extensions architecture

A Camera2 application can use extensions through the Camera2 API. The Camera2 API provides ways to query for available extensions, configure an extension camera session, and communicate with the Camera Extensions OEM library. This allows your application to use extensions like Night, HDR, Auto, Bokeh, or Face Retouch.

## Test a camera device for Camera2 Extensions API compatibility

The following code snippet checks if the device supports the Camera2 Extensions API. Extensions are not supported by all devices or the device might support a subset of extensions. The snippet returns a list of compatible camera IDs which support camera extensions.  

### Kotlin

```kotlin
private fun getExtensionCameraIds(cameraManager: CameraManager): List<String> =
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        cameraManager.cameraIdList.filter { cameraId ->
            val characteristics = cameraManager.getCameraCharacteristics(cameraId)
            val extensionCharacteristics =
                cameraManager.getCameraExtensionCharacteristics(cameraId)
            val capabilities =
                characteristics.get(CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES)
            extensionCharacteristics.supportedExtensions.isNotEmpty() &&
                    capabilities?.contains(
                        CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES_BACKWARD_COMPATIBLE
                    ) ?: false
        }
    } else emptyList()
```

### Java

```java
private List<String> getExtensionCameraIds(CameraManager cameraManager)
        throws CameraAccessException {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        return Arrays.stream(cameraManager.getCameraIdList()).filter(cameraId -> {
            try {
                CameraCharacteristics characteristics =
                        cameraManager.getCameraCharacteristics(cameraId);
                CameraExtensionCharacteristics extensionCharacteristics =
                        cameraManager.getCameraExtensionCharacteristics(cameraId);
                IntStream capabilities =
                    Arrays.stream(
                                characteristics.get(
                                        CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES
                                )
                        );
                return !extensionCharacteristics.getSupportedExtensions().isEmpty() &&
                       capabilities.anyMatch(capability -> capability == CameraCharacteristics
                                        .REQUEST_AVAILABLE_CAPABILITIES_BACKWARD_COMPATIBLE
                        );
            } catch (CameraAccessException e) {
                throw new RuntimeException(e);
            }
        }).collect(Collectors.toList());
    } else {
        return Collections.emptyList();
    }
}
```

## Create a CameraExtensionSession with the Camera2 Extensions API

The Camera2 Extensions API, when used with compatible devices, lets you access certain camera extensions. The following code snippet showcases an example of how to create a[`CameraExtensionSession`](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionSession)for using night capture mode for an existing Camera2 application.  

### Kotlin

```kotlin
private val captureCallbacks = object : CameraExtensionSession.ExtensionCaptureCallback() {
    // Implement Capture Callbacks
}
private val extensionSessionStateCallback = object : CameraExtensionSession.StateCallback() {
    override fun onConfigured(session: CameraExtensionSession) {
        cameraExtensionSession = session
        try {
            val captureRequest =
                cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW).apply {
                    addTarget(previewSurface)
                }.build()
            session.setRepeatingRequest(
                captureRequest,
                Dispatchers.IO.asExecutor(),
                captureCallbacks
            )
        } catch (e: CameraAccessException) {
            Snackbar.make(
                previewView,
                "Failed to preview capture request",
                Snackbar.LENGTH_SHORT
            ).show()
            requireActivity().finish()
        }
    }

    override fun onClosed(session: CameraExtensionSession) {
        super.onClosed(session)
        cameraDevice.close()
    }

    override fun onConfigureFailed(session: CameraExtensionSession) {
        Snackbar.make(
            previewView,
            "Failed to start camera extension preview",
            Snackbar.LENGTH_SHORT
        ).show()
        requireActivity().finish()
    }
}

private fun startExtensionSession() {
    val outputConfig = arrayListOf(
        OutputConfiguration(stillImageReader.surface),
        OutputConfiguration(previewSurface)
    )
    val extensionConfiguration = ExtensionSessionConfiguration(
        CameraExtensionCharacteristics.EXTENSION_NIGHT,
        outputConfig,
        Dispatchers.IO.asExecutor(),
        extensionSessionStateCallback
    )
    cameraDevice.createExtensionSession(extensionConfiguration)
}
```

### Java

```java
private CameraExtensionSession.ExtensionCaptureCallback captureCallbacks =
        new CameraExtensionSession.ExtensionCaptureCallback() {
            // Implement Capture Callbacks
        };

private CameraExtensionSession.StateCallback extensionSessionStateCallback =
        new CameraExtensionSession.StateCallback() {
            @Override
            public void onConfigured(@NonNull CameraExtensionSession session) {
                cameraExtensionSession = session;
                try {
                    CaptureRequest.Builder captureRequestBuilder =
                            cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);
                    captureRequestBuilder.addTarget(previewSurface);
                    CaptureRequest captureRequest = captureRequestBuilder.build();
                    session.setRepeatingRequest(captureRequest, backgroundExecutor, captureCallbacks);
                } catch (CameraAccessException e) {
                    Snackbar.make(
                            previewView,
                            "Failed to preview capture request",
                            Snackbar.LENGTH_SHORT
                    ).show();
                    requireActivity().finish();
                }
            }

            @Override
            public void onClosed(@NonNull CameraExtensionSession session) {
                super.onClosed(session);
                cameraDevice.close();
            }

            @Override
            public void onConfigureFailed(@NonNull CameraExtensionSession session) {
                Snackbar.make(
                        previewView,
                        "Failed to start camera extension preview",
                        Snackbar.LENGTH_SHORT
                ).show();
                requireActivity().finish();
            }
        };

private void startExtensionSession() {
    ArrayList<OutputConfiguration> outputConfig = new ArrayList<>();
    outputConfig.add(new OutputConfiguration(stillImageReader.getSurface()));
    outputConfig.add(new OutputConfiguration(previewSurface));
    ExtensionSessionConfiguration extensionConfiguration = new ExtensionSessionConfiguration(
            CameraExtensionCharacteristics.EXTENSION_NIGHT,
            outputConfig,
            backgroundExecutor,
            extensionSessionStateCallback
    );
}
```

## Additional resources

For more information, see[`CameraExtensionCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics)and view the public[Camera2 Extensions API samples](https://github.com/android/camera-samples/tree/master/Camera2Extensions)for more.