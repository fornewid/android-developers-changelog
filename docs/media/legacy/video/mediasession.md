---
title: https://developer.android.com/media/legacy/video/mediasession
url: https://developer.android.com/media/legacy/video/mediasession
source: md.txt
---

# Media session callbacks

Since a video app runs its media session and media controller in the same activity, the media session callbacks are different from the implementation shown for the[audio app](https://developer.android.com/guide/topics/media-apps/audio-app/building-an-audio-app)server/client architecture. There are no service calls, and notifications are handled via the NotificationManager. The following table shows how the various features are controlled in each callback method:

<br />

|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------------------|
|                                                                                                             | **onPlay()**                                                                                                                       | **onPause()**                      | **onStop()**                                   |
| [Audio Focus](https://developer.android.com/guide/topics/media-apps/volume-and-earphones#audio-focus)       | `requestFocus()`passing in your`OnAudioFocusChangeListener`. *Always call`requestFocus()`first, proceed only if focus is granted.* |                                    | `abandonAudioFocus()`                          |
| [Media Session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)         | `setActive(true)` - Update metadata and state                                                                                      | - Update metadata and state        | `setActive(false)` - Update metadata and state |
| Player Implementation                                                                                       | Start the player                                                                                                                   | Pause the player                   | Stop the player                                |
| [Becoming Noisy](https://developer.android.com/guide/topics/media-apps/volume-and-earphones#becoming-noisy) | Register your`BroadcastReceiver`                                                                                                   | Unregister your`BroadcastReceiver` |                                                |
| Notifications                                                                                               | Show notification                                                                                                                  | Update notification                |                                                |

<br />

| **Note:** People using the Google Assistant can control your app with voice commands if you create your MediaSession with the necessary callbacks. The requirements are explained in the[Google Assistant documentation](https://developer.android.com/guide/topics/media-apps/interacting-with-assistant).