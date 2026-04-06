---
title: Media session callbacks  |  Legacy media APIs  |  Android Developers
url: https://developer.android.com/media/legacy/audio/mediasession
source: html-scrape
---

These guides discuss the MediaCompat APIs, which are no longer updated. We strongly recommend using the [Jetpack Media3](/guide/topics/media/media3) library instead.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media session callbacks Stay organized with collections Save and categorize content based on your preferences.



Your media session callbacks call methods in several APIs to control the player, manage the audio focus,
and communicate with the media session and media browser service. Note that the
`MediaSession` logic that responds to callbacks must be consistent. The behavior
of the callback must not depend on the identity of the caller, which could be
an activity in the same app running the `MediaSession` or any other app with a
`MediaController` connected to the `MediaSession`.

The following table summarizes how these tasks are distributed across callbacks.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **onPlay()** | **onPause()** | **onStop()** |
| [Audio Focus](/guide/topics/media-apps/audio-focus) | `requestFocus()` passing in your `OnAudioFocusChangeListener`. *Always call `requestFocus()` first, proceed only if focus is granted.* |  | `abandonAudioFocus()` |
| [Service](/guide/topics/media-apps/audio-app/building-a-mediabrowserservice) | `startService()` |  | `stopSelf()` |
| [Media Session](/guide/topics/media-apps/working-with-a-media-session) | `setActive(true)`   - Update metadata and state | - Update metadata and state | `setActive(false)`   - Update metadata and state |
| Player Implementation | Start the player | Pause the player | Stop the player |
| [Becoming Noisy](/guide/topics/media-apps/volume-and-earphones#becoming-noisy) | Register your `BroadcastReceiver` | Unregister your `BroadcastReceiver` |  |
| [Notifications](/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#mediastyle-notifications) | `startForeground(notification)` | `stopForeground(false)` | `stopForeground(false)` |

Here is a sample framework for the callback:

### Kotlin

```
private val intentFilter = IntentFilter(ACTION_AUDIO_BECOMING_NOISY)

// Defined elsewhere...
private lateinit var afChangeListener: AudioManager.OnAudioFocusChangeListener
private val myNoisyAudioStreamReceiver = BecomingNoisyReceiver()
private lateinit var myPlayerNotification: MediaStyleNotification
private lateinit var mediaSession: MediaSessionCompat
private lateinit var service: MediaBrowserService
private lateinit var player: SomeKindOfPlayer

private lateinit var audioFocusRequest: AudioFocusRequest

private val callback = object: MediaSessionCompat.Callback() {
    override fun onPlay() {
        val am = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
        // Request audio focus for playback, this registers the afChangeListener

        audioFocusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN).run {
            setOnAudioFocusChangeListener(afChangeListener)
            setAudioAttributes(AudioAttributes.Builder().run {
                setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                build()
            })
            build()
        }
        val result = am.requestAudioFocus(audioFocusRequest)
        if (result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
            // Start the service
            startService(Intent(context, MediaBrowserService::class.java))
            // Set the session active  (and update metadata and state)
            mediaSession.isActive = true
            // start the player (custom call)
            player.start()
            // Register BECOME_NOISY BroadcastReceiver
            registerReceiver(myNoisyAudioStreamReceiver, intentFilter)
            // Put the service in the foreground, post notification
            service.startForeground(id, myPlayerNotification)
        }
    }

    public override fun onStop() {
        val am = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
        // Abandon audio focus
        am.abandonAudioFocusRequest(audioFocusRequest)
        unregisterReceiver(myNoisyAudioStreamReceiver)
        // Stop the service
        service.stopSelf()
        // Set the session inactive  (and update metadata and state)
        mediaSession.isActive = false
        // stop the player (custom call)
        player.stop()
        // Take the service out of the foreground
        service.stopForeground(false)
    }

    public override fun onPause() {
        val am = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
        // Update metadata and state
        // pause the player (custom call)
        player.pause()
        // unregister BECOME_NOISY BroadcastReceiver
        unregisterReceiver(myNoisyAudioStreamReceiver)
        // Take the service out of the foreground, retain the notification
        service.stopForeground(false)
    }
}
```

### Java

```
private IntentFilter intentFilter = new IntentFilter(AudioManager.ACTION_AUDIO_BECOMING_NOISY);

// Defined elsewhere...
private AudioManager.OnAudioFocusChangeListener afChangeListener;
private BecomingNoisyReceiver myNoisyAudioStreamReceiver = new BecomingNoisyReceiver();
private MediaStyleNotification myPlayerNotification;
private MediaSessionCompat mediaSession;
private MediaBrowserService service;
private SomeKindOfPlayer player;

private AudioFocusRequest audioFocusRequest;

MediaSessionCompat.Callback callback = new
    MediaSessionCompat.Callback() {
        @Override
        public void onPlay() {
            AudioManager am = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
            // Request audio focus for playback, this registers the afChangeListener
            AudioAttributes attrs = new AudioAttributes.Builder()
                    .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                    .build();
            audioFocusRequest = new AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
                    .setOnAudioFocusChangeListener(afChangeListener)
                    .setAudioAttributes(attrs)
                    .build();
            int result = am.requestAudioFocus(audioFocusRequest);

            if (result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
                // Start the service
                startService(new Intent(context, MediaBrowserService.class));
                // Set the session active  (and update metadata and state)
                mediaSession.setActive(true);
                // start the player (custom call)
                player.start();
                // Register BECOME_NOISY BroadcastReceiver
                registerReceiver(myNoisyAudioStreamReceiver, intentFilter);
                // Put the service in the foreground, post notification
                service.startForeground(id, myPlayerNotification);
            }
        }

        @Override
        public void onStop() {
            AudioManager am = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
            // Abandon audio focus
            am.abandonAudioFocusRequest(audioFocusRequest);
            unregisterReceiver(myNoisyAudioStreamReceiver);
            // Stop the service
            service.stopSelf();
            // Set the session inactive  (and update metadata and state)
            mediaSession.setActive(false);
            // stop the player (custom call)
            player.stop();
            // Take the service out of the foreground
            service.stopForeground(false);
        }

        @Override
        public void onPause() {
            AudioManager am = (AudioManager) context.getSystemService(Context.AUDIO_SERVICE);
            // Update metadata and state
            // pause the player (custom call)
            player.pause();
            // unregister BECOME_NOISY BroadcastReceiver
            unregisterReceiver(myNoisyAudioStreamReceiver);
            // Take the service out of the foreground, retain the notification
            service.stopForeground(false);
        }
    };
```

**Note:** People using the Google Assistant can control your app with voice commands
if you create your MediaSession with the necessary callbacks. The
requirements are explained in the
[Google Assistant documentation](/guide/topics/media-apps/interacting-with-assistant).