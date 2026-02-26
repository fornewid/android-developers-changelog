---
title: https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl
url: https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl
source: md.txt
---

This page covers AGSL basics, and different ways to use AGSL in your Android
app.

## A simple AGSL shader

Your shader code is called for each drawn pixel, and returns the color the pixel
should be painted with. An extremely simple shader is one that always returns
a single color; this example uses red. The shader is defined inside of a `String`.

### Kotlin

```kotlin
private const val COLOR_SHADER_SRC =
   """half4 main(float2 fragCoord) {
      return half4(1,0,0,1);
   }"""
```

### Java

```java
private static final String COLOR_SHADER_SRC =
   "half4 main(float2 fragCoord) {\n" +
      "return half4(1,0,0,1);\n" +
   "}";
```

The next step is to create a [`RuntimeShader`](https://developer.android.com/reference/android/graphics/RuntimeShader)
object initialized with your shader string. This also compiles the shader.

### Kotlin

```kotlin
val fixedColorShader = RuntimeShader(COLOR_SHADER_SRC)
```

### Java

```java
RuntimeShader fixedColorShader = new RuntimeShader(COLOR_SHADER_SRC);
```

Your `RuntimeShader` can be used anywhere a standard Android shader can. As an
example, you can use it to draw into a custom `View` using a
[`Canvas`](https://developer.android.com/reference/android/graphics/Canvas).

### Kotlin

```kotlin
val paint = Paint()
paint.shader = fixedColorShader
override fun onDrawForeground(canvas: Canvas?) {
   canvas?.let {
      canvas.drawPaint(paint) // fill the Canvas with the shader
   }
}
```

### Java

```java
Paint paint = new Paint();
paint.setShader(fixedColorShader);
public void onDrawForeground(@Nullable Canvas canvas) {
   if (canvas != null) {
      canvas.drawPaint(paint); // fill the Canvas with the shader
   }
}
```

This draws a red `View`. You can use a `uniform` to pass a color parameter into
the shader to be drawn. First, add the color `uniform` to the shader:

### Kotlin

```kotlin
private const val COLOR_SHADER_SRC =
"""layout(color) uniform half4 iColor;
   half4 main(float2 fragCoord) {
      return iColor;
   }"""
```

### Java

```java
private static final String COLOR_SHADER_SRC =
   "layout(color) uniform half4 iColor;\n"+
      "half4 main(float2 fragCoord) {\n" +
      "return iColor;\n" +
   "}";
```

Then, call `setColorUniform` from your custom `View` to pass the desired color
into the AGSL shader.

### Kotlin

```kotlin
fixedColorShader.setColorUniform("iColor", Color.GREEN )
```

### Java

```java
fixedColorShader.setColorUniform("iColor", Color.GREEN );
```

Now, you get a green `View`; the `View` color is controlled using a
parameter from code in your custom `View` instead of being embedded in the
shader.

You can create a color gradient effect instead. You'll first need to change
the shader to accept the `View` resolution as input:

### Kotlin

```kotlin
private const val COLOR_SHADER_SRC =
"""uniform float2 iResolution;
   half4 main(float2 fragCoord) {
      float2 scaled = fragCoord/iResolution.xy;
      return half4(scaled, 0, 1);
   }"""
```

### Java

```java
private static final String COLOR_SHADER_SRC =
   "uniform float2 iResolution;\n" +
      "half4 main(float2 fragCoord) {\n" +
      "float2 scaled = fragCoord/iResolution.xy;\n" +
      "return half4(scaled, 0, 1);\n" +
   "}";
```

## Drawing the gradient

This shader does something slightly fancy. For each pixel, it creates a `float2`
vector that contains the x and y coordinates divided by the resolution, which
will create a value between zero and one. It then uses that scaled vector to
construct the red and green components of the return color.

You pass the resolution of the `View` into an AGSL shader `uniform` by calling
`setFloatUniform`.

### Kotlin

```kotlin
val paint = Paint()
paint.shader = fixedColorShader
override fun onDrawForeground(canvas: Canvas?) {
   canvas?.let {
      fixedColorShader.setFloatUniform("iResolution", width.toFloat(), height.toFloat())
      canvas.drawPaint(paint)
   }
}
```

### Java

```java
Paint paint = new Paint();
paint.setShader(fixedColorShader);
public void onDrawForeground(@Nullable Canvas canvas) {
   if (canvas != null) {
      fixedColorShader.setFloatUniform("iResolution", (float)getWidth(), (float()getHeight()));
      canvas.drawPaint(paint);
   }
}
```
![Red and Green gradient](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-gradient.png) Red and green gradient

## Animating the shader

You can use a similar technique to animate the shader by modifying it to receive `iTime` and `iDuration` uniforms. The shader will use these values to create a
triangular wave for the colors, causing them to cycle back and forth across their gradient values.

### Kotlin

```kotlin
private const val DURATION = 4000f
private const val COLOR_SHADER_SRC = """
   uniform float2 iResolution;
   uniform float iTime;
   uniform float iDuration;
   half4 main(in float2 fragCoord) {
      float2 scaled = abs(1.0-mod(fragCoord/iResolution.xy+iTime/(iDuration/2.0),2.0));
      return half4(scaled, 0, 1.0);
   }
"""
```

### Java

```java
private static final float DURATION = 4000f;
private static final String COLOR_SHADER_SRC =
   "uniform float2 iResolution;\n"+
   "uniform float iTime;\n"+
   "uniform float iDuration;\n"+
   "half4 main(in float2 fragCoord) {\n"+
      "float2 scaled = abs(1.0-mod(fragCoord/iResolution.xy+iTime/(iDuration/2.0),2.0));\n"+
      "return half4(scaled, 0, 1.0);\n"+
   "}";
```

From the custom view source code, a
[`ValueAnimator`](https://developer.android.com/reference/android/animation/ValueAnimator) updates the
`iTime` uniform.

### Kotlin

```kotlin
// declare the ValueAnimator
private val shaderAnimator = ValueAnimator.ofFloat(0f, DURATION)

// use it to animate the time uniform
shaderAnimator.duration = DURATION.toLong()
shaderAnimator.repeatCount = ValueAnimator.INFINITE
shaderAnimator.repeatMode = ValueAnimator.RESTART
shaderAnimator.interpolator = LinearInterpolator()

animatedShader.setFloatUniform("iDuration", DURATION )
shaderAnimator.addUpdateListener { animation ->
    animatedShader.setFloatUniform("iTime", animation.animatedValue as Float )
}
shaderAnimator.start()
```

### Java

```java
// declare the ValueAnimator
private final ValueAnimator shaderAnimator = ValueAnimator.ofFloat(0f, DURATION);

// use it to animate the time uniform
shaderAnimator.setDuration((long)DURATION);
shaderAnimator.setRepeatCount(ValueAnimator.INFINITE);
shaderAnimator.setRepeatMode(ValueAnimator.RESTART);
shaderAnimator.setInterpolator(new LinearInterpolator());

animatedShader.setFloatUniform("iDuration", DURATION );
shaderAnimator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
   public final void onAnimationUpdate(ValueAnimator animation) {
      animatedShader.setFloatUniform("iTime", (float)animation.getAnimatedValue());
   }
});
```
![Red and Green animated gradient](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-animated-gradient.gif) Red and Green animated gradient

## Painting complex objects

You don't have to draw the shader to fill the background; it can be
used in any place that accepts a
[`Paint`](https://developer.android.com/reference/android/graphics/Paint) object, such as
[`drawText`](https://developer.android.com/reference/android/graphics/Canvas#drawText(java.lang.String,%20float,%20float,%20android.graphics.Paint)).

### Kotlin

```kotlin
canvas.drawText(ANIMATED_TEXT, TEXT_MARGIN_DP, TEXT_MARGIN_DP + bounds.height(),
   paint)
```

### Java

```java
canvas.drawText(ANIMATED_TEXT, TEXT_MARGIN_DP, TEXT_MARGIN_DP + bounds.height(),
   paint);
```
![Red and Green animated gradient text](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-animated-gradient-text.gif) Red and Green animated gradient text

## Shading and Canvas transformations

You can apply additional `Canvas` transformations on your shaded text, such as
rotation. In the `ValueAnimator`, you can update a matrix for 3D rotations
using the built-in
[`android.graphics.Camera`](https://developer.android.com/reference/android/graphics/Camera) class.

### Kotlin

```kotlin
// in the ValueAnimator
camera.rotate(0.0f, animation.animatedValue as Float / DURATION * 360f, 0.0f)
```

### Java

```java
// in the ValueAnimator
camera.rotate(0.0f, (Float)animation.getAnimatedValue() / DURATION * 360f, 0.0f);
```

Since you want to rotate the text from the center axis rather than from the corner,
get the text bounds and then use `preTranslate` and `postTranslate` to alter the
matrix to translate the text so that 0,0 is the center of the rotation without
changing the position the text is drawn on the screen.

### Kotlin

```kotlin
linearColorPaint.getTextBounds(ANIMATED_TEXT, 0, ANIMATED_TEXT.length, bounds)
camera.getMatrix(rotationMatrix)
val centerX = (bounds.width().toFloat())/2
val centerY = (bounds.height().toFloat())/2
rotationMatrix.preTranslate(-centerX, -centerY)
rotationMatrix.postTranslate(centerX, centerY)
canvas.save()
canvas.concat(rotationMatrix)
canvas.drawText(ANIMATED_TEXT, 0f, 0f + bounds.height(), paint)
canvas.restore()
```

### Java

```java
linearColorPaint.getTextBounds(ANIMATED_TEXT, 0, ANIMATED_TEXT.length(), bounds);
camera.getMatrix(rotationMatrix);
float centerX = (float)bounds.width()/2.0f;
float centerY = (float)bounds.height()/2.0f;
rotationMatrix.preTranslate(-centerX, -centerY);
rotationMatrix.postTranslate(centerX, centerY);
canvas.save();
canvas.concat(rotationMatrix);
canvas.drawText(ANIMATED_TEXT, 0f, 0f + bounds.height(), paint);
canvas.restore();
```
![Red and Green rotating animated gradient text](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-rotating-animated-gradient-text.gif) Red and Green rotating animated gradient text

## Using RuntimeShader with Jetpack Compose

It's even easier to use `RuntimeShader` if you're rendering your UI using
[Jetpack Compose](https://developer.android.com/jetpack/compose). Starting with the same gradient shader from
before:

    private const val COLOR_SHADER_SRC =
        """uniform float2 iResolution;
       half4 main(float2 fragCoord) {
       float2 scaled = fragCoord/iResolution.xy;
       return half4(scaled, 0, 1);
    }"""

You can apply that shader to a
[`ShaderBrush`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ShaderBrush). You
then use the `ShaderBrush` as a parameter to the drawing commands within your
`Canvas`'s draw scope.

    // created as top level constants
    val colorShader = RuntimeShader(COLOR_SHADER_SRC)
    val shaderBrush = ShaderBrush(colorShader)

    Canvas(
       modifier = Modifier.fillMaxSize()
    ) {
       colorShader.setFloatUniform("iResolution",
       size.width, size.height)
       drawCircle(brush = shaderBrush)
    }

![AGSL Compose gradient circle](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-compose-gradient-circle.png) Red and green gradient circle

## Using RuntimeShader with RenderEffect

You can use
[`RenderEffect`](https://developer.android.com/reference/android/graphics/RenderEffect) to apply a
[`RuntimeShader`](https://developer.android.com/reference/android/graphics/RuntimeShader) to a parent `View`
*and* all child views. This is more expensive than drawing a custom `View`. but
it allows you to easily create an effect that incorporates what would have
originally been drawn using
[`createRuntimeShaderEffect`](https://developer.android.com/reference/android/graphics/RenderEffect#createRuntimeShaderEffect(android.graphics.RuntimeShader,%20java.lang.String)).

### Kotlin

```kotlin
view.setRenderEffect(RenderEffect.createRuntimeShaderEffect(myShader, "background"))
```

### Java

```java
view.setRenderEffect(RenderEffect.createRuntimeShaderEffect(myShader, "background"));
```

The second parameter is the name of a shader uniform that you can `eval` with a
coordinate parameter (such as the passed in fragCoord) to get the original color
of the
[`RenderNode`](https://developer.android.com/reference/android/graphics/RenderNode) (the View and its child
views), allowing you to perform all sorts of effects.

    uniform shader background;       // Root node of View tree to be altered
    return mix(returnColor, background.eval(fragCoord), 0.5);

![Grid blended over button](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-grid-blend.png) AGSL grid blended over button

A grid effect mixed over a button, but underneath a floating action button
(since it's in a different `View` hierarchy).