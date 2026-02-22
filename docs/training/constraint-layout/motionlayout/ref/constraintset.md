---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset
source: md.txt
---

# &lt;ConstraintSet&gt;

Specifies the positions and attributes of all views at one point in a motion sequence. Typically, a[`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)element points to two`<ConstraintSet>`elements, one defining the beginning of the motion sequence and one defining the end.

## Syntax

```xml
<ConstraintSet
  id="@id/name">
  [ deriveConstraintsFrom="id" ]
    ...
</ConstraintSet>
```

## Attributes

`deriveConstraintsFrom`
:   *(optional)* The ID of another`ConstraintSet`. If specified, all constraints from that set are applied to this`ConstraintSet`, unless this set specifically overrides them.

`android:id`
:   Unique identifier for this constraint set. The`<Transition>`needs this ID to identify the start and end points of the motion sequence.

## Must contain

- One or more[`<Constraint>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/constraint)elements.

## Contained in

- [`<MotionScene>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene)