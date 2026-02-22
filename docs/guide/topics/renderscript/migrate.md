---
title: https://developer.android.com/guide/topics/renderscript/migrate
url: https://developer.android.com/guide/topics/renderscript/migrate
source: md.txt
---

# Migrate from RenderScript

RenderScript APIs are deprecated starting in Android 12. Device and component manufacturers have already stopped providing hardware acceleration support, and RenderScript support is expected to be removed entirely in a future release.

C/C++ performance may be adequate for many use cases, and if you were only reliant on RenderScript for intrinsics, you can replace those uses with the[RenderScript Intrinsics Replacement Toolkit](https://developer.android.com/guide/topics/renderscript/migrate#intrinsics), which is easier to use and comes with a potential 2x performance improvement!

If you need to take full advantage of GPU acceleration, we recommend[migrating your scripts to Vulkan](https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan), Other accelerated options include[migrating your scripts to OpenGL](https://developer.android.com/guide/topics/renderscript/migrate/migrate-gles), using[Canvas-based image operations](https://developer.android.com/guide/topics/renderscript/migrate#built-in), or leveraging the[Android Graphics Shading Language (AGSL)](https://developer.android.com/guide/topics/renderscript/migrate#AGSL-processing).

Following the deprecation of RenderScript in the Android platform, support for RenderScript is being removed in the Android Gradle plugin. Starting with Android Gradle plugin 7.2, the RenderScript APIs are deprecated. They continue to function, but invoke warnings. Future versions of AGP will no longer include Renderscript support. This guide explains how to migrate from RenderScript.

## Migrate from intrinsics

Although the RenderScript intrinsics functions continue to function after the RenderScript deprecation, they may execute only on the CPU rather than the GPU.

For some of these operations, there are more efficient options now built into the platform or in Jetpack libraries.

### Built-in accelerated image operations

The Android platform supports accelerated image processing operations that can be applied to images, independent of RenderScript intrinsics. Examples include:

- Blend
- Blur
- Color Matrix
- Resize

#### Image blur on Android 12+ into a View

[`RenderEffect`](https://developer.android.com/reference/android/graphics/RenderEffect "RenderEffect")with support for blur was added into Android 12, API level 31, allowing you to blur a[`RenderNode`](https://developer.android.com/reference/android/graphics/RenderNode "RenderNode").`RenderNode`is a construct of the display list that Android uses to help accelerate platform graphics.

Android provides a shortcut to applying an effect to the`RenderNode`associated with a`View`. To blur a`View`, call[`View.setRenderEffect()`](https://developer.android.com/reference/android/view/View#setRenderEffect(android.graphics.RenderEffect) "setRenderEffect"):  

    val blurRenderEffect = RenderEffect.createBlurEffect(radius, radius,
            Shader.TileMode.MIRROR
        )
    view.setRenderEffect(blurRenderEffect)

#### Image blur on Android 12+ rendered into a Bitmap

If you need the blurred image rendered into a`Bitmap`, the framework supports accelerated rendering with a[`HardwareRenderer`](https://developer.android.com/reference/android/graphics/HardwareRenderer "HardwareRenderer")backed by a[`HardwareBuffer`](https://developer.android.com/reference/android/hardware/HardwareBuffer "HardwareBuffer"). The following code creates the`HardwareRenderer`,`RenderNode`, and the`RenderEffect`for the blur:  

    val imageReader = ImageReader.newInstance(
        bitmap.width, bitmap.height,
        PixelFormat.RGBA_8888, numberOfOutputImages,
        HardwareBuffer.USAGE_GPU_SAMPLED_IMAGE or HardwareBuffer.USAGE_GPU_COLOR_OUTPUT
    )
    val renderNode = RenderNode("BlurEffect")
    val hardwareRenderer = HardwareRenderer()

    hardwareRenderer.setSurface(imageReader.surface)
    hardwareRenderer.setContentRoot(renderNode)
    renderNode.setPosition(0, 0, imageReader.width, imageReader.height)
    val blurRenderEffect = RenderEffect.createBlurEffect(
        radius, radius,
        Shader.TileMode.MIRROR
    )
    renderNode.setRenderEffect(blurRenderEffect)

Applying the effect involves using the internal[`RecordingCanvas`](https://developer.android.com/reference/android/graphics/RecordingCanvas "RecordingCanvas")for the`RenderNode`. The following code records the drawing, creates the render request, and then waits for the request to finish:  

    val renderCanvas = it.renderNode.beginRecording()
    renderCanvas.drawBitmap(it.bitmap, 0f, 0f, null)
    renderNode.endRecording()
    hardwareRenderer.createRenderRequest()
        .setWaitForPresent(true)
        .syncAndDraw()

The rendered image is in a[`HardwareBuffer`](https://developer.android.com/reference/android/hardware/HardwareBuffer "HardwareBuffer")associated with the[`ImageReader`](https://developer.android.com/reference/android/media/ImageReader "ImageReader"). The following code acquires the`Image`and returns a`Bitmap`that wraps its`HardwareBuffer`.  

    val image = imageReader.acquireNextImage() ?: throw RuntimeException("No Image")
    val hardwareBuffer = image.hardwareBuffer ?: throw RuntimeException("No HardwareBuffer")
    val bitmap = Bitmap.wrapHardwareBuffer(hardwareBuffer, null)
        ?: throw RuntimeException("Create Bitmap Failed")

The following code cleans-up after rendering the image. Note that the`ImageReader`,`RenderNode`,`RenderEffect`, and`HardwareRenderer`can be used to process multiple images.  

    hardwareBuffer.close()
    image.close()
    imageReader.close()
    renderNode.discardDisplayList()
    hardwareRenderer.destroy()

#### AGSL for image processing

The[Android Graphics Shading Language (AGSL)](https://developer.android.com/develop/ui/views/graphics/agsl)is used by Android 13+ to define the behavior of programmable[`RuntimeShader`](https://developer.android.com/reference/android/graphics/RuntimeShader)objects. AGSL shares much of its syntax with GLSL fragment shaders, but works within the Android graphics rendering system to both customize painting within`Canvas`and filter`View`content. This can be used to add custom image processing during drawing operations, or by using a`RenderNode`directly to render an image into a`Bitmap`canvas. The following example demonstrates how to apply a custom shader to replace the image blur effect.

Begin by creating a`RuntimeShader`, instantiating it with the AGSL shader code. This shader is used to apply a color matrix for hue rotation:  

    val hueShader = RuntimeShader("""
        uniform float2 iResolution;       // Viewport resolution (pixels)
        uniform float2 iImageResolution;  // iImage1 resolution (pixels)
        uniform float iRadian;            // radian to rotate things around
        uniform shader iImage1;           // An input image
        half4 main(float2 fragCoord) {
        float cosR = cos(iRadian);
        float sinR = sin(iRadian);
            mat4 hueRotation =
            mat4 (
                    0.299 + 0.701 * cosR + 0.168 * sinR, //0
                    0.587 - 0.587 * cosR + 0.330 * sinR, //1
                    0.114 - 0.114 * cosR - 0.497 * sinR, //2
                    0.0,                                 //3
                    0.299 - 0.299 * cosR - 0.328 * sinR, //4
                    0.587 + 0.413 * cosR + 0.035 * sinR, //5
                    0.114 - 0.114 * cosR + 0.292 * sinR, //6
                    0.0,                                 //7
                    0.299 - 0.300 * cosR + 1.25 * sinR,  //8
                    0.587 - 0.588 * cosR - 1.05 * sinR,  //9
                    0.114 + 0.886 * cosR - 0.203 * sinR, //10
                    0.0,                                 //11
                    0.0, 0.0, 0.0, 1.0 );                //12,13,14,15
            float2 scale = iImageResolution.xy / iResolution.xy;
            return iImage1.eval(fragCoord * scale)*hueRotation;
        }
    """)

The shader can be applied to a`RenderNode`, just like any other`RenderEffect`. The following example demonstrates how to set the uniforms in the hueShader:  

    hueShader.setFloatUniform("iImageResolution", bitmap.width.toFloat(),
        bitmap.height.toFloat())
    hueShader.setFloatUniform("iResolution", bitmap.width.toFloat(),
        bitmap.height.toFloat())
    hueShader.setFloatUniform("iRadian", radian)
    hueShader.setInputShader( "iImage1", BitmapShader(bitmap, Shader.TileMode.MIRROR,
        Shader.TileMode.MIRROR))
    val colorFilterEffect = RenderEffect.createShaderEffect(it.hueShader)
    renderNode.setRenderEffect(colorFilterEffect)

To get the`Bitmap`, the same technique is used as in the previous image blur sample.

- The internal[`RecordingCanvas`](https://developer.android.com/reference/android/graphics/RecordingCanvas "RecordingCanvas")for the`RenderNode`applies the shader.
- The`Image`is acquired, returning a`Bitmap`that wraps its`HardwareBuffer`.

### Convert from planar YUV to RGB using CameraX

Converting from[planar YUV](https://developer.android.com/reference/android/graphics/ImageFormat#YUV_420_888)to RGB for use in image processing is supported as part of the[ImageAnalysis](https://developer.android.com/training/camerax/analyze)use case within Jetpack's CameraX.

There are resources on using`ImageAnalysis`as part of the[Getting Started with CameraX](https://developer.android.com/codelabs/camerax-getting-started)codelab and in the Android camera[samples](https://github.com/android/camera-samples/)repository.

### The Renderscript intrinsics replacement toolkit

If your application uses intrinsics, you can use the standalone replacement library; our tests indicate it's faster than using the existing RenderScript CPU implementation.

The toolkit includes the following functions:

- Blend
- Blur
- Color matrix
- Convolve
- Histogram and histogramDot
- Lookup table (LUT) and LUT 3D
- Resize
- YUV to RGB

For full details and limitations, see the toolkit's[`README.md`](https://github.com/android/renderscript-intrinsics-replacement-toolkit/blob/main/README.md)and[`Toolkit.kt`](https://github.com/android/renderscript-intrinsics-replacement-toolkit/blob/main/renderscript-toolkit/src/main/java/com/google/android/renderscript/Toolkit.kt). files.

Perform the following steps to download, add, and use the library:

1. Download the[project](https://github.com/android/renderscript-intrinsics-replacement-toolkit)from GitHub.

2. Locate and build the`renderscript-toolkit module`.

   | **Note:** If you'd like to run the intrinsics on the GPU instead, refer to the examples of coding blur and color matrix in[Vulkan](https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan)or[OpenGL ES](https://developer.android.com/guide/topics/renderscript/migrate/migrate-gles).
3. Add the library to your Android Studio project by modifying the app's`build.gradle`file.

4. Invoke the appropriate method of the toolkit.

### Example: migrate from the ScriptIntrinsicBlur function

To replace the`ScriptIntrinsicBlur`function:

- To blur a bitmap, call`Toolkit.blur`.

      var blurredBitmap = Toolkit.blur(myBitmap, radius)

- If you want to blur an image represented by an array of bytes, specify the width, height, and the number of bytes per pixel.

      val outArray = Toolkit.blur(inputArray, bytesPerPixel, width, height, radius)

| **Note:** Check the toolkit documentation for the latest guidance.

## Migrate from scripts

If your use case cannot be solved with:

- The[RenderScript Intrinsics Replacement Toolkit](https://developer.android.com/guide/topics/renderscript/migrate#intrinsics)
- New APIs within the Android platform such as`RenderEffect`and`AGSL`
- Android Jetpack library APIs such as`CameraX`

And, your use case can benefit from GPU acceleration, Android supports GPU compute on cross-platform Vulkan and OpenGL ES (GLES) APIs. You may find this unnecessary because on most devices your scripts are already running on the CPU instead of the GPU: C/C++ may be faster than RenderScript, GLES, or Vulkan compute for some use cases. (or at least fast enough for your use case)

To better understand how to migrate, review the[sample app](https://github.com/android/renderscript-samples/tree/main/RenderScriptMigrationSample/). The sample demonstrates how to both blur a bitmap and do a color-matrix conversion in RenderScript, and has equivalent code in Vulkan and OpenGL.

If your application needs to support a range of releases, use RenderScript for devices running Android 6 (API level 23) and lower, and Vulkan or GLES on supported devices with Android 7 (API level 24) and higher. If your`minSdkVersion`is 24 or higher, you may not need to use RenderScript; Vulkan or GLES 3.1 can be used anywhere you need GPU compute support.
| **Note:** RenderScript provides support for CPU compute on devices that don't have GPU compute support.

Android provides SDK bindings for GLES APIs, so it is not necessary to use the NDK when working in OpenGL ES.

Vulkan doesn't provide SDK bindings, so there is no direct mapping from RenderScript to Vulkan; you write the Vulkan code using the NDK and create JNI functions to access this code from Kotlin or Java.

The following pages cover aspects of migrating from RenderScript. The sample app implements almost all of these considerations. To better understand them, compare the RenderScript and Vulkan equivalent code.

- [Migrate scripts to OpenGL ES 3.1](https://developer.android.com/guide/topics/renderscript/migrate/migrate-gles)
- [Migrate scripts to Vulkan](https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan)