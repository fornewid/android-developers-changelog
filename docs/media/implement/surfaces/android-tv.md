---
title: https://developer.android.com/media/implement/surfaces/android-tv
url: https://developer.android.com/media/implement/surfaces/android-tv
source: md.txt
---

Android offers a rich user experience that's optimized for apps running on large
screen devices, such as high-definition televisions. You can extend your app's
audience by developing it for Android TV. This document provides guidance on how
to do it effectively.

## Build TV apps

TV apps use the same structure as those for phones and tablets. This approach
means you can create new TV apps based on what you already know about building
apps for Android, or extend your existing apps to also run on TV devices.

However, the user interaction model for TV is substantially different from phone
and tablet devices. In order to make your app successful on TV devices, you must
design new layouts that can be clearly understood from 10 feet away, and provide
navigation that works with just a directional pad and a select button.

For more information about considerations such as how to handle TV hardware
controllers, building TV layouts, and creating TV navigation, see
[Build TV apps](https://developer.android.com/training/tv/start).

## Use Media3 ExoPlayer

Jetpack Media3 provides a Player interface that defines basic features such as
the ability to play, pause, seek, and display track information. ExoPlayer is
the default implementation of this interface in Media3.

Compared to Android's MediaPlayer API, it adds additional conveniences such as
support for multiple streaming protocols, default audio and video renderers,
and components that handle media buffering.

You can customize and extend ExoPlayer, and it can be updated through Play Store
application updates. For more information,
see [Media3 ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer).

### Use Media3 `MediaSession`

Media sessions provide a universal way for the system to interact with your
app's audio or video player. One of the primary characteristics that
distinguishes Media3 from previous media APIs is that there is no longer a need
for connectors between components.

The new `MediaSession` class takes any class that implements the Player
interface. Both ExoPlayer and MediaController are classes which implement that
interface. This facilitates much simpler interaction between the components.
For more information, see [The Player interface](https://developer.android.com/guide/topics/media/session/player).

For more information about creating a media playback app, see
[Create a basic media player using ExoPlayer](https://developer.android.com/media/implement/playback-app).

To create the best experience for the end users of your media app, you need to
implement `MediaSession`. To do so, initialize a `Player` and supply it to
`MediaSession.Builder` like this:  

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context).build()
val mediaSession = MediaSession.Builder(context, player).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context).build();
MediaSession mediaSession = new MediaSession.Builder(context, player).build();
```

#### Automatic state handling

The Media3 library automatically updates the media session using the player's
state. As such, you don't need to manually handle the mapping from player to
session. This helps ensure that your users always see the up-to-date information
on the playing media, including in the [Now Playing card](https://developer.android.com/training/tv/playback/now-playing).

### Control and advertise playback

In Media3, the default player is the ExoPlayer class, which implements the
Player interface. Connecting the media session to the player allows an app to
advertise media playback externally and to receive playback commands from
external sources. The media session delegates these commands to the media
app's player.

The media session is the key to controlling playback. It lets you route
commands from external sources to the player that does the work of playing your
media. External clients can use a media controller to issue playback commands
to your media app. These are received by your media session, which ultimately
delegates commands to the media player.
| **Note:** When playing media in the background, your MediaSession and the player need to be housed within a MediaSessionService or MediaLibraryService that runs as a foreground service. For more information, see [Background playback with a MediaSessionService](https://developer.android.com/guide/topics/media/session/mediasessionservice).

For more information about playback, such as how to customize playback command
behavior, see [Control and advertise playback using MediaSession](https://developer.android.com/guide/topics/media/session/mediasession#creating-media).

### Avoid disruptions in your app

Using `MediaSession` lets you avoid unnecessary disruptions such as:

- **Unexpected and continued playback** when switching off the TV or switching
  TV inputs. This also causes high energy consumption for TV hardware. With
  `MediaSession`, your app can inform the platform that it's playing media, and
  the platform is able to inform the app that playback can stop.

- **Music playback stops unexpectedly** when switching out of the app, or
  switching off the TV display. Using `MediaSession` APIs enables continued
  playback in a background service.

- **Restricted interaction with content** that inhibits users from controlling
  playback. For example, returning to your app if it's playing music in the
  background, or supporting voice commands. With `MediaSession` in your app,
  users can [use voice commands](https://developer.android.com/media/implement/assistant) to seek and skip
  songs or episodes.

## Further Considerations

As you extend your media app to Android for TV, you need to consider
accessibility issues, how to drive engagement, how to enable users to find
content, as well as how to build games and TV input services.

### TV accessibility

Although assistive technologies can and do help users with low vision, it's
important to support accessibility in content discovery journeys for TV apps.

For example, pay extra attention to providing navigation guidance and properly
labeling elements, and help ensure that TV apps work well with accessibility
features like TalkBack. These steps can significantly improve the experience
for users with vision impairments.

The first step toward improving accessibility is awareness. For more information
about text scaling, keyboard layouts, and audio descriptions, see
[accessibility resources](https://developer.android.com/training/tv/accessibility#android_accessibility_resources).

### Best practices to drive engagement on Google TV

All apps built for Android TV work on devices running Google TV. To provide the
best user experience on Google TV, we recommend that you apply the following
best practices.

You need to use `MediaSession`, to provide a universal way of interacting with
an audio or video player. For more information about how to implement this, see
[Use Media3 MediaSession](https://developer.android.com/media/implement/surfaces/android-tv#use_media3_mediasession).

As a baseline, your app needs to support Google Cast. It lets you extend your
Android, iOS, and Chrome apps to enable audio and video streaming to Android TVs
as well as Chromecast devices and Assistant devices. For more information, see
the [Google Cast documentation](https://developers.google.com/cast/docs/overview).

You also can help users:

- **Discover content across surfaces** by offering a media actions feed, or
  integrating Watch Next.

- **Take advantage of voice and engagement** by supporting account linking and
  entitlement sync, offering voice casting, and enabling Cast Connect.

- **Pay more easily** by integrating Google Play billing, and providing
  frictionless subscriptions.

### Build TV input framework

Watching live TV shows and other continuous, channel-based content is a big part
of the TV experience. Users are accustomed to selecting and watching shows on
TV by channel browsing. The TV Input Framework creates channels for publishing
ideo or music content in the TV programming guide.

The TV Input Framework provides a unified method for the receiving and playback
of live video content from hardware sources, such as HDMI ports and
built-in-tuners, and software sources, such as video streamed over the internet.
For further information, see [Build TV input services](https://developer.android.com/training/tv/tif).