---
title: https://developer.android.com/training/tv/playback/now-playing
url: https://developer.android.com/training/tv/playback/now-playing
source: md.txt
---

# Display a Now Playing card

TV apps that play audio may continue to do so after the user returns to the home screen or switches to another app. To do so, the app must provide a**Now Playing**card on the home screen. This card lets users understand where the audio is coming from and return to your app to control media playback.

Whenever an active[MediaSession](https://developer.android.com/reference/android/media/session/MediaSession)is present, the Android framework displays a**Now Playing**card on the home screen. The card includes media metadata such as album art, title, and app icon. When the user selects the card, the system opens the app.

## Now Playing card

After you[implement a media session](https://developer.android.com/training/tv/playback/media-session), set the session to active, and request audio focus, the**Now Playing**card appears.

**Note:** The**Now Playing** card displays only for a media session with the[FLAG_HANDLES_TRANSPORT_CONTROLS](https://developer.android.com/reference/android/media/session/MediaSession#FLAG_HANDLES_TRANSPORT_CONTROLS)flag set. This flag is deprecated on API level 26. However, this flag could still be needed on older devices for backwards compatibility.

The card is removed from the launcher screen when a[setActive(false)](https://developer.android.com/reference/android/media/session/MediaSession#setActive(boolean))call deactivates the media session or when another app initiates media playback. If playback is completely stopped and there is no active media, deactivate the media session immediately. If playback is paused, deactivate the media session after a delay, usually from 5 to 30 minutes.

## Update the card

Whenever your app updates the playback state in the`MediaSession`, the**Now Playing** card updates to show the state of the current media. To learn how to do this, see[Update the playback state](https://developer.android.com/training/tv/playback/media-session#state).

Similarly, your app can update the[MediaMetadata](https://developer.android.com/reference/android/media/MediaMetadata)to provide information to the**Now Playing** card about the current media, such as the title, subtitle, and various icons. To learn how to do this, see[Update the media metadata](https://developer.android.com/training/tv/playback/media-session#metadata).

## Respond to user action

When the user selects the**Now Playing** card, the system opens the app that owns the session. If your app provides a[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)to[setSessionActivity()](https://developer.android.com/reference/android/media/session/MediaSession#setSessionActivity(android.app.PendingIntent)), the system launches the activity you specify, as shown in the following code snippet. If not, the default system intent opens. The activity you specify must provide playback controls that let users pause or stop playback.  

### Kotlin

```kotlin
val pi: PendingIntent = Intent(context, MyActivity::class.java).let { intent ->
    PendingIntent.getActivity(
            context, 99 /*request code*/,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT
    )
}
session.setSessionActivity(pi)
```

### Java

```java
Intent intent = new Intent(context, MyActivity.class);
PendingIntent pi = PendingIntent.getActivity(context, 99 /*request code*/,
        intent, PendingIntent.FLAG_UPDATE_CURRENT);
session.setSessionActivity(pi);
```

## Accepted use cases

The**Now Playing**card should only be used in cases where the user expects audio to continue playing in the background when leaving your app. Video playback or sound from a game should always pause, unless your app is integrating and compliant with picture-in-picture.