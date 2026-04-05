---
title: https://developer.android.com/media/camera/camerax/camera1-to-camerax
url: https://developer.android.com/media/camera/camerax/camera1-to-camerax
source: md.txt
---

# Migrate Camera1 to CameraX

If your app uses the original[`Camera`](https://developer.android.com/reference/android/hardware/Camera)class ("Camera1"), which has been deprecated since[Android 5.0 (API level 21)](https://developer.android.com/about/versions/lollipop), we highly recommend updating to a modern Android camera API. Android offers[CameraX](https://developer.android.com/training/camerax)(a standardized, robust[Jetpack](https://developer.android.com/jetpack)camera API) and[Camera2](https://developer.android.com/training/camera2)(a low-level, framework API). For the vast majority of cases, we recommend migrating your app to CameraX. Here's why:

- **Ease of use:**CameraX handles the low-level details, so that you can focus less on building a camera experience from scratch and more on differentiating your app.
- **CameraX handles fragmentation for you:** CameraX reduces long-term maintenance costs and device-specific code, bringing higher quality experiences to users. For more on this, check out our[Better Device Compatibility with CameraX](https://android-developers.googleblog.com/2022/10/better-device-compatibility-with-camerax.html)blog post.
- **Advanced capabilities:** CameraX is carefully designed to make advanced functionality simple to incorporate into your app. For example, you can easily apply Bokeh, Face Retouch, HDR (High Dynamic Range), and low-light-brightening Night capture mode to your photos with[CameraX Extensions](https://developer.android.com/training/camerax/extensions-api).
- **Updatability:** Android releases new capabilities and bug fixes to CameraX throughout the year. By migrating to CameraX, your app gets the latest Android camera technology[with each CameraX release](https://developer.android.com/jetpack/androidx/releases/camera), not just on the annual Android version releases.

In this guide, you'll find common scenarios for camera applications. Each scenario includes a Camera1 implementation and a CameraX implementation for comparison.

When it comes to migration, sometimes you need extra flexibility to integrate with an existing codebase. All CameraX code in this guide has a[`CameraController`](https://developer.android.com/reference/androidx/camera/view/CameraController)implementation---great if you want the simplest way to use CameraX---and also a[`CameraProvider`](https://developer.android.com/reference/androidx/camera/core/CameraProvider)implementation---great if you need more flexibility. To help you decide which is the right one for you, here are the benefits of each:

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #### CameraController                                                                                                                                                                                                                             | #### CameraProvider                                                                                                                                                                          |
| Requires little setup code                                                                                                                                                                                                                        | Allows for more control                                                                                                                                                                      |
| Allowing CameraX to handle more of the setup process means functionality like tap-to-focus and pinch-to-zoom work automatically                                                                                                                   | Since the app developer handles setup, there are more opportunities to customize the configuration, like enabling output image rotation or setting the output image format in`ImageAnalysis` |
| Requiring`PreviewView`for the camera preview allows CameraX to offer seamless end-to-end integration, as in our ML Kit integration which can map the ML model result coordinates (like face bounding boxes) directly onto the preview coordinates | The ability to use a custom \`Surface\` for camera preview allows for more flexibility, such as using your existing \`Surface\` code which could be an input to other parts of your app      |

If you get stuck trying to migrate, reach out to us on the[CameraX Discussion Group](https://groups.google.com/a/android.com/g/camerax-developers).

## Before you migrate

### Compare CameraX to Camera1 usage

While the code may look different, the underlying concepts in Camera1 and CameraX are very similar. CameraX[abstracts common camera functionality into use cases](https://developer.android.com/training/camerax/architecture#structure), and as a result, many tasks that were left to the developer in Camera1 are handled automatically by CameraX. There are four[`UseCase`](https://developer.android.com/reference/androidx/camera/core/UseCase)s in CameraX, which you can use for a variety of camera tasks:[`Preview`](https://developer.android.com/training/camerax/preview),[`ImageCapture`](https://developer.android.com/training/camerax/take-photo),[`VideoCapture`](https://developer.android.com/training/camerax/video-capture), and[`ImageAnalysis`](https://developer.android.com/training/camerax/analyze).

One example of CameraX handling low-level details for developers is the[`ViewPort`](https://developer.android.com/reference/androidx/camera/core/ViewPort)that is shared among active`UseCase`s. This ensures all`UseCase`s see exactly the same pixels. In Camera1, you have to manage these details yourself, and given the variability in aspect ratios across devices' camera sensors and screens, it can be tricky to ensure your preview matches captured photos and videos.

As another example, CameraX handles`Lifecycle`callbacks automatically on the`Lifecycle`instance you pass it. This means CameraX handles your app's connection to the camera during the entire[Android activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle), including the following cases: closing the camera when your app goes into the background; removing the camera preview when the screen no longer requires displaying it; and pausing the camera preview when another activity takes foreground precedence, like an incoming video call.

Finally, CameraX handles rotation and scaling without any additional code needed on your part. In the case of an`Activity`with an unlocked orientation, the`UseCase`setup is done every time the device is rotated, as the system destroys and recreates the`Activity`on orientation changes. This results in the`UseCases`setting their target rotation to match the display's orientation by default each time.[Read more about rotations in CameraX](https://developer.android.com/training/camerax/orientation-rotation).

Before jumping into the details, here's a high-level look at CameraX's`UseCase`s and how a Camera1 app would relate. (CameraX concepts are in**blue**and Camera1 concepts are in**green**.)  

|---------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------|
| #### CameraX                                                                                                                                                                                                             ||||
| CameraController / CameraProvider Configuration                                                                                                                                                                          ||||
| **↓**                                       | **↓**                                                | **↓**                                                           | **↓**                                                |
| Preview                                     | ImageCapture                                         | VideoCapture                                                    | ImageAnalysis                                        |
| ⁞                                           | ⁞                                                    | ⁞                                                               | ⁞                                                    |
| Manage preview Surface and set it on Camera | Set PictureCallback and call takePicture() on Camera | Manage Camera and MediaRecorder configuration in specific order | Custom analysis code built on top of preview Surface |
| **↑**                                       | **↑**                                                | **↑**                                                           | **↑**                                                |
| Device-specific Code                                                                                                                                                                                                     ||||
| **↑**                                                                                                                                                                                                                    ||||
| Device Rotation and Scaling Management                                                                                                                                                                                   ||||
| **↑**                                                                                                                                                                                                                    ||||
| Camera Session Management (Camera Selection, Lifecycle Management)                                                                                                                                                       ||||
| #### Camera1                                                                                                                                                                                                             ||||

### Compatibility and performance in CameraX

CameraX supports devices running[Android 5.0 (API level 21)](https://developer.android.com/about/versions/lollipop)and higher. This represents over 98% of existing Android devices. CameraX is built to handle differences between devices automatically, reducing the need for device-specific code in your app. Furthermore, we test over 150 physical devices on all Android versions since 5.0 in our[CameraX Test Lab](https://developer.android.com/training/camerax#consistency). You can review the full list of[devices currently in the Test Lab](https://developer.android.com/training/camerax/devices).

CameraX uses an[`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor)to drive the camera stack. You can[set your own executor on CameraX](https://developer.android.com/reference/androidx/camera/core/CameraXConfig.Builder#setCameraExecutor(java.util.concurrent.Executor))if your app has specific threading requirements. If not set, CameraX creates and uses an optimized default internal`Executor`. Many of the platform APIs on which CameraX is built require blocking interprocess communication (IPC) with hardware that can sometimes take hundreds of milliseconds to respond. For this reason, CameraX only calls these APIs from background threads, which ensures the main thread is not blocked and that the UI remains fluid.[Read more about threads](https://developer.android.com/training/camerax/configuration#threads).

If the target market for your app includes low-end devices, CameraX provides a way to reduce setup time with a[camera limiter](https://developer.android.com/training/camerax/configuration#camera-limiter). Since the process of connecting to hardware components can take a non-trivial amount of time, especially on low-end devices, you can specify the set of cameras your app needs. CameraX only connects to these cameras during setup. For example, if the application uses only back-facing cameras, it can set this configuration with`DEFAULT_BACK_CAMERA`and then CameraX avoids initializing front-facing cameras to reduce the latency.

### Android development concepts

This guide assumes a general familiarity with Android development. Beyond the basics, here are a couple of concepts that are helpful to understand before jumping into the code below:

- [View Binding](https://developer.android.com/topic/libraries/view-binding)generates a binding class for your XML layout files, allowing you to easily[reference your views in Activities](https://developer.android.com/topic/libraries/view-binding#activities), as is done in several code snippets below. There are some[differences between view binding and`findViewById()`](https://developer.android.com/topic/libraries/view-binding#findviewbyid)(the prior way to reference views), but in the code below you should be able to replace the view binding lines with a similar`findViewById()`call.
- [Asynchronous Coroutines](https://developer.android.com/kotlin/coroutines)are a concurrency design pattern added in Kotlin 1.3 that can be used to handle CameraX methods that return a[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture). This is made easier with the Jetpack[Concurrent](https://developer.android.com/jetpack/androidx/releases/concurrent)library as of version 1.1.0. To add an asynchronous coroutine to your app:
  1. Add`implementation("androidx.concurrent:concurrent-futures-ktx:1.1.0")`to your Gradle file.
  2. Put any CameraX code that returns a`ListenableFuture`in a[`launch`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/launch.html)block or[suspending function](https://kotlinlang.org/docs/composing-suspending-functions.html).
  3. Add an[`await()`](https://developer.android.com/reference/androidx/concurrent/futures/ListenableFutureKt#(com.google.common.util.concurrent.ListenableFuture).await())call to the function call that returns a`ListenableFuture`.
  4. For a deeper understanding of how coroutines work, see the[Start a coroutine](https://developer.android.com/kotlin/coroutines/coroutines-adv#start)guide.

## Migrate common scenarios

This section explains how to migrate common scenarios from Camera1 to CameraX. Each scenario covers a Camera1 implementation, a CameraX`CameraProvider`implementation, and a CameraX`CameraController`implementation.

### Selecting a camera

In your camera application, one of the first things you may want to offer is a way to select different cameras.

#### Camera1

In Camera1, you can either call[`Camera.open()`](https://developer.android.com/reference/android/hardware/Camera#open())with no parameters to open the first back-facing camera, or you can pass in an integer ID for the camera you want to open. Here's an example of how that might look:  

```kotlin
// Camera1: select a camera from id.

// Note: opening the camera is a non-trivial task, and it shouldn't be
// called from the main thread, unlike CameraX calls, which can be
// on the main thread since CameraX kicks off background threads
// internally as needed.

private fun safeCameraOpen(id: Int): Boolean {
    return try {
        releaseCameraAndPreview()
        camera = Camera.open(id)
        true
    } catch (e: Exception) {
        Log.e(TAG, "failed to open camera", e)
        false
    }
}

private fun releaseCameraAndPreview() {
    preview?.setCamera(null)
    camera?.release()
    camera = null
}
```

#### CameraX: CameraController

In CameraX, camera selection is handled by the`CameraSelector`class. CameraX makes the common case of using the default camera easy. You can specify whether you want the default front camera or the default back camera. Furthermore, CameraX's`CameraControl`object lets you easily[set the zoom level](https://developer.android.com/training/camerax/configuration#zoom)for your app, so if your app is running on a device that supports[logical cameras](https://developer.android.com/training/camera2/multi-camera#logical), then it will switch to the proper lens.

Here's the CameraX code for using the default back camera with a`CameraController`:  

```kotlin
// CameraX: select a camera with CameraController

var cameraController = LifecycleCameraController(baseContext)
val selector = CameraSelector.Builder()
    .requireLensFacing(CameraSelector.LENS_FACING_BACK).build()
cameraController.cameraSelector = selector
```

#### CameraX: CameraProvider

Here's an example of selecting the default front camera with`CameraProvider`(either the front or back camera can be used with either`CameraController`or`CameraProvider`):  

```kotlin
// CameraX: select a camera with CameraProvider.

// Use await() within a suspend function to get CameraProvider instance.
// For more details on await(), see the "Android development concepts"
// section above.
private suspend fun startCamera() {
    val cameraProvider = ProcessCameraProvider.getInstance(this).await()

    // Set up UseCases (more on UseCases in later scenarios)
    var useCases:Array = ...

    // Set the cameraSelector to use the default front-facing (selfie)
    // camera.
    val cameraSelector = CameraSelector.DEFAULT_FRONT_CAMERA

    try {
        // Unbind UseCases before rebinding.
        cameraProvider.unbindAll()

        // Bind UseCases to camera. This function returns a camera
        // object which can be used to perform operations like zoom,
        // flash, and focus.
        var camera = cameraProvider.bindToLifecycle(
            this, cameraSelector, useCases)

    } catch(exc: Exception) {
        Log.e(TAG, "UseCase binding failed", exc)
    }
})

...

// Call startCamera in the setup flow of your app, such as in onViewCreated.
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)

    ...

    lifecycleScope.launch {
        startCamera()
    }
}
```

If you want control over which camera is selected, this is also possible in CameraX if you use`CameraProvider`by calling[`getAvailableCameraInfos()`](https://developer.android.com/reference/androidx/camera/core/CameraProvider#getAvailableCameraInfos()), which gives you a`CameraInfo`object for checking certain camera properties like[`isFocusMeteringSupported()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#isFocusMeteringSupported(androidx.camera.core.FocusMeteringAction)). You can then convert it to a`CameraSelector`to be used like in the above examples with the`CameraInfo.getCameraSelector()`method.

You can get more details about each camera by using the[`Camera2CameraInfo`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraInfo)class. Call[`getCameraCharacteristic()`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraInfo#getCameraCharacteristic(android.hardware.camera2.CameraCharacteristics.Key%3CT%3E))with a key for the camera data you want. Check the[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics)class for a list of all the keys you can query for.

Here's an example using a custom`checkFocalLength()`function that you could define yourself:  

```kotlin
// CameraX: get a cameraSelector for first camera that matches the criteria
// defined in checkFocalLength().

val cameraInfo = cameraProvider.getAvailableCameraInfos()
    .first { cameraInfo ->
        val focalLengths = Camera2CameraInfo.from(cameraInfo)
            .getCameraCharacteristic(
                CameraCharacteristics.LENS_INFO_AVAILABLE_FOCAL_LENGTHS
            )
        return checkFocalLength(focalLengths)
    }
val cameraSelector = cameraInfo.getCameraSelector()
```

### Showing a preview

A majority of camera applications need to show the camera feed on-screen at some point. With Camera1, you need to manage the lifecycle callbacks correctly, and you also need to determine the rotation and scaling for your preview.

Additionally, in Camera1 you need to decide whether to use a[`TextureView`](https://developer.android.com/reference/android/view/TextureView)or a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)as your preview surface. Both options come with tradeoffs, and in either case, Camera1 requires you to handle rotation and scaling correctly. CameraX's`PreviewView`, on the other hand, has underlying implementations for both`TextureView`and`SurfaceView`. CameraX decides which implementation is best depending on factors such as the type of device and the Android version your app is running on. If either implementation is compatible, you can declare your preference with[`PreviewView.ImplementationMode`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ImplementationMode). The`COMPATIBLE`option uses a`TextureView`for the preview, and the`PERFORMANCE`value uses a`SurfaceView`(when possible).

#### Camera1

To show a preview, you need to write your own`Preview`class with an implementation of the[`android.view.SurfaceHolder.Callback`](https://developer.android.com/reference/android/view/SurfaceHolder.Callback)interface, which is used to pass image data from the camera hardware to the application. Then, before you can start the live image preview, the`Preview`class must be passed to the`Camera`object.  

```kotlin
// Camera1: set up a camera preview.

class Preview(
        context: Context,
        private val camera: Camera
) : SurfaceView(context), SurfaceHolder.Callback {

    private val holder: SurfaceHolder = holder.apply {
        addCallback(this@Preview)
        setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS)
    }

    override fun surfaceCreated(holder: SurfaceHolder) {
        // The Surface has been created, now tell the camera
        // where to draw the preview.
        camera.apply {
            try {
                setPreviewDisplay(holder)
                startPreview()
            } catch (e: IOException) {
                Log.d(TAG, "error setting camera preview", e)
            }
        }
    }

    override fun surfaceDestroyed(holder: SurfaceHolder) {
        // Take care of releasing the Camera preview in your activity.
    }

    override fun surfaceChanged(holder: SurfaceHolder, format: Int,
                                w: Int, h: Int) {
        // If your preview can change or rotate, take care of those
        // events here. Make sure to stop the preview before resizing
        // or reformatting it.
        if (holder.surface == null) {
            return  // The preview surface does not exist.
        }

        // Stop preview before making changes.
        try {
            camera.stopPreview()
        } catch (e: Exception) {
            // Tried to stop a non-existent preview; nothing to do.
        }

        // Set preview size and make any resize, rotate or
        // reformatting changes here.

        // Start preview with new settings.
        camera.apply {
            try {
                setPreviewDisplay(holder)
                startPreview()
            } catch (e: Exception) {
                Log.d(TAG, "error starting camera preview", e)
            }
        }
    }
}

class CameraActivity : AppCompatActivity() {
    private lateinit var viewBinding: ActivityMainBinding
    private var camera: Camera? = null
    private var preview: Preview? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        viewBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(viewBinding.root)

        // Create an instance of Camera.
        camera = getCameraInstance()

        preview = camera?.let {
            // Create the Preview view.
            Preview(this, it)
        }

        // Set the Preview view as the content of the activity.
        val cameraPreview: FrameLayout = viewBinding.cameraPreview
        cameraPreview.addView(preview)
    }
}
```

#### CameraX: CameraController

In CameraX, there's a lot less for you, the developer, to manage. If you use a`CameraController`, then you must also use`PreviewView`. This means the`Preview``UseCase`is implied, making the setup much less work:  

```kotlin
// CameraX: set up a camera preview with a CameraController.

class MainActivity : AppCompatActivity() {
    private lateinit var viewBinding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        viewBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(viewBinding.root)

        // Create the CameraController and set it on the previewView.
        var cameraController = LifecycleCameraController(baseContext)
        cameraController.bindToLifecycle(this)
        val previewView: PreviewView = viewBinding.cameraPreview
        previewView.controller = cameraController
    }
}
```

#### CameraX: CameraProvider

With CameraX's`CameraProvider`, you do not have to use`PreviewView`, but it still greatly simplifies the preview setup over Camera1. For demonstration purposes, this example uses a`PreviewView`, but you can write a custom`SurfaceProvider`to pass into`setSurfaceProvider()`if you have more complex needs.

Here, the`Preview``UseCase`is not implied like it is with`CameraController`, so you need to set it up:  

```kotlin
// CameraX: set up a camera preview with a CameraProvider.

// Use await() within a suspend function to get CameraProvider instance.
// For more details on await(), see the "Android development concepts"
// section above.
private suspend fun startCamera() {
    val cameraProvider = ProcessCameraProvider.getInstance(this).await()

    // Create Preview UseCase.
    val preview = Preview.Builder()
        .build()
        .also {
            it.setSurfaceProvider(
                viewBinding.viewFinder.surfaceProvider
            )
        }

    // Select default back camera.
    val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

    try {
        // Unbind UseCases before rebinding.
        cameraProvider.unbindAll()

        // Bind UseCases to camera. This function returns a camera
        // object which can be used to perform operations like zoom,
        // flash, and focus.
        var camera = cameraProvider.bindToLifecycle(
            this, cameraSelector, useCases)

    } catch(exc: Exception) {
        Log.e(TAG, "UseCase binding failed", exc)
    }
})

...

// Call startCamera() in the setup flow of your app, such as in onViewCreated.
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)

    ...

    lifecycleScope.launch {
        startCamera()
    }
}
```

### Tap-to-focus

When your camera preview is on screen, a common control is to set the focus point when the user taps on the preview.

#### Camera1

To implement tap-to-focus in Camera1, you must calculate the optimal focus`Area`to indicate where the`Camera`should attempt to focus. This`Area`is passed into`setFocusAreas()`. Also, you must set a compatible focus mode on the`Camera`. Focus area only has effect if the current focus mode is`FOCUS_MODE_AUTO`,`FOCUS_MODE_MACRO`,`FOCUS_MODE_CONTINUOUS_VIDEO`, or`FOCUS_MODE_CONTINUOUS_PICTURE`.

Each`Area`is a rectangle with specified weight. The weight is a value between 1 and 1000, and it's used to prioritize focus`Areas`if multiple are set. This example only uses one`Area`, so the weight value doesn't matter. Coordinates of the rectangle range from -1000 to 1000. The upper left point is (-1000, -1000). The lower right point is (1000, 1000). The direction is relative to the sensor orientation, that is, what the sensor sees. The direction is not affected by the rotation or mirroring of`Camera.setDisplayOrientation()`, so you need to convert the touch event coordinates to the sensor coordinates.  

```kotlin
// Camera1: implement tap-to-focus.

class TapToFocusHandler : Camera.AutoFocusCallback {
    private fun handleFocus(event: MotionEvent) {
        val camera = camera ?: return
        val parameters = try {
            camera.getParameters()
        } catch (e: RuntimeException) {
            return
        }

        // Cancel previous auto-focus function, if one was in progress.
        camera.cancelAutoFocus()

        // Create focus Area.
        val rect = calculateFocusAreaCoordinates(event.x, event.y)
        val weight = 1  // This value's not important since there's only 1 Area.
        val focusArea = Camera.Area(rect, weight)

        // Set the focus parameters.
        parameters.setFocusMode(Parameters.FOCUS_MODE_AUTO)
        parameters.setFocusAreas(listOf(focusArea))

        // Set the parameters back on the camera and initiate auto-focus.
        camera.setParameters(parameters)
        camera.autoFocus(this)
    }

    private fun calculateFocusAreaCoordinates(x: Int, y: Int) {
        // Define the size of the Area to be returned. This value
        // should be optimized for your app.
        val focusAreaSize = 100

        // You must define functions to rotate and scale the x and y values to
        // be values between 0 and 1, where (0, 0) is the upper left-hand side
        // of the preview, and (1, 1) is the lower right-hand side.
        val normalizedX = (rotateAndScaleX(x) - 0.5) * 2000
        val normalizedY = (rotateAndScaleY(y) - 0.5) * 2000

        // Calculate the values for left, top, right, and bottom of the Rect to
        // be returned. If the Rect would extend beyond the allowed values of
        // (-1000, -1000, 1000, 1000), then crop the values to fit inside of
        // that boundary.
        val left = max(normalizedX - (focusAreaSize / 2), -1000)
        val top = max(normalizedY - (focusAreaSize / 2), -1000)
        val right = min(left + focusAreaSize, 1000)
        val bottom = min(top + focusAreaSize, 1000)

        return Rect(left, top, left + focusAreaSize, top + focusAreaSize)
    }

    override fun onAutoFocus(focused: Boolean, camera: Camera) {
        if (!focused) {
            Log.d(TAG, "tap-to-focus failed")
        }
    }
}
```

#### CameraX: CameraController

`CameraController`listens to`PreviewView`'s touch events to handle tap-to-focus automatically. You can enable and disable tap-to-focus with[`setTapToFocusEnabled()`](https://developer.android.com/reference/androidx/camera/view/CameraController#setTapToFocusEnabled(boolean)), and check the value with the corresponding getter[`isTapToFocusEnabled()`](https://developer.android.com/reference/androidx/camera/view/CameraController#isTapToFocusEnabled()).

The[`getTapToFocusState()`](https://developer.android.com/reference/androidx/camera/view/CameraController#getTapToFocusState())method returns a[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)object for tracking changes to the focus state on the`CameraController`.  

```kotlin
// CameraX: track the state of tap-to-focus over the Lifecycle of a PreviewView,
// with handlers you can define for focused, not focused, and failed states.

val tapToFocusStateObserver = Observer { state ->
    when (state) {
        CameraController.TAP_TO_FOCUS_NOT_STARTED ->
            Log.d(TAG, "tap-to-focus init")
        CameraController.TAP_TO_FOCUS_STARTED ->
            Log.d(TAG, "tap-to-focus started")
        CameraController.TAP_TO_FOCUS_FOCUSED ->
            Log.d(TAG, "tap-to-focus finished (focus successful)")
        CameraController.TAP_TO_FOCUS_NOT_FOCUSED ->
            Log.d(TAG, "tap-to-focus finished (focused unsuccessful)")
        CameraController.TAP_TO_FOCUS_FAILED ->
            Log.d(TAG, "tap-to-focus failed")
    }
}

cameraController.getTapToFocusState().observe(this, tapToFocusStateObserver)
```

#### CameraX: CameraProvider

When using a`CameraProvider`, there is some setup required to get tap-to-focus working. This example assumes you're using`PreviewView`. If not, you need to adapt the logic to apply to your custom`Surface`.

Here are the steps when using`PreviewView`:

1. Set up a gesture detector to handle tap events.
2. With the tap event, create a`MeteringPoint`using`MeteringPointFactory.createPoint()`.
3. With the`MeteringPoint`, create a`FocusMeteringAction`.
4. With the`CameraControl`object on your`Camera`(returned from`bindToLifecycle()`), call`startFocusAndMetering()`, passing in the`FocusMeteringAction`.
5. (Optional) Respond to the`FocusMeteringResult`.
6. Set your gesture detector to respond to touch events in`PreviewView.setOnTouchListener()`.

```kotlin
// CameraX: implement tap-to-focus with CameraProvider.

// Define a gesture detector to respond to tap events and call
// startFocusAndMetering on CameraControl. If you want to use a
// coroutine with await() to check the result of focusing, see the
// "Android development concepts" section above.
val gestureDetector = GestureDetectorCompat(context,
    object : SimpleOnGestureListener() {
        override fun onSingleTapUp(e: MotionEvent): Boolean {
            val previewView = previewView ?: return
            val camera = camera ?: return
            val meteringPointFactory = previewView.meteringPointFactory
            val focusPoint = meteringPointFactory.createPoint(e.x, e.y)
            val meteringAction = FocusMeteringAction
                .Builder(meteringPoint).build()
            lifecycleScope.launch {
                val focusResult = camera.cameraControl
                    .startFocusAndMetering(meteringAction).await()
                if (!result.isFocusSuccessful()) {
                    Log.d(TAG, "tap-to-focus failed")
                }
            }
        }
    }
)

...

// Set the gestureDetector in a touch listener on the PreviewView.
previewView.setOnTouchListener { _, event ->
    // See pinch-to-zooom scenario for scaleGestureDetector definition.
    var didConsume = scaleGestureDetector.onTouchEvent(event)
    if (!scaleGestureDetector.isInProgress) {
        didConsume = gestureDetector.onTouchEvent(event)
    }
    didConsume
}
```

### Pinch-to-zoom

Zooming in and out of a preview is another common direct manipulation of the camera preview. With the increasing number of cameras on devices, users also expect the lens with the best focal length to be automatically selected as the result of zooming.

#### Camera1

There are two ways to zoom using Camera1. The`Camera.startSmoothZoom()`method animates from the current zoom level to the zoom level you pass in. The`Camera.Parameters.setZoom()`method jumps directly to the zoom level you pass in. Before using either one, call`isSmoothZoomSupported()`or`isZoomSupported()`, respectively, to ensure the related zoom methods you need are available on your Camera.

To implement pinch-to-zoom, this example uses`setZoom()`because the touch listener on the preview surface continually fires events as the pinch gesture happens, so it updates the zoom level immediately each time. The`ZoomTouchListener`class is defined below, and it should be set as a callback to your preview surface's touch listener.  

```kotlin
// Camera1: implement pinch-to-zoom.

// Define a scale gesture detector to respond to pinch events and call
// setZoom on Camera.Parameters.
val scaleGestureDetector = ScaleGestureDetector(context,
    object : ScaleGestureDetector.OnScaleGestureListener {
        override fun onScale(detector: ScaleGestureDetector): Boolean {
            val camera = camera ?: return false
            val parameters = try {
                camera.parameters
            } catch (e: RuntimeException) {
                return false
            }

            // In case there is any focus happening, stop it.
            camera.cancelAutoFocus()

            // Set the zoom level on the Camera.Parameters, and set
            // the Parameters back onto the Camera.
            val currentZoom = parameters.zoom
            parameters.setZoom(detector.scaleFactor * currentZoom)
        camera.setParameters(parameters)
            return true
        }
    }
)

// Define a View.OnTouchListener to attach to your preview view.
class ZoomTouchListener : View.OnTouchListener {
    override fun onTouch(v: View, event: MotionEvent): Boolean =
        scaleGestureDetector.onTouchEvent(event)
}

// Set a ZoomTouchListener to handle touch events on your preview view
// if zoom is supported by the current camera.
if (camera.getParameters().isZoomSupported()) {
    view.setOnTouchListener(ZoomTouchListener())
}
```

#### CameraX: CameraController

Similar to tap-to-focus,`CameraController`listens to PreviewView's touch events to handle pinch-to-zoom automatically. You can enable and disable pinch-to-zoom with[`setPinchToZoomEnabled()`](https://developer.android.com/reference/androidx/camera/view/CameraController#setPinchToZoomEnabled(boolean)), and check the value with the corresponding getter[`isPinchToZoomEnabled()`](https://developer.android.com/reference/androidx/camera/view/CameraController#isPinchToZoomEnabled()).

The[`getZoomState()`](https://developer.android.com/reference/androidx/camera/view/CameraController#getZoomState())method returns a`LiveData`object for tracking changes to the[`ZoomState`](https://developer.android.com/reference/androidx/camera/core/ZoomState)on the`CameraController`.  

```kotlin
// CameraX: track the state of pinch-to-zoom over the Lifecycle of
// a PreviewView, logging the linear zoom ratio.

val pinchToZoomStateObserver = Observer { state ->
    val zoomRatio = state.getZoomRatio()
    Log.d(TAG, "ptz-zoom-ratio $zoomRatio")
}

cameraController.getZoomState().observe(this, pinchToZoomStateObserver)
```

#### CameraX: CameraProvider

To get pinch-to-zoom working with`CameraProvider`, some setup is required. If you're not using`PreviewView`, you need to adapt the logic to apply to your custom`Surface`.

Here are the steps when using`PreviewView`:

1. Set up a scale gesture detector to handle pinch events.
2. Get the`ZoomState`from the`Camera.CameraInfo`object, where the`Camera`instance is returned when you call[`bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...)).
3. If the`ZoomState`has a`zoomRatio`value, save that as the current zoom ratio. If there is no`zoomRatio`on`ZoomState`, then use the camera's default zoom rate (1.0).
4. Take the product of the current zoom ratio with the`scaleFactor`to determine the new zoom ratio, and pass that into`CameraControl.setZoomRatio()`.
5. Set your gesture detector to respond to touch events in`PreviewView.setOnTouchListener()`.

```kotlin
// CameraX: implement pinch-to-zoom with CameraProvider.

// Define a scale gesture detector to respond to pinch events and call
// setZoomRatio on CameraControl.
val scaleGestureDetector = ScaleGestureDetector(context,
    object : SimpleOnGestureListener() {
        override fun onScale(detector: ScaleGestureDetector): Boolean {
            val camera = camera ?: return
            val zoomState = camera.cameraInfo.zoomState
            val currentZoomRatio: Float = zoomState.value?.zoomRatio ?: 1f
            camera.cameraControl.setZoomRatio(
                detector.scaleFactor * currentZoomRatio
            )
        }
    }
)

...

// Set the scaleGestureDetector in a touch listener on the PreviewView.
previewView.setOnTouchListener { _, event ->
    var didConsume = scaleGestureDetector.onTouchEvent(event)
    if (!scaleGestureDetector.isInProgress) {
        // See pinch-to-zooom scenario for gestureDetector definition.
        didConsume = gestureDetector.onTouchEvent(event)
    }
    didConsume
}
```

### Taking a photo

This section shows how to trigger photo capture, whether you need to do it on a shutter button press, after a timer has elapsed, or on any other event of your choosing.

#### Camera1

In Camera1, you first define a[`Camera.PictureCallback`](https://developer.android.com/reference/android/hardware/Camera.PictureCallback)to manage the picture data when it's requested. Here's a simple example of`PictureCallback`for handling JPEG image data:  

```kotlin
// Camera1: define a Camera.PictureCallback to handle JPEG data.

private val picture = Camera.PictureCallback { data, _ ->
    val pictureFile: File = getOutputMediaFile(MEDIA_TYPE_IMAGE) ?: run {
        Log.d(TAG,
              "error creating media file, check storage permissions")
        return@PictureCallback
    }

    try {
        val fos = FileOutputStream(pictureFile)
        fos.write(data)
        fos.close()
    } catch (e: FileNotFoundException) {
        Log.d(TAG, "file not found", e)
    } catch (e: IOException) {
        Log.d(TAG, "error accessing file", e)
    }
}
```

Then, whenever you want to take a picture, you call the`takePicture()`method on your`Camera`instance. This`takePicture()`method has three different parameters for different data types. The first parameter is for a`ShutterCallback`(which isn't defined in this example). The second parameter is for a`PictureCallback`to handle the raw (uncompressed) camera data. The third parameter is the one this example uses, since it's a`PictureCallback`to handle JPEG image data.  

```kotlin
// Camera1: call takePicture on Camera instance, passing our PictureCallback.

camera?.takePicture(null, null, picture)
```

#### CameraX: CameraController

CameraX's`CameraController`maintains the simplicity of Camera1 for image capture by implementing a`takePicture()`method of its own. Here, define a function to configure a`MediaStore`entry and take a photo to be saved there.  

```kotlin
// CameraX: define a function that uses CameraController to take a photo.

private val FILENAME_FORMAT = "yyyy-MM-dd-HH-mm-ss-SSS"

private fun takePhoto() {
   // Create time stamped name and MediaStore entry.
   val name = SimpleDateFormat(FILENAME_FORMAT, Locale.US)
              .format(System.currentTimeMillis())
   val contentValues = ContentValues().apply {
       put(MediaStore.MediaColumns.DISPLAY_NAME, name)
       put(MediaStore.MediaColumns.MIME_TYPE, "image/jpeg")
       if(Build.VERSION.SDK_INT > Build.VERSION_CODES.P) {
           put(MediaStore.Images.Media.RELATIVE_PATH, "Pictures/CameraX-Image")
       }
   }

   // Create output options object which contains file + metadata.
   val outputOptions = ImageCapture.OutputFileOptions
       .Builder(context.getContentResolver(),
            MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)
       .build()

   // Set up image capture listener, which is triggered after photo has
   // been taken.
   cameraController.takePicture(
       outputOptions,
       ContextCompat.getMainExecutor(this),
       object : ImageCapture.OnImageSavedCallback {
           override fun onError(e: ImageCaptureException) {
               Log.e(TAG, "photo capture failed", e)
           }

           override fun onImageSaved(
               output: ImageCapture.OutputFileResults
           ) {
               val msg = "Photo capture succeeded: ${output.savedUri}"
               Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
               Log.d(TAG, msg)
           }
       }
   )
}
```

#### CameraX: CameraProvider

Taking a photo with`CameraProvider`works almost the exact same way as with`CameraController`, but you first need to create and bind an`ImageCapture``UseCase`to have an object to call`takePicture()`on:  

```kotlin
// CameraX: create and bind an ImageCapture UseCase.

// Make a reference to the ImageCapture UseCase at a scope that can be accessed
// throughout the camera logic in your app.
private var imageCapture: ImageCapture? = null

...

// Create an ImageCapture instance (can be added with other
// UseCase definitions).
imageCapture = ImageCapture.Builder().build()

...

// Bind UseCases to camera (adding imageCapture along with preview here, but
// preview is not required to use imageCapture). This function returns a camera
// object which can be used to perform operations like zoom, flash, and focus.
var camera = cameraProvider.bindToLifecycle(
    this, cameraSelector, preview, imageCapture)
```

Then, whenever you want to capture a photo, you can call`ImageCapture.takePicture()`. See the`CameraController`code in this section for a full example of the`takePhoto()`function.  

```kotlin
// CameraX: define a function that uses CameraController to take a photo.

private fun takePhoto() {
    // Get a stable reference of the modifiable ImageCapture UseCase.
    val imageCapture = imageCapture ?: return

    ...

    // Call takePicture on imageCapture instance.
    imageCapture.takePicture(
        ...
    )
}
```

### Recording a video

Recording a video is considerably more complicated than the scenarios looked at so far. Each part of the process must be set up properly, usually in a particular order. Also, you might need to verify that the video and audio are in sync or deal with additional device inconsistencies.

As you'll see, CameraX again handles a lot of this complexity for you.

#### Camera1

Video capture using Camera1 requires careful management of the`Camera`and[`MediaRecorder`](https://developer.android.com/reference/android/media/MediaRecorder), and the methods must be called in a particular order. You**must**follow this order for your application to work properly:

1. Open the camera.
2. Prepare and start a preview (if your app shows the video being recorded, which is usually the case).
3. Unlock the camera for use by`MediaRecorder`by calling`Camera.unlock()`.
4. Configure the recording by calling these methods on`MediaRecorder`:
   1. Connect your`Camera`instance with`setCamera(camera)`.
   2. Call`setAudioSource(MediaRecorder.AudioSource.CAMCORDER)`.
   3. Call`setVideoSource(MediaRecorder.VideoSource.CAMERA)`.
   4. Call`setProfile(CamcorderProfile.get(CamcorderProfile.QUALITY_1080P))`to set the quality. See[`CamcorderProfile`](https://developer.android.com/reference/android/media/CamcorderProfile)for all of the quality options.
   5. Call`setOutputFile(getOutputMediaFile(MEDIA_TYPE_VIDEO).toString())`.
   6. If your app has a preview of the video, call`setPreviewDisplay(preview?.holder?.surface)`.
   7. Call`setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)`.
   8. Call`setAudioEncoder(MediaRecorder.AudioEncoder.DEFAULT)`.
   9. Call`setVideoEncoder(MediaRecorder.VideoEncoder.DEFAULT)`.
   10. Call`prepare()`to finalize the configuration of your`MediaRecorder`.
5. To start recording, call`MediaRecorder.start()`.
6. To stop recording, call these methods. Again, follow this exact order:
   1. Call`MediaRecorder.stop()`.
   2. Optionally, remove the current`MediaRecorder`configuration by calling`MediaRecorder.reset()`.
   3. Call`MediaRecorder.release()`.
   4. Lock the camera so that future`MediaRecorder`sessions can use it by calling`Camera.lock()`.
7. To stop the preview, call`Camera.stopPreview()`.
8. Finally, to release the`Camera`so other processes can use it, call`Camera.release()`.

Here are all of those steps combined:  

```kotlin
// Camera1: set up a MediaRecorder and a function to start and stop video
// recording.

// Make a reference to the MediaRecorder at a scope that can be accessed
// throughout the camera logic in your app.
private var mediaRecorder: MediaRecorder? = null
private var isRecording = false

...

private fun prepareMediaRecorder(): Boolean {
    mediaRecorder = MediaRecorder()

    // Unlock and set camera to MediaRecorder.
    camera?.unlock()

    mediaRecorder?.run {
        setCamera(camera)

        // Set the audio and video sources.
        setAudioSource(MediaRecorder.AudioSource.CAMCORDER)
        setVideoSource(MediaRecorder.VideoSource.CAMERA)

        // Set a CamcorderProfile (requires API Level 8 or higher).
        setProfile(CamcorderProfile.get(CamcorderProfile.QUALITY_HIGH))

        // Set the output file.
        setOutputFile(getOutputMediaFile(MEDIA_TYPE_VIDEO).toString())

        // Set the preview output.
        setPreviewDisplay(preview?.holder?.surface)

        setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
        setAudioEncoder(MediaRecorder.AudioEncoder.DEFAULT)
        setVideoEncoder(MediaRecorder.VideoEncoder.DEFAULT)

        // Prepare configured MediaRecorder.
        return try {
            prepare()
            true
        } catch (e: IllegalStateException) {
            Log.d(TAG, "preparing MediaRecorder failed", e)
            releaseMediaRecorder()
            false
        } catch (e: IOException) {
            Log.d(TAG, "setting MediaRecorder file failed", e)
            releaseMediaRecorder()
            false
        }
    }
    return false
}

private fun releaseMediaRecorder() {
    mediaRecorder?.reset()
    mediaRecorder?.release()
    mediaRecorder = null
    camera?.lock()
}

private fun startStopVideo() {
    if (isRecording) {
        // Stop recording and release camera.
        mediaRecorder?.stop()
        releaseMediaRecorder()
        camera?.lock()
        isRecording = false

        // This is a good place to inform user that video recording has stopped.
    } else {
        // Initialize video camera.
        if (prepareVideoRecorder()) {
            // Camera is available and unlocked, MediaRecorder is prepared, now
            // you can start recording.
            mediaRecorder?.start()
            isRecording = true

            // This is a good place to inform the user that recording has
            // started.
        } else {
            // Prepare didn't work, release the camera.
            releaseMediaRecorder()

            // Inform user here.
        }
    }
}
```

#### CameraX: CameraController

With CameraX's`CameraController`, you can toggle the`ImageCapture`,`VideoCapture`, and`ImageAnalysis``UseCase`s independently,[as long as the list of UseCases can be used concurrently](https://developer.android.com/training/camerax/architecture#combine-use-cases). The`ImageCapture`and`ImageAnalysis``UseCase`s are enabled by default, which is why you didn't need to call`setEnabledUseCases()`for taking a photo.

To use a`CameraController`for video recording, you first need to use`setEnabledUseCases()`to allow the`VideoCapture``UseCase`.  

```kotlin
// CameraX: Enable VideoCapture UseCase on CameraController.

cameraController.setEnabledUseCases(VIDEO_CAPTURE);
```

When you want to start recording video, you can call the[`CameraController.startRecording()`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:camera/camera-view/src/main/java/androidx/camera/view/CameraController.java;l=1132;drc=59727137d55ce3b0a2321b745ecc854b3409379b)function. This function can save the recorded video to a`File`, as you can see in the example below. Additionally, you need to pass an`Executor`and a class that implements[`OnVideoSavedCallback`](https://android.googlesource.com/platform/frameworks/support/+/f2e05c341382db64d127118a13451dcaa554b702/camera/camera-view/src/main/java/androidx/camera/view/video/OnVideoSavedCallback.java)to handle success and error callbacks. When the recording should end, call[`CameraController.stopRecording()`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:camera/camera-view/src/main/java/androidx/camera/view/CameraController.java;l=1164;drc=59727137d55ce3b0a2321b745ecc854b3409379b).

**Note:** If you're using CameraX 1.3.0-alpha02 or later, there is an additional[`AudioConfig`](https://developer.android.com/reference/androidx/camera/view/video/AudioConfig)parameter that allows you to enable or disable audio recording on your video. To enable audio recording, you need to ensure you have microphone permissions. Additionally, the`stopRecording()`method is removed in 1.3.0-alpha02, and`startRecording()`returns a`Recording`object that can be used for pausing, resuming, and stopping the video recording.  

```kotlin
// CameraX: implement video capture with CameraController.

private val FILENAME_FORMAT = "yyyy-MM-dd-HH-mm-ss-SSS"

// Define a VideoSaveCallback class for handling success and error states.
class VideoSaveCallback : OnVideoSavedCallback {
    override fun onVideoSaved(outputFileResults: OutputFileResults) {
        val msg = "Video capture succeeded: ${outputFileResults.savedUri}"
        Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
        Log.d(TAG, msg)
    }

    override fun onError(videoCaptureError: Int, message: String,
                         cause: Throwable?) {
        Log.d(TAG, "error saving video: $message", cause)
    }
}

private fun startStopVideo() {
    if (cameraController.isRecording()) {
        // Stop the current recording session.
        cameraController.stopRecording()
        return
    }

    // Define the File options for saving the video.
    val name = SimpleDateFormat(FILENAME_FORMAT, Locale.US)
        .format(System.currentTimeMillis())

    val outputFileOptions = OutputFileOptions
        .Builder(File(this.filesDir, name))
        .build()

    // Call startRecording on the CameraController.
    cameraController.startRecording(
        outputFileOptions,
        ContextCompat.getMainExecutor(this),
        VideoSaveCallback()
    )
}
```

#### CameraX: CameraProvider

If you're using a`CameraProvider`, you need to create a`VideoCapture``UseCase`and pass in a`Recorder`object. On the`Recorder.Builder`, you can set the video quality and, optionally, a[`FallbackStrategy`](https://developer.android.com/reference/androidx/camera/video/FallbackStrategy), which handles cases when a device can't meet your desired quality specifications. Then bind the`VideoCapture`instance to the`CameraProvider`with your other`UseCase`s.  

```kotlin
// CameraX: create and bind a VideoCapture UseCase with CameraProvider.

// Make a reference to the VideoCapture UseCase and Recording at a
// scope that can be accessed throughout the camera logic in your app.
private lateinit var videoCapture: VideoCapture
private var recording: Recording? = null

...

// Create a Recorder instance to set on a VideoCapture instance (can be
// added with other UseCase definitions).
val recorder = Recorder.Builder()
    .setQualitySelector(QualitySelector.from(Quality.FHD))
    .build()
videoCapture = VideoCapture.withOutput(recorder)

...

// Bind UseCases to camera (adding videoCapture along with preview here, but
// preview is not required to use videoCapture). This function returns a camera
// object which can be used to perform operations like zoom, flash, and focus.
var camera = cameraProvider.bindToLifecycle(
    this, cameraSelector, preview, videoCapture)
```

At this point, the`Recorder`can be accessed on the`videoCapture.output`property. The`Recorder`can start video recordings that are saved to a`File`,`ParcelFileDescriptor`, or`MediaStore`. This example uses`MediaStore`.

On the`Recorder`, there are several methods to call to prepare it. Call`prepareRecording()`to set the`MediaStore`output options. If your app has permission to use the device's microphone, call`withAudioEnabled()`as well. Then, call`start()`to begin recording, passing in a context and a`Consumer<VideoRecordEvent>`event listener to handle video record events. If successful, the returned`Recording`can be used to pause, resume, or stop the recording.  

```kotlin
// CameraX: implement video capture with CameraProvider.

private val FILENAME_FORMAT = "yyyy-MM-dd-HH-mm-ss-SSS"

private fun startStopVideo() {
   val videoCapture = this.videoCapture ?: return

   if (recording != null) {
       // Stop the current recording session.
       recording.stop()
       recording = null
       return
   }

   // Create and start a new recording session.
   val name = SimpleDateFormat(FILENAME_FORMAT, Locale.US)
       .format(System.currentTimeMillis())
   val contentValues = ContentValues().apply {
       put(MediaStore.MediaColumns.DISPLAY_NAME, name)
       put(MediaStore.MediaColumns.MIME_TYPE, "video/mp4")
       if (Build.VERSION.SDK_INT > Build.VERSION_CODES.P) {
           put(MediaStore.Video.Media.RELATIVE_PATH, "Movies/CameraX-Video")
       }
   }

   val mediaStoreOutputOptions = MediaStoreOutputOptions
       .Builder(contentResolver, MediaStore.Video.Media.EXTERNAL_CONTENT_URI)
       .setContentValues(contentValues)
       .build()

   recording = videoCapture.output
       .prepareRecording(this, mediaStoreOutputOptions)
       .withAudioEnabled()
       .start(ContextCompat.getMainExecutor(this)) { recordEvent ->
           when(recordEvent) {
               is VideoRecordEvent.Start -> {
                   viewBinding.videoCaptureButton.apply {
                       text = getString(R.string.stop_capture)
                       isEnabled = true
                   }
               }
               is VideoRecordEvent.Finalize -> {
                   if (!recordEvent.hasError()) {
                       val msg = "Video capture succeeded: " +
                           "${recordEvent.outputResults.outputUri}"
                       Toast.makeText(
                           baseContext, msg, Toast.LENGTH_SHORT
                       ).show()
                       Log.d(TAG, msg)
                   } else {
                       recording?.close()
                       recording = null
                       Log.e(TAG, "video capture ends with error",
                             recordEvent.error)
                   }
                   viewBinding.videoCaptureButton.apply {
                       text = getString(R.string.start_capture)
                       isEnabled = true
                   }
               }
           }
       }
}
```

## Additional resources

We have several complete CameraX apps in our[Camera Samples GitHub Repository](https://github.com/android/camera-samples). These samples show you how the scenarios in this guide fit into a fully-fledged Android app.

If you'd like additional support in migrating to CameraX or have questions regarding the suite of Android Camera APIs, please reach out to us on the[CameraX Discussion Group](https://groups.google.com/a/android.com/g/camerax-developers).