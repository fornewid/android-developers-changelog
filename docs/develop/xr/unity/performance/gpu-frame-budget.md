---
title: Plan a GPU frame budget  |  Android Developers
url: https://developer.android.com/develop/xr/unity/performance/gpu-frame-budget
source: html-scrape
---

* [Develop](https://developer.android.com/develop)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Plan a GPU frame budget Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

Hitting the right frame rate is critical for XR apps, as missing your frame rate
targets can cause discomfort and motion sickness for a user.

Here's what you need to achieve:

* **Minimum target**: As part of our [Android XR app quality guidelines](/docs/quality-guidelines/android-xr),
  we recommend aiming for 72fps at a minimum.
* **Ideal target**: 90fps target, which means your app has an 11ms budget per
  frame.

These frame budgets not only avoid discomfort for users, but they also help your
app provide a smooth, comfortable XR experience.

[Previous

arrow\_back

Overview](/develop/xr/unity/performance)

[Next

Adjust OpenXR Feature settings for optimal performance

arrow\_forward](/develop/xr/unity/performance/openxr-feature-settings)