---
title: https://developer.android.com/media/camera/camera2/multi-camera
url: https://developer.android.com/media/camera/camera2/multi-camera
source: md.txt
---

# Multi-camera API

<br />

**Note:** This page refers to the[Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary)package. Unless your app requires specific, low-level features from Camera2, we recommend using[CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

Multi-camera was introduced with Android 9 (API level 28). Since its release, devices have come to market that support the API. Many multi-camera use cases are tightly coupled with a specific hardware configuration. In other words, not all use cases are compatible with every device,  which makes multi-camera features a good candidate for[Play Feature Delivery](https://developer.android.com/guide/app-bundle/play-feature-delivery).

Some typical use cases include:

- **Zoom**: switching between cameras depending on crop region or desired focal length.
- **Depth**: using multiple cameras to build a depth map.
- **Bokeh**: using inferred depth information to simulate a DSLR-like narrow focus range.

## The difference between logical and physical cameras

Understanding the multi-camera API requires understanding the difference between logical and physical cameras. For reference, consider a device with three back-facing cameras. In this example, each of the three back cameras is considered a physical camera. A logical camera is then a grouping of two or more of those physical cameras. The output of the logical camera can be a stream that comes from one of the underlying physical cameras, or a fused stream coming from more than one underlying physical camera simultaneously. Either way, the stream is handled by the camera Hardware Abstraction Layer (HAL).

Many phone manufacturers develop first-party camera applications, which usually come pre-installed on their devices. To use all of the hardware's capabilities, they may use private or hidden APIs or receive special treatment from the driver implementation that other applications do not have access to. Some devices implement the concept of logical cameras by providing a fused stream of frames from the different physical cameras, but only to certain privileged applications. Often, only one of the physical cameras is exposed to the framework. The situation for third-party developers prior to Android 9 is illustrated in the following diagram:
![](https://developer.android.com/static/images/training/camera/camera2/multi-camera-1.png)**Figure 1.**Camera capabilities typically only available to privileged applications

Beginning with Android 9, private APIs are no longer allowed in Android apps. With the inclusion of multi-camera support in the framework, Android best practices strongly recommend that phone manufacturers expose a logical camera for all physical cameras facing the same direction. The following is what third-party developers should expect to see on devices running Android 9 and higher:
![](https://developer.android.com/static/images/training/camera/camera2/multi-camera-2.png)**Figure 2.**Full developer access to all camera devices starting in Android 9

What the logical camera provides is entirely dependent on the OEM implementation of the Camera HAL. For example, a device like Pixel 3 implements its logical camera in such a way that it chooses one of its physical cameras based on the requested focal length and crop region.

## The multi-camera API

The new API adds the following new constants, classes, and methods:

- [`CameraMetadata.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA)
- [`CameraCharacteristics.getPhysicalCameraIds()`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#getPhysicalCameraIds())
- [`CameraCharacteristics.getAvailablePhysicalCameraRequestKeys()`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#getAvailablePhysicalCameraRequestKeys())
- [`CameraDevice.createCaptureSession(SessionConfiguration config)`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(android.hardware.camera2.params.SessionConfiguration))
- [`CameraCharacteritics.LOGICAL_MULTI_CAMERA_SENSOR_SYNC_TYPE`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#LOGICAL_MULTI_CAMERA_SENSOR_SYNC_TYPE)
- [`OutputConfiguration`](https://developer.android.com/reference/android/hardware/camera2/params/OutputConfiguration)and[`SessionConfiguration`](https://developer.android.com/reference/android/hardware/camera2/params/SessionConfiguration)

Due to changes to the Android Compatibility Definition Document (CDD), the multi-camera API also comes with certain expectations from developers. Devices with dual cameras existed prior to Android 9, but opening more than one camera simultaneously involved trial and error. On Android 9 and higher, multi-camera gives a set of rules to specify when it is possible to open a pair of physical cameras that are part of the same logical camera.

In most cases, devices running Android 9 and higher expose all physical cameras (except possibly for less-common sensor types like infrared) along with an easier-to-use logical camera. For every combination of streams that are guaranteed to work, one stream belonging to a logical camera can be replaced by two streams from the underlying physical cameras.

## Multiple streams simultaneously

[Using multiple camera streams simultaneously](https://developer.android.com/media/camera/camera2/multiple-camera-streams-simultaneously)covers the rules for using multiple streams simultaneously in a single camera. With one notable addition, the same rules apply for multiple cameras.[`CameraMetadata.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA)explains how to replace a logical YUV_420_888 or raw stream with two physical streams. That is, each stream of type YUV or RAW can be replaced with two streams of identical type and size. You can start with a camera stream of the following guaranteed configuration for single-camera devices:

- Stream 1: YUV type,`MAXIMUM`size from logical camera`id = 0`

Then, a device with multi-camera support allows you to create a session replacing that logical YUV stream with two physical streams:

- Stream 1: YUV type,`MAXIMUM`size from physical camera`id = 1`
- Stream 2: YUV type,`MAXIMUM`size from physical camera`id = 2`

You can replace a YUV or RAW stream with two equivalent streams if and only if those two cameras are part of a logical camera grouping,  which is listed under[`CameraCharacteristics.getPhysicalCameraIds()`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#getPhysicalCameraIds()).

The guarantees provided by the framework are just the bare minimum required to get frames from more than one physical camera simultaneously. Additional streams are supported in most devices, sometimes even allowing opening multiple physical camera devices independently. Since it's not a hard guarantee from the framework, doing that requires performing per-device testing and tuning using trial and error.

## Creating a session with multiple physical cameras

When using physical cameras on a multi-camera enabled device, open a single`CameraDevice`(the logical camera) and interact with it within a single session. Create the single session using the API`CameraDevice.createCaptureSession(SessionConfiguration config)`, which was added in API level 28. The session configuration has a number of output configurations, each of which has a set of output targets and, optionally, a desired physical camera ID.
![](https://developer.android.com/static/images/training/camera/camera2/multi-camera-3.png)**Figure 3.**SessionConfiguration and OutputConfiguration model

Capture requests have an output target associated with them. The framework determines which physical (or logical) camera the requests are sent to based on what output target is attached. If the output target corresponds to one of the output targets that was sent as an output configuration along with a physical camera ID, then that physical camera receives and processes the request.

## Using a pair of physical cameras

Another addition to the camera APIs for multi-camera is the ability to identify logical cameras and find the physical cameras behind them. You can define a function to help identify potential pairs of physical cameras that you can use to replace one of the logical camera streams:  

### Kotlin

```kotlin
/**
     * Helper class used to encapsulate a logical camera and two underlying
     * physical cameras
     */
    data class DualCamera(val logicalId: String, val physicalId1: String, val physicalId2: String)

    fun findDualCameras(manager: CameraManager, facing: Int? = null): List {
        val dualCameras = MutableList()

        // Iterate over all the available camera characteristics
        manager.cameraIdList.map {
            Pair(manager.getCameraCharacteristics(it), it)
        }.filter {
            // Filter by cameras facing the requested direction
            facing == null || it.first.get(CameraCharacteristics.LENS_FACING) == facing
        }.filter {
            // Filter by logical cameras
            // CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA requires API >= 28
            it.first.get(CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES)!!.contains(
                CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA)
        }.forEach {
            // All possible pairs from the list of physical cameras are valid results
            // NOTE: There could be N physical cameras as part of a logical camera grouping
            // getPhysicalCameraIds() requires API >= 28
            val physicalCameras = it.first.physicalCameraIds.toTypedArray()
            for (idx1 in 0 until physicalCameras.size) {
                for (idx2 in (idx1 + 1) until physicalCameras.size) {
                    dualCameras.add(DualCamera(
                        it.second, physicalCameras[idx1], physicalCameras[idx2]))
                }
            }
        }

        return dualCameras
    }
```

### Java

```java
/**
     * Helper class used to encapsulate a logical camera and two underlying
     * physical cameras
     */
    final class DualCamera {
        final String logicalId;
        final String physicalId1;
        final String physicalId2;

        DualCamera(String logicalId, String physicalId1, String physicalId2) {
            this.logicalId = logicalId;
            this.physicalId1 = physicalId1;
            this.physicalId2 = physicalId2;
        }
    }
    List findDualCameras(CameraManager manager, Integer facing) {
        List dualCameras = new ArrayList<>();

        List cameraIdList;
        try {
            cameraIdList = Arrays.asList(manager.getCameraIdList());
        } catch (CameraAccessException e) {
            e.printStackTrace();
            cameraIdList = new ArrayList<>();
        }

        // Iterate over all the available camera characteristics
        cameraIdList.stream()
                .map(id -> {
                    try {
                        CameraCharacteristics characteristics = manager.getCameraCharacteristics(id);
                        return new Pair<>(characteristics, id);
                    } catch (CameraAccessException e) {
                        e.printStackTrace();
                        return null;
                    }
                })
                .filter(pair -> {
                    // Filter by cameras facing the requested direction
                    return (pair != null) &&
                            (facing == null || pair.first.get(CameraCharacteristics.LENS_FACING).equals(facing));
                })
                .filter(pair -> {
                    // Filter by logical cameras
                    // CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA requires API >= 28
                    IntPredicate logicalMultiCameraPred =
                            arg -> arg == CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES_LOGICAL_MULTI_CAMERA;
                    return Arrays.stream(pair.first.get(CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES))
                            .anyMatch(logicalMultiCameraPred);
                })
                .forEach(pair -> {
                    // All possible pairs from the list of physical cameras are valid results
                    // NOTE: There could be N physical cameras as part of a logical camera grouping
                    // getPhysicalCameraIds() requires API >= 28
                    String[] physicalCameras = pair.first.getPhysicalCameraIds().toArray(new String[0]);
                    for (int idx1 = 0; idx1 < physicalCameras.length; idx1++) {
                        for (int idx2 = idx1 + 1; idx2 < physicalCameras.length; idx2++) {
                            dualCameras.add(
                                    new DualCamera(pair.second, physicalCameras[idx1], physicalCameras[idx2]));
                        }
                    }
                });
return dualCameras;
}
```

State handling of the physical cameras is controlled by the logical camera. To open a "dual camera," open the logical camera corresponding to the physical cameras:  

### Kotlin

```kotlin
fun openDualCamera(cameraManager: CameraManager,
                       dualCamera: DualCamera,
        // AsyncTask is deprecated beginning API 30
                       executor: Executor = AsyncTask.SERIAL_EXECUTOR,
                       callback: (CameraDevice) -> Unit) {

        // openCamera() requires API >= 28
        cameraManager.openCamera(
            dualCamera.logicalId, executor, object : CameraDevice.StateCallback() {
                override fun onOpened(device: CameraDevice) = callback(device)
                // Omitting for brevity...
                override fun onError(device: CameraDevice, error: Int) = onDisconnected(device)
                override fun onDisconnected(device: CameraDevice) = device.close()
            })
    }
```

### Java

```java
void openDualCamera(CameraManager cameraManager,
                        DualCamera dualCamera,
                        Executor executor,
                        CameraDeviceCallback cameraDeviceCallback
    ) {

        // openCamera() requires API >= 28
        cameraManager.openCamera(dualCamera.logicalId, executor, new CameraDevice.StateCallback() {
            @Override
            public void onOpened(@NonNull CameraDevice cameraDevice) {
               cameraDeviceCallback.callback(cameraDevice);
            }

            @Override
            public void onDisconnected(@NonNull CameraDevice cameraDevice) {
                cameraDevice.close();
            }

            @Override
            public void onError(@NonNull CameraDevice cameraDevice, int i) {
                onDisconnected(cameraDevice);
            }
        });
    }
```

Besides selecting which camera to open, the process is the same as opening a camera in past Android versions. Creating a capture session using the new session configuration API tells the framework to associate certain targets with specific physical camera IDs:  

### Kotlin

```kotlin
/**
 * Helper type definition that encapsulates 3 sets of output targets:
 *
 *   1. Logical camera
 *   2. First physical camera
 *   3. Second physical camera
 */
typealias DualCameraOutputs =
        Triple<MutableList?, MutableList?, MutableList?>

fun createDualCameraSession(cameraManager: CameraManager,
                            dualCamera: DualCamera,
                            targets: DualCameraOutputs,
                            // AsyncTask is deprecated beginning API 30
                            executor: Executor = AsyncTask.SERIAL_EXECUTOR,
                            callback: (CameraCaptureSession) -> Unit) {

    // Create 3 sets of output configurations: one for the logical camera, and
    // one for each of the physical cameras.
    val outputConfigsLogical = targets.first?.map { OutputConfiguration(it) }
    val outputConfigsPhysical1 = targets.second?.map {
        OutputConfiguration(it).apply { setPhysicalCameraId(dualCamera.physicalId1) } }
    val outputConfigsPhysical2 = targets.third?.map {
        OutputConfiguration(it).apply { setPhysicalCameraId(dualCamera.physicalId2) } }

    // Put all the output configurations into a single flat array
    val outputConfigsAll = arrayOf(
        outputConfigsLogical, outputConfigsPhysical1, outputConfigsPhysical2)
        .filterNotNull().flatMap { it }

    // Instantiate a session configuration that can be used to create a session
    val sessionConfiguration = SessionConfiguration(
        SessionConfiguration.SESSION_REGULAR,
        outputConfigsAll, executor, object : CameraCaptureSession.StateCallback() {
            override fun onConfigured(session: CameraCaptureSession) = callback(session)
            // Omitting for brevity...
            override fun onConfigureFailed(session: CameraCaptureSession) = session.device.close()
        })

    // Open the logical camera using the previously defined function
    openDualCamera(cameraManager, dualCamera, executor = executor) {

        // Finally create the session and return via callback
        it.createCaptureSession(sessionConfiguration)
    }
}
```

### Java

```java
/**
 * Helper class definition that encapsulates 3 sets of output targets:
 * 
 * 1. Logical camera
 * 2. First physical camera
 * 3. Second physical camera
 */
final class DualCameraOutputs {
    private final List logicalCamera;
    private final List firstPhysicalCamera;
    private final List secondPhysicalCamera;

    public DualCameraOutputs(List logicalCamera, List firstPhysicalCamera, List third) {
        this.logicalCamera = logicalCamera;
        this.firstPhysicalCamera = firstPhysicalCamera;
        this.secondPhysicalCamera = third;
    }

    public List getLogicalCamera() {
        return logicalCamera;
    }

    public List getFirstPhysicalCamera() {
        return firstPhysicalCamera;
    }

    public List getSecondPhysicalCamera() {
        return secondPhysicalCamera;
    }
}

interface CameraCaptureSessionCallback {
    void callback(CameraCaptureSession cameraCaptureSession);
}

void createDualCameraSession(CameraManager cameraManager,
                                 DualCamera dualCamera,
                                 DualCameraOutputs targets,
                                 Executor executor,
                                 CameraCaptureSessionCallback cameraCaptureSessionCallback) {

        // Create 3 sets of output configurations: one for the logical camera, and
        // one for each of the physical cameras.
        List outputConfigsLogical = targets.getLogicalCamera().stream()
                .map(OutputConfiguration::new)
                .collect(Collectors.toList());
        List outputConfigsPhysical1 = targets.getFirstPhysicalCamera().stream()
                .map(s -> {
                    OutputConfiguration outputConfiguration = new OutputConfiguration(s);
                    outputConfiguration.setPhysicalCameraId(dualCamera.physicalId1);
                    return outputConfiguration;
                })
                .collect(Collectors.toList());
        List outputConfigsPhysical2 = targets.getSecondPhysicalCamera().stream()
                .map(s -> {
                    OutputConfiguration outputConfiguration = new OutputConfiguration(s);
                    outputConfiguration.setPhysicalCameraId(dualCamera.physicalId2);
                    return outputConfiguration;
                })
                .collect(Collectors.toList());

        // Put all the output configurations into a single flat array
        List outputConfigsAll = Stream.of(
                        outputConfigsLogical, outputConfigsPhysical1, outputConfigsPhysical2
                )
                .filter(Objects::nonNull)
                .flatMap(Collection::stream)
                .collect(Collectors.toList());

        // Instantiate a session configuration that can be used to create a session
        SessionConfiguration sessionConfiguration = new SessionConfiguration(
                SessionConfiguration.SESSION_REGULAR,
                outputConfigsAll, executor, new CameraCaptureSession.StateCallback() {
            @Override
            public void onConfigured(@NonNull CameraCaptureSession cameraCaptureSession) {
                cameraCaptureSessionCallback.callback(cameraCaptureSession);
            }
            // Omitting for brevity...
            @Override
            public void onConfigureFailed(@NonNull CameraCaptureSession cameraCaptureSession) {
                cameraCaptureSession.getDevice().close();
            }
        });

        // Open the logical camera using the previously defined function
        openDualCamera(cameraManager, dualCamera, executor, (CameraDevice c) ->
                // Finally create the session and return via callback
                c.createCaptureSession(sessionConfiguration));
    }
```

See[`createCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession%28android.hardware.camera2.params.SessionConfiguration%29)for information on which combination of streams is supported. Combining streams is for multiple streams on a single logical camera. The compatibility extends to using the same configuration and replacing one of those streams with two streams from two physical cameras that are part of the same logical camera.

With the[camera session](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession)ready, dispatch the desired[capture requests](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest). Each target of the capture request receives its data from its associated physical camera, if any are in use, or fall back to the logical camera.

## Zoom example use-case

It is possible to use the merging of physical cameras into a single stream so that users can switch between the different physical cameras to experience a different field-of-view, effectively capturing a different "zoom level."
![](https://developer.android.com/static/images/training/camera/camera2/multi-camera-4.gif)**Figure 4.**Example of swapping cameras for zoom level use-case (from Pixel 3 Ad)

Start by selecting the pair of physical cameras to allow users to switch between. For maximum effect, you can choose the pair of cameras that provide the minimum and maximum focal length available.  

### Kotlin

```kotlin
fun findShortLongCameraPair(manager: CameraManager, facing: Int? = null): DualCamera? {

    return findDualCameras(manager, facing).map {
        val characteristics1 = manager.getCameraCharacteristics(it.physicalId1)
        val characteristics2 = manager.getCameraCharacteristics(it.physicalId2)

        // Query the focal lengths advertised by each physical camera
        val focalLengths1 = characteristics1.get(
            CameraCharacteristics.LENS_INFO_AVAILABLE_FOCAL_LENGTHS) ?: floatArrayOf(0F)
        val focalLengths2 = characteristics2.get(
            CameraCharacteristics.LENS_INFO_AVAILABLE_FOCAL_LENGTHS) ?: floatArrayOf(0F)

        // Compute the largest difference between min and max focal lengths between cameras
        val focalLengthsDiff1 = focalLengths2.maxOrNull()!! - focalLengths1.minOrNull()!!
        val focalLengthsDiff2 = focalLengths1.maxOrNull()!! - focalLengths2.minOrNull()!!

        // Return the pair of camera IDs and the difference between min and max focal lengths
        if (focalLengthsDiff1 < focalLengthsDiff2) {
            Pair(DualCamera(it.logicalId, it.physicalId1, it.physicalId2), focalLengthsDiff1)
        } else {
            Pair(DualCamera(it.logicalId, it.physicalId2, it.physicalId1), focalLengthsDiff2)
        }

        // Return only the pair with the largest difference, or null if no pairs are found
    }.maxByOrNull { it.second }?.first
}
```

### Java

```java
// Utility functions to find min/max value in float[]
    float findMax(float[] array) {
        float max = Float.NEGATIVE_INFINITY;
        for(float cur: array)
            max = Math.max(max, cur);
        return max;
    }
    float findMin(float[] array) {
        float min = Float.NEGATIVE_INFINITY;
        for(float cur: array)
            min = Math.min(min, cur);
        return min;
    }

DualCamera findShortLongCameraPair(CameraManager manager, Integer facing) {
        return findDualCameras(manager, facing).stream()
                .map(c -> {
                    CameraCharacteristics characteristics1;
                    CameraCharacteristics characteristics2;
                    try {
                        characteristics1 = manager.getCameraCharacteristics(c.physicalId1);
                        characteristics2 = manager.getCameraCharacteristics(c.physicalId2);
                    } catch (CameraAccessException e) {
                        e.printStackTrace();
                        return null;
                    }

                    // Query the focal lengths advertised by each physical camera
                    float[] focalLengths1 = characteristics1.get(
                            CameraCharacteristics.LENS_INFO_AVAILABLE_FOCAL_LENGTHS);
                    float[] focalLengths2 = characteristics2.get(
                            CameraCharacteristics.LENS_INFO_AVAILABLE_FOCAL_LENGTHS);

                    // Compute the largest difference between min and max focal lengths between cameras
                    Float focalLengthsDiff1 = findMax(focalLengths2) - findMin(focalLengths1);
                    Float focalLengthsDiff2 = findMax(focalLengths1) - findMin(focalLengths2);

                    // Return the pair of camera IDs and the difference between min and max focal lengths
                    if (focalLengthsDiff1 < focalLengthsDiff2) {
                        return new Pair<>(new DualCamera(c.logicalId, c.physicalId1, c.physicalId2), focalLengthsDiff1);
                    } else {
                        return new Pair<>(new DualCamera(c.logicalId, c.physicalId2, c.physicalId1), focalLengthsDiff2);
                    }

                }) // Return only the pair with the largest difference, or null if no pairs are found
                .max(Comparator.comparing(pair -> pair.second)).get().first;
    }
```

A sensible architecture for this would be to have two[`SurfaceViews`](https://developer.android.com/reference/android/view/SurfaceView)---one for each stream. These`SurfaceViews`get swapped based on user interaction so that only one is visible at any given time.

The following code shows how to open the logical camera, configure the camera outputs, create a camera session, and start two preview streams:  

### Kotlin

```kotlin
val cameraManager: CameraManager = ...

// Get the two output targets from the activity / fragment
val surface1 = ...  // from SurfaceView
val surface2 = ...  // from SurfaceView

val dualCamera = findShortLongCameraPair(manager)!!
val outputTargets = DualCameraOutputs(
    null, mutableListOf(surface1), mutableListOf(surface2))

// Here you open the logical camera, configure the outputs and create a session
createDualCameraSession(manager, dualCamera, targets = outputTargets) { session ->

  // Create a single request which has one target for each physical camera
  // NOTE: Each target receive frames from only its associated physical camera
  val requestTemplate = CameraDevice.TEMPLATE_PREVIEW
  val captureRequest = session.device.createCaptureRequest(requestTemplate).apply {
    arrayOf(surface1, surface2).forEach { addTarget(it) }
  }.build()

  // Set the sticky request for the session and you are done
  session.setRepeatingRequest(captureRequest, null, null)
}
```

### Java

```java
CameraManager manager = ...;

        // Get the two output targets from the activity / fragment
        Surface surface1 = ...;  // from SurfaceView
        Surface surface2 = ...;  // from SurfaceView

        DualCamera dualCamera = findShortLongCameraPair(manager, null);
                DualCameraOutputs outputTargets = new DualCameraOutputs(
                null, Collections.singletonList(surface1), Collections.singletonList(surface2));

        // Here you open the logical camera, configure the outputs and create a session
        createDualCameraSession(manager, dualCamera, outputTargets, null, (session) -> {
            // Create a single request which has one target for each physical camera
            // NOTE: Each target receive frames from only its associated physical camera
            CaptureRequest.Builder captureRequestBuilder;
            try {
                captureRequestBuilder = session.getDevice().createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);
                Arrays.asList(surface1, surface2).forEach(captureRequestBuilder::addTarget);

                // Set the sticky request for the session and you are done
                session.setRepeatingRequest(captureRequestBuilder.build(), null, null);
            } catch (CameraAccessException e) {
                e.printStackTrace();
            }
        });
```

All that is left to do is provide a UI for the user to switch between the two surfaces, such as a button or double-tapping the`SurfaceView`. You could even perform some form of scene analysis and switch between the two streams automatically.

## Lens distortion

All lenses produce a certain amount of distortion. In Android, you can query the distortion created by lenses using[`CameraCharacteristics.LENS_DISTORTION`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#LENS_DISTORTION), which replaces the now-deprecated[`CameraCharacteristics.LENS_RADIAL_DISTORTION`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#LENS_RADIAL_DISTORTION). For logical cameras, the distortion is minimal and your application can use the frames more or less as they come from the camera. For physical cameras, there are potentially very different lens configurations, especially on wide lenses.

Some devices may implement automatic distortion correction via[`CaptureRequest.DISTORTION_CORRECTION_MODE`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#DISTORTION_CORRECTION_MODE). Distortion correction defaults to being on for most devices.  

### Kotlin

```kotlin
val cameraSession: CameraCaptureSession = ...

        // Use still capture template to build the capture request
        val captureRequest = cameraSession.device.createCaptureRequest(
            CameraDevice.TEMPLATE_STILL_CAPTURE
        )

        // Determine if this device supports distortion correction
        val characteristics: CameraCharacteristics = ...
        val supportsDistortionCorrection = characteristics.get(
            CameraCharacteristics.DISTORTION_CORRECTION_AVAILABLE_MODES
        )?.contains(
            CameraMetadata.DISTORTION_CORRECTION_MODE_HIGH_QUALITY
        ) ?: false

        if (supportsDistortionCorrection) {
            captureRequest.set(
                CaptureRequest.DISTORTION_CORRECTION_MODE,
                CameraMetadata.DISTORTION_CORRECTION_MODE_HIGH_QUALITY
            )
        }

        // Add output target, set other capture request parameters...

        // Dispatch the capture request
        cameraSession.capture(captureRequest.build(), ...)
```

### Java

```java
CameraCaptureSession cameraSession = ...;

        // Use still capture template to build the capture request
        CaptureRequest.Builder captureRequestBuilder = null;
        try {
            captureRequestBuilder = cameraSession.getDevice().createCaptureRequest(
                    CameraDevice.TEMPLATE_STILL_CAPTURE
            );
        } catch (CameraAccessException e) {
            e.printStackTrace();
        }

        // Determine if this device supports distortion correction
        CameraCharacteristics characteristics = ...;
        boolean supportsDistortionCorrection = Arrays.stream(
                        characteristics.get(
                                CameraCharacteristics.DISTORTION_CORRECTION_AVAILABLE_MODES
                        ))
                .anyMatch(i -> i == CameraMetadata.DISTORTION_CORRECTION_MODE_HIGH_QUALITY);
        if (supportsDistortionCorrection) {
            captureRequestBuilder.set(
                    CaptureRequest.DISTORTION_CORRECTION_MODE,
                    CameraMetadata.DISTORTION_CORRECTION_MODE_HIGH_QUALITY
            );
        }

        // Add output target, set other capture request parameters...

        // Dispatch the capture request
        cameraSession.capture(captureRequestBuilder.build(), ...);
```

Setting a capture request in this mode can impact the frame rate that can be produced by the camera. You may choose to set the distortion correction on only still image captures.