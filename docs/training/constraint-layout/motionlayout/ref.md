---
title: MotionLayout reference  |  Android Developers
url: https://developer.android.com/training/constraint-layout/motionlayout/ref
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# MotionLayout reference Stay organized with collections Save and categorize content based on your preferences.



[`MotionLayout`](/reference/androidx/constraintlayout/motion/widget/MotionLayout)
uses a *motion scene* file to define a motion sequence. A motion scene file is
an XML file that specifies all the aspects of a motion sequence.
The `<MotionLayout>` node in
the layout file has an `app:layoutDescription` attribute that points to the
motion scene file.

This reference is not comprehensive. It provides information on the most
important motion scene file elements and their most commonly used attributes.

[`<MotionScene>`](/training/constraint-layout/motionlayout/ref/motionscene)
:   The root element of a motion scene file.

[`<ConstraintSet>`](/training/constraint-layout/motionlayout/ref/constraintset)
:   Specifies the positions and attributes of all views at one point in a
    motion sequence.

[`<Constraint>`](/training/constraint-layout/motionlayout/ref/constraint)
:   Specifies the location and attributes of one element of a motion
    sequence.

[`<Transition>`](/training/constraint-layout/motionlayout/ref/transition)
:   Specifies the beginning and end states of a motion sequence, the desired
    intermediate states, and the user interactions that trigger the sequence.

[`<OnClick>`](/training/constraint-layout/motionlayout/ref/onclick)
:   Specifies the action to perform when the user taps a view.

[`<OnSwipe>`](/training/constraint-layout/motionlayout/ref/onswipe)
:   Specifies the action to perform when the user swipes on the layout.

[`<KeyFrameSet>`](/training/constraint-layout/motionlayout/ref/keyframeset)
:   Specifies location and attributes for views over the course of the motion
    sequence.

[`<KeyPosition>`](/training/constraint-layout/motionlayout/ref/keyposition)
:   Specifies a view's location at a specific moment during the motion sequence.

[`<KeyAttribute>`](/training/constraint-layout/motionlayout/ref/keyattribute)
:   Specifies a view's attributes at a specific moment during the motion sequence.