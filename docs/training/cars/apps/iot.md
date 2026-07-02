---
title: Build an internet of things app  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/iot
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Build an internet of things app Stay organized with collections Save and categorize content based on your preferences.





IoT apps enable users to take relevant actions on connected devices from within
the car. Examples include controlling the state of certain devices, such as
opening a garage door, flipping home light switches, or enabling home security.

## Declare category support in your manifest

Your app must declare the `androidx.car.app.category.IOT`
[car app category](/training/cars/apps/library/set-up-project#supported-app-categories)
in the intent filter of its
[`CarAppService`](/reference/androidx/car/app/CarAppService).

```
<application>
    ...
   <service
       ...
        android:name=".MyCarAppService"
        android:exported="true">
      <intent-filter>
        <action android:name="androidx.car.app.CarAppService" />
        <category android:name="androidx.car.app.category.IOT"/>
      </intent-filter>
    </service>
    ...
<application>
```

## Implement your app's functionality

To implement your app, see
[Using the Android for Cars App Library](/training/cars/apps) on how Car App
Library apps are built. Also, be sure to read the
[Car App Quality Guidelines for IOT apps](/docs/quality-guidelines/car-app-quality?category=iot#app_categories)
, because your app will be reviewed against these guidelines.

For IoT apps, the [`GridTemplate`](/reference/androidx/car/app/model/GridTemplate)
is a good choice for displaying a list of devices and letting users
interact with them, as shown in the following sample:

```
val listBuilder = ItemList.Builder()
val headerBuilder = Header.Builder()
val garageIcon = IconCompat.createWithResource(
    carContext,
    R.drawable.ic_garage
)

listBuilder.addItem(
    GridItem.Builder()
        .setTitle("Garage door")
        .setImage(
            CarIcon.Builder(garageIcon).build(),
            GridItem.IMAGE_TYPE_ICON
        )
        .setOnClickListener {
            // Handle user interactions
        }
        .build()
)

listBuilder.addItem(
    GridItem.Builder()
        .setTitle("Garage lights")
        // Show a loading indicator until the status of the device is known
        // (call invalidate() when the status is known to refresh the screen)
        .setLoading(true)
        .build()
)

return GridTemplate.Builder()
    .setHeader(
        headerBuilder.setTitle("Devices")
            .setStartHeaderAction(Action.APP_ICON).build()
    )
    .setSingleList(listBuilder.build())
    .build()

IOT.kt
```