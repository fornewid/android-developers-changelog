---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk
url: https://developer.android.com/develop/xr/jetpack-xr-sdk
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Jetpack XR SDK includes all the tools and libraries you need to build
immersive and augmented experiences for Android XR devices.

## Build fully-immersive experiences

Target dedicated, high-fidelity devices such as XR headsets and wired XR
glasses. Use modern Android development tools like [Kotlin](https://developer.android.com/develop/ui/compose/kotlin) and [Compose](https://developer.android.com/compose),
as well as previous generation tools such as Java and [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout). You can
[spatialize your UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), [load and render 3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models) and semantically
understand the real world.

If you already have a mobile or large screen app on Android, the Jetpack XR SDK
[brings your app into a new dimension](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) by spatializing existing layouts and
enhancing your experiences with 3D models and immersive environments. See our
[quality guidelines](https://developer.android.com/docs/quality-guidelines/android-xr) for our recommendations on spatializing your existing
Android app.
[![](https://developer.android.com/static/images/picto-icons/set-square.svg) Go build immersive Get started building immersive experiences for XR headsets and XR glasses.](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the
video](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/index/jetpack-xr-sdk.mp4) and watch it with a video player.

## Build augmented and helpful experiences

Target lightweight and stylish AI glasses. Use modern Android development tools
like [Kotlin](https://developer.android.com/develop/ui/compose/kotlin) and [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer). Use APIs that facilitate
projected app experiences from a phone to AI glasses.
[![](https://developer.android.com/static/images/picto-icons/set-square.svg) Go build augmented Get started building augmented experiences for AI glasses.](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/build) Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the
video](https://developer.android.com/static/videos/xr/augmented-experiences.mp4) and watch it with a video player.

## Use Jetpack libraries

The Jetpack XR SDK libraries provide a comprehensive toolkit for building rich,
[immersive experiences](https://developer.android.com/design/ui/xr/guides/foundations), lightweight, [augmented experiences](https://developer.android.com/design/ui/ai-glasses) and
everything in between. The following libraries are part of the Jetpack XR SDK:

- [**Jetpack Compose for XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-compose): Declaratively build spatial UI layouts that take advantage of Android XR's spatial capabilities.
- [**Material Design for XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk#material-design): Build with Material components and layouts that adapt for XR.
- [**Jetpack SceneCore**](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-scenecore): Build and manipulate the Android XR scene graph with 3D content.
- [**ARCore for Jetpack XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk#arcore-jetpack): Bring digital content into the real world with perception capabilities.
- [**Jetpack Compose Glimmer**](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-compose-glimmer): A UI toolkit for building augmented Android XR experiences, optimized for display AI Glasses.
- [**Jetpack Projected**](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-projected): APIs that facilitate projected app experiences from a phone to AI glasses.

### API development during Developer Preview

Jetpack XR SDK libraries are part of the Android XR Developer Preview, and these
APIs are still under development. See the library release notes for known
issues:

- [Jetpack Compose for XR Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-compose)
- [ARCore for Jetpack XR Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-arcore)
- [Jetpack SceneCore Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-scenecore)
- [XR Runtime Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-runtime)
- [Jetpack Compose Glimmer Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-glimmer)
- [Jetpack Projected Release Notes](https://developer.android.com/jetpack/androidx/releases/xr-projected)

If you run into an issue that isn't on one of theses lists, [please report a bug
or submit feedback](https://developer.android.com/develop/xr/support).

### Jetpack Compose for XR

**Applicable XR devices**: XR headsets, wired XR glasses

With Jetpack Compose for XR, you can use familiar [Compose concepts](https://developer.android.com/develop/ui/compose/layouts/basics) such as
[rows](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) and [columns](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)) to create spatial UI layouts in XR, whether you're
porting an existing 2D app to XR or creating a new XR app from scratch.

This library provides [subspace composeables](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SubspaceComposable), such as [spatial panels](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(android.content.Intent,androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape))
and [orbiters](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/package-summary#Orbiter(androidx.xr.compose.spatial.ContentEdge.Horizontal,androidx.compose.ui.unit.Dp,androidx.xr.compose.spatial.OrbiterOffsetType,androidx.compose.ui.Alignment.Horizontal,androidx.xr.compose.subspace.layout.SpatialShape,androidx.compose.ui.unit.Dp,kotlin.Boolean,kotlin.Function0)), which let you place your existing 2D Compose or Views-based
UI in a spatial layout.

See [Develop UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) for detailed guidance.
![Develop UI XR components orbiter generic example](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/index/develop-ui-xr-component-orbiter-generic.jpg)

Compose for XR introduces the [`Volume`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#Volume(androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.Function1)) subspace composable, which lets you
place [SceneCore](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-scenecore) entities, such as 3D models, relative to your UI.

Learn how to [spatialize your existing Android app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) or view the API reference
for more detailed information.

### Material Design for XR

**Applicable XR devices**: XR headsets, wired XR glasses

Material Design provides components and layouts that adapt for XR. If you're
building with [adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive). [Learn more about implementing
Material Design for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design).

### Jetpack SceneCore

**Applicable XR devices**: XR headsets, wired XR glasses

The Jetpack SceneCore library lets you place and arrange 3D content, defined by
[entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities), relative to each other and your environment. With SceneCore, you
can:

- Set [spatial environments](https://developer.android.com/design/ui/xr/guides/environments)
- Create instances of a [`PanelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/PanelEntity)
- [Place and animate 3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models)
- [Specify spatial audio sources](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-audio)
- [Add Components to entities that make them movable, resizable, and can be
  anchored to the real world](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities)

The Jetpack SceneCore library also provides support for spatializing
applications built using Views. See our [guide to working with views](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui-views) for
more details.

View the [API reference](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/package-summary) for more detailed information.

### ARCore for Jetpack XR

**Applicable XR devices**: XR headsets, wired XR glasses, AI glasses

Inspired by the existing [ARCore library](https://developers.google.com/ar), the ARCore for
Jetpack XR library provides capabilities for blending digital content with the
real world. This library includes motion tracking, persistent anchors, hit
testing, and plane identification with semantic labeling (for example, floor,
walls, and tabletops). This library leverages the underlying perception stack
powered by [OpenXR](https://developer.android.com/develop/xr/openxr), which ensures compatibility with a wide range of
devices and helping to future-proof apps.

View [Work with ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore) for more detailed information.

> [!WARNING]
> **Preview:** Unlike its predecessor, ARCore for Jetpack XR currently only supports Android XR.

### Jetpack Compose Glimmer

**Applicable XR devices**: AI glasses

Jetpack Compose Glimmer is a UI toolkit for building augmented Android XR
experiences, optimized for display AI Glasses. Build beautiful, minimal, and
comfortable UI for devices that are worn all day.

- **Built for glanceability and legibility** : Unlike phones, the primary canvas is an optical see-through display---it's transparent. Jetpack Compose Glimmer provides [glasses-specific theming](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#theme), [simplified color
  palettes](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#colors), and [typography](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#typography) to make your content easy to read, fast to process, and never distracting.
- **Optimized for wearable-specific interactions** : We've optimized interaction models for how people use glasses. [Jetpack Compose Glimmer
  components](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#components) feature [clear focus states](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/focus#focus-states), like optimized outlines instead of distracting ripple effects, and are built to handle common physical inputs like taps, swipes on the frame, and of course, voice.
- **Use familiar declarative UI patterns** : Because Jetpack Compose Glimmer is built entirely on [Jetpack Compose](https://developer.android.com/compose), you can use everything you already know about declarative UI building in Android. We provide a full set of core, prebuilt Composable functions---things like [Text](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text), [Icon](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons), [Button](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons), and specialized components like [TitleChip](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)---all optimized for the glasses environment.

![Develop UI XR components orbiter generic example](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/glimmer/glimmer-overview.jpg)

### Jetpack Projected

**Applicable XR devices**: AI glasses

When you [build for AI glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/build), your app runs on a companion *host device*,
such as an Android phone, that projects your app's XR experiences. Jetpack
Projected lets these Android host devices communicate with AI glasses if the
host devices have XR projected capabilities.

- **Access projected device hardware** : A device context tied to the projected device (AI glasses). This [projected context](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types#projected-context) provides access to projected device hardware, such as the camera. Dedicated activities created specifically to display on AI glasses [already function as a projected
  context](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context#glasses-activity). If another part of your app (such as a phone activity or a service) needs to access the AI glasses hardware, it can [obtain a projected
  context](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context#phone-activity-service).
- **Simplify permission requests** : AI glasses follow the [standard Android
  permission model](https://developer.android.com/guide/topics/permissions/overview), with glasses-specific permissions that must be [requested at runtime](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions#request-permissions) before your app can access device hardware, such as the camera. Permission helper streamlines these permission request mechanisms across both phone and AI glasses interfaces to provide a consistent request experience.
- **Check device and display capabilities**: Check if the projected device has a display and the state of the display to present visuals. Adapt your app based on capabilities of the device. For example, you might want to provide more audio context if the device has no display or the display is off.
- **Access app camera actions**: Your app can access user camera actions, for example to turn the camera on or off in a video streaming app.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.