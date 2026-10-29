---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-external-surface
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/spatial-external-surface
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A [`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialExternalSurface.composable) is a [subspace composable](https://developer.android.com/develop/xr/jetpack-xr-sdk/compose/components#subspace-composables) that creates and
manages the [`Surface`](https://developer.android.com/reference/kotlin/android/view/Surface) into which your app can draw content, such as an
image or [video](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video). [`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialExternalSurface.composable) supports either stereoscopic
or monoscopic content.

## Add a surface for image or video content

This example demonstrates how to load side-by-side stereoscopic video using
[Media3 Exoplayer](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models) and [`SpatialExternalSurface`](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design):


```kotlin
@OptIn(ExperimentalComposeApi::class)
@Composable
fun SpatialExternalSurfaceContent() {
    val context = LocalContext.current
    Subspace {
        SpatialExternalSurface(
            modifier = SubspaceModifier
                .width(1200.dp) // Default width is 400.dp if no width modifier is specified
                .height(676.dp), // Default height is 400.dp if no height modifier is specified
            // Use StereoMode.Mono, StereoMode.SideBySide, or StereoMode.TopBottom, depending
            // upon which type of content you are rendering: monoscopic content, side-by-side stereo
            // content, or top-bottom stereo content
            stereoMode = StereoMode.SideBySide,
        ) {
            val exoPlayer = remember { ExoPlayer.Builder(context).build() }
            val videoUri = Uri.Builder()
                .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
                // Represents a side-by-side stereo video, where each frame contains a pair of
                // video frames arranged side-by-side. The frame on the left represents the left
                // eye view, and the frame on the right represents the right eye view.
                .path("sbs_video.mp4")
                .build()
            val mediaItem = MediaItem.fromUri(videoUri)

            // onSurfaceCreated is invoked only one time, when the Surface is created
            onSurfaceCreated { surface ->
                exoPlayer.setVideoSurface(surface)
                exoPlayer.setMediaItem(mediaItem)
                exoPlayer.prepare()
                exoPlayer.play()
            }
            // onSurfaceDestroyed is invoked when the SpatialExternalSurface composable and its
            // associated Surface are destroyed
            onSurfaceDestroyed { exoPlayer.release() }
        }
    }
}
```

<br />

### Key points about the code

- Set [`StereoMode`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/StereoMode) to `Mono`, `SideBySide`, or `TopBottom` depending upon which type of content you are rendering:
  - `Mono`: The image or video frame consists of a single, identical image shown to both eyes.
  - `SideBySide`: The image or video frame contains a pair of images or video frames arranged side-by-side, where the image or frame on the left represents the left eye view, and the image or frame on the right represents the right eye view.
  - `TopBottom`: The image or video frame contains a pair of images or video frames stacked vertically, where the image or frame on the top represents the left eye view, and the image or frame on the bottom represents the right eye view.
- [`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialExternalSurface.composable) only supports rectangular surfaces.
- This [`Surface`](https://developer.android.com/reference/kotlin/android/view/Surface) doesn't capture input events.
- It's not possible to synchronize [`StereoMode`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/StereoMode) changes with application rendering or video decoding.
- This composable can't render in front of other panels, so you shouldn't use a `MovePolicy` if there are other panels in the layout.

## Add a surface for DRM protected video content

[`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialExternalSurface.composable) also supports playback of DRM-protected video
streams. To enable this, you must create a secure surface that renders to
protected graphics buffers. This prevents the content from being screen-recorded
or accessed by non-secure system components.

To create a secure surface, set the `SpatialExternalSurfaceProtection` parameter
to `SpatialExternalSurfaceProtection.Protected` on the
[`SpatialExternalSurface`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialExternalSurface.composable) composable. Additionally, you must configure
[Media3 Exoplayer](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models) with the appropriate DRM information to handle the license
acquisition from a license server.

The following example demonstrates how to configure `SpatialExternalSurface` and
`ExoPlayer` to play a DRM-protected video stream:


```kotlin
@OptIn(ExperimentalComposeApi::class)
@Composable
fun DrmSpatialVideoPlayer() {
    val context = LocalContext.current
    Subspace {
        SpatialExternalSurface(
            modifier = SubspaceModifier
                .width(1200.dp)
                .height(676.dp),
            stereoMode = StereoMode.SideBySide,
            surfaceProtection = SpatialExternalSurfaceProtection.Protected
        ) {
            val exoPlayer = remember { ExoPlayer.Builder(context).build() }

            // Define the URI for your DRM-protected content and license server.
            val videoUri = "https://your-content-provider.com/video.mpd"
            val drmLicenseUrl = "https://your-license-server.com/license"

            // Build a MediaItem with the necessary DRM configuration.
            val mediaItem = MediaItem.Builder()
                .setUri(videoUri)
                .setDrmConfiguration(
                    MediaItem.DrmConfiguration.Builder(C.WIDEVINE_UUID)
                        .setLicenseUri(drmLicenseUrl)
                        .build()
                )
                .build()

            onSurfaceCreated { surface ->
                // The created surface is secure and can be used by the player.
                exoPlayer.setVideoSurface(surface)
                exoPlayer.setMediaItem(mediaItem)
                exoPlayer.prepare()
                exoPlayer.play()
            }

            onSurfaceDestroyed { exoPlayer.release() }
        }
    }
}
```

<br />

#### Key points about the code

- Protected Surface: Setting `surfaceProtection =
  SpatialExternalSurfaceProtection.Protected` on `SpatialExternalSurface` is essential so that the underlying `Surface` is backed by secure buffers suitable for DRM content.
- DRM Configuration: You must configure the `MediaItem` with the DRM scheme (for example, `C.WIDEVINE_UUID`) and the URI of your license server. ExoPlayer uses this information to manage the DRM session.
- Secure Content: When rendering to a protected surface, the video content is decoded and displayed on a secure path, which helps satisfy content licensing requirements. This also prevents the content from appearing in screen captures.