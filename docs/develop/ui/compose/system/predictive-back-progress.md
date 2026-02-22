---
title: https://developer.android.com/develop/ui/compose/system/predictive-back-progress
url: https://developer.android.com/develop/ui/compose/system/predictive-back-progress
source: md.txt
---

The [`PredictiveBackHandler`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#PredictiveBackHandler(kotlin.Boolean,kotlin.coroutines.SuspendFunction1)) composable in Jetpack Compose lets you
intercept the back gesture and access its progress. You can react to the user's
back gesture in real-time, creating custom animations or behaviors based on how
far the user swipes.

To use the `PredictiveBackHandler`, ensure you are using
`androidx.activity:activity:1.6.0` or higher.

`PredictiveBackHandler` provides a `Flow<BackEventCompat>` that emits events
representing the progress of the back gesture. Each event contains information
such as:

- `progress`: A float value between 0 and 1 indicating the progress of the back gesture (0 = gesture started, 1 = gesture completed).
- `touchX` and `touchY`: The X and Y coordinates of the touch event.

The following snippet shows basic usage of `PredictiveBackHandler`:


```kotlin
PredictiveBackHandler(true) { progress: Flow<BackEventCompat> ->
    // code for gesture back started
    try {
        progress.collect { backEvent ->
            // code for progress
            boxScale = 1F - (1F * backEvent.progress)
        }
        // code for completion
        boxScale = 0F
    } catch (e: CancellationException) {
        // code for cancellation
        boxScale = 1F
        throw e
    }
}
```

<br />

## Example: Integrate with a navigation drawer

This example demonstrates how to implement a custom in-app animation using `PredictiveBackHandler` to create a smooth interaction with a navigation
drawer in response to back gestures in [JetLagged](https://github.com/android/compose-samples/blob/main/JetLagged/app/src/main/java/com/example/jetlagged/JetLaggedDrawer.kt):
**Figure 5.** Navigation drawer with predictive back support.

In this example, `PredictiveBackHandler` is used to:

- Track the progress of the back gesture.
- Update the `translationX` of the drawer based on the gesture progress.
- Use a `velocityTracker` to smoothly open or close the drawer based on the gesture velocity when the gesture is completed or canceled.