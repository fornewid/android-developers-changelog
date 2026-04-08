---
title: https://developer.android.com/develop/ui/compose/graphics/draw/brush
url: https://developer.android.com/develop/ui/compose/graphics/draw/brush
source: md.txt
---

[Video](https://www.youtube.com/watch?v=qh72KAX6TSI)

A [`Brush`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush) in Compose describes how something is drawn on screen: it
determines the color(s) that are drawn in the drawing area (i.e. a circle,
square, path). There are a few built-in Brushes that are useful for drawing,
such as [`LinearGradient`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/LinearGradient), [`RadialGradient`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/RadialGradient) or a plain
[`SolidColor`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/SolidColor) brush.

Brushes can be used with [`Modifier.background()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier.background(androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Shape))), [`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle), or
[`DrawScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope) draw calls to apply the painting style to the content
being drawn.

For example, a horizontal gradient brush can be applied to drawing a circle in
`DrawScope`:


```kotlin
val brush = Brush.horizontalGradient(listOf(Color.Red, Color.Blue))
Canvas(
    modifier = Modifier.size(200.dp),
    onDraw = {
        drawCircle(brush)
    }
)
```
![Circle drawn with Horizontal Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/draw_circle_example.png) **Figure 1**: Circle drawn with Horizontal Gradient

<br />

## Gradient brushes

There are many built-in gradient brushes that can be used to achieve different
gradient effects. These brushes allow you to specify the list of colors that you
would like to create a gradient from.

A list of available gradient brushes and their corresponding output:

| Gradient Brush Type | Output |
|---|---|
| [`Brush.horizontalGradient(colorList)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush#horizontalGradient(kotlin.collections.List,kotlin.Float,kotlin.Float,androidx.compose.ui.graphics.TileMode)) | ![Horizontal Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/horizontal_gradient.png) |
| [`Brush.linearGradient(colorList)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush#linearGradient(kotlin.Array,androidx.compose.ui.geometry.Offset,androidx.compose.ui.geometry.Offset,androidx.compose.ui.graphics.TileMode)) | ![Linear Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/linear_gradient.png) |
| [`Brush.verticalGradient(colorList)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush#verticalGradient(kotlin.collections.List,kotlin.Float,kotlin.Float,androidx.compose.ui.graphics.TileMode)) | ![Vertical Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/vertical_gradient.png) |
| [`Brush.sweepGradient(colorList)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush#sweepGradient(kotlin.Array,androidx.compose.ui.geometry.Offset)) Note: To get a smooth transition between colors - set the last color to the start color. | ![Sweep Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/sweep_gradient.png) |
| [`Brush.radialGradient(colorList)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Brush#radialGradient(kotlin.Array,androidx.compose.ui.geometry.Offset,kotlin.Float,androidx.compose.ui.graphics.TileMode)) | ![Radial Gradient](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/radial_gradient.png) |

### Change distribution of colors with `colorStops`

To customize how the colors appear in the gradient, you can tweak the
`colorStops` value for each one. `colorStops` should be specified as a fraction,
between 0 and 1. Values greater than 1 will result in those colors not rendering
as part of the gradient.

You can configure the color stops to have different amounts, such as less or
more of one color:


```kotlin
val colorStops = arrayOf(
    0.0f to Color.Yellow,
    0.2f to Color.Red,
    1f to Color.Blue
)
Box(
    modifier = Modifier
        .requiredSize(200.dp)
        .background(Brush.horizontalGradient(colorStops = colorStops))
)
```

<br />

The colors are dispersed at the provided offset as defined in the `colorStop`
pair, less yellow than red and blue.
![Brush configured with different color stops](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/color_stops.png) **Figure 2**: Brush configured with different color stops

### Repeat a pattern with `TileMode`

Each gradient brush has the option to set a [`TileMode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/TileMode) on it. You may not
notice the `TileMode` if you haven't set a start and end for the gradient, as
it'll default to fill the whole area. A `TileMode` will only tile the gradient
if the size of the area is bigger than the Brush size.

The following code will repeat the gradient pattern 4 times, since the `endX` is
set to `50.dp` and the size is set to `200.dp`:


```kotlin
val listColors = listOf(Color.Yellow, Color.Red, Color.Blue)
val tileSize = with(LocalDensity.current) {
    50.dp.toPx()
}
Box(
    modifier = Modifier
        .requiredSize(200.dp)
        .background(
            Brush.horizontalGradient(
                listColors,
                endX = tileSize,
                tileMode = TileMode.Repeated
            )
        )
)
```

<br />

Here is a table detailing what the different Tile Modes do for the
`HorizontalGradient` example above:

| TileMode | Output |
|---|---|
| [`TileMode.Repeated`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/TileMode#Repeated()): Edge is repeated from last color to first. | ![TileMode Repeated](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/tile_mode_repeated.png) |
| [`TileMode.Mirror`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/TileMode#Mirror()): Edge is mirrored from last color to first. | ![TileMode Mirror](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/tile_mode_mirror.png) |
| [`TileMode.Clamp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/TileMode#Clamp()): Edge is clamped to the final color. It'll then paint the closest color for the rest of the region. | ![Tile Mode Clamp](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/tile_mode_clamp.png) |
| [`TileMode.Decal`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/TileMode#Decal()): Render only up to the size of the bounds. `TileMode.Decal` leverages transparent black to sample content outside the original bounds whereas `TileMode.Clamp` samples the edge color. | ![Tile Mode Decal](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/tile_mode_decal.png) |

> [!NOTE]
> **Note:** `TileMode.Decal` is only available on API 31+. Use `TileMode.isSupported()` to determine if a `TileMode` is supported on a device. If a `TileMode` that is not supported is used, the default of `TileMode.Clamp` is applied.

`TileMode` works in a similar way for the other directional gradients, the
difference being the direction that the repetition occurs.

### Change brush Size

If you know the size of the area in which your brush will be drawn, you can
set the tile `endX` as we've seen above in the `TileMode` section. If you are in
a `DrawScope`, you can use its [`size`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#size()) property to get the size of the area.

If you don't know the size of your drawing area (for example if the
`Brush` is assigned to Text), you can extend `Shader` and utilize the size of
the drawing area in the `createShader` function.

In this example, divide the size by 4 to repeat the pattern 4 times:


```kotlin
val listColors = listOf(Color.Yellow, Color.Red, Color.Blue)
val customBrush = remember {
    object : ShaderBrush() {
        override fun createShader(size: Size): Shader {
            return LinearGradientShader(
                colors = listColors,
                from = Offset.Zero,
                to = Offset(size.width / 4f, 0f),
                tileMode = TileMode.Mirror
            )
        }
    }
}
Box(
    modifier = Modifier
        .requiredSize(200.dp)
        .background(customBrush)
)
```

<br />

![Shader size divided by 4](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/tile_mode_mirror.png) **Figure 3**: Shader size divided by 4

You can also change the brush size of any other gradient, such as radial
gradients. If you don't specify a size and center, the gradient will occupy the
full bounds of the `DrawScope`, and the center of the radial gradient defaults
to the center of the `DrawScope` bounds. This results in the radial gradient's
center appearing as the center of the smaller dimension (either width or
height):


```kotlin
Box(
    modifier = Modifier
        .fillMaxSize()
        .background(
            Brush.radialGradient(
                listOf(Color(0xFF2be4dc), Color(0xFF243484))
            )
        )
)
```

<br />

![Radial Gradient set without size changes](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/radial_gradient_default.png) **Figure 4**: Radial Gradient set without size changes

When the radial gradient is changed to set the radius size to the max dimension,
you can see that it produces a better radial gradient effect:


```kotlin
val largeRadialGradient = object : ShaderBrush() {
    override fun createShader(size: Size): Shader {
        val biggerDimension = maxOf(size.height, size.width)
        return RadialGradientShader(
            colors = listOf(Color(0xFF2be4dc), Color(0xFF243484)),
            center = size.center,
            radius = biggerDimension / 2f,
            colorStops = listOf(0f, 0.95f)
        )
    }
}

Box(
    modifier = Modifier
        .fillMaxSize()
        .background(largeRadialGradient)
)
```

<br />

![Bigger radius on radial gradient, based on size of area](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/radial_size_biggest_dimension.png) **Figure 5**: Bigger radius on radial gradient, based on size of area

It is worth noting that the actual size that is passed into the creation of the
shader is determined from where it is invoked. By default, `Brush` will
reallocate its `Shader` internally if the size is different from the last
creation of the `Brush`, or if a state object used in creation of the shader has
changed.

The following code creates the shader three different times with different
sizes, as the size of the drawing area changes:


```kotlin
val colorStops = arrayOf(
    0.0f to Color.Yellow,
    0.2f to Color.Red,
    1f to Color.Blue
)
val brush = Brush.horizontalGradient(colorStops = colorStops)
Box(
    modifier = Modifier
        .requiredSize(200.dp)
        .drawBehind {
            drawRect(brush = brush) // will allocate a shader to occupy the 200 x 200 dp drawing area
            inset(10f) {
      /* Will allocate a shader to occupy the 180 x 180 dp drawing area as the
       inset scope reduces the drawing  area by 10 pixels on the left, top, right,
      bottom sides */
                drawRect(brush = brush)
                inset(5f) {
        /* will allocate a shader to occupy the 170 x 170 dp drawing area as the
         inset scope reduces the  drawing area by 5 pixels on the left, top,
         right, bottom sides */
                    drawRect(brush = brush)
                }
            }
        }
)
```

<br />

## Use an image as a brush

To use an [ImageBitmap](https://developer.android.com/develop/ui/compose/graphics/images/compare#image-bitmap) as a `Brush`, load up the image as an `ImageBitmap`,
and create an `ImageShader` brush:


```kotlin
val imageBrush =
    ShaderBrush(ImageShader(ImageBitmap.imageResource(id = R.drawable.dog)))

// Use ImageShader Brush with background
Box(
    modifier = Modifier
        .requiredSize(200.dp)
        .background(imageBrush)
)

// Use ImageShader Brush with TextStyle
Text(
    text = "Hello Android!",
    style = TextStyle(
        brush = imageBrush,
        fontWeight = FontWeight.ExtraBold,
        fontSize = 36.sp
    )
)

// Use ImageShader Brush with DrawScope#drawCircle()
Canvas(onDraw = {
    drawCircle(imageBrush)
}, modifier = Modifier.size(200.dp))
```

<br />

The Brush is applied to a few different types of drawing: a background, the Text
and Canvas. This outputs the following:
![ImageShader Brush used in different ways](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/image_brush.png) **Figure 6**: Using ImageShader Brush to draw a background, draw Text and draw a Circle

Notice that the text is now also rendered using the `ImageBitmap` to paint the
pixels for the text.

## Advanced example: Custom brush

### AGSL `RuntimeShader` brush

[Video](https://www.youtube.com/watch?v=wJx7EhGaDow)

[AGSL](https://developer.android.com/develop/ui/views/graphics/agsl) offers a subset of [GLSL](https://developer.android.com/develop/ui/views/graphics/agsl/agsl-vs-glsl) Shader capabilities. Shaders can be
written in AGSL and used with a Brush in Compose.

To create a Shader brush, first define the Shader as AGSL shader string:


```kotlin
@Language("AGSL")
val CUSTOM_SHADER = """
    uniform float2 resolution;
    layout(color) uniform half4 color;
    layout(color) uniform half4 color2;

    half4 main(in float2 fragCoord) {
        float2 uv = fragCoord/resolution.xy;

        float mixValue = distance(uv, vec2(0, 1));
        return mix(color, color2, mixValue);
    }
""".trimIndent()
```

<br />

The shader above takes two input colors, calculates the distance from the bottom
left (`vec2(0, 1)`) of the drawing area and does a `mix` between the two colors
based on the distance. This produces a gradient effect.

Then, create the Shader Brush, and set the uniforms for `resolution` - the size
of the drawing area, and the `color` and `color2` you want to use as input to
your custom gradient:


```kotlin
val Coral = Color(0xFFF3A397)
val LightYellow = Color(0xFFF8EE94)

@RequiresApi(Build.VERSION_CODES.TIRAMISU)
@Composable
@Preview
fun ShaderBrushExample() {
    Box(
        modifier = Modifier
            .drawWithCache {
                val shader = RuntimeShader(CUSTOM_SHADER)
                val shaderBrush = ShaderBrush(shader)
                shader.setFloatUniform("resolution", size.width, size.height)
                onDrawBehind {
                    shader.setColorUniform(
                        "color",
                        android.graphics.Color.valueOf(
                            LightYellow.red, LightYellow.green,
                            LightYellow
                                .blue,
                            LightYellow.alpha
                        )
                    )
                    shader.setColorUniform(
                        "color2",
                        android.graphics.Color.valueOf(
                            Coral.red,
                            Coral.green,
                            Coral.blue,
                            Coral.alpha
                        )
                    )
                    drawRect(shaderBrush)
                }
            }
            .fillMaxWidth()
            .height(200.dp)
    )
}
```

<br />

Running this, you can see the following rendered on screen:
![Custom AGSL Shader running in Compose](https://developer.android.com/static/develop/ui/compose/images/graphics/brush/shaders.png) **Figure 7**: Custom AGSL Shader running in Compose

It's worth noting that you can do a lot more with shaders than just gradients,
as it's all math-based calculations. For more information on AGSL, check out the
AGSL [documentation](https://developer.android.com/develop/ui/views/graphics/agsl).

> [!NOTE]
> **Note:** `RuntimeShaders` only works on Android 13+. Wrap your Composable in an API if-else check and provide a suitable fallback.

## Additional resources

For more examples of using Brush in Compose, check out the following resources:

- [Animating brush Text coloring in Compose 🖌️](https://medium.com/androiddevelopers/animating-brush-text-coloring-in-compose-%EF%B8%8F-26ae99d9b402)
- [Custom Graphics and Layouts in Compose - Android Dev Summit 2022](https://youtu.be/xcfEQO0k_gU)
- [JetLagged Sample - RuntimeShader Brush](https://github.com/android/compose-samples/blob/main/JetLagged/app/src/main/java/com/example/jetlagged/Background.kt)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Graphics Modifiers](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers)
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview)
- [Style text](https://developer.android.com/develop/ui/compose/text/style-text)