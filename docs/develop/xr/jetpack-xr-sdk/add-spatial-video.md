---
title: Add spatial video to your app  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Add spatial video to your app Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

The Jetpack XR SDK supports the playback of stereoscopic [side-by-side
video](https://en.wikipedia.org/wiki/Stereoscopy#Side-by-side) onto flat surfaces. With stereoscopic video, each frame
consists of a left-eye and a right-eye image to give viewers a sense of
depth—also known as *stereopsis*.

You can render non-stereoscopic 2D video on Android XR apps with the [standard
media APIs](/media/audio-and-video) used for Android development on other form factors.

## Play side-by-side video using Jetpack SceneCore

With side-by-side video, each stereoscopic frame is presented as two images
arranged horizontally adjacent to each other. Top-and-bottom video frames are
arranged vertically adjacent to each other.

Side-by-side video is not a codec but rather a way of organizing stereoscopic
frames, which means it can be encoded in any of the [codecs supported by
Android](/media/platform/supported-formats#video-codecs).

You can load side-by-side video using [Media3 Exoplayer](/media/media3/exoplayer) and then render it
using the new [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity). To create a `SurfaceEntity`, call
`SurfaceEntity.create`, as shown in the following example.

```
val stereoSurfaceEntity = SurfaceEntity.create(
    session = xrSession,
    stereoMode = SurfaceEntity.StereoMode.SIDE_BY_SIDE,
    pose = Pose(Vector3(0.0f, 0.0f, -1.5f)),
    shape = SurfaceEntity.Shape.Quad(FloatSize2d(1.0f, 1.0f))
)
val videoUri = Uri.Builder()
    .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
    .path("sbs_video.mp4")
    .build()
val mediaItem = MediaItem.fromUri(videoUri)

val exoPlayer = ExoPlayer.Builder(this).build()
exoPlayer.setVideoSurface(stereoSurfaceEntity.getSurface())
exoPlayer.setMediaItem(mediaItem)
exoPlayer.prepare()
exoPlayer.play()

SpatialVideo.kt
```

## Play MV-HEVC video using Jetpack SceneCore

The MV-HEVC codec standard is optimized and designed for stereoscopic video,
allowing your app to efficiently play back immersive videos at great quality.
MV-HEVC files have a primary stream, usually the left eye, and a stereo stream
with the other eye.

Similar to side-by-side video, you can load it using [Media3 Exoplayer](/media/media3/exoplayer) and
render it using the [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity). You will want to specify whether your
MV-HEVC file is left or right primary in the `stereoMode` parameter when calling
`SurfaceEntity.create`.

**Important:** You must use [Media3 1.6.0](/jetpack/androidx/releases/media3#1.6.0) or later and an Android XR device with
MV-HEVC decoding support to playback MV-HEVC content.

```
// Create the SurfaceEntity with the StereoMode corresponding to the MV-HEVC content
val stereoSurfaceEntity = SurfaceEntity.create(
    session = xrSession,
    stereoMode = SurfaceEntity.StereoMode.MULTIVIEW_LEFT_PRIMARY,
    pose = Pose(Vector3(0.0f, 0.0f, -1.5f)),
    shape = SurfaceEntity.Shape.Quad(FloatSize2d(1.0f, 1.0f))
)
val videoUri = Uri.Builder()
    .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
    .path("mvhevc_video.mp4")
    .build()
val mediaItem = MediaItem.fromUri(videoUri)

val exoPlayer = ExoPlayer.Builder(this).build()
exoPlayer.setVideoSurface(stereoSurfaceEntity.getSurface())
exoPlayer.setMediaItem(mediaItem)
exoPlayer.prepare()
exoPlayer.play()

SpatialVideo.kt
```

## Play DRM-protected spatial video using Jetpack SceneCore

The Jetpack XR SDK supports playback of encrypted video streams using Android's
built-in [Digital Rights Management (DRM) framework](https://source.android.com/docs/core/media/drm). DRM
protects your content by enabling secure distribution and preventing
unauthorized copying or playback.

The process involves your media player application contacting a license server
to obtain decryption keys. On Android, this process is managed securely, and the
decrypted video frames are rendered to a protected graphics buffer that cannot
be accessed by the system or other applications, preventing screen capture.

To play DRM-protected video with Jetpack SceneCore, you need to:

1. Configure [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity) to request a protected surface.
2. Configure [Media3 Exoplayer](/media/media3/exoplayer) with the necessary DRM information to handle
   the key exchange.
3. Set the player's output to the [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity)'s surface.

The following example shows how to configure ExoPlayer to play a DRM-protected
stream and render it on a [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity):

```
// Create a SurfaceEntity with DRM content

// Define the URI for your DRM-protected content and license server.
val videoUri = "https://your-content-provider.com/video.mpd"
val drmLicenseUrl = "https://your-license-server.com/license"

// Create the SurfaceEntity with the PROTECTED content security level.
val protectedSurfaceEntity = SurfaceEntity.create(
    session = xrSession,
    stereoMode = SurfaceEntity.StereoMode.SIDE_BY_SIDE,
    pose = Pose(Vector3(0.0f, 0.0f, -1.5f)),
    shape = SurfaceEntity.Shape.Quad(FloatSize2d(1.0f, 1.0f)),
    surfaceProtection = SurfaceEntity.SurfaceProtection.PROTECTED
)

// Build a MediaItem with the necessary DRM configuration.
val mediaItem = MediaItem.Builder()
    .setUri(videoUri)
    .setDrmConfiguration(
        MediaItem.DrmConfiguration.Builder(C.WIDEVINE_UUID)
            .setLicenseUri(drmLicenseUrl)
            .build()
    )
    .build()

// Initialize ExoPlayer and set the protected surface.
val exoPlayer = ExoPlayer.Builder(this).build()
exoPlayer.setVideoSurface(protectedSurfaceEntity.getSurface())

// Set the media item and start playback.
exoPlayer.setMediaItem(mediaItem)
exoPlayer.prepare()
exoPlayer.play()

SpatialVideo.kt
```

For a more detailed overview of Android's media DRM framework, see the [Media
DRM documentation on source.android.com](https://en.wikipedia.org/wiki/Stereoscopy#Side-by-side).

## Play 180-degree and 360-degree video using Jetpack SceneCore

[`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity) supports playback of 180° videos on hemispherical surfaces
and 360° videos on spherical surfaces. The `radius` parameter refers to the
radial size of the respective surfaces in meters by default.

The following code shows how to set up `SurfaceEntity` for playback on a 180°
hemisphere and a 360° sphere. When using these canvas shapes, position the
surface by leveraging the user's head pose to provide an immersive experience.

**Note:** [`ResizableComponent`](/reference/kotlin/androidx/xr/scenecore/ResizableComponent) isn't supported for [`SurfaceEntity`](/reference/kotlin/androidx/xr/scenecore/SurfaceEntity) when
the `SurfaceEntity` has a `canvasShape` of `Hemisphere` or `Sphere`.

```
val devicePose = ArDevice.getInstance(xrSession).state.value.devicePose
val activitySpacePose = xrSession.scene.perceptionSpace.transformPoseTo(devicePose, xrSession.scene.activitySpace)

// Set up the surface for playing a 180° video on a hemisphere.
val hemisphereStereoSurfaceEntity =
    SurfaceEntity.create(
        session = xrSession,
        stereoMode = SurfaceEntity.StereoMode.SIDE_BY_SIDE,
        pose = activitySpacePose,
        shape = SurfaceEntity.Shape.Hemisphere(1.0f),
    )
// ... and use the surface for playing the media.

SpatialVideo.kt
```

```
val devicePose = ArDevice.getInstance(xrSession).state.value.devicePose
val activitySpacePose = xrSession.scene.perceptionSpace.transformPoseTo(devicePose, xrSession.scene.activitySpace)
// Set up the surface for playing a 360° video on a sphere.
val sphereStereoSurfaceEntity =
    SurfaceEntity.create(
        session = xrSession,
        stereoMode = SurfaceEntity.StereoMode.TOP_BOTTOM,
        pose = activitySpacePose,
        shape = SurfaceEntity.Shape.Sphere(1.0f),
    )
// ... and use the surface for playing the media.

SpatialVideo.kt
```

## Advanced SurfaceEntity control

For more-advanced control over video and image rendering, such as applying
custom material effects, you can work directly with `SurfaceEntity` from the
SceneCore library.

The following sections describe some of the advanced features available on
`SurfaceEntity`.

#### Apply edge feathering

Soften the edges of the surface to help it blend with the environment by
setting the `edgeFeatheringParams` property.

**Note:** Edge feathering is not recommended for 360 videos.

```
// Create a SurfaceEntity.
val surfaceEntity = SurfaceEntity.create(
    session = xrSession,
    pose = Pose(Vector3(0.0f, 0.0f, -1.5f))
)

// Feather the edges of the surface.
surfaceEntity.edgeFeatheringParams =
    SurfaceEntity.EdgeFeatheringParams.RectangleFeather(0.1f, 0.1f)

SpatialVideo.kt
```

#### Apply an alpha mask

Apply an alpha mask to create non-rectangular surfaces or add transparency
effects. First, load a `Texture` from an asset, then assign it to the
`primaryAlphaMaskTexture` property:

```
// Create a SurfaceEntity.
val surfaceEntity = SurfaceEntity.create(
    session = xrSession,
    pose = Pose(Vector3(0.0f, 0.0f, -1.5f))
)

// Load the texture in a coroutine scope.
activity.lifecycleScope.launch {
    val alphaMaskTexture =
        Texture.create(
            xrSession,
            Paths.get("textures", "alpha_mask.png"),
        )

    // Apply the alpha mask.
    surfaceEntity.primaryAlphaMaskTexture = alphaMaskTexture

    // To remove the mask, set the property to null.
    surfaceEntity.primaryAlphaMaskTexture = null
}

SpatialVideo.kt
```

## Play spatial video using Jetpack Compose for XR

If you're interested in learning how to play video using Jetpack Compose for XR,
learn how to [add a surface for image or video content](/develop/xr/jetpack-xr-sdk/ui-compose#add-surface).