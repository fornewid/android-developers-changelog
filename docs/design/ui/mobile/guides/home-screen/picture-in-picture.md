---
title: https://developer.android.com/design/ui/mobile/guides/home-screen/picture-in-picture
url: https://developer.android.com/design/ui/mobile/guides/home-screen/picture-in-picture
source: md.txt
---

# Picture-in-picture

![](https://developer.android.com/static/images/design/ui/mobile/pip-hero.png)

Picture-in-picture (PiP) is a type of multi-window mode intended for activities that play full-screen video. It lets the user watch a video in a small window pinned to a corner of the screen while navigating between apps or browsing content on the main screen.
![](https://developer.android.com/static/images/design/ui/mobile/pip-1-continue-video-experience.png)**Figure 1:**Your users can continue their video experience even when not in your app

## Takeaways

- Make sure UI elements are hidden and video playback continues when the activity is in PiP mode.
- Disable seamless resizing for non-video content.
- Video playback activities with minimal UI provide the best user experience.
- Avoid showing anything except the video content.

## Add support for picture-in-picture to your app

By default, the system does not automatically support PiP for apps and needs to be declared to support the feature.

The PiP window appears in the topmost layer of the screen, in a corner chosen by the system.

### Controls

By default, Android provides PiP controls for closing the window, expanding it back to fullscreen, settings, and media playback. Your app can add custom actions and appropriate icon assets to allow users to interact with the PiP content.

The user can display these controls from the PiP window menu by tapping the window on a mobile device or selecting the menu from the TV remote. If an app has an[active media session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session), controls for play, pause, next, and previous also display. Read about how to[add these controls](https://developer.android.com/develop/ui/views/picture-in-picture#add_controls).

In PiP mode, your activity displays in a small window. Users cannot interact with your app's other UI elements in this mode, and the details of small UI elements in the PiP window may be difficult to see.

<br />

![Default PiP controls](https://developer.android.com/static/images/design/ui/mobile/pip-2-default-controls.png)

Default PiP controls.  
![Example of custom PiP controls](https://developer.android.com/static/images/design/ui/mobile/pip-3-custom-controls.png)

Example of custom PiP controls.

<br />

## Usage

Allow users to continue watching their video not only within your app, but continue across their device. Your app controls when the current activity enters PiP mode--this can be an interaction such as leaving the current view or swiping up to go home.

Here are some examples of possible actions:

- An activity can enter PiP mode when the user taps the home button or swipes up to home. This is how Google Maps continues to display directions while the user runs another activity at the same time.

  ![](https://developer.android.com/static/images/design/ui/mobile/pip-4-wayfinding.png)**Figure 4:**PiP used to continue wayfinding experience
- Your app can move a video into PiP mode when the user navigates back from the video to browse other content.

- Your app can switch a video into PiP mode while a user watches the end of an episode of content. The main screen displays promotional or summary information about the next episode in the series.

- Your app can provide a way for users to queue up additional content while they watch a video. The video continues playing in PiP mode while the main screen displays a content selection activity.

Use an interaction pattern that compliments the viewing experience without being disruptive. For example, if a video is at the end of an episode of content, entering PiP when leaving the home screen will require additional user action to return and stop playback or navigate small controls.

In your app, a user might select a new video when browsing for content on the main screen, while a video playback activity is in PiP mode. Play the new video in the existing playback activity in full screen mode, instead of launching a new activity that might confuse the user.

### Interaction patterns

Users can drag the PiP window to another location.

**Single-tap**the window to display a full-screen toggle, a close button, a settings button, and custom actions provided by your app (for example, play controls).

<br />

![](https://developer.android.com/static/images/design/ui/mobile/PiP_defaultControls_fullWidth.png)**Figure 5:**Default PiP controls

<br />

**Double-tap**the window to toggle between the current PiP size and the maximum or minimum PiP size---for example, double-tapping a maximized window minimizes it, and the converse is true as well.

<br />

![](https://developer.android.com/static/images/design/ui/mobile/pip-6-toggling-between-min-max-size.png)**Figure 6:**Toggling between min and max size PiP with double-tap

<br />

**Stash**the window by dragging it to the left or right edge. To unstash the window, either tap the visible part of the stashed window or drag it out.

<br />

![](https://developer.android.com/static/images/design/ui/mobile/pip-7-stashed.png)**Figure 7:**PiP stashed

<br />

**Resize**the PiP window using pinch-to-zoom.

**Swipe**the PiP down to remove the window.

<br />

![](https://developer.android.com/static/images/design/ui/mobile/pip-8-swiping-down.png)**Figure 8:**Swiping down

<br />

### Transitions

#### Smooth enter to PiP animation

A user triggering PiP mode causes the current activity to shrink from fullscreen to a small window, which continues showing the content without overlaying any UI.

Android 12 added significant cosmetic improvements to the animated transitions between fullscreen and PiP windows. We strongly recommend implementing all applicable changes; once you've done so, these changes automatically scale to large screens such as foldables and tablets without any further required work.

If your app doesn't include these applicable updates, PiP transitions are still functional, but the animations are less polished. For example, transitioning from fullscreen to PiP mode can cause the PiP window to disappear during the transition before it reappears when the transition is complete.

Starting in Android 12, the[`PictureInPictureParams.Builder.setAutoEnterEnabled(true)`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean))flag provides much smoother animation for transitioning to video content in PiP mode using gesture navigation---for example, when swiping up to home from fullscreen. We recommend this if your app falls in the`ENTERTAINMENT`,`COMMUNICATION`, or`VIDEO_PLAYER`app category.

If your app doesn't include this change, PiP transitions with gesture navigation are still functional but the animations are less polished. Video 1 shows an example of this: the window shrinks into the app icon and disappears, then reappears when the transition is complete.

<br />

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/PiP-video-1-before-setAutoEnterEnabled.mp4)and watch it with a video player.

Less polished transition experience when PiP does not have`setAutoEnterEnabled`properly implemented  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/PiP-video-2-after.mp4)and watch it with a video player.

Polished transition experience with`setAutoEnterEnabled`added to the app.

<br />

| **Note:** Setting`setAutoEnterEnabled(true)`also disables seamless resizing for non-video content---for example, maps.

#### Smooth video visuals

When we introduced PiP in Android 8.0,[`sourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect))indicated the area of the activity that is visible following the transition into PiP---for example, the video view bounds in a video player. Starting with Android 12, the OS uses`sourceRectHint`to implement a much smoother animation both when entering and exiting PiP mode.

If your app doesn't provide a proper`sourceRectHint`, PiP transitions are still functional but animations are less polished. For example, video 3 shows a less polished example of a transition from fullscreen to PiP mode: after the fullscreen window shrinks to the PiP window, it's covered by a black overlay before revealing the video once again.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/PiP-video-3-before-sourceRectHint.mp4)and watch it with a video player.**Video 3:** Less polished transition experience when PiP does not have`sourceRectHint`properly implemented

To see an example of how PiP animation looks when`sourceRectHint`is properly implemeneted, see video 2 in the preceding section.

Refer to the[Android Kotlin PictureInPicture sample](https://github.com/android/media-samples/tree/main/PictureInPictureKotlin/#readme)as a reference for enabling a polished transition experience.

For more on implementing PiP, see the[Picture-in-picture developer documentation](https://developer.android.com/develop/ui/views/picture-in-picture).