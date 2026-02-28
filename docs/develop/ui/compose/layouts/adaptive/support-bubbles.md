---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-bubbles
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-bubbles
source: md.txt
---

Bubbles is a windowing mode feature that offers a new floating UI experience
similar to the [messaging bubbles API](https://developer.android.com/develop/ui/views/notifications/bubbles). Users can create an app bubble on
their phone, foldable, or tablet by long-pressing an app icon on the launcher.
![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/Bubbles.gif) **Figure 1.** Bubbling the calendar app

On large screens, there is a bubble bar as part of the taskbar where users can
organize, move between, and move bubbles to and from anchored points on the
screen.

This experience is available to all apps that comply with the existing best
practices for [multi-window support](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode). Developers should follow the guidelines
for supporting multi-window mode to make their app work correctly as a bubble.