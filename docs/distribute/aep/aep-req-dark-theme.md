---
title: https://developer.android.com/distribute/aep/aep-req-dark-theme
url: https://developer.android.com/distribute/aep/aep-req-dark-theme
source: md.txt
---

Implement a comprehensive **dark theme** that reduces luminance by shifting the
UI to dark grays or low tonal values to improve legibility and reduce eye
strain. Your app must automatically adopt the system-wide dark theme preference.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Dark themes must be applied to 100% of the app's screens, overlays, and system-level components like the navigation bar.
- All text and icons must maintain a contrast ratio of at least 4.5:1 against their backgrounds, meeting [WCAG AA accessibility standards](https://www.w3.org/WAI/standards-guidelines/wcag/).
- The app must correctly react to the [`uiMode`](https://developer.android.com/reference/android/content/res/Configuration#uiMode) configuration change when the user toggles dark themes at the system level.

## Guideline applicability

This guideline applies:

- To apps that provide a comparable dark theme experience on a non-Android platform.
- To all form factors on which the app is available.

## Exemptions

There are no exemptions for this guideline.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Dark Theme** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Implement dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme)