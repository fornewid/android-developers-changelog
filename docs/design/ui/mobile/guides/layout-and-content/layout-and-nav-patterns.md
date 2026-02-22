---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns
source: md.txt
---

If your app contains multiple destinations for users to traverse, we recommend
employing layout and navigation pairings that are commonly used by other apps.
Because many users already possess the mental models for these pairings, your
app will be more intuitive for them.

## Layout and navigation pairings

The navigation bar and modal navigation drawer are used as primary navigation
patterns for parent layout views and primary navigation destinations.  
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-18-primary-navigation-destinations.png)  

The navigation bar can hold three to five navigation destinations across the
same hierarchy level. This component translates to the navigation rail for large
screens.


Although the navigation drawer can hold more than five navigation destinations,
the pattern is not as ideal as the navigation bar.
This is due to the need to reach to the top bar on compact sizes.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-19-tabs-secondary.png)  

[Material 3 Tabs](https://m3.material.io/components/tabs/overview) and the [bottom app bar](https://m3.material.io/components/bottom-app-bar/overview) are
secondary navigation patterns that you can can use to supplement primary
navigation or appear on children views.


Here, tabs act as a secondary navigation layer to group sibling content.

## Layout actions

Provide controls to enable users to accomplish actions. Common patterns include
top bar actions, floating action button (FAB), and menus.  

For actions of the highest importance, a [FAB](https://m3.material.io/components/floating-action-button/overview) provides a large
and prominent button for the user. Provide only one action at a time at this
level. A FAB can appear in multiple sizes and an expanded form, which includes a
label. Use [Scaffold](https://developer.android.com/jetpack/compose/components/scaffold) to pin a FAB, making sure it's always
visible even on scroll by.


A floating action button (FAB) that allows the
user to quickly add plants to the plant gallery
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-20-FAB-provided.png)

You can place secondary actions within the top bar or, if it's grouped near
related content, within the page.
![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-21-alert-action.png) **Figure 20:** Alert action in the top bar on show detail (left) and overflow icon inline of list item (right)

For any additional actions that aren't promptly or frequently needed, add those
actions in an overflow menu.