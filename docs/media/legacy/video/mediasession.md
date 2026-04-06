---
title: Media session callbacks  |  Legacy media APIs  |  Android Developers
url: https://developer.android.com/media/legacy/video/mediasession
source: html-scrape
---

These guides discuss the MediaCompat APIs, which are no longer updated. We strongly recommend using the [Jetpack Media3](/guide/topics/media/media3) library instead.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media session callbacks Stay organized with collections Save and categorize content based on your preferences.




Since a video app runs its media session and media controller in the same activity, the media session callbacks
are different from the implementation shown for the
[audio app](/guide/topics/media-apps/audio-app/building-an-audio-app)
server/client architecture. There are no service calls, and notifications are handled via the NotificationManager. The following table shows how the various features are controlled in each callback method:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **onPlay()** | **onPause()** | **onStop()** |
| [Audio Focus](/guide/topics/media-apps/volume-and-earphones#audio-focus) | `requestFocus()` passing in your `OnAudioFocusChangeListener`. *Always call `requestFocus()` first, proceed only if focus is granted.* |  | `abandonAudioFocus()` |
| [Media Session](/guide/topics/media-apps/working-with-a-media-session) | `setActive(true)`   - Update metadata and state | - Update metadata and state | `setActive(false)` - Update metadata and state |
| Player Implementation | Start the player | Pause the player | Stop the player |
| [Becoming Noisy](/guide/topics/media-apps/volume-and-earphones#becoming-noisy) | Register your `BroadcastReceiver` | Unregister your `BroadcastReceiver` |  |
| Notifications | Show notification | Update notification |  |

**Note:** People using the Google Assistant can control your app with voice commands
if you create your MediaSession with the necessary callbacks. The
requirements are explained in the
[Google Assistant documentation](/guide/topics/media-apps/interacting-with-assistant).