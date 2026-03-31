---
title: Set up your app for PiP  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/pip-setup
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Set up your app for PiP Stay organized with collections Save and categorize content based on your preferences.



In the activity tag of your `AndroidManifest.xml` file, do the following:

1. Add `supportsPictureInPicture` and set it to `true` to declare you'll be
   using picture-in-picture (PiP) in your app.
2. Add `configChanges` and set it to
   `orientation|screenLayout|screenSize|smallestScreenSize` to specify that
   your activity handles layout configuration changes. This way, your activity
   doesn't relaunch when layout changes occur during PiP mode transitions.

```
<activity
    android:name=".SnippetsActivity"
    android:exported="true"
    android:supportsPictureInPicture="true"
    android:configChanges="orientation|screenLayout|screenSize|smallestScreenSize"
    android:theme="@style/Theme.Snippets">
```

**Note:** To learn more about configuration changes, how to restrict activity
recreation, and how to react to those configuration changes, see the [Handle
configuration changes](/guide/topics/resources/runtime-changes) page.

In your Compose code, do the following:

1. Add this extension on `Context`. You'll use this extension multiple times
   throughout the guide to access the activity.

   ```
   internal fun Context.findActivity(): ComponentActivity {
       var context = this
       while (context is ContextWrapper) {
           if (context is ComponentActivity) return context
           context = context.baseContext
       }
       throw IllegalStateException("Picture in picture should be called in the context of an Activity")
   }

   PictureInPictureSnippets.kt
   ```

## Add PiP on leave app for pre-Android 12

To add PiP for pre-Android 12, use [`addOnUserLeaveHintProvider`](/reference/androidx/core/app/OnUserLeaveHintProvider). Follow
these steps to add PiP for pre-Android 12:

1. Add a version gate so that this code is only accessed in versions O until R.
2. Use a `DisposableEffect` with `Context` as the key.
3. Inside the `DisposableEffect`, define the behavior for when the
   `onUserLeaveHintProvider` is triggered using a lambda. In the lambda, call
   [`enterPictureInPictureMode()`](/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) on `findActivity()` and pass in
   [`PictureInPictureParams.Builder().build()`](/reference/android/app/PictureInPictureParams.Builder).
4. Add `addOnUserLeaveHintListener` using `findActivity()` and pass in the
   lambda.
5. In `onDispose`, add `removeOnUserLeaveHintListener` using `findActivity()`
   and pass in the lambda.

```
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O &&
    Build.VERSION.SDK_INT < Build.VERSION_CODES.S
) {
    val context = LocalContext.current
    DisposableEffect(context) {
        val onUserLeaveBehavior = Runnable {
            context.findActivity()
                .enterPictureInPictureMode(PictureInPictureParams.Builder().build())
        }
        context.findActivity().addOnUserLeaveHintListener(
            onUserLeaveBehavior
        )
        onDispose {
            context.findActivity().removeOnUserLeaveHintListener(
                onUserLeaveBehavior
            )
        }
    }
} else {
    Log.i("PiP info", "API does not support PiP")
}

PictureInPictureSnippets.kt
```

## Add PiP on leave app for post-Android 12

Post-Android 12, the [`PictureInPictureParams.Builder`](/reference/android/app/PictureInPictureParams.Builder) is added through a
modifier that is passed to the app's video player.

1. Create a `modifier` and call [`onGloballyPositioned`](/reference/kotlin/androidx/compose/ui/layout/OnGloballyPositionedModifier) on it. The layout
   coordinates will be used in a later step.
2. Create a variable for the `PictureInPictureParams.Builder()`.
3. Add an `if` statement to check if the SDK is S or later. If so, add
   [`setAutoEnterEnabled`](/reference/android/app/PictureInPictureParams.Builder#setAutoEnterEnabled(boolean)) to the builder and set it to `true` to enter PiP
   mode upon swipe. This provides a smoother animation than going through
   [`enterPictureInPictureMode`](/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)).
4. Use `findActivity()` to call `setPictureInPictureParams()`. Call `build()`
   on the `builder` and pass it in.

```
val pipModifier = modifier.onGloballyPositioned { layoutCoordinates ->
    val builder = PictureInPictureParams.Builder()

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        builder.setAutoEnterEnabled(true)
    }
    context.findActivity().setPictureInPictureParams(builder.build())
}
VideoPlayer(pipModifier)

PictureInPictureSnippets.kt
```

## Use `setAspectRatio` to set PiP window's aspect ratio

To set the aspect ratio of the PiP window, you can either choose a specific
aspect ratio or use the width and height of the player's video size. If you are
using a media3 player, check that the player is not null and that the player's
video size is not equal to [`VideoSize.UNKNOWN`](/reference/androidx/media3/common/VideoSize#UNKNOWN) before setting the aspect
ratio.

```
val context = LocalContext.current

val pipModifier = modifier.onGloballyPositioned { layoutCoordinates ->
    val builder = PictureInPictureParams.Builder()
    if (shouldEnterPipMode && player != null && player.videoSize != VideoSize.UNKNOWN) {
        val sourceRect = layoutCoordinates.boundsInWindow().toAndroidRectF().toRect()
        builder.setSourceRectHint(sourceRect)
        builder.setAspectRatio(
            Rational(player.videoSize.width, player.videoSize.height)
        )
    }

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        builder.setAutoEnterEnabled(shouldEnterPipMode)
    }
    context.findActivity().setPictureInPictureParams(builder.build())
}

VideoPlayer(pipModifier)

PictureInPictureSnippets.kt
```

**Warning:** The bounds of what the aspect ratio can be are between 2.39:1 and
1:2.39 (inclusive). If your aspect ratio does not fall between these values,
your app will crash.

If you're using a custom player, set the aspect ratio on the player's height
and width using the syntax specific to your player. Be aware that if your player
resizes during initialization, if it falls outside of the valid bounds of what
the aspect ratio can be, your app will crash. You may need to add checks around
when the aspect ratio can be calculated, similar to how it is done for a media3
player.

[Previous

arrow\_back

About PiP](/develop/ui/compose/system/picture-in-picture)

[Next

Enter PiP at correct times

arrow\_forward](/develop/ui/compose/system/pip-enter)