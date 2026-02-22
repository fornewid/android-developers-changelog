---
title: https://developer.android.com/training/cars/apps/poi
url: https://developer.android.com/training/cars/apps/poi
source: md.txt
---

# Build a point of interest app

This guide details the different features of the Car App Library that you can use to implement the functionality of your point of interest (POI) app.

## Declare category support in your manifest

Your app needs to declare the`androidx.car.app.category.POI`[car app category](https://developer.android.com/training/cars/apps#supported-app-categories)in the intent filter of its[`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService).
| **Important:** As of Car App Library version 1.3, the`androidx.car.app.category.PARKING`and`androidx.car.app.category.CHARGING`[car app categories](https://developer.android.com/training/cars/apps#supported-app-categories)are deprecated. Use the`androidx.car.app.category.POI`category instead.

The following example shows how to declare the app category:  

    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.POI"/>
          </intent-filter>
        </service>
        ...
    <application>

## Access the map templates

POI apps can access the[`PlaceListMapTemplate`](https://developer.android.com/reference/androidx/car/app/model/PlaceListMapTemplate)and[`MapWithContentTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapWithContentTemplate).

The`PlaceListMapTemplate`is specifically designed for showing a list of the POIs alongside a map that is rendered by the host.

The`MapWithContentTemplate`can be used to display lists and other types of content alongside a map that is rendered by your app. See[Draw maps](https://developer.android.com/training/cars/apps#draw-maps)for more details on using this template.

To access these templates, your app needs to declare the`androidx.car.app.MAP_TEMPLATES`permission in its`AndroidManifest.xml`file:  

    <manifest ...>
      ...
      <uses-permission android:name="androidx.car.app.MAP_TEMPLATES"/>
      ...
    </manifest>

| **Note:** The`PlaceListMapTemplate`is available for use only by apps declaring the`androidx.car.app.category.POI`category or the deprecated`androidx.car.app.category.PARKING`or`androidx.car.app.category.CHARGING`categories. For navigation apps, see[Access the navigation templates](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates).

## Refresh PlaceListMapTemplate content

You can let drivers refresh content with the tap of a button while browsing lists of places built with[`PlaceListMapTemplate`](https://developer.android.com/reference/androidx/car/app/model/PlaceListMapTemplate). Implement the[`OnContentRefreshListener`](https://developer.android.com/reference/androidx/car/app/model/OnContentRefreshListener)interface's[`onContentRefreshRequested`](https://developer.android.com/reference/androidx/car/app/model/OnContentRefreshListener#onContentRefreshRequested())method, and use[`PlaceListMapTemplate.Builder.setOnContentRefreshListener`](https://developer.android.com/reference/kotlin/androidx/car/app/model/PlaceListMapTemplate.Builder#setoncontentrefreshlistener)to set the listener on the template to enable list refresh.

The following snippet shows how to set the listener on the template:  

### Kotlin

```kotlin
PlaceListMapTemplate.Builder()
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
new PlaceListMapTemplate.Builder()
        ...
        .setOnContentRefreshListener(() -> {
            // Execute any desired logic
            ...
            // Then call invalidate() so onGetTemplate() is called again
            invalidate();
        })
        .build();
```

The refresh button is only shown in the header of the`PlaceListMapTemplate`if the listener has a value.

When the user clicks the refresh button, the`onContentRefreshRequested`method of your`OnContentRefreshListener`implementation is called. Within`onContentRefreshRequested`, call the[`Screen.invalidate`](https://developer.android.com/reference/androidx/car/app/Screen#invalidate())method. The host then calls back into your app's[`Screen.onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate())method to retrieve the template with the refreshed content. See[Refresh the contents of a template](https://developer.android.com/training/cars/apps#refresh-template)for more information about refreshing templates. As long as the next template returned by`onGetTemplate`is of the same type, it is counted as a refresh and does not count toward the template quota.

## Integrate with Google Assistant using App Actions

Voice-enable your POI app using Assistant to allow users to search for points of interest by asking things like,*"Hey Google, find nearby charging stations on ExampleApp"* . For detailed instructions, see[App Actions for Cars](https://developer.android.com/guide/app-actions/cars).

*** ** * ** ***