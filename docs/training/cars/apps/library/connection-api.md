---
title: https://developer.android.com/training/cars/apps/library/connection-api
url: https://developer.android.com/training/cars/apps/library/connection-api
source: md.txt
---

| **Warning:** For apps that use the `CarConnection` API and [target](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) Android 14 (API level 34) and higher, use Car App Library version `1.3.0-beta01` or later. Earlier versions of the library throw an exception on devices running Android 14 or later due to the requirement for [context-registered receivers to specify export behavior](https://developer.android.com/about/versions/14/behavior-changes-14#runtime-receivers-exported).  
|
| Regardless of the Car App Library version, for apps that target Android 13 (API level 33) or lower, `CarConnection` API doesn't encounter this issue, even on a device running Android 14 or higher.

To determine if your app is running on Android Auto or Android Automotive OS,
use the [`CarConnection` API](https://developer.android.com/reference/androidx/car/app/connection/CarConnection) to retrieve connection information at runtime.
For example:

1. In your car app's `Session`, initialize a `CarConnection` and subscribe to
   `LiveData` updates:

   ### Kotlin

       CarConnection(carContext).type.observe(this, ::onConnectionStateUpdated)

   ### Java

       new CarConnection(getCarContext()).getType().observe(this, this::onConnectionStateUpdated);

2. In the observer, react to changes in the connection state:

   ### Kotlin

       fun onConnectionStateUpdated(connectionState: Int) {
         val message = when(connectionState) {
           CarConnection.CONNECTION_TYPE_NOT_CONNECTED -> "Not connected to a head unit"
           CarConnection.CONNECTION_TYPE_NATIVE -> "Connected to Android Automotive OS"
           CarConnection.CONNECTION_TYPE_PROJECTION -> "Connected to Android Auto"
           else -> "Unknown car connection type"
         }
         CarToast.makeText(carContext, message, CarToast.LENGTH_SHORT).show()
       }

   ### Java

       private void onConnectionStateUpdated(int connectionState) {
         String message;
         switch(connectionState) {
           case CarConnection.CONNECTION_TYPE_NOT_CONNECTED:
             message = "Not connected to a head unit";
             break;
           case CarConnection.CONNECTION_TYPE_NATIVE:
             message = "Connected to Android Automotive OS";
             break;
           case CarConnection.CONNECTION_TYPE_PROJECTION:
             message = "Connected to Android Auto";
             break;
           default:
             message = "Unknown car connection type";
             break;
         }
         CarToast.makeText(getCarContext(), message, CarToast.LENGTH_SHORT).show();
       }