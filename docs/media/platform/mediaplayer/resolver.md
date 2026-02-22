---
title: https://developer.android.com/media/platform/mediaplayer/resolver
url: https://developer.android.com/media/platform/mediaplayer/resolver
source: md.txt
---

# Retrieve media from a content resolver

You can have your media player application retrieve music that the user has on their device by querying the[`ContentResolver`](https://developer.android.com/reference/android/content/ContentResolver)for external media:  

### Kotlin

    val resolver: ContentResolver = contentResolver
    val uri = android.provider.MediaStore.Audio.Media.EXTERNAL_CONTENT_URI
    val cursor: Cursor? = resolver.query(uri, null, null, null, null)
    when {
        cursor == null -> {
            // query failed, handle error.
        }
        !cursor.moveToFirst() -> {
            // no media on the device
        }
        else -> {
            val titleColumn: Int = cursor.getColumnIndex(android.provider.MediaStore.Audio.Media.TITLE)
            val idColumn: Int = cursor.getColumnIndex(android.provider.MediaStore.Audio.Media._ID)
            do {
                val thisId = cursor.getLong(idColumn)
                val thisTitle = cursor.getString(titleColumn)
                // ...process entry...
            } while (cursor.moveToNext())
        }
    }
    cursor?.close()

### Java

    ContentResolver contentResolver = getContentResolver();
    Uri uri = android.provider.MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
    Cursor cursor = contentResolver.query(uri, null, null, null, null);
    if (cursor == null) {
        // query failed, handle error.
    } else if (!cursor.moveToFirst()) {
        // no media on the device
    } else {
        int titleColumn = cursor.getColumnIndex(android.provider.MediaStore.Audio.Media.TITLE);
        int idColumn = cursor.getColumnIndex(android.provider.MediaStore.Audio.Media._ID);
        do {
           long thisId = cursor.getLong(idColumn);
           String thisTitle = cursor.getString(titleColumn);
           // ...process entry...
        } while (cursor.moveToNext());
    }

To use this with the[`MediaPlayer`](https://developer.android.com/reference/android/media/MediaPlayer), you can do this:  

### Kotlin

    val id: Long = /* retrieve it from somewhere */
    val contentUri: Uri =
        ContentUris.withAppendedId(android.provider.MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, id )

    mediaPlayer = MediaPlayer().apply {
        setAudioAttributes(
            AudioAttributes.Builder()
                .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .build()
        )
        setDataSource(applicationContext, contentUri)
    }

    // ...prepare and start...

### Java

    long id = /* retrieve it from somewhere */;
    Uri contentUri = ContentUris.withAppendedId(
            android.provider.MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, id);

    mediaPlayer = new MediaPlayer();
    mediaPlayer.setAudioAttributes(
        new AudioAttributes.Builder()
            .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
            .setUsage(AudioAttributes.USAGE_MEDIA)
            .build()
    );
    mediaPlayer.setDataSource(getApplicationContext(), contentUri);

    // ...prepare and start...

## Learn more

Jetpack Media3 is the recommended solution for media playback in your app.[Read more](https://developer.android.com/media/media3)about it.

These pages cover topics relating to recording, storing, and playing back audio and video:

- [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats)
- [MediaRecorder](https://developer.android.com/guide/topics/media/mediarecorder)
- [Data Storage](https://developer.android.com/guide/topics/data/data-storage)