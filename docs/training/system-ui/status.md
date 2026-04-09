---
title: Hide the status bar  |  Android Developers
url: https://developer.android.com/training/system-ui/status
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Hide the status bar Stay organized with collections Save and categorize content based on your preferences.



This lesson describes how to hide the status bar on different versions of
Android. Hiding the status bar (and optionally, the navigation bar) lets the
content use more of the display space, thereby providing a more immersive user experience.

Figure 1 shows an app with a visible status bar:

![system bars](/static/images/training/status_bar_show.png)

**Figure 1.** Visible status bar.

Figure 2 shows an app with a hidden status bar. Note that the action bar is hidden too.
You should never show the action bar without the status bar.

![system bars](/static/images/training/status_bar_hide.png)

**Figure 2.** Hidden status bar.

## Hide the Status Bar on Android 4.0 and Lower

You can hide the status bar on Android 4.0 (API level 14) and lower by setting
`WindowManager` flags. You can do this programmatically or by
setting an activity theme in your app's manifest file. Setting an activity theme in your app's
manifest file is the preferred approach if the status bar should always remain
hidden in your app (though strictly speaking, you could programmatically override the
theme if you wanted to). For example:

```
<application
    ...
    android:theme="@android:style/Theme.Holo.NoActionBar.Fullscreen" >
    ...
</application>
```

The advantages of using an activity theme are as follows:

* It's easier to maintain and less error-prone than setting a flag programmatically.
* It results in smoother UI transitions, because the system has the information it needs
  to render your UI before instantiating your app's main activity.

Alternatively, you can programmatically set `WindowManager` flags.
This approach makes it easier to hide and show the status bar as the user interacts with
your app:

### Kotlin

```
class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // If the Android version is lower than Jellybean, use this call to hide
        // the status bar.
        if (Build.VERSION.SDK_INT < 16) {
            window.setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN)
        }
        setContentView(R.layout.activity_main)
    }
    ...
}
```

### Java

```
public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // If the Android version is lower than Jellybean, use this call to hide
        // the status bar.
        if (Build.VERSION.SDK_INT < 16) {
            getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN);
        }
        setContentView(R.layout.activity_main);
    }
    ...
}
```

When you set `WindowManager` flags (whether through an activity theme or
programmatically), the flags remain in effect unless your app clears them.

You can use
`FLAG_LAYOUT_IN_SCREEN`
to set your activity layout to use the same screen area that's available when you've enabled
`FLAG_FULLSCREEN`. This prevents your
content from resizing when the status bar hides and shows.

## Hide the Status Bar on Android 4.1 and Higher

You can hide the status bar on Android 4.1 (API level 16) and higher by
using `setSystemUiVisibility()`.
`setSystemUiVisibility()` sets UI flags at
the individual view level; these settings are aggregated to the window level. Using
`setSystemUiVisibility()` to set UI flags
gives you more granular control over the system bars than using
`WindowManager` flags. This snippet hides the status bar:

### Kotlin

```
// Hide the status bar.
window.decorView.systemUiVisibility = View.SYSTEM_UI_FLAG_FULLSCREEN
// Remember that you should never show the action bar if the
// status bar is hidden, so hide that too if necessary.
actionBar?.hide()
```

### Java

```
View decorView = getWindow().getDecorView();
// Hide the status bar.
int uiOptions = View.SYSTEM_UI_FLAG_FULLSCREEN;
decorView.setSystemUiVisibility(uiOptions);
// Remember that you should never show the action bar if the
// status bar is hidden, so hide that too if necessary.
ActionBar actionBar = getActionBar();
actionBar.hide();
```

Note the following:

* Once UI flags have been cleared (for example, by navigating away from the
  activity), your app needs to reset them if you want to hide the bars again.
  See [Responding to UI Visibility Changes](/training/system-ui/visibility) for a
  discussion of how to listen for UI visibility changes so that your app can
  respond accordingly.
* Where you set the UI flags makes a difference. If you hide the system bars in your activity's
  `onCreate()` method and the user presses Home, the system bars will
  reappear. When the user reopens the activity, `onCreate()`
  won't get called, so the system bars will remain visible. If you want system UI changes to
  persist as the user navigates in and out of your activity, set UI flags in
  `onResume()`
  or `onWindowFocusChanged()`.
* The method `setSystemUiVisibility()`
  only has an effect if the view you call it from is visible.
* Navigating away from the view causes flags
  set with `setSystemUiVisibility()`
  to be cleared.

## Make Content Appear Behind the Status Bar

On Android 4.1 and higher, you can set your application's content to appear behind
the status bar, so that the content doesn't resize as the status bar hides and shows.
To do this, use
`SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN`.
You may also need to use
`SYSTEM_UI_FLAG_LAYOUT_STABLE` to help your app maintain a
stable layout.

When you use this approach, it becomes your responsibility to ensure that critical parts
of your app's UI (for example, the built-in controls in a Maps application) don't end up
getting covered by system bars. This could make your app unusable. In most cases you can
handle this by adding the `android:fitsSystemWindows` attribute to your XML layout file, set to
`true`. This adjusts the padding of the parent `ViewGroup`
to leave space for the system windows. This is sufficient for most applications.

In some cases, however, you may need to modify the default padding to get the desired
layout for your app. To directly manipulate how your
content lays out relative to the system bars (which occupy a space known as the window's
"content insets"), override `fitSystemWindows(Rect insets)`.
The `fitSystemWindows()` method is called by the
view hierarchy when the content insets for a window have changed, to allow the window to
adjust its content accordingly. By overriding this method you can handle the
insets (and hence your app's layout) however you want.