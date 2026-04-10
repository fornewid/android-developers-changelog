---
title: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2
source: md.txt
---

Optimized apps fully support all screen types and device states, including state
transitions.

![Depiction of the three quality tiers as layers stacked vertically with the middle tier highlighted.](https://developer.android.com/static/images/docs/quality-guidelines/tier-2/tier_2_header.png)

## Guidelines

Build your app to adapt to all display sizes and device states.

### User interface

| ID | Tests | Description |
|---|---|---|
| Responsive_adaptive_layouts | [T-Layout_Flow](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Layout_Flow) | App has responsive and adaptive layouts designed for all screen sizes. All layouts are responsive (see [Migrate your UI to responsive layouts](https://developer.android.com/guide/topics/large-screens/migrate-to-responsive-layouts)). Implementation of adaptive layouts is determined by [window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes). The app UI can include the following: - Leading‑edge navigation rails that expand on larger window sizes into full navigation panels - Grid layouts that scale the number of columns to accommodate window size changes - Columns of text on large screens - Trailing‑edge panels that are open by default on desktop screen sizes; closed, on smaller screens Create multi-pane layouts (where appropriate) to take advantage of large screen space. See [Canonical layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts). [Activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding) enables activity-based apps to create multi‑pane layouts by displaying activities side by side. |
| UI_Secondary_Elements | [T-Layout_Flow](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Layout_Flow) | Modals, context menus, and other secondary elements are properly formatted on all screen types and device states, for example: - Bottom sheets are not full width on large screens. (Apply a maximum width to avoid stretching.) See [Behavior](https://material.io/components/sheets-bottom#behavior) in [Sheets: bottom](https://material.io/components/sheets-bottom). - Buttons are not full width on large screens. See [Behavior](https://material.io/components/buttons#behavior) in [Buttons](https://material.io/components/buttons). - Text fields and boxes don't stretch to full width on large screens. See [Behavior](https://material.io/components/text-fields#behavior) in [Text fields](https://material.io/components/text-fields). - Small edit menus or modals don't cover the entire screen and maintain context for the user as much as possible. See [Menus](https://material.io/components/menus). - Context menus appear next to the item the user selected. See the "Context menus" topic in [Menus](https://m3.material.io/components/menus/guidelines). - Navigation rails replace navigation bars for better ergonomics on large screens. See [Navigation rail](https://m3.material.io/components/navigation-rail/overview). - Navigation drawers are updated to expanded navigation rails. See [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview). - Dialog boxes are updated to the latest material component. See [Dialogs](https://material.io/components/dialogs). - Images are displayed at a proper resolution and are not stretched or cropped. |
| Touch_Targets | [T-Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Touch_Targets) | Touch targets are least 48dp. See the Material Design [Layout and typography](https://material.io/design/usability/accessibility.html#layout-and-typography) guidelines. |
| Drawable_Focus | [T-Drawable_Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Drawable_Focus) | A focused state is created for custom drawables that are interactive. A custom drawable is any visual UI element not provided by the Android framework. If users can interact with a custom drawable, the drawable must be focusable when the device is not in [Touch Mode](https://developer.android.com/reference/kotlin/android/view/View#touch-mode), and a visual indication of the focused state must be apparent. |

### Keyboard, mouse, and trackpad

| ID | Tests | Description |
|---|---|---|
| Keyboard_Navigation | [T-Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Keyboard_Navigation) | The main task flows in the app support keyboard navigation, including <kbd>Tab</kbd> and arrow key navigation. See [Build more accessible apps](https://developer.android.com/guide/topics/ui/accessibility). |
| Keyboard_Shortcuts | [T-Keyboard_Shortcuts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Keyboard_Shortcuts) | App supports keyboard shortcuts for commonly used actions such as select, cut, copy, paste, undo, and redo. See [Input compatibility](https://chromeos.dev/en/android/input-compatibility). |
| Keyboard_Media_Playback | [T-Keyboard_Media_Playback](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Keyboard_Media_Playback) | Keyboard can be used to control media playback; for example, the <kbd>Spacebar</kbd> plays and pauses media. |
| Keyboard_Send | [T-Keyboard_Send](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Keyboard_Send) | Keyboard <kbd>Enter</kbd> key performs a *send* function in communication apps. |
| Context_Menus | [T-Context_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Context_Menus) | Context menus are accessible by typical mouse and trackpad right‑click (secondary mouse button or secondary tap) behavior. |
| Content_Zoom | [T-Content_Zoom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Content_Zoom) | App content can be zoomed using the mouse scroll wheel (in conjunction with pressing the <kbd>Control</kbd>, or <kbd>Ctrl</kbd>, key) and trackpad pinch gestures. |
| Hover_States | [T-Hover_States](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Hover_States) | Actionable UI elements have hover states (where appropriate) to indicate to mouse and trackpad users that the elements are interactive. |

## Tests

To ensure your app is optimized and responsive to all display configurations,
perform the following tests.

### User interface

| ID | Feature | Description |
|---|---|---|
| T-Layout_Flow | [Responsive_adaptive_layouts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Responsive_adaptive_layouts), [UI_Secondary_Elements](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#UI_Secondary_Elements) | Run the app on devices that have a wide variety of screen sizes, including phones, foldable phones, small and large tablets, and desktop devices. Run the app in multi-window mode on the devices. Verify that the app layout responds and adapts to different screen and window sizes. Check whether the app expands and contracts navigation rails, scales the number of columns in grid layouts, flows text into columns, and so forth. Observe whether UI elements are formatted for both aesthetics and function. For apps using activity embedding, test whether activities are displayed side by side on large screens, stacked on small screens. |
| T-Touch_Targets | [Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Touch_Targets) | Verify that touch targets maintain a consistent, accessible size and position and are not hidden or obscured by other UI elements for all display sizes and configurations. For information on accessibility, see the [Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor). |
| T-Drawable_Focus | [Drawable_Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Drawable_Focus) | On each app screen that contains an interactive custom drawable, verify that the drawable can be focused using an external keyboard, D‑pad, or other device that enables UI elements to be focused. Verify that a visual indication of the focused state is apparent. For related information, see [Touch Mode](https://developer.android.com/reference/kotlin/android/view/View#touch-mode). |

### Keyboard, mouse, and trackpad

| ID | Feature | Description |
|---|---|---|
| T-Keyboard_Navigation | [T-Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#T-Keyboard_Navigation) | Navigate through the app's focusable components using the Tab and arrow keys of an external keyboard. |
| T-Keyboard_Shortcuts | [Keyboard_Shortcuts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Keyboard_Shortcuts) | Use keyboard shortcuts on an external keyboard to perform select, cut, copy, paste, undo, and redo actions. |
| T-Keyboard_Media_Playback | [Keyboard_Media_Playback](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Keyboard_Media_Playback) | Use an external keyboard to start, stop, pause, rewind, and fast forward media playback. |
| T-Keyboard_Send | [Keyboard_Send](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Keyboard_Send) | Use the <kbd>Enter</kbd> key of an external keyboard to send or submit data. |
| T-Context_Menus | [Context_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Context_Menus) | Use the secondary mouse button or trackpad secondary tap capability to access the context menu of interactive elements. |
| T-Content_Zoom | [Content_Zoom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Content_Zoom) | Use the mouse scroll wheel (in conjunction with the <kbd>Control</kbd>, or <kbd>Ctrl</kbd>, key) and trackpad pinch gestures to zoom content in and out. |
| T-Hover_States | [Hover_States](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2#Hover_States) | Hover the mouse or trackpad cursor over actionable UI elements to activate the element's hover state. |