---
title: Keyboard interaction  |  Desktop experience  |  Android Developers
url: https://developer.android.com/design/ui/desktop/guides/interaction/keyboard
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Desktop experience](https://developer.android.com/design/ui/desktop)
* [Guides](https://developer.android.com/design/ui/desktop/guides/foundations/design-principles)

# Keyboard interaction Stay organized with collections Save and categorize content based on your preferences.



In desktop experiences, physical keyboards enable more than just typing—they are
key to app efficiency and accessibility.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/desktop/guides/desktop_ixd_keyboard.webp)

## Takeaways when adapting to desktop inputs

1. Your users should be able to navigate conveniently with only a keyboard.
2. Consider efficiency actions that could translate to keyboard shortcuts.

## Keyboard navigation

Physical keyboards and D-pads enable desktop navigation and are especially
important for users with limited reach and dexterity.

The Tab key should cycle through all interactive elements of your app in the
logical reading order, typically top-to-bottom and left-to-right, automatically
adapting to right-to-left for RTL languages.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/desktop/guides/desktop_ixd_keyboard_focus.webp)

Arrow keys should navigate through all interactive elements directionally. For
example, the Right arrow moves focus to the next item in a row and the Down
arrow moves focus to the next row.

In specific contexts like modal dialogs, keyboard navigation should stay within
the dialog, preventing focus from moving to the underlying page. Allow users to
dismiss the focused element using the Escape key.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/desktop/guides/desktop_ixd_esc.webp)

## Component interaction

Adhere to component-specific navigation patterns. For example, when keyboard
focus lands on a slider, users expect the Left and Right arrow keys to adjust
the value rather than moving focus to the next element. For component-specific
navigation guidance, read more on [ARIA Authoring Practices Guide: Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/).

While the Android framework automatically handles most keyboard navigation, you
may need to manage focus manually for a seamless user experience. For
design guidance, learn more on [inputs](https://m3.material.io/foundations/interaction/inputs) and [input compatibility on large
screens](/develop/ui/compose/touch-input/input-compatibility-on-large-screens) for implementation details.

Whenever possible, set the initial keyboard focus to a UI element that serves an
important use case in your app, such as a search bar or primary action button.
This reduces keystrokes and improves navigation efficiency.

Users should be able to identify which element holds focus by applying distinct
and consistent focus styles to all interactive elements in your app. For design
guidance, learn more at [states](https://m3.material.io/foundations/interaction/states/overview).

Allow users to dismiss temporary UI elements, such as dialogs,
menus, and bottom sheets, by pressing the Escape key, which acts strictly as a
local 'cancel' command.

## Keyboard shortcuts

Use physical keyboards to support standard and custom shortcuts. This meets
user expectations for common actions and accelerates productivity.

To help users discover available commands and view system and app shortcuts in a
unified location, integrate your app with Android's built-in Keyboard Shortcuts
Helper. For implementation details, [Keyboard Shortcuts Helper](/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper).

![](/static/images/design/ui/desktop/guides/desktop_ixd_keyboard-shortcut.webp)


**Figure 3.** Shortcuts let users efficiently complete
actions.

For design guidance on keyboard interactions, read more on [inputs](https://m3.material.io/foundations/interaction/inputs#9dc04cea-5f5b-4922-b9c5-22fcc0c9d501).

[Previous

arrow\_back

Cursors](/design/ui/desktop/guides/interaction/cursors)

[Next

System bars

arrow\_forward](/design/ui/desktop/guides/system/system-bars)