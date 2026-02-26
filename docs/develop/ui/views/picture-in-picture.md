---
title: https://developer.android.com/develop/ui/views/picture-in-picture
url: https://developer.android.com/develop/ui/views/picture-in-picture
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to support picture-in-picture in Compose. [Picture-in-picture →](https://developer.android.com/develop/ui/compose/system/picture-in-picture) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Starting in Android 8.0 (API level 26), Android allows activities to launch in
picture-in-picture (PiP) mode. PiP is a special type of multi-window mode used
for video playback, video calls, and navigation. It lets the user pin the
existing activity window to a corner of the screen while navigating between apps
or browsing content on the main screen.

> [!CAUTION]
> **Caution:** Don't use a system alert window (SAW) for implementing a Picture-in-Picture experience. SAW is reserved for the framework's system-level user interactions.

Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/images/pip.mp4) and watch it with a video player.

PiP leverages the multi-window APIs made available in Android 7.0 to provide the
pinned video overlay window. To add PiP to your app, you need to register your
activities that support PiP, switch your activity to PiP mode as needed, and
make sure UI elements are hidden and video playback continues when the activity
is in PiP mode.

The PiP window appears in the topmost layer of the screen, in a corner chosen by
the system.

> [!TIP]
> **Tip:** While this guide describes implementing PiP in views, see [Add PiP to your app with a Compose video player](https://developer.android.com/jetpack/compose/system/picture-in-picture) to do this in Compose.

PiP is also supported on compatible Android TV OS devices running
Android 14 (API level 34) or later. While there are many similarities, there are
additional considerations when using
[PiP on TV](https://developer.android.com/training/tv/start/multitasking).

## How users can interact with the PiP window

Users can drag the PiP window to another location. Starting in Android 12, users
can also:

- Single-tap the window to display a full-screen toggle, a close button, a
  settings button, and custom actions provided by your app (for example, play
  controls).

- Double-tap the window to toggle between the current PiP size and the maximum
  or minimum PiP size---for example, double-tapping a maximized window
  minimizes it, and the converse is true as well.

- Stash the window by dragging it to the left or right edge. To unstash the
  window, either tap the visible part of the stashed window or drag it out.

- Resize the PiP window using pinch-to-zoom.

Your app controls when the current activity enters PiP mode. Here are some
examples:

- An activity can enter PiP mode when the user taps the home button or swipes
  up to home. This is how Google Maps continues to display directions while
  the user runs another activity at the same time.

- Your app can move a video into PiP mode when the user navigates back from
  the video to browse other content.

- Your app can switch a video into PiP mode while a user watches the end of an
  episode of content. The main screen displays promotional or summary
  information about the next episode in the series.

- Your app can provide a way for users to queue up additional content while
  they watch a video. The video continues playing in PiP mode while the main
  screen displays a content selection activity.

## Declare PiP support

By default, the system does not automatically support PiP for apps. If you want
support PiP in your app, register your video activity in your manifest by
setting `android:supportsPictureInPicture` to `true`. Also, specify that your
activity handles layout configuration changes so that your activity doesn't
relaunch when layout changes occur during PiP mode transitions.

    <activity android:name="VideoActivity"
        android:supportsPictureInPicture="true"
        android:configChanges=
            "screenSize|smallestScreenSize|screenLayout|orientation"
        ...

> [!NOTE]
> **Note:** To learn more about configuration changes, how to restrict Activity recreation if needed, and how to react to those configuration changes from the View system and Jetpack Compose, check out the [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes) page.

## Implement PiP with Jetpack

Use the [Jetpack Picture-in-Picture library](https://developer.android.com/jetpack/androidx/releases/core#core-pip_version_10_2) to implement
picture-in-picture experience as it streamlines integration and reduces common
in-app issues. Refer to our [platform sample app](https://github.com/android/platform-samples/tree/main/samples/user-interface/picture-in-picture) to see an
example of its usage. However, if you prefer to implement PiP using the
platform APIs, refer to the following documentation.

## Switch your activity to PiP

Starting with Android 12, you can switch your activity to PiP mode by setting
the [`setAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)) flag to `true`. With this setting, an activity
automatically switches to PiP mode as needed without having to explicitly call
[`enterPictureInPictureMode()`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) in [`onUserLeaveHint`](https://developer.android.com/reference/android/app/Activity#onUserLeaveHint()). And this has the
added benefit of providing much smoother transitions. For details, see [Make
transitions to PiP mode smoother from gesture navigation](https://developer.android.com/develop/ui/views/picture-in-picture#setautoenterenabled).

If you're targeting Android 11 or lower, an activity must call
[`enterPictureInPictureMode()`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode())
to switch to PiP mode. For example, the following code switches an activity to
PiP mode when the user clicks a dedicated button in the app's UI:

### Kotlin

```kotlin
override fun onActionClicked(action: Action) {
    if (action.id.toInt() == R.id.lb_control_picture_in_picture) {
        activity?.enterPictureInPictureMode()
        return
    }
}
```

### Java

```java
@Override
public void onActionClicked(Action action) {
    if (action.getId() == R.id.lb_control_picture_in_picture) {
        getActivity().enterPictureInPictureMode();
        return;
    }
    ...
}
```

You might want to include logic that switches an activity into PiP mode instead
of going into the background. For example, Google Maps switches to PiP mode if
the user presses the home or recents button while the app is navigating. You can
catch this case by overriding
[`onUserLeaveHint()`](https://developer.android.com/reference/android/app/Activity#onUserLeaveHint()):

### Kotlin

```kotlin
override fun onUserLeaveHint() {
    if (iWantToBeInPipModeNow()) {
        enterPictureInPictureMode()
    }
}
```

### Java

```java
@Override
public void onUserLeaveHint () {
    if (iWantToBeInPipModeNow()) {
        enterPictureInPictureMode();
    }
}
```

## Recommended: provide users a polished PiP transition experience

Android 12 added significant cosmetic improvements to the animated transitions
between fullscreen and PiP windows. We strongly recommend implementing all
applicable changes; once you've done so, these changes automatically scale to
large screens such as foldables and tablets without any further required work.

If your app doesn't include applicable updates, PiP transitions are still
functional, but the animations are less polished. For example, transitioning
from fullscreen to PiP mode can cause the PiP window to disappear during the
transition before it reappears when the transition is complete.

These changes involve the following.

- Making transitions to PiP mode smoother from gesture navigation
- Setting a proper `sourceRectHint` for entering and exiting PiP mode
- Disabling seamless resizing for non-video content

Refer to the [Android
Kotlin PictureInPicture sample](https://github.com/android/media-samples/tree/main/PictureInPictureKotlin/#readme)
as a reference for enabling a polished transition experience.

### Make transitions to PiP mode smoother from gesture navigation

Starting in Android 12, the [`setAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)) flag provides much
smoother animation for transitioning to video content in PiP mode using gesture
navigation---for example, when swiping up to home from fullscreen.

Complete the following steps to make this change:

1. Use `setAutoEnterEnabled` to construct
   [`PictureInPictureParams.Builder`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder):

   ### Kotlin

   ```kotlin
   setPictureInPictureParams(PictureInPictureParams.Builder()
       .setAspectRatio(aspectRatio)
       .setSourceRectHint(sourceRectHint)
       .setAutoEnterEnabled(true)
       .build())
   ```

   ### Java

   ```java
   setPictureInPictureParams(new PictureInPictureParams.Builder()
       .setAspectRatio(aspectRatio)
       .setSourceRectHint(sourceRectHint)
       .setAutoEnterEnabled(true)
       .build());
   ```

   > [!NOTE]
   > **Note:** When `setAutoEnterEnabled` is enabled, you don't need to explicitly call [`enterPictureInPictureMode`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) in [`onUserLeaveHint`](https://developer.android.com/reference/android/app/Activity#onUserLeaveHint()).

2. Call `setPictureInPictureParams` with the up-to-date
   `PictureInPictureParams` early. The app doesn't wait for the
   `onUserLeaveHint` callback (as it would have done in Android 11).

   For example, you may want to call `setPictureInPictureParams` on the very
   first playback and any following playback if the aspect ratio is changed.
3. Call `setAutoEnterEnabled(false)`, but only as it's necessary. For example,
   you probably don't want to enter PiP if the current playback is in a paused
   state.

### Set a proper `sourceRectHint` for entering and exiting PiP mode

Starting with the introduction of PiP in Android 8.0, [`setSourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect))
indicated the area of the activity that is visible following the transition into
picture-in-picture---for example, the video view bounds in a video player.

With Android 12, the system uses `sourceRectHint` to implement a much smoother
animation both when entering and exiting PiP mode.

> [!NOTE]
> **Note:** If your app doesn't provide a proper `sourceRectHint`, the system tries to apply a content overlay during the PiP entering animation, which makes for a poor user experience.

To properly set `sourceRectHint` for entering and exiting PiP mode:

1. Construct [`PictureInPictureParams`](https://developer.android.com/reference/android/app/PictureInPictureParams)
   using the proper bounds as `sourceRectHint`. We recommend also attaching a
   layout change listener to the video player:

   ### Kotlin

   ```kotlin
   val mOnLayoutChangeListener =
   OnLayoutChangeListener { v: View?, oldLeft: Int,
           oldTop: Int, oldRight: Int, oldBottom: Int, newLeft: Int, newTop:
           Int, newRight: Int, newBottom: Int ->
       val sourceRectHint = Rect()
       mYourVideoView.getGlobalVisibleRect(sourceRectHint)
       val builder = PictureInPictureParams.Builder()
           .setSourceRectHint(sourceRectHint)
       setPictureInPictureParams(builder.build())
   }

   mYourVideoView.addOnLayoutChangeListener(mOnLayoutChangeListener)
   ```

   ### Java

   ```java
   private final View.OnLayoutChangeListener mOnLayoutChangeListener =
           (v, oldLeft, oldTop, oldRight, oldBottom, newLeft, newTop, newRight,
           newBottom) -> {
       final Rect sourceRectHint = new Rect();
       mYourVideoView.getGlobalVisibleRect(sourceRectHint);
       final PictureInPictureParams.Builder builder =
           new PictureInPictureParams.Builder()
               .setSourceRectHint(sourceRectHint);
       setPictureInPictureParams(builder.build());
   };

   mYourVideoView.addOnLayoutChangeListener(mOnLayoutChangeListener);
   ```
2. If necessary, update the [`sourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect)) before the system starts the
   exit transition. When the system is about to exit PiP mode, the activity's
   view hierarchy is laid out to its destination configuration (for example,
   full screen). The app can attach a layout change listener to its root view
   or target view (such as the video player view) to detect the event and
   update the `sourceRectHint` before the animation begins.

   ### Kotlin

   ```kotlin
   // Listener is called immediately after the user exits PiP but before animating.
   playerView.addOnLayoutChangeListener { _, left, top, right, bottom,
                       oldLeft, oldTop, oldRight, oldBottom ->
       if (left != oldLeft
           || right != oldRight
           || top != oldTop
           || bottom != oldBottom) {
           // The playerView's bounds changed, update the source hint rect to
           // reflect its new bounds.
           val sourceRectHint = Rect()
           playerView.getGlobalVisibleRect(sourceRectHint)
           setPictureInPictureParams(
               PictureInPictureParams.Builder()
                   .setSourceRectHint(sourceRectHint)
                   .build()
           )
       }
   }
   ```

   ### Java

   ```java
   // Listener is called right after the user exits PiP but before animating.
   playerView.addOnLayoutChangeListener((v, left, top, right, bottom,
                       oldLeft, oldTop, oldRight, oldBottom) -> {
       if (left != oldLeft
           || right != oldRight
           || top != oldTop
           || bottom != oldBottom) {
           // The playerView's bounds changed, update the source hint rect to
           // reflect its new bounds.
           final Rect sourceRectHint = new Rect();
           playerView.getGlobalVisibleRect(sourceRectHint);
           setPictureInPictureParams(
               new PictureInPictureParams.Builder()
                   .setSourceRectHint(sourceRectHint)
                   .build());
       }
   });
   ```

> [!NOTE]
> **Note:** The Jetpack library `androidx.activity` exposes the method [`trackPipAnimationHintView`](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#(android.app.Activity).trackPipAnimationHintView(android.view.View)) that does the work of setting the [`sourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect)). It implements the work outlined in the preceding steps, using the view passed into that method.

### Disable seamless resizing for non-video content

Android 12 adds the [`setSeamlessResizeEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSeamlessResizeEnabled(boolean)) flag, which provides a much
smoother cross-fading animation when resizing non-video content in the PiP
window. Previously, resizing non-video content in a PiP window could create
jarring visual artifacts.

> [!NOTE]
> **Note:** Make sure the content is actually seamless resize capable before turning on this flag.

To enable seamless resizing for video content:

### Kotlin

```kotlin
setPictureInPictureParams(PictureInPictureParams.Builder()
    .setSeamlessResizeEnabled(true)
    .build())
```

### Java

```java
setPictureInPictureParams(new PictureInPictureParams.Builder()
    .setSeamlessResizeEnabled(true)
    .build());
```

## Handle UI during PiP

When the activity enters or exits Picture-in-Picture (PiP) mode, the system calls [`Activity.onPictureInPictureModeChanged()`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureModeChanged(boolean,%0Aandroid.content.res.Configuration))
or [`Fragment.onPictureInPictureModeChanged()`](https://developer.android.com/reference/android/app/Fragment#onPictureInPictureModeChanged(boolean,%0Aandroid.content.res.Configuration)).

Android 15 introduces changes that ensure an even
smoother transition when entering PiP mode. This is beneficial for apps that
have UI elements overlaid on top of their main UI, which goes into PiP.

Developers use the [`onPictureInPictureModeChanged()`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureModeChanged(boolean,%20android.content.res.Configuration)) callback to define logic that toggles the visibility of the overlaid UI elements.
This callback is triggered when the PiP enter or exit animation is completed.
Beginning in Android 15, the [`PictureInPictureUiState`](https://developer.android.com/reference/android/app/PictureInPictureUiState) class includes a new state.

With this new UI state, apps targeting Android 15 observe the [`Activity#onPictureInPictureUiStateChanged()`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureUiStateChanged(android.app.PictureInPictureUiState))
callback being invoked with [`isTransitioningToPip()`](https://developer.android.com/reference/android/app/PictureInPictureUiState#isTransitioningToPip()) as soon as the PiP animation starts.
There are many UI elements that are not relevant for the app when it is in PiP mode,
for example, views or layout that include information such as suggestions, upcoming
video, ratings, and titles. When the app goes into PiP mode, use the `onPictureInPictureUiStateChanged()` callback to hide these UI elements. When the
app goes to full screen mode from the PiP window, use the `onPictureInPictureModeChanged()` callback to unhide these elements, as shown in the following examples:

### Kotlin

```kotlin
override fun onPictureInPictureUiStateChanged(pipState: PictureInPictureUiState) {
        if (pipState.isTransitioningToPip()) {
          // Hide UI elements.
        }
    }
```

### Java

```java
@Override
public void onPictureInPictureUiStateChanged(PictureInPictureUiState pipState) {
        if (pipState.isTransitioningToPip()) {
          // Hide UI elements.
        }
    }
```

### Kotlin

```kotlin
override fun onPictureInPictureModeChanged(isInPictureInPictureMode: Boolean) {
        if (isInPictureInPictureMode) {
          // Unhide UI elements.
        }
    }
```

### Java

```java
@Override
public void onPictureInPictureModeChanged(boolean isInPictureInPictureMode) {
        if (isInPictureInPictureMode) {
          // Unhide UI elements.
        }
    }
```

This quick visibility toggle of irrelevant UI elements (for a PiP window) helps
ensure a smoother and flicker-free PiP enter animation.

Override these callbacks to redraw the activity's UI elements. Keep in
mind that, in PiP mode, your activity is shown in a small window. Users cannot interact
with your app's UI elements when the app is in PiP mode and the details of small UI elements
may be difficult to see. Video playback activities with minimal UI provide the best
user experience.

If your app needs to provide custom actions for PiP, see [Add controls](https://developer.android.com/develop/ui/views/picture-in-picture#add_controls) on this page. Remove other UI
elements before your activity enters PiP and restore them when your activity becomes
full screen again.

### Add controls

The PiP window can display controls when the user opens the window's menu (by
tapping the window on a mobile device, or selecting the menu from the TV
remote.)

If an app has an [active media
session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session), then play,
pause, next, and previous controls will appear.

You can also specify custom actions explicitly by building
[`PictureInPictureParams`](https://developer.android.com/reference/android/app/PictureInPictureParams)
with
[`PictureInPictureParams.Builder.setActions()`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setActions(java.util.List&lt;android.app.RemoteAction&gt;))
before entering PiP mode, and pass the params when you enter PiP mode using
[`enterPictureInPictureMode(android.app.PictureInPictureParams)`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams))
or
[`setPictureInPictureParams(android.app.PictureInPictureParams)`](https://developer.android.com/reference/android/app/Activity#setPictureInPictureParams(android.app.PictureInPictureParams)).
Be careful. If you try to add more than
[`getMaxNumPictureInPictureActions()`](https://developer.android.com/reference/android/app/Activity#getMaxNumPictureInPictureActions()),
you'll only get the maximum number.

## Continuing video playback while in PiP

When your activity switches to PiP, the system places the activity in the paused
state and calls the activity's
[`onPause()`](https://developer.android.com/reference/android/app/Activity#onPause()) method. Video
playback shouldn't be paused and instead continue playing if the activity is
paused while transitioning to PiP mode.

In Android 7.0 and later, you should pause and resume video playback when the
system calls your activity's
[`onStop()`](https://developer.android.com/reference/android/app/Activity#onStop()) and
[`onStart()`](https://developer.android.com/reference/android/app/Activity#onStart()). By doing this,
you can avoid having to check if your app is in PiP mode in `onPause()` and
explicitly continuing playback.

If you haven't set the [`setAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)) flag to `true` and you need to
pause playback in your `onPause()` implementation, check for PiP mode by calling
`isInPictureInPictureMode()` and handle playback appropriately. For example:

### Kotlin

```kotlin
override fun onPause() {
    super.onPause()
    // If called while in PiP mode, do not pause playback.
    if (isInPictureInPictureMode) {
        // Continue playback.
    } else {
        // Use existing playback logic for paused activity behavior.
    }
}
```

### Java

```java
@Override
public void onPause() {
    // If called while in PiP mode, do not pause playback.
    if (isInPictureInPictureMode()) {
        // Continue playback.
        ...
    } else {
        // Use existing playback logic for paused activity behavior.
        ...
    }
}
```

When your activity switches out of PiP mode back to full-screen mode, the system
resumes your activity and calls your
[`onResume()`](https://developer.android.com/reference/android/app/Activity#onResume()) method.

## Use a single playback activity for PiP

In your app, a user might select a new video when browsing for content on the
main screen, while a video playback activity is in PiP mode. Play the new video
in the existing playback activity in full screen mode, instead of launching a
new activity that might confuse the user.

To ensure a single activity is used for video playback requests and switched
into or out of PiP mode as needed, set the activity's `android:launchMode` to
`singleTask` in your manifest:

    <activity android:name="VideoActivity"
        ...
        android:supportsPictureInPicture="true"
        android:launchMode="singleTask"
        ...

In your activity, override
[`onNewIntent()`](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent))
and handle the new video, stopping any existing video playback if needed.

## Best practices

PiP might be disabled on devices that have low RAM. Before your app uses PiP,
check to be sure it is available by calling
[`hasSystemFeature(PackageManager.FEATURE_PICTURE_IN_PICTURE)`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)).

PiP is intended for activities that play full-screen video. When switching your
activity into PiP mode, avoid showing anything except video content. Track when
your activity enters PiP mode and hide UI elements, as described in [Handling UI
during PiP](https://developer.android.com/develop/ui/views/picture-in-picture#handling_ui).

When an activity is in PiP mode, by default it doesn't get input focus. To
receive input events while in PiP mode, use
[`MediaSession.setCallback()`](https://developer.android.com/reference/android/media/session/MediaSession#setCallback(android.media.session.MediaSession.Callback)).
For more information on using `setCallback()` see [Display a Now Playing
card](https://developer.android.com/training/tv/playback/now-playing).

When your app is in PiP mode, video playback in the PiP window can cause audio
interference with another app, such as a music player app or voice search app.
To avoid this, request audio focus when you start playing the video, and handle
audio focus change notifications, as described in [Managing Audio
Focus](https://developer.android.com/guide/topics/media-apps/audio-focus). If you receive notification
of audio focus loss when in PiP mode, pause or stop video playback.

When your app is about to enter PiP, note only the top activity enters
picture-in-picture. In some situations such as on multi-window devices, it is
possible the activity below will now be shown and become visible again alongside
the PiP activity. You should handle this case accordingly, including the
activity below getting an `onResume()` or an `onPause()` callback. It is also
possible that the user may interact with the activity. For example, if you have
a video list activity displayed and the playing video activity in PiP mode, the
user might select a new video from the list and the PiP activity should update
accordingly.

## Additional sample code

To download a sample app written in Kotlin, see [Android PictureInPicture Sample
(Kotlin)](https://github.com/android/platform-samples/tree/main/samples/user-interface/picture-in-picture).