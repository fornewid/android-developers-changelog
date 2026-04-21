---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-navigation-drawer
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-navigation-drawer
source: md.txt
---

<br />

The [navigation drawer](https://material.io/components/navigation-drawer) component is a slide-in menu that lets users navigate
to various sections of your app. Users can activate it by swiping from the side
or tapping a menu icon.

Consider these three use cases for implementing a navigation drawer:

- **Content organization:** Enable users to switch between different categories, such as in news or blogging apps.
- **Account management:** Provide quick links to account settings and profile sections in apps with user accounts.
- **Feature discovery:** Organize multiple features and settings in a single menu to facilitate user discovery and access in complex apps.

In Material Design, there are two types of navigation drawers:

- **Standard:** Share space within a screen with other content.
- **Modal:** Appears over the top of other content within a screen.

## Results

![](https://developer.android.com/static/develop/ui/compose/images/layouts/material/m3-navigation-drawer.png)
**Figure 1.** A standard navigation drawer (left) and a modal navigation drawer (right).

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_504265100ae01120c9f8aa6e5287923881f65f7e4bc6b06f0aa1c8888205eb6f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a navigation drawer

You can use the [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalNavigationDrawer.composable#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)) composable to implement a
navigation drawer:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_6fc2bf4a5c4529002522f18993692fff7c318b423775d53c0601d1e29989816c.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points

- Use the `drawerContent` slot to provide a [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalDrawerSheet.composable#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and
  provide the drawer's contents.

- `ModalNavigationDrawer` accepts a number of additional drawer parameters.
  For example, you can toggle whether or not the drawer responds to drags with
  the `gesturesEnabled` parameter as in the following example:

  <iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_326707fff222b3b9aeb67dfefa1e3511dca29f4c363591c3234a33732efa8f70.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Control navigation drawer behavior

To control how the drawer opens and closes, use [`DrawerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_0f5f2a9058f2e38fd2e2a71296c988257bccfa54a2e77fb238c57a4b4361164b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points

- Pass a `DrawerState` to `ModalNavigationDrawer` using the `drawerState` parameter.
- `DrawerState` provides access to the [`open`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState#open) and [`close`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState#close) functions, as well as properties related to the current drawer state. These suspending functions require a `CoroutineScope`, which you can instantiate using [`rememberCoroutineScope`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remembercoroutinescope). You can also call the suspending functions in response to UI events.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)