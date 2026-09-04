---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/physical-input
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/physical-input
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

To capture and process user input that is delivered to your app's [projected
activity](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/support-different-types#activity-lifecycle), or to implement custom touchpad behaviors, [use indirect pointer
inputs](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/indirect-pointer). To handle other types of events (such as the camera action), see the
following sections in this guide.

## Handle the camera action

Whenever a user presses a device's camera button, the system delivers an input
event to your app's projected activity as a
[`ProjectedInputEvent.ProjectedInputAction.TOGGLE_APP_CAMERA`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedInputEvent.ProjectedInputAction#TOGGLE_APP_CAMERA()) action. Your
app can observe this action using a dedicated dispatcher:


```kotlin
@OptIn(ExperimentalProjectedApi::class)
class CameraActionInputSnippetActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Observe hardware camera action events when RESUMED
        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.RESUMED) {
                withContext(Dispatchers.Default) {
                    try {
                        val projectedActivity = ProjectedActivityCompat.create(this@CameraActionInputSnippetActivity)
                        try {
                            projectedActivity.projectedInputEvents.collect { inputEvent ->
                                if (inputEvent.inputAction == TOGGLE_APP_CAMERA) {
                                    withContext(Dispatchers.Main) {
                                        onCameraActionTriggered()
                                    }
                                }
                            }
                        } finally {
                            projectedActivity.close()
                        }
                    } catch (e: CancellationException) {
                        throw e
                    } catch (e: Exception) {
                        Log.w("CameraActionSnippet", "ProjectedActivityCompat unavailable: ${e.message}")
                    }
                }
            }
        }

        setContent {
            GlimmerTheme {
                TouchpadInputSnippet(
                    onTap = { Log.i("CameraActionSnippet", "Touchpad tapped") }
                )
            }
        }
    }

    private fun onCameraActionTriggered() {
        Log.i("CameraActionSnippet", "Camera action button double-pressed!")
    }
}
```

<br />

## Inspect generic motion events

Use [`dispatchGenericMotionEvent`](https://developer.android.com/reference/kotlin/android/app/Activity#dispatchgenericmotionevent) to inspect generic motion events delivered
to your app's projected activity. Generic motion events are delivered at the
activity boundary and don't require a focused Jetpack Compose Glimmer component.

A `MotionEvent` can include:

- A masked action, such as [`ACTION_DOWN`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_down), [`ACTION_MOVE`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_move), or [`ACTION_UP`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_up).
- Pointer coordinates, such as [`AXIS_X`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_x), [`AXIS_Y`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_y), or [`AXIS_Z`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#axis_z).
- Device and source information, such as the [device ID](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getdeviceid) and [source](https://developer.android.com/reference/kotlin/android/view/MotionEvent#getsource).

Not every value is meaningful for every action. Inspect the action and source
before treating a raw event as a completed gesture.


```kotlin
class MotionGestureInputSnippetActivity : ComponentActivity() {

    override fun dispatchGenericMotionEvent(ev: MotionEvent): Boolean {
        val actionName = when (ev.actionMasked) {
            MotionEvent.ACTION_DOWN -> "ACTION_DOWN" // First contact with the glasses touchpad
            MotionEvent.ACTION_MOVE -> "ACTION_MOVE" // Contact moving across the glasses touchpad
            MotionEvent.ACTION_UP -> "ACTION_UP"     // Contact lifted from the glasses touchpad
            else -> "ACTION_${ev.actionMasked}"
        }

        Log.d(
            "MotionGestureSnippet",
            "MotionEvent: action=$actionName x=${ev.x} y=${ev.y}"
        )

        // Delegate to super unless intentionally consuming the event
        return super.dispatchGenericMotionEvent(ev)
    }
}
```

<br />

Return `true` only when the activity intentionally consumes the event.
Otherwise, return `super.dispatchGenericMotionEvent(ev)` so the event can
continue through normal dispatch.

## Handle the system Back gesture

When a screen needs custom back behavior, your app should handle the glasses
Back gesture using the same Android APIs that you use for other activities, such
as [`OnBackPressedDispatcher`](https://developer.android.com/guide/navigation/navigation-custom-back) and [`OnBackPressedCallback`](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback).

The user gesture depends on the glasses type:

- On display glasses, swiping down on the touchpad performs the system Back gesture.
- On audio glasses, swiping back on the touchpad performs the system Back gesture.

Register a back callback when the current screen needs to intercept Back, such
as closing an overlay or showing an exit confirmation.


```kotlin
class BackGestureInputSnippetActivity : ComponentActivity() {

    private val backCallback = object : OnBackPressedCallback(true) {
        override fun handleOnBackPressed() {
            onBackGestureReceived()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Register back gesture callback with Activity's onBackPressedDispatcher
        onBackPressedDispatcher.addCallback(this, backCallback)
    }

    private fun onBackGestureReceived() {
        Log.i("BackGestureSnippet", "System back gesture intercepted")
    }
}
```

<br />

The callback should only be enabled when the active screen should intercept
Back. Disable or remove the callback when default system or navigation behavior
should handle Back.

## Next steps

After implementing input handling for these events, you can learn more about
handling other types of input events in the following topics:

- For more information about UI input, see [Focus in Jetpack Compose
  Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/focus) and [Handle indirect pointer inputs](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/indirect-pointer).
- For projected input events, see [`ProjectedActivityCompat`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedActivityCompat), [`ProjectedInputEvent`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedInputEvent), and [`ProjectedInputEvent.ProjectedInputAction`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedInputEvent.ProjectedInputAction).
- For platform input and navigation, see [`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent) and [Provide
  custom back navigation](https://developer.android.com/guide/navigation/navigation-custom-back).