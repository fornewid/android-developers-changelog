---
title: https://developer.android.com/develop/ui/compose/graphics/draw/overview
url: https://developer.android.com/develop/ui/compose/graphics/draw/overview
source: md.txt
---

[Video](https://www.youtube.com/watch?v=1yiuxWK74vI)

Many apps need to be able to precisely control exactly what's drawn on the
screen. This might be as small as putting a box or a circle on the screen in
just the right place, or it might be an elaborate arrangement of graphic
elements in many different styles.

## Basic drawing with modifiers and `DrawScope`

The core way to draw something custom in Compose is with modifiers, such as
[`Modifier.drawWithContent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithContent(kotlin.Function1)),
[`Modifier.drawBehind`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawBehind(kotlin.Function1)), and
[`Modifier.drawWithCache`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithCache(kotlin.Function1)).

For example, to draw something behind your composable, you can use the
`drawBehind` modifier to start executing drawing commands:


```kotlin
Spacer(
    modifier = Modifier
        .fillMaxSize()
        .drawBehind {
            // this = DrawScope
        }
)
```

<br />

If all you need is a composable that draws, you can use the
[`Canvas`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/package-summary#Canvas(android.graphics.Canvas)) composable. The `Canvas` composable is a
convenient wrapper around [`Modifier.drawBehind`](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers#drawbehind). You place the `Canvas` in
your layout the same way you would with any other Compose UI element. Within the
`Canvas`, you can draw elements with precise control over their style and
location.

> [!NOTE]
> **Note:** Under the hood, Compose relies on the view-based UI's [Canvas and other
> associated objects](https://developer.android.com/develop/ui/views/graphics/drawables). However, Compose simplifies many of the more confusing aspects of `Canvas`. For example, most of the view-based graphics elements rely on a `Paint` helper object. You need to know which configuration options you set in the `Paint`, and which you set in the method call. You also need to be careful to create your `Paint` objects in a way that won't harm performance. Compose takes care of those details for you.

All drawing modifiers expose a [`DrawScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope), a scoped drawing environment
that maintains its own state. This lets you set the parameters for a group of
graphical elements. The `DrawScope` provides several useful fields, like `size`,
a `Size` object specifying the current dimensions of the `DrawScope`.

To draw something, you can use one of the many draw functions on `DrawScope`. For
example, the following code draws a rectangle in the top left corner of the
screen:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    val canvasQuadrantSize = size / 2F
    drawRect(
        color = Color.Magenta,
        size = canvasQuadrantSize
    )
}
```

<br />

![Pink rectangle drawn on a white background that takes up a quarter of the screen](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_draw_rect.png) **Figure 1**. Rectangle drawn using Canvas in Compose.

To learn more about different drawing modifiers, see the [Graphics Modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers)
documentation.

## Coordinate system

To draw something on screen, you need to know the offset (`x` and `y`) and size of
your item. With many of the draw methods on `DrawScope`, the position and size
are provided by [default parameter values](https://developer.android.com/develop/ui/compose/kotlin#default-args). The default parameters generally
position the item at the `[0, 0]` point on the canvas, and provide a default
`size` that fills the entire drawing area, as in the example above - you can see
the rectangle is positioned in the top left. To adjust the size and position of
your item, you need to understand the coordinate system in Compose.

The origin of the coordinate system (`[0,0]`) is at the top leftmost pixel in the
drawing area. `x` increases as it moves right and `y` increases as it moves
downwards.

> [!NOTE]
> **Note:** All drawing operations are performed using pixel sizing. To ensure consistent sizing of your items across different device densities and screen sizes, be sure to either convert from `dp` using [`.toPx()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/unit/Density#(androidx.compose.ui.unit.Dp).toPx()) or work in fractions of the size.

![A grid showing the coordinate system showing the top left \[0, 0\] and bottom right \[width, height\]](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_coordinate_system_drawing.png) **Figure 2**. Drawing coordinate system / drawing grid.

For example, if you want to draw a diagonal line from the top-right corner of
the canvas area to the bottom-left corner, you can use the
[`DrawScope.drawLine()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawLine(androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Offset,kotlin.Float,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.graphics.PathEffect,kotlin.Float,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) function, and specify a start and end offset with
the corresponding x and y positions:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    val canvasWidth = size.width
    val canvasHeight = size.height
    drawLine(
        start = Offset(x = canvasWidth, y = 0f),
        end = Offset(x = 0f, y = canvasHeight),
        color = Color.Blue
    )
}
```

<br />

## Basic transformations

`DrawScope` offers transformations to change where or how the drawing commands
are executed.

> [!NOTE]
> **Note:** These transformations only apply in the [draw phase of the Composable
> lifecycle](https://developer.android.com/develop/ui/compose/phases#phase3-drawing) - any changes to size or position won't change the layout size and position. Elements may draw over other elements if they are moved out of their layout size and position.

### Scale

Use
[`DrawScope.scale()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).scale(kotlin.Float,kotlin.Float,androidx.compose.ui.geometry.Offset,kotlin.Function1))
to increase the size of your drawing operations by a factor. Operations like
`scale()` apply to all drawing operations within the corresponding lambda. For
example, the following code increases the `scaleX` 10 times and `scaleY` 15
times:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    scale(scaleX = 10f, scaleY = 15f) {
        drawCircle(Color.Blue, radius = 20.dp.toPx())
    }
}
```

<br />

![A circle scaled non-uniformly](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_scale.png) **Figure 3**. Applying a scale operation to a circle on Canvas.

### Translate

Use
[`DrawScope.translate()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).translate(kotlin.Float,kotlin.Float,kotlin.Function1))
to move your drawing operations up, down, left, or right. For example, the
following code moves the drawing 100 px to the right and 300 px up:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    translate(left = 100f, top = -300f) {
        drawCircle(Color.Blue, radius = 200.dp.toPx())
    }
}
```

<br />

![A circle that has moved off center](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_translate.png) **Figure 4**. Applying a translate operation to a circle on Canvas.

### Rotate

Use
[`DrawScope.rotate()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).rotate(kotlin.Float,androidx.compose.ui.geometry.Offset,kotlin.Function1))
to rotate your drawing operations around a pivot point. For example, the
following code rotates a rectangle 45 degrees:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    rotate(degrees = 45F) {
        drawRect(
            color = Color.Gray,
            topLeft = Offset(x = size.width / 3F, y = size.height / 3F),
            size = size / 3F
        )
    }
}
```

<br />

![A phone with a rectangle rotated by 45 degrees in the center of the screen](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_rotate.png) **Figure 5** . We use `rotate()` to apply a rotation to the current drawing scope, which rotates the rectangle by 45 degrees.

### Inset

Use [`DrawScope.inset()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/package-summary#(androidx.compose.ui.graphics.drawscope.DrawScope).inset(kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Function1)) to adjust the default parameters of the current
`DrawScope`, changing the drawing boundaries and translating the drawings
accordingly:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    val canvasQuadrantSize = size / 2F
    inset(horizontal = 50f, vertical = 30f) {
        drawRect(color = Color.Green, size = canvasQuadrantSize)
    }
}
```

<br />

This code effectively adds padding to the drawing commands:
![A rectangle that has been padded all around it](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_inset.png) **Figure 6**. Applying an inset to drawing commands.

### Multiple transformations

To apply multiple transformations to your drawings, use the
[`DrawScope.withTransform()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/package-summary#(androidx.compose.ui.graphics.drawscope.DrawScope).withTransform(kotlin.Function1,kotlin.Function1)) function, which creates and
applies a single transformation that combines all your desired changes. Using
`withTransform()` is more efficient than making nested calls to individual
transformations, because all the transformations are performed together in a
single operation, instead of Compose needing to calculate and save each of the
nested transformations.

For example, the following code applies both a translation and a rotation to the
rectangle:


```kotlin
Canvas(modifier = Modifier.fillMaxSize()) {
    withTransform({
        translate(left = size.width / 5F)
        rotate(degrees = 45F)
    }) {
        drawRect(
            color = Color.Gray,
            topLeft = Offset(x = size.width / 3F, y = size.height / 3F),
            size = size / 3F
        )
    }
}
```

<br />

![A phone with a rotated rectangle shifted to the side of the screen](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_multiple_transforms.png) **Figure 7** . Use `withTransform` to apply both a rotation and a translation, rotating the rectangle and shifting it to the left.

## Common drawing operations

### Draw text

To draw text in Compose, you can typically use the `Text` composable. However,
if you are in a `DrawScope` or you want to draw your text manually with
customization, you can use the
[`DrawScope.drawText()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).drawText(androidx.compose.ui.text.TextMeasurer,androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.geometry.Offset,androidx.compose.ui.text.TextStyle,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.collections.List,androidx.compose.ui.unit.IntSize))
method.

To draw text, create a [`TextMeasurer`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextMeasurer) using [`rememberTextMeasurer`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#rememberTextMeasurer(kotlin.Int))
and call `drawText` with the measurer:


```kotlin
val textMeasurer = rememberTextMeasurer()

Canvas(modifier = Modifier.fillMaxSize()) {
    drawText(textMeasurer, "Hello")
}
```

<br />

![Showing a Hello drawn on Canvas](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_draw_text.png) **Figure 8**. Drawing text on Canvas.

#### Measure text

Drawing text works a bit differently from other drawing commands. Normally, you
give the drawing command the size (width and height) to draw the shape/image as.
With text, there are a few parameters that control the size of the rendered
text, such as font size, font, ligatures, and letter spacing.

With Compose, you can use a [`TextMeasurer`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextMeasurer) to get access to the measured
size of text, depending on the above factors. If you want to draw a background
behind the text, you can use the measured information to get the size of the
area that the text takes up:


```kotlin
val textMeasurer = rememberTextMeasurer()

Spacer(
    modifier = Modifier
        .drawWithCache {
            val measuredText =
                textMeasurer.measure(
                    AnnotatedString(longTextSample),
                    constraints = Constraints.fixedWidth((size.width * 2f / 3f).toInt()),
                    style = TextStyle(fontSize = 18.sp)
                )

            onDrawBehind {
                drawRect(pinkColor, size = measuredText.size.toSize())
                drawText(measuredText)
            }
        }
        .fillMaxSize()
)
```

<br />

> [!NOTE]
> **Note:** The above example uses `Modifier.drawWithCache`, since drawing text is an expensive operation. Using `drawWithCache` helps cache the created objects until the size of the drawing area changes. For more information, see the [`Modifier.drawWithCache` documentation](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers#drawwithcache).

This code snippet produces a pink background on the text:
![Multi-line text taking up ⅔ size of the full area, with a background rectangle](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_text_measured.png) **Figure 9**. Multi-line text taking up ⅔ size of the full area, with a background rectangle.

Adjusting the constraints, font size, or any property that affects measured size
results in a new size reported. You can set a fixed size for both the `width`
and `height`, and the text then follows the set [`TextOverflow`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextOverflow). For
example, the following code renders text in ⅓ of the height and ⅓ of the width
of the composable area, and sets the `TextOverflow` to `TextOverflow.Ellipsis`:


```kotlin
val textMeasurer = rememberTextMeasurer()

Spacer(
    modifier = Modifier
        .drawWithCache {
            val measuredText =
                textMeasurer.measure(
                    AnnotatedString(longTextSample),
                    constraints = Constraints.fixed(
                        width = (size.width / 3f).toInt(),
                        height = (size.height / 3f).toInt()
                    ),
                    overflow = TextOverflow.Ellipsis,
                    style = TextStyle(fontSize = 18.sp)
                )

            onDrawBehind {
                drawRect(pinkColor, size = measuredText.size.toSize())
                drawText(measuredText)
            }
        }
        .fillMaxSize()
)
```

<br />

The text is now drawn in the constraints with an ellipsis at the end:
![Text drawn on pink background, with ellipsis cutting off the text.](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_text_ellipsis.png) **Figure 10** . `TextOverflow.Ellipsis` with fixed constraints on measuring text.

> [!NOTE]
> **Note:** For more information on text, see the [Text](https://developer.android.com/develop/ui/compose/text) documentation.

### Draw image

To draw an [`ImageBitmap`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap) with `DrawScope`, load up the image using
`ImageBitmap.imageResource()` and then call `drawImage`:


```kotlin
val dogImage = ImageBitmap.imageResource(id = R.drawable.dog)

Canvas(modifier = Modifier.fillMaxSize(), onDraw = {
    drawImage(dogImage)
})
```

<br />

![An image of a dog drawn on Canvas](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_image.png) **Figure 11** . Drawing an `ImageBitmap` on Canvas.

> [!NOTE]
> **Note:** See the [Image customization documentation](https://developer.android.com/develop/ui/compose/graphics/images/customize) for more information on how to apply filters to your images.

### Draw basic shapes

There are many shape drawing functions on `DrawScope`. To draw a shape, use one
of the predefined draw functions, such as `drawCircle`:


```kotlin
val purpleColor = Color(0xFFBA68C8)
Canvas(
    modifier = Modifier
        .fillMaxSize()
        .padding(16.dp),
    onDraw = {
        drawCircle(purpleColor)
    }
)
```

<br />

|---|---|
| API | Output |
| [`drawCircle()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawCircle(androidx.compose.ui.graphics.Brush,kotlin.Float,androidx.compose.ui.geometry.Offset,kotlin.Float,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw circle](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_draw_circle.png) |
| [`drawRect()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawRect(androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Size,kotlin.Float,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw rect](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_rect.png) |
| [`drawRoundedRect()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawRoundRect(androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Size,androidx.compose.ui.geometry.CornerRadius,kotlin.Float,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw rounded rect](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_rounded_rect.png) |
| [`drawLine()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawLine(androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Offset,kotlin.Float,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.graphics.PathEffect,kotlin.Float,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw line](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_line.png) |
| [`drawOval()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawOval(androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Size,kotlin.Float,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw oval](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_oval.png) |
| [`drawArc()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawArc(androidx.compose.ui.graphics.Brush,kotlin.Float,kotlin.Float,kotlin.Boolean,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Size,kotlin.Float,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw arc](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_arc.png) |
| [`drawPoints()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#drawPoints(kotlin.collections.List,androidx.compose.ui.graphics.PointMode,androidx.compose.ui.graphics.Brush,kotlin.Float,androidx.compose.ui.graphics.StrokeCap,androidx.compose.ui.graphics.PathEffect,kotlin.Float,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.BlendMode)) | ![draw points](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_points.png) |

### Draw path

A path is a series of mathematical instructions that result in a drawing once
executed. `DrawScope` can draw a path using the `DrawScope.drawPath()` method.

For example, say you wanted to draw a triangle. You can generate a path with
functions such as `lineTo()` and `moveTo()` using the size of the drawing area.
Then, call `drawPath()` with this newly created path to get a triangle.


```kotlin
Spacer(
    modifier = Modifier
        .drawWithCache {
            val path = Path()
            path.moveTo(0f, 0f)
            path.lineTo(size.width / 2f, size.height / 2f)
            path.lineTo(size.width, 0f)
            path.close()
            onDrawBehind {
                drawPath(path, Color.Magenta, style = Stroke(width = 10f))
            }
        }
        .fillMaxSize()
)
```

<br />

![An upside-down purple path triangle drawn on Compose](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_path.png) **Figure 12** . Creating and drawing a `Path` in Compose.

## Accessing `Canvas` object

With `DrawScope`, you don't have direct access to a `Canvas` object. You can use
[`DrawScope.drawIntoCanvas()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).drawIntoCanvas(kotlin.Function1)) to get
access to the `Canvas` object itself that you can call functions on.

For example, if you have a custom `Drawable` that you'd like to draw onto the
canvas, you can access the canvas and call `Drawable#draw()`, passing in the
`Canvas` object:


```kotlin
val drawable = ShapeDrawable(OvalShape())
Spacer(
    modifier = Modifier
        .drawWithContent {
            drawIntoCanvas { canvas ->
                drawable.setBounds(0, 0, size.width.toInt(), size.height.toInt())
                drawable.draw(canvas.nativeCanvas)
            }
        }
        .fillMaxSize()
)
```

<br />

![An oval black ShapeDrawable taking up full size](https://developer.android.com/static/develop/ui/compose/images/graphics/introduction/compose_graphics_canvas_draw_into_canvas.png) **Figure 13** . Accessing canvas to draw a `Drawable`.

## Learn more

For more information on Drawing in Compose, take a look at the following
resources:

- [Graphics Modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers) - Learn about the different types of drawing modifiers.
- [Brush](https://developer.android.com/develop/ui/compose/graphics/draw/brush) - Learn how to customize the painting of your content.
- [Custom Layouts and Graphics in Compose - Android Dev Summit
  2022](https://www.youtube.com/watch?v=xcfEQO0k_gU&ab_channel=AndroidDevelopers) - Learn how to build a custom UI in Compose with Layouts and Graphics.
- [JetLagged Sample](https://github.com/android/compose-samples/tree/main/JetLagged) - Compose Sample that shows how to draw a custom graph.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Graphics Modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers)
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics)
- [Alignment lines in Jetpack Compose](https://developer.android.com/develop/ui/compose/layouts/alignment-lines)