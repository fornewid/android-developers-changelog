---
title: Image bitmap versus image vector  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/graphics/images/compare
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Image bitmap versus image vector Stay organized with collections Save and categorize content based on your preferences.



The two most common kinds of image formats are raster and vector images.

A raster graphic format contains pixels: tiny individual squares that contain a
color (made up of red, green, blue, and alpha values). When placing a lot of
pixels together, a very detailed image can be formed, such as a photograph. A
raster graphic has a fixed resolution (fixed number of pixels). This means that
when you increase the size of the image, it loses detail, and pixelation can
occur. Examples of raster graphic formats are JPEG, PNG, and WEBP.

![A close-up photograph of a golden retriever dog.](/static/develop/ui/compose/images/graphics-sourceimage.jpg)


**Figure 1.** JPEG file example.

Vector images, on the other hand, are scalable mathematical representations of a
visual element on screen. A vector is a set of commands describing how to draw
the image on screen—for example, a line, point, or fill. When scaling a vector
on screen, it won't lose quality, as the mathematical formula maintains the
relationship between the different commands. Good examples of `ImageVector`s are
the Material [Symbols](https://fonts.google.com/icons), as they can all be defined with mathematical
formulas.

![A simple line-art icon of a shopping cart with a handle, basket, and two wheels.](/static/develop/ui/compose/images/graphics-shopping.png)


**Figure 2**. Vector example (file extensions are .xml or defined in Kotlin code).

## `ImageBitmap`

In Compose, a raster image (often referred to as a `Bitmap`) can be loaded up
into an `ImageBitmap` instance, and a `BitmapPainter` is what is responsible for
drawing the bitmap to screen.

For basic use cases, `painterResource()` can be used to create an `ImageBitmap`
and returns a `Painter` object (in this case - a `BitmapPainter`):

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description)
)

VectorVsBitmapSnippets.kt
```

If you require further customization (for example, a [custom painter
implementation](/develop/ui/compose/graphics/images/custompainter)) and need access to the `ImageBitmap` itself, you can load it
in the following way:

```
val imageBitmap = ImageBitmap.imageResource(R.drawable.dog)

VectorVsBitmapSnippets.kt
```

## `ImageVector`

A `VectorPainter` is responsible for drawing an `ImageVector` to screen.
`ImageVector` supports a subset of Scalable Vector Graphics (SVG) commands. Not
all images can be represented as vectors (for example, the photos you take with
your camera cannot be transformed into a vector).

You can create a custom `ImageVector` either by importing an existing vector
drawable XML file (imported into Android Studio using the [import tool](/studio/write/vector-asset-studio#running)) or
implementing the class and issuing path commands manually.

For basic use cases, `painterResource()` works for `ImageVectors` in the same
way it does for the `ImageBitmap` class, returning a `VectorPainter` as the
result. `painterResource()` handles the loading of `VectorDrawables` and
`BitmapDrawables` into `VectorPainter` and `BitmapPainter` respectively. To load
a `VectorDrawable` into an image, use:

```
Image(
    painter = painterResource(id = R.drawable.baseline_shopping_cart_24),
    contentDescription = stringResource(id = R.string.shopping_cart_content_desc)
)

VectorVsBitmapSnippets.kt
```

If you require further customization and need to access to the `ImageVector`
itself, you can load it in the following way:

```
val imageVector = ImageVector.vectorResource(id = R.drawable.baseline_shopping_cart_24)

VectorVsBitmapSnippets.kt
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Custom painter {:#custom-painter}](/develop/ui/compose/graphics/images/custompainter)
* [Resources in Compose](/develop/ui/compose/resources)
* [Loading images {:#loading-images}](/develop/ui/compose/graphics/images/loading)

[Previous

arrow\_back

Loading images](/develop/ui/compose/graphics/images/loading)

[Next

Material icons

arrow\_forward](/develop/ui/compose/graphics/images/material)