---
title: https://developer.android.com/media/camera/camerax/mlkitanalyzer
url: https://developer.android.com/media/camera/camerax/mlkitanalyzer
source: md.txt
---

# ML Kit Analyzer

Google's[ML Kit](https://developers.google.com/ml-kit/guides)provides on-device machine learning Vision APIs for detecting faces, scanning barcodes, labeling images, and more. ML Kit Analyzer makes it easier to integrate ML Kit with your CameraX app.

ML Kit Analyzer is an implementation of the[`ImageAnalysis.Analyzer`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer)interface. It overrides the[default target resolution](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis.Analyzer#getDefaultTargetResolution())(if needed) to optimize for ML Kit usage, handles the coordinate transformations, and passes the frames to ML Kit, which returns the aggregated analysis results.

## Implement ML Kit Analyzer

To implement ML Kit Analyzer, we recommend using the[`CameraController`](https://developer.android.com/reference/androidx/camera/view/CameraController)class, which works with[`PreviewView`](https://developer.android.com/reference/androidx/camera/view/PreviewView)to display UI elements. When implemented using`CameraController`, ML Kit Analyzer handles the coordinate transformations between the original`ImageAnalysis`stream and`PreviewView`for you. It receives the target coordinate system from CameraX, calculates the coordinate transformation, and forwards it to ML Kit's[`Detector`](https://developers.google.com/android/reference/com/google/mlkit/vision/interfaces/Detector)class for analysis.

To use ML Kit Analyzer with`CameraController`, call[`setImageAnalysisAnalyzer()`](https://developer.android.com/reference/androidx/camera/view/CameraController#setImageAnalysisAnalyzer(java.util.concurrent.Executor,androidx.camera.core.ImageAnalysis.Analyzer))and pass it a new ML Kit Analyzer object with the following in its constructor:

- A list of ML Kit`Detector`s, which CameraX invokes sequentially in order.
- The target coordinate system that determines the coordinates of the ML Kit output:

  - [`COORDINATE_SYSTEM_VIEW_REFERENCED`](https://developer.android.com/reference/androidx/camera/view/CameraController#COORDINATE_SYSTEM_VIEW_REFERENCED()): the transformed`PreviewView`coordinates.
  - [`COORDINATE_SYSTEM_ORIGINAL`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis#COORDINATE_SYSTEM_ORIGINAL()): the original`ImageAnalysis`stream coordinates.
- An[`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor)that invokes the Consumer callback and delivers the[`MlKitAnalyzer.Result`](https://developer.android.com/reference/androidx/camera/mlkit/vision/MlKitAnalyzer.Result), or the aggregated ML Kit result of a camera frame, to the app.

- A[`Consumer`](https://developer.android.com/reference/androidx/core/util/Consumer), which CameraX invokes when there is new ML Kit output.

The following code implements ML Kit Analyzer using`CameraController`to set up a[`BarcodeScanner`](https://developers.google.com/android/reference/com/google/mlkit/vision/barcode/BarcodeScanner)to detect QR codes:  

### Kotlin

```kotlin
// create BarcodeScanner object
val options = BarcodeScannerOptions.Builder()
  .setBarcodeFormats(Barcode.FORMAT_QR_CODE)
  .build()
val barcodeScanner = BarcodeScanning.getClient(options)

cameraController.setImageAnalysisAnalyzer(
            ContextCompat.getMainExecutor(this),
            MlKitAnalyzer(
                listOf(barcodeScanner),
                COORDINATE_SYSTEM_VIEW_REFERENCED,
                ContextCompat.getMainExecutor(this)
            ) { result: MlKitAnalyzer.Result? ->
    // The value of result.getResult(barcodeScanner) can be used directly for drawing UI overlay.
    }
)
```

### Java

```java
// create BarcodeScanner object
BarcodeScannerOptions options = new BarcodeScannerOptions.Builder()
   .setBarcodeFormats(Barcode.FORMAT_QR_CODE)
   .build();
BarcodeScanner barcodeScanner = BarcodeScanning.getClient(options);

cameraController.setImageAnalysisAnalyzer(executor,
    new MlKitAnalyzer(List.of(barcodeScanner), COORDINATE_SYSTEM_VIEW_REFERENCED,
    executor, result -> {
   // The value of result.getResult(barcodeScanner) can be used directly for drawing UI overlay.
 });
```

In the code sample above, ML Kit Analyzer passes the following to`BarcodeScanner`'s`Detector`class:

- The transformation[Matrix](https://developer.android.com/reference/android/graphics/Matrix)based on`COORDINATE_SYSTEM_VIEW_REFERENCED`that represents the target coordinate system.
- The camera frames.

If`BarcodeScanner`runs into any issues, then its`Detector`[throws an error](https://developer.android.com/reference/androidx/camera/mlkit/vision/MlKitAnalyzer.Result#getThrowable(com.google.mlkit.vision.interfaces.Detector%3C?%3E)), and ML Kit Analyzer propagates it to your app. If successful, then ML Kit Analyzer returns[`MLKitAnalyzer.Result#getValue()`](https://developer.android.com/reference/androidx/camera/mlkit/vision/MlKitAnalyzer.Result#getValue(com.google.mlkit.vision.interfaces.Detector%3CT%3E)), which in this case is the[`Barcode`](https://developers.google.com/android/reference/com/google/mlkit/vision/barcode/common/Barcode)object.

You can also implement ML Kit Analyzer using the[`ImageAnalysis`](https://developer.android.com/reference/androidx/camera/core/ImageAnalysis)class that is part of`camera-core`. However, because`ImageAnalysis`is not integrated with`PreviewView`, you must manually handle the coordinate transformations. For more information, see the[ML Kit Analyzer](https://developer.android.com/reference/androidx/camera/mlkit/vision/MlKitAnalyzer)reference documentation.

## Additional resources

For a working camera app with ML Kit Analyzer functionality, see the[CameraX-MLKit](https://github.com/android/camera-samples/tree/main/CameraX-MLKit)sample.