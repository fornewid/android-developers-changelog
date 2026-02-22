---
title: https://developer.android.com/develop/ui/compose/graphics/draw/modifiers
url: https://developer.android.com/develop/ui/compose/graphics/draw/modifiers
source: md.txt
---

In addition to the `Canvas` composable, Compose has several useful graphics
`Modifiers` which aid in drawing custom content. These modifiers are useful
because they can be applied to any composable.

## Drawing modifiers

All drawing commands are done with a drawing modifier in Compose. There are
three main drawing modifiers in Compose:

- [`drawWithContent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithContent(kotlin.Function1))
- [`drawBehind`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawBehind(kotlin.Function1))
- [`drawWithCache`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithCache(kotlin.Function1))

The base modifier for drawing is `drawWithContent`, where you can decide the
drawing order of your Composable and the drawing commands issued inside the
modifier. `drawBehind` is a convenient wrapper around `drawWithContent` which has
the drawing order set to behind the content of the composable. `drawWithCache`
calls either `onDrawBehind` or `onDrawWithContent` inside of it - and provides a
mechanism for caching the objects created in them.

### `Modifier.drawWithContent`: Choose drawing order

[`Modifier.drawWithContent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithContent(kotlin.Function1)) lets you
execute [`DrawScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope) operations before or after the content of the
composable. Be sure to call `drawContent` to then render the actual content of
the composable. With this modifier, you can decide the order of operations, if
you want your content to be drawn before or after your custom drawing
operations.

For example, if you wished to render a radial gradient on top of your content to
create a flashlight keyhole effect on the UI, you could do the following:


```kotlin
var pointerOffset by remember {
    mutableStateOf(Offset(0f, 0f))
}
Column(
    modifier = Modifier
        .fillMaxSize()
        .pointerInput("dragging") {
            detectDragGestures { change, dragAmount ->
                pointerOffset += dragAmount
            }
        }
        .onSizeChanged {
            pointerOffset = Offset(it.width / 2f, it.height / 2f)
        }
        .drawWithContent {
            drawContent()
            // draws a fully black area with a small keyhole at pointerOffset that'll show part of the UI.
            drawRect(
                Brush.radialGradient(
                    listOf(Color.Transparent, Color.Black),
                    center = pointerOffset,
                    radius = 100.dp.toPx(),
                )
            )
        }
) {
    // Your composables here
}
```

<br />

**Figure 1**: Modifier.drawWithContent used on top of a Composable to create a flashlight type UI experience.

### `Modifier.drawBehind`: Drawing behind a composable

[`Modifier.drawBehind`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawBehind(kotlin.Function1)) lets you perform
`DrawScope` operations behind the composable content that is drawn on screen. If
you take a look at the implementation of [`Canvas`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Canvas), you might notice that it
is just a convenient wrapper around `Modifier.drawBehind`.

To draw a rounded rectangle behind `Text`:


```kotlin
Text(
    "Hello Compose!",
    modifier = Modifier
        .drawBehind {
            drawRoundRect(
                Color(0xFFBBAAEE),
                cornerRadius = CornerRadius(10.dp.toPx())
            )
        }
        .padding(4.dp)
)
```

<br />

Which produces the following result:
![Text and a background drawn using Modifier.drawBehind](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/modifier_draw_behind.png) **Figure 2**: Text and a background drawn using Modifier.drawBehind

### `Modifier.drawWithCache`: Drawing and caching draw objects

[`Modifier.drawWithCache`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithCache(kotlin.Function1)) keeps the objects
that are created inside of it cached. The objects are cached as long as the size
of the drawing area is the same, or any state objects that are read have not
changed. This modifier is useful for improving performance of drawing calls as
it avoids the need to reallocate objects (such as: `Brush, Shader, Path` etc.)
that are created on draw.

Alternatively, you could also cache objects using `remember`, outside of the
modifier. However, this is not always possible as you don't always have access
to the composition. It can be more performant to use `drawWithCache` if the
objects are only used for drawing.

> [!NOTE]
> **Note:** Only use `Modifier.drawWithCache` when you're creating objects that must be cached. Using this modifier without needing to cache objects, can result in unnecessary lambda allocations.

For example, if you create a `Brush` to draw a gradient behind a `Text`, using
`drawWithCache` caches the `Brush` object until the size of the drawing area
changes:


```kotlin
Text(
    "Hello Compose!",
    modifier = Modifier
        .drawWithCache {
            val brush = Brush.linearGradient(
                listOf(
                    Color(0xFF9E82F0),
                    Color(0xFF42A5F5)
                )
            )
            onDrawBehind {
                drawRoundRect(
                    brush,
                    cornerRadius = CornerRadius(10.dp.toPx())
                )
            }
        }
)
```

<br />

![Caching the Brush object with drawWithCache](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/modifier_draw_with_cache.png) **Figure 3**: Caching the Brush object with drawWithCache

## Graphics modifiers

### `Modifier.graphicsLayer`: Apply transformations to composables

[Video](https://www.youtube.com/watch?v=KawI7srRvOM)

[`Modifier.graphicsLayer`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/package-summary#(androidx.compose.ui.Modifier.graphicsLayer(kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,androidx.compose.ui.graphics.TransformOrigin,androidx.compose.ui.graphics.Shape,kotlin.Boolean,androidx.compose.ui.graphics.RenderEffect,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.CompositingStrategy)))
is a modifier that makes the content of the composable draw into a draw layer. A
layer provides a few different functions, such as:

- Isolation for its drawing instructions (similar to [`RenderNode`](https://developer.android.com/reference/android/graphics/RenderNode)). Drawing instructions captured as part of a layer can be re-issued efficiently by the rendering pipeline without re-executing application code.
- Transformations that apply to all the drawing instructions contained within a layer.
- Rasterization for composition capabilities. When a layer is rasterized, its drawing instructions are executed and the output is captured into an offscreen buffer. [Compositing](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers#heading=%7B:compositing-strategy%7D) such a buffer for subsequent frames is faster than executing the individual instructions, but it will behave as a bitmap when transforms like scaling or rotation are applied.

#### Transformations

`Modifier.graphicsLayer` provides isolation for its drawing instructions; for
instance, various transformations can be applied using `Modifier.graphicsLayer`.
These can be animated or modified without needing to re-execute the drawing
lambda.

`Modifier.graphicsLayer` does not change the measured size or placement of your
composable, as it only affects the draw phase. This means that your composable
might overlap others if it ends up drawing outside of its layout bounds.

> [!NOTE]
> **Note:** You should prefer the lambda version of this modifier when performing animations or using a `State` object to update a `graphicsLayer` property.

The following transformations can be applied with this modifier:

##### Scale - increase size

`scaleX` and `scaleY` enlarges or shrinks content in the horizontal or vertical
direction, respectively. A value of `1.0f` indicates no change in scale, a value
of `0.5f` means half of the dimension.


```kotlin
Image(
    painter = painterResource(id = R.drawable.sunset),
    contentDescription = "Sunset",
    modifier = Modifier
        .graphicsLayer {
            this.scaleX = 1.2f
            this.scaleY = 0.8f
        }
)
```

<br />

**Figure 4**: scaleX and scaleY applied to an Image composable

##### Translation

`translationX` and `translationY` can be changed with `graphicsLayer`,
`translationX` moves the composable left or right. `translationY` moves the
composable up or down.


```kotlin
Image(
    painter = painterResource(id = R.drawable.sunset),
    contentDescription = "Sunset",
    modifier = Modifier
        .graphicsLayer {
            this.translationX = 100.dp.toPx()
            this.translationY = 10.dp.toPx()
        }
)
```

<br />

**Figure 5**: translationX and translationY applied to Image with Modifier.graphicsLayer

##### Rotation

Set `rotationX` to rotate horizontally, `rotationY` to rotate vertically and
`rotationZ` to rotate on the Z axis (standard rotation). This value is specified
in degrees (0-360).


```kotlin
Image(
    painter = painterResource(id = R.drawable.sunset),
    contentDescription = "Sunset",
    modifier = Modifier
        .graphicsLayer {
            this.rotationX = 90f
            this.rotationY = 275f
            this.rotationZ = 180f
        }
)
```

<br />

**Figure 6**: rotationX, rotationY and rotationZ set on Image by Modifier.graphicsLayer

##### Origin

A `transformOrigin` can be specified. It is then used as the point from which
transformations take place. All the examples so far have used
`TransformOrigin.Center`, which is at `(0.5f, 0.5f)`. If you specify the origin at
`(0f, 0f)`, the transformations then start from the top-left corner of the
composable.

If you change the origin with a `rotationZ` transformation, you can see that the
item rotates around the top left of the composable:


```kotlin
Image(
    painter = painterResource(id = R.drawable.sunset),
    contentDescription = "Sunset",
    modifier = Modifier
        .graphicsLayer {
            this.transformOrigin = TransformOrigin(0f, 0f)
            this.rotationX = 90f
            this.rotationY = 275f
            this.rotationZ = 180f
        }
)
```

<br />

**Figure 7**: Rotation applied with TransformOrigin set to 0f, 0f

#### Clip and Shape

Shape specifies the outline that the content clips to when `clip = true`. In
this example, we set two boxes to have two different clips - one using
`graphicsLayer` clip variable, and the other using the convenient wrapper
`Modifier.clip`.


```kotlin
Column(modifier = Modifier.padding(16.dp)) {
    Box(
        modifier = Modifier
            .size(200.dp)
            .graphicsLayer {
                clip = true
                shape = CircleShape
            }
            .background(Color(0xFFF06292))
    ) {
        Text(
            "Hello Compose",
            style = TextStyle(color = Color.Black, fontSize = 46.sp),
            modifier = Modifier.align(Alignment.Center)
        )
    }
    Box(
        modifier = Modifier
            .size(200.dp)
            .clip(CircleShape)
            .background(Color(0xFF4DB6AC))
    )
}
```

<br />

The contents of the first box (the text saying "Hello Compose") are clipped to
the circle shape:
![Clip applied to Box composable](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/clip_applied.png) **Figure 8**: Clip applied to Box composable

If you then apply a `translationY` to the top pink circle, you see that the bounds
of the Composable are still the same, but the circle draws underneath the bottom
circle (and outside of its bounds).
![Clip applied with translationY, and red border for outline](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/clip_applied_red_border.png) **Figure 9**: Clip applied with translationY, and red border for outline

To clip the composable to the region it's drawn in, you can add another
`Modifier.clip(RectangleShape)` at the start of the modifier chain. The content
then remains inside of the original bounds.


```kotlin
Column(modifier = Modifier.padding(16.dp)) {
    Box(
        modifier = Modifier
            .clip(RectangleShape)
            .size(200.dp)
            .border(2.dp, Color.Black)
            .graphicsLayer {
                clip = true
                shape = CircleShape
                translationY = 50.dp.toPx()
            }
            .background(Color(0xFFF06292))
    ) {
        Text(
            "Hello Compose",
            style = TextStyle(color = Color.Black, fontSize = 46.sp),
            modifier = Modifier.align(Alignment.Center)
        )
    }

    Box(
        modifier = Modifier
            .size(200.dp)
            .clip(RoundedCornerShape(500.dp))
            .background(Color(0xFF4DB6AC))
    )
}
```

<br />

![Clip applied on top of graphicsLayer transformation](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/clip_applied_everything.png) **Figure 10**: Clip applied on top of graphicsLayer transformation

#### Alpha

`Modifier.graphicsLayer` can be used to set an `alpha` (opacity) for the whole
layer. `1.0f` is fully opaque and `0.0f` is invisible.


```kotlin
Image(
    painter = painterResource(id = R.drawable.sunset),
    contentDescription = "clock",
    modifier = Modifier
        .graphicsLayer {
            this.alpha = 0.5f
        }
)
```

<br />

![Image with alpha applied](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/image_alpha.png) **Figure 11**: Image with alpha applied

> [!NOTE]
> **Note:** When an alpha is set to less than 1.0f, the entire contents of the layer are drawn to an offscreen buffer (if the [`CompositingStrategy`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy) is not set to [`ModulateAlpha`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy#ModulateAlpha())). See the `CompositingStrategy` section for more information.

#### Compositing strategy

Working with alpha and transparency might not be as simple as changing a single
alpha value. In addition to changing an alpha, there is also the option to set a
[`CompositingStrategy`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy) on a `graphicsLayer`. A `CompositingStrategy` determines how the
content of the composable is composited (put together) with the other
content already drawn on screen.

> [!NOTE]
> **Note:** `CompositingStrategy` was introduced in Compose `1.4.0-alpha02`.

The different strategies are:

##### Auto (default)

The [compositing strategy](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy#Auto()) is determined by the rest of the `graphicsLayer`
parameters. It renders the layer into an offscreen buffer if alpha is less than
1.0f or a `RenderEffect` is set. Whenever the alpha is less than 1f, a
compositing layer is created automatically to render the contents and then draw
this offscreen buffer to the destination with the corresponding alpha. Setting a
[`RenderEffect`](https://developer.android.com/reference/android/graphics/RenderEffect) or overscroll always renders content into an offscreen
buffer regardless of the `CompositingStrategy` set.

##### Offscreen

The contents of the composable are **always** rasterized to an offscreen
texture or bitmap before rendering to the destination. This is useful for
applying [`BlendMode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/BlendMode) operations to mask content, and for performance when
rendering complex sets of drawing instructions.

An example of using [`CompositingStrategy.Offscreen`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy#Offscreen()) is with `BlendModes`. Taking a look at the example below,
say you want to remove parts of an `Image` composable by issuing a draw command that
uses `BlendMode.Clear`. If you do not set the `compositingStrategy` to
`CompositingStrategy.Offscreen`, the `BlendMode` interacts with all the contents
below it.


```kotlin
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = "Dog",
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(120.dp)
        .aspectRatio(1f)
        .background(
            Brush.linearGradient(
                listOf(
                    Color(0xFFC5E1A5),
                    Color(0xFF80DEEA)
                )
            )
        )
        .padding(8.dp)
        .graphicsLayer {
            compositingStrategy = CompositingStrategy.Offscreen
        }
        .drawWithCache {
            val path = Path()
            path.addOval(
                Rect(
                    topLeft = Offset.Zero,
                    bottomRight = Offset(size.width, size.height)
                )
            )
            onDrawWithContent {
                clipPath(path) {
                    // this draws the actual image - if you don't call drawContent, it wont
                    // render anything
                    this@onDrawWithContent.drawContent()
                }
                val dotSize = size.width / 8f
                // Clip a white border for the content
                drawCircle(
                    Color.Black,
                    radius = dotSize,
                    center = Offset(
                        x = size.width - dotSize,
                        y = size.height - dotSize
                    ),
                    blendMode = BlendMode.Clear
                )
                // draw the red circle indication
                drawCircle(
                    Color(0xFFEF5350), radius = dotSize * 0.8f,
                    center = Offset(
                        x = size.width - dotSize,
                        y = size.height - dotSize
                    )
                )
            }
        }
)
```

<br />

By setting the `CompositingStrategy` to `Offscreen`, it creates an offscreen
texture to execute the commands to (applying the `BlendMode` only to the
contents of this composable). It then renders it on top of what is already
rendered on screen, not affecting the content already drawn.
![Modifier.drawWithContent on an Image showing a circle indication, with the BlendMode.Clear inside app](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/complex_modifier_example_drawWithCache_background.png) **Figure 12**: Modifier.drawWithContent on an Image showing a circle indication, with the BlendMode.Clear and CompositingStrategy.Offscreen inside app

If you didn't use `CompositingStrategy.Offscreen`, the results of applying
`BlendMode.Clear` clears all the pixels in the destination, regardless of what
was already set-- leaving the window's rendering buffer (black) visible. Many of
the `BlendModes` that involve alpha won't work as expected without an
offscreen buffer. Note the black ring around the red circle indicator:
![Modifier.drawWithContent on an Image showing a circle indication, with the BlendMode.Clear and no CompositingStrategy set](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/blendmode_without_compositing_strategy.png) **Figure 13**: Modifier.drawWithContent on an Image showing a circle indication, with the BlendMode.Clear and no CompositingStrategy set

To understand this a bit further: if the app had a translucent window
background, and you did not use the `CompositingStrategy.Offscreen`, the
`BlendMode` would interact with the whole app. It would clear all of the pixels to show
the app or wallpaper underneath, as in this example:
![No CompositingStrategy set and using BlendMode.Clear with an app that has a translucent window background. The pink wallpaper is shown through the area around the red status circle.](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/compositing_strategy_punch_through_to_wallpaper.png) **Figure 14**: No CompositingStrategy set and using BlendMode.Clear with an app that has a translucent window background. Notice how the pink wallpaper is shown through the area around the red status circle.

It's worth noting that when using `CompositingStrategy.Offscreen`, an offscreen
texture that is the size of the drawing area is created and rendered back on
screen. Any drawing commands that are done with this strategy, are by default be
clipped to this region. The below code snippet illustrates the differences when
switching to using offscreen textures:


```kotlin
@Composable
fun CompositingStrategyExamples() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .wrapContentSize(Alignment.Center)
    ) {
        // Does not clip content even with a graphics layer usage here. By default, graphicsLayer
        // does not allocate + rasterize content into a separate layer but instead is used
        // for isolation. That is draw invalidations made outside of this graphicsLayer will not
        // re-record the drawing instructions in this composable as they have not changed
        Canvas(
            modifier = Modifier
                .graphicsLayer()
                .size(100.dp) // Note size of 100 dp here
                .border(2.dp, color = Color.Blue)
        ) {
            // ... and drawing a size of 200 dp here outside the bounds
            drawRect(color = Color.Magenta, size = Size(200.dp.toPx(), 200.dp.toPx()))
        }

        Spacer(modifier = Modifier.size(300.dp))

        /* Clips content as alpha usage here creates an offscreen buffer to rasterize content
        into first then draws to the original destination */
        Canvas(
            modifier = Modifier
                // force to an offscreen buffer
                .graphicsLayer(compositingStrategy = CompositingStrategy.Offscreen)
                .size(100.dp) // Note size of 100 dp here
                .border(2.dp, color = Color.Blue)
        ) {
            /* ... and drawing a size of 200 dp. However, because of the CompositingStrategy.Offscreen usage above, the
            content gets clipped */
            drawRect(color = Color.Red, size = Size(200.dp.toPx(), 200.dp.toPx()))
        }
    }
}
```

<br />

![CompositingStrategy.Auto vs CompositingStrategy.Offscreen - offscreen clips to the region, where auto doesn’t](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/graphics_compositing_strategy.png) **Figure 15**: CompositingStrategy.Auto vs CompositingStrategy.Offscreen - offscreen clips to the region, where auto doesn't

##### `ModulateAlpha`

This [composition strategy](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/CompositingStrategy#ModulateAlpha()) modulates the alpha for each of the drawing
instructions recorded within the `graphicsLayer`. It won't create an
offscreen buffer for alpha below 1.0f unless a `RenderEffect` is set, so it can
be more efficient for alpha rendering. However, it can provide different results
for overlapping content. For use cases where it is known in advance that content
is not overlapping, this can provide better performance than
`CompositingStrategy.Auto` with alpha values less than 1.

Another example of different composition strategies is below - applying different
alphas to different parts of the composables, and applying a `Modulate`
strategy:


```kotlin
@Preview
@Composable
fun CompositingStrategy_ModulateAlpha() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(32.dp)
    ) {
        // Base drawing, no alpha applied
        Canvas(
            modifier = Modifier.size(200.dp)
        ) {
            drawSquares()
        }

        Spacer(modifier = Modifier.size(36.dp))

        // Alpha 0.5f applied to whole composable
        Canvas(
            modifier = Modifier
                .size(200.dp)
                .graphicsLayer {
                    alpha = 0.5f
                }
        ) {
            drawSquares()
        }
        Spacer(modifier = Modifier.size(36.dp))

        // 0.75f alpha applied to each draw call when using ModulateAlpha
        Canvas(
            modifier = Modifier
                .size(200.dp)
                .graphicsLayer {
                    compositingStrategy = CompositingStrategy.ModulateAlpha
                    alpha = 0.75f
                }
        ) {
            drawSquares()
        }
    }
}

private fun DrawScope.drawSquares() {

    val size = Size(100.dp.toPx(), 100.dp.toPx())
    drawRect(color = Red, size = size)
    drawRect(
        color = Purple, size = size,
        topLeft = Offset(size.width / 4f, size.height / 4f)
    )
    drawRect(
        color = Yellow, size = size,
        topLeft = Offset(size.width / 4f * 2f, size.height / 4f * 2f)
    )
}

val Purple = Color(0xFF7E57C2)
val Yellow = Color(0xFFFFCA28)
val Red = Color(0xFFEF5350)
```

<br />

![ModulateAlpha applies the alpha set to each individual draw command](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/modulate_alpha.png) **Figure 16**: ModulateAlpha applies the alpha set to each individual draw command

## Write contents of a composable to a bitmap

> [!NOTE]
> **Note:** The `rememberGraphicsLayer()` function used in this snippet is only available from Compose 1.7.0-alpha07+.

A common use case is to create a `Bitmap` from a composable. To copy the
contents of your composable to a `Bitmap`, create a `GraphicsLayer` using
`rememberGraphicsLayer()`.

Redirect the drawing commands to the new layer using `drawWithContent()` and
`graphicsLayer.record{}`. Then draw the layer in the visible canvas using
`drawLayer`:


```kotlin
val coroutineScope = rememberCoroutineScope()
val graphicsLayer = rememberGraphicsLayer()
Box(
    modifier = Modifier
        .drawWithContent {
            // call record to capture the content in the graphics layer
            graphicsLayer.record {
                // draw the contents of the composable into the graphics layer
                this@drawWithContent.drawContent()
            }
            // draw the graphics layer on the visible canvas
            drawLayer(graphicsLayer)
        }
        .clickable {
            coroutineScope.launch {
                val bitmap = graphicsLayer.toImageBitmap()
                // do something with the newly acquired bitmap
            }
        }
        .background(Color.White)
) {
    Text("Hello Android", fontSize = 26.sp)
}
```

<br />

You can save the bitmap to disk and share it. For more details, see the [full
example snippet](https://github.com/android/snippets/blob/latest/compose/snippets/src/main/java/com/example/compose/snippets/graphics/AdvancedGraphicsSnippets.kt#L123). Be sure to check for on device permissions before trying
to save to disk.

## Custom drawing modifier

To create your own custom modifier, implement the `DrawModifier` interface. This
gives you access to a `ContentDrawScope`, which is the same as what is exposed
when using `Modifier.drawWithContent()`. You can then extract common drawing
operations to custom drawing modifiers to clean up the code and provide
convenient wrappers; for example, `Modifier.background()` is a convenient
`DrawModifier`.

For example, if you wanted to implement a `Modifier` that vertically flips
content, you can create one as follows:


```kotlin
class FlippedModifier : DrawModifier {
    override fun ContentDrawScope.draw() {
        scale(1f, -1f) {
            this@draw.drawContent()
        }
    }
}

fun Modifier.flipped() = this.then(FlippedModifier())
```

<br />

Then use this flipped modifier applied on `Text`:


```kotlin
Text(
    "Hello Compose!",
    modifier = Modifier
        .flipped()
)
```

<br />

![Custom Flipped Modifier on Text](https://developer.android.com/static/develop/ui/compose/images/graphics/modifiers/modifier_flipped.png) **Figure 17**: Custom Flipped Modifier on Text

## Additional resources

For more examples using `graphicsLayer` and custom drawing, check out the
following resources:

- [Making Jellyfish move in Compose](https://medium.com/androiddevelopers/making-jellyfish-move-in-compose-animating-imagevectors-and-applying-agsl-rendereffects-3666596a8888)
- [ADS 2022 Layouts and Graphics in Compose](https://youtu.be/xcfEQO0k_gU)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview)
- [Customize an image {:#customize-image}](https://developer.android.com/develop/ui/compose/graphics/images/customize)
- [Kotlin for Jetpack Compose](https://developer.android.com/develop/ui/compose/kotlin)