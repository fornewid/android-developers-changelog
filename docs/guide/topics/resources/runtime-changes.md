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
[`Configuration`](https://developer.android.com/reference/kotlin/android/content/res/Configuration) object.

> [!NOTE]
> **Note:** Connecting or disconnecting external peripherals and multi-tasking are more common on [large screen devices](https://developer.android.com/large-screens) such as tablets, foldables, or ChromeOS. Configuration changes can occur more often in those devices due to their flexibility.

These parameters usually require large enough changes to your application's UI
that the Android platform has a purpose-built mechanism for when they change.
This mechanism is *`Activity` recreation*.

## Activity recreation

The system recreates an `Activity` when a configuration change occurs. To do
this, the system calls [`onDestroy`](https://developer.android.com/reference/kotlin/android/app/Activity#ondestroy) and destroys the existing `Activity`
instance. It then creates a new instance using [`onCreate`](https://developer.android.com/reference/kotlin/android/app/Activity#onCreate(android.os.Bundle)), and this new
`Activity` instance is initialized with the new, updated configuration. This
also means that the system also recreates the UI with the new configuration.

Typically, the `Activity` acts as a host for composables. When the `Activity` is
recreated, Compose also recreates your UI using the new configuration values.

The recreation behavior helps your application adapt to new configurations by
automatically reloading your application with alternative resources that match
the new device configuration.

### Recreation example

Consider a composable that displays a static title using a string resource:


```kotlin
// In the res/values/strings.xml file
// <string name="compose">Jetpack Compose</string>

// In your Compose code
Text(
    text = stringResource(R.string.compose)
)
```

<br />

When the `Activity` is created, the `Text` composable reads the current
configuration (such as language) and resolves the appropriate string resource.

If the language changes, the system recreates the activity. When this happens,
Compose recreates the UI. Because `stringResource` reads from the current
configuration, the title automatically updates to the correct localized value.

The recreation also clears out any state kept as fields in the
`Activity`.

To preserve your UI state across configuration changes, use recommended state
management patterns. Use `ViewModel` for data and business logic, and use
`rememberSaveable` for UI-level state. With these mechanisms, your state
survives `Activity` recreation while the UI updates to reflect the new
configuration.

For more information about saving state in Compose, see
[Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving).

> [!NOTE]
> **Note:** `Activity` recreation due to configuration changes is only one of the cases in which the system might destroy an `Activity` and recreate it later. For more information, read about the [`Activity` lifecycle](https://developer.android.com/guide/components/activities/intro-activities#mtal).

## User expectations

The user of an app expects state to be preserved. If a user is filling out a
form and opens another app in [multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) to reference information,
it is a bad user experience if they return to a cleared form or to somewhere
else in the app entirely. As a developer, you must provide a consistent user
experience through configuration changes and activity recreation.

To verify whether state is preserved in your application, you can perform
actions that cause configuration changes both while the app is in the foreground
and while it is in the background. These actions include:

- Rotating the device
- Entering multi-window mode
- Resizing the application while in multi-window mode or a free-form window
- Folding a foldable device with multiple displays
- Changing the system theme, such as dark mode versus light mode
- Changing the font size
- Changing the system or app language
- Connecting or disconnecting a hardware keyboard
- Connecting or disconnecting a dock

> [!NOTE]
> **Note:** Historically, you could prevent some of these configuration changes by restricting supported aspect ratios and orientations or disabling resizing. In Android 12L (API level 32) and higher, an app that has added these restrictions enters a [compatibility mode](https://developer.android.com/guide/practices/enhanced-letterboxing) if it does not directly support the current device state. If an app has added these restrictions to avoid `Activity` recreation, make sure that the app functions correctly and that it does not lose state when unlocking those restrictions to make full use of the screen on all devices.

There are several approaches you can take to preserve relevant state through
`Activity` recreation. Which to use depends on the type of state you want to
preserve:

- [Local persistence](https://developer.android.com/topic/libraries/architecture/saving-states#local) to handle process death for complex or large data. Persistent local storage includes databases or [`DataStore`](https://developer.android.com/topic/libraries/architecture/datastore).
- [Retained objects](https://developer.android.com/topic/libraries/architecture/saving-states#viewmodel) such as [`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel) instances to handle UI-related state in memory while the user is actively using the app.
- [`rememberSaveable`](https://developer.android.com/develop/ui/compose/state-saving) to preserve transient UI state across configuration changes and system-initiated process death. This is appropriate for state that depends on user input, scroll position, or navigation but doesn't belong in a `ViewModel`.

To read about the APIs for each of these in detail,
and when using each is appropriate, see [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).

## Restrict activity recreation

You can prevent automatic activity recreation for certain configuration changes.
In modern Compose-only apps, your UI is recomposed either way, but it's
recommended to handle the configuration change directly.

By default, a configuration change forces the system to destroy and recreate
the Activity, including the UI and any objects derived from the Activity. If
you declare that your Activity handles the configuration change itself, the
system prevents this. Instead, only the `Configuration` object updates, and
Compose recomposes your UI with the new values.

Handling configuration changes directly in Compose has several benefits:

- **Improved performance:** Recomposing the UI is less expensive than a full Activity recreation cycle, especially for minor changes.
- **Fluid animations:** Avoiding an Activity restart lets you run continuous animations across configuration changes, such as smooth layout transitions during device rotation.
- **State preservation:** Retaining the Activity instance reduces the risk of transient UI state loss during an event like screen rotation. Note that you must still handle state preservation for system-initiated process death.

To disable activity recreation for particular configuration changes,
add the configuration type to `android:configChanges` in the
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) entry in your `AndroidManifest.xml` file. Possible values
appear in the documentation for the [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config) attribute.

The following manifest code disables `Activity` recreation for `MyActivity` when
the screen orientation and keyboard availability change:

    <activity
        android:name=".MyActivity"
        android:configChanges="orientation|screenSize|screenLayout|keyboardHidden"
        android:label="@string/app_name">

> [!WARNING]
> **Warning:** Even when you disable activity recreation for a given configuration change, the change itself continues to occur. Disabling `Activity` recreation transfers the responsibility of handling that configuration change to the `Activity`. Your Compose UI automatically recomposes with the new configuration, but you must update any other code relying on the configuration. Specifically, you must manually update embedded components like `AndroidView` and `AndroidFragment`, which rely on `Activity` recreation to refresh their resources.

## React to configuration changes

Jetpack Compose lets your app more easily react to configuration changes.
However, if you disable `Activity` recreation for all configuration changes
where it is possible to do so, your app still must correctly handle
configuration changes.

The [`Configuration`](https://developer.android.com/reference/kotlin/android/content/res/Configuration) object is available in the Compose UI hierarchy with
the [`LocalConfiguration`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalConfiguration()) composition local. Whenever it changes,
composable functions reading from `LocalConfiguration.current` recompose. For
information about how composition locals work, see [Locally scoped
data with CompositionLocal](https://developer.android.com/jetpack/compose/compositionlocal).

> [!IMPORTANT]
> **Important:** As discussed in the [Restrict `Activity` recreation](https://developer.android.com/guide/topics/resources/runtime-changes#restrict-activity) section, it is impossible to entirely disable `Activity` recreation in an Android app, so it is still necessary to save state correctly when the system recreates an `Activity`. In addition, views embedded in Compose with the [interoperability APIs](https://developer.android.com/jetpack/compose/interop/interop-apis), such as `AndroidView`, can expect `Activity` recreation to occur on configuration changes. While a composable function recomposes due to a configuration change, views used inside the interoperability APIs aren't recreated.  
>
> Before disabling `Activity` recreation altogether, consider whether you can achieve your solution by preserving UI state using `rememberSaveable` or `ViewModel` and reading configuration values when needed using `LocalConfiguration`.

### Example

In the following example, a composable displays a date with a specific format.
The composable reacts to system locale configuration changes by calling
[`ConfigurationCompat.getLocales`](https://developer.android.com/reference/kotlin/androidx/core/os/ConfigurationCompat#getLocales(android.content.res.Configuration)) with `LocalConfiguration.current`.

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

To avoid `Activity` recreation when the locale changes, the `Activity` hosting
the Compose code needs to opt out of locale configuration changes. To do so, you
set `android:configChanges` to `locale|layoutDirection`.

> [!WARNING]
> **Warning:** For composable functions to recompose, the read state must be of type [`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State). This is the case with configuration-related composition locals and `LocalConfiguration` in particular. Attempting to read the current locale in Compose using `Locale.getDefault` doesn't cause the composable to recompose and doesn't react to configuration changes. This is because it's not of type `State`. For more information about state in Compose, see [State and Jetpack
> Compose](https://developer.android.com/jetpack/compose/state).

## Configuration changes: Key concepts and best practices

These are the key concepts you need to know when working on configuration
changes:

- **Configurations:** Device configurations define how the UI displays to the user, such as app display size, locale, or system theme. In Compose, you can access configuration values using `LocalConfiguration`.
- **Configuration changes:** Configurations change through user interaction. For example, the user might change device settings or how they physically interact with the device. There's no way to prevent configuration changes.
- **`Activity` recreation:** Configuration changes result in `Activity` recreation by default. This is a built-in mechanism to re-initialize app state for the new configuration.
- **`Activity` destruction:** `Activity` recreation causes the system to destroy the old `Activity` instance and create a new one in its place. The old instance is now obsolete. Avoid retaining references to lifecycle-scoped objects beyond their intended scope.
- **State:** State in the old `Activity` instance is not present in the new `Activity` instance, because they are two different object instances. Instead of tying state to the Activity, use recommended APIs to preserve the app and user's state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).
- **Opt-out:** Opting out of activity recreation for a type of configuration change requires that your app properly update in reaction to the new configuration. For most Compose apps, this isn't recommended.

To provide a good user experience, observe the following best practices:

- **Be prepared for frequent configuration changes:** Don't assume that configuration changes are rare or never happen, regardless of API level, form factor, or UI toolkit. When a user causes a configuration change, they expect apps to update and continue to work correctly with the new configuration.
- **Preserve state:** Don't lose the user's state when `Activity` recreation occurs. Preserve the state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states) using APIs such as `ViewModel` and `rememberSaveable`.
- **Avoid opting out as a quick fix:** Don't opt out of `Activity` recreation as a shortcut to avoid state loss. Opting out of activity recreation requires you to fulfill the promise of handling the change, and you can still lose the state due to `Activity` recreation from other configuration changes, process death, or closing the app. It is impossible to entirely disable `Activity` recreation. Preserve the state as described in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).
- **Don't avoid configuration changes:** Don't put restrictions on orientation, aspect ratio, or resizability to avoid configuration changes and `Activity` recreation. This negatively impacts users who want to use your app in their preferred way.

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
[`Activity.onConfigurationChanged`](https://developer.android.com/reference/kotlin/android/app/Activity#onconfigurationchanged). Any composables reading
`LocalConfiguration.current` automatically recompose to reflect the new size.

> [!IMPORTANT]
> **Important:** In Android 12 (API level 31) and Android 12L (API level 32), `Activity.onConfigurationChanged` is called only when the change is significant. This is a bug that was fixed in later API versions.

`Activity` recreation is disabled for size-based configuration changes when
you have
`android:configChanges="screenSize|smallestScreenSize|orientation|screenLayout"`
in your manifest file.

## Additional resources

For more information about handling configuration changes, see the following
additional resources:

### Documentation

- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)

### Views content

- [Handle configuration changes (Views)](https://developer.android.com/topic/architecture/views/resources/runtime-changes-views)