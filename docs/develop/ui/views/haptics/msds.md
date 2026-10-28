---
title: https://developer.android.com/develop/ui/views/haptics/msds
url: https://developer.android.com/develop/ui/views/haptics/msds
source: md.txt
---

The page describes how to enrich applications with audio-haptic feedback
following the guidelines from the Multisensory Design System (MSDS).
keywords_public: \>
haptics, vibration, audio, feedback, Android, UI, UX, design, multisensory,
msds

Apps running on devices that run Android can deliver multisensory
audio-haptic feedback compliant with the Multisensory Design System (MSDS),
a tokenized component library for consistent audio and haptics.

## Why use MSDS?

MSDS is a centralized design system for improved audio and haptic
feedback. With MSDS, you don't need to design, select or craft
your own tactile or auditory feedback for common user interactions.

In addition, MSDS works consistently across devices, synchronizing
audio and haptics optimally based on device capabilities.

## When should you use MSDS?

MSDS provides feedback for common active user interactions. This feedback
triggers in response to a user action that causes an effect in the system or
the app, and falls into two categories:

- **Gesture feedback:** Confirms the real-time physical manipulation of UI
  elements from direct user gestures.

- **Semantic feedback:** Confirms real-time state changes, selections, or user
  progress.

## How do you use MSDS?

The [`MultisensoryManager`](https://developer.android.com/reference/android/os/multisensory/MultisensoryManager) API is the entry point for
delivering MSDS feedback. You can play tokenized feedback by using the
[`playToken()`](https://developer.android.com/reference/android/os/multisensory/MultisensoryManager#playToken(int)) method.

To see available tokens, read the public integer constants of
`MultisensoryManager`. To use the manager in your app, query it as a system
service and play tokens:


```kotlin
@RequiresApi(Build.VERSION_CODES_FULL.CINNAMON_BUN_2)
@Composable
fun MultisensorySwitch() {
    val context = LocalContext.current
    val multisensoryManager =
        remember(context) { context.getSystemService(MultisensoryManager::class.java) }
    var checked by remember { mutableStateOf(false) }
    Switch(
        checked = checked,
        onCheckedChange = { isChecked ->
            checked = isChecked
            if (isChecked) {
                multisensoryManager?.playToken(MultisensoryManager.TOKEN_SWITCH_ON)
            } else {
                multisensoryManager?.playToken(MultisensoryManager.TOKEN_SWITCH_OFF)
            }
        }
    )
}
```

<br />

You can also keep a reference to the `MultisensoryManager` in a
`ViewModel` to trigger MSDS playback in response to method calls or UI
state changes.

## Recommendations

MSDS feedback usually plays alongside animations or user gestures because
it triggers from active user interactions. Play feedback at the appropriate
time so that visuals, audio, and haptics trigger as close together as
possible.

Depending on your app structure, this recommendation can result in playback
calls inside UI composable callbacks (like the earlier `Switch` example),
changes to UI [`State`](https://developer.android.com/develop/ui/compose/state) or [`StateFlow`](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow#stateflow), animation frames,
or UI responses to direct user input.

In all cases, the general recommendation is to deliver feedback once the user
can perceive the consequence of their action in the system.