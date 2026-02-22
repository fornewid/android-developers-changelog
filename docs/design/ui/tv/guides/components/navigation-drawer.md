---
title: https://developer.android.com/design/ui/tv/guides/components/navigation-drawer
url: https://developer.android.com/design/ui/tv/guides/components/navigation-drawer
source: md.txt
---

# Navigation drawers are essential components in any TV app as they allow users to access different destinations and features. A navigation drawer is the backbone of the app's information architecture, providing a clear and intuitive way to navigate through the app.

In contrast to the mobile navigation drawer, the navigation drawer on TV has both expanded and collapsed states visible to the user.

![Cover Navigation Drawer](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-navigation-drawer.webp)

## Resources

|      Type      |                                                                                                                                                                                                                                                                   Link                                                                                                                                                                                                                                                                   |  Status   |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Design         | [Design source (Figma)](https://goo.gle/tv-desing-kit)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Available |
| Implementation | [Jetpack Compose (NavigationDrawer)](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary#NavigationDrawer(kotlin.Function2,androidx.compose.ui.Modifier,androidx.tv.material3.DrawerState,kotlin.Function0)) [Jetpack Compose (ModalNavigationDrawer)](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary#ModalNavigationDrawer(kotlin.Function2,androidx.compose.ui.Modifier,androidx.tv.material3.DrawerState,androidx.compose.ui.graphics.Brush,kotlin.Function0)) | Available |

## Highlights

- Destinations are ordered according to user importance, with frequent destinations first and related destinations grouped together.
- A navigation rail is required for both standard and modal navigation drawers when collapsed.

## Variants

There are two type of navigation drawer styles:

1. **Standard navigation drawer**--- Expands to create additional space for navigation, pushing the page content aside.
2. **Modal navigation drawer**--- Appears as an overlay on top of the app's content with a scrim that helps to improve readability when the drawer is expanded.

![Standard Navigation Drawer](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/standard-navigation-drawer.webp)

![Modal Navigation Drawer](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/modal-navigation-drawer.webp)

## Standard navigation drawer

### Anatomy

![Standard navigation drawer anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/standard-navigation-drawer-anatomy.webp)

1. **Top section:**Features the app logo. Serves as a button to switch profiles or to trigger search action. In the collapsed state, only the icon remains visible in the top container.
2. **Navigation item:**Each item in the navigation rail features a combination of an icon and text, with only the icon visible in the collapsed state.
3. **Navigation rail:**The Navigation Rail is a column that shows 3 to 7 app destinations, acting as the main menu. Each destination has a text label and an optional icon, with the option of grouping menu items for better contextuality.
4. **Bottom section:**Can have one to three action buttons, which are ideal for pages like settings, help, or profile.

### Behavior

- **Navigation drawer expansion:**When expanded the standard navigation drawers pushes the page content making space for the expanded version for the navigation.
- **Navigation updates:**Moving from one nav item to another, the page automatically updates to the new destination.

## Modal navigation drawer

### Anatomy

![Modal navigation drawer anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/modal-navigation-drawer-anatomy.webp)

1. **Top section:**Features the app logo. Serves as a button to switch profiles or to trigger a search action. In the collapsed state, only the icon remains visible in the top container.
2. **Navigation item:**Each item in the navigation rail features a combination of an icon and text, with only the icon visible in the collapsed state.
3. **Navigation rail:**Column that shows three to seven app destinations, acting as the main menu. Each destination has a text label and an optional icon, with the option of grouping menu items for better contextuality.
4. **Scrim:**For better readability of navigation item text.
5. **Bottom section:**Can have one to three action buttons, which are ideal for pages like settings, help, or profile.

### Behavior

- **Drawer expansion:**Appears as an overlay on top of the app's content, with a scrim that improves readability when the drawer is expanded.
- **Navigation updates:**Occur when the user selects a navigation item.

### Scrim

For the modal navigation drawer, a scrim behind the drawer ensures the drawer content is readable. You can use a gradient or solid surface behind the navigation drawer to create different variations of the UI.

<br />

![Standard Navigation Drawer](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/gradient-scrim.webp)

Gradient scrim  
![Modal Navigation Drawer](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/solid-scrim.webp)

Solid scrim

<br />

## Spec

![Spec Width](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/spec-width.webp)

![Spec Padding](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/spec-padding.webp)

![Navigation Item Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/nav-item-spec.webp)

## Usage

<br />

### Active Indicator

The active indicator is a visual cue that highlights the navigation drawer destination that is displayed. The indicator is typically represented by a background shape that is visually distinct from the other items in the drawer. The active indicator helps users understand where they are in the app and which destination they are browsing. Ensure that the active indicator is clearly visible and easier to distinguish from the other items in the navigation drawer.  
![Active indicator](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/modal-drawer-selected.webp)

<br />

<br />

### Dividers (optional)

Dividers can be used to separate groups of destinations within the navigation drawer for better organization. However, it's important to use them sparingly as too many dividers can create visual noise and add unnecessary cognitive overload for users.  
![Dividers (optional)](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/dividers.webp)

<br />

### Badges

Badges are visual cues that can be added to navigation items to provide additional information. For example, a badge could be used to indicate the number of new movies available in a streaming app. Use badges sparingly and only when necessary, as they can make the UI appear busy and cluttered. When using badges, ensure that they are clear and easier to understand and that they don't interfere with the user's ability to navigate the app.

<br />

![Badge Expanded](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/badge-expand.webp)

Badge expanded  
![Badge Collapsed](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/badge-collapse.webp)

Badge collapsed

<br />

### Labels

Labels in the navigation drawer should be clear and concise so that they are easier to read.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/labels-do.webp)  
warning

### Caution

If it's impossible to avoid using long labels, truncate the label using an ellipsis.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/label-dont.webp)  
cancel

### Don't

Avoid using long text labels that require wrapping.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/no-icons.webp)  
cancel

### Don't

Avoid creating a navigation drawer without icons, as this can make it difficult for users to navigate the app.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/no-mixing-icons.webp)  
cancel

### Don't

Avoid mixing icon navigation items with non-icon navigation items, as this can make the navigation experience confusing for users.

Navigation drawers are foundational elements that represent your app's hierarchy and should be used to list only five to six primary navigation destinations.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/navigation-count-do.webp)  
check_circle

### Do

Limit the number of main navigation destinations in the navigation drawer to five to six for a better user experience.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/navigation-drawer/navigation-count-dont.webp)  
cancel

### Don't

Avoid adding too many navigation items as this can create a vertical scroll and make it harder for users to navigate the app.