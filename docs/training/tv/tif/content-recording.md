---
title: https://developer.android.com/training/tv/tif/content-recording
url: https://developer.android.com/training/tv/tif/content-recording
source: md.txt
---

# Support content recording

TV input services let the user pause and resume channel playback using[time-shifting APIs](https://developer.android.com/training/tv/tif/time-shifting). Android 7.0 expands on time-shifting by letting the user save multiple recorded sessions.

Users can schedule recordings in advance or start a recording as they watch a program. Once the system saves a recording, the user can browse, manage, and play back the recording using the system TV app.

If you want to provide recording functionality for your TV input service, you must indicate to the system that your app supports recording, implement the ability to record programs, handle and communicate any errors that occur during recording, and manage your recorded sessions.

## Indicate support for recording

To tell the system that your TV input service supports recording, set the`android:canRecord`attribute in your service metadata XML file to`true`:  

```xml
<tv-input xmlns:android="http://schemas.android.com/apk/res/android"
  android:canRecord="true"
  android:setupActivity="com.example.sampletvinput.SampleTvInputSetupActivity" />
```

For more information on the service metadata file, see[Declare your TV input service in the manifest](https://developer.android.com/training/tv/tif/tvinput#manifest).

Alternatively, you can indicate recording support in your code using these steps:

1. In your TV input service[onCreate()](https://developer.android.com/reference/android/app/Service#onCreate())method, create a new[TvInputInfo](https://developer.android.com/reference/android/media/tv/TvInputInfo)object using the[TvInputInfo.Builder](https://developer.android.com/reference/android/media/tv/TvInputInfo.Builder)class.
2. When creating the new`TvInputInfo`object, call[setCanRecord(true)](https://developer.android.com/reference/android/media/tv/TvInputInfo.Builder#setCanRecord(boolean))before calling[build()](https://developer.android.com/reference/android/media/tv/TvInputInfo.Builder#build())to indicate that your service supports recording.
3. Register your`TvInputInfo`object with the system by calling[TvInputManager.updateTvInputInfo()](https://developer.android.com/reference/android/media/tv/TvInputManager#updateTvInputInfo(android.media.tv.TvInputInfo)).

## Record a session

After your TV input service registers that it supports recording functionality, the system calls your[TvInputService.onCreateRecordingSession()](https://developer.android.com/reference/android/media/tv/TvInputService#onCreateRecordingSession(java.lang.String))method when it needs to access your app's recording implementation. Implement your own[TvInputService.RecordingSession](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession)subclass and return it when the`onCreateRecordingSession()`callback fires. This subclass is responsible for switching to the correct channel data, recording the requested data, and communicating recording status and errors to the system.

When the system calls[RecordingSession.onTune()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#onTune(android.net.Uri)), passing in a channel URI, tune to the channel that the URI specifies. Notify the system that your app has tuned to the desired channel by calling[notifyTuned()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#notifyTuned(android.net.Uri))or, if your app can't tune to the proper channel, call[notifyError()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#notifyError(int)).

The system next invokes the[RecordingSession.onStartRecording()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#onStartRecording(android.net.Uri))callback. Your app must start recording immediately. When the system invokes this callback, it might provide a URI that contains information about the program that is about to be recorded. When the recording is done, copy this data to the[RecordedPrograms](https://developer.android.com/reference/android/media/tv/TvContract.RecordedPrograms)data table.

Finally, the system calls[RecordingSession.onStopRecording()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#onStopRecording()). At this point, your app must stop recording immediately. You also need to create an entry in the`RecordedPrograms`table that includes the recorded session data URI in the[RecordedPrograms.COLUMN_RECORDING_DATA_URI](https://developer.android.com/reference/android/media/tv/TvContract.RecordedPrograms#COLUMN_RECORDING_DATA_URI)column, and any program information that the system provided in the initial call to`onStartRecording()`.

For more details on how to access the`RecordedPrograms`table, see the[Manage recorded sessions](https://developer.android.com/training/tv/tif/content-recording#sessions)section.

## Handle recording errors

If an error occurs during recording, resulting in unusable recorded data, notify the system by calling[notifyError()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#notifyError(int)). You can also callnotifyError()after a recording session is created to let the system know that your app can no longer record sessions.

If an error occurs during recording but you want to provide a partial recording to users for playback, call[notifyRecordingStopped()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#notifyRecordingStopped(android.net.Uri))to enable the system to use the partial session.

## Manage recorded sessions

The system maintains information for all recorded sessions from all recording-capable channel apps in the[RecordedPrograms](https://developer.android.com/reference/android/media/tv/TvContract.RecordedPrograms)content provider table. This information is accessible through theRecordedProgramscontent recording URIs. Use content provider APIs to read, add, and delete entries from this table.

For more information on working with content provider data, see[Content provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics).

## Best practices

TV devices might have limited storage, so use your best judgment when allocating storage to save recorded sessions. Use[RecordingCallback.onError(RECORDING_ERROR_INSUFFICIENT_SPACE)](https://developer.android.com/reference/android/media/tv/TvRecordingClient.RecordingCallback#onError(int))when there isn't enough space to save a recorded session.

When the user initiates recording, start recording data as soon as possible. To facilitate this, complete any up-front time-consuming tasks, like accessing and allocating storage space, when the system invokes the[onCreateRecordingSession()](https://developer.android.com/reference/android/media/tv/TvInputService#onCreateRecordingSession(java.lang.String))callback. Doing so lets you start recording immediately when the[onStartRecording()](https://developer.android.com/reference/android/media/tv/TvInputService.RecordingSession#onStartRecording(android.net.Uri))callback fires.