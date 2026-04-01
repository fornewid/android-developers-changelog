---
title: Load and display images  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/load-images
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Load and display images Stay organized with collections Save and categorize content based on your preferences.




To display images in your app for content and for responses to user actions,
load the images from the disk or from an external source on the internet. You
can load images the following ways:

* From the disk
* From a network using Coil
* From a network using Glide

## Results

![An image of a dog](/static/develop/ui/compose/quick-guides/content/dog.png)


**Figure 1.** An image loaded and displayed.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

## Load an image from the disk

You can load locally stored images from the disk to display them in your app for
content and to respond to user actions.

### Dependencies

### Load the image

Use the following code to load a locally stored image from the disk to display
in your app:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description)
)

LoadingImagesSnippets.kt
```

#### Key points about the code

* A defined Compose [`Image`](/reference/kotlin/androidx/compose/foundation/Image.composable) object with a `painter` attribute set to a
  [`painterResource()`](/reference/kotlin/androidx/compose/ui/res/package-summary#painterresource) that loads an image from app resources.
* A `contentDescription` that `TalkBack` can read to make your app more
  accessible.
* A `stringResource()` to load translated content description from the
  `strings.xml` file.

## Load an image over the network

You can load images stored externally on the internet using either Coil or
Glide. To choose which library to use for your project, consider factors such as
project requirements and performance constraints.

### Load an image using Coil

You can load images from the internet using [Coil](https://coil-kt.github.io/coil/), a third-party
library. Coil is backed by Kotlin coroutines, and takes responsibility for
loading the image away from the Main thread, and displays it once loaded. Follow
this guidance to load images from the internet using Coil.

### Dependencies

#### Load the image

Use the following code to load images using Coil:

```
AsyncImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)

LoadingImagesSnippets.kt
```

### Load an image using Glide

You can load images stored externally on the internet using
[Glide](https://github.com/bumptech/glide) to display them in your app's feed. Glide is a fast and
efficient image loading library for Android focused on smooth scrolling, and
takes responsibility for loading the image away from the Main thread, and
displays it once loaded.

#### Dependencies

#### Load the image

Use the following code to load images using Glide:

```
GlideImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)

LoadingImagesSnippets.kt
```

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