---
title: https://developer.android.com/develop/ui/views/graphics/opengl/draw
url: https://developer.android.com/develop/ui/views/graphics/opengl/draw
source: md.txt
---

After you define shapes to be drawn with OpenGL, you probably want to draw them. Drawing shapes
with the OpenGL ES 2.0 takes a bit more code than you might imagine, because the API provides a
great deal of control over the graphics rendering pipeline.

This lesson explains how to draw the shapes you defined in the previous lesson using the OpenGL
ES 2.0 API.

## Initialize shapes

Before you do any drawing, you must initialize and load the shapes you plan to draw. Unless the
structure (the original coordinates) of the shapes you use in your program change during the course
of execution, you should initialize them in the
`https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig)` method of your
renderer for memory and processing efficiency.

### Kotlin

```kotlin
class MyGLRenderer : GLSurfaceView.Renderer {
    ...
    private lateinit var mTriangle: Triangle
    private lateinit var mSquare: Square

    override fun onSurfaceCreated(unused: GL10, config: EGLConfig) {
        ...
        // initialize a triangle
        mTriangle = Triangle()
        // initialize a square
        mSquare = Square()
    }
    ...
}
```

### Java

```java
public class MyGLRenderer implements GLSurfaceView.Renderer {

    ...
    private Triangle mTriangle;
    private Square   mSquare;

    public void onSurfaceCreated(GL10 unused, EGLConfig config) {
        ...
        // initialize a triangle
        mTriangle = new Triangle();
        // initialize a square
        mSquare = new Square();
    }
    ...
}
```

## Draw a shape

Drawing a defined shape using OpenGL ES 2.0 requires a significant amount of code, because you
must provide a lot of details to the graphics rendering pipeline. Specifically, you must define the
following:

- *Vertex Shader* - OpenGL ES graphics code for rendering the vertices of a shape.
- *Fragment Shader* - OpenGL ES code for rendering the face of a shape with colors or textures.
- *Program* - An OpenGL ES object that contains the shaders you want to use for drawing one or more shapes.

You need at least one vertex shader to draw a shape and one fragment shader to color that shape.
These shaders must be compiled and then added to an OpenGL ES program, which is then used to draw
the shape. Here is an example of how to define basic shaders you can use to draw a shape in the
`Triangle` class:

### Kotlin

```kotlin
class Triangle {

    private val vertexShaderCode =
            "attribute vec4 vPosition;" +
            "void main() {" +
            "  gl_Position = vPosition;" +
            "}"

    private val fragmentShaderCode =
            "precision mediump float;" +
            "uniform vec4 vColor;" +
            "void main() {" +
            "  gl_FragColor = vColor;" +
            "}"

    ...
}
```

### Java

```java
public class Triangle {

    private final String vertexShaderCode =
        "attribute vec4 vPosition;" +
        "void main() {" +
        "  gl_Position = vPosition;" +
        "}";

    private final String fragmentShaderCode =
        "precision mediump float;" +
        "uniform vec4 vColor;" +
        "void main() {" +
        "  gl_FragColor = vColor;" +
        "}";

    ...
}
```

Shaders contain OpenGL Shading Language (GLSL) code that must be compiled prior to using it in
the OpenGL ES environment. To compile this code, create a utility method in your renderer class:

### Kotlin

```kotlin
fun loadShader(type: Int, shaderCode: String): Int {

    // create a vertex shader type (GLES20.GL_VERTEX_SHADER)
    // or a fragment shader type (GLES20.GL_FRAGMENT_SHADER)
    return GLES20.glCreateShader(type).also { shader ->

        // add the source code to the shader and compile it
        GLES20.glShaderSource(shader, shaderCode)
        GLES20.glCompileShader(shader)
    }
}
```

### Java

```java
public static int loadShader(int type, String shaderCode){

    // create a vertex shader type (GLES20.GL_VERTEX_SHADER)
    // or a fragment shader type (GLES20.GL_FRAGMENT_SHADER)
    int shader = GLES20.glCreateShader(type);

    // add the source code to the shader and compile it
    GLES20.glShaderSource(shader, shaderCode);
    GLES20.glCompileShader(shader);

    return shader;
}
```

In order to draw your shape, you must compile the shader code, add them to a OpenGL ES program
object and then link the program. Do this in your drawn object's constructor, so it is only done
once.

**Note:** Compiling OpenGL ES shaders and linking programs is expensive
in terms of CPU cycles and processing time, so you should avoid doing this more than once. If you do
not know the content of your shaders at runtime, you should build your code such that they only
get created once and then cached for later use.

### Kotlin

```kotlin
class Triangle {
    ...

    private var mProgram: Int

    init {
        ...

        val vertexShader: Int = loadShader(GLES20.GL_VERTEX_SHADER, vertexShaderCode)
        val fragmentShader: Int = loadShader(GLES20.GL_FRAGMENT_SHADER, fragmentShaderCode)

        // create empty OpenGL ES Program
        mProgram = GLES20.glCreateProgram().also {

            // add the vertex shader to program
            GLES20.glAttachShader(it, vertexShader)

            // add the fragment shader to program
            GLES20.glAttachShader(it, fragmentShader)

            // creates OpenGL ES program executables
            GLES20.glLinkProgram(it)
        }
    }
}
```

### Java

```java
public class Triangle() {
    ...

    private final int mProgram;

    public Triangle() {
        ...

        int vertexShader = MyGLRenderer.loadShader(GLES20.GL_VERTEX_SHADER,
                                        vertexShaderCode);
        int fragmentShader = MyGLRenderer.loadShader(GLES20.GL_FRAGMENT_SHADER,
                                        fragmentShaderCode);

        // create empty OpenGL ES Program
        mProgram = GLES20.glCreateProgram();

        // add the vertex shader to program
        GLES20.glAttachShader(mProgram, vertexShader);

        // add the fragment shader to program
        GLES20.glAttachShader(mProgram, fragmentShader);

        // creates OpenGL ES program executables
        GLES20.glLinkProgram(mProgram);
    }
}
```

At this point, you are ready to add the actual calls that draw your shape. Drawing shapes with
OpenGL ES requires that you specify several parameters to tell the rendering pipeline what you want
to draw and how to draw it. Since drawing options can vary by shape, it's a good idea to have your
shape classes contain their own drawing logic.

Create a `draw()` method for drawing the shape. This code sets the position and
color values to the shape's vertex shader and fragment shader, and then executes the drawing
function.

### Kotlin

```kotlin
private var positionHandle: Int = 0
private var mColorHandle: Int = 0

private val vertexCount: Int = triangleCoords.size / COORDS_PER_VERTEX
private val vertexStride: Int = COORDS_PER_VERTEX * 4 // 4 bytes per vertex

fun draw() {
    // Add program to OpenGL ES environment
    GLES20.glUseProgram(mProgram)

    // get handle to vertex shader's vPosition member
    positionHandle = GLES20.glGetAttribLocation(mProgram, "vPosition").also {

        // Enable a handle to the triangle vertices
        GLES20.glEnableVertexAttribArray(it)

        // Prepare the triangle coordinate data
        GLES20.glVertexAttribPointer(
                it,
                COORDS_PER_VERTEX,
                GLES20.GL_FLOAT,
                false,
                vertexStride,
                vertexBuffer
        )

        // get handle to fragment shader's vColor member
        mColorHandle = GLES20.glGetUniformLocation(mProgram, "vColor").also { colorHandle ->

            // Set color for drawing the triangle
            GLES20.glUniform4fv(colorHandle, 1, color, 0)
        }

        // Draw the triangle
        GLES20.glDrawArrays(GLES20.GL_TRIANGLES, 0, vertexCount)

        // Disable vertex array
        GLES20.glDisableVertexAttribArray(it)
    }
}
```

### Java

```java
private int positionHandle;
private int colorHandle;

private final int vertexCount = triangleCoords.length / COORDS_PER_VERTEX;
private final int vertexStride = COORDS_PER_VERTEX * 4; // 4 bytes per vertex

public void draw() {
    // Add program to OpenGL ES environment
    GLES20.glUseProgram(mProgram);

    // get handle to vertex shader's vPosition member
    positionHandle = GLES20.glGetAttribLocation(mProgram, "vPosition");

    // Enable a handle to the triangle vertices
    GLES20.glEnableVertexAttribArray(positionHandle);

    // Prepare the triangle coordinate data
    GLES20.glVertexAttribPointer(positionHandle, COORDS_PER_VERTEX,
                                 GLES20.GL_FLOAT, false,
                                 vertexStride, vertexBuffer);

    // get handle to fragment shader's vColor member
    colorHandle = GLES20.glGetUniformLocation(mProgram, "vColor");

    // Set color for drawing the triangle
    GLES20.glUniform4fv(colorHandle, 1, color, 0);

    // Draw the triangle
    GLES20.glDrawArrays(GLES20.GL_TRIANGLES, 0, vertexCount);

    // Disable vertex array
    GLES20.glDisableVertexAttribArray(positionHandle);
}
```

Once you have all this code in place, drawing this object just requires a call to the
`draw()` method from within your renderer's `https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer#onDrawFrame(javax.microedition.khronos.opengles.GL10)` method:

### Kotlin

```kotlin
override fun onDrawFrame(unused: GL10) {
    ...

    mTriangle.draw()
}
```

### Java

```java
public void onDrawFrame(GL10 unused) {
    ...

    mTriangle.draw();
}
```

When you run the application, it should look something like this:
![](https://developer.android.com/static/images/opengl/ogl-triangle.png)


**Figure 1.** Triangle drawn without a projection or camera view.

There are a few problems with this code example. First of all, it is not going to impress your
friends. Secondly, the triangle is a bit squashed and changes shape when you change the screen
orientation of the device. The reason the shape is skewed is due to the fact that the object's
vertices have not been corrected for the proportions of the screen area where the
`https://developer.android.com/reference/android/opengl/GLSurfaceView` is displayed. You can fix that problem using a projection and camera
view in the next lesson.

Lastly, the triangle is stationary, which is a bit boring. In the
[Add motion](https://developer.android.com/training/graphics/opengl/motion) lesson, you make this shape
rotate and make more interesting use of the OpenGL ES graphics pipeline.