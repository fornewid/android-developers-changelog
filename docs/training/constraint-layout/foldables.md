---
title: https://developer.android.com/training/constraint-layout/foldables
url: https://developer.android.com/training/constraint-layout/foldables
source: md.txt
---

# Designing for foldables

![](https://developer.android.com/static/images/training/constraint-layout/foldable_resized_2.gif)

In the[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)2.1 release, several features were added to help manage[foldable devices](https://developer.android.com/guide/topics/ui/foldables), including[`SharedValues`](https://developer.android.com/reference/androidx/constraintlayout/widget/SharedValues),[`ReactiveGuide`](https://github.com/androidx/constraintlayout/blob/d89c45dbb74bf19ad4834198a04af306696357bc/constraintlayout/constraintlayout/src/main/java/androidx/constraintlayout/widget/ReactiveGuide.java), and enhanced support for animation with[`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout).

## Shared Values

We added a new mechanism to inject runtime values in`ConstraintLayout`-- this is intended to be used for system-wide values, as all instances of`ConstraintLayout`are able to access the value.

In the context of foldable devices, we can use this mechanism to inject the position of the fold at runtime:  

### Kotlin

```kotlin
ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, fold)
```

### Java

```java
ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, fold);
```

In a custom helper, you can access the shared values by adding a listener for any changes:  

### Kotlin

```kotlin
val sharedValues: SharedValues = ConstraintLayout.getSharedValues()
sharedValues.addListener(mAttributeId, this)
```

### Java

```java
SharedValues sharedValues = ConstraintLayout.getSharedValues();
sharedValues.addListener(mAttributeId, this);
```

You can look at the[FoldableExperiments example](https://github.com/androidx/constraintlayout/blob/main/projects/FoldableExperiments/app/src/main/java/com/example/experiments/MainActivity.kt)to see how we capture the position of the fold using the[Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window)library and inject the position into`ConstraintLayout`.  

### Kotlin

```kotlin
inner class StateContainer : Consumer<WindowLayoutInfo> {

    override fun accept(newLayoutInfo: WindowLayoutInfo) {

        // Add views that represent display features
        for (displayFeature in newLayoutInfo.displayFeatures) {
            val foldFeature = displayFeature as? FoldingFeature
            if (foldFeature != null) {
                if (foldFeature.isSeparating &&
                    foldFeature.orientation == FoldingFeature.Orientation.HORIZONTAL
                ) {
                    // The foldable device is in tabletop mode
                    val fold = foldPosition(motionLayout, foldFeature)
                    ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, fold)
                } else {
                    ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, 0);
                }
            }
        }
    }
}
```

### Java

```java
class StateContainer implements Consumer<WindowLayoutInfo> {

    @Override
    public void accept(WindowLayoutInfo newLayoutInfo) {

        // Add views that represent display features
        for (DisplayFeature displayFeature : newLayoutInfo.getDisplayFeatures()) {
            if (displayFeature instanceof FoldingFeature) {
                FoldingFeature foldFeature = (FoldingFeature)displayFeature;
                if (foldFeature.isSeparating() &&
                    foldFeature.getOrientation() == FoldingFeature.Orientation.HORIZONTAL
                ) {
                    // The foldable device is in tabletop mode
                    int fold = foldPosition(motionLayout, foldFeature);
                    ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, fold);
                } else {
                    ConstraintLayout.getSharedValues().fireNewValue(R.id.fold, 0);
                }
            }
        }
    }
}
```

`fireNewValue()`takes an ID representing the value as the first parameter and the value to inject as the second parameter.

## `ReactiveGuide`

![](https://developer.android.com/static/images/training/constraint-layout/fold-2.png)

One way to take advantage of a`SharedValue`in a layout, without having to write any code, is to use the[`ReactiveGuide`](https://github.com/androidx/constraintlayout/blob/main/constraintlayout/constraintlayout/src/main/java/androidx/constraintlayout/widget/ReactiveGuide.java)helper. This will position a horizontal or vertical guideline according to the linked`SharedValue`.  

        <androidx.constraintlayout.widget.ReactiveGuide
            android:id="@+id/fold"
            app:reactiveGuide_valueId="@id/fold"
            android:orientation="horizontal" />

It can then be used as a you would with a normal guideline.

## `MotionLayout`for foldables

We added several features in`MotionLayout`in 2.1 that helps morphing state -- something particularly useful for foldables, as we typically have to handle animating between the different possible layouts.

There are two approaches available for foldables:

- At runtime, update your current layout (`ConstraintSet`) to show or hide the fold.
- Use a separate`ConstraintSet`for each of the foldable states you want to support (`closed`,`folded`, or`fully open`).

### Animating a`ConstraintSet`

The function`updateStateAnimate()`in`MotionLayout`was added in the 2.1 release:  

### Kotlin

```kotlin
fun updateStateAnimate(stateId: Int, set: ConstraintSet, duration: Int)
```

### Java

```java
void updateStateAnimate(int stateId, ConstraintSet set, int duration);
```

This function will automatically animate the changes when updating a given`ConstraintSet`instead of doing an immediate update (which you can do with`updateState(stateId, constraintset)`). This allows you to update your UI on the fly, depending on changes, such as which foldable state you are in.

### `ReactiveGuide`inside a`MotionLayout`

`ReactiveGuide`also supports two useful attributes when used inside a`MotionLayout`:

- `app:reactiveGuide_animateChange="true|false"`

- `app:reactiveGuide_applyToAllConstraintSets="true|false"`

The first one will modify the current`ConstraintSet`and animate the change automatically. The second one will apply the new value of the`ReactiveGuide`position to all`ConstraintSet`s in the`MotionLayout`. A typical approach for foldables would be to use a`ReactiveGuide`representing the fold position, setting up your layout elements relative to the`ReactiveGuide`.

### Using multiple`ConstraintSet`s to represent foldable state

Instead of updating the current`MotionLayout`state, another way to architect your UI to support foldables is to create specific separate states (including`closed`,`folded`, and`fully open`).

![](https://developer.android.com/static/images/training/constraint-layout/fold-1.png)

In this scenario, you might still want to use a`ReactiveGuide`to represent the fold, but you would have a lot more control (compared to the automated animation when updating the current`ConstraintSet`) on how each state would transition into another.

With this approach, in your`DeviceState`listener, you would simply direct the`MotionLayout`to transition to specific states through the[`MotionLayout.transitionToState(stateId)`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout#transitionToState(int))method.