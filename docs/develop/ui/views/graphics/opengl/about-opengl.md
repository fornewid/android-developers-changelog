---
title: https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl
url: https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl
source: md.txt
---

Android includes support for high performance 2D and 3D graphics with the Open Graphics Library
(OpenGL®), specifically, the OpenGL ES API. OpenGL is a cross-platform graphics API that
specifies a
standard software interface for 3D graphics processing hardware. OpenGL ES is a flavor of the OpenGL
specification intended for embedded devices. Android supports several versions of the OpenGL ES
API:

- OpenGL ES 2.0 - This API specification is supported by Android 2.2 (API level 8) and higher.
- OpenGL ES 3.0 - This API specification is supported by Android 4.3 (API level 18) and higher.
- OpenGL ES 3.1 - This API specification is supported by Android 5.0 (API level 21) and higher.
- OpenGL ES 3.2 - This API specification is supported by Android 7.0 (API level 24) and higher.

**Caution:**
Regardless of the Android platform version, a device cannot support
the OpenGL ES 3.0 API unless the device manufacturer provides an
implementation of this graphics pipeline. If you specify in the manifest that
OpenGL ES 3.0 is required, you can be sure that that version will be present
on the device. If you specify that a lower-level version is required but you
want to use 3.0 features if they're available, you should check at run time
to see what version of OpenGL the device supports. For information on how to
do this, see [Checking OpenGL ES version](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#version-check).

**Note:**
Android includes support for OpenGL ES 1.0 and 1.1, but these versions of the API
are deprecated and shouldn't be used by modern applications.

**Note:**
The specific API provided by the Android framework is similar to the J2ME JSR239 OpenGL ES API,
but isn't identical. If you are familiar with J2ME JSR239 specification, be alert for
variations.

Also see

- [Displaying graphics with OpenGL ES](https://developer.android.com/training/graphics/opengl)
- [OpenGL ES](http://www.khronos.org/opengles/)
- [OpenGL ES 2.x specification](http://www.khronos.org/opengles/2_X/)
- [OpenGL ES 3.x specification](http://www.khronos.org/opengles/3_X/)

## The basics

Android supports OpenGL both through its framework API and the Native Development
Kit (NDK). This topic focuses on the Android framework interfaces. For more information about the
NDK, see the [Android NDK](https://developer.android.com/tools/sdk/ndk).

There are two foundational classes in the Android framework that let you create and manipulate
graphics with the OpenGL ES API: `https://developer.android.com/reference/android/opengl/GLSurfaceView` and
`https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer`. If your goal is to use OpenGL in your Android application,
understanding how to implement these classes in an activity should be your first objective.

**`https://developer.android.com/reference/android/opengl/GLSurfaceView`**
:   This class is a `https://developer.android.com/reference/android/view/View` where you can draw and manipulate objects using
    OpenGL API calls and is similar in function to a `https://developer.android.com/reference/android/view/SurfaceView`. You can use
    this class by creating an instance of `https://developer.android.com/reference/android/opengl/GLSurfaceView` and adding your
    `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer` to it. However, if you want to capture
    touch screen events, you should extend the `https://developer.android.com/reference/android/opengl/GLSurfaceView` class to
    implement the touch listeners, as shown in OpenGL training lesson,
    [Responding to touch events](https://developer.android.com/training/graphics/opengl/touch).

**`https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer`**
:   This interface defines the methods required for drawing graphics in a `https://developer.android.com/reference/android/opengl/GLSurfaceView`. You must provide an implementation of this interface as a
    separate class and attach it to your `https://developer.android.com/reference/android/opengl/GLSurfaceView` instance using
    `https://developer.android.com/reference/android/opengl/GLSurfaceView#setRenderer(android.opengl.GLSurfaceView.Renderer)`.

    The `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer` interface requires that you implement the
    following methods:

    - `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig)`: The system calls this method once, when creating the `https://developer.android.com/reference/android/opengl/GLSurfaceView`. Use this method to perform actions that need to happen only once, such as setting OpenGL environment parameters or initializing OpenGL graphic objects.
    - `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onDrawFrame(javax.microedition.khronos.opengles.GL10)`: The system calls this method on each redraw of the `https://developer.android.com/reference/android/opengl/GLSurfaceView`. Use this method as the primary execution point for drawing (and re-drawing) graphic objects.
    - `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceChanged(javax.microedition.khronos.opengles.GL10, int, int)`: The system calls this method when the `https://developer.android.com/reference/android/opengl/GLSurfaceView` geometry changes, including changes in size of the `https://developer.android.com/reference/android/opengl/GLSurfaceView` or orientation of the device screen. For example, the system calls this method when the device changes from portrait to landscape orientation. Use this method to respond to changes in the `https://developer.android.com/reference/android/opengl/GLSurfaceView` container.

### OpenGL ES packages

Once you have established a container view for OpenGL ES using `https://developer.android.com/reference/android/opengl/GLSurfaceView` and `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer`, you can begin
calling OpenGL APIs using the following classes:

- OpenGL ES 2.0 API Class
  - `https://developer.android.com/reference/android/opengl/GLES20` - This package provides the interface to OpenGL ES 2.0 and is available starting with Android 2.2 (API level 8).
- OpenGL ES 3.0/3.1/3.2 API Packages
  - `https://developer.android.com/reference/android/opengl/package-summary` - This package provides the interface to the OpenGL ES 3.0/3.1 classes. Version 3.0 is available starting with Android 4.3 (API level 18). Version 3.1 is available starting with Android 5.0 (API level 21). Version 3.2 is available starting with Android 7.0 (API level 24).
    - `https://developer.android.com/reference/android/opengl/GLES30`
    - `https://developer.android.com/reference/android/opengl/GLES31`
    - `https://developer.android.com/reference/android/opengl/GLES31Ext` ([Android Extension Pack](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#aep))
    - `https://developer.android.com/reference/android/opengl/GLES32`

If you want to start building an app with OpenGL ES right away, follow the
[Displaying graphics with OpenGL ES](https://developer.android.com/training/graphics/opengl)
class.

## Declaring OpenGL requirements

If your application uses OpenGL features that are not available on all devices, you must include
these requirements in your [AndroidManifest.xml](https://developer.android.com/guide/topics/manifest/manifest-intro)
file. Here are the most common OpenGL manifest declarations:

- **OpenGL ES version requirements** - If your application requires a specific version of OpenGL ES, you must declare that requirement by adding the following settings to your manifest as shown below.

  For OpenGL ES 2.0:

  ```xml
  <!-- Tell the system this app requires OpenGL ES 2.0. -->
  <uses-feature android:glEsVersion="0x00020000" android:required="true" />
  ```

  Adding this declaration causes Google Play to restrict your application from being
  installed on devices that do not support OpenGL ES 2.0. If your application is exclusively for
  devices that support OpenGL ES 3.0, you can also specify this in your manifest:

  For OpenGL ES 3.0:

  ```xml
  <!-- Tell the system this app requires OpenGL ES 3.0. -->
  <uses-feature android:glEsVersion="0x00030000" android:required="true" />
  ```

  For OpenGL ES 3.1:

  ```xml
  <!-- Tell the system this app requires OpenGL ES 3.1. -->
  <uses-feature android:glEsVersion="0x00030001" android:required="true" />
  ```

  For OpenGL ES 3.2:

  ```xml
  <!-- Tell the system this app requires OpenGL ES 3.2. -->
  <uses-feature android:glEsVersion="0x00030002" android:required="true" />
  ```

  **Note:**
  The OpenGL ES 3.x API is backwards-compatible with the 2.0 API, which means you can be more
  flexible with your implementation of OpenGL ES in your application. By declaring the OpenGL
  ES 2.0 API as a requirement in your manifest, you can use that API version as a default, check
  for the availability of the 3.x API at run time and then use OpenGL ES 3.x features if the
  device supports it. For more information about checking the OpenGL ES version supported by a
  device, see [Checking OpenGL ES version](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#version-check).
- **Texture compression requirements** - If your application uses texture compression formats, you must declare the formats your application supports in your manifest file using [`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element). For more information about available texture compression formats, see [Texture compression support](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#textures).

  Declaring texture compression requirements in your manifest hides your application from users
  with devices that do not support at least one of your declared compression types. For more
  information on how Google Play filtering works for texture compressions, see the
  [Google Play and texture compression filtering](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element#market-texture-filtering) section of the `<supports-gl-texture>` documentation.

## Mapping coordinates for drawn objects

One of the basic problems in displaying graphics on Android devices is that their screens can
vary in size and shape. OpenGL assumes a square, uniform coordinate system and, by default, happily
draws those coordinates onto your typically non-square screen as if it is perfectly square.
![](https://developer.android.com/static/images/opengl/coordinates.png)


**Figure 1.** Default OpenGL coordinate system (left) mapped to a typical Android
device screen (right).

The illustration above shows the uniform coordinate system assumed for an OpenGL frame on the
left, and how these coordinates actually map to a typical device screen in landscape orientation
on the right. To solve this problem, you can apply OpenGL projection modes and camera views to
transform coordinates so your graphic objects have the correct proportions on any display.

In order to apply projection and camera views, you create a projection matrix and a camera view
matrix and apply them to the OpenGL rendering pipeline. The projection matrix recalculates the
coordinates of your graphics so that they map correctly to Android device screens. The camera view
matrix creates a transformation that renders objects from a specific eye position.

### Projection and camera view in OpenGL ES 2.0 and higher

In the ES 2.0 and 3.0 APIs, you apply projection and camera view by first adding a matrix member
to the vertex shaders of your graphics objects. With this matrix member added, you can then
generate and apply projection and camera viewing matrices to your objects.

1. **Add matrix to vertex shaders** - Create a variable for the view projection matrix and include it as a multiplier of the shader's position. In the following example vertex shader code, the included `uMVPMatrix` member allows you to apply projection and camera viewing matrices to the coordinates of objects that use this shader.

   ### Kotlin

   ```kotlin
   private val vertexShaderCode =

       // This matrix member variable provides a hook to manipulate
       // the coordinates of objects that use this vertex shader.
       "uniform mat4 uMVPMatrix;   \n" +

       "attribute vec4 vPosition;  \n" +
       "void main(){               \n" +
       // The matrix must be included as part of gl_Position
       // Note that the uMVPMatrix factor *must be first* in order
       // for the matrix multiplication product to be correct.
       " gl_Position = uMVPMatrix * vPosition; \n" +

       "}  \n"
   ```

   ### Java

   ```java
   private final String vertexShaderCode =

       // This matrix member variable provides a hook to manipulate
       // the coordinates of objects that use this vertex shader.
       "uniform mat4 uMVPMatrix;   \n" +

       "attribute vec4 vPosition;  \n" +
       "void main(){               \n" +
       // The matrix must be included as part of gl_Position
       // Note that the uMVPMatrix factor *must be first* in order
       // for the matrix multiplication product to be correct.
       " gl_Position = uMVPMatrix * vPosition; \n" +

       "}  \n";
   ```

   **Note:** The example above defines a single transformation matrix
   member in the vertex shader into which you apply a combined projection matrix and camera view
   matrix. Depending on your application requirements, you may want to define separate projection
   matrix and camera viewing matrix members in your vertex shaders so you can change them
   independently.
2. **Access the shader matrix** - After creating a hook in your vertex shaders to apply projection and camera view, you can then access that variable to apply projection and camera viewing matrices. The following code shows how to modify the `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig)` method of a `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer` implementation to access the matrix variable defined in the vertex shader above.

   ### Kotlin

   ```kotlin
   override fun onSurfaceCreated(gl: GL10, config: EGLConfig) {
       ...
       muMVPMatrixHandle = GLES20.glGetUniformLocation(program, "uMVPMatrix")
       ...
   }
   ```

   ### Java

   ```java
   public void onSurfaceCreated(GL10 unused, EGLConfig config) {
       ...
       muMVPMatrixHandle = GLES20.glGetUniformLocation(program, "uMVPMatrix");
       ...
   }
   ```
3. **Create projection and camera viewing matrices** - Generate the projection and viewing matrices to be applied the graphic objects. The following example code shows how to modify the `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig)` and `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceChanged(javax.microedition.khronos.opengles.GL10, int, int)` methods of a `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer` implementation to create camera view matrix and a projection matrix based on the screen aspect ratio of the device.

   ### Kotlin

   ```kotlin
   override fun onSurfaceCreated(gl: GL10, config: EGLConfig) {
       ...
       // Create a camera view matrix
       Matrix.setLookAtM(vMatrix, 0, 0f, 0f, -3f, 0f, 0f, 0f, 0f, 1.0f, 0.0f)
   }

   override fun onSurfaceChanged(gl: GL10, width: Int, height: Int) {
       GLES20.glViewport(0, 0, width, height)

       val ratio: Float = width.toFloat() / height.toFloat()

       // create a projection matrix from device screen geometry
       Matrix.frustumM(projMatrix, 0, -ratio, ratio, -1f, 1f, 3f, 7f)
   }
   ```

   ### Java

   ```java
   public void onSurfaceCreated(GL10 unused, EGLConfig config) {
       ...
       // Create a camera view matrix
       Matrix.setLookAtM(vMatrix, 0, 0, 0, -3, 0f, 0f, 0f, 0f, 1.0f, 0.0f);
   }

   public void onSurfaceChanged(GL10 unused, int width, int height) {
       GLES20.glViewport(0, 0, width, height);

       float ratio = (float) width / height;

       // create a projection matrix from device screen geometry
       Matrix.frustumM(projMatrix, 0, -ratio, ratio, -1, 1, 3, 7);
   }
   ```
4. **Apply projection and camera viewing matrices** - To apply the projection and camera view transformations, multiply the matrices together and then set them into the vertex shader. The following example code shows how modify the `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onDrawFrame(javax.microedition.khronos.opengles.GL10)` method of a `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer` implementation to combine the projection matrix and camera view created in the code above and then apply it to the graphic objects to be rendered by OpenGL.

   ### Kotlin

   ```kotlin
   override fun onDrawFrame(gl: GL10) {
       ...
       // Combine the projection and camera view matrices
       Matrix.multiplyMM(vPMatrix, 0, projMatrix, 0, vMatrix, 0)

       // Apply the combined projection and camera view transformations
       GLES20.glUniformMatrix4fv(muMVPMatrixHandle, 1, false, vPMatrix, 0)

       // Draw objects
       ...
   }
   ```

   ### Java

   ```java
   public void onDrawFrame(GL10 unused) {
       ...
       // Combine the projection and camera view matrices
       Matrix.multiplyMM(vPMatrix, 0, projMatrix, 0, vMatrix, 0);

       // Apply the combined projection and camera view transformations
       GLES20.glUniformMatrix4fv(muMVPMatrixHandle, 1, false, vPMatrix, 0);

       // Draw objects
       ...
   }
   ```

For a complete example of how to apply projection and camera view with OpenGL ES 2.0, see the [Displaying graphics with OpenGL ES](https://developer.android.com/training/graphics/opengl)
class.

## Shape faces and winding

In OpenGL, the face of a shape is a surface defined by three or more points in three-dimensional
space. A set of three or more three-dimensional points (called vertices in OpenGL) have a front face
and a back face. How do you know which face is front and which is the back? Good question. The
answer has to do with winding, or, the direction in which you define the points of a shape.
![Coordinates at
vertices of a triangle](https://developer.android.com/static/images/opengl/ccw-winding.png)


**Figure 1.** Illustration of a coordinate list which translates into a
counterclockwise drawing order.

In this example, the points of the triangle are defined in an order such that they are drawn in a
counterclockwise direction. The order in which these coordinates are drawn defines the winding
direction for the shape. By default, in OpenGL, the face which is drawn counterclockwise is the
front face. The triangle shown in Figure 1 is defined so that you are looking at the front face of
the shape (as interpreted by OpenGL) and the other side is the back face.

Why is it important to know which face of a shape is the front face? The answer has to do with a
commonly used feature of OpenGL, called face culling. Face culling is an option for the OpenGL
environment which allows the rendering pipeline to ignore (not calculate or draw) the back face of a
shape, saving time, memory and processing cycles:

### Kotlin

```kotlin
gl.apply {
    // enable face culling feature
    glEnable(GL10.GL_CULL_FACE)
    // specify which faces to not draw
    glCullFace(GL10.GL_BACK)
}
```

### Java

```java
// enable face culling feature
gl.glEnable(GL10.GL_CULL_FACE);
// specify which faces to not draw
gl.glCullFace(GL10.GL_BACK);
```

If you try to use the face culling feature without knowing which sides of your shapes are the
front and back, your OpenGL graphics are going to look a bit thin, or possibly not show up at all.
So, always define the coordinates of your OpenGL shapes in a counterclockwise drawing order.

**Note:** It is possible to set an OpenGL environment to treat the
clockwise face as the front face, but doing so requires more code and is likely to confuse
experienced OpenGL developers when you ask them for help. So don't do that.

## OpenGL versions and device compatibility

The OpenGL ES 1.0 and 1.1 API specifications have been supported since Android 1.0.
Graphics programming with OpenGL ES 1.0/1.1 API is significantly different than using the 2.0
and higher versions.
OpenGL ES 2.0 is supported by all Android devices beginning with Android 2.2 (API level 8) and is
the earliest version recommended for new applications being developed with OpenGL ES.
OpenGL ES 3.0 is supported with Android 4.3 (API level 18) and higher, on devices that provide an
implementation of the OpenGL ES 3.0 API.
For information about the relative number of Android-powered devices
that support a given version of OpenGL ES, see the
[OpenGL ES version dashboard](https://developer.android.com/about/dashboards#OpenGL).

You should carefully consider the graphics requirements and choose the API
version that works best for your application. For more information, see
[Choosing an OpenGL API version](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#choosing-version).

The OpenGL ES 3.0 API provides additional features and better performance than the 2.0 API and is
also backward compatible. This means that you can potentially write your application targeting
OpenGL ES 2.0 and conditionally include OpenGL ES 3.0 graphics features if they are available. For
more information on checking for availability of the 3.0 API, see
[Checking OpenGL ES version](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#version-check)

### Texture compression support

Texture compression can significantly increase the performance of your OpenGL application by
reducing memory requirements and making more efficient use of memory bandwidth. The Android
framework provides support for the ETC1 compression format as a standard feature, including a
`https://developer.android.com/reference/android/opengl/ETC1Util` utility class and the `etc1tool` compression tool (located in the
Android SDK at `<sdk>/tools/`). For an example of an Android application that uses
texture compression, see the `CompressedTextureActivity` code sample in Android SDK
(`<sdk>/samples/<version>/ApiDemos/src/com/example/android/apis/graphics/`).

The ETC1 format is supported by all Android devices that support OpenGL ES 2.0 or higher.

**Note:** The ETC1 texture compression format does not support textures with a
transparency (alpha channel). If your application requires textures with transparency, you should
investigate other texture compression formats available on your target devices. A
method of rendering alpha channel textures using ETC1 is to bind two ETC1 texture objects: the
first with color data, the second with alpha channel data and then combine the values from the two
textures in the fragment shader.

The ETC2/EAC texture compression formats are guaranteed to be available when using the OpenGL ES
3.0 API. This texture format offers excellent compression ratios with high visual quality and the
format also supports transparency (alpha channel).

Beyond the ETC formats, Android devices have varied support for texture compression based on
their GPU chipsets and OpenGL implementations. You should investigate texture compression support on
the devices you are are targeting to determine what compression types your application should
support. In order to determine what texture formats are supported on a given device, you must
[query the device](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#gl-extension-query) and review the *OpenGL extension names*,
which identify what texture compression formats (and other OpenGL features) are supported by the
device. Some commonly supported texture compression formats are as follows:

- **Adaptable Scalable Texture Compression (ASTC)** - A texture compression format designed to supersede prior formats. More flexible than previous formats due to support for various block sizes.
  - `GL_KHR_texture_compression_astc_ldr`
  - `GL_KHR_texture_compression_astc_hdr`(high dynamic range)
- **S3TC (DXT*n*/DXTC)** - S3 texture compression (S3TC) has several format variations (DXT1 to DXT5) and is less widely available. The format supports RGB textures with 4-bit alpha or 8-bit alpha channels. These formats are represented by the following OpenGL extension name:
  - `GL_EXT_texture_compression_s3tc`

  Some devices only support the DXT1 format variation; this limited support is represented by the following OpenGL extension name:
  <!-- -->

  - `GL_EXT_texture_compression_dxt1`

The following texture compression formats are considered legacy formats and aren't recommended
for use in new applications:

- **ATITC (ATC)** - ATI texture compression (ATITC or ATC) is available on a wide variety of devices and supports fixed rate compression for RGB textures with and without an alpha channel. This format may be represented by several OpenGL extension names, for example:
  - `GL_AMD_compressed_ATC_texture`
  - `GL_ATI_texture_compression_atitc`
- **PVRTC** - PowerVR texture compression (PVRTC) is available on a wide variety of devices and supports 2-bit and 4-bit per pixel textures with or without an alpha channel. This format is represented by the following OpenGL extension name:
  - `GL_IMG_texture_compression_pvrtc`
- **3DC** - 3DC texture compression (3DC) is a less widely available format that supports RGB textures with an alpha channel. This format is represented by the following OpenGL extension name:
  - `GL_AMD_compressed_3DC_texture`

**Warning:** These texture compression formats are *not
supported* on all devices. Support for these formats can vary by manufacturer and device. For
information on how to determine what texture compression formats are on a particular device, see
the next section.

**Note:** Once you decide which texture compression formats your
application will support, make sure you declare them in your manifest using
[\<supports-gl-texture\>](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element). Using this declaration enables filtering by external services such as Google Play, so that
your app is installed only on devices that support the formats your app requires. For details, see
[OpenGL manifest declarations](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#manifest).

### Determining OpenGL extensions

Implementations of OpenGL vary by Android device in terms of the extensions to the OpenGL ES API
that are supported. These extensions include texture compressions, but typically also include other
extensions to the OpenGL feature set.

To determine what texture compression formats, and other OpenGL extensions, are supported on a
particular device:

1. Run the following code on your target devices to determine what texture compression formats are supported:

   ### Kotlin

   ```kotlin
   var extensions = gl.glGetString(GL10.GL_EXTENSIONS)
   ```

   ### Java

   ```java
   String extensions = gl.glGetString(GL10.GL_EXTENSIONS);
   ```

   **Warning:** The results of this call *vary by device model!* You
   must run this call on several target devices to determine what compression types are commonly
   supported.
2. Review the output of this method to determine what OpenGL extensions are supported on the device.

#### Android Extension Pack (AEP)

The AEP ensures that your application supports a standardized set of OpenGL extensions above
and beyond
the core set described in the OpenGL 3.1 specification. Packaging these extensions together
encourages a consistent set of functionality across devices, while allowing developers to take full
advantage of the latest crop of mobile GPU devices.

The AEP also improves support for images, shader storage buffers, and atomic counters in
fragment shaders.

For your app to be able to use the AEP, the app's manifest must declare that the AEP is required.
In addition, the platform version must support it.

All of the additional features specified in the AEP are included in the base OpenGL ES 3.2
specification. If your app requires OpenGL ES 3.2 you do not need to require the AEP.

Declare the AEP requirement in the manifest as follows:

```xml
<uses-feature android:name="android.hardware.opengles.aep"
              android:required="true" />
```

To verify that the platform version supports the AEP, use the
`https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)` method, passing in
`https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_OPENGLES_EXTENSION_PACK` as the argument. The following code snippet
shows an example of how to do so:

### Kotlin

```kotlin
var deviceSupportsAEP: Boolean =
        packageManager.hasSystemFeature(PackageManager.FEATURE_OPENGLES_EXTENSION_PACK)
```

### Java

```java
boolean deviceSupportsAEP = getPackageManager().hasSystemFeature
     (PackageManager.FEATURE_OPENGLES_EXTENSION_PACK);
```

If the method returns true, AEP is supported.


For more information about the AEP, visit its page at the
[Khronos OpenGL ES Registry](https://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt).


### Checking the OpenGL ES version

There are several versions of OpenGL ES available on Android devices. You can specify the
minimum version of the API your application requires in your [manifest](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#manifest), but
you may also want to take advantage of features in a newer API at the same time. For example,
the OpenGL ES 3.0 API is backward-compatible with the 2.0 version of the API, so you may want to
write your application so that it uses OpenGL ES 3.0 features, but falls back to the 2.0 API if the
3.0 API is not available.

Before using OpenGL ES features from a version higher than the minimum required in your
application manifest, your application should check the version of the API available on the device.
You can do this in one of two ways:

1. Attempt to create the higher-level OpenGL ES context (`https://developer.android.com/reference/android/opengl/EGLContext`) and check the result.
2. Create a minimum-supported OpenGL ES context and check the version value.

The following example code demonstrates how to check the available OpenGL ES version by creating
an `https://developer.android.com/reference/android/opengl/EGLContext` and checking the result. This example shows how to check for
OpenGL ES 3.0 version:

### Kotlin

```kotlin
private const val EGL_CONTEXT_CLIENT_VERSION = 0x3098
private const val glVersion = 3.0
private class ContextFactory : GLSurfaceView.EGLContextFactory {

    override fun createContext(egl: EGL10, display: EGLDisplay, eglConfig: EGLConfig): EGLContext {

        Log.w(TAG, "creating OpenGL ES $glVersion context")
        return egl.eglCreateContext(
                display,
                eglConfig,
                EGL10.EGL_NO_CONTEXT,
                intArrayOf(EGL_CONTEXT_CLIENT_VERSION, glVersion.toInt(), EGL10.EGL_NONE)
        ) // returns null if 3.0 is not supported
    }
}
```

### Java

```java
private static double glVersion = 3.0;

private static class ContextFactory implements GLSurfaceView.EGLContextFactory {

  private static int EGL_CONTEXT_CLIENT_VERSION = 0x3098;

  public EGLContext createContext(
          EGL10 egl, EGLDisplay display, EGLConfig eglConfig) {

      Log.w(TAG, "creating OpenGL ES " + glVersion + " context");
      int[] attrib_list = {EGL_CONTEXT_CLIENT_VERSION, (int) glVersion,
              EGL10.EGL_NONE };
      // attempt to create a OpenGL ES 3.0 context
      EGLContext context = egl.eglCreateContext(
              display, eglConfig, EGL10.EGL_NO_CONTEXT, attrib_list);
      return context; // returns null if 3.0 is not supported;
  }
}
```

If the `createContext()` method show above returns null, your code should create a OpenGL
ES 2.0 context instead and fall back to using only that API.

The following code example demonstrates how to check the OpenGL ES version by creating a minimum
supported context first, and then checking the version string:

### Kotlin

```kotlin
// Create a minimum supported OpenGL ES context, then check:
gl.glGetString(GL10.GL_VERSION).also {
    Log.w(TAG, "Version: $it")
}
 // The version format is displayed as: "OpenGL ES <major>.<minor>"
 // followed by optional content provided by the implementation.
```

### Java

```java
// Create a minimum supported OpenGL ES context, then check:
String version = gl.glGetString(GL10.GL_VERSION);
Log.w(TAG, "Version: " + version );
// The version format is displayed as: "OpenGL ES <major>.<minor>"
// followed by optional content provided by the implementation.
```

With this approach, if you discover that the device supports a higher-level API version, you
must destroy the minimum OpenGL ES context and create a new context with the higher
available API version.

## Choosing an OpenGL API version

OpenGL ES version 2.0, and version 3.0 both provide high
performance graphics interfaces for creating 3D games, visualizations and user interfaces. Graphics
progamming for OpenGL ES 2.0 and 3.0 is largely similar, with version 3.0 representing a superset
of the 2.0 API with additional features. Programming for the OpenGL ES 1.0/1.1 API versus OpenGL ES
2.0 and 3.0 differs significantly, and isn't recommended for new applications.
Developers should carefully consider the following factors before starting development with
these APIs:

- **Device Compatibility** - Developers should consider the types of devices, Android versions and the OpenGL ES versions available to their customers. For more information on OpenGL compatibility across devices, see the [OpenGL versions and
  device compatibility](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#compatibility) section.
- **Texture Support** - The OpenGL ES 3.0 API has the best support for texture compression because it guarantees availability of the ETC2 compression format, which supports transparency. The 2.0 API implementations include support for ETC1, however this texture format doesn't support transparency. To implement transparency with compressed textures you must either use two ETC1 textures (split between color and alpha) or provide resources in other compression formats supported by the devices you are targeting. For more information, see [Texture compression support](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#textures).

While compatibility, and texture support may influence your
decision, you should pick an OpenGL API version based on what you think provides the best experience
for your users.