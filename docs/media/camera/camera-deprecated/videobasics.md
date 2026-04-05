---
title: Record videos  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/camera-deprecated/videobasics
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Record videos Stay organized with collections Save and categorize content based on your preferences.



**Note:** This page refers to the
[Camera](/reference/android/hardware/Camera) class, which is deprecated. We
recommend using [CameraX](/media/camera/camerax) or, for specific use cases,
[Camera2](/media/camera/camera2). Both CameraX and Camera2 support Android 5.0
(API level 21) and higher.

This lesson explains how to capture video using existing camera
applications.

Your application has a job to do, and integrating videos is only a small
part of it. You want to take videos with minimal fuss, and not reinvent the
camcorder. Happily, most Android-powered devices already have a camera application that
records video. In this lesson, you make it do this for you.

Refer to the following related resources:

* [Camera](/guide/topics/media/camera)
* [Intents and Intent
  Filters](/guide/components/intents-filters)

## Request the camera feature

To advertise that your application depends on having a camera, put a
`<uses-feature>` tag in the manifest file:

```
<manifest ... >
    <uses-feature android:name="android.hardware.camera"
                  android:required="true" />
    ...
</manifest>
```

If your application uses, but does not require a camera in order to function, set `android:required` to `false`. In doing so, Google Play will allow devices without a
camera to download your application. It's then your responsibility to check for the availability
of the camera at runtime by calling `hasSystemFeature(PackageManager.FEATURE_CAMERA)`.
If a camera is not available, you should then disable your camera features.

## View the video

The Android Camera application returns the video in the `Intent` delivered
to `onActivityResult()` as a `Uri` pointing to the video location in storage. The following code
retrieves this video and displays it in a `VideoView`.

### Kotlin

```
override fun onActivityResult(requestCode: Int, resultCode: Int, intent: Intent) {
    if (requestCode == REQUEST_VIDEO_CAPTURE && resultCode == RESULT_OK) {
        val videoUri: Uri = intent.data
        videoView.setVideoURI(videoUri)
    }
}
```

### Java

```
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent intent) {
    if (requestCode == REQUEST_VIDEO_CAPTURE && resultCode == RESULT_OK) {
        Uri videoUri = intent.getData();
        videoView.setVideoURI(videoUri);
    }
}
```