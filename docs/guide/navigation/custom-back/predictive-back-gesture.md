---
title: https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture
url: https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture
source: md.txt
---

![](https://developer.android.com/static/images/about/versions/13/predictive-back-nav-home.gif) **Figure 1.**Mockup of the predictive back gesture look and feel on a phone

Predictive Back, a gesture navigation feature, lets users preview where the
back swipe takes them.

For example, using a back gesture can display an animated preview of
the Home screen behind your app, as presented in the mockup in figure 1.

Starting with Android 15, the developer option for predictive back animations is
no longer available. System animations such as back-to-home, cross-task, and
cross-activity now appear for apps that have opted in to the predictive back
gesture either entirely or at an activity level.

You can [test this back-to-home animation](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#dev-option) (as described in a
following section of this page).

Supporting the predictive back gesture requires updating your app, using the
backward compatible
[`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback) [AppCompat 1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/activity#1.6.0-alpha05)
(AndroidX) or higher API, or using the new [`OnBackInvokedCallback`](https://developer.android.com/reference/android/window/OnBackInvokedCallback)
platform API. Most apps use the backward compatible AndroidX API.

This update provides a migration path to properly intercept back navigation,
which involves replacing back interceptions from [`KeyEvent.KEYCODE_BACK`](https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_BACK)
and any classes with `onBackPressed` methods such as `Activity` and
[`Dialog`](https://developer.android.com/reference/android/app/Dialog#onBackPressed()) with the new system Back APIs.
| **Note:** `KeyEvent.KEYCODE_BACK` is not deprecated as there are some supported use cases of `KeyEvent.KEYCODE_BACK`; however, intercepting back events from `KeyEvent.KEYCODE_BACK` is no longer supported.

#### Codelab and Google I/O video

[Video](https://www.youtube.com/watch?v=Elpqr5xpLxQ)

In addition to using this documentation on this page, [try out our codelab](https://codelabs.developers.google.com/handling-gesture-back-navigation).
It provides a common use-case implementation of a WebView handling the
predictive back gesture using AndroidX Activity APIs.

You can also view our Google I/O video, which covers additional examples of
implementing the AndroidX and platform APIs.

## Update an app that uses default back navigation

Predictive back is enabled by default.

If your app uses Fragments or the Navigation Component, also upgrade to
[AndroidX Activity 1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/activity#1.6.0-alpha05)
or higher.

## Update an app that uses custom back navigation

If your app implements custom back behavior, there are different migration paths
depending on whether it uses AndroidX and how it handles back navigation.

|---|---|---|
| **Your app uses AndroidX** | **How your app handles back navigation** | **Recommended migration path** (link on this page) |
| Yes | AndroidX APIs | [Migrate an existing AndroidX back implementation](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#migrate-existing) |
| Yes | Unsupported platform APIs | [Migrate an AndroidX app containing unsupported back navigation APIs to AndroidX APIs](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#migrate-androidx) |
| No | Unsupported platform APIs, able to migrate | [Migrate an app that uses unsupported back navigation APIs to platform APIs](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#migrate-app) |
| No | Unsupported platform APIs, but unable to migrate | Temporarily opt out by setting the [`android:enableOnBackInvokedCallback`](https://developer.android.com/guide/topics/manifest/activity-element#enabledCallback) attribute to `false` in the `&ltapplication>` or `&ltactivity>` tag of your app's `AndroidManifest.xml` file. |

| **Important:** We strongly recommend that you implement predictive back navigation as soon as possible. Otherwise, users might experience unexpected behavior in a future release of Android.

### Migrate an AndroidX back navigation implementation

This use case is the most common (and the most recommended). It applies to new
or existing apps that implement custom gesture navigation handling with
[`OnBackPressedDispatcher`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher), as described in
[Provide custom back navigation](https://developer.android.com/guide/navigation/navigation-custom-back).

To make sure that APIs that are already using `OnBackPressedDispatcher`
(such as Fragments and the Navigation Component) work seamlessly with the
predictive back gesture, upgrade to
[AndroidX Activity 1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/activity#1.6.0-alpha05).

    ```xml
    // In your build.gradle file:
    dependencies {

    // Add this in addition to your other dependencies
    implementation "androidx.activity:activity:1.6.0-alpha05"
    ```

### Migrate an AndroidX app containing unsupported back navigation APIs to AndroidX APIs

If your app uses AndroidX libraries but implements or makes reference to the
unsupported back navigation APIs, you'll need to migrate to using AndroidX APIs
to support the new behavior.
| **Note:** We strongly recommend using AndroidX libraries. AndroidX automatically enables updated system Back navigation in your app when you enable the feature, and also provides [many other useful features](https://developer.android.com/jetpack/androidx) that automatically update APIs with each release to save you work and time.

To migrate unsupported APIs to AndroidX APIs:

1. Migrate your system Back handling logic to AndroidX's
   [`OnBackPressedDispatcher`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher) with an implementation of
   [`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback). For detailed guidance, see
   [Provide custom back navigation](https://developer.android.com/guide/navigation/navigation-custom-back).

2. Disable the `OnBackPressedCallback` when ready to stop intercepting the back
   gesture.

3. Stop intercepting back events via `OnBackPressed` or
   `KeyEvent.KEYCODE_BACK`.

4. Make sure to upgrade to
   [AndroidX Activity 1.6.0-alpha05](https://developer.android.com/jetpack/androidx/releases/activity#1.6.0-alpha05).

       // In your build.gradle file:
       dependencies {

       // Add this in addition to your other dependencies
       implementation "androidx.activity:activity:1.6.0-alpha05"

   | **Note:** `OnBackPressedCallback` is always called regardless of the value of `android:enableOnBackInvokedCallback`. In other words, disabling the system animation doesn't affect your app's back handling logic if it uses `OnBackPressedCallback`.

### Migrate an app that uses unsupported back navigation APIs to platform APIs

If your app cannot use AndroidX libraries and instead implements or makes
reference to custom Back navigation using the unsupported APIs, you must migrate
to the `OnBackInvokedCallback` platform API.
| **Note:** We strongly recommend using AndroidX libraries. AndroidX automatically enables updated system Back navigation in your app when you enable the feature, and also provides [many other useful features](https://developer.android.com/jetpack/androidx) that automatically update APIs with each release to save you work and time.

Complete the following steps to migrate unsupported APIs to the platform API:

1. Use the new `OnBackInvokedCallback` API on devices running Android 13 or
   higher, and rely on the unsupported APIs on devices running Android 12 or
   lower.

2. Register your custom back logic in `OnBackInvokedCallback` with
   `onBackInvokedDispatcher`. This prevents the current activity from being
   finished, and your callback gets a chance to react to the Back action once
   the user completes the system Back navigation.

3. Unregister the `OnBackInvokedCallback` when ready to stop intercepting the
   back gesture. Otherwise, users may see undesirable behavior when using a
   system Back navigation---for example, "getting stuck" between views and
   forcing them to force quit your app.

   Here's an example of how to migrate logic out of `onBackPressed`:

   ### Kotlin

   ```kotlin
   @Override
   fun onCreate() {
       if (BuildCompat.isAtLeastT()) {
           onBackInvokedDispatcher.registerOnBackInvokedCallback(
               OnBackInvokedDispatcher.PRIORITY_DEFAULT
           ) {
               /**
                * onBackPressed logic goes here. For instance:
                * Prevents closing the app to go home screen when in the
                * middle of entering data to a form
                * or from accidentally leaving a fragment with a WebView in it
                *
                * Unregistering the callback to stop intercepting the back gesture:
                * When the user transitions to the topmost screen (activity, fragment)
                * in the BackStack, unregister the callback by using
                * OnBackInvokeDispatcher.unregisterOnBackInvokedCallback
                * (https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher#unregisteronbackinvokedcallback)
                */
           }
       }
   }
   ```

   ### Java

   ```java
   @Override
   void onCreate() {
     if (BuildCompat.isAtLeastT()) {
       getOnBackInvokedDispatcher().registerOnBackInvokedCallback(
           OnBackInvokedDispatcher.PRIORITY_DEFAULT,
           () -> {
             /**
              * onBackPressed logic goes here - For instance:
              * Prevents closing the app to go home screen when in the
              * middle of entering data to a form
              * or from accidentally leaving a fragment with a WebView in it
              *
              * Unregistering the callback to stop intercepting the back gesture:
              * When the user transitions to the topmost screen (activity, fragment)
              * in the BackStack, unregister the callback by using
              * OnBackInvokeDispatcher.unregisterOnBackInvokedCallback
              * (https://developer.android.com/reference/kotlin/android/view/OnBackInvokedDispatcher#unregisteronbackinvokedcallback)
              */
           }
       );
     }
   }
   ```
4. Stop intercepting back events using `OnBackPressed` or `KeyEvent.KEYCODE_BACK`
   for Android 13 and later.

You can register an `OnBackInvokedCallback` with `PRIORITY_DEFAULT` or
`PRIORITY_OVERLAY`, which is not available in the similar AndroidX
`OnBackPressedCallback`. Registering a callback with `PRIORITY_OVERLAY` is
helpful in some instances.

This applies when you migrate from `onKeyPreIme()` and your callback needs to
receive the back gesture instead of an open IME. IMEs register callbacks with
`PRIORITY_DEFAULT` when opened. Register your callback with `PRIORITY_OVERLAY`
to ensure `OnBackInvokedDispatcher` dispatches the back gesture to your callback
instead of the open IME.

## Opt out of predictive back

To opt out, in `AndroidManifest.xml`, in the `<application>` tag, set the
`android:enableOnBackInvokedCallback` flag to `false`.

    <application
        ...
        android:enableOnBackInvokedCallback="false"
        ... >
    ...
    </application>

Setting this to false does the following:

- Disables the predictive back gesture system animation.
- Ignores `OnBackInvokedCallback`, but `OnBackPressedCallback` calls continue to work.

### Opt out at an activity level

The `android:enableOnBackInvokedCallback` flag lets you opt out of predictive
system animations at the activity level. This behavior makes it more manageable
to migrate large multi-activity apps to predictive back gestures.

The following code shows an example of `enableOnBackInvokedCallback` set to
enable the back-to-home system animation from the `MainActivity`:

    <manifest ...>
        <application . . .

            android:enableOnBackInvokedCallback="false">

            <activity
                android:name=".MainActivity"
                android:enableOnBackInvokedCallback="true"
                ...
            </activity>
            <activity
                android:name=".SecondActivity"
                android:enableOnBackInvokedCallback="false"
                ...
            </activity>
        </application>
    </manifest>

Keep in mind the following considerations when using the
`android:enableOnBackInvokedCallback` flag:

- Setting `android:enableOnBackInvokedCallback=false` turns off predictive back animations either at the activity level or at the app level, depending on where you set the tag, and instructs the system to ignore calls to the `OnBackInvokedCallback` platform API. However, calls to `OnBackPressedCallback` continue to run because `OnBackPressedCallback` is backward compatible and calls the `onBackPressed` API, which is unsupported prior to Android 13.
- Setting the `enableOnBackInvokedCallback` flag at the app level establishes the default value for all activities in the app. You can override the default per activity by setting the flag at the activity level, as shown in the preceding code example.

## Callback best practices

Here are best practices for using the supported system back callbacks;
`BackHandler` (for Compose), `OnBackPressedCallback`, or
`OnBackInvokedCallback`.

### Determine the UI State that enables and disables each callback

[UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state)
is a property that describes the UI. We recommend following these high-level
steps.

1. Determine the UI state that enables and disables each callback.

2. Define that state using an [observable data holder
   type](https://developer.android.com/topic/architecture/ui-layer#expose-ui-state), such as `StateFlow` or
   Compose State, and enable or disable the callback as the state changes.

If your app was previously associating back logic with conditional statements,
this might signify you are reacting to the back event after it has
already occurred. Avoid this pattern with newer callbacks.
If possible, move the callback outside of the conditional statement and instead
associate the callback to an observable data holder type.

### Use system back callbacks for UI Logic

[UI logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#logic)
dictates how to display UI. Use system back callbacks to run UI logic, such as
displaying a dialog or running an animation.

If your app enables an `OnBackPressedCallback` or an `OnBackInvokedCallback`
with `PRIORITY_DEFAULT` or `PRIORITY_OVERLAY`, the predictive back animations
don't run and you must handle the back event. Don't create these callbacks to
run business logic or to log.

Use the following approaches if your app must run business logic or log when the
user swipes back:

- Use `OnBackInvokedCallback` with [`PRIORITY_SYSTEM_NAVIGATION_OBSERVER`](https://developer.android.com/reference/android/window/OnBackInvokedDispatcher#PRIORITY_SYSTEM_NAVIGATION_OBSERVER) on devices running Android 16 and higher. This creates an observer-callback that doesn't consume the back event. For example, you may register this callback when the user swipes back from the root activity, or in other words, when the user has left your app. In this case, you can log the back event or run other business logic, and the back-to-home animation will still play.
- For activity-to-activity cases or fragment-to-activity cases, log if `isFinishing` within `onDestroy` is `true` within the Activity lifecycle.
- For fragment-to-fragment cases, log if `isRemoving` within `onDestroy` is true within the Fragment's view lifecycle. Or log using `onBackStackChangeStarted` or `onBackStackChangeCommitted` methods within `FragmentManager.OnBackStackChangedListener`.
- For the Compose case, log within the `onCleared()` callback of a `ViewModel` associated with the Compose destination. This is the best signal for knowing when a compose destination is popped off the back stack and destroyed.

### Create single responsibility callbacks

You can add multiple callbacks to the dispatcher. The callbacks are added to a
stack in which the last added enabled callback handles the next back gesture
with one callback per back gesture.

It is easier to manage the enabled state of a callback if that callback has a
single responsibility. For example:
![Ordering of callbacks in a stack.](https://developer.android.com/static/guide/navigation/custom-back/callback_stack_diagram.png) **Figure 2.** Callback stack diagram.

Figure 2 shows how you can have multiple callbacks in the stack, each
responsible for one thing. A callback only runs if the callbacks above it
in the stack are disabled. In this example, the "Are you sure..." callback is
enabled when the user enters data into a form, and disabled otherwise.
The callback opens a confirmation dialog when the user swipes back to exit the
form.

The other callback can include a material component that supports predictive
back, an AndroidX transition using the Progress APIs, or another custom
callback.

A `childFragmentManager`'s callback runs if the above callbacks are
disabled and the back stack for this `FragmentManager` isn't empty, where
`childFragmentManager` is attached within a Fragment. In this example, this
internal callback is disabled.

Likewise, `supportFragmentManager`'s internal callback runs if the above
callbacks are disabled and its stack is non-empty. This behavior is consistent
when using either `FragmentManager` or `NavigationComponent` for navigation,
as `NavigationComponent` relies on `FragmentManager`. In this example,
this callback runs if the user didn't enter text into the form causing the
"Are you sure..." callback to be disabled.

Finally, `super.onBackPressed()`is the system-level callback, that again runs if
the above callbacks are disabled. In order to trigger system animations such as
back-to-home, cross-activity, and cross-task, `supportFragmentManager`'s back
stack must be empty so its internal callback is disabled.

## Test the predictive back gesture animation

| **Note:** With Android 15, system animations such as back-to-home, cross-task, and cross-activity are no longer behind the developer option. They now appear for apps that have opted into the predictive back gesture either entirely or at an activity level.

If you still use Android 13 or Android 14, you can test the back-to-home
animation shown in Figure 1.

To test this animation, complete the following steps:

1. On your device, go to **Settings \> System \> Developer options**.

2. Select **Predictive back animations**.

3. Launch your updated app, and use the back gesture to see it in action.