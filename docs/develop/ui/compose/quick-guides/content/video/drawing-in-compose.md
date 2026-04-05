---
title: Intro to drawing in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/drawing-in-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Intro to drawing in Compose Stay organized with collections Save and categorize content based on your preferences.




Learn how to draw something custom in Compose. With custom drawing, you can
improve the look and feel of your app when the built-in components don't cover
exactly what your app needs.

## Key points

* [`DrawScope`](/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope) is a declarative, stateless drawing API to draw shapes,
  paths, and more without needing to maintain the state of the component
  manually.
* Several drawing modifiers give you access to `DrawScope`, letting you draw
  with other composables:
  + [`drawBehind`](/reference/kotlin/androidx/compose/ui/draw/drawBehind.modifier#(androidx.compose.ui.Modifier).drawBehind(kotlin.Function1)): draws behind the composables content.
  + [`drawWithContent`](/reference/kotlin/androidx/compose/ui/draw/drawWithContent.modifier#(androidx.compose.ui.Modifier).drawWithContent(kotlin.Function1)): useful for rearranging content. You can choose
    when to call the content of the composable, either before or after.
  + [`drawWithCache`](/reference/kotlin/androidx/compose/ui/draw/drawWithCache.modifier#(androidx.compose.ui.Modifier).drawWithCache(kotlin.Function1)): caches the objects until the size changes or the
    state variables read inside change.
* The coordinate system in Compose is the same as the view system.
* All draw and layout calls are performed in pixel values, not [`dp`](/reference/kotlin/androidx/compose/ui/unit/package-summary#(kotlin.Int).dp()). To
  draw consistently across screens, use `dp` and convert to pixels before
  drawing.
* Draw calls are always relative to the parent composable.

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