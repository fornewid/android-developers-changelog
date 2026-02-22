---
title: https://developer.android.com/media/camera/camera-intents
url: https://developer.android.com/media/camera/camera-intents
source: md.txt
---

To perform basic camera actions like capturing a photo or video using the device's default camera application, you do not need to integrate with a [Camera library](https://developer.android.com/training/camera/choose-camera-library). Instead, use an [`Intent`](https://developer.android.com/reference/android/content/Intent).

## Take a photo with a camera app

Android delegates actions to other applications by invoking an `Intent`. This process involves three pieces: the `Intent` itself, a call to start the external `Activity`, and some code to handle the image data when focus returns to your activity.

Here's a function that invokes an `Intent` to capture a photo.  

### Kotlin

```kotlin
val REQUEST_IMAGE_CAPTURE = 1
 
private fun dispatchTakePictureIntent() {
    val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
    try {
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
    } catch (e: ActivityNotFoundException) {
        // display error state to the user
    }
}
```

### Java

```java
static final int REQUEST_IMAGE_CAPTURE = 1;
 
private void dispatchTakePictureIntent() {
    Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    try {
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
    } catch (ActivityNotFoundException e) {
        // display error state to the user
    }
}
```

## Record a video with a camera app

You can also invoke an `Intent` to capture a video.  

### Kotlin

```kotlin
val REQUEST_VIDEO_CAPTURE = 1
 
private fun dispatchTakeVideoIntent() {
    Intent(MediaStore.ACTION_VIDEO_CAPTURE).also { takeVideoIntent ->
        takeVideoIntent.resolveActivity(packageManager)?.also {
            startActivityForResult(takeVideoIntent, REQUEST_VIDEO_CAPTURE)
        } ?: run {
          //display error state to the user
        }
    }
}
```

### Java

```java
static final int REQUEST_VIDEO_CAPTURE = 1;
 
private void dispatchTakeVideoIntent() {
    Intent takeVideoIntent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
    if (takeVideoIntent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(takeVideoIntent, REQUEST_VIDEO_CAPTURE);
    }
    else {
      //display error state to the user
    }
}
```

The `startActivityForResult()` method is protected by a condition that calls `resolveActivity()`, which returns the first activity component that can handle the `Intent`. Perform this check to ensure that you are invoking an `Intent` that won't crash your app.

## Additional Resources

For basic camera actions, use an `Intent`. Otherwise, it is recommended to use the Camera2 and CameraX libraries for anything more complex than basic image or video capture.

- [CameraX camera package](https://developer.android.com/training/camerax)
- [Camera2 camera package](https://developer.android.com/training/camera2)
- [Camera sample projects](https://github.com/android/camera-samples)