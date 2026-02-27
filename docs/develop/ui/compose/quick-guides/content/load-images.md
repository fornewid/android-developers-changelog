---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/load-images
url: https://developer.android.com/develop/ui/compose/quick-guides/content/load-images
source: md.txt
---

<br />

To display images in your app for content and for responses to user actions,
load the images from the disk or from an external source on the internet. You
can load images the following ways:

- From the disk
- From a network using Coil
- From a network using Glide

## Results

:dog: **Figure 1.** An image loaded and displayed.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

## Load an image from the disk

You can load locally stored images from the disk to display them in your app for
content and to respond to user actions.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/load-images_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Load the image

Use the following code to load a locally stored image from the disk to display
in your app:


```kotlin
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description)
)
```

<br />

#### Key points about the code

- A defined Compose [`Image`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#Image) object with a `painter` attribute set to a [`painterResource()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/res/package-summary#painterresource) that loads an image from app resources.
- A `contentDescription` that `TalkBack` can read to make your app more accessible.
- A `stringResource()` to load translated content description from the `strings.xml` file.

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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/load-images_331ebc57e656a7ad92549b590ed3e49228694c1d4c5f0e52419b3dc4167c538d.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

#### Load the image

Use the following code to load images using Coil:


```kotlin
AsyncImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)
```

<br />

### Load an image using Glide

You can load images stored externally on the internet using
[Glide](https://github.com/bumptech/glide) to display them in your app's feed. Glide is a fast and
efficient image loading library for Android focused on smooth scrolling, and
takes responsibility for loading the image away from the Main thread, and
displays it once loaded.

#### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/load-images_461feebb02a68d4439700b6d42650b53231d42aa70d6e374e1eb3425e7ec956a.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

#### Load the image

Use the following code to load images using Glide:


```kotlin
GlideImage(
    model = "https://example.com/image.jpg",
    contentDescription = "Translated description of what the image contains"
)
```

<br />

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display images

Discover techniques for using bright, engaging visuals to give your Android app a beautiful look and feel. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-images) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)