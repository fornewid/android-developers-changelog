---
title: https://developer.android.com/training/system-ui/dim
url: https://developer.android.com/training/system-ui/dim
source: md.txt
---

# Dim the system bars (deprecated)

| **Deprecated:** [setSystemUiVisibility](https://developer.android.com/reference/android/view/View#setSystemUiVisibility(int))is deprecated in API Level 30

This lesson describes how to dim the system bars (that is, the status and the navigation bars) on Android 4.0 (API level 14) and higher. Android does not provide a built-in way to dim the system bars on earlier versions.

When you use this approach, the content doesn't resize, but the icons in the system bars visually recede. As soon as the user touches either the status bar or the navigation bar area of the screen, both bars become fully visible. The advantage of this approach is that the bars are still present but their details are obscured, thus creating an immersive experience without sacrificing easy access to the bars.

## Dim the Status and Navigation Bars

You can dim the status and navigation bars using the[SYSTEM_UI_FLAG_LOW_PROFILE](https://developer.android.com/reference/android/view/View#SYSTEM_UI_FLAG_LOW_PROFILE)flag, as follows:  

### Kotlin

```kotlin
// This example uses decor view, but you can use any visible view.
activity?.window?.decorView?.apply {
    systemUiVisibility = View.SYSTEM_UI_FLAG_LOW_PROFILE
}
```

### Java

```java
// This example uses decor view, but you can use any visible view.
View decorView = getActivity().getWindow().getDecorView();
int uiOptions = View.SYSTEM_UI_FLAG_LOW_PROFILE;
decorView.setSystemUiVisibility(uiOptions);
```

As soon as the user touches the status or navigation bar, the flag is cleared, causing the bars to be undimmed. Once the flag has been cleared, your app needs to reset it if you want to dim the bars again.

Figure 1 shows a gallery image in which the navigation bar is dimmed (note that the Gallery app completely hides the status bar; it doesn't dim it). Notice that the navigation bar (right side of the image) has faint white dots on it to represent the navigation controls:

![system bars](https://developer.android.com/static/images/training/low_profile_hide2x.png)

**Figure 1.**Dimmed system bars.

Figure 2 shows the same gallery image, but with the system bars displayed:

![system bars](https://developer.android.com/static/images/training/low_profile_show2x.png)

**Figure 2.**Visible system bars.

## Reveal the Status and Navigation Bars

If you want to programmatically clear flags set with[setSystemUiVisibility()](https://developer.android.com/reference/android/view/View#setSystemUiVisibility(int)), you can do so as follows:  

### Kotlin

```kotlin
activity?.window?.decorView?.apply {
    // Calling setSystemUiVisibility() with a value of 0 clears
    // all flags.
    systemUiVisibility = 0
}
```

### Java

```java
View decorView = getActivity().getWindow().getDecorView();
// Calling setSystemUiVisibility() with a value of 0 clears
// all flags.
decorView.setSystemUiVisibility(0);
```