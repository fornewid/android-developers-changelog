---
title: https://developer.android.com/guide/topics/large-screens/user-interface
url: https://developer.android.com/guide/topics/large-screens/user-interface
source: md.txt
---

![Tier 2 adaptive optimized icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-2/tier_2_icon.png)

TIER 2 --- Adaptive optimized
| **Objective:** Make your app [adaptive optimized](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_optimized) by meeting the following user interface requirements of the [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) guidelines:
|
| - [UI:Layouts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Layouts)
| - [UI:Elements](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Elements)
| - [UI:Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Touch_Targets)
| - [UI:Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Focus)

To users, the user interface is the app. The UI determines the user experience,
which determines user satisfaction, app usage, app purchases, customer
retention.

Large screens offer expansive display space for innovative, accommodative UIs
that provide a UX small screens can't replicate.

Optimize your app for large screens by including the following UI elements:

- Navigation rail or navigation drawer
- Large touch targets
- Well-placed menus and dialogs
- Multipane layouts

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

- [About adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive)
- [Canonical layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts)
- [Build responsive navigation](https://developer.android.com/develop/ui/views/layout/build-responsive-navigation)
- [Activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding)