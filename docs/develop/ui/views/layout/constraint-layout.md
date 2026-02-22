---
title: https://developer.android.com/develop/ui/views/layout/constraint-layout
url: https://developer.android.com/develop/ui/views/layout/constraint-layout
source: md.txt
---

# Build a responsive UI with ConstraintLayout
Part of [Android Jetpack](https://developer.android.com/jetpack).


Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.  
[ConstraintLayout in Compose →](https://developer.android.com/develop/ui/compose/layouts/constraintlayout)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

[`ConstraintLayout`](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout)
lets you create large, complex layouts with a flat view hierarchy---no
nested view groups. It's similar to
[`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout)
in that all views are laid out according to relationships between sibling views
and the parent layout, but it's more flexible than `RelativeLayout`
and easier to use with Android Studio's Layout Editor.

All the power of `ConstraintLayout` is available directly from the
Layout Editor's visual tools, because the layout API and the Layout Editor are
specially built for each other. You can build your layout with
`ConstraintLayout` entirely by dragging instead of editing the
XML.  

This page shows how to build a layout with `ConstraintLayout` in
Android Studio 3.0 or higher. For more information about the Layout Editor,
see [Build a UI with Layout Editor](https://developer.android.com/studio/write/layout-editor).


To see a variety of layouts you can create with `ConstraintLayout`,
see the
[Constraint Layout Examples project on GitHub](https://github.com/android/views-widgets-samples/tree/main/ConstraintLayoutExamples).

## Constraints overview

To define a view's position in `ConstraintLayout`, you add at
least one horizontal and one vertical constraint for the view. Each constraint
represents a connection or alignment to another view, the parent layout, or an
invisible guideline. Each constraint defines the view's position along the
vertical or horizontal axis. Each view must have a minimum of one constraint for
each axis, but often more are necessary.

When you drop a view into the Layout Editor, it stays where you leave it even
if it has no constraints. This is only to make editing easier. If a view has no
constraints when you run your layout on a device, it is drawn at position \[0,0\]
(the top-left corner).

In figure 1, the layout looks good in the editor, but there's no vertical
constraint on view C. When this layout draws on a device, view C horizontally
aligns with the left and right edges of view A, but it appears at the top of the
screen because it has no vertical constraint.  
![](https://developer.android.com/static/training/constraint-layout/images/constraint-fail_2x.png)

**Figure 1.** The editor shows view C below A, but it
has no vertical constraint.  
![](https://developer.android.com/static/training/constraint-layout/images/constraint-fail-fixed_2x.png)

**Figure 2.** View C is now vertically constrained
below view A.

Although a missing constraint doesn't cause a compilation error, the Layout
Editor indicates missing constraints as an error in the toolbar. To view the
errors and other warnings, click **Show Warnings and Errors**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-errors.png).
To help you avoid missing constraints, the Layout Editor automatically adds
constraints for you with the
[Autoconnect and infer constraints](https://developer.android.com/develop/ui/views/layout/constraint-layout#use-autoconnect-and-infer-constraints)
features.

## Add ConstraintLayout to your project

To use `ConstraintLayout` in your project, proceed as follows:

1. Ensure you have the `maven.google.com` repository declared in your `settings.gradle` file:  

   ### Groovy

   ```groovy
       dependencyResolutionManagement {
         ...
         repositories {
             google()
         }
       )
       
   ```

   ### Kotlin

   ```kotlin
       dependencyResolutionManagement {
         ...
         repositories {
             google()
         }
       }
       
   ```
2. Add the library as a dependency in the module-level `build.gradle` file, as shown in the following example. The latest version might be different than what is shown in the example.  

   ### Groovy

   ```groovy
   dependencies {
       implementation "androidx.constraintlayout:constraintlayout:2.2.1"
       // To use constraintlayout in compose
       implementation "androidx.constraintlayout:constraintlayout-compose:1.1.1"
   }
   ```

   ### Kotlin

   ```kotlin
   dependencies {
       implementation("androidx.constraintlayout:constraintlayout:2.2.1")
       // To use constraintlayout in compose
       implementation("androidx.constraintlayout:constraintlayout-compose:1.1.1")
   }
   ```
3. In the toolbar or sync notification, click **Sync Project with Gradle
   Files**.

Now you're ready to build your layout with `ConstraintLayout`.

### Convert a layout

![](https://developer.android.com/static/training/constraint-layout/images/layout-editor-convert-to-constraint_2x.png)


**Figure 3.** The menu to convert a layout to
`ConstraintLayout`.

To convert an existing layout to a constraint layout, follow these steps:

1. Open your layout in Android Studio and click the **Design** tab at the bottom of the editor window.
2. In the **Component Tree** window, right-click the layout and click **Convert LinearLayout to ConstraintLayout**.

### Create a new layout

To start a new constraint layout file, follow these steps:

1. In the **Project** window, click the module folder and select **File \> New \> XML \> Layout XML**.
2. Enter a name for the layout file and enter "androidx.constraintlayout.widget.ConstraintLayout" for the **Root
   Tag**.
3. Click **Finish**.

## Add or remove a constraint

To add a constraint, do the following:  


**Video 1.**The left side of a view is constrained to the left
side of the parent.

1. Drag a view from the **Palette** window into the editor.

   When you add a view in a `ConstraintLayout`, it displays in a
   bounding box with square resizing handles on each corner and circular
   constraint handles on each side.
2. Click the view to select it.
3. Do one of the following:
   - Click a constraint handle and drag it to an available anchor point. This point can be the edge of another view, the edge of the layout, or a guideline. Notice that as you drag the constraint handle, the Layout Editor shows potential connection anchors and blue overlays.
   - Click one of the **Create a connection**
     ![](https://developer.android.com/static/studio/images/buttons/attributes-plus-icon_2x.png)
     buttons in the **Layout** section of the **Attributes** window, as shown
     in figure 4.

     ![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-create-constraint-2x.png)

     **Figure 4.** The **Layout**
     section of the **Attributes** window lets you create
     connections.

When the constraint is created, the editor gives it a
[default margin](https://developer.android.com/develop/ui/views/layout/constraint-layout#adjust-the-view-margins) to separate the two views.

When creating constraints, remember the following rules:

- Every view must have at least two constraints: one horizontal and one vertical.
- You can create constraints only between a constraint handle and an anchor point that share the same plane. A vertical plane---the left and right sides---of a view can be constrained only to another vertical plane, and baselines can constrain only to other baselines.
- Each constraint handle can be used for just one constraint, but you can create multiple constraints from different views to the same anchor point.

You can delete a constraint by doing any of the following:

- Click a constraint to select it, and then click <kbd>Delete</kbd>.
- <kbd>Control</kbd>-click (<kbd>Command</kbd>-click on macOS) a
  constraint anchor. The constraint turns red to indicate that you can click to
  delete it, as shown in figure 5.

  ![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-delete-1-2x.png)

  **Figure 5.** A red constraint indicates
  that you can click to delete it.
- In the **Layout** section of the **Attributes** window, click
  a constraint anchor, as shown in figure 6.

  ![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-delete-2-2x.png)

  **Figure 6.** Click a constraint
  anchor to delete it.


**Video 2.** Adding a constraint that opposes an existing one.

If you add opposing constraints on a view, the constraint lines become
coiled like a spring to indicate the opposing forces, as shown in video 2. The
effect is most visible when the view size is set to "fixed" or "wrap content,"
in which case the view is centered between the constraints. If you instead want
the view to stretch its size to meet the constraints,
[switch the size](https://developer.android.com/develop/ui/views/layout/constraint-layout#adjust-the-view-size) to "match constraints." If
you want to keep the current size but move the view so that it's not centered,
[adjust the constraint bias](https://developer.android.com/develop/ui/views/layout/constraint-layout#adjust-the-constraint-bias).

You can use constraints to achieve different types of layout behavior, as
described in the following sections.

### Parent position

Constrain the side of a view to the corresponding edge of the layout.

In figure 7, the left side of the view is connected to the left edge of the
parent layout. You can define the distance from the edge with margin.  
![](https://developer.android.com/static/training/constraint-layout/images/parent-constraint_2x.png)

**Figure 7.**A horizontal constraint to
the parent.

### Order position

Define the order of appearance for two views, either vertically or
horizontally.

In figure 8, B is constrained to always be to the right of A, and C is
constrained below A. However, these constraints don't imply alignment, so B can
still move up and down.  
![](https://developer.android.com/static/training/constraint-layout/images/position-constraint_2x.png)

**Figure 8.** A horizontal and vertical
constraint.

### Alignment

Align the edge of a view to the same edge of another view.

In figure 9, the left side of B is aligned to the left side of A. If you want
to align the view centers, create a constraint on both sides.

You can offset the alignment by dragging the view inward from the constraint.
For example, figure 10 shows B with a 24dp offset alignment. The offset is
defined by the constrained view's margin.

You can also select all the views you want to align, and then click
**Align**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-align.png)
in the toolbar to select the alignment type.  
![](https://developer.android.com/static/training/constraint-layout/images/alignment-constraint_2x.png)

**Figure 9.** A horizontal alignment
constraint.  
![](https://developer.android.com/static/training/constraint-layout/images/alignment-constraint-offset_2x.png)

**Figure 10.** An offset horizontal
alignment constraint.

### Baseline alignment

Align the text baseline of a view to the text baseline of another view.

In figure 11, the first line of B is aligned with the text in A.

To create a baseline constraint, right-click the text view you want to
constrain and then click **Show Baseline**. Then click on the text
baseline and drag the line to another baseline.  
![](https://developer.android.com/static/training/constraint-layout/images/baseline-constraint_2x.png)

**Figure 11.** A baseline alignment
constraint.

### Constrain to a guideline

You can add a vertical or horizontal guideline that lets you constrain your
views and is invisible to your app's users. You can position the guideline
within the layout based on either dp units or a percentage relative to the
layout's edge.

To create a guideline, click **Guidelines**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-guidelines.png)
in the toolbar, and then click either **Add Vertical Guideline** or **Add
Horizontal Guideline**.

Drag the dotted line to reposition it, and click the circle at the edge of
the guideline to toggle the measurement mode.  
![](https://developer.android.com/static/training/constraint-layout/images/guideline-constraint_2x.png)

**Figure 12.** A view constrained to a
guideline.

### Constrain to a barrier

Similar to a guideline, a barrier is an invisible line that you can constrain
views to, except a barrier doesn't define its own position. Instead, the barrier
position moves based on the position of views contained within it. This is
useful when you want to constrain a view to a set of views rather than to one
specific view.

For example, in figure 13 view C is constrained to the right side of a
barrier. The barrier is set to the "end" (or the right side, in a left-to-right
layout) of both view A and view B. The barrier moves depending on whether the
right side of view A or of view B is is farthest right.

To create a barrier, follow these steps:

1. Click **Guidelines** ![](https://developer.android.com/static/studio/images/buttons/layout-editor-guidelines.png) in the toolbar, and then click **Add Vertical Barrier** or **Add Horizontal Barrier**.
2. In the **Component Tree** window, select the views you want inside the barrier and drag them into the barrier component.
3. Select the barrier from the **Component Tree** , open the **Attributes** ![](https://developer.android.com/static/studio/images/buttons/window-properties.png) window, and then set **barrierDirection**.

Now you can create a constraint from another view to the barrier.

You can also constrain views that are *inside* the barrier to the
barrier. This way, you can align all the views in the barrier to each other,
even if you don't know which view is the longest or tallest.

You can also include a guideline inside a barrier to ensure a "minimum"
position for the barrier.  
![](https://developer.android.com/static/training/constraint-layout/images/barrier-constraint_2x.png)

**Figure 13.** View C is constrained to a barrier,
which moves based on the position and size of both view A and view B.

## Adjust the constraint bias

When you add a constraint to both sides of a view, and the view size for the
same dimension is either "fixed" or "wrap content", the view becomes centered
between the two constraints with a bias of 50% by default. You can adjust the
bias by dragging the bias slider in the **Attributes** window or by dragging
the view, as shown in video 3.

If you instead want the view to stretch its size to meet the constraints,
[switch the size](https://developer.android.com/develop/ui/views/layout/constraint-layout#adjust-the-view-size) to "match constraints."  

**Video 3.** Adjusting the constraint bias.

## Adjust the view size

![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-editor-attributes-2x.png)

**Figure 14.** When selecting a view, the
**Attributes** window includes controls for
1 size ratio,
2 deleting constraints,
3 height or width mode,
4 margins, and
5 constraint bias. You can also highlight
individual constraints in the Layout Editor by clicking them in the
6 constraint list.

You can use the corner handles to resize a view, but this hardcodes the
size---the view doesn't resize for different content or screen sizes. To
select a different sizing mode, click a view and open the **Attributes**
![](https://developer.android.com/static/studio/images/buttons/window-properties.png)
window on the right side of the editor.

Near the top of the **Attributes** window is the view inspector, which
includes controls for several layout attributes, as shown in figure 14. This is
available only for views in a constraint layout.

You can change the way the height and width are calculated by clicking the
symbols indicated with callout 3 in figure 14.
These symbols represent the size mode as follows. Click the symbol to toggle
between these settings:

- ![](https://developer.android.com/static/studio/images/buttons/layout-width-fixed.png) **Fixed**: specify a specific dimension in the following text box or by resizing the view in the editor.
- ![](https://developer.android.com/static/studio/images/buttons/layout-width-wrap.png) **Wrap Content**: the view expands only as much as needed to fit its contents.
  - **layout_constrainedWidth**
  - Set this to `true` to let the horizontal dimension change to respect constraints. By default, a widget set to `WRAP_CONTENT` isn't limited by constraints.
- ![](https://developer.android.com/static/studio/images/buttons/layout-width-match.png) **Match Constraints** : the view expands as much as possible to meet the constraints on each side, after accounting for the view's margins. However, you can modify that behavior with the following attributes and values. These attributes take effect only when you set the view width to "match constraints":
  - **layout_constraintWidth_min**

    This takes a `dp` dimension for the view's minimum width.
  - **layout_constraintWidth_max**

    This takes a `dp` dimension for the view's maximum width.

  <br />

  However, if the given dimension has only one constraint, then the view
  expands to fit its contents. Using this mode on either the height or width also
  lets you [set a size ratio](https://developer.android.com/develop/ui/views/layout/constraint-layout#set-size-as-a-ratio).

| **Note** : You can't use `match_parent` for any view in a `ConstraintLayout`. Instead, use "match constraints" (`0dp`).
|
| <br />
|
### Set size as a ratio

![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-ratio-2x.png)

**Figure 15.** The view is set to a 16:9 aspect with
the width based on a ratio of the height.

You can set the view size to a ratio, such as 16:9, if at least one of the
view dimensions is set to "match constraints" (`0dp`). To enable the
ratio, click **Toggle Aspect Ratio Constraint** (callout
1 in figure 14) and enter the
<var translate="no">width</var>:<var translate="no">height</var> ratio in the input that appears.

If both the width and height are set to "match constraints," you can click
**Toggle Aspect Ratio Constraint** to select which dimension is based on a
ratio of the other. The view inspector indicates which dimension is set as a
ratio by connecting the corresponding edges with a solid line.

For example, if you set both sides to "match constraints," click **Toggle
Aspect Ratio Constraint** twice to set the width to be a ratio of the height.
The entire size is dictated by the height of the view, which can be defined in
any way, as shown in figure 15.

## Adjust the view margins

To make your views evenly spaced, click **Margin**
![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-margin-icon-2x.png)
in the toolbar to select the default margin for each view that you add to the
layout. Any change you make to the default margin applies only to the views you
add from then on.

You can control the margin for each view in the **Attributes** window by
clicking the number on the line that represents each constraint. In figure 14,
callout 4 shows the bottom margin is set to
16dp.

![](https://developer.android.com/static/images/training/constraint-layout/constraint-layout-margin-2x.png)

**Figure 16.** The toolbar's **Margin**
button.

<br />

All margins offered by the tool are factors of 8dp to help your views align
to Material Design's 8dp square grid recommendations.

## Control linear groups with a chain

![](https://developer.android.com/static/training/constraint-layout/images/constraint-chain_2x.png)

**Figure 17.** A horizontal chain with
two views.

A chain is a group of views that are linked to each other with bi-directional
position constraints. The views within a chain can be distributed either
vertically or horizontally.  
![](https://developer.android.com/static/training/constraint-layout/images/constraint-chain-styles_2x.png)

**Figure 18.** Examples of each chain
style.

Chains can be styled in one of the following ways:

1. **Spread:** the views are evenly distributed after margins are accounted for. This is the default.
2. **Spread inside:** the first and last views are affixed to the constraints on each end of the chain, and the rest are evenly distributed.
3. **Weighted:** when the chain is set to **spread** or **spread inside** , you can fill the remaining space by setting one or more views to "match constraints" (`0dp`). By default, the space is evenly distributed between each view that's set to "match constraints," but you can assign a weight of importance to each view using the `layout_constraintHorizontal_weight` and `layout_constraintVertical_weight` attributes. This works the same way as `layout_weight` in a [linear layout](https://developer.android.com/guide/topics/ui/layout/linear): the view with the highest weight value gets the most space, and views that have the same weight get the same amount of space.
4. **Packed:** the views are packed together after margins are accounted for. You can adjust the whole chain's bias---left or right, or up or down---by changing the chain's "head" view bias.

The chain's "head" view---the leftmost view in a horizontal chain
(in a left-to-right layout) and the
top-most view in a vertical chain---defines the chain's style in XML.
However, you can toggle between **spread** , **spread inside** , and
**packed** by selecting any view in the chain and clicking the chain button
![](https://developer.android.com/static/studio/images/buttons/layout-editor-action-chain.png)
that appears below the view.

To create a chain, do the following, as shown in video 4:

1. Select all the views to be included in the chain.
2. Right-click one of the views.
3. Select **Chains**.
4. Select either **Center Horizontally** or **Center Vertically**.

**Video 4.** Creating a horizontal chain.

Here are a few things to consider when using chains:

- A view can be a part of both a horizontal and a vertical chain, so you can build flexible grid layouts.
- A chain works properly only if each end of the chain is constrained to another object on the same axis, as shown in figure 14.
- Although the orientation of a chain is vertical or horizontal, using one doesn't align the views in that direction. To achieve the proper position for each view in the chain, include other constraints, such as [alignment constraints](https://developer.android.com/develop/ui/views/layout/constraint-layout#alignment).

## Automatically create constraints

Instead of adding constraints to every view as you place them in the layout,
you can move each view into the positions you want in the Layout Editor and
then click **Infer Constraints**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-infer.png)
to automatically create constraints.

**Infer Constraints** scans the layout to determine the most effective set
of constraints for all views. It constrains the views to their current positions
while providing flexibility. You might need to make adjustments to make the
layout respond as you intend for different screen sizes and orientations.

**Autoconnect to Parent** is a separate feature that you can enable. When
it's enabled and you add child views to a parent, this feature automatically
creates two or more constraints for each view as you add them to the
layout---but only when it's appropriate to constrain the view to the parent
layout. Autoconnect doesn't create constraints to other views in the layout.

Autoconnect is disabled by default. Enable it by clicking **Enable
Autoconnection to Parent**
![](https://developer.android.com/static/studio/images/buttons/layout-editor-autoconnect-on.png)
in the Layout Editor toolbar.

## Keyframe animations

Within a `ConstraintLayout`, you can animate changes to the size
and position of elements by using
[ConstraintSet](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintSet)
and
[TransitionManager](https://developer.android.com/reference/android/transition/TransitionManager).

A `ConstraintSet` is a lightweight object that represents the
constraints, margins, and padding of all child elements within a
`ConstraintLayout`. When you apply a `ConstraintSet` to a
displayed `ConstraintLayout`, the layout updates the constraints of
all its children.

To build an animation using `ConstraintSet`, specify two layout
files that act as start and end keyframes for the animation. You can then load
a `ConstraintSet` from the second keyframe file and apply it to the
displayed `ConstraintLayout`.
| **Note:** `ConstraintSet` animations animate only the size and position of child elements. They don't animate other attributes, such as color.

The following code example shows how to animate moving a single button to the
bottom of the screen.  

    // MainActivity.kt

    fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.keyframe_one)
        constraintLayout = findViewById(R.id.constraint_layout) // member variable
    }

    fun animateToKeyframeTwo() {
        val constraintSet = ConstraintSet()
        constraintSet.load(this, R.layout.keyframe_two)
        TransitionManager.beginDelayedTransition()
        constraintSet.applyTo(constraintLayout)
    }

```xml
// layout/keyframe1.xml
// Keyframe 1 contains the starting position for all elements in the animation
// as well as final colors and text sizes.

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:id="@+id/button2"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Button"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```  

```xml
// layout/keyframe2.xml
// Keyframe 2 contains another ConstraintLayout with the final positions.

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:id="@+id/button2"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:text="Button"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintBottom_toBottomOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```
| **Note:** With Android Studio 3.6 and higher, the [view binding](https://developer.android.com/topic/libraries/view-binding) feature can replace `findViewById()` calls. It also provides compile-time type safety for code that interacts with views. Consider using view binding instead of `findViewById()`.

## Additional resources

`ConstraintLayout` is used in the
[Sunflower](https://github.com/android/sunflower)
demo app.