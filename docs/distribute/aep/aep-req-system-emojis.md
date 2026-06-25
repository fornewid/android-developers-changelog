---
title: https://developer.android.com/distribute/aep/aep-req-system-emojis
url: https://developer.android.com/distribute/aep/aep-req-system-emojis
source: md.txt
---

Implement the system-provided emoji font to ensure that emoji rendered within
your app visually match those shown in the default keyboard and other system
surfaces. This consistency provides Android users with a crafted and delightful
experience that matches their device, preventing a sub-premium messaging and
creation experience compared to other platforms.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Emoji rendered in any input fields, such as text boxes or floating text elements, match those shown in the default keyboard of the device or in other system surfaces, such as notifications.
- If the emoji is expandable by way of enlarging the text view, the app uses the highest-available emoji font size for the appropriate surface (e.g. rendering up to 192 pixels by 192 pixels). This ensures crisp UI and parity with other platforms.

## Guideline applicability

This guideline applies:

- To apps that provide a comparable emoji implementation on a non-Android platform.
- To apps that render emoji, including. the following use cases:
  - Apps that send or store text from users for messaging, comments, reviews and more.
  - Apps that send images with text that include emoji.
  - Apps that allow for reacting to content with emoji.
  - Apps that render emoji in an aesthetic display (for example, a wallpaper provider).
- To all form factors on which the app is available.

## Exemptions

There are no exemptions for this guideline.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **System Emoji** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2)
- [Use the Emoji2 library](https://developer.android.com/jetpack/androidx/releases/emoji2)