---
title: https://developer.android.com/media/platform/integrate-eclipsa-video
url: https://developer.android.com/media/platform/integrate-eclipsa-video
source: md.txt
---

High Dynamic Range (HDR) video delivery on mobile devices often suffers from a
major flaw: visual inconsistency across different panels. When browsing
mixed-content feeds where Standard Dynamic Range (SDR) and HDR elements coexist,
rendering pipelines struggle to balance them. This results in erratic, jarring
transitions and unpredictable brightness spikes.

For content creators, this lack of uniformity compromises artistic intent. An
HDR video meticulously graded on a professional monitor can render with clipped
highlights, washed-out tones, or crushed shadows when viewed on a consumer
device.

Eclipsa video is a modern HDR video standard designed to solve these exact
cross-device ecosystem challenges. Built upon the [SMPTE ST 2094-50
specification](https://github.com/SMPTE/st2094-50), Eclipsa video enables displays to dynamically adapt content
mapping based on both physical hardware capabilities and real-time ambient
lighting conditions. Backed by built-in, zero-configuration integration in
Jetpack Media3 ExoPlayer and standard Camera2 capture pipelines, Eclipsa video
offers mobile engineering teams a zero-cost, friction-free path to implementing
next-generation, hardware-adaptive video streaming that preserves artistic
intent on every screen.

## Technical architecture of SMPTE ST 2094-50

Mobile displays vary drastically in their luminance headroom, the amount of
brightness available above the display's reference white point. When a display's
hardware limitations don't align with an HDR video's mastering requirements,
highlights clip or look dull. A screen's actual headroom and reference white
point change dynamically as ambient light sensors adjust the panel to the
surrounding environment.

SMPTE ST 2094-50 solves this by introducing dual-layered metadata that
ensures visual consistency through two primary pillars:

### The reference white anchor

This establishes a strict baseline that maps the peak brightness of SDR elements
directly to the display's reference white point. Any luminance value exceeding
this anchor is reserved strictly for HDR highlights. This predictable anchoring
mechanism ensures that when SDR and HDR layers are composited together on
screen, they maintain their intended visual relationship without washing each
other out.

### Headroom-adaptive gain curves

Instead of forcing a static tone-mapping curve, creators embed parametric
metadata that instructs the display pipeline exactly how to scale when limited
headroom is available. The standard gives creators the granular flexibility to
choose whether a targeted panel should soft-clip highlights, hard-clip them, or
compress midtones and shadows to actively preserve the finest details in bright
regions.

## Platform support

Platform-level support for Eclipsa video playback and capture is introduced in
Android 17 (API Level 37).

## Implement playback

For standard app development, Media3 ExoPlayer provides out-of-the-box support
for Eclipsa video. When parsing files embedded with SMPTE 2094-50 metadata,
ExoPlayer extracts and applies the metadata seamlessly, requiring no custom
player configurations.

- **Standard player initialization:** To instantiate your player surface, see
  [Overview of Media3 ExoPlayer](https://developer.android.com/media/media3/exoplayer).

- **Track overrides:** If your app programmatically queries or locks specific
  HDR profiles, see [Media3 track selection API](https://developer.android.com/media/media3/exoplayer/track-selection).

We recommend offloading playback pipelines to Jetpack Media3. ExoPlayer natively
handles low-level container extraction, which completely bypasses known
platform-level decoding artifacts present on legacy rendering layers in
Android 16 (API level 36) and lower.

## Implement video capture

To record Eclipsa video from a device, your camera pipeline must be configured
to generate SMPTE 2094-50 metadata by assigning a compatible dynamic range
profile.

After device support is validated using `CameraCharacteristics`, route the
stream to your encoder surface using the
`DynamicRangeProfiles.HLG10_SMPTE_2094_50` profile. For instructions on how to
query and configure dynamic range profiles in camera sessions, see
[HDR video capture](https://developer.android.com/media/camera/camera2/hdr-video-capture).

No explicit codec configuration is required for SMPTE 2094-50 metadata. The
Android media framework automatically attaches and passes the metadata down if
it exists in the active dynamic profile.

## Compatibility and performance considerations

To monitor performance, retrieve the active `Display` object and check for
`LutProperties` on its `overlayProperties` to identify the availability of
hardware-accelerated paths.

For devices that don't have hardware-acceleration capabilities, support for
opting out of Eclipsa video rendering in Exoplayer is in development.

## Additional resources

- [The SMPTE ST 2094-50 specification](https://github.com/SMPTE/st2094-50)
- [HDR Explorer: web app for inspecting SMPTE ST 2094-50 metadata and gain
  curves](https://github.com/webmproject/hdr-explorer)