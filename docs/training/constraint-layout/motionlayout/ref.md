---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref
url: https://developer.android.com/training/constraint-layout/motionlayout/ref
source: md.txt
---

# MotionLayout reference

[`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout)uses a*motion scene* file to define a motion sequence. A motion scene file is an XML file that specifies all the aspects of a motion sequence. The`<MotionLayout>`node in the layout file has an`app:layoutDescription`attribute that points to the motion scene file.

This reference is not comprehensive. It provides information on the most important motion scene file elements and their most commonly used attributes.

[`<MotionScene>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/motionscene)
:   The root element of a motion scene file.

[`<ConstraintSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/constraintset)
:   Specifies the positions and attributes of all views at one point in a motion sequence.

[`<Constraint>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/constraint)
:   Specifies the location and attributes of one element of a motion sequence.

[`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)
:   Specifies the beginning and end states of a motion sequence, the desired intermediate states, and the user interactions that trigger the sequence.

[`<OnClick>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onclick)
:   Specifies the action to perform when the user taps a view.

[`<OnSwipe>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe)
:   Specifies the action to perform when the user swipes on the layout.

[`<KeyFrameSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset)
:   Specifies location and attributes for views over the course of the motion sequence.

[`<KeyPosition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition)
:   Specifies a view's location at a specific moment during the motion sequence.

[`<KeyAttribute>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyattribute)
:   Specifies a view's attributes at a specific moment during the motion sequence.