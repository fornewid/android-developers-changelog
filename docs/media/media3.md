---
title: https://developer.android.com/media/media3
url: https://developer.android.com/media/media3
source: md.txt
---

> Documentation index: https://developer.android.com/media/media3/llms.txt

Jetpack Media3 is the new home for media libraries that enables Android apps to
display rich audio and visual experiences. Media3 offers a straightforward
architecture with powerful customization, reliability, and optimizations based
on device capabilities to abstract away the complexity that comes with
fragmentation.

This document provides an introduction to key APIs for implementing playback and
editing use cases with Media3.

## Playback Components

Media3 offers several key components for playback use cases. The classes that
make up these components will be familiar to you if you have worked with
previous Android media libraries.

The following diagram demonstrates how these components come together in a
typical app.
![The different components of a media app that uses Media3 connect
together in several simple ways owing to their sharing of interfaces
and classes.](https://developer.android.com/static/guide/topics/media/images/overview.png) **Figure 1**: Media app components

> [!IMPORTANT]
> **Important:** One of the primary characteristics that distinguishes Media3 from previous media APIs is that there is no longer a need for connectors between components. The new `MediaSession` class takes any class that implements the `Player` interface, as can the UI. Both `ExoPlayer` and `MediaController` are classes which implement that interface. This facilitates much simpler interaction between the components.

### The media player

A media player is a component of your app that allows playback of media files.
In Media3, you'll find:

| **Class** | **Description** | **Implementation note** |
|---|---|---|
| [`Player`](https://developer.android.com/reference/androidx/media3/common/Player.md.txt) | `Player` is an interface that defines traditional high-level capabilities for a media player, such as the ability to play, pause, and seek. | In Media3, the `Player` interface is a common API implemented or used by several components, including `MediaSession` and `MediaController`, for example. |
| [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.md.txt) | `ExoPlayer` is the default implementation of the `Player` interface in Media3. |   |

[Learn more about Media3 ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)

### The media session

A media session provides a universal way to interact with a media player. This
enables an app to advertise media playback to external sources and to receive
playback control requests from external sources. In Media3, you'll find:

| **Class** | **Description** | **Implementation note** |
|---|---|---|
| [`MediaSession`](https://developer.android.com/reference/androidx/media3/session/MediaSession.md.txt) | Media sessions enable your app to interact with an audio or video player. They advertise media playback externally and receive playback commands from external sources. | In Media3, a `MediaSession` needs a `Player` to execute commands and obtain the current state. |
| [`MediaSessionService`](https://developer.android.com/reference/androidx/media3/session/MediaSessionService.md.txt) | The `MediaSessionService` holds a media session and its associated player in a service separate from your app's main `Activity` to facilitate background playback. |   |
| [`MediaController`](https://developer.android.com/reference/androidx/media3/session/MediaController.md.txt) | The `MediaController` class is generally used to send commands from outside your app, for example, from other apps or the system itself. The commands are sent to the underlying `Player` of the associated `MediaSession`. | The `MediaController` class implements the `Player` interface, but when calling a method, the `MediaController` sends the command sent to the connected `MediaSession`. Client apps like Google Assistant can use `MediaController` to control playback in a connected session. |
| [`MediaLibraryService`](https://developer.android.com/reference/androidx/media3/session/MediaLibraryService.md.txt) | A `MediaLibraryService` is similar to a `MediaSessionService`, except that it includes additional APIs so you can serve your content library to client apps. |   |
| [`MediaBrowser`](https://developer.android.com/reference/androidx/media3/session/MediaBrowser.md.txt) | The `MediaBrowser` class allows the user to navigate through a media app's content library and select which items to play. | The `MediaBrowser` class implements both the `MediaController` and `Player` interfaces. Similar to `MediaController`, client apps such as Android Auto generally implement `MediaBrowser`. |

[Learn more about Media3 MediaSession](https://developer.android.com/guide/topics/media/session/mediasession)

### The UI components

Media3 provides default UI components for viewing video and controlling
playback.

| **Class** | **Description** | **Implementation note** |
|---|---|---|
| [`PlayerView`](https://developer.android.com/reference/androidx/media3/ui/PlayerView.md.txt) | A default `View` to show video and playback controls. | Connects to `ExoPlayer`, `MediaController` or any other custom `Player`. |
| [`PlayerSurface`](https://developer.android.com/reference/kotlin/androidx/media3/ui/compose/PlayerSurface.composable#PlayerSurface(androidx.media3.common.Player,androidx.compose.ui.Modifier,kotlin.Int)) | A Composable representing a dedicated drawing `Surface` to show video. | Connects to any `Player`, but does not contain playback controls. Only used for rendering of frames and can be resized according to various ` ContentScale` types. This and many other composables can be found in the [Compose UI utilities](https://developer.android.com/media/media3/ui/compose.md.txt). |

[Learn more about Media3 UI](https://developer.android.com/guide/topics/media/ui/overview)

## Editing components

Media3 includes the Transformer APIs for media editing use cases, including:

- Audio and video processing, such as adding filters and effects
- Handling special formats, such as HDR video and slow-motion video
- Composition, such as combining multiple input files
- Exporting the final output to a file

| **Class** | **Description** | **Implementation note** |
|---|---|---|
| [`Transformer`](https://developer.android.com/reference/androidx/media3/transformer/Transformer.md.txt) | Use the `Transformer` class to start and stop transformations and to check for progress updates on a running transformation. |   |
| [`Effects`](https://developer.android.com/reference/androidx/media3/transformer/Effects.md.txt) | An `Effects` object is a collection of audio and video effects to apply to a media item. | You can use `ExoPlayer` to preview the effects added to a media item before starting the export process. |
| [`EditedMediaItem`](https://developer.android.com/reference/androidx/media3/transformer/EditedMediaItem.md.txt) | An `EditedMediaItem` represents a media item to process and the edits to apply to it. |   |

[Learn more about Media3 Transformer](https://developer.android.com/guide/topics/media/transformer)

## Introduction video

Watch this video for an introduction to Media3 from the engineers who built
it:
[Video](https://www.youtube.com/watch?v=sTIBDcyCmCg)

## Useful links

- [Media Developer Center](https://developer.android.com/media)
- [`ExoPlayer` docs](https://developer.android.com/guide/topics/media/exoplayer)
- [Migration guide](https://developer.android.com/guide/topics/media/media3/getting-started/migration-guide)
- [AndroidX Media3 on GitHub](https://github.com/androidx/media)
- [Media3 media session sample app](https://github.com/androidx/media/tree/release/demos/session)
- [Universal Android Music Player sample app](https://github.com/android/uamp)