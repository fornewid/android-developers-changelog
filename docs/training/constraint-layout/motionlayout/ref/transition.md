---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/transition
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/transition
source: md.txt
---

# &lt;Transition&gt;

Specifies the beginning and end state of a motion sequence, the target intermediate states, and the user interactions that trigger the motion.

## Syntax

```xml
<Transition
  motion:constraintSetStart="start"
  motion:constraintSetEnd="end"
  [ motion:duration="integer" ] >
  ...
</Transition>
```

## Attributes

`motion:constraintSetStart`
:   Initial state of the motion sequence. This can either be the ID of a[`<ConstraintSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset)or a layout. To specify a`<ConstraintSet>`, set this attribute to`"@+id/`<var translate="no">constraintSetId</var>`"`. To specify a layout, set it to`"@layout/`<var translate="no">layoutState</var>`"`.

`motion:constraintSetEnd`
:   Final state of the motion sequence. This can either be the ID of a`<ConstraintSet>`, or a layout. To specify a`<ConstraintSet>`, set this attribute to`"@+id/`<var translate="no">constraintSetId</var>`"`. To specify a layout, set it to`"@layout/`<var translate="no">layoutState</var>`"`.

`motion:duration`
:   Duration of the motion sequence in milliseconds. If not specified, the[`<MotionScene>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene)element's`defaultDuration`is used.

## Can contain

[`<onClick>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onclick)
:   Indicates that the motion sequence is triggered by a user touch.

[`<onSwipe>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe)
:   Indicates that the motion sequence is triggered by a user swipe.

[`<KeyFrameSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset)
:   Specifies one or more intermediate positions or attribute settings for elements in the motion sequence.

## Contained in

- [`<MotionScene>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene)