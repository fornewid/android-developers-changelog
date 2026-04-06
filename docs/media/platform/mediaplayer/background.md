---
title: https://developer.android.com/media/platform/mediaplayer/background
url: https://developer.android.com/media/platform/mediaplayer/background
source: md.txt
---

# Play media in the background

You can play media in the background even when your application is not on screen, for example, while the user is interacting with other applications.

To do so, you embed the MediaPlayer in a[`MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat)service and have it interact with a[`MediaBrowserCompat`](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat)in another activity.

Be cautious with implementing this client and server setup. There are expectations about how a player running in a background service interacts with the rest of the system. If your application does not fulfill those expectations, the user may have a bad experience. See[Building an Audio App](https://developer.android.com/guide/topics/media-apps/audio-app/building-an-audio-app)for details.

This page describes special instructions for managing a MediaPlayer when it you implement it inside a service.

## Run asynchronously

Like an[`Activity`](https://developer.android.com/reference/android/app/Activity), all work in a[`Service`](https://developer.android.com/reference/android/app/Service)is done in a single thread by default. In fact, when you run an activity and a service from the same application, they use the same thread (the "main thread") by default.

Services must process incoming intents quickly and never perform lengthy computations when responding to them. You must perform any heavy work or blocking calls asynchronously: either from another thread you implement yourself, or using the framework's many facilities for asynchronous processing.

For example, when you use[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)from your main thread, you should:

- Call[`prepareAsync()`](https://developer.android.com/reference/android/media/MediaPlayer#prepareAsync())rather than[`prepare()`](https://developer.android.com/reference/android/media/MediaPlayer#prepare()), and
- Implement a[`MediaPlayer.OnPreparedListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnPreparedListener)in order to be notified when the preparation is complete and you can start playing.

For example:  

### Kotlin

    private const val ACTION_PLAY: String = "com.example.action.PLAY"

    class MyService: Service(), MediaPlayer.OnPreparedListener {

        private var mMediaPlayer: MediaPlayer? = null

        override fun onStartCommand(intent: Intent, flags: Int, startId: Int): Int {
            ...
            val action: String = intent.action
            when(action) {
                ACTION_PLAY -> {
                    mMediaPlayer = ... // initialize it here
                    mMediaPlayer?.apply {
                        setOnPreparedListener(this@MyService)
                        prepareAsync() // prepare async to not block main thread
                    }

                }
            }
            ...
        }

        /** Called when MediaPlayer is ready */
        override fun onPrepared(mediaPlayer: MediaPlayer) {
            mediaPlayer.start()
        }
    }

### Java

    public class MyService extends Service implements MediaPlayer.OnPreparedListener {
        private static final String ACTION_PLAY = "com.example.action.PLAY";
        MediaPlayer mediaPlayer = null;

        public int onStartCommand(Intent intent, int flags, int startId) {
            ...
            if (intent.getAction().equals(ACTION_PLAY)) {
                mediaPlayer = ... // initialize it here
                mediaPlayer.setOnPreparedListener(this);
                mediaPlayer.prepareAsync(); // prepare async to not block main thread
            }
        }

        /** Called when MediaPlayer is ready */
        public void onPrepared(MediaPlayer player) {
            player.start();
        }
    }

### Handle asynchronous errors

On synchronous operations, errors are signaled with an exception or an error code. When you use asynchronous resources, however, you should notify your application of errors appropriately. In the case of a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), you implement a[`MediaPlayer.OnErrorListener`](https://developer.android.com/reference/android/media/MediaPlayer.OnErrorListener)and set it in your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)instance:  

### Kotlin

    class MyService : Service(), MediaPlayer.OnErrorListener {

        private var mediaPlayer: MediaPlayer? = null

        fun initMediaPlayer() {
            // ...initialize the MediaPlayer here...
            mediaPlayer?.setOnErrorListener(this)
        }

        override fun onError(mp: MediaPlayer, what: Int, extra: Int): Boolean {
            // ... react appropriately ...
            // The MediaPlayer has moved to the Error state, must be reset!
        }
    }

### Java

    public class MyService extends Service implements MediaPlayer.OnErrorListener {
        MediaPlayer mediaPlayer;

        public void initMediaPlayer() {
            // ...initialize the MediaPlayer here...
            mediaPlayer.setOnErrorListener(this);
        }

        @Override
        public boolean onError(MediaPlayer mp, int what, int extra) {
            // ... react appropriately ...
            // The MediaPlayer has moved to the Error state, must be reset!
        }
    }

When an error occurs, the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)moves to the*Error* state. must reset it before you can use it again. For details, see the full state diagram for the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)class.

## Use wake locks

When you play or stream music in the background, you must use wake locks to prevent the system from interfering with your playback, for example, by having the device go to sleep.

A wake lock is a signal to the system that your application is using features that should stay available even when the phone is idle.
| **Note:** You should always use wake locks sparingly and hold them only for as long as truly necessary, because they significantly reduce the battery life of the device.

To ensure that the CPU continues running while your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)is playing, call the[`setWakeMode()`](https://developer.android.com/reference/android/media/MediaPlayer#setWakeMode(android.content.Context,%20int))method when you initialize your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer). The[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)holds the specified lock while playing and releases the lock when paused or stopped:  

### Kotlin

    mediaPlayer = MediaPlayer().apply {
        // ... other initialization here ...
        setWakeMode(applicationContext, PowerManager.PARTIAL_WAKE_LOCK)
    }

### Java

    mediaPlayer = new MediaPlayer();
    // ... other initialization here ...
    mediaPlayer.setWakeMode(getApplicationContext(), PowerManager.PARTIAL_WAKE_LOCK);

However, the wake lock acquired in this example ensures only that the CPU remains awake. If you are streaming media over the network and you are using Wi-Fi, you probably want to hold a[`WifiLock`](https://developer.android.com/reference/android/net/wifi/WifiManager.WifiLock)as well, which you must acquire and release manually. So, when you start preparing the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)with the remote URL, you should create and acquire the Wi-Fi lock.

For example:  

### Kotlin

    val wifiManager = getSystemService(Context.WIFI_SERVICE) as WifiManager
    val wifiLock: WifiManager.WifiLock =
        wifiManager.createWifiLock(WifiManager.WIFI_MODE_FULL, "mylock")

    wifiLock.acquire()

### Java

    WifiLock wifiLock = ((WifiManager) getSystemService(Context.WIFI_SERVICE))
        .createWifiLock(WifiManager.WIFI_MODE_FULL, "mylock");

    wifiLock.acquire();

When you pause or stop your media, or when you no longer need the network, you should release the lock:  

### Kotlin

    wifiLock.release()

### Java

    wifiLock.release();

## Perform cleanup

As mentioned earlier, a[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)object can consume a significant amount of system resources, so you should keep it only for as long as you need and call[`release()`](https://developer.android.com/reference/android/media/MediaPlayer#release())when you are done with it. It's important to call this cleanup method explicitly rather than rely on system garbage collection because it might take some time before the garbage collector reclaims the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), as it's only sensitive to memory needs and not to shortage of other media-related resources. So, in the case when you're using a service, you should always override the[`onDestroy()`](https://developer.android.com/reference/android/app/Service#onDestroy())method to make sure you are releasing the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer):  

### Kotlin

    class MyService : Service() {

        private var mediaPlayer: MediaPlayer? = null
        // ...

        override fun onDestroy() {
            super.onDestroy()
            mediaPlayer?.release()
        }
    }

### Java

    public class MyService extends Service {
       MediaPlayer mediaPlayer;
       // ...

       @Override
       public void onDestroy() {
           super.onDestroy();
           if (mediaPlayer != null) mediaPlayer.release();
       }
    }

You should always look for other opportunities to release your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)as well, apart from releasing it when being shut down. For example, if you expect not to be able to play media for an extended period of time (after losing audio focus, for example), you should definitely release your existing[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)and create it again later. On the other hand, if you only expect to stop playback for a very short time, you should probably hold on to your[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer)to avoid the overhead of creating and preparing it again.

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app.[Read more](https://developer.android.com/media/media3)about it.

These pages cover topics relating to recording, storing, and playing back audio and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)