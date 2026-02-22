---
title: https://developer.android.com/develop/ui/views/graphics/opengl/motion
url: https://developer.android.com/develop/ui/views/graphics/opengl/motion
source: md.txt
---

# Add motion

Drawing objects on screen is a pretty basic feature of OpenGL, but you can do this with other Android graphics framework classes, including[Canvas](https://developer.android.com/reference/android/graphics/Canvas)and[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)objects. OpenGL ES provides additional capabilities for moving and transforming drawn objects in three dimensions or in other unique ways to create compelling user experiences.

In this lesson, you take another step forward into using OpenGL ES by learning how to add motion to a shape with rotation.

## Rotate a shape

Rotating a drawing object with OpenGL ES 2.0 is relatively simple. In your renderer, create another transformation matrix (a rotation matrix) and then combine it with your projection and camera view transformation matrices:  

### Kotlin

```kotlin
private val rotationMatrix = FloatArray(16)

override fun onDrawFrame(gl: GL10) {
    val scratch = FloatArray(16)

    ...

    // Create a rotation transformation for the triangle
    val time = SystemClock.uptimeMillis() % 4000L
    val angle = 0.090f * time.toInt()
    Matrix.setRotateM(rotationMatrix, 0, angle, 0f, 0f, -1.0f)

    // Combine the rotation matrix with the projection and camera view
    // Note that the vPMatrix factor *must be first* in order
    // for the matrix multiplication product to be correct.
    Matrix.multiplyMM(scratch, 0, vPMatrix, 0, rotationMatrix, 0)

    // Draw triangle
    mTriangle.draw(scratch)
}
```

### Java

```java
private float[] rotationMatrix = new float[16];
@Override
public void onDrawFrame(GL10 gl) {
    float[] scratch = new float[16];

    ...

    // Create a rotation transformation for the triangle
    long time = SystemClock.uptimeMillis() % 4000L;
    float angle = 0.090f * ((int) time);
    Matrix.setRotateM(rotationMatrix, 0, angle, 0, 0, -1.0f);

    // Combine the rotation matrix with the projection and camera view
    // Note that the vPMatrix factor *must be first* in order
    // for the matrix multiplication product to be correct.
    Matrix.multiplyMM(scratch, 0, vPMatrix, 0, rotationMatrix, 0);

    // Draw triangle
    mTriangle.draw(scratch);
}
```

If your triangle does not rotate after making these changes, make sure you have commented out the[GLSurfaceView.RENDERMODE_WHEN_DIRTY](https://developer.android.com/reference/android/opengl/GLSurfaceView#RENDERMODE_WHEN_DIRTY)setting, as described in the next section.

## Enable continuous rendering

If you have diligently followed along with the example code in this class to this point, make sure you comment out the line that sets the render mode only draw when dirty, otherwise OpenGL rotates the shape only one increment and then waits for a call to[requestRender()](https://developer.android.com/reference/android/opengl/GLSurfaceView#requestRender())from the[GLSurfaceView](https://developer.android.com/reference/android/opengl/GLSurfaceView)container:  

### Kotlin

```kotlin
class MyGLSurfaceView(context: Context) : GLSurfaceView(context) {

    init {
        ...
        // Render the view only when there is a change in the drawing data.
        // To allow the triangle to rotate automatically, this line is commented out:
        // renderMode = GLSurfaceView.RENDERMODE_WHEN_DIRTY
    }
}
```

### Java

```java
public class MyGLSurfaceView(Context context) extends GLSurfaceView {
    ...
    // Render the view only when there is a change in the drawing data.
    // To allow the triangle to rotate automatically, this line is commented out:
    //setRenderMode(GLSurfaceView.RENDERMODE_WHEN_DIRTY);
}
```

Unless you have objects changing without any user interaction, it's usually a good idea have this flag turned on. Be ready to uncomment this code, because the next lesson makes this call applicable once again.