---
title: https://developer.android.com/google/play/installreferrer/library
url: https://developer.android.com/google/play/installreferrer/library
source: md.txt
---

# Play Install Referrer Library

You can use the Google Play Store's Install Referrer API to securely retrieve referral content from Google Play. The Play Install Referrer API Client Library is written in the Java programming language and is a wrapper for the Android Interface Definition Language (AIDL) file that defines the interface to the Install Referrer service. You can use the Play Install Referrer API Client Library to simplify your development process.

This guide covers the basics of retrieving referral information from Google Play using the Play Install Referrer Library.
| **Note:** If you are developing your app using a language other than the Kotlin programming language or the Java programming language, you can interact directly with the AIDL file by using the[Play Install Referrer API](https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice).

## Updating your app's dependencies

Add the following line to the dependencies section of the`build.gradle`file for your app:  

### Groovy

```groovy
dependencies {
    ...
    implementation "com.android.installreferrer:installreferrer:2.2"
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("com.android.installreferrer:installreferrer:2.2")
}
```

## Connecting to Google Play

Before you can use the Play Install Referrer API Library, you must establish a connection to the Play Store app using the following steps:

1. Call the[`newBuilder()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#newBuilder(android.content.Context))method to create an instance of[`InstallReferrerClient`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient)class.
2. Call the[`startConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#startConnection(com.android.installreferrer.api.InstallReferrerStateListener))to establish a connection to Google Play.

3. The[`startConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#startConnection(com.android.installreferrer.api.InstallReferrerStateListener))method is asynchronous, so you must override[`InstallReferrerStateListener`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerStateListener)to receive a callback after[`startConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#startConnection(com.android.installreferrer.api.InstallReferrerStateListener))completes.

4. Override the[`onInstallReferrerSetupFinished()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerStateListener#onInstallReferrerSetupFinished(int))method to be notified when the callback completes. This method is called with a response code that you must use to handle the different states.[`OK`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient.InstallReferrerResponse#OK)indicates that the connection was successful. Each of the other[`InstallReferrerResponse`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient.InstallReferrerResponse)constants are for different types of errors.

5. Override the[`onInstallReferrerServiceDisconnected()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerStateListener#oninstallreferrerservicedisconnected)method to handle lost connections to Google Play. For example, the Play Install Referrer Library client may lose the connection if the Play Store service is updating in the background. The library client must call the[`startConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#startConnection(com.android.installreferrer.api.InstallReferrerStateListener))method to restart the connection before making further requests.

The following code demonstrates how to start and test a connection to the Play Store app:  

### Kotlin

```kotlin
private lateinit var referrerClient: InstallReferrerClient

referrerClient = InstallReferrerClient.newBuilder(this).build()
referrerClient.startConnection(object : InstallReferrerStateListener {

    override fun onInstallReferrerSetupFinished(responseCode: Int) {
        when (responseCode) {
            InstallReferrerResponse.OK -> {
                // Connection established.
            }
            InstallReferrerResponse.FEATURE_NOT_SUPPORTED -> {
                // API not available on the current Play Store app.
            }
            InstallReferrerResponse.SERVICE_UNAVAILABLE -> {
                // Connection couldn't be established.
            }
        }
    }

    override fun onInstallReferrerServiceDisconnected() {
        // Try to restart the connection on the next request to
        // Google Play by calling the startConnection() method.
    }
})
```

### Java

```java
InstallReferrerClient referrerClient;

referrerClient = InstallReferrerClient.newBuilder(this).build();
referrerClient.startConnection(new InstallReferrerStateListener() {
    @Override
    public void onInstallReferrerSetupFinished(int responseCode) {
        switch (responseCode) {
            case InstallReferrerResponse.OK:
                // Connection established.
                break;
            case InstallReferrerResponse.FEATURE_NOT_SUPPORTED:
                // API not available on the current Play Store app.
                break;
            case InstallReferrerResponse.SERVICE_UNAVAILABLE:
                // Connection couldn't be established.
                break;
        }
    }

    @Override
    public void onInstallReferrerServiceDisconnected() {
        // Try to restart the connection on the next request to
        // Google Play by calling the startConnection() method.
    }
});
```

## Getting the install referrer

After you have established a connection to the Play Store app, get the details from the install referrer by completing the following steps:

1. Use the synchronized[`getInstallReferrer()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#getInstallReferrer())method to return an instance of[`ReferrerDetails`](https://developer.android.com/reference/com/android/installreferrer/api/ReferrerDetails).

2. Use the methods that the[`ReferrerDetails`](https://developer.android.com/reference/com/android/installreferrer/api/ReferrerDetails)class provides to get details about the install referrer.

The following code demonstrates how you can access the install referrer information:  

### Kotlin

```kotlin
val response: ReferrerDetails = referrerClient.installReferrer
val referrerUrl: String = response.installReferrer
val referrerClickTime: Long = response.referrerClickTimestampSeconds
val appInstallTime: Long = response.installBeginTimestampSeconds
val instantExperienceLaunched: Boolean = response.googlePlayInstantParam
```

### Java

```java
ReferrerDetails response = referrerClient.getInstallReferrer();
String referrerUrl = response.getInstallReferrer();
long referrerClickTime = response.getReferrerClickTimestampSeconds();
long appInstallTime = response.getInstallBeginTimestampSeconds();
boolean instantExperienceLaunched = response.getGooglePlayInstantParam();
```

**Caution:** The install referrer information will be available for 90 days and**won't change** unless the application is reinstalled. To avoid unnecessary API calls in your app, you should invoke the API**only once**during the first execution after install.

## Closing service connection

After getting referrer information, call the[`endConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient#endConnection())method on your[`InstallReferrerClient`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient)instance to close the connection. Closing the connection will help you avoid leaks and performance problems.

For further information, refer to the[Play Install Referrer Library Reference](https://developer.android.com/reference/com/android/installreferrer/packages).