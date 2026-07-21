---
title: https://developer.android.com/training/wearables/always-on
url: https://developer.android.com/training/wearables/always-on
source: md.txt
---

This guide explains how to make your app always-on, how to react to power state
transitions, and how to manage application behavior to provide a good user
experience while [conserving battery](https://developer.android.com/training/wearables/apps/power).

Making an app constantly visible significantly impacts battery life, so consider
the power impact when adding this feature.

## Key Concepts

When a Wear OS app is displayed on the full screen, it is in one of two power
states:

- **Interactive**: A high-power state where the screen is at full brightness, allowing for full user interaction.
- **Ambient** : A low-power state where the display dims to conserve power. In this state, your app's UI still occupies the full screen, but the system might alter its appearance by blurring it or showing overlay content like the time. This is also referred to as **Ambient Mode**.

The operating system controls the transition between these states.

An **Always-On App** is an application that displays content in both the
*Interactive* and *Ambient* states.

When an always-on app continues to display its own UI while the device is in the
low-power *Ambient* state, it is described as being in **ambiactive mode**.

## System transitions and default behavior

When an app is in the foreground, the system manages power state transitions
based on two timeouts triggered by user inactivity.

- **Timeout #1: Interactive to Ambient state:** After a period of user inactivity, the device enters the *Ambient* state.
- **Timeout #2: Return to watch face:** After a further period of inactivity, the system may hide the current app and display the watch face.

Immediately after the system passes through the first transition into the
*Ambient* state, the default behavior depends on the Wear OS version and your
app's configuration:

- **On Wear OS 5 and lower** , the system displays a blurred screenshot of your paused application, with the time overlaid on top. This state is represented by the "AOD Lite" node in [the following flowchart](https://developer.android.com/training/wearables/always-on#flowchart).
- **On Wear OS 6 and higher** , if an app targets SDK 36 or newer, it is considered always-on. The display is dimmed, but the application continues running and remains visible. (Updates may be as infrequent as once per minute.) This state is represented by the "Global AOD" node in [the
  following flowchart](https://developer.android.com/training/wearables/always-on#flowchart).

## Customize behavior for the Ambient state

Regardless of the default system behavior, on all Wear OS versions you can
customize your app's appearance or behavior while in the *Ambient* state by
using [`LocalAmbientModeManager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/rememberAmbientModeManager.composable) to observe state transitions in
Jetpack Compose on Wear OS. This state is represented by the "Ambiactive Mode"
node in [the following flowchart](https://developer.android.com/training/wearables/always-on#flowchart).

### Observe ambient state

To react to ambient mode events in Jetpack Compose on Wear OS:

1. Use [`LocalAmbientModeManager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/rememberAmbientModeManager.composable) to observe changes to the system's
   ambient mode status, adjusting your composables accordingly. Configure your
   component to adjust to a lower-power mode in the `AmbientMode.Ambient` state,
   and restore it to a full interactive display in the `AmbientMode.Interactive`
   state.


   ```kotlin
   // In a production application, the AmbientModeManager should be instantiated and provided at
   // the highest level of the Compose hierarchy (typically in the host Activity's setContent
   // block) using a CompositionLocalProvider. This ensures proper lifecycle management and
   // broad accessibility.

   // For this self-contained demo, AmbientModeManager is created and provided locally:
   val activityAmbientModeManager = rememberAmbientModeManager()
   CompositionLocalProvider(LocalAmbientModeManager provides activityAmbientModeManager) {
       val ambientModeManager = LocalAmbientModeManager.current
       val ambientMode = ambientModeManager?.currentAmbientMode

       if (ambientModeManager != null) {
           ambientModeManager.AmbientTickEffect {
               // While device is in ambient mode, update properties every minute or so
               // ...
           }
       }

       // ...
           val ambientModeName =
               when (ambientMode) {
                   is AmbientMode.Interactive -> "Interactive"
                   is AmbientMode.Ambient -> "Ambient"
                   else -> "Unknown"
               }

           Text(text = "$ambientModeName Mode")
           // ...
   }
   ```

   <br />

For developers using Jetpack Compose, use [`LocalAmbientModeManager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/rememberAmbientModeManager.composable), which
simplifies the implementation of this pattern.

### Ambient behavior flowchart

The following flowchart illustrates how the system determines the ambient
behavior based on the device's Wear OS version, your app's `targetSdkVersion`,
and whether it implements `AmbientLifecycleCallback`.
![A flowchart illustrating the decision logic for Wear OS ambient mode. It shows how the device's OS version and the app's configuration determine one of three outcomes: a blurred overlay, Global AOD, or app-managed Ambiactive Mode.](https://developer.android.com/static/training/wearables/images/ambient-flowchart.png) **Figure 1.**: A flowchart illustrating the decision logic for Wear OS ambient mode.

## Control screen-on duration

The following sections describe how to manage how long your app stays on the
screen.

### Prevent returning to the watch face with an Ongoing Activity or Live Update

After a period of time in the *Ambient* state (Timeout #2), the system will
typically return to the watch face. The user can configure the timeout duration
in the system settings. For certain use cases, like a user tracking a workout,
an app might need to remain visible for longer.

On Wear OS 5 and higher, you can prevent this by implementing an **Ongoing
Activity** . If your app is displaying information about an ongoing user task,
such as a workout session, you can use the [Ongoing Activity API](https://developer.android.com/training/wearables/notifications/ongoing-activity) to keep
your app visible until the task ends. If a user manually returns to the
watchface, the ongoing activity indicator provides a one-tap way for them to
return to your app.

Alternatively, on Wear OS 7 and higher, you can use a [Live Update](https://developer.android.com/training/wearables/notifications/live-updates) in
place of an Ongoing Activity. For backward compatibility, continue to support
Ongoing Activity on devices that run Wear OS 6 or lower.

> [!NOTE]
> **Note:** If media is playing on the Wear OS device, an ongoing activity will automatically be created. In this case, you don't need to create another ongoing activity to keep your app visible.

To implement this, the ongoing notification's touch intent must point to your
always-on activity, as shown in the following code snippet:


```kotlin
val activityIntent =
    Intent(this, AlwaysOnActivity::class.java).apply {
        flags = Intent.FLAG_ACTIVITY_SINGLE_TOP
    }

val pendingIntent =
    PendingIntent.getActivity(
        this,
        0,
        activityIntent,
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
    )

val notificationBuilder =
    NotificationCompat.Builder(this, CHANNEL_ID)
        // ...
        // ...
        .setOngoing(true)

// ...

val ongoingActivity =
    OngoingActivity.Builder(applicationContext, NOTIFICATION_ID, notificationBuilder)
        // ...
        // ...
        .setTouchIntent(pendingIntent)
        .build()

ongoingActivity.apply(applicationContext)

val notification = notificationBuilder.build()
```

<br />

### Keep the screen on and prevent Ambient state

In rare cases, you might need to completely prevent the device from entering the
*Ambient* state. That is, to avoid Timeout #1. To do this, you can use the
[`keepScreenOn`](https://developer.android.com/reference/kotlin/androidx/compose/ui/keepScreenOn.modifier) modifier. This functions as a wake lock, keeping
the device in the *Interactive* state. Use this with extreme caution as it
severely impacts battery life.

## Recommendations for Ambient mode

To provide the best user experience and conserve power in *Ambient* mode, follow
these design guidelines. These recommendations prioritize a clear user
experience, by preventing misleading information and reducing visual clutter,
while simultaneously optimizing display power.

- **Reduce visual clutter and display power.** A clean, minimalist UI signals to the user that the app is in a low-power state and saves significant battery by limiting bright pixels.
  - Keep at least 85% of the screen black.
  - Show only the most critical information, moving secondary details to the interactive display.
  - Use outlines for large icons or buttons rather than solid fills.
  - Avoid large blocks of solid color and non-functional branding or background images.
- **Handle stale dynamic data**
  - The `AmbientTickEffect` callback is invoked only periodically -- typically once per minute -- to conserve power. Because of this limitation, any data that changes frequently -- such as a stopwatch, heart rate, or workout distance -- becomes stale between updates. To avoid displaying misleading and incorrect information, replace these live values with static placeholder content, such as `--`.
- **Maintain a consistent layout**
  - Keep elements in the same position across *Interactive* and *Ambient* modes to create a smooth transition.
  - Always show the time.
- **Be context aware**
  - If the user was on a settings or configuration screen when the device enters ambient mode, consider showing a more relevant screen from your app instead of the settings view.
- **Handle device-specific requirements**
  - In the [`AmbientMode`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/AmbientMode) object returned from `currentAmbientMode`:
    - If `isLowBitAmbientSupported` is `true`, disable anti-aliasing where possible.
    - If `isBurnInProtectionRequired` is `true`, periodically shift the UI elements slightly and avoid solid white areas to prevent screen burn-in.

## Debugging and testing

These [`adb`](https://developer.android.com/tools/adb) commands may be useful when developing or testing how your app
behaves when the device is in ambient mode:

    # put device in ambient mode if the always on display is enabled in settings
    # (and not disabled by other settings, such as theatre mode)
    $ adb shell input keyevent KEYCODE_SLEEP

    # put device in interactive mode
    $ adb shell input keyevent KEYCODE_WAKEUP

## Example: Workout app

Consider a workout app that needs to display metrics to the user for the entire
duration of their exercise session. The app must remain visible through
*Ambient* state transitions and avoid being replaced by the watch face.

To achieve this, the developer should do the following:

1. Use `LocalAmbientModeManager` to handle UI changes between *Interactive* and *Ambient* states, such as dimming the screen and removing non-essential data.
2. Create [a new low-powered layout](https://developer.android.com/training/wearables/always-on#ambient-appearance) for the *Ambient* state that follows the best practices.
3. Use the [Ongoing Activity API](https://developer.android.com/training/wearables/notifications/ongoing-activity) (or [Live Updates](https://developer.android.com/training/wearables/notifications/live-updates) on Wear OS 7 and higher) for the duration of the workout to prevent the system from returning to the watch face.

For a complete implementation, see the compose-based [Exercise sample](https://github.com/android/health-samples/tree/main/health-services/ExerciseSampleCompose) on
GitHub. This sample also demonstrates the use of the
[`LocalAmbientModeManager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/rememberAmbientModeManager.composable) composable to simplify ambient mode handling
in Compose.