---
title: https://developer.android.com/training/wearables/compose/one-handed-gestures
url: https://developer.android.com/training/wearables/compose/one-handed-gestures
source: md.txt
---

Compose for Wear OS Material version <button value="2.5">2.5</button> <button value="3" default="">3</button>

*** ** * ** ***

Beginning with Wear OS 7 (API level 37), a one-handed gestures
framework, along with an API that's part of Compose for Wear OS,
lets users interact with your app touch-free.

While initially supported on Pixel Watch devices (Pixel Watch 3 and later), the
framework is available to all OEMs. By adopting this API, your app's gesture
support automatically scales across the ecosystem as hardware support expands.

To help users discover available gestures without cluttering the UI,
the Wear OS framework provides animated gesture indicators. These
visual hints highlight where a gesture can be performed, while the
system automatically manages their display cadence and muting
frequency according to user preferences.

## Supported gestures and actions

The Wear OS gestures framework supports two gesture types:

- **Primary action (Double pinch):** Maps to the main action on a screen, such as answering a call or toggling media playback.
- **Dismiss action (Wrist turn):** Maps to backward navigation, dismissing a dialog, or canceling a prompt.

## Configure gestures in Compose

Although the one-handed gestures API can enhance your UI, it's important to
keep in mind that some hardware and OEMs don't support these gestures. If the
API detects that your app is running on one of these unsupported devices, the
library automatically no-ops without affecting standard touch interactions.

As with standard Compose behaviors, you enable one-handed gestures on UI
elements using [modifiers](https://developer.android.com/develop/ui/compose/modifiers). You configure your app's gestures
according to the action to perform---either primary or dismiss---and a `gestureId`
to coordinate with system-level user preferences, such as hint display cadence
and frequency muting. You express this configuration by creating a
`OneHandedGestureConfiguration` object; we recommend using the
`rememberOneHandedGestureConfiguration` function to create it. The
`OneHandedGestureConfiguration` is also where you can provide the gesture
priority.

The `rememberOneHandedGestureConfiguration` function tracks user interaction
history across recompositions without exposing application state. Once your
app has created the configuration, it should pass the configuration to
`Modifier.oneHandedGesture` on your interactive composable.

To help users discover available gestures, the library provides the
`OneHandedGestureClickIndicator` method. This method acts as a wrapper that
replaces its underlying content to indicate to the user that a gesture action
is available.

### Interactive components

To enable gestures on an interactive control like a button, create a
configuration specifying `OneHandedGestureAction.Primary` and apply the
`oneHandedGesture` modifier. Pass the same `MutableInteractionSource` to both
the control and the modifier so gesture events emit visual press feedback onto
the control.

To enable the gesture indicator, create and remember an instance of
`OneHandedGestureClickIndicatorState`. Then, to trigger the visual feedback,
call `showIndicator` within the `onGestureAvailable` callback provided by the
`oneHandedGesture` modifier, which signals to the system that an indication
event has occurred. Once called, the component briefly replaces its normal
content with a gesture animation.

<br />

```kotlin
var isPlaying by remember { mutableStateOf(false) }
val onClick = { isPlaying = !isPlaying }

val gestureConfig = rememberOneHandedGestureConfiguration(
    action = OneHandedGestureAction.Primary
)
val indicatorState = remember { OneHandedGestureClickIndicatorState() }
val coroutineScope = rememberCoroutineScope()
val interactionSource = remember { MutableInteractionSource() }

Button(
    onClick = onClick,
    interactionSource = interactionSource,
    modifier = Modifier
        .fillMaxWidth()
        .oneHandedGesture(
            gestureConfiguration = gestureConfig,
            interactionSource = interactionSource,
            onGestureLabel = if (isPlaying) "pause" else "play",
            onGestureAvailable = { coroutineScope.launch { indicatorState.showIndicator() } },
            onGesture = onClick
        )
) {
    OneHandedGestureClickIndicator(
        gestureConfiguration = gestureConfig,
        state = indicatorState
    ) {
        Text(if (isPlaying) "Pause" else "Play", modifier = Modifier.fillMaxWidth())
    }
}
```

<br />

### Scrollable containers

For scrollable screens or lists, create a configuration specifying
`OneHandedGestureAction.Primary` and apply the `oneHandedGesture` modifier to
your container, calling a scrolling helper such as `scrollDown`.

To provide visual feedback for scrolling actions, you can use the
[`OneHandedGestureScrollIndicator`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureScrollIndicator.composable). This component functions
as a standard scroll indicator that shows the scroll position, but it can also
indicate that a scroll gesture is available to the user. This indicator is
typically passed to the `scrollIndicator` slot of a
[`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ScreenScaffold.composable) and is coupled with the state of a
scrollable container, such as a `TransformingLazyColumn`. It also observes a
`OneHandedGestureScrollIndicatorState` to manage its visual transitions.

To trigger the visual feedback, call `showIndicator` on this state---typically
inside the `onGestureAvailable` callback of the `oneHandedGesture` modifier.
Once triggered, the indicator temporarily replaces its standard visual state
with a gesture animation sequence to alert the user.

<br />

```kotlin
val scrollState = rememberTransformingLazyColumnState()
val gestureConfig = rememberOneHandedGestureConfiguration(
    action = OneHandedGestureAction.Primary,
    priority = OneHandedGesturePriority.Scrollable
)
val indicatorState = remember(gestureConfig) { OneHandedGestureScrollIndicatorState() }
val coroutineScope = rememberCoroutineScope()

ScreenScaffold(
    scrollState = scrollState,
    scrollIndicator = {
        OneHandedGestureScrollIndicator(
            gestureConfiguration = gestureConfig,
            indicatorState = indicatorState,
            scrollState = scrollState,
            modifier = Modifier.align(Alignment.CenterEnd)
        )
    }
) { contentPadding ->
    TransformingLazyColumn(
        state = scrollState,
        contentPadding = contentPadding,
        modifier = Modifier
            .fillMaxSize()
            .oneHandedGesture(
                gestureConfiguration = gestureConfig,
                onGestureLabel = "scroll",
                onGestureAvailable = {
                    coroutineScope.launch { indicatorState.showIndicator() }
                },
                onGesture = { OneHandedGestureDefaults.scrollDown(scrollState) }
            )
    ) {
        items(10) { index ->
            Text("Item $index", modifier = Modifier.padding(8.dp))
        }
    }
}
```

<br />

### Combine multiple gestures

You can configure both a scroll gesture and a click gesture with the same
primary action by adding `gesturePriority` to your
`OneHandedGestureConfiguration` object:

- **[`OneHandedGesturePriority.Clickable`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGesturePriority)** (highest): Assign to interactive controls---such as those with type `Button` or `Card`---so that they capture gestures when visible on screen.
- **[`OneHandedGesturePriority.Scrollable`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGesturePriority)** (medium): Assign to scrollable or pageable containers so they yield to clickable children but scroll when no clickable control is visible.
- **[`OneHandedGesturePriority.Unspecified`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGesturePriority)** (lowest): An unassigned priority. This is the default value for a gesture that doesn't have a `priority` set.

By explicitly setting `priority = OneHandedGesturePriority.Clickable`
on an inner button and `priority = OneHandedGesturePriority.Scrollable`
on its parent list, the system can show this gesture-priority behavior.
When the user triggers the primary action by the one-handed gesture, it
first scrolls the list down until the button is visible. Then, it
captures the button's click action.

## Test and debug gestures with ADB

You can test one-handed gestures on a physical device or emulator
without performing physical wrist movements by using the Android Debug
Bridge (`adb`) and the `IWearGestureService` system service.

### Enable gesture simulation

1. Verify that your Wear OS device is running Wear OS 7 (API level 37) and higher.
2. If testing on a physical device that's not on the wrist or on a charger, override the off-body sensor state so the device remains active:

    adb shell cmd sensorservice set-off-body-state 0

### Trigger gesture events using ADB

To simulate the **Double Pinch** (`Primary` action) gesture, run the following
ADB shell command:

    adb shell cmd IWearGestureService gesture 1

To simulate the **Wrist Turn** (`Dismiss` action) gesture, run the following ADB
shell command:

    adb shell cmd IWearGestureService gesture 2

### Reset gesture hint tracking

The system tracks user interaction history and displays floating gesture
hints based on the global cadence setting (such as **Always** or
**Daily**). When debugging your app's gesture indicators, reset this
tracking history so hints appear again for your package:

    adb shell cmd IWearGestureService hint clear <your_package_name>

To reset the off-body sensor state when finished testing:

    adb shell cmd sensorservice reset-off-body-state

## Additional resources

For design guidance on when and where to use one-handed gestures, see
[One-handed gestures](https://developer.android.com/design/ui/wear/guides/patterns/gestures).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [One-handed gestures design guide](https://developer.android.com/design/ui/wear/guides/patterns/gestures)