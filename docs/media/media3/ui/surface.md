---
title: https://developer.android.com/media/media3/ui/surface
url: https://developer.android.com/media/media3/ui/surface
source: md.txt
---

This page describes the different types of surfaces that can be used for video playback with Media3, and how to choose the right type for your use case. To find out more about Surface objects in Android, read this[graphics documentation](https://source.android.com/docs/core/graphics/arch-sh).

## Set the surface

There are four entry points for the`Player`to connect its video output to some`Surface`:

- [`void setVideoSurface(@Nullable Surface surface)`](https://developer.android.com/reference/androidx/media3/common/Player#setVideoSurface(android.view.Surface))
- [`void setVideoSurfaceHolder(@Nullable SurfaceHolder surfaceHolder)`](https://developer.android.com/reference/androidx/media3/common/Player#setVideoSurfaceHolder(android.view.SurfaceHolder))
- [`void setVideoSurfaceView(@Nullable SurfaceView surfaceView)`](https://developer.android.com/reference/androidx/media3/common/Player#setVideoSurfaceView(android.view.SurfaceView))
- [`void setVideoTextureView(@Nullable TextureView textureView)`](https://developer.android.com/reference/androidx/media3/common/Player#setVideoTextureView(android.view.TextureView))

There are also different ways to clear it:

- [`void clearVideoSurface()`](https://developer.android.com/reference/androidx/media3/common/Player#clearVideoSurface())
- [`void clearVideoSurface(@Nullable Surface surface)`](https://developer.android.com/reference/androidx/media3/common/Player#clearVideoSurface(android.view.Surface))
- [`void clearVideoSurfaceHolder(@Nullable SurfaceHolder surfaceHolder)`](https://developer.android.com/reference/androidx/media3/common/Player#clearVideoSurfaceHolder(android.view.SurfaceHolder))
- [`void clearVideoSurfaceView(@Nullable SurfaceView surfaceView)`](https://developer.android.com/reference/androidx/media3/common/Player#clearVideoSurfaceView(android.view.SurfaceView))
- [`void clearVideoTextureView(@Nullable TextureView textureView)`](https://developer.android.com/reference/androidx/media3/common/Player#clearVideoTextureView(android.view.TextureView))

## Choose a surface type for PlayerView

The`surface_type`attribute of[`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView)lets you set the type of surface used for video playback. The allowed values are:

- `surface_view`([`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView))
- `texture_view`([`TextureView`](https://developer.android.com/reference/android/view/TextureView))
- `spherical_gl_surface_view`([`SphericalGLSurfaceView`](https://developer.android.com/reference/androidx/media3/exoplayer/video/spherical/SphericalGLSurfaceView)) - for spherical video playback
- `video_decoder_gl_surface_view`([`VideoDecoderGLSurfaceView`](https://developer.android.com/reference/androidx/media3/exoplayer/video/VideoDecoderGLSurfaceView)) - video rendering using extension renderers
- `none`- which is for audio playback only and should be used to avoid having to create a surface because doing so can be expensive.

If the view is for regular video playback then`surface_view`or`texture_view`should be used.[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)has a number of benefits over[`TextureView`](https://developer.android.com/reference/android/view/TextureView)for video playback:

- Significantly[lower power consumption](https://developer.android.com/media/media3/exoplayer/battery-consumption)on many devices.
- More accurate frame timing, resulting in smoother video playback.
- Support for higher quality HDR video output on capable devices.
- Support for secure output when playing DRM-protected content.
- The ability to render video content at the full resolution of the display on Android TV devices that upscale the UI layer.

`SurfaceView`should therefore be preferred over`TextureView`where possible.`TextureView`should be used only if`SurfaceView`does not meet your needs. One example is where smooth animations or scrolling of the video surface is required prior to Android 7.0 (API level 24), as described in the following notes. For this case, it's preferable to use`TextureView`only when[`SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT)is less than 24 (Android 7.0) and`SurfaceView`otherwise.
| **Note:** `SurfaceView`rendering wasn't properly synchronized with view animations until Android 7.0 (API level 24). On earlier releases, improper synchronization could result in unwanted effects when a`SurfaceView`was placed into a scrolling container, or when it was animated. Unwanted effects included the view's contents appearing to lag slightly behind where it should be displayed, and the view turning black when animated. To achieve smooth animation or scrolling of video prior to Android 7.0, use`TextureView`rather than`SurfaceView`.
| **Note:** The lifecycle of a`SurfaceView`'s surface is tied to view visibility, whereas a`TextureView`'s surface lifecycle is tied to window attachment and detachment. Therefore, in scrolling UIs that use`SurfaceView`, starting playback can take longer because the output surface becomes available slightly later. From Android 14 onwards,`PlayerView`uses[`SurfaceView.setSurfaceLifecycle(SURFACE_LIFECYCLE_FOLLOWS_ATTACHMENT)`](https://developer.android.com/reference/android/view/SurfaceView#setSurfaceLifecycle(int))to avoid this behavior. If your app uses`SurfaceView`directly (without`PlayerView`) then you may want to enable this mode. Before Android 14, it's possible to work around the surface being destroyed by translating views off-screen when recycling them.
| **Note:** Some Android TV devices run their UI layer at a resolution that's lower than the full resolution of the display, upscaling it for presentation to the user. For example, the UI layer may be run at 1080p on an Android TV that has a 4K display. On such devices,`SurfaceView`must be used to render content at the full resolution of the display. The full resolution of the display (in its current display mode) can be queried using[`Util.getCurrentDisplayModeSize`](https://developer.android.com/reference/androidx/media3/common/util/Util#getCurrentDisplayModeSize(android.content.Context)). The UI layer resolution can be queried using Android's[`Display.getSize`](https://developer.android.com/reference/android/view/Display#getSize(android.graphics.Point))API.
| **Note:** If you are using`PlayerView`inside of`AndroidView`, we cannot guarantee compatibility because`PlayerView`was not made with Compose in mind. One of the common problems for`SDK_INT == 34`is a stretched/cropped/leaked Surface that does not match the parent container (`AspectRatioFrameLayout`) correctly. You can opt into a Compose workaround by calling`PlayerView.setEnableComposeSurfaceSyncWorkaround`, but note that it causes issues with XML-based shared transitions.

## Choose a surface type in Compose

In Compose, the interop solution uses the`AndroidView`Composable to wrap[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)and[`TextureView`](https://developer.android.com/reference/android/view/TextureView). The two Composables that correspond to that are[`AndroidExternalSurface`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#AndroidExternalSurface(androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.unit.IntSize,androidx.compose.foundation.AndroidExternalSurfaceZOrder,kotlin.Boolean,kotlin.Function1))and[`AndroidEmbeddedExternalSurface`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#AndroidEmbeddedExternalSurface(androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.unit.IntSize,androidx.compose.ui.graphics.Matrix,kotlin.Function1))from`androidx.compose.foundation`. However, these proxy classes provide an API surface that limits access of the underlying views. Those views are needed by the`Player`to handle a[full lifecycle](https://developer.android.com/reference/android/view/SurfaceHolder.Callback)of the surface (creation and[size updates](https://developer.android.com/reference/androidx/media3/common/Player.Listener#onSurfaceSizeChanged(int,int))).

In`media3-ui-compose`module, you can find[`ContentFrame`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#ContentFrame(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.ui.layout.ContentScale,kotlin.Boolean,kotlin.Function0))and[`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/package-summary#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int))composables that link the[`Player`](https://developer.android.com/reference/androidx/media3/common/Player)to a`Surface`in a lifecycle-aware manner. The surface types in this case are:

- `androidx.media3.ui.compose.SURFACE_TYPE_SURFACE_VIEW`
- `androidx.media3.ui.compose.SURFACE_TYPE_TEXTURE_VIEW`

There is no type`none`, since that would correspond to not including the composable in your Compose UI tree.