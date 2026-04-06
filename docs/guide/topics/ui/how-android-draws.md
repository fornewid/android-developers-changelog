---
title: https://developer.android.com/guide/topics/ui/how-android-draws
url: https://developer.android.com/guide/topics/ui/how-android-draws
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn about Compose phases. [Compose phases →](https://developer.android.com/develop/ui/compose/phases) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The Android framework asks an
`https://developer.android.com/reference/android/app/Activity` to draw its layout when the
`Activity` receives focus. The Android framework handles the procedure for drawing, but the
`Activity` must provide the root node of its layout hierarchy.

The Android framework draws the root node of the layout and measures and draws the layout tree. It
draws by walking the tree and rendering each
`https://developer.android.com/reference/android/view/View` that intersects the invalid region.
Each `https://developer.android.com/reference/android/view/ViewGroup` is responsible for
requesting that each of its children be drawn, using the
`https://developer.android.com/reference/android/view/View#draw(android.graphics.Canvas)`
method, and each `View` is responsible for drawing itself. Because the tree is traversed
pre-order, the framework draws parents before---in other words, *behind*---their
children, and it draws siblings in the order they appear in the tree.
| **Note:** The framework doesn't draw `View` objects that aren't in a valid region. It also takes care of drawing the `View` background for you. You can force a `View` to draw by calling `https://developer.android.com/reference/android/view/View#invalidate()`.

The Android framework draws the layout in a two-pass process: a measure pass and a layout pass. The
framework performs the measure pass in
`https://developer.android.com/reference/android/view/View#measure(int, int)` and
performs a top-down traversal of the `View` tree. Each `View` pushes dimension
specifications down the tree during the recursion. At the end of the measure pass, every
`View` stores its measurements. The framework performs the second pass in
`https://developer.android.com/reference/android/view/View#layout(int, int, int, int)`
and is also top-down. During this pass, each parent is responsible for positioning all of its children
using the sizes computed in the measure pass.

The two passes of the layout process are described in more detail in the following sections.

## Initiate a measure pass

When a `View` object's
`https://developer.android.com/reference/android/view/View#measure(int, int)` method
returns, set its
`https://developer.android.com/reference/android/view/View#getMeasuredWidth()`
and
`https://developer.android.com/reference/android/view/View#getMeasuredHeight()`
values, along with those for all of the `View` object's descendants. A `View`
object's measured width and measured height values must respect the constraints imposed by the
`View` object's parents. This helps ensure that at the end of the measure pass, all parents
accept all of their children's measurements.

A parent `View` might call `measure()` more than once on its children. For
example, the parent might measure the children once with unspecified dimensions to determine their
preferred sizes. If the sum of the children's unconstrained sizes is too big or too small, the parent
might call `measure()` again with values that constrain the children's sizes.

The measure pass uses two classes to communicate dimensions. The
`https://developer.android.com/reference/android/view/ViewGroup.LayoutParams`
class is how `View` objects communicate their preferred sizes and positions. The base
`ViewGroup.LayoutParams` class describes the preferred width and height of the
`View`. For each dimension, it can specify one of the following:

- An exact dimension.
- `https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#MATCH_PARENT`, meaning the preferred size for the `View` is the size of its parent, minus padding.
- `https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#WRAP_CONTENT`, meaning the preferred size for the `View` is just big enough to enclose its content, plus padding.

There are subclasses of `ViewGroup.LayoutParams` for different subclasses of
`ViewGroup`. For example,
`https://developer.android.com/reference/android/widget/RelativeLayout` has its own
subclass of `ViewGroup.LayoutParams` that includes the ability to center child
`View` objects horizontally and vertically.

`https://developer.android.com/reference/android/view/View.MeasureSpec` objects are
used to push requirements down the tree from parent to child. A `MeasureSpec` can be in
one of three modes:

- `https://developer.android.com/reference/android/view/View.MeasureSpec#UNSPECIFIED`: the parent uses this to determine the target dimension of a child `View`. For example, a `https://developer.android.com/reference/android/widget/LinearLayout` might call `measure()` on its child with the height set to `UNSPECIFIED` and a width of `https://developer.android.com/reference/android/view/View.MeasureSpec#EXACTLY` 240 to find out how tall the child `View` wants to be, given a width of 240 pixels.
- `https://developer.android.com/reference/android/view/View.MeasureSpec#EXACTLY`: the parent uses this to impose an exact size on the child. The child must use this size and guarantee that all of its descendants fit within this size.
- `https://developer.android.com/reference/android/view/View.MeasureSpec#AT_MOST`: the parent uses this to impose a maximum size on the child. The child must guarantee that it and all of its descendants fit within this size.

## Initiate a layout pass

To initiate a layout, call
`https://developer.android.com/reference/android/view/View#requestLayout()`. This
method is typically called by a `View` on itself when it believes it can no longer fit
within its bounds.

## Implement a custom measurement and layout logic

If you want to implement a custom measurement or layout logic, override the methods where the logic
is implemented:
`https://developer.android.com/reference/android/view/View#onMeasure(int,%20int)`
and
`https://developer.android.com/reference/android/view/View#onLayout(boolean,%20int,%20int,%20int,%20int)`.
These methods are called by `measure(int, int)` and
`layout(int, int, int, int)`, respectively. Don't try to override the
`measure(int, int)` or `layout(int, int)` methods---both of these methods
are `final`, so they can't be overridden.

The following example shows how to do this in the
[\`SplitLayout\`](https://github.com/android/user-interface-samples/blob/main/WindowManager/app/src/main/java/com/example/windowmanagersample/SplitLayout.kt)
class from the
[WindowManager](https://github.com/android/user-interface-samples/tree/main/WindowManager)
sample app. If the `SplitLayout` has two or more child views, and the display has a fold,
then it positions the two child views on either side of the fold. The following example shows a use
case for overriding the measurement and layout, but for production, use
`https://developer.android.com/reference/androidx/slidingpanelayout/widget/SlidingPaneLayout`
if you want this behavior.

### Kotlin

```kotlin
/**
 * An example of split-layout for two views, separated by a display
 * feature that goes across the window. When both start and end views are
 * added, it checks whether there are display features that separate the area
 * in two---such as a fold or hinge---and places them side-by-side or
 * top-bottom.
 */
class SplitLayout : FrameLayout {
   private var windowLayoutInfo: WindowLayoutInfo? = null
   private var startViewId = 0
   private var endViewId = 0

   private var lastWidthMeasureSpec: Int = 0
   private var lastHeightMeasureSpec: Int = 0

   ...

   fun updateWindowLayout(windowLayoutInfo: WindowLayoutInfo) {
      this.windowLayoutInfo = windowLayoutInfo
      requestLayout()
   }

   override fun onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
      val startView = findStartView()
      val endView = findEndView()
      val splitPositions = splitViewPositions(startView, endView)

      if (startView != null && endView != null && splitPositions != null) {
            val startPosition = splitPositions[0]
            val startWidthSpec = MeasureSpec.makeMeasureSpec(startPosition.width(), EXACTLY)
            val startHeightSpec = MeasureSpec.makeMeasureSpec(startPosition.height(), EXACTLY)
            startView.measure(startWidthSpec, startHeightSpec)
            startView.layout(
               startPosition.left, startPosition.top, startPosition.right,
               startPosition.bottom
            )

            val endPosition = splitPositions[1]
            val endWidthSpec = MeasureSpec.makeMeasureSpec(endPosition.width(), EXACTLY)
            val endHeightSpec = MeasureSpec.makeMeasureSpec(endPosition.height(), EXACTLY)
            endView.measure(endWidthSpec, endHeightSpec)
            endView.layout(
               endPosition.left, endPosition.top, endPosition.right,
               endPosition.bottom
            )
      } else {
            super.onLayout(changed, left, top, right, bottom)
      }
   }

   /**
   * Gets the position of the split for this view.
   * @return A rect that defines of split, or {@code null} if there is no split.
   */
   private fun splitViewPositions(startView: View?, endView: View?): Array? {
      if (windowLayoutInfo == null || startView == null || endView == null) {
            return null
      }

      // Calculate the area for view's content with padding.
      val paddedWidth = width - paddingLeft - paddingRight
      val paddedHeight = height - paddingTop - paddingBottom

      windowLayoutInfo?.displayFeatures
            ?.firstOrNull { feature -> isValidFoldFeature(feature) }
            ?.let { feature ->
               getFeaturePositionInViewRect(feature, this)?.let {
                  if (feature.bounds.left == 0) { // Horizontal layout.
                        val topRect = Rect(
                           paddingLeft, paddingTop,
                           paddingLeft + paddedWidth, it.top
                        )
                        val bottomRect = Rect(
                           paddingLeft, it.bottom,
                           paddingLeft + paddedWidth, paddingTop + paddedHeight
                        )

                        if (measureAndCheckMinSize(topRect, startView) &&
                           measureAndCheckMinSize(bottomRect, endView)
                        ) {
                           return arrayOf(topRect, bottomRect)
                        }
                  } else if (feature.bounds.top == 0) { // Vertical layout.
                        val leftRect = Rect(
                           paddingLeft, paddingTop,
                           it.left, paddingTop + paddedHeight
                        )
                        val rightRect = Rect(
                           it.right, paddingTop,
                           paddingLeft + paddedWidth, paddingTop + paddedHeight
                        )

                        if (measureAndCheckMinSize(leftRect, startView) &&
                           measureAndCheckMinSize(rightRect, endView)
                        ) {
                           return arrayOf(leftRect, rightRect)
                        }
                  }
               }
            }

      // You previously tried to fit the children and measure them. Since they
      // don't fit, measure again to update the stored values.
      measure(lastWidthMeasureSpec, lastHeightMeasureSpec)
      return null
   }

   override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
      super.onMeasure(widthMeasureSpec, heightMeasureSpec)
      lastWidthMeasureSpec = widthMeasureSpec
      lastHeightMeasureSpec = heightMeasureSpec
   }

   /**
   * Measures a child view and sees if it fits in the provided rect.
   * This method calls [View.measure] on the child view, which updates its
   * stored values for measured width and height. If the view ends up with
   * different values, measure again.
   */
   private fun measureAndCheckMinSize(rect: Rect, childView: View): Boolean {
      val widthSpec = MeasureSpec.makeMeasureSpec(rect.width(), AT_MOST)
      val heightSpec = MeasureSpec.makeMeasureSpec(rect.height(), AT_MOST)
      childView.measure(widthSpec, heightSpec)
      return childView.measuredWidthAndState and MEASURED_STATE_TOO_SMALL == 0 &&
               childView.measuredHeightAndState and MEASURED_STATE_TOO_SMALL == 0
   }

   private fun isValidFoldFeature(displayFeature: DisplayFeature) =
      (displayFeature as? FoldingFeature)?.let { feature ->
            getFeaturePositionInViewRect(feature, this) != null
      } ?: false
}
```

### Java

```java
/**
* An example of split-layout for two views, separated by a display feature
* that goes across the window. When both start and end views are added, it checks
* whether there are display features that separate the area in two---such as
* fold or hinge---and places them side-by-side or top-bottom.
*/
public class SplitLayout extends FrameLayout {
   @Nullable
   private WindowLayoutInfo windowLayoutInfo = null;
   private int startViewId = 0;
   private int endViewId = 0;

   private int lastWidthMeasureSpec = 0;
   private int lastHeightMeasureSpec = 0;

   ...

   void updateWindowLayout(WindowLayoutInfo windowLayoutInfo) {
      this.windowLayoutInfo = windowLayoutInfo;
      requestLayout();
   }

   @Override
   protected void onLayout(boolean changed, int left, int top, int right, int bottom) {
      @Nullable
      View startView = findStartView();
      @Nullable
      View endView = findEndView();
      @Nullable
      List splitPositions = splitViewPositions(startView, endView);

      if (startView != null && endView != null && splitPositions != null) {
            Rect startPosition = splitPositions.get(0);
            int startWidthSpec = MeasureSpec.makeMeasureSpec(startPosition.width(), EXACTLY);
            int startHeightSpec = MeasureSpec.makeMeasureSpec(startPosition.height(), EXACTLY);
            startView.measure(startWidthSpec, startHeightSpec);
            startView.layout(
                  startPosition.left,
                  startPosition.top,
                  startPosition.right,
                  startPosition.bottom
            );

            Rect endPosition = splitPositions.get(1);
            int endWidthSpec = MeasureSpec.makeMeasureSpec(endPosition.width(), EXACTLY);
            int endHeightSpec = MeasureSpec.makeMeasureSpec(endPosition.height(), EXACTLY);
            startView.measure(endWidthSpec, endHeightSpec);
            startView.layout(
                  endPosition.left,
                  endPosition.top,
                  endPosition.right,
                  endPosition.bottom
            );
      } else {
            super.onLayout(changed, left, top, right, bottom);
      }
   }

   /**
   * Gets the position of the split for this view.
   * @return A rect that defines of split, or {@code null} if there is no split.
   */
   @Nullable
   private List splitViewPositions(@Nullable View startView, @Nullable View endView) {
      if (windowLayoutInfo == null || startView == null || endView == null) {
            return null;
      }

      int paddedWidth = getWidth() - getPaddingLeft() - getPaddingRight();
      int paddedHeight = getHeight() - getPaddingTop() - getPaddingBottom();

      List displayFeatures = windowLayoutInfo.getDisplayFeatures();

      @Nullable
      DisplayFeature feature = displayFeatures
               .stream()
               .filter(item ->
                  isValidFoldFeature(item)
               )
               .findFirst()
               .orElse(null);

      if (feature != null) {
            Rect position = SampleToolsKt.getFeaturePositionInViewRect(feature, this, true);
            Rect featureBounds = feature.getBounds();
            if (featureBounds.left == 0) { // Horizontal layout.
               Rect topRect = new Rect(
                        getPaddingLeft(),
                        getPaddingTop(),
                        getPaddingLeft() + paddedWidth,
                        position.top
               );
               Rect bottomRect = new Rect(
                        getPaddingLeft(),
                        position.bottom,
                        getPaddingLeft() + paddedWidth,
                        getPaddingTop() + paddedHeight
               );
               if (measureAndCheckMinSize(topRect, startView) &&
                        measureAndCheckMinSize(bottomRect, endView)) {
                  ArrayList rects = new ArrayList();
                  rects.add(topRect);
                  rects.add(bottomRect);
                  return rects;
               }
            } else if (featureBounds.top == 0) { // Vertical layout.
               Rect leftRect = new Rect(
                        getPaddingLeft(),
                        getPaddingTop(),
                        position.left,
                        getPaddingTop() + paddedHeight
               );
               Rect rightRect = new Rect(
                        position.right,
                        getPaddingTop(),
                        getPaddingLeft() + paddedWidth,
                        getPaddingTop() + paddedHeight
               );
               if (measureAndCheckMinSize(leftRect, startView) &&
                        measureAndCheckMinSize(rightRect, endView)) {
                  ArrayList rects = new ArrayList();
                  rects.add(leftRect);
                  rects.add(rightRect);
                  return rects;
               }
            }
      }

      // You previously tried to fit the children and measure them. Since
      // they don't fit, measure again to update the stored values.
      measure(lastWidthMeasureSpec, lastHeightMeasureSpec);
      return null;
   }

   @Override
   protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
      super.onMeasure(widthMeasureSpec, heightMeasureSpec);
      lastWidthMeasureSpec = widthMeasureSpec;
      lastHeightMeasureSpec = heightMeasureSpec;
   }

   /**
   * Measures a child view and sees if it fits in the provided rect.
   * This method calls [View.measure] on the child view, which updates
   * its stored values for measured width and height. If the view ends up with
   * different values, measure again.
   */
   private boolean measureAndCheckMinSize(Rect rect, View childView) {
      int widthSpec = MeasureSpec.makeMeasureSpec(rect.width(), AT_MOST);
      int heightSpec = MeasureSpec.makeMeasureSpec(rect.height(), AT_MOST);
      childView.measure(widthSpec, heightSpec);
      return (childView.getMeasuredWidthAndState() & MEASURED_STATE_TOO_SMALL) == 0 &&
               (childView.getMeasuredHeightAndState() & MEASURED_STATE_TOO_SMALL) == 0;
   }

   private boolean isValidFoldFeature(DisplayFeature displayFeature) {
      if (displayFeature instanceof FoldingFeature) {
            return SampleToolsKt.getFeaturePositionInViewRect(displayFeature, this, true) != null;
      } else {
            return false;
      }
   }
}
```