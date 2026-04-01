---
title: Navigation  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Navigation Stay organized with collections Save and categorize content based on your preferences.




Screen gestures are a primary means of navigation in Wear OS apps. Users
navigate by scrolling, swiping, and tapping the screen. For more information
about implementing swipe to dismiss using Compose for Wear OS, see
[Swipe to dismiss](/training/wearables/compose/swipe-to-dismiss).

## Swipe to close

Instead of back buttons, Wear OS devices use left-to-right swipe gestures to
close the current view and go back to the previous view.

The left-to-right swipe is the primary way to close an app. Keep all navigation
not intended to close the app to a vertical axis and avoid horizontal carousels
when designing for Wear OS.

If your app requires a pannable view, like Google Maps, use an edge-drag
threshold on the left screen edge to limit the gesture to swipes that start
within the edge threshold.

Use
[SwipeDismissFrameLayout](/reference/androidx/wear/widget/SwipeDismissFrameLayout)
to implement the swipe to close behavior.