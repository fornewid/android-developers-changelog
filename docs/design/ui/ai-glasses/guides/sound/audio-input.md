---
title: https://developer.android.com/design/ui/ai-glasses/guides/sound/audio-input
url: https://developer.android.com/design/ui/ai-glasses/guides/sound/audio-input
source: md.txt
---

Audio and display glasses route all sound through shared speakers, managed by
Android's audio focus system. When an app starts playback, it requests audio
focus. Concurrent streams seamlessly duck, pause, or stop in the background
without playing audio cues or announcing state changes. [Understand physical
input routing for audio glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/input-routing-audio).

## Choose the behavior that fits your content

The right behavior depends on what the user would lose if they missed part of
your audio. If a few seconds of music sit under a notification, nothing
important is lost. If a sentence of an audiobook gets talked over, the user
loses the story.

- **Music and ambient audio** will duck and keep playing because there's no missed information.
- **Spoken content**, like audiobooks, will pause and rewind the audio, so the user doesn't miss information.
- **Calls, live translation, and agent readouts** need a user's full attention, so other audio interruptions are paused.
- **Short, important updates**, like a navigation update, will duck briefly to the incoming sound.

The system assigns behavior based on the content type assigned. Learn more
about [optimizing audio focus](https://developer.android.com/media/optimize/audio-focus).

### Playing earcons alongside other audio

How an earcon plays over other audio depends on its job. Earcons that confirm
the user's own action are instant and frequent, so they mix on top of whatever
is playing. All other earcons carry information the user needs to hear, so they
duck other audio briefly and then let it return.

### Designing for each behavior

- If your earcon **mixes**, design it to cut through on its own with a clean,
  defined attack, a tight duration and a distinct timbre. Nothing gets out of its
  way, so its character has to do the work.

- If your earcon **ducks**, design it to account for the ducking curve. The
  other audio takes a moment to dip, so a clear start helps the earcon register
  before the dip finishes.

## System Overrides

Certain system events---like privacy indicators, calls, and critical hardware
alerts---always override other audio and app focus. They also have a set of
[earcon and LED behaviors](https://developer.android.com/design/ui/ai-glasses/sound/earcon).

![flow diagram of system override behavior](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_ixd_audio_override.png)