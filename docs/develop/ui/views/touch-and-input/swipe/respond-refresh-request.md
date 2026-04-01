---
title: https://developer.android.com/develop/ui/views/touch-and-input/swipe/respond-refresh-request
url: https://developer.android.com/develop/ui/views/touch-and-input/swipe/respond-refresh-request
source: md.txt
---

# Respond to a refresh request

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to pull to refresh in Compose.  
[Pull to refresh in Compose →](https://developer.android.com/develop/ui/compose/components/pull-to-refresh)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

This document shows how to update your app when the user requests a manual refresh, whether they trigger it with a swipe gesture or use the action bar refresh action.

## Respond to the refresh gesture

When the user makes the swipe-to-refresh gesture, the system displays the progress indicator and calls your app's callback method. Your callback method is responsible for updating the app's data.

To respond to the refresh gesture in your app, implement the[SwipeRefreshLayout.OnRefreshListener](https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout.OnRefreshListener)interface and its[onRefresh()](https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout.OnRefreshListener#onRefresh())method. The`onRefresh()`method is invoked when the user performs a swipe gesture.

Put the code for the actual update operation in a separate method, preferably in a`ViewModel`, and call that update method from your`onRefresh()`implementation. That way, you can use the same update method to perform the update when the user triggers a refresh from the action bar.

In your update method, call[setRefreshing(false)](https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout#setRefreshing(boolean))when it finishes updating the data. Calling this method instructs the[SwipeRefreshLayout](https://developer.android.com/reference/androidx/swiperefreshlayout/widget/SwipeRefreshLayout)to remove the progress indicator and update the view contents.

For example, the following code implements`onRefresh()`and invokes the method`myUpdateOperation()`to update the data displayed by a[ListView](https://developer.android.com/reference/android/widget/ListView):  

### Kotlin

```kotlin
// Sets up a SwipeRefreshLayout.OnRefreshListener that invokes when
// the user performs a swipe-to-refresh gesture.

mySwipeRefreshLayout.setOnRefreshListener {
    Log.i(LOG_TAG, "onRefresh called from SwipeRefreshLayout")

    // This method performs the actual data-refresh operation and calls
    // setRefreshing(false) when it finishes.
    myUpdateOperation()
}
```

### Java

```java
// Sets up a SwipeRefreshLayout.OnRefreshListener that is invoked when
// the user performs a swipe-to-refresh gesture.

mySwipeRefreshLayout.setOnRefreshListener(() -> {
    Log.i(LOG_TAG, "onRefresh called from SwipeRefreshLayout");

    // This method performs the actual data-refresh operation and calls
    // setRefreshing(false) when it finishes.
    myUpdateOperation();
  }
);
```

## Respond to the refresh action

If the user requests a refresh by using the action bar, the system calls the[onOptionsItemSelected()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onOptionsItemSelected(android.view.MenuItem))method. Your app responds to this call by displaying the progress indicator and refreshing the app's data.

To respond to the refresh action, override`onOptionsItemSelected()`. In your override method, trigger the`SwipeRefreshLayout`progress indicator by calling`setRefreshing()`with the value`true`, then perform the update operation. Perform the actual update in a separate method, so the same method can be called whether the user triggers the update with a swipe or uses the action bar. When the update finishes, call`setRefreshing(false)`to remove the refresh progress indicator.

The following code shows how to respond to the request action:  

### Kotlin

```kotlin
// Listen for option item selections to receive a notification when the user
// requests a refresh by selecting the refresh action bar item.

override fun onOptionsItemSelected(item: MenuItem): Boolean {
    when (item.itemId) {

        // Check whether the user triggers a refresh:
        R.id.menu_refresh -> {
            Log.i(LOG_TAG, "Refresh menu item selected")

            // Signal SwipeRefreshLayout to start the progress indicator.
            mySwipeRefreshLayout.isRefreshing = true

            // Start the refresh background task. This method calls
            // setRefreshing(false) when it finishes.
            myUpdateOperation()

            return true
        }
    }

    // User doesn't trigger a refresh. Let the superclass handle this action.
    return super.onOptionsItemSelected(item)
}
```

### Java

```java
// Listen for option item selections to receive a notification when the user
// requests a refresh by selecting the refresh action bar item.

@Override
public boolean onOptionsItemSelected(MenuItem item) {
    switch (item.getItemId()) {

        // Check whether the user triggers a refresh:
        case R.id.menu_refresh:
            Log.i(LOG_TAG, "Refresh menu item selected");

            // Signal SwipeRefreshLayout to start the progress indicator.
            mySwipeRefreshLayout.setRefreshing(true);

            // Start the refresh background task. This method calls
            // setRefreshing(false) when it finishes.
            myUpdateOperation();

            return true;
    }

    // User doesn't trigger a refresh. Let the superclass handle this action.
    return super.onOptionsItemSelected(item);
}
```