---
title: https://developer.android.com/design/ui/desktop/guides/system/system-bars
url: https://developer.android.com/design/ui/desktop/guides/system/system-bars
source: md.txt
---

When an extended or connected display is available the system UI adapts to a
desktop-like environment.

## Taskbar

In desktop experiences, a taskbar is displayed at the bottom of the screen. Your
app's icon will be shown on the taskbar when it's open. Users can pin apps to
the taskbar.
![Taskbar appears on larger screens like
tablets.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_taskbar.webp)

After an app is pinned, the icon stays in the taskbar even when the app is
closed. Users can long-press or right-click an app icon to access system
features like pinning to the taskbar, adding new windows, and closing the app,
and App Shortcuts defined by your app. They can also access App Shortcuts
defined by your app.
![Picture-in-picture modal on a large
screen.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_pin-app.webp)

## Window header bar

When your app is displayed in a free-form window, Android adds a header bar
containing essential window controls, such as maximize, minimize, and close.
![When windowed and app takes on a header
bar.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_headerbar.webp)

Use the customizable space in the middle of the header bar to display
app-specific content, like navigation elements of your app or global actions
like search.
![Windowed apps take on a header bar for more control.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_headerbar_custom.webp)

Learn how to implement [customizable header insets](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing#customizable_header_insets).