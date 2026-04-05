---
title: https://developer.android.com/media/camera/camera2/foldable-devices
url: https://developer.android.com/media/camera/camera2/foldable-devices
source: md.txt
---

# Foldable devices and cameras

**Note:** This page refers to the [Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary) package. Unless your app requires specific, low-level features from Camera2, we recommend using [CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

Camera developers might encounter unique challenges when working on camera
applications that run on foldable devices. Unlike smartphones, where several
assumptions related to display orientation, camera orientation, and facing are
often valid, foldable devices can have diverse form factors, display layouts,
and camera combinations.

Smartphones commonly have cameras with portrait orientation
matching the display. However, this may not be true for certain foldable states.
An unfolded screen might have one sensor with portrait orientation and another
sensor with landscape orientation.

If your camera application uses a [`SurfaceTexture`](https://developer.android.com/reference/android/graphics/SurfaceTexture) or a
custom rendering pipeline, be aware of the camera sensor orientation.

This ensures that rendered content is always physically upright and pixels
remain square, avoiding stretching in horizontal or vertical directions.

This guide provides information on what Camera2 developers need to consider
and the steps to adjust camera preview rendering for different foldable device
states.

## How device state switches affect cameras

Foldable devices may include:

- Two or more physical displays
- Several physical camera devices

These devices can become active depending on the device state. To simplify
device state handling, certain devices implement a logical camera that consists
of two or more physical sensors.

If developers open and enable preview streaming on such a logical camera
device, the camera automatically switches between physical devices in response
to specific fold states.

For example, consider a foldable device with two displays:

- A regular portrait screen in folded state with a physical 'outer' front camera in portrait orientation.
- A foldable screen enabled in unfolded state with an 'inner' front physical camera with landscape orientation relative to the unfolded display.

When the user folds or unfolds the device while an application streams from
the front logical camera, the device implementation may switch between the
inner and outer physical sensors in response to each device state switch.

The display switch may require the application to adjust its UI.

Along with any UI adjustments, developers may need to consider adjusting how
the camera preview renders with regard to the active physical camera.

## Physical camera device switches

The logical camera device interface provides the necessary APIs to handle
physical camera switches. Developers must monitor the value of the
[active physical id](https://developer.android.com/reference/kotlin/android/hardware/camera2/CaptureResult#logical_multi_camera_active_physical_id).

On foldable devices the active physical ID capture result can change in response
to different foldable state switches like folding and unfolding.

In such events, developers must use the current active physical ID and check the
corresponding [camera characteristics](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraCharacteristics).

The two most important camera characteristics that can potentially change
and affect preview rendering are the [sensor orientation](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraCharacteristics#sensor_orientation)
and the [lens facing](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraCharacteristics#lens_facing).

If your application's preview rendering pipeline depends on static camera
parameters to calculate its final transformation matrix, ensure that you pass
the current values and update the graphics transformations.

For a deeper understanding of camera preview pipelines and how transformations
are calculated, consult the [camera preview guide](https://developer.android.com/media/camera/camera2/camera-preview).

## Additional invalid assumptions

Caching of camera characteristic values is not recommended.

You can't assume that camera characteristics will remain constant, since the
characteristics can change when the device is folded or unfolded. For that
reason, you shouldn't store and reuse camera characteristics. Instead, check
the camera characteristics each time.

Consider the case where a camera application starts on the outer front
display and caches the current front and back camera characteristics. If the
application restarts on the inner display, the active front physical
sensor may have a different orientation, potentially triggering unwanted preview
render side effects.