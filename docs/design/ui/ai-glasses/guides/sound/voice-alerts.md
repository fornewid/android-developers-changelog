---
title: https://developer.android.com/design/ui/ai-glasses/guides/sound/voice-alerts
url: https://developer.android.com/design/ui/ai-glasses/guides/sound/voice-alerts
source: md.txt
---

Voice alerts are vocal sound messages. Most voice alerts should be preceded
with an [earcon](https://developer.android.com/design/ui/ai-glasses/guides/sound/earcons) to let the user
know the system is about to speak. Because they're typically accompanied by an
earcon, voice alerts should also follow the [audio focus
patterns](https://developer.android.com/design/ui/ai-glasses/guides/sound/audio-input).

Voice alerts provide clarity that can't be provided by an earcon alone, like a
unique interaction or state change. For example, a lost connection or closing
translation.

If an interaction is performed on mobile and affects the glasses experience,
like mute, play an earcon but forgo the voice alert. For example, muting a Meet
call from the phone.


![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_block_dont.webp)

### Don't

Block experience with voice alert. Voice alerts that might interrupt an experience, like 'muting a call', should be used sparingly and prioritize brevity.

<br />

## Information readout

If an app is paused or lacks frequent audio output, an Information readout
updates users when tapping the glasses. This keeps users informed without
needing to recall recent app activity or assuming it stopped. On audio
glasses, tapping the touchpad triggers a status readout or play and pause
instead of holding Gemini or agents.

## Generic

Generic voice alerts don't benefit from a unique voice, they exist purely to
help the user understand the state of the audio app. Generic voice alerts take
advantage of the default text-to-speech solutions.

Use the standard system voice for consistency when possible to reduce cognitive
load and feel more premium and considered.

The following are examples of generic voice alerts:


![Having trouble connecting to the internet.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_connect.webp) **Notifying the user of connection issues.** ![Check your exercise states.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_educate.webp) **Education type alert to inform the user of possible actions.**

<br />


![Resuming cooking voice alert.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_resume.webp) **Focus change alert to inform the user an activity has resumed.** ![Welcome to Google Maps voice alert.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_start.webp) **An audio splash to welcome the user to an app.**

<br />

## Bespoke

These voices are unique and core to the audio experience. It's important to
allow these to be custom and branded to heighten the audio experience. Bespoke
voice alerts use a custom text-to-speech implementation.

Use a branded voice only when it matters. Leverage bespoke voices for high
impact \& distinct shifts in experience.


![Aap kaise hain? From glasses How are you?](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_bespoke_translate.webp) **Illustrating a translation experience.** ![Now close your eyes and imagine a river rushing through a dense forest.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_bespoke_meditation.webp) **Illustrating a meditation experience.**

<br />

## What makes a good voice alert?

When designing and writing for your app's voice alerts, consider the following:

### Use a non-technical and personal style

Write your app's voice in a consistent, concise, conversational, and helpful
style. Consider starting with an active verb for actions to help direct users
clearly.

Action starts with the active verb, *"Starting...", "Closing..."*
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_technical_do.webp)

### Do

Use non-technical language. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_technical_dont.webp)

### Don't

Use technical terms, even for sake of brevity. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_direct_do.webp)

### Do

Speak to the user directly, with 'you' type language. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_direct_dont.webp)

### Don't

Write voice alerts to reference themselves, or use 'I' or 'We' wording.

### Balance brevity with clarity

Common voice alerts shouldn't disrupt the user's experience, meaning a good
brief message is better than a perfect and exact, but long message. More
uncommon use cases can benefit from more explanation to help avoid cognitive
overload or to leave the user guessing a solution. Consider what information is
needed to proceed.


![Aap kaise hain? From glasses How are you?](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_bespoke_translate.webp) **Illustrating a translation experience.** ![Now close your eyes and imagine a river rushing through a dense forest.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_use_bespoke_meditation.webp) **Illustrating a meditation experience.**

<br />


![Voice alert notifying the user 'Mic off'.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_frequent.webp) Frequent voice alerts prioritize brevity to avoid disturbing the core experience. ![You're not connected to the Internet. Reconnect, or select one of your downloaded languages in Google Translate to continue offline.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_infrequent.webp) Infrequent voice alerts that require explanation should prioritize clarity

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_info_do.webp)

### Do

Deliver only the information that's needed to proceed. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_info_dont.webp)

### Don't

Get in the user's way with too much explanation or try to troubleshoot lengthy processes.

### Consider the user's environment

Voice alerts on display and audio glasses need to contend with the user's
environment and multidevice use cases. For example, they might need to start or
end a user flow on their phone.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_device_do.webp)

### Do

Consider multidevice experiences. Call out when something happens on the phone versus wearable. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_device_dont.webp)

### Don't

Assume the user is only using their glasses when creating voice alerts.

### Follow error writing best practices

Voice alerts should follow standard [UX writing](https://m3.material.io/foundations/content-design/style-guide/ux-writing-best-practices) methodology, especially with
error messages.errors. Offer possible solutions by explaining why and how to
resolve them. If a problem can be resolved with another attempt, encourage the
user to do so. Don't write in a playful or mocking tone when an error occurs.

![Voice alert with error message.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_sound_principle_error.webp)