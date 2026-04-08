---
title: System UI  |  AI Glasses  |  Android Developers
url: https://developer.android.com/design/ui/ai-glasses/guides/surfaces/sysui
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [AI Glasses](https://developer.android.com/design/ui/ai-glasses)
* [Guides](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)

# System UI Stay organized with collections Save and categorize content based on your preferences.



Display AI glasses system UI weaves together with the app and hardware surfaces.
The following are various system UI components to be aware of when designing for
glasses.

### Home

Acts as a familiar base for your user. Can contain a clock, weather,
notifications, and Gemini visual feedback. Home is the lowest layer of the
system. It provides minimal, contextual information and actions, and is inspired
by the phone's lock screen.

* A familiar screen you wake and come back to
* Contextual, glanceable information without requiring any input
* Shortcuts to what you likely want to do next
* Multitasking abilities when multiple activities are running simultaneously

![The home screen on
glasses.](/static/images/design/ui/glasses/guides/glasses_sysui_home.png)

### System bar

The system bar houses Gemini visual feedback and secondary, glanceable
information like notifications, alerts, chips, and the clock. Apps cannot use
this space outside of notifications chips. When not in use, it's invisible
(except for home). Content displayed in the system bar depends on its location
in the system:

* Home
* App view

![The system bar shows device alerts and
notifications.](/static/images/design/ui/glasses/guides/glasses_sysui_systembar.png)

Additionally, there are ephemeral items that can appear "at any time" across
locations. For example: Heads-up Notifications (HUNs), or other locations.

### Notifications

Glasses notifications behave like [mobile notifications](/design/ui/mobile/guides/home-screen/notifications) that need to be
brief, timely, and relevant. These are templated surfaces that can appear in
different states depending on focus and display availability.

![A notification is condensed when it first appears.](/static/images/design/ui/glasses/guides/glasses_surface_sysUI_notifications.png)


Notifications appear in a chip to prevent obstructing the user's view..

![Notificaiton expanding once in focus](/static/images/design/ui/glasses/guides/glasses_surface_sysUI_notifications_expanded.png)


Notifications expand once in focus.

### LEDs

There are two LEDs on all glasses, one for the wearer and one for bystanders.  
The LED provides visual feedback regarding feature and device states and should
be considered when thinking about the holistic user experience. These are system
UI indicators and can't be changed.

![AI Glasses include two
LEDs.](/static/images/design/ui/glasses/guides/glasses_surface_sysui_led.png)

[Previous

arrow\_back

Overview](/design/ui/ai-glasses/guides/surfaces/overview)

[Next

App view

arrow\_forward](/design/ui/ai-glasses/guides/surfaces/app)