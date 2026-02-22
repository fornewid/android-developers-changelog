---
title: https://developer.android.com/training/cars/apps/library/car-hardware-api
url: https://developer.android.com/training/cars/apps/library/car-hardware-api
source: md.txt
---

Starting with Car App API level 3, you can use Car App Library APIs to access
vehicle properties and sensors.

## Requirements

To use the APIs with Android Auto, start by adding a dependency on
`androidx.car.app:app-projected` to the `build.gradle` file for your Android
Auto module. For Android Automotive OS, add a dependency on
`androidx.car.app:app-automotive` to the `build.gradle` file for your Android
Automotive OS module.

Additionally, in your `AndroidManifest.xml` file, you need to [declare the
relevant permissions](https://developer.android.com/training/permissions/declaring) needed to request the car data you want to use. These
permissions must also be [granted](https://developer.android.com/training/permissions/requesting) to you by the user. You can use
the [same code](https://developer.android.com/training/cars/apps/car-apps-library/request-permissions) on Android Auto and Android Automotive OS, rather than
creating platform-dependent flows. However, the permissions needed differ.

## CarInfo

This table describes the properties provided in the [`CarInfo`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo) APIs and the
permissions you must request to use them.

| Methods | Properties | Permissions: Android Auto | Permissions: AAOS | Car App API |
|---|---|---|---|---|
| [`fetchModel`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchModel(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Model>)) | Make, model, year |   | `android.car.permission.CAR_INFO` | 3 |
| [`fetchEnergyProfile`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchEnergyProfile(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyProfile>)) | EV connector types, fuel types | `com.google.android.gms.permission.CAR_FUEL` | `android.car.permission.CAR_INFO` | 3 |
| [`fetchExteriorDimensions`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchExteriorDimensions(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.ExteriorDimensions>)) *Data available only on some AAOS vehicles that run API 30 or later.* | Exterior dimensions | N/A | `android.car.permission.CAR_INFO` | 7 |
| [`addTollListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addTollListener(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.TollCard>)) [`removeTollListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeTollListener(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.TollCard>)) | Toll card state, toll card type |   |   | 3 |
| [`addEnergyLevelListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addEnergyLevelListener(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyLevel>)) [`removeEnergyLevelListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeEnergyLevelListener(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyLevel>)) | Battery level, fuel level, fuel level low, range remaining | `com.google.android.gms.permission.CAR_FUEL` | `android.car.permission.CAR_ENERGY` `android.car.permission.CAR_ENERGY_PORTS` `android.car.permission.READ_CAR_DISPLAY_UNITS` | 3 |
| [`addSpeedListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addSpeedListener(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Speed>)) [`removeSpeedListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeSpeedListener(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Speed>)) | Raw speed, display speed (shown on car's cluster display) | `com.google.android.gms.permission.CAR_SPEED` | `android.car.permission.CAR_SPEED` `android.car.permission.READ_CAR_DISPLAY_UNITS` | 3 |
| [`addMileageListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addMileageListener(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Mileage>)) [`removeMileageListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeMileageListener(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Mileage>)) | Odometer distance | `com.google.android.gms.permission.CAR_MILEAGE` | *Data not available to Android Automotive OS apps installed from Google Play.* | 3 |

For example, to get the remaining range, instantiate a
`CarInfo` object, then create and register an `OnCarDataAvailableListener`:  

### Kotlin

    val carInfo = carContext.getCarService(CarHardwareManager::class.java).carInfo

    val listener = OnCarDataAvailableListener<EnergyLevel> { data ->
        if (data.rangeRemainingMeters.status == CarValue.STATUS_SUCCESS) {
          val rangeRemaining = data.rangeRemainingMeters.value
        } else {
          // Handle error
        }
      }

    carInfo.addEnergyLevelListener(carContext.mainExecutor, listener)
    ...
    // Unregister the listener when you no longer need updates
    carInfo.removeEnergyLevelListener(listener)

### Java

    CarInfo carInfo = getCarContext().getCarService(CarHardwareManager.class).getCarInfo();

    OnCarDataAvailableListener<EnergyLevel> listener = (data) -> {
      if(data.getRangeRemainingMeters().getStatus() == CarValue.STATUS_SUCCESS) {
        float rangeRemaining = data.getRangeRemainingMeters().getValue();
      } else {
        // Handle error
      }
    };

    carInfo.addEnergyLevelListener(getCarContext().getMainExecutor(), listener);
    ...
    // Unregister the listener when you no longer need updates
    carInfo.removeEnergyLevelListener(listener);

Don't assume that the data from the car is available at all times. If you get an
error, check the[status](https://developer.android.com/reference/androidx/car/app/hardware/common/CarValue#getStatus()) of the value you requested to better understand why
the data you requested couldn't be retrieved. To learn more about the `CarInfo`
class definition, see the [reference documentation](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo).

## CarSensors

The [`CarSensors`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarSensors) class gives you access to the vehicle's accelerometer,
gyroscope, compass, and location data. The availability of these values may
depend on the OEM. The format for the data from the accelerometer, gyroscope,
and compass is the same as you would get from the [`SensorManager` API](https://developer.android.com/reference/android/hardware/SensorManager).

For example, to check the vehicle's heading:  

### Kotlin

    val carSensors = carContext.getCarService(CarHardwareManager::class.java).carSensors

    val listener = OnCarDataAvailableListener<Compass> { data ->
        if (data.orientations.status == CarValue.STATUS_SUCCESS) {
          val orientation = data.orientations.value
        } else {
          // Data not available, handle error
        }
      }

    carSensors.addCompassListener(CarSensors.UPDATE_RATE_NORMAL, carContext.mainExecutor, listener)
    ...
    // Unregister the listener when you no longer need updates
    carSensors.removeCompassListener(listener)

### Java

    CarSensors carSensors = getCarContext().getCarService(CarHardwareManager.class).getCarSensors();

    OnCarDataAvailableListener<Compass> listener = (data) -> {
      if (data.getOrientations().getStatus() == CarValue.STATUS_SUCCESS) {
        List<Float> orientations = data.getOrientations().getValue();
      } else {
        // Data not available, handle error
      }
    };

    carSensors.addCompassListener(CarSensors.UPDATE_RATE_NORMAL, getCarContext().getMainExecutor(),
        listener);
    ...
    // Unregister the listener when you no longer need updates
    carSensors.removeCompassListener(listener);

To access location data from the car, you also need to declare and request the
`android.permission.ACCESS_FINE_LOCATION` permission.
| **Caution:** On Android Automotive OS, `CarSensors` data returns [`STATUS_UNIMPLEMENTED`](https://developer.android.com/reference/androidx/car/app/hardware/common/CarValue#STATUS_UNIMPLEMENTED()). Instead, use standard Android APIs to access the data, such as `SensorManager` or [`LocationManager`](https://developer.android.com/reference/android/location/LocationManager).

## Test

To simulate sensor data when testing on Android Auto, see the
[Sensors](https://developer.android.com/training/cars/testing/dhu#sensors) and [Sensor configuration](https://developer.android.com/training/cars/testing/dhu#sensor-configuration) sections of the Desktop Head Unit
guide. To simulate sensor data when testing on Android Automotive OS, refer to
[Emulate hardware state](https://developer.android.com/training/cars/testing/emulator#emulate-state) in the Android Automotive OS emulator guide.