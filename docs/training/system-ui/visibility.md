---
title: Respond to UI visibility changes  |  Android Developers
url: https://developer.android.com/training/system-ui/visibility
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Respond to UI visibility changes Stay organized with collections Save and categorize content based on your preferences.



This lesson describes how to register a listener so that your app can get notified
of system UI visibility changes. This is useful if you want to
synchronize other parts of your UI with the hiding/showing of system bars.

## Register a Listener

To get notified of system UI visibility changes, register an
`View.OnSystemUiVisibilityChangeListener` to your view.
This is typically the view you are using to control the navigation visibility.

For example, you could add this code to your activity's
`onCreate()` method:

### Kotlin

```
window.decorView.setOnSystemUiVisibilityChangeListener { visibility ->
    // Note that system bars will only be "visible" if none of the
    // LOW_PROFILE, HIDE_NAVIGATION, or FULLSCREEN flags are set.
    if (visibility and View.SYSTEM_UI_FLAG_FULLSCREEN == 0) {
        // TODO: The system bars are visible. Make any desired
        // adjustments to your UI, such as showing the action bar or
        // other navigational controls.
    } else {
        // TODO: The system bars are NOT visible. Make any desired
        // adjustments to your UI, such as hiding the action bar or
        // other navigational controls.
    }
}
```

### Java

```
View decorView = getWindow().getDecorView();
decorView.setOnSystemUiVisibilityChangeListener
        (new View.OnSystemUiVisibilityChangeListener() {
    @Override
    public void onSystemUiVisibilityChange(int visibility) {
        // Note that system bars will only be "visible" if none of the
        // LOW_PROFILE, HIDE_NAVIGATION, or FULLSCREEN flags are set.
        if ((visibility & View.SYSTEM_UI_FLAG_FULLSCREEN) == 0) {
            // TODO: The system bars are visible. Make any desired
            // adjustments to your UI, such as showing the action bar or
            // other navigational controls.
        } else {
            // TODO: The system bars are NOT visible. Make any desired
            // adjustments to your UI, such as hiding the action bar or
            // other navigational controls.
        }
    }
});
```

It's generally good practice to keep your UI in sync with changes in system bar
visibility. For example, you could use this listener to hide and show the action bar in
concert with the status bar hiding and showing.