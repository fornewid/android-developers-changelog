---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene
source: md.txt
---

# &lt;MotionScene&gt;

Root element of a motion scene file. The`<MotionScene>`contains one or more[`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)elements, each of which defines the start and end state of a motion sequence and the transition between the two.

## Syntax

```xml
<MotionScene xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:android="http://schemas.android.com/apk/res/android">
    ...
</MotionScene>
```

## Must contain

`<Transition>`
:   Specifies the motion sequence to perform. If the`<MotionScene>`contains multiple`<Transition>`elements, the`MotionLayout`chooses the most appropriate`<Transition>`based on the user's interaction. For example, a`<MotionScene>`might have four`<Transition>`children, each with an[`<OnSwipe>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe)for a user swipe in a different direction. When the user swipes on the screen, the`MotionLayout`uses the appropriate`<Transition>`for a swipe in that direction.

## Can contain

[`<ConstraintSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset)
:   Specifies a beginning or ending state for one or more of the`<Transition>`nodes. The`<MotionLayout>`is not permitted to have`<ConstraintSet>`children, since the`<Transition>`can point to XML layouts instead of pointing to constraint sets.

## Attributes

`defaultDuration`
:   Default duration for all transitions in milliseconds. The default duration is used for motion sequences that don't specify their own duration. For example, if you set`defaultDuration="300"`, all motion sequences default to 300 milliseconds in length if they don't explicitly specify their own duration.