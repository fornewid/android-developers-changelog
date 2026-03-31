---
title: <ConstraintSet>  |  Android Developers
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# <ConstraintSet> Stay organized with collections Save and categorize content based on your preferences.



Specifies the positions and attributes of all views at one point in a motion
sequence. Typically, a
[`<Transition>`](/training/constraint-layout/motionlayout/ref/transition)
element points to two `<ConstraintSet>` elements, one defining the beginning of
the motion sequence and one defining the end.

## Syntax

```
<ConstraintSet
  id="@id/name">
  [ deriveConstraintsFrom="id" ]
    ...
</ConstraintSet>
```

## Attributes

`deriveConstraintsFrom`
:   *(optional)* The ID of another `ConstraintSet`. If specified, all constraints
    from that set are applied to this `ConstraintSet`, unless this set specifically
    overrides them.

`android:id`
:   Unique identifier for this constraint set. The `<Transition>` needs this ID to
    identify the start and end points of the motion sequence.

## Must contain

* One or more
  [`<Constraint>`](/training/constraint-layout/motionlayout/ref/constraint)
  elements.

## Contained in

* [`<MotionScene>`](/training/constraint-layout/motionlayout/ref/motionscene)