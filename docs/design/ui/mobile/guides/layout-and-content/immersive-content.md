---
title: https://developer.android.com/design/ui/mobile/guides/layout-and-content/immersive-content
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/immersive-content
source: md.txt
---

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-hero.png)

You can use [immersive mode](https://developer.android.com/develop/ui/views/layout/immersive) to hide the system bars for a full-screen
experience. This is useful for enabling users to enjoy a fully immersive
experience for video, games, images, and books, and to avoid accidental exits
during a game.

## Takeaways

- Provide an intuitive way for users to display UI--for example, tapping on the
  screen during video playback displays video playback controls and system bars.

- Never permanently hide system bars on personal devices. You cannot permanently
  hide system bars in your app unless for an [Android Enterprise](https://www.android.com/enterprise/management/)
  deployment, so your designs should account for them to provide the optimal
  experience. Read more about [designing for system bars](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars).

- Provide an overlay or scrim for overlaying text and controls.

- Combine immersive mode with other features, such as picture-in-picture (PiP)
  and Chromecast, to continue the experience.

- Immersive mode causes users to lose easy access to system navigation, so use
  it only when the benefit to the user experience goes beyond simply using extra
  screen space.

- Fullscreen experiences aren't appropriate for all content. Consider when to
  help a user avoid accidental exits from frequent taps, like a game, or have an
  uninterrupted view to enjoy videos or books.

Be mindful of how often users jump in and out of apps to check notifications, to
conduct impromptu searches, or to take other actions. Immersive mode causes
users to lose easy access to system navigation, so use it only when the benefit
to the user experience goes beyond simply using extra screen space.

Fullscreen experiences aren't appropriate for all content. Consider when to help
a user avoid accidental exits from frequent taps, like a game, or have an
uninterrupted view to enjoy videos or books.

To implement immersive mode, you can use `WindowInsetsControllerCompat` to hide
both the status bar and the navigation bar--or just one of them. For details,
refer to the [Hide system bars developer guide](https://developer.android.com/develop/ui/views/layout/immersive).

The following sections describe examples of immersive mode use cases.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/images/design/ui/mobile/immersive-mode-tap-to-reveal.mp4) and watch it with a video player. **Video 1:** Video playback - tapping to reveal relevant video player UI

<br />

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-1-hidden-status.png) **Figure 1:** Hidden status and navigation bars can help the reader fully engage with books

<br />

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-2-game.png) **Figure 2:** Take advantage of immersive mode in game apps to prevent accidental system UI taps

<br />

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-3-video-call.png) **Figure 3:** Full-screen imagery increases the immersion of a video call

<br />

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-4-audience-immersion.png) **Figure 4:** Presentation in full screen allows for audience immersion

<br />

![](https://developer.android.com/static/images/design/ui/mobile/immersive-content-5-wayfinding.png) **Figure 5:** Wayfinding directory kiosk on a non-personal device ([DPC](https://developer.android.com/work/dpc/build-dpc) or enterprise deployment app)

## Related services \& Technologies

Android has several features that work well to enhance your user's content
experience. For more check out:

- [Exoplayer](https://developer.android.com/guide/topics/media/exoplayer)
- [Picture in picture](https://developer.android.com/design/ui/mobile/guides/home-screen/picture-in-picture)
- [Chromecast](https://developers.google.com/cast/docs/ux_guidelines)