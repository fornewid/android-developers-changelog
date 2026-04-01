---
title: https://developer.android.com/develop/ui/compose/system/pip-add
url: https://developer.android.com/develop/ui/compose/system/pip-add
source: md.txt
---

To enter PiP mode through a button click, call
[`enterPictureInPictureMode()`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) on `findActivity()`.

The parameters are already set by previous calls to the
[`PictureInPictureParams.Builder`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)), so you do not need to set new parameters
on the builder. However, if you do want to change any parameters on button
click, you can set them here.


```kotlin
val context = LocalContext.current
Button(onClick = {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        context.findActivity().enterPictureInPictureMode(
            PictureInPictureParams.Builder().build()
        )
    } else {
        Log.i(PIP_TAG, "API does not support PiP")
    }
}) {
    Text(text = "Enter PiP mode!")
}
```

<br />