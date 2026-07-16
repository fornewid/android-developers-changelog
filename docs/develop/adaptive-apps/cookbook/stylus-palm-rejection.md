---
title: https://developer.android.com/develop/adaptive-apps/cookbook/stylus-palm-rejection
url: https://developer.android.com/develop/adaptive-apps/cookbook/stylus-palm-rejection
source: md.txt
---

![Five star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/five-star-rating.png)

A stylus can be an exceptionally productive and creative tool. But when users
draw, write, or interact with an app using a stylus, they sometimes touch the
screen with the palm of their hands. The touch event can be reported to your app
before the system recognizes and dismisses the event as an accidental palm
touch.

## Best practices

Your app must identify extraneous touch events and ignore them. In Jetpack
Compose, you can access the underlying Android [`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent) from a
[`PointerEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent). Check the `MotionEvent` for [`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel), which
indicates that a gesture should stop and may need to be rolled back. On
Android 13 (API level 33) and higher, check for the [`FLAG_CANCELED`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#flag_canceled) flag
on [`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel) and [`ACTION_POINTER_UP`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_pointer_up) events, which provides a
strong signal that the touch was unintentional, such as a palm touch.

## Ingredients

- [`Modifier.pointerInput()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary): The Compose modifier used to process pointer input.
- [`PointerEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent): Represents a pointer event in Compose, which contains one or more changes.
- [`PointerEvent.motionEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent#motionEvent()): Extension property that provides access to the underlying Android `MotionEvent` (nullable).
- [`MotionEvent`](https://developer.android.com/reference/kotlin/android/view/MotionEvent): Represents touch and movement events. Contains the information necessary to determine whether an event should be disregarded.
- [`ACTION_CANCEL`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_cancel): `MotionEvent` constant that indicates a gesture has been canceled; the gesture should stop and may need to be rolled back.
- [`ACTION_POINTER_UP`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#action_pointer_up): `MotionEvent` constant that indicates a pointer other than the first pointer has gone up (that is, has relinquished contact with the device screen).
- [`FLAG_CANCELED`](https://developer.android.com/reference/kotlin/android/view/MotionEvent#flag_canceled): `MotionEvent` constant that indicates that the pointer going up caused an unintentional touch event. Added to `ACTION_POINTER_UP` and `ACTION_CANCEL` events on Android 13 (API level 33) and higher.

## Steps

Examine `MotionEvent` objects dispatched to your app. Use the `MotionEvent` APIs
to determine event characteristics:

- **Single-pointer events** --- Check for `ACTION_CANCEL`, which indicates the gesture should stop. On Android 13 and higher, also check for `FLAG_CANCELED` to confirm the touch was unintentional.
- **Multi-pointer events** --- On Android 13 and higher, check for `ACTION_POINTER_UP` and `FLAG_CANCELED` to identify unintentional touches.

Respond to these events by stopping the gesture and rolling back any temporary
changes.

> [!WARNING]
> **Warning:** Android 12 (API level 32) and lower provide only `ACTION_POINTER_UP` for non-primary multi-pointer events. `FLAG_CANCELED` is not set for cancelable events such as palm touches. As a result, apps cannot determine whether the touch was intended or not on Android 12 and lower.

### 1. Acquire motion event objects

Use `Modifier.pointerInput` to process pointer input on a Composable. Within the
pointer input scope, use `awaitPointerEventScope` and `awaitPointerEvent` to
receive events, and retrieve the underlying Android `MotionEvent` using the
`motionEvent` property:


```kotlin
import androidx.compose.ui.input.pointer.pointerInput
    Box(
        modifier = Modifier
            .fillMaxSize()
            .pointerInput(Unit) {
                awaitPointerEventScope {
                    while (true) {
                        val event = awaitPointerEvent()
                        val motionEvent = event.motionEvent
                        if (motionEvent != null) {
                            // Process motion event.
                        }
                    }
                }
            }
    )
```

<br />

### 2. Determine the event action and flags

Check the `MotionEvent` for `ACTION_CANCEL`, which indicates a single-pointer
event on all API levels. On Android 13 and higher, check `ACTION_POINTER_UP`
for `FLAG_CANCELED`:


```kotlin
import androidx.compose.ui.input.pointer.pointerInput
    Box(
        modifier = Modifier
            .fillMaxSize()
            .pointerInput(Unit) {
                awaitPointerEventScope {
                    while (true) {
                        val event = awaitPointerEvent()
                        val motionEvent = event.motionEvent ?: continue

                        when (motionEvent.actionMasked) {
                            MotionEvent.ACTION_CANCEL -> {
                                // Process canceled single-pointer motion event for all SDK versions.
                            }
                            MotionEvent.ACTION_POINTER_UP -> {
                                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU &&
                                    (motionEvent.flags and MotionEvent.FLAG_CANCELED) == MotionEvent.FLAG_CANCELED
                                ) {
                                    // Process canceled multi-pointer motion event for Android 13 and higher.
                                }
                            }
                        }
                    }
                }
            }
    )
```

<br />

### 3. Undo the gesture

Once you've identified a palm touch, you can undo the onscreen effects of the
gesture.

Your app must keep a history of user actions so that unintended inputs such as
palm touches can be undone. See [Implement a basic drawing app](https://developer.android.com/codelabs/large-screens/advanced-stylus-support#2) in the
*Enhance stylus support in an Android app* codelab for an example.

## Results

Your app can now identify and reject palm touches for multi-pointer
events on Android 13 and higher API levels and for single-pointer events on
all API levels.

## Additional resources

For more information, see the following:

- Android 13 features and APIs --- [Improved palm rejection](https://developer.android.com/about/versions/13/features/large-screens#palm_rejection)
- Developer guides
  - [Advanced stylus features](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features)
  - [Palm rejection](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#palm_rejection) section of *Input compatibility on large screens*
- Codelab --- [Enhance stylus support in an Android app](https://developer.android.com/codelabs/large-screens/advanced-stylus-support)