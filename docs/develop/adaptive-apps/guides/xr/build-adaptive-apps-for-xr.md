---
title: https://developer.android.com/develop/adaptive-apps/guides/xr/build-adaptive-apps-for-xr
url: https://developer.android.com/develop/adaptive-apps/guides/xr/build-adaptive-apps-for-xr
source: md.txt
---

Android XR supports a variety of devices for immersive and augmented
experiences. On immersive devices, compatible Android apps will automatically
run in *Home Space* , and you can build fully immersive experiences in *Full
Space*. Building adaptive apps is critical for XR so users can freely resize and
reposition app windows in 3D space.

## Key considerations for XR

- **Infinite resizability** : Unlike physical devices with fixed screen sizes, XR panels can be resized to almost any aspect ratio or dimension. Use [window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) to ensure your layout adapts to these changes dynamically in Home Space. In Full Space, use [`recommendedContentBoxInFullSpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace#recommendedContentBoxInFullSpace()) to understand the specific dimensions for the bounding box inside the immersive environment and adapt your layout accordingly.
- **Input diversity**: XR users might interact using gaze and pinch, hand tracking, or connected controllers. Ensure your touch targets are ample and your navigation is accessible through multiple input methods.
- **Spatial placement**: Apps in XR exist alongside other apps in a 3D environment. Consider how your UI components can utilize depth and spatial positioning to improve clarity and hierarchy.
- **App continuity**: Users can move panels between different positions or states. Maintaining app state and a smooth layout transition during these movements is essential.

## Adaptation strategies

1. **Use canonical layouts** : See [Implement Material Design for your spatial
   UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design) for details on Material 3 components for XR.
2. **Flexible navigation** : Implement [`NavigationSuiteScaffold`](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation) to switch between a bottom bar on small panels and a navigation rail on larger or wider panels.
3. **Optimize for spatial viewing**: Avoid crowded layouts. Use whitespace effectively to ensure content is readable when viewed at different depths and angles.

## Learn more

For comprehensive Android XR development guidance, see [Develop with the Android
XR SDK](https://developer.android.com/develop/xr/get-started).