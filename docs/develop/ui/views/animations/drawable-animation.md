---
title: https://developer.android.com/develop/ui/views/animations/drawable-animation
url: https://developer.android.com/develop/ui/views/animations/drawable-animation
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose. [Animate vector drawables →](https://developer.android.com/develop/ui/compose/animation/vectors) ![](https://developer.android.com/static/images/android-compose-ui-logo.png) ![](https://developer.android.com/static/training/animation/videos/drawable-animation.gif) **Figure 1.** An animated drawable.


In some situations, images need to be animated. This is useful if you want to display
a custom loading animation composed of several images or if you want an icon to morph after a user's
action. Android provides two options for animating drawables.


The first option is to use an [`AnimationDrawable`](https://developer.android.com/develop/ui/views/animations/drawable-animation#AnimationDrawable). This
lets you specify several static
[drawable files](https://developer.android.com/guide/topics/graphics/2d-graphics) that display one at a time to
create an animation. The second option is to use an
[`AnimatedVectorDrawable`](https://developer.android.com/develop/ui/views/animations/drawable-animation#AnimVector), which lets you animate the properties
of a [vector drawable](https://developer.android.com/guide/topics/graphics/vector-drawable-resources).

## Use AnimationDrawable


One way to create an animation is to load a sequence of drawable resources, like a roll of film.
The [`AnimationDrawable` class](https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable)
is the basis for these kinds of drawable animations.

You can define the frames of an animation in your code by using the `AnimationDrawable`
class API, but it's easier to define them with a single XML file that lists the frames that
make up the animation. The XML file for this kind of animation belongs in the `res/drawable/`
directory of your Android project. In this case, the instructions give the order and duration for
each frame in the animation.

The XML file consists of an `<animation-list>` element as the root node and a
series of child `<item>` nodes that each define a frame---a drawable resource
and its duration. Here's an example XML file for a `Drawable` animation:

```xml
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="true">
    <item android:drawable="@drawable/rocket_thrust1" android:duration="200" />
    <item android:drawable="@drawable/rocket_thrust2" android:duration="200" />
    <item android:drawable="@drawable/rocket_thrust3" android:duration="200" />
</animation-list>
```

This animation runs for three frames. Setting the `android:oneshot`
attribute of the list to `true` makes it cycle once and then stop and hold
on the last frame. If you set `android:oneshot` to `false`,
the animation loops.

If you save this XML as `rocket_thrust.xml` in the `res/drawable/`
directory of the project, you can add it as the background image to a `View` and then
call `start()` to make it play. Here's an example of an activity in which the animation is added to an
`https://developer.android.com/reference/android/widget/ImageView` and then animated
when the screen is touched:

### Kotlin

```kotlin
private lateinit var rocketAnimation: AnimationDrawable

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main)

    val rocketImage = findViewById<ImageView>(R.id.rocket_image).apply {
        setBackgroundResource(R.drawable.rocket_thrust)
        rocketAnimation = background as AnimationDrawable
    }

    rocketImage.setOnClickListener({ rocketAnimation.start() })
}
```

### Java

```java
AnimationDrawable rocketAnimation;

public void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.main);

  ImageView rocketImage = (ImageView) findViewById(R.id.rocket_image);
  rocketImage.setBackgroundResource(R.drawable.rocket_thrust);
  rocketAnimation = (AnimationDrawable) rocketImage.getBackground();

  rocketImage.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View view) {
        rocketAnimation.start();
      }
  });
}
```


It's important to note that the `start()` method called on the
`AnimationDrawable` can't be called during the `onCreate()` method of your
`Activity`, because the `AnimationDrawable` is not yet fully attached to the
window. To play the animation immediately, without requiring interaction, you can call it from the
`` `https://developer.android.com/reference/android/app/Activity#onStart()` ``
method in your `Activity`, which is called when Android makes the view visible on screen.


For more information on the XML syntax and available tags and attributes, see [Animation resources](https://developer.android.com/guide/topics/resources/animation-resource).

## Use AnimatedVectorDrawable

A [vector drawable](https://developer.android.com/guide/topics/graphics/vector-drawable-resources)
is a type of drawable that is scalable without getting pixelated or blurry. The
[`AnimatedVectorDrawable`
class](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable)---and [`AnimatedVectorDrawableCompat`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/AnimatedVectorDrawableCompat) for backward compatibility---lets you animate the
properties of a vector drawable, such as rotating it or changing the path data to morph it into a
different image.


You normally define animated vector drawables in three XML files:

- A vector drawable with the `<vector>` element in `res/drawable/`.
- An animated vector drawable with the `<animated-vector>` element in `res/drawable/`.
- One or more object animators with the `<objectAnimator>` element in `res/animator/`.


Animated vector drawables can animate the attributes of the `<group>` and
`<path>` elements. The `<group>` element defines a set of
paths or subgroups, and the `<path>` element defines paths to be drawn.


When you define a vector drawable that you want to animate, use the `android:name`
attribute to assign a unique name to groups and paths, so you can refer to them from your animator
definitions. For example:

res/drawable/vectordrawable.xml

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:height="64dp"
    android:width="64dp"
    android:viewportHeight="600"
    android:viewportWidth="600">
    <group
        android:name="rotationGroup"
        android:pivotX="300.0"
        android:pivotY="300.0"
        android:rotation="45.0" >
        <path
            android:name="v"
            android:fillColor="#000000"
            android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z" />
    </group>
</vector>
```


The animated vector drawable definition refers to the groups and paths in the vector drawable
by their names:

res/drawable/animatorvectordrawable.xml

```xml
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
  android:drawable="@drawable/vectordrawable" >
    <target
        android:name="rotationGroup"
        android:animation="@animator/rotation" />
    <target
        android:name="v"
        android:animation="@animator/path_morph" />
</animated-vector>
```


The animation definitions represent
`https://developer.android.com/reference/android/animation/ObjectAnimator` or
`https://developer.android.com/reference/android/animation/AnimatorSet` objects. The
first animator in this example rotates the target group 360 degrees:

res/animator/rotation.xml

```xml
<set xmlns:android="http://schemas.android.com/apk/res/android">
  <objectAnimator
      android:duration="6000"
      android:propertyName="rotation"
      android:valueFrom="0"
      android:valueTo="360" />
</set>
```


The second animator in this example morphs the vector drawable's path from one shape to
another. The paths must be compatible for morphing: they must have the same number of commands
and the same number of parameters for each command.

res/animator/path_morph.xml

```xml
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <objectAnimator
        android:duration="3000"
        android:propertyName="pathData"
        android:valueFrom="M300,70 l 0,-70 70,70 0,0   -70,70z"
        android:valueTo="M300,70 l 0,-70 70,0  0,140 -70,0 z"
        android:valueType="pathType" />
</set>
```


Here is the resulting `AnimatedVectorDrawable`:
**Figure 2.** An `AnimatedVectorDrawable`.

### Animated Vector Drawable (AVD) preview


The Animated Vector Drawable tool in Android Studio lets you preview animated
drawable resources. This tool helps you preview `<animation-list>`,
`<animated-vector>`, and `<animated-selector>` resources in
Android Studio and makes it easier to refine your custom animations.
![User previewing and playing an animation inside Android Studio](https://developer.android.com/static/studio/images/releases/avd-preview.gif) **Figure 3.** The Animated Vector Drawable tool in Android Studio.

<br />


For more information, see the API reference for
`https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable`.