---
title: Add support for predictive back animations  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/custom-back/support-animations
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Add support for predictive back animations Stay organized with collections Save and categorize content based on your preferences.



When using the system back APIs, you can opt in to receive in-app animations and
support custom transitions.

[

Alas, your browser doesn't support HTML5 video. That's OK! You can still
[download the video](/static/guide/navigation/custom-back/pb-cross-activity-and-back-to-home (1).mp4) and watch it with a video player.
](/static/guide/navigation/custom-back/pb-cross-activity-and-back-to-home (1).mp4)


**Video 1:** Predictive back animations

After opting in, your app displays animations for back-to-home, cross-activity,
and cross-task.

The video shows a brief example of predictive back animations for
cross-activity and back-to-home using the Android Settings app.

1. In the animation, the user swipes back to return to the previous settings
   screen—an example of a cross-activity animation.
2. Now on the previous screen, the user begins swiping back a second time,
   showing a preview of the home screen with its wallpaper—an example of
   the back-to-home animation.
3. The user continues to swipe right, showing an animation of the window
   shrinking down to the icon on the home screen.
4. The user has now fully returned to the home screen.

Learn more about how to [Add support for predictive back gestures](/guide/navigation/custom-back/predictive-back-gesture).

## Add custom in-app transitions and animations

You can create custom in-app property animations and transitions, custom
cross-activity animations, and custom cross-fragment animations with predictive
back gestures.

### Add custom transitions in Jetpack Compose

You can use `PredictiveBackHandler` to handle predictive back gestures in
Jetpack Compose for creating custom in-app transitions. This feature is
available in `androidx.activity:activity-compose:1.8.0-alpha01` or higher.

`PredictiveBackHandler` provides a callback lambda that exposes a
`Flow<BackEventCompat>` which emits events as the user swipes back from edge.
These events provide information about user touch position, swipe edge, and
most importantly `progress`, which can be used to animate components away as
part of handling the back gesture.

The following snippet shows an example of using `PredictiveBackHandler` to
animate a `Surface` scaling down and moving away with gesture progress:

```
@Composable
fun DetailScreen(onBack: () -> Unit) {
    var scale by remember { mutableFloatStateOf(1f) }
    var xOffset by remember { mutableFloatStateOf(0f) }
    val scope = rememberCoroutineScope()

    PredictiveBackHandler { progressFlow ->
        try {
            progressFlow.collectLatest { backEvent ->
                scale = 1f - backEvent.progress
                xOffset = backEvent.progress * 100f
            }
            // User completed gesture
            onBack()
        } catch (e: CancellationException) {
            // User cancelled gesture
            // Animate scale and xOffset back to 1f and 0f respectively
            scope.launch {
                animate(scale, 1f) { value, _ -> scale = value }
            }
            scope.launch {
                animate(xOffset, 0f) { value, _ -> xOffset = value }
            }
        }
    }
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Surface(
            modifier = Modifier
                .size(200.dp)
                .scale(scale)
                .offset(x = xOffset.dp, y = 0.dp),
            color = Color.Blue
        ) {}
    }
}
```