---
title: https://developer.android.com/google/play/licensing/overview
url: https://developer.android.com/google/play/licensing/overview
source: md.txt
---

# Licensing Overview

Google Play Licensing is a network-based service that lets an application query a trusted Google Play licensing server to determine whether the application is licensed to the current device user. The licensing service is based on the capability of the Google Play licensing server to determine whether a given user is licensed to use a given application. Google Play considers a user to be licensed if the user is a recorded purchaser of the application.

The request starts when your application makes a request to a service hosted by the Google Play client application. The Google Play application then sends a request to the licensing server and receives the result. The Google Play application sends the result to your application, which can allow or disallow further use of the application as needed.

**Note:** If a version of an app is in the closed or open testing tracks, all users who are authorized to download and install that app are considered to be licensed users of the app. For more information, see[Use testing tracks to get invaluable early feedback from users](https://developer.android.com/distribute/best-practices/launch/test-tracks).  
![](https://developer.android.com/static/images/google/play/licensing/licensing_arch.png)

**Figure 1.**Your application initiates a license check through the License Verification Library and the Google Play client, which handles communication with the Google Play server.

**Note:** Previously you could test an app by uploading an unpublished "draft" version. This functionality is no longer supported; instead, you must publish it to the closed or open testing tracks. For more information, see[Draft Apps are No Longer Supported](https://developer.android.com/google/play/billing/billing_testing#draft_apps).

To properly identify the user and determine the license status, the licensing server requires information about the application and user---your application and the Google Play client work together to assemble the information and the Google Play client passes it to the server.

To help you add licensing to your application, the Android SDK provides a downloadable set of library sources that you can include in your application project: the Google Market Licensing package. The License Verification Library (LVL) is a library you can add to your application that handles all of the licensing-related communication with the Google Play licensing service. With the LVL added to your application, your application can determine its licensing status for the current user by simply calling a method and implementing a callback that receives the status response.

Your application does not query the licensing server directly, but instead calls the Google Play client over remote IPC to initiate a license request. In the license request:

- Your application provides: its package name, a nonce that is later used to validate any response from the server, and a callback over which the response can be returned asynchronously.
- The Google Play client collects the necessary information about the user and the device, such as the device's primary Google Account username, IMSI, and other information. It then sends the license check request to the server on behalf of your application.
- The Google Play server evaluates the request using all available information, attempting to establish the user's identity to a sufficient level of confidence. The server then checks the user identity against purchase records for your application and returns a license response, which the Google Play client returns to your application over the IPC callback.

You can choose when, and how often, you want your application to check its license and you have full control over how it handles the response, verifies the signed response data, and enforces access controls.

Notice that during a license check, your application does not manage any network connections or use any licensing related APIs in the Android platform.

## License Responses are Secure

To ensure the integrity of each license query, the server signs the license response data using an RSA key pair that is shared exclusively between the Google Play server and you.

The licensing service generates a single licensing key pair for each application and exposes the public key in your application's**Services \& APIs**page in the Play Console. You must copy the public key from the Play Console and embed it in your application source code. The server retains the private key internally and uses it to sign license responses for the applications you publish with that account.

When your application receives a signed response, it uses the embedded public key to verify the data. The use of public key cryptography in the licensing service makes it possible for the application to detect responses that have been tampered with or that are spoofed.

## Licensing Verification Library

The Android SDK provides a downloadable package called the Google Market Licensing package, which includes the License Verification Library (LVL). The LVL greatly simplifies the process of adding licensing to your application and helps ensure a more secure, robust implementation for your application. The LVL provides internal classes that handle most of the standard operations of a license query, such as contacting the Google Play client to initiate a license request and verifying and validating the responses. It also exposes interfaces that let you easily plug in your custom code for defining licensing policy and managing access as needed by your application. The key LVL interfaces are:

`Policy`
:   Your implementation determines whether to allow access to the application, based on the license response received from the server and any other data available (such as from a backend server associated with your application). The implementation can evaluate the various fields of the license response and apply other constraints, if needed. The implementation also lets you manage the handling of license checks that result in errors, such as network errors.

`LicenseCheckerCallback`
:   Your implementation manages access to the application, based on the result of the`Policy`object's handling of the license response. Your implementation can manage access in any way needed, including displaying the license result in the UI or directing the user to purchase the application (if not currently licensed).

To help you get started with a`Policy`, the LVL provides two fully complete`Policy`implementations that you can use without modification or adapt to your needs:

[`ServerManagedPolicy`](https://developer.android.com/google/play/licensing/adding-licensing#ServerManagedPolicy)
:   A flexible`Policy`that uses settings provided by the licensing server to manage response caching and access to the application while the device is offline (such as when the user is on an airplane). For most applications, the use of`ServerManagedPolicy`is highly recommended.

[`StrictPolicy`](https://developer.android.com/google/play/licensing/adding-licensing#StrictPolicy)
:   A restrictive`Policy`that does not cache any response data and allows the application access*only*when the server returns a licensed response.

The LVL is available as a downloadable package of the Android SDK. The package includes both the LVL itself and an example application that shows how the library should be integrated with your application and how your application should manage response data, UI interaction, and error conditions.

The LVL sources are provided as an Android*library project*, which means that you can maintain a single set of library sources and share them across multiple applications. A full test environment is also available through the SDK, so you can develop and test the licensing implementation in your applications before publishing them, even if you don't have access to a physical device.

## Requirements and Limitations

Google Play Licensing is designed to let you apply license controls to applications that you publish through Google Play. The service is not designed to let you control access to applications that are not published through Google Play or that are run on devices that do not offer the Google Play client.

Here are some points to keep in mind as you implement licensing in your application:

- An application can use the service only if the Google Play client is installed on its host device and the device is running Android 1.5 (API level 3) or higher.
- To complete a license check, the licensing server must be accessible over the network. You can implement license caching behaviors to manage access to your application when there is no network connectivity.
- The security of your application's licensing controls ultimately relies on the design of your implementation itself. The service provides the building blocks that let you securely check licensing, but the actual enforcement and handling of the license are factors that are up to you. By following the best practices in the following documents, you can help ensure that your implementation will be secure.
- Adding licensing to an application does not affect the way the application functions when run on a device that does not offer Google Play.
- You can implement licensing controls for a free app, but only if you're using the service to provide[APK expansion files](https://developer.android.com/google/play/expansion-files).

## Replacement for Copy Protection

Google Play Licensing is a flexible, secure mechanism for controlling access to your applications. It effectively replaces the Copy Protection mechanism (no longer supported) that was previously offered on Google Play and gives you wider distribution potential for your applications.

Licensing lets you move to a license-based model that is enforceable on all devices that have access to Google Play. Access is not bound to the characteristics of the host device, but to your application on Google Play (through the app's public key) and the licensing policy that you define. Your application can be installed and managed on any device on any storage, including SD card.

Although no license mechanism can completely prevent all unauthorized use, the licensing service lets you control access for most types of normal usage, across all compatible devices, locked or unlocked.

To begin adding application licensing to your application, continue to[Setting Up for Licensing](https://developer.android.com/google/play/licensing/setting-up).