---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/navigation
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/navigation
source: md.txt
---

# Navigation

Screen gestures are a primary means of navigation in Wear OS apps. Users navigate by scrolling, swiping, and tapping the screen. For more information about implementing swipe to dismiss using Compose for Wear OS, see[Swipe to dismiss](https://developer.android.com/training/wearables/compose/swipe-to-dismiss).

## Swipe to close

Instead of back buttons, Wear OS devices use left-to-right swipe gestures to close the current view and go back to the previous view.

The left-to-right swipe is the primary way to close an app. Keep all navigation not intended to close the app to a vertical axis and avoid horizontal carousels when designing for Wear OS.

If your app requires a pannable view, like Google Maps, use an edge-drag threshold on the left screen edge to limit the gesture to swipes that start within the edge threshold.

Use[SwipeDismissFrameLayout](https://developer.android.com/reference/androidx/wear/widget/SwipeDismissFrameLayout)to implement the swipe to close behavior.