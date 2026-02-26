---
title: https://developer.android.com/develop/xr/unity/performance/audio
url: https://developer.android.com/develop/xr/unity/performance/audio
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Adjust the following performance-related Unity settings and follow these
guidelines to prevent audio-related impacts on your app's performance.

- Limit simultaneous audio sources to avoid CPU spikes.
- Enable spatial audio only on nearby sounds - use panning for distant sounds to reduce CPU load.
- Avoid streaming from compressed Asset Bundles (even with LZ4) when dealing with music. The decompression overhead will cause high, spikey CPU usage that severely impacts performance.
- In your Unity's project's audio settings, enable **Load in Background** and
  set the **Load type** to **Decompress on Load** to force the audio to
  pre-load.

  ![Unity settings for optimizing audio performance](https://developer.android.com/static/images/develop/xr/unity/performance/audio-performance-settings.png)