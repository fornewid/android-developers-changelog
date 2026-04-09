---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyattribute
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyattribute
source: md.txt
---

[Video](https://www.youtube.com/watch?v=jUm_AkH_mAQ)

Specifies view attributes at a specific moment during the motion sequence. You
can use `<KeyAttribute>` to set the view's [standard attributes](https://developer.android.com/reference/android/support/constraint/motion/MotionLayout#standard-attributes).

Suppose a view's opacity (`android:alpha`) is set to 0 in the initial
`<ConstraintSet>` and 1 in the final `<ConstraintSet>`. By default, this makes
the view linearly fade in for the entire motion sequence. If you want the view
to remain invisible for 80% of the motion sequence and then fade in quickly, add
a `<KeyAttribute>` node with the `motion:framePosition` attribute set to 80 and
the `android:alpha` attribute set to 0.

## Syntax

```xml
<KeyAttribute
  motion:motionTarget="@id/targetPath"
  motion:framePosition="percentage"
  [ attribute = value ]
/>
```

## Attributes

`motion:motionTarget`
:   View whose attributes are controlled by this `<KeyAttribute>`.

`motion:framePosition`
:   Integer from 1 to 99 specifying when in the motion sequence the view has the
    attributes specified by this `<KeyAttribute>`. For example, if `framePosition`
    is 25, then the view has the specified attributes one-quarter of the way
    through the motion sequence.

You can set the following view attributes. For more information about these
attributes, see the [`View`](https://developer.android.com/reference/android/view/View) reference page.

- `android:alpha`
- `android:elevation`
- `android:rotation`
- `android:rotationX`
- `android:rotationY`
- `android:scaleX`
- `android:scaleY`
- `android:translationX`
- `android:translationY`
- `android:translationZ`
- `android:visibility`
- `transitionPathRotate`

## Contained in

- [`<KeyFrameSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset)