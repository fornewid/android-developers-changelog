---
title: https://developer.android.com/media/camera/camera-deprecated/videobasics
url: https://developer.android.com/media/camera/camera-deprecated/videobasics
source: md.txt
---

# Record videos

**Note:** This page refers to the[Camera](https://developer.android.com/reference/android/hardware/Camera)class, which is deprecated. We recommend using[CameraX](https://developer.android.com/media/camera/camerax)or, for specific use cases,[Camera2](https://developer.android.com/media/camera/camera2). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

This lesson explains how to capture video using existing camera applications.

Your application has a job to do, and integrating videos is only a small part of it. You want to take videos with minimal fuss, and not reinvent the camcorder. Happily, most Android-powered devices already have a camera application that records video. In this lesson, you make it do this for you.  
Refer to the following related resources:

- [Camera](https://developer.android.com/guide/topics/media/camera)
- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)

## Request the camera feature

To advertise that your application depends on having a camera, put a`<uses-feature>`tag in the manifest file:  

```xml
<manifest ... >
    <uses-feature android:name="android.hardware.camera"
                  android:required="true" />
    ...
</manifest>
```

If your application uses, but does not require a camera in order to function, set`android:required`to`false`. In doing so, Google Play will allow devices without a camera to download your application. It's then your responsibility to check for the availability of the camera at runtime by calling[hasSystemFeature(PackageManager.FEATURE_CAMERA)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)). If a camera is not available, you should then disable your camera features.

## View the video

The Android Camera application returns the video in the[Intent](https://developer.android.com/reference/android/content/Intent)delivered to[onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent))as a[Uri](https://developer.android.com/reference/android/net/Uri)pointing to the video location in storage. The following code retrieves this video and displays it in a[VideoView](https://developer.android.com/reference/android/widget/VideoView).  

### Kotlin

```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, intent: Intent) {
    if (requestCode == REQUEST_VIDEO_CAPTURE && resultCode == RESULT_OK) {
        val videoUri: Uri = intent.data
        videoView.setVideoURI(videoUri)
    }
}
```

### Java

```java
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent intent) {
    if (requestCode == REQUEST_VIDEO_CAPTURE && resultCode == RESULT_OK) {
        Uri videoUri = intent.getData();
        videoView.setVideoURI(videoUri);
    }
}
```