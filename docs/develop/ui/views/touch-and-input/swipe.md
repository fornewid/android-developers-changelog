---
title: https://developer.android.com/develop/ui/views/touch-and-input/swipe
url: https://developer.android.com/develop/ui/views/touch-and-input/swipe
source: md.txt
---

# About swipe-to-refresh

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to pull to refresh in Compose.  
[Pull to refresh in Compose →](https://developer.android.com/develop/ui/compose/components/pull-to-refresh)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)  
**Figure 1.**A swipe-to-refresh action updating a weather app.

Even if your app automatically updates its content on a regular basis, you can also let users request manual updates. For example, a weather forecasting app can let users refresh the app to get the latest forecasts on demand. To provide a standard user experience for requesting updates, the Android platform includes the swipe-to-refresh design pattern, which lets users trigger an update with a vertical swipe.

Download the sample apps:

- [SwipeRefreshLayoutBasic](https://github.com/android/views-widgets-samples/tree/main/SwipeRefreshLayoutBasic)
- [SwipeRefreshMultipleViews](https://github.com/android/views-widgets-samples/tree/main/SwipeRefreshMultipleViews/)

## Lessons

**[Add swipe-to-refresh to your app](https://developer.android.com/develop/ui/views/touch-and-input/swipe/add-swipe-interface)**
:   Learn how to provide swipe-to-refresh support in a[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)and how to provide a more accessible refresh option using the action bar.

**[Respond to a refresh request](https://developer.android.com/develop/ui/views/touch-and-input/swipe/respond-refresh-request)**
:   Learn how to respond to the swipe-to-refresh gesture and how to perform the same update from an action bar refresh action.