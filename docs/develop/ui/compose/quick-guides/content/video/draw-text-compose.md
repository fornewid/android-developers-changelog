---
title: Draw text in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/draw-text-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Draw text in Compose Stay organized with collections Save and categorize content based on your preferences.



See how to use Compose APIs specifically designed to draw text on a canvas. This
segment shows the code to draw an emoji font in a rounded rectangle.

## Key points

* In Compose, you can draw text on a canvas by creating a text measure and
  calling [`drawText`](/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope#(androidx.compose.ui.graphics.drawscope.DrawScope).drawText(androidx.compose.ui.text.TextLayoutResult,androidx.compose.ui.graphics.Brush,androidx.compose.ui.geometry.Offset,kotlin.Float,androidx.compose.ui.graphics.Shadow,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.graphics.drawscope.DrawStyle,androidx.compose.ui.graphics.BlendMode)), resulting in the measuring string.
* You can also customize the text size, alignment, and other properties.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways
you can present text in your app to provide a delightful user
experience.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-text)

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