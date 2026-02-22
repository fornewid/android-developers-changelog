---
title: https://developer.android.com/develop/xr/openxr
url: https://developer.android.com/develop/xr/openxr
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

<br />

![The OpenXR text logo](https://developer.android.com/static/images/develop/xr/openxr.svg)

Android XR supports apps built with[OpenXR](https://www.khronos.org/openxr/)through its support for the[OpenXR 1.1 specification and select vendor extensions](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html). OpenXR is an open standard that lets you create immersive and interactive experiences using a common set of APIs across a wide range of XR devices.

## Features

Android XR supports features that allow you to build apps that take full advantage of the unique capabilities of XR devices, using OpenXR. These features include the following.

Trackables
:   Supports*plane detection* , which is the ability to identify and track flat surfaces within the environment, enabling the placement of virtual objects in relation to the real world and*Anchors*which are virtual points of reference that can be attached to real-world objects or locations, so that virtual content remains accurately positioned and oriented even as the user moves around.

Raycasting
:   A technique used to determine the intersection point between a virtual ray and objects in the scene, facilitating interactions such as selecting and manipulating virtual elements.

Anchor persistence
:   The capability to save and restore anchors across multiple sessions, allowing for persistent and consistent placement of virtual content within the environment.

Object tracking
:   The ability to track mouse, keyboard and other objects in the real-world.

QR Code tracking
:   The ability to track QR Codes in the physical environment and decode their data.

Depth textures
:   The generation of depth maps that provide information about the distance between the camera and objects in the scene, enabling more realistic occlusion and interaction effects.

Passthrough
:   The ability to blend real-world camera footage with virtual content, creating a mixed reality experience that seamlessly combines the physical and digital worlds.

Scene meshing
:   The ability to acquire a 3D mesh of the environment, which can be used for physics, occlusion, and other world-aware interactions.

Composition layer passthrough
:   Allows for a polygon passthrough composition layer cutout, can be used for bringing real world objects into a scene.

Face tracking
:   The ability to track the features of the user's face, enabling the creation of more realistic and expressive avatars and virtual characters.

Eye tracking
:   Provides position and orientation of the user's eye, which is designed to make eye pose for avatars more realistic.

Hand tracking
:   The ability to track the position and movement of the user's hands.

Hand mesh
:   Provides an accurate representation of the user's hands as a low poly mesh. Optimized for platform-to-application delivery to make sure you get the best performance possible. This is an alternative to other extensions which use a bind pose and blend weights.

Light estimation
:   Used for lighting models to match the user's real world lighting conditions.

## Supported input devices

Android XR also supports the following input devices.

Hand Interaction
:   The recognition of specific hand gestures, such as pinching, swiping, and pointing, enabling the users to interact with virtual objects using gestures and hand movements.

Eye Gaze Interaction
:   The ability to track the user's eye movements, allowing them to select and interact with virtual objects using their gaze.

6DoF Motion Controllers
:   The ability to track the controllers position and movement along with Dpad and button bindings for triggering actions, or hover events within the app.

Mouse Interaction
:   The ability for users to interact with objects through a mouse pointer in 3D space

## Supported performance features

Android XR supports the following performance-related features.

Eye-tracked foveation
:   Allows an app to render higher resolution content only at the eyes focal point.

Space warp
:   Uses velocity vectors and depth texture information to generate tween frames which effectively boosts the frame rate required to keep your users immersed in your experiences

Performance metrics
:   Provides Android XR performance metrics at runtime of the current XR device, compositor, and XR app. This includes CPU frametime, GPU frame time, GPU utilization, CPU frequency, frames per second and[more](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics).

See the[OpenXR Feature Overview](https://developer.android.com/develop/xr/openxr/extensions)for a full list of supported features and extensions.

## Supported engines

The following engines are supported for OpenXR development with Android XR.

### Unity

Android XR's Unity support, built on top of OpenXR, lets developers create experiences using Unity 6. Learn more about building XR apps with Unity in the[Unity overview](https://developer.android.com/develop/xr/unity).
| **Note:** The[Android XR emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses)is not supported for Unity or OpenXR apps.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.