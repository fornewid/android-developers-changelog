---
title: https://developer.android.com/develop/ui/compose/touch-input/stylus-input/ink-api-modules
url: https://developer.android.com/develop/ui/compose/touch-input/stylus-input/ink-api-modules
source: md.txt
---

[Ink API](https://developer.android.com/jetpack/androidx/releases/ink#1.0.0-alpha01)is modularized, so you can use only what you need.

## Strokes

The[strokes](https://developer.android.com/reference/kotlin/androidx/ink/strokes/package-summary)module serves as the foundation of the Ink API. Key data types within this module are:

- [**`StrokeInputBatch`**](https://developer.android.com/reference/kotlin/androidx/ink/strokes/StrokeInputBatch): Represents a series of pointer inputs, including their position, timestamp, and optionally pressure, tilt, and orientation.
- [**`InProgressStroke`**](https://developer.android.com/reference/kotlin/androidx/ink/strokes/InProgressStroke): Represents a stroke that is actively being drawn.`InProgressStroke`is used to render partial strokes with low latency and to build the final`Stroke`once input is complete, after which the object can be reused.`InProgressStroke`is used by the[`InProgressStrokes`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1))composable.
- [**`Stroke`**](https://developer.android.com/reference/kotlin/androidx/ink/strokes/Stroke): An immutable representation of a finalized stroke with fixed geometry. Each`Stroke`has an[`ImmutableStrokeInputBatch`](https://developer.android.com/reference/kotlin/androidx/ink/strokes/ImmutableStrokeInputBatch)(input points), a[`Brush`](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush)(style), and a[`PartitionedMesh`](https://developer.android.com/reference/kotlin/androidx/ink/geometry/PartitionedMesh)(geometric shape). You can store, manipulate, and render strokes within your application.

## Geometry

The[Geometry](https://developer.android.com/reference/kotlin/androidx/ink/geometry/package-summary)module supports geometric operations on primitive shapes (using dedicated classes like[Box](https://developer.android.com/reference/kotlin/androidx/ink/geometry/Box&sa=D&source=docs&ust=1761326799140765&usg=AOvVaw1pQKRdqNKmIbX_E3mu9XBG)and[Vec](https://developer.android.com/reference/kotlin/androidx/ink/geometry/Vec)), as well as arbitrary shapes (using[PartitionedMesh](https://developer.android.com/reference/kotlin/androidx/ink/geometry/PartitionedMesh)), including intersection detection and transformation.[PartitionedMesh](https://developer.android.com/reference/kotlin/androidx/ink/geometry/PartitionedMesh)can also hold additional data to support rendering.

## Brush

The[`brush`](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush)module defines the style of strokes. It consists of two main parts:

- [**`Brush`**](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush): Specifies the style of a stroke including base color, base size, and[`BrushFamily`](https://developer.android.com/reference/kotlin/androidx/ink/brush/BrushFamily).`BrushFamily`is analogous to a font family, it defines a stroke's style. For example, a`BrushFamily`can represent a specific style of marker or highlighter, allowing strokes with different sizes and colors to share that style.
- [**`StockBrushes`**](https://developer.android.com/reference/kotlin/androidx/ink/brush/StockBrushes): Provides factory functions for creating ready-to-use`BrushFamily`instances.

## Authoring

The Compose[Authoring](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary)module lets you capture user touch input and render it as low-latency strokes on the screen in real time. This is achieved through the[`InProgressStrokes`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1))composable, which processes motion events and displays the strokes as they are drawn.

Once a stroke is completed, the composable notifies the client application using an[`InProgressStrokesFinishedListener`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesFinishedListener)callback. This allows the application to retrieve the finished strokes for rendering or storage.

In Compose,`InProgressStrokes`takes this callback in the`onStrokesFinished`parameter. Pass the finished strokes to another composable to commit them to the screen using the[rendering module](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/package-summary).

## Rendering

The Rendering module simplifies drawing ink strokes onto an Android[`Canvas`](https://developer.android.com/reference/kotlin/android/graphics/Canvas). It provides[`CanvasStrokeRenderer`](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/CanvasStrokeRenderer)for Compose and[`ViewStrokeRenderer`](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/view/ViewStrokeRenderer)for view-based layouts. These renderers optimize rendering performance and help deliver high-quality visuals, including antialiasing.

To render strokes, call the[`create()`](https://developer.android.com/reference/androidx/ink/rendering/android/canvas/CanvasStrokeRenderer#create(androidx.ink.brush.TextureBitmapStore))method to get a`CanvasStrokeRenderer`instance, and then call the[`draw()`](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/CanvasStrokeRenderer#draw(android.graphics.Canvas,androidx.ink.strokes.InProgressStroke,androidx.ink.geometry.AffineTransform))method to render either finished ([`Stroke`](https://developer.android.com/reference/kotlin/androidx/ink/strokes/Stroke)) or in-progress ([`InProgressStroke`](https://developer.android.com/reference/kotlin/androidx/ink/strokes/InProgressStroke)) strokes onto a`Canvas`.

You can transform the canvas when you draw a stroke. Examples include panning, zooming, and rotating. To render the stroke correctly, you must also pass the`canvas`transform to[`CanvasStrokeRenderer.draw`](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/CanvasStrokeRenderer#draw(android.graphics.Canvas,androidx.ink.strokes.InProgressStroke,androidx.ink.geometry.AffineTransform)).

To avoid tracking the`canvas`transform separately, use[`ViewStrokeRenderer`](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/view/ViewStrokeRenderer)instead.

## Storage

The[storage](https://developer.android.com/reference/kotlin/androidx/ink/storage/package-summary)module provides utilities for efficiently serializing and deserializing stroke data, primarily focusing on[`StrokeInputBatch`](https://developer.android.com/reference/kotlin/androidx/ink/strokes/StrokeInputBatch).

The module uses[protocol buffers](https://protobuf.dev/)and optimized delta compression techniques, resulting in significant storage savings compared to naive methods.

The storage module simplifies saving, loading, and sharing strokes.