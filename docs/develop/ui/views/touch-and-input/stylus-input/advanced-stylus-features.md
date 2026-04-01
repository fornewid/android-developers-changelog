---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with a stylus in Compose. [Advanced stylus features →](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Android and ChromeOS provide a variety of APIs to help you build apps that offer
users an exceptional stylus experience. The
[`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent) class exposes
information about stylus interaction with the screen, including stylus pressure,
orientation, tilt, hover, and palm detection. Low-latency graphics and motion
prediction libraries enhance stylus on‑screen rendering to provide a
natural, pen‑and‑paper‑like experience.

## `MotionEvent`

The `MotionEvent` class represents user input interactions such as the position
and movement of touch pointers on the screen. For stylus input, `MotionEvent`
also exposes pressure, orientation, tilt, and hover data.

### Event data

To access `MotionEvent` data, set up an [`onTouchListener`](https://developer.android.com/reference/kotlin/android/view/View.OnTouchListener) callback:

### Kotlin

    val onTouchListener = View.OnTouchListener { view, event ->
      // Process motion event.
    }

### Java

    View.OnTouchListener listener = (view, event) -> {
      // Process motion event.
    };

The listener receives `MotionEvent` objects from the system, so your app can
process them.

> [!NOTE]
> **Note:** `MotionEvent` objects are dispatched every time the stylus moves on screen. Optimize your app's motion event handling code as much as possible. For example, avoid heap allocation by forgoing the creation of new objects or the use of lambdas.

A `MotionEvent` object provides data related to the following aspects of a UI
event:

- Actions: Physical interaction with the device---touching the screen, moving a pointer over the screen surface, hovering a pointer over the screen surface
- Pointers: Identifiers of objects interacting with the screen---finger, stylus, mouse
- Axis: Type of data---x and y coordinates, pressure, tilt, orientation, and hover (distance)

### Actions

To implement stylus support, you need to understand what action the user is
performing.

`MotionEvent` provides a wide variety of `ACTION` constants that define motion
events. The most important actions for stylus include the following:

| Action | Description |
|---|---|
| ACTION_DOWN ACTION_POINTER_DOWN | Pointer has made contact with the screen. |
| ACTION_MOVE | Pointer is moving on the screen. |
| ACTION_UP ACTION_POINTER_UP | Pointer is not in contact with the screen anymore |
| ACTION_CANCEL | When previous or current motion set should be canceled. |

Your app can perform tasks like starting a new stroke when `ACTION_DOWN`
happens, drawing the stroke with `ACTION_MOVE,` and finishing the stroke when
`ACTION_UP` is triggered.

The set of `MotionEvent` actions from `ACTION_DOWN` to `ACTION_UP` for a given
pointer is called a motion set.

### Pointers

Most screens are multi-touch: the system assigns a pointer for each finger,
stylus, mouse, or other pointing object interacting with the screen. A pointer
index enables you to get axis information for a specific pointer, like the
position of the first finger touching the screen or the second.

Pointer indexes range from zero to the number of pointers returned by
[`MotionEvent#pointerCount()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getpointercount)
minus 1.

Axis values of the pointers can be accessed with the [`getAxisValue(axis,
pointerIndex)`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getaxisvalue) method.
When the pointer index is omitted, the system returns the value for the first
pointer, pointer zero (0).

`MotionEvent` objects contain information about the type of pointer in use. You
can get the pointer type by iterating through the pointer indexes and calling
the
[`getToolType(pointerIndex)`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gettooltype)
method.

> [!NOTE]
> **Note:** A pointer is a way to interact with the screen---finger, stylus, capacitive stylus, mouse. Since most screens support multi-touch, a `MotionEvent` object can contain multiple pointers (one for each object in contact with the screen).

To learn more about pointers, see [Handle multi-touch
gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi).

### Stylus inputs

You can filter for stylus inputs with
[`TOOL_TYPE_STYLUS`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_stylus):

### Kotlin

```kotlin
val isStylus = TOOL_TYPE_STYLUS == event.getToolType(pointerIndex)
```

### Java

```java
boolean isStylus = TOOL_TYPE_STYLUS == event.getToolType(pointerIndex);
```

The stylus can also report that it is used as an eraser with
[`TOOL_TYPE_ERASER`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#tool_type_eraser):

### Kotlin

```kotlin
val isEraser = TOOL_TYPE_ERASER == event.getToolType(pointerIndex)
```

### Java

```java
boolean isEraser = TOOL_TYPE_ERASER == event.getToolType(pointerIndex);
```

### Stylus axis data

`ACTION_DOWN` and `ACTION_MOVE` provide axis data about the stylus, namely x and
y coordinates, pressure, orientation, tilt, and hover.

To enable access to this data, the `MotionEvent` API provides
[`getAxisValue(int)`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getaxisvalue),
where the parameter is any of the following axis identifiers:

| Axis | Return value of `getAxisValue()` |
|---|---|
| [`AXIS_X`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_x) | X coordinate of a motion event. |
| [`AXIS_Y`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_y) | Y coordinate of a motion event. |
| [`AXIS_PRESSURE`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_pressure) | For a touchscreen or touchpad, the pressure applied by a finger, stylus, or other pointer. For a mouse or trackball, 1 if the primary button is pressed, 0 otherwise. |
| [`AXIS_ORIENTATION`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_pressure) | For a touchscreen or touchpad, the orientation of a finger, stylus, or other pointer relative to the vertical plane of the device. |
| [`AXIS_TILT`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_tilt) | The tilt angle of the stylus in radians. |
| [`AXIS_DISTANCE`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_distance) | The distance of the stylus from the screen. |

For example, `MotionEvent.getAxisValue(AXIS_X)` returns the x coordinate for the
first pointer.

> [!NOTE]
> **Note:** Each object interacting with the screen in the case of multi-touch has its own axis data.

See also [Handle multi-touch
gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi).

#### Position

You can retrieve the x and y coordinates of a pointer with the following calls:

- `MotionEvent#getAxisValue(AXIS_X)` or [`MotionEvent#getX()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getx_1)
- `MotionEvent#getAxisValue(AXIS_Y)` or [`MotionEvent#getY()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#gety)

![Stylus drawing on screen with x and y coordinates mapped.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_x_y_coordinates.png) **Figure 1.** X and y screen coordinates of a stylus pointer.

#### Pressure

You can retrieve the pointer pressure with
`MotionEvent#getAxisValue(AXIS_PRESSURE)` or, for the first pointer,
[`MotionEvent#getPressure()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getpressure).

The pressure value for touchscreens or touchpads is a value between 0 (no
pressure) and 1, but higher values can be returned depending on the screen
calibration.
![Stylus stroke that represents a continuum of low to high pressure. The stroke is narrow and faint on the left, indicating low pressure. The stroke becomes wider and darker from left to right until it is widest and darkest on the far right, indicating highest pressure.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_pressure.png) **Figure 2.** Pressure representation---low pressure on left, high pressure on right.

> [!NOTE]
> **Note:** Make sure you verify the value is between 0 and 1 and normalize the value if it is greater than 1.

#### Orientation

Orientation indicates which direction the stylus is pointing.

Pointer orientation can be retrieved using `getAxisValue(AXIS_ORIENTATION)` or
[`getOrientation()`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getorientation)
(for the first pointer).

For a stylus, the orientation is returned as a radian value between 0 to pi (𝛑)
clockwise or 0 to -pi counterclockwise.

Orientation enables you to implement a real-life brush. For example, if the
stylus represents a flat brush, the width of the flat brush depends on the
stylus orientation.
![](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_orientation.png) **Figure 3.** Stylus pointing to the left about minus .57 radians.

#### Tilt

Tilt measures the inclination of the stylus relative to the screen.

Tilt returns the positive angle of the stylus in radians, where zero is
perpendicular to the screen and 𝛑/2 is flat on the surface.

The tilt angle can be retrieved using `getAxisValue(AXIS_TILT)` (no shortcut for
the first pointer).

Tilt can be used to reproduce as close as possible real-life tools, like
mimicking shading with a tilted pencil.
![Stylus inclined about 40 degrees from the screen surface.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_tilt.png) **Figure 4.** Stylus tilted at about .785 radians, or 45 degrees from perpendicular.

> [!NOTE]
> **Note:** Because of the physical constraints of the stylus, it is nearly impossible to achieve a value of 𝛑/2 (flat).

#### Hover

The distance of the stylus from the screen can be obtained with
`getAxisValue(AXIS_DISTANCE)`. The method returns a value from 0.0 (contact with
the screen) to higher values as the stylus moves away from the screen. The hover
distance between the screen and the nib (point) of the stylus depends on the
manufacturer of both the screen and the stylus. Because implementations can
vary, don't rely on precise values for app-critical functionality.

Stylus hover can be used to preview the size of the brush or indicate that a
button is going to be selected.
![](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_hover.png) **Figure 5.** Stylus hovering over a screen. App reacts even though stylus doesn't touch the screen surface. **Note:** Compose provides modifiers that affect the interactive state of UI elements:

- [`hoverable`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).hoverable(androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean)): Configure component to be hoverable using pointer enter and exit events.
- [`indication`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).indication(androidx.compose.foundation.interaction.InteractionSource,androidx.compose.foundation.Indication)): Draws visual effects for this component when interactions occur.

## Palm rejection, navigation, and unwanted inputs

Sometimes multi-touch screens can register unwanted touches, for example, when a
user naturally rests their hand on the screen for support while handwriting.
Palm rejection is a mechanism that detects this behavior and notifies you that
the last `MotionEvent` set should be canceled.

As a result, you must keep a history of user inputs so that the unwanted touches
can be removed from the screen and the legitimate user inputs can be
re-rendered.

### ACTION_CANCEL and FLAG_CANCELED

[`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel) and
[`FLAG_CANCELED`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#flag_canceled) are
both designed to inform you that the previous `MotionEvent` set should be
canceled from the last `ACTION_DOWN`, so you can, for example, undo the last
stroke for a drawing app for a given pointer.

#### ACTION_CANCEL

Added in Android 1.0 (API level 1)

`ACTION_CANCEL` indicates the previous set of motion events should be canceled.

`ACTION_CANCEL` is triggered when any of the following is detected:

- Navigation gestures
- Palm rejection

When `ACTION_CANCEL` is triggered, you should identify the active pointer with
`https://developer.android.com/reference/kotlin/android/view/MotionEvent#getpointerid(https://developer.android.com/reference/kotlin/android/view/MotionEvent#getactionindex)`. Then remove the stroke created with that pointer from the input history, and re-render the scene.

#### FLAG_CANCELED

Added in Android 13 (API level 33)

[`FLAG_CANCELED`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#flag_canceled)
indicates that the pointer going up was an unintentional user touch. The flag is
typically set when the user accidentally touches the screen, such as by gripping
the device or placing the palm of the hand on the screen.

You access the flag value as follows:

### Kotlin

```kotlin
val cancel = (event.flags and FLAG_CANCELED) == FLAG_CANCELED
```

### Java

```java
boolean cancel = (event.getFlags() & FLAG_CANCELED) == FLAG_CANCELED;
```

If the flag is set, you need to undo the last `MotionEvent` set, from the last
`ACTION_DOWN` from this pointer.

Like `ACTION_CANCEL`, the pointer can be found with `getPointerId(actionIndex)`.
Your browser doesn't support the video tag. **Figure 6.** Stylus stroke and palm touch create `MotionEvent` sets. Palm touch is canceled, and display is re-rendered.

### Full screen, edge-to-edge, and navigation gestures

If an app is full screen and has actionable elements near the edge, such as the
canvas of a drawing or note-taking app, swiping from the bottom of the screen to
display the navigation or move the app to the background might result in an
unwanted touch on the canvas.
Your browser doesn't support the video tag. **Figure 7.** Swipe gesture to move an app to the background.

To prevent gestures from triggering unwanted touches in your app, you can take
advantage of [insets](https://developer.android.com/reference/kotlin/android/graphics/Insets) and
`ACTION_CANCEL`.

See also the [Palm rejection, navigation, and unwanted inputs](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features#palm_rejection)
section.

Use the
[`setSystemBarsBehavior()`](https://developer.android.com/reference/kotlin/android/view/WindowInsetsController#setsystembarsbehavior)
method and
[`BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE`](https://developer.android.com/reference/kotlin/android/view/WindowInsetsController#behavior_show_transient_bars_by_swipe)
of
[`WindowInsetsController`](https://developer.android.com/reference/kotlin/android/view/WindowInsetsController)
to prevent navigation gestures from causing unwanted touch events:

<br />

### Kotlin

```kotlin
// Configure the behavior of the hidden system bars.
windowInsetsController.systemBarsBehavior =
    WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
```

### Java

```java
// Configure the behavior of the hidden system bars.
windowInsetsController.setSystemBarsBehavior(
    WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
);
```

To learn more about inset and gesture management, see:

- [Hide system bars for immersive mode](https://developer.android.com/develop/ui/views/layout/immersive)
- [Ensure compatibility with gesture navigation](https://developer.android.com/develop/ui/views/touch-and-input/gestures/gesturenav)
- [Display content edge-to-edge in your app](https://developer.android.com/develop/ui/views/layout/edge-to-edge)

## Low latency

Latency is the time required by the hardware, system, and application to process
and render user input.

Latency = hardware and OS input processing + app processing + system compositing

- hardware rendering

![Latency causes the rendered stroke to lag behind the stylus position. The gap between the stroke rendered and the stylus position represents the latency.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_latency.png) **Figure 8.** Latency causes the rendered stroke to lag behind the stylus position.

### Source of latency

- Registering stylus with touchscreen (hardware): Initial wireless connection when the stylus and OS communicate to be registered and synced.
- Touch sampling rate (hardware): The number of times per second a touchscreen checks whether a pointer is touching the surface, ranging from 60 to 1000Hz.
- Input processing (app): Applying color, graphic effects, and transformation on user input.
- Graphic rendering (OS + hardware): Buffer swapping, hardware processing.

### Low-latency graphics

The [Jetpack low-latency graphics library](https://developer.android.com/jetpack/androidx/releases/graphics)
reduces the processing time between user input and on-screen rendering.

The library reduces processing time by avoiding multi-buffer rendering and
leveraging a front-buffer rendering technique, which means writing directly to
the screen.

> [!NOTE]
> **Note:** Multi-buffer and front-buffer rendering are available for developers implementing rendering with [OpenGL](https://en.wikipedia.org/wiki/OpenGL).

#### Front-buffer rendering

The front buffer is the memory the screen uses for rendering. It is the closest
apps can get to drawing directly to the screen. The low-latency library enables
apps to render directly to the front buffer. This improves performance by
preventing buffer swapping, which can happen for regular multi-buffer rendering
or double-buffer rendering (the most common case).
![App writes to screen buffer and reads from screen buffer.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/front_buffer_rendering.png) **Figure 9.** Front-buffer rendering. ![App writes to multi-buffer, which swaps with screen buffer. App reads from screen buffer.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/multi-buffer_rendering.png) **Figure 10.** Multi-buffer rendering.

While front-buffer rendering is a great technique to render a small area of the
screen, it is not designed to be used for refreshing the entire screen. With
front-buffer rendering, the app is rendering content into a buffer from which
the display is reading. As a result, there is the possibility of rendering
artifacts or [tearing](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features#tearing)(see below).

The low-latency library is available from Android 10 (API level 29) and higher
and on ChromeOS devices running Android 10 (API level 29) and higher.

#### Dependencies

The low-latency library provides the components for front-buffer rendering
implementation. The library is added as a dependency in the app's module
`build.gradle` file:

    dependencies {
        implementation "androidx.graphics:graphics-core:1.0.0-alpha03"
    }

#### GLFrontBufferRenderer callbacks

The low-latency library includes the
[`GLFrontBufferRenderer.Callback`](https://developer.android.com/reference/kotlin/androidx/graphics/lowlatency/GLFrontBufferedRenderer.Callback)
interface, which defines the following methods:

- [`onDrawFrontBufferedLayer()`](https://developer.android.com/reference/kotlin/androidx/graphics/lowlatency/GLFrontBufferedRenderer.Callback#onDrawFrontBufferedLayer(androidx.graphics.opengl.egl.EGLManager,androidx.graphics.lowlatency.BufferInfo,kotlin.FloatArray,kotlin.Any))
  - [`onDrawDoubleBufferedLayer()`](https://developer.android.com/reference/kotlin/androidx/graphics/lowlatency/GLFrontBufferedRenderer.Callback#onDrawDoubleBufferedLayer(androidx.graphics.opengl.egl.EGLManager,androidx.graphics.lowlatency.BufferInfo,kotlin.FloatArray,kotlin.collections.Collection))

The low-latency library is not opinionated about the type of data you use with
`GLFrontBufferRenderer`.

However, the library processes the data as a stream of hundreds of data points;
and so, design your data to optimize memory usage and allocation.

##### Callbacks

To enable rendering callbacks, implement `GLFrontBufferedRenderer.Callback` and
override `onDrawFrontBufferedLayer()` and `onDrawDoubleBufferedLayer()`.
`GLFrontBufferedRenderer` uses the callbacks to render your data in the most
optimized way possible.

<br />

### Kotlin

```kotlin
val callback = object: GLFrontBufferedRenderer.Callback<DATA_TYPE> {
   override fun onDrawFrontBufferedLayer(
       eglManager: EGLManager,
       bufferInfo: BufferInfo,
       transform: FloatArray,
       param: DATA_TYPE
   ) {
       // OpenGL for front buffer, short, affecting small area of the screen.
   }
   override fun onDrawMultiDoubleBufferedLayer(
       eglManager: EGLManager,
       bufferInfo: BufferInfo,
       transform: FloatArray,
       params: Collection<DATA_TYPE>
   ) {
       // OpenGL full scene rendering.
   }
}
```

### Java

```java
GLFrontBufferedRenderer.Callback<DATA_TYPE> callbacks =
    new GLFrontBufferedRenderer.Callback<DATA_TYPE>() {
        @Override
        public void onDrawFrontBufferedLayer(@NonNull EGLManager eglManager,
            @NonNull BufferInfo bufferInfo,
            @NonNull float[] transform,
            DATA_TYPE data_type) {
                // OpenGL for front buffer, short, affecting small area of the screen.
        }

    @Override
    public void onDrawDoubleBufferedLayer(@NonNull EGLManager eglManager,
        @NonNull BufferInfo bufferInfo,
        @NonNull float[] transform,
        @NonNull Collection<? extends DATA_TYPE> collection) {
            // OpenGL full scene rendering.
    }
};
```

##### Declare an instance of GLFrontBufferedRenderer

Prepare the `GLFrontBufferedRenderer` by providing the `SurfaceView` and
callbacks you created earlier. `GLFrontBufferedRenderer` optimizes the rendering
to the front and double buffer using your callbacks:

### Kotlin

```kotlin
var glFrontBufferRenderer = GLFrontBufferedRenderer<DATA_TYPE>(surfaceView, callbacks)
```

### Java

```java
GLFrontBufferedRenderer<DATA_TYPE> glFrontBufferRenderer =
    new GLFrontBufferedRenderer<DATA_TYPE>(surfaceView, callbacks);
```

##### Rendering

Front-buffer rendering starts when you call the
[`renderFrontBufferedLayer()`](https://developer.android.com/reference/kotlin/androidx/graphics/lowlatency/GLFrontBufferedRenderer#renderFrontBufferedLayer(kotlin.Any))
method, which triggers the `onDrawFrontBufferedLayer()` callback.

Double-buffer rendering resumes when you call the
[`commit()`](https://developer.android.com/reference/kotlin/androidx/graphics/lowlatency/GLFrontBufferedRenderer#commit())
function, which triggers the `onDrawMultiDoubleBufferedLayer()` callback.

In the example that follows, the process renders to the front buffer (fast
rendering) when the user starts drawing on the screen (`ACTION_DOWN`) and moves
the pointer around (`ACTION_MOVE`). The process renders to the double buffer
when the pointer leaves the surface of the screen (`ACTION_UP`).

You can use
[`requestUnbufferedDispatch()`](https://developer.android.com/reference/kotlin/android/view/View#requestunbuffereddispatch)
to ask that the input system doesn't batch motion events but instead delivers
them as soon as they're available:

<br />

### Kotlin

```kotlin
when (motionEvent.action) {
   MotionEvent.ACTION_DOWN -> {
       // Deliver input events as soon as they arrive.
       view.requestUnbufferedDispatch(motionEvent)
       // Pointer is in contact with the screen.
       glFrontBufferRenderer.renderFrontBufferedLayer(DATA_TYPE)
   }
   MotionEvent.ACTION_MOVE -> {
       // Pointer is moving.
       glFrontBufferRenderer.renderFrontBufferedLayer(DATA_TYPE)
   }
   MotionEvent.ACTION_UP -> {
       // Pointer is not in contact in the screen.
       glFrontBufferRenderer.commit()
   }
   MotionEvent.CANCEL -> {
       // Cancel front buffer; remove last motion set from the screen.
       glFrontBufferRenderer.cancel()
   }
}
```

### Java

```java
switch (motionEvent.getAction()) {
   case MotionEvent.ACTION_DOWN: {
       // Deliver input events as soon as they arrive.
       surfaceView.requestUnbufferedDispatch(motionEvent);

       // Pointer is in contact with the screen.
       glFrontBufferRenderer.renderFrontBufferedLayer(DATA_TYPE);
   }
   break;
   case MotionEvent.ACTION_MOVE: {
       // Pointer is moving.
       glFrontBufferRenderer.renderFrontBufferedLayer(DATA_TYPE);
   }
   break;
   case MotionEvent.ACTION_UP: {
       // Pointer is not in contact in the screen.
       glFrontBufferRenderer.commit();
   }
   break;
   case MotionEvent.ACTION_CANCEL: {
       // Cancel front buffer; remove last motion set from the screen.
       glFrontBufferRenderer.cancel();
   }
   break;
}
```

#### Rendering do's and don'ts

✓ Do

Small portions of the screen, handwriting, drawing, sketching.
✗ Don't

Fullscreen update, panning, zooming. Can result in tearing.

##### Tearing

Tearing happens when the screen refreshes while the screen buffer is being
modified at the same time. A part of the screen shows new data, while another
shows old data.
![Upper and lower parts of Android image are misaligned due to tearing as screen refreshes.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/tearing.png) **Figure 11.** Tearing as screen is refreshed from top to bottom.

### Motion prediction

The [Jetpack motion prediction
library](https://developer.android.com/reference/androidx/input/motionprediction/package-summary) reduces
perceived latency by estimating the user's stroke path and providing temporary,
artificial points to the renderer.

The motion prediction library gets real user inputs as `MotionEvent` objects.
The objects contain information about x and y coordinates, pressure, and time,
which are leveraged by the motion predictor to predict future `MotionEvent`
objects.

Predicted `MotionEvent` objects are only estimates. Predicted events can reduce
perceived latency, but predicted data must be replaced with actual `MotionEvent`
data once it is received.

The motion prediction library is available from Android 4.4 (API level 19) and
higher and on ChromeOS devices running Android 9 (API level 28) and higher.
![Latency causes the rendered stroke to lag behind the stylus position. The gap between the stroke and stylus is filled with prediction points. The remaining gap is the perceived latency.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/advanced-stylus/stylus_reduced_latency.png) **Figure 12.** Latency reduced by motion prediction.

#### Dependencies

The motion prediction library provides the implementation of prediction. The
library is added as a dependency in the app's module `build.gradle` file:

    dependencies {
        implementation "androidx.input:input-motionprediction:1.0.0-beta01"
    }

#### Implementation

The motion prediction library includes the
[`MotionEventPredictor`](https://developer.android.com/reference/kotlin/androidx/input/motionprediction/MotionEventPredictor)
interface, which defines the following methods:

- [`record()`](https://developer.android.com/reference/kotlin/androidx/input/motionprediction/MotionEventPredictor#record(android.view.MotionEvent)): Stores `MotionEvent` objects as a record of the user's actions
- [`predict()`](https://developer.android.com/reference/kotlin/androidx/input/motionprediction/MotionEventPredictor#predict()): Returns a predicted `MotionEvent`

##### Declare an instance of `MotionEventPredictor`

### Kotlin

```kotlin
var motionEventPredictor = MotionEventPredictor.newInstance(view)
```

### Java

```java
MotionEventPredictor motionEventPredictor = MotionEventPredictor.newInstance(surfaceView);
```

##### Feed the predictor with data

### Kotlin

```kotlin
motionEventPredictor.record(motionEvent)
```

### Java

```java
motionEventPredictor.record(motionEvent);
```

##### Predict

<br />

### Kotlin

```kotlin
when (motionEvent.action) {
   MotionEvent.ACTION_MOVE -> {
       val predictedMotionEvent = motionEventPredictor?.predict()
       if(predictedMotionEvent != null) {
            // use predicted MotionEvent to inject a new artificial point
       }
   }
}
```

### Java

```java
switch (motionEvent.getAction()) {
   case MotionEvent.ACTION_MOVE: {
       MotionEvent predictedMotionEvent = motionEventPredictor.predict();
       if(predictedMotionEvent != null) {
           // use predicted MotionEvent to inject a new artificial point
       }
   }
   break;
}
```

> [!NOTE]
> **Note:** The `MotionEvent` object returned by the `predict()` method contains all data including x and y coordinates, pressure, orientation and tilt.

#### Motion prediction do's and don'ts

✓ Do

Remove prediction points when a new predicted point is added.
✗ Don't

Don't use prediction points for final rendering.

## Note-taking apps

ChromeOS enables your app to declare some note-taking actions.

To register an app as a note-taking app on ChromeOS, see [Input
compatibility](https://chromeos.dev/en/android/input-compatibility#note-taking-apps).

To register an app as a note-taking on Android, see [Create a note-taking
app](https://developer.android.com/guide/topics/large-screens/create-a-note-taking-app#app_manifest).

Android 14 (API level 34), introduced the
[`ACTION_CREATE_NOTE`](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_NOTE)
intent, which enables your app to start a note-taking activity on the lock
screen.

## Digital ink recognition with ML Kit

With the [ML Kit digital ink
recognition](https://developers.google.com/ml-kit/vision/digital-ink-recognition/android),
your app can recognize handwritten text on a digital surface in hundreds of
languages. You can also classify sketches.

ML Kit provides the
[`Ink.Stroke.Builder`](https://developers.google.com/ml-kit/vision/digital-ink-recognition/android#build_an_ink_object)
class to create `Ink` objects that can be processed by machine learning models
to convert handwriting to text.

In addition to handwriting recognition, the model is able to recognize
[gestures](https://developers.google.com/ml-kit/vision/digital-ink-recognition#gestures),
such as delete and circle.

See [Digital ink
recognition](https://developers.google.com/ml-kit/vision/digital-ink-recognition)
to learn more.

## Additional resources

### Developer guides

- [Create a note-taking app](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/create-a-note-taking-app)

<!-- -->

- [Recognizing digital ink with ML Kit on Android](https://developers.google.com/ml-kit/vision/digital-ink-recognition/android)

### Codelabs

- [Enhance stylus support in an Android app](https://developer.android.com/codelabs/large-screens/advanced-stylus-support)