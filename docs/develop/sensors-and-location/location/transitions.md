---
title: https://developer.android.com/develop/sensors-and-location/location/transitions
url: https://developer.android.com/develop/sensors-and-location/location/transitions
source: md.txt
---

It might be necessary to design your app to identify when a user starts or stops
a particular activity, such as walking, biking, or driving. For example, a
mileage tracking app could start tracking miles when a user starts driving, or a
messaging app could mute all conversations until the user stops driving.

The Activity Recognition Transition API can be used to detect changes in the
user's activity. Your app subscribes to a transition in activities of interest
and the API notifies your app only when needed. This page shows how to use the
Activity Recognition Transition API, also called the Transition API for short.

## Set up your project

To use the Transition API in your app, you must declare a dependency to the
**Google Location and Activity Recognition** API version 12.0.0 or higher and
specify the `com.google.android.gms.permission.ACTIVITY_RECOGNITION` permission
in the app manifest.

1. To declare a dependency to the API, add a reference to the Google maven repository and add an implementation entry to `com.google.android.gms:play-services-location:12.0.0` to the dependencies section of your app `build.gradle` file. For more information, see [Set Up
   Google Play Services](https://developers.google.com/android/guides/setup).
2. To specify the `com.google.android.gms.permission.ACTIVITY_RECOGNITION`
   permission, add a
   [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
   element in the app manifest, as shown in the following example:

        <manifest xmlns:android="http://schemas.android.com/apk/res/android"
                package="com.example.myapp">

          <uses-permission android:name="com.google.android.gms.permission.ACTIVITY_RECOGNITION" />
          ...
        </manifest>

## Register for activity transition updates

To start receiving notifications about activity transitions, you must implement
the following:

- An [`ActivityTransitionRequest`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionRequest) object that specifies the type of activity and transition.
- A `https://developer.android.com/reference/android/app/PendingIntent` callback where your app receives notifications. For more information, see [Using a pending
  intent](https://developer.android.com/guide/components/intents-filters#PendingIntent).

To create the
[`ActivityTransitionRequest`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionRequest)
object, you must create a list of
[`ActivityTransition`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition)
objects, which represent the transition that you want to receive notifications
about. An
[`ActivityTransition`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition)
object includes the following data:

- An activity type, represented by the [`DetectedActivity`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity) class. The Transition API supports the following activities:
  - [`IN_VEHICLE`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#IN_VEHICLE)
  - [`ON_BICYCLE`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#ON_BICYCLE)
  - [`RUNNING`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#RUNNING)
  - [`STILL`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#STILL)
  - [`WALKING`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#WALKING)
- A transition type of [`ACTIVITY_TRANSITION_ENTER`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition#ACTIVITY_TRANSITION_ENTER) or [`ACTIVITY_TRANSITION_EXIT`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition#ACTIVITY_TRANSITION_EXIT). For more information, refer to the [`ActivityTransition`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition) class.

The following code shows how to create a list of `ActivityTransition` objects:

### Kotlin

```kotlin
val transitions = mutableListOf<ActivityTransition>()

transitions +=
        ActivityTransition.Builder()
          .setActivityType(DetectedActivity.IN_VEHICLE)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_ENTER)
          .build()

transitions +=
        ActivityTransition.Builder()
          .setActivityType(DetectedActivity.IN_VEHICLE)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_EXIT)
          .build()

transitions +=
        ActivityTransition.Builder()
          .setActivityType(DetectedActivity.WALKING)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_EXIT)
          .build()
```

### Java

```java
List<ActivityTransition> transitions = new ArrayList<>();

transitions.add(
        new ActivityTransition.Builder()
          .setActivityType(DetectedActivity.IN_VEHICLE)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_ENTER)
          .build());

transitions.add(
        new ActivityTransition.Builder()
          .setActivityType(DetectedActivity.IN_VEHICLE)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_EXIT)
          .build());

transitions.add(
        new ActivityTransition.Builder()
          .setActivityType(DetectedActivity.WALKING)
          .setActivityTransition(ActivityTransition.ACTIVITY_TRANSITION_EXIT)
          .build());
```

You can create an
[`ActivityTransitionRequest`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionRequest)
object by passing the list of `ActivityTransitions` to the
`ActivityTransitionRequest` class, as shown in the following example:

### Kotlin

```kotlin
val request = ActivityTransitionRequest(transitions)
```

### Java

```java
ActivityTransitionRequest request = new ActivityTransitionRequest(transitions);
```

You can register for activity transition updates by passing your instance of
[`ActivityTransitionRequest`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionRequest)
and your `https://developer.android.com/reference/android/app/PendingIntent` object to the
[`requestActivityTransitionUpdates()`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionClient#requestActivityTransitionUpdates(com.google.android.gms.location.ActivityTransitionRequest,%20android.app.PendingIntent))
method. The `requestActivityTransitionUpdates()` method returns a
[`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task)
object that you can check for success or failure, as shown in the following code
example:

### Kotlin

```kotlin
// myPendingIntent is the instance of PendingIntent where the app receives callbacks.
val task = ActivityRecognition.getClient(context)
        .requestActivityTransitionUpdates(request, myPendingIntent)

task.addOnSuccessListener {
    // Handle success
}

task.addOnFailureListener { e: Exception ->
    // Handle error
}
```

### Java

```java
// myPendingIntent is the instance of PendingIntent where the app receives callbacks.
Task<Void> task = ActivityRecognition.getClient(context)
          .requestActivityTransitionUpdates(request, myPendingIntent);

task.addOnSuccessListener(
    new OnSuccessListener<Void>() {
        @Override
        public void onSuccess(Void result) {
            // Handle success
        }
    }
);

task.addOnFailureListener(
    new OnFailureListener() {
        @Override
        public void onFailure(Exception e) {
            // Handle error
        }
    }
);
```

After successfully registering for activity transition updates, your app
receives notifications in the registered `PendingIntent`.

## Process activity transition events

When the requested activity transition occurs, you app receives an `https://developer.android.com/reference/android/content/Intent` callback. An
[`ActivityTransitionResult`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionResult)
object can be extracted from the `Intent`, which includes a list of
[`ActivityTransitionEvent`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransitionEvent)
objects. The events are ordered in chronological order, for example, if an app
requests for the
[`IN_VEHICLE`](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity.html#IN_VEHICLE)
activity type on the
[`ACTIVITY_TRANSITION_ENTER`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition#ACTIVITY_TRANSITION_ENTER)
and
[`ACTIVITY_TRANSITION_EXIT`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityTransition.html#ACTIVITY_TRANSITION_EXIT)
transitions, then it receives an `ActivityTransitionEvent` object when the user
starts driving, and another one when the user transitions to any other activity.

You can implement your callback by creating a subclass of `https://developer.android.com/reference/android/content/BroadcastReceiver` and implementing the `https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)` method to get the list
of activity transition events. For more information, see
[Broadcasts](https://developer.android.com/guide/components/broadcasts). The following example shows how
to implement the `onReceive()` method:

### Kotlin

```kotlin
override fun onReceive(context: Context, intent: Intent) {
    if (ActivityTransitionResult.hasResult(intent)) {
        val result = ActivityTransitionResult.extractResult(intent)!!
        for (event in result.transitionEvents) {
            // chronological sequence of events....
        }
    }
}
```

### Java

```java
@Override
public void onReceive(Context context, Intent intent) {
    if (ActivityTransitionResult.hasResult(intent)) {
        ActivityTransitionResult result = ActivityTransitionResult.extractResult(intent);
        for (ActivityTransitionEvent event : result.getTransitionEvents()) {
            // chronological sequence of events....
        }
    }
}
```
| **Note:** The latency of event detection might vary by device.

## Deregister for activity transition updates

You can deregister for activity transition updates by calling the
[`removeActivityTransitionUpdates()`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionClient#removeActivityTransitionUpdates(android.app.PendingIntent))
method of the
[`ActivityRecognitionClient`](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionClient)
and passing your `https://developer.android.com/reference/android/app/PendingIntent` object as a parameter, as
shown in the following example:

### Kotlin

```kotlin
// myPendingIntent is the instance of PendingIntent where the app receives callbacks.
val task = ActivityRecognition.getClient(context)
        .removeActivityTransitionUpdates(myPendingIntent)

task.addOnSuccessListener {
    myPendingIntent.cancel()
}

task.addOnFailureListener { e: Exception ->
    Log.e("MYCOMPONENT", e.message)
}
```

### Java

```java
// myPendingIntent is the instance of PendingIntent where the app receives callbacks.
Task<Void> task = ActivityRecognition.getClient(context)
        .removeActivityTransitionUpdates(myPendingIntent);

task.addOnSuccessListener(
    new OnSuccessListener<Void>() {
        @Override
        public void onSuccess(Void result) {
            myPendingIntent.cancel();
        }
    }
);

task.addOnFailureListener(
    new OnFailureListener() {
        @Override
        public void onFailure(Exception e) {
            Log.e("MYCOMPONENT", e.getMessage());
        }
    }
);
```

## Additional resources

To learn more about user activity recognition API usage, view the following
materials:

### Samples

[Sample](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/useractivityrecog) to demonstrate best practices for user activity recognition.