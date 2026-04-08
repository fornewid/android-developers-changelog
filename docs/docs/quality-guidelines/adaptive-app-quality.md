---
title: Adaptive app quality guidelines  |  App quality  |  Android Developers
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Adaptive app quality guidelines Stay organized with collections Save and categorize content based on your preferences.



Devices that can run Android apps come in a variety of form
factors—phones, tablets, foldables, desktops, car displays, TVs,
XR—which represent a wide range of display sizes. Android supports
multiple display modes, including multi-window, multi-display, multi-instance,
and picture-in-picture. Foldable devices can be in various folded states, or
postures, such as tabletop posture or book posture.

![Depiction of the three quality tiers as layers stacked vertically.](/static/images/docs/quality-guidelines/quality_guidelines_header.png)

To ensure your app provides a great user experience regardless of device form
factor, screen size, display mode, or posture, follow the adaptive app
compatibility [checklists](#adaptive_app_compatibility_checklists) and complete
the compatibility [tests](#adaptive_app_compatibility_tests).

The checklists and tests define a comprehensive set of quality requirements for
most types of Android apps. Your app probably doesn't need to meet all of the
requirements. Implement the ones that make sense for your app's use cases.

The adaptive app quality guidelines replace and extend the guidance formerly
provided in the
[large screen app quality guidelines](/docs/quality-guidelines/archive/adaptive/large-screen-app-quality).

As you enhance your app with adaptive capabilities, help users better understand
your app's multi-form-factor experience by updating your app listing on Google
Play. Upload screenshots that show off the app on tablets and foldables. Call
attention to XR features in your app description. For more information and best
practices, see [Google Play Help](https://support.google.com/googleplay/android-developer/answer/9866151).

For examples of optimized and differentiated layouts on screens of all sizes,
see the [adaptive layout gallery](/large-screens/gallery).

## Adaptive app compatibility checklists

The compatibility checklists define criteria to help you assess the level of
support your app provides for adaptive design.

Levels of support include the following:

![Icon for Tier 3 Adaptive Ready](/static/images/docs/quality-guidelines/tier-3/tier_3_icon.svg)

### [TIER 3 (basic) — Adaptive ready](/docs/quality-guidelines/adaptive-app-quality/tier-3)

Your app runs full screen (or full window in multi-window mode) on all devices,
but app layout might not be ideal. The app is not letterboxed; it does not run
in compatibility mode. Users can complete critical task flows but with a less
than optimal user experience. The app provides basic support for external input
devices, including keyboard, mouse, trackpad, and stylus.

![Icon for Tier 2 Adaptive Optimized](/static/images/docs/quality-guidelines/tier-2/tier_2_icon.svg)

### [TIER 2 (better) — Adaptive optimized](/docs/quality-guidelines/adaptive-app-quality/tier-2)

Your app implements layout optimizations for all screen sizes and device
configurations along with enhanced support for external input devices.

![Icon for Tier 1 Adaptive Differentiated](/static/images/docs/quality-guidelines/tier-1/tier_1_icon.svg)

### [TIER 1 (best) — Adaptive differentiated](/docs/quality-guidelines/adaptive-app-quality/tier-1)

Your app provides a user experience designed for the device or display the app
is running on. Where applicable, the app supports multitasking, foldable
postures, drag and drop, and stylus input.

Complete the Tier 2 requirements to enable your app to provide an excellent user
experience on all Android devices. To make your app outstanding on foldables and
large screens such as desktops, complete Tier 1.

## Adaptive app compatibility tests

The compatibility tests help you discover quality issues in your app. You can
combine the tests or integrate groups of tests together in your own test plans.

For layout and UX purposes, test on at least the following device types:

* Foldable (841x701 dp)
* 8-inch tablet (1024x640 dp)
* 10.5-inch tablet (1280x800 dp)
* 13-inch Chromebook (1600x900 dp)

Use the following Android emulators to test adaptive device compatibility:

* Foldable phone — 7.6" Fold-in with outer display
* Tablet — Pixel C 9.94"
* Dual-display foldable — Microsoft Surface Duo

Use the Android [resizable emulator](/about/versions/12/12L/get#resizable-emulator) to test a variety of device
configurations.

## Get started

Select a quality tier and get started making your app adaptive today!

* [![](/static/images/docs/quality-guidelines/tier-3/tier_3_icon.svg)
  Adaptive ready](/docs/quality-guidelines/adaptive-app-quality/tier-3)
* [![](/static/images/docs/quality-guidelines/tier-2/tier_2_icon.svg)
  Adaptive optimized](/docs/quality-guidelines/adaptive-app-quality/tier-2)
* [![](/static/images/docs/quality-guidelines/tier-1/tier_1_icon.svg)
  Adaptive differentiated](/docs/quality-guidelines/adaptive-app-quality/tier-1)

## Archive

Previous versions of the adaptive app quality guidelines:

* [2026-01-21 — Large screen app quality guidelines](/docs/quality-guidelines/archive/adaptive/large-screen-app-quality)

  [ID map — large screen app quality guidelines to adaptive app quality guidelines](/docs/quality-guidelines/archive/adaptive/id-map-ls-adaptive)