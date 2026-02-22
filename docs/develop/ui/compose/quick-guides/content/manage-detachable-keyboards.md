---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-detachable-keyboards
url: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-detachable-keyboards
source: md.txt
---

<br />

The Android system triggers a configuration change every time a keyboard is
attached to or detached from a device. To provide a seamless user experience and
maximize user productivity on large screen devices with detachable keyboards,
your app needs to effectively manage keyboard configuration changes.

## Results

Your app responds to an external keyboard being attached or detached without
recreating the running activity.

## Version compatibility

Set your project's `minSDK` to API level 8 for this implementation (see
[`View#onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged)).

### Dependencies

None.

## Prevent activity recreation on keyboard change

To prevent your activity from being recreated when a detachable keyboard is
attached or detached, add keyboard-related values to the
[`configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config) attribute of your app manifest and
add a view to the activity's view hierarchy so your app can listen for
configuration changes.

### 1. Declare the `configChanges` attribute

Update the `<activity>` element in the app manifest by adding the
`keyboard|keyboardHidden` values to the list of already managed configuration
changes:  

    <activity
        ...
        android:configChanges="...|keyboard|keyboardHidden">

### 2. Add an empty view to the view hierarchy

Declare a new view and add your handler code inside the view's
`onConfigurationChanged()` method:  

### Kotlin

    val v = object : View(this) {
        override fun onConfigurationChanged(newConfig: Configuration?) {
            super.onConfigurationChanged(newConfig)
            // Handler code here.
        }
    }

### Java

    View v = new View(this) {
        @Override
        protected void onConfigurationChanged(Configuration newConfig) {
            super.onConfigurationChanged(newConfig);
            // Handler code here.
        }
    };

| **Note:** Compose-based hierarchies require the addition of a view because the view's configuration handler is the only method that is always called for configuration changes.

## Key points

- [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config): Attribute of the app manifest's `<activity>` element. Informs the system about configuration changes the app manages.
- [`View#onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/view/View#onconfigurationchanged) : Method that reacts to propagation of a new app configuration.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader
Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Optimize for large screens

Enable your app to support an optimized user experience on tablets, foldables, and ChromeOS devices.  
[Quick guide collection](https://developer.android.com/quick-guides/collections/optimize-for-large-screens)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)