---
title: Migrate  |  Android Developers
url: https://developer.android.com/agents/skills/camera/camera1-to-camerax/skill
source: html-scrape
---

# Migrate Stay organized with collections Save and categorize content based on your preferences.





## Step 0: Add Dependencies

Check for and add the required CameraX dependencies. Use version 1.3.0 or higher
for interoperability, or version 1.5.0 or higher for Compose extensions.

If you are using a Version Catalog (`libs.versions.toml`), add the following:

```
[versions]
camerax = "<minimum_version_needed>"

[libraries]
androidx-camera-core = { group = "androidx.camera", name = "camera-core", version.ref = "camerax" }
androidx-camera-camera2 = { group = "androidx.camera", name = "camera-camera2", version.ref = "camerax" }
androidx-camera-lifecycle = { group = "androidx.camera", name = "camera-lifecycle", version.ref = "camerax" }
androidx-camera-view = { group = "androidx.camera", name = "camera-view", version.ref = "camerax" }
androidx-camera-compose = { group = "androidx.camera", name = "camera-compose", version.ref = "camerax" }

Camera1ToCameraXSnippets.kt
```

And in your `build.gradle.kts` (or `build.gradle`):

```
implementation(libs.androidx.camera.core)
implementation(libs.androidx.camera.camera2)
implementation(libs.androidx.camera.lifecycle)
implementation(libs.androidx.camera.view)
implementation(libs.androidx.camera.compose)

Camera1ToCameraXSnippets.kt
```

Without a Version Catalog, fall back to these standard Gradle dependencies:

```
implementation "androidx.camera:camera-core:<minimum_version_needed>"
implementation "androidx.camera:camera-camera2:<minimum_version_needed>"
implementation "androidx.camera:camera-lifecycle:<minimum_version_needed>"
implementation "androidx.camera:camera-view:<minimum_version_needed>"
implementation "androidx.camera:camera-compose:<minimum_version_needed>"

Camera1ToCameraXSnippets.kt
```

## Step 1: Remove Legacy Implementation

1. Delete all `android.hardware.Camera` instances.
2. Delete `SurfaceView` and `SurfaceHolder.Callback` implementations
   (`surfaceCreated`, `surfaceChanged`, `surfaceDestroyed`).
3. Remove custom lifecycle handling that opens or releases the camera in
   `onResume` or `onPause`.
4. Remove manual matrix calculations for orientation.

## Step 2: Initialize ProcessCameraProvider

Request the `ProcessCameraProvider` and bind use cases to the Activity or
Fragment lifecycle.

```
val context = LocalContext.current
val lifecycleOwner = LocalLifecycleOwner.current
LaunchedEffect(context, lifecycleOwner) {
  val cameraProviderFuture = ProcessCameraProvider.getInstance(context)
  cameraProviderFuture.addListener({
      val cameraProvider = cameraProviderFuture.get()

      val cameraSelector = CameraSelector.Builder()
        .requireLensFacing(CameraSelector.LENS_FACING_BACK)
        .build()

      val preview = Preview.Builder().build()
      val imageCapture = ImageCapture.Builder()
        .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
        .build()

      cameraProvider.unbindAll() // Unbind before rebinding

      val camera = cameraProvider.bindToLifecycle(
        lifecycleOwner,
        cameraSelector,
        preview,
        imageCapture
      )
      val cameraControl = camera.cameraControl
    }, ContextCompat.getMainExecutor(context)
  )
}

Camera1ToCameraXSnippets.kt
```

## Step 3: Implement the Preview & Tap-to-Focus

Choose exactly one of the following patterns based on the app's UI toolkit:

### Option A: For Android Views (XML Legacy)

Use `androidx.camera.view.PreviewView`.

**1. Set up preview**:

```
preview.setSurfaceProvider(previewView.surfaceProvider)

Camera1ToCameraXSnippets.kt
```

**2. Handle tap-to-focus**:

```
val factory = previewView.meteringPointFactory
val point = factory.createPoint(x, y) // x, y from touch event
val action = FocusMeteringAction.Builder(point, FocusMeteringAction.FLAG_AF).build()
cameraControl?.startFocusAndMetering(action)

Camera1ToCameraXSnippets.kt
```

### Option B: For Jetpack Compose

Use `androidx.camera.compose.CameraXViewfinder`.

**1. Set up preview and SurfaceRequest**:

```
var surfaceRequest by remember { mutableStateOf<SurfaceRequest?>(null) }
val preview = remember {
  Preview.Builder().build().apply {
    setSurfaceProvider { request -> surfaceRequest = request }
  }
}

Camera1ToCameraXSnippets.kt
```

**2. Render viewfinder**:

```
surfaceRequest?.let { request ->
  CameraXViewfinder(
    surfaceRequest = request,
    coordinateTransformer = coordinateTransformer,
    modifier = Modifier
  )
}

Camera1ToCameraXSnippets.kt
```

**3. Handle tap-to-focus in Compose**:

```
// Inside your tap gesture handler...
val surfaceCoords = with(coordinateTransformer) { offset.transform() }
val factory = SurfaceOrientedMeteringPointFactory(
  request.resolution.width.toFloat(),
  request.resolution.height.toFloat()
)
val point = factory.createPoint(surfaceCoords.x, surfaceCoords.y)
val action = FocusMeteringAction.Builder(point, FocusMeteringAction.FLAG_AF).build()
cameraControl?.startFocusAndMetering(action)

Camera1ToCameraXSnippets.kt
```

**4. Update target rotation for Compose**:

```
LaunchedEffect(configuration) {
  if (!view.isInEditMode) {
    val rotation = view.display?.rotation ?: Surface.ROTATION_0
    imageCapture.targetRotation = rotation
    preview.targetRotation = rotation
  }
}

Camera1ToCameraXSnippets.kt
```

## Step 4: Capture Photo

Use the `ImageCapture` use case to take the picture. The `ImageProxy` handles
rotation directly.

```
imageCapture.takePicture(
  cameraExecutor,
  object : ImageCapture.OnImageCapturedCallback() {
    override fun onCaptureSuccess(image: ImageProxy) {
      val buffer = image.planes[0].buffer
      val bytes = ByteArray(buffer.remaining())
      buffer.get(bytes)
      val bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.size)

      // Adjust rotation natively via ImageProxy
      val matrix = Matrix()
      matrix.postRotate(image.imageInfo.rotationDegrees.toFloat())
      if (lensFacing == CameraSelector.LENS_FACING_FRONT) {
        matrix.postScale(-1f, 1f) // Mirror for front camera
      }

      val rotatedBitmap = Bitmap.createBitmap(
        bitmap, 0, 0, bitmap.width, bitmap.height, matrix, true
      )

      // MUST close proxy
      image.close()
    }

    override fun onError(exception: ImageCaptureException) {
      Log.e("CameraX", "Capture failed: ${exception.message}", exception)
    }
  }
)

Camera1ToCameraXSnippets.kt
```

## Step 5: Switch Cameras

To flip between front and rear cameras, change the `CameraSelector` and
re-trigger the `ProcessCameraProvider` logic.

```
lensFacing = if (lensFacing == CameraSelector.LENS_FACING_BACK) {
  CameraSelector.LENS_FACING_FRONT
} else {
  CameraSelector.LENS_FACING_BACK
}

Camera1ToCameraXSnippets.kt
```

## Constraints

* **Don't manage the camera lifecycle manually**: Bind the camera to a
  `LifecycleOwner` through the `ProcessCameraProvider`. Avoid manual camera
  open or close logic in `onResume` or `onPause`.
* **Don't calculate focus matrices manually**: `MeteringPointFactory` handles
  coordinate transformations, including device rotation offsets. Avoid custom
  matrix implementations.
* **Don't forget to close the ImageProxy**: Remember to invoke `image.close()`
  in the capture callback. Skipping this call locks the capture pipeline and
  interrupts subsequent photos.
* **Don't wrap `PreviewView` in `AndroidView` for Compose code**: For Compose
  UI layouts, use `CameraXViewfinder`. Compiling `PreviewView` in an
  `AndroidView` is an old fallback option that introduces resizing issues.