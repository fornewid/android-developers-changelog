---
title: https://developer.android.com/training/wearables/views
url: https://developer.android.com/training/wearables/views
source: md.txt
---

Try the Compose way Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS. [Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose.md.txt) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)


[Android Jetpack](https://developer.android.com/jetpack/androidx.md.txt) includes the Wear OS UI Library.
The Wear OS UI library includes the following classes:

- `
  CurvedTextView`: a component for easily writing text that follows the curvature of the largest circle that can be inscribed in the view.
- `
  DismissibleFrameLayout`: a layout that lets the user dismiss any view by pressing the back button or swiping on the screen from left to right. Wear OS users expect left-to-right swiping for the back action.
- `
  WearableRecyclerView`: a view that provides basic offsetting logic for updating child layouts using a `
  WearableLinearLayoutManager`.
- `
  AmbientLifecycleObserver`: an interface used with the `
  AmbientLifecycleObserver.AmbientLifecycleCallback` interface to provide lifecycle-aware support for ambient mode.


For a full list, read the [release notes](https://developer.android.com/jetpack/androidx/releases/wear.md.txt).

## Add a dependency on the Wear OS UI Library


To start creating apps, create a Wear-OS-specific project. Then add the following dependencies
to your app's `build.gradle` file:

```groovy
dependencies {
    ...
  // Standard Wear OS libraries
  implementation "androidx.wear:wear:1.4.0"
  // includes support for wearable specific inputs
  implementation "androidx.wear:wear-input:1.1.0"
}
```

## Import classes from the Wear OS UI Library package


To use UI components from the Wear OS UI Library, import them from the
`androidx.wear.widget` package, or from
`androidx.wear.ambient` for ambient mode support.

## Use the right element names in layout files


In layout files, use fully qualified names that correspond to the Wear OS UI
Library.


For example, to use the
`
DismissibleFrameLayout` class from the Wear OS UI Library, you could specify
the following in a layout file:

```xml
<androidx.wear.widget.DismissibleFrameLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:id="@+id/swipe_dismiss_root" >

    <TextView
        android:id="@+id/test_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:text="Swipe the screen to dismiss me." />
</androidx.wear.widget.DismissibleFrameLayout>
```