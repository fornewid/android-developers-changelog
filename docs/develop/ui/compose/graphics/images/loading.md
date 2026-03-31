---
title: Loading images  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/graphics/images/loading
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Loading images Stay organized with collections Save and categorize content based on your preferences.




## Load an image from the disk

Use the [`Image`](/reference/kotlin/androidx/compose/foundation/Image.composable) composable to display a graphic on screen. To load an image
(for example: PNG, JPEG, WEBP) or vector resource from the disk, use the
[`painterResource`](/develop/ui/compose/quick-guides/content/load-images?hl=en) API with your image reference. You don't need to know the type
of the asset, just use `painterResource` in `Image` or `paint` modifiers.

`DrawScope`:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description)
)

LoadingImagesSnippets.kt
```

To ensure that your app is [accessible](/develop/ui/compose/accessibility), supply a `contentDescription` for
visual elements on screen. TalkBack reads out the content description, so you
must ensure that the text is meaningful if read out loud and translated. In the
above example, a `stringResource()` is used to load up the translated content
description from the `strings.xml` file. If your visual element on screen is
purely for visual decoration, set your `contentDescription` to `null` for the
screen reader to ignore it.

If you need lower-level `ImageBitmap` specific functionality, you can use
`ImageBitmap.imageResource()` to load up a Bitmap. For more information on
ImageBitmaps, read the [ImageBitmap versus ImageVector](/develop/ui/compose/graphics/images/compare) section.

### Drawable support

`painterResource` currently supports the following drawable types:

* [`AnimatedVectorDrawable`](/reference/android/graphics/drawable/AnimatedVectorDrawable)
* [`BitmapDrawable`](/reference/android/graphics/drawable/BitmapDrawable) (PNG, JPG, WEBP)
* [`ColorDrawable`](/reference/android/graphics/drawable/ColorDrawable)
* [`VectorDrawable`](/reference/android/graphics/drawable/VectorDrawable)

## Load an image from the internet

To load an image from the internet, there are several third-party libraries
available to help you handle the process. Image loading libraries do a lot of
the heavy lifting for you; they handle both caching (so you don't download the
image multiple times) and networking logic to download the image and display it
on screen.

For example, to load an image with [Coil](https://github.com/coil-kt/coil#jetpack-compose)
from Instacart, add the library to your gradle file, and use an `AsyncImage` to load an image from a URL:

```
AsyncImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)

LoadingImagesSnippets.kt
```

[### Coil](https://github.com/coil-kt/coil#jetpack-compose)

An image loading library backed by Kotlin Coroutines (Instacart).

[![Maven version for Coil](https://img.shields.io/maven-central/v/io.coil-kt/coil-compose)](https://search.maven.org/artifact/io.coil-kt/coil-compose "Maven version of the library")

[### Glide](https://bumptech.github.io/glide/int/compose.html)

A fast and efficient image loading library for Android focused on smooth scrolling (Google).

[![Maven version for Glide](https://img.shields.io/maven-central/v/com.github.bumptech.glide/compose)](https://search.maven.org/artifact/com.github.bumptech.glide/compose "Maven version of the library")

## Additional resources

* [Load and display images](/develop/ui/compose/quick-guides/content/load-images?hl=en)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Resources in Compose](/develop/ui/compose/resources)
* [Accessibility in Compose](/develop/ui/compose/accessibility)
* [Graphics in Compose](/develop/ui/compose/graphics/draw/overview)

[Previous

arrow\_back

Overview](/develop/ui/compose/graphics/images)

[Next

ImageBitmap vs ImageVector

arrow\_forward](/develop/ui/compose/graphics/images/compare)