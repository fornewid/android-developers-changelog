---
title: https://developer.android.com/develop/ui/views/animations/reposition-view
url: https://developer.android.com/develop/ui/views/animations/reposition-view
source: md.txt
---

# Move a View with animation

<br />

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.  
[Animate position →](https://developer.android.com/develop/ui/compose/animation/quick-guide#animate-position)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Objects on screen often need to be repositioned due to user interaction or processing behind the scenes. Instead of immediately updating the object's position, which causes it to blink from one area to another, use an animation to move it from the starting position to its end position.

One way that Android lets you reposition your view objects on screen is by using[`ObjectAnimator`](https://developer.android.com/develop/ui/views/animations/reposition-view#UseObjectAnimator). You provide the end position you want the object to settle in as well as the duration of the animation. You can also use time interpolators to control the acceleration or deceleration of the animation.

## Change the view position with ObjectAnimator

The[`ObjectAnimator`](https://developer.android.com/reference/android/animation/ObjectAnimator)API provides a way to change the properties of a view with a specified duration. It contains static methods to create instances of`ObjectAnimator`depending on what type of attribute you are animating. When repositioning your views on screen, use the`translationX`and`translationY`attributes.

Here's an example of an`ObjectAnimator`that moves the view to a position 100 pixels from the left of the screen in 2 seconds:  

### Kotlin

```kotlin
ObjectAnimator.ofFloat(view, "translationX", 100f).apply {
    duration = 2000
    start()
}
```

### Java

```java
ObjectAnimator animation = ObjectAnimator.ofFloat(view, "translationX", 100f);
animation.setDuration(2000);
animation.start();
```

This example uses the[`ObjectAnimator.ofFloat()`](https://developer.android.com/reference/android/animation/ObjectAnimator#ofFloat(T,%20android.util.Property%3CT,%20java.lang.Float%3E,%20android.util.Property%3CT,%20java.lang.Float%3E,%20android.graphics.Path))method, because the translation values have to be floats. The first parameter is the view you want to animate. The second parameter is the property you are animating. Since the view needs to move horizontally, the`translationX`property is used. The last parameter is the end value of the animation. In this example, the value of 100 indicates a position that many pixels from the left of the screen.

The next method specifies how long the animation takes, in milliseconds. In this example, the animation runs for 2 seconds (2000 milliseconds).

The last method causes the animation to run, which updates the view's position on screen.

For more information about using`ObjectAnimator`, see[Animate using ObjectAnimator](https://developer.android.com/guide/topics/graphics/prop-animation#object-animator).

## Add curved motion

While using the`ObjectAnimator`is convenient, by default it repositions the view along a straight line between the starting and ending points. Material design relies on curves for spatial movement of objects on the screen and the timing of an animation. Using curved motion gives your app a more material feel while making your animations more interesting.

### Define your own path

The`ObjectAnimator`class has constructors that let you animate coordinates using two or more properties at once along with a path. For example, the following animator uses a[`Path`](https://developer.android.com/reference/android/graphics/Path)object to animate the X and Y properties of a view:  

### Kotlin

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    val path = Path().apply {
        arcTo(0f, 0f, 1000f, 1000f, 270f, -180f, true)
    }
    val animator = ObjectAnimator.ofFloat(view, View.X, View.Y, path).apply {
        duration = 2000
        start()
    }
} else {
    // Create animator without using curved path
}
```

### Java

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  Path path = new Path();
  path.arcTo(0f, 0f, 1000f, 1000f, 270f, -180f, true);
  ObjectAnimator animator = ObjectAnimator.ofFloat(view, View.X, View.Y, path);
  animator.setDuration(2000);
  animator.start();
} else {
  // Create animator without using curved path
}
```

Here is what the arc animation looks like:

**Figure 1.**A curved path animation.

An[`Interpolator`](https://developer.android.com/develop/ui/views/animations/prop-animation#interpolators)is an implementation of an easing curve. See the[Material Design documentation](https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration)for more information about the concept of easing curves. An`Interpolator`defines how specific values in an animation are calculated as a function of time. The system provides XML resources for the three basic curves in the Material Design specification:

- `@interpolator/fast_out_linear_in.xml`
- `@interpolator/fast_out_slow_in.xml`
- `@interpolator/linear_out_slow_in.xml`

### Use PathInterpolator

The[`PathInterpolator`](https://developer.android.com/reference/android/view/animation/PathInterpolator)class is an interpolator introduced in Android 5.0 (API 21). It is based on a[Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)or a`Path`object. The Android examples in the[Material Design documentation for easing](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs#433b1153-2ea3-4fe2-9748-803a47bc97ee)use`PathInterpolator`.

`PathInterpolator`has constructors based on different types of Bézier curves. All Bézier curves have start and end points fixed at`(0,0)`and`(1,1)`, respectively. The other constructor arguments depend on the type of Bézier curve being created.

For example, for a quadratic Bézier curve only the X and Y coordinates of one control point are needed:  

### Kotlin

```kotlin
val myInterpolator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    PathInterpolator(0.67f, 0.33f)
} else {
    LinearInterpolator()
}
```

### Java

```java
Interpolator myInterpolator = null;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  myInterpolator = new PathInterpolator(0.67f, 0.33f);
} else {
  myInterpolator = new LinearInterpolator();
}
```

This produces an easing curve that starts quickly and decelerates as it approaches the end.

The cubic Bézier constructor similarly has fixed start and end points, but it requires two control points:  

### Kotlin

```kotlin
val myInterpolator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    PathInterpolator(0.5f, 0.7f, 0.1f, 1.0f)
} else {
    LinearInterpolator()
}
```

### Java

```java
Interpolator myInterpolator = null;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  myInterpolator = new PathInterpolator(0.5f, 0.7f, 0.1f, 1.0f);
} else {
  myInterpolator = new LinearInterpolator();
}
```

This is an implementation of the Material Design[*emphasized decelerate*](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs#cbea5c6e-7b0d-47a0-98c3-767080a38d95)easing curve.

For greater control, an arbitrary`Path`can be used to define the curve:  

### Kotlin

```kotlin
val myInterpolator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  val path = Path().apply {
    moveTo(0.0f, 0.0f)
    cubicTo(0.5f, 0.7f, 0.1f, 1.0f, 1.0f, 1.0f)
  }
  PathInterpolator(path)
} else {
  LinearInterpolator()
}
```

### Java

```java
Interpolator myInterpolator = null;
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
  Path path = new Path();
  path.moveTo(0.0f, 0.0f);
  path.cubicTo(0.5f, 0.7f, 0.1f, 1.0f, 1.0f, 1.0f);
  myInterpolator = new PathInterpolator(path);
} else {
  myInterpolator = new LinearInterpolator();
}
```

This produces the same easing curve as the cubic Bézier example, but it uses a`Path`instead.

You can also define a path interpolator as an XML resource:  

    <pathInterpolator xmlns:android="http://schemas.android.com/apk/res/android"
        android:controlX1="0.5"
        android:controlY1="0.7"
        android:controlX2="0.1f"
        android:controlY2="1.0f"/>

Once you create a`PathInterpolator`object, you can pass it to the[`Animator.setInterpolator()`](https://developer.android.com/reference/android/animation/Animator#setInterpolator(android.animation.TimeInterpolator))method. The`Animator`uses the interpolator to determine the timing or path curve when it is started.  

### Kotlin

```kotlin
val animation = ObjectAnimator.ofFloat(view, "translationX", 100f).apply {
    interpolator = myInterpolator
    start()
}
```

### Java

```java
ObjectAnimator animation = ObjectAnimator.ofFloat(view, "translationX", 100f);
animation.setInterpolator(myInterpolator);
animation.start();
```