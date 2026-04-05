---
title: Control the camera  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/camera-deprecated/cameradirect
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Control the camera Stay organized with collections Save and categorize content based on your preferences.



In this lesson, we discuss how to control the camera hardware directly using
the framework APIs.

**Note:** This page refers to the
[Camera](/reference/android/hardware/Camera) class, which is deprecated. We
recommend using [CameraX](/media/camera/camerax) or, for specific use cases,
[Camera2](/media/camera/camera2). Both CameraX and Camera2 support Android 5.0
(API level 21) and higher.

Directly controlling a device camera requires a lot more code than requesting pictures or videos
from existing camera applications. However, if you want to build a specialized camera application
or something fully integrated in your app UI, this lesson shows you how.

Refer to the following related resources:

* [Building a Camera App](/guide/topics/media/camera#custom-camera)

## Open the Camera Object

Getting an instance of the `Camera` object is the first step in the
process of directly controlling the camera. As Android's own Camera application does, the
recommended way to access the camera is to open `Camera` on a separate thread
that's launched from `onCreate()`. This approach is a good idea
since it can take a while and might bog down the UI thread. In a more basic implementation,
opening the camera can be deferred to the `onResume()` method to facilitate code reuse and keep the flow of
control simple.

Calling `Camera.open()` throws an
exception if the camera is already in use by another application, so we wrap it
in a `try` block.

### Kotlin

```
private fun safeCameraOpen(id: Int): Boolean {
    return try {
        releaseCameraAndPreview()
        mCamera = Camera.open(id)
        true
    } catch (e: Exception) {
        Log.e(getString(R.string.app_name), "failed to open Camera")
        e.printStackTrace()
        false
    }
}

private fun releaseCameraAndPreview() {
    preview?.setCamera(null)
    mCamera?.also { camera ->
        camera.release()
        mCamera = null
    }
}
```

### Java

```
private boolean safeCameraOpen(int id) {
    boolean qOpened = false;

    try {
        releaseCameraAndPreview();
        camera = Camera.open(id);
        qOpened = (camera != null);
    } catch (Exception e) {
        Log.e(getString(R.string.app_name), "failed to open Camera");
        e.printStackTrace();
    }

    return qOpened;
}

private void releaseCameraAndPreview() {
    preview.setCamera(null);
    if (camera != null) {
        camera.release();
        camera = null;
    }
}
```

Since API level 9, the camera framework supports multiple cameras. If you use the
legacy API and call `open()` without an
argument, you get the first rear-facing camera.

## Create the Camera Preview

Taking a picture usually requires that your users see a preview of their subject before clicking
the shutter. To do so, you can use a `SurfaceView` to draw previews of what the
camera sensor is picking up.

### Preview Class

To get started with displaying a preview, you need preview class. The
preview requires an implementation of the `android.view.SurfaceHolder.Callback` interface, which is used to pass image
data from the camera hardware to the application.

### Kotlin

```
class Preview(
        context: Context,
        val surfaceView: SurfaceView = SurfaceView(context)
) : ViewGroup(context), SurfaceHolder.Callback {

    var mHolder: SurfaceHolder = surfaceView.holder.apply {
        addCallback(this@Preview)
        setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS)
    }
    ...
}
```

### Java

```
class Preview extends ViewGroup implements SurfaceHolder.Callback {

    SurfaceView surfaceView;
    SurfaceHolder holder;

    Preview(Context context) {
        super(context);

        surfaceView = new SurfaceView(context);
        addView(surfaceView);

        // Install a SurfaceHolder.Callback so we get notified when the
        // underlying surface is created and destroyed.
        holder = surfaceView.getHolder();
        holder.addCallback(this);
        holder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
    }
...
}
```

The preview class must be passed to the `Camera` object before the live
image preview can be started, as shown in the next section.

### Set and Start the Preview

A camera instance and its related preview must be created in a specific
order, with the camera object being first. In the snippet below, the
process of initializing the camera is encapsulated so that `Camera.startPreview()` is called by the
`setCamera()` method, whenever the user does something to change the
camera. The preview must also be restarted in the preview class `surfaceChanged()` callback method.

### Kotlin

```
fun setCamera(camera: Camera?) {
    if (mCamera == camera) {
        return
    }

    stopPreviewAndFreeCamera()

    mCamera = camera

    mCamera?.apply {
        mSupportedPreviewSizes = parameters.supportedPreviewSizes
        requestLayout()

        try {
            setPreviewDisplay(holder)
        } catch (e: IOException) {
            e.printStackTrace()
        }

        // Important: Call startPreview() to start updating the preview
        // surface. Preview must be started before you can take a picture.
        startPreview()
    }
}
```

### Java

```
public void setCamera(Camera camera) {
    if (mCamera == camera) { return; }

    stopPreviewAndFreeCamera();

    mCamera = camera;

    if (mCamera != null) {
        List<Size> localSizes = mCamera.getParameters().getSupportedPreviewSizes();
        supportedPreviewSizes = localSizes;
        requestLayout();

        try {
            mCamera.setPreviewDisplay(holder);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Important: Call startPreview() to start updating the preview
        // surface. Preview must be started before you can take a picture.
        mCamera.startPreview();
    }
}
```

## Modify Camera Settings

Camera settings change the way that the camera takes pictures, from the zoom
level to exposure compensation. This example changes only the preview size;
see the source code of the Camera application for many more.

### Kotlin

```
override fun surfaceChanged(holder: SurfaceHolder, format: Int, w: Int, h: Int) {
    mCamera?.apply {
        // Now that the size is known, set up the camera parameters and begin
        // the preview.
        parameters?.also { params ->
            params.setPreviewSize(previewSize.width, previewSize.height)
            requestLayout()
            parameters = params
        }

        // Important: Call startPreview() to start updating the preview surface.
        // Preview must be started before you can take a picture.
        startPreview()
    }
}
```

### Java

```
@Override
public void surfaceChanged(SurfaceHolder holder, int format, int w, int h) {
    // Now that the size is known, set up the camera parameters and begin
    // the preview.
    Camera.Parameters parameters = mCamera.getParameters();
    parameters.setPreviewSize(previewSize.width, previewSize.height);
    requestLayout();
    mCamera.setParameters(parameters);

    // Important: Call startPreview() to start updating the preview surface.
    // Preview must be started before you can take a picture.
    mCamera.startPreview();
}
```

## Set the Preview Orientation

Most camera applications lock the display into landscape mode because that is the natural
orientation of the camera sensor. This setting does not prevent you from taking portrait-mode
photos, because the orientation of the device is recorded in the EXIF header. The `setCameraDisplayOrientation()` method lets you change
how the preview is displayed without affecting how the image is recorded. However, in Android prior
to API level 14, you must stop your preview before changing the orientation and then restart it.

## Take a Picture

Use the `Camera.takePicture()`
method to take a picture once the preview is started. You can create `Camera.PictureCallback` and `Camera.ShutterCallback` objects and pass them into `Camera.takePicture()`.

If you want to grab images continuously, you can create a `Camera.PreviewCallback` that implements `onPreviewFrame()`. For
something in between, you can capture only selected preview frames, or set up a
delayed action to call `takePicture()`.

## Restart the Preview

After a picture is taken, you must restart the preview before the user
can take another picture. In this example, the restart is done by overloading
the shutter button.

### Kotlin

```
fun onClick(v: View) {
    previewState = if (previewState == K_STATE_FROZEN) {
        camera?.startPreview()
        K_STATE_PREVIEW
    } else {
        camera?.takePicture(null, rawCallback, null)
        K_STATE_BUSY
    }
    shutterBtnConfig()
}
```

### Java

```
@Override
public void onClick(View v) {
    switch(previewState) {
    case K_STATE_FROZEN:
        camera.startPreview();
        previewState = K_STATE_PREVIEW;
        break;

    default:
        camera.takePicture( null, rawCallback, null);
        previewState = K_STATE_BUSY;
    } // switch
    shutterBtnConfig();
}
```

## Stop the Preview and Release the Camera

Once your application is done using the camera, it's time to clean up. In
particular, you must release the `Camera` object, or you risk crashing other
applications, including new instances of your own application.

When should you stop the preview and release the camera? Well, having your
preview surface destroyed is a pretty good hint that it’s time to stop the
preview and release the camera, as shown in these methods from the `Preview` class.

### Kotlin

```
override fun surfaceDestroyed(holder: SurfaceHolder) {
    // Surface will be destroyed when we return, so stop the preview.
    // Call stopPreview() to stop updating the preview surface.
    mCamera?.stopPreview()
}

/**
 * When this function returns, mCamera will be null.
 */
private fun stopPreviewAndFreeCamera() {
    mCamera?.apply {
        // Call stopPreview() to stop updating the preview surface.
        stopPreview()

        // Important: Call release() to release the camera for use by other
        // applications. Applications should release the camera immediately
        // during onPause() and re-open() it during onResume()).
        release()

        mCamera = null
    }
}
```

### Java

```
@Override
public void surfaceDestroyed(SurfaceHolder holder) {
    // Surface will be destroyed when we return, so stop the preview.
    if (mCamera != null) {
        // Call stopPreview() to stop updating the preview surface.
        mCamera.stopPreview();
    }
}

/**
 * When this function returns, mCamera will be null.
 */
private void stopPreviewAndFreeCamera() {

    if (mCamera != null) {
        // Call stopPreview() to stop updating the preview surface.
        mCamera.stopPreview();

        // Important: Call release() to release the camera for use by other
        // applications. Applications should release the camera immediately
        // during onPause() and re-open() it during onResume()).
        mCamera.release();

        mCamera = null;
    }
}
```

Earlier in the lesson, this procedure was also part of the `setCamera()` method, so initializing a camera always begins with stopping the
preview.