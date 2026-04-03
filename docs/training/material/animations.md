---
title: Defining Custom Animations  |  Android Developers
url: https://developer.android.com/training/material/animations
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Defining Custom Animations Stay organized with collections Save and categorize content based on your preferences.



**This page is deprecated.** See below for the new location for
documentation that used to be here.

## Customize Touch Feedback

Touch feedback in material design provides an instantaneous visual confirmation at the
point of contact when users interact with UI elements. The default touch feedback animations
for buttons use the new `RippleDrawable` class, which transitions
between different states with a ripple effect.

In most cases, you should apply this functionality in your view XML by specifying the view
background as:

* `?android:attr/selectableItemBackground` for a bounded ripple.
* `?android:attr/selectableItemBackgroundBorderless` for a ripple that extends beyond
  the view. It will be drawn upon, and bounded by, the nearest parent of the view with a non-null
  background.

**Note:** `selectableItemBackgroundBorderless` is a new
attribute introduced in API level 21.

Alternatively, you can define a `RippleDrawable`
as an XML resource using the `ripple` element.

You can assign a color to `RippleDrawable` objects. To change
the default touch feedback color, use the theme's `android:colorControlHighlight`
attribute.

For more information, see the API reference for the `RippleDrawable` class.

## Use the Reveal Effect

See [Create a circular reveal animation](/training/animation/reveal-or-hide-view#Reveal).

## Customize Activity Transitions

See [Start an Activity with an Animation](/training/transitions/start-activity).

## Use Curved Motion

See [Use curved motion](/training/animation/reposition-view#CurvedMotion).

## Animate View State Changes

See [Using StateListAnimator to
animate view state changes](/guide/topics/graphics/prop-animation#ViewState).

## Animate Vector Drawables

See [Animate Drawable Graphics](/guide/topics/graphics/drawable-animation).