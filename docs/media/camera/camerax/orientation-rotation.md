---
title: https://developer.android.com/media/camera/camerax/orientation-rotation
url: https://developer.android.com/media/camera/camerax/orientation-rotation
source: md.txt
---

# CameraX use case rotations

This topic showcases how to set up CameraX use cases inside your app to get images with the correct rotation information, whether it's from the`ImageAnalysis`or the`ImageCapture`use case. So:

- The`ImageAnalysis`use case's`Analyzer`should receive frames with the correct rotation.
- The`ImageCapture`use case should take pictures with the correct rotation.

## Terminology

This topic uses the following terminology, so understanding what each term means is important:

Display orientation
:   This refers to which side of the device is in the upward position, and can be one of four values: portrait, landscape, reverse portrait, or reverse landscape.

Display rotation
:   This is the value returned by[`Display.getRotation()`](https://developer.android.com/reference/android/view/Display#getRotation()), and represents the degrees by which the device is rotated counter-clockwise from its natural orientation.

Target rotation
:   This represents the number of degrees through which to rotate the device clockwise to reach its natural orientation.

## How to determine the target rotation

The following examples show how to determine the target rotation for a device based on its natural orientation.

### Example 1: Portrait natural orientation

|                                                                                                 Device example: Pixel 3 XL                                                                                                 ||
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Natural orientation = Portrait Current orientation = Portrait Display rotation = 0 Target rotation = 0    | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-02.png) |
| Natural orientation = Portrait Current orientation = Landscape Display rotation = 90 Target rotation = 90 | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-03.png) |

### Example 2: Landscape natural orientation

|                                                                                                   Device example: Pixel C                                                                                                    ||
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Natural orientation = Landscape Current orientation = Landscape Display rotation = 0 Target rotation = 0    | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-04.png) |
| Natural orientation = Landscape Current orientation = Portrait Display rotation = 270 Target rotation = 270 | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-05.png) |

## Image rotation

Which end is up? The sensor orientation is defined in Android as a constant value, which represents the degrees (0, 90, 180, 270) the sensor is rotated from the top of the device when the device is in a natural position. For all the cases in the diagrams, the image rotation describes how the data should be rotated clockwise to appear upright.

The following examples show what the image rotation should be depending on the camera sensor orientation. They also assume the target rotation is set to the display rotation.

### Example 1: Sensor rotated 90 degrees

|                                                                                Device example: Pixel 3 XL                                                                                 ||
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Display rotation = 0 Display orientation = Portrait Image rotation = 90  | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-06.svg) |
| Display rotation = 90 Display orientation = Landscape Image rotation = 0 | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-07.svg) |

### Example 2: Sensor rotated 270 degrees

|                                                                                  Device example: Nexus 5X                                                                                   ||
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Display rotation = 0 Display orientation = Portrait Image rotation = 270   | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-08.svg) |
| Display rotation = 90 Display orientation = Landscape Image rotation = 180 | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-09.svg) |

### Example 3: Sensor rotated 0 degrees

|                                                                              Device example: Pixel C (Tablet)                                                                              ||
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Display rotation = 0 Display orientation = Landscape Image rotation = 0   | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-10.svg) |
| Display rotation = 270 Display orientation = Portrait Image rotation = 90 | ![](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-11.svg) |

## Computing an image's rotation

### ImageAnalysis

`ImageAnalysis`'s`Analyzer`receives images from the camera in the form of`ImageProxy`s. Each image contains rotation information, which is accessible via:  

```kotlin
val rotation = imageProxy.imageInfo.rotationDegrees
```

This value represents the degrees by which the image needs to be rotated clockwise to match`ImageAnalysis`'s target rotation. In the context of an Android app,`ImageAnalysis`'s target rotation would typically match the screen's orientation.

### ImageCapture

A callback is attached to an`ImageCapture`instance to signal when a capture result is ready. The result can be either the captured image or an error.

When taking a picture, the provided callback can be of one of the following types:

- **`OnImageCapturedCallback`:** Receives an image with in-memory access in the form of an`ImageProxy`.
- **`OnImageSavedCallback`:** Invoked when the captured image has been successfully stored in the location specified by`ImageCapture.OutputFileOptions`. The options can specify a`File`, an`OutputStream`, or a location in`MediaStore`.

The rotation of the captured image, regardless of its format (`ImageProxy`,`File`,`OutputStream`,`MediaStore Uri`) represents the rotation degrees by which the captured image needs to be rotated clockwise to match`ImageCapture`'s target rotation, which again, in the context of an Android app, would typically match the screen's orientation.

Retrieving the captured image's rotation can be done in one of the following ways:

`ImageProxy`  

```kotlin
val rotation = imageProxy.imageInfo.rotationDegrees
```

`File`  

```kotlin
val exif = Exif.createFromFile(file)
val rotation = exif.rotation
```

`OutputStream`  

```kotlin
val byteArray = outputStream.toByteArray()
val exif = Exif.createFromInputStream(ByteArrayInputStream(byteArray))
val rotation = exif.rotation
```

`MediaStore uri`  

```kotlin
val inputStream = contentResolver.openInputStream(outputFileResults.savedUri)
val exif = Exif.createFromInputStream(inputStream)
val rotation = exif.rotation
```

### Verify an image's rotation

The`ImageAnalysis`and`ImageCapture`use cases receive`ImageProxy`s from the camera after a successful capture request. An`ImageProxy`wraps an image and information about it, including its rotation. This rotation information represents the degrees by which the image has to be rotated to match the use case's target rotation.
![An image's rotation verification flow](https://developer.android.com/static/images/training/camera/camerax/rotations-tests/rotations-tests-01.svg)

## ImageCapture/ImageAnalysis target rotation guidelines

Since many devices don't rotate to reverse portrait or reverse landscape by default, some Android apps don't support these orientations. Whether an app supports it or not changes the way the use cases' target rotation can be updated.

Below are two tables defining how to keep the use cases' target rotation in sync with the display rotation. The first shows how to do so while supporting all four orientations; the second only handles the orientations the device rotates to by default.

To choose which guidelines to follow in your app:

1. Verify whether your app's camera`Activity`has a locked orientation, an unlocked orientation, or if it overrides orientation configuration changes.

2. Decide whether your app's camera`Activity`should handle all four device orientations (portrait, reverse portrait, landscape, and reverse landscape), or if it should only handle orientations the device it's running on supports by default.

### Support all four orientations

<br />

<br />

<br />

<br />

<br />

<br />

This table mentions certain guidelines to follow for cases where the device doesn't rotate to reverse portrait. The same can be applied to devices that don't rotate to reverse landscape.

|                                                             Scenario                                                              |                                                                                                                                                                                         Guidelines                                                                                                                                                                                         |                                                                                  Single-window mode                                                                                  |                                                                                                                 Multi-window split-screen mode                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unlocked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#unlocked)                          | Set up the[use cases](https://developer.android.com/media/camera/camerax/orientation-rotation#use-cases-setup)every time the`Activity`is created, such as in the`Activity`'s`onCreate()`callback.                                                                                                                                                                                          |                                                                                                                                                                                      |                                                                                                                                                                                                                                                                 |
| [Unlocked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#unlocked)                          | Use`OrientationEventListener`'s[`onOrientationChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#orientation-event-listener-setup). Inside the callback, update the target rotation of the use cases. This handles cases where the system doesn't recreate the`Activity`even after an orientation change, such as when the device is rotated 180 degrees. | Also handles when the display is in a reverse portrait orientation and the device doesn't rotate to reverse portrait by default.                                                     | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |
| [Unlocked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#unlocked)                          | Optional: Set the`Activity`'s`screenOrientation`property to`fullSensor`in the`AndroidManifest`file.                                                                                                                                                                                                                                                                                        | This allows for the UI to be upright when the device is in reverse portrait, and allows for the`Activity`to be recreated by the system whenever the device is rotated by 90 degrees. | Has no effect on devices that don't rotate to reverse portrait by default. Multi-window mode isn't supported while the display is in a reverse portrait orientation.                                                                                            |
| [Locked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#locked-orientation)                  | Set up the use cases only once, when the`Activity`is first created, such as in the`Activity`'s`onCreate()`callback.                                                                                                                                                                                                                                                                        |                                                                                                                                                                                      |
| [Locked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#locked-orientation)                  | Use`OrientationEventListener`'s[`onOrientationChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#orientation-event-listener-setup). Inside the callback, update the target rotation of the use cases except Preview.                                                                                                                                      |                                                                                                                                                                                      | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |
| [Orientation configChanges overridden](https://developer.android.com/media/camera/camerax/orientation-rotation#config-overridden) | Set up the use cases only once, when the`Activity`is first created, such as in the`Activity`'s`onCreate()`callback.                                                                                                                                                                                                                                                                        |                                                                                                                                                                                      |                                                                                                                                                                                                                                                                 |
| [Orientation configChanges overridden](https://developer.android.com/media/camera/camerax/orientation-rotation#config-overridden) | Use`OrientationEventListener`'s[`onOrientationChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#orientation-event-listener-setup). Inside the callback, update the target rotation of the use cases.                                                                                                                                                     |                                                                                                                                                                                      | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |
| [Orientation configChanges overridden](https://developer.android.com/media/camera/camerax/orientation-rotation#config-overridden) | Optional: Set the Activity's screenOrientation property to fullSensor in the AndroidManifest file.                                                                                                                                                                                                                                                                                         | Allows for the UI to be upright when the device is in reverse portrait.                                                                                                              | Has no effect on devices that don't rotate to reverse portrait by default. Multi-window mode isn't supported while the display is in a reverse portrait orientation.                                                                                            |

### Support only device-supported orientations

Support only orientations the device supports by default (which may or may not include reverse portrait/reverse landscape).

|                                                             Scenario                                                              |                                                                                                                        Guidelines                                                                                                                        |                                                                                                                 Multi-window split-screen mode                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unlocked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#unlocked)                          | Set up the[use cases](https://developer.android.com/media/camera/camerax/orientation-rotation#use-cases-setup)every time the`Activity`is created, such as in the`Activity`'s`onCreate()`callback.                                                        |                                                                                                                                                                                                                                                                 |
| [Unlocked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#unlocked)                          | Use`DisplayListener`'s[`onDisplayChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#displayListener). Inside the callback, update the target rotation of the use cases, such as when the device is rotated 180 degrees. | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |
| [Locked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#locked-orientation)                  | Set up the use cases only once, when the`Activity`is first created, such as in the`Activity`'s`onCreate()`callback.                                                                                                                                      |                                                                                                                                                                                                                                                                 |
| [Locked orientation](https://developer.android.com/media/camera/camerax/orientation-rotation#locked-orientation)                  | Use`OrientationEventListener`'s[`onOrientationChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#orientation-event-listener-setup). Inside the callback, update the target rotation of the use cases.                   | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |
| [Orientation configChanges overridden](https://developer.android.com/media/camera/camerax/orientation-rotation#config-overridden) | Set up the use cases only once, when the`Activity`is first created, such as in the`Activity`'s`onCreate()`callback.                                                                                                                                      |                                                                                                                                                                                                                                                                 |
| [Orientation configChanges overridden](https://developer.android.com/media/camera/camerax/orientation-rotation#config-overridden) | Use`DisplayListener`'s[`onDisplayChanged()`](https://developer.android.com/media/camera/camerax/orientation-rotation#displayListener). Inside the callback, update the target rotation of the use cases, such as when the device is rotated 180 degrees. | Also handles cases where the`Activity`isn't recreated when the device rotates (90 degrees, for example). This happens on small form factor devices when the app takes up half the screen, and on larger devices when the app takes up two thirds of the screen. |

#### Unlocked orientation

An`Activity`has an unlocked orientation when its display orientation (such as portrait or landscape) matches the device's physical orientation, with the exception of reverse portrait/landscape, which some devices don't support by default. To force the device to rotate to all four orientations, set the`Activity`'s`screenOrientation`property to`fullSensor`.

In multi-window mode, a device that doesn't support reverse portrait/landscape by default won't rotate to reverse portrait/landscape, even when its`screenOrientation`property is set to`fullSensor`.  

```xml
<!-- The Activity has an unlocked orientation, but might not rotate to reverse
portrait/landscape in single-window mode if the device doesn't support it by
default. -->
<activity android:name=".UnlockedOrientationActivity" />

<!-- The Activity has an unlocked orientation, and will rotate to all four
orientations in single-window mode. -->
<activity
   android:name=".UnlockedOrientationActivity"
   android:screenOrientation="fullSensor" />
```

#### Locked orientation

A display has a locked orientation when it stays in the same display orientation (such as portrait or landscape) regardless of the physical orientation of the device. This can be done by specifying an`Activity`'s`screenOrientation`property inside its declaration in the`AndroidManifest.xml`file.

When the display has a locked orientation, the system doesn't destroy and recreate the`Activity`as the device is rotated.  

```xml
<!-- The Activity keeps a portrait orientation even as the device rotates. -->
<activity
   android:name=".LockedOrientationActivity"
   android:screenOrientation="portrait" />
```

#### Orientation configuration changes overridden

When an`Activity`overrides orientation configuration changes, the system doesn't destroy and recreate it when the device's physical orientation changes. The system updates the UI though to match the device's physical orientation.  

```xml
<!-- The Activity's UI might not rotate in reverse portrait/landscape if the
device doesn't support it by default. -->
<activity
   android:name=".OrientationConfigChangesOverriddenActivity"
   android:configChanges="orientation|screenSize" />

<!-- The Activity's UI will rotate to all 4 orientations in single-window
mode. -->
<activity
   android:name=".OrientationConfigChangesOverriddenActivity"
   android:configChanges="orientation|screenSize"
   android:screenOrientation="fullSensor" />
```

### Camera use cases setup

In the scenarios described above, the camera use cases can be set up when the`Activity`is first created.

In the case of an`Activity`with an unlocked orientation, this setup is done every time the device is rotated, as the system destroys and recreates the`Activity`on orientation changes. This results in the use cases setting their target rotation to match the display's orientation by default each time.

In the case of an`Activity`with a locked orientation or one that overrides orientation configuration changes, this setup is done once, when the`Activity`is first created.  

```kotlin
class CameraActivity : AppCompatActivity() {
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)

       val cameraProcessFuture = ProcessCameraProvider.getInstance(this)
       cameraProcessFuture.addListener(Runnable {
          val cameraProvider = cameraProcessFuture.get()

          // By default, the use cases set their target rotation to match the
          // display's rotation.
          val preview = buildPreview()
          val imageAnalysis = buildImageAnalysis()
          val imageCapture = buildImageCapture()

          cameraProvider.bindToLifecycle(
              this, cameraSelector, preview, imageAnalysis, imageCapture)
       }, mainExecutor)
   }
}
```

### OrientationEventListener setup

Using an`OrientationEventListener`allows you to continuously update the target rotation of the camera use cases as the device's orientation changes.  

```kotlin
class CameraActivity : AppCompatActivity() {

    private val orientationEventListener by lazy {
        object : OrientationEventListener(this) {
            override fun onOrientationChanged(orientation: Int) {
                if (orientation == ORIENTATION_UNKNOWN) {
                    return
                }

                val rotation = when (orientation) {
                     in 45 until 135 -> Surface.ROTATION_270
                     in 135 until 225 -> Surface.ROTATION_180
                     in 225 until 315 -> Surface.ROTATION_90
                     else -> Surface.ROTATION_0
                 }

                 imageAnalysis.targetRotation = rotation
                 imageCapture.targetRotation = rotation
            }
        }
    }

    override fun onStart() {
        super.onStart()
        orientationEventListener.enable()
    }

    override fun onStop() {
        super.onStop()
        orientationEventListener.disable()
    }
}
```

### DisplayListener setup

Using a`DisplayListener`allows you to update the target rotation of the camera use cases in certain situations, for instance when the system doesn't destroy and recreate the`Activity`after the device rotates by 180 degrees.  

```kotlin
class CameraActivity : AppCompatActivity() {

    private val displayListener = object : DisplayManager.DisplayListener {
        override fun onDisplayChanged(displayId: Int) {
            if (rootView.display.displayId == displayId) {
                val rotation = rootView.display.rotation
                imageAnalysis.targetRotation = rotation
                imageCapture.targetRotation = rotation
            }
        }

        override fun onDisplayAdded(displayId: Int) {
        }

        override fun onDisplayRemoved(displayId: Int) {
        }
    }

    override fun onStart() {
        super.onStart()
        val displayManager = getSystemService(Context.DISPLAY_SERVICE) as DisplayManager
        displayManager.registerDisplayListener(displayListener, null)
    }

    override fun onStop() {
        super.onStop()
        val displayManager = getSystemService(Context.DISPLAY_SERVICE) as DisplayManager
        displayManager.unregisterDisplayListener(displayListener)
    }
}
```