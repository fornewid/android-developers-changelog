---
title: Use a projected context to access hardware on audio glasses and display glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Use a projected context to access hardware on audio glasses and display glasses Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Audio &  
Display Glasses

[Learn about XR device types →](/develop/xr/devices)

After you've [requested and been granted the necessary permissions](/develop/xr/jetpack-xr-sdk/request-hardware-permissions), your app
can access the hardware on the audio glasses or display glasses. The key to
accessing the glasses' hardware (instead of the phone's hardware), is to use a
[projected context](/develop/xr/jetpack-xr-sdk/glasses/support-different-types#projected-context).

There are two primary ways to get a projected context, depending on where your
code is executing:

## Get a projected context if your code is running in an projected activity

If your app's code is running from within your [projected activity](/develop/xr/jetpack-xr-sdk/glasses/support-different-types#activity-lifecycle), its own
activity context is already a [projected context](/develop/xr/jetpack-xr-sdk/glasses/support-different-types#projected-context). In this scenario, calls
made within that activity can already access the glasses' hardware.

## Get a projected context for code running in a phone app component

If a part of your app outside of your projected activity (such as a phone
activity or a service) needs to access the glasses' hardware, it must explicitly
obtain a projected context. To do this, use the
[`createProjectedDeviceContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedDeviceContext(android.content.Context)) method:

```
@RequiresApi(Build.VERSION_CODES.BAKLAVA)
@OptIn(ExperimentalProjectedApi::class, ExperimentalCoroutinesApi::class)
private fun monitorProjectedConnectivity(activity: ComponentActivity) {
    activity.lifecycleScope.launch {
        // Before creating a projected context, check to see if the projected device is connected.
        // While this method returns true, the projected context remains valid.
        ProjectedContext.isProjectedDeviceConnected(activity, coroutineContext)
            .collectLatest { isConnected ->
                if (isConnected) {
                    // From a phone Activity or Service, get a context for the audio and display glasses.
                    // Re-initialize on reconnect: Obtain another context instance.
                    val projectedContext = try {
                        ProjectedContext.createProjectedDeviceContext(activity)
                    } catch (e: IllegalStateException) {
                        Log.e(TAG, "Failed to create projected context", e)
                        return@collectLatest
                    }

                    // Use the projectedContext to initialize system services (e.g., CameraManager).
                    Log.i(TAG, "Projected device connected. Initializing hardware...")
                } else {
                    // The projected context is destroyed when the device disconnects.
                    // Clean up on disconnect: Listen for 'false' and release resources.
                    Log.i(TAG, "Projected device disconnected. Cleaning up hardware resources...")
                }
            }
    }
}

ProjectedHardware.kt
```

### Check for validity

Wrap the [`createProjectedDeviceContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedDeviceContext(android.content.Context)) call within the
[`ProjectedContext.isProjectedDeviceConnected`](/reference/kotlin/androidx/xr/projected/ProjectedContext#isProjectedDeviceConnected(android.content.Context,kotlin.coroutines.CoroutineContext)). While this method returns
`true`, the projected context remains valid to the connected device, and your
phone app activity or service (such as a `CameraManager`) can access the AI
glasses hardware.

### Clean up on disconnect

The projected context is tied to the lifecycle of the connected device, so it is
destroyed when the device disconnects. When the device disconnects,
[`ProjectedContext.isProjectedDeviceConnected`](/reference/kotlin/androidx/xr/projected/ProjectedContext#isProjectedDeviceConnected(android.content.Context,kotlin.coroutines.CoroutineContext)) returns `false`. Your app
should listen for this change and clean up any system services (such as a
`CameraManager`) or resources that your app created using that projected
context.

### Re-initialize on reconnect

When the glasses reconnect, your app can obtain another projected
context instance using [`createProjectedDeviceContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedDeviceContext(android.content.Context)), and then
re-initialize any system services or resources using the new projected context.

## Record audio with the glasses' microphone

You can record audio from the glasses using two distinct methods:

* Use a [projected context](/develop/xr/jetpack-xr-sdk/glasses/support-different-types#projected-context).
* Use Bluetooth Hands-Free Profile (HFP).

### Choose a recording methods

The method you choose depends on whether you need high-fidelity, XR-specific
audio processing, or standard Bluetooth audio input.

| Recording method | Microphone access | Common use case |
| --- | --- | --- |
| Projected Context | Multiple microphones | Recording using a projected context lets your app access multiple microphones from the glasses and its specialized hardware features, such as:   * XR-specific spatialization. * Advanced denoising. * Voice separation that isolates the wearer's voice. * Maintain recording access in multidevice environments even when the glasses are not the active Bluetooth device. |
| Bluetooth HFP | Single microphone | Relies on the Bluetooth Hands-Free Profile (HFP) for immediate, out-of-the-box compatibility. In this mode, the glasses connect to the phone using standard Headset and Advanced Audio Distribution Profile (A2DP) [profiles](/develop/connectivity/bluetooth/profiles), functioning like a typical Bluetooth peripheral.  If your app is already designed for standard Bluetooth recording, you can use this method to record audio from the glasses without integrating any XR-specific capabilities. |

### Record audio using a projected context

To record audio using a projected context, first request the required runtime
permissions, and then record the audio using the [`AudioRecord`](/reference/kotlin/android/media/AudioRecord) API, as
described in the following sections.

#### Request runtime permissions

To access multiple microphones on the glasses, you must request audio
permissions specifically for the projected device. The standard, phone-scoped
`RECORD_AUDIO` permission that a user has granted for your app on their mobile
device is insufficient.

Follow these steps to request the permissions:

1. [Declare the `RECORD_AUDIO` permission](/develop/xr/jetpack-xr-sdk/request-hardware-permissions#declare-permissions) in your app's manifest file.
2. Request the projected-device-scoped permissions in one of the following
   ways, depending on where your code is executing:

   * **Code executing from a projected activity**: Use the
     [`ActivityResultLauncher`](/reference/kotlin/androidx/activity/result/ActivityResultLauncher) with the
     [`ProjectedPermissionsResultContract`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsResultContract#ProjectedPermissionsResultContract()). For more information on
     using this method, see the [register the permissions launcher](/develop/xr/jetpack-xr-sdk/request-hardware-permissions#register)
     section and subsequent sections in the guide for requesting hardware
     permissions.
   * **Code executing from a host phone activity**: Use
     [`Activity#requestPermissions(permissions, requestCode, deviceId)`](/reference/kotlin/android/app/Activity#requestpermissions_1)
     and provide the device ID obtained from your `projectedDeviceContext`,
     as described in the [understand the permission request user flow](/develop/xr/jetpack-xr-sdk/request-hardware-permissions#permissions-user-flow)
     section of the guide for requesting hardware permissions.

#### Initialize AudioRecord with a projected context

To ensure that audio is recorded from the glasses rather than the host phone,
you must associate the `AudioRecord` object with the projected device context.

The following code uses the [`AudioRecord.Builder`](/reference/kotlin/android/media/AudioRecord.Builder) and passes the
`projectedDeviceContext` to the [`setContext`](/reference/kotlin/android/media/AudioRecord.Builder#setcontext) method:

```
// Initialize AudioRecord with projected device context
val audioRecord = AudioRecord.Builder()
    .setAudioSource(MediaRecorder.AudioSource.CAMCORDER)
    .setAudioFormat(audioFormat)
    .setBufferSizeInBytes(bufferSize)
    // pass in the projected device context
    .setContext(projectedDeviceContext)
    .build()

audioRecord.startRecording()

ProjectedHardware.kt
```

##### Key points about the code

* You can set the audio source to [`CAMCORDER`](/reference/kotlin/android/media/MediaRecorder.AudioSource#camcorder),
  [`VOICE_RECOGNITION`](/reference/kotlin/android/media/MediaRecorder.AudioSource#voice_recognition), [`VOICE_COMMUNICATION`](/reference/kotlin/android/media/MediaRecorder.AudioSource#voice_communication), or
  [`UNPROCESSED`](/reference/kotlin/android/media/MediaRecorder.AudioSource#unprocessed) to tailor the audio processing to your specific use
  case.

  For example, use `VOICE_COMMUNICATION` if your use case needs automatic
  noise reduction or to isolate the wearer's voice. `VOICE_RECOGNITION` is
  processed with acoustic echo cancellation (AEC), which can be useful when
  there's concurrent audio playback while recording. And if you need raw,
  unaltered audio, select `UNPROCESSED` or `CAMCORDER`.
* To ensure compatibility with the glasses, the `audioFormat` object must
  define a sample rate of 16kHz and a channel configuration of either mono or
  stereo (using [`CHANNEL_IN_MONO`](/reference/kotlin/android/media/AudioFormat#channel_in_mono) or [`CHANNEL_IN_STEREO`](/reference/kotlin/android/media/AudioFormat#channel_in_stereo)).
* Use [`AudioRecord.getMinBufferSize()`](/reference/kotlin/android/media/AudioRecord#getminbuffersize) to determine the minimum buffer
  size to create the `AudioRecord` object. However, to prevent audio drops
  from the glasses, you should read from this buffer in short, frequent chunks
  (ideally 20ms slices) rather than waiting for the entire buffer to fill.

**Preview:** Support for using the [`MediaRecorder`](/reference/kotlin/android/media/MediaRecorder) API with a projected
context will be available in an upcoming Android Beta release.

##### Clean up after use

When your app no longer needs the microphone, or when the activity is stopped,
call [`stop`](/reference/kotlin/android/media/AudioRecord#stop) and [`release`](/reference/kotlin/android/media/AudioRecord#release) on the `AudioRecord` object.

##### Check for runtime permissions before recording

Before calling [`startRecording`](/reference/kotlin/android/media/AudioRecord#startrecording), [verify that the user has granted the
microphone permission for the glasses](/develop/xr/jetpack-xr-sdk/request-hardware-permissions#check-function) using the projected context.

### Record audio using Bluetooth HFP

To record audio using Bluetooth HFP, first request the required runtime
permissions, and then record the audio using the [`AudioManager`](/reference/kotlin/android/media/AudioManager) API, as
described in the following sections.

#### Request permissions

As with any standard Bluetooth audio device, the [`RECORD_AUDIO`](/reference/kotlin/android/Manifest.permission#record_audio),
[`BLUETOOTH_CONNECT`](/reference/kotlin/android/Manifest.permission#bluetooth_connect), and other related permissions are controlled by the
phone and not the connected device (such as audio glasses or display glasses).

Follow these steps to request the permissions:

1. [Declare following permissions](/develop/xr/jetpack-xr-sdk/request-hardware-permissions#declare-permissions) in your app's manifest file:

   * [`RECORD_AUDIO`](/reference/kotlin/android/Manifest.permission#record_audio)
   * [`BLUETOOTH_CONNECT`](/reference/kotlin/android/Manifest.permission#bluetooth_connect)
   * [`MODIFY_AUDIO_SETTINGS`](/reference/kotlin/android/Manifest.permission#modify_audio_settings)
2. Request both the `RECORD_AUDIO` and `BLUETOOTH_CONNECT` permissions at
   runtime using the [standard Android permission flow](/training/permissions/requesting).

#### Use AudioManager to route audio

After the user has granted your app the necessary runtime permissions, use the
[`AudioManager`](/reference/kotlin/android/media/AudioManager) API to set the communication device to
[`TYPE_BLUETOOTH_SCO`](/reference/kotlin/android/media/AudioDeviceInfo#type_bluetooth_sco) to route the audio through Bluetooth HFP. This
directs the system to retrieve audio from the Bluetooth peripheral.

```
val audioManager = context.getSystemService(AudioManager::class.java) ?: return
val devices = audioManager.getDevices(AudioManager.GET_DEVICES_INPUTS)
val hfpDevice = devices.find { it.type == AudioDeviceInfo.TYPE_BLUETOOTH_SCO }

hfpDevice?.let { device ->
    val audioRecord = AudioRecord.Builder()
        .setAudioSource(MediaRecorder.AudioSource.VOICE_COMMUNICATION)
        .setAudioFormat(audioFormat)
        .setBufferSizeInBytes(bufferSize)
        .build()

    // Route recording to the Bluetooth device
    audioRecord.setPreferredDevice(device)
    audioManager.setCommunicationDevice(device)

    audioRecord.startRecording()

ProjectedHardware.kt
```

**Note:** To learn more about Bluetooth connectivity, refer to our
[documentation](/develop/connectivity/bluetooth).

## Capture an image with the glasses' camera

To capture an image with the glasses' camera, set up and bind the CameraX's
[`ImageCapture`](/reference/kotlin/androidx/camera/core/ImageCapture) [use case](/media/camera/camerax#ease-of-use) to the glasses' camera using the correct
context for your app:

```
private fun startCameraOnGlasses(activity: ComponentActivity) {
    activity.lifecycleScope.launch {
        // Before creating a projected context, check to see if the projected device is connected.
        ProjectedContext.isProjectedDeviceConnected(activity, coroutineContext)
            .collectLatest { isConnected ->
                if (isConnected) {
                    // 1. Get the CameraProvider using the projected context.
                    // When using the projected context, DEFAULT_BACK_CAMERA maps to the audio and display glasses' camera.
                    val projectedContext = try {
                        ProjectedContext.createProjectedDeviceContext(activity)
                    } catch (e: IllegalStateException) {
                        Log.e(TAG, "Projected context could not be created", e)
                        return@collectLatest
                    }

                    val cameraProviderFuture = ProcessCameraProvider.getInstance(projectedContext)

                    cameraProviderFuture.addListener({
                        val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()
                        val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

                        // 2. Check for the presence of a camera.
                        if (!cameraProvider.hasCamera(cameraSelector)) {
                            Log.w(TAG, "The selected camera is not available.")
                            return@addListener
                        }

                        // 3. Query supported streaming resolutions using Camera2 Interop.
                        val cameraInfo = cameraProvider.getCameraInfo(cameraSelector)
                        val camera2CameraInfo = Camera2CameraInfo.from(cameraInfo)
                        val cameraCharacteristics = camera2CameraInfo.getCameraCharacteristic(
                            CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP
                        )

                        // 4. Define the resolution strategy.
                        val targetResolution = Size(1920, 1080)
                        val resolutionStrategy = ResolutionStrategy(
                            targetResolution,
                            ResolutionStrategy.FALLBACK_RULE_CLOSEST_LOWER
                        )
                        val resolutionSelector = ResolutionSelector.Builder()
                            .setResolutionStrategy(resolutionStrategy)
                            .build()

                        // 5. If you have other continuous use cases bound, such as Preview or ImageAnalysis,
                        // you can use  Camera2 Interop's CaptureRequestOptions to set the FPS
                        val fpsRange = Range(30, 60)
                        val captureRequestOptions = CaptureRequestOptions.Builder()
                            .setCaptureRequestOption(CaptureRequest.CONTROL_AE_TARGET_FPS_RANGE, fpsRange)
                            .build()

                        // 6. Initialize the ImageCapture use case with options.
                        val imageCapture = ImageCapture.Builder()
                            // Optional: Configure resolution, format, etc.
                            .setResolutionSelector(resolutionSelector)
                            .build()

                        try {
                            // Unbind use cases before rebinding.
                            cameraProvider.unbindAll()

                            // Bind use cases to camera using the Activity as the LifecycleOwner.
                            cameraProvider.bindToLifecycle(
                                activity,
                                cameraSelector,
                                imageCapture
                            )
                        } catch (exc: Exception) {
                            Log.e(TAG, "Use case binding failed", exc)
                        }
                    }, ContextCompat.getMainExecutor(activity))
                }
            }
    }
}

ProjectedHardware.kt
```

### Key points about the code

* Obtains an instance of the [`ProcessCameraProvider`](/reference/kotlin/androidx/camera/lifecycle/ProcessCameraProvider) using the
  [**projected device context**](#phone-activity-service).
* Within the projected context's scope, the glasses' primary,
  outward-pointing camera maps to the `DEFAULT_BACK_CAMERA` when selecting a
  camera.
* A pre-binding check uses [`cameraProvider.hasCamera(cameraSelector)`](/reference/kotlin/androidx/camera/lifecycle/ProcessCameraProvider#hasCamera(androidx.camera.core.CameraSelector)) to
  verify that the selected camera is available on the device before
  proceeding.
* Uses **Camera2 Interop** with [`Camera2CameraInfo`](/reference/kotlin/androidx/camera/camera2/interop/Camera2CameraInfo) to read the
  underlying [`CameraCharacteristics#SCALER_STREAM_CONFIGURATION_MAP`](/reference/kotlin/android/hardware/camera2/CameraCharacteristics#scaler_stream_configuration_map),
  which can be useful for advanced checks on supported resolutions.
* A custom [`ResolutionSelector`](/reference/kotlin/androidx/camera/core/resolutionselector/ResolutionSelector) is built to precisely control the output
  image resolution for [`ImageCapture`](/reference/kotlin/androidx/camera/core/ImageCapture).
* Creates an `ImageCapture` use case that is configured with a custom
  `ResolutionSelector`.
* Binds the `ImageCapture` use case to the activity's lifecycle. This
  automatically manages the opening and closing of the camera based on the
  activity's state (for example, stopping the camera when the activity is
  paused).

After the glasses' camera is set up, you can capture an image with the
CameraX's `ImageCapture` class. Refer to the CameraX's documentation to learn
about using [`takePicture`](/media/camera/camerax/take-photo#take_a_picture) to [capture an image](/media/camera/camerax/take-photo#take_a_picture).

### Capture a video with the glasses' camera

To capture a video instead of an image with the glasses' camera, replace the
`ImageCapture` components with the corresponding [`VideoCapture`](/reference/kotlin/androidx/camera/video/VideoCapture) components
and modify the capture execution logic.

The main changes involve using a different use case, creating a different output
file, and initiating the capture using the appropriate video recording method.
For more information about the `VideoCapture` API and how to use it, see the
[CameraX's video capture documentation](/media/camera/camerax/video-capture#using-videocapture-api).

**Important:** Battery power and thermal dissipation on glasses devices is often
limited. When developing for glasses, pay close attention to the requested
**output format** and **resolution**, as these can severely impact system power
and temperature.

The following table shows the recommended resolution and frame rate depending on
your app's use case:

| Use case | Resolution | Frame rate |
| --- | --- | --- |
| Video Communication | 1280 x 720 | 15 FPS |
| Computer Vision | 640 x 480 | 10 FPS |
| AI Video Streaming | 640 x 480 | 1 FPS |

## Access a phone's hardware from a projected activity

An [projected activity](/develop/xr/jetpack-xr-sdk/glasses/support-different-types#activity-lifecycle) can also access the phone's hardware (such as the
camera or microphone) by using [`createHostDeviceContext(context)`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createHostDeviceContext(android.content.Context)) to get
the host device's (phone) context:

```
@OptIn(ExperimentalProjectedApi::class)
private fun getPhoneContext(activity: ComponentActivity): Context? {
    return try {
        // From a projected Activity, get a context for the phone.
        ProjectedContext.createHostDeviceContext(activity)
    } catch (e: IllegalStateException) {
        Log.e(TAG, "Failed to create host device context", e)
        null
    }
}

ProjectedHardware.kt
```

When accessing hardware or resources that are specific to the host device
(phone) in a hybrid app (an app containing both mobile and glasses
experiences), you must explicitly select the correct context to make sure your
app can access the correct hardware:

* Use the [`Activity`](/reference/kotlin/android/app/Activity) context from the phone `Activity` or the
  [`ProjectedContext.createHostDeviceContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createHostDeviceContext(android.content.Context)) to get the phone's
  context.
* Don't use [`getApplicationContext`](/reference/kotlin/android/content/Context#getapplicationcontext) because the application context
  can incorrectly return the glasses' context if a projected activity was the
  most-recently-launched component.

[Previous

arrow\_back

Request hardware permissions](/develop/xr/jetpack-xr-sdk/request-hardware-permissions)