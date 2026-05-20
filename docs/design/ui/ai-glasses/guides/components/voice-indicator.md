---
title: https://developer.android.com/design/ui/ai-glasses/guides/components/voice-indicator
url: https://developer.android.com/design/ui/ai-glasses/guides/components/voice-indicator
source: md.txt
---

Voice input indicator visualizes audio input from the user.

![Voice indicators](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voiceindicator.png)

### Principles

**Clear Feedback**: The indicator provides immediate feedback to show the user
the microphone is receiving input.

**Consistent**: All indicators should share a core visual language to be
instantly recognizable.

## Usage \& Placement

The voice input indicator communicates whether the app is actively accessing
the microphone. The indicator doesn't control the microphone.

Both contained and uncontained indicators can be used independently without any
accompanying surface, like a card.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice_container_do.png)

### Do

Use uncontained indicator on a card or button. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice_container_dont.png)

### Don't

Use indicator with container on colored surface.

**If displayed on a card**


![Align indicator to center of card with 1 to 2 lines.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice-indicator_align-center.png)

<br />

Align the voice input indicator to the vertical center if there are 1 or 2
content rows.

![Align indicator to top of card with 2 or more lines.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice-indicator_align-top.png)

<br />

Anchor the voice input indicator to the top right corner of the card if there
are 2 or more content rows.

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice_color_do.png)

### Do

Use the color to match the app's primary brand color. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice_color_warning.png)

### Warning

Use red for voice input indicator, which is reserved for system-level warning, unless the branding color is red.

## Anatomy

![Progress anatomy](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voice_anatomy.png)

Voice indicator with container and without container

## Customization

The voice indicator container and color can be customized depending on placement
and branding.

<br />

| Properties | Customization | Defaults |
|---|---|---|
| Show container | Yes | False |
| Color | Yes | Primary |

<br />