---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

With the Geospatial API in ARCore for Jetpack XR, your app can remotely attach
content to any area covered by Google [Street View](https://www.google.com/streetview/) and
create AR experiences on a global scale. The Geospatial API uses device sensor
and GPS data to detect the device's environment, then matches the recognizable
parts of that environment to a localization model provided by Google's [Visual
Positioning System (VPS)](https://research.google/blog/using-global-localization-to-improve-navigation/) to determine the precise location of a
user's device.

On supported immersive devices, the Geospatial API also merges the user's local
coordinates with the geographic coordinates from VPS so that you can work within
a single coordinate system.

When VPS is able to determine the user's position, it can often offer precise
sub-meter (less than one meter) positional accuracy and sub-degree orientation
accuracy. This level of precision is significantly more accurate than what is
possible with standard GPS alone. Your app can use this precise positioning on
supported devices to create experiences that are tied to the real world.

[Get started with the Geospatial API](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/setup)

> [!NOTE]
> **Note:** The Geospatial API is not available in all regions. The [troubleshooting
> guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/troubleshooting) describes steps you can take to determine whether or not the Geospatial API and VPS are supported in your areas of interest.