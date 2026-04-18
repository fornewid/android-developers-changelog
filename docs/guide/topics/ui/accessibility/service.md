---
title: https://developer.android.com/guide/topics/ui/accessibility/service
url: https://developer.android.com/guide/topics/ui/accessibility/service
source: md.txt
---

> [!NOTE]
> **Note:** Documentation across [developer.android.com](https://developer.android.com/) is being refactored to show how to accomplish tasks with Compose. We recommend using Compose for your app, but you can still access the Views-specific information for the concepts on this page at [Create your own accessibility service (Views)](https://developer.android.com/guide/topics/ui/accessibility/views/service).

An *accessibility service* is an app that enhances the user interface to assist
users with disabilities or who might temporarily be unable to fully interact
with a device. These services run in the background and communicate with the
system to inspect screen content and interact with apps on the user's behalf.
Examples include screen readers (like TalkBack), Switch Access tools, and voice
control systems.

This guide covers the basics of building an Android accessibility service.

> [!CAUTION]
> **Caution:** An accessibility service is a specialized tool, not a standard way to make your app accessible.
>
> - If you want to make your app accessible to existing services like TalkBack, use standard Android accessibility APIs. For more information, see [Accessibility in Jetpack Compose](https://developer.android.com/develop/ui/compose/accessibility).
> - Only build an accessibility service if you are creating a general-purpose assistive tool.

## Accessibility service lifecycle

To create an accessibility service, you must extend the
[`AccessibilityService`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityService)
class and declare the service in your app's manifest.

### Create the service class

Create a class that extends `AccessibilityService`. You must override the
following methods:

- **`onAccessibilityEvent`**: Called when the system detects an event that matches your service's configuration (for example, focus change or a button click). This is where your service interprets the user interface.
- **`onInterrupt`**: Called when the system interrupts your service's feedback (for example, to stop speech output when the user moves focus quickly).

```kotlin
package com.example.android.apis.accessibility

import android.accessibilityservice.AccessibilityService
import android.accessibilityservice.AccessibilityServiceInfo
import android.accessibilityservice.FingerprintGestureController
import android.accessibilityservice.AccessibilityButtonController
import android.accessibilityservice.GestureDescription
import android.view.accessibility.AccessibilityEvent
import android.view.accessibility.AccessibilityNodeInfo
import android.graphics.Path
import android.os.Build
import android.media.AudioManager
import android.content.Context

class MyAccessibilityService : AccessibilityService() {

    override fun onAccessibilityEvent(event: AccessibilityEvent) {
        // Interpret the event and provide feedback to the user
    }

    override fun onInterrupt() {
        // Interrupt any ongoing feedback
    }

    override fun onServiceConnected() {
        // Perform initialization here
    }
}
```

### Declare in the manifest

Register your service in the `AndroidManifest.xml` file. You must strictly
enforce the
[`BIND_ACCESSIBILITY_SERVICE`](https://developer.android.com/reference/kotlin/android/Manifest.permission#bind_accessibility_service)
permission so that only the system can bind to your service.

To make sure the settings button works, declare the `ServiceSettingsActivity`.

```xml
<application>
  <service android:name=".accessibility.MyAccessibilityService"
      android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"
      android:exported="true"
      android:label="@string/accessibility_service_label">
      <intent-filter>
          <action android:name="android.accessibilityservice.AccessibilityService" />
      </intent-filter>
      <meta-data
          android:name="android.accessibilityservice"
          android:resource="@xml/accessibility_service_config" />
  </service>

  <activity android:name=".accessibility.ServiceSettingsActivity"
      android:exported="true"
      android:label="@string/accessibility_service_settings_label" />
</application>
```

### Configure the service

Create a configuration file in `res/xml/accessibility_service_config.xml`. This
file defines what events your service handles and what feedback it provides.
Make sure to reference the `ServiceSettingsActivity` that you declared in your
manifest:

```xml
<accessibility-service xmlns:android="http://schemas.android.com/apk/res/android"
    android:description="@string/accessibility_service_description"
    android:accessibilityEventTypes="typeAllMask"
    android:accessibilityFlags="flagDefault|flagRequestFingerprintGestures|flagRequestAccessibilityButton"
    android:accessibilityFeedbackType="feedbackSpoken"
    android:notificationTimeout="100"
    android:canRetrieveWindowContent="true"
    android:canPerformGestures="true"
    android:settingsActivity="com.example.android.apis.accessibility.ServiceSettingsActivity" />
```

> [!NOTE]
> **Note:** Be careful---using `typeAllMask` can be resource intensive because it forces the system to notify your application of every accessibility event that occurs across the entire OS.

The configuration file includes the following key attributes:

- **`android:accessibilityEventTypes`** : The events you want to receive. Use `typeAllMask` for a general-purpose service.
- **`android:canRetrieveWindowContent`** : Must be `true` if your service needs to inspect the UI hierarchy (for example, to read text from the screen).
- **`android:canPerformGestures`** : Must be `true` if you intend to dispatch gestures (like swipes or taps) programmatically.
- **`android:accessibilityFlags`** : Combine flags to enable features. `flagRequestFingerprintGestures` is required for fingerprint gestures. `flagRequestAccessibilityButton` is required for the software accessibility button.

For a full list of configuration options, see
[`AccessibilityServiceInfo`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityServiceInfo).

### Runtime configuration

While XML configuration is static, you can also modify your service
configuration dynamically at runtime. This is useful for toggling features based
on user preferences.

Override `onServiceConnected()` to apply runtime updates using
`setServiceInfo()`:

```kotlin
override fun onServiceConnected() {
    val info = AccessibilityServiceInfo()

    // Set the type of events that this service wants to listen to.
    info.eventTypes = AccessibilityEvent.TYPE_VIEW_CLICKED or AccessibilityEvent.TYPE_VIEW_FOCUSED

    // Set the type of feedback your service provides.
    info.feedbackType = AccessibilityServiceInfo.FEEDBACK_SPOKEN

    // Set flags at runtime.
    info.flags = AccessibilityServiceInfo.FLAG_DEFAULT or
            AccessibilityServiceInfo.FLAG_REQUEST_FINGERPRINT_GESTURES

    this.setServiceInfo(info)
}
```

## Interpret UI content

When `onAccessibilityEvent()` triggers, the system provides an
`AccessibilityEvent`. This event acts as the entry point to the
*accessibility tree*, a hierarchical representation of the screen content.

Your service interacts primarily with
[`AccessibilityNodeInfo`](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityNodeInfo)
objects, which represent UI elements like buttons, lists, and text. Data about
these UI elements is normalized into `AccessibilityNodeInfo`.

The following example shows how to retrieve the source of an event and traverse
the accessibility tree to find information.

```kotlin
override fun onAccessibilityEvent(event: AccessibilityEvent) {
    // Get the source node of the event
    val sourceNode: AccessibilityNodeInfo? = event.source

    if (sourceNode == null) return

    // Inspect properties
    if (sourceNode.isCheckable) {
        val state = if (sourceNode.isChecked) "Checked" else "Unchecked"
        val label = sourceNode.text ?: sourceNode.contentDescription
        
        // Provide feedback (for example, speak to the user)
        speakToUser("$label is $state")
    }

    // Always recycle nodes to prevent memory leaks
    sourceNode.recycle()
}

private fun speakToUser(text: String) {
    // Your text-to-speech implementation goes here
}
```

## Act on behalf of users

Accessibility services can perform actions, such as clicking buttons or
scrolling lists, on behalf of the user.

To perform an action, call `performAction()` on an `AccessibilityNodeInfo`
object.

```kotlin
fun performClick(node: AccessibilityNodeInfo) {
    if (node.isClickable) {
        node.performAction(AccessibilityNodeInfo.ACTION_CLICK)
    }
}
```

For global actions that affect the entire system (like pressing the Back button
or opening the notification shade), use `performGlobalAction()`.

```kotlin
// Navigate back
fun navigateBack() {
    performGlobalAction(AccessibilityService.GLOBAL_ACTION_BACK)
}
```

## Manage focus

Android has two distinct types of focus: *input focus* (where keyboard input
goes) and *accessibility focus* (what the accessibility service is inspecting).

The following snippet shows how to find the element that currently has
accessibility focus:

```kotlin
// Find the node that currently has accessibility focus
// Note: rootInActiveWindow can be null if the window is not available
val root = rootInActiveWindow
if (root != null) {
    val focusedNode = root.findFocus(AccessibilityNodeInfo.FOCUS_ACCESSIBILITY)

    // Do something with focusedNode

    // Always recycle nodes
    focusedNode?.recycle()
    // rootInActiveWindow doesn't need to be recycled, but obtained nodes do.
}
```

The following snippet shows how to move accessibility focus to a specific
element:

```kotlin
// Request that the system give focus to a given node
fun focusNode(node: AccessibilityNodeInfo) {
    node.performAction(AccessibilityNodeInfo.ACTION_ACCESSIBILITY_FOCUS)
}
```

When creating an accessibility service, respect the user's focus state and
avoid stealing focus unless explicitly triggered by a user action.

## Perform gestures

Your service can dispatch custom gestures to the screen, such as swipes, taps,
or multi-touch interactions. To do this, declare
`android:canPerformGestures="true"` in your configuration so that you can use
the `dispatchGesture()` API.

### Simple gestures

To perform simple gestures, start by creating a `Path` object to represent the
movement associated with a given gesture. Then, wrap the `Path` in a
`GestureDescription` to describe the stroke. Finally, call `dispatchGesture`
to dispatch the gesture.

```kotlin
fun swipeRight() {
    // Create a path for the swipe (from x=100 to x=500)
    val swipePath = Path()
    swipePath.moveTo(100f, 500f)
    swipePath.lineTo(500f, 500f)

    // Build the stroke description (0ms delay, 500ms duration)
    val stroke = GestureDescription.StrokeDescription(swipePath, 0, 500)

    // Build the gesture description
    val gestureBuilder = GestureDescription.Builder()
    gestureBuilder.addStroke(stroke)

    // Dispatch the gesture
    dispatchGesture(gestureBuilder.build(), object : AccessibilityService.GestureResultCallback() {
        override fun onCompleted(gestureDescription: GestureDescription?) {
            super.onCompleted(gestureDescription)
            // Gesture finished successfully
        }
    }, null)
}
```

### Continued gestures

For complex interactions (like drawing an L shape or performing a precise
multi-step drag), you can chain strokes together using the `willContinue`
parameter.

```kotlin
fun performLShapedGesture() {
    val path1 = Path().apply {
        moveTo(200f, 200f)
        lineTo(400f, 200f)
    }

    val path2 = Path().apply {
        moveTo(400f, 200f)
        lineTo(400f, 400f)
    }

    // First stroke: willContinue = true
    val stroke1 = GestureDescription.StrokeDescription(path1, 0, 500, true)

    // Second stroke: continues immediately after stroke1
    val stroke2 = stroke1.continueStroke(path2, 0, 500, false)

    val builder = GestureDescription.Builder()
    builder.addStroke(stroke1)
    builder.addStroke(stroke2)

    dispatchGesture(builder.build(), null, null)
}
```

## Audio management

When creating an accessibility service (especially a screen reader), use the
`STREAM_ACCESSIBILITY` audio stream. This lets users control the service volume
independently from the system media volume.

```kotlin
fun increaseAccessibilityVolume() {
    val audioManager = getSystemService(Context.AUDIO_SERVICE) as AudioManager
    audioManager.adjustStreamVolume(
        AudioManager.STREAM_ACCESSIBILITY,
        AudioManager.ADJUST_RAISE,
        0
    )
}
```

Be sure to include the `FLAG_ENABLE_ACCESSIBILITY_VOLUME` flag in your
configuration, either in XML or through `setServiceInfo` at runtime.

## Advanced features

### Fingerprint gestures

On devices running Android 10 (API level 29) or higher, your service can capture
directional swipes on the fingerprint sensor. This is useful for providing
alternative navigation controls.

> [!NOTE]
> **Note:** The `FingerprintGestureController` API was added in Android 10 (API 29). You must check the SDK version before accessing it to prevent crashes on older devices.

Add the following logic to your `onServiceConnected()` method:

```kotlin
// Import: android.os.Build
// Import: android.accessibilityservice.FingerprintGestureController

private var gestureController: FingerprintGestureController? = null

override fun onServiceConnected() {
    // Check if the device is running Android 10 (Q) or higher
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        gestureController = fingerprintGestureController

        val callback = object : FingerprintGestureController.FingerprintGestureCallback() {
            override fun onGestureDetected(gesture: Int) {
                when (gesture) {
                    FingerprintGestureController.FINGERPRINT_GESTURE_SWIPE_DOWN -> {
                        // Handle swipe down
                    }
                    FingerprintGestureController.FINGERPRINT_GESTURE_SWIPE_UP -> {
                        // Handle swipe up
                    }
                }
            }
        }

        gestureController?.registerFingerprintGestureCallback(callback, null)
    }
}
```

### Accessibility button

On devices using software navigation keys, users can invoke your service through
an accessibility button in the navigation bar.

To use this feature, add the `FLAG_REQUEST_ACCESSIBILITY_BUTTON` flag to your
service configuration. Then add the registration logic to your
`onServiceConnected()` method.

> [!CAUTION]
> **Caution:** Don't override `onServiceConnected` a second time. Merge this logic into your existing method.

```kotlin
// Import: android.accessibilityservice.AccessibilityButtonController

override fun onServiceConnected() {
    // ... existing initialization code ...

    val controller = accessibilityButtonController

    controller.registerAccessibilityButtonCallback(
        object : AccessibilityButtonController.AccessibilityButtonCallback() {
            override fun onClicked(controller: AccessibilityButtonController) {
                // Respond to button tap
            }
        }
    )
}
```

### Multilingual text-to-speech

A service that reads text aloud can automatically switch languages if the source
text is tagged with `LocaleSpan`. This lets your service correctly pronounce
mixed-language content without manual switching.

```kotlin
import android.text.Spannable
import android.text.SpannableStringBuilder
import android.text.style.LocaleSpan
import java.util.Locale

// Wrap text in LocaleSpan to indicate language
val spannable = SpannableStringBuilder("Bonjour")
spannable.setSpan(
    LocaleSpan(Locale.FRANCE),
    0,
    spannable.length,
    Spannable.SPAN_EXCLUSIVE_EXCLUSIVE
)
```

When your service processes `AccessibilityNodeInfo`, inspect the `text` property
for `LocaleSpan` objects to determine the correct text-to-speech language.

## Additional resources

To learn more, see the following resources:

### Guides

- [Build accessible apps](https://developer.android.com/guide/topics/ui/accessibility)
- [Accessibility in Jetpack Compose](https://developer.android.com/develop/ui/compose/accessibility)
- [Quick Guide: Accessibility in Compose](https://developer.android.com/develop/ui/compose/quick-guides/content/video/accessibility-in-compose)

### Codelabs

- [Accessibility in Jetpack Compose](https://developer.android.com/codelabs/jetpack-compose-accessibility)

### Views content

- [Create your accessibility service (Views)](https://developer.android.com/guide/topics/ui/accessibility/views/service)