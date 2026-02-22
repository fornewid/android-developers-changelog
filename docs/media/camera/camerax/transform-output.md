---
title: https://developer.android.com/media/camera/camerax/transform-output
url: https://developer.android.com/media/camera/camerax/transform-output
source: md.txt
---

The output of a CameraX use case is twofold: the buffer and the transformation
info. The buffer is a byte array and the transformation info is how the buffer
should be cropped and rotated before being shown to end users. How to apply the
transformation depends on the format of the buffer.

## ImageCapture

For the `ImageCapture` use case, the crop rect buffer is applied before saving
to disk and the rotation is saved in the Exif data. There is no additional
action needed from the app.

## Preview

For the `Preview` use case, you can get the transformation information by
calling
[`SurfaceRequest.setTransformationInfoListener()`](https://developer.android.com/reference/androidx/camera/core/SurfaceRequest#setTransformationInfoListener(java.util.concurrent.Executor,%20androidx.camera.core.SurfaceRequest.TransformationInfoListener)).
Every time the transformation is updated, the caller receives a new
[`SurfaceRequest.TransformationInfo`](https://developer.android.com/reference/androidx/camera/core/SurfaceRequest.TransformationInfo)
object.

How to apply the transformation information depends on the source of the
`Surface`, and is usually non-trivial. If the goal is to simply display the
preview, use `PreviewView`. `PreviewView` is a custom view that automatically
handles transformation. For advanced uses, when you need to edit the preview
stream, such as with OpenGL, look at the code sample in the [CameraX core test
app](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/camera/integration-tests/coretestapp/src/main/java/androidx/camera/integration/core).

## Transform coordinates

Another common task is to work with the coordinates instead of the buffer, such
as drawing a box around the detected face in preview. In cases such as this, you
need to transform the coordinates of the detected face from image analysis to
preview.

The following code snippet creates a matrix that maps from image analysis
coordinates to `PreviewView` coordinates. To transform the (x, y) coordinates
with a [`Matrix`](https://developer.android.com/reference/android/graphics/Matrix), see
[`Matrix.mapPoints()`](https://developer.android.com/reference/android/graphics/Matrix#mapPoints(float%5B%5D)).  

### Kotlin

```kotlin
fun getCorrectionMatrix(imageProxy: ImageProxy, previewView: PreviewView) : Matrix {
   val cropRect = imageProxy.cropRect
   val rotationDegrees = imageProxy.imageInfo.rotationDegrees
   val matrix = Matrix()

   // A float array of the source vertices (crop rect) in clockwise order.
   val source = floatArrayOf(
       cropRect.left.toFloat(),
       cropRect.top.toFloat(),
       cropRect.right.toFloat(),
       cropRect.top.toFloat(),
       cropRect.right.toFloat(),
       cropRect.bottom.toFloat(),
       cropRect.left.toFloat(),
       cropRect.bottom.toFloat()
   )

   // A float array of the destination vertices in clockwise order.
   val destination = floatArrayOf(
       0f,
       0f,
       previewView.width.toFloat(),
       0f,
       previewView.width.toFloat(),
       previewView.height.toFloat(),
       0f,
       previewView.height.toFloat()
   )

   // The destination vertexes need to be shifted based on rotation degrees. The
   // rotation degree represents the clockwise rotation needed to correct the image.

   // Each vertex is represented by 2 float numbers in the vertices array.
   val vertexSize = 2
   // The destination needs to be shifted 1 vertex for every 90° rotation.
   val shiftOffset = rotationDegrees / 90 * vertexSize;
   val tempArray = destination.clone()
   for (toIndex in source.indices) {
       val fromIndex = (toIndex + shiftOffset) % source.size
       destination[toIndex] = tempArray[fromIndex]
   }
   matrix.setPolyToPoly(source, 0, destination, 0, 4)
   return matrix
}
```

### Java

```java
Matrix getMappingMatrix(ImageProxy imageProxy, PreviewView previewView) {
   Rect cropRect = imageProxy.getCropRect();
   int rotationDegrees = imageProxy.getImageInfo().getRotationDegrees();
   Matrix matrix = new Matrix();

   // A float array of the source vertices (crop rect) in clockwise order.
   float[] source = {
       cropRect.left,
       cropRect.top,
       cropRect.right,
       cropRect.top,
       cropRect.right,
       cropRect.bottom,
       cropRect.left,
       cropRect.bottom
   };

   // A float array of the destination vertices in clockwise order.
   float[] destination = {
       0f,
       0f,
       previewView.getWidth(),
       0f,
       previewView.getWidth(),
       previewView.getHeight(),
       0f,
       previewView.getHeight()
   };

   // The destination vertexes need to be shifted based on rotation degrees.
   // The rotation degree represents the clockwise rotation needed to correct
   // the image.

   // Each vertex is represented by 2 float numbers in the vertices array.
   int vertexSize = 2;
   // The destination needs to be shifted 1 vertex for every 90° rotation.
   int shiftOffset = rotationDegrees / 90 * vertexSize;
   float[] tempArray = destination.clone();
   for (int toIndex = 0; toIndex < source.length; toIndex++) {
       int fromIndex = (toIndex + shiftOffset) % source.length;
       destination[toIndex] = tempArray[fromIndex];
   }
   matrix.setPolyToPoly(source, 0, destination, 0, 4);
   return matrix;
}
```