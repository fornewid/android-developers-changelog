---
title: https://developer.android.com/guide/components/activities/parcelables-and-bundles
url: https://developer.android.com/guide/components/activities/parcelables-and-bundles
source: md.txt
---

[Parcelable](https://developer.android.com/reference/android/os/Parcelable)and[Bundle](https://developer.android.com/reference/android/os/Bundle)objects are intended to be used across process boundaries such as with IPC/Binder transactions, between activities with intents, and to store transient state across configuration changes. This page provides recommendations and best practices for using[Parcelable](https://developer.android.com/reference/android/os/Parcelable)and[Bundle](https://developer.android.com/reference/android/os/Bundle)objects.

**Note:** [Parcel](https://developer.android.com/reference/android/os/Parcel)is not a general-purpose serialization mechanism, and you should never store any[Parcel](https://developer.android.com/reference/android/os/Parcel)data on disk or send it over the network.

## Sending data between activities

When an app creates an[Intent](https://developer.android.com/reference/android/content/Intent)object to use in[startActivity(android.content.Intent)](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent))in starting a new Activity, the app can pass in parameters using the[putExtra(java.lang.String, java.lang.String)](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String, java.lang.String))method.

The following code snippet shows an example of how to perform this operation.  

### Kotlin

```kotlin
val intent = Intent(this, MyActivity::class.java).apply {
    putExtra("media_id", "a1b2c3")
    // ...
}
startActivity(intent)
```

### Java

```java
Intent intent = new Intent(this, MyActivity.class);
intent.putExtra("media_id", "a1b2c3");
// ...
startActivity(intent);
```

The OS parcels the underlying[Bundle](https://developer.android.com/reference/android/os/Bundle)of the intent. Then, the OS creates the new activity, un-parcels the data, and passes the intent to the new activity.

We recommend that you use the[Bundle](https://developer.android.com/reference/android/os/Bundle)class to set primitives known to the OS on[Intent](https://developer.android.com/reference/android/content/Intent)objects. The[Bundle](https://developer.android.com/reference/android/os/Bundle)class is highly optimized for marshalling and unmarshalling using parcels.

In some cases, you may need a mechanism to send composite or complex objects across activities. In such cases, the custom class should implement Parcelable, and provide the appropriate[writeToParcel(android.os.Parcel, int)](https://developer.android.com/reference/android/os/Parcelable#writeToParcel(android.os.Parcel, int))method. It must also provide a non-null field called`CREATOR`that implements the[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator)interface, whose[createFromParcel()](https://developer.android.com/reference/android/os/Parcelable.Creator#createFromParcel(android.os.Parcel))method is used for converting the[Parcel](https://developer.android.com/reference/android/os/Parcel)back to the current object. For more information, see the reference documentation for the[Parcelable](https://developer.android.com/reference/android/os/Parcelable)object.

<br />

When sending data via an intent, you should be careful to limit the data size to a few KB. Sending too much data can cause the system to throw a[TransactionTooLargeException](https://developer.android.com/reference/android/os/TransactionTooLargeException)exception.

## Sending data between processes

Sending data between processes is similar to doing so between activities. However, when sending between processes, we recommend that you do not use custom parcelables. If you send a custom[Parcelable](https://developer.android.com/reference/android/os/Parcelable)object from one app to another, you need to be certain that the exact same version of the custom class is present on both the sending and receiving apps. Typically this could be a common library used across both apps. An error can occur if your app tries to send a custom parcelable to the system, because the system cannot unmarshal a class that it has no knowledge of.

For example, an app might set an alarm using the[AlarmManager](https://developer.android.com/reference/android/app/AlarmManager)class, and use a custom[Parcelable](https://developer.android.com/reference/android/os/Parcelable)on the alarm intent. When the alarm goes off, the system modifies the intent's[Bundle](https://developer.android.com/reference/android/os/Bundle)of extras to add a repeat count. This modification can result in the system's stripping the custom[Parcelable](https://developer.android.com/reference/android/os/Parcelable)from the extras. This stripping, in turn, can result in the app's crashing when it receives the modified alarm intent, because the app expects to receive extra data that is no longer there.

The Binder transaction buffer has a limited fixed size, currently 1MB, which is shared by all transactions in progress for the process. Since this limit is at the process level rather than at the per activity level, these transactions include all binder transactions in the app such as onSaveInstanceState, startActivity and any interaction with the system. When the size limit is exceeded, a TransactionTooLargeException is thrown.

For the specific case of savedInstanceState, the amount of data should be kept small because the system process needs to hold on to the provided data for as long as the user can ever navigate back to that activity (even if the activity's process is killed). We recommend that you keep saved state to less than 50k of data.

**Note:**In Android 7.0 (API level 24) and higher, the system throws a TransactionTooLargeException as a runtime exception. In lower versions of Android, the system only shows a warning in logcat.