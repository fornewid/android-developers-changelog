---
title: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_mouse_interaction
url: https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_mouse_interaction
source: md.txt
---

**Name String**

`XR_ANDROID_mouse_interaction`

**Extension Type**

Instance extension

**Registered Extension Number**

705

**Revision**

1

**Extension and Version Dependencies**

[OpenXR 1.0](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#versions-1.0)

**Last Modified Date**

2025-01-21

**IP Status**

No known IP claims.

**Contributors**

Sharayu Shenoy, Google

Chiara Coetzee, Google

Levana Chen, Google

Spencer Quin, Google

## Overview

This extension provides an[`XrPath`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XrPath)for getting mouse input and defines one commonly used action pose for user mouse profiles, including both mouse devices and trackpad devices.

This extension also introduces a new interaction profile specifically designed for mouse devices to input through the[OpenXR action system](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#input).

## Action pose for mouse interactions

The following action pose (i.e. "aim") enables a 3D pointer ray, whether the tracking inputs are provided by a mouse device or a trackpad device.

The*.../input/aim/pose* action subpath will be supported on all[interaction profiles](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#semantic-paths-interaction-profiles)that are valid for the user path of*/user/mouse*, including those interaction profiles enabled through extensions.

### Aim pose

The*.../input/aim/pose*is designed for interacting with objects through a mouse pointer in 3D space. For example, using a virtual laser pointer to aim at a virtual button on the wall is an interaction suited to the "aim" pose.

This is the same "aim" pose defined in[Standard pose identifiers](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#semantic-paths-standard-pose-identifiers). Every tracked controller profile already supports this pose.

![Example aim pose](https://developer.android.com/static/images/develop/xr/openxr/mouse-interaction-aim-pose-1.png)

**Position**

The position of the "aim" pose is typically the user's head, that is, the same position of the head when a mouse movement is detected. The aim pose for the mouse is calculated when there is a mouse movement. The last known aim position will be kept until the next mouse movement.

**Orientation**

The orientation of the "aim" pose**may**be used to render a 3D pointer ray to interact with a virtual object, for example, clicking a menu button on the wall.

The aim pose for the mouse is calculated when there is a mouse movement. The last known aim orientation will be kept until the next mouse movement.

The -Z direction is the forward direction of the aiming gesture, that is, where the aiming ray is pointing at.

The relative X,Y movement of the mouse is used to compute the relative movement of the mouse along a sphere around the user's head.

![Example aim pose](https://developer.android.com/static/images/develop/xr/openxr/mouse-interaction-aim-pose-2.png)

Depth movement will be supported using primary click and scroll. When an action to move in depth is in process, the position is offset from the head position in positive or negative Z-direction along the ray depending on the positive or negative scroll value. The system will stabilize the depth movement within the sphere around the user's head.

## The interaction profile for mouse devices

The mouse interaction profile is designed for runtimes which provide mouse inputs using mouse devices or trackpad devices with buttons and scroll. This allows mouse devices and trackpad devices to provide commonly used clicks, scroll, and action pose to the[OpenXR action system](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#input).

Interaction profile path:

- */interaction_profiles/android/mouse_interaction_android*

Valid for top level user path:

- */user/mouse*

Supported component paths:

- *.../input/aim/pose*
- *.../input/select/click*
- *.../input/secondary_android/click*
- *.../input/tertiary_android/click*
- *.../input/scroll_android/value*

This interaction profile supports the[action pose](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_mouse_interaction#android_mouse_interaction-action-pose)described in this section, as well as the following two groups of action inputs.

### Click action

This interaction profile supports*.../input/select/click, .../input/secondary_android/click*and /input/tertiary_android/click actions.

The*.../input/select/click* is a boolean input, where the value`XR_TRUE`indicates that the primary button on the mouse or trackpad is pressed.

The*.../input/secondary_android/click* is a boolean input, where the value`XR_TRUE`indicates that the secondary button on the mouse or trackpad is pressed.

The*.../input/tertiary_android/click* is a boolean input, where the value`XR_TRUE`indicates that the mouse scroll or the tertiary button is pressed.

### Scroll action

This interaction profile supports*.../input/scroll_android/value*actions.

The*.../input/scroll_android/value*is a 1D input component varying from -1 to 1 to map to scroll down and scroll up.

**New Object Types**

**New Flag Types**

**New Enum Constants**

**New Enums**

**New Structures**

**New Functions**

**Issues**

**Version History**

- Revision 1, 2024-08-29 (Levana Chen)
  - Initial extension description

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.