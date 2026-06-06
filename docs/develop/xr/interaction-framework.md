---
title: https://developer.android.com/develop/xr/interaction-framework
url: https://developer.android.com/develop/xr/interaction-framework
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Android XR Interaction Framework (AXRIF) provides familiar, high-level,
opinionated interactions for OpenXR apps on Android XR. AXRIF bridges
the gap between system-level interactions and in-app interactions, offering an
intuitive and cohesive way to handle user input.

Building natural and comfortable interaction design from scratch is difficult
and can consume a large portion of your development time. Use AXRIF to inherit
the exact input, interaction, and transition behaviors of the Android XR system
in your own apps.

AXRIF provides your app with the following key features:

- **Seamless multimodal transitions**: AXRIF features a built-in Transition Manager that handles automatic transitions between peripherals, hands, eyes, and direct touch.
- **Future-proof compatibility**: When interaction modes are added in Android XR releases, AXRIF automatically includes support for them with minimal developer effort.
- **Flexible control**: You can choose to enable only the specific interaction modes your app needs, and you can override the framework with the API if you need to temporarily take manual control of input logic.

### Supported input modalities

AXRIF supports a comprehensive suite of input modalities. Transitions between
all supported modalities are available and handled automatically.

| Modality | Description |
|---|---|
| XR Controllers | Use 6DoF controllers to point and select from a distance. |
| Gaze + Pinch | Use eyes to aim and hands to select. You can also configure AXRIF to use head to aim rather than eyes. |
| Hand Poke | Reach out and poke to directly interact with UI elements. |
| Hand Raycast | Use hands to point and select from a distance. |
| Mouse | Supports familiar mouse interactions like click and scroll, projected into your 3D scene. |

### Architecture at a glance

To promote better performance and cross-engine compatibility, AXRIF has two
primary components:

1. **Core library**: This component houses the universally-shared, engine-agnostic logic for interactions.
2. **Engine plug-ins**: These integration layers convert native data types into the respective engine's analogous structures. For example, the AXRIF Unity Package integrates directly with Unity's XR Interaction Toolkit (XRIT) to maximize compatibility with the input systems you are already familiar with.

### Get started

See the [getting started guide](https://developer.android.com/develop/xr/unity/interaction-framework) for instructions on setting up and trying out
AXRIF with Unity.