---
title: https://developer.android.com/develop/adaptive-apps/guides/tv/build-adaptive-apps-for-tv
url: https://developer.android.com/develop/adaptive-apps/guides/tv/build-adaptive-apps-for-tv
source: md.txt
---

Android TV provides a "leanback" experience where users interact with apps from
a distance, typically using a remote control. Creating an adaptive app for TV
requires focusing on visibility, D-pad navigation, and a large-screen-first
UI design.

## Key considerations for TV

- **D-pad navigation**: TV devices do not have touchscreens. All interactions are performed using a directional pad (D-pad) on a remote or game controller. Ensure every UI element is reachable and has a clear focused state.
- **10-foot UI**: TV apps are viewed from several feet away. Use large text, high-contrast colors, and bold graphics to ensure content is legible and interactive elements are easy to identify.
- **Landscape orientation** : TV displays are fixed in landscape orientation. Your app should be designed exclusively for this layout and declare `android:screenOrientation="landscape"` in the manifest.
- **Overscan handling**: Some older TV sets may crop the edges of the screen. Maintain a safe margin (typically 5%) around the edges of your layout to ensure critical UI elements are not cut off.
- **No background multitasking**: Unlike phones or tablets, TVs typically focus on one immersive task at a time. Ensure your app handles being paused or stopped correctly when the user switches to another app or input.

## Adaptation strategies

1. **D-pad focus management** : Use the Compose `FocusRequester` or View-based `nextFocus` attributes to create a logical and intuitive navigation flow between UI components.
2. **Optimize for high resolution**: Provide high-quality assets (xhdpi or higher) to ensure your app looks sharp on 4K and large HDTV screens.
3. **Simplify interactions**: Reduce the number of clicks required to reach primary content. Use horizontal rows and vertical grids that are easy to navigate with a D-pad.

## Learn more

For Android TV development guidance, see [Android TV overview](https://developer.android.com/training/tv).