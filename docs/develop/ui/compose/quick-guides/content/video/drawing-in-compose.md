---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/video/drawing-in-compose
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/drawing-in-compose
source: md.txt
---

<br />

Learn how to draw something custom in Compose. With custom drawing, you can
improve the look and feel of your app when the built-in components don't cover
exactly what your app needs.  

## Key points

- [`DrawScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/drawscope/DrawScope) is a declarative, stateless drawing API to draw shapes, paths, and more without needing to maintain the state of the component manually.
- Several drawing modifiers give you access to `DrawScope`, letting you draw with other composables:
  - [`drawBehind`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawBehind(kotlin.Function1)): draws behind the composables content.
  - [`drawWithContent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithContent(kotlin.Function1)): useful for rearranging content. You can choose when to call the content of the composable, either before or after.
  - [`drawWithCache`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).drawWithCache(kotlin.Function1)): caches the objects until the size changes or the state variables read inside change.
- The coordinate system in Compose is the same as the view system.
- All draw and layout calls are performed in pixel values, not [`dp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/unit/package-summary#(kotlin.Int).dp()). To draw consistently across screens, use `dp` and convert to pixels before drawing.
- Draw calls are always relative to the parent composable.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Display images

Discover techniques for using bright, engaging visuals to give your Android app a beautiful look and feel.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-images)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)