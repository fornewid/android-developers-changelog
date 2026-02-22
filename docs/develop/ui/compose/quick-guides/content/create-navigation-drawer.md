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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a navigation drawer

You can use the [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)) composable to implement a
navigation drawer:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_d5c2695818add3d1e81c8ac18bb3e50839b31e1fb6e48ac00a796ec81fb99ee5.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points

- Use the `drawerContent` slot to provide a [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and
  provide the drawer's contents.

- `ModalNavigationDrawer` accepts a number of additional drawer parameters.
  For example, you can toggle whether or not the drawer responds to drags with
  the `gesturesEnabled` parameter as in the following example:

  <iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_ab591abe90fa79aac4ce0aefdad60c85128ee9a534e952a1e56fd75e9d0d272b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Control navigation drawer behavior

To control how the drawer opens and closes, use [`DrawerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_a36ad48f85f409deeb84e4c8e378a86bf6ad6720f7d15feb42160b6a140d84f6.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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