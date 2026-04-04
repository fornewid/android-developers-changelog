---
title: Create a custom transition animation  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/animations/transitions/custom-transitions
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Create a custom transition animation Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add animations in Compose.

[Add multiple properties with a transition in Compose →](https://developer.android.com/develop/ui/compose/animation/value-based#updateTransition)

![](/static/images/android-compose-ui-logo.png)

A custom transition lets you create an animation that is not available from any of
the built-in transition classes. For example, you can define a custom transition that turns
the foreground color of text and input fields to gray to indicate that the fields are disabled
in the new screen. This type of change helps users see the fields you disabled.

A custom transition, like one of the built-in transition types, applies animations to
child views of both the starting and ending scenes. However, unlike built-in transition types,
you have to provide the code that captures property values and generates animations.
You might also want to define a subset of target views for your animation.

This page teaches you how to capture property values and generate animations to create
custom transitions.

## Extend the Transition class

To create a custom transition, add a class to your project that extends the `Transition` class and override the functions shown in the following snippet:

### Kotlin

```
class CustomTransition : Transition() {

    override fun captureStartValues(transitionValues: TransitionValues) {}

    override fun captureEndValues(transitionValues: TransitionValues) {}

    override fun createAnimator(
        sceneRoot: ViewGroup,
        startValues: TransitionValues?,
        endValues: TransitionValues?
    ): Animator? {}

}
```

### Java

```
public class CustomTransition extends Transition {

    @Override
    public void captureStartValues(TransitionValues values) {}

    @Override
    public void captureEndValues(TransitionValues values) {}

    @Override
    public Animator createAnimator(ViewGroup sceneRoot,
                                   TransitionValues startValues,
                                   TransitionValues endValues) {}
}
```

The following sections explain how to override these functions.

## Capture view property values

Transition animations use the property animation system described in
[Property animation overview](/guide/topics/graphics/prop-animation). Property
animations change a view property from a starting value to an ending value over a specified
period of time, so the framework needs to have both the starting and ending values of
the property to construct the animation.

However, a property animation usually needs only a small subset of all the view's property
values. For example, a color animation needs color property values, while a movement
animation needs position property values. Since the property values needed for an animation
are specific to a transition, the transitions framework does not provide every property value
to a transition. Instead, the framework invokes callback functions that allow a transition to
capture only the property values it needs and store them in the framework.

### Capture starting values

To pass the starting view values to the framework, implement the
`captureStartValues(transitionValues)`
function. The framework calls this function for every view in the starting scene. The function
argument is a `TransitionValues` object that contains a reference
to the view and a `Map` instance in which you can store the view values you
want. In your implementation, retrieve these property values and pass them back to the
framework by storing them in the map.

To ensure that the key for a property value does not conflict with other
`TransitionValues` keys, use the following naming scheme:

```
package_name:transition_name:property_name
```

The following snippet shows an implementation of the `captureStartValues()` function:

### Kotlin

```
class CustomTransition : Transition() {

    // Define a key for storing a property value in
    // TransitionValues.values with the syntax
    // package_name:transition_class:property_name to avoid collisions
    private val PROPNAME_BACKGROUND = "com.example.android.customtransition:CustomTransition:background"

    override fun captureStartValues(transitionValues: TransitionValues) {
        // Call the convenience method captureValues
        captureValues(transitionValues)
    }

    // For the view in transitionValues.view, get the values you
    // want and put them in transitionValues.values
    private fun captureValues(transitionValues: TransitionValues) {
        // Get a reference to the view
        val view = transitionValues.view
        // Store its background property in the values map
        transitionValues.values[PROPNAME_BACKGROUND] = view.background
    }

    ...

}
```

### Java

```
public class CustomTransition extends Transition {

    // Define a key for storing a property value in
    // TransitionValues.values with the syntax
    // package_name:transition_class:property_name to avoid collisions
    private static final String PROPNAME_BACKGROUND =
            "com.example.android.customtransition:CustomTransition:background";

    @Override
    public void captureStartValues(TransitionValues transitionValues) {
        // Call the convenience method captureValues
        captureValues(transitionValues);
    }


    // For the view in transitionValues.view, get the values you
    // want and put them in transitionValues.values
    private void captureValues(TransitionValues transitionValues) {
        // Get a reference to the view
        View view = transitionValues.view;
        // Store its background property in the values map
        transitionValues.values.put(PROPNAME_BACKGROUND, view.getBackground());
    }
    ...
}
```

### Capture ending values

The framework calls the `captureEndValues(TransitionValues)` function
once for every target view in the ending scene. In all other respects, `captureEndValues()` works the same as `captureStartValues()`.

The following code snippet shows an implementation of the `captureEndValues()` function:

### Kotlin

```
override fun captureEndValues(transitionValues: TransitionValues) {
    captureValues(transitionValues)
}
```

### Java

```
@Override
public void captureEndValues(TransitionValues transitionValues) {
    captureValues(transitionValues);
}
```

In this example, both the `captureStartValues()` and `captureEndValues()`
functions invoke `captureValues()` to retrieve and store values. The view property
that `captureValues()` retrieves is the same, but it has different values in the
starting and ending scenes. The framework maintains separate maps for the starting and ending
states of a view.

## Create a custom animator

To animate the changes to a view between its state in the starting scene and its state in
the ending scene, provide an animator by overriding the
`createAnimator()`
function. When the framework calls this function, it passes in the scene root view and the
`TransitionValues` objects that contain the starting and ending values
you captured.

The number of times the framework calls the `createAnimator()` function depends on the
changes that occur between the starting and ending scenes.

For example, consider a fade-out or
fade-in animation implemented as a custom transition. If the starting scene has five targets, of
which two are removed from the ending scene, and the ending scene has the three targets from the
starting scene plus a new target, then the framework calls `createAnimator()` six times.
Three of the calls animate the fade-out and fade-in of the targets that stay in both scene
objects. Two more calls animate the fade-out of the targets removed from the ending scene. One
call animates the fade-in of the new target in the ending scene.

For target views that exist in both the starting and ending scenes, the framework provides
a `TransitionValues` object for both the `startValues` and
`endValues` arguments. For target views that only exist in the starting or the
ending scene, the framework provides a `TransitionValues` object
for the corresponding argument and `null` for the other.

To implement the `createAnimator(ViewGroup, TransitionValues, TransitionValues)` function when you create
a custom transition, use the view property values you captured to create an `Animator` object and return it to the framework. For an example implementation,
see the `ChangeColor` class in the [CustomTransition](https://github.com/android/animation-samples/tree/main/CustomTransition) sample. For more information about property animators, see
[Property animation](/guide/topics/graphics/prop-animation).

## Apply a custom transition

Custom transitions work the same as built-in transitions. You can apply a custom transition
using a transition manager, as described in [Apply a transition](/training/transitions/transitions#Apply).