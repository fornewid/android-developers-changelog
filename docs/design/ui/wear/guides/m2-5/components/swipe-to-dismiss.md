---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/swipe-to-dismiss
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/swipe-to-dismiss
source: md.txt
---

# Swipe to dismiss

[Swipe to dismiss](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/package-summary#BasicSwipeToDismissBox(androidx.wear.compose.foundation.SwipeToDismissBoxState,androidx.compose.ui.Modifier,kotlin.Any,kotlin.Any,kotlin.Boolean,kotlin.Function2))animation conveys the transition when users navigate to the previous page.

The animation details for swipe to dismiss are similar to the RSB press. Your finger controls the progress of the animation up to 50%.

There is an additional animation on the App View that is linked to the dismiss gesture. The amount of movement shown on the app view is not exactly the same as the distance that the finger needs to move. The app view should never leave the edge of the screen, displaying a squeeze like effect with some resistance.

## Implementation

[`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary#SwipeDismissableNavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState,kotlin.String,kotlin.Function1))from the[navigation library](https://developer.android.com/training/wearables/compose/navigation)provides the swipe-to-dismiss navigation gesture by default.

If you are not using the navigation library, then you can still support this full screen navigation gesture by using[`BasicSwipeToDismissBox`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/package-summary#BasicSwipeToDismissBox(androidx.wear.compose.foundation.SwipeToDismissBoxState,androidx.compose.ui.Modifier,kotlin.Any,kotlin.Any,kotlin.Boolean,kotlin.Function2))directly.

## Design

When designing the swipe to dismiss action, keep the following two principles in mind:

### Edge of the screen

Account for other UI elements that are swipable, such as paginated app views. When swipe to dismiss is possible, reserve 20% of the edge of the screen to trigger that motion.

See this[example from the Compose Material for Wear OS codebase](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:wear/compose/compose-material/samples/src/main/java/androidx/wear/compose/material/samples/SwipeToDismissBoxSample.kt;l=151)for an example of edge-swiping when the content is horizontally scrollable.

### Threshold to go back or stay on app view

If the user has dragged their finger across over 50% of the screen width, the app should trigger the rest of the swipe back animation. If it's less than that, the app should snap back to the full app view.

If the gesture is quick, ignore the 50% threshold rule and swipe back.