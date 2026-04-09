---
title: Hide the navigation bar  |  Android Developers
url: https://developer.android.com/training/system-ui/navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Hide the navigation bar Stay organized with collections Save and categorize content based on your preferences.



This lesson describes how to hide the navigation bar, which was introduced in
Android 4.0 (API level 14).

Even though this lesson focuses on hiding the
navigation bar, you should design your app to hide the status bar
at the same time, as described in [Hiding the Status Bar](/training/system-ui/status).
Hiding the navigation and status bars (while still keeping them readily accessible)
lets the content use the entire display space, thereby providing a more immersive
user experience.

![system bars](/static/images/training/navigation-bar.png)

**Figure 1.** Navigation bar.

## Hide the Navigation Bar

You can hide the navigation bar using the
`SYSTEM_UI_FLAG_HIDE_NAVIGATION` flag. This snippet hides both
the navigation bar and the status bar:

### Kotlin

```
window.decorView.apply {
    // Hide both the navigation bar and the status bar.
    // SYSTEM_UI_FLAG_FULLSCREEN is only available on Android 4.1 and higher, but as
    // a general rule, you should design your app to hide the status bar whenever you
    // hide the navigation bar.
    systemUiVisibility = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION or View.SYSTEM_UI_FLAG_FULLSCREEN
}
```

### Java

```
View decorView = getWindow().getDecorView();
// Hide both the navigation bar and the status bar.
// SYSTEM_UI_FLAG_FULLSCREEN is only available on Android 4.1 and higher, but as
// a general rule, you should design your app to hide the status bar whenever you
// hide the navigation bar.
int uiOptions = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
              | View.SYSTEM_UI_FLAG_FULLSCREEN;
decorView.setSystemUiVisibility(uiOptions);
```

Note the following:

* With this approach, touching anywhere on the screen causes the navigation bar (and
  status bar) to reappear and remain visible. The user interaction causes the flags to be
  be cleared.
* Once the flags have been cleared, your app needs to reset them if you
  want to hide the bars again. See [Responding to UI Visibility Changes](/training/system-ui/visibility) for a
  discussion of how to listen for UI visibility changes so that your app can
  respond accordingly.
* Where you set the UI flags makes a difference. If you hide the system bars in your activity's
  `onCreate()` method and the user presses Home, the system bars will
  reappear. When the user reopens the activity, `onCreate()`
  won't get called, so the system bars will remain visible. If you want system UI changes to
  persist as the user navigates in and out of your activity, set UI flags in
  `onResume()`
  or `onWindowFocusChanged()`.
* The method `setSystemUiVisibility()` only
  has an effect if the view you call it from is visible.
* Navigating away from the view causes flags
  set with `setSystemUiVisibility()`
  to be cleared.

## Make Content Appear Behind the Navigation Bar

On Android 4.1 and higher, you can set your application's content to appear behind
the navigation bar, so that the content doesn't resize as the navigation bar hides and
shows. To do this, use
`SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION`.
You may also need to use
`SYSTEM_UI_FLAG_LAYOUT_STABLE` to help your app maintain a
stable layout.

When you use this approach, it becomes your responsibility to ensure that critical parts
of your app's UI don't end up getting covered by system bars. For more
discussion of this topic, see the [Hiding the Status Bar](/training/system-ui/status#behind) lesson.