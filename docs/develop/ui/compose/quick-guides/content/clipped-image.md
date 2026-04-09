---
title: Display an image clipped to a shape  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/clipped-image
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Display an image clipped to a shape Stay organized with collections Save and categorize content based on your preferences.




You can fit an image to a clipped shape, and draw shadows around the perimeter
of the shape to impart a three-dimensional feel. This technique is useful for
creating designs such as avatars and product thumbnails, or displaying
logos with custom shapes.

To display an image clipped to a shape, you must do the following:

* Create the shape.
* Clip the image to the shape.

## Results

![Dog in hexagon with shadow applied around the edges](/static/develop/ui/compose/images/graphics/shapes/clip_with_shadow.png)


**Figure 1.** Custom shape applied as clip.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a shape

The following code creates a custom shape that can dynamically draw and render
a rounded polygon:

```
fun RoundedPolygon.getBounds() = calculateBounds().let { Rect(it[0], it[1], it[2], it[3]) }
class RoundedPolygonShape(
    private val polygon: RoundedPolygon,
    private var matrix: Matrix = Matrix()
) : Shape {
    private var path = Path()
    override fun createOutline(
        size: Size,
        layoutDirection: LayoutDirection,
        density: Density
    ): Outline {
        path.rewind()
        path = polygon.toPath().asComposePath()
        matrix.reset()
        val bounds = polygon.getBounds()
        val maxDimension = max(bounds.width, bounds.height)
        matrix.scale(size.width / maxDimension, size.height / maxDimension)
        matrix.translate(-bounds.left, -bounds.top)

        path.transform(matrix)
        return Outline.Generic(path)
    }
}

ShapesSnippets.kt
```

### Key points about the code

* `RoundedPolygon.getBounds()` defines an extension function on the
  [`RoundedPolygon`](/reference/kotlin/androidx/graphics/shapes/RoundedPolygon) class to calculate its bounds.
* The `RoundedPolygonShape` class implements the
  [`Shape`](/reference/kotlin/androidx/compose/ui/graphics/Shape) interface,
  allowing you to define a custom shape (a rounded polygon) in Jetpack Compose.
* The shape uses a [`Matrix`](/reference/kotlin/androidx/compose/ui/graphics/Matrix) to manage scaling and translation operations
  for flexible rendering.
* The `createOutline()` function takes a `RoundedPolygon` object, scales and
  translates it to fit within a given size, and returns an [`Outline`](/reference/kotlin/androidx/compose/ui/graphics/Outline) object
  that describes the final shape to be drawn.

## Clip the image to a shape

The following code crops the image to a hexagon, and adds a subtle drop
shadow to provide a sense of depth:

```
val hexagon = remember {
    RoundedPolygon(
        6,
        rounding = CornerRounding(0.2f)
    )
}
val clip = remember(hexagon) {
    RoundedPolygonShape(polygon = hexagon)
}
Box(
    modifier = Modifier
        .clip(clip)
        .background(MaterialTheme.colorScheme.secondary)
        .size(200.dp)
) {
    Text(
        "Hello Compose",
        color = MaterialTheme.colorScheme.onSecondary,
        modifier = Modifier.align(Alignment.Center)
    )
}

ShapesSnippets.kt
```

### Key points about the code

* The `RoundedPolygon` and `RoundedPolygonShape` objects are used to define and apply a hexagonal shape to the image.
* The code uses [`graphicsLayer`](/reference/kotlin/androidx/compose/ui/graphics/graphicsLayer.modifier#(androidx.compose.ui.Modifier).graphicsLayer(kotlin.Function1)) to add an elevation-based shadow to the image.
  This creates a sense of depth and visual separation from the background.
* The use of [`remember`](/reference/kotlin/androidx/compose/runtime/remember.composable#remember(kotlin.Function0)) blocks optimizes performance by ensuring that the shape
  and clipping definitions are calculated only once and remembered for later
  recompositions of the UI.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display images

Discover techniques for using bright, engaging visuals to
give your Android app a beautiful look and feel.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-images)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)