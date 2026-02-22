---
title: https://developer.android.com/training/wearables/views
url: https://developer.android.com/training/wearables/views
source: md.txt
---

# Build View-based UIs on Wear OS

Try the Compose way  
Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.  
[Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

[Android Jetpack](https://developer.android.com/jetpack/androidx)includes the Wear OS UI Library. The Wear OS UI library includes the following classes:

- [CurvedTextView](https://developer.android.com/reference/kotlin/androidx/wear/widget/CurvedTextView): a component for easily writing text that follows the curvature of the largest circle that can be inscribed in the view.
- [DismissibleFrameLayout](https://developer.android.com/reference/androidx/wear/widget/DismissibleFrameLayout): a layout that lets the user dismiss any view by pressing the back button or swiping on the screen from left to right. Wear OS users expect left-to-right swiping for the back action.
- [WearableRecyclerView](https://developer.android.com/reference/androidx/wear/widget/WearableRecyclerView): a view that provides basic offsetting logic for updating child layouts using a[WearableLinearLayoutManager](https://developer.android.com/reference/androidx/wear/widget/WearableLinearLayoutManager).
- [AmbientModeSupport](https://developer.android.com/reference/androidx/wear/ambient/AmbientModeSupport): a class used with the[AmbientModeSupport.AmbientCallbackProvider](https://developer.android.com/reference/androidx/wear/ambient/AmbientModeSupport.AmbientCallbackProvider)interface to provide support for ambient mode.

For a full list, read the[release notes](https://developer.android.com/jetpack/androidx/releases/wear).

## Add a dependency on the Wear OS UI Library

To start creating apps, create a Wear-OS-specific project. Then add the following dependencies to your app's`build.gradle`file:  

```groovy
dependencies {
    ...
  // Standard Wear OS libraries
  implementation "androidx.wear:wear:1.2.0"
  // includes support for wearable specific inputs
  implementation "androidx.wear:wear-input:1.1.0"
}
```

## Import classes from the Wear OS UI Library package

To use a class from the Wear OS UI Library, import it from the`androidx.wear.widget`package.

## Use the right element names in layout files

In layout files, use fully qualified names that correspond to the Wear OS UI Library.

For example, to use the[DismissibleFrameLayout](https://developer.android.com/reference/androidx/wear/widget/DismissibleFrameLayout)class from the Wear OS UI Library, you could specify the following in a layout file:  

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