---
title: https://developer.android.com/media/camera/camerax/extensions-api
url: https://developer.android.com/media/camera/camerax/extensions-api
source: md.txt
---

> Documentation index: https://developer.android.com/media/camera/camerax/llms.txt

> [!CAUTION]
> **Caution:** Starting November 1, 2026, CameraX Extensions support is removed on some devices for apps using **CameraX 1.5 or lower** . This change improves camera performance and reliability. CameraX version 1.6 and higher continues to fully support CameraX Extensions. To keep Extensions working for your users, update your app to **CameraX 1.6 or higher** as soon as possible.

CameraX provides an Extensions API for accessing [extensions](https://developer.android.com/media/camera/camera-extensions.md.txt)
that device manufacturers have implemented on various Android devices, such as
Night, HDR, Auto, Bokeh, and Face Retouch. For a list of devices that support
extensions, see [Supported devices](https://developer.android.com/media/camera/supported-devices.md.txt).

## Extensions architecture

The following image shows the camera extensions architecture.
![A CameraX app uses the CameraX Extensions API, which communicates
with the device's camera extensions implementation.](https://developer.android.com/static/images/training/camera/camerax/camerax-camera-extensions-architecture.png) **Figure 1.**Camera Extensions architecture

A CameraX app uses extensions through the CameraX Extensions API. The API
queries which extensions are available, configures an extension camera session,
and communicates with the device's camera extensions implementation.

## Enable an extension

To enable an extension, do the following:

1. Get an [`ExtensionsManager`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager.md.txt) instance.
2. Check that the extension mode is available for the camera with [`isExtensionAvailable()`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager.md.txt#isExtensionAvailable(androidx.camera.core.CameraSelector,kotlin.Int)). Not every device supports every mode.
3. Create an [`ExtensionSessionConfig`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionSessionConfig.md.txt) with the extension mode and your `Preview` and `ImageCapture` use cases.
4. Bind the session config with [`ProcessCameraProvider.bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider.md.txt#bindToLifecycle(androidx.lifecycle.LifecycleOwner,androidx.camera.core.CameraSelector,androidx.camera.core.SessionConfig)). The extension mode is applied to the `Preview` and `ImageCapture` use cases.

### Kotlin

```kotlin
suspend fun bindNightMode(
    context: Context,
    lifecycleOwner: LifecycleOwner,
    surfaceProvider: Preview.SurfaceProvider,
) {
    val cameraProvider = ProcessCameraProvider.awaitInstance(context)
    val extensionsManager =
        ExtensionsManager.getInstance(context, cameraProvider)
    val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

    // Not every device supports every mode, and binding a mode that the
    // camera doesn't support fails. Check availability first.
    val isNightAvailable = extensionsManager.isExtensionAvailable(
        cameraSelector, ExtensionMode.NIGHT
    )
    if (!isNightAvailable) {
        // Bind a regular session instead (not shown) so that the camera
        // still works on devices without the Night extension.
        return
    }

    val preview = Preview.Builder().build()
    preview.setSurfaceProvider(surfaceProvider)
    val imageCapture = ImageCapture.Builder().build()

    // The session config ties the extension mode to the use cases, so
    // CameraX applies Night mode to both Preview and ImageCapture.
    val sessionConfig = ExtensionSessionConfig(
        ExtensionMode.NIGHT,
        extensionsManager,
        preview,
        imageCapture,
    )

    cameraProvider.bindToLifecycle(
        lifecycleOwner, cameraSelector, sessionConfig
    )
}
```

### Java

```java
void bindNightMode(Context context, LifecycleOwner lifecycleOwner,
        Preview.SurfaceProvider surfaceProvider) {
    Executor mainExecutor = ContextCompat.getMainExecutor(context);
    ListenableFuture<ProcessCameraProvider> providerFuture =
            ProcessCameraProvider.getInstance(context);

    // Both the camera provider and ExtensionsManager initialize
    // asynchronously. Bind only after both are ready.
    providerFuture.addListener(() -> {
        try {
            ProcessCameraProvider cameraProvider = providerFuture.get();
            ListenableFuture<ExtensionsManager> managerFuture =
                    ExtensionsManager.getInstanceAsync(
                            context, cameraProvider);
            managerFuture.addListener(() -> {
                try {
                    bindNightModeSession(managerFuture.get(),
                            cameraProvider, lifecycleOwner,
                            surfaceProvider);
                } catch (ExecutionException | InterruptedException e) {
                    Log.e(TAG, "Failed to get ExtensionsManager", e);
                }
            }, mainExecutor);
        } catch (ExecutionException | InterruptedException e) {
            Log.e(TAG, "Failed to get the camera provider", e);
        }
    }, mainExecutor);
}

void bindNightModeSession(ExtensionsManager extensionsManager,
        ProcessCameraProvider cameraProvider,
        LifecycleOwner lifecycleOwner,
        Preview.SurfaceProvider surfaceProvider) {
    CameraSelector cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA;

    // Not every device supports every mode, and binding a mode that the
    // camera doesn't support fails. Check availability first.
    if (!extensionsManager.isExtensionAvailable(
            cameraSelector, ExtensionMode.NIGHT)) {
        // Bind a regular session instead (not shown) so that the camera
        // still works on devices without the Night extension.
        return;
    }

    Preview preview = new Preview.Builder().build();
    preview.setSurfaceProvider(surfaceProvider);
    ImageCapture imageCapture = new ImageCapture.Builder().build();

    // The session config ties the extension mode to the use cases, so
    // CameraX applies Night mode to both Preview and ImageCapture.
    ExtensionSessionConfig sessionConfig = new ExtensionSessionConfig(
            ExtensionMode.NIGHT, extensionsManager, preview, imageCapture);

    cameraProvider.bindToLifecycle(
            lifecycleOwner, cameraSelector, sessionConfig);
}
```

> [!NOTE]
> **Note:** Query capabilities such as zoom range, preview stabilization, and supported output formats from the `CameraInfo` of the extension-enabled camera. They can differ from those of the same camera without extensions.

## Supported use cases

The following table shows which use cases you can bind with an extension
enabled:

| Use case | With an extension enabled |
|---|---|
| `Preview`, `ImageCapture` | Supported. The extension mode is applied. |
| `VideoCapture` | Supported. `VideoCapture` records the shared `Preview` stream. |
| `ImageAnalysis` | Not supported. |

## Check whether the camera supports a session config

If you add more use cases, such as `VideoCapture`, or set other features, check
that the camera supports the whole combination before you bind it:

1. Call `isExtensionAvailable()` with the same `CameraSelector` and mode.
2. Pass the `ExtensionSessionConfig` to [`ProcessCameraProvider.getCameraInfo()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider.md.txt#getCameraInfo(androidx.camera.core.CameraSelector,androidx.camera.core.SessionConfig)). It returns the `CameraInfo` of the camera that `bindToLifecycle()` would bind for that config.
3. Call [`isSessionConfigSupported()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo.md.txt#isSessionConfigSupported(androidx.camera.core.SessionConfig)) on that `CameraInfo`.

If either check fails, bind a regular `SessionConfig` instead.

> [!NOTE]
> **Note:** `getCameraInfo()` throws an `IllegalArgumentException` if no camera matches the `CameraSelector` and session config. Checking `isExtensionAvailable()` first with the same `CameraSelector` and mode makes sure that a matching camera exists, so you don't need a `try`-`catch` block.

### Kotlin

```kotlin
fun createSessionConfig(
    mode: Int,
    vararg useCases: UseCase,
): SessionConfig {
    // getCameraInfo() throws if no camera matches the extension, so check
    // that the mode is available first.
    if (extensionsManager.isExtensionAvailable(cameraSelector, mode)) {
        val extensionConfig =
            ExtensionSessionConfig(mode, extensionsManager, *useCases)
        // Check the camera that would actually be bound for this config,
        // and verify that it supports these use cases together with the
        // extension, for example VideoCapture.
        if (cameraProvider.getCameraInfo(cameraSelector, extensionConfig)
                .isSessionConfigSupported(extensionConfig)
        ) {
            return extensionConfig
        }
    }
    // The same use cases can still run in a regular session, so the app
    // keeps working without the extension.
    return SessionConfig(*useCases)
}

cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    createSessionConfig(
        ExtensionMode.NIGHT, preview, imageCapture, videoCapture
    ),
)
```

### Java

```java
SessionConfig createSessionConfig(int mode, UseCase... useCases) {
    // getCameraInfo() throws if no camera matches the extension, so check
    // that the mode is available first.
    if (extensionsManager.isExtensionAvailable(cameraSelector, mode)) {
        ExtensionSessionConfig extensionConfig =
                new ExtensionSessionConfig(
                        mode, extensionsManager, useCases);
        // Check the camera that would actually be bound for this config,
        // and verify that it supports these use cases together with the
        // extension, for example VideoCapture.
        if (cameraProvider.getCameraInfo(cameraSelector, extensionConfig)
                .isSessionConfigSupported(extensionConfig)) {
            return extensionConfig;
        }
    }
    // The same use cases can still run in a regular session, so the app
    // keeps working without the extension.
    return new SessionConfig(useCases);
}

cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector,
        createSessionConfig(
                ExtensionMode.NIGHT, preview, imageCapture, videoCapture));
```

## Switch or disable an extension

To switch to another extension mode, call `bindToLifecycle()` again with a new
`ExtensionSessionConfig`. To disable extensions, bind a regular
[`SessionConfig`](https://developer.android.com/reference/androidx/camera/core/SessionConfig.md.txt) with the same use cases. You don't need to
call `unbind()` or `unbindAll()` first: the previously bound session config and
its use cases are unbound automatically.

### Kotlin

```kotlin
// Binding a new session config unbinds the previous one and its use
// cases, so you don't need to call unbindAll() before switching modes.
cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    ExtensionSessionConfig(
        ExtensionMode.NIGHT, extensionsManager, preview, imageCapture
    ),
)

// A regular SessionConfig with the same use cases turns the extension off
// while Preview and ImageCapture keep working.
cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    SessionConfig(preview, imageCapture),
)
```

### Java

```java
// Binding a new session config unbinds the previous one and its use
// cases, so you don't need to call unbindAll() before switching modes.
cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.NIGHT,
                extensionsManager, preview, imageCapture));

// A regular SessionConfig with the same use cases turns the extension off
// while Preview and ImageCapture keep working.
cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector,
        new SessionConfig(preview, imageCapture));
```

## Improve the capture experience

Some extension modes, such as Night and HDR, can take several seconds to process
a still image. To keep users informed while they wait, use postview and capture
progress when the device supports them:

- **Postview** delivers a low-resolution image early, which you can show until the final image is ready.
- **Capture process progress** reports processing progress from 0 to 100, which you can show as a progress indicator.

Enable postview with
[`ImageCapture.Builder.setPostviewEnabled()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder.md.txt#setPostviewEnabled(boolean)) before you
bind. If the camera doesn't support postview, no postview image is generated.
After binding, use
[`ImageCapture.getImageCaptureCapabilities()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.md.txt#getImageCaptureCapabilities(androidx.camera.core.CameraInfo))
with the bound camera's `CameraInfo` to check
[`isPostviewSupported()`](https://developer.android.com/reference/androidx/camera/core/ImageCaptureCapabilities.md.txt#isPostviewSupported()) and
[`isCaptureProcessProgressSupported()`](https://developer.android.com/reference/androidx/camera/core/ImageCaptureCapabilities.md.txt#isCaptureProcessProgressSupported()),
and set up your UI to match.

### Kotlin

```kotlin
// Postview must be configured before binding. If the camera doesn't
// support postview, enabling it has no effect.
val imageCapture = ImageCapture.Builder()
    .setPostviewEnabled(true)
    .build()

val camera = cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    ExtensionSessionConfig(
        ExtensionMode.NIGHT, extensionsManager, preview, imageCapture
    ),
)

// Postview and progress support depend on the extension-enabled camera,
// so query the capabilities of the bound camera.
val capabilities =
    ImageCapture.getImageCaptureCapabilities(camera.cameraInfo)
setUpCaptureUi(
    showPostview = capabilities.isPostviewSupported,
    showProgress = capabilities.isCaptureProcessProgressSupported,
)

// Extension captures can take several seconds. Progress updates and an
// early postview image show users that the capture is being processed.
val results = imageCapture.takePicture(
    outputFileOptions,
    onCaptureProcessProgressed = { progress -> updateProgress(progress) },
    onPostviewBitmapAvailable = { bitmap -> showPostview(bitmap) },
)
// Processing is done. Replace the postview with the final image.
showFinalImage(results.savedUri)
```

### Java

```java
// Postview must be configured before binding. If the camera doesn't
// support postview, enabling it has no effect.
ImageCapture imageCapture = new ImageCapture.Builder()
        .setPostviewEnabled(true)
        .build();

Camera camera = cameraProvider.bindToLifecycle(
        lifecycleOwner, cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.NIGHT,
                extensionsManager, preview, imageCapture));

// Postview and progress support depend on the extension-enabled camera,
// so query the capabilities of the bound camera.
ImageCaptureCapabilities capabilities =
        ImageCapture.getImageCaptureCapabilities(camera.getCameraInfo());
setUpCaptureUi(
        capabilities.isPostviewSupported(),
        capabilities.isCaptureProcessProgressSupported());

// Extension captures can take several seconds. Progress updates and an
// early postview image show users that the capture is being processed.
imageCapture.takePicture(outputFileOptions, mainExecutor,
        new ImageCapture.OnImageSavedCallback() {
            @Override
            public void onCaptureProcessProgressed(int progress) {
                updateProgress(progress);
            }

            @Override
            public void onPostviewBitmapAvailable(@NonNull Bitmap bitmap) {
                showPostview(bitmap);
            }

            @Override
            public void onImageSaved(
                    @NonNull ImageCapture.OutputFileResults results) {
                // Processing is done. Replace the postview with the final
                // image.
                showFinalImage(results.getSavedUri());
            }

            @Override
            public void onError(@NonNull ImageCaptureException exception) {
                Log.e(TAG, "Capture failed", exception);
            }
        });
```

### Capture Ultra HDR images

Some devices support capturing [Ultra HDR](https://developer.android.com/media/grow/ultra-hdr.md.txt) images while an extension
is enabled. The output format must be set before binding, and binding fails if
the format isn't supported. So check support first: after
`isExtensionAvailable()` returns `true`, get the `CameraInfo` of the
extension-enabled camera with `getCameraInfo()` and an `ExtensionSessionConfig`,
then check whether
[`getSupportedOutputFormats()`](https://developer.android.com/reference/androidx/camera/core/ImageCaptureCapabilities.md.txt#getSupportedOutputFormats()) includes
`OUTPUT_FORMAT_JPEG_ULTRA_HDR`.

### Kotlin

```kotlin
// Supported output formats can differ when an extension is enabled, so
// query them from the extension-enabled camera. isExtensionAvailable()
// must have returned true for this selector and mode first; otherwise,
// getCameraInfo() throws.
val extensionCameraInfo = cameraProvider.getCameraInfo(
    cameraSelector,
    ExtensionSessionConfig(ExtensionMode.NIGHT, extensionsManager),
)
val supportedFormats = ImageCapture
    .getImageCaptureCapabilities(extensionCameraInfo)
    .supportedOutputFormats

// Binding fails if the output format isn't supported, so request Ultra HDR
// only when the extension-enabled camera supports it.
val imageCapture = ImageCapture.Builder().apply {
    if (ImageCapture.OUTPUT_FORMAT_JPEG_ULTRA_HDR in supportedFormats) {
        setOutputFormat(ImageCapture.OUTPUT_FORMAT_JPEG_ULTRA_HDR)
    }
}.build()

cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    ExtensionSessionConfig(
        ExtensionMode.NIGHT, extensionsManager, preview, imageCapture
    ),
)
```

### Java

```java
// Supported output formats can differ when an extension is enabled, so
// query them from the extension-enabled camera. isExtensionAvailable()
// must have returned true for this selector and mode first; otherwise,
// getCameraInfo() throws.
CameraInfo extensionCameraInfo = cameraProvider.getCameraInfo(
        cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.NIGHT, extensionsManager));
Set<Integer> supportedFormats =
        ImageCapture.getImageCaptureCapabilities(extensionCameraInfo)
                .getSupportedOutputFormats();

// Binding fails if the output format isn't supported, so request Ultra HDR
// only when the extension-enabled camera supports it.
ImageCapture.Builder builder = new ImageCapture.Builder();
if (supportedFormats.contains(ImageCapture.OUTPUT_FORMAT_JPEG_ULTRA_HDR)) {
    builder.setOutputFormat(ImageCapture.OUTPUT_FORMAT_JPEG_ULTRA_HDR);
}
ImageCapture imageCapture = builder.build();

cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.NIGHT,
                extensionsManager, preview, imageCapture));
```

## Monitor and adjust the extension

After binding, use
[`ExtensionsManager.getCameraExtensionsInfo()`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager.md.txt#getCameraExtensionsInfo(androidx.camera.core.CameraInfo)) and
[`ExtensionsManager.getCameraExtensionsControl()`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager.md.txt#getCameraExtensionsControl(androidx.camera.core.CameraControl))
with the bound camera to monitor and adjust the extension.

### Adjust the extension strength

If [`isExtensionStrengthAvailable()`](https://developer.android.com/reference/androidx/camera/extensions/CameraExtensionsInfo.md.txt#isExtensionStrengthAvailable()) returns
`true`, call [`setExtensionStrength()`](https://developer.android.com/reference/androidx/camera/extensions/CameraExtensionsControl.md.txt#setExtensionStrength(int)) with a value
from 0 to 100. A value of 0 applies no extension processing, and 100 is the
default. What the strength controls depends on the mode; for example, in Night
mode it controls how many images are fused and how bright the final image is.
Observe `getExtensionStrength()` for the current value.

### Kotlin

```kotlin
val camera = cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    ExtensionSessionConfig(
        ExtensionMode.NIGHT, extensionsManager, preview, imageCapture
    ),
)
// Pass the bound extension-enabled camera. For a camera without an
// extension, strength isn't available and the control is null.
val extensionsInfo =
    extensionsManager.getCameraExtensionsInfo(camera.cameraInfo)
val extensionsControl =
    extensionsManager.getCameraExtensionsControl(camera.cameraControl)

// Not every device lets apps adjust the strength, so check support before
// showing a strength control.
if (extensionsInfo.isExtensionStrengthAvailable) {
    // For example, connect this to a slider in your UI.
    extensionsControl?.setExtensionStrength(50)
}
```

### Java

```java
Camera camera = cameraProvider.bindToLifecycle(
        lifecycleOwner, cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.NIGHT,
                extensionsManager, preview, imageCapture));
// Pass the bound extension-enabled camera. For a camera without an
// extension, strength isn't available and the control is null.
CameraExtensionsInfo extensionsInfo =
        extensionsManager.getCameraExtensionsInfo(camera.getCameraInfo());
CameraExtensionsControl extensionsControl =
        extensionsManager.getCameraExtensionsControl(
                camera.getCameraControl());

// Not every device lets apps adjust the strength, so check support before
// showing a strength control.
if (extensionsInfo.isExtensionStrengthAvailable()
        && extensionsControl != null) {
    // For example, connect this to a slider in your UI.
    extensionsControl.setExtensionStrength(50);
}
```

### Show the current extension mode

`ExtensionMode.AUTO` can switch to modes such as Night or HDR depending on the
scene. If
[`isCurrentExtensionModeAvailable()`](https://developer.android.com/reference/androidx/camera/extensions/CameraExtensionsInfo.md.txt#isCurrentExtensionModeAvailable())
returns `true`, observe `getCurrentExtensionMode()` to show users which mode is
active.

### Kotlin

```kotlin
val camera = cameraProvider.bindToLifecycle(
    lifecycleOwner,
    cameraSelector,
    ExtensionSessionConfig(
        ExtensionMode.AUTO, extensionsManager, preview, imageCapture
    ),
)
val extensionsInfo =
    extensionsManager.getCameraExtensionsInfo(camera.cameraInfo)

// In AUTO mode, the active mode can change with the scene, for example to
// NIGHT in low light. The LiveData is null when the device doesn't report
// the current mode.
if (extensionsInfo.isCurrentExtensionModeAvailable) {
    extensionsInfo.currentExtensionMode?.observe(lifecycleOwner) { mode ->
        showActiveModeBadge(mode)
    }
}
```

### Java

```java
Camera camera = cameraProvider.bindToLifecycle(
        lifecycleOwner, cameraSelector,
        new ExtensionSessionConfig(ExtensionMode.AUTO,
                extensionsManager, preview, imageCapture));
CameraExtensionsInfo extensionsInfo =
        extensionsManager.getCameraExtensionsInfo(camera.getCameraInfo());

// In AUTO mode, the active mode can change with the scene, for example to
// NIGHT in low light. The LiveData is null when the device doesn't report
// the current mode.
LiveData<Integer> currentMode = extensionsInfo.getCurrentExtensionMode();
if (extensionsInfo.isCurrentExtensionModeAvailable()
        && currentMode != null) {
    currentMode.observe(lifecycleOwner, this::showActiveModeBadge);
}
```

### Suggest Night mode

The night mode indicator tells your app when the scene is dark enough that the
Night extension would help, so you can suggest that the user switch to it. The
indicator is reported while the camera is running **without** an extension. Use
[`CameraInfo.isNightModeIndicatorSupported()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo.md.txt#isNightModeIndicatorSupported())
to check support, then observe
[`CameraInfo.getNightModeIndicator()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo.md.txt#getNightModeIndicator()). When the value
is [`NightModeIndicator.RECOMMENDED`](https://developer.android.com/reference/androidx/camera/core/NightModeIndicator.md.txt), show a suggestion.
If the user accepts, bind an `ExtensionSessionConfig` with
`ExtensionMode.NIGHT`.

The night mode indicator requires CameraX 1.7.0 or higher and a device running
Android 16 (API level 36) or higher. `isNightModeIndicatorSupported()` returns
`false` on lower API levels.

### Kotlin

```kotlin
// The indicator is reported while a regular (non-extension) session is
// running with Preview, so the app can suggest Night mode only when the
// scene is dark enough to need it.
val cameraInfo = camera.cameraInfo

// Don't suggest a mode that the camera can't bind.
val isNightAvailable = extensionsManager.isExtensionAvailable(
    cameraSelector, ExtensionMode.NIGHT
)

// If the indicator isn't supported, its value is always UNKNOWN.
if (cameraInfo.isNightModeIndicatorSupported && isNightAvailable) {
    cameraInfo.nightModeIndicator.observe(lifecycleOwner) { indicator ->
        showNightModeSuggestion(
            visible = indicator == NightModeIndicator.RECOMMENDED
        )
    }
}

fun onNightModeSuggestionAccepted() {
    // Binding the extension session config replaces the regular session.
    cameraProvider.bindToLifecycle(
        lifecycleOwner,
        cameraSelector,
        ExtensionSessionConfig(
            ExtensionMode.NIGHT, extensionsManager, preview, imageCapture
        ),
    )
}
```

### Java

```java
// The indicator is reported while a regular (non-extension) session is
// running with Preview, so the app can suggest Night mode only when the
// scene is dark enough to need it.
CameraInfo cameraInfo = camera.getCameraInfo();

// Don't suggest a mode that the camera can't bind.
boolean isNightAvailable = extensionsManager.isExtensionAvailable(
        cameraSelector, ExtensionMode.NIGHT);

// If the indicator isn't supported, its value is always UNKNOWN.
if (cameraInfo.isNightModeIndicatorSupported() && isNightAvailable) {
    cameraInfo.getNightModeIndicator().observe(lifecycleOwner,
            indicator -> showNightModeSuggestion(
                    indicator == NightModeIndicator.RECOMMENDED));
}

void onNightModeSuggestionAccepted() {
    // Binding the extension session config replaces the regular session.
    cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector,
            new ExtensionSessionConfig(ExtensionMode.NIGHT,
                    extensionsManager, preview, imageCapture));
}
```

## Dependencies

The CameraX Extensions API is implemented in the `camera-extensions` library.
The extensions depend on the CameraX core modules (`core`, `camera2`, and
`lifecycle`). Use the same version for all `androidx.camera` libraries.

### Kotlin

```kotlin
dependencies {
    val camerax_version = "1.7.0"
    implementation("androidx.camera:camera-core:${camerax_version}")
    implementation("androidx.camera:camera-camera2:${camerax_version}")
    implementation("androidx.camera:camera-lifecycle:${camerax_version}")
    // The CameraX Extensions library
    implementation("androidx.camera:camera-extensions:${camerax_version}")
}
```

### Groovy

```groovy
dependencies {
    def camerax_version = "1.7.0"
    implementation "androidx.camera:camera-core:${camerax_version}"
    implementation "androidx.camera:camera-camera2:${camerax_version}"
    implementation "androidx.camera:camera-lifecycle:${camerax_version}"
    // The CameraX Extensions library
    implementation "androidx.camera:camera-extensions:${camerax_version}"
}
```

## Migrate from the deprecated camera selector API

[`ExtensionsManager.getExtensionEnabledCameraSelector()`](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager.md.txt#getExtensionEnabledCameraSelector(androidx.camera.core.CameraSelector,kotlin.Int))
has been deprecated since CameraX 1.7.0-alpha02. Use `ExtensionSessionConfig`
instead, as shown in the following table:

| Deprecated | Replacement |
|---|---|
| `getExtensionEnabledCameraSelector(cameraSelector, mode)` | `ExtensionSessionConfig(mode, extensionsManager, useCases)` |
| `bindToLifecycle(owner, extensionCameraSelector, preview, imageCapture)` | `bindToLifecycle(owner, cameraSelector, extensionSessionConfig)` |
| `getCameraInfo(extensionCameraSelector)` | `getCameraInfo(cameraSelector, extensionSessionConfig)` |
| `unbindAll()`, then bind again to switch modes | Bind the new session config. The previous one is unbound automatically. |

## Additional resources

For more information about CameraX, see the following resources.

### Codelab


- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [Camera Samples catalog](https://github.com/android/camera-samples) (see the Extensions sample)

### Other references

- [CameraX Vendor Extensions](https://source.android.com/docs/core/camera/camerax-vendor-extensions)
- [CameraX Vendor Extensions Validation Tool](https://source.android.com/docs/core/camera/camerax-vendor-extensions-validation-tool)