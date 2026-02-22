---
title: https://developer.android.com/studio/write/motion-editor
url: https://developer.android.com/studio/write/motion-editor
source: md.txt
---

# Build animation with the Motion Editor

Android Studio includes a visual design editor for the
[MotionLayout](https://developer.android.com/training/constraint-layout/motionlayout) layout type, making it
easier to create and preview animations.

The Motion Editor provides a simple interface for manipulating elements from the
MotionLayout library that serves as the foundation for animation in Android
apps. Without Android Studio, creating and altering these elements requires
manually editing constraints in XML resource files. The Motion Editor, however,
can generate this XML for you, with support for start and end states, keyframes,
transitions, and timelines.
| **Note:** Before using the Motion Editor, be sure to set the `ConstraintLayout` dependency in your `build.gradle` file to version `2.0.0-beta3`, as described in the MotionLayout [reference documentation](https://developer.android.com/training/constraint-layout/motionlayout#getting_started).

To get started with the Motion Editor:

1. [Create a ConstraintLayout](https://developer.android.com/training/constraint-layout#add-constraintlayout-to-your-project).
2. Right-click on the preview in the Layout Editor.
3. Click **Convert to MotionLayout**, as shown below.

![](https://developer.android.com/static/studio/images/write/motion-editor-convert.png)

After Android Studio converts your ConstraintLayout to MotionLayout, a Motion
Scene file (an `.xml` file with `_scene` appended to your layout filename) is
also added to the directory containing your XML.

![](https://developer.android.com/static/studio/images/write/convert_to_motion_layout.png)

The `MotionLayout` then becomes your root layout, and it appears in the Motion
Editor UI. The layout already includes a start `ConstraintSet`, end
`ConstraintSet`, and a transition going from start to end.

![](https://developer.android.com/static/studio/images/write/start_end_constraint_set.png)

You can use the overview graphic to select a `ConstraintSet` or
`Transition` and to select components on the selection panel.

![](https://developer.android.com/static/studio/images/write/motion-editor-select.gif)

Then you can edit the constraints and attributes of either the start or end
`ConstraintSet` the same way you would edit a `ConstraintLayout`.

![](https://developer.android.com/static/studio/images/write/motion_edit_constraints.gif)

If you want to build more elements to your graph, you can use the creation
icons to quickly add a `ConstraintSet`, `Transition`, or `OnClick`/`OnSwipe`
gestures.

![](https://developer.android.com/static/studio/images/write/motion_creation_icons.png)

To add a keyframe, first click on the **Transition** arrow:

![](https://developer.android.com/static/studio/images/write/motion-editor-add-keyframe.png)

Then, in the **Transition** timeline pane, click on the top-right corner and
select **KeyPosition**:

![](https://developer.android.com/static/studio/images/write/motion-editor-keyposition.png)

This action opens a dialog where you can set attributes for the keyframe.

You can also add `OnClick` and `OnSwipe` handlers to the Transition in the
attribute panel.

![](https://developer.android.com/static/studio/images/write/motion_attribute_panel.png)

This action opens a dialog where you can set attributes of the click such as
target components and drag direction.

The Motion Editor supports previewing animations on the design surface. When an
animation is selected, click **Play**
![](https://developer.android.com/static/studio/images/write/motion_play_icon.png)
above the timeline to preview the animation.

![](https://developer.android.com/static/studio/images/write/motion_animation_preview.gif)