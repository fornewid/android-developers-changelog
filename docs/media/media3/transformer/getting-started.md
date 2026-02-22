---
title: https://developer.android.com/media/media3/transformer/getting-started
url: https://developer.android.com/media/media3/transformer/getting-started
source: md.txt
---

Getting started with `Transformer` consists of the following steps:

1. Add Media3 Transformer as a dependency in your project.
2. Build an `EditedMediaItem` representing the media to process and edits to apply to it.
3. Build a `Transformer`, describing the required output and a listener for completion and error events.
4. Start the export operation, passing in the `EditedMediaItem` to edit and an output path. During export, you can query the current progress or cancel the operation.
5. When exporting finishes, handle the output as needed. For example, you can share the output to another app or upload it to a server.

Read on for more detail about these steps, and see `TransformerActivity` in the
[transformer demo
app](https://github.com/androidx/media/tree/release/demos/transformer) for a
complete example.

## Add Media3 Transformer as a dependency

The easiest way to get started using Transformer is to add gradle dependencies
on the library in the `build.gradle` file of your app module:  

### Kotlin

```kotlin
implementation("androidx.media3:media3-transformer:1.9.2")
implementation("androidx.media3:media3-effect:1.9.2")
implementation("androidx.media3:media3-common:1.9.2")
```

### Groovy

```groovy
implementation "androidx.media3:media3-transformer:1.9.2"
implementation "androidx.media3:media3-effect:1.9.2"
implementation "androidx.media3:media3-common:1.9.2"
```

where 1.9.2 is your preferred version. The latest version can be
found by consulting the [release
notes](https://github.com/androidx/media/tree/release/RELEASENOTES.md).
| **Important:** If you're using any other Media3 modules, including Media3 ExoPlayer, they must all be the same version.

More information on the library modules that are available can be found on the
[Google Maven AndroidX Media3
page](https://maven.google.com/web/index.html?q=media3).

### Turn on Java 8 support

If not enabled already, you need to turn on Java 8 support in all `build.gradle`
files that depend on Transformer by adding the following to the `android`
section:  

    compileOptions {
      targetCompatibility JavaVersion.VERSION_1_8
    }

## Start a transformation

Here's an example of creating an `EditedMediaItem` to remove audio for an input
file, then creating and configuring a `Transformer` instance to export
H.265/HEVC video, outputting the result to `outputPath`.  

### Kotlin

```kotlin
val inputMediaItem = MediaItem.fromUri("path_to_input_file")
val editedMediaItem =
    EditedMediaItem.Builder(inputMediaItem).setRemoveAudio(true).build()
val transformer = Transformer.Builder(context)
    .setVideoMimeType(MimeTypes.VIDEO_H265)
    .addListener(transformerListener)
    .build()
transformer.start(editedMediaItem, outputPath)
```

### Java

```java
MediaItem inputMediaItem = MediaItem.fromUri("path_to_input_file");
EditedMediaItem editedMediaItem =
    new EditedMediaItem.Builder(inputMediaItem).setRemoveAudio(true).build();
Transformer transformer =
    new Transformer.Builder(context)
        .setVideoMimeType(MimeTypes.VIDEO_H265)
        .addListener(transformerListener)
        .build();
transformer.start(editedMediaItem, outputPath);
```

<br />

For more information about media items, see the [ExoPlayer media items
page](https://developer.android.com/media/media3/exoplayer/media-items). The input can be a progressive or an adaptive
stream, but the output is always a progressive stream. For adaptive inputs, the
highest-resolution tracks are always selected for the transformation. The input
can be of any container format [supported](https://developer.android.com/media/media3/transformer/supported-formats) by ExoPlayer, but
the output is always an MP4 file.

You can execute multiple export operations sequentially on the same
`Transformer` instance, but concurrent exports with the same instance are not
supported.
| **Note:** Support for generating media by composing together multiple inputs is planned for future versions of Transformer.

### A note on threading

Transformer instances must be accessed from a single application thread, and the
listener methods are called on the same thread. For the majority of cases, the
application thread can just be the main thread of the application. Internally,
Transformer does its work in the background and posts its calls to listener
methods on the application thread.

## Listen to events

The `start` method is asynchronous. It returns immediately and the app is
notified of events through the listener passed to the `Transformer` builder.  

### Kotlin

```kotlin
val transformerListener: Transformer.Listener =
    object : Transformer.Listener {
  override fun onCompleted(composition: Composition, result: ExportResult) {
    playOutput()
  }

  override fun onError(composition: Composition, result: ExportResult,
                       exception: ExportException) {
    displayError(exception)
  }
}
```

### Java

```java
Transformer.Listener transformerListener =
    new Transformer.Listener() {
      @Override
      public void onCompleted(Composition composition, ExportResult result) {
        playOutput();
      }

      @Override
      public void onError(Composition composition, ExportResult result,
          ExportException exception) {
        displayError(exception);
      }
    };
```

<br />

`ExportResult` includes information about the output file, including the file
size and average bitrates for audio and video, as applicable.

## Get progress updates

Call `Transformer.getProgress` to query the current progress of a
transformation. The returned value indicates the progress state. If the progress
state is `PROGRESS_STATE_AVAILABLE`, then the provided `ProgressHolder` is
updated with the current progress percentage. The following example shows how to
periodically query the progress of a transformation, where the
`updateProgressInUi` method can be implemented to update a progress bar.  

### Kotlin

```kotlin
transformer.start(inputMediaItem, outputPath)
val progressHolder = ProgressHolder()
mainHandler.post(
    object : Runnable {
      override fun run() {
        val progressState: @ProgressState Int = transformer.getProgress(progressHolder)
        updateProgressInUi(progressState, progressHolder)
        if (progressState != Transformer.PROGRESS_STATE_NOT_STARTED) {
          mainHandler.postDelayed(/* r= */this,  /* delayMillis= */500)
        }
      }
    }
)
```

### Java

```java
transformer.start(inputMediaItem, outputPath);
ProgressHolder progressHolder = new ProgressHolder();
mainHandler.post(
    new Runnable() {
      @Override
      public void run() {
        @Transformer.ProgressState int progressState = transformer.getProgress(progressHolder);
        updateProgressInUi(progressState, progressHolder);
        if (progressState != PROGRESS_STATE_NOT_STARTED) {
          mainHandler.postDelayed(/* r= */ this, /* delayMillis= */ 500);
        }
      }
    });
```

<br />

## Cancel a transformation

If the user chooses to back out of an export flow, cancel the export operation
with `Transformer.cancel`. Resources like hardware video codecs are limited,
especially on lower-end devices, so it's important to do this to free up
resources if the output isn't needed.