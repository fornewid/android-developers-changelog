---
title: https://developer.android.com/develop/ui/views/animations/overview
url: https://developer.android.com/develop/ui/views/animations/overview
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.  
[Animations in Compose →](https://developer.android.com/jetpack/compose/animation)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Animations can add visual cues that notify users about what's going on in your
app. They are especially useful when the UI changes state, such as when new
content loads or new actions become available. Animations also add a polished
look to your app, which gives it a higher quality look and feel.

Android includes different animation APIs depending on what type of animation
you want. This documentation provides an overview of the different ways you can
add motion to your UI.

To better understand when you should use animations, also see the [Material
Design guide about motion](https://www.google.com/url?sa=D&q=https://m3.material.io/styles/motion/overview).
| **Note:** For guidance on animations in Jetpack Compose, see [Animation](https://developer.android.com/jetpack/compose/animation).

## Animate bitmaps

**Figure 1.** An animated drawable.

To animate a bitmap graphic such as an icon or illustration, use the drawable
animation APIs. Usually, these animations are defined statically with a drawable
resource, but you can also define the animation behavior at runtime.

For example, a nice way to communicate to the user that two actions are related
is to animate a play button that transforms into a pause button when it's
tapped.

For more information, read [Animate drawable graphics](https://developer.android.com/guide/topics/graphics/drawable-animation).

## Animate UI visibility and motion

**Figure 2.** A subtle animation when a dialog appears
and disappears makes the UI change less jarring.

When you need to change the visibility or position of views in your layout, it's
best to include subtle animations to help the user understand how the UI is
changing.

To move, reveal, or hide views within the current layout, you can use the
property animation system provided by the [`android.animation`](https://developer.android.com/reference/android/animation/package-summary) package, available in Android 3.0
(API level 11) and higher. These APIs update the properties of your [`View`](https://developer.android.com/reference/android/view/View) objects over a period of time, continuously
redrawing the view as the properties change. For example, when you change the
position properties, the view moves across the screen. When you change the alpha
property, the view fades in or out.

For the simplest way to create these animations, enable animations on your
layout so that when you change the visibility of a view, an animation applies
automatically. For more information, see [Auto animate layout updates](https://developer.android.com/training/animation/layout).

To learn how to build animations using the property animation system, read the
[Property animation overview](https://developer.android.com/guide/topics/graphics/prop-animation). You
can also see the following pages to create common animations:

- [Change a view visibility with a crossfade](https://developer.android.com/training/animation/reveal-or-hide-view#Crossfade).

- [Change a view visibility with a circular reveal](https://developer.android.com/training/animation/reveal-or-hide-view#Reveal).

- [Swap views with a card flip](https://developer.android.com/training/animation/reveal-or-hide-view#Cardflip).

- [Change the view size with a zoom animation](https://developer.android.com/training/animation/zoom).

### Physics-based motion

**Figure 3.** Animation built with ObjectAnimator.  

**Figure 4.** Animation built with physics-based
APIs.

Whenever possible, apply real-world physics to your animations so that they are
natural-looking. For example, they should maintain momentum when their target
changes and make smooth transitions during any changes.

To provide these behaviors, the Android Support library includes physics-based
animation APIs that rely on the laws of physics to control how your animations
occur.

Two common physics-based animations are the following:

- [Spring animation](https://developer.android.com/develop/ui/views/animations/spring-animation).

- [Fling animation](https://developer.android.com/develop/ui/views/animations/fling-animation).

Animations not based on physics---such as those built with [`ObjectAnimator`](https://developer.android.com/reference/android/animation/ObjectAnimator) APIs---are fairly static and have a
fixed duration. If the target value changes, you must cancel the animation at
the time of target value change, re-configure the animation with a new value as
the new start value, and add the new target value. Visually, this process
creates an abrupt stop in the animation, and a disjointed movement afterwards,
as shown in figure 3.

Animations built by with physics-based animation APIs, such as
[`DynamicAnimation`](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation), are driven by
force. The change in the target value results in a change in force. The new
force applies on the existing velocity, which makes a continuous transition to
the new target. This process results in a more natural-looking animation, as
shown in figure 4.

## Animate layout changes


**Figure 5.** An animation to show more details can be achieved by
either changing the layout or starting a new activity.

On Android 4.4 (API level 19) and higher, you can use the transition framework
to create animations when you swap the layout within the current activity or
fragment. All you need to do is specify the starting and ending layout and what
type of animation you want to use. Then the system figures out and executes an
animation between the two layouts. You can use this to swap out the entire UI or
to move or replace just some views.

For example, when the user taps an item to see more information, you can replace
the layout with the item details, applying a transition like the one shown in
figure 5.

The starting and ending layout are each stored in a
[`Scene`](https://developer.android.com/reference/android/transition/Scene), though the starting scene is
usually determined automatically from the current layout. You create a
[`Transition`](https://developer.android.com/reference/android/transition/Transition) to tell the system what
type of animation you want, then call
[`TransitionManager.go()`](https://developer.android.com/reference/android/transition/TransitionManager#go(android.transition.Scene,%20android.transition.Transition))
and the system runs the animation to swap the layouts.

For more information, read [Animate layout changes using a transition](https://developer.android.com/develop/ui/views/animations/transitions). For sample code, check out
[BasicTransition](https://github.com/android/animation-samples/tree/main/BasicTransition)
.

## Animate between activities

On Android 5.0 (API level 21) and higher, you can also create animations that
transition between your activities. This is based on the same transition
framework described in the previous section, but it lets you create animations
between layouts in *separate activities*.

You can apply simple animations such as sliding the new activity in from the
side or fading it in, but you can also create animations that transition between
shared views in each activity. For example, when the user taps an item to see
more information, you can transition into a new activity with an animation that
seamlessly grows that item to fill the screen, like the animation shown in
figure 5.

As usual, you call
[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)),
but pass it a bundle of options provided by
[`ActivityOptions.makeSceneTransitionAnimation()`](https://developer.android.com/reference/android/app/ActivityOptions#makeSceneTransitionAnimation(android.app.Activity,%20android.view.View,%20java.lang.String)).
This bundle of options might include which views are shared between the
activities so the transition framework can connect them during the animation.

For additional resources, see:

- [Start an activity using an animation](https://developer.android.com/training/transitions/start-activity)
- [ActivitySceneTransitionBasic](https://github.com/android/animation/tree/main/ActivitySceneTransitionBasic)