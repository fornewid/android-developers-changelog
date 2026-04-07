---
title: MotionLayout examples  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/animations/motionlayout/examples
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# MotionLayout examples Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to use animations in Compose.

[Animations in Compose →](https://developer.android.com/develop/ui/compose/animation/introduction)

![](/static/images/android-compose-ui-logo.png)

This document contains examples of how to use
[`MotionLayout`](/reference/androidx/constraintlayout/motion/widget/MotionLayout).
Each example includes a video demonstrating the motion, along with corresponding
code for the motion scene and layouts.

## Basic motion

This example contains a single view that you can touch and drag to move
horizontally.

* View the [layout XML](https://github.com/android/platform-samples/blob/main/samples/user-interface/constraintlayout/src/main/res/layout/motion_02_basic.xml).
* View the [`MotionScene` XML](https://github.com/android/platform-samples/blob/main/samples/user-interface/constraintlayout/src/main/res/xml/scene_02.xml).

[
](/static/images/training/constraint-layout/basic-horizontal-motion.mp4)


**Figure 1.** Dragging a view.

## Custom attribute - backgroundColor

This example is similar to the [Basic motion](#basic) example. In addition to
the basic motion, the background color of the view changes as the view moves.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_03_custom_attribute.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_03.xml).

[
](/static/images/training/constraint-layout/custom-attribute.mp4)


**Figure 2.** Dragging a view while its
background color changes.

## ImageFilterView - image transition

This example shows how to transition the saturation value of an
`ImageFilterView`.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_05_imagefilter.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_05.xml).

[
](/static/images/training/constraint-layout/imagefilterview2.mp4)


**Figure 3.** Dragging an image while its
saturation changes.

## Keyframe position

This example uses `<KeyFrameSet>` to alter the Y position of the view during
motion.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_06_keyframe.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_06.xml).

[
](/static/images/training/constraint-layout/keyframe1.mp4)


**Figure 4.** Dragging a view and altering its
Y position.

## Keyframe interpolation

This example builds on the [Keyframe position](#keyframe-position) example,
adding rotation and scaling to the view transition.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_07_keyframe.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_07.xml).

[
](/static/images/training/constraint-layout/keyframe2.mp4)


**Figure 5.** Dragging a view and altering its
Y position, rotation, and scale.

## Keyframe cycle

This example adds `<KeyCycle>` elements to add wavelike motion to the view.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_08_cycle.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_08.xml).

[
](/static/images/training/constraint-layout/keyframe3.mp4)


**Figure 6.** Dragging a view with a wavelike
motion while altering its color.

## CoordinatorLayout (1/2)

This example adds a `MotionLayout` to an existing `AppBarLayout` to add motion
to the app bar. This example is further described in
[Introduction to MotionLayout (part III)](https://medium.com/google-developers/introduction-to-motionlayout-part-iii-47cd64d51a5).

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_09_coordinatorlayout.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_09.xml).

[
](/static/images/training/constraint-layout/coordinatorlayout1.mp4)


**Figure 7.** Scrolling content while the app
bar expands.

## CoordinatorLayout (2/2)

This example adds a `MotionLayout` to an existing `AppBarLayout` to add motion
to the app bar.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_10_coordinatorlayout.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_10_header.xml).

[
](/static/images/training/constraint-layout/coordinatorlayout2.mp4)


**Figure 8.** Scrolling content while the app
bar expands and text animates in and out of the app bar.

## DrawerLayout (1/2)

This example shows how to add motion to a `DrawerLayout`. This example is
further described in
[Introduction to MotionLayout (part III)](https://medium.com/google-developers/introduction-to-motionlayout-part-iii-47cd64d51a5).

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_12_drawerlayout.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_12_content.xml).

[
](/static/images/training/constraint-layout/drawerlayout1.mp4)


**Figure 9.** Expanding `DrawerLayout`.

## DrawerLayout (2/2)

This example shows how to add motion to a `DrawerLayout`.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_13_drawerlayout.xml).
* View the [`MotionScene` XML for the main content](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_12_content.xml).
* View the [`MotionScene` XML for the menu](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_13_menu.xml).

[
](/static/images/training/constraint-layout/drawerlayout2.mp4)


**Figure 10.** Expanding `DrawerLayout` with
animated menu text.

## Side panel

This example shows how to display a side panel when dragging the main content
area to the right.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_14_side_panel.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_14.xml).

[
](/static/images/training/constraint-layout/sidepanel.mp4)


**Figure 11.** Showing a side panel by dragging
the main content.

## Parallax

This example demonstrates a parallax background, where different background
layers move at different speeds.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_15_parallax.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_15.xml).

[
](/static/images/training/constraint-layout/parallax.mp4)


**Figure 12.** Parallax effect in the header
image.

## ViewPager

This example shows how you can add motion when swiping between `ViewPager` tabs.
This example is further described in
[Introduction to MotionLayout (part III)](https://medium.com/google-developers/introduction-to-motionlayout-part-iii-47cd64d51a5).

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_16_viewpager.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_15.xml).

[
](/static/images/training/constraint-layout/viewpager.mp4)


**Figure 13.** Parallax effect in the header
image while swiping a `ViewPager`.

## ViewPager - Lottie

This example shows how you can add motion when swiping between `ViewPager` tabs.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_23_viewpager.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_23.xml).

[
](/static/images/training/constraint-layout/viewpager-lottie.mp4)


**Figure 14.** An image showing a Lottie effect
in the header image while swiping a `ViewPager`.

## Complex motion (1/3)

This example combines elements from previous examples to demonstrate complex
motion.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_17_coordination.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_17.xml).

[
](/static/images/training/constraint-layout/complex1.mp4)


**Figure 15.** Combining effects to create
complex motion.

## Complex motion (2/3)

This example combines elements from previous examples to demonstrate complex
motion.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_18_coordination.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_18.xml).

[
](/static/images/training/constraint-layout/complex2.mp4)


**Figure 16.** Combining effects to create
complex motion.

## Complex motion (3/3)

This example combines elements from previous examples to demonstrate complex
motion.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_19_coordination.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_19.xml).

[
](/static/images/training/constraint-layout/complex3.mp4)


**Figure 17.** Combining effects to create
complex motion.

## Fragment transition (1/2)

This example shows how you can use `MotionLayout` to transition between
fragments.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/main_activity.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/main_scene.xml).

[
](/static/images/training/constraint-layout/fragment-transition-1.mp4)


**Figure 18.** Fragment transition.

## Fragment transition (2/2)

This example shows how you can use `MotionLayout` to transition between
fragments.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/main_activity.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/main_scene.xml).

[
](/static/images/training/constraint-layout/fragment-transition-2.mp4)


**Figure 19.** Fragment transition.

## YouTube-like motion

This example demonstrates transitioning between a compact view and a full-screen
experience with additional content.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_24_youtube.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_24.xml).

[
](/static/images/training/constraint-layout/youtube-motion.mp4)


**Figure 20.** Fragments transition similar to
YouTube.

## KeyTrigger

This example demonstrates how to show and hide a floating action button when
the transition crosses a progress threshold.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_25_keytrigger.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_25.xml).

[
](/static/images/training/constraint-layout/keytrigger.mp4)


**Figure 21.** Show and hide a floating action
button.

## Multi-state

This example shows how to use state to determine which motion to apply.

* View the [layout XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/layout/motion_26_multistate.xml).
* View the [`MotionScene` XML](https://github.com/android/views-widgets-samples/blob/master/ConstraintLayoutExamples/motionlayout/src/main/res/xml/scene_26.xml).

[
](/static/images/training/constraint-layout/multistate.mp4)


**Figure 22.** Different motions based on state.