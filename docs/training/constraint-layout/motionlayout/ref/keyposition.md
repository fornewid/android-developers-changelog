---
title: <KeyPosition>  |  Android Developers
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# <KeyPosition> Stay organized with collections Save and categorize content based on your preferences.



Specifies a view's position at a specific moment during the motion sequence.
This attribute is used to adjust the default path of the motion.

For example, if an object begins at the upper-left corner and ends at the
lower-right corner, the default motion sequence moves the object diagonally down
the screen. By adding one or more `<KeyPosition>` elements, you can deform the
path.

## Syntax

```
<KeyPosition
    motion:motionTarget="@id/targetPath"
    motion:framePosition="percentage"
    motion:keyPositionType="type"
    motion:percentX="xOffset"
  motion:percentY="yOffset"
/>
```

## Attributes

`motion:motionTarget`
:   View whose motion is controlled by this `<KeyPosition>`.

`motion:framePosition`
:   Integer from 1 to 99 specifying when in the motion sequence the view reaches
    the point specified by this `<KeyPosition>`. For example, if
    `framePosition` is 25, the view reaches the specified point
    one-quarter of the way through the motion.

`motion:percentX`, `motion:percentY`
:   Specify the position the view reaches. The `keyPositionType`
    attribute specifies how these values are interpreted.

`motion:keyPositionType`
:   Specifies how the `percentX` and `percentY` values are
    interpreted. Possible settings are the following:

* `parentRelative`
:   `percentX` and `percentY` are specified relative to
    the parent view. *X* is the horizontal axis, ranging from 0 for the left
    side to 1 for the right side. *Y* is the vertical axis, with 0 being the
    top and 1 being the bottom.

    For example, if you want the target view to reach a point midway down the
    right side of the parent view, set `percentX` to 1 and
    `percentY` to 0.5.
* `deltaRelative`
:   `percentX` and `percentY` are specified relative to
    the distance the view moves over the course of the whole motion sequence.
    *X* is the horizontal axis and *Y* is the vertical axis. In both
    cases, 0 is the starting position of the view in that axis, and 1 is the final
    position.

    Suppose the target view moves 100 dp up and 100 dp to the right, but you want
    the view to move down 40 dp for the first quarter of the motion, then arc back
    up. Set `framePosition` to 25, `keyPositionType` to
    `deltaRelative`, and `percentY` to -0.4.
* `pathRelative`
:   The X-axis is the direction the target view moves over the course of the
    path, with 0 being the starting position and 1 being the final position. The
    Y-axis is perpendicular to the X-axis, with positive values to the left of the
    path and negative values to the right. So the initial position of the view is
    `(0,0)` and the final position is `(1,0)`. Setting a
    non-zero `percentY` causes the view to arc to one direction or the
    other.

    Suppose you want the view to take half of the motion sequence to cover 10% of
    the total distance, then speed up to cover the other 90%. Set
    `framePosition` to 50, `keyPositionType` to
    `pathRelative`, and `percentX` to 0.1.
    `percentY` remains 0.

## Contained In

* [`<KeyFrameSet>`](/training/constraint-layout/motionlayout/ref/keyframeset)