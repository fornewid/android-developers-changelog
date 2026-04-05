---
title: https://developer.android.com/develop/ui/views/animations/spring-animation
url: https://developer.android.com/develop/ui/views/animations/spring-animation
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.  
[Spring AnimationSpec →](https://developer.android.com/jetpack/compose/animation/customize#spring)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

[Physics-based motion](https://developer.android.com/training/animation/overview#physics-based)is driven by force. Spring force is one such force that guides interactivity and motion. A spring force has the following properties: damping and stiffness. In a spring-based animation, the value and the velocity are calculated based on the spring force that are applied on each frame.

If you'd like your app's animations to slow down in only one direction, consider using a friction-based[fling animation](https://developer.android.com/guide/topics/graphics/fling-animation)instead.

## Lifecycle of a spring animation

In a spring-based animation, the[SpringForce](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce)class lets you customize spring's stiffness, its damping ratio, and its final position. As soon as the animation begins, the spring force updates the animation value and the velocity on each frame. The animation continues until the spring force reaches an equilibrium.

For example, if you drag an app icon around the screen and later release it by lifting your finger from the icon, the icon tugs back to its original place by an invisible but a familiar force.

Figure 1 demonstrates a similar spring effect. The plus sign (+) sign in the middle of the circle indicates the force applied through a touch gesture.
![Spring release](https://developer.android.com/static/images/guide/topics/graphics/spring-release.gif)**Figure 1.**Spring release effect

## Build a spring animation

The general steps for building a spring animation for your application are as follows:

- [**Add the support library**](https://developer.android.com/develop/ui/views/animations/spring-animation#adding-support-library)You must add the support library to your project to use the spring animation classes.
- [**Create a spring animation:**](https://developer.android.com/develop/ui/views/animations/spring-animation#creating-spring-animation)The primary step is to create an instance of the[SpringAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation)class and set the motion behavior parameters.
- [**(Optional) Register listeners:**](https://developer.android.com/develop/ui/views/animations/spring-animation#registering-listeners)Register listeners to watch for animation lifecycle changes and animation value updates.

  **Note:**Update listener should be registered only if you need per-frame update on the animation value changes. An update listener prevents the animation from potentially running on a separate thread.
- [**(Optional) Remove listeners:**](https://developer.android.com/develop/ui/views/animations/spring-animation#removing-listeners)Remove listeners that are no longer in use.
- [**(Optional) Set a start value:**](https://developer.android.com/develop/ui/views/animations/spring-animation#setting-start-value)Customize the animation start value.
- [**(Optional) Set a value range:**](https://developer.android.com/develop/ui/views/animations/spring-animation#setting-value-range)Set the animation value range to restrain values within the minimum and the maximum range.
- [**(Optional) Set start velocity:**](https://developer.android.com/develop/ui/views/animations/spring-animation#setting-velocity)Set the start velocity for the animation.
- [**(Optional) Set spring properties:**](https://developer.android.com/develop/ui/views/animations/spring-animation#setting-properties)Set the damping ratio and the stiffness on the spring.
- [**(Optional) Create a custom spring:**](https://developer.android.com/develop/ui/views/animations/spring-animation#using-custom-spring)Create a custom spring in case you do not intend to use the default spring or want to use a common spring throughout the animation.
- [**Start animation:**](https://developer.android.com/develop/ui/views/animations/spring-animation#starting-animation)Start the spring animation.
- [**(Optional) Cancel animation:**](https://developer.android.com/develop/ui/views/animations/spring-animation#cancelling-animation)Cancel the animation in case the user abruptly exits the app or the view becomes invisble.

The following sections discuss the general steps of building a spring animation in detail.

## Add the support library

To use the physics-based support library, you must add the support library to your project as follows:

1. Open the`build.gradle`file for your app module.
2. Add the support library to the`dependencies`section.

   ### Groovy

   ```groovy
           dependencies {
               def dynamicanimation_version = '1.0.0'
               implementation "androidx.dynamicanimation:dynamicanimation:$dynamicanimation_version"
           }
           
   ```

   ### Kotlin

   ```kotlin
           dependencies {
               val dynamicanimation_version = "1.0.0"
               implementation("androidx.dynamicanimation:dynamicanimation:$dynamicanimation_version")
           }
           
   ```

   To view the current versions for this library, see the information about Dynamicanimation on the[versions](https://developer.android.com/jetpack/androidx/versions)page.

### Create a spring animation

The[SpringAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation)class lets you create a spring animation for an object. To build a spring animation, you need to create an instance of the[SpringAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation)class and provide an object, an object's property that you want to animate, and an optional final spring position where you want the animation to rest.

**Note:** At the time of creating a spring animation, the final position of the spring is optional. Though, it*must*be defined before starting the animation.  

### Kotlin

```kotlin
val springAnim = findViewById<View>(R.id.imageView).let { img ->
    // Setting up a spring animation to animate the view's translationY property with the final
    // spring position at 0.
    SpringAnimation(img, DynamicAnimation.TRANSLATION_Y, 0f)
}
```

### Java

```java
final View img = findViewById(R.id.imageView);
// Setting up a spring animation to animate the view's translationY property with the final
// spring position at 0.
final SpringAnimation springAnim = new SpringAnimation(img, DynamicAnimation.TRANSLATION_Y, 0);
```

The spring-based animation can animate views on the screen by changing the actual properties in the view objects. The following views are available in the system:

- [ALPHA](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#ALPHA): Represents the alpha transparency on the view. The value is 1 (opaque) by default, with a value of 0 representing full transparency (not visible).
- [TRANSLATION_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_X),[TRANSLATION_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Y), and[TRANSLATION_Z](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Z): These properties control where the view is located as a delta from its left coordinate, top coordinate, and elevation, which are set by its layout container.
  - [TRANSLATION_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_X)describes the left coordinate.
  - [TRANSLATION_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Y)describes the top coordinate.
  - [TRANSLATION_Z](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Z)describes the depth of the view relative to its elevation.
- [ROTATION](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#ROTATION),[ROTATION_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#ROTATION_X), and[ROTATION_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#ROTATION_Y): These properties control the rotation in 2D (`rotation`property) and 3D around the pivot point.
- [SCROLL_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#SCROLL_X)and[SCROLL_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#SCROLL_Y): These properties indicate the scroll offset of the source left and the top edge in pixels. It also indicates the position in terms how much the page is scrolled.
- [SCALE_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#SCALE_X)and[SCALE_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#SCALE_Y): These properties control the 2D scaling of a view around its pivot point.
- [X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#X),[Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#Y), and[Z](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#Z): These are basic utility properties to describe the final location of the view in its container.
  - [X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#X)is a sum of the left value and[TRANSLATION_X](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_X).
  - [Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#Y)is a sum of the top value and[TRANSLATION_Y](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Y).
  - [Z](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#Z)is a sum of the elevation value and[TRANSLATION_Z](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#TRANSLATION_Z).

### Register listeners

The[DynamicAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation)class provides two listeners:[OnAnimationUpdateListener](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationUpdateListener)and[OnAnimationEndListener](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationEndListener). These listeners listen to the updates in animation such as when there is a change in the animation value and when the animation comes to an end.

#### OnAnimationUpdateListener

When you want to animate multiple views to create a chained animation, you can set up[OnAnimationUpdateListener](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationUpdateListener)to receive a callback every time there is a change in the current view's property. The callback notifies the other view to update its spring position based on the change incurred in the current view's property. To register the listener, perform the following steps:

1. Call the[addUpdateListener()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#addUpdateListener(android.support.animation.DynamicAnimation.OnAnimationUpdateListener))method and attach the listener to the animation.

   **Note:**You need to register the update listener before the animation begins. Though, update listener should be registered only if you need per-frame update on the animation value changes. An update listener prevents the animation from potentially running on a separate thread.
2. Override the[onAnimationUpdate()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationUpdateListener#onAnimationUpdate(android.support.animation.DynamicAnimation, float, float))method to notify the caller about the change in the current object. The following sample code illustrates the overall use of[OnAnimationUpdateListener](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationUpdateListener).

### Kotlin

```kotlin
// Setting up a spring animation to animate the view1 and view2 translationX and translationY properties
val (anim1X, anim1Y) = findViewById<View>(R.id.view1).let { view1 ->
    SpringAnimation(view1, DynamicAnimation.TRANSLATION_X) to
            SpringAnimation(view1, DynamicAnimation.TRANSLATION_Y)
}
val (anim2X, anim2Y) = findViewById<View>(R.id.view2).let { view2 ->
    SpringAnimation(view2, DynamicAnimation.TRANSLATION_X) to
            SpringAnimation(view2, DynamicAnimation.TRANSLATION_Y)
}

// Registering the update listener
anim1X.addUpdateListener { _, value, _ ->
    // Overriding the method to notify view2 about the change in the view1's property.
    anim2X.animateToFinalPosition(value)
}

anim1Y.addUpdateListener { _, value, _ -> anim2Y.animateToFinalPosition(value) }
```

### Java

```java
// Creating two views to demonstrate the registration of the update listener.
final View view1 = findViewById(R.id.view1);
final View view2 = findViewById(R.id.view2);

// Setting up a spring animation to animate the view1 and view2 translationX and translationY properties
final SpringAnimation anim1X = new SpringAnimation(view1,
        DynamicAnimation.TRANSLATION_X);
final SpringAnimation anim1Y = new SpringAnimation(view1,
    DynamicAnimation.TRANSLATION_Y);
final SpringAnimation anim2X = new SpringAnimation(view2,
        DynamicAnimation.TRANSLATION_X);
final SpringAnimation anim2Y = new SpringAnimation(view2,
        DynamicAnimation.TRANSLATION_Y);

// Registering the update listener
anim1X.addUpdateListener(new DynamicAnimation.OnAnimationUpdateListener() {

// Overriding the method to notify view2 about the change in the view1's property.
    @Override
    public void onAnimationUpdate(DynamicAnimation dynamicAnimation, float value,
                                  float velocity) {
        anim2X.animateToFinalPosition(value);
    }
});

anim1Y.addUpdateListener(new DynamicAnimation.OnAnimationUpdateListener() {

  @Override
    public void onAnimationUpdate(DynamicAnimation dynamicAnimation, float value,
                                  float velocity) {
        anim2Y.animateToFinalPosition(value);
    }
});
```

#### OnAnimationEndListener

[OnAnimationEndListener](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationEndListener)notifies the end of an animation. You can set up the listener to receive callback whenever the animation reaches equilibrium or it is canceled. To register the listener, perform the following steps:

1. Call the[addEndListener()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#addEndListener(android.support.animation.DynamicAnimation.OnAnimationEndListener))method and attach the listener to the animation.
2. Override the[onAnimationEnd()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.OnAnimationEndListener#onAnimationEnd(android.support.animation.DynamicAnimation, boolean, float, float))method to receive notification whenever an animation reaches equilibrium or is canceled.

### Remove listeners

To stop receiving animation update callbacks and animation end callbacks, call[removeUpdateListener()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#removeUpdateListener(android.support.animation.DynamicAnimation.OnAnimationUpdateListener))and[removeEndListener()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#removeEndListener(android.support.animation.DynamicAnimation.OnAnimationEndListener))methods, respectively.

### Set animation start value

To set the start value of the animation, call the[setStartValue()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#setStartValue(float))method and pass the start value of the animation. If you do not set the start value, the animation uses the current value of the object's property as the start value.

### Set animation value range

You can set the minimum and the maximum animation values when you want to restrain the property value to a certain range. It also helps to control the range in case you animate properties that have an intrinsic range, such as alpha (from 0 to 1).

- To set the minimum value, call the[setMinValue()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#setMinValue(float))method and pass the minimum value of the property.
- To set the maximum value, call the[setMaxValue()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#setMaxValue(float))method and pass the maximum value of the property.

Both methods return the animation for which the value is being set.

**Note:**If you have set the start value and have defined an animation value range, ensure the start value is within the minimum and the maximum value range.

### Set start velocity

Start velocity defines the speed at which the animation property changes at the beginning of the animation. The default start velocity is set to zero pixels per second. You can set the velocity either with the velocity of touch gestures or by using a fixed value as the start velocity. If you choose to provide a fixed value, we recommend to define the value in dp per second and then convert it to pixels per second. Defining the value in dp per second allows velocity to be independent of density and form factors. For more information about converting value to pixels per second, refer to the[Converting dp per second to pixels per second](https://developer.android.com/develop/ui/views/animations/spring-animation#converting-value)section.

To set the velocity, call the[setStartVelocity()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#setStartVelocity(float))method and pass the velocity in pixels per second. The method returns the spring force object on which the velocity is set.

**Note:** Use the[GestureDetector.OnGestureListener](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener)or the[VelocityTracker](https://developer.android.com/reference/android/view/VelocityTracker)class methods to retrieve and compute the velocity of touch gestures.  

### Kotlin

```kotlin
findViewById<View>(R.id.imageView).also { img ->
    SpringAnimation(img, DynamicAnimation.TRANSLATION_Y).apply {
        ...
        // Compute velocity in the unit pixel/second
        vt.computeCurrentVelocity(1000)
        val velocity = vt.yVelocity
        setStartVelocity(velocity)
    }
}
```

### Java

```java
final View img = findViewById(R.id.imageView);
final SpringAnimation anim = new SpringAnimation(img, DynamicAnimation.TRANSLATION_Y);
...
// Compute velocity in the unit pixel/second
vt.computeCurrentVelocity(1000);
float velocity = vt.getYVelocity();
anim.setStartVelocity(velocity);
```

#### Converting dp per second to pixels per second

Velocity of a spring must be in pixels per second. If you choose to provide a fixed value as the start of the velocity, provide the value in dp per second and then convert it to pixels per second. For conversion, use the[applyDimension()](https://developer.android.com/reference/android/util/TypedValue#applyDimension(int, float, android.util.DisplayMetrics))method from the[TypedValue](https://developer.android.com/reference/android/util/TypedValue)class. Refer to the following sample code:  

### Kotlin

```kotlin
val pixelPerSecond: Float =
    TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dpPerSecond, resources.displayMetrics)
```

### Java

```java
float pixelPerSecond = TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dpPerSecond, getResources().getDisplayMetrics());
```

### Set spring properties

The[SpringForce](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce)class defines the getter and the setter methods for each of the spring properties, such as damping ratio and stiffness. To set the spring properties, it is important to either retrieve the spring force object or create a custom spring force on which you can set the properties. For more information about creating a custom spring force, refer to the[Creating a custom spring force](https://developer.android.com/develop/ui/views/animations/spring-animation#creating-custom-spring)section.

**Tip:**While using the setter methods, you can create a method chain as all the setter methods return the spring force object.

#### Damping ratio

The damping ratio describes a gradual reduction in a spring oscillation. By using the damping ratio, you can define how rapidly the oscillations decay from one bounce to the next. There are four different ways you can damp a spring:

- Overdamping occurs when the damping ratio is greater than one. It lets the object gently return to the rest position.
- Critical damping occurs when the damping ratio is equal to one. It lets the object return to the rest position within the shortest amount of time.
- Underdamping occurs when the damping ratio is less than one. It lets object overshoot multiple times by passing the rest position, and then gradually reaches the rest position.
- Undamped occurs when the damping ratio is equal to zero. It lets the object oscillate forever.

To add the damping ratio to the spring, perform the following steps:

1. Call the[getSpring()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#getSpring())method to retrieve the spring to add the damping ratio.
2. Call the[setDampingRatio()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#setDampingRatio(float))method and pass the damping ratio that you want to add to the spring. The method returns the spring force object on which the damping ratio is set.

   **Note:** The damping ratio*must*be a non-negative number. If you set the damping ratio to zero, the spring will never reach the rest position. In other words, it oscillates forever.

The following damping ratio constants are available in the system:

- [DAMPING_RATIO_HIGH_BOUNCY](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#DAMPING_RATIO_HIGH_BOUNCY)
- [DAMPING_RATIO_MEDIUM_BOUNCY](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#DAMPING_RATIO_MEDIUM_BOUNCY)
- [DAMPING_RATIO_LOW_BOUNCY](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#DAMPING_RATIO_LOW_BOUNCY)
- [DAMPING_RATIO_NO_BOUNCY](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#DAMPING_RATIO_NO_BOUNCY)

![](https://developer.android.com/static/images/guide/topics/graphics/high_bounce.gif)Figure 2: High bounce

![](https://developer.android.com/static/images/guide/topics/graphics/medium_bounce.gif)Figure 3: Medium bounce

![](https://developer.android.com/static/images/guide/topics/graphics/low_bounce.gif)Figure 4: Low bounce

![](https://developer.android.com/static/images/guide/topics/graphics/no_bounce.gif)Figure 5: No bounce

<br />

The default damping ratio is set to[DAMPING_RATIO_MEDIUM_BOUNCY](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#DAMPING_RATIO_MEDIUM_BOUNCY).  

### Kotlin

```kotlin
findViewById<View>(R.id.imageView).also { img ->
    SpringAnimation(img, DynamicAnimation.TRANSLATION_Y).apply {
        ...
        // Setting the damping ratio to create a low bouncing effect.
        spring.dampingRatio = SpringForce.DAMPING_RATIO_LOW_BOUNCY
        ...
    }
}
```

### Java

```java
final View img = findViewById(R.id.imageView);
final SpringAnimation anim = new SpringAnimation(img, DynamicAnimation.TRANSLATION_Y);
...
// Setting the damping ratio to create a low bouncing effect.
anim.getSpring().setDampingRatio(SpringForce.DAMPING_RATIO_LOW_BOUNCY);
...
```

#### Stiffness

Stiffness defines the spring constant, which measures the strength of the spring. A stiff spring applies more force to the object that is attached when the spring is not at the rest position. To add the stiffness to the spring, perform the following steps:

1. Call the[getSpring()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#getSpring())method to retrieve the spring to add the stiffness.
2. Call the[setStiffness()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#setStiffness(float))method and pass the stiffness value that you want to add to the spring. The method returns the spring force object on which the stiffness is set.

   **Note:**The stiffness must be a positive number.

The following stiffness constants are available in the system:

- [STIFFNESS_HIGH](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#STIFFNESS_HIGH)
- [STIFFNESS_MEDIUM](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#STIFFNESS_MEDIUM)
- [STIFFNESS_LOW](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#STIFFNESS_LOW)
- [STIFFNESS_VERY_LOW](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#STIFFNESS_VERY_LOW)

![](https://developer.android.com/static/images/guide/topics/graphics/high_stiffness.gif)Figure 6: High stiffness

![](https://developer.android.com/static/images/guide/topics/graphics/medium_stiffness.gif)Figure 7: Medium stiffness

![](https://developer.android.com/static/images/guide/topics/graphics/low_stiffness.gif)Figure 8: Low stiffness

![](https://developer.android.com/static/images/guide/topics/graphics/very_low_stiffness.gif)Figure 9: Very low stiffness

<br />

The default stiffness is set to[STIFFNESS_MEDIUM](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#STIFFNESS_MEDIUM).  

### Kotlin

```kotlin
findViewById<View>(R.id.imageView).also { img ->
    SpringAnimation(img, DynamicAnimation.TRANSLATION_Y).apply {
        ...
        // Setting the spring with a low stiffness.
        spring.stiffness = SpringForce.STIFFNESS_LOW
        ...
    }
}
```

### Java

```java
final View img = findViewById(R.id.imageView);
final SpringAnimation anim = new SpringAnimation(img, DynamicAnimation.TRANSLATION_Y);
...
// Setting the spring with a low stiffness.
anim.getSpring().setStiffness(SpringForce.STIFFNESS_LOW);
...
```

### Create a custom spring force

You can create a custom spring force as an alternative to using the default spring force. The custom spring force lets you share the same spring force instance across multiple spring animations. Once you have created the spring force, you can set properties such as damping ratio and stiffness.

1. Create a[SpringForce](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce)object.

   `SpringForce force = new SpringForce();`
2. Assign the properties by calling the respective methods. You can also create a method chain.`force.setDampingRatio(DAMPING_RATIO_LOW_BOUNCY).setStiffness(STIFFNESS_LOW);`

3. Call the[setSpring()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#setSpring(android.support.animation.SpringForce))method to set the spring to the animation.

   `setSpring(force);`

### Start animation

There are two ways you can start a spring animation: By calling the[start()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#start())or by calling the[animateToFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#animateToFinalPosition(float))method. Both the methods need to be called on the main thread.

[animateToFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#animateToFinalPosition(float))method performs two tasks:

- Sets the final position of the spring.
- Starts the animation, if it has not started.

Since the method updates the final position of the spring and starts the animation if needed, you can call this method any time to change the course of an animation. For example, in a chained spring animation, the animation of one view depends on another view. For such an animation, it's more convenient to use the[animateToFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#animateToFinalPosition(float))method. By using this method in a chained spring animation, you don't need to worry if the animation you want to update next is currently running.

Figure 10 illustrates a chained spring animation, where the animation of one view depends on another view.
![Chained spring demo](https://developer.android.com/static/images/guide/topics/graphics/spring_chain.gif)**Figure 10.**Chained spring demo

To use the[animateToFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#animateToFinalPosition(float))method, call the[animateToFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#animateToFinalPosition(float))method and pass the rest position of the spring. You can also set the rest position of the spring by calling the[setFinalPosition()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringForce#setFinalPosition(float))method.

The[start()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#start())method does not set the property value to the start value immediately. The property value changes at each animation pulse, which happens before the draw pass. As a result, the changes are reflected in the next frame, as if the values are set immediately.  

### Kotlin

```kotlin
findViewById<View>(R.id.imageView).also { img ->
    SpringAnimation(img, DynamicAnimation.TRANSLATION_Y).apply {
        ...
        // Starting the animation
        start()
        ...
    }
}
```

### Java

```java
final View img = findViewById(R.id.imageView);
final SpringAnimation anim = new SpringAnimation(img, DynamicAnimation.TRANSLATION_Y);
...
// Starting the animation
anim.start();
...
```

### Cancel animation

You can cancel or skip to the end of the animation. An ideal situation where you need to cancel or skip to the end of the amiation is when a user interaction demands the animation to be terminated immediately. This is mostly when a user exits an app abruptly or the view becomes invisible.

There are two methods that you can use to terminate the animation. The[cancel()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#cancel())method terminates the animation at the value where it is. The[skipToEnd()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#skipToEnd())method skips the animation to the final value and then terminates it.

Before you can terminate the animation, it is important to first check the state of the spring. If the state is undamped, the animation can never reach the rest position. To check the state of the spring, call the[canSkipToEnd()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#canSkipToEnd())method. If the spring is damped, the method returns`true`, otherwise`false`.

Once you know the state of the spring, you can terminate an animation by using either[skipToEnd()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#skipToEnd())method or the[cancel()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#cancel())method. The[cancel()](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation#cancel())method*must*be called only on the main thread.

**Note:** In general, the[skipToEnd()](https://developer.android.com/reference/androidx/dynamicanimation/animation/SpringAnimation#skipToEnd())method causes a visual jump.