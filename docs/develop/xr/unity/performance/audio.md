---
title: Improve audio performance  |  Android Developers
url: https://developer.android.com/develop/xr/unity/performance/audio
source: html-scrape
---

* [Develop](https://developer.android.com/develop)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Improve audio performance Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

Adjust the following performance-related Unity settings and follow these
guidelines to prevent audio-related impacts on your app's performance.

* Limit simultaneous audio sources to avoid CPU spikes.
* Enable spatial audio only on nearby sounds - use panning for distant sounds
  to reduce CPU load.
* Avoid streaming from compressed Asset Bundles (even with LZ4) when dealing
  with music. The decompression overhead will cause high, spikey CPU usage
  that severely impacts performance.
* In your Unity's project's audio settings, enable **Load in Background** and
  set the **Load type** to **Decompress on Load** to force the audio to
  pre-load.

  ![Unity settings for optimizing audio performance
  ](/static/images/develop/xr/unity/performance/audio-performance-settings.png)

[Previous

arrow\_back

Optimize performance using Unity tools and APIs](/develop/xr/unity/performance/unity-tools)