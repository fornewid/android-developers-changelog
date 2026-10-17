---
title: https://developer.android.com/agents/skills/xr/projected-hardware/skill
url: https://developer.android.com/agents/skills/xr/projected-hardware/skill
source: md.txt
---

## Prerequisites

- You must use a `compileSdk` of 36 or higher.

## Connection and lifecycle management

Intelligent eyewear hardware is only accessible while the glasses are connected
to the host phone. Monitor connection state and manage resource lifecycles using
`ProjectedContext`. You must read
[Understand projected activities and projected contexts](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/support-different-types) to understand
how to get a projected context and [how to manage its lifecycle](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/check-availability).

## Request glasses hardware permissions

- **Hardware permissions and opt-in** : You must read [Request hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions) to understand how to declare camera and microphone runtime permissions in the Android Manifest file, request runtime permissions in different scenarios, and handle permission results.

## Glasses hardware access and capabilities

- **Camera capture and CameraX** : You must read [Capture an image with the glasses' camera](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context) to understand the implementation patterns for capturing a photo with the glasses' camera using a `ProjectedContext`.