---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Your 2D mobile or large-screen Android app works by default in Android XR,
displayed as a 2D panel inside 3D space. You can add immersive XR features to
enhance your existing 2D Android app, transitioning it from a flat screen
experience to a dynamic, 3D environment.

Consider these important principles when bringing your Android app into XR.

- **Spatial capabilities** : Android XR offers a diverse range of spatial features available to your app, but you don't have to implement every single capability. Strategically implement those that complement your app's visual hierarchy, layouts, and user journeys. Consider incorporating custom environments and multiple panels to create a truly immersive experience. Refer to the [spatial UI design guidance](https://developer.android.com/design/ui/xr/guides/spatial-ui) to determine the optimal integration of spatial elements.
- **Adaptive UI** : XR gives you the flexibility to design a spacious UI that adapts seamlessly to an infinite canvas and freely resizable windows. One of the most important considerations is to use our [large screen design
  guidance](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) to optimize your app's layout for this expansive environment. Even if your app is mobile-only today, you can still utilize captivating environments to enhance the user experience, but a UI that's optimized for large screens is one of the best ways to optimize your app for Android XR.
- **UI framework** : We recommend constructing your UI with Jetpack Compose for XR. If your app relies on Views, review [working with Views in
  XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui-views) to learn more about leveraging Compose interoperability when working with Views, or evaluate working directly with the Jetpack SceneCore library.
- **Publishing on the Play Store** : To verify your XR-enhanced app is discoverable on the Play Store:
  - Consider streamlining your app by [removing any unnecessary feature
    requirements](https://android-developers.googleblog.com/2023/12/increase-your-apps-availability-across-device-types.html).
  - Verify your app isn't opted-out of XR publishing from your [Google Play
    Console](https://developer.android.com/distribute/console) to prevent your app from being excluded from Play Store search results.

## Tips for converting 2D UI components to 3D

Following these tips can make a big difference in making your app feel like it's
been optimized for XR.

- **Prioritize large screen compatibility** : Ensure your app's UI adheres to [large screen design principles](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) to help ensure optimal legibility of text and content in expansive XR environments.
- **Use spatial features strategically**: Identify key moments within your app's user journey where incorporating spatial features will enhance the experience and take advantage of the unique capabilities of the platform.
- **Place spatial panels with user comfort in mind**: When designing your layout with spatial panels, position them at a comfortable distance from the user to avoid overwhelming or feeling too close.
- **Use adaptive UI for spatial layouts**: Utilize adaptive UI concepts such as panes and progressive revealing to effectively decompose your layout into multiple spatial panels, optimizing information presentation.
- **Use orbiters for persistent elements and patterns**: Reserve orbiters for persistent and contextual UX elements such as navigation and controls. Limit the use of orbiters to maintain clarity and avoid clutter.
- **Make judicious use of elevation**: Apply spatial elevation to temporary components that remain stationary and don't scroll with the content. Avoid elevating large areas to prevent visual discomfort and maintain a balanced visual hierarchy.

Jetpack Compose for XR introduces new components that manage XR enhancements so
that you don't have to. For example, you can use [`SpatialPopup`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#SpatialPopup(androidx.compose.ui.Alignment,androidx.compose.ui.unit.IntOffset,kotlin.Function0,androidx.xr.compose.spatial.SpatialPopupProperties,kotlin.Function0)) and
[`SpatialDialog`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#SpatialDialog(kotlin.Function0,androidx.xr.compose.spatial.SpatialDialogProperties,kotlin.Function0)) to replace their 2D counterparts. These components appear
as typical 2D UI when spatial UI isn't available, and they show your app's
spatial UI when they can. Using them is as straightforward as making a one-line
change to replace the corresponding 2D UI element.

## Convert a dialog to SpatialDialog


```kotlin
// Previous approach
Dialog(
    onDismissRequest = onDismissRequest
) {
    MyDialogContent()
}

// New XR differentiated approach
SpatialDialog(
    onDismissRequest = onDismissRequest
) {
    MyDialogContent()
}
```

<br />

## Convert a popup to SpatialPopup


```kotlin
// Previous approach
Popup(onDismissRequest = onDismissRequest) {
    MyPopupContent()
}

// New XR differentiated approach
SpatialPopup(onDismissRequest = onDismissRequest) {
    MyPopupContent()
}
```

<br />

## Elevate 2D UI elements

When you want to elevate UI with more fine-grained control, we provide
`SpatialElevation` to allow you to elevate any composable in your app to a level
above the spatial panel on the Z-axis that you set with `SpatialElevationLevel`.
This helps get a user's attention, creates better hierarchy, and improves
legibility, as shown in the following example.


```kotlin
// Elevate an otherwise 2D Composable (signified here by ComposableThatShouldElevateInXr).
SpatialElevation(elevation = SpatialElevationLevel.Level4) {
    ComposableThatShouldElevateInXr()
}
```

<br />

### Key points about the code

- Don't spatialize or elevate big areas and planes such as bottom sheets and side sheets.
- Don't elevate UI elements that are scrollable with the content.

## Migrate 2D components to orbiters

Orbiters are floating elements that typically contain controls the user can
interact with. Orbiters can be anchored to spatial panels or other entities such
as spatial layouts. They allow the content to have more space and give users
quick access to features without obstructing the main content.


![Non-spatialized navigation
rail](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-xr-to-existing/non-spatialized-nav-rail.jpg)

Non-spatialized navigation rail
![Spatialized (XR-adapted) navigation
rail](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-xr-to-existing/spatialized-nav-rail.jpg)

Spatialized (XR-adapted) navigation rail

<br />

The following example code shows how you might migrate a 2D UI component to an
orbiter.


```kotlin
// Previous approach
NavigationRail()

// New XR differentiated approach
Orbiter(
    position = ContentEdge.Start,
    offset = dimensionResource(R.dimen.start_orbiter_padding),
    alignment = Alignment.Top
) {
    NavigationRail()
}
```

<br />

### Key points about orbiters

- Orbiters are components designed to attach existing UI elements to a spatial panel
- See our [Android XR app design guidance](https://developer.android.com/docs/quality-guidelines/android-xr) to verify which elements to migrate for orbiters, and for patterns to avoid.
- We recommend adapting only a few navigation components like the navigation rail, top app bar, or bottom app bar.
- Orbiters don't show up when spatial UI isn't enabled. For example, they won't show up in Home Space or on devices like phones, tablets, and foldables.

## Migrate 2D components to Spatial panels

Spatial panels are the fundamental building blocks of Android XR apps' UI.

Panels serve as containers for UI elements, interactive components, and
immersive content. When designing, you can add components like orbiters for user
controls, and spatially elevate UI elements to call attention to specific
interactions.

### Key points about the code

- See [Android XR app design guidance](https://developer.android.com/docs/quality-guidelines/android-xr) to verify which elements to migrate to panels, and for patterns to avoid.
- Follow best practices for spatial panel placement:
  - Panels should spawn center 1.5m from the user's eyes.
  - Content should appear in the center 41° of the user's field of view.
- Panels stay in place as a user moves. Anchoring is only available for passthrough.
- Stick to the system recommended 32 dp rounded corners for panels.
- Touch targets should be 56 dp and no smaller than 48 dp.
- Keep contrast ratios for readability, especially if you use any transparent backgrounds.
- Follow [Android design Color principles](https://developer.android.com/design/ui/mobile/guides/styles/color) and use the [Material Design
  color system](https://m3.material.io/styles/color/system/overview) to implement dark and light themes for your app.
- Use the spatial panels API with existing UI elements.

### Migrate 2D UI to a single spatial panel

By default, your app shows with a single panel in Home Space. [Learn how to
transition between Home Space and Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space). To bring that content to Full
Space, you can use [`SpatialPanel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,kotlin.Function0)).

Here's an example of how you might do this.


```kotlin
if (LocalSpatialCapabilities.current.isSpatialUiEnabled) {
    Subspace {
        SpatialPanel(
            dragPolicy = MovePolicy(),
            resizePolicy = ResizePolicy(),
        ) {
            AppContent()
        }
    }
} else {
    AppContent()
}
```

<br />

### Migrate your 2D UI to multiple spatial panels

You can either use a single spatial panel for your app's UI, or you can migrate
your 2D UI to multiple spatial panels. If you choose to use multiple panels for
your app's UI, you can position and rotate panels (analogous to laying out your
UI in 2D). You'll start with a clear design vision for what you want to
accomplish, and then you can use Spatial UI Layout APIs ([`SpatialBox`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialBox(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,kotlin.Boolean,kotlin.Function1)),
[`SpatialRow`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialRow(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,kotlin.Function1)), [`SpatialColumn`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialColumn(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialAlignment,kotlin.Function1)), [`SpatialLayoutSpacer`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialLayoutSpacer(androidx.xr.compose.subspace.layout.SubspaceModifier)),
[`SpatialAlignment`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SpatialAlignment)) and subspace modifiers to position and rotate panels.
There are some key patterns that you'll want to avoid as you implement multiple
panels.

- Avoid overlapping panels that would block the user from seeing critical information.
- Avoid overwhelming the user with panels.
- Avoid placing panels in uncomfortable or unnoticeable placements. Example: panels placed behind the user are difficult to notice.
- For more on developing your spatial UI, check out our full [guidance](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui).


![Non-spatialized
content](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-xr-to-existing/jetnews-non-spatialized-1394x888.jpg)

Non-spatialized content
![Spatialized (XR-adapted) media controls within an orbiter and content broken
up into multiple spatial
panels](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-xr-to-existing/jetnews-spatialized-1394x888.jpg)

Spatialized (XR-adapted) media controls within an orbiter and content broken up
into multiple spatial panels

<br />


```kotlin
SpatialRow {
    SpatialPanel(
        SubspaceModifier
            .width(384.dp)
            .height(592.dp)
    ) {
        StartSupportingPanelContent()
    }
    SpatialPanel(
        SubspaceModifier
            .height(824.dp)
            .width(1400.dp)
    ) {
        App()
    }
    SpatialPanel(
        SubspaceModifier
            .width(288.dp)
            .height(480.dp)
    ) {
        EndSupportingPanelContent()
    }
}
```

<br />

## Check for spatial capabilities

When you're deciding whether to display a specific UI element, avoid checking
for specific XR devices or modes. Checking for devices or modes rather than
capabilities can cause problems when the capabilities on a given device change
over time. Instead, use
[`LocalSpatialCapabilities.current.isSpatialUiEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSpatialCapabilities()) to directly check
for the necessary spatialization capabilities as shown in the following example.
This approach ensures your app adapts correctly to a wide range of XR
experiences without needing updates every time new devices emerge or
capabilities change.


```kotlin
if (LocalSpatialCapabilities.current.isSpatialUiEnabled) {
    SupportingInfoPanel()
} else {
    ButtonToPresentInfoModal()
}

// Similar check for audio
val spatialAudioEnabled = LocalSpatialCapabilities.current.isSpatialAudioEnabledhttps://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/xr/src/main/java/com/example/xr/compose/SpatialCapabilities.kt#L37-L44
```

<br />

## Use environments to change the user's surroundings

When you want to create a feeling of immersion in your app by changing your
user's surroundings, you can do so with environments. Adding an environment in
code is a straightforward change that you can make without significantly
impacting your app's existing UI. For more on setting environments, be sure to
check out our full [guidance](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments).

## Add 3D content

3D content such as 3D models and spatial video can help create a more immersive
experience and add spatial understanding. Your app can only show 3D content when
spatial capabilities are available, so you'll want to [check if spatial](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
capabilities are available first.

Refer to the appropriate guide for adding [3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models), [spatial video](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video)
or [spatial audio](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio).