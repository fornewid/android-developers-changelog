---
title: https://developer.android.com/develop/ui/views/graphics/opengl/environment
url: https://developer.android.com/develop/ui/views/graphics/opengl/environment
source: md.txt
---

# Build an OpenGL ES environment

In order to draw graphics with OpenGL ES in your Android application, you must create a view container for them. One of the more straight-forward ways to do this is to implement both a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)and a[GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer). A[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)is a view container for graphics drawn with OpenGL and[GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer)controls what is drawn within that view. For more information about these classes, see the[OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)developer guide.

[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)is just one way to incorporate OpenGL ES graphics into your application. For a full-screen or near-full screen graphics view, it is a reasonable choice. Developers who want to incorporate OpenGL ES graphics in a small portion of their layouts should take a look at[TextureView](https://developer.android.com/reference/android/view/TextureView). For real, do-it-yourself developers, it is also possible to build up an OpenGL ES view using[SurfaceView](https://developer.android.com/reference/android/view/SurfaceView), but this requires writing quite a bit of additional code.

This lesson explains how to complete a minimal implementation of[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)and[GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer)in a simple application activity.

## Declare OpenGL ES use in the manifest

In order for your application to use the OpenGL ES 2.0 API, you must add the following declaration to your manifest:  

```xml
<uses-feature android:glEsVersion="0x00020000" android:required="true" />
```

If your application uses texture compression, you must also declare which compression formats your app supports, so that it is only installed on compatible devices.  

```xml
<supports-gl-texture android:name="GL_OES_compressed_ETC1_RGB8_texture" />
<supports-gl-texture android:name="GL_OES_compressed_paletted_texture" />
```

For more information about texture compression formats, see the[OpenGL](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#textures)developer guide.

## Create an activity for OpenGL ES graphics

Android applications that use OpenGL ES have activities just like any other application that has a user interface. The main difference from other applications is what you put in the layout for your activity. While in many applications you might use[TextView](https://developer.android.com/reference/android/widget/TextView),[Button](https://developer.android.com/reference/android/widget/Button)and[ListView](https://developer.android.com/reference/android/widget/ListView), in an app that uses OpenGL ES, you can also add a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView).

The following code example shows a minimal implementation of an activity that uses a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)as its primary view:  

### Kotlin

```kotlin
class OpenGLES20Activity : Activity() {

    private lateinit var gLView: GLSurfaceView

    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Create a GLSurfaceView instance and set it
        // as the ContentView for this Activity.
        gLView = MyGLSurfaceView(this)
        setContentView(gLView)
    }
}
```

### Java

```java
public class OpenGLES20Activity extends Activity {

    private GLSurfaceView gLView;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Create a GLSurfaceView instance and set it
        // as the ContentView for this Activity.
        gLView = new MyGLSurfaceView(this);
        setContentView(gLView);
    }
}
```

**Note:**OpenGL ES 2.0 requires Android 2.2 (API Level 8) or higher, so make sure your Android project targets that API or higher.

## Build a GLSurfaceView object

A[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)is a specialized view where you can draw OpenGL ES graphics. It does not do much by itself. The actual drawing of objects is controlled in the[GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer)that you set on this view. In fact, the code for this object is so thin, you may be tempted to skip extending it and just create an unmodified[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)instance, but don't do that. You need to extend this class in order to capture touch events, which is covered in the[Respond to touch events](https://developer.android.com/develop/ui/views/graphics/opengl/environment#touch.html)lesson.

The essential code for a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)is minimal, so for a quick implementation, it is common to just create an inner class in the activity that uses it:  

### Kotlin

```kotlin
import android.content.Context
import android.opengl.GLSurfaceView

class MyGLSurfaceView(context: Context) : GLSurfaceView(context) {

    private val renderer: MyGLRenderer

    init {

        // Create an OpenGL ES 2.0 context
        setEGLContextClientVersion(2)

        renderer = MyGLRenderer()

        // Set the Renderer for drawing on the GLSurfaceView
        setRenderer(renderer)
    }
}
```

### Java

```java
import android.content.Context;
import android.opengl.GLSurfaceView;

class MyGLSurfaceView extends GLSurfaceView {

    private final MyGLRenderer renderer;

    public MyGLSurfaceView(Context context){
        super(context);

        // Create an OpenGL ES 2.0 context
        setEGLContextClientVersion(2);

        renderer = new MyGLRenderer();

        // Set the Renderer for drawing on the GLSurfaceView
        setRenderer(renderer);
    }
}
```

One other optional addition to your[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)implementation is to set the render mode to only draw the view when there is a change to your drawing data using the[GLSurfaceView.RENDERMODE_WHEN_DIRTY](https://developer.android.com/reference/android/opengl/GLSurfaceView#RENDERMODE_WHEN_DIRTY)setting:  

### Kotlin

```kotlin
// Render the view only when there is a change in the drawing data
renderMode = GLSurfaceView.RENDERMODE_WHEN_DIRTY
```

### Java

```java
// Render the view only when there is a change in the drawing data
setRenderMode(GLSurfaceView.RENDERMODE_WHEN_DIRTY);
```

This setting prevents the[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)frame from being redrawn until you call[requestRender()](https://developer.android.com/reference/android/opengl/GLSurfaceView#requestRender()), which is more efficient for this sample app.

## Build a renderer class

The implementation of the[GLSurfaceView.Renderer](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer)class, or renderer, within an application that uses OpenGL ES is where things start to get interesting. This class controls what gets drawn on the[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)with which it is associated. There are three methods in a renderer that are called by the Android system in order to figure out what and how to draw on a[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView):

- [onSurfaceCreated()](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig))- Called once to set up the view's OpenGL ES environment.
- [onDrawFrame()](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onDrawFrame(javax.microedition.khronos.opengles.GL10))- Called for each redraw of the view.
- [onSurfaceChanged()](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceChanged(javax.microedition.khronos.opengles.GL10, int, int))- Called if the geometry of the view changes, for example when the device's screen orientation changes.

Here is a very basic implementation of an OpenGL ES renderer, that does nothing more than draw a black background in the[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView):  

### Kotlin

```kotlin
import javax.microedition.khronos.egl.EGLConfig
import javax.microedition.khronos.opengles.GL10

import android.opengl.GLES20
import android.opengl.GLSurfaceView

class MyGLRenderer : GLSurfaceView.Renderer {

    override fun onSurfaceCreated(unused: GL10, config: EGLConfig) {
        // Set the background frame color
        GLES20.glClearColor(0.0f, 0.0f, 0.0f, 1.0f)
    }

    override fun onDrawFrame(unused: GL10) {
        // Redraw background color
        GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT)
    }

    override fun onSurfaceChanged(unused: GL10, width: Int, height: Int) {
        GLES20.glViewport(0, 0, width, height)
    }
}
```

### Java

```java
import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

import android.opengl.GLES20;
import android.opengl.GLSurfaceView;

public class MyGLRenderer implements GLSurfaceView.Renderer {

    public void onSurfaceCreated(GL10 unused, EGLConfig config) {
        // Set the background frame color
        GLES20.glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    }

    public void onDrawFrame(GL10 unused) {
        // Redraw background color
        GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT);
    }

    public void onSurfaceChanged(GL10 unused, int width, int height) {
        GLES20.glViewport(0, 0, width, height);
    }
}
```

That's all there is to it! The code examples above create a simple Android application that displays a black screen using OpenGL. While this code does not do anything very interesting, by creating these classes, you have laid the foundation you need to start drawing graphic elements with OpenGL.

**Note:** You may wonder why these methods have a[GL10](https://developer.android.com/reference/javax/microedition/khronos/opengles/GL10)parameter, when you are using the OpengGL ES 2.0 APIs. These method signatures are simply reused for the 2.0 APIs to keep the Android framework code simpler.

If you are familiar with the OpenGL ES APIs, you should now be able to set up a OpenGL ES environment in your app and start drawing graphics. However, if you need a bit more help getting started with OpenGL, head on to the next lessons for a few more hints.