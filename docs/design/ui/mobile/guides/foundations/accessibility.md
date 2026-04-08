---
title: https://developer.android.com/design/ui/mobile/guides/foundations/accessibility
url: https://developer.android.com/design/ui/mobile/guides/foundations/accessibility
source: md.txt
---

# Accessibility

![Greenish decorative hero image design](https://developer.android.com/static/images/design/ui/mobile/accessibility-hero.png)

According to a [2011 report by the World Health Organization (WHO) and the
World Bank](https://www.who.int/teams/noncommunicable-diseases/sensory-functions-disability-and-rehabilitation/world-report-on-disability), approximately 15% of the global population--that is,
about one in six people--experience a significant or temporary disability in
their lifetime. Accessibility in design, then, is *fundamental* to creating an
inclusive, usable, and high-quality app--it leads to the best results for users
and can prevent costly rework. Android ships with a variety of features to help
you build your app to support accessibility options by default.  

## Design for vision

Ensure your app's content is as legible as possible by checking color contrast
and text sizing, and that components are visually comprehensible and easy to
discern from each other.

Follow these guidelines to design for vision accessibility.

- To allow users to adjust the font size, specify font size in [scalable pixels
  (sp)](https://developer.android.com/training/multiscreen/screendensities#TaskUseDP)
- Don't make the body size any smaller than 12 sp. This guideline aligns with the Material typescale as a default.
- Ensure the contrast between the background and text is at least 4.5:1. [Learn
  how to check color contrast](https://codelabs.developers.google.com/color-contrast-accessibility#0).
- Use a 3:1 ratio between surfaces and non-text elements. For example, the ratio of a background to an icon would be 3:1.
- Use more than one visual affordance for actions like links.

Use Material's [Accessible color system](https://m3.material.io/styles/color/the-color-system/accessibility). This color system is
based on tonal palettes, and is central to making color schemes accessible by
default.
![There are two blocks of text. The first
block is colored dark olive while second text block is colored dark grey.
Both are overlaid on a very dark (almost black) background. Callouts to
the dark olive text indicate that it is in the 'primary30' tone, and that
it fails the ratio test at 1.83:1. Callouts to the grey text indicate
that it's in the 'neutral40' tone and that it still fails the ratio test
at a ratio of 2.65:1.](https://developer.android.com/static/images/design/ui/mobile/accessibility-text-fail-color-contrast.png) **Figure 1:**Example of text failing color contrast

## Design for sound

[TalkBack](https://support.google.com/accessibility/android/answer/6283677) is a Google screen reader included on Android devices
that gives users eyes-free control. You can manually test this by [exploring
your app with TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#explore_your_app_with_talkback) or with the [A11y scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor).

Follow these guidelines to ensure your app is prepared for screen readers:

- [Describe UI elements](https://developer.android.com/guide/topics/ui/accessibility/apps#describe-ui-element) in your code. Compose uses [Semantics
  properties](https://developer.android.com/jetpack/compose/semantics#properties) to inform accessibility services about the information shown in UI elements.
- To satisfy Android framework requirements, provide additional textual description of icons and images.
- Set decorative item descriptions to null.
- To allow skipping between blocks of actions and content, consider UI granularity and group UI elements..

Check out Material's [Design to Implementation Walk](https://m3.material.io/foundations/accessible-design/design-to-implementation), which
walks you through accessibility considerations and notation using Web Content
Accessibility Guidelines (WCAG).
![](https://developer.android.com/static/images/design/ui/mobile/accessibility-ui-elements-labeled.png) **Figure 2:**UI elements labeled for accessibility: heading, hiding decorative image, and button label

## Design for audio

Android provides features to enable users to interact with their devices through
a variety of voice commands and queries.

The [Voice Access](https://support.google.com/accessibility/android/answer/6151848) app for Android lets you control your device
with spoken commands. Use your voice to open apps, navigate, and edit text
hands-free.

## Design for motor skill

[Switch Access](https://support.google.com/accessibility/android/answer/6122836) lets users interact with your Android device
using one or more devices, which can be helpful for users with limited dexterity
who have trouble interacting directly with a touch screen.

Manually test by [exploring switch access](https://developer.android.com/guide/topics/ui/accessibility/testing#explore_your_app_using_switch_access).

- Don't rely on gestures to complete all actions; [create accessibility
  actions](https://developer.android.com/guide/topics/ui/accessibility/principles#accessibility-actions) to support all user flows in your app.
- Ensure all touch targets are at least 48 dp, even if this extends past the UI element visual.
- Consider [haptic feedback](https://developer.android.com/develop/ui/views/haptics/haptics-principles) to help inform the user with additional, real-time sensory input.

<br />

![The UI on the left lets the user delete only by swiping,
while the UI on the right also provides an additional affordance in the form
of a trash icon button.](https://developer.android.com/static/images/design/ui/mobile/accessibility-motor-skill.png) **Figure 3:**The UI on the left lets the user delete only by swiping, while the UI on the right also provides an additional affordance in the form of a trash icon button.

<br />