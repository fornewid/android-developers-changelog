---
title: Surfaces  |  AI Glasses  |  Android Developers
url: https://developer.android.com/design/ui/ai-glasses/guides/surfaces/overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [AI Glasses](https://developer.android.com/design/ui/ai-glasses)
* [Guides](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)

# Surfaces Stay organized with collections Save and categorize content based on your preferences.



When designing for AI Glasses, it's crucial to consider various surfaces and
contexts. These include the Glasses System UI (Home and Notifications), your app
projected on Glasses, and the seamless handoff experience integrated within your
mobile application.

Design surfaces can be described in three states: Home, App view, and system
bar.

### Home

Inspired by the phone's lock screen, [home](/design/ui/ai-glasses/guides/surfaces/sysui) acts as a familiar base for your
user. It provides minimal, contextual information and actions.

![An existing mobile app that hasn't been modified to adapt to a large screen or
any other form
factor.](/static/images/design/ui/glasses/guides/glasses_surfaces_overview_home.png)

### App view

The [app view](/design/ui/ai-glasses/guides/surfaces/app) is the canvas for your app's UI. The system bar is empty by
default to allow for system alerts to be less intrusive for the user's line of
sight.

![A large screen Tier 1 or Tier 2 Android app that has implemented layout
optimizations for all screen sizes and device configurat
ions.](/static/images/design/ui/glasses/guides/glasses_surfaces_overview_nonhome.png)

### System bar

[System bar](/design/ui/ai-glasses/guides/surfaces/sysui) elements temporarily display as needed. This can include Gemini,
Notifications, system alerts, device controls, etc.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on
XR.](/static/images/design/ui/glasses/guides/glasses_surfaces_overview_anytime.png)

## Customize system surfaces

Customization is limited for interface surfaces, while system UI utilizes
templated APIs for a visually cohesive and unobtrusive user experience in
real-world settings and effortless developer experience. Content on notification
extensions must follow system-defined templates, allowing only minimal brand
accents for consistency.

System icons are a color branding opportunity.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on
XR.](/static/images/design/ui/glasses/guides/glasses_surfaces_overview_customize.png)

[Previous

arrow\_back

Get started](/design/ui/ai-glasses/guides/foundations/get-started)

[Next

System UI

arrow\_forward](/design/ui/ai-glasses/guides/surfaces/sysui)