---
title: https://developer.android.com/training/cars/media/enable-playback
url: https://developer.android.com/training/cars/media/enable-playback
source: md.txt
---

To enable media playback in Android Auto and Android Automotive OS (AAOS),
implement playback controls by registering a media session and handling its
callback methods. This page explains how to:

- Register a `MediaSessionCompat` object in your media browser service.

- Implement `MediaSessionCompat.Callback` methods to respond to user playback
  requests.

- Configure standard and custom playback actions.

- Set the initial playback state for your media session.

- Add icons to indicate audio format.

- Create links from actively playing media items.

Android Auto and AAOS send playback control commands through
[`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat) for your service. You must register a session and
implement the associated callback methods.

## Register a media session

In your media browser service's [`onCreate`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onCreate()) method, create an instance of
[`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat), then call [`setSessionToken`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#setSessionToken(android.support.v4.media.session.MediaSessionCompat.Token)) to register the
media session. This code snippet shows how to create and register a media
session:  

### Kotlin

    override fun onCreate() {
        super.onCreate()
        ...
        // Start a new MediaSession.
        val session = MediaSessionCompat(this, "session tag").apply {
            // Set a callback object that implements MediaSession.Callback
            // to handle play control requests.
            setCallback(MyMediaSessionCallback())
        }
        sessionToken = session.sessionToken
        ...
    }

### Java

    public void onCreate() {
        super.onCreate();
        ...
        // Start a new MediaSession.
        MediaSessionCompat session = new MediaSessionCompat(this, "session tag");
        setSessionToken(session.getSessionToken());

        // Set a callback object that implements MediaSession.Callback
        // to handle play control requests.
        session.setCallback(new MyMediaSessionCallback());
        ...
    }

When you create the media session object, you set a callback object that is used
to handle playback control requests. You create this callback object by
providing an implementation of the [`MediaSessionCompat.Callback`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback)
class for your app. The next section discusses how to implement this object.
| **Note:** To inspect the media session run `adb shell dumpsys media_session`

## Implement play commands

When a user requests playback for a media item from your app, Android Automotive
OS and Android Auto use the [`MediaSessionCompat.Callback`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback)
class from your app's [`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat) object that they obtained from
your app's media browser service. When a user wants to control content playback,
such as pausing playback or skipping to the next track, Android Auto and Android
Automotive OS invoke one of the callback object's methods.

To handle content playback, your app must extend the abstract
`MediaSessionCompat.Callback` class and implement the methods that your app
supports.

Implement each of these callback methods that make sense for the type of content
offered by your app:

[`onPrepare`](https://developer.android.com/reference/android/media/session/MediaSession.Callback#onPrepare())
:   AAOS invokes this method when the media source changes.

[`onPlay`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlay())

:   Invoked when the user selects play without choosing a specific item. Your
    app must play its default content or, if playback was paused with
    [`onPause`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPause()), your app resumes playback.

    | **Note:** Your app mustn't automatically start playing music when Android Automotive OS or Android Auto connect to the media browser service. To learn more, see [Set initial PlaybackState](https://developer.android.com/training/cars/media/enable-playback#initial-playback-state).

[`onPlayFromMediaId`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromMediaId(java.lang.String,android.os.Bundle))

:   Invoked when the user chooses to play a specific item. The method receives
    the [ID](https://developer.android.com/cars/media/create-media-browser/content-hierarchy#onLoadChildren) that your media browser service assigned to the media item in the
    content hierarchy.

[`onPlayFromSearch`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPlayFromSearch(java.lang.String,android.os.Bundle))

:   Invoked when the user chooses to play from a search query. The app must make
    an appropriate choice based on the search string that was passed in.

[`onPause`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onPause())

:   Invoked when the user chooses to pause playback.

[`onSkipToNext`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToNext())

:   Invoked when the user chooses to skip to the next item.

[`onSkipToPrevious`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToPrevious())

:   Invoked when the user chooses to skip to the previous item.

[`onStop`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onStop())

:   Invoked when the user chooses to stop play. Override these methods in your
    app to provide the chosen result. You needn't implement a method if its purpose
    isn't supported by your app. For example, if your app plays a livestream, such
    as a sports broadcast, you needn't implement `onSkipToNext`. Instead, use the
    default implementation of `onSkipToNext`.

Your app doesn't need any special logic to play content through the car's
speakers. When your app receives a request to play content, it plays audio
in the same way that content is played through a user's phone speakers or
headphones. Android Auto and AAOS automatically send the audio
content to the car's system to play over the car's speakers.

To learn more about playing audio content, see [Media Player overview](https://developer.android.com/guide/topics/media/mediaplayer),
[Audio app overview](https://developer.android.com/training/managing-audio), and the ExoPlayer [overview](https://developer.android.com/guide/topics/media/exoplayer).

## Set standard playback actions

Android Auto and AAOS display playback controls based on the
actions that are enabled in the [`PlaybackStateCompat`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat)
object. By default, your app must support the following actions:

- [`ACTION_PLAY`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_PLAY())
- [`ACTION_PAUSE`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_PAUSE())
- [`ACTION_STOP`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_STOP())
- [`ACTION_PLAY_FROM_MEDIA_ID`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_PLAY_FROM_MEDIA_ID())
- [`ACTION_PLAY_FROM_SEARCH`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_PLAY_FROM_SEARCH())

Your app can additionally support the following actions if they are relevant to
the app's content:

- [`ACTION_SKIP_TO_PREVIOUS`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_SKIP_TO_PREVIOUS())
- [`ACTION_SKIP_TO_NEXT`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_SKIP_TO_NEXT())

In addition, you can optionally create a play queue for display to for the user.
To do this, call the [`setQueue`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setQueue(java.util.List%3Candroid.support.v4.media.session.MediaSessionCompat.QueueItem%3E)) and [`setQueueTitle`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setQueueTitle(java.lang.CharSequence)) methods, enable
the [`ACTION_SKIP_TO_QUEUE_ITEM`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#ACTION_SKIP_TO_QUEUE_ITEM()) action, and define the callback
[`onSkipToQueueItem`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onSkipToQueueItem(long)).

Also, add support for the **Now playing** icon, which is an indicator for what
is playing. To do this, call the [`setActiveQueueItemId`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setActiveQueueItemId(long)) method and pass
the ID of the playing item in the queue. You need to update
`setActiveQueueItemId` whenever there is a queue change.
| **Note:** Adding support for a **Now playing** icon is only required when supporting a play queue.

Android Auto and AAOS display buttons for each enabled action as well as the
playback queue. When users click these buttons, the system invokes the
corresponding callback from [`MediaSessionCompat.Callback`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback).

### Reserve unused space

Android Auto and AAOS reserve space in the UI for the
`ACTION_SKIP_TO_PREVIOUS` and `ACTION_SKIP_TO_NEXT` actions. If your app does
not support one of these functions, Android Auto and AAOS use
the space to display any custom actions you create.

If you don't want to fill those spaces with custom actions, you can reserve
them so that Android Auto and AAOS leave the space blank
whenever your app doesn't support the corresponding function.

To do so, call the [`setExtras`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat#setExtras(android.os.Bundle)) method with an extras bundle that contains
constants that correspond to the reserved functions.
[`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_NEXT())
corresponds to `ACTION_SKIP_TO_NEXT`, and
[`SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#SESSION_EXTRAS_KEY_SLOT_RESERVATION_SKIP_TO_PREV())
corresponds to `ACTION_SKIP_TO_PREVIOUS`. Use these constants as keys in the
bundle, and use the boolean `true` as values.

## Set initial PlaybackState

As Android Auto and AAOS communicate with your media browser
service, your media session communicates the status of content playback using
the [`PlaybackStateCompat`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat).

Your app shouldn't automatically start playing music when AAOS or Android Auto
connects to your media browser service. Instead, rely on Android Auto and AAOS
to resume or start playback based on the car's state or user actions.

To accomplish this, set the initial `PlaybackStateCompat`
of your media session to [`STATE_STOPPED`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_STOPPED()), [`STATE_PAUSED`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_PAUSED()),
[`STATE_NONE`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_NONE()), or [`STATE_ERROR`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat#STATE_ERROR()).
| **Note:** When `PlaybackStateCompat` is set to `STATE_NONE`, Android Auto and AAOS make playback UI inaccessible. Only send this state when the app has nothing to play and the user needs to select new content to initiate playback.

Media sessions within Android Auto and AAOS only last for the
duration of the drive, so users start and stop these sessions frequently. To
promote a seamless experience between drives, keep track of the user's previous
session state, so that when the media app receives a resume request, the user
can automatically pick up where they left off. For example, the last played
media item, the `PlaybackStateCompat`, and the queue.

## Add custom playback actions

You can add custom playback actions to display additional actions that your
media app supports. If [space permits](https://developer.android.com/training/cars/media/enable-playback#reserve-space) (and you don't reserve it), Android
adds the custom actions to the transport controls. Otherwise, the custom
actions appear in the **Overflow** menu. Android displays custom actions in the
order you add them to `PlaybackStateCompat`.

Use custom actions to provide behavior distinct from [standard actions](https://developer.android.com/training/cars/media/enable-playback#required-actions).
Don't use them to replace or duplicate standard actions.

To add custom actions, use the [`addCustomAction`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#addCustomAction(android.support.v4.media.session.PlaybackStateCompat.CustomAction)) method in the
[`PlaybackStateCompat.Builder`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.Builder) class. This code snippet shows how to add
a custom action to "Start a radio channel":  

### Kotlin

    val customActionExtras = Bundle()
    customActionExtras.putInt(
      androidx.media3.session.MediaConstants.EXTRAS_KEY_COMMAND_BUTTON_ICON_COMPAT,
      androidx.media3.session.CommandButton.ICON_RADIO)

    stateBuilder.addCustomAction(
        PlaybackStateCompat.CustomAction.Builder(
            CUSTOM_ACTION_START_RADIO_FROM_MEDIA,
            resources.getString(R.string.start_radio_from_media),
            startRadioFromMediaIcon // or R.drawable.media3_icon_radio
        ).run {
            setExtras(customActionExtras)
            build()
        }
    )

### Java

    Bundle customActionExtras = new Bundle();
    customActionExtras.putInt(
      androidx.media3.session.MediaConstants.EXTRAS_KEY_COMMAND_BUTTON_ICON_COMPAT,
      androidx.media3.session.CommandButton.ICON_RADIO);

    stateBuilder.addCustomAction(
        new PlaybackStateCompat.CustomAction.Builder(
            CUSTOM_ACTION_START_RADIO_FROM_MEDIA,
            resources.getString(R.string.start_radio_from_media),
            startRadioFromMediaIcon) // or R.drawable.media3_icon_radio
        .setExtras(customActionExtras)
        .build());

For a more detailed example of this method, see the [`setCustomAction`](https://github.com/googlesamples/android-UniversalMusicPlayer/blob/f3154af7ac972ee9b7b1fd32ca3c935e02268a18/mobile/src/main/java/com/example/android/uamp/playback/PlaybackManager.java#L150-L171)
method in the Universal Android Music Player sample app on GitHub. After you
create your custom action, your media session can respond to the actions
by overriding the [`onCustomAction`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat.Callback#onCustomAction(java.lang.String,%20android.os.Bundle)) method.

This code snippet shows how your app could respond to a "Start a radio channel"
action:  

### Kotlin

    override fun onCustomAction(action: String, extras: Bundle?) {
        when(action) {
            CUSTOM_ACTION_START_RADIO_FROM_MEDIA -> {
                ...
            }
        }
    }

### Java

    @Override
    public void onCustomAction(@NonNull String action, Bundle extras) {
        if (CUSTOM_ACTION_START_RADIO_FROM_MEDIA.equals(action)) {
            ...
        }
    }

To learn more, see the [`onCustomAction`](https://github.com/googlesamples/android-UniversalMusicPlayer/blob/f3154af7ac972ee9b7b1fd32ca3c935e02268a18/mobile/src/main/java/com/example/android/uamp/playback/PlaybackManager.java#L328-L346) method in the Universal Android
Music Player sample app on GitHub.

### Create icons for custom actions

Each custom action that you create requires an icon.

If the description of that icon matches one of the [`CommandButton.ICON_`](https://developer.android.com/reference/kotlin/androidx/media3/session/CommandButton#ICON_ALBUM())
constants, set the integer value for the
[`EXTRAS_KEY_COMMAND_BUTTON_ICON_COMPAT`](https://developer.android.com/reference/androidx/media3/session/MediaConstants#EXTRAS_KEY_COMMAND_BUTTON_ICON_COMPAT()) key of the custom action's
extras. On supported systems, doing so overrides the icon resource passed to
[`CustomAction.Builder`](https://developer.android.com/reference/android/support/v4/media/session/PlaybackStateCompat.CustomAction.Builder#Builder(java.lang.String,java.lang.CharSequence,int)), allowing system components to consistently render
your action and other playback actions.

You must also specify an icon resource. Apps in cars can run on many different
screen sizes and densities, so icons that you provide must be
[vector drawables](https://developer.android.com/guide/topics/graphics/vector-drawable-resources). Use a vector drawable to scale assets without
losing detail. A vector drawable can align edges and corners to pixel boundaries
at smaller resolutions.

If a custom action is *stateful* (if it toggles a playback setting on or off),
provide different icons for the different states to help users see a change when
they select the action.

### Provide alternative icon styles for disabled actions

When a custom action is unavailable for the current context, swap the custom
action icon with an alternative icon that shows the action as disabled.
![Samples of off-style custom action icons.](https://developer.android.com/static/images/training/icon_off.png) Figure 1. Samples of off-style custom action icons.

## Indicate audio format

To indicate that the playing media uses a special audio format,
you can specify icons that are rendered in cars that support this feature. You
can set the [`KEY_CONTENT_FORMAT_TINTABLE_LARGE_ICON_URI`](https://developer.android.com/reference/androidx/car/app/mediaextensions/MetadataExtras#KEY_CONTENT_FORMAT_TINTABLE_LARGE_ICON_URI()) and the
[`KEY_CONTENT_FORMAT_TINTABLE_SMALL_ICON_URI`](https://developer.android.com/reference/androidx/car/app/mediaextensions/MetadataExtras#KEY_CONTENT_FORMAT_TINTABLE_SMALL_ICON_URI()) in the extras bundle of the
currently playing media item (passed to [`MediaSession.setMetadata`](https://developer.android.com/reference/android/media/session/MediaSession#setMetadata(android.media.MediaMetadata))).
Set both extras to accommodate the different layouts.

In addition, you can set the [`KEY_IMMERSIVE_AUDIO`](https://developer.android.com/reference/androidx/car/app/mediaextensions/MetadataExtras#KEY_IMMERSIVE_AUDIO()) extra
to tell car OEMs that this is immersive audio, and they should be very careful
when deciding whether to apply audio effects that might interfere with the
immersive content.

## Add links from currently-playing item

You can configure the playing media item so its subtitle, description,
or both are links to other media items. That lets the user jump quickly to
related items; for example, they might jump to other songs by the same artist or
to other episodes of a podcast. If the car supports this feature, users
can tap the link to browse to that content.

To add links, configure the [`KEY_SUBTITLE_LINK_MEDIA_ID`](https://developer.android.com/reference/androidx/car/app/mediaextensions/MetadataExtras#KEY_SUBTITLE_LINK_MEDIA_ID()) metadata
(to link from the subtitle) or [`KEY_DESCRIPTION_LINK_MEDIA_ID`](https://developer.android.com/reference/androidx/car/app/mediaextensions/MetadataExtras#KEY_DESCRIPTION_LINK_MEDIA_ID()) (to link
from the description). For details, see the reference documentation for those
metadata fields.