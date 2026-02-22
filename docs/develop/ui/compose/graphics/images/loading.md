---
title: https://developer.android.com/develop/ui/compose/graphics/images/loading
url: https://developer.android.com/develop/ui/compose/graphics/images/loading
source: md.txt
---

## Load an image from the disk

Use the [`Image`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#Image) composable to display a graphic on screen. To load an image
(for example: PNG, JPEG, WEBP) or vector resource from the disk, use the
[`painterResource`](https://developer.android.com/develop/ui/compose/quick-guides/content/load-images?hl=en) API with your image reference. You don't need to know the type
of the asset, just use `painterResource` in `Image` or `paint` modifiers.

`DrawScope`:


```kotlin
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description)
)
```

<br />

To ensure that your app is [accessible](https://developer.android.com/develop/ui/compose/accessibility), supply a `contentDescription` for
visual elements on screen. TalkBack reads out the content description, so you
must ensure that the text is meaningful if read out loud and translated. In the
above example, a `stringResource()` is used to load up the translated content
description from the `strings.xml` file. If your visual element on screen is
purely for visual decoration, set your `contentDescription` to `null` for the
screen reader to ignore it.

If you need lower-level `ImageBitmap` specific functionality, you can use
`ImageBitmap.imageResource()` to load up a Bitmap. For more information on
ImageBitmaps, read the [ImageBitmap versus ImageVector](https://developer.android.com/develop/ui/compose/graphics/images/compare) section.

### Drawable support

`painterResource` currently supports the following drawable types:

- [`AnimatedVectorDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable)
- [`BitmapDrawable`](https://developer.android.com/reference/android/graphics/drawable/BitmapDrawable) (PNG, JPG, WEBP)
- [`ColorDrawable`](https://developer.android.com/reference/android/graphics/drawable/ColorDrawable)
- [`VectorDrawable`](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable)

## Load an image from the internet

To load an image from the internet, there are several third-party libraries
available to help you handle the process. Image loading libraries do a lot of
the heavy lifting for you; they handle both caching (so you don't download the
image multiple times) and networking logic to download the image and display it
on screen.

For example, to load an image with [Coil](https://github.com/coil-kt/coil#jetpack-compose)
from Instacart, add the library to your gradle file, and use an `AsyncImage` to load an image from a URL:


```kotlin
AsyncImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)
```

<br />

[### Coil](https://github.com/coil-kt/coil#jetpack-compose)

An image loading library backed by Kotlin Coroutines (Instacart).
[![Maven version for Coil](https://img.shields.io/maven-central/v/io.coil-kt/coil-compose)](https://search.maven.org/artifact/io.coil-kt/coil-compose "Maven version of the library") [### Glide](https://bumptech.github.io/glide/int/compose.html)

A fast and efficient image loading library for Android focused on smooth scrolling (Google).
[![Maven version for Glide](https://img.shields.io/maven-central/v/com.github.bumptech.glide/compose)](https://search.maven.org/artifact/com.github.bumptech.glide/compose "Maven version of the library")

## Additional resources

- [Load and display images](https://developer.android.com/develop/ui/compose/quick-guides/content/load-images?hl=en)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Resources in Compose](https://developer.android.com/develop/ui/compose/resources)
- [Accessibility in Compose](https://developer.android.com/develop/ui/compose/accessibility)
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview)