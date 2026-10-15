---
title: Bubbles  |  Adaptive Apps  |  Android Developers
url: https://developer.android.com/develop/adaptive-apps/guides/support-bubbles
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
* [Guides](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)

# Bubbles Stay organized with collections Save and categorize content based on your preferences.





Bubbles is a windowing mode feature that offers a new floating UI experience
similar to the [notification bubbles API](/develop/ui/views/notifications/bubbles). Users can create an app bubble on
their phone, foldable, or tablet by long-pressing an app icon on the launcher.

![](/static/develop/ui/compose/images/layouts/adaptive/Bubbles.gif)


**Figure 1.** Bubbling the calendar app

On large screens, there is a bubble bar as part of the taskbar where users can
organize, move between, and move bubbles to and from anchored points on the
screen.

This experience is available to all apps that comply with the existing best
practices for [multi-window support](/develop/ui/compose/layouts/adaptive/support-multi-window-mode). These requirements are listed
explicitly in [App requirements for bubbles](#app-requirements).

## App requirements for bubbles

To enable bubbles, your app must have the following:

* `android:resizeableActivity="true"`

**Note:** `resizableActivity` is set to `true` by default for apps targeting
Android 16 and higher if the screen size width is greater than, or equal to, `600dp`.

To avoid interfering with the app's existing tasks, we also recommend:

* `android:documentLaunchMode="always"`

For more information, see [Multi-window mode configuration](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-window_mode_configuration).