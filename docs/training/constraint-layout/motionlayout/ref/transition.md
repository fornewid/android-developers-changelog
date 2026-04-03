---
title: <Transition>  |  Android Developers
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/transition
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# <Transition> Stay organized with collections Save and categorize content based on your preferences.



Specifies the beginning and end state of a motion sequence, the target
intermediate states, and the user interactions that trigger the motion.

## Syntax

```
<Transition
  motion:constraintSetStart="start"
  motion:constraintSetEnd="end"
  [ motion:duration="integer" ] >
  ...
</Transition>
```

## Attributes

`motion:constraintSetStart`
:   Initial state of the motion sequence. This can either be the ID of a
    [`<ConstraintSet>`](/training/constraint-layout/motionlayout/ref/constraintset)
    or a layout. To specify a `<ConstraintSet>`, set this
    attribute to
    `"@+id/constraintSetId"`. To specify a layout, set
    it to `"@layout/layoutState"`.

`motion:constraintSetEnd`
:   Final state of the motion sequence. This can either be the ID of a
    `<ConstraintSet>`, or a layout. To specify a `<ConstraintSet>`, set this
    attribute to `"@+id/constraintSetId"`. To specify a
    layout, set it to `"@layout/layoutState"`.

`motion:duration`
:   Duration of the motion sequence in milliseconds. If not specified, the
    [`<MotionScene>`](/training/constraint-layout/motionlayout/ref/motionscene)
    element's `defaultDuration` is used.

## Can contain

[`<onClick>`](/training/constraint-layout/motionlayout/ref/onclick)
:   Indicates that the motion sequence is triggered by a user touch.

[`<onSwipe>`](/training/constraint-layout/motionlayout/ref/onswipe)
:   Indicates that the motion sequence is triggered by a user swipe.

[`<KeyFrameSet>`](/training/constraint-layout/motionlayout/ref/keyframeset)
:   Specifies one or more intermediate positions or attribute settings for
    elements in the motion sequence.

## Contained in

* [`<MotionScene>`](/training/constraint-layout/motionlayout/ref/motionscene)