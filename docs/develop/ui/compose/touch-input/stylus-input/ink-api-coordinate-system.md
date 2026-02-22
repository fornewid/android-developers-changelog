---
title: https://developer.android.com/develop/ui/compose/touch-input/stylus-input/ink-api-coordinate-system
url: https://developer.android.com/develop/ui/compose/touch-input/stylus-input/ink-api-coordinate-system
source: md.txt
---

Your choice of a coordinate system---in other words, your choice of what 1
*world unit* means---goes hand in hand with your choice of brush epsilon value.
The coordinate system is reflected in the inputToWorld transform matrix value
you pass to [`InProgressStrokesView.startStroke()`](https://developer.android.com/reference/kotlin/androidx/ink/authoring/InProgressStrokesView#startStroke(androidx.ink.strokes.StrokeInput,androidx.ink.brush.Brush,android.graphics.Matrix)) and the similar transform
you apply to the `Canvas` when drawing dry strokes.

A typical app can consider only world units and leave the
`strokeToWorldTransform` argument of `startStroke()` as the default identity
matrix.

If your app supports panning, zooming, or rotating a drawing surface, then the
exact value of those transform matrices will change over time, but those changes
reflect a change in how your world coordinate system is being
viewed by the *camera* that the user views the drawing surface through.

The world coordinate system can be envisioned as a grid with each cell being
the size of a world unit. Epsilon is a size in that grid, a floating point
number of world units.

As users zoom in on your content, they also zoom in on the world unit grid, so
the choice of world unit and epsilon size in terms of a default 100% zoom level
is important.

The world unit size definition and the epsilon value in world units
must be fixed values throughout the lifetime of your app.

The internal implementation uses epsilon to determine how close two points must
be to each other to be treated as the same point. In other words, any distance
less than epsilon is treated as zero distance. This is used to quantize and
round internal calculations.

## What are reasonable world unit sizes and epsilon values?

For portability across different screen sizes and [device densities](https://developer.android.com/training/multiscreen/screendensities), the world
unit size should be density independent. The classic unit for such scenarios is
density-independent pixels (dp). Typically choose 1 dp as your
world unit size.

When choosing a fixed epsilon value, avoid the internal implementation rounding
numbers to any distance that would be larger than a pixel. With a world unit
size of 1 dp, epsilon should be at most 1/4 (0.25 world units) to be the
size of a pixel on high display density devices where 1 dp can be
4 px. However, if you want
to support the user zooming in on their content by up to 10x and still keep
epsilon-related rounding to 1 px or less, then epsilon should be 0.25
divided by 10, which equals 0.025 world units.

This doesn't mean that you can't zoom in further than 10x, but you might start
seeing some imprecision and artifacts in the stroke rendering at that point.

Choosing an epsilon value is a balance between precise detail when zooming in
and computational resources such as:

- CPU cycles to calculate more precise geometry
- Memory to store more details in that geometry
- GPU time to render that geometry

These guidelines are reasonable defaults, but you can use them to choose
coordinate system and epsilon values that are more suited to your needs.

Deviating too far from these recommended values can adversely affect your
application. For example, increased resource consumption can make your
application run slowly. In some cases, floating-point precision issues can also
manifest as strange visual artifacts.