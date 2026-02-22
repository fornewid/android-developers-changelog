---
title: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset
url: https://developer.android.com/training/constraint-layout/motionlayout/ref/keyframeset
source: md.txt
---

# &lt;KeyFrameSet&gt;

Specifies location and attributes for views over the course of the motion sequence. By default, motion proceeds from the initial state to the end state. By using`<KeyFrameSet>`, you can build more complex motions.

The`<KeyFrameSet>`contains[`<KeyPosition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition)or[`<KeyAttribute>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyattribute)nodes. These nodes specify the position or attributes of a target view at a specific point in the motion.[`MotionLayout`](https://developer.android.com/reference/androidx/constraintlayout/motion/widget/MotionLayout)smoothly animates the view from the starting point to each intermediate point and then to the final destination.

Suppose the initial state of the motion sequence has an opaque ball in the lower-left corner of the view, and the final state makes the ball transparent in the upper-right corner. By default, the`MotionLayout`moves the ball smoothly in a diagonal line, gradually becoming transparent until it vanishes when it reaches its destination. By using`<KeyFrameSet>`, you can change this behavior. For example, you can make the ball move vertically to the upper-left corner while remaining entirely opaque, then move horizontally to the upper-right corner while fading out. You can do this by creating a`<KeyFrameSet>`and adding a`<KeyPosition>`and`<KeyAttribute>`inside it. The`<KeyPosition>`specifies the intermediate location of the ball, and the`<KeyAttribute>`specifies that the ball remains opaque at the midpoint of the motion.

## Syntax

```xml
<KeyFrameSet>
    [ <KeyPosition/>... ]
    [ <KeyAttribute/>...]
</KeyFrameSet>
```

## Contained in

[`<Transition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/transition)

## Contains

[`<KeyPosition>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyposition)
:   Specifies a view's position at a specific moment during the motion sequence.

[`<KeyAttribute>`](https://developer.android.com/training/constraint-layout/motionlayout/ref/keyattribute)
:   Specifies view attributes at a specific moment during the motion sequence.