---
title: https://developer.android.com/work/guide
url: https://developer.android.com/work/guide
source: md.txt
---

# Developer guide

Android's enterprise features provide organizations with a secure, flexible, and unified Android mobility platform---combining devices, applications, and management. Android apps are compatible with Android's enterprise features by default. However, there are additional features you can use to make your app work best on managed Android devices:

- [Work profile compatibility](https://developer.android.com/work/guide#work-profiles)---Modify your Android app so it functions best on a managed device.
- [Managed configurations](https://developer.android.com/work/guide#managed-configurations)---Modify your app to allow IT admins the option to specify custom settings for your apps.
- [Dedicated devices](https://developer.android.com/work/guide#dedicated-device)---Optimize your app so that it can be deployed on an Android device as a kiosk.
- [Single Sign-On (SSO)](https://developer.android.com/work/guide#sso)---Simplify the sign-on process for users signing in to different apps on their managed Android device.

### Prerequisites

1. You've created an Android app.
2. You're ready to modify your app so that it works best for organizations.
3. Minimum version: Android 5.0 Lollipop recommended version: Android 6.0 Marshmallow and later.

Note: Android's enterprise features are built into most Android 5.0 devices; however, Android 6.0 and later offers additional features, especially with regard to dedicated devices.

## Work profiles

You can manage a user's business data and applications through a work profile. A work profile is a managed corporate profile associated with the primary user account on an Android device. A work profile securely isolates work apps and data from personal apps and data. This work profile is in a separate container from the personal profile, which your user controls. These separate profiles allow organizations to manage the business data they care about, but leave everything else on a user's device under the user's control. For a deep dive into best practices, see the[Work profiles](https://developer.android.com/work/managed-profiles)guide. For an overview of those best practices, see below.

### Key features of a work profile

- Separate and secure profile
- Managed Google Play for application distribution
- Separate badged work applications
- Profile-only management capabilities controlled by an admin

### Work profile benefits on Android 5.0+

- Full device encryption
- One Android application package (APK) for both profiles when there's a personal profile and a work profile present on the device
- [Device policy controller](https://support.google.com/work/android/answer/6192678)(DPC) is limited to the work profile
- Device administration via the[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)class

### Considerations for work profiles

- The Android system prevents intents[from crossing profiles](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#clearCrossProfileIntentFilters(android.content.ComponentName))and IT admins can[enable or disable system apps](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#enableSystemApp(android.content.ComponentName,%20java.lang.String)).
- A file path (Uniform Resource Identifier \[URI\]) that's valid on one profile may not be valid on the other.

### Prevent intents from failing between profiles

It's difficult to know which intents can cross between profiles, and which ones are blocked. The only way to know for sure is by testing. Before your app starts an activity, you should verify that the request is resolved by calling[`Intent.resolveActivity()`](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager)).

- If it returns`null`, the request doesn't resolve.
- If it returns something, it shows that the intent resolves, and it's safe to send the intent.

**Note** : For detailed testing instructions, see[Prevent Failed Intents](https://developer.android.com/work/managed-profiles#prevent_failed_intents).

### Share files across profiles

Some developers use URIs to mark file paths in Android. However, because there are separate file systems when a work profile is present, we recommend:

|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Use:** Content URIs   | - The[content URIs](https://developer.android.com/reference/android/content/ContentUris)contain the authority, path, and ID for a specific file. You can generate this using[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)subclass.[Learn more](https://developer.android.com/training/secure-file-sharing) - Share and grant permissions to access the content URI using an Intent. Permissions can only be passed across the profile boundary using Intents. If you grant another app access rights to your file using[`Context.grantUriPermission()`](https://developer.android.com/reference/android/content/Context#grantUriPermission(java.lang.String,%20android.net.Uri,%20int)), it only is granted for that app in the same profile. |
| **Don't use:** File URI | - Contains the absolute path of the file on the device's storage. - A file path URI that's valid on one profile isn't valid on the other. - If you attach a file URI to an intent, a handler is unable to access the file in another profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**Next steps** : Once your app supports managed profiles, test it in a work profile. See[Test your app](https://developer.android.com/work/guide#testing).

## Implement managed configurations

Managed configurations are a set of instructions that IT admins can use to manage their users' mobile devices in a specific way. These instructions are universal and work across any EMM, allowing admins to remotely configure applications on their users' phones.

If you're developing apps for business or government, you may need to satisfy your industry's specific set of requirements. Using managed configurations, the IT admin can remotely specify settings and enforce policies for their users' Android apps; for example:

- Configure if an app can sync data via cellular/3G, or only Wi-Fi
- Allow or block URLs on a web browser
- Configure an app's email settings
- Enable or disable printing
- Manage bookmarks

### Best practices for implementing managed configurations

The[Set up Managed Configurations](https://developer.android.com/work/managed-configurations)guide is the key source for information on how to build and deploy managed configurations. After you've reviewed this documentation, see recommendations below for additional guidance.

#### When first launching the app

As soon as you launch an application, you can see if managed configurations are already set for this app in`onStart()`or`onResume()`. Additionally, you can find out if your application is managed or unmanaged. For example, if[`getApplicationRestrictions()`](https://developer.android.com/reference/android/content/RestrictionsManager#getApplicationRestrictions())returns:

- **A set of application-specific restrictions**---You can configure the managed configurations silently (without requiring user input).
- **An empty bundle**---Your application acts like it's unmanaged (for example, how the app behaves in a personal profile).
- **A bundle with a single key value pair with[`KEY_RESTRICTIONS_PENDING`](https://developer.android.com/reference/android/os/UserManager#KEY_RESTRICTIONS_PENDING)set to true**---your application is being managed, but the DPC isn't configured correctly. You should block this user from your app, and direct them to their IT admin.

#### Listen for changes to managed configurations

IT admins can change managed configurations and what policies they want to enforce on their users at any time. Because of this, we recommend you ensure that your app can accept new restrictions for your managed configuration as follows:

- **Fetch restrictions on launch** ---Your app should call`getApplicationRestrictions()`in`onStart()`and`onResume()`, and compare against old restrictions to see if changes are required.
- **Listen while running** ---Dynamically register[`ACTION_APPLICATION_RESTRICTIONS_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_RESTRICTIONS_CHANGED)in your running activities or services, after you've checked for new restrictions. This intent is sent only to listeners that are dynamically registered, and not to listeners declared in the app manifest.
- **Unregister while not running** ---In`onPause()`, you should unregister for the broadcast of`ACTION_APPLICATION_RESTRICTIONS_CHANGED`.

## Dedicated devices

Dedicated devices are kiosk devices used for a single purpose, such as digital signage displays, ticket printing kiosks, or checkout registers.

When an Android device is configured as a dedicated device, the user sees an application locked to the screen with no Home or Recent Apps buttons to escape the app. Dedicated devices can also be configured to show a set of applications, such as a library kiosk with an app for the library catalog and a web browser.

For instructions, see[Dedicated-device](https://developer.android.com/work/cosu).

## Set up single sign-on with Chrome Custom Tabs

Enterprise users often have multiple apps on their device, and they prefer to sign in once to access all of their work applications. Typically, users sign in through a[WebView](https://developer.chrome.com/multidevice/webview/overview); however, there are a couple reasons why this isn't ideal:

1. Users often need to sign in multiple times with the same credentials. The WebView solution often isn't a true single sign-on (SSO) experience.
2. There can be security risks, including malicious applications inspecting cookies or injecting JavaScript® to access a user's credentials. Even trusted developers are at risk if they rely on potentially malicious third-party SDKs.

A solution to both problems is to authenticate users using browser Custom Tabs, instead of WebView. This ensures that authentication:

- Occurs in a secure context (the system browser) where the host app cannot inspect contents.
- Has a shared cookie state, ensuring the user has to sign in only once.

### Requirements

[Custom Tabs](https://developer.android.com/topic/libraries/support-library/features.html#custom-tabs)are supported back to API level 15 (Android 4.0.3). To use Custom Tabs you need a supported browser, such as Chrome. Chrome 45 and later implement this feature as[Chrome Custom Tabs](https://developer.chrome.com/multidevice/android/customtabs).

### How do I implement SSO with Custom Tabs?

Google has open sourced an OAuth client library that uses Custom Tabs, contributing it to the OpenID Connect working group of the OpenID Foundation. To set up Custom Tabs for SSO with the AppAuth library, see the[documentation and sample code on GitHub](https://github.com/openid/AppAuth-Android).

## Test your app

After you've developed your app, you'll want to test it---both in a work profile and on a fully managed device. See the instructions below.

### Use Test DPC to test your Android app

We provide the Test DPC app to help Android developers test their apps in an enterprise environment. Using Test DPC, you can set EMM policies or managed configuration values on a device---as if an organization managed the device using an EMM. To install Test DPC on a device, choose one of the following methods:

- Install Test DPC from[GooglePlay](https://play.google.com/store/apps/details?id=com.afwsamples.testdpc).
- Build from the source on[GitHub](https://github.com/googlesamples/android-testdpc).

For more information on how to configure Test DPC, see the instructions below and the[Test DPC User Guide](https://github.com/googlesamples/android-testdpc).

### Provision a work profile

To test your app in a work profile, you need to first provision a work profile on device using the Test DPC app, as follows:

1. Install Test DPC on the device.
2. In the Android launcher, tap the**Set up Test DPC**app icon.
3. Follow the onscreen instructions.
4. Install your app on the device and test to see how it runs in the work profile.

Android creates a work profile and installs a copy of Test DPC in the work profile. You use this work-badged instance of Test DPC to set policies and managed configurations in the work profile. To learn more about setting up a work profile for development, read the developer's guide[Work profiles](https://developer.android.com/work/managed-profiles).

### Provision a fully managed device

Organizations use fully managed devices because they can enforce a full range of management policies on the device. To provision a fully managed device, follow these steps:

1. Install Test DPC on the device.
2. Confirm that there are no other users or a work profile on the device.
3. Confirm that there are no accounts on the device.
4. Run the following[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)(adb) command in your terminal:  

   ```
   adb shell dpm set-device-owner com.afwsamples.testdpc/.DeviceAdminReceiver
   ```
5. Once you've completed provisioning the device owner, you can test your app on that device. You should specifically test how[managed configurations](https://developer.android.com/work/managed-configurations)and[intents](https://developer.android.com/work/managed-profiles#prevent_failed_intents)work on that device.

You can also use other provisioning methods---see the[Test DPC User Guide](https://github.com/googlesamples/android-testdpc). To learn how IT admins typically enroll and provision Android-powered devices, read[Provision devices](https://developers.google.com/android/work/play/emm-api/prov-devices).

### End-to-end testing

After you've finished testing your app in the environments above, you'll likely want to test your app in an end-to-end production environment. This process includes the steps a customer needs to take to deploy your app in their organization, including:

- App distribution through Play
- Server-side managed configuration
- Server-side profile policy control

You need to access an EMM console to complete the end-to-end testing. The easiest way to get one is to request a testing console from your EMM. Once you have access, complete these tasks:

1. Create a test version of your application with a[new ApplicationId](http://tools.android.com/tech-docs/new-build-system/applicationid-vs-packagename).
2. Claim a[managed Google domain](https://support.google.com/work/android/answer/6174056)and bind it to your EMM. If you already have a testing domain that's bound to an EMM, you may need to unbind it to test it with your preferred EMM. Please consult your EMM for the specific unbinding steps.
3. [Publish your application to the private channel](https://support.google.com/a/answer/2494992)for their managed Google domain.
4. Use the EMM console and EMM application to:
   1. Set up work devices.
   2. Distribute your application.
   3. Set managed configuration.
   4. Set device policies.

This process will differ based on your EMM. Please consult your EMM's documentation for further details. Congrats! You've completed these steps and verified that your app works well for enterprise users.