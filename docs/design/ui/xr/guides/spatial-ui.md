---
title: https://developer.android.com/design/ui/xr/guides/spatial-ui
url: https://developer.android.com/design/ui/xr/guides/spatial-ui
source: md.txt
---

# Spatial UI

| **Preview:** Currently, spatial UI is only available in[Full Space](https://developer.android.com/design/ui/xr/guides/foundations#modes).

When building an Android XR differentiated app, you may want to use spatial UI to place content in a user's physical or virtual environment. You can break out your app into[spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels),[orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters), and add[spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation)(described in more detail on this page). You can also incorporate[spatial video](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video)in your design.

## Spatial panels

Spatial panels are the fundamental building blocks of Android XR apps. You can use them to build an XR-differentiated experience on an unlimited display, with content expanding across a user's space. Spatial panels serve as containers for UI elements, interactive components, and immersive content.

![An Android XR app with the Northern Lights and a snowy mountain. Three user control menus are in orbiters. They are elevated above the main panel, one to its left, right, and bottom sides.](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-panels.jpg)

## Understand how UI scales and moves

Spatial panels automatically adjust their size based on their distance from the user. This dynamic scaling ensures that UI elements remain legible and interactive when viewed from different distances. The size stays consistent between 0.75 meters and 1.75 meters. Then the scaling rate grows at 0.5 meters per meter, and elements will appear smaller.

To avoid conflicts with the system UI, keep within the**default panel movement limits**:

- Minimum depth: 0.75 meters from user
- Maximum depth: 5 meters from user

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-scale.mp4)and watch it with a video player.Users can scale a spatial panel up or down so it's large enough to see clearly, no matter the distance from the user. When a user moves a spatial panel, Android XR automatically scales its size.

## Spatial panel sizes

Android XR is designed to make your app comfortable, legible, and accessible to a wide audience. For an optimal experience, the system uses 0.868 dp-to-dmm. When viewed on a headset, your app will appear farther away from a user than when they view an app on a phone or tablet, so it must be larger for ease of use.
| **Key Term:** Dmm, or distance-independent millimeters, are angular units that remain constant regardless of the distance between a user and a virtual object.[Dp](https://developer.android.com/training/multiscreen/screendensities), or density-independent pixels, are units that scale to have uniform dimensions on any screen. They provide a flexible way to accommodate a design across platforms.

In Full Space, there's no minimum size for a spatial panel, and the maximum is 2560dp x 1800dp due to physical limitations.

![A visualization of a user who is 1.75 meters from an XR app.](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-distance.jpg)

## Where to place spatial panels

In Full Space, you can determine panel placement in both passthrough and virtual environments. When users switch from Home Space to Full Space, elements stay in the same predictable position, unless you assign a custom position.  
![A user looking at an XR app, with a natural eye level that's 5 degrees below the panel center.](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-eye-level.jpg)**Spawn the panel center 1.75 meters from a user's line of sight**. Place the panel's vertical center 5° below a user's eye level to maximize comfort, as users tend to look downward.  
![A user looking at a panel in the center 41 degrees of their field of view.](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-field-of-view-update.jpg)**For optimal comfort, place content in the center 41° of a user's field of view**. This will ensure clear visibility and minimize the need for excessive head or body movement.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-stationary.mp4)and watch it with a video player.A user can move around in their space, and spatial panels will stay in place.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-interaction-patterns.mp4)and watch it with a video player.Android XR includes ready-to-go interaction patterns to make it easy for users to manipulate elements and to simplify your development process. A user can move elements to adapt to their personal space. You can configure move and resize behaviors.

To help users position UI elements relative to real-world objects in their space, you can allow them to[anchor a spatial panel](https://developer.android.com/xr/jetpack-xr-sdk/work-with-entities#use_movablecomponent_to_make_an_entity_user-movable)to a specific location in the real world, such as the floor, chair, wall, ceiling, or table. Anchoring is available in passthrough only.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-anchor.mp4)and watch it with a video player.To help users feel stable and well-oriented, you can allow users to anchor a spatial panel to a specific location in the real world, such as the floor, chair, wall, ceiling, or table. Anchoring is available in passthrough only.

## Create your own spatial layout

You can decompose your app into multiple spatial panels, in any layout you choose. The spatial UI APIs don't limit the number panels. They include the ability to create layouts with rows and columns, and flat and curved rows. Spatial panel positions can be specific or arbitrary.[Learn how to develop spatial UI layouts](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui).
| **Note:** Avoid overlapping panels that would block a user from seeing critical information.

<br />

![Person looking at three panels arranged side-by-side in a flat row](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-flat.jpg)

Flat row layout  
![Person looking at three flat panels arranged side-by-side in a curved row, with the outer right and left panels closer to them](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-curved.jpg)

Curved row layout  
![Person looking at three flat panels of different sizes at arbitrary positions, with the outer right and left panels further away from themt](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-arbitrary.jpg)

Arbitrary positions layout

<br />

## Spatial videos

[Spatial videos](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video)can add a dimensional, immersive feel to your content. You can incorporate them into your designs as monoscopic or stereoscopic videos displayed on flat, 180° hemispherical, or 360° spherical surfaces.

## Orbiters

Orbiters are floating UI elements that are typically used to control the content within spatial panels and other entities that they're anchored to. They allow the content to have more space, and users can quickly access features while the main content remains visible. Orbiters give you the versatility to integrate existing UI components or to create new ones.

Orbiters should be used sparingly and with careful consideration of user needs and intent. A large number of spatialized UI elements can lead to content fatigue and overwhelm users with excessive competing actions. It's recommended to adapt a few key navigational components, such as the navigation rail or navigation bar.

<br />

![Non-spatialized navigation rail from Material Design in Home Space](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-rail-1.jpg)

Non-spatialized[navigation rail](https://m3.material.io/components/navigation-rail/overview)from Material Design in Home Space  
![A spatial navigation rail from Material Design in Full Space](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-rail-2.jpg)

A spatial navigation rail from Material Design in Full Space

<br />

<br />

![Non-spatialized navigation bar from Material Design in Home Space](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-bar-1.jpg)

Non-spatialized[navigation bar](https://m3.material.io/components/navigation-bar/overview)from Material Design in Home Space  
![A spatial navigation bar from Material Design in Full Space](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-nav-bar-2.jpg)

A spatial navigation bar from Material Design in Full Space

<br />

### Guidelines

- Adjust the padding to the panel to determine its flex or percentage position.
- Determine the offset of orbiters. 20dp is the recommended visual distance.
- Adjust the orbiter elevation level if needed using the spatial elevation levels. By default, they are elevated 15dp in Z-depth.
- Size can be fixed or flexible when the panel is resized.
- Determine if you want an orbiter to dynamically expand to fit the content.

### Design patterns to avoid

- Avoid overlapping an orbiter by more than 50% of its size.
- Avoid placing orbiters too far from the spatial panel.
- Don't use absolute X or Y coordinates.
- Avoid using too many orbiters.

## Spatial elevation

When you add spatial elevation to a component, it displays above the spatial panel on the Z-axis. This helps get a user's attention, creates better hierarchy, and improves legibility.
| **Note:** Android XR is in developer preview. Spatial elevation levels may change with future releases.

| Spatial Elevation Level |   Component   |  DP  |
|-------------------------|---------------|------|
| 0                       | Not Assigned  | .1dp |
| 1                       | Orbiter       | 16dp |
| 2                       | Not assigned  | 24dp |
| 3                       | SpatialPopup  | 32dp |
| 4                       | Not assigned  | 40dp |
| 5                       | SpatialDialog | 56dp |

<br />

![Material Design dialog on a large-screen app](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-elevation-1.jpg)

[Material Design dialog](https://m3.material.io/components/dialogs/guidelines#6e105e80-5cac-472b-809a-5ab51f251ea5)on a large-screen app  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-elevation-2.mp4)and watch it with a video player.

A dialog using spatial elevation in Android XR

<br />

<br />

![Material Design dropdown menu on a large-screen app](https://developer.android.com/static/images/design/ui/xr/guides/spatial-ui-elevation-3.jpg)

[Material Design drop-down menu](https://m3.material.io/components/menus/overview)on a large-screen app  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-ui-elevation-4.mp4)and watch it with a video player.

A drop-down menu using elevation in Android XR

<br />

##### Design patterns to avoid

- Avoid spatializing or elevating big areas and planes such as bottom sheets and side sheets.
- Avoid elevating UI elements with scrollable content.

## Design large target sizes

In an XR app, a target is the pointable area that users interact with. Android XR adheres to[Material Design's target guidelines](https://m3.material.io/foundations/designing/structure#dab862b1-e042-4c40-b680-b484b9f077f6), and recommends larger targets to increase precision, comfort, and usability.

Learn about XR[targets](https://developer.android.com/design/ui/xr/guides/visual-design#targets-android)and[hover states](https://developer.android.com/design/ui/xr/guides/visual-design#hover-states).

## Make typography accessible

Font legibility is critical to a comfortable user experience in XR. We recommend using typescale options with a font size of 14dp or larger, and a font weight of normal or higher for improved legibility.

If your existing app follows Material Design guidelines, it's already optimized for Android XR. You can define a new app's typography based on[Material Design](https://m3.material.io/styles/typography/overview).

[Learn about XR typography](https://developer.android.com/design/ui/xr/guides/visual-design#xr-typography).

## Use Material Design components and layouts

Take advantage of[Material Design's component library](https://m3.material.io/components)and adaptive layouts when designing your Android XR app. These interactive building blocks help speed up development so you can focus on core functionality and innovation.

[Material Design for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design)enhances Material 3 components and adaptive layouts with spatial UI behaviors. These can make your app feel more native to the platform and optimize for space.

You may also spatialize existing UI components by placing them in[orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters)and applying[spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation), as described on this page.

![Collage of elements from the Material 3 Design Kit](https://developer.android.com/static/images/design/ui/xr/guides/material-3-kit.jpg)[Download the Material 3 Design Kit to get started](https://www.figma.com/community/file/1035203688168086460).