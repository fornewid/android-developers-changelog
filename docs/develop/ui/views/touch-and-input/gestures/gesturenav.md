---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/gesturenav
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/gesturenav
source: md.txt
---

Beginning with Android 10 (API level 29), the Android system supports fully
gesture-based navigation. There are two things app developers must do to ensure
their apps are compatible with this feature:

- Extend app content from edge to edge.
- Handle conflicting app gestures.

In addition, Android 13 (API level 33) introduces a
[predictive back gesture](https://developer.android.com/guide/navigation/predictive-back-gesture) for Android
devices such as phones, large screens, and foldables that is part of a multiyear
release. App developers can take steps to ensure that their apps support the
predictive back gesture.

## Provide edge-to-edge app content

To take advantage of the additional screen space made available by the floating
navigation bar, you need to configure certain changes in your app.

See [Display content edge-to-edge in your app](https://developer.android.com/training/gestures/edge-to-edge)
for details.

## Handle conflicting app gestures

The gesture navigation model might conflict with gestures that were previously
used by app developers. You might need to make adjustments to your app's user
interface as a result.

### Conflicts with back gestures

The new system gesture for back is an inward swipe from either the left or the
right edge of the screen. This might interfere with app navigation elements in
those areas. To maintain functionality of elements on the left and right edges
of the screen, opt out of the back gesture selectively by indicating to the
system which regions need to receive touch input. You can do this by passing a
`List<Rect>` to the [`View.setSystemGestureExclusionRects()`](https://developer.android.com/reference/android/view/View#setSystemGestureExclusionRects(java.util.List%3Candroid.graphics.Rect%3E))
API introduced in Android 10. This method is also available in [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat) as of
`androidx.core:core:1.1.0-dev01`.

For example:  

### Kotlin

```kotlin
var exclusionRects = listOf(rect1, rect2, rect3)

fun onLayout(
        changedCanvas: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
  // Update rect bounds and the exclusionRects list
  setSystemGestureExclusionRects(exclusionRects)
}

fun onDraw(canvas: Canvas) {
  // Update rect bounds and the exclusionRects list
  setSystemGestureExclusionRects(exclusionRects)
}
```

### Java

```java
List<Rect> exclusionRects;

public void onLayout(
        boolean changedCanvas, int left, int top, int right, int bottom) {
    // Update rect bounds and the exclusionRects list
    setSystemGestureExclusionRects(exclusionRects);
}

public void onDraw(Canvas canvas) {
    // Update rect bounds and the exclusionRects list
    setSystemGestureExclusionRects(exclusionRects);
}
```
| **Note:** The `DrawerLayout` and `SeekBar` components support automatic opt-out behavior out of the box.

### Conflicts with home or quick-switch gestures

The new system gestures for home and quick switch both involve swipes at the
bottom of the screen in the space previously occupied by the nav bar. Apps
can't opt out of these gestures as they can with the back gesture.

To mitigate this problem, Android 10 introduces the
[`WindowInsets.getMandatorySystemGestureInsets()`](https://developer.android.com/reference/android/view/WindowInsets.Type#mandatorySystemGestures())
API, which informs apps of the touch recognition thresholds.

### Games and other non-View apps

Games and other apps that don't have a view hierarchy often require the user to
swipe near the system gesture areas. In those cases, games can use
[`Window.setSystemGestureExclusionRects()`](https://developer.android.com/reference/android/view/Window#setSystemGestureExclusionRects(java.util.List%3Candroid.graphics.Rect%3E))
to exclude areas that overlap with areas reserved for system gestures. Games
must make sure to only exclude these areas when necessary, such as during
gameplay.

If a game requires the user to swipe near the home gesture area, the app can
request to be laid out in [immersive mode](https://developer.android.com/training/system-ui/immersive#immersive). This disables the system gestures
while the user is interacting with the game, but lets the user re-enable
the system gestures by swiping from the bottom of the screen.

## Update your app to support the predictive back gesture

Android 13 (API level 33) introduces a predictive back gesture for Android
devices such as phones, large screens, and foldables. The predictive back
gesture is part of a multiyear release. When fully implemented, this feature
lets users preview the destination or other result of a back gesture before
they fully complete it, allowing them to decide whether to continue or stay in
the current view.

See
[Add support for the predictive back gesture](https://developer.android.com/guide/navigation/predictive-back-gesture)
for details.

## Additional resources

To learn more about gesture navigation, see the following:

### Blog posts

- [Gesture Navigation: handling visual overlaps (II)](https://medium.com/androiddevelopers/gesture-navigation-handling-visual-overlaps-4aed565c134c)

### Videos

- [Android 10: Gestural navigation](https://www.youtube.com/watch?v=Ljtz7T8R_Hk)
- [Dark theme \& gesture navigation (Google I/O '19)](https://www.youtube.com/watch?v=OCHEjeLC_UY)