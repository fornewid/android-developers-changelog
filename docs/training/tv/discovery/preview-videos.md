---
title: Preview videos  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/discovery/preview-videos
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Preview videos Stay organized with collections Save and categorize content based on your preferences.



A preview video is a great way to encourage users to deep-link into your TV app.
Previews can range from short clips to full movie trailers.

When you create a preview, consider these guidelines:

* Do not show ads in a preview. If you stitch ads on the client side,
  do not stitch them into preview videos. If you stich ads on the server side,
  provide an ad-free video for previews.
* For best quality, preview videos should be 16:9 or 4:3. See
  [Video program attributes](/training/tv/discovery/video-programs#preview_images)
  for the recommended sizes of preview videos.
* When the preview video and the poster art have different aspect ratios, the
  home screen resizes the poster view to the video's aspect ratio before playing the preview.
  The video is not letterboxed. For example, if
  the poster art ratio is
  [`ASPECT_RATIO_MOVIE_POSTER`](/reference/androidx/tvprovider/media/tv/TvContractCompat.PreviewPrograms#aspect_ratio_movie_poster) (1:1.441)
  but the video ratio is 16:9, the poster view transforms to a 16:9 region.
* When you create a preview, its content can be publicly accessible or
  protected under DRM. Different procedures apply in each case. This page
  describes both.

## Play the preview on the home screen

If you create a preview using any of the [video types](http://google.github.io/ExoPlayer/supported-formats.html)
supported by [ExoPlayer](/guide/topics/media/exoplayer)
and the preview is publicly accessible, you can play the preview directly on the home screen.

When you build a [PreviewProgram](/training/tv/discovery/recommendations-channel#programs)
use `setPreviewVideoUri()` with a publicly accessible HTTPS
URL as shown in the example below. The preview can be either
[video](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setpreviewvideouri) or
[audio](/reference/androidx/tvprovider/media/tv/PreviewProgram.Builder#setpreviewaudiouri).

### Kotlin

```
val previewVideoUrl = Uri.parse("https://www.example.com/preview.mp4")
val builder = PreviewProgram.Builder()
builder.setChannelId(channelId)
    // ...
    .setPreviewVideoUri(previewVideoUrl)
```

### Java

```
Uri previewVideoUrl = Uri.parse("https://www.example.com/preview.mp4");
PreviewProgram.Builder builder = new PreviewProgram.Builder();
builder.setChannelId(channelId)
    // ...
    .setPreviewVideoUri(Uri.parse(previewVideoUrl));
```

## Render the preview on a surface

If your video is DRM-protected or in a media type not supported by
[ExoPlayer](/guide/topics/media/exoplayer), use a `TvInputService`.
The Android TV home screen passes a `Surface` to your service
by calling `onSetSurface()`. Your app draws video directly on this surface from `onTune()`.

Direct surface rendering lets your app control what is rendered and how it is
rendered. You can overlay metadata such as channel attribution.

### Declare your TvInputService in the manifest

Your app must provide an implementation of `TvInputService`
so the home screen can render your preview.

In your service declaration, include an intent filter that specifies
`TvInputService` as the action to perform with the
intent. Also declare the service metadata as a separate XML resource. The
service declaration, intent filter, and service metadata declaration are shown
in the following example:

```
<service android:name=".rich.PreviewInputService"
    android:permission="android.permission.BIND_TV_INPUT">
    <!-- Required filter used by the system to launch our account service. -->
    <intent-filter>
        <action android:name="android.media.tv.TvInputService" />
    </intent-filter>
    <!-- An XML file which describes this input. -->
    <meta-data
        android:name="android.media.tv.input"
        android:resource="@xml/previewinputservice" />
</service>
```

Define the service metadata in a separate XML file.
The service metadata file is located in the XML resources directory
for your app and must match the name of the resource you declared in the
manifest. Using the manifest entries from the previous example, you would
create an XML file at `res/xml/previewinputservice.xml`, with an empty
`tv-input` tag:

```
<?xml version="1.0" encoding="utf-8"?>
<tv-input/>
```

[TV Input Framework](/training/tv/tif) must have this tag. However,
it's only used to configure live channels. Since you are rendering a video,
the tag should be empty.

### Create a video URI

To indicate that your preview video should be rendered by your app rather than
the Android TV home screen, you must create a video URI for a `PreviewProgram`.
The URI should end with the identifier that your app uses for the content, so you
can retrieve the content later in the `TvInputService`.

If your identifier is type `Long`, use
[TvContractCompat.buildPreviewProgramUri()](/reference/androidx/tvprovider/media/tv/TvContractCompat#buildPreviewProgramUri(long)):

### Kotlin

```
val id: Long = 1L // content identifier
val componentName = new ComponentName(context, PreviewVideoInputService.class)
val previewProgramVideoUri = TvContractCompat.buildPreviewProgramUri(id)
   .buildUpon()
   .appendQueryParameter("input", TvContractCompat.buildInputId(componentName))
   .build()
```

### Java

```
Long id = 1L; // content identifier
ComponentName componentName = new ComponentName(context, PreviewVideoInputService.class);
previewProgramVideoUri = TvContractCompat.buildPreviewProgramUri(id)
       .buildUpon()
       .appendQueryParameter("input", TvContractCompat.buildInputId(componentName))
       .build();
```

If your identifier is not type `Long`, build the URI using
`Uri.withAppendedPath()`:

### Kotlin

```
val previewProgramVideoUri = Uri.withAppendedPath(PreviewPrograms.CONTENT_URI, "content-identifier")
       .buildUpon()
       .appendQueryParameter("input", TvContractCompat.buildInputId(componentName))
       .build()
```

### Java

```
previewProgramVideoUri = Uri.withAppendedPath(PreviewPrograms.CONTENT_URI, "content-identifier")
       .buildUpon()
       .appendQueryParameter("input", TvContractCompat.buildInputId(componentName))
       .build();
```

Your app calls
`onTune(Uri videoUri)`
to make Android TV start the preview video.

### Create a service

The following example shows how to extend `TvInputService` to create your own
`PreviewInputService`. Note that the service uses a `MediaPlayer` for playback,
but your code can use any available video player.

### Kotlin

```
import android.content.Context
import android.media.MediaPlayer
import android.media.tv.TvInputService
import android.net.Uri
import android.util.Log
import android.view.Surface
import java.io.IOException

class PreviewVideoInputService : TvInputService() {

    override fun onCreateSession(inputId: String): TvInputService.Session? {
        return PreviewSession(this)
    }

    private inner class PreviewSession(
        internal var context: Context
    ) : TvInputService.Session(context) {
    
        internal var mediaPlayer: MediaPlayer? = MediaPlayer()

        override fun onRelease() {
            mediaPlayer?.release()
            mediaPlayer = null
        }

        override fun onTune(uri: Uri): Boolean {
            // Let the TvInputService know that the video is being loaded.
            notifyVideoUnavailable(VIDEO_UNAVAILABLE_REASON_TUNING)
            // Fetch the stream url from the TV Provider database
            // for content://android.media.tv/preview_program/
            val id = uri.lastPathSegment
            // Load your video in the background.
            retrieveYourVideoPreviewUrl(id) { videoUri ->
                if (videoUri == null) {
                  Log.d(TAG, "Could not find video $id")
                  notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_UNKNOWN)
                }

                try {
                    mPlayer.setDataSource(getApplicationContext(), videoUri)
                    mPlayer.prepare()
                    mPlayer.start()
                    notifyVideoAvailable()
                } catch (IOException e) {
                    Log.e(TAG, "Could not prepare media player", e)
                    notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_UNKNOWN)
                }
              }
          return true
        }

        override fun onSetSurface(surface: Surface?): Boolean {
            mediaPlayer?.setSurface(surface)
            return true
        }

        override fun onSetStreamVolume(volume: Float) {
            // The home screen may fade in and out the video's volume.
            // Your player should be updated accordingly.
            mediaPlayer?.setVolume(volume, volume)
        }

        override fun onSetCaptionEnabled(b: Boolean) {
            // enable/disable captions here
        }
    }

    companion object {
        private const val TAG = "PreviewInputService"
    }
}
```

### Java

```
import android.content.Context;
import android.media.MediaPlayer;
import android.media.tv.TvInputService;
import android.net.Uri;
import android.support.annotation.Nullable;
import android.util.Log;
import android.view.Surface;
import java.io.IOException;

public class PreviewVideoInputService extends TvInputService {
    private static final String TAG = "PreviewVideoInputService";

    @Nullable
    @Override
    public Session onCreateSession(String inputId) {
        return new PreviewSession(this);
    }

    private class PreviewSession extends TvInputService.Session {

        private MediaPlayer mPlayer;

        PreviewSession(Context context) {
            super(context);
            mPlayer = new MediaPlayer();
        }

        @Override
        public boolean onTune(Uri channelUri) {
            // Let the TvInputService know that the video is being loaded.
            notifyVideoUnavailable(VIDEO_UNAVAILABLE_REASON_TUNING);
            // Fetch the stream url from the TV Provider database
            // for content://android.media.tv/preview_program/
            String id = uri.getLastPathSegment();
            // Load your video in the background.
            retrieveYourVideoPreviewUrl(id, new MyCallback() {
              public void callback(Uri videoUri) {
                if (videoUri == null) {
                  Log.d(TAG, "Could not find video" + id);
                  notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_UNKNOWN);
                }

                try {
                    mPlayer.setDataSource(getApplicationContext(), videoUri);
                    mPlayer.prepare();
                    mPlayer.start();
                    notifyVideoAvailable();
                } catch (IOException e) {
                    Log.e(TAG, "Could not prepare media player", e);
                    notifyVideoUnavailable(TvInputManager.VIDEO_UNAVAILABLE_REASON_UNKNOWN);
                }
              }
            });
            return true;
        }

        @Override
        public boolean onSetSurface(@Nullable Surface surface) {
            if (mPlayer != null) {
                mPlayer.setSurface(surface);
            }
            return true;
        }

        @Override
        public void onRelease() {
            if (mPlayer != null) {
                mPlayer.release();
            }
            mPlayer = null;
        }

        @Override
        public void onSetStreamVolume(float volume) {
            if (mPlayer != null) {
                // The home screen may fade in and out the video's volume.
                // Your player should be updated accordingly.
                mPlayer.setVolume(volume, volume);
            }
        }

        @Override
        public void onSetCaptionEnabled(boolean enabled) {
            // enable/disable captions here
        }
    }
}
```

[Previous

arrow\_back

Guidelines for TV providers](/training/tv/discovery/guidelines-tv-providers)

[Next

Recommendations in Android N and earlier

arrow\_forward](/training/tv/discovery/recommendations-row)