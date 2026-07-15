---
title: https://developer.android.com/develop/adaptive-apps/cookbook/webview-state
url: https://developer.android.com/develop/adaptive-apps/cookbook/webview-state
source: md.txt
---

![Three star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/three-star-rating.png)

[`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView) is a commonly used component that offers an advanced system for
state management. A `WebView` must maintain its state and scroll position across
configuration changes. A `WebView` can lose scroll position when the user
rotates the device or unfolds a foldable phone, which forces the user to scroll
again from the top of the `WebView` to the previous scroll position.

## Best practices

Minimize the number of times a `WebView` is recreated. `WebView` is good at
managing its state, and you can leverage this quality by managing as many
configuration changes as possible. Your app must handle configuration changes
because `Activity` recreation (the system's way of handling configuration
changes) recreates the `WebView` as well, which causes the `WebView` to lose its
state.

## Ingredients

- [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config): Attribute of the manifest `<activity>` element. Lists the configuration changes handled by the activity.
- [`View#invalidate()`](https://developer.android.com/reference/kotlin/android/view/View#invalidate_2): Method that causes a view to be redrawn. Inherited by `WebView`.

## Steps

To save the `WebView` state, avoid [`Activity`](https://developer.android.com/reference/kotlin/android/app/Activity) recreation as much as
possible, and then let the `WebView` invalidate so that it can resize while
retaining its state.

### 1. Add configuration changes to `AndroidManifest.xml`

Avoid activity recreation by specifying the configuration changes handled by
your app (rather than by the system):

    <activity
      android:name=".MyActivity"
      android:configChanges="screenLayout|orientation|screenSize
          |keyboard|keyboardHidden|smallestScreenSize" />

> [!NOTE]
> **Note:** While this non-exhaustive list of configuration changes might be okay for many applications, make sure to manage the configuration changes that make the most sense for your case, based on how your users would interact with the app, for how long, and when. To find the best combination of configurations for your app see [`android:configChanges`](https://developer.android.com/guide/topics/manifest/activity-element#config).

### 2. Invalidate `WebView` on configuration changes

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

This step applies only to the view system, as Jetpack Compose does not need to
invalidate anything to resize [`Composable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable) elements correctly. However,
Compose recreates a `WebView` often if not managed correctly. Use the
[Accompanist WebView](https://google.github.io/accompanist/web/) wrapper to save and restore `WebView` state
in your Compose apps.

## Results

Your app's `WebView` components now retain their state and scroll position
across multiple configuration changes, from resizing to orientation change to
folding and unfolding.

## Additional resources

To learn more about configuration changes and how to manage them, see [Handle
configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).