---
title: https://developer.android.com/media/implement/surfaces/wear-os
url: https://developer.android.com/media/implement/surfaces/wear-os
source: md.txt
---

Wear OS is a great platform for Android users to engage with a variety of audio
content---such as audiobooks, music, podcasts, and radio---while on the go. [Wear OS
by Google](https://developer.android.com/wear) lets you write apps for a variety of categories, including
audio content, that help users stay connected, stay healthy, and express
themselves.

If you have developed for Android, then features such as apps and
[notifications](https://developer.android.com/develop/ui/views/notifications) might be familiar to you.
You can use your knowledge of
[Modern Android development](https://developer.android.com/modern-android-development) when you develop for
Wear OS.

## Principles of Wear OS development

Wear OS is based on Android, so many of the best practices for Android also
apply to Wear OS. To optimize your development time, review these
[principles](https://developer.android.com/training/wearables/principles) before you start building your
Wear OS app.

### Create and run an app on Wear OS

The best way to get started is to see a Wear OS app for yourself! You can build
your first app for Wear OS using a template from Android Studio. The app
showcases the different ways to view information at a glance on Wear OS devices,
and introduces some best practices for developing apps on the platform.

For a step-by-step guide, see
[Create and run an app on Wear OS](https://developer.android.com/training/wearables/get-started/creating).

### Wear OS versus mobile development

There are some differences between how you design a mobile app and how you
design a Wear OS app. To find out how a specific feature, API, or best practice
is different in Wear OS app development compared to Android mobile development,
review the [feature table](https://developer.android.com/training/wearables/wear-v-mobile).

## Common use cases for media apps on Wear OS

Build a media app on Wear OS to let users stream and play downloaded content
from the watch. To produce the best user experience, consider implementing the
following media use cases, which work particularly well on Wear OS devices.

### Play downloaded content

Users can listen to content when they are working out without needing a network
connection. Although a Wear OS device generally supports Bluetooth and Wi-Fi,
it might not support LTE. Design for spotty connections and offline use cases,
such as exercising and commuting, when a user may leave their mobile device at
home. For more information, see
[Working with downloaded content](https://developer.android.com/training/wearables/principles#downloaded-content).

### Stream on any available network

Users can listen to music, podcasts, or a radio station by streaming from the
watch, but streaming can drain the watch battery. Prioritize downloaded content
when users choose to listen on the watch by exposing recently used downloads on
the browse list. Consider adding a button that takes them to a full list of
downloads as shown in the following images.

![A list of audio libraries includes](https://developer.android.com/static/wear/images/design/media_apps_5.png)
![A list of audio libraries, including a playlist and an audio book](https://developer.android.com/static/wear/images/design/media_apps_3.png)

## Build with Compose for Wear OS

[Compose for Wear OS](https://developer.android.com/training/wearables/compose) is part of Android Jetpack,
and like the other Wear Jetpack libraries you use, it helps you write better
code faster. This is Google's
recommended approach for [building user interfaces for
Wear OS apps](https://developer.android.com/training/wearables/user-interfaces#apps).

Many of the development principles for Jetpack Compose on mobile devices apply
to Compose for Wear OS. However, there are some key differences. As you build
with Compose for Wear OS, it's important to design apps that let
users conveniently and quickly access media on their watch. The watch is a
unique surface on which ease and speed of interactions is a high priority, as
users spend much less time interacting with their watch than their phone or
tablet.

For more information about the general advantages of a declarative UI framework,
see [Why Compose](https://developer.android.com/jetpack/compose/why-adopt). If you are unfamiliar with using
the Jetpack Compose toolkit, see the
[Compose pathway](https://developer.android.com/courses/jetpack-compose/course).
To learn more about Compose for Wear OS, see the
[Compose for Wear OS Pathway](https://developer.android.com/courses/pathways/wear-compose) and the
[Wear OS samples
repository](https://github.com/android/wear-os-samples#readme)
on GitHub.

## Wear OS media toolkit

The [Wear OS media
toolkit](https://google.github.io/horologist/#media) is a
set of libraries which accelerates the development of high-quality media apps
for Wear OS. The toolkit is part of the
[Horologist](https://github.com/google/horologist) project.
Horologist is an additional library that helps accelerate your app development.

The toolkit uses the best-in-class libraries for media use cases, from a UI
implemented with [Compose for Wear OS](https://developer.android.com/training/wearables/compose), to
playback capabilities implemented using [Media3](https://developer.android.com/guide/topics/media/media3).
If your app has specific requirements, you can adopt the UI implementation from
the toolkit while still relying on your existing player.

The media toolkit can help you to solve challenges like avoiding playing media
on the watch's built-in speakers, enabling
[audio offload](https://developer.android.com/guide/topics/media/exoplayer/battery-consumption#audio-playback),
and avoiding the need to ping the network unnecessarily.

[Design media apps](https://developer.android.com/design/ui/wear/guides/foundations/media-apps) provides the
guidance you implement with Horologist, as well as information about
architecture and use cases for Wear OS.

## Best practices for challenges specific to Wear OS

When creating a media app on Wear OS, consider how the user experience is
different on watches than on mobile devices, particularly regarding the
following:

- Built-in speakers are not designed for music playback. Therefore, use Bluetooth speakers or headphones.
- Network connectivity is limited or varied, so you should optimize your app for varied network conditions and minimize network use.
- Smaller batteries have limited power. The battery is consumed more quickly when the device performs audio processing on the main CPU and when the device has a poor LTE signal. Add support for audio offload to help conserve power.
- The device offers several UI surfaces for letting users re-engage with your app. Showcase your app's capabilities on these surfaces.

### Use Bluetooth speakers or headphones

Although watch speakers can be used for calls and guided activities, they don't
deliver the best experience for listening to media content.

To give the best user experience, your app can use the
[Media Toolkit](https://google.github.io/horologist/#media)
to make sure it plays audio when Bluetooth headphones or speakers are connected
to the watch.

The Media Toolkit provides a specific [Media3
extension](https://github.com/google/horologist/tree/main/media/backend-media3)
that decorates the [ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer) instance and
proactively stops accidental playback before it emits sound.

### Optimize for network conditions

For your media app to perform well on a watch, you need make choices about the
following streaming considerations and network conditions:

- Optimize the content by choosing a low bitrate for streaming, such as 48 kbps and codecs such as [AAC and MP3](https://developer.android.com/guide/topics/media/platform/supported-formats#audio-formats).
- Optimize the [prefetch strategy](https://developer.android.com/develop/connectivity/network-ops/network-access-optimization#prefetch-data) for images and tracks to allow for continuing playback when you lose a connection temporarily.
- Test your app in all network configurations: Wi-Fi, LTE, and watch connected to the phone using Bluetooth. Also test what happens when the watch switches between networks.

The Wear OS media toolkit helps to build the foundation of a performant app,
such as providing the [Network
Awareness](https://github.com/google/horologist/tree/main/network-awareness)
module to choose the better connection for a specific operation.

### Enable audio offload

For better performance and less power consumption for apps on Wear OS, use
[audio
offload](https://exoplayer.dev/battery-consumption.html#audio-playback).
It allows audio processing to be offloaded from the CPU to a
dedicated signal processor. The Media Toolkit provides support with the
[`AudioOffloadManager`](https://github.com/google/horologist/blob/main/media/sample/src/main/java/com/google/android/horologist/mediasample/data/service/offload/AudioOffloadManager.kt)

If you are not sure if audio offload is supported for a given audio format,
use the [`AudioManager.isOffloadedPlaybackSupported()`](https://developer.android.com/reference/android/media/AudioManager#isOffloadedPlaybackSupported(android.media.AudioFormat,%20android.media.AudioAttributes)) method.
For more information, see the
[Exoplayer
documentation](https://exoplayer.dev/battery-consumption.html#audio-playback).

### Avoid network connections unless absolutely necessary

When you develop for Wear OS, you can expect users to have limited network
connectivity. By using the
[MediaDownloadService](https://github.com/google/horologist/blob/main/media/data/src/main/java/com/google/android/horologist/media/data/service/download/MediaDownloadService.kt),
you let users have reliable, performant downloads so they can play
media on-the-go.

The toolkit lets you optimize media downloads more efficiently by using
Media3's DownloadManager and
[AndroidX WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) to schedule
downloads.

Media3 starts all the necessary notifications and foreground services. The
sample app code [configures WorkManager](https://github.com/google/horologist/blob/main/media/sample/src/main/java/com/google/android/horologist/mediasample/di/DownloadModule.kt)
to run the downloads when Wi-Fi connection is available to provide better
performance. Using the [Network Awareness](https://github.com/google/horologist/tree/main/network-awareness)
module lets developers map network operations with network type.

### Keep users aware of ongoing media playback

On Wear OS 3 and higher, an ongoing notification can appear on multiple surfaces
within the Wear OS user interface. When the [ongoing activity](https://developer.android.com/training/wearables/notifications/ongoing-activity#ongoing-not)
notification is tapped, the app opens the player screen.

With Media3, Wear OS automatically takes care of creating
[ongoing activities](https://developer.android.com/training/wearables/notifications/ongoing-activity)
for media apps with an intent for opening the app. This lets users stay more
engaged with long-running activities, such as media playback.