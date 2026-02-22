---
title: https://developer.android.com/training/tv/tif/tvinput
url: https://developer.android.com/training/tv/tif/tvinput
source: md.txt
---

A TV input service represents a media stream source, and lets you present your media content in a
linear, broadcast TV fashion as channels and programs. With a TV input service, you can provide
parental controls, program guide information, and content ratings. The TV input service works
with the Android system TV app. This app ultimately controls and presents channel content
on the TV. The system TV app is developed specifically for the device and immutable
by third-party apps. For more information about the TV Input Framework (TIF)
architecture and its components, see
[TV Input Framework](https://source.android.com/devices/tv/index.html).

## Create a TV input service using the TIF Companion Library


The TIF Companion Library is a framework that provides extensible
implementations of common TV input service features. It is meant to be used by OEMs to build
channels for Android 5.0 (API level 21) through Android 7.1 (API level 25) only.

### Update your project


The TIF Companion Library is available for legacy use by OEMs in the
[androidtv-sample-inputs](https://github.com/googlesamples/androidtv-sample-inputs)
repository. See that repository for an example of how to include the library in an app.

### Declare your TV input service in the manifest

Your app must provide a [TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)-compatible
service that the system uses to access your app. The TIF
Companion Library provides the `BaseTvInputService` class, which
provides a default implementation of [TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)
that you can customize. Create a subclass of `BaseTvInputService`,
and declare the subclass in your manifest as a service.

Within the manifest declaration, specify the
[BIND_TV_INPUT](https://developer.android.com/reference/android/Manifest.permission#BIND_TV_INPUT) permission to allow the
service to connect the TV input to the system. A system service
performs the binding and has the
[BIND_TV_INPUT](https://developer.android.com/reference/android/Manifest.permission#BIND_TV_INPUT) permission.
The system TV app sends requests to TV input services
via the [TvInputManager](https://developer.android.com/reference/android/media/tv/TvInputManager) interface.

In your service declaration, include an intent filter that specifies
[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService) as the action to perform with the
intent. Also declare the service metadata as a separate XML resource. The
service declaration, intent filter, and service metadata declaration are shown
in the following example:  

```xml
<service android:name=".rich.RichTvInputService"
    android:label="@string/rich_input_label"
    android:permission="android.permission.BIND_TV_INPUT">
    <!-- Required filter used by the system to launch our account service. -->
    <intent-filter>
        <action android:name="android.media.tv.TvInputService" />
    </intent-filter>
    <!-- An XML file which describes this input. This provides pointers to
    the RichTvInputSetupActivity to the system/TV app. -->
    <meta-data
        android:name="android.media.tv.input"
        android:resource="@xml/richtvinputservice" />
</service>
```

Define the service metadata in a separate XML file. The service
metadata XML file must include a setup interface that describes the TV input's
initial configuration and channel scan. The metadata file should also contain a
flag stating whether or not users are able to record content. For more
information on how to support recording content in your app, see
[Support content recording](https://developer.android.com/training/tv/tif/content-recording).

The service metadata file is located in the XML resources directory
for your app and must match the name of the resource you declared in the
manifest. Using the manifest entries from the previous example, you would
create the XML file at `res/xml/richtvinputservice.xml`, with the
following contents:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<tv-input xmlns:android="http://schemas.android.com/apk/res/android"
  android:canRecord="true"
  android:setupActivity="com.example.android.sampletvinput.rich.RichTvInputSetupActivity" />
```

### Define channels and create your setup activity

Your TV input service must define at least one channel that users
access via the system TV app. You should register your channels
in the system database, and provide a setup activity that the system
invokes when it cannot find a channel for your app.

First, enable your app to read from and write to the system Electronic
Programming Guide (EPG), whose data includes channels and programs available
to the user. To enable your app to perform these actions, and sync with the
EPG after device restart, add the following elements to your app manifest:  

```xml
<uses-permission android:name="com.android.providers.tv.permission.WRITE_EPG_DATA" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED "/>
```

Add the following element to ensure that your app shows up in the
Google Play Store as an app that provides content channels in Android TV:  

```xml
<uses-feature
    android:name="android.software.live_tv"
    android:required="true" />
```

Next, create a class which extends the `EpgSyncJobService`
class. This abstract class makes it easy to create a job service that
creates and updates channels in the system database.

In your subclass, create and return your full list of channels in
`getChannels()`. If your channels come from an XMLTV file,
use the `XmlTvParser` class. Otherwise, generate
channels programmatically using the `Channel.Builder` class.

For each channel, the system calls `getProgramsForChannel()`
when it needs a list of programs that can be viewed within a given time window
on the channel. Return a list of `Program` objects for the
channel. Use the `XmlTvParser` class to obtain programs from an
XMLTV file, or generate them programmatically using the
`Program.Builder` class.

For each `Program` object, use an
`InternalProviderData` object to set program information such as the
program's video type. If you only have a limited number of programs that you
want the channel to repeat in a loop, use the
`InternalProviderData.setRepeatable()` method with a value of
`true` when setting information about your program.

After you've implemented the job service, add it to your app manifest:  

```xml
<service
    android:name=".sync.SampleJobService"
    android:permission="android.permission.BIND_JOB_SERVICE"
    android:exported="true" />
```

Finally, create a setup activity. Your setup activity should provide a way
to sync channel and program data. One way to do this is for the user to do it
via the UI in the activity. You might also have the app do it automatically
when the activity starts. When the setup activity needs to sync channel and
program info, the app should start the job service:  

### Kotlin

```kotlin
val inputId = getActivity().intent.getStringExtra(TvInputInfo.EXTRA_INPUT_ID)
EpgSyncJobService.cancelAllSyncRequests(getActivity())
EpgSyncJobService.requestImmediateSync(
        getActivity(),
        inputId,
        ComponentName(getActivity(), SampleJobService::class.java)
)
```

### Java

```java
String inputId = getActivity().getIntent().getStringExtra(TvInputInfo.EXTRA_INPUT_ID);
EpgSyncJobService.cancelAllSyncRequests(getActivity());
EpgSyncJobService.requestImmediateSync(getActivity(), inputId,
        new ComponentName(getActivity(), SampleJobService.class));
```

Use the `requestImmediateSync()` method to sync
the job service. The user must wait for the sync to finish, so you should
keep your request period relatively short.

Use the `setUpPeriodicSync()` method to have the job service
periodically sync channel and program data in the background:  

### Kotlin

```kotlin
EpgSyncJobService.setUpPeriodicSync(
        context,
        inputId,
        ComponentName(context, SampleJobService::class.java)
)
```

### Java

```java
EpgSyncJobService.setUpPeriodicSync(context, inputId,
        new ComponentName(context, SampleJobService.class));
```

The TIF Companion Library provides an additional overloaded method of
`requestImmediateSync()` that lets you specify the duration of
channel data to sync in milliseconds. The default method syncs one hour's
worth of channel data.

The TIF Companion Library also provides an additional overloaded method of
`setUpPeriodicSync()` that lets you specify the duration of
channel data to sync, and how often the periodic sync should occur. The
default method syncs 48 hours of channel data every 12 hours.

For more details about channel data and the EPG, see
[Work with channel data](https://developer.android.com/training/tv/tif/channel).

### Handle tuning requests and media playback

When a user selects a specific channel, the system TV app uses a
`Session`, created by your app, to tune to the requested channel
and play content. The TIF Companion Library provides several
classes you can extend to handle channel and session calls from the system.

Your `BaseTvInputService` subclass creates sessions which handle
tuning requests. Override the
`onCreateSession()` method, create a session extended from
the `BaseTvInputService.Session` class, and call
`super.sessionCreated()` with your new session. In the following
example, `onCreateSession()` returns a
`RichTvInputSessionImpl` object that extends
`BaseTvInputService.Session`:  

### Kotlin

```kotlin
override fun onCreateSession(inputId: String): Session =
        RichTvInputSessionImpl(this, inputId).apply {
            setOverlayViewEnabled(true)
        }
```

### Java

```java
@Override
public final Session onCreateSession(String inputId) {
    RichTvInputSessionImpl session = new RichTvInputSessionImpl(this, inputId);
    session.setOverlayViewEnabled(true);
    return session;
}
```

When the user uses the system TV app to start viewing one of your channels,
the system calls your session's `onPlayChannel()` method. Override
this method if you need to do any special channel initialization before the
program starts playing.

The system then obtains the currently scheduled program and calls your
session's `onPlayProgram()` method, specifying the program
information and start time in milliseconds. Use the
`TvPlayer` interface to start playing the program.

Your media player code should implement `TvPlayer` to handle
specific playback events. The `TvPlayer` class handles features
like time-shifting controls without adding complexity to your
`BaseTvInputService` implementation.

In your session's `getTvPlayer()` method, return
your media player that implements `TvPlayer`. The
[TV Input Service](https://github.com/googlesamples/androidtv-sample-inputs) sample app implements a media player that uses
[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer).

## Create a TV input service using the TV input framework

If your TV input service can't use the TIF Companion Library, you need
to implement the following components:

- [TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService) provides long-running and background availability for the TV input
- [TvInputService.Session](https://developer.android.com/reference/android/media/tv/TvInputService.Session) maintains the TV input state and communicates with the hosting app
- [TvContract](https://developer.android.com/reference/android/media/tv/TvContract) describes the channels and programs available to the TV input
- [TvContract.Channels](https://developer.android.com/reference/android/media/tv/TvContract.Channels) represents information about a TV channel
- [TvContract.Programs](https://developer.android.com/reference/android/media/tv/TvContract.Programs) describes a TV program with data such as program title and start time
- [TvTrackInfo](https://developer.android.com/reference/android/media/tv/TvTrackInfo) represents an audio, video, or subtitle track
- [TvContentRating](https://developer.android.com/reference/android/media/tv/TvContentRating) describes a content rating, allows for custom content rating schemes
- [TvInputManager](https://developer.android.com/reference/android/media/tv/TvInputManager) provides an API to the system TV app and manages the interaction with TV inputs and apps

You also need to do the following:

1. Declare your TV input service in the manifest, as described in [Declare your TV input service in the
   manifest](https://developer.android.com/training/tv/tif/tvinput#manifest).
2. Create the service metadata file.
3. Create and register your channel and program information.
4. Create your setup activity.

### Define your TV input service

For your service, you extend the [TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService) class. A
[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService) implementation is a
[bound service](https://developer.android.com/guide/components/bound-services) where the system service
is the client that binds to it. The service life cycle methods
you need to implement are illustrated in figure 1.

The [onCreate()](https://developer.android.com/reference/android/app/Service#onCreate()) method initializes and starts the
[HandlerThread](https://developer.android.com/reference/android/os/HandlerThread) which provides a process thread separate from the UI thread to
handle system-driven actions. In the following example, the [onCreate()](https://developer.android.com/reference/android/app/Service#onCreate())
method initializes the [CaptioningManager](https://developer.android.com/reference/android/view/accessibility/CaptioningManager) and prepares to handle
the [ACTION_BLOCKED_RATINGS_CHANGED](https://developer.android.com/reference/android/media/tv/TvInputManager#ACTION_BLOCKED_RATINGS_CHANGED)
and [ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED](https://developer.android.com/reference/android/media/tv/TvInputManager#ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED) actions. These
actions describe system intents fired when the user changes the parental control settings, and when
there is a change on the list of blocked ratings.  

### Kotlin

```kotlin
override fun onCreate() {
    super.onCreate()
    handlerThread = HandlerThread(javaClass.simpleName).apply {
        start()
    }
    dbHandler = Handler(handlerThread.looper)
    handler = Handler()
    captioningManager = getSystemService(Context.CAPTIONING_SERVICE) as CaptioningManager

    setTheme(android.R.style.Theme_Holo_Light_NoActionBar)

    sessions = mutableListOf<BaseTvInputSessionImpl>()
    val intentFilter = IntentFilter().apply {
        addAction(TvInputManager.ACTION_BLOCKED_RATINGS_CHANGED)
        addAction(TvInputManager.ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED)
    }
    registerReceiver(broadcastReceiver, intentFilter)
}
```

### Java

```java
@Override
public void onCreate() {
    super.onCreate();
    handlerThread = new HandlerThread(getClass()
      .getSimpleName());
    handlerThread.start();
    dbHandler = new Handler(handlerThread.getLooper());
    handler = new Handler();
    captioningManager = (CaptioningManager)
      getSystemService(Context.CAPTIONING_SERVICE);

    setTheme(android.R.style.Theme_Holo_Light_NoActionBar);

    sessions = new ArrayList<BaseTvInputSessionImpl>();
    IntentFilter intentFilter = new IntentFilter();
    intentFilter.addAction(TvInputManager
      .ACTION_BLOCKED_RATINGS_CHANGED);
    intentFilter.addAction(TvInputManager
      .ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED);
    registerReceiver(broadcastReceiver, intentFilter);
}
```  
![](https://developer.android.com/static/images/tv/tvinput-life.png)

**Figure 1.**TvInputService lifecycle.

See [Control content](https://developer.android.com/training/tv/tif/ui#control) for more information about working with blocked content and providing
parental control. See [TvInputManager](https://developer.android.com/reference/android/media/tv/TvInputManager) for more system-driven actions that
you may want to handle in your TV input service.

The [TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService) creates a
[TvInputService.Session](https://developer.android.com/reference/android/media/tv/TvInputService.Session) that implements [Handler.Callback](https://developer.android.com/reference/android/os/Handler.Callback)
to handle player state changes. With
[onSetSurface()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onSetSurface(android.view.Surface)),
the [TvInputService.Session](https://developer.android.com/reference/android/media/tv/TvInputService.Session) sets the [Surface](https://developer.android.com/reference/android/view/Surface) with the
video content. See [Integrate player with surface](https://developer.android.com/training/tv/tif/ui#surface)
for more information about working with [Surface](https://developer.android.com/reference/android/view/Surface) to render video.

The [TvInputService.Session](https://developer.android.com/reference/android/media/tv/TvInputService.Session) handles the
[onTune()](https://developer.android.com/reference/android/media/tv/TvInputService.Session#onTune(android.net.Uri))
event when the user selects a channel, and notifies the system TV app for changes in the content and
content metadata. These `notify()` methods are described in
[Control Content](https://developer.android.com/training/tv/tif/ui#control) and [Handle track selection](https://developer.android.com/training/tv/tif/ui#track)
further in this training.

### Define your setup activity

The system TV app works with the setup activity you define for your TV input. The
setup activity is required and must provide at least one channel record for the system database. The
system TV app invokes the setup activity when it cannot find a channel for the TV input.

The setup activity describes to the system TV app the channels made available through the TV
input, as demonstrated in the next lesson, [Create
and update channel data](https://developer.android.com/training/tv/tif/channel).

## Additional references

- [android.media.tv](https://developer.android.com/reference/android/media/tv/package-summary)
- [TV
  Input Framework](https://source.android.com/devices/tv/index.html)