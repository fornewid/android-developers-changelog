---
title: https://developer.android.com/develop/ui/views/layout/insets/rounded-corners
url: https://developer.android.com/develop/ui/views/layout/insets/rounded-corners
source: md.txt
---

Starting in Android 12 (API level 31), you can use
[`RoundedCorner`](https://developer.android.com/reference/android/view/RoundedCorner) and
[`WindowInsets.getRoundedCorner(int
position)`](https://developer.android.com/reference/android/view/WindowInsets#getRoundedCorner(int)) to get
the radius and center point for rounded corners of the device screen. These APIs
keep your app's UI elements from being truncated on screens with rounded
corners. The framework provides the
[`getPrivacyIndicatorBounds()`](https://developer.android.com/reference/android/view/WindowInsets#getPrivacyIndicatorBounds())
API, which returns the bounded rectangle of any visible [microphone and camera
indicators](https://developer.android.com/about/versions/12/behavior-changes-all#mic-camera-indicators).

When implemented in your app, these APIs have no effect on devices with
non-rounded screens.
![Image showing a rounded corners with radii and a center point](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/rounded-corners-radius.png) **Figure 1.** Rounded corners with radii and a center point.

To implement this feature, get the `RoundedCorner` info using
`WindowInsets.getRoundedCorner(int position)` relative to the bounds of the
application. If the app doesn't take up the whole screen, the API applies the
rounded corner by basing the center point of the rounded corner on the window
bounds of the app.

The following code snippet shows how an app can avoid having its UI truncated by
setting a margin of the view based on the info from `RoundedCorner`. In this
case, it is the top-right rounded corner.

### Kotlin

```kotlin
// Get the top-right rounded corner from WindowInsets.
val insets = rootWindowInsets
val topRight = insets.getRoundedCorner(RoundedCorner.POSITION_TOP_RIGHT) ?: return

// Get the location of the close button in window coordinates.
val location = IntArray(2)
closeButton!!.getLocationInWindow(location)
val buttonRightInWindow = location[0] + closeButton.width
val buttonTopInWindow = location[1]

// Find the point on the quarter circle with a 45-degree angle.
val offset = (topRight.radius * Math.sin(Math.toRadians(45.0))).toInt()
val topBoundary = topRight.center.y - offset
val rightBoundary = topRight.center.x + offset

// Check whether the close button exceeds the boundary.
if (buttonRightInWindow < rightBoundary << buttonTopInWindow > topBoundary) {
   return
}

// Set the margin to avoid truncating.
val parentLocation = IntArray(2)
getLocationInWindow(parentLocation)
val lp = closeButton.layoutParams as FrameLayout.LayoutParams
lp.rightMargin = Math.max(buttonRightInWindow - rightBoundary, 0)
lp.topMargin = Math.max(topBoundary - buttonTopInWindow, 0)
closeButton.layoutParams = lp
```

### Java

```java
// Get the top-right rounded corner from WindowInsets.
final WindowInsets insets = getRootWindowInsets();
final RoundedCorner topRight = insets.getRoundedCorner(POSITION_TOP_RIGHT);
if (topRight == null) {
   return;
}

// Get the location of the close button in window coordinates.
int [] location = new int[2];
closeButton.getLocationInWindow(location);
final int buttonRightInWindow = location[0] + closeButton.getWidth();
final int buttonTopInWindow = location[1];

// Find the point on the quarter circle with a 45-degree angle.
final int offset = (int) (topRight.getRadius() * Math.sin(Math.toRadians(45)));
final int topBoundary = topRight.getCenter().y - offset;
final int rightBoundary = topRight.getCenter().x + offset;

// Check whether the close button exceeds the boundary.
if (buttonRightInWindow < rightBoundary << buttonTopInWindow > topBoundary) {
   return;
}

// Set the margin to avoid truncating.
int [] parentLocation = new int[2];
getLocationInWindow(parentLocation);
FrameLayout.LayoutParams lp = (FrameLayout.LayoutParams) closeButton.getLayoutParams();
lp.rightMargin = Math.max(buttonRightInWindow - rightBoundary, 0);
lp.topMargin = Math.max(topBoundary - buttonTopInWindow, 0);
closeButton.setLayoutParams(lp);
```

## Be careful of clipping

If your UI fills the entire display, round corners can cause issues with content
clipping. For example, figure 2 shows an icon in the corner of the display with
the layout being drawn behind the system bars:
![An icon being clipped by rounded corners](https://developer.android.com/static/develop/ui/views/theming/images/rounded-corners-none.png) **Figure 2.** An icon being clipped by rounded corners.

You can avoid this by checking for rounded corners and applying padding to keep
your app's content out of the device's corners, as shown in the following
example:

### Kotlin

```kotlin
class InsetsLayout(context: Context, attrs: AttributeSet) : FrameLayout(context, attrs) {

    override fun onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
        val insets = rootWindowInsets

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S && insets != null) {
            applyRoundedCornerPadding(insets)
        }
        super.onLayout(changed, left, top, right, bottom)

    }

    @RequiresApi(Build.VERSION_CODES.S)
    private fun applyRoundedCornerPadding(insets: WindowInsets) {
        val topLeft = insets.getRoundedCorner(RoundedCorner.POSITION_TOP_LEFT)
        val topRight = insets.getRoundedCorner(RoundedCorner.POSITION_TOP_RIGHT)
        val bottomLeft = insets.getRoundedCorner(RoundedCorner.POSITION_BOTTOM_LEFT)
        val bottomRight = insets.getRoundedCorner(RoundedCorner.POSITION_BOTTOM_RIGHT)

        val leftRadius = max(topLeft?.radius ?: 0, bottomLeft?.radius ?: 0)
        val topRadius = max(topLeft?.radius ?: 0, topRight?.radius ?: 0)
        val rightRadius = max(topRight?.radius ?: 0, bottomRight?.radius ?: 0)
        val bottomRadius = max(bottomLeft?.radius ?: 0, bottomRight?.radius ?: 0)

        val windowManager = context.getSystemService(Context.WINDOW_SERVICE) as WindowManager
        val windowBounds = windowManager.currentWindowMetrics.bounds
        val safeArea = Rect(
            windowBounds.left + leftRadius,
            windowBounds.top + topRadius,
            windowBounds.right - rightRadius,
            windowBounds.bottom - bottomRadius
        )

        val location = intArrayOf(0, 0)
        getLocationInWindow(location)

        val leftMargin = location[0] - windowBounds.left
        val topMargin = location[1] - windowBounds.top
        val rightMargin = windowBounds.right - right - location[0]
        val bottomMargin = windowBounds.bottom - bottom - location[1]

        val layoutBounds = Rect(
            location[0] + paddingLeft,
            location[1] + paddingTop,
            location[0] + width - paddingRight,
            location[1] + height - paddingBottom
        )

        if (layoutBounds != safeArea && layoutBounds.contains(safeArea)) {
            setPadding(
                calculatePadding(leftRadius, leftMargin, paddingLeft),
                calculatePadding(topRadius, topMargin, paddingTop),
                calculatePadding(rightRadius, rightMargin, paddingRight),
                calculatePadding(bottomRadius, bottomMargin, paddingBottom)
            )
        }
    }

    private fun calculatePadding(radius1: Int?, radius2: Int?, margin: Int, padding: Int): Int =
        (max(radius1 ?: 0, radius2 ?: 0) - margin - padding).coerceAtLeast(0)
}
```

### Java

```java
public class InsetsLayout extends FrameLayout {
    public InsetsLayout(@NonNull Context context) {
        super(context);
    }

    public InsetsLayout(@NonNull Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    protected void onLayout(boolean changed, int left, int top, int right, int bottom) {
        WindowInsets insets = getRootWindowInsets();
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S && insets != null) {
            applyRoundedCornerPadding(insets);
        }
        super.onLayout(changed, left, top, right, bottom);
    }

    @RequiresApi(Build.VERSION_CODES.S)
    private void applyRoundedCornerPadding(WindowInsets insets) {
        RoundedCorner topLeft = insets.getRoundedCorner(RoundedCorner.POSITION_TOP_LEFT);
        RoundedCorner topRight = insets.getRoundedCorner(RoundedCorner.POSITION_TOP_RIGHT);
        RoundedCorner bottomLeft = insets.getRoundedCorner(RoundedCorner.POSITION_BOTTOM_LEFT);
        RoundedCorner bottomRight = insets.getRoundedCorner(RoundedCorner.POSITION_BOTTOM_RIGHT);
        int radiusTopLeft = 0;
        int radiusTopRight = 0;
        int radiusBottomLeft = 0;
        int radiusBottomRight = 0;
        if (topLeft != null) radiusTopLeft = topLeft.getRadius();
        if (topRight != null) radiusTopRight = topRight.getRadius();
        if (bottomLeft != null) radiusBottomLeft = bottomLeft.getRadius();
        if (bottomRight != null) radiusBottomRight = bottomRight.getRadius();

        int leftRadius = Math.max(radiusTopLeft, radiusBottomLeft);
        int topRadius = Math.max(radiusTopLeft, radiusTopRight);
        int rightRadius = Math.max(radiusTopRight, radiusBottomRight);
        int bottomRadius = Math.max(radiusBottomLeft, radiusBottomRight);

        WindowManager windowManager =
                (WindowManager) getContext().getSystemService(Context.WINDOW_SERVICE);
        Rect windowBounds = windowManager.getCurrentWindowMetrics().getBounds();
        Rect safeArea = new Rect(
                windowBounds.left + leftRadius,
                windowBounds.top + topRadius,
                windowBounds.right - rightRadius,
                windowBounds.bottom - bottomRadius
        );
        int[] location = {0, 0};
        getLocationInWindow(location);

        int leftMargin = location[0] - windowBounds.left;
        int topMargin = location[1] - windowBounds.top;
        int rightMargin = windowBounds.right - getRight() - location[0];
        int bottomMargin = windowBounds.bottom - getBottom() - location[1];

        Rect layoutBounds = new Rect(
                location[0] + getPaddingLeft(),
                location[1] + getPaddingTop(),
                location[0] + getWidth() - getPaddingRight(),
                location[1] + getHeight() - getPaddingBottom()
        );

        if (!layoutBounds.equals(safeArea) && layoutBounds.contains(safeArea)) {
            setPadding(
                    calculatePadding(radiusTopLeft, radiusBottomLeft,
                                         leftMargin, getPaddingLeft()),
                    calculatePadding(radiusTopLeft, radiusTopRight,
                                         topMargin, getPaddingTop()),
                    calculatePadding(radiusTopRight, radiusBottomRight,
                                         rightMargin, getPaddingRight()),
                    calculatePadding(radiusBottomLeft, radiusBottomRight,
                                         bottomMargin, getPaddingBottom())
            );
        }
    }

    private int calculatePadding(int radius1, int radius2, int margin, int padding) {
        return Math.max(Math.max(radius1, radius2) - margin - padding, 0);
    }
}
```

This layout determines whether the UI extends to the area of the rounded corners
and adds padding where it does. Figure 3 has the "Show layout bounds" developer
option enabled to show the padding being applied more clearly:
![An icon with padding applied to move it away from the corner.](https://developer.android.com/static/develop/ui/views/theming/images/rounded-corners-both.png) **Figure 3.** An icon with padding applied to move it away from the corner.

To make this determination, this layout calculates two rectangles: `safeArea` is
the area within the radii of the round corners, and `layoutBounds` is the size
of the layout minus any padding. If `layoutArea` fully contains `safeArea`, then
the children of the layout might be clipped. If this is the case, padding is
added to make sure the layout remains inside `safeArea`.

By checking whether `layoutBounds` fully encloses `safeArea`, you avoid adding
padding when the layout doesn't extend to the edges of the display. Figure 4
shows the layout when it isn't drawn behind the navigation bar. In this case,
the layout doesn't extend down far enough to be within the rounded corners, as
they fit within the area occupied by the navigation bar. No padding is required.
![A layout that doesn't draw behind the system and navigation bars.](https://developer.android.com/static/develop/ui/views/theming/images/rounded-corners-neither.png) **Figure 4.** A layout that doesn't draw behind the system and navigation bars.