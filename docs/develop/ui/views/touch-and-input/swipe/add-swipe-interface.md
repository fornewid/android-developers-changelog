---
title: https://developer.android.com/develop/ui/views/touch-and-input/swipe/add-swipe-interface
url: https://developer.android.com/develop/ui/views/touch-and-input/swipe/add-swipe-interface
source: md.txt
---

# Add swipe-to-refresh to your app

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to pull to refresh in Compose.  
[Pull to refresh in Compose →](https://developer.android.com/develop/ui/compose/components/pull-to-refresh)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The swipe-to-refresh user interface pattern is implemented entirely within the[SwipeRefreshLayout](https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout)widget, which detects the vertical swipe, displays a distinctive progress bar, and triggers callback methods in your app. Enable this behavior by adding the widget to your layout file as the parent of a[ListView](https://developer.android.com/reference/android/widget/ListView)or[GridView](https://developer.android.com/reference/android/widget/GridView)and implementing the refresh behavior that is invoked when the user swipes.

This page shows how to add the widget to an existing layout. It also shows how to add a refresh action to the action bar overflow area so that users who can't use the swipe gesture can trigger a manual update with an external device.

## Add SwipeRefreshLayout dependency

To use`SwipeRefreshLayout`in your app, add the following dependency to your`build.gradle`file:  

### Groovy

```groovy
dependencies {
    implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.swiperefreshlayout:swiperefreshlayout:1.2.0-alpha01")
}
```

## Add the SwipeRefreshLayout Widget

To add the swipe-to-refresh widget to an existing app, add`SwipeRefreshLayout`as the parent of a single`ListView`or`GridView`.`SwipeRefreshLayout`only supports a single`ListView`or`GridView`child.

The following example demonstrates how to add the`SwipeRefreshLayout`widget to an existing layout file containing a`ListView`:  

```xml
<androidx.swiperefreshlayout.widget.SwipeRefreshLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/swiperefresh"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ListView
        android:id="@android:id/list"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</androidx.swiperefreshlayout.widget.SwipeRefreshLayout>
```

You can also use the`SwipeRefreshLayout`widget with a[ListFragment](https://developer.android.com/reference/androidx/fragment/app/ListFragment). If the layout contains a`ListView`with the ID`"@android:id/list"`, the swipe-to-refresh functionality is automatically supported. However, explicitly declaring the`ListView`this way supersedes the default`ListFragment`view structure. If you want to use the default view structure, override parts of the`SwipeRefreshLayout`and`ListFragment`behavior.

## Add a refresh action to the action bar

Add a refresh action to your app's action bar so users who can't perform swipe gestures can trigger a manual update. For example, users with accessibility needs can trigger action bar actions using external devices, such as keyboards and D-pads.

Add the refresh action as a menu item, rather than as a button, by setting the attribute`android:showAsAction=never`. If you display the action as a button, users might assume the refresh button action is different from the swipe-to-refresh action. Making the refresh action less conspicuous in the action bar encourages users to perform manual updates with swipe gestures while maintaining the accessible option where D-pad users look for it.

The following code demonstrates how to add the swipe-to-refresh action to the overflow area:  

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android" >
    <item
        android:id="@+id/menu_refresh"
        android:showAsAction="never"
        android:title="@string/menu_refresh"/>
</menu>
```