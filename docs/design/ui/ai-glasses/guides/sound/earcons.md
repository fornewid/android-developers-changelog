---
title: https://developer.android.com/design/ui/ai-glasses/guides/sound/earcons
url: https://developer.android.com/design/ui/ai-glasses/guides/sound/earcons
source: md.txt
---

*Earcons*, short for audio icons, provide brief audio cues or feedback to
the user. Glasses provide earcons for common interactions.

Due to their cognitive load to learn, similar to visual icons, make sure to use
earcons thoughtfully. Avoiding contradicting established sounds provided by the
system.

- Avoid earcons that need explanation that could be replaced by natural language phrase.
- Avoid creating custom earcons that mimic system sounds, as they could confuse your users.
- Users commonly learn earcons in context of an action.
- Earcons should be simplified and intuitive.
- Earcons are less descriptive compared to audio alerts.

Your app will pick up mobile earcons as well, so align the earcons used on
glasses and your mobile app to keep the sound landscape consistent and
simplified. For example, share the mute earcon between your app on a phone
and glasses.

## System earcons

Common system-wide sounds are provided by default and should be accounted for in
your app. These can include:


![Having trouble connecting to the internet.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_earcon_touch.webp) Default tap or touch feedback sounds. ![Check your exercise states.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_earcon_notification.webp) Sounds that alert the user about a new notification.

<br />

### Privacy and critical earcons

Critical hardware alerts and privacy earcons take priority over all audio. The
microphone mute functions as a system-controlled privacy chime.

| System sound | Behavior |
|---|---|
| Microphone mute / unmute | System-controlled privacy sound. |
| Critical Low Battery | - Plays at a 20% minimum hardware volume floor - Bypasses DnD - Plays when disconnected from the phone - Completely suppresses all other audio streams, including active phone calls |
| Thermal Overheat Mitigation Triggered | - Plays at a 20% minimum hardware volume floor - Bypasses DnD - Plays when disconnected from the phone - Completely suppresses all other audio streams, including active phone calls |
| Device Disconnected / Link Lost | - Plays at a 20% minimum hardware volume floor - Bypasses DnD - Plays when disconnected from the phone - Completely suppresses all other audio streams, including active phone calls |

### Camera earcons

All camera and shutter earcons are non-mutable system sounds that play at a 60%
minimum hardware volume floor and ignore Do Not Disturb (DnD) to protect
wearer and bystander privacy.

When an app (such as a video-calling, or visual assistance app)
requests access to open the user's front-facing camera stream, the system
plays a non-mutable sequence that warns the user before the camera stream
turns on and allows them to dismiss it if needed:

1. **Stream start sequence** - Non-mutable earcon that warns the user an app is requesting access to open the front-facing camera stream.
2. **3-second countdown** - Audible 3-second countdown indicator before the camera stream turns on, giving the user time to dismiss or cancel camera access if needed.
3. **Stream on** - Plays the non-mutable open-camera-stream earcon when the stream goes live.
4. **Stream off / dismiss** - Unified non-mutable sound played when the camera stream turns off or when the user dismisses the countdown.

## App earcons

Earcons can be found throughout apps, typically with the following functions.
Consider including sounds for these, as they aren't provided by default:

### Generic earcons

**Generic earcons** are standardized sounds, shared between apps to help users
understand a common semantic sound language. You should use the provided sounds
within your app.

| Action | Use | Audio |
|---|---|---|
| App open | An earcon to greet your user as your app opens. A verbal greeting is appropriate if your app is primarily conversational. | [Download audio](https://developer.android.com/static/design/ui/ai-glasses/guides/sound/audio/app_open.ogg) |
| Loading | An earcon to indicate that content is loading. | [Download audio](https://developer.android.com/static/design/ui/ai-glasses/guides/sound/audio/app_loading.ogg) |
| Media mute (App-level) | Optional, app-controlled earcon for muting app audio or media playback (distinct from system-controlled microphone mute). | [Download audio](https://developer.android.com/static/design/ui/ai-glasses/guides/sound/audio/mute.ogg) |
| Media unmute (App-level) | Optional, app-controlled earcon for unmuting app audio or media playback (distinct from system-controlled microphone unmute). | [Download audio](https://developer.android.com/static/design/ui/ai-glasses/guides/sound/audio/unmute.ogg) |
| Error/Announcement | An earcon to indicate that an error has occurred. | [Download audio](https://developer.android.com/static/design/ui/ai-glasses/guides/sound/audio/announcement_alert.ogg) |

Apps don't play exit earcons; keep exit signals limited to optional, spoken
activity wrap-ups. For example, "Hike ended. You walked 2.8 miles."

### Bespoke earcons

**Bespoke earcons** are customized sounds that are unique to your app, not
provided by the system. For example, a branded app start or an orientation sound
on Maps.


### Don't

Over-use earcons for experiential alerts. If an experience, like Maps, has semi-frequent voice alerts which are core to the experience forego earcons to reduce auditory clutter.

<br />

For more information about creating bespoke earcons, read
[design custom sounds](https://developer.android.com/design/ui/ai-glasses/guides/sound/create-bespoke-earcons).