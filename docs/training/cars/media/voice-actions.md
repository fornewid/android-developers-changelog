---
title: https://developer.android.com/training/cars/media/voice-actions
url: https://developer.android.com/training/cars/media/voice-actions
source: md.txt
---

# Support voice actions

Integrate voice actions into your media app to enhance driver safety and convenience by minimizing distractions. When Android Auto or Android Automotive OS (AAOS) detects and interprets a voice action, they deliver the action to your app through the`onPlayFromSearch`callback.

Upon receiving the callback, your app finds content that matches the query string and then starts playback. Your app must account for various query categories, such as genre, artist, album, song name, radio station, or playlist. Additionally, your app must handle an empty query string, which indicates a general request for music.

If your app is playing one media item, the user can say "Play \[song title\]" to tell your app to play a different song without looking at or touching the car's display. Users can initiate queries by clicking the appropriate buttons on their steering wheel or speaking the hotwords "OK Google."
| **Design guidelines:** To learn more, see[Create apps](https://developer.android.com/cars/design/create-apps).

When Android Auto or AAOS detects and interprets a voice action, Android Auto or AAOS delivers that voice action to the app through[`onPlayFromSearch`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)). Upon receiving this callback, the app finds content to match the`query`string and then starts playback.

Users can specify different categories of terms in their query: genre, artist, album, song name, radio station, or playlist, among others. When building support for search, account for all the categories that make sense for your app. If Android Auto or AAOS detects that a given query fits into a specific category, extras are appended in the`extras`parameter. You can send these extras:

- [`EXTRA_MEDIA_ALBUM`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ALBUM)
- [`EXTRA_MEDIA_ARTIST`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST)
- [`EXTRA_MEDIA_GENRE`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_GENRE)
- [`EXTRA_MEDIA_PLAYLIST`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_PLAYLIST)
- [`EXTRA_MEDIA_TITLE`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_TITLE)

Account for an empty`query`string, which can be sent by Android Auto or AAOS if the user doesn't specify search terms. For example, if the user says "Play some music." In this case, your app can start a recently played or new track.

If your app can't process a search quickly, don't block in`onPlayFromSearch`. Instead, set the playback state to[`STATE_CONNECTING`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_CONNECTING())and perform the search on an async thread.

When playback starts, consider populating the media session's queue with related content. For example, if the user requests an album to be played, your app could fill the queue with the album's tracklist.

In addition to "Play" queries, Android Auto and AAOS recognize voice queries to control playback like "pause music" and "next song" and match these commands to the appropriate media session callbacks, such as`onPause`and`onSkipToNext`.

To learn more about implementing voice-enabled playback actions, see[Google Assistant and media apps](https://developer.android.com/media/implement/assistant).