---
title: https://developer.android.com/media/implement/assistant
url: https://developer.android.com/media/implement/assistant
source: md.txt
---

Google Assistant lets you use voice commands to control many devices, like
Google Home, your phone, and more. It has a built-in capability to
understand media commands ("play something by Beyoncé") and supports
media controls (like pause, skip, fast forward, thumbs up).

Assistant communicates with Android media apps using a [media
session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session). It can use
[intents](https://developer.android.com/media/implement/assistant#playback-with-an-intent) or [services](https://developer.android.com/media/implement/assistant#playback-from-service) to
launch your app and start playback. For the best results, your app should
implement all the features described on this page.
| **Note:** This guide explains how to create a media app so that the Assistant can help a user control their media. To learn how Android apps use the Assist API to improve the assistant user experience, see [Optimizing Content for the
| Assistant](https://developer.android.com/training/articles/assistant)

## Use a media session

Every audio and video app must implement a
[media session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)
so that the Assistant can operate
the transport controls once playback has started.

Note that while the Assistant only uses the actions listed in this section, the
best practice is to implement all preparation and playback APIs to ensure
compatibility with other applications. For any actions that you do not support,
the media session callbacks can simply return an error using
[`ERROR_CODE_NOT_SUPPORTED`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat#error_code_not_supported).

Enable the media and transport controls by setting these flags in your app's
`MediaSession` object:

### Kotlin

```kotlin
session.setFlags(
        MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS or
        MediaSessionCompat.FLAG_HANDLES_TRANSPORT_CONTROLS
)
```

### Java

```java
session.setFlags(MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS |
    MediaSessionCompat.FLAG_HANDLES_TRANSPORT_CONTROLS);
```
| **Note:** The Google Assistant can send commands to an existing media session. In order for the Google Assistant to create your media session, see [Playback from
| a service](https://developer.android.com/media/implement/assistant#playback-from-service).

Your app's media session must declare the actions it supports, and implement the
corresponding media session callbacks. Declare your supported actions in
[`setActions()`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setActions(long)).

The
[Universal Android Music Player](https://github.com/android/uamp)
sample project is a good example of how to set up a media session.

### Playback actions

In order to [start playback from a service](https://developer.android.com/media/implement/assistant#playback-from-service), a media session must have these `PLAY` actions and their callbacks:

| Action | Callback |
|---|---|
| `ACTION_PLAY` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlay()` |
| `ACTION_PLAY_FROM_SEARCH` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String, android.os.Bundle)` |
| `ACTION_PLAY_FROM_URI` (\*) | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromUri(android.net.Uri, android.os.Bundle)` |

Your session should also implement these `PREPARE` actions and their callbacks:

| Action | Callback |
|---|---|
| `ACTION_PREPARE` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPrepare()` |
| `ACTION_PREPARE_FROM_SEARCH` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPrepareFromSearch(java.lang.String, android.os.Bundle)` |
| `ACTION_PREPARE_FROM_URI` (\*) | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPrepareFromUri(android.net.Uri, android.os.Bundle)` |

(\*) Google Assistant URI-based actions only work for companies
that provide URIs to Google. To learn more about describing your media content to Google
see [Media Actions](https://developers.google.com/actions/media/).

By implementing the preparation APIs, the playback latency after a voice command
can be reduced. Media apps that want to improve playback latency can use the
extra time to start caching content and preparing media playback.

### Parse search queries

When a user searches for a specific media item, such as *"Play jazz on
\[your app name\]"* or *"Listen to \[song title\]"* , the
[`onPrepareFromSearch()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPrepareFromSearch(java.lang.String,%20android.os.Bundle)) or
[`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle))
callback method receives a query parameter and an extras bundle.

Your app should parse the voice search query and start playback by following these
steps:

1. Use the extras bundle and search query string returned from the voice search to filter results.
2. Build a playback queue based on these results.
3. Play the most relevant media item from the results.

| **Note:** If you support `ACTION_PREPARE_FROM_URI` and `ACTION_PLAY_FROM_URI`, you must also support `ACTION_PREPARE_FROM_SEARCH` and `ACTION_PLAY_FROM_SEARCH`. The Google Assistant will use the search query if a URI is not available.

The [`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle))
method takes an extras parameter with more detailed information from the voice
search. These extras help you find the audio content in your app for playback.
If the search results are unable to provide this data, you can implement logic
to parse the raw search query and play the appropriate tracks based on the
query.

The following extras are supported in Android Automotive OS and Android Auto:

- [`EXTRA_MEDIA_ALBUM`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ALBUM)
- [`EXTRA_MEDIA_ARTIST`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST)
- [`EXTRA_MEDIA_GENRE`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_GENRE)
- [`EXTRA_MEDIA_PLAYLIST`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_PLAYLIST)
- [`EXTRA_MEDIA_TITLE`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_TITLE)

The following code snippet shows how to override the [`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle))
method in your [`MediaSession.Callback`](https://developer.android.com/reference/android/media/session/MediaSession.Callback)
implementation to parse the voice search query and begin playback:

### Kotlin

```kotlin
override fun onPlayFromSearch(query: String?, extras: Bundle?) {
    if (query.isNullOrEmpty()) {
        // The user provided generic string e.g. 'Play music'
        // Build appropriate playlist queue
    } else {
        // Build a queue based on songs that match "query" or "extras" param
        val mediaFocus: String? = extras?.getString(MediaStore.EXTRA_MEDIA_FOCUS)
        if (mediaFocus == MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE) {
            isArtistFocus = true
            artist = extras.getString(MediaStore.EXTRA_MEDIA_ARTIST)
        } else if (mediaFocus == MediaStore.Audio.Albums.ENTRY_CONTENT_TYPE) {
            isAlbumFocus = true
            album = extras.getString(MediaStore.EXTRA_MEDIA_ALBUM)
        }

        // Implement additional "extras" param filtering
    }

    // Implement your logic to retrieve the queue
    var result: String? = when {
        isArtistFocus -> artist?.also {
            searchMusicByArtist(it)
        }
        isAlbumFocus -> album?.also {
            searchMusicByAlbum(it)
        }
        else -> null
    }
    result = result ?: run {
        // No focus found, search by query for song title
        query?.also {
            searchMusicBySongTitle(it)
        }
    }

    if (result?.isNotEmpty() == true) {
        // Immediately start playing from the beginning of the search results
        // Implement your logic to start playing music
        playMusic(result)
    } else {
        // Handle no queue found. Stop playing if the app
        // is currently playing a song
    }
}
```

### Java

```java
@Override
public void onPlayFromSearch(String query, Bundle extras) {
    if (TextUtils.isEmpty(query)) {
        // The user provided generic string e.g. 'Play music'
        // Build appropriate playlist queue
    } else {
        // Build a queue based on songs that match "query" or "extras" param
        String mediaFocus = extras.getString(MediaStore.EXTRA_MEDIA_FOCUS);
        if (TextUtils.equals(mediaFocus,
                MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE)) {
            isArtistFocus = true;
            artist = extras.getString(MediaStore.EXTRA_MEDIA_ARTIST);
        } else if (TextUtils.equals(mediaFocus,
                MediaStore.Audio.Albums.ENTRY_CONTENT_TYPE)) {
            isAlbumFocus = true;
            album = extras.getString(MediaStore.EXTRA_MEDIA_ALBUM);
        }

        // Implement additional "extras" param filtering
    }

    // Implement your logic to retrieve the queue
    if (isArtistFocus) {
        result = searchMusicByArtist(artist);
    } else if (isAlbumFocus) {
        result = searchMusicByAlbum(album);
    }

    if (result == null) {
        // No focus found, search by query for song title
        result = searchMusicBySongTitle(query);
    }

    if (result != null && !result.isEmpty()) {
        // Immediately start playing from the beginning of the search results
        // Implement your logic to start playing music
        playMusic(result);
    } else {
        // Handle no queue found. Stop playing if the app
        // is currently playing a song
    }
}
```
| **Note:** Your app should start playback in the [`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)) method as soon as you have generated a playback queue based on the user's search.

For a more detailed example on how to implement voice search to play audio
content in your app, see the [Universal Android Music Player](https://github.com/android/uamp)
sample.

### Handle empty queries

If `onPrepare()`, `onPlay()`, `onPrepareFromSearch()`, or `onPlayFromSearch()`
are called without a search query, your media app should play the "current"
media. If there is no current media, the app should try to play something, such
as a song from the most recent playlist or a random queue. The assistant uses
these APIs when a user asks to *"Play music on \[your app name\]"* without
additional information.

When a user says *"Play music on \[your app name\]"* , Android Automotive OS or
Android Auto attempts to launch your app and play audio by calling your app's [`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle))
method. However, because the user did not say the name of media item, the [`onPlayFromSearch()`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle))
method receives an empty query parameter. In these cases, your app should
respond by immediately playing audio, such as a song from the most recent
playlist or a random queue.

### Declare legacy support for voice actions

In most cases, handling the playback actions described above gives your app all
the playback functionality it needs. However, some systems require your app to
contain an Intent filter for search. You should declare support for this Intent
filter in your app's manifest files.

Include this code in the manifest file for a phone app:

    <activity>
        <intent-filter>
            <action android:name=
                 "android.media.action.MEDIA_PLAY_FROM_SEARCH" />
            <category android:name=
                 "android.intent.category.DEFAULT" />
        </intent-filter>
    </activity>

### Transport controls

After your app's media session is active, the Assistant can issue voice commands
to control playback and update media metadata. In order for this to work, your
code should enable the following actions and implement the corresponding
callbacks:

| Action | Callback | Description |
|---|---|---|
| `ACTION_SKIP_TO_NEXT` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToNext()` | Next video |
| `ACTION_SKIP_TO_PREVIOUS` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToPrevious()` | Previous song |
| `ACTION_PAUSE, ACTION_PLAY_PAUSE` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPause()` | Pause |
| `ACTION_STOP` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onStop()` | Stop |
| `ACTION_PLAY` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlay()` | Resume |
| `ACTION_SEEK_TO` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSeekTo(long)` | Rewind by 30 seconds |
| `ACTION_SET_RATING` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSetRating(android.support.v4.media.RatingCompat)` | Thumbs up/down. |
| `ACTION_SET_CAPTIONING_ENABLED` | `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSetCaptioningEnabled(boolean)` | Turn captioning on/off. |

Please note:

- For seek commands to work, the `https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat` needs to be up-to-date with the `https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setState(int, long, float, long)`. The app must call `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setPlaybackState(android.support.v4.media.session.PlaybackStateCompat)` when the state changes.
- The media app must also keep the media session metadata up-to-date. This supports questions such as "what song is playing?" The app must call `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setMetadata(android.support.v4.media.MediaMetadataCompat)` when the applicable fields (such as track title, artist, and name) change.
- `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setRatingType(int)` must be set to indicate the type of rating the app supports, and the app must implement `https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSetRating(android.support.v4.media.RatingCompat)`. If the app does not support rating, it should set the rating type to `RATING_NONE`.

The voice actions you support will likely vary by content type.

| Content Type | Required Actions |
|---|---|
| Music | **Must support**: Play, Pause, Stop, Skip to Next, and Skip to Previous **Strongly recommend support for**: Seek To |
| Podcast | **Must support**: Play, Pause, Stop, and Seek To **Recommend support for**: Skip to Next and Skip to Previous |
| Audiobook | **Must support**: Play, Pause, Stop, and Seek To |
| Radio | **Must support**: Play, Pause, and Stop |
| News | **Must support**: Play, Pause, Stop, Skip to Next, and Skip to Previous |
| Video | **Must support**: Play, Pause, Stop, Seek To, Rewind, and Fast Forward **Strongly recommend support for**: Skip to Next and Skip to Previous |

You must support as many of the actions listed above as your product offerings
allow, but still respond gracefully to any other actions. For example, if only
premium users have the ability to return to the previous item, you might raise
an error if a free tier user asks the Assistant to return to the previous item.
See the [error handling section](https://developer.android.com/media/implement/assistant#errors) for more guidance.

#### Sample voice queries to try

The following table outlines some sample queries that you should use as you
test your implementation:

| MediaSession Callback | "Hey Google" phrase to use ||
|---|---|---|
| [`onPlay()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlay()) | "Play." "Resume." ||
| [`onPlayFromSearch()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)) [`onPlayFromUri()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromUri(android.net.Uri,%20android.os.Bundle)) | **Music** | "Play music or songs on ***(app name)***." This is an empty query. "Play ***(song \| artist \| album \| genre \| playlist)*** on ***(app name)***." |
| [`onPlayFromSearch()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)) [`onPlayFromUri()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromUri(android.net.Uri,%20android.os.Bundle)) | **Radio** | "Play ***(frequency \| station)*** on ***(app name)***." |
| [`onPlayFromSearch()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)) [`onPlayFromUri()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromUri(android.net.Uri,%20android.os.Bundle)) | **Audiobook** | "Read my audiobook on ***(app name)***." "Read ***(audiobook)*** on ***(app name)***." |
| [`onPlayFromSearch()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,%20android.os.Bundle)) [`onPlayFromUri()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromUri(android.net.Uri,%20android.os.Bundle)) | **Podcasts** | "Play ***(podcast)*** on ***(app name)***." |
| [`onPause()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPause()) | "Pause." ||
| [`onStop()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onStop()) | "Stop." ||
| [`onSkipToNext()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToNext()) | "Next ***(song \| episode \| track)***." ||
| [`onSkipToPrevious()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToPrevious()) | "Previous ***(song \| episode \| track)***." ||
| [`onSeekTo()`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSeekTo(long)) | "Restart." "Skip ahead ***##*** seconds." "Go back ***##*** minutes." ||
| N/A (keep your [`MediaMetadata`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/MediaSessionCompat#setMetadata(android.support.v4.media.MediaMetadataCompat)) updated) | "What's playing?" ||

### Errors

The Assistant handles errors from a media session when they occur, and reports
them to users. Be sure that your media session updates the transport state and
error code in its `PlaybackState` correctly, as described in [Working with a
media session](https://developer.android.com/media/implement/assistant/working-with-a-media-session#errors). The Assistant
recognizes all the error codes returned by
[`getErrorCode()`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#getErrorCode()).

#### Commonly mishandled cases

Here are some examples of error cases that you should make sure you're handling
correctly:

- User needs to sign in
  - Set the `PlaybackState` error code to [`ERROR_CODE_AUTHENTICATION_EXPIRED`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat#ERROR_CODE_AUTHENTICATION_EXPIRED:kotlin.Int).
  - Set the `PlaybackState` error message.
  - If required for playback, set the `PlaybackState` state to `STATE_ERROR`, otherwise retain the rest of the `PlaybackState` as-is.
- User requests an unavailable action
  - Set the `PlaybackState` error code appropriately. For example, set the `PlaybackState` to [`ERROR_CODE_NOT_SUPPORTED`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat#ERROR_CODE_AUTHENTICATION_EXPIRED:kotlin.Int) if the action is not supported or [`ERROR_CODE_PREMIUM_ACCOUNT_REQUIRED`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat#error_code_premium_account_required) if the action is sign-in protected.
  - Set the `PlaybackState` error message.
  - Retain the rest of the `PlaybackState` as-is.
- User requests content not available in the app
  - Set the `PlaybackState` error code appropriately. For example, use [`ERROR_CODE_NOT_AVAILABLE_IN_REGION`](https://developer.android.com/reference/kotlin/android/support/v4/media/session/PlaybackStateCompat#error_code_not_available_in_region).
  - Set the `PlaybackState` error message.
  - Set the `PlaybackSate` state to `STATE_ERROR` to interrupt playback, otherwise retain the rest of the `PlaybackState` as-is.
- User requests content where an exact match is unavailable. For example, a free-tier user asking for content only available to premium-tier users.
  - We recommend that you do not return an error, and should instead prioritize finding something similar to play. The Assistant will handle speaking the most relevant voice response before playback starts.

## Playback with an intent

The Assistant can launch an audio or video app and start playback by sending an
intent with a [deep link](https://developer.android.com/training/app-links).

The intent and its deep link can come from different sources:

- When the Assistant is starting a mobile app, it can use Google search to retrieve marked up content that supplies a [watch action](https://developers.google.com/search/docs/data-types/tv-movies#watch-actions) with a link.
- When Assistant is starting a TV app, your app should include a [TV Search Provider](https://developer.android.com/training/tv/discovery/searchable) to expose URIs for media content. The Assistant sends a query to the content provider which should return an intent containing a URI for the deep link and an optional action. If the query returns an action in the intent, the Assistant sends that action and the URI back to the your app. If the provider did not specify an action, Assistant will add `https://developer.android.com/reference/android/content/Intent#ACTION_VIEW` to the Intent.

The Assistant adds the extra `https://developer.android.com/reference/androidx/core/content/IntentCompat#EXTRA_START_PLAYBACK` with value `true`
to the intent it sends to your app. Your app should start playback when it
receives an intent with `EXTRA_START_PLAYBACK`.
| **Note:** The Assistant might cache the query results from your on-device content provider for up to seven days, and send the cached intent rather than running a new query if the user repeats a request. This means your app could receive a request to play content that is no longer available. Your app should handle this situation gracefully: Display an error message and let the user return to your landing activity (or perhaps another relevant activity).

### Handling intents while active

Users can ask the Assistant to play something while your app is still playing
content from a previous request. This means your app can receive new intents to
start playback while its playback activity is already launched and active.

The activities that support intents with deep links should override
`https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent)`
to handle new requests.

When starting playback, the Assistant might add [additional
flags](https://developer.android.com/guide/components/activities/tasks-and-back-stack#IntentFlagsForTasks)
to the intent it sends to your app. In particular, it may add
`https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_CLEAR_TOP` or
`https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK` or both. Although your code
does not need to handle these flags, the Android system responds to them.
This might affect the behavior of your app when a second playback request with a new URI arrives
while the previous URI is still playing. It's a good idea to test how your app responds in this case. You can use the `adb` command
line tool to simulate the situation (the constant `0x14000000` is the boolean bitwise OR of the two flags):

    adb shell 'am start -a android.intent.action.VIEW --ez android.intent.extra.START_PLAYBACK true -d "<first_uri>"' -f 0x14000000
    adb shell 'am start -a android.intent.action.VIEW --ez android.intent.extra.START_PLAYBACK true -d "<second_uri>"' -f 0x14000000

## Playback from a service

If your app has a
`https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat`
that permits connections from the Assistant,
the Assistant can start the app by communicating with the service's
`https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat`.
The media browser service should never launch an Activity.
The Assistant will launch your Activity based on the `PendingIntent` you define
with [setSessionActivity()](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.html#setSessionActivity(android.app.PendingIntent)).
| **Note:** Currently, the Assistant does not use services to start video apps (it starts them with an intent). However, for future compatibility, we highly recommend including a media browser service in video apps.

Be sure to set the MediaSession.Token when you
[initialize the media browser service](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#init-session).
Remember to set the supported [playback actions](https://developer.android.com/media/implement/assistant#playback_actions)
at all times, including during initialization. The Assistant expects your media
app to set the playback actions before the Assistant sends the first playback
command.

To start from a service, the Assistant implements the media browser client APIs.
It performs TransportControls calls that trigger PLAY action callbacks on your
app's media session.

The following diagram shows the order of calls generated by the Assistant and the
corresponding media session callbacks. (The prepare callbacks are sent only
if your app supports them.) All calls are asynchronous. The Assistant does not
wait for any response from your app.

![Starting playback with a media session](https://developer.android.com/static/media/images/assistant-session-play.png)

When a user issues a voice command to play, the Assistant responds with a short announcement.
As soon as the announcement is complete the Assistant issues a PLAY action. It does not wait for any specific playback state.

If your app supports the `ACTION_PREPARE_*` actions, the Assistant calls the `PREPARE` action before starting the announcement.

### Connecting to a MediaBrowserService

In order to use a service to start your app, the Assistant must be able to connect to the app's MediaBrowserService and
retrieve its MediaSession.Token. Connection requests are handled in the service's
`https://developer.android.com/reference/android/service/media/MediaBrowserService#onGetRoot(java.lang.String, int, android.os.Bundle)`
method. There are two ways to handle requests:

- Accept all connection requests
- Accept connection requests from the Assistant app only

| **Note:** The `onGetRoot()` method should quickly return a non-null value. User authentication and other slow processes should not run in `onGetRoot()`. Most business logic should be handled in the `onLoadChildren()` method.

#### Accept all connection requests

You must return a BrowserRoot in order to allow the Assistant to send commands to your media session. The easiest way is to allow all MediaBrowser apps to connect to your MediaBrowserService. You must return a non-null BrowserRoot. Here is the applicable code from the [Universal Music Player](https://github.com/android/uamp/blob/ad3334ae1db0adae144996e715c0ae3a1e5d2fea/mobile/src/main/java/com/example/android/uamp/MusicService.java#L302):

### Kotlin

```kotlin
override fun onGetRoot(
        clientPackageName: String,
        clientUid: Int,
        rootHints: Bundle?
): BrowserRoot? {

    // To ensure you are not allowing any arbitrary app to browse your app's contents, you
    // need to check the origin:
    if (!packageValidator.isCallerAllowed(this, clientPackageName, clientUid)) {
        // If the request comes from an untrusted package, return an empty browser root.
        // If you return null, then the media browser will not be able to connect and
        // no further calls will be made to other media browsing methods.
        Log.i(TAG, "OnGetRoot: Browsing NOT ALLOWED for unknown caller. Returning empty "
                + "browser root so all apps can use MediaController. $clientPackageName")
        return MediaBrowserServiceCompat.BrowserRoot(MEDIA_ID_EMPTY_ROOT, null)
    }

    // Return browser roots for browsing...
}
```

### Java

```java
@Override
public BrowserRoot onGetRoot(@NonNull String clientPackageName, int clientUid,
                             Bundle rootHints) {

    // To ensure you are not allowing any arbitrary app to browse your app's contents, you
    // need to check the origin:
    if (!packageValidator.isCallerAllowed(this, clientPackageName, clientUid)) {
        // If the request comes from an untrusted package, return an empty browser root.
        // If you return null, then the media browser will not be able to connect and
        // no further calls will be made to other media browsing methods.
        LogHelper.i(TAG, "OnGetRoot: Browsing NOT ALLOWED for unknown caller. "
                + "Returning empty browser root so all apps can use MediaController."
                + clientPackageName);
        return new MediaBrowserServiceCompat.BrowserRoot(MEDIA_ID_EMPTY_ROOT, null);
    }

    // Return browser roots for browsing...
}
```

#### Accept the Assistant app package and signature

You can explicitly allow the Assistant to connect to your media browser service by checking for its package name and signature. Your app will receive the package name in the onGetRoot method of your MediaBrowserService. You must return a BrowserRoot in order to allow the Assistant to send commands to your media session. The
[Universal Music Player](https://github.com/android/uamp/blob/bffac196050a6453f82ee6ad6297a7056603cb82/common/src/main/res/xml/allowed_media_browser_callers.xml)
sample maintains a list of known package names and signatures. Below are the package names and signatures that are used by the Google Assistant.

    <signature name="Google" package="com.google.android.googlequicksearchbox">
        <key release="false">19:75:b2:f1:71:77:bc:89:a5:df:f3:1f:9e:64:a6:ca:e2:81:a5:3d:c1:d1:d5:9b:1d:14:7f:e1:c8:2a:fa:00</key>
        <key release="true">f0:fd:6c:5b:41:0f:25:cb:25:c3:b5:33:46:c8:97:2f:ae:30:f8:ee:74:11:df:91:04:80:ad:6b:2d:60:db:83</key>
    </signature>

    <signature name="Google Assistant on Android Automotive OS" package="com.google.android.carassistant">
        <key release="false">17:E2:81:11:06:2F:97:A8:60:79:7A:83:70:5B:F8:2C:7C:C0:29:35:56:6D:46:22:BC:4E:CF:EE:1B:EB:F8:15</key>
        <key release="true">74:B6:FB:F7:10:E8:D9:0D:44:D3:40:12:58:89:B4:23:06:A6:2C:43:79:D0:E5:A6:62:20:E3:A6:8A:BF:90:E2</key>
    </signature>