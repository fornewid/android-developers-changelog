---
title: https://developer.android.com/about/dashboards
url: https://developer.android.com/about/dashboards
source: md.txt
---

This page provides information about the relative number of devices on Google Play that share a certain characteristic, such as screen size and density. Each snapshot of data represents all of the active devices during a 7-day period ending on November 24, 2025.

For more robust and granular information to help you make better decisions about which specs to build for, where to launch, and what to test, we recommend using[Reach and devices](https://play.google.com/console/about/reachanddevices/)in the[Google Play Console](https://developer.android.com/static/distribute/console).

With*Reach and devices*, all developers have access to the following:

- Distributions of installs, revenue, and issue rates for your app and for peersets of your choice.
- Data broken out by Android version, RAM, SoC, Vulkan version, OpenGL ES version, screen metrics, and ABI.
- Historical trends.
- CSV exports.

## Vulkan version

This section provides data about the relative number of devices that support a particular version of Vulkan. Devices that lack Vulkan support are represented by None. Note that support for one particular version of Vulkan also implies support for any lower version (for example, support for version 1.1 also implies support for 1.0.3).

To declare which version of Vulkan your application requires, you should create a[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element defining`android.hardware.vulkan.version`. See[`FEATURE_VULKAN_HARDWARE_VERSION`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_VERSION)for more details on the hardware version. You can also use`android.hardware.vulkan.level`to declare a required Vulkan feature level. See[`FEATURE_VULKAN_HARDWARE_LEVEL`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL)for more details on the feature level.

For handheld devices:

| Vulkan Version | Distribution |
|----------------|--------------|
| None           | 7.37%        |
| Vulkan 1.0.3   | 3.86%        |
| Vulkan 1.1     | 62.09%       |
| Vulkan 1.3     | 26.01%       |
| Vulkan 1.4     | 0.67%        |

For all devices:

| Vulkan Version | Distribution |
|----------------|--------------|
| None           | 8.85%        |
| Vulkan 1.0.3   | 3.82%        |
| Vulkan 1.1     | 60.52%       |
| Vulkan 1.3     | 26.22%       |
| Vulkan 1.4     | 0.59         |

*Data collected from active devices running Android API level 23 and higher during a 28-day period ending on November 24, 2025.*

For more robust and granular Vulkan distribution data, use[Reach and devices](https://play.google.com/console/about/reachanddevices/)in the Google Play Console.

## OpenGL ES version

This section provides data about the relative number of devices that support a particular version of OpenGL ES. Note that support for one particular version of OpenGL ES also implies support for any lower version (for example, support for version 2.0 also implies support for 1.1).

To declare which version of OpenGL ES your application requires, you should use the`android:glEsVersion`attribute of the[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element. You can also use the[`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element)element to declare the GL compression formats that your application uses.

For handheld devices:

| OpenGL ES Version | Distribution |
|-------------------|--------------|
| GL 2.0            | 0.49%        |
| GL 3.0            | 0.86%        |
| GL 3.1            | 0.39%        |
| GL 3.2            | 98.24%       |

For all devices:

| OpenGL ES Version | Distribution |
|-------------------|--------------|
| GL 2.0            | 1.91%        |
| GL 3.0            | 0.80%        |
| GL 3.1            | 2.62%        |
| GL 3.2            | 94.64%       |

For more robust and granular OpenGL ES distribution data, use[Reach and devices](https://play.google.com/console/about/reachanddevices/)in the Google Play Console.

## Android Vulkan Profiles

This section provides data about the relative number of Vulkan capable devices supported by each[Android Vulkan Profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile).

| Android Vulkan Profile release | Percent supported |
|--------------------------------|-------------------|
| AVP 2025                       | 80.1%             |
| AVP 2022                       | 86.5%             |
| AVP 2021                       | 95.5%             |