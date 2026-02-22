---
title: https://developer.android.com/google/play/licensing/client-side-verification
url: https://developer.android.com/google/play/licensing/client-side-verification
source: md.txt
---

# Adding Client-Side License Verification to Your App

**Warning:**When your app performs the license verification process on the client side, it's easier for potential attackers to modify or remove the logic associated with this verification process.

For this reason, we**strongly** encourage you to[perform server-side license verification instead](https://developer.android.com/google/play/licensing/server-side-verification).

After you've set up a publisher account and development environment (see[Setting Up for Licensing](https://developer.android.com/google/play/licensing/setting-up)), you are ready to add license verification to your app with the License Verification Library (LVL).

Adding license verification with the LVL involves these tasks:

1. [Adding the licensing permission](https://developer.android.com/google/play/licensing/client-side-verification#manifest-permission)your application's manifest.
2. [Implementing a Policy](https://developer.android.com/google/play/licensing/client-side-verification#impl-Policy)--- you can choose one of the full implementations provided in the LVL or create your own.
3. [Implementing an Obfuscator](https://developer.android.com/google/play/licensing/client-side-verification#impl-Obfuscator), if your`Policy`will cache any license response data.
4. [Adding code to check the license](https://developer.android.com/google/play/licensing/client-side-verification#impl-lc)in your application's main Activity.
5. [Implementing a DeviceLimiter](https://developer.android.com/google/play/licensing/client-side-verification#impl-DeviceLimiter)(optional and not recommended for most applications).

The sections below describe these tasks. When you are done with the integration, you should be able to compile your application successfully and you can begin testing, as described in[Setting Up the Test Environment](https://developer.android.com/google/play/licensing/setting-up#test-env).

For an overview of the full set of source files included in the LVL, see[Summary of LVL Classes and Interfaces](https://developer.android.com/google/play/licensing/licensing-reference#lvl-summary).

## Adding the Licensing Permission

To use the Google Play application for sending a license check to the server, your application must request the proper permission,`com.android.vending.CHECK_LICENSE`. If your application does not declare the licensing permission but attempts to initiate a license check, the LVL throws a security exception.

To request the licensing permission in your application, declare a[`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)element as a child of`<manifest>`, as follows:

`<uses-permission
android:name="com.android.vending.CHECK_LICENSE" />`

For example, here's how the LVL sample application declares the permission:  

```xml
<?xml version="1.0" encoding="utf-8"?>

<manifest xmlns:android="http://schemas.android.com/apk/res/android" ...">
    <!-- Devices >= 3 have version of Google Play that supports licensing. -->
    <uses-sdk android:minSdkVersion="3" />
    <!-- Required permission to check licensing. -->
    <uses-permission android:name="com.android.vending.CHECK_LICENSE" />
    ...
</manifest>
```

**Note:** Currently, you cannot declare the`CHECK_LICENSE`permission in the LVL library project's manifest, because the SDK Tools will not merge it into the manifests of dependent applications. Instead, you must declare the permission in each dependent application's manifest.

## Implementing a Policy

Google Play licensing service doesn't itself determine whether a given user with a given license should be granted access to your application. Rather, that responsibility is left to a`Policy`implementation that you provide in your application.

Policy is an interface declared by the LVL that is designed to hold your application's logic for allowing or disallowing user access, based on the result of a license check. To use the LVL, your application*must* provide an implementation of`Policy`.

The`Policy`interface declares two methods,`allowAccess()`and`processServerResponse()`, which are called by a`LicenseChecker`instance when processing a response from the license server. It also declares an enum called`LicenseResponse`, which specifies the license response value passed in calls to`processServerResponse()`.

- `processServerResponse()`lets you preprocess the raw response data received from the licensing server, prior to determining whether to grant access.

  A typical implementation would extract some or all fields from the license response and store the data locally to a persistent store, such as through[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)storage, to ensure that the data is accessible across application invocations and device power cycles. For example, a`Policy`would maintain the timestamp of the last successful license check, the retry count, the license validity period, and similar information in a persistent store, rather than resetting the values each time the application is launched.

  When storing response data locally, the`Policy`must ensure that the data is obfuscated (see[Implementing an Obfuscator](https://developer.android.com/google/play/licensing/client-side-verification#impl-Obfuscator), below).
- `allowAccess()`determines whether to grant the user access to your application, based on any available license response data (from the licensing server or from cache) or other application-specific information. For example, your implementation of`allowAccess()`could take into account additional criteria, such as usage or other data retrieved from a backend server. In all cases, an implementation of`allowAccess()`should only return`true`if the user is licensed to use the application, as determined by the licensing server, or if there is a transient network or system problem that prevents the license check from completing. In such cases, your implementation can maintain a count of retry responses and provisionally allow access until the next license check is complete.

To simplify the process of adding licensing to your application and to provide an illustration of how a`Policy`should be designed, the LVL includes two full`Policy`implementations that you can use without modification or adapt to your needs:

- [ServerManagedPolicy](https://developer.android.com/google/play/licensing/client-side-verification#ServerManagedPolicy), a flexible`Policy`that uses server-provided settings and cached responses to manage access across varied network conditions, and
- [StrictPolicy](https://developer.android.com/google/play/licensing/client-side-verification#StrictPolicy), which doesn't cache any response data and allows access*only*if the server returns a licensed response.

For most applications, the use of ServerManagedPolicy is highly recommended. ServerManagedPolicy is the LVL default and is integrated with the LVL sample application.

### Guidelines for custom policies

In your licensing implementation, you can use one of the complete policies provided in the LVL (ServerManagedPolicy or StrictPolicy) or you can create a custom policy. For any type of custom policy, there are several important design points to understand and account for in your implementation.

The licensing server applies general request limits to guard against overuse of resources that could result in denial of service. When an application exceeds the request limit, the licensing server returns a 503 response, which gets passed through to your application as a general server error. This means that no license response will be available to the user until the limit is reset, which can affect the user for an indefinite period.

If you are designing a custom policy, we recommend that the`Policy`:

1. Caches (and properly obfuscates) the most recent successful license response in local persistent storage.
2. Returns the cached response for all license checks, for as long as the cached response is valid, rather than making a request to the licensing server. Setting the response validity according to the server-provided`VT`extra is highly recommended. See[Server Response Extras](https://developer.android.com/google/play/licensing/licensing-reference#extras)for more information.
3. Uses an exponential backoff period, if retrying any requests the result in errors. Note that the Google Play client automatically retries failed requests, so in most cases there is no need for your`Policy`to retry them.
4. Provides for a "grace period" that allows the user to access your application for a limited time or number of uses, while a license check is being retried. The grace period benefits the user by allowing access until the next license check can be completed successfully and it benefits you by placing a hard limit on access to your application when there is no valid license response available.

Designing your`Policy`according to the guidelines listed above is critical, because it ensures the best possible experience for users while giving you effective control over your application even in error conditions.

Note that any`Policy`can use settings provided by the licensing server to help manage validity and caching, retry grace period, and more. Extracting the server-provided settings is straightforward and making use of them is highly recommended. See the ServerManagedPolicy implementation for an example of how to extract and use the extras. For a list of server settings and information about how to use them, see[Server Response Extras](https://developer.android.com/google/play/licensing/licensing-reference#extras).

### ServerManagedPolicy

The LVL includes a full and recommended implementation of the`Policy`interface called ServerManagedPolicy. The implementation is integrated with the LVL classes and serves as the default`Policy`in the library.

ServerManagedPolicy provides all of the handling for license and retry responses. It caches all of the response data locally in a[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)file, obfuscating it with the application's`Obfuscator`implementation. This ensures that the license response data is secure and persists across device power cycles. ServerManagedPolicy provides concrete implementations of the interface methods`processServerResponse()`and`allowAccess()`and also includes a set of supporting methods and types for managing license responses.

Importantly, a key feature of ServerManagedPolicy is its use of server-provided settings as the basis for managing licensing across an application's refund period and through varying network and error conditions. When an application contacts the Google Play server for a license check, the server appends several settings as key-value pairs in the extras field of certain license response types. For example, the server provides recommended values for the application's license validity period, retry grace period, and maximum allowable retry count, among others. ServerManagedPolicy extracts the values from the license response in its`processServerResponse()`method and checks them in its`allowAccess()`method. For a list of the server-provided settings used by ServerManagedPolicy, see[Server Response Extras](https://developer.android.com/google/play/licensing/licensing-reference#extras).

For convenience, best performance, and the benefit of using license settings from the Google Play server,**using ServerManagedPolicy as your licensing`Policy`is strongly recommended**.

If you are concerned about the security of license response data that is stored locally in[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences), you can use a stronger obfuscation algorithm or design a stricter`Policy`that doesn't store license data. The LVL includes an example of such a`Policy`--- see[StrictPolicy](https://developer.android.com/google/play/licensing/client-side-verification#StrictPolicy)for more information.

To use ServerManagedPolicy, simply import it to your Activity, create an instance, and pass a reference to the instance when constructing your`LicenseChecker`. See[Instantiate LicenseChecker and LicenseCheckerCallback](https://developer.android.com/google/play/licensing/client-side-verification#lc-lcc)for more information.

### StrictPolicy

The LVL includes an alternative full implementation of the`Policy`interface called StrictPolicy. The StrictPolicy implementation provides a more restrictive Policy than ServerManagedPolicy, in that it doesn't allow the user to access the application unless a license response is received from the server at the time of access that indicates that the user is licensed.

The principal feature of StrictPolicy is that it doesn't store*any* license response data locally, in a persistent store. Because no data is stored, retry requests aren't tracked and cached responses cannot be used to fulfill license checks. The`Policy`allows access only if:

- The license response is received from the licensing server, and
- The license response indicates that the user is licensed to access the application.

Using StrictPolicy is appropriate if your primary concern is to ensure that, in all possible cases, no user will be allowed to access the application unless the user is confirmed to be licensed at the time of use. Additionally, the Policy offers slightly more security than ServerManagedPolicy --- since there is no data cached locally, there is no way a malicious user could tamper with the cached data and obtain access to the application.

At the same time, this`Policy`presents a challenge for normal users, since it means that they won't be able to access the application when there is no network (cell or Wi-Fi) connection available. Another side-effect is that your application will send more license check requests to the server, since using a cached response isn't possible.

Overall, this policy represents a tradeoff of some degree of user convenience for absolute security and control over access. Consider the tradeoff carefully before using this`Policy`.

To use StrictPolicy, simply import it to your Activity, create an instance, and pass a reference to it when constructing your`LicenseChecker`. See[Instantiate LicenseChecker and LicenseCheckerCallback](https://developer.android.com/google/play/licensing/client-side-verification#lc-lcc)for more information.

A typical`Policy`implementation needs to save the license response data for an application to a persistent store, so that it is accessible across application invocations and device power cycles. For example, a`Policy`would maintain the timestamp of the last successful license check, the retry count, the license validity period, and similar information in a persistent store, rather than resetting the values each time the application is launched. The default`Policy`included in the LVL, ServerManagedPolicy, stores license response data in a[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)instance, to ensure that the data is persistent.

Because the`Policy`will use stored license response data to determine whether to allow or disallow access to the application, it*must* ensure that any stored data is secure and cannot be reused or manipulated by a root user on a device. Specifically, the`Policy`must always obfuscate the data before storing it, using a key that is unique for the application and device. Obfuscating using a key that is both application-specific and device-specific is critical, because it prevents the obfuscated data from being shared among applications and devices.

The LVL assists the application with storing its license response data in a secure, persistent manner. First, it provides an`Obfuscator`interface that lets your application supply the obfuscation algorithm of its choice for stored data. Building on that, the LVL provides the helper class PreferenceObfuscator, which handles most of the work of calling the application's`Obfuscator`class and reading and writing the obfuscated data in a[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)instance.

The LVL provides a full`Obfuscator`implementation called AESObfuscator that uses AES encryption to obfuscate data. You can use AESObfuscator in your application without modification or you can adapt it to your needs. If you are using a`Policy`(such as ServerManagedPolicy) that caches license response data, using AESObfuscator as basis for your`Obfuscator`implementation is highly recommended. For more information, see the next section.

### AESObfuscator

The LVL includes a full and recommended implementation of the`Obfuscator`interface called AESObfuscator. The implementation is integrated with the LVL sample application and serves as the default`Obfuscator`in the library.

AESObfuscator provides secure obfuscation of data by using AES to encrypt and decrypt the data as it is written to or read from storage. The`Obfuscator`seeds the encryption using three data fields provided by the application:

1. A salt --- an array of random bytes to use for each (un)obfuscation.
2. An application identifier string, typically the package name of the application.
3. A device identifier string, derived from as many device-specific sources as possible, so as to make it as unique.

To use AESObfuscator, first import it to your Activity. Declare a private static final array to hold the salt bytes and initialize it to 20 randomly generated bytes.  

### Kotlin

```kotlin
// Generate 20 random bytes, and put them here.
private val SALT = byteArrayOf(
        -46, 65, 30, -128, -103, -57, 74, -64, 51, 88,
        -95, -45, 77, -117, -36, -113, -11, 32, -64, 89
)
```

### Java

```java
...
    // Generate 20 random bytes, and put them here.
    private static final byte[] SALT = new byte[] {
     -46, 65, 30, -128, -103, -57, 74, -64, 51, 88, -95,
     -45, 77, -117, -36, -113, -11, 32, -64, 89
     };
    ...
```

Next, declare a variable to hold a device identifier and generate a value for it in any way needed. For example, the sample application included in the LVL queries the system settings for the`android.Settings.Secure.ANDROID_ID`, which is unique to each device.

Note that, depending on the APIs you use, your application might need to request additional permissions in order to acquire device-specific information. For example, to query the[TelephonyManager](https://developer.android.com/reference/android/telephony/TelephonyManager)to obtain the device IMEI or related data, the application will also need to request the`android.permission.READ_PHONE_STATE`permission in its manifest.

Before requesting new permissions for the*sole purpose* of acquiring device-specific information for use in your`Obfuscator`, consider how doing so might affect your application or its filtering on Google Play (since some permissions can cause the SDK build tools to add the associated`<uses-feature>`).

Finally, construct an instance of AESObfuscator, passing the salt, application identifier, and device identifier. You can construct the instance directly, while constructing your`Policy`and`LicenseChecker`. For example:  

### Kotlin

```kotlin
    ...
    // Construct the LicenseChecker with a Policy.
    private val checker = LicenseChecker(
            this,
            ServerManagedPolicy(this, AESObfuscator(SALT, packageName, deviceId)),
            BASE64_PUBLIC_KEY
    )
    ...
```

### Java

```java
    ...
    // Construct the LicenseChecker with a Policy.
    checker = new LicenseChecker(
        this, new ServerManagedPolicy(this,
            new AESObfuscator(SALT, getPackageName(), deviceId)),
        BASE64_PUBLIC_KEY // Your public licensing key.
        );
    ...
```

For a complete example, see MainActivity in the LVL sample application.

## Checking the License from an Activity

Once you've implemented a`Policy`for managing access to your application, the next step is to add a license check to your application, which initiates a query to the licensing server if needed and manages access to the application based on the license response. All of the work of adding the license check and handling the response takes place in your main[Activity](https://developer.android.com/reference/android/app/Activity)source file.

To add the license check and handle the response, you must:

1. [Add imports](https://developer.android.com/google/play/licensing/client-side-verification#imports)
2. [Implement LicenseCheckerCallback](https://developer.android.com/google/play/licensing/client-side-verification#lc-impl)as a private inner class
3. [Create a Handler](https://developer.android.com/google/play/licensing/client-side-verification#thread-handler)for posting from LicenseCheckerCallback to the UI thread
4. [Instantiate LicenseChecker](https://developer.android.com/google/play/licensing/client-side-verification#lc-lcc)and LicenseCheckerCallback
5. [Call checkAccess()](https://developer.android.com/google/play/licensing/client-side-verification#check-access)to initiate the license check
6. [Embed your public key](https://developer.android.com/google/play/licensing/client-side-verification#account-key)for licensing
7. [Call your LicenseChecker's onDestroy() method](https://developer.android.com/google/play/licensing/client-side-verification#handler-cleanup)to close IPC connections.

The sections below describe these tasks.

### Overview of license check and response

In most cases, you should add the license check to your application's main[Activity](https://developer.android.com/reference/android/app/Activity), in the[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method. This ensures that when the user launches your application directly, the license check will be invoked immediately. In some cases, you can add license checks in other locations as well. For example, if your application includes multiple Activity components that other applications can start by[Intent](https://developer.android.com/reference/android/content/Intent), you could add license checks in those Activities.

A license check consists of two main actions:

- A call to a method to initiate the license check --- in the LVL, this is a call to the`checkAccess()`method of a`LicenseChecker`object that you construct.
- A callback that returns the result of the license check. In the LVL, this is a`LicenseCheckerCallback`interface that you implement. The interface declares two methods,`allow()`and`dontAllow()`, which are invoked by the library based on to the result of the license check. You implement these two methods with whatever logic you need, to allow or disallow the user access to your application. Note that these methods don't determine*whether* to allow access --- that determination is the responsibility of your`Policy`implementation. Rather, these methods simply provide the application behaviors for*how* to allow and disallow access (and handle application errors).

  The`allow()`and`dontAllow()`methods do provide a "reason" for their response, which can be one of the`Policy`values,`LICENSED`,`NOT_LICENSED`, or`RETRY`. In particular, you should handle the case in which the method receives the`RETRY`response for`dontAllow()`and provide the user with an "Retry" button, which might have happened because the service was unavailable during the request.

![](https://developer.android.com/static/images/licensing_flow.png)  
**Figure 1.**Overview of a typical license check interaction.

The diagram above illustrates how a typical license check takes place:

1. Code in the application's main Activity instantiates`LicenseCheckerCallback`and`LicenseChecker`objects. When constructing`LicenseChecker`, the code passes in[Context](https://developer.android.com/reference/android/content/Context), a`Policy`implementation to use, and the publisher account's public key for licensing as parameters.
2. The code then calls the`checkAccess()`method on the`LicenseChecker`object. The method implementation calls the`Policy`to determine whether there is a valid license response cached locally, in[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences).
   - If so, the`checkAccess()`implementation calls`allow()`.
   - Otherwise, the`LicenseChecker`initiates a license check request that is sent to the licensing server.

   **Note:** The licensing server always returns`LICENSED`when you perform a license check of a draft application.
3. When a response is received,`LicenseChecker`creates a LicenseValidator that verifies the signed license data and extracts the fields of the response, then passes them to your`Policy`for further evaluation.
   - If the license is valid, the`Policy`caches the response in[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)and notifies the validator, which then calls the`allow()`method on the`LicenseCheckerCallback`object.
   - If the license not valid, the`Policy`notifies the validator, which calls the`dontAllow()`method on`LicenseCheckerCallback`.
4. In case of a recoverable local or server error, such as when the network is not available to send the request,`LicenseChecker`passes a`RETRY`response to your`Policy`object's`processServerResponse()`method.

   Also, both the`allow()`and`dontAllow()`callback methods receive a`reason`argument. The`allow()`method's reason is usually`Policy.LICENSED`or`Policy.RETRY`and the`dontAllow()`reason is usually`Policy.NOT_LICENSED`or`Policy.RETRY`. These response values are useful so you can show an appropriate response for the user, such as by providing a "Retry" button when`dontAllow()`responds with`Policy.RETRY`, which might have been because the service was unavailable.
5. In case of a application error, such as when the application attempts to check the license of an invalid package name,`LicenseChecker`passes an error response to the LicenseCheckerCallback's`applicationError()`method.

Note that, in addition to initiating the license check and handling the result, which are described in the sections below, your application also needs to provide a[Policy implementation](https://developer.android.com/google/play/licensing/client-side-verification#impl-Policy)and, if the`Policy`stores response data (such as ServerManagedPolicy), an[Obfuscator](https://developer.android.com/google/play/licensing/client-side-verification#impl-Obfuscator)implementation.

### Add imports

First, open the class file of the application's main Activity and import`LicenseChecker`and`LicenseCheckerCallback`from the LVL package.  

### Kotlin

```kotlin
import com.google.android.vending.licensing.LicenseChecker
import com.google.android.vending.licensing.LicenseCheckerCallback
```

### Java

```java
import com.google.android.vending.licensing.LicenseChecker;
import com.google.android.vending.licensing.LicenseCheckerCallback;
```

If you are using the default`Policy`implementation provided with the LVL, ServerManagedPolicy, import it also, together with the AESObfuscator. If you are using a custom`Policy`or`Obfuscator`, import those instead.  

### Kotlin

```kotlin
import com.google.android.vending.licensing.ServerManagedPolicy
import com.google.android.vending.licensing.AESObfuscator
```

### Java

```java
import com.google.android.vending.licensing.ServerManagedPolicy;
import com.google.android.vending.licensing.AESObfuscator;
```

### Implement LicenseCheckerCallback as a private inner class

`LicenseCheckerCallback`is an interface provided by the LVL for handling result of a license check. To support licensing using the LVL, you must implement`LicenseCheckerCallback`and its methods to allow or disallow access to the application.

The result of a license check is always a call to one of the`LicenseCheckerCallback`methods, made based on the validation of the response payload, the server response code itself, and any additional processing provided by your`Policy`. Your application can implement the methods in any way needed. In general, it's best to keep the methods simple, limiting them to managing UI state and application access. If you want to add further processing of license responses, such as by contacting a backend server or applying custom constraints, you should consider incorporating that code into your`Policy`, rather than putting it in the`LicenseCheckerCallback`methods.

In most cases, you should declare your implementation of`LicenseCheckerCallback`as a private class inside your application's main Activity class.

Implement the`allow()`and`dontAllow()`methods as needed. To start with, you can use simple result-handling behaviors in the methods, such as displaying the license result in a dialog. This helps you get your application running sooner and can assist with debugging. Later, after you have determined the exact behaviors you want, you can add more complex handling.

Some suggestions for handling unlicensed responses in`dontAllow()`include:

- Display a "Try again" dialog to the user, including a button to initiate a new license check if the`reason`supplied is`Policy.RETRY`.
- Display a "Purchase this application" dialog, including a button that deep-links the user to the application's details page on Google Play, from which the use can purchase the application. For more information on how to set up such links, see[Linking to Your Products](https://developer.android.com/distribute/tools/promote/linking).
- Display a Toast notification that indicates that the features of the application are limited because it isn't licensed.

The example below shows how the LVL sample application implements`LicenseCheckerCallback`, with methods that display the license check result in a dialog.  

### Kotlin

```kotlin
private inner class MyLicenseCheckerCallback : LicenseCheckerCallback {

    override fun allow(reason: Int) {
        if (isFinishing) {
            // Don't update UI if Activity is finishing.
            return
        }
        // Should allow user access.
        displayResult(getString(R.string.allow))
    }

    override fun dontAllow(reason: Int) {
        if (isFinishing) {
            // Don't update UI if Activity is finishing.
            return
        }
        displayResult(getString(R.string.dont_allow))

        if (reason == Policy.RETRY) {
            // If the reason received from the policy is RETRY, it was probably
            // due to a loss of connection with the service, so we should give the
            // user a chance to retry. So show a dialog to retry.
            showDialog(DIALOG_RETRY)
        } else {
            // Otherwise, the user isn't licensed to use this app.
            // Your response should always inform the user that the application
            // isn't licensed, but your behavior at that point can vary. You might
            // provide the user a limited access version of your app or you can
            // take them to Google Play to purchase the app.
            showDialog(DIALOG_GOTOMARKET)
        }
    }
}
```

### Java

```java
private class MyLicenseCheckerCallback implements LicenseCheckerCallback {
    public void allow(int reason) {
        if (isFinishing()) {
            // Don't update UI if Activity is finishing.
            return;
        }
        // Should allow user access.
        displayResult(getString(R.string.allow));
    }

    public void dontAllow(int reason) {
        if (isFinishing()) {
            // Don't update UI if Activity is finishing.
            return;
        }
        displayResult(getString(R.string.dont_allow));

        if (reason == Policy.RETRY) {
            // If the reason received from the policy is RETRY, it was probably
            // due to a loss of connection with the service, so we should give the
            // user a chance to retry. So show a dialog to retry.
            showDialog(DIALOG_RETRY);
        } else {
            // Otherwise, the user isn't licensed to use this app.
            // Your response should always inform the user that the application
            // isn't licensed, but your behavior at that point can vary. You might
            // provide the user a limited access version of your app or you can
            // take them to Google Play to purchase the app.
            showDialog(DIALOG_GOTOMARKET);
        }
    }
}
```

Additionally, you should implement the`applicationError()`method, which the LVL calls to let your application handle errors that are not retryable. For a list of such errors, see[Server Response Codes](https://developer.android.com/google/play/licensing/licensing-reference#server-response-codes)in the[Licensing Reference](https://developer.android.com/google/play/licensing/licensing-reference). You can implement the method in any way needed. In most cases, the method should log the error code and call`dontAllow()`.

### Create a Handler for posting from LicenseCheckerCallback to the UI thread

During a license check, the LVL passes the request to the Google Play application, which handles communication with the licensing server. The LVL passes the request over asynchronous IPC (using[Binder](https://developer.android.com/reference/android/os/Binder)) so the actual processing and network communication don't take place on a thread managed by your application. Similarly, when the Google Play application receives the result, it invokes a callback method over IPC, which in turn executes in an IPC thread pool in your application's process.

The`LicenseChecker`class manages your application's IPC communication with the Google Play application, including the call that sends the request and the callback that receives the response.`LicenseChecker`also tracks open license requests and manages their timeouts.

So that it can handle timeouts properly and also process incoming responses without affecting your application's UI thread,`LicenseChecker`spawns a background thread at instantiation. In the thread it does all processing of license check results, whether the result is a response received from the server or a timeout error. At the conclusion of processing, the LVL calls your`LicenseCheckerCallback`methods from the background thread.

To your application, this means that:

1. Your`LicenseCheckerCallback`methods will be invoked, in many cases, from a background thread.
2. Those methods won't be able to update state or invoke any processing in the UI thread, unless you create a Handler in the UI thread and have your callback methods post to the Handler.

If you want your`LicenseCheckerCallback`methods to update the UI thread, instantiate a[Handler](https://developer.android.com/reference/android/os/Handler)in the main Activity's[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method, as shown below. In this example, the LVL sample application's`LicenseCheckerCallback`methods (see above) call`displayResult()`to update the UI thread through the Handler's[post()](https://developer.android.com/reference/android/os/Handler#post(java.lang.Runnable))method.  

### Kotlin

```kotlin
    private lateinit var handler: Handler

    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        handler = Handler()
    }
```

### Java

```java
    private Handler handler;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        ...
        handler = new Handler();
    }
```

Then, in your`LicenseCheckerCallback`methods, you can use Handler methods to post Runnable or Message objects to the Handler. Here's how the sample application included in the LVL posts a Runnable to a Handler in the UI thread to display the license status.  

### Kotlin

```kotlin
private fun displayResult(result: String) {
    handler.post {
        statusText.text = result
        setProgressBarIndeterminateVisibility(false)
        checkLicenseButton.isEnabled = true
    }
}
```

### Java

```java
private void displayResult(final String result) {
        handler.post(new Runnable() {
            public void run() {
                statusText.setText(result);
                setProgressBarIndeterminateVisibility(false);
                checkLicenseButton.setEnabled(true);
            }
        });
    }
```

### Instantiate LicenseChecker and LicenseCheckerCallback

In the main Activity's[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method, create private instances of LicenseCheckerCallback and`LicenseChecker`. You must instantiate`LicenseCheckerCallback`first, because you need to pass a reference to that instance when you call the constructor for`LicenseChecker`.

When you instantiate`LicenseChecker`, you need to pass in these parameters:

- The application[Context](https://developer.android.com/reference/android/content/Context)
- A reference to the`Policy`implementation to use for the license check. In most cases, you would use the default`Policy`implementation provided by the LVL, ServerManagedPolicy.
- The String variable holding your publisher account's public key for licensing.

If you are using ServerManagedPolicy, you won't need to access the class directly, so you can instantiate it in the`LicenseChecker`constructor, as shown in the example below. Note that you need to pass a reference to a new Obfuscator instance when you construct ServerManagedPolicy.

The example below shows the instantiation of`LicenseChecker`and`LicenseCheckerCallback`from the`onCreate()`method of an Activity class.  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {
    ...
    private lateinit var licenseCheckerCallback: LicenseCheckerCallback
    private lateinit var checker: LicenseChecker

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ...
        // Construct the LicenseCheckerCallback. The library calls this when done.
        licenseCheckerCallback = MyLicenseCheckerCallback()

        // Construct the LicenseChecker with a Policy.
        checker = LicenseChecker(
                this,
                ServerManagedPolicy(this, AESObfuscator(SALT, packageName, deviceId)),
                BASE64_PUBLIC_KEY // Your public licensing key.
        )
        ...
    }
}
```

### Java

```java
public class MainActivity extends Activity {
    ...
    private LicenseCheckerCallback licenseCheckerCallback;
    private LicenseChecker checker;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        // Construct the LicenseCheckerCallback. The library calls this when done.
        licenseCheckerCallback = new MyLicenseCheckerCallback();

        // Construct the LicenseChecker with a Policy.
        checker = new LicenseChecker(
            this, new ServerManagedPolicy(this,
                new AESObfuscator(SALT, getPackageName(), deviceId)),
            BASE64_PUBLIC_KEY // Your public licensing key.
            );
        ...
    }
}
```

Note that`LicenseChecker`calls the`LicenseCheckerCallback`methods from the UI thread*only*if there is valid license response cached locally. If the license check is sent to the server, the callbacks always originate from the background thread, even for network errors.

### Call checkAccess() to initiate the license check

In your main Activity, add a call to the`checkAccess()`method of the`LicenseChecker`instance. In the call, pass a reference to your`LicenseCheckerCallback`instance as a parameter. If you need to handle any special UI effects or state management before the call, you might find it useful to call`checkAccess()`from a wrapper method. For example, the LVL sample application calls`checkAccess()`from a`doCheck()`wrapper method:  

### Kotlin

```kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ...
        // Call a wrapper method that initiates the license check
        doCheck()
        ...
    }
    ...
    private fun doCheck() {
        checkLicenseButton.isEnabled = false
        setProgressBarIndeterminateVisibility(true)
        statusText.setText(R.string.checking_license)
        checker.checkAccess(licenseCheckerCallback)
    }
```

### Java

```java
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ...
        // Call a wrapper method that initiates the license check
        doCheck();
        ...
    }
    ...
    private void doCheck() {
        checkLicenseButton.setEnabled(false);
        setProgressBarIndeterminateVisibility(true);
        statusText.setText(R.string.checking_license);
        checker.checkAccess(licenseCheckerCallback);
    }
```

### Embed your public key for licensing

For each application, the Google Play service automatically generates a 2048-bit RSA public/private key pair that is used for licensing and in-app billing. The key pair is uniquely associated with the application. Although associated with the application, the key pair is*not*the same as the key that you use to sign your applications (or derived from it).

The Google Play Console exposes the public key for licensing to any developer signed in to the Play Console, but it keeps the private key hidden from all users in a secure location. When an application requests a license check for an application published in your account, the licensing server signs the license response using the private key of your application's key pair. When the LVL receives the response, it uses the public key provided by the application to verify the signature of the license response.

To add licensing to an application, you must obtain your application's public key for licensing and copy it into your application. Here's how to find your application's public key for licensing:

1. Go to the Google[Play Console](http://play.google.com/apps/publish)and sign in. Make sure that you sign in to the account from which the application you are licensing is published (or will be published).
2. In the application details page, locate the**Services \& APIs**link and click it.
3. In the**Services \& APIs** page, locate the**Licensing \& In-App Billing** section. Your public key for licensing is given in the**Your License Key For This Application**field.

To add the public key to your application, simply copy/paste the key string from the field into your application as the value of the String variable`BASE64_PUBLIC_KEY`. When you are copying, make sure that you have selected the entire key string, without omitting any characters.

Here's an example from the LVL sample application:  

### Kotlin

```kotlin
private const val BASE64_PUBLIC_KEY = "MIIBIjANBgkqhkiG ... " //truncated for this example
class LicensingActivity : AppCompatActivity() {
    ...
}
```

### Java

```java
public class MainActivity extends Activity {
    private static final String BASE64_PUBLIC_KEY = "MIIBIjANBgkqhkiG ... "; //truncated for this example
    ...
}
```

### Call your LicenseChecker's onDestroy() method to close IPC connections

Finally, to let the LVL clean up before your application[Context](https://developer.android.com/reference/android/content/Context)changes, add a call to the`LicenseChecker`'s`onDestroy()`method from your Activity's[onDestroy()](https://developer.android.com/reference/android/app/Activity#onDestroy())implementation. The call causes the`LicenseChecker`to properly close any open IPC connection to the Google Play application's ILicensingService and removes any local references to the service and handler.

Failing to call the`LicenseChecker`'s`onDestroy()`method can lead to problems over the lifecycle of your application. For example, if the user changes screen orientation while a license check is active, the application[Context](https://developer.android.com/reference/android/content/Context)is destroyed. If your application does not properly close the`LicenseChecker`'s IPC connection, your application will crash when the response is received. Similarly, if the user exits your application while a license check is in progress, your application will crash when the response is received, unless it has properly called the`LicenseChecker`'s`onDestroy()`method to disconnect from the service.

Here's an example from the sample application included in the LVL, where`mChecker`is the`LicenseChecker`instance:  

### Kotlin

```kotlin
    override fun onDestroy() {
        super.onDestroy()
        checker.onDestroy()
        ...
    }
```

### Java

```java
    @Override
    protected void onDestroy() {
        super.onDestroy();
        checker.onDestroy();
        ...
    }
```

If you are extending or modifying`LicenseChecker`, you might also need to call the`LicenseChecker`'s`finishCheck()`method, to clean up any open IPC connections.

## Implementing a DeviceLimiter

In some cases, you might want your`Policy`to limit the number of actual devices that are permitted to use a single license. This would prevent a user from moving a licensed application onto a number of devices and using the application on those devices under the same account ID. It would also prevent a user from "sharing" the application by providing the account information associated with the license to other individuals, who could then sign in to that account on their devices and access the license to the application.

The LVL supports per-device licensing by providing a`DeviceLimiter`interface, which declares a single method,`allowDeviceAccess()`. When a LicenseValidator is handling a response from the licensing server, it calls`allowDeviceAccess()`, passing a user ID string extracted from the response.

If you don't want to support device limitation,**no work is required** --- the`LicenseChecker`class automatically uses a default implementation called NullDeviceLimiter. As the name suggests, NullDeviceLimiter is a "no-op" class whose`allowDeviceAccess()`method simply returns a`LICENSED`response for all users and devices.  
**Caution:** Per-device licensing is*not recommended for most applications*because:

- It requires that you provide a backend server to manage a users and devices mapping, and
- It could inadvertently result in a user being denied access to an application that they have legitimately purchased on another device.

## Obfuscating Your Code

To ensure the security of your application, particularly for a paid application that uses licensing and/or custom constraints and protections, it's very important to obfuscate your application code. Properly obfuscating your code makes it more difficult for a malicious user to decompile the application's bytecode, modify it --- such as by removing the license check --- and then recompile it.

Several obfuscator programs are available for Android applications, including[ProGuard](http://proguard.sourceforge.net/), which also offers code-optimization features. The use of ProGuard or a similar program to obfuscate your code is*strongly recommended*for all applications that use Google Play Licensing.

## Publishing a Licensed Application

When you are finished testing your license implementation, you are ready to publish the application on Google Play. Follow the normal steps to[prepare](https://developer.android.com/tools/publishing/preparing),[sign](https://developer.android.com/tools/publishing/app-signing), and then[publish the application](https://developer.android.com/distribute/tools/launch-checklist).

## Where to Get Support

If you have questions or encounter problems while implementing or deploying publishing in your applications, please use the support resources listed in the table below. By directing your queries to the correct forum, you can get the support you need more quickly.

**Table 2.**Developer support resources for Google Play Licensing Service.

|                Support Type                 |                                           Resource                                            |                                                                     Range of Topics                                                                      |
|---------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Development and testing issues              | Google Groups:[android-developers](http://groups.google.com/group/android-developers)         | LVL download and integration, library projects,`Policy`questions, user experience ideas, handling of responses,`Obfuscator`, IPC, test environment setup |
| Development and testing issues              | Stack Overflow:<http://stackoverflow.com/questions/tagged/android>                            | LVL download and integration, library projects,`Policy`questions, user experience ideas, handling of responses,`Obfuscator`, IPC, test environment setup |
| Accounts, publishing, and deployment issues | [Google Play Help Forum](http://www.google.com/support/forum/p/Android+Market)                | Publisher accounts, licensing key pair, test accounts, server responses, test responses, application deployment and results                              |
| Accounts, publishing, and deployment issues | [Market Licensing Support FAQ](http://market.android.com/support/bin/answer.py?answer=186113) | Publisher accounts, licensing key pair, test accounts, server responses, test responses, application deployment and results                              |
| LVL issue tracker                           | [Marketlicensing project issue tracker](http://code.google.com/p/marketlicensing/issues/)     | Bug and issue reports related specifically to the LVL source code classes and interface implementations                                                  |

For general information about how to post to the groups listed above, see[Community Resources](https://developer.android.com/resources/community-groups)section on the Developer Support Resources page.

## Additional Resources

The sample application included with the LVL provides a full example of how to initiate a license check and handle the result, in the`MainActivity`class.