---
title: https://developer.android.com/media/platform/mediaplayer/state-resources
url: https://developer.android.com/media/platform/mediaplayer/state-resources
source: md.txt
---

# Manage MediaPlayer state and resources

This document covers two areas with potential pitfalls.

- **State.**With "Medialayer\`, certain operations are valid only in specific states. Incorrect operations can cause exceptions or unexpected behavior.

- **Resources** When you make configuration changes, such as screen rotation, You must release a`MediaPlayer`object to free up system resources and avoid resource exhaustion.

## Manage state

[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)is state-based. That is, it has an internal state that you must always be aware of when you write your code, because certain operations are only valid when the player is in specific states. If you perform an operation while in the wrong state, the system may throw an exception or cause other undesirable behaviors.

The state diagram in the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)class documentation clarifies which methods move the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)from one state to another. For example:

- When you create a new[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), it is in the*Idle*state.
- You initialize it by calling[`setDataSource()`](https://developer.android.com/reference/android/media/MediaPlayer#setDataSource(android.content.Context,%20android.net.Uri)), which changes it to the*Initialized*state.
- You prepare it using either the[`prepare()`](https://developer.android.com/reference/android/media/MediaPlayer#prepare())or[`prepareAsync()`](https://developer.android.com/reference/android/media/MediaPlayer#prepareAsync())method.
- When the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)is done preparing, it enters the`Prepared`state, which means you can call[`start()`](https://developer.android.com/reference/android/media/MediaPlayer#start())to make it play the media.

At that point, as the diagram illustrates, you can move between the`Started`,`Paused`and`PlaybackCompleted`states by calling such methods as[`start()`](https://developer.android.com/reference/android/media/MediaPlayer#start()),[`pause()`](https://developer.android.com/reference/android/media/MediaPlayer#pause()), and[`seekTo()`](https://developer.android.com/reference/android/media/MediaPlayer#seekTo(int)), among others.

When you call[`stop()`](https://developer.android.com/reference/android/media/MediaPlayer#stop()), however, notice that you cannot call[`start()`](https://developer.android.com/reference/android/media/MediaPlayer#start())again until you prepare the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)again.

Always keep[the state diagram](https://developer.android.com/static/images/mediaplayer_state_diagram.gif)in mind when writing code that interacts with a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)object, because calling its methods from the wrong state is a common cause of bugs.

## Release the MediaPlayer

A[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)can consume valuable system resources. Therefore, you should always take extra precautions to make sure you are not hanging on to a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)instance longer than necessary. When you are done with it, you should always call[`release()`](https://developer.android.com/reference/android/media/MediaPlayer#release())to make sure any system resources allocated to it are properly released.

For example, if you are using a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)and your activity receives a call to[`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()), you must release the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), because it makes little sense to hold on to it while your activity is not interacting with the user (unless you are playing media in the background, which is discussed in the next section).

When your activity is resumed or restarted, of course, you need to create a new[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)and prepare it again before resuming playback.

Here's how you should release and then nullify your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer):  

### Kotlin

    mediaPlayer?.release()
    mediaPlayer = null

### Java

    mediaPlayer.release();
    mediaPlayer = null;

As an example, consider the problems that arise if you forget to release the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)when your activity stops, but create a new one when the activity starts again. When the user changes the screen orientation (or changes the device configuration in another way), the system restarts the activity by default. You might quickly consume all of the system resources as the user rotates the device back and forth between portrait and landscape, because at each orientation change, you create a new[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)that you never release.

For more information about runtime restarts, see[Handling Runtime Changes](https://developer.android.com/guide/topics/resources/runtime-changes).

You may be wondering what happens if you want to continue playing "background media" even when the user leaves your activity, much in the same way that the built-in Music application behaves. In this case, what you need is a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)controlled by a Service, as discussed in the next section

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app.[Read more](https://developer.android.com/media/media3)about it.

These pages cover topics relating to recording, storing, and playing back audio and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)