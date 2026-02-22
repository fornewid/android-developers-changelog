---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-snackbar-notification
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-snackbar-notification
source: md.txt
---

<br />

The [snackbar component](https://material.io/components/snackbars) serves as a brief notification that appears at the
bottom of the screen. It provides feedback about an operation or action without
interrupting the user experience. Snackbars disappear after a few seconds. The
user can also dismiss them with an action, such as tapping a button.

Consider these three use cases where you might use a snackbar:

- **Action confirmation:** After a user deletes an email or message, a snackbar appears to confirm the action and offer an "Undo" option.
- **Network status:** When the app loses its internet connection, a snackbar pops up to note that it is now offline.
- **Data submission:** Upon successfully submitting a form or updating settings, a snackbar notes that the change has saved successfully.

## Results

![](https://developer.android.com/static/develop/ui/compose/images/layouts/material/m3-snackbar.png)
**Figure 1.** Snackbar notifications with action.

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21
or higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-snackbar-notification_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a basic snackbar

To implement a snackbar, you first create [`SnackbarHost`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SnackbarHost(androidx.compose.material3.SnackbarHostState,androidx.compose.ui.Modifier,kotlin.Function1)), which includes a
[`SnackbarHostState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarHostState) property. `SnackbarHostState` provides access to the
[`showSnackbar()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarHostState#showsnackbar) function which you can use to display your snackbar.

This suspending function requires a `CoroutineScope` such as with using
[`rememberCoroutineScope`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope) --- and can be called in response to UI events to
show a [`Snackbar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#snackbar) within `Scaffold`.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-snackbar-notification_e31d1222b3685bfd4683f5f64c97f81ece51a04138fe4e7735378d24b0d523dd.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a snackbar with action

You can provide an optional action and adjust the duration of the `Snackbar`.
The `snackbarHostState.showSnackbar()` function accepts additional `actionLabel`
and `duration` parameters, and returns a [`SnackbarResult`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarResult).
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-snackbar-notification_0703d663292119ee691fd2dd46285cc66d641673650ff6fa22e062be3871565a.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

You can provide a custom `Snackbar` with the `snackbarHost` parameter. See the
[`SnackbarHost` API reference docs](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#snackbarhost) for more information.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)