---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition
source: md.txt
---

# &lt;KeyPosition&gt;

Specifies a view's position at a specific moment during the motion sequence. This attribute is used to adjust the default path of the motion.

For example, if an object begins at the upper-left corner and ends at the lower-right corner, the default motion sequence moves the object diagonally down the screen. By adding one or more`<KeyPosition>`elements, you can deform the path.

## Syntax

```xml
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
:   View whose motion is controlled by this`<KeyPosition>`.

`motion:framePosition`
:   Integer from 1 to 99 specifying when in the motion sequence the view reaches the point specified by this`<KeyPosition>`. For example, if`framePosition`is 25, the view reaches the specified point one-quarter of the way through the motion.

`motion:percentX`,`motion:percentY`
:   Specify the position the view reaches. The`keyPositionType`attribute specifies how these values are interpreted.

`motion:keyPositionType`
:   Specifies how the`percentX`and`percentY`values are interpreted. Possible settings are the following:

## Contained In

- [`<KeyFrameSet>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset)