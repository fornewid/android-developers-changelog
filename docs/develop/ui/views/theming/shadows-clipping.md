---
title: Create shadows and clip views  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/theming/shadows-clipping
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create shadows and clip views Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with theming in Compose.

[Modifier.shadow() →](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).shadow(androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,kotlin.Boolean,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color))

![](/static/images/android-compose-ui-logo.png)

Material Design introduces elevation for UI elements. Elevation helps users
understand the relative importance of each element and focus their attention to
the current task.

**Note:** This page describes shadows obtained by elevation.
`Material3` introduces an elevation approach based on surface
color. For more information about maintanability and approaching the user
experience, see
[Material
Elevation](https://m3.material.io/styles/elevation/overview), and consider migrating your project to
[Jetpack Compose](/jetpack/compose/interop).

The elevation of a view, represented by the *Z* property, determines the
visual appearance of its shadow. Views with higher *Z* values cast larger,
softer shadows, and they occlude views with lower *Z* values. However, the
*Z* value of a view doesn't affect the view's size.

![An image showing how a view elevation produces a shadow.](/static/images/ui/material-design/cast-shadows_2x.png)


**Figure 1.** Elevation on the *Z*-axis and the resulting shadow.

Shadows are drawn by the parent of the elevated view. They are subject to
standard view clipping and are clipped by the parent by default.

Elevation is also useful to create animations where widgets temporarily rise
above the view plane when performing actions.

For more information, see
[Elevation in
Material Design](https://material.io/design/environment/elevation.html).

## Assign elevation to your views

The *Z* value for a view has two components:

* Elevation: the static component
* Translation: the dynamic component used for animations

`Z = elevation + translationZ`

The *Z* values are measured in dp (density-independent pixels).

![An image showing different shadows for different elevations in dp](/static/training/material/images/shadows-depth.png)


**Figure 2.** Different shadows for different elevations in dp.

To set the default (resting) elevation of a view, use the
`android:elevation` attribute in the XML layout. To set the elevation
of a view in the code of an activity, use the
`View.setElevation()`
method.

To set the translation of a view, use the
`View.setTranslationZ()`
method.

The
`ViewPropertyAnimator.z()`
and
`ViewPropertyAnimator.translationZ()`
methods let you animate the elevation of views. For more information, see the
API reference for
`ViewPropertyAnimator`
and the [property
animation](/guide/topics/graphics/prop-animation) developer guide.

You can also use a
`StateListAnimator`
to specify these animations in a declarative way. This is especially useful for
cases where state changes trigger animations, like when the user taps a button.
For more information, see
[Animate view
state changes using StateListAnimator](/develop/ui/views/animations/prop-animation#ViewState).

## Customize view shadows and outlines

The bounds of a view's background drawable determine the default shape of its
shadow. *Outlines* represent the outer shape of a graphics object and
define the ripple area for touch feedback.

Consider the following view, which is defined with a background drawable:

```
<TextView
    android:id="@+id/myview"
    ...
    android:elevation="2dp"
    android:background="@drawable/myrect" />
```

The background drawable is defined as a rectangle with rounded corners:

```
<!-- res/drawable/myrect.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
       android:shape="rectangle">
    <solid android:color="#42000000" />
    <corners android:radius="5dp" />
</shape>
```

The view casts a shadow with rounded corners, since the background drawable
defines the view's outline. Providing a custom outline overrides the default
shape of a view's shadow.

To define a custom outline for a view in your code, do the following:

1. Extend the
   `ViewOutlineProvider`
   class.
2. Override the
   `getOutline()`
   method.
3. Assign the new outline provider to your view with the
   `View.setOutlineProvider()`
   method.

You can create oval and rectangular outlines with rounded corners using the
methods in the
`Outline`
class. The default outline provider for views obtains the outline from the
view's background. To prevent a view from casting a shadow, set its
outline provider to `null`.

## Clip views

Clipping views lets you change the shape of a view. You can clip views for
consistency with other design elements or to change the shape of a view in
response to user input. You can clip a view to its outline area using the
`View.setClipToOutline()`
method. Only outlines that are rectangles, circles, and round rectangles support
clipping, as determined by the
`Outline.canClip()`
method.

To clip a view to the shape of a drawable, set the drawable as the
background of the view—as shown in the preceding example—and call
the `View.setClipToOutline()` method.

Clipping views is an expensive operation, so don't animate the shape you use
to clip a view. To achieve this effect, use the
[reveal
animation](/develop/ui/views/animations/reveal-or-hide-view#Reveal).