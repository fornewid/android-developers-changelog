---
title: https://developer.android.com/media/platform/mediaplayer/basics
url: https://developer.android.com/media/platform/mediaplayer/basics
source: md.txt
---

# Get started with Media Player

This document introduces the basic concepts you should be familiar with before you work with Media Player.

## Sound and video classes

The following classes play sound and video in the Android framework:

- [`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer): This class is the primary API for playing sound and video.
- [`AudioManager`](https://developer.android.com/reference/android/media/AudioManager): This class manages audio sources and audio output on a device.

## Manifest declarations

Before you start development on your application using MediaPlayer, make sure your manifest has the appropriate declarations to allow use of related features.

- **Internet Permission:**If you are using MediaPlayer to stream network-based content, your application must request network access.

      <uses-permission android:name="android.permission.INTERNET" />

- **Wake Lock Permission:** If your player application needs to keep the screen from dimming or the processor from sleeping, or uses the[`MediaPlayer.setScreenOnWhilePlaying(boolean)`](https://developer.android.com/reference/android/media/MediaPlayer#setScreenOnWhilePlaying(boolean))or[`MediaPlayer.setWakeMode(android.content.Context, int)`](https://developer.android.com/reference/android/media/MediaPlayer#setWakeMode(android.content.Context,%20int))methods, you must request this permission.

      <uses-permission android:name="android.permission.WAKE_LOCK" />

## Use the MediaPlayer class

The[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)class is n essential component of the media framework. An object of this class can fetch, decode, and play both audio and video with minimal setup.`MediaPlayer`supports several media sources, including:

- Local resources
- Internal URIs, such as one you might obtain from a Content Resolver
- External URLs (streaming)

For a list of media formats that Android supports, see the[Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)page.

### Examples of working with audio sources

Here is an example of how to play audio that's available as a local raw resource (saved in your application's`res/raw/`directory):  

### Kotlin

    var mediaPlayer = MediaPlayer.create(context, R.raw.sound_file_1)
    mediaPlayer.start() // no need to call prepare(); create() does that for you

### Java

    MediaPlayer mediaPlayer = MediaPlayer.create(context, R.raw.sound_file_1);
    mediaPlayer.start(); // no need to call prepare(); create() does that for you

In this case, a "raw" resource is a file that the system does not try to parse in any particular way. However, the content of this resource shouldn't be raw audio. It should be a properly encoded and formatted media file in one of the supported formats.

And here is how you might play from a URI available locally in the system (that you obtained through a Content Resolver, for instance):  

### Kotlin

    val myUri: Uri = .... // initialize Uri here
    val mediaPlayer = MediaPlayer().apply {
        setAudioAttributes(
            AudioAttributes.Builder()
                .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .build()
        )
        setDataSource(applicationContext, myUri)
        prepare()
        start()
    }

### Java

    Uri myUri = ....; // initialize Uri here
    MediaPlayer mediaPlayer = new MediaPlayer();
    mediaPlayer.setAudioAttributes(
        new AudioAttributes.Builder()
            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
            .setUsage(AudioAttributes.USAGE_MEDIA)
            .build()
    );
    mediaPlayer.setDataSource(getApplicationContext(), myUri);
    mediaPlayer.prepare();
    mediaPlayer.start();

Playing from a remote URL using HTTP streaming looks like this:  

### Kotlin

    val url = "http://........" // your URL here
    val mediaPlayer = MediaPlayer().apply {
        setAudioAttributes(
            AudioAttributes.Builder()
                .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .build()
        )
        setDataSource(url)
        prepare() // might take long! (for buffering, etc)
        start()
    }

### Java

    String url = "http://........"; // your URL here
    MediaPlayer mediaPlayer = new MediaPlayer();
    mediaPlayer.setAudioAttributes(
        new AudioAttributes.Builder()
            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
            .setUsage(AudioAttributes.USAGE_MEDIA)
            .build()
    );
    mediaPlayer.setDataSource(url);
    mediaPlayer.prepare(); // might take long! (for buffering, etc)
    mediaPlayer.start();

| **Note:** If you're passing a URL to stream an online media file, the file must be capable of progressive download.
| **Caution:** You must either catch or pass[`IllegalArgumentException`](https://developer.android.com/reference/java/lang/IllegalArgumentException)and[`IOException`](https://developer.android.com/reference/java/io/IOException)when using[`setDataSource()`](https://developer.android.com/reference/android/media/MediaPlayer#setDataSource(android.content.Context,%20android.net.Uri))because the file you are referencing might not exist.

## Use Asynchronous preparation to improve performance

Keep performance in mind when you use[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer). For example, the call to[`prepare()`](https://developer.android.com/reference/android/media/MediaPlayer#prepare())can take a long time to execute, because it might involve fetching and decoding media data. So, like any method that may take a long time to execute,**never call it from your application's UI thread**. Doing so causes the UI to stop responding until the method returns, which is a bad user experience and can cause an ANR (Application Not Responding) error.

To avoid hanging your UI thread, spawn another thread to prepare the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)and notify the main thread when done. The framework supplies a convenient way to accomplish the[`prepareAsync()`](https://developer.android.com/reference/android/media/MediaPlayer#prepareAsync())method for doing this task. This method starts preparing the media in the background and returns immediately. When the media is done preparing, the[`onPrepared()`](https://developer.android.com/reference/android/media/MediaPlayer.OnPreparedListener#onPrepared(android.media.MediaPlayer))method of the[`MediaPlayer.OnPreparedListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnPreparedListener), configured through[`setOnPreparedListener()`](https://developer.android.com/reference/android/media/MediaPlayer#setOnPreparedListener(android.media.MediaPlayer.OnPreparedListener))is called.

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app.[Read more](https://developer.android.com/media/media3)about it.

These pages cover topics relating to recording, storing, and playing back audio and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)