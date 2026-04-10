---
title: https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager
url: https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager
source: md.txt
---

# Localbroadcastmanager

# Localbroadcastmanager

[User Guide](https://developer.android.com/guide/components/broadcasts)[Code Sample](https://github.com/android/location-samples/blob/master/LocationUpdatesForegroundService/app/src/main/java/com/google/android/gms/location/sample/locationupdatesforegroundservice/MainActivity.java)  
API Reference  
[androidx.localbroadcastmanager.content](https://developer.android.com/reference/kotlin/androidx/localbroadcastmanager/content/package-summary)  
This artifact and its classes are deprecated. Use LiveData or reactive streams instead.  

|  Latest Update   |                                        Stable Release                                        | Release Candidate | Beta Release | Alpha Release |
|------------------|----------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| January 12, 2022 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/localbroadcastmanager#1.1.0) | -                 | -            | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460939+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460939&template=1422575)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

January 12, 2022

`androidx.localbroadcastmanager:localbroadcastmanager:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abade69a222024e74015882531553477622890a5..d2d922e60b4cb018c91276a85fb27a05b8a2b0c9/localbroadcastmanager/localbroadcastmanager)

**Important changes since 1.0.0**

`androidx.localbroadcastmanager`has been fully deprecated. There will be no further releases of this library. Developers should replace usages of`LocalBroadcastManager`with other implementations of the observable pattern. Depending on the use case, suitable options may be`LiveData`or reactive streams.

### Version 1.1.0-rc01

December 15, 2021

`androidx.localbroadcastmanager:localbroadcastmanager:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86267e31251cdaf875674004b9937ff3da0c3f24..abade69a222024e74015882531553477622890a5/localbroadcastmanager/localbroadcastmanager)

### Version 1.1.0-alpha01

December 17, 2018

`androidx.localbroadcastmanager`is being deprecated in version`1.1.0-alpha01`.

**Reason**

- `LocalBroadcastManager`is an application-wide event bus and embraces layer violations in your app; any component may listen to events from any other component.
- It inherits unnecessary use-case limitations of system`BroadcastManager`; developers have to use`Intent`even though objects live in only one process and never leave it. For this same reason, it doesn't follow feature-wise`BroadcastManager`.

These add up to a confusing developer experience.

**Replacement**

- You can replace usage of`LocalBroadcastManager`with other implementations of the observable pattern. Depending on your use case, suitable options may be`LiveData`or reactive streams.