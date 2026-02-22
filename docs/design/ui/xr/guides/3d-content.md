---
title: https://developer.android.com/design/ui/xr/guides/3d-content
url: https://developer.android.com/design/ui/xr/guides/3d-content
source: md.txt
---

# 3D model design

In Android XR, 3D models are digital objects rendered with depth and volume to add a sense of realism and spatial understanding to your app. Users can naturally interact with 3D models, creating a transformative and engaging experience.
| **Preview:** Currently, 3D models are only available in Full Space.

Android XR supports 3D models with either a`.glTF`or`.glb`file extension.[GL Transmission Format (glTF)](https://www.khronos.org/glTF)is a standard 3D file format that minimizes asset size, loads fast, and is operable across platforms. You can export these file formats from third-party digital content creation tools such as[Blender](https://www.blender.org/),[Maya](https://www.autodesk.com/products/maya),[Spline](https://spline.design/), among others.

To optimize performance, prioritize small file sizes. Avoid excessive polygon counts or high-resolution textures that could impact rendering speed.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/3d-content-shark.mp4)and watch it with a video player.

## Methods to integrate 3D models

Android XR offers different tools to add interactive 3D models in your app: with SceneCore APIs or Scene Viewer. If you're building with Compose for XR, you can place 3D models relative to your UI using the[volume subspace composable](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui#use-volume).

- **SceneCore APIs** . You can create your own interactions including rotate, move, and scale. This allows users to interact with 3D models alongside your app's spatial panels and environment. You can also create parent relationships between panels and 3D models.[Learn about SceneCore APIs](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities).
- **Scene Viewer** can be used to load and display 3D models with interactions including rotate, move, and scale. However, Scene Viewer runs as a separate app. As a result, users won't be able to see your app's panels and environment while interacting with 3D models.[Learn about Scene Viewer](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#load-3d).

## SceneCore APIs

With SceneCore APIs, you can develop rich interactions for 3D models while keeping users in the context of your app. Since SceneCore lets you keep showing panels and environments alongside 3D models, you can create relationships between 3D models and panels, and use scene perception to anchor content to a user's physical space.

With SceneCore, you can also add:

- Annotations to the 3D models
- Playback of[animations](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#animate-3d)embedded in 3D models
- Multiple 3D models
- A custom menu and launch positions

### Relationships

3D models can have parent relationships with panels or other 3D models, so that the child element follows the parent's movement.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/3d-content-parent-child.mp4)and watch it with a video player.

### Anchors

Users can fix 3D models to a specific point in the real world. You have the option to add anchors to general horizontal or vertical surfaces or specific surfaces such as the floor or wall.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/3d-content-anchor.mp4)and watch it with a video player.

### Scene Viewer

Scene Viewer allows users to see and interact with 3D models. Users can open supported .glTF 3D models like a .glb file and place objects in space. You can[integrate the 3D viewer](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#load-3d)in your app to make it simple for users to visualize products, explore educational content, and experience 3D models. Scene Viewer provides built-in UI for basic interactions including moving, rotating, scaling, and anchoring.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/3d-content-spawn.mp4)and watch it with a video player.

### Launch position

3D models launch at 1.5 meters and 15 degrees below a user's line of sight, in the center of their field of view. They open in the miniature size of 1.5 meters per axis.

![A map showing the distance between a woman's line of sight and a 3D globe.](https://developer.android.com/static/images/design/ui/xr/guides/3d-content-spawn-still.jpg)

### Interactions Includes

UI and interactions that allow users to move, rotate, anchor, and scale 3D models using natural gestures.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/3d-content-gestures.mp4)and watch it with a video player.

### Interaction menu

The 3D model menu can be customized with additional actions. If the glTF file contains different sizes such as a suggested size and an actual size, the 1:1 button allows users to quickly switch between them. To exit the 3D model view and return to the app, users can click the mandatory close button.

![To increase a 3D globe's size from 100% to 135%, a user pinches their thumb and index finger on each hand, and gestures outward.](https://developer.android.com/static/images/design/ui/xr/guides/3d-content-globe.jpg)