---
title: Tier 2 — Adaptive optimized  |  App quality  |  Android Developers
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Tier 2 — Adaptive optimized Stay organized with collections Save and categorize content based on your preferences.



Optimized apps fully support all screen types and device states, including state
transitions.

![Depiction of the three quality tiers as layers stacked vertically with the middle tier highlighted.](/static/images/docs/quality-guidelines/tier-2/tier_2_header.png)

## Guidelines

Build your app to adapt to all display sizes and device states.

### User interface

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Responsive\_adaptive\_layouts | [T-Layout\_Flow](#T-Layout_Flow) | App has responsive and adaptive layouts designed for all screen sizes. All layouts are responsive (see [Migrate your UI to responsive layouts](/guide/topics/large-screens/migrate-to-responsive-layouts)). Implementation of adaptive layouts is determined by [window size classes](/develop/ui/compose/layouts/adaptive/window-size-classes).  The app UI can include the following:   * Leading‑edge navigation rails that expand on larger window sizes into full navigation panels * Grid layouts that scale the number of columns to accommodate window size changes * Columns of text on large screens * Trailing‑edge panels that are open by default on desktop screen sizes; closed, on smaller screens   Create multi-pane layouts (where appropriate) to take advantage of large screen space. See [Canonical layouts](/develop/ui/compose/layouts/adaptive/canonical-layouts).  [Activity embedding](/develop/ui/views/layout/activity-embedding) enables activity-based apps to create multi‑pane layouts by displaying activities side by side. |
| UI\_Secondary\_Elements | [T-Layout\_Flow](#T-Layout_Flow) | Modals, context menus, and other secondary elements are properly formatted on all screen types and device states, for example:   * Bottom sheets are not full width on large screens. (Apply a maximum width to avoid stretching.) See [Behavior](https://material.io/components/sheets-bottom#behavior) in [Sheets: bottom](https://material.io/components/sheets-bottom). * Buttons are not full width on large screens. See [Behavior](https://material.io/components/buttons#behavior) in [Buttons](https://material.io/components/buttons). * Text fields and boxes don't stretch to full width on large screens. See [Behavior](https://material.io/components/text-fields#behavior) in [Text fields](https://material.io/components/text-fields). * Small edit menus or modals don't cover the entire screen and maintain context for the user as much as possible. See [Menus](https://material.io/components/menus). * Context menus appear next to the item the user selected. See the "Context menus" topic in [Menus](https://m3.material.io/components/menus/guidelines). * Navigation rails replace navigation bars for better ergonomics on large screens. See [Navigation rail](https://m3.material.io/components/navigation-rail/overview). * Navigation drawers are updated to expanded navigation rails. See [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview). * Dialog boxes are updated to the latest material component. See [Dialogs](https://material.io/components/dialogs). * Images are displayed at a proper resolution and are not stretched or cropped. |
| Touch\_Targets | [T-Touch\_Targets](#T-Touch_Targets) | Touch targets are least 48dp. See the Material Design [Layout and typography](https://material.io/design/usability/accessibility.html#layout-and-typography) guidelines. |
| Drawable\_Focus | [T-Drawable\_Focus](#T-Drawable_Focus) | A focused state is created for custom drawables that are interactive. A custom drawable is any visual UI element not provided by the Android framework. If users can interact with a custom drawable, the drawable must be focusable when the device is not in [Touch Mode](/reference/kotlin/android/view/View#touch-mode), and a visual indication of the focused state must be apparent. |

### Keyboard, mouse, and trackpad

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Keyboard\_Navigation | [T-Keyboard\_Navigation](#T-Keyboard_Navigation) | The main task flows in the app support keyboard navigation, including `Tab` and arrow key navigation. See [Build more accessible apps](/guide/topics/ui/accessibility). |
| Keyboard\_Shortcuts | [T-Keyboard\_Shortcuts](#T-Keyboard_Shortcuts) | App supports keyboard shortcuts for commonly used actions such as select, cut, copy, paste, undo, and redo. See [Input compatibility](https://chromeos.dev/en/android/input-compatibility). |
| Keyboard\_Media\_Playback | [T-Keyboard\_Media\_Playback](#T-Keyboard_Media_Playback) | Keyboard can be used to control media playback; for example, the `Spacebar` plays and pauses media. |
| Keyboard\_Send | [T-Keyboard\_Send](#T-Keyboard_Send) | Keyboard `Enter` key performs a *send* function in communication apps. |
| Context\_Menus | [T-Context\_Menus](#T-Context_Menus) | Context menus are accessible by typical mouse and trackpad right‑click (secondary mouse button or secondary tap) behavior. |
| Content\_Zoom | [T-Content\_Zoom](#T-Content_Zoom) | App content can be zoomed using the mouse scroll wheel (in conjunction with pressing the `Control`, or `Ctrl`, key) and trackpad pinch gestures. |
| Hover\_States | [T-Hover\_States](#T-Hover_States) | Actionable UI elements have hover states (where appropriate) to indicate to mouse and trackpad users that the elements are interactive. |

## Tests

To ensure your app is optimized and responsive to all display configurations, perform the following tests.

### User interface

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Layout\_Flow | [Responsive\_adaptive\_layouts](#Responsive_adaptive_layouts), [UI\_Secondary\_Elements](#UI_Secondary_Elements) | Run the app on devices that have a wide variety of screen sizes, including phones, foldable phones, small and large tablets, and desktop devices. Run the app in multi-window mode on the devices.  Verify that the app layout responds and adapts to different screen and window sizes. Check whether the app expands and contracts navigation rails, scales the number of columns in grid layouts, flows text into columns, and so forth. Observe whether UI elements are formatted for both aesthetics and function.  For apps using activity embedding, test whether activities are displayed side by side on large screens, stacked on small screens. |
| T-Touch\_Targets | [Touch\_Targets](#Touch_Targets) | Verify that touch targets maintain a consistent, accessible size and position and are not hidden or obscured by other UI elements for all display sizes and configurations. For information on accessibility, see the [Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor). |
| T-Drawable\_Focus | [Drawable\_Focus](#Drawable_Focus) | On each app screen that contains an interactive custom drawable, verify that the drawable can be focused using an external keyboard, D‑pad, or other device that enables UI elements to be focused. Verify that a visual indication of the focused state is apparent. For related information, see [Touch Mode](/reference/kotlin/android/view/View#touch-mode). |

### Keyboard, mouse, and trackpad

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Keyboard\_Navigation | [Keyboard\_Navigation](#Keyboard_Navigation) | Navigate through the app's focusable components using the Tab and arrow keys of an external keyboard. |
| T-Keyboard\_Shortcuts | [Keyboard\_Shortcuts](#Keyboard_Shortcuts) | Use keyboard shortcuts on an external keyboard to perform select, cut, copy, paste, undo, and redo actions. |
| T-Keyboard\_Media\_Playback | [Keyboard\_Media\_Playback](#Keyboard_Media_Playback) | Use an external keyboard to start, stop, pause, rewind, and fast forward media playback. |
| T-Keyboard\_Send | [Keyboard\_Send](#Keyboard_Send) | Use the `Enter` key of an external keyboard to send or submit data. |
| T-Context\_Menus | [Context\_Menus](#Context_Menus) | Use the secondary mouse button or trackpad secondary tap capability to access the context menu of interactive elements. |
| T-Content\_Zoom | [Content\_Zoom](#Content_Zoom) | Use the mouse scroll wheel (in conjunction with the `Control`, or `Ctrl`, key) and trackpad pinch gestures to zoom content in and out. |
| T-Hover\_States | [Hover\_States](#Hover_States) | Hover the mouse or trackpad cursor over actionable UI elements to activate the element's hover state. |