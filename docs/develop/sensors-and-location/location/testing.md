---
title: https://developer.android.com/develop/sensors-and-location/location/testing
url: https://developer.android.com/develop/sensors-and-location/location/testing
source: md.txt
---

# Test your app&#39;s location workflows

The guidelines on this page help you evaluate your app as you make updates to support the latest location features and behavior.

## Test how your app handles approximate location

To evaluate whether you need to update your app to support user-configurable location accuracy, complete the tests described in this section.

### Handle approximate location request from dialog

To check how your app handles a user's request for your app to have approximate location access from the dialog, do the following:

1. Request both`ACCESS_FINE_LOCATION`and`ACCESS_COARSE_LOCATION`.
2. In the dialog that appears, where the user can[request approximate location](https://developer.android.com/training/location/permissions#approximate-request), select**Approximate** near the top, and either**While using the app** or**Only this time**near the bottom.
3. Check whether your app's use cases still work as expected, even when your app only has approximate location access.

### Handle approximate location downgrade from system settings

![](https://developer.android.com/static/images/training/location/approximate-settings.svg)**Figure 1.** An app's location permissions screen in system settings includes**Use precise location**. This option is independent from the location access settings that appear closer to the top of the screen.

To check how your app handles a user's request to change your app's location access from precise to approximate in system settings, do the following:

1. Request both`ACCESS_FINE_LOCATION`and`ACCESS_COARSE_LOCATION`.
2. In the dialog that appears, where the user can[request approximate location](https://developer.android.com/training/location/permissions#approximate-request), select**Precise** near the top, and either**While using the app** or**Only this time**near the bottom.
3. Navigate to your app's permissions screen in system settings.
4. On the location permission screen, turn off**Use precise location** . This option appears infigure 1.

   As with any permission downgrade, the system restarts your app's process.
5. Check whether your app's use cases still work as expected, even when your app only has approximate location access.

### Handle precise location upgrade from system settings

To check how your app handles a user's request to change your app's location access from approximate to precise in system settings, do the following:

1. Request both`ACCESS_FINE_LOCATION`and`ACCESS_COARSE_LOCATION`.
2. In the dialog that appears, where the user can[request approximate location](https://developer.android.com/training/location/permissions#approximate-request), select**Approximate** near the top, and either**While using the app** or**Only this time**near the bottom.
3. Navigate to your app's permissions screen in system settings.
4. On the location permission screen, turn on**Use precise location** , as shown infigure 1.

   Because this permission change is an*upgrade*, the system doesn't restart your app.
5. Check whether your app receives more accurate location data in its location-based use cases.