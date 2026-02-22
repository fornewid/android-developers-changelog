---
title: https://developer.android.com/media/camera/camerax/architecture
url: https://developer.android.com/media/camera/camerax/architecture
source: md.txt
---

This page covers the architecture of CameraX, including its structure, how to work with the API, how to work with lifecycles, and how to combine use cases.

## CameraX structure

You can use CameraX to interface with a device's camera through an
abstraction called a use case. The following use cases are available:

- **Preview** : accepts a surface for displaying a preview, such as a `PreviewView`.
- **Image analysis**: provides CPU-accessible buffers for analysis, such as for machine learning.
- **Image capture**: captures and saves a photo.
- **Video capture** : capture video and audio with [`VideoCapture`](https://developer.android.com/reference/androidx/camera/video/VideoCapture)

Use cases can be combined and active concurrently. For example, an app can let
the user view the image that the camera sees using a preview use case, have an
image analysis use case that determines whether the people in the photo are
smiling, and include an image capture use case to take a picture once they are.

## API model

To work with the library, you specify the following things:

- The desired use case with configuration options.
- What to do with output data by attaching listeners.
- The intended flow, such as when to enable cameras and when to produce data, by binding the use case to [Android Architecture
  Lifecycles](https://developer.android.com/topic/libraries/architecture).

There are 2 ways to write a CameraX app: a
[`CameraController`](https://developer.android.com/reference/androidx/camera/view/CameraController) (great if
you want the simplest way to use CameraX) or a
[`CameraProvider`](https://developer.android.com/reference/androidx/camera/core/CameraProvider) (great if you
need more flexibility).

### CameraController

A `CameraController` provides most of the CameraX core functionality in a single
class. It requires little setup code, and it automatically handles camera
initialization, use case management, target rotation, tap-to-focus,
pinch-to-zoom, and more. The concrete class that extends `CameraController` is
[`LifecycleCameraController`](https://developer.android.com/reference/androidx/camera/view/LifecycleCameraController).

### Kotlin

```kotlin
val previewView: PreviewView = viewBinding.previewView
var cameraController = LifecycleCameraController(baseContext)
cameraController.bindToLifecycle(this)
cameraController.cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
previewView.controller = cameraController
```

### Java

```java
PreviewView previewView = viewBinding.previewView;
LifecycleCameraController cameraController = new LifecycleCameraController(baseContext);
cameraController.bindToLifecycle(this);
cameraController.setCameraSelector(CameraSelector.DEFAULT_BACK_CAMERA);
previewView.setController(cameraController);
```

The default `UseCase`s for `CameraController` are `Preview`, `ImageCapture`, and
`ImageAnalysis`. To turn `ImageCapture` or `ImageAnalysis` off, or to turn
`VideoCapture` on, use the
[`setEnabledUseCases()`](https://developer.android.com/reference/androidx/camera/view/CameraController#setEnabledUseCases(int))
method.

For more uses of `CameraController`, see the
[QR Code scanner sample](https://github.com/android/camera-samples/tree/main/CameraX-MLKit)
or the
[`CameraController` basics video](https://www.youtube.com/watch?v=fazzQs-O31U).

### CameraProvider

A `CameraProvider` is still easy-to-use, but since the app developer handles
more of the setup, there are more opportunities to customize the configuration,
like enabling output image rotation or setting the output image format in
`ImageAnalysis`. You can also use a custom `Surface` for camera preview allows
for more flexibility, whereas with CameraController you are required to use a
`PreviewView`. Using your existing `Surface` code could be useful if it's
already an input to other parts of your app.

You configure use cases using `set()` methods and finalize them with the `build()`
method. Each use case object provides a set of use case-specific APIs. For
example, the image capture use case provides a `takePicture()` method call.

Instead of an application placing specific start and stop method calls in
`onResume()` and `onPause()`, the application specifies a lifecycle to associate
the camera with, using
[`cameraProvider.bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...)).
That lifecycle then informs CameraX when to configure the camera capture session
and ensures camera state changes appropriately to match lifecycle transitions.

For implementation steps for each use case, see [Implement a
preview](https://developer.android.com/training/camerax/preview), [Analyze
images](https://developer.android.com/training/camerax/analyze), [Image
capture](https://developer.android.com/training/camerax/take-photo), and [Video capture](https://developer.android.com/training/camerax/video-capture)

The preview use case interacts with a
[`Surface`](https://developer.android.com/reference/android/view/Surface) for display. Applications
create the use case with configuration options using the following code:

### Kotlin

```kotlin
val preview = Preview.Builder().build()
val viewFinder: PreviewView = findViewById(R.id.previewView)

// The use case is bound to an Android Lifecycle with the following code
val camera = cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview)

// PreviewView creates a surface provider and is the recommended provider
preview.setSurfaceProvider(viewFinder.getSurfaceProvider())
```

### Java

```java
Preview preview = new Preview.Builder().build();
PreviewView viewFinder = findViewById(R.id.view_finder);

// The use case is bound to an Android Lifecycle with the following code
Camera camera = cameraProvider.bindToLifecycle(lifecycleOwner, cameraSelector, preview);

// PreviewView creates a surface provider, using a Surface from a different
// kind of view will require you to implement your own surface provider.
preview.previewSurfaceProvider = viewFinder.getSurfaceProvider();
```

For more example code, see the [official CameraX sample
app](https://github.com/android/camera-samples/tree/main/CameraXBasic).

## CameraX Lifecycles

CameraX observes a lifecycle to determine when to open the camera, when to
create a capture session, and when to stop and shut down. Use case APIs provide
method calls and callbacks to monitor progress.

As explained in [Combine use cases](https://developer.android.com/media/camera/camerax/architecture#combine-use-cases), you can bind some mixes of
use cases to a single lifecycle. When your app needs to support use cases that
can't be combined, you can do one of the following:

- Group compatible use cases together into more than one [fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment) and then switch between fragments
- Create a custom lifecycle component and use it to manually control the camera lifecycle

If you decouple your view and camera use cases' Lifecycle owners (for example,
if you use a custom lifecycle or a [retain
fragment](https://developer.android.com/reference/android/app/Fragment#setRetainInstance(boolean))), then you
must ensure that all use cases are unbound from CameraX by using
[`ProcessCameraProvider.unbindAll()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#unbindAll())
or by unbinding each use case individually. Alternatively, when you bind use
cases to a Lifecycle, you can let CameraX
manage opening and closing the capture session and unbinding the use cases.

If all of your camera functionality corresponds to the lifecycle of a single
lifecycle-aware component such as an
[`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity) or an
`AppCompat` fragment, then using the lifecycle of that component when binding
all the desired use cases will ensure that the camera functionality is ready
when the lifecycle-aware component is active, and safely disposed of, not
consuming any resources, otherwise.

## Custom LifecycleOwners

For advanced cases, you can create a custom
[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner) to enable your
app to explicitly control the CameraX session lifecycle instead of tying it to a
standard Android `LifecycleOwner`.

The following code sample shows how to create a simple custom LifecycleOwner:

### Kotlin

```kotlin
class CustomLifecycle : LifecycleOwner {
    private val lifecycleRegistry: LifecycleRegistry

    init {
        lifecycleRegistry = LifecycleRegistry(this);
        lifecycleRegistry.markState(Lifecycle.State.CREATED)
    }
    ...
    fun doOnResume() {
        lifecycleRegistry.markState(State.RESUMED)
    }
    ...
    override fun getLifecycle(): Lifecycle {
        return lifecycleRegistry
    }
}
```

### Java

```java
public class CustomLifecycle implements LifecycleOwner {
    private LifecycleRegistry lifecycleRegistry;
    public CustomLifecycle() {
        lifecycleRegistry = new LifecycleRegistry(this);
        lifecycleRegistry.markState(Lifecycle.State.CREATED);
    }
   ...
   public void doOnResume() {
        lifecycleRegistry.markState(State.RESUMED);
    }
   ...
    public Lifecycle getLifecycle() {
        return lifecycleRegistry;
    }
}
```

Using this `LifecycleOwner`, your app can place state transitions at desired
points in its code. For more on implementing this functionality in your app,
see [Implementing a custom
LifecycleOwner](https://developer.android.com/topic/libraries/architecture/lifecycle#implementing-lco).

## Concurrent use cases

Use cases can run concurrently. While use cases can be sequentially bound to a
lifecycle, it is better to bind all use cases with a single call to
`CameraProcessProvider.bindToLifecycle()`. For more information on best
practices for configuration changes, see [Handle configuration
changes](https://developer.android.com/guide/topics/resources/runtime-changes).

In the following code sample, the app specifies the two use cases to be created
and run simultaneously. It also specifies the lifecycle to use for both use
cases, so that they both start and stop according to the lifecycle.

### Kotlin

```kotlin
private lateinit var imageCapture: ImageCapture

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)

    val cameraProviderFuture = ProcessCameraProvider.getInstance(this)

    cameraProviderFuture.addListener(Runnable {
        // Camera provider is now guaranteed to be available
        val cameraProvider = cameraProviderFuture.get()

        // Set up the preview use case to display camera preview.
        val preview = Preview.Builder().build()

        // Set up the capture use case to allow users to take photos.
        imageCapture = ImageCapture.Builder()
                .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
                .build()

        // Choose the camera by requiring a lens facing
        val cameraSelector = CameraSelector.Builder()
                .requireLensFacing(CameraSelector.LENS_FACING_FRONT)
                .build()

        // Attach use cases to the camera with the same lifecycle owner
        val camera = cameraProvider.bindToLifecycle(
                this as LifecycleOwner, cameraSelector, preview, imageCapture)

        // Connect the preview use case to the previewView
        preview.setSurfaceProvider(
                previewView.getSurfaceProvider())
    }, ContextCompat.getMainExecutor(this))
}
```

### Java

```java
private ImageCapture imageCapture;

@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    PreviewView previewView = findViewById(R.id.previewView);

    ListenableFuture<ProcessCameraProvider> cameraProviderFuture =
            ProcessCameraProvider.getInstance(this);

    cameraProviderFuture.addListener(() -> {
        try {
            // Camera provider is now guaranteed to be available
            ProcessCameraProvider cameraProvider = cameraProviderFuture.get();

            // Set up the view finder use case to display camera preview
            Preview preview = new Preview.Builder().build();

            // Set up the capture use case to allow users to take photos
            imageCapture = new ImageCapture.Builder()
                    .setCaptureMode(ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY)
                    .build();

            // Choose the camera by requiring a lens facing
            CameraSelector cameraSelector = new CameraSelector.Builder()
                    .requireLensFacing(lensFacing)
                    .build();

            // Attach use cases to the camera with the same lifecycle owner
            Camera camera = cameraProvider.bindToLifecycle(
                    ((LifecycleOwner) this),
                    cameraSelector,
                    preview,
                    imageCapture);

            // Connect the preview use case to the previewView
            preview.setSurfaceProvider(
                    previewView.getSurfaceProvider());
        } catch (InterruptedException | ExecutionException e) {
            // Currently no exceptions thrown. cameraProviderFuture.get()
            // shouldn't block since the listener is being called, so no need to
            // handle InterruptedException.
        }
    }, ContextCompat.getMainExecutor(this));
}
```

CameraX allows simultaneous use of one instance each of `Preview`,
`VideoCapture`, `ImageAnalysis`, and `ImageCapture`. Additionally,

- Every use case can work on its own. For example, an app can record video without using preview.
- When extensions are enabled, only the `ImageCapture` and `Preview` combination is guaranteed to work. Depending on OEM implementation, it may not be possible to also add `ImageAnalysis`; extensions can not be enabled for the `VideoCapture` use case. Check the [Extension reference doc](https://developer.android.com/reference/androidx/camera/extensions/ExtensionsManager) for details.
- Depending on camera capability, some cameras may support the combination at lower resolution modes, but can not support the same combination at some higher resolutions.
- On devices with camera hardware level `FULL` or lower, combining `Preview`, `VideoCapture`, and either `ImageCapture` or `ImageAnalysis` may force CameraX to duplicate the camera's `PRIV` stream for `Preview` and `VideoCapture`. This duplication, called stream sharing, enables the simultaneous use of these features but comes at the cost of increased processing demands. You might experience slightly higher latency and reduced battery life as a result.

The [supported hardware level](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL)
can be retrieved from `Camera2CameraInfo`. For example, the following code
checks whether the default back facing camera is a `LEVEL_3` device:

### Kotlin

```kotlin
@androidx.annotation.OptIn(ExperimentalCamera2Interop::class)
fun isBackCameraLevel3Device(cameraProvider: ProcessCameraProvider) : Boolean {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        return CameraSelector.DEFAULT_BACK_CAMERA
            .filter(cameraProvider.availableCameraInfos)
            .firstOrNull()
            ?.let { Camera2CameraInfo.from(it) }
            ?.getCameraCharacteristic(CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL) ==
            CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_3
    }
    return false
}
```

### Java

```java
@androidx.annotation.OptIn(markerClass = ExperimentalCamera2Interop.class)
Boolean isBackCameraLevel3Device(ProcessCameraProvider cameraProvider) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        List\<CameraInfo\> filteredCameraInfos = CameraSelector.DEFAULT_BACK_CAMERA
                .filter(cameraProvider.getAvailableCameraInfos());
        if (!filteredCameraInfos.isEmpty()) {
            return Objects.equals(
                Camera2CameraInfo.from(filteredCameraInfos.get(0)).getCameraCharacteristic(
                        CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL),
                CameraCharacteristics.INFO_SUPPORTED_HARDWARE_LEVEL_3);
        }
    }
    return false;
}
```
| **Note:** If an incompatible combination of use cases is created, a runtime error is thrown the first time [`createCaptureSession()`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(android.hardware.camera2.params.SessionConfiguration)) is called. If additional use cases are added to the running session, a reconfiguration may be required, potentially causing a visible glitch.

## Permissions

Your app will need the
[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) permission. To
save images to files, it will also require the
[`WRITE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)
permission, except on devices running Android 10 or later.

For more information about configuring permissions for your app, read [Request
App Permissions](https://developer.android.com/training/permissions/requesting).

## Requirements

CameraX has the following minimum version requirements:

- Android API level 21
- Android Architecture Components 1.1.1

For lifecycle-aware activities, use
[`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity) or
[`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity).

## Declare dependencies

To add a dependency on CameraX, you must add the [Google Maven
repository](https://developer.android.com/studio/build/dependencies#google-maven) to your project.

Open the `settings.gradle` file for your project and add the `google()` repository
as shown in the following:

### Groovy

```groovy
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
```

### Kotlin

```kotlin
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
```

Add the following to the end of the Android block:

### Groovy

```groovy
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    // For Kotlin projects
    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
android {
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    // For Kotlin projects
    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

Add the following to each module's `build.gradle` file for an app:

### Groovy

```groovy
dependencies {
  // CameraX core library using the camera2 implementation
  def camerax_version = "1.6.0-beta02"
  // The following line is optional, as the core library is included indirectly by camera-camera2
  implementation "androidx.camera:camera-core:${camerax_version}"
  implementation "androidx.camera:camera-camera2:${camerax_version}"
  // If you want to additionally use the CameraX Lifecycle library
  implementation "androidx.camera:camera-lifecycle:${camerax_version}"
  // If you want to additionally use the CameraX VideoCapture library
  implementation "androidx.camera:camera-video:${camerax_version}"
  // If you want to additionally use the CameraX View class
  implementation "androidx.camera:camera-view:${camerax_version}"
  // If you want to additionally add CameraX ML Kit Vision Integration
  implementation "androidx.camera:camera-mlkit-vision:${camerax_version}"
  // If you want to additionally use the CameraX Extensions library
  implementation "androidx.camera:camera-extensions:${camerax_version}"
}
```

### Kotlin

```kotlin
dependencies {
    // CameraX core library using the camera2 implementation
    val camerax_version = "1.6.0-beta02"
    // The following line is optional, as the core library is included indirectly by camera-camera2
    implementation("androidx.camera:camera-core:${camerax_version}")
    implementation("androidx.camera:camera-camera2:${camerax_version}")
    // If you want to additionally use the CameraX Lifecycle library
    implementation("androidx.camera:camera-lifecycle:${camerax_version}")
    // If you want to additionally use the CameraX VideoCapture library
    implementation("androidx.camera:camera-video:${camerax_version}")
    // If you want to additionally use the CameraX View class
    implementation("androidx.camera:camera-view:${camerax_version}")
    // If you want to additionally add CameraX ML Kit Vision Integration
    implementation("androidx.camera:camera-mlkit-vision:${camerax_version}")
    // If you want to additionally use the CameraX Extensions library
    implementation("androidx.camera:camera-extensions:${camerax_version}")
}
```

For more information on configuring your app to conform to these requirements,
see [Declaring
dependencies](https://developer.android.com/jetpack/androidx/releases/lifecycle#declaring_dependencies).

## CameraX interoperability with Camera2

CameraX is built on Camera2, and CameraX exposes ways to read and even write
properties in the Camera2 implementation. For full details, see the
[Interop package](https://developer.android.com/reference/androidx/camera/camera2/interop/package-summary).

For more information about how CameraX has configured Camera2 properties, use
[`Camera2CameraInfo`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraInfo)
to read the underlying [`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics). You can also choose to write the underlying Camera2
properties in one of the following two pathways:

- Use [`Camera2CameraControl`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraControl),
  which lets you set properties on the underlying
  [`CaptureRequest`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest),
  such as the auto-focus mode.

- Extend a CameraX [`UseCase`](https://developer.android.com/reference/androidx/camera/core/UseCase) with a
  [`Camera2Interop.Extender`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2Interop.Extender).
  This lets you set properties on the CaptureRequest, just like
  [`Camera2CameraControl`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraControl).
  It also gives you some additional controls, like setting the stream use case to
  optimize the camera for your usage scenario. For information, see [Use Stream Use Cases for better
  performance](https://developer.android.com/training/camera2/capture-sessions-requests#use-stream-use-case-for-better-performance).

| **Note:** Setting the underlying Camera2 properties is marked "Experimental" in CameraX because Google expects developers to understand its use. The values you set override any values that CameraX sets. We only recommend doing this when absolutely necessary, and we recommend additional testing on your end.

The following code sample uses stream use cases to optimize for a video call.
Use [`Camera2CameraInfo`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2CameraInfo)
to fetch whether the video call stream use case is available. Then, use a
[`Camera2Interop.Extender`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2Interop.Extender)
to set the underlying stream use case.

### Kotlin

```kotlin
// Set underlying Camera2 stream use case to optimize for video calls.

val videoCallStreamId =
    CameraMetadata.SCALER_AVAILABLE_STREAM_USE_CASES_VIDEO_CALL.toLong()

// Check available CameraInfos to find the first one that supports
// the video call stream use case.
val frontCameraInfo = cameraProvider.getAvailableCameraInfos()
    .first { cameraInfo ->
        val isVideoCallStreamingSupported = Camera2CameraInfo.from(cameraInfo)
            .getCameraCharacteristic(
                CameraCharacteristics.SCALER_AVAILABLE_STREAM_USE_CASES
            )?.contains(videoCallStreamId)
        val isFrontFacing = (cameraInfo.getLensFacing() == 
                             CameraSelector.LENS_FACING_FRONT)
        (isVideoCallStreamingSupported == true) && isFrontFacing
    }

val cameraSelector = frontCameraInfo.cameraSelector

// Start with a Preview Builder.
val previewBuilder = Preview.Builder()
    .setTargetAspectRatio(screenAspectRatio)
    .setTargetRotation(rotation)

// Use Camera2Interop.Extender to set the video call stream use case.
Camera2Interop.Extender(previewBuilder).setStreamUseCase(videoCallStreamId)

// Bind the Preview UseCase and the corresponding CameraSelector.
val preview = previewBuilder.build()
camera = cameraProvider.bindToLifecycle(this, cameraSelector, preview)
```

### Java

```java
// Set underlying Camera2 stream use case to optimize for video calls.

Long videoCallStreamId =
    CameraMetadata.SCALER_AVAILABLE_STREAM_USE_CASES_VIDEO_CALL.toLong();

// Check available CameraInfos to find the first one that supports
// the video call stream use case.
List<CameraInfo> cameraInfos = cameraProvider.getAvailableCameraInfos();
CameraInfo frontCameraInfo = null;
for (cameraInfo in cameraInfos) {
    Long[] availableStreamUseCases = Camera2CameraInfo.from(cameraInfo)
        .getCameraCharacteristic(
            CameraCharacteristics.SCALER_AVAILABLE_STREAM_USE_CASES
        );
    boolean isVideoCallStreamingSupported = Arrays.List(availableStreamUseCases)
                .contains(videoCallStreamId);
    boolean isFrontFacing = (cameraInfo.getLensFacing() ==
                             CameraSelector.LENS_FACING_FRONT);

    if (isVideoCallStreamingSupported && isFrontFacing) {
        frontCameraInfo = cameraInfo;
    }
}

if (frontCameraInfo == null) {
    // Handle case where video call streaming is not supported.
}

CameraSelector cameraSelector = frontCameraInfo.getCameraSelector();

// Start with a Preview Builder.
Preview.Builder previewBuilder = Preview.Builder()
    .setTargetAspectRatio(screenAspectRatio)
    .setTargetRotation(rotation);

// Use Camera2Interop.Extender to set the video call stream use case.
Camera2Interop.Extender(previewBuilder).setStreamUseCase(videoCallStreamId);

// Bind the Preview UseCase and the corresponding CameraSelector.
Preview preview = previewBuilder.build()
Camera camera = cameraProvider.bindToLifecycle(this, cameraSelector, preview)
```

## Additional resources

To learn more about CameraX, consult the following additional resources.

### Codelab


- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- 
- [CameraX sample apps](https://github.com/android/camera-samples/)