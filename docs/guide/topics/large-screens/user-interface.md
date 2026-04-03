---
title: User interface  |  Large screens  |  Android Developers
url: https://developer.android.com/guide/topics/large-screens/user-interface
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Large screens](https://developer.android.com/guide/topics/large-screens)
* [Guides](https://developer.android.com/guide/topics/large-screens/tier-3-overview)

# User interface Stay organized with collections Save and categorize content based on your preferences.




![Tier 2 adaptive optimized icon](/static/images/docs/quality-guidelines/tier-2/tier_2_icon.png)

TIER 2 — Adaptive optimized

**Objective:** Make your app [adaptive optimized](/docs/quality-guidelines/adaptive-app-quality/tier-2) by meeting the following user interface requirements of the [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality):

* [Responsive\_adaptive\_layouts](/docs/quality-guidelines/adaptive-app-quality/tier-2#Responsive_adaptive_layouts)
* [UI\_Secondary\_Elements](/docs/quality-guidelines/adaptive-app-quality/tier-2#UI_Secondary_Elements)
* [Touch\_Targets](/docs/quality-guidelines/adaptive-app-quality/tier-2#Touch_Targets)
* [Drawable\_Focus](/docs/quality-guidelines/adaptive-app-quality/tier-2#Drawable_Focus)

To users, the user interface is the app. The UI determines the user experience,
which determines user satisfaction, app usage, app purchases, customer
retention.

Large screens offer expansive display space for innovative, accommodative UIs
that provide a UX small screens can't replicate.

Optimize your app for large screens by including the following UI elements:

* Navigation rail or navigation drawer
* Large touch targets
* Well-placed menus and dialogs
* Multipane layouts

## Adaptive layouts

Create adaptive layouts that optimize your app's UI on screens large and small.
Design and build for multiple form factors simultaneously. Future-proof your app
for new device types.

## Canonical layouts

Take advantage of proven adaptive layouts to make your app UX exceptional.
Create a list‑detail, supporting pane, or feed layout to make more content
more manageable and more enjoyable.

## Responsive UI

Format UI elements based on display size. Constrain the width of buttons, cards,
and text fields that are full width on small displays to a functionally
appropriate size on large displays. Don't let dialog boxes and other modal
windows fill the entire display. Position context menus and other
element‑related pop‑ups adjacent to the element the user selected,
not centered on screen.

## Activity embedding

Update your activity‑based legacy apps with multipane layouts on large
screens. No code refactoring required. Configure your layouts in XML or with a
few Jetpack WindowManager API calls.

## Next steps

To learn about UI development for optimized UX, see the following developer
guides:

* [About adaptive layouts](/develop/ui/compose/layouts/adaptive)
* [Canonical layouts](/develop/ui/compose/layouts/adaptive/canonical-layouts)
* [Build responsive navigation](/develop/ui/views/layout/build-responsive-navigation)
* [Activity embedding](/develop/ui/views/layout/activity-embedding)