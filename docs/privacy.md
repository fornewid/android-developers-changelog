---
title: https://developer.android.com/privacy
url: https://developer.android.com/privacy
source: md.txt
---

# Privacy | Android Developers

![](http://developer.android.com/static/images/cluster-illustrations/identity.svg)  

### Protect user privacy

Android empowers developers to build apps that are inherently secure and respect user privacy. Google Play's policies and guidelines further ensure a safe and trustworthy ecosystem for your creations.

As a developer, you can prioritize privacy in your apps by minimizing data collection, only requesting necessary permissions, and limiting location access whenever possible. Enhance the security of your apps by implementing industry-standard encryption, ensuring data integrity, and using strong authentication. By adhering to these principles, you contribute to the Android platform's reputation for security and privacy, while fostering trust with your users.
[![](http://developer.android.com/static/images/spot-icons/handle-data.svg)](http://developer.android.com/privacy/best-practices)  
Guide

### [Ensure user privacy](http://developer.android.com/privacy/best-practices)

Learn how to provide transparency for your users, give your users control over their private data, and treat data responsibly.  
[Learn more](http://developer.android.com/privacy/best-practices)  
[![](http://developer.android.com/static/images/cluster-illustrations/android-games.svg)](http://developer.android.com/docs/quality-guidelines/core-app-quality#sc)  
Guide

### [Google Play privacy \& security requirements](http://developer.android.com/docs/quality-guidelines/core-app-quality#sc)

Learn about Google Play's requirements for how your app should handle user data and personal information safely, with the appropriate level of permission.  
[Learn more](http://developer.android.com/docs/quality-guidelines/core-app-quality#sc)[![](http://developer.android.com/static/images/cluster-illustrations/build-apps.svg)](http://developer.android.com/privacy/cheat-sheet)  

### [Build apps to be private](http://developer.android.com/privacy/cheat-sheet)

In the Android ecosystem, privacy is a fundamental principle. As the platform advances, it consistently integrates privacy-centric features. With increasing user awareness of the data that apps can gather, Android developers must proactively prioritize user trust in their applications.  
[Cheatsheet](http://developer.android.com/privacy/cheat-sheet)[Codelab](http://developer.android.com/codelabs/android-privacy-codelab)

## Android platform privacy

Learn more about how the Android platform has added features and enhancements to help you protect the privacy of your users.  
[![](http://developer.android.com/static/images/about/versions/13/android-13-hero.png)](http://developer.android.com/about/versions/13/features#privacy-security)  

### [Android 13](http://developer.android.com/about/versions/13/features#privacy-security)

- Notification permission
- Wi-Fi and storage permissions
- Photo picker  
[Learn more](http://developer.android.com/about/versions/13/features#privacy-security)  
[![](http://developer.android.com/static/images/spot-icons/android-14.svg)](http://developer.android.com/about/versions/14/features)  

### [Android 14](http://developer.android.com/about/versions/14/features)

- Screenshot detection
- Partial access to photos and videos  
[Learn more](http://developer.android.com/about/versions/14/features)  
[![](http://developer.android.com/static/images/spot-icons/android-15.svg)](http://developer.android.com/about/versions/15/features)  

### [Android 15](http://developer.android.com/about/versions/15/features)

- Screen recording detection
- Expanded IntentFilter capabilities
- Private space
- Partial screen sharing  
[Learn more](http://developer.android.com/about/versions/15/features)![](http://developer.android.com/static/images/picto-icons/user-friendly-integration.svg)  

## App permissions

Understand how app permissions can be used to protect user privacy by restricting data and actions.  
Guide

### [Learn about permissions on Android](http://developer.android.com/guide/topics/permissions/overview)

App permissions help support user privacy by protecting access restricted data, such as system state and users' contact information, and restricted actions, such as connecting to a paired device and recording audio.  
[Learn more](http://developer.android.com/guide/topics/permissions/overview)  
Guide

### [Declare app permissions](http://developer.android.com/training/permissions/declaring)

If your app requests app permissions, you must declare these permissions in your app's manifest file.  
[Learn more](http://developer.android.com/training/permissions/declaring)  
Guide

### [Minimize permissions](http://developer.android.com/training/permissions/evaluating)

Before you declare permissions in your app, consider whether you need to. Learn how the system can help you.  
[Learn more](http://developer.android.com/training/permissions/evaluating)  
Guide

### [Use the Android photo picker](http://developer.android.com/training/data-storage/shared/photopicker)

Use the system photo picker to give your users the control to choose specific media items to share with your app.  
[Learn more](http://developer.android.com/training/data-storage/shared/photopicker)  
Guide

### [Access app-specific data](http://developer.android.com/training/data-storage/app-specific)

Use the system-provided folder for app-specific information. Your app doesn't need any storage permissions to access this folder.  
[Learn more](http://developer.android.com/training/data-storage/app-specific)  
Guide

### [Handle runtime permissions requests](http://developer.android.com/training/permissions/requesting)

Every Android app runs in a limited-access sandbox. If your app needs to use resources or information outside of its own sandbox, you can declare a runtime permission and set up a permission request that provides this access. If your app targets Android 13 or higher, the self-revoke APIs allow your app to revoke access to already-granted permissions that your app no longer requires.  
[Learn more](http://developer.android.com/training/permissions/requesting)![](http://developer.android.com/static/images/picto-icons/location.svg)  

## Control location access

Guide

### [Location permissions](http://developer.android.com/training/location/permissions)

Learn more about location permissions. Upgrade to precise location settings only when needed.  
[Learn more](http://developer.android.com/training/location/permissions)  
Guide

### [Background location access](http://developer.android.com/develop/sensors-and-location/location/background)

Only his background location access when foreground locations services will not suffice.  
[Learn more](http://developer.android.com/develop/sensors-and-location/location/background)![](http://developer.android.com/static/images/picto-icons/private-by-design.svg)  

## Minimize data visibility

Guide

### [Package visibility](http://developer.android.com/training/package-visibility/declaring)

If your app targets Android 11 or higher, declare the set of packages that you expect your app to interact with.  
[Learn more](http://developer.android.com/training/package-visibility/declaring)  
Guide

### [Device identifiers](http://developer.android.com/training/articles/user-data-ids#common-use-cases)

Use the appropriate user-resettable identifier for your app's use case. Starting in Android 12, the system restricts the set of device identifiers that apps can use.  
[Learn more](http://developer.android.com/training/articles/user-data-ids#common-use-cases)![](http://developer.android.com/static/images/picto-icons/toggle.svg)  

## Give users control

Guide

### [Request runtime permissions](http://developer.android.com/training/permissions/requesting)

Every Android app runs in a limited-access sandbox. If your app needs to use resources or information outside of its own sandbox, you can declare a runtime permission and set up a permission request that provides this access.  
[Learn more](http://developer.android.com/training/permissions/requesting)  
Guide

### [Explain access to more sensitive information](http://developer.android.com/training/permissions/explaining-access)

The permissions related to location, microphone, and camera grant your app access to particularly sensitive information about users. Android includes several mechanisms to help users stay in control over which apps can access this information.  
[Learn more](http://developer.android.com/training/permissions/explaining-access)[![](http://developer.android.com/static/images/security/privacy-sandbox_cluster.svg)](https://developers.google.com/privacy-sandbox)  

### [Privacy Sandbox on Android](https://developers.google.com/privacy-sandbox)

The Privacy Sandbox initiative aims to create technologies that both protect people's privacy online and give companies and developers tools to build thriving digital businesses.  
[Privacy Sandbox overview](https://developers.google.com/privacy-sandbox)[Privacy Sandbox on Android](https://developers.google.com/privacy-sandbox/overview/android)