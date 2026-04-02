---
title: https://developer.android.com/develop/ui/compose/system/picture-in-picture
url: https://developer.android.com/develop/ui/compose/system/picture-in-picture
source: md.txt
---

Picture-in-picture (PiP) is a special type of multi-window mode mostly used for
video playback. It lets the user watch a video in a small window pinned to a
corner of the screen while navigating between apps or browsing content on the
main screen.

PiP leverages the multi-window APIs made available in Android 7.0 to provide the
pinned video overlay window. To add PiP to your app, you need to register your
activity, switch your activity to PiP mode as needed, and make sure UI elements
are hidden and video playback continues when the activity is in PiP mode.

## Implement PiP with Jetpack

Use the [Jetpack Picture-in-Picture library](https://developer.android.com/jetpack/androidx/releases/core#core-pip_version_10_2) to implement
picture-in-picture experience as it streamlines integration and reduces common
in-app issues. Refer to our [platform sample app](https://github.com/android/platform-samples/tree/main/samples/user-interface/picture-in-picture) to see an
example of its usage. However, if you prefer to implement PiP using the
platform APIs, refer to the following documentation.

## Handle your UI in PiP mode

When you enter PiP mode, your app's entire UI enters the PiP window unless you
specify how your UI should look in and out of PiP mode.

First, you need to know when your app is in PiP mode or not. You can use
[`OnPictureInPictureModeChangedProvider`](https://developer.android.com/reference/androidx/core/app/OnPictureInPictureModeChangedProvider) to achieve this.
The code below tells you if your app is in PiP mode.


```kotlin
@Composable
fun rememberIsInPipMode(): Boolean {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val activity = LocalContext.current.findActivity()
        var pipMode by remember { mutableStateOf(activity.isInPictureInPictureMode) }
        DisposableEffect(activity) {
            val observer = Consumer<PictureInPictureModeChangedInfo> { info ->
                pipMode = info.isInPictureInPictureMode
            }
            activity.addOnPictureInPictureModeChangedListener(
                observer
            )
            onDispose { activity.removeOnPictureInPictureModeChangedListener(observer) }
        }
        return pipMode
    } else {
        return false
    }
}
```

<br />

Now, you can use `rememberIsInPipMode()` to toggle which UI elements to show
when the app enters PiP mode:


```kotlin
val inPipMode = rememberIsInPipMode()

Column(modifier = modifier) {
    // This text will only show up when the app is not in PiP mode
    if (!inPipMode) {
        Text(
            text = "Picture in Picture",
        )
    }
    VideoPlayer()
}
```

<br />