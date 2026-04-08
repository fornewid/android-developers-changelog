---
title: Property Animation Overview  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/animations/prop-animation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Property Animation Overview Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.

[animate\*AsState →](https://developer.android.com/jetpack/compose/animation/value-based#animate-as-state)

![](/static/images/android-compose-ui-logo.png)

The property animation system is a robust framework that allows you
to animate almost anything. You can define an animation to change any object property over time,
regardless of whether it draws to the screen or not. A property animation changes a property's
(a field in an object) value over a specified length of time. To animate something, you specify the
object property that you want to animate, such as an object's position on the screen, how long
you want to animate it for, and what values you want to animate between.

The property animation system lets you define the following characteristics of an
animation:

* Duration: You can specify the duration of an animation. The default length is 300 ms.
* Time interpolation: You can specify how the values for the property are calculated as a
  function of the animation's current elapsed time.
* Repeat count and behavior: You can specify whether or not to have an animation repeat when
  it reaches the end of a duration and how many times to repeat the animation. You can also
  specify whether you want the animation to play back in reverse. Setting it to reverse plays
  the animation forwards then backwards repeatedly, until the number of repeats is reached.
* Animator sets: You can group animations into logical sets that play together or
  sequentially or after specified delays.
* Frame refresh delay: You can specify how often to refresh frames of your animation. The
  default is set to refresh every 10 ms, but the speed in which your application can refresh frames is
  ultimately dependent on how busy the system is overall and how fast the system can service the underlying timer.

To see a full example of property animation, see the
`ChangeColor` class in the [CustomTransition](https://github.com/android/animation-samples/tree/main/CustomTransition)
sample on GitHub.

## How property animation works

First, let's go over how an animation works with a simple example. Figure 1 depicts a
hypothetical object that is animated with its `x` property, which represents its
horizontal location on a screen. The duration of the animation is set to 40 ms and the distance
to travel is 40 pixels. Every 10 ms, which is the default frame refresh rate, the object moves
horizontally by 10 pixels. At the end of 40ms, the animation stops, and the object ends at
horizontal position 40. This is an example of an animation with linear interpolation, meaning the
object moves at a constant speed.

![](/static/images/animation/animation-linear.png)

**Figure 1.** Example of a linear animation

You can also specify animations to have a non-linear interpolation. Figure 2 illustrates a
hypothetical object that accelerates at the beginning of the animation, and decelerates at the
end of the animation. The object still moves 40 pixels in 40 ms, but non-linearly. In the
beginning, this animation accelerates up to the halfway point then decelerates from the
halfway point until the end of the animation. As Figure 2 shows, the distance traveled
at the beginning and end of the animation is less than in the middle.

![](/static/images/animation/animation-nonlinear.png)

**Figure 2.** Example of a non-linear animation

Let's take a detailed look at how the important components of the property animation system
would calculate animations like the ones illustrated above. Figure 3 depicts how the main classes
work with one another.

![](/static/images/animation/valueanimator.png)

**Figure 3.** How animations are calculated

The `ValueAnimator` object keeps track of your animation's timing,
such as how long the animation has been running, and the current value of the property that it is
animating.

The `ValueAnimator` encapsulates a `TimeInterpolator`, which defines animation interpolation, and a `TypeEvaluator`, which defines how to calculate values for the property being
animated. For example, in Figure 2, the `TimeInterpolator` used would be
`AccelerateDecelerateInterpolator` and the `TypeEvaluator` would be `IntEvaluator`.

To start an animation, create a `ValueAnimator` and give it the
starting and ending values for the property that you want to animate, along with the duration of
the animation. When you call `start()` the animation
begins. During the whole animation, the `ValueAnimator` calculates an *elapsed fraction*
between 0 and 1, based on the duration of the animation and how much time has elapsed. The
elapsed fraction represents the percentage of time that the animation has completed, 0 meaning 0%
and 1 meaning 100%. For example, in Figure 1, the elapsed fraction at t = 10 ms would be .25
because the total duration is t = 40 ms.

When the `ValueAnimator` is done calculating an elapsed fraction, it
calls the `TimeInterpolator` that is currently set, to calculate an
*interpolated fraction*. An interpolated fraction maps the elapsed fraction to a new
fraction that takes into account the time interpolation that is set. For example, in Figure 2,
because the animation slowly accelerates, the interpolated fraction, about .15, is less than the
elapsed fraction, .25, at t = 10 ms. In Figure 1, the interpolated fraction is always the same as
the elapsed fraction.

When the interpolated fraction is calculated, `ValueAnimator` calls
the appropriate `TypeEvaluator`, to calculate the value of the
property that you are animating, based on the interpolated fraction, the starting value, and the
ending value of the animation. For example, in Figure 2, the interpolated fraction was .15 at t =
10 ms, so the value for the property at that time would be .15 × (40 - 0), or 6.

## How property animation differs from view animation

The view animation system provides the capability to only animate `View`
objects, so if you wanted to animate non-`View` objects, you have to implement
your own code to do so. The view animation system is also constrained in the fact that it only
exposes a few aspects of a `View` object to animate, such as the scaling and
rotation of a View but not the background color, for instance.

Another disadvantage of the view animation system is that it only modified where the
View was drawn, and not the actual View itself. For instance, if you animated a button to move
across the screen, the button draws correctly, but the actual location where you can click the
button does not change, so you have to implement your own logic to handle this.

With the property animation system, these constraints are completely removed, and you can animate
any property of any object (Views and non-Views) and the object itself is actually modified.
The property animation system is also more robust in the way it carries out animation. At
a high level, you assign animators to the properties that you want to animate, such as color,
position, or size and can define aspects of the animation such as interpolation and
synchronization of multiple animators.

The view animation system, however, takes less time to setup and requires less code to write.
If view animation accomplishes everything that you need to do, or if your existing code already
works the way you want, there is no need to use the property animation system. It also might
make sense to use both animation systems for different situations if the use case arises.

## API overview

You can find most of the property animation system's APIs in `android.animation`. Because the view animation system already
defines many interpolators in `android.view.animation`, you can use
those interpolators in the property animation system as well. The following tables describe the main
components of the property animation system.

The `Animator` class provides the basic structure for creating
animations. You normally do not use this class directly as it only provides minimal
functionality that must be extended to fully support animating values. The following
subclasses extend `Animator`:

**Table 1.** Animators

| Class | Description |
| --- | --- |
| `ValueAnimator` | The main timing engine for property animation that also computes the values for the property to be animated. It has all of the core functionality that calculates animation values and contains the timing details of each animation, information about whether an animation repeats, listeners that receive update events, and the ability to set custom types to evaluate. There are two pieces to animating properties: calculating the animated values and setting those values on the object and property that is being animated. `ValueAnimator` does not carry out the second piece, so you must listen for updates to values calculated by the `ValueAnimator` and modify the objects that you want to animate with your own logic. See the section about [Animating with ValueAnimator](#value-animator) for more information. |
| `ObjectAnimator` | A subclass of `ValueAnimator` that allows you to set a target object and object property to animate. This class updates the property accordingly when it computes a new value for the animation. You want to use `ObjectAnimator` most of the time, because it makes the process of animating values on target objects much easier. However, you sometimes want to use `ValueAnimator` directly because `ObjectAnimator` has a few more restrictions, such as requiring specific accessor methods to be present on the target object. |
| `AnimatorSet` | Provides a mechanism to group animations together so that they run in relation to one another. You can set animations to play together, sequentially, or after a specified delay. See the section about [Choreographing multiple animations with Animator Sets](#choreography) for more information. |

Evaluators tell the property animation system how to calculate values for a given
property. They take the timing data that is provided by an `Animator`
class, the animation's start and end value, and calculate the animated values of the property
based on this data. The property animation system provides the following evaluators:

**Table 2.** Evaluators

| Class/Interface | Description |
| --- | --- |
| `IntEvaluator` | The default evaluator to calculate values for `int` properties. |
| `FloatEvaluator` | The default evaluator to calculate values for `float` properties. |
| `ArgbEvaluator` | The default evaluator to calculate values for color properties that are represented as hexadecimal values. |
| `TypeEvaluator` | An interface that allows you to create your own evaluator. If you are animating an object property that is *not* an `int`, `float`, or color, you must implement the `TypeEvaluator` interface to specify how to compute the object property's animated values. You can also specify a custom `TypeEvaluator` for `int`, `float`, and color values as well, if you want to process those types differently than the default behavior. See the section about [Using a TypeEvaluator](#type-evaluator) for more information on how to write a custom evaluator. |

A time interpolator defines how specific values in an animation are calculated as a
function of time. For example, you can specify animations to happen linearly across the whole
animation, meaning the animation moves evenly the entire time, or you can specify animations
to use non-linear time, for example, accelerating at the beginning and decelerating at the
end of the animation. Table 3 describes the interpolators that are contained in `android.view.animation`. If none of the provided interpolators suits
your needs, implement the `TimeInterpolator` interface and create your own. See [Using interpolators](#interpolators) for more information on how to write a custom
interpolator.

**Table 3.** Interpolators

| Class/Interface | Description |
| --- | --- |
| `AccelerateDecelerateInterpolator` | An interpolator whose rate of change starts and ends slowly but accelerates through the middle. |
| `AccelerateInterpolator` | An interpolator whose rate of change starts out slowly and then accelerates. |
| `AnticipateInterpolator` | An interpolator whose change starts backward then flings forward. |
| `AnticipateOvershootInterpolator` | An interpolator whose change starts backward, flings forward and overshoots the target value, then finally goes back to the final value. |
| `BounceInterpolator` | An interpolator whose change bounces at the end. |
| `CycleInterpolator` | An interpolator whose animation repeats for a specified number of cycles. |
| `DecelerateInterpolator` | An interpolator whose rate of change starts out quickly and then decelerates. |
| `LinearInterpolator` | An interpolator whose rate of change is constant. |
| `OvershootInterpolator` | An interpolator whose change flings forward and overshoots the last value then comes back. |
| `TimeInterpolator` | An interface that allows you to implement your own interpolator. |

## Animate using ValueAnimator

The `ValueAnimator` class lets you animate values of some type for the
duration of an animation by specifying a set of `int`, `float`, or color
values to animate through. You obtain a `ValueAnimator` by calling one of
its factory methods: `ofInt()`, `ofFloat()`, or `ofObject()`. For example:

### Kotlin

```
ValueAnimator.ofFloat(0f, 100f).apply {
    duration = 1000
    start()
}
```

### Java

```
ValueAnimator animation = ValueAnimator.ofFloat(0f, 100f);
animation.setDuration(1000);
animation.start();
```

In this code, the `ValueAnimator` starts calculating the values of the
animation, between 0 and 100, for a duration of 1000 ms, when the `start()` method runs.

You can also specify a custom type to animate by doing the following:

### Kotlin

```
ValueAnimator.ofObject(MyTypeEvaluator(), startPropertyValue, endPropertyValue).apply {
    duration = 1000
    start()
}
```

### Java

```
ValueAnimator animation = ValueAnimator.ofObject(new MyTypeEvaluator(), startPropertyValue, endPropertyValue);
animation.setDuration(1000);
animation.start();
```

In this code, the `ValueAnimator` starts calculating the values of the
animation, between `startPropertyValue` and `endPropertyValue` using the
logic supplied by `MyTypeEvaluator` for a duration of 1000 ms, when the `start()` method runs.

You can use the values of the animation by adding an
`AnimatorUpdateListener`
to the `ValueAnimator` object, as shown in the
following code:

### Kotlin

```
ValueAnimator.ofObject(...).apply {
    ...
    addUpdateListener { updatedAnimation ->
        // You can use the animated value in a property that uses the
        // same type as the animation. In this case, you can use the
        // float value in the translationX property.
        textView.translationX = updatedAnimation.animatedValue as Float
    }
    ...
}
```

### Java

```
animation.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
    @Override
    public void onAnimationUpdate(ValueAnimator updatedAnimation) {
        // You can use the animated value in a property that uses the
        // same type as the animation. In this case, you can use the
        // float value in the translationX property.
        float animatedValue = (float)updatedAnimation.getAnimatedValue();
        textView.setTranslationX(animatedValue);
    }
});
```

In the `onAnimationUpdate()`
method you can access the updated animation value and use it in a property of
one of your views. For more information on listeners, see the section about
[Animation listeners](#listeners).

## Animate using ObjectAnimator

The `ObjectAnimator` is a subclass of the `ValueAnimator` (discussed in the previous section) and combines the timing
engine and value computation of `ValueAnimator` with the ability to
animate a named property of a target object. This makes animating any object much easier, as you
no longer need to implement the `ValueAnimator.AnimatorUpdateListener`,
because the animated property updates automatically.

Instantiating an `ObjectAnimator` is similar to a `ValueAnimator`, but you also specify the object and the name of that object's property (as
a String) along with the values to animate between:

### Kotlin

```
ObjectAnimator.ofFloat(textView, "translationX", 100f).apply {
    duration = 1000
    start()
}
```

### Java

```
ObjectAnimator animation = ObjectAnimator.ofFloat(textView, "translationX", 100f);
animation.setDuration(1000);
animation.start();
```

To have the `ObjectAnimator` update properties
correctly, you must do the following:

* The object property that you are animating must have a setter function (in camel case) in the form of
  `set<PropertyName>()`. Because the `ObjectAnimator`
  automatically updates the property during animation, it must be able to access the property
  with this setter method. For example, if the property name is `foo`, you need to
  have a `setFoo()` method. If this setter method does not exist, you have three
  options:
  + Add the setter method to the class if you have the rights to do so.
  + Use a wrapper class that you have rights to change and have that wrapper receive the
    value with a valid setter method and forward it to the original object.
  + Use `ValueAnimator` instead.
* If you specify only one value for the `values...` parameter in one of the `ObjectAnimator` factory methods, it is assumed to be the ending value of the
  animation. Therefore, the object property that you are animating must have a getter function
  that is used to obtain the starting value of the animation. The getter function must be in the
  form of `get<PropertyName>()`. For example, if the property name is
  `foo`, you need to have a `getFoo()` method.
* The getter (if needed) and setter methods of the property that you are animating must
  operate on the same type as the starting and ending values that you specify to `ObjectAnimator`. For example, you must have
  `targetObject.setPropName(float)` and `targetObject.getPropName()`
  if you construct the following `ObjectAnimator`:

  ```
  ObjectAnimator.ofFloat(targetObject, "propName", 1f)
  ```
* Depending on what property or object you are animating, you might need to call the `invalidate()` method on a View to force the screen to redraw itself with the
  updated animated values. You do this in the
  `onAnimationUpdate()`
  callback. For example, animating the color property of a Drawable object only causes updates to the
  screen when that object redraws itself. All of the property setters on View, such as
  `setAlpha()` and `setTranslationX()`
  invalidate the View properly, so you do not need to invalidate the View when calling these
  methods with new values. For more information on listeners, see the section about
  [Animation listeners](#listeners).

## Choreograph multiple animations using an AnimatorSet

In many cases, you want to play an animation that depends on when another animation starts or
finishes. The Android system lets you bundle animations together into an `AnimatorSet`, so that you can specify whether to start animations
simultaneously, sequentially, or after a specified delay. You can also nest `AnimatorSet` objects within each other.

The following code snippet plays the following `Animator`
objects in the following manner:

1. Plays `bounceAnim`.
2. Plays `squashAnim1`, `squashAnim2`, `stretchAnim1`, and
   `stretchAnim2` at the same time.
3. Plays `bounceBackAnim`.
4. Plays `fadeAnim`.

### Kotlin

```
val bouncer = AnimatorSet().apply {
    play(bounceAnim).before(squashAnim1)
    play(squashAnim1).with(squashAnim2)
    play(squashAnim1).with(stretchAnim1)
    play(squashAnim1).with(stretchAnim2)
    play(bounceBackAnim).after(stretchAnim2)
}
val fadeAnim = ObjectAnimator.ofFloat(newBall, "alpha", 1f, 0f).apply {
    duration = 250
}
AnimatorSet().apply {
    play(bouncer).before(fadeAnim)
    start()
}
```

### Java

```
AnimatorSet bouncer = new AnimatorSet();
bouncer.play(bounceAnim).before(squashAnim1);
bouncer.play(squashAnim1).with(squashAnim2);
bouncer.play(squashAnim1).with(stretchAnim1);
bouncer.play(squashAnim1).with(stretchAnim2);
bouncer.play(bounceBackAnim).after(stretchAnim2);
ValueAnimator fadeAnim = ObjectAnimator.ofFloat(newBall, "alpha", 1f, 0f);
fadeAnim.setDuration(250);
AnimatorSet animatorSet = new AnimatorSet();
animatorSet.play(bouncer).before(fadeAnim);
animatorSet.start();
```

## Animation listeners

You can listen for important events during an animation's duration with the listeners described below.

* `Animator.AnimatorListener`
  + `onAnimationStart()`
    - Called when the animation starts.
  + `onAnimationEnd()` -
    Called when the animation ends.
  + `onAnimationRepeat()` - Called when the animation repeats itself.
  + `onAnimationCancel()` - Called when the animation is canceled. A cancelled animation
    also calls `onAnimationEnd()`,
    regardless of how they were ended.
* `ValueAnimator.AnimatorUpdateListener`
  + `onAnimationUpdate()` - called on every frame of the animation. Listen to this event to
    use the calculated values generated by `ValueAnimator` during an
    animation. To use the value, query the `ValueAnimator` object
    passed into the event to get the current animated value with the `getAnimatedValue()` method. Implementing this
    listener is required if you use `ValueAnimator`.

    Depending on what property or object you are animating, you might need to call
    `invalidate()` on a View to force that area of the
    screen to redraw itself with the new animated values. For example, animating the
    color property of a Drawable object only cause updates to the screen when that object
    redraws itself. All of the property setters on View,
    such as `setAlpha()` and
    `setTranslationX()` invalidate the View
    properly, so you do not need to invalidate the View when calling these methods with new values.

You can extend the `AnimatorListenerAdapter` class instead of
implementing the `Animator.AnimatorListener` interface, if you do not
want to implement all of the methods of the `Animator.AnimatorListener`
interface. The `AnimatorListenerAdapter` class provides empty
implementations of the methods that you can choose to override.

For example, the following code snippet creates an `AnimatorListenerAdapter`
for just the `onAnimationEnd()`
callback:

### Kotlin

```
ObjectAnimator.ofFloat(newBall, "alpha", 1f, 0f).apply {
    duration = 250
    addListener(object : AnimatorListenerAdapter() {
        override fun onAnimationEnd(animation: Animator) {
            balls.remove((animation as ObjectAnimator).target)
        }
    })
}
```

### Java

```
ValueAnimator fadeAnim = ObjectAnimator.ofFloat(newBall, "alpha", 1f, 0f);
fadeAnim.setDuration(250);
fadeAnim.addListener(new AnimatorListenerAdapter() {
public void onAnimationEnd(Animator animation) {
    balls.remove(((ObjectAnimator)animation).getTarget());
}
```

## Animate layout changes to ViewGroup objects

The property animation system provides the capability to animate changes to ViewGroup objects
as well as provide an easy way to animate View objects themselves.

You can animate layout changes within a ViewGroup with the
`LayoutTransition` class. Views inside a ViewGroup can
go through an appearing and disappearing animation when you add them to or
remove them from a ViewGroup or when you call a View's
`setVisibility()` method with
`VISIBLE`, `INVISIBLE`, or
`GONE`. The remaining Views in the ViewGroup can also
animate into their new positions when you add or remove Views. You can define
the following animations in a `LayoutTransition` object
by calling `setAnimator()`
and passing in an `Animator` object with one of the
following `LayoutTransition` constants:

* `APPEARING` - A flag indicating the animation that runs on items that are
  appearing in the container.
* `CHANGE_APPEARING` - A flag indicating the animation that runs on items that are
  changing due to a new item appearing in the container.
* `DISAPPEARING` - A flag indicating the animation that runs on items that are
  disappearing from the container.
* `CHANGE_DISAPPEARING` - A flag indicating the animation that runs on items that
  are changing due to an item disappearing from the container.

You can define your own custom animations for these four types of events to customize the look
of your layout transitions or just tell the animation system to use the default animations.

To set the `android:animateLayoutchanges` attribute to `true` for the
ViewGroup do the following:

```
<LinearLayout
    android:orientation="vertical"
    android:layout_width="wrap_content"
    android:layout_height="match_parent"
    android:id="@+id/verticalContainer"
    android:animateLayoutChanges="true" />
```

Setting this attribute to true automatically animates Views that are added or removed from the
ViewGroup as well as the remaining Views in the ViewGroup.

## Animate view state changes using StateListAnimator

The `StateListAnimator` class lets you define animators that run when
the state of a view changes. This object behaves as a wrapper for an
`Animator` object, calling that animation whenever the specified
view state (such as "pressed" or "focused") changes.

The `StateListAnimator` can be defined in an XML resource with a root
`<selector>` element and child `<item>` elements that each specify
a different view state defined by the `StateListAnimator` class. Each
`<item>` contains the definition for a [property animation set](/guide/topics/resources/animation-resource#Property).

For example, the following file creates a state list animator that changes the x and y scale
of the view when it's pressed:

res/xml/animate\_scale.xml

```
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- the pressed state; increase x and y size to 150% -->
    <item android:state_pressed="true">
        <set>
            <objectAnimator android:propertyName="scaleX"
                android:duration="@android:integer/config_shortAnimTime"
                android:valueTo="1.5"
                android:valueType="floatType"/>
            <objectAnimator android:propertyName="scaleY"
                android:duration="@android:integer/config_shortAnimTime"
                android:valueTo="1.5"
                android:valueType="floatType"/>
        </set>
    </item>
    <!-- the default, non-pressed state; set x and y size to 100% -->
    <item android:state_pressed="false">
        <set>
            <objectAnimator android:propertyName="scaleX"
                android:duration="@android:integer/config_shortAnimTime"
                android:valueTo="1"
                android:valueType="floatType"/>
            <objectAnimator android:propertyName="scaleY"
                android:duration="@android:integer/config_shortAnimTime"
                android:valueTo="1"
                android:valueType="floatType"/>
        </set>
    </item>
</selector>
```

To attach the state list animator to a view, add the [`android:stateListAnimator`](/reference/android/view/View#attr_android:stateListAnimator) attribute as follows:

```
<Button android:stateListAnimator="@xml/animate_scale"
        ... />
```

Now the animations defined in `animate_scale.xml` are used when this button's
state changes.

Or to instead assign a state list animator to a view in your code, use the
`AnimatorInflater.loadStateListAnimator()` method, and assign the animator to
your view with the `View.setStateListAnimator()` method.

Or instead of animating properties of the view, you can play a drawable animation between
state changes, using `AnimatedStateListDrawable`.
Some of the system widgets in
Android 5.0 use these animations by default. The following example shows how
to define an `AnimatedStateListDrawable` as an XML resource:

```
<!-- res/drawable/myanimstatedrawable.xml -->
<animated-selector
    xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- provide a different drawable for each state-->
    <item android:id="@+id/pressed" android:drawable="@drawable/drawableP"
        android:state_pressed="true"/>
    <item android:id="@+id/focused" android:drawable="@drawable/drawableF"
        android:state_focused="true"/>
    <item android:id="@id/default"
        android:drawable="@drawable/drawableD"/>

    <!-- specify a transition -->
    <transition android:fromId="@+id/default" android:toId="@+id/pressed">
        <animation-list>
            <item android:duration="15" android:drawable="@drawable/dt1"/>
            <item android:duration="15" android:drawable="@drawable/dt2"/>
            ...
        </animation-list>
    </transition>
    ...
</animated-selector>
```

## Use a TypeEvaluator

If you want to animate a type that is unknown to the Android system, you can create your own
evaluator by implementing the `TypeEvaluator` interface. The types that
are known by the Android system are `int`, `float`, or a color, which are
supported by the `IntEvaluator`, `FloatEvaluator`, and `ArgbEvaluator` type
evaluators.

There is only one method to implement in the `TypeEvaluator`
interface, the `evaluate()` method. This allows
the animator that you are using to return an appropriate value for your animated property at the
current point of the animation. The `FloatEvaluator` class demonstrates
how to do this:

### Kotlin

```
private class FloatEvaluator : TypeEvaluator<Any> {

    override fun evaluate(fraction: Float, startValue: Any, endValue: Any): Any {
        return (startValue as Number).toFloat().let { startFloat ->
            startFloat + fraction * ((endValue as Number).toFloat() - startFloat)
        }
    }

}
```

### Java

```
public class FloatEvaluator implements TypeEvaluator {

    public Object evaluate(float fraction, Object startValue, Object endValue) {
        float startFloat = ((Number) startValue).floatValue();
        return startFloat + fraction * (((Number) endValue).floatValue() - startFloat);
    }
}
```

**Note:** When `ValueAnimator` (or `ObjectAnimator`) runs, it calculates a current elapsed fraction of the
animation (a value between 0 and 1) and then calculates an interpolated version of that depending
on what interpolator that you are using. The interpolated fraction is what your `TypeEvaluator` receives through the `fraction` parameter, so you do
not have to take into account the interpolator when calculating animated values.

## Use Interpolators

An interpolator define how specific values in an animation are calculated as a function of
time. For example, you can specify animations to happen linearly across the whole animation,
meaning the animation moves evenly the entire time, or you can specify animations to use
non-linear time, for example, using acceleration or deceleration at the beginning or end of the
animation.

Interpolators in the animation system receive a fraction from Animators that represent the
elapsed time of the animation. Interpolators modify this fraction to coincide with the type of
animation that it aims to provide. The Android system provides a set of common interpolators in
the `android.view.animation package`. If none of these suit your
needs, you can implement the `TimeInterpolator` interface and create your
own.

As an example, how the default interpolator `AccelerateDecelerateInterpolator` and the `LinearInterpolator` calculate interpolated fractions are compared below.
The `LinearInterpolator` has no effect on the elapsed fraction. The `AccelerateDecelerateInterpolator` accelerates into the animation and
decelerates out of it. The following methods define the logic for these interpolators:

**AccelerateDecelerateInterpolator**

### Kotlin

```
override fun getInterpolation(input: Float): Float =
        (Math.cos((input + 1) * Math.PI) / 2.0f).toFloat() + 0.5f
```

### Java

```
@Override
public float getInterpolation(float input) {
    return (float)(Math.cos((input + 1) * Math.PI) / 2.0f) + 0.5f;
}
```

**LinearInterpolator**

### Kotlin

```
override fun getInterpolation(input: Float): Float = input
```

### Java

```
@Override
public float getInterpolation(float input) {
    return input;
}
```

The following table represents the approximate values that are calculated by these
interpolators for an animation that lasts 1000ms:

| ms elapsed | Elapsed fraction/Interpolated fraction (Linear) | Interpolated fraction (Accelerate/Decelerate) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 200 | .2 | .1 |
| 400 | .4 | .345 |
| 600 | .6 | .654 |
| 800 | .8 | .9 |
| 1000 | 1 | 1 |

As the table shows, the `LinearInterpolator` changes the values
at the same speed, .2 for every 200ms that passes. The `AccelerateDecelerateInterpolator` changes the values faster than `LinearInterpolator` between 200ms and 600ms and slower between 600ms and
1000ms.

## Specify keyframes

A `Keyframe` object consists of a time/value pair that lets you define
a specific state at a specific time of an animation. Each keyframe can also have its own
interpolator to control the behavior of the animation in the interval between the previous
keyframe's time and the time of this keyframe.

To instantiate a `Keyframe` object, you must use one of the factory
methods, `ofInt()`, `ofFloat()`, or `ofObject()` to obtain the appropriate type of `Keyframe`. You then call
the `ofKeyframe()` factory method to
obtain a `PropertyValuesHolder` object. Once you have the object, you can
obtain an animator by passing in the `PropertyValuesHolder` object and
the object to animate. The following code snippet demonstrates how to do this:

### Kotlin

```
val kf0 = Keyframe.ofFloat(0f, 0f)
val kf1 = Keyframe.ofFloat(.5f, 360f)
val kf2 = Keyframe.ofFloat(1f, 0f)
val pvhRotation = PropertyValuesHolder.ofKeyframe("rotation", kf0, kf1, kf2)
ObjectAnimator.ofPropertyValuesHolder(target, pvhRotation).apply {
    duration = 5000
}
```

### Java

```
Keyframe kf0 = Keyframe.ofFloat(0f, 0f);
Keyframe kf1 = Keyframe.ofFloat(.5f, 360f);
Keyframe kf2 = Keyframe.ofFloat(1f, 0f);
PropertyValuesHolder pvhRotation = PropertyValuesHolder.ofKeyframe("rotation", kf0, kf1, kf2);
ObjectAnimator rotationAnim = ObjectAnimator.ofPropertyValuesHolder(target, pvhRotation);
rotationAnim.setDuration(5000);
```

## Animate views

The property animation system allow streamlined animation of View objects and offers
a few advantages over the view animation system. The view
animation system transformed View objects by changing the way that they were drawn. This was
handled in the container of each View, because the View itself had no properties to manipulate.
This resulted in the View being animated, but caused no change in the View object itself. This
led to behavior such as an object still existing in its original location, even though it was
drawn on a different location on the screen. In Android 3.0, new properties and the corresponding
getter and setter methods were added to eliminate this drawback.

The property animation system
can animate Views on the screen by changing the actual properties in the View objects. In
addition, Views also automatically call the `invalidate()`
method to refresh the screen whenever its properties are changed. The new properties in the `View` class that facilitate property animations are:

* `translationX` and `translationY`: These properties control where the
  View is located as a delta from its left and top coordinates which are set by its layout
  container.
* `rotation`, `rotationX`, and `rotationY`: These properties
  control the rotation in 2D (`rotation` property) and 3D around the pivot point.
* `scaleX` and `scaleY`: These properties control the 2D scaling of a
  View around its pivot point.
* `pivotX` and `pivotY`: These properties control the location of the
  pivot point, around which the rotation and scaling transforms occur. By default, the pivot
  point is located at the center of the object.
* `x` and `y`: These are simple utility properties to describe the
  final location of the View in its container, as a sum of the left and top values and
  translationX and translationY values.
* `alpha`: Represents the alpha transparency on the View. This value is 1 (opaque)
  by default, with a value of 0 representing full transparency (not visible).

To animate a property of a View object, such as its color or rotation value, all you need to
do is create a property animator and specify the View property that you want to
animate. For example:

### Kotlin

```
ObjectAnimator.ofFloat(myView, "rotation", 0f, 360f)
```

### Java

```
ObjectAnimator.ofFloat(myView, "rotation", 0f, 360f);
```

For more information on creating animators, see the sections on animating with
[ValueAnimator](#value-animator) and [ObjectAnimator](#object-animator).

### Animate using ViewPropertyAnimator

The `ViewPropertyAnimator` provides a simple way to animate several
properties of a `View` in parallel, using a single underlying `Animator`
object. It behaves much like an `ObjectAnimator`, because it modifies the
actual values of the view's properties, but is more efficient when animating many properties at
once. In addition, the code for using the `ViewPropertyAnimator` is much
more concise and easier to read. The following code snippets show the differences in using multiple
`ObjectAnimator` objects, a single
`ObjectAnimator`, and the `ViewPropertyAnimator` when
simultaneously animating the `x` and `y` property of a view.

**Multiple ObjectAnimator objects**

### Kotlin

```
val animX = ObjectAnimator.ofFloat(myView, "x", 50f)
val animY = ObjectAnimator.ofFloat(myView, "y", 100f)
AnimatorSet().apply {
    playTogether(animX, animY)
    start()
}
```

### Java

```
ObjectAnimator animX = ObjectAnimator.ofFloat(myView, "x", 50f);
ObjectAnimator animY = ObjectAnimator.ofFloat(myView, "y", 100f);
AnimatorSet animSetXY = new AnimatorSet();
animSetXY.playTogether(animX, animY);
animSetXY.start();
```

**One ObjectAnimator**

### Kotlin

```
val pvhX = PropertyValuesHolder.ofFloat("x", 50f)
val pvhY = PropertyValuesHolder.ofFloat("y", 100f)
ObjectAnimator.ofPropertyValuesHolder(myView, pvhX, pvhY).start()
```

### Java

```
PropertyValuesHolder pvhX = PropertyValuesHolder.ofFloat("x", 50f);
PropertyValuesHolder pvhY = PropertyValuesHolder.ofFloat("y", 100f);
ObjectAnimator.ofPropertyValuesHolder(myView, pvhX, pvhY).start();
```

**ViewPropertyAnimator**

### Kotlin

```
myView.animate().x(50f).y(100f)
```

### Java

```
myView.animate().x(50f).y(100f);
```

For more detailed information about `ViewPropertyAnimator`, see the corresponding Android Developers
[blog
post](http://android-developers.blogspot.com/2011/05/introducing-viewpropertyanimator.html).

## Declare animations in XML

The property animation system lets you declare property animations with XML instead of doing
it programmatically. By defining your animations in XML, you can easily reuse your animations
in multiple activities and more easily edit the animation sequence.

To distinguish animation files that use the new property animation APIs from those that use the
legacy [view animation](/guide/topics/graphics/view-animation) framework,
starting with Android 3.1, you should save the XML files for property animations in the `res/animator/` directory.

The following property animation classes have XML declaration support with the
following XML tags:

* `ValueAnimator` - `<animator>`
* `ObjectAnimator` - `<objectAnimator>`
* `AnimatorSet` - `<set>`

To find the attributes that you can use in your XML declaration, see [Animation
resources](/guide/topics/resources/animation-resource#Property). The following example plays the two sets of object animations
sequentially, with the first nested set playing two object animations together:

```
<set android:ordering="sequentially">
    <set>
        <objectAnimator
            android:propertyName="x"
            android:duration="500"
            android:valueTo="400"
            android:valueType="intType"/>
        <objectAnimator
            android:propertyName="y"
            android:duration="500"
            android:valueTo="300"
            android:valueType="intType"/>
    </set>
    <objectAnimator
        android:propertyName="alpha"
        android:duration="500"
        android:valueTo="1f"/>
</set>
```

In order to run this animation, you must inflate the XML resources in your code to an `AnimatorSet` object, and then set the target objects for all of the animations
before starting the animation set. Calling `setTarget()` sets a single target object for all children of the `AnimatorSet` as a convenience. The following code shows how to do this:

### Kotlin

```
(AnimatorInflater.loadAnimator(myContext, R.animator.property_animator) as AnimatorSet).apply {
    setTarget(myObject)
    start()
}
```

### Java

```
AnimatorSet set = (AnimatorSet) AnimatorInflater.loadAnimator(myContext,
    R.animator.property_animator);
set.setTarget(myObject);
set.start();
```

You can also declare a `ValueAnimator` in XML, as
shown in the following example:

```
<animator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:valueType="floatType"
    android:valueFrom="0f"
    android:valueTo="-100f" />
```

To use the previous `ValueAnimator` in your code, you
must inflate the object, add an
`AnimatorUpdateListener`,
get the updated animation value, and use it in a property of one of your views,
as shown in the following code:

### Kotlin

```
(AnimatorInflater.loadAnimator(this, R.animator.animator) as ValueAnimator).apply {
    addUpdateListener { updatedAnimation ->
        textView.translationX = updatedAnimation.animatedValue as Float
    }

    start()
}
```

### Java

```
ValueAnimator xmlAnimator = (ValueAnimator) AnimatorInflater.loadAnimator(this,
        R.animator.animator);
xmlAnimator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() {
    @Override
    public void onAnimationUpdate(ValueAnimator updatedAnimation) {
        float animatedValue = (float)updatedAnimation.getAnimatedValue();
        textView.setTranslationX(animatedValue);
    }
});

xmlAnimator.start();
```

For information about the XML syntax for defining property animations, see [Animation
resources](/guide/topics/resources/animation-resource#Property) .

## Potential effects on UI performance

Animators that update the UI cause extra rendering work for every frame in
which the animation runs. For this reason, using resource intensive animations
can negatively impact the performance of your app.

Work required to animate your UI is added to the [animation stage](/topic/performance/rendering/profile-gpu#at) of
the rendering pipeline. You can find out if your animations impact the
performance of your app by enabling **Profile GPU Rendering** and
monitoring the animation stage. For more information, see  [Profile GPU rendering
walkthrough](/studio/profile/dev-options-rendering).