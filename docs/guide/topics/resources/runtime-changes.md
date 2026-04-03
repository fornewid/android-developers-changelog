---
title: https://developer.android.com/guide/topics/resources/runtime-changes
url: https://developer.android.com/guide/topics/resources/runtime-changes
source: md.txt
---

Some device configurations can change while the app is running. These include,
but aren't limited to:

- App display size
- Screen orientation
- Font size and weight
- Locale
- Dark mode versus light mode
- Keyboard availability

Most of these configuration changes occur due to some user interaction. For
example, rotating or folding the device changes the amount of screen space
available to your app. Likewise, altering device settings like the font size,
language, or preferred theme changes their respective values in the
[`Configuration`](https://developer.android.com/reference/android/content/res/Configuration) object.
| **Note:** Connecting or disconnecting external peripherals and multi-tasking is more common on [large screen devices](https://developer.android.com/large-screens) such as tablets, foldables, or Chrome OS. Configuration changes can occur more often in those devices due to their flexibility.

These parameters usually require large enough changes to your application's UI
that the Android platform has a purpose-built mechanism for when they change.
This mechanism is *`Activity` recreation*.

## Activity recreation

The system recreates an `Activity` when a configuration change occurs. To do this, the system
calls [`onDestroy()`](https://developer.android.com/reference/android/app/Activity#onDestroy()) and destroys the existing `Activity` instance. It then
creates a new instance using [`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)), and this new `Activity` instance is
initialized with the new, updated configuration. This also means that the system
also recreates the UI with the new configuration.

The recreation behavior helps your application adapt to new configurations by
automatically reloading your application with alternative resources that match
the new device configuration.

### Recreation example

Consider a `TextView` that displays a static title using
`android:text="@string/title"`, as defined in a layout XML file. When the view
is created, it sets the text exactly once, based on the current language. If the
language changes, the system recreates the activity. Consequently, the system
also recreates the view and initializes it to the correct value based on the new
language.

The recreation also clears out any state kept as fields in the
`Activity` or in any of its contained `Fragment`, `View`, or other objects. This
is because `Activity` recreation creates a completely new instance of the `Activity`
and the UI. Furthermore, the old `Activity` is no longer visible or valid, so any
remaining references to it or its contained objects are stale. They can cause
bugs, memory leaks, and crashes.
| **Note:** `Activity` recreation due to configuration changes is only one of the cases in which the system might destroy an `Activity` and recreate it later. For more information, read about the [`Activity` lifecycle](https://developer.android.com/guide/components/activities/intro-activities#mtal).

## User expectations

The user of an app expects state to be preserved. If a user is filling out a form
and opens another app in [multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) to reference information, it
is a bad user experience if they return to a cleared form or to
somewhere else in the app entirely. As a developer, you must provide a consistent user experience
through configuration changes and activity recreation.

To verify whether state is preserved in your application, you can perform
actions that cause configuration changes both while the app is in the foreground and
while it is in the background. These actions include:

- Rotating the device
- Entering multi-window mode
- Resizing the application while in multi-window mode or a free-form window
- Folding a foldable device with multiple displays
- Changing the system theme, such as dark mode versus light mode
- Changing the font size
- Changing the system or app language
- Connecting or disconnecting a hardware keyboard
- Connecting or disconnecting a dock

| **Note:** Historically, you could prevent some of these configuration changes by restricting supported aspect ratios and orientations or disabling resizing. In Android 12L (API level 32) and higher, an app that has added these restrictions enters a [compatibility mode](https://developer.android.com/guide/practices/enhanced-letterboxing) if it does not directly support the current device state. If an app has added these restrictions to avoid `Activity` recreation, make sure that the app functions correctly and that it does not lose state when unlocking those restrictions to make full use of the screen on all devices.

There are three primary approaches you can take to preserve relevant state through
`Activity` recreation. Which to use depends on the type of state you want to
preserve:

- [Local persistence](https://developer.android.com/topic/libraries/architecture/saving-states#local) to handle process death for complex or large data. Persistent local storage includes databases or [`DataStore`](https://developer.android.com/topic/libraries/architecture/datastore).
- [Retained objects](https://developer.android.com/topic/libraries/architecture/saving-states#viewmodel) such as [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) instances to handle UI-related state in memory while the user is actively using the app.
- [Saved instance state](https://developer.android.com/topic/libraries/architecture/saving-states#onsaveinstancestate) to handle system-initiated process death and keep transient state that depends on user input or navigation.

To read about the APIs for each of these in detail,
and when using each is appropriate, see [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).

## Restrict activity recreation

You can prevent automatic activity recreation for certain configuration changes.
`Activity` recreation results in recreating the entire UI, and any objects derived
from the `Activity`. You might have good reasons to avoid this. For
example, your app might not need to update resources during a specific
configuration change, or you might have a performance limitation. In that case,
you can declare that your activity handles the configuration change itself and
prevent the system from restarting your activity.

To disable activity recreation for particular configuration changes,
add the configuration type to `android:configChanges` in the
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) entry in your `AndroidManifest.xml` file. Possible values appear in the
documentation for the [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config) attribute.

The following manifest code disables `Activity` recreation for `MyActivity` when
the screen orientation and keyboard availability change:

    <activity
        android:name=".MyActivity"
        android:configChanges="orientation|screenSize|screenLayout|keyboardHidden"
        android:label="@string/app_name">

Some configuration changes always cause the activity to restart. You can't disable
them. For example, you can't disable the [dynamic colors change](https://developer.android.com/develop/ui/views/theming/dynamic-colors)
introduced in Android 12L (API level 32).
| **Warning:** Even when you disable activity recreation for a given configuration change, the change itself continues to occur. Disabling `Activity` recreation transfers the responsibility of handling that configuration change to the `Activity`. If you disable `Activity` recreation, your app must appropriately handle the change when it does occur.

## React to configuration changes in the View system

In the `View` system, when a configuration change occurs for which you have
disabled `Activity` recreation, the activity receives a call to
[`Activity.onConfigurationChanged()`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)). Any attached views also receive a
call to [`View.onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged). For configuration changes you
have not added to `android:configChanges`, the system recreates the activity
as usual.
| **Warning:** In the `View` system, disabling `Activity` recreation can make it much more difficult to use alternative resources. This is because the system no longer applies them for you. In apps built with the `View` system, only disable `Activity` recreation as a last resort when you must avoid restarts due to a configuration change. It is not recommended for most applications.

The `onConfigurationChanged()` callback method receives a
[`Configuration`](https://developer.android.com/reference/android/content/res/Configuration) object that specifies the new device configuration. Read
the fields in the `Configuration` object to determine what your new
configuration is. To make the subsequent changes, update the resources
you use in your interface. When the system calls this method, your activity's
`Resources` object is updated to return resources based on the new
configuration. This lets you reset elements of your UI without the system
restarting your activity.

For example, the following `onConfigurationChanged()` implementation checks
whether a keyboard is available:

### Kotlin

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)

        // Checks whether a keyboard is available
        if (newConfig.keyboardHidden === Configuration.KEYBOARDHIDDEN_YES) {
            Toast.makeText(this, "Keyboard available", Toast.LENGTH_SHORT).show()
        } else if (newConfig.keyboardHidden === Configuration.KEYBOARDHIDDEN_NO) {
            Toast.makeText(this, "No keyboard", Toast.LENGTH_SHORT).show()
        }
    }

### Java

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        // Checks whether a keyboard is available
        if (newConfig.keyboardHidden == Configuration.KEYBOARDHIDDEN_YES) {
            Toast.makeText(this, "Keyboard available", Toast.LENGTH_SHORT).show();
        } else if (newConfig.keyboardHidden == Configuration.KEYBOARDHIDDEN_NO){
            Toast.makeText(this, "No keyboard", Toast.LENGTH_SHORT).show();
        }
    }

If you don't need to update your application based on these configuration
changes, you can instead not implement `onConfigurationChanged()`. In that
case, all the resources used before the configuration change are still used,
and you only avoided the restart of your activity. For example, a TV app
might not want to react when a Bluetooth keyboard is attached or detached.

### Retain state

When you use this technique, you must still retain state during the normal
activity lifecycle. This is because of the following:

- **Unavoidable changes:** configuration changes that you cannot prevent can restart your application.
- **Process death:** your application must be able to handle system-initiated process death. If the user leaves your application and the app goes to the background, the system might destroy the app.

| **Important:** When you disable activity recreation for a configuration change, you are responsible for resetting any elements for which you provide alternatives. For example, if you disable activity recreation for an `Activity` that has images that change between landscape and portrait, you must reassign each resource to each element during [`onConfigurationChanged`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration))().

## React to configuration changes in Jetpack Compose

Jetpack Compose lets your app more easily react to configuration changes.
However, if you disable `Activity` recreation for all configuration changes where it is
possible to do so, your app still must correctly handle
configuration changes.

The [`Configuration`](https://developer.android.com/reference/android/content/res/Configuration) object is available in the Compose UI hierarchy with
the [`LocalConfiguration`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalConfiguration()) composition local. Whenever it changes,
composable functions reading from `LocalConfiguration.current` recompose. For
information about how composition locals work, see [Locally scoped
data with CompositionLocal](https://developer.android.com/jetpack/compose/compositionlocal).
| **Important:** As discussed in the [Restrict `Activity` recreation](https://developer.android.com/guide/topics/resources/runtime-changes#restrict-activity) section, it is impossible to entirely disable `Activity` recreation in an Android app, so it is still necessary to save state correctly when the system recreates an `Activity`. In addition, views embedded in Compose with the [interoperability APIs](https://developer.android.com/jetpack/compose/interop/interop-apis), such as `AndroidView`, can expect `Activity` recreation to occur on configuration changes. Also, if a composable function recomposes due to a configuration change, views used inside the interoperability APIs recompose as well.

### Example

In the following example, a composable displays a date with a specific format.
The composable reacts to system locale configuration changes by calling
[`ConfigurationCompat.getLocales()`](https://developer.android.com/reference/androidx/core/os/ConfigurationCompat#getLocales(android.content.res.Configuration)) with `LocalConfiguration.current`.

    @Composable
    fun DateText(year: Int, dayOfYear: Int) {
        val dateTimeFormatter = DateTimeFormatter.ofPattern(
            "MMM dd",
            ConfigurationCompat.getLocales(LocalConfiguration.current)[0]
        )
        Text(
            dateTimeFormatter.format(LocalDate.ofYearDay(year, dayOfYear))
        )
    }

To avoid `Activity` recreation when the locale changes, the `Activity` hosting the
Compose code needs to opt out of locale configuration changes. To do so, you
set `android:configChanges` to `locale|layoutDirection`.
| **Warning:** For composable functions to recompose, the read state must be of type [`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State). This is the case with configuration-related composition locals and `LocalConfiguration` in particular. Attempting to read the current locale in Compose using `Locale.getDefault()` doesn't cause the composable to recompose and doesn't react to configuration changes. This is because it's not of type `State`. For more information about state in Compose, see [State and Jetpack
| Compose](https://developer.android.com/jetpack/compose/state).

## Configuration changes: Key concepts and best practices

These are the key concepts you need to know when working on configuration
changes:

- **Configurations:** device configurations define how the UI displays to the user, such as app display size, locale, or system theme.
- **Configuration changes:** configurations change through user interaction. For example, the user might change device settings or how they physically interact with the device. There's no way to prevent configuration changes.
- **`Activity` recreation:** configuration changes result in `Activity` recreation by default. This is a built-in mechanism to re-initialize app state for the new configuration.
- **`Activity` destruction:** `Activity` recreation causes the system to destroy the old `Activity` instance and create a new one in its place. The old instance is now obsolete. Any remaining references to it result in memory leaks, bugs, or crashes.
- **State:** state in the old `Activity` instance is not present in the new `Activity` instance, because they are two different object instances. Preserve the app and user's state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).
- **Opt-out:** opting out of activity recreation for a type of configuration change is a potential optimization. It requires that your app properly updates in reaction to the new configuration.

To provide a good user experience, observe the following best practices:

- **Be prepared for frequent configuration changes:** don't assume that configuration changes are rare or never happen, regardless of API level, form factor, or UI toolkit. When a user causes a configuration change, they expect apps to update and continue to work correctly with the new configuration.
- **Preserve state:** don't lose the user's state when `Activity` recreation occurs. Preserve the state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).
- **Avoid opting out as a quick fix:** don't opt-out of `Activity` recreation as a shortcut to avoid state loss. Opting out of activity recreation requires you to fulfill the promise of handling the change, and you can still lose the state due to `Activity` recreation from other configuration changes, process death, or closing the app. It is impossible to entirely disable `Activity` recreation. Preserve the state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).
- **Don't avoid configuration changes:** don't put restrictions on orientation, aspect ratio, or resizability to avoid configuration changes and `Activity` recreation. This negatively impacts users who want to use your app in their preferred way.

## Handle size-based config changes

Size-based configuration changes can happen at any time and are more likely
when your app runs on a [large screen](https://developer.android.com/guide/topics/large-screens/get-started-with-large-screens) device where users can enter
[multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#config). They expect your app to work well in that
environment.

There are two general types of size changes: significant and
insignificant. A *significant* size change is one where a different set of
alternative resources applies to the new configuration due to a difference in
screen size, such as width, height, or smallest width. These resources include
those that the app defines itself and those from any of its libraries.

### Restrict activity recreation for size-based config changes

When you disable `Activity` recreation for size-based configuration changes, the
system doesn't recreate the `Activity`. Instead, it receives a call to
[`Activity.onConfigurationChanged()`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)). Any attached views receive a call to
[`View.onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged).
| **Important:** In Android 12 (API level 31) and Android 12L (API level 32), `Activity.onConfigurationChanged()` is called only when the change is significant. This is a bug that was fixed in future API versions.

`Activity` recreation is disabled for size-based configuration changes when
you have
`android:configChanges="screenSize|smallestScreenSize|orientation|screenLayout"`
in your manifest file.

### Allow activity recreation for size-based config changes

On Android 7.0 (API level 24) and higher, `Activity` recreation *only* occurs for size-based
configuration changes if the size change is significant. When the system doesn't
recreate an `Activity` due to insufficient size, the system might call
[`Activity.onConfigurationChanged()`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)) and
[`View.onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged) instead.

There are some caveats to observe regarding the `Activity` and `View`
callbacks when the `Activity` isn't recreated:

- On Android 11 (API level 30) through Android 13 (API level 33), `Activity.onConfigurationChanged()` isn't called.
- There is a known issue where `View.onConfigurationChanged()` may not be called in some cases on Android 12L (API level 32) and early versions of Android 13 (API level 33). For more information, see [this public issue](https://issuetracker.google.com/issues/247143459). This has since been addressed in later Android 13 releases and Android 14.

For code that is dependent on listening for size-based configuration
changes, we recommend using a utility `View` with an overridden
`View.onConfigurationChanged()` instead of relying on `Activity` recreation or
`Activity.onConfigurationChanged()`.
| **Note:** `Activity` recreation isn't disabled if you have `android:configChanges=""` for the `Activity` in the manifest file. This also occurs with unrelated size-based configuration changes like `android:configChanges="uiMode"`.