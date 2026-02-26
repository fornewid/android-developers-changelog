---
title: https://developer.android.com/develop/ui/views/animations/motionlayout
url: https://developer.android.com/develop/ui/views/animations/motionlayout
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use animations in Compose. [Animations in Compose →](https://developer.android.com/develop/ui/compose/animation/introduction) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

[Video](https://www.youtube.com/watch?v=M1jE3W3_NTQ)

[`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout)
is a layout type that helps you manage motion and widget animation in your app.
`MotionLayout` is a subclass of
[`ConstraintLayout`](https://developer.android.com/training/constraint-layout) and builds on its rich
layout capabilities. As part of the `ConstraintLayout` library, `MotionLayout`
is available as a support library.

`MotionLayout` bridges the gap between layout transitions and complex motion
handling, offering a mix of features between the [property animation
framework](https://developer.android.com/guide/topics/graphics/prop-animation),
[`TransitionManager`](https://developer.android.com/training/transitions), and
[`CoordinatorLayout`](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout).
**Figure 1.** Basic touch-controlled motion.

In addition to describing transitions between layouts, `MotionLayout` lets you
animate any layout properties. Moreover, it inherently supports *seekable
transitions* . This means you can instantly show any point within the transition
based on some condition, such as touch input. `MotionLayout` also supports
keyframes, enabling fully customized transitions to suit your needs.

`MotionLayout` is fully declarative, meaning you can describe any transitions in
XML, no matter how complex.

> [!NOTE]
> **Note:** `MotionLayout` works only with its direct children. It doesn't support nested layout hierarchies or activity transitions.

## Design considerations

`MotionLayout` is intended to move, resize, and animate UI elements with which
users interact, such as buttons and title bars. Don't use motion in your app as
a gratuitous special effect. Use it to help users understand what your app is
doing. For more information about designing your app with motion, see the
Material Design section [Understanding
motion](https://material.io/design/motion).

## Get started

Follow these steps to start using `MotionLayout` in your project.

1. **Add the `ConstraintLayout` dependency:** to use
   `MotionLayout` in your project, add the
   `ConstraintLayout` 2.0 dependency to your app's
   `build.gradle` file. If you're using AndroidX, add the
   following dependency:

   ### Groovy

   ```groovy
   dependencies {
       implementation "androidx.constraintlayout:constraintlayout:2.2.1"
       // To use constraintlayout in compose
       implementation "androidx.constraintlayout:constraintlayout-compose:1.1.1"
   }
   ```

   ### Kotlin

   ```kotlin
   dependencies {
       implementation("androidx.constraintlayout:constraintlayout:2.2.1")
       // To use constraintlayout in compose
       implementation("androidx.constraintlayout:constraintlayout-compose:1.1.1")
   }
   ```
2. **Create a `MotionLayout` file:** `MotionLayout`
   is a subclass of `ConstraintLayout`, so you can transform any
   existing `ConstraintLayout` into a `MotionLayout` by
   replacing the class name in your layout resource file, as shown in the
   following examples:

   ### AndroidX

   ```xml
   <!-- before: ConstraintLayout -->
   <androidx.constraintlayout.widget.ConstraintLayout .../>
   <!-- after: MotionLayout -->
   <androidx.constraintlayout.motion.widget.MotionLayout .../>
             
   ```

   ### Support library

   ```xml
   <!-- before: ConstraintLayout -->
   <android.support.constraint.ConstraintLayout .../>
   <!-- after: MotionLayout -->
   <android.support.constraint.motion.MotionLayout .../>
             
   ```

   Here's a full example of a `MotionLayout` file, which
   defines the layout shown in figure 1:

   ### AndroidX

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <!-- activity_main.xml -->
   <androidx.constraintlayout.motion.widget.MotionLayout
       xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:app="http://schemas.android.com/apk/res-auto"
       xmlns:tools="http://schemas.android.com/tools"
       android:id="@+id/motionLayout"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
       app:layoutDescription="@xml/scene_01"
       tools:showPaths="true">

       <View
           android:id="@+id/button"
           android:layout_width="64dp"
           android:layout_height="64dp"
           android:background="@color/colorAccent"
           android:text="Button" />

   </androidx.constraintlayout.motion.widget.MotionLayout>
           
   ```

   ### Support library

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <!-- activity_main.xml -->
   <android.support.constraint.motion.MotionLayout
       xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:app="http://schemas.android.com/apk/res-auto"
       xmlns:tools="http://schemas.android.com/tools"
       android:id="@+id/motionLayout"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
       app:layoutDescription="@xml/scene_01"
       tools:showPaths="true">

       <View
           android:id="@+id/button"
           android:layout_width="64dp"
           android:layout_height="64dp"
           android:background="@color/colorAccent"
           android:text="Button" />

   </android.support.constraint.motion.MotionLayout>
           
   ```
3. **Create a MotionScene:** in the previous `MotionLayout`
   example, the `app:layoutDescription` attribute references a
   *motion scene* . A motion scene is an XML resource file. Within its
   [`<MotionScene>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene)
   root element, a motion scene contains all the motion descriptions for the
   corresponding layout. To keep layout information separate from motion
   descriptions, each `MotionLayout` references a separate motion
   scene. The definitions in the motion scene take precedence over any similar
   definitions in the `MotionLayout`.

   Here's an example motion scene file that describes the basic horizontal
   motion in figure 1:

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <MotionScene xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:motion="http://schemas.android.com/apk/res-auto">

       <Transition
           motion:constraintSetStart="@+id/start"
           motion:constraintSetEnd="@+id/end"
           motion:duration="1000">
           <OnSwipe
               motion:touchAnchorId="@+id/button"
               motion:touchAnchorSide="right"
               motion:dragDirection="dragRight" />
       </Transition>

       <ConstraintSet android:id="@+id/start">
           <Constraint
               android:id="@+id/button"
               android:layout_width="64dp"
               android:layout_height="64dp"
               android:layout_marginStart="8dp"
               motion:layout_constraintBottom_toBottomOf="parent"
               motion:layout_constraintStart_toStartOf="parent"
               motion:layout_constraintTop_toTopOf="parent" />
       </ConstraintSet>

       <ConstraintSet android:id="@+id/end">
           <Constraint
               android:id="@+id/button"
               android:layout_width="64dp"
               android:layout_height="64dp"
               android:layout_marginEnd="8dp"
               motion:layout_constraintBottom_toBottomOf="parent"
               motion:layout_constraintEnd_toEndOf="parent"
               motion:layout_constraintTop_toTopOf="parent" />
       </ConstraintSet>

   </MotionScene>
       
   ```

   Note the following:
   - [`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)
     contains the base definition of the motion.

     - `motion:constraintSetStart` and
       `motion:constraintSetEnd` are references to the
       endpoints of the motion. These endpoints are defined in the
       `<ConstraintSet>` elements later in the motion scene.

     - `motion:duration` specifies the number of milliseconds
       it takes for the motion to complete.

   - [`<OnSwipe>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe)
     lets you create touch control for the motion.

     - `motion:touchAnchorId` refers to the view the user can
       swipe and drag.

     - `motion:touchAnchorSide` means the
       view is being dragged from the right side.

     - `motion:dragDirection` refers to the *progress*
       direction of the drag. For example,
       `motion:dragDirection="dragRight"` means progress
       increases as the view is dragged to the right.

   - `https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset`
     is where you define the various constraints that describe your motion.
     In this example, one `<ConstraintSet>` is defined for
     each endpoint of your motion. These endpoints are centered vertically
     using `app:layout_constraintTop_toTopOf="parent"` and
     `app:layout_constraintBottom_toBottomOf="parent"`.
     Horizontally, the endpoints are at the far left and right sides of the
     screen.

   For a more detailed look at the various elements that a motion scene
   supports, see the
   [MotionLayout examples](https://developer.android.com/training/constraint-layout/motion-layout-examples).

## Interpolated attributes

Within a motion scene file, `ConstraintSet` elements can contain additional
attributes that are interpolated during transition. In addition to position and
bounds, the following attributes are interpolated by `MotionLayout`:

- `alpha`
- `visibility`
- `elevation`
- `rotation`, `rotationX`, `rotationY`
- `translationX`, `translationY`, `translationZ`
- `scaleX`, `scaleY`

## Custom attributes

Within a `<Constraint>`, you can use the `<CustomAttribute>` element to specify
a transition for attributes that aren't simply related to position or `View`
attributes.

```xml
<Constraint
    android:id="@+id/button" ...>
    <CustomAttribute
        motion:attributeName="backgroundColor"
        motion:customColorValue="#D81B60"/>
</Constraint>
```

A `<CustomAttribute>` contains two attributes of its own:

- `motion:attributeName` is required and must match an object with getter and setter methods. The getter and setter must match a specific pattern. For example, `backgroundColor` is supported, since the view has underlying `getBackgroundColor()` and `setBackgroundColor()` methods.
- The other attribute you must provide is based on the value type. Choose from the following supported types:
  - `motion:customColorValue` for colors
  - `motion:customIntegerValue` for integers
  - `motion:customFloatValue` for floats
  - `motion:customStringValue` for strings
  - `motion:customDimension` for dimensions
  - `motion:customBoolean` for booleans

When specifying a custom attribute, define endpoint values in both the start and
end `<ConstraintSet>` elements.

### Change background color

Building on the previous example, suppose you want the view's colors to change
as part of its motion, as shown in figure 2.
**Figure 2.** The view changes its background color as it moves.

Add a `<CustomAttribute>` element to each `ConstraintSet` elements, as shown in
the following code snippet:

```xml
<ConstraintSet android:id="@+id/start">
    <Constraint
        android:id="@+id/button"
        android:layout_width="64dp"
        android:layout_height="64dp"
        android:layout_marginStart="8dp"
        motion:layout_constraintBottom_toBottomOf="parent"
        motion:layout_constraintStart_toStartOf="parent"
        motion:layout_constraintTop_toTopOf="parent">
        <CustomAttribute
            motion:attributeName="backgroundColor"
            motion:customColorValue="#D81B60" />
    </Constraint>
</ConstraintSet>

<ConstraintSet android:id="@+id/end">
    <Constraint
        android:id="@+id/button"
        android:layout_width="64dp"
        android:layout_height="64dp"
        android:layout_marginEnd="8dp"
        motion:layout_constraintBottom_toBottomOf="parent"
        motion:layout_constraintEnd_toEndOf="parent"
        motion:layout_constraintTop_toTopOf="parent">
        <CustomAttribute
            motion:attributeName="backgroundColor"
            motion:customColorValue="#9999FF" />
    </Constraint>
</ConstraintSet>
```

## Additional MotionLayout attributes

In addition to the attributes in the preceding example, `MotionLayout` has other
attributes you might want to specify:

- `app:applyMotionScene="boolean"` indicates whether to apply the motion scene. The default value for this attribute is `true`.
- `app:showPaths="boolean"` indicates whether to show the motion paths as the motion is running. The default value for this attribute is `false`.
- `app:progress="float"` lets you explicitly specify transition progress. You can use any floating-point value from `0` (the start of the transition) to `1` (the end of the transition).
- `app:currentState="reference"` lets you specify a specific `ConstraintSet`.
- `app:motionDebug` lets you display additional debug information about the motion. Possible values are `"SHOW_PROGRESS"`, `"SHOW_PATH"`, or `"SHOW_ALL"`.

## Additional resources

For more information about `MotionLayout`, see the following resources:

- [Advanced Android in Kotlin 03.2: Animation with MotionLayout](https://codelabs.developers.google.com/codelabs/motion-layout)
- [MotionLayout examples](https://developer.android.com/training/constraint-layout/motion-layout-examples)
- [MotionLayout/ConstraintLayout Samples](https://github.com/android/views-widgets-samples/tree/main/ConstraintLayoutExamples) on GitHub
- [Introduction to MotionLayout (part I)](https://medium.com/google-developers/introduction-to-motionlayout-part-i-29208674b10d)
- [Introduction to MotionLayout (part II)](https://medium.com/google-developers/introduction-to-motionlayout-part-ii-a31acc084f59)
- [Introduction to MotionLayout (part III)](https://medium.com/google-developers/introduction-to-motionlayout-part-iii-47cd64d51a5)
- [Introduction to MotionLayout (part IV)](https://medium.com/google-developers/defining-motion-paths-in-motionlayout-6095b874d37)