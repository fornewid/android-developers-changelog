---
title: Add PiP through a button  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/pip-add
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Add PiP through a button Stay organized with collections Save and categorize content based on your preferences.




To enter PiP mode through a button click, call
[`enterPictureInPictureMode()`](/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) on `findActivity()`.

The parameters are already set by previous calls to the
[`PictureInPictureParams.Builder`](/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)), so you do not need to set new parameters
on the builder. However, if you do want to change any parameters on button
click, you can set them here.

```
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

PictureInPictureSnippets.kt
```

[Previous

arrow\_back

Enter PiP at correct times](/develop/ui/compose/system/pip-enter)

[Next

Add remote actions to PiP

arrow\_forward](/develop/ui/compose/system/pip-remote-actions)