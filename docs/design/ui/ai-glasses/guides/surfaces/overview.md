---
title: https://developer.android.com/design/ui/ai-glasses/guides/surfaces/overview
url: https://developer.android.com/design/ui/ai-glasses/guides/surfaces/overview
source: md.txt
---

When designing for AI Glasses, it's crucial to consider various surfaces and contexts. These include the Glasses System UI (Home and Notifications), your app projected on Glasses, and the seamless handoff experience integrated within your mobile application.

Design surfaces can be described in three states: Home, App view, and system bar.

### Home

Inspired by the phone's lock screen,[home](https://developer.android.com/design/ui/ai-glasses/guides/surfaces/sysui)acts as a familiar base for your user. It provides minimal, contextual information and actions.

![An existing mobile app that hasn't been modified to adapt to a large screen or any other form factor.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_surfaces_overview_home.png)

### App view

The[app view](https://developer.android.com/design/ui/ai-glasses/guides/surfaces/app)is the canvas for your app's UI. The system bar is empty by default to allow for system alerts to be less intrusive for the user's line of sight.

![A large screen Tier 1 or Tier 2 Android app that has implemented layout optimizations for all screen sizes and device configurations.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_surfaces_overview_nonhome.png)

### System bar

[System bar](https://developer.android.com/design/ui/ai-glasses/guides/surfaces/sysui)elements temporarily display as needed. This can include Gemini, Notifications, system alerts, device controls, etc.

![An XR differentiated app has a user experience explicitly designed for XR, and it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_surfaces_overview_anytime.png)

## Customizing system surfaces

Customization is limited for interface surfaces, while system UI utilizes templated APIs for a visually cohesive and unobtrusive user experience in real-world settings and easy developer experience. Content on notifications and extensions must follow system-defined templates, allowing only minimal brand accents for consistency.

System icons are a color branding opportunity.

![An XR differentiated app has a user experience explicitly designed for XR, and it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_surfaces_overview_customize.png)