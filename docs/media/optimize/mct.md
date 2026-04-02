---
title: https://developer.android.com/media/optimize/mct
url: https://developer.android.com/media/optimize/mct
source: md.txt
---

# Using the media controller test app

Media apps that interact by voice with the Google Assistant on Android phones, cars, TVs, and headphones are powered by Android media session APIs and use media actions. The media action lifecycle can be hard to follow. Even a simple play from search request has many intermediate steps where something could go wrong, as shown in the simplified timeline:

![The Media Action Lifecycle](https://developer.android.com/static/media/images/MCT/Media-Action-Lifecycle.png)
**Figure 1.**The Media Action Lifecycle

<br />

The Media Controller Test (MCT) app lets you test the intricacies of media playback on Android and helps verify your media session implementation.

The Media Controller Test app is available in two versions:

- The client app is implemented on top of the legacy`MediaControllerCompat`. This allows testing your media session app built on top of a legacy`MediaSessionCompat`or the Media3`MediaSession`when accessed by an external app through a legacy`MediaControllerCompat`. Find the[source code of the legacy version](https://github.com/googlesamples/android-media-controller)on GitHub.
- The client app is implemented on top of the most recent Media3`MediaController`. This allows testing your media session app built on top of a legacy`MediaSessionCompat`or the Media3`MediaSession`when accessed by an external app through a Media3`MediaController`. Find the[source code of the Media3 version](https://github.com/androidx/media/tree/release/testapps/controller)on GitHub.

The MCT surfaces information about your app's`MediaController`, such as its`PlaybackState`and metadata, and can be used to test inter-app media controls. The MCT also includes a[verification testing framework](https://developer.android.com/media/optimize/mct#verification-tests)that lets you automate your QA testing.

In order to use the MCT, your app must have a media browser service and you must allow the MCT to connect to it. See[Building a media browser service](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice)for more information.

## Starting the MCT

![The MCT Launch Page](https://developer.android.com/static/media/images/MCT/MCT-Launch-Screen.png)**Figure 2.**The MCT Launch Page

When you launch MCT, you'll see two lists:

- **Active MediaSessions** - This list is initially empty when you launch the MCT and you'll see the message "No media apps found. Notification Listener permission is required to scan for active media sessions." Click**Settings**to go to the permissions screen and enable the permission for the MCT.
- **MediaBrowserService Implementations** - This list shows apps that have implemented a media browser service. If you've implemented a media browser service, your app will appear in this list, but you can only use the MCT if you've configured your app to accept all connections or allowlisted the MCT. See[Controlling client connections with onGetRoot()](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowserservice#controlling_client_connections_with_ongetroot)for more information.

## Manually testing a phone app

If you allowed the MCT to connect to your app's media browser service, your app appears in the list of media browser service list implementations. Find it there and click**Control**to start your app in the background.

Otherwise, you must first start your app yourself in the background, then click**Control**when it appears in the list of active media sessions.

### Testing prepare and play

When the MCT starts to control your app, it displays the app's current session metadata: the currently selected media and the actions that the session is prepared to handle.  
![The Control Page](https://developer.android.com/static/media/images/MCT/audio-focus.png)**Figure 3.**The Control Page

The top of the MCT controls page contains a drop-down menu where you can select**Search** ,**URI** ,**Media ID** , or**None**, along with a text field to specify the input data associated with the Search, URI, or Media ID if you select one of those options.

The**Prepare** and**Play** buttons just below the text field perform the appropriate calls (`onPrepare()`,`onPrepareFromSearch()`,`onPrepareFromUri()`,`onPrepareFromMediaId()`,`onPlay()`,`onPlayFromSearch()`,`onPlayFromUri()`,`onPlayFromMediaId()`) depending on what action you selected.

### Testing audio focus

A well-behaved media app should be able to handle[audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus). You can test audio focus by running another audio app alongside your app. The MCT controls page includes a button that requests and releases audio focus.

To test audio focus, follow these steps:

1. Use the**Audio Focus** drop-down menu to select one of the three duration hints`AUDIOFOCUS_GAIN`,`AUDIOFOCUS_GAIN_TRANSIENT`, or`AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`.
2. Press the button to request focus.
3. Press the button again to release focus.

### Testing transport controls

![Testing Transport Controls](https://developer.android.com/static/media/images/MCT/MCT-Controller-Screen.png)**Figure 4.**Testing Transport Controls

Swipe left to display the MCT's UI view. This view has the standard media controller transport buttons and shows the session's program image and data. Transport buttons that are disabled are circled in orange. All the others are active.

Test your player using the transport buttons. The state of the transport buttons should change as expected. For example, when you press the PLAY button it should become disabled, and the PAUSE and STOP buttons become enabled.

Swipe left again for a view that displays optional actions. Each action has a control that shows whether or not it's active. If it is active, you can perform the action by clicking on it.

If you connected from the list of apps that have a media browser service, you can swipe left two more times for views that let you walk up and down your app's content hierarchy, or search the content tree.  

## Manually testing a video app

Use split-screen mode to test video app controllers. First, open your video app in one window and then open the MCT in split-screen mode.

## Running verification tests

The verification testing framework offers one-click tests that you can run to ensure that your media app responds correctly to a playback request.

### Testing a phone app

![The Test Button](https://developer.android.com/static/media/images/MCT/MCT-Test-Button.png)**Figure 5.**The Test Button

To access the verification tests, click the**Test**button next to your media app.  

#### MCT state

![The Media Control State](https://developer.android.com/static/media/images/MCT/MCT-Testing-Info-Screen.png)**Figure 6.**The Media Control State

The next view shows you detailed information about the MCT's`MediaController`, for example the`PlaybackState`, metadata, and queue. There are two buttons on the top right of the toolbar. The button on the left toggles between parsable and formatted logs. The button on the right refreshes the view to display the most current information.  

#### Selecting a test

![The Test Selection Page](https://developer.android.com/static/media/images/MCT/MCT-Testing-Verification-Screen.png)**Figure 7.**The Test Selection Page

By swiping to the left, you arrive at the verification tests view, where you can see a scrollable list of available tests. If a test uses a query, like the play from search test shown in Figure 7, there is a text field to enter the query string.

The MCT includes tests for the following media actions, and more tests are continually added to the project:

- Play
- Play From Search
- Play From Media ID
- Play From URI
- Pause
- Stop
- Skip To Next
- Skip To Previous
- Skip To Queue Item
- Seek To

#### Test results

![A Successful Test Result](https://developer.android.com/static/media/images/MCT/MCT-Testing-Success-Screen.png)**Figure 8.**A Successful Test Result

The results area at the bottom of the view is initially empty. It will show the results when you run a test. For example, to run the play from search test, enter a search query into the text field and click**Run Test**. The following screenshot shows a successful test result.  

### Testing an Android TV app

When you launch the MCT on Android TV, you see a list of installed media apps. Note that an app will only appear in this list if it implements a media browser service.

![The MCT Launch Page on TV](https://developer.android.com/static/media/images/MCT/MCT-TV-Launch-Screen.png)
**Figure 9.**The MCT Launch Page on TV

<br />

Selecting an app takes you to the testing screen, which displays a list of verification tests on the right.

![The Verification Tests Page on TV](https://developer.android.com/static/media/images/MCT/MCT-TV-Testing-Screen.png)
**Figure 10.**The Verification Tests Page on TV

<br />

When you run a test, the left side of the screen displays information about the selected MediaController. For more details, check the MCT logs in Logcat.

![The Test Information Page on TV](https://developer.android.com/static/media/images/MCT/MCT-TV-Testing-Pause.png)
**Figure 11.**The Test Information Page on TV

<br />

Tests that require a query are marked with a keyboard icon. Clicking on one of these tests opens an input field for the query. Click**Enter**to run the test.

To make text input easier, you can also use an`adb`command:  

```
adb shell input text your-query
```

You can use "%s" to add a space between words. For example, the following command adds the text "hello world" to the input field.  

```
adb shell input text hello%sworld
```

### Building a test

You can submit a pull request with more tests you think are useful. To learn how to build new tests, visit the[MCT GitHub Wiki](https://github.com/googlesamples/android-media-controller/wiki/Verification-Tests)and see the[verification test instructions](https://github.com/googlesamples/android-media-controller/wiki/Verification-Tests).

Please review the[contribution instructions](https://github.com/googlesamples/android-media-controller/blob/master/CONTRIBUTING.md).

## Additional resources

The MCT is meant to be used in conjunction with apps that implement media APIs. See the[Universal Android Music Player](https://github.com/googlesamples/android-UniversalMusicPlayer)for an example of such an app.

Bug fixes and improvements are always welcome. Please see the[contribution instructions](https://github.com/googlesamples/android-media-controller/blob/master/CONTRIBUTING.md).