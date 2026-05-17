---
title: https://developer.android.com/develop/adaptive-apps/guides/chromeos/build-adaptive-apps-for-chromeos
url: https://developer.android.com/develop/adaptive-apps/guides/chromeos/build-adaptive-apps-for-chromeos
source: md.txt
---

ChromeOS devices, such as Chromebooks, provide a unique desktop-like environment
for Android apps. Users expect apps to behave like desktop applications,
featuring resizable windows, robust keyboard and mouse support, and
high-productivity layouts.

## Key considerations for ChromeOS

- **Desktop windowing** : Apps on ChromeOS typically run in free-form windows that can be resized, maximized, or tiled. Use [window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) to ensure your app adjusts its layout fluidly as the window dimensions change.
- **Keyboard and mouse input** : Unlike touch-primary devices, ChromeOS centers on physical input. Ensure your app supports:
  - **Keyboard shortcuts**: Common actions (like Ctrl+C/V) and app-specific shortcuts.
  - **Mouse interactions**: Right-click context menus, scroll wheel support, and hover states for interactive elements.
- **Built-in display**: Chromebook displays are often larger than tablets. Take advantage of this space by using multi-pane layouts and expanded navigation components.
- **External displays** : Many ChromeOS users connect their devices to external monitors. Support [connected displays](https://developer.android.com/develop/adaptive-apps/guides/support-connected-displays) to provide a seamless multi-screen experience.

## Adaptation strategies

1. **Optimize for productivity** : Implement [canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts) like list-detail to display more information on a large ChromeOS display, reducing the need for frequent screen transitions.
2. **Handle configuration changes** : Ensure your app [maintains state](https://developer.android.com/develop/adaptive-apps/guides/support-multi-window-mode) during window resizing to prevent data loss or UI resets.
3. **Refine navigation** : Use [`NavigationSuiteScaffold`](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation) to automatically switch to a navigation rail or drawer when the app window is expanded on a desktop screen.

## Learn more

For ChromeOS development guidance, see [ChromeOS devices](https://developer.android.com/chrome-os/intro).