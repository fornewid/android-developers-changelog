---
title: https://developer.android.com/develop/xr/audio-sdk
url: https://developer.android.com/develop/xr/audio-sdk
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Android XR Audio SDK provides high-quality spatial audio rendering and
acoustic simulation for XR apps on Android XR. Powered by an updated Resonance
Audio engine, this SDK lets you render realistic 3D soundscapes, simulate
physical room acoustics based on scene geometry, and precompute high-fidelity
reverb for complex environments.

## Key features

The extension transforms audio from basic stereo panning to a fully-spatialized,
immersive experience that responds dynamically to user movement:

- **Binaural 3D Spatializer** : Renders a standard, mono
  [`AudioSource`](https://docs.unity3d.com/ScriptReference/AudioSource.html) in 3D space with high-fidelity binaural
  rendering:

  - Audio source distance attenuation and directivity customization
  - Audio source spread
  - Occlusion masking
  - Near-field effects
- **Ambisonic Decoder**: Decodes and renders 3-Degrees-of-Freedom (3DOF)
  ambisonic soundfields to recreate complex, prerecorded acoustic
  environments.

- **Dynamic Room Effects**: Simulates early reflections and late reverberation
  based on shoebox-shaped room boundaries and adjustable acoustic materials.

- **Acoustic Reverb Probes**: Employs ray tracing to analyze complex visual
  geometries and bake realistic, performance-friendly reverb configurations
  directly into your scene.

- **Soundfield Recorder**: Captures multiple active, spatialized real-time
  audio sources from your editor session and exports them directly into
  seamless, loopable ambisonic files.

## Get started

Follow these steps to import the package and configure Unity's native audio
engine to use the Android XR Audio pipelines.

### 1. Download and install the package

First, download and install the package:

1. Download the latest package by clicking the following button:

   <button class="devsite-dialog-button button button-primary gc-analytics-event" data-category="xr_audio_sdk" data-label="xr_audio_sdk" data-action="download" data-modal-dialog-id="xr_audio_sdk"> Download Android XR Audio SDK for Unity </button>
2. Open your Unity project.

3. Navigate to **Window \> Package Manager**.

4. Click "**+** " in the top-left corner and select **Add package from
   tarball...**.

5. Select the `com.google.xr.audio.spatializer.tgz` file in your local SDK
   directory.

### 2. Configure Unity project audio settings

To route Unity's audio pipeline through the spatializer:

1. Go to **Edit \> Project Settings \> Audio**.
2. From the **Spatializer Plugin** drop-down, select **Android XR Audio**.
3. From the **Ambisonic Decoder Plugin** drop-down, select **Android XR
   Audio**.

### 3. Route output to the Dedicated Audio Mixer

The plugin requires a specialized mixer to render spatialized outputs:

1. Locate the pre-configured mixer asset at the following file location:

       Packages/Android XR Audio/Resources/AndroidXRAudioMixer.mixer

2. For every active `AudioSource` in your scene that needs spatialization,
   assign its **Output** property to the **Master** group of this
   `AndroidXRAudioMixer`.

> [!IMPORTANT]
> **Important:** Don't manually add an "Android XR Audio Renderer" effect to other custom mixers. The provided `AndroidXRAudioMixer` already contains the single, required master instance.

## Explore optional core components

Optional core components provide supplemental controls for customizing spatial
audio behavior. They aren't strictly required, as the extension can use default
parameter values for spatial audio rendering if these components aren't
attached.

### AndroidXRAudioListener

Extends Unity [`AudioListener`](https://docs.unity3d.com/ScriptReference/AudioListener.html) with global spatial audio
settings and provides an in-editor soundfield recorder to pre-render spatial
sources into ambisonic audio files.

Must coexist on the same [`GameObject`](https://docs.unity3d.com/ScriptReference/GameObject.html) as your active Unity
`AudioListener` (typically your Main Camera or XR Rig).

- **Global Gain (dB)**: Fine-tunes the master output level of all spatialized sources.
- **Occlusion Mask**: Defines the layer mask used for physical raycast checks to calculate sound obstruction.
- **Enable Stereo Speaker Mode**: Forces standard stereo panning. Keep this disabled for headphone-based binaural XR rendering; enable only when outputting to physical, external loudspeakers.

### AndroidXRAudioSource

Extends any spatialized Unity `AudioSource` with additional parameters for
spatial audio sources.

- **Bypass Room Effects**: When checked, the source ignores reflections from local rooms or baked reverb probes.
- **Directivity (Alpha \& Sharpness)**: Shapes the emission pattern of the sound (e.g., creating a highly focused directional cone versus an omnidirectional source).
- **Near Field Effect**: Boosts low frequencies when a spatialized source passes extremely close to the listener's head.
- **Quality Level**: Adjusts rendering overhead from basic Stereo, to Low, up to CPU-intensive High Binaural.

### AndroidXRAudioRoom

Defines a customizable "shoebox" volume to simulate realistic, real-time early
reflections and reverberation.

- **Surface Material Selection**: Map unique materials (such as concrete, glass, plaster, or acoustic tile) to each of the six room boundaries.
- **Reflectivity**: Scales the strength of the initial bounce reflections.
- **Reverb Settings**: Provides direct modifiers for late-stage reverb gain, overall decay time, and high-frequency brightness.

## Try advanced editor tools

Try out the advanced editor tools in this section for specialized use cases.

### Reverb baking

For non-shoebox rooms or complex, organic geometry, use the CPU ray tracer to
precompute highly accurate reverb parameters. Follow these steps to set it up:

1. **Acoustic Material Mapping**:

   1. Go to **Assets \> Create \> Android XR Audio \> Material Map**.
   2. Create an asset that pairs your project's visual Unity Materials with physical acoustic behaviors.
   3. Assign the acoustic materials to corresponding Unity Materials in your scene.
2. **Open the Baking Window** : Navigate to **Android XR Audio \> Reverb Baking**
   and assign your newly-created Material Map.

3. **Place Probes** : Place `AndroidXRAudioReverbProbes` into your scene where
   the user is likely to travel and set their bounding influence zones (like a
   Box or Sphere).

4. **Bake**:

   1. Configure your occlusion layer masks.
   2. Toggle **Visualize Mode** to verify material assignments in the scene view.
   3. Click **Bake**.

   The ray-traced acoustic properties write directly into the probes' runtime
   parameters. Use the Gain, Brightness, and Time parameters on individual
   Reverb Probes to fine-tune reverb behavior.

## Download Android XR Audio SDK for Unity

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By using Android XR Audio SDK for Unity, you agree to the [Google Terms of Service](https://policies.google.com/terms). I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android XR Audio SDK for Unity for Windows </button> [Download Android XR Audio SDK for Unity
for
Windows](https://dl.google.com/arcore/bin/com.google.xr.audio.spatializer/com.google.xr.audio.spatializer-0.3.20251005.tgz)

*com.google.xr.audio.spatializer-0.3.20251005.tgz*