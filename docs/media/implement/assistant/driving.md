---
title: https://developer.android.com/media/implement/assistant/driving
url: https://developer.android.com/media/implement/assistant/driving
source: md.txt
---

# Media apps on Google Assistant driving mode

Google Assistant helps drivers perform tasks they're already doing while driving. It reduces distraction by providing glanceable, voice-forward multimodal experiences. Driving mode helps make every drive safer, more informed, connected, and enjoyable.

## Using driving mode

A device automatically enters driving mode when you start navigating in Google Maps.

To disable driving mode:

1. Navigate to**Google Maps Settings \> Navigation Settings \> Google Assistant settings \> Manage Driving Mode**.
2. Turn off the**Driving Mode**setting.

![](https://developer.android.com/static/media/images/ADM/adm-driving-mode.png)

## App prerequisites

In order for driving mode to work correctly with your media app, the app must meet these requirements:

- Follow all the directions in[Google Assistant and media apps](https://developer.android.com/media/implement/assistant)
- Your app must declare that it supports media for Android Auto. Follow the directions at[declare media support for Android Auto](https://developer.android.com/training/cars/media/auto#manifest-car-app).
- Handle[audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus)
- Use`PlaybackState`to[report errors](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session#errors)
- Implement a[MediaBrowserService](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice)and a[MediaSession](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)
- Your MediaSession must implement these callbacks:
  - `onPlay()`
  - `onPlayFromSearch()`
  - `onPlayFromUri()`
  - `onSkipToNext()`
  - `onSkipToPrevious()`
  - `onPause()`
  - `onStop()`
- Keep the`MediaSession`metadata current by calling`setMetadata()`.

## Driving mode and playback controls

Each app determines the transport controls that appear on the screen. Do this by[connecting its`MediaSession`to`TransportControls`](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowser-client#connect-ui-and-mediacontroller). For example, a music player usually shows these controls:  
![](https://developer.android.com/static/media/images/ADM/adm-controls.png)

Any other supported actions are invoked via voice commands.

## Media recommendations in driving mode

Driving mode displays recommendations in two places, the "For you" page and the app's browse page. The screens look similar:  
![controls](https://developer.android.com/static/media/images/ADM/adm-for-you.png)**For you**  
![controls](https://developer.android.com/static/media/images/ADM/adm-app-browse.png)**App browse**  

The Assistant calls[`MediaBrowserService.onGetRoot()`](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice)with the hint[`EXTRA_SUGGESTED`](https://developer.android.com/reference/android/service/media/MediaBrowserService.BrowserRoot#EXTRA_SUGGESTED)to retrieve recommendations. You should return a flat list of playable[`MediaItem`](https://developer.android.com/reference/android/media/browse/MediaBrowser.MediaItem)objects. The app's browse screen displays all the items in the list. The "for you" screen is not guaranteed to show the recommendations at all if there are less than 15 items in the list.

Each`MediaItem`must have media art. You can provide the type of a`MediaItem`by adding a`CONTENT_TYPE`key-value pair to the[Bundle](https://developer.android.com/reference/android/os/Bundle)in the[MediaDescription](https://developer.android.com/reference/android/media/MediaDescription)of each`MediaItem`. This helps improve the item's ranking in the "for you" page.

The possible values for`CONTENT_TYPE`are:

- ALBUM
- ARTIST
- PLAYLIST
- TV_SHOW_EPISODE
- PODCAST_EPISODE
- MUSIC
- AUDIO_BOOK
- RADIO_STATION
- VIDEO
- NEWS

## Testing

Use the[Media Control test app](https://developer.android.com/guide/topics/media-apps/audio-app/media-controller-test)to verify your app.

## Known issues

It is important to avoid opening a media app in the foreground while in driving mode. For example, when the Assistant calls`MediaBrowserService.onGetRoot()`to retrieve recommendations, your app should ensure that the state of your`PlaybackState`is`STATE_NONE`. This prevents your app from being brought to the foreground. Currently there is no way for an app to detect whether it is in driving mode or not.