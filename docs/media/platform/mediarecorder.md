---
title: https://developer.android.com/media/platform/mediarecorder
url: https://developer.android.com/media/platform/mediarecorder
source: md.txt
---

# MediaRecorder overview

The Android multimedia framework includes support for capturing and encoding a variety of common audio and video formats. You can use the[MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder)APIs if supported by the device hardware.

This document shows you how to use`MediaRecorder`to write an application that captures audio from a device microphone, save the audio, and play it back (with[MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer)). To record video you'll need to use the device's camera along with`MediaRecorder`. This is described in the[Camera](https://developer.android.com/guide/topics/media/camera)guide.

**Note:**The Android Emulator cannot record audio. Be sure to test your code on a real device that can record.

## Requesting permission to record audio

To be able to record, your app must tell the user that it will access the device's audio input. You must include this permission tag in the app's manifest file:  

```xml
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

`RECORD_AUDIO`is considered a["dangerous" permission](https://developer.android.com/guide/topics/permissions/requesting#normal-dangerous)because it may pose a risk to the user's privacy. Starting with Android 6.0 (API level 23) an app that uses a dangerous permission must ask the user for approval at run time. After the user has granted permission, the app should remember and not ask again. The sample code below shows how to implement this behavior using[ActivityCompat.requestPermissions()](https://developer.android.com/reference/androidx/core/app/ActivityCompat#requestPermissions(android.app.Activity, java.lang.String[], int)).

## Creating and running a MediaRecorder

Initialize a new instance of[MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder)with the following calls:

- Set the audio source using[setAudioSource()](https://developer.android.com/reference/android/media/MediaRecorder#setAudioSource(int)). You'll probably use[MIC](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#MIC).

  **Note:** Most of the audio sources (including`DEFAULT`) apply processing to the audio signal. To record raw audio select[UNPROCESSED](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#UNPROCESSED). Some devices do not support unprocessed input. Call[AudioManager.getProperty(AudioManager.PROPERTY_SUPPORT_AUDIO_SOURCE_UNPROCESSED)](https://developer.android.com/reference/android/media/AudioManager#getProperty(java.lang.String))first to verify it's available. If it is not, try using[VOICE_RECOGNITION](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource#VOICE_RECOGNITION)instead, which does not employ AGC or noise suppression. You can use`UNPROCESSED`as an audio source even when the property is not supported, but there is no guarantee whether the signal will be unprocessed or not in that case.
- Set the output file format using[setOutputFormat()](https://developer.android.com/reference/android/media/MediaRecorder#setOutputFormat(int)). Note that starting with Android 8.0 (API level 26)`MediaRecorder`supports the MPEG2_TS format, which is useful for streaming:  

  ### Kotlin

  ```kotlin
  mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_2_TS)
  ```

  ### Java

  ```java
  mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_2_TS);
  ```
- Set the output file name using[setOutputFile()](https://developer.android.com/reference/android/media/MediaRecorder#setOutputFile(java.io.File)). You must specify a file descriptor that represents an actual file.
- Set the audio encoder using[setAudioEncoder()](https://developer.android.com/reference/android/media/MediaRecorder#setAudioEncoder(int)).
- Complete the initialization by calling[prepare()](https://developer.android.com/reference/android/media/MediaRecorder#prepare()).

Start and stop the recorder by calling[start()](https://developer.android.com/reference/android/media/MediaRecorder#start())and[stop()](https://developer.android.com/reference/android/media/MediaRecorder#start())respectively.

When you are done with the`MediaRecorder`instance free its resources as soon as possible by calling[release()](https://developer.android.com/reference/android/media/MediaRecorder#release()).

**Note:** On devices running Android 9 (API level 28) or higher, apps running in the background cannot access the microphone. Therefore, your app should record audio only when it's in the foreground or when you include an instance of`MediaRecorder`in a[foreground service](https://developer.android.com/guide/components/services#Foreground).

## Using MediaMuxer to record multiple channels

Starting with Android 8.0 (API level 26) you can use a[MediaMuxer](https://developer.android.com/reference/android/media/MediaMuxer)to record multiple simultaneous audio and video streams. In earlier versions of Android you can only record one audio track and/or one video track at a time.

Use the[addTrack()](https://developer.android.com/reference/android/media/MediaMuxer#addTrack(android.media.MediaFormat))method to mix multiple tracks together.

You can also add one or more metadata tracks with custom information for each frame, but only to MP4 containers. Your app defines the format and content of the metadata.

## Adding metadata

Metadata can be useful for offline processing. For example, data captured from the gyro sensor could be used to perform video stabilization.

When you add a metadata track, the track's mime format must start with the prefix`application/`. Writing metadata is the same as writing video or audio data, except that the data does not come from a`MediaCodec`. Instead, the app passes a`ByteBuffer`with an associated timestamp to the[writeSampleData()](https://developer.android.com/reference/android/media/MediaMuxer#writeSampleData(int, java.nio.ByteBuffer, android.media.MediaCodec.BufferInfo))method. The timestamp must be in the same time base as the video and audio tracks.

The generated MP4 file uses the`TextMetaDataSampleEntry`defined in section 12.3.3.2 of the[ISO BMFF](https://en.wikipedia.org/wiki/ISO_base_media_file_format)specification to signal the metadata's mime format. When you use a[MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor)to extract a file that contains metadata tracks, the metadata's mime format appears as an instance of[MediaFormat](https://developer.android.com/reference/android/media/MediaFormat).

## Sample code

The[MediaRecorder](https://github.com/android/media-samples/tree/main/MediaRecorder/)sample demonstrates how to make a video recording using MediaRecorder and the Camera API.

The example activity below shows how to use`MediaRecorder`to record an audio file. It Also uses`MediaPlayer`to play the audio back.  

### Kotlin

```kotlin
package com.android.audiorecordtest

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.media.MediaPlayer
import android.media.MediaRecorder
import android.os.Bundle
import android.support.v4.app.ActivityCompat
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.View.OnClickListener
import android.view.ViewGroup
import android.widget.Button
import android.widget.LinearLayout
import java.io.IOException

private const val LOG_TAG = "AudioRecordTest"
private const val REQUEST_RECORD_AUDIO_PERMISSION = 200

class AudioRecordTest : AppCompatActivity() {

    private var fileName: String = ""

    private var recordButton: RecordButton? = null
    private var recorder: MediaRecorder? = null

    private var playButton: PlayButton? = null
    private var player: MediaPlayer? = null

    // Requesting permission to RECORD_AUDIO
    private var permissionToRecordAccepted = false
    private var permissions: Array<String> = arrayOf(Manifest.permission.RECORD_AUDIO)

    override fun onRequestPermissionsResult(
            requestCode: Int,
            permissions: Array<String>,
            grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        permissionToRecordAccepted = if (requestCode == REQUEST_RECORD_AUDIO_PERMISSION) {
            grantResults[0] == PackageManager.PERMISSION_GRANTED
        } else {
            false
        }
        if (!permissionToRecordAccepted) finish()
    }

    private fun onRecord(start: Boolean) = if (start) {
        startRecording()
    } else {
        stopRecording()
    }

    private fun onPlay(start: Boolean) = if (start) {
        startPlaying()
    } else {
        stopPlaying()
    }

    private fun startPlaying() {
        player = MediaPlayer().apply {
            try {
                setDataSource(fileName)
                prepare()
                start()
            } catch (e: IOException) {
                Log.e(LOG_TAG, "prepare() failed")
            }
        }
    }

    private fun stopPlaying() {
        player?.release()
        player = null
    }

    private fun startRecording() {
        recorder = MediaRecorder().apply {
            setAudioSource(MediaRecorder.AudioSource.MIC)
            setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP)
            setOutputFile(fileName)
            setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB)

            try {
                prepare()
            } catch (e: IOException) {
                Log.e(LOG_TAG, "prepare() failed")
            }

            start()
        }
    }

    private fun stopRecording() {
        recorder?.apply {
            stop()
            release()
        }
        recorder = null
    }

    internal inner class RecordButton(ctx: Context) : Button(ctx) {

        var mStartRecording = true

        var clicker: OnClickListener = OnClickListener {
            onRecord(mStartRecording)
            text = when (mStartRecording) {
                true -> "Stop recording"
                false -> "Start recording"
            }
            mStartRecording = !mStartRecording
        }

        init {
            text = "Start recording"
            setOnClickListener(clicker)
        }
    }

    internal inner class PlayButton(ctx: Context) : Button(ctx) {
        var mStartPlaying = true
        var clicker: OnClickListener = OnClickListener {
            onPlay(mStartPlaying)
            text = when (mStartPlaying) {
                true -> "Stop playing"
                false -> "Start playing"
            }
            mStartPlaying = !mStartPlaying
        }

        init {
            text = "Start playing"
            setOnClickListener(clicker)
        }
    }

    override fun onCreate(icicle: Bundle?) {
        super.onCreate(icicle)

        // Record to the external cache directory for visibility
        fileName = "${externalCacheDir.absolutePath}/audiorecordtest.3gp"

        ActivityCompat.requestPermissions(this, permissions, REQUEST_RECORD_AUDIO_PERMISSION)

        recordButton = RecordButton(this)
        playButton = PlayButton(this)
        val ll = LinearLayout(this).apply {
            addView(recordButton,
                    LinearLayout.LayoutParams(
                            ViewGroup.LayoutParams.WRAP_CONTENT,
                            ViewGroup.LayoutParams.WRAP_CONTENT,
                            0f))
            addView(playButton,
                    LinearLayout.LayoutParams(
                            ViewGroup.LayoutParams.WRAP_CONTENT,
                            ViewGroup.LayoutParams.WRAP_CONTENT,
                            0f))
        }
        setContentView(ll)
    }

    override fun onStop() {
        super.onStop()
        recorder?.release()
        recorder = null
        player?.release()
        player = null
    }
}
```

### Java

```java
package com.android.audiorecordtest;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;

import java.io.IOException;

public class AudioRecordTest extends AppCompatActivity {

    private static final String LOG_TAG = "AudioRecordTest";
    private static final int REQUEST_RECORD_AUDIO_PERMISSION = 200;
    private static String fileName = null;

    private RecordButton recordButton = null;
    private MediaRecorder recorder = null;

    private PlayButton playButton = null;
    private MediaPlayer player = null;

    // Requesting permission to RECORD_AUDIO
    private boolean permissionToRecordAccepted = false;
    private String [] permissions = {Manifest.permission.RECORD_AUDIO};

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        switch (requestCode){
            case REQUEST_RECORD_AUDIO_PERMISSION:
                permissionToRecordAccepted  = grantResults[0] == PackageManager.PERMISSION_GRANTED;
                break;
        }
        if (!permissionToRecordAccepted ) finish();

    }

    private void onRecord(boolean start) {
        if (start) {
            startRecording();
        } else {
            stopRecording();
        }
    }

    private void onPlay(boolean start) {
        if (start) {
            startPlaying();
        } else {
            stopPlaying();
        }
    }

    private void startPlaying() {
        player = new MediaPlayer();
        try {
            player.setDataSource(fileName);
            player.prepare();
            player.start();
        } catch (IOException e) {
            Log.e(LOG_TAG, "prepare() failed");
        }
    }

    private void stopPlaying() {
        player.release();
        player = null;
    }

    private void startRecording() {
        recorder = new MediaRecorder();
        recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        recorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        recorder.setOutputFile(fileName);
        recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);

        try {
            recorder.prepare();
        } catch (IOException e) {
            Log.e(LOG_TAG, "prepare() failed");
        }

        recorder.start();
    }

    private void stopRecording() {
        recorder.stop();
        recorder.release();
        recorder = null;
    }

    class RecordButton extends Button {
        boolean mStartRecording = true;

        OnClickListener clicker = new OnClickListener() {
            public void onClick(View v) {
                onRecord(mStartRecording);
                if (mStartRecording) {
                    setText("Stop recording");
                } else {
                    setText("Start recording");
                }
                mStartRecording = !mStartRecording;
            }
        };

        public RecordButton(Context ctx) {
            super(ctx);
            setText("Start recording");
            setOnClickListener(clicker);
        }
    }

    class PlayButton extends Button {
        boolean mStartPlaying = true;

        OnClickListener clicker = new OnClickListener() {
            public void onClick(View v) {
                onPlay(mStartPlaying);
                if (mStartPlaying) {
                    setText("Stop playing");
                } else {
                    setText("Start playing");
                }
                mStartPlaying = !mStartPlaying;
            }
        };

        public PlayButton(Context ctx) {
            super(ctx);
            setText("Start playing");
            setOnClickListener(clicker);
        }
    }

    @Override
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);

        // Record to the external cache directory for visibility
        fileName = getExternalCacheDir().getAbsolutePath();
        fileName += "/audiorecordtest.3gp";

        ActivityCompat.requestPermissions(this, permissions, REQUEST_RECORD_AUDIO_PERMISSION);

        LinearLayout ll = new LinearLayout(this);
        recordButton = new RecordButton(this);
        ll.addView(recordButton,
                new LinearLayout.LayoutParams(
                        ViewGroup.LayoutParams.WRAP_CONTENT,
                        ViewGroup.LayoutParams.WRAP_CONTENT,
                        0));
        playButton = new PlayButton(this);
        ll.addView(playButton,
                new LinearLayout.LayoutParams(
                        ViewGroup.LayoutParams.WRAP_CONTENT,
                        ViewGroup.LayoutParams.WRAP_CONTENT,
                        0));
        setContentView(ll);
    }

    @Override
    public void onStop() {
        super.onStop();
        if (recorder != null) {
            recorder.release();
            recorder = null;
        }

        if (player != null) {
            player.release();
            player = null;
        }
    }
}
```

## Learn more

These pages cover topics relating to recording, storing, and playing back audio and video.

- [Supported media formats](https://developer.android.com/guide/topics/media/media-formats)
- [Requesting permissions](https://developer.android.com/guide/topics/permissions/requesting)
- [Data storage](https://developer.android.com/guide/topics/data/data-storage)
- [MediaPlayer](https://developer.android.com/guide/topics/media/mediaplayer)