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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a navigation drawer

You can use the [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)) composable to implement a
navigation drawer:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_fd58a9b348f8ac7a553cf0fc54dfbf71513ba6f1736a20ec1f2c925b4f00a30f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points

- Use the `drawerContent` slot to provide a [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and
  provide the drawer's contents.

- `ModalNavigationDrawer` accepts a number of additional drawer parameters.
  For example, you can toggle whether or not the drawer responds to drags with
  the `gesturesEnabled` parameter as in the following example:

  <iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_f08aaa7197b048357d6aec9432c05ef29eebaf014a732b7e4b5dd70fd6faeb19.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Control navigation drawer behavior

To control how the drawer opens and closes, use [`DrawerState`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DrawerState):
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-navigation-drawer_39a9317578fe290758f2af1f440354fa963db01d8fffb7f4d8afd1f0f47c8613.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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