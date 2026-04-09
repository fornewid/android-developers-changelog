---
title: Getting started  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/hello-world
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Getting started Stay organized with collections Save and categorize content based on your preferences.



**Tip:** Another way to get started is to work through
[the ExoPlayer codelab](https://codelabs.developers.google.com/codelabs/exoplayer-intro/).

For simple use cases, getting started with `ExoPlayer` consists of implementing
the following steps:

1. Add ExoPlayer as a dependency to your project.
2. Create an `ExoPlayer` instance.
3. Attach the player to a view (for video output and user input).
4. Prepare the player with a `MediaItem` to play.
5. Release the player when done.

These steps are described in more detail below. For a complete example, refer to
`PlayerActivity` in the [main demo app](https://github.com/androidx/media/tree/release/demos/main/).

## Add ExoPlayer as a dependency

### Add ExoPlayer modules

The easiest way to get started using AndroidX Media3 is to add gradle
dependencies on the libraries you need in the `build.gradle` file of your app
module.

For example, to depend on ExoPlayer with DASH playback support and UI components
you can add dependencies on the modules like this:

### Kotlin

```
implementation("androidx.media3:media3-exoplayer:1.10.0")
implementation("androidx.media3:media3-exoplayer-dash:1.10.0")
implementation("androidx.media3:media3-ui:1.10.0")
implementation("androidx.media3:media3-ui-compose-material3:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-exoplayer:1.10.0"
implementation "androidx.media3:media3-exoplayer-dash:1.10.0"
implementation "androidx.media3:media3-ui:1.10.0"
implementation("androidx.media3:media3-ui-compose-material3:1.10.0")
```

where 1.10.0 is your preferred version (the latest version can be found by
consulting the [release notes](https://github.com/androidx/media/tree/release/RELEASENOTES.md)). All modules must be of the same version.

AndroidX Media3 has library modules that depend on
external libraries to provide additional functionality. Some are
available from the Maven repository, whereas others must be built manually.
Browse the [libraries directory](https://github.com/androidx/media/tree/main/libraries) and see individual READMEs for details.

More information on the library modules that are available can be found on the
[Google Maven AndroidX Media page](https://maven.google.com/web/index.html#androidx.media3).

### Turn on Java 8 support

If not enabled already, you need to turn on at least Java 8 support in all
`build.gradle` files that depend on ExoPlayer, by adding the following to the
`android` section:

```
compileOptions {
  targetCompatibility JavaVersion.VERSION_1_8
}
```

## Create the player

You can create an `ExoPlayer` instance using `ExoPlayer.Builder`, which provides
a range of customization options. The following code is the simplest example of
creating an instance.

### Kotlin

```
val player = ExoPlayer.Builder(context).build()

HelloWorld.kt
```

### Java

```
ExoPlayer player = new ExoPlayer.Builder(context).build();

HelloWorld.java
```

### A note on threading

ExoPlayer instances must be accessed from a single application thread. For the
vast majority of cases, this should be the application's main thread. Using the
application's main thread is a requirement when using ExoPlayer's UI components
or the IMA extension.

The thread on which an ExoPlayer instance must be accessed can be explicitly
specified by passing a `Looper` when creating the player. If no `Looper` is
specified, then the `Looper` of the thread that the player is created on is
used, or if that thread does not have a `Looper`, the `Looper` of the
application's main thread is used. In all cases, the `Looper` of the thread from
which the player must be accessed can be queried using
`Player.getApplicationLooper`.

**Note:** If you see `IllegalStateException` being thrown with the message "Player is
accessed on the wrong thread", then some code in your app is accessing an
`ExoPlayer` instance on the wrong thread (the exception's stack trace shows you
where).

For more information about ExoPlayer's threading model, see the
["Threading model" section of the ExoPlayer Javadoc](/reference/androidx/media3/exoplayer/ExoPlayer).

## Attach the player to a view

The `media3-ui` library provides a range of prebuilt UI components for media
playback. These include `PlayerView`, which encapsulates a `PlayerControlView`,
a `SubtitleView`, and a `Surface` onto which video is rendered. A `PlayerView`
can be included in your application's layout xml. For example, to bind the
player to the view:

### Kotlin

```
// Bind the player to the view.
playerView.player = player

HelloWorld

.kt
```