---
title: https://developer.android.com/training/tv/get-started/multitasking
url: https://developer.android.com/training/tv/get-started/multitasking
source: md.txt
---

Android 14 (API level 34) introduces some enhancements to the
[picture-in-picture](https://developer.android.com/guide/topics/ui/picture-in-picture) (PiP) APIs to allow for multitasking. While PiP
support was introduced in Android 8.0 (API level 26), it was not widely
supported on Android TV, and not supported at all on Google TV prior to Android
13. Multitasking for TV uses PiP mode to allow two
separate apps to coexist on the screen: one running in full
screen, with a second running in PiP mode. There are
different requirements for apps running in either of these modes.

The default behavior is that the PiP app overlays the full-screen app. This is
much the same as standard [Android picture-in-picture](https://developer.android.com/guide/topics/ui/picture-in-picture) behavior.

Note that when integrating multitasking, your application must declare its
[usage types](https://developer.android.com/training/tv/get-started/multitasking#usage-types) in
[accordance with the TV app quality guidelines](https://developer.android.com/docs/quality-guidelines/tv-app-quality#TV-IC).

## Run your app in PiP mode

For TV devices running Android 14 (API level 34) or higher, run your app in PiP
mode by calling [`enterPictureInPictureMode()`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)). TV devices running earlier
versions of Android don't support PiP mode.
| **Note:** There is a deprecated `enterPictureInPictureMode()` method for API level 26 and earlier that does not use `PictureInPictureParams.Builder`. Avoid using it, because it's not supported on TV devices.

Here is an example of how to implement the logic of a button to enter
PiP mode:  

### Kotlin

```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)
    pictureInPictureButton.visibility =
        if (requireActivity().packageManager.hasSystemFeature(FEATURE_PICTURE_IN_PICTURE)) {
            pictureInPictureButton.setOnClickListener {
                val aspectRatio = Rational(view.width, view.height)
                val params = PictureInPictureParams.Builder()
                    .setAspectRatio(aspectRatio)
                    .build()
                val result = requireActivity().enterPictureInPictureMode(params)
            }
            View.VISIBLE
        } else {
            View.GONE
        }
}
```

### Java

```java
@Override
public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
    super.onViewCreated(view, savedInstanceState);
    if (requireActivity().getPackageManager().hasSystemFeature(FEATURE_PICTURE_IN_PICTURE)) {
        pictureInPictureButton.setVisibility(View.VISIBLE);
        pictureInPictureButton.setOnClickListener(v -> {
            Rational aspectRatio = new Rational(view.getWidth(), view.getHeight());
            PictureInPictureParams params = new PictureInPictureParams.Builder()
                    .setAspectRatio(aspectRatio)
                    .setTitle("My Streaming App")
                    .setSubtitle("My On-Demand Content")
                    .build();
            Boolean result = requireActivity().enterPictureInPictureMode(params);
        });
    } else {
        pictureInPictureButton.setVisibility(View.GONE);
    }
}
```

The action is only added if the device has the system feature
[`FEATURE_PICTURE_IN_PICTURE`](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#feature_picture_in_picture). Also, when the action is triggered, the
aspect ratio of PiP mode is set to match the aspect ratio of the video being
played.

Be sure to add a [title](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setTitle(java.lang.CharSequence)) and [subtitle](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSubtitle(java.lang.CharSequence)) to give the user information
about what this PIP is generally being used for.
| **Note:** Entering picture-in picture mode requires explicit and intentional action by the user within the app. For details, see the [TV app quality guidelines](https://developer.android.com/docs/quality-guidelines/tv-app-quality#pip).

## Coexist with apps running in PiP mode

When your app is running as a fullscreen app it may need to adapt for other
apps running in PiP mode.

### Keep-clear APIs

In some cases, the PiP app may overlay important UI components within the
fullscreen app. To mitigate this, there are keep-clear APIs that apps can
use to identify critical UI components that shouldn't be overlaid. The system
attempts to honor the requests to avoid covering these components by
repositioning the PiP window.

![Keep-Clear](https://developer.android.com/static/training/tv/images/keep-clear.png)
| **Note:** The system might not honor these requests if too many UI components are marked as keep-clear, or if they take up large portions of the screen. Be mindful of this when using these APIs.

To specify that a view shouldn't be overlaid, use [`preferKeepClear`](https://developer.android.com/reference/android/R.attr#preferKeepClear) in your
XML layout as in the following example:  

    <TextView
        android:id="@+id/important_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:preferKeepClear="true"
        android:text="@string/app_name"/>

You can also do this programmatically using [`setPreferKeepClear()`](https://developer.android.com/reference/android/view/View#setPreferKeepClear(boolean)):  

### Kotlin

```kotlin
private lateinit var binding: MyLayoutBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    binding = MyLayoutBinding.inflate(layoutInflater)
    setContentView(binding.root)
    binding.importantText.isPreferKeepClear = true
}
```

### Java

```java
private MyLayoutBinding binding;

@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    binding = MyLayoutBinding.inflate(getLayoutInflater());
    setContentView(binding.getRoot());
    binding.importantText.setPreferKeepClear(true);
}
```

There may be times when you don't need to keep an entire [`View`](https://developer.android.com/reference/android/view/View) clear, but
only a section of it. The [`setPreferKeepClearRects()`](https://developer.android.com/reference/android/view/View#setPreferKeepClearRects(java.util.List%3Candroid.graphics.Rect%3E)) can be used to
specify regions of the `View` that shouldn't be overlaid. UIs that don't use
`View`s natively, such as Flutter, Jetpack Compose, and WebView, may have
sub-sections that need regions kept clear. This API can be used for those cases.
| **Note:** If you set [`setPreferKeepClear()`](https://developer.android.com/reference/android/view/View#setPreferKeepClear(boolean)) to `true`, the entire `View` is marked as keep clear, and any regions specified using [`setPreferKeepClearRects()`](https://developer.android.com/reference/android/view/View#setPreferKeepClearRects(java.util.List%3Candroid.graphics.Rect%3E)) are ignored.

## Usage types

Your app must declare a [meta-data value attribute](https://developer.android.com/guide/topics/manifest/meta-data-element) of
`com.google.android.tv.pip.category` that corresponds with the primary type or
types of usage for the picture-in-picture mode. Any `<activity>` that has set
`android:supportsPictureInPicture="true"` should declare this attribute with a
relevant value from the table below.

Usage types that don't fall into any of these categories, in particular any
playback of media content, are not allowed in picture-in-picture mode on TV.

| Value | Description |
|---|---|
| "`communication`" | Communications use cases, such as video or voice calls. |
| "`smartHome`" | Smart home integrations, such as connected doorbells or baby monitors. |
| "`health`" | Health use cases, such as fitness tracking or health monitoring. |
| "`ticker`" | Ticker use cases, such as live sports scores or news and stock tickers. |

Multiple values are separated by a vertical bar (`|`). For example:  

```xml
<meta-data android:name="com.google.android.tv.pip.category" android:value="smartHome|health" />
```

<br />