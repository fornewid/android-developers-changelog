---
title: https://developer.android.com/design/ui/ai-glasses/guides/sound/bespoke-earcon
url: https://developer.android.com/design/ui/ai-glasses/guides/sound/bespoke-earcon
source: md.txt
---

![Hero image of a sound wave intro illustration](https://developer.android.com/static/images/design/ui/glasses/guides/hero_sound_bespoke.png)

Interested in creating your own custom earcons for your app? This guide will
help you create and introduce custom earcons with Android sound design best
practices.

Every earcon should be:

- Immediate \& Legible: Instantly distinguishable from background environmental noise.
- Acoustically Polite: Harmonious with everyday life, avoiding startle reflexes or ear fatigue.
- DSP-Aware: Thoughtfully structured to prevent distortion when processed by onboard hardware amplifiers and limiters.

## Ergonomics

Ear fatigue is the primary failure mode of wearable audio. What sounds subtle on
studio monitors can become irritating after 50 daily repetitions near the ear.

- Apply a smooth high-shelf filter to roll off frequencies above 8 kHz. Sharp
  near-ear transients cause rapid listener fatigue.

- Provide softened, filtered alternate assets for high-frequency interactions.
  For example, volume.

- If an earcon triggers repeatedly within a narrow window, consider suppressing
  secondary triggers or transition to a minimal click, like continuous paging.

## Audio file support

When delivering audio files, lean and efficient assets work best. Here are some
parameters to achieve a quality audio asset.

| Parameter | Specification |
|---|---|
| Format | .ogg (Ogg Vorbis) |
| Bit Depth \& Sample Rate | 16-bit / 48 kHz (or 44.1 kHz) |
| Asset Size Limit | \< 1 MB (Uncompressed) |
| Headroom Ceilings | -3.0 dB to -6.0 dB True Peak |
| Channel Format | Stereo / Binaural / Mono |

## Mental models

Because there are no visual indicators, users rely entirely on auditory
intuition to construct mental models of the operating system. The user should
feel that the obvious answer is the right one. Use the existing mental
model understanding to develop a language that the user will immediately
recognize.
Ascending pitch trajectories are often associated with positivity. Think of a
happy major scale upward, these sounds can be paired with positive interactions
to enforce such mental models.

Similarly, a descending trajectory evokes finality, which can pair with
negative, decreasing, or dismissal actions.

While pitch trajectories are powerful, you should use caution when solely
relying on them when conveying critical state changes as they can be lost in a
noisy environment. Instead pitch motion and rhythmic patterning can be used. For
example, success can be conveyed with two rapid ascending chimes or a warning
can use a staccato descending pulse. Ensure related actions share sound language
consistency.

## Spectral design

To ensure clear communication in diverse auditory environments without causing
cognitive overload or physical discomfort, we recommend aligning earcon
frequency distribution across three primary spectral bands:

| Spectral Region | Frequency Range |
|---|---|
| Gentle High-Pass Filtering | \< 100 Hz |
| Target Audibility Band | 2 kHz -- 5 kHz |
| High-Shelf Roll-Off | \> 8 kHz |

Concentrate the core melodic and transient energy in the target audibility band.
The human ear exhibits peak sensitivity here, allowing cues to remain distinctly
intelligible without raising the master volume.

Use crisp attack envelopes so cues register instantly through background
chatter, traffic, or media playback.

Use synthetic, intentional waveforms (sine, clean FM, crystalline bells) rather
than naturalistic or organic samples (wood, paper, snaps). Organic textures
blend into real-world ambient sounds and create confusion.

Onboard DSP adds saturation during playback. Starting with clean, pure
fundamentals (sine waves or low-order harmonics) ensures clean, pristine
output on physical hardware.

## Duration targets

Because the glasses are being used in everyday scenarios, it's important to
keep the environment clean and avoid noise fatigue. Interactions need to be
thought through with the background of ambient sound from the outside
environment.

| Category | Target Duration | Example |
|---|---|---|
| Micro-Interactions | 15 ms---60 ms | Short, crisp interactions. |
| Confirmations | 80 ms---220 ms | Slightly longer, with a clear beginning and end. |
| State Alerts | 250 ms---500 ms | Longer, with a clear beginning and end. |
| Hero Moments | 500 ms --- 1000 ms | Longer, with a clear beginning and end. |