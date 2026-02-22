---
title: https://developer.android.com/privacy-and-security/about
url: https://developer.android.com/privacy-and-security/about
source: md.txt
---

# Privacy checklist

Android is focused on helping users take advantage of the latest innovations while making their security and privacy top priorities. Use the checklists on this page as a source for common privacy guidelines and best practices.

Some of the best practices described on this page also appear in the[cheat sheet](https://developer.android.com/privacy-and-security/about#privacy-cheatsheet).

## Checklist: minimize your permissions requests

![](https://developer.android.com/static/privacy-and-security/images/permissions.svg)Build trust with your users by being transparent and providing users control over how they experience your app.

- **Request the minimum permissions that your feature needs:** when introducing major changes to your app, review the[requested permissions](https://developer.android.com/training/permissions/usage-notes#avoid_requesting_unnecessary_permissions)to confirm that your app's features still need them.
  - Newer versions of Android often introduce ways to access data in a privacy-conscious manner without requiring permissions. For more information, see[Evaluate whether your app needs to declare permissions](https://developer.android.com/training/permissions/evaluating).
  - If your app is distributed on Google Play, you can use[Android vitals](https://developer.android.com/topic/performance/vitals/permissions#use_android_vitals_to_gauge_user_perceptions)to obtain the percentage of users that deny permissions in your app. Use this data to reassess the design of features whose required permissions are most commonly denied.
- **Explain why a feature in your app needs a permission:** follow the[recommended flow](https://developer.android.com/training/permissions/requesting#explain)to do so. Request the permission when it's needed, rather than at app startup, so that the permission need is clear to users.
- **Be aware that users or the system can deny the permission multiple times:**Android respects this user choice by ignoring permission requests from the same app.
- **Degrade gracefully without permission:**your app should degrade gracefully when users deny or revoke a permission---for example, disabling voice input if the user doesn't grant the microphone permission.
- **Remove access to unnecessary permissions** : when you update your app,[remove its access](https://developer.android.com/training/permissions/requesting#remove-access)to any runtime permissions that it no longer needs.
- **Understand the permissions required by an SDK or library:** if you're using an SDK or library that accesses data guarded by dangerous permissions, users generally attribute this to your app. Make sure you[understand the permissions that your SDKs require and why](https://developer.android.com/training/permissions/usage-notes#sdk-libraries).

## Checklist: minimize your use of location

![](https://developer.android.com/static/images/cluster-illustrations/location-access.svg)

Data about a user's location is sensitive; avoid using location data if possible. If you must use location services, take steps to minimize the collection of location data. Use the following checklist to minimize your app's use of location.

- **Degrade gracefully without location data:**on Android 10 (API level 29) and higher, users can limit your app's location access to while the app is in use. Design your app so that it degrades gracefully when it doesn't have uninterrupted access to location.
- **Use nearby Bluetooth or Wi-Fi devices:** if your app needs to pair the user's device with a nearby device over Bluetooth or Wi-Fi, use the[companion device manager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing), which doesn't require location permissions. Learn more about[Bluetooth](https://developer.android.com/guide/topics/connectivity/bluetooth/permissions)and[Wi-Fi](https://developer.android.com/guide/topics/connectivity/wifi-permissions)permissions.
- **Use coarse location accuracy when possible:** review the[level of location granularity](https://developer.android.com/training/location/permissions#accuracy)that your app needs. Coarse location access is sufficient to fulfill most location-related use cases.
- **Access location in the background only as necessary:** if your app requires background location, such as with geofencing, implement it to be obvious to users. Learn more about[considerations for using background location](https://developer.android.com/training/location/background).
- **Access location data while your app is visible to the user:**this lets users better understand why your app requests location information.
- **Don't initiate foreground services from the background:** consider launching your app from a notification and then executing location code when your app's UI becomes visible. If your app must retain location access to support a user-initiated ongoing task after the user navigates away from your app's UI,[start a foreground service](https://developer.android.com/guide/components/services#Types-of-services)before going into the background.

## Checklist: handle data safely

**Note:** You can read more about what's considered sensitive data in the[User Data article](https://play.google.com/about/privacy-security-deception/user-data/#!?zippy_activeEl=personal-sensitive#personal-sensitive)page in the Google Play Developer Policy Center.

![](https://developer.android.com/static/images/privacy/data.svg)Be transparent, secure, and thorough in how you handle sensitive data. Use the following checklist as guidance to handle user data more safely in your app.

- **Audit access to data:** on Android 11 (API level 30) and higher,[perform data access auditing](https://developer.android.com/security-and-privacy/data/audit-access)to gain insights into how your app and its dependencies access private data from users, making it easier to identify unexpected data access.

- **Declare package visibility needs:** if your app targets Android 11 or higher, the system makes certain apps invisible to your app by default. Learn how to[make those other apps visible to your app](https://developer.android.com/training/package-visibility/declaring).

- **Support scoped storage:** to give users more control and limit file clutter, apps targeting Android 10 (API level 29) or higher automatically have scoped access into external storage, or[*scoped storage*](https://developer.android.com/training/data-storage#scoped-storage). Such apps have access only to their own directory and media they've created. Learn how to[migrate to scoped storage](https://developer.android.com/training/data-storage/use-cases).

- **Work with user-resettable identifiers:** to protect the privacy of your users, use the most restrictive identifier that satisfies your use case---see the[checklist for resettable identifiers in this document](https://developer.android.com/privacy-and-security/about#resettable-identifiers).

- **Provide prominent disclosure and consent:** follow the[Google Play User Data policy best practices](https://support.google.com/googleplay/android-developer/answer/11150561)for providing prominent disclosure and consent requests to users.

- **Declare your app's data use:** [properly fill out the Google Play Console Data safety form](https://developer.android.com/security-and-privacy/data/declare-data-use), which explains to users which types of user data your app collects and shares.

- **Securely pass sensitive data to other apps:** use an explicit intent to pass sensitive data to another app.[Grant one-time data access](https://developer.android.com/topic/security/best-practices#permissions-share-data)to further restrict another app's access.

- **Don't include sensitive data in Logcat messages or log files:** [learn more](https://developer.android.com/privacy-and-security/security-tips#UserData).

| **Note:** Jetpack offers several libraries to keep your app's data more secure. Learn more in the guides on using the[Jetpack Security library](https://developer.android.com/topic/security/data)and the[Jetpack Preferences library](https://developer.android.com/guide/topics/ui/settings/use-saved-values).

## Checklist: use resettable identifiers

![](https://developer.android.com/static/images/privacy/identifiers.svg)Respect your users' privacy and use resettable identifiers. See[Best practices for unique identifiers](https://developer.android.com/training/articles/user-data-ids)for more information.

- **Don't access IMEI or the device serial number:** these identifiers are persistent. An app targeting Android 10 (API level 29) or higher causes a[`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException)if it tries to access these identifiers.

- **Only use an advertising ID for user profiling or ads use cases:** always respect user preferences on[advertisement tracking](https://support.google.com/googleplay/android-developer/answer/6048248)for personalization.**Important:**This is required for Google Play.

- **Use a privately-stored GUID:** for the vast majority of non-ads use cases,[use a privately-stored globally-unique ID (GUID)](https://developer.android.com/training/articles/user-data-ids#signed-out-anon-user-analytics), which is app-scoped.

- **Use the SSAID for apps that you own:** to share states between apps that you own without requiring users to sign into an account, use secure settings Android ID (SSAID). Learn more about[how to save signed-out user preferences between apps](https://developer.android.com/training/articles/user-data-ids#signed-out-user-prefs).

## Checklist: support user-facing privacy features

![](https://developer.android.com/static/images/picto-icons/user-friendly-integration.svg)

Be transparent, secure, and thorough in how you handle sensitive data. Use the following checklist as guidance to ensure your app safely handles user data.

- **Provide a rationale for access to sensitive information:** on Android 12 (API level 31) and higher, users can access the Privacy Dashboard in system settings to learn details related to when apps access location, microphone, and camera information. Learn more about[providing this explanation to users](https://developer.android.com/training/permissions/explaining-access#privacy-dashboard).

- **Prompt the user to disable app hiberation** : if a user hasn't interacted with an app that targets Android 11 (API level 30) or higher for a few months, the system places that app in a hiberation state. Learn about[app hibernation and how to ask the user to disable it](https://developer.android.com/topic/performance/app-hibernation).

- **Securely pass sensitive data to other apps:** if you need to pass sensitive data to another app, use an[explicit intent](https://developer.android.com/guide/components/intents-filters#Types).[Grant one-time data access](https://developer.android.com/topic/security/best-practices#permissions-share-data)to further restrict another app's access.

- **Visually indicate your app is capturing audio or imagery:** even when your app is in the foreground, show a real-time indicator that you are capturing from the microphone or camera. Note: Android 9 (API level 28) and higher[don't allow for microphone or camera access when your app is in the background](https://developer.android.com/about/versions/pie/android-9.0-changes-all#privacy-changes-all).

## Privacy cheat sheet

The privacy cheat sheet is a quick reference of some of the most useful privacy APIs in Android, as well as the best practices that you should keep top of mind when you design your app.

The cheat sheet is also downloadable in PDF format:

- [Light mode PDF](https://developer.android.com/static/privacy-and-security/images/cheat-sheet-light.pdf)
- [Dark mode PDF](https://developer.android.com/static/privacy-and-security/images/cheat-sheet-dark.pdf)

![](https://developer.android.com/static/privacy-and-security/images/cheat-sheet.svg)