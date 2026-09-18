---
title: https://developer.android.com/topic/performance/hardware-accel
url: https://developer.android.com/topic/performance/hardware-accel
source: md.txt
---

The Android 2D rendering pipeline supports hardware acceleration, meaning that
all drawing operations that are performed on the canvas use the GPU. Because of
the increased resources required to enable hardware acceleration, your app will
consume more RAM.

Hardware acceleration is enabled by default. If your application uses only
standard composables, turning it on globally shouldn't cause any adverse drawing
effects. However, because hardware acceleration isn't supported for all of the
2D drawing operations, turning it on might affect some of your custom drawing
calls. Problems usually manifest themselves as invisible elements, exceptions,
or wrongly rendered pixels. To remedy this, Android gives you the option to
enable or disable hardware acceleration at multiple levels. See [Control
hardware acceleration](https://developer.android.com/topic/performance/hardware-accel#controlling).

If your application performs custom drawing, test your application on actual
hardware devices with hardware acceleration turned on to find any problems. The
[Support for drawing operations](https://developer.android.com/topic/performance/hardware-accel#drawing-support) section describes known issues with hardware
acceleration and how to work around them.

Also see [OpenGL with the Framework APIs](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl).

## Control hardware acceleration

You can control hardware acceleration at the following levels:

- Application
- Activity
- Window
- Composable

> [!NOTE]
> **Note:** Jetpack Compose UIs are hardware accelerated by default. The control levels in this section apply to all apps, including Compose apps.

#### Application level

In your Android manifest file, add the following attribute to the
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) tag to enable hardware acceleration for your entire
application:

    <application android:hardwareAccelerated="true" ...>

#### Activity level

If your application does not behave properly with hardware acceleration turned
on globally, you can control it for individual activities as well. To enable or
disable hardware acceleration at the activity level, you can use the
`android:hardwareAccelerated` attribute for the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) element. The
following example enables hardware acceleration for the entire application but
disables it for one activity:

    <application android:hardwareAccelerated="true">
        <activity ... />
        <activity android:hardwareAccelerated="false" />
    </application>

#### Window level

If you need even more fine-grained control, you can enable hardware acceleration
for a given window with the following code:

    window.setFlags(
            WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
            WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED
    )

> [!NOTE]
> **Note:** You currently cannot disable hardware acceleration at the window level.

#### Composable level

In Compose, there is no per-composable switch to disable hardware acceleration.

To render a composable into its own layer, use `Modifier.graphicsLayer`. This
lets transform properties (such as `alpha`, `scaleX`, `scaleY`, `translationX`,
`translationY`, `rotationX`, `rotationY`, `rotationZ`, and `transformOrigin`)
change without rerunning the composable's drawing code. For the best
performance, always use the lambda form of the modifier to set these properties.

To explicitly force an off-screen buffer for advanced drawing operations, such
as custom blending within the layer, use [`CompositingStrategy.Offscreen`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy#Offscreen()).
For more information, see [Graphics modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers).

If you have a custom drawing operation that strictly requires software
rendering, you can host a legacy View using `AndroidView` and call
`setLayerType(View.LAYER_TYPE_SOFTWARE, null)` on that view.

## Support for drawing operations

When hardware accelerated, the 2D rendering pipeline supports the most commonly
used [`Canvas`](https://developer.android.com/reference/kotlin/android/graphics/Canvas) drawing operations as well as many less-used operations. All
of the drawing operations that are used to render applications that ship with
Android, standard composables, and common advanced visual effects such as
reflections and tiled textures are supported.

The following table describes the support level of various operations across API
levels:

> [!NOTE]
> **Note:** Jetpack Compose requires a minimum of API level 21. In the following table, drawing operations with a first supported API level of 21 or earlier are universally supported in Compose apps.


|---|---|---|---|---|
|   |   |
|   | First supported API level |
| Canvas |||||
| drawBitmapMesh() (colors array) | 18 |
| drawPicture() | 23 |
| drawPosText() | 16 |
| drawTextOnPath() | 16 |
| drawVertices() | 29 |
| setDrawFilter() | 16 |
| clipPath() | 18 |
| clipRegion() | 18 |
| clipRect(Region.Op.XOR) | 18 |
| clipRect(Region.Op.Difference) | 18 |
| clipRect(Region.Op.ReverseDifference) | 18 |
| clipRect() with rotation/perspective | 18 |
| Paint |||||
| setAntiAlias() (for text) | 18 |
| setAntiAlias() (for lines) | 16 |
| setFilterBitmap() | 17 |
| setLinearText() | ✗ |
| setMaskFilter() | ✗ |
| setPathEffect() (for lines) | 28 |
| setShadowLayer() (other than text) | 28 |
| setStrokeCap() (for lines) | 18 |
| setStrokeCap() (for points) | 19 |
| setSubpixelText() | 28 |
| Xfermode |||||
| PorterDuff.Mode.DARKEN (framebuffer) | 28 |
| PorterDuff.Mode.LIGHTEN (framebuffer) | 28 |
| PorterDuff.Mode.OVERLAY (framebuffer) | 28 |
| Shader |||||
| ComposeShader inside ComposeShader | 28 |
| Same type shaders inside ComposeShader | 28 |
| Local matrix on ComposeShader | 18 |

<br />

### Canvas scaling

The hardware accelerated 2D rendering pipeline was built first to support
unscaled drawing, with some drawing operations degrading quality significantly
at higher scale values. These operations are implemented as textures drawn at
scale 1.0, transformed by the GPU. Starting in API level 28, all drawing
operations can scale without issue.

The following table shows when implementation was changed to correctly handle
large scales:

<br />

|---|---|
|   |   |
| Drawing operation to be scaled | First supported API level |
| drawText() | 18 |
| drawPosText() | 28 |
| drawTextOnPath() | 28 |
| Simple Shapes | 17 |
| Complex Shapes | 28 |
| drawPath() | 28 |
| Shadow layer | 28 |

<br />

> [!NOTE]
> **Note:** 'Simple' shapes are `drawRect()`, `drawCircle()`, `drawOval()`, `drawRoundRect()`, and `drawArc()` (with `useCenter=false`) commands issued with a `Paint` that doesn't have a `PathEffect`, and doesn't contain non-default joins (using `setStrokeJoin()` or `setStrokeMiter()`). Other instances of those draw commands fall under 'Complex' in the preceding chart.

If a drawing operation you depend on isn't hardware accelerated, render the
affected drawing into an off-screen software `Bitmap` (or `ImageBitmap`) and
draw the result. The rest of your UI keeps the hardware-accelerated path.

## Tips and tricks

Switching to hardware accelerated 2D graphics can instantly increase
performance, but you should still design your application to use the GPU
effectively by following these recommendations:

**Minimize layout complexity and recomposition**
:   Keep the layout tree shallow, and limit how much recomposes. Defer state reads to the narrowest scope, so that a change redraws the smallest possible region. For example, read animated state inside `Modifier.graphicsLayer { }` rather than in a composable's body. For more information, see [Jetpack Compose performance](https://developer.android.com/develop/ui/compose/performance).

**Avoid overdraw**
:   Don't draw too many layers on top of each other. Remove any UI elements that are completely
    obscured by other opaque elements on top of them. If you need to draw several layers blended on top of each other, consider merging them into a single layer. A good rule of thumb with current
    hardware is to not draw more than 2.5 times the number of pixels on screen per frame
    (transparent pixels in a bitmap count!).

**Don't create render objects in draw methods**
:   A common mistake is to create a new `https://developer.android.com/reference/kotlin/android/graphics/Paint` or a new `https://developer.android.com/reference/kotlin/android/graphics/Path` every time a rendering method is invoked. This forces the garbage
    collector to run more often and also bypasses caches and optimizations in the hardware
    pipeline. To avoid this, reuse and mutate your objects:

    - **Use standard methods** : Standard `DrawScope` methods (like `drawRect` and `drawCircle`) already reuse `Paint` objects internally without requiring developer allocation.
    - **Mutate instead of re-allocating** : When writing custom logic, use `path.rewind` to clear an existing `Path` rather than instantiating a new `Path`.
    - **Hold state efficiently** : Inside a composable, allocate objects once using `remember { Path() }`. If you are building reusable custom modifier extensions, implement a custom `Modifier.Node` using `DrawModifierNode` to allocate and reuse the objects without causing new heap allocations.


**Don't modify shapes too often**
:   Complex shapes, paths, and circles for example, are rendered using texture masks. Every
    time you create or modify a path, the hardware pipeline creates a new mask, which can be
    expensive.

**Don't modify bitmaps too often**
:   Every time you change the content of a bitmap, it is uploaded again as a GPU texture the
    next time you draw it.

**Use alpha with care**
:   When you make a composable translucent using `Modifier.alpha` or Compose animation APIs, it is typically rendered in an off-screen buffer which doubles the required fill-rate. To avoid the off-screen buffer overhead for non-overlapping content, set `CompositingStrategy.ModulateAlpha`. For individual draw calls, apply alpha directly to the drawing command (like with `color = Color.Red.copy(alpha = 0.5f)`) without creating a layer.

## Additional resources

### Views content

- [Hardware acceleration (Views)](https://developer.android.com/topic/performance/views/hardware-accel-views)