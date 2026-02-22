---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-webview-state
url: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-webview-state
source: md.txt
---

# Manage WebView state

<br />

[`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView)is a commonly used component that offers an advanced system for state management. A`WebView`must maintain its state and scroll position across configuration changes. A`WebView`can lose scroll position when the user rotates the device or unfolds a foldable phone, which forces the user to scroll again from the top of the`WebView`to the previous scroll position.

`WebView`is good at managing its state. You can take advantage of this quality by managing as many configuration changes as possible to minimize the number of times a`WebView`is recreated. Your app should handle configuration changes because activity recreation (the system's way of handling configuration changes) recreates the`WebView`, which causes the`WebView`to lose state.

## Results

Your app's`WebView`components retain their state and scroll position across multiple configuration changes, from resizing to orientation changes to device folding and unfolding.

## Version compatibility

This implementation is compatible with all API levels.

### Dependencies

None.

## Manage state

Avoid activity recreation as much as possible during configuration changes, and let the`WebView`invalidate so it can resize while retaining its state.

To manage`WebView`state:

- Declare configuration changes handled by your app
- Invalidate the`WebView`state

### 1. Add configuration changes to your app's`AndroidManifest.xml`file

Avoid activity recreation by specifying the configuration changes handled by your app (rather than by the system):  

    <activity
      android:name=".MyActivity"
      android:configChanges="screenLayout|orientation|screenSize
          |keyboard|keyboardHidden|smallestScreenSize" />

| **Note:** While this nonexhaustive list of configuration changes might be okay for many applications, make sure to manage the configuration changes that make the most sense for your case based on how your users interact with the app, for how long, and when. To find the best combination of configurations for your app, see[`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config).

### 2. Invalidate`WebView`whenever your app receives a configuration change

### Kotlin

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        webView.invalidate()
    }

### Java

    @Override
    public void onConfigurationChanged(@NonNull Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        webview.invalidate();
    }

This step applies only to the view system, as Jetpack Compose does not need to invalidate anything to resize[`Composable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable)elements correctly. However, Compose recreates a`WebView`often if not managed correctly.

## Key points

- [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config): Attribute of the manifest`<activity>`element. Lists the configuration changes handled by the activity.
- [`View#invalidate()`](https://developer.android.com/reference/kotlin/android/view/View#invalidate_2): Method that causes a view to be redrawn. Inherited by`WebView`.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Optimize for large screens

Enable your app to support an optimized user experience on tablets, foldables, and ChromeOS devices.  
[Quick guide collection](https://developer.android.com/quick-guides/collections/optimize-for-large-screens)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq)[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)