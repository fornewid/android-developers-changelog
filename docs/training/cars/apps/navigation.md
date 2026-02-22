---
title: https://developer.android.com/training/cars/apps/navigation
url: https://developer.android.com/training/cars/apps/navigation
source: md.txt
---

# Build a navigation app

This page details the different features of the Car App Library that you can use to implement the functionality of your turn-by-turn navigation app.
| **Design guidelines:** Refer to[Navigation apps](https://developers.google.com/cars/design/create-apps/app-types/navigation)for UX guidance specific to navigation apps.

## Declare navigation support in your manifest

Your navigation app needs to declare the`androidx.car.app.category.NAVIGATION`[car app category](https://developer.android.com/training/cars/apps#supported-app-categories)in the intent filter of its[`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService):  

    <application>
        ...
       <service
           ...
            android:name=".MyNavigationCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.NAVIGATION"/>
          </intent-filter>
        </service>
        ...
    </application>

| **Important:** Navigation apps built for Android Automotive OS require additional declarations in the manifest, as described in[Additional requirements for navigation apps](https://developer.android.com/training/cars/apps/automotive-os#navigation-reqs).

## Support navigation intents

A variety of intent formats enable navigation apps to work with other apps, such as point of interest apps and voice assistants.

To support these intent formats, first declare support by adding intent filters in your app's manifest. The location of these intent filters depends on the platform:

- **Android Auto** : Within the`<activity>`manifest element for the`Activity`used to handle the intent when a user isn't using Android Auto.
- **Android Automotive OS** : Within the`<activity>`manifest element for the`CarAppActivity`.

Then, read and handle the intents in both the[`onCreateScreen()`](https://developer.android.com/reference/androidx/car/app/Session#onCreateScreen(android.content.Intent))and[`onNewIntent()`](https://developer.android.com/reference/androidx/car/app/Session#onNewIntent(android.content.Intent))callbacks in your app's`Session`implementation.

### Required intent formats

To meet the[`NF-6`](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=navigation#NF-6)quality requirement, your app must handle[navigation intents](https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app#navigation-intent).

### Optional intent formats

You can also support the following intent formats to further increase your app's interoperability:

- [Search intent](https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app#search-intent)
- [Custom action intent](https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app#custom-action-intent)

## Access the navigation templates

Navigation apps can access the following templates, which display a surface in the background with the map and, during active navigation, turn-by-turn directions.

- [`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate): also displays an optional informational message and travel estimates during active navigation.
- [`MapWithContentTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapWithContentTemplate): A template that allows an app to render map tiles with some sort of content (for example, a list). The content is usually rendered as an overlay on top of the map tiles, with the map visible and stable areas adjusting to the content.

For more details about how to design your navigation app's user interface using these templates, see[Navigation apps](https://developers.google.com/cars/design/create-apps/app-types/navigation).

To get access to the navigation templates, your app needs to declare the`androidx.car.app.NAVIGATION_TEMPLATES`permission in its`AndroidManifest.xml`file:  

    <manifest ...>
      ...
      <uses-permission android:name="androidx.car.app.NAVIGATION_TEMPLATES"/>
      ...
    </manifest>

An additional permission is required to[draw maps](https://developer.android.com/training/cars/apps#draw-maps).
| **Note:** The`NavigationTemplate`(as well as the deprecated`MapTemplate`,`PlaceListNavigationTemplate`, and`RoutePreviewNavigationTemplate`) can only be used by apps declaring the`androidx.car.app.category.NAVIGATION`[car app category](https://developer.android.com/training/cars/apps#supported-app-categories). Only declare the`NAVIGATION_TEMPLATES`permission for navigation apps. For point of interest (POI) apps, see "Access the map templates" in[Build a point of interest app](https://developer.android.com/training/cars/apps/poi#access-map-templates).

### Migrate to the MapWithContentTemplate

Starting with Car App API Level 7, the[`MapTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapTemplate),[`PlaceListNavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/PlaceListNavigationTemplate), and[`RoutePreviewNavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/RoutePreviewNavigationTemplate)are deprecated. Deprecated templates will continue to be supported, but migrating to the`MapWithContentTemplate`is strongly recommended.

The functionality provided by these templates can be implemented using the`MapWithContentTemplate`. See the following snippets for examples:  

#### MapTemplate

### Kotlin

```kotlin
// MapTemplate (deprecated)
val template = MapTemplate.Builder()
    .setPane(paneBuilder.build())
    .setActionStrip(actionStrip)
    .setHeader(header)
    .setMapController(mapController)
    .build()

// MapWithContentTemplate
val template = MapWithContentTemplate.Builder()
    .setContentTemplate(
        PaneTemplate.Builder(paneBuilder.build())
            .setHeader(header)
            .build())
    .setActionStrip(actionStrip)
    .setMapController(mapController)
    .build()
```

### Java

```java
// MapTemplate (deprecated)
MapTemplate template = new MapTemplate.Builder()
    .setPane(paneBuilder.build())
    .setActionStrip(actionStrip)
    .setHeader(header)
    .setMapController(mapController)
    .build();

// MapWithContentTemplate
MapWithContentTemplate template = new MapWithContentTemplate.Builder()
    .setContentTemplate(new PaneTemplate.Builder(paneBuilder.build())
        .setHeader(header)
        build())
    .setActionStrip(actionStrip)
    .setMapController(mapController)
    .build();
```  

#### PlaceListNavigationTemplate

### Kotlin

```kotlin
// PlaceListNavigationTemplate (deprecated)
val template = PlaceListNavigationTemplate.Builder()
    .setItemList(itemListBuilder.build())
    .setHeader(header)
    .setActionStrip(actionStrip)
    .setMapActionStrip(mapActionStrip)
    .build()

// MapWithContentTemplate
val template = MapWithContentTemplate.Builder()
    .setContentTemplate(
        ListTemplate.Builder()
            .setSingleList(itemListBuilder.build())
            .setHeader(header)
            .build())
    .setActionStrip(actionStrip)
    .setMapController(
        MapController.Builder()
            .setMapActionStrip(mapActionStrip)
            .build())
    .build()
```

### Java

```java
// PlaceListNavigationTemplate (deprecated)
PlaceListNavigationTemplate template = new PlaceListNavigationTemplate.Builder()
    .setItemList(itemListBuilder.build())
    .setHeader(header)
    .setActionStrip(actionStrip)
    .setMapActionStrip(mapActionStrip)
    .build();

// MapWithContentTemplate
MapWithContentTemplate template = new MapWithContentTemplate.Builder()
    .setContentTemplate(new ListTemplate.Builder()
        .setSingleList(itemListBuilder.build())
        .setHeader(header)
        .build())
    .setActionStrip(actionStrip)
    .setMapController(new MapController.Builder()
        .setMapActionStrip(mapActionStrip)
        .build())
    .build();
```  

#### RoutePreviewNavigationTemplate

### Kotlin

```kotlin
// RoutePreviewNavigationTemplate (deprecated)
val template = RoutePreviewNavigationTemplate.Builder()
    .setItemList(
        ItemList.Builder()
            .addItem(
                Row.Builder()
                    .setTitle(title)
                    .build())
            .build())
    .setHeader(header)
    .setNavigateAction(
        Action.Builder()
            .setTitle(actionTitle)
            .setOnClickListener { ... }
            .build())
    .setActionStrip(actionStrip)
    .setMapActionStrip(mapActionStrip)
    .build()

// MapWithContentTemplate
val template = MapWithContentTemplate.Builder()
    .setContentTemplate(
        ListTemplate.Builder()
            .setSingleList(
                ItemList.Builder()
                    .addItem(
                        Row.Builder()
                            .setTitle(title)
                            .addAction(
                                Action.Builder()
                                    .setTitle(actionTitle)
                                    .setOnClickListener { ... }
                                    .build())
                            .build())
                    .build())
            .setHeader(header)
            .build())
    .setActionStrip(actionStrip)
    .setMapController(
        MapController.Builder()
            .setMapActionStrip(mapActionStrip)
            .build())
    .build()
```

### Java

```java
// RoutePreviewNavigationTemplate (deprecated)
RoutePreviewNavigationTemplate template = new RoutePreviewNavigationTemplate.Builder()
    .setItemList(new ItemList.Builder()
        .addItem(new Row.Builder()
            .setTitle(title))
            .build())
        .build())
    .setHeader(header)
    .setNavigateAction(new Action.Builder()
        .setTitle(actionTitle)
        .setOnClickListener(() -> { ... })
        .build())
    .setActionStrip(actionStrip)
    .setMapActionStrip(mapActionStrip)
    .build();

// MapWithContentTemplate
MapWithContentTemplate template = new MapWithContentTemplate.Builder()
    .setContentTemplate(new ListTemplate.Builder()
        .setSingleList(new ItemList.Builder()
            .addItem(new Row.Builder()
                  .setTitle(title))
                  .addAction(new Action.Builder()
                      .setTitle(actionTitle)
                      .setOnClickListener(() -> { ... })
                      .build())
                  .build())
            .build()))
        .setHeader(header)
        .build())
    .setActionStrip(actionStrip)
    .setMapController(new MapController.Builder()
        .setMapActionStrip(mapActionStrip)
        .build())
    .build();
```

## Communicate navigation metadata

Navigation apps must communicate additional navigation metadata with the host. The host uses the information to provide information to the vehicle head unit and to prevent navigation applications from clashing over shared resources.

Navigation metadata is provided through the[`NavigationManager`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager)car service accessible from the[`CarContext`](https://developer.android.com/reference/androidx/car/app/CarContext):  

### Kotlin

```kotlin
val navigationManager = carContext.getCarService(NavigationManager::class.java)
```

### Java

```java
NavigationManager navigationManager = carContext.getCarService(NavigationManager.class);
```

### Start, end, and stop navigation

For the host to manage multiple navigation apps, routing notifications, and vehicle cluster data, it needs to be aware of the current state of navigation. When a user starts navigation, call[`NavigationManager.navigationStarted`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager#navigationStarted()). Similarly, when navigation ends---for example, when the user arrives at their destination or the user cancels navigation---call[`NavigationManager.navigationEnded`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager#navigationEnded()).

Only call`NavigationManager.navigationEnded`when the user finishes navigating. For example, if you need to recalculate the route in the middle of a trip, use[`Trip.Builder.setLoading(true)`](https://developer.android.com/reference/androidx/car/app/navigation/model/Trip.Builder#setLoading(boolean))instead.

Occasionally, the host needs an app to stop navigation and calls`onStopNavigation`in a[`NavigationManagerCallback`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManagerCallback)object provided by your app through[`NavigationManager.setNavigationManagerCallback`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager#setNavigationManagerCallback(java.util.concurrent.Executor,androidx.car.app.navigation.NavigationManagerCallback)). The app must then stop issuing next-turn information in the cluster display, navigation notifications, and voice guidance.

### Update trip information

During active navigation, call[`NavigationManager.updateTrip`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager#updateTrip(androidx.car.app.navigation.model.Trip)). The information provided in this call can be used by the vehicle's cluster and heads-up displays. Depending on the particular vehicle being driven, not all the information is displayed to the user. For example, the Desktop Head Unit (DHU) shows the[`Step`](https://developer.android.com/reference/androidx/car/app/navigation/model/Step)added to the[`Trip`](https://developer.android.com/reference/androidx/car/app/navigation/model/Trip), but does not show the[`Destination`](https://developer.android.com/reference/androidx/car/app/navigation/model/Destination)information.
| **Tip:** You can verify your implementation by using the DHU's[instrument cluster emulation](https://developer.android.com/training/cars/testing/dhu#instrument_cluster).

## Drawing to the Cluster Display

To provide the most immersive user experience, you may want to go beyond[showing basic metadata](https://developer.android.com/training/cars/apps/navigation#trip-information)on the vehicle's cluster display. Starting with Car App API Level 6, navigation apps have the option of rendering their own content directly on the cluster display (in supported vehicles), with the following limitations:

- The cluster display API does not support input controls
- Car app quality guideline[`NF-9`](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=navigation#NF-9): The cluster display should only show map tiles. An active navigation route can optionally be displayed on these tiles.
- The cluster display API only supports use of the[`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate)
  - Unlike main displays, cluster displays may not consistently show all`NavigationTemplate`UI elements, such as turn-by-turn instructions, ETA cards, and actions. Map tiles are the only consistently displayed UI element.

| **Note:** In vehicles that have multiple displays, multiple cluster sessions can run simultaneously.

### Declare Cluster Support

To let the host application know that your app supports rendering on cluster displays, you must add an`androidx.car.app.category.FEATURE_CLUSTER``<category>`element to your`CarAppService`'s`<intent-filter>`as shown in the following snippet:  

```xml
<application>
    ...
   <service
       ...
        android:name=".MyNavigationCarAppService"
        android:exported="true">
      <intent-filter>
        <action android:name="androidx.car.app.CarAppService" />
        <category android:name="androidx.car.app.category.NAVIGATION"/>
        <category android:name="androidx.car.app.category.FEATURE_CLUSTER"/>
      </intent-filter>
    </service>
    ...
</application>
```

### Lifecycle and State Management

Starting with API level 6, the car app[lifecycle flow](https://developer.android.com/training/cars/apps#carappservice-session-screen-lifecycles)stays the same, but now`CarAppService::onCreateSession`takes a parameter of type[`SessionInfo`](https://developer.android.com/reference/androidx/car/app/SessionInfo)that provides additional information about the`Session`being created (namely, the display type and the set of supported templates).

Apps have the option to either use the same`Session`class to handle both the cluster and main display, or create display-specific`Sessions`to customize behavior on each display (as shown in the following snippet).  

### Kotlin

```kotlin
override fun onCreateSession(sessionInfo: SessionInfo): Session {
  return if (sessionInfo.displayType == SessionInfo.DISPLAY_TYPE_CLUSTER) {
    ClusterSession()
  } else {
    MainDisplaySession()
  }
}
```

### Java

```java
@Override
@NonNull
public Session onCreateSession(@NonNull SessionInfo sessionInfo) {
  if (sessionInfo.getDisplayType() == SessionInfo.DISPLAY_TYPE_CLUSTER) {
    return new ClusterSession();
  } else {
    return new MainDisplaySession();
  }
}
```

There are no guarantees about when or if the cluster display is provided, and it's also possible for the cluster`Session`to be the only`Session`(for example, the user swapped the main display to another app while your app is actively navigating). The "standard" agreement is that the app gains control of cluster display only after`NavigationManager::navigationStarted`has been called. However, it's possible for the app to be provided the cluster display while no active navigation is occurring, or to never be provided the cluster display. It is up to your app to handle these scenarios by rendering your app's idle state of map tiles.

The host creates separate binder and`CarContext`instances per`Session`. This means that, when using the methods like`ScreenManager::push`or`Screen::invalidate`, only the`Session`from which they are called is affected. Apps should create their own communication channels between these instances if cross-`Session`communication is needed (for example, by using[broadcasts](https://developer.android.com/guide/components/broadcasts), a shared singleton, or something else).

### Testing Cluster Support

You can test your implementation on both Android Auto and Android Automotive OS. For Android Auto, this is done by[configuring the Desktop Head Unit to emulate a secondary cluster display](https://developer.android.com/training/cars/testing/dhu#cluster_display). For Android Automotive OS, the[generic system images](https://developer.android.com/training/cars/testing/emulator#generic-images)for API level 30 and greater emulate a cluster display.
| **Note:** There is a known issue with the Android Automotive OS emulator which may cause the cluster window to not show up on boot. This can usually be remedied by hiding and then showing the "Running Devices" tool window in Android Studio.

## Customize TravelEstimate with text or an icon

To customize the travel estimate with text, an icon, or both, use the[`TravelEstimate.Builder`](https://developer.android.com/reference/androidx/car/app/navigation/model/TravelEstimate.Builder)class's[`setTripIcon`](https://developer.android.com/reference/androidx/car/app/navigation/model/TravelEstimate.Builder#setTripIcon(androidx.car.app.model.CarIcon))or[`setTripText`](https://developer.android.com/reference/androidx/car/app/navigation/model/TravelEstimate.Builder#setTripText(androidx.car.app.model.CarText))methods. The[`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate)uses[`TravelEstimate`](https://developer.android.com/reference/androidx/car/app/navigation/model/TravelEstimate)to optionally set text and icons alongside or in place of the estimated time of arrival, remaining time, and remaining distance.
![](https://developer.android.com/training/cars/images/eta-custom-IconText.png)**Figure 1.**Travel estimate with custom icon and text.

The following snippet uses`setTripIcon`and`setTripText`to customize the travel estimate:  

### Kotlin

```kotlin
TravelEstimate.Builder(Distance.create(...), DateTimeWithZone.create(...))
      ...
      .setTripIcon(CarIcon.Builder(...).build())
      .setTripText(CarText.create(...))
      .build()
```

### Java

```java
new TravelEstimate.Builder(Distance.create(...), DateTimeWithZone.create(...))
      ...
      .setTripIcon(CarIcon.Builder(...).build())
      .setTripText(CarText.create(...))
      .build();
```

## Provide turn-by-turn notifications

Provide turn-by-turn (TBT) navigation instructions using a frequently updated navigation notification. To be treated as a navigation notification in the car screen, your notification's builder must do the following:

1. Mark the notification as ongoing with the[`NotificationCompat.Builder.setOngoing`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setOngoing(boolean))method.
2. Set the notification's category to`Notification.CATEGORY_NAVIGATION`.
3. Extend the notification with a[`CarAppExtender`](https://developer.android.com/reference/androidx/car/app/notification/CarAppExtender).

A navigation notification displays in the rail widget at the bottom of the car screen. If the notification's importance level is set to`IMPORTANCE_HIGH`, it also displays as a heads-up notification (HUN). If the importance is not set with the[`CarAppExtender.Builder.setImportance`](https://developer.android.com/reference/androidx/car/app/notification/CarAppExtender.Builder#setImportance(int))method, the[notification channel's importance](https://developer.android.com/reference/android/app/NotificationChannel#getImportance())is used.

The app can set a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)in the`CarAppExtender`that is sent to the app when the user taps on the HUN or the rail widget.

If[`NotificationCompat.Builder.setOnlyAlertOnce`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setOnlyAlertOnce(boolean))is called with a value of`true`, a high-importance notification alerts only once in the HUN.

The following snippet shows how to build a navigation notification:  

### Kotlin

```kotlin
NotificationCompat.Builder(context, NOTIFICATION_CHANNEL_ID)
    ...
    .setOnlyAlertOnce(true)
    .setOngoing(true)
    .setCategory(NotificationCompat.CATEGORY_NAVIGATION)
    .extend(
        CarAppExtender.Builder()
            .setContentTitle(carScreenTitle)
            ...
            .setContentIntent(
                PendingIntent.getBroadcast(
                    context,
                    ACTION_OPEN_APP.hashCode(),
                    Intent(ACTION_OPEN_APP).setComponent(
                        ComponentName(context, MyNotificationReceiver::class.java)),
                        0))
            .setImportance(NotificationManagerCompat.IMPORTANCE_HIGH)
            .build())
    .build()
```

### Java

```java
new NotificationCompat.Builder(context, NOTIFICATION_CHANNEL_ID)
    ...
    .setOnlyAlertOnce(true)
    .setOngoing(true)
    .setCategory(NotificationCompat.CATEGORY_NAVIGATION)
    .extend(
        new CarAppExtender.Builder()
            .setContentTitle(carScreenTitle)
            ...
            .setContentIntent(
                PendingIntent.getBroadcast(
                    context,
                    ACTION_OPEN_APP.hashCode(),
                    new Intent(ACTION_OPEN_APP).setComponent(
                        new ComponentName(context, MyNotificationReceiver.class)),
                        0))
            .setImportance(NotificationManagerCompat.IMPORTANCE_HIGH)
            .build())
    .build();
```

Update the TBT notification regularly for distance changes, which updates the rail widget, and only show the notification as a HUN. You can control the HUN behavior by setting the notification's importance with`CarAppExtender.Builder.setImportance`. Setting the importance to`IMPORTANCE_HIGH`shows a HUN. Setting it to any other value only updates the rail widget.
| **Note:** When the app displays the routing information on the car screen, such as during active navigation to a destination, the TBT HUNs are suppressed.

## Refresh PlaceListNavigationTemplate content

You can let drivers refresh content with the tap of a button while browsing lists of places built with[`PlaceListNavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/PlaceListNavigationTemplate). To enable list refresh, implement the[`OnContentRefreshListener`](https://developer.android.com/reference/androidx/car/app/model/OnContentRefreshListener)interface's[`onContentRefreshRequested`](https://developer.android.com/reference/androidx/car/app/model/OnContentRefreshListener#onContentRefreshRequested())method and use[`PlaceListNavigationTemplate.Builder.setOnContentRefreshListener`](https://developer.android.com/reference/androidx/car/app/navigation/model/PlaceListNavigationTemplate.Builder#setOnContentRefreshListener(androidx.car.app.model.OnContentRefreshListener))to set the listener on the template.

The following snippet shows how to set the listener on the template:  

### Kotlin

```kotlin
PlaceListNavigationTemplate.Builder()
    ...
    .setOnContentRefreshListener {
        // Execute any desired logic
        ...
        // Then call invalidate() so onGetTemplate() is called again
        invalidate()
    }
    .build()
```

### Java

```java
new PlaceListNavigationTemplate.Builder()
        ...
        .setOnContentRefreshListener(() -> {
            // Execute any desired logic
            ...
            // Then call invalidate() so onGetTemplate() is called again
            invalidate();
        })
        .build();
```

The refresh button is only shown in the header of the`PlaceListNavigationTemplate`if the listener has a value.

When the user clicks the refresh button, the`onContentRefreshRequested`method of your`OnContentRefreshListener`implementation is called. Within`onContentRefreshRequested`, call the[`Screen.invalidate`](https://developer.android.com/reference/androidx/car/app/Screen#invalidate())method. The host then calls back into your app's[`Screen.onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate())method to retrieve the template with the refreshed content. See[Refresh the contents of a template](https://developer.android.com/training/cars/apps#refresh-template)for more information about refreshing templates. As long as the next template returned by[`onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate())is of the same type, it counts as a refresh and does not count toward the template quota.

## Provide audio guidance

To play navigation guidance over the car speakers, your app must request[audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus). As a part of your[`AudioFocusRequest`](https://developer.android.com/reference/android/media/AudioFocusRequest), set the usage as`AudioAttributes.USAGE_ASSISTANCE_NAVIGATION_GUIDANCE`. Also, set the focus gain as`AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`.

## Simulate navigation

To verify your app's navigation functionality when you submit it to the Google Play Store, your app must implement the[`NavigationManagerCallback.onAutoDriveEnabled`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManagerCallback#onAutoDriveEnabled())callback. When this callback is called, your app must simulate navigation to the chosen destination when the user begins navigation. Your app can exit this mode whenever the lifecycle of the current[`Session`](https://developer.android.com/reference/androidx/car/app/Session)reaches the[`Lifecycle.Event.ON_DESTROY`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_DESTROY)state.

You can test that your implementation of`onAutoDriveEnabled`is called by executing the following from a command line:  

    adb shell dumpsys activity service <var translate="no">CAR_APP_SERVICE_NAME</var> AUTO_DRIVE

This is shown in the following example:  

    adb shell dumpsys activity service androidx.car.app.samples.navigation.car.NavigationCarAppService AUTO_DRIVE

## Default navigation car app

In Android Auto, the default navigation car app corresponds to the last navigation app that the user launched. The default app[receives navigation intents](https://developer.android.com/training/cars/apps#start-car-app)when the user invokes navigation commands through the Assistant or when another app sends an intent to start navigation.

## Display in-context navigation alerts

[`Alert`](https://developer.android.com/reference/androidx/car/app/model/Alert)displays important information to the driver with optional actions‐without leaving the context of the navigation screen. To provide the best experience to the driver,`Alert`works within the[`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate)to avoid blocking the navigation route and to minimize driver distraction.

`Alert`is only available within the`NavigationTemplate`. To notify the user outside of the`NavigationTemplate`, consider using a heads-up notification (HUN), as explained in[Display notifications](https://developer.android.com/training/cars/apps#display-notifications).

For example, use`Alert`to:

- Inform the driver of an update relevant to the current navigation, such as a change in traffic conditions.
- Ask the driver for an update related to the current navigation, such as the existence of a speed trap.
- Propose an upcoming task and ask whether the driver accepts it, such as whether the driver is willing to pick up someone on their way.

In its basic form, an`Alert`consists of a title and the`Alert`duration time. The duration time is represented by a progress bar. Optionally, you can add a subtitle, an icon, and up to two[`Action`](https://developer.android.com/reference/androidx/car/app/model/Action)objects.
![](https://developer.android.com/training/cars/images/CarAppLib-Alert.png)**Figure 2.**In-context navigation alert.

Once an`Alert`is shown, it does not carry over to another template if the driver interaction results in leaving the`NavigationTemplate`. It stays in the original`NavigationTemplate`until`Alert`times out, the user takes an action, or the app dismisses the`Alert`.

### Create an alert

Use[`Alert.Builder`](https://developer.android.com/reference/androidx/car/app/model/Alert.Builder)to create an[`Alert`](https://developer.android.com/reference/androidx/car/app/model/Alert)instance:  

### Kotlin

```kotlin
Alert.Builder(
        /*alertId*/ 1,
        /*title*/ CarText.create("Hello"),
        /*durationMillis*/ 5000
    )
    // The fields below are optional
    .addAction(firstAction)
    .addAction(secondAction)
    .setSubtitle(CarText.create(...))
    .setIcon(CarIcon.APP_ICON)
    .setCallback(...)
    .build()
```

### Java

```java
new Alert.Builder(
        /*alertId*/ 1,
        /*title*/ CarText.create("Hello"),
        /*durationMillis*/ 5000
    )
    // The fields below are optional
    .addAction(firstAction)
    .addAction(secondAction)
    .setSubtitle(CarText.create(...))
    .setIcon(CarIcon.APP_ICON)
    .setCallback(...)
    .build();
```

If you want to listen for`Alert`cancellation or dismissal, create an implementation of the[`AlertCallback`](https://developer.android.com/reference/androidx/car/app/model/AlertCallback)interface. The`AlertCallback`call paths are:

- If the`Alert`times out, the host calls the[`AlertCallback.onCancel`](https://developer.android.com/reference/androidx/car/app/model/AlertCallback#onCancel(int))method with the[`AlertCallback.REASON_TIMEOUT`](https://developer.android.com/reference/androidx/car/app/model/AlertCallback#REASON_TIMEOUT())value. It then calls the[`AlertCallback.onDismiss`](https://developer.android.com/reference/androidx/car/app/model/AlertCallback#onDismiss())method.

- If the driver clicks one of the action buttons, the host calls[`Action.OnClickListener`](https://developer.android.com/reference/androidx/car/app/model/OnClickListener)and then calls`AlertCallback.onDismiss`.

- If the`Alert`is not supported, the host calls`AlertCallback.onCancel`with the[`AlertCallback.REASON_NOT_SUPPORTED`](https://developer.android.com/reference/androidx/car/app/model/AlertCallback#REASON_NOT_SUPPORTED())value. The host does not call`AlertCallback.onDismiss`, because the`Alert`was not shown.

### Configure alert duration

Choose an[`Alert`](https://developer.android.com/reference/androidx/car/app/model/Alert)duration that matches your app's needs. The recommended duration for a navigation`Alert`is 10 seconds. Refer to[Navigation alerts](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/navigation-template#alerts)for more information.

### Show an alert

To show an[`Alert`](https://developer.android.com/reference/androidx/car/app/model/Alert), call the[`AppManager.showAlert`](https://developer.android.com/reference/androidx/car/app/AppManager?showAlert(androidx.car.app.model.Alert)#showAlert(androidx.car.app.model.Alert))method available through your app's[`CarContext`](https://developer.android.com/reference/androidx/car/app/CarContext).  

    // Show an alert
    carContext.getCarService(AppManager.class).showAlert(alert)

- Calling`showAlert`with an`Alert`that has an[`alertId`](https://developer.android.com/reference/androidx/car/app/model/Alert.Builder#Builder(int,%20androidx.car.app.model.CarText,%20long))that is the same as the ID of the`Alert`currently on display does nothing. The`Alert`doesn't update. To update an`Alert`, you must recreate it with a new`alertId`.
- Calling`showAlert`with an`Alert`that has a different`alertId`than the`Alert`currently on display dismisses the`Alert`currently displayed.

### Dismiss an alert

While an[`Alert`](https://developer.android.com/reference/androidx/car/app/model/Alert)automatically dismiss due to timeout or driver interaction, you can also manually dismiss an`Alert`, such as if its information becomes outdated. To dismiss an`Alert`, call the[`dismissAlert`](https://developer.android.com/reference/androidx/car/app/AppManager#dismissAlert(int))method with the[`alertId`](https://developer.android.com/reference/androidx/car/app/model/Alert.Builder#Builder(int,%20androidx.car.app.model.CarText,%20long))of the`Alert`.  

    // Dismiss the same alert
    carContext.getCarService(AppManager.class).dismissAlert(alert.getId())

Calling`dismissAlert`with an`alertId`that doesn't match the currently displayed`Alert`does nothing. It doesn't throw an exception.