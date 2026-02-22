---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/onswipe
source: md.txt
---

# &lt;OnSwipe&gt;

Specifies the action to perform when the user swipes on the layout. The speed of the motion sequence and the motion of the targeted view are affected by the speed and direction of the swipe, subject to the limits you set with optional parameters.

There can be multiple`<OnSwipe>`nodes for a single`<Transition>`, with each`<OnSwipe>`specifying a different swipe direction and a different action to perform when the user performs that swipe.

## Syntax

```xml
<OnSwipe
  motion:touchAnchorId="@id/target_view"
  motion:touchAnchorSide="side"
[ motion:dragDirection="direction" ]
[ motion:dragScale="scale" ]
[ motion:maxVelocity="maxVelocity" ]
[ motion:maxAcceleration="maxAcceleration" ]
 />
```

## Attributes

`motion:touchAnchorId`
:   View that is being moved by the swipe.

`motion:touchAnchorSide`
:   Side of the target view that the swipe is anchored to.`MotionLayout`keeps a constant distance between the anchor and the user's finger. Acceptable values are`"left"`,`"right"`,`"top"`, and`"bottom"`.

`motion:dragDirection`
:   Direction of the user's swipe motion. If this attribute is set, this`<OnSwipe>`only applies to swipes in the specified direction. Acceptable values are`"dragLeft"`,`"dragRight"`,`"dragUp"`, and`"dragDown"`.

`motion:dragScale`

:   Controls the distance the view moves relative to the length of the swipe. The default value is 1, indicating that the view moves as far as the swipe does. If`dragScale`is less than 1, the view moves less than the swipe distance. For example, a`dragScale`of 0.5 means that if the swipe moves 4 cm, the target view moves 2 cm.

    If`dragScale`is greater than 1, the view moves farther than the swipe distance. For example, a`dragScale`of 1.5 means that if the swipe moves 4 cm, the target view moves 6 cm.

`motion:maxVelocity`

:   Maximum velocity of the target view.

`motion:maxAcceleration`

:   Maximum acceleration of the target view.

## Contained in

- [`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)