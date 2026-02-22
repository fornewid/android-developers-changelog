---
title: https://developer.android.com/media/camera/camerax/preview
url: https://developer.android.com/media/camera/camerax/preview
source: md.txt
---

# Implement a preview

When adding a preview to your app, use[`PreviewView`](https://developer.android.com/reference/kotlin/androidx/camera/view/PreviewView), which is a`View`that can be cropped, scaled, and rotated for proper display.

The image preview streams to a surface inside the`PreviewView`when the camera becomes active.

## Use the PreviewView

Implementing a preview for CameraX using`PreviewView`involves the following steps, which are covered in later sections:

1. Optionally configure a[`CameraXConfig.Provider`](https://developer.android.com/reference/kotlin/androidx/camera/core/CameraXConfig.Provider).
2. Add a`PreviewView`to your layout.
3. Request a[`ProcessCameraProvider`](https://developer.android.com/reference/kotlin/androidx/camera/lifecycle/ProcessCameraProvider).
4. On`View`creation, check for the`ProcessCameraProvider`.
5. Select a camera and bind the lifecycle and use cases.

Using`PreviewView`has some limitations. When using`PreviewView`, you can't do any of the following things:

- Create a`SurfaceTexture`to set on`TextureView`and[`Preview.SurfaceProvider`](https://developer.android.com/reference/androidx/camera/core/Preview.SurfaceProvider).
- Retrieve the`SurfaceTexture`from`TextureView`and set it on`Preview.SurfaceProvider`.
- Get the`Surface`from`SurfaceView`and set it on`Preview.SurfaceProvider`.

If any of these happen, then the`Preview`stops streaming frames to the`PreviewView`.

### Add a PreviewView to your layout

The following sample shows a`PreviewView`in a layout:  

```xml
<FrameLayout
    android:id="@+id/container">
        <androidx.camera.view.PreviewView
            android:id="@+id/previewView" />
</FrameLayout>
```

### Request a CameraProvider

The following code shows how to request a`CameraProvider`:  

### Kotlin

```kotlin
import androidx.camera.lifecycle.ProcessCameraProvider
import com.google.common.util.concurrent.ListenableFuture

class MainActivity : AppCompatActivity() {
    private lateinit var cameraProviderFuture : ListenableFuture<ProcessCameraProvider>
    override fun onCreate(savedInstanceState: Bundle?) {
        cameraProviderFuture = ProcessCameraProvider.getInstance(this)
    }
}
```

### Java

```java
import androidx.camera.lifecycle.ProcessCameraProvider
import com.google.common.util.concurrent.ListenableFuture

public class MainActivity extends AppCompatActivity {
    private ListenableFuture<ProcessCameraProvider> cameraProviderFuture;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        cameraProviderFuture = ProcessCameraProvider.getInstance(this);
    }
}
```

### Check for CameraProvider availability

After requesting a`CameraProvider`, verify that its initialization succeeded when the view is created. The following code shows how to do this:  

### Kotlin

```kotlin
cameraProviderFuture.addListener(Runnable {
    val cameraProvider = cameraProviderFuture.get()
    bindPreview(cameraProvider)
}, ContextCompat.getMainExecutor(this))
```

### Java

```java
cameraProviderFuture.addListener(() -> {
    try {
        ProcessCameraProvider cameraProvider = cameraProviderFuture.get();
        bindPreview(cameraProvider);
    } catch (ExecutionException | InterruptedException e) {
        // No errors need to be handled for this Future.
        // This should never be reached.
    }
}, ContextCompat.getMainExecutor(this));
```

For an example of the`bindPreview`function used in this sample, see the code provided in the next section.

### Select a camera and bind the lifecycle and use cases

Once you have created and confirmed the`CameraProvider`, do the following:

1. Create a`Preview`.
2. Specify the desired camera`LensFacing`option.
3. Bind the selected camera and any use cases to the lifecycle.
4. Connect the`Preview`to the`PreviewView`.

The following code shows an example:  

### Kotlin

```kotlin
fun bindPreview(cameraProvider : ProcessCameraProvider) {
    var preview : Preview = Preview.Builder()
            .build()

    var cameraSelector : CameraSelector = CameraSelector.Builder()
          .requireLensFacing(CameraSelector.LENS_FACING_BACK)
          .build()

    preview.setSurfaceProvider(previewView.getSurfaceProvider())

    var camera = cameraProvider.bindToLifecycle(this as LifecycleOwner, cameraSelector, preview)
}
```

### Java

```java
void bindPreview(@NonNull ProcessCameraProvider cameraProvider) {
    Preview preview = new Preview.Builder()
            .build();

    CameraSelector cameraSelector = new CameraSelector.Builder()
            .requireLensFacing(CameraSelector.LENS_FACING_BACK)
            .build();

    preview.setSurfaceProvider(previewView.getSurfaceProvider());

    Camera camera = cameraProvider.bindToLifecycle((LifecycleOwner)this, cameraSelector, preview);
}
```

Note that[`bindToLifecycle()`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider#bindToLifecycle(androidx.lifecycle.LifecycleOwner,%20androidx.camera.core.CameraSelector,%20androidx.camera.core.UseCase...))returns a[`Camera`](https://developer.android.com/reference/androidx/camera/core/Camera)object. For more information about controlling camera output, such as zoom and exposure, see[Camera output](https://developer.android.com/training/camerax/configuration#camera-output).

You are now done implementing the camera preview. Build your app and confirm that your preview appears in your app and functions as you intend it to.

## Additional controls for PreviewView

CameraX`PreviewView`provides some additional APIs to configure properties such as:

- The[implementation mode](https://developer.android.com/reference/androidx/camera/view/PreviewView.ImplementationMode)for rendering preview streams.
- The preview image[scale type](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType).

### Implementation mode

`PreviewView`can use one of the following modes to render a preview stream onto the target`View`:

- [`PERFORMANCE`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ImplementationMode#PERFORMANCE)is the default mode.`PreviewView`uses a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)to display the video stream, but falls back to a[`TextureView`](https://developer.android.com/reference/android/view/TextureView)in[certain cases](https://developer.android.com/reference/androidx/camera/view/PreviewView.ImplementationMode#PERFORMANCE).`SurfaceView`has a dedicated drawing surface, which has a better chance of being implemented with a hardware overlay by the[internal hardware compositor](https://source.android.com/devices/graphics/hwc), especially when there are no other UI elements (like buttons) on top of the preview video. By rendering with a hardware overlay, video frames avoid a GPU path, which can reduce platform power consumption and latency.

- [`COMPATIBLE`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ImplementationMode#COMPATIBLE)mode. In this mode,`PreviewView`uses a`TextureView`which, unlike`SurfaceView`, does not have a dedicated drawing surface. As a result, video renders with blending so that it can be displayed. During this extra step, the application can perform additional processing, such as scaling and rotating videos without restriction.

Use[`PreviewView.setImplementationMode()`](https://developer.android.com/reference/androidx/camera/view/PreviewView#setImplementationMode(androidx.camera.view.PreviewView.ImplementationMode))to select the implementation mode suitable for your application. If the default`PERFORMANCE`mode isn't suitable for your application, the following code sample shows how to set`COMPATIBLE`mode:  

### Kotlin

```kotlin
// viewFinder is a PreviewView instance
viewFinder.implementationMode = PreviewView.ImplementationMode.COMPATIBLE
```

### Scale type

When the preview video resolution differs from the dimensions of your target`PreviewView`, video content needs to be fit to the view either by cropping or letterboxing (maintaining the original aspect ratio).`PreviewView`provides the following[`ScaleTypes`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType)for this purpose:

- [`FIT_CENTER`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FIT_CENTER),[`FIT_START`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FIT_START), and[`FIT_END`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FIT_END)for letterboxing. The full video content is scaled (either up or down) to the maximum possible size that can be displayed in the target`PreviewView`. However, although the full video frame is visible, some portion of the screen might be blank. Depending on which of these three scale types you choose, the video frame aligns to the center, start, or end of the target View.

- [`FILL_CENTER`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FILL_CENTER),[`FILL_START`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FILL_START),[`FILL_END`](https://developer.android.com/reference/androidx/camera/view/PreviewView.ScaleType#FILL_END)for cropping. If a video doesn't match the`PreviewView`aspect ratio, only a portion of the content is visible, but the video fills the entire`PreviewView`.

The default scale type CameraX uses is`FILL_CENTER`. Use[`PreviewView.setScaleType()`](https://developer.android.com/reference/androidx/camera/view/PreviewView#setScaleType(androidx.camera.view.PreviewView.ScaleType))to set the scale type most appropriate for your application. The following code sample sets the`FIT_CENTER`scale type:  

### Kotlin

```kotlin
// viewFinder is a PreviewView instance
viewFinder.scaleType = PreviewView.ScaleType.FIT_CENTER
```

The process for displaying a video consists of the following steps:

1. Scale the video:
   - For`FIT_*`scale types, scale the video with`min(dst.width/src.width, dst.height/src.height)`.
   - For`FILL_*`scale types, scale the video with`max(dst.width/src.width, dst.height/src.height)`.
2. Align the scaled video with the destination`PreviewView`:
   - For`FIT_CENTER/FILL_CENTER`, center align the scaled video and the destination`PreviewView`.
   - For`FIT_START/FILL_START`, align the scaled video and the destination`PreviewView`with respect to the top-left corner of each.
   - For`FIT_END/FILL_END`, align the scaled video and the destination`PreviewView`with respect to the bottom-right corner of each.

For example, here is a 640x480 source video and a 1920x1080 destination`PreviewView`:

![Image showing a 640x480 video compared to a 1920x1080 preview](https://developer.android.com/static/images/training/camera/camerax/camera-preview/camera_preview_view_scale_type_default.png)

The following image shows the`FIT_START`/`FIT_CENTER`/`FIT_END`scaling process:

![Image showing the FIT_START, FIT_CENTER, and FIT_END scaling process](https://developer.android.com/static/images/training/camera/camerax/camera-preview/camera_preview_view_scale_type_fit.png)

The process works like this:

1. Scale the video frame (maintaining the original aspect ratio) with`min(1920/640, 1080/480) = 2.25`to get an intermediate video frame of 1440x1080.
2. Align the 1440x1080 video frame with the 1920x1080`PreviewView`.
   - For`FIT_CENTER`, align the video frame with the**center** of the`PreviewView`window. The starting and ending 240 pixel columns of the`PreviewView`are blank.
   - For`FIT_START`, align the video frame with the**start** (top-left corner) of the`PreviewView`window. The ending 480 pixel columns of the`PreviewView`are blank.
   - For`FIT_END`, align the video frame with the**end** (bottom-right corner) of the`PreviewView`window. The starting 480 pixel columns of the`PreviewView`are blank.

The following image shows the`FILL_START`/`FILL_CENTER`/`FILL_END`scaling process:

![Image showing the FILL_START, FILL_CENTER, and FILL_END scaling process](https://developer.android.com/static/images/training/camera/camerax/camera-preview/camera_preview_view_scale_type_fill.png)

The process works like this:

1. Scale the video frame with`max(1920/640, 1080/480) = 3`to get an intermediate video frame of 1920x1440 (which is larger than the size of the`PreviewView`).
2. Crop the 1920x1440 video frame to fit the 1920x1080`PreviewView`window.
   - For`FILL_CENTER`, crop 1920x1080 from the**center**of the 1920x1440 scaled video. The top and bottom 180 lines of video are not visible.
   - For`FILL_START`, crop 1920x1080 from the**start**of the 1920x1440 scaled video. The bottom 360 lines of video are not visible.
   - For`FILL_END`, crop 1920x1080 from the**end**of the 1920x1440 scaled video. The top 360 lines of video are not visible.

## Additional resources

To learn more about CameraX, see the following additional resources.

### Codelab

<br />

- [Getting Started with CameraX](https://codelabs.developers.google.com/codelabs/camerax-getting-started)

### Code sample

- [CameraX sample apps](https://github.com/android/camera-samples/)