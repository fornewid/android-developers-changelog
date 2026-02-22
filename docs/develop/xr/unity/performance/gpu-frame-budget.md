---
title: https://developer.android.com/develop/xr/unity/performance/gpu-frame-budget
url: https://developer.android.com/develop/xr/unity/performance/gpu-frame-budget
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg)XR Headsets[](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg)Wired XR Glasses[](https://developer.android.com/develop/xr/devices#xr-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Hitting the right frame rate is critical for XR apps, as missing your frame rate targets can cause discomfort and motion sickness for a user.

Here's what you need to achieve:

- **Minimum target** : As part of our[Android XR app quality guidelines](https://developer.android.com/docs/quality-guidelines/android-xr), we recommend aiming for 72fps at a minimum.
- **Ideal target**: 90fps target, which means your app has an 11ms budget per frame.

These frame budgets not only avoid discomfort for users, but they also help your app provide a smooth, comfortable XR experience.