---
title: https://developer.android.com/jetpack/androidx/releases/remotecallback
url: https://developer.android.com/jetpack/androidx/releases/remotecallback
source: md.txt
---

# Remotecallback

# Remotecallback

API Reference  
[androidx.remotecallback](https://developer.android.com/reference/kotlin/androidx/remotecallback/package-summary)  
[androidx.remotecallback.compiler](https://developer.android.com/reference/kotlin/androidx/remotecallback/compiler/package-summary)  
Create a wrapper that makes it easier for developers to provide a PendingIntent.  

|   Latest Update   | Stable Release | Release Candidate | Beta Release |                                             Alpha Release                                             |
|-------------------|----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------|
| November 19, 2025 | -              | -                 | -            | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/remotecallback#1.0.0-alpha03) |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:878799+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=878799&template=1442106)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0.0

### Version 1.0.0-alpha03

November 19, 2025

`androidx.remotecallback:remotecallback:1.0.0-alpha03`and`androidx.remotecallback:remotecallback-processor:1.0.0-alpha03`are released. Version 1.0.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3979d96937e945201359c48c6d992447ef7ef79c..8000d1fa297fd9b56e9a0e4e13e0ad2f66c080d1/remotecallback).

**API Changes**

- The Slices framework has been deprecated, it will not receive any update moving forward. If you are looking for a framework that handles communication across apps, consider using AppSearchManager. ([Ie09cb](https://android-review.googlesource.com/#/q/Ie09cb59a17bfdffa99551032c3966bc13be0d6c2),[b/207128063](https://issuetracker.google.com/issues/207128063))

### Version 1.0.0-alpha02

May 7, 2019

`androidx.remotecallback:*:1.0.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/76a0131c6783572a9dc3c06a0b686d3cbc68d713..3979d96937e945201359c48c6d992447ef7ef79c/remotecallback).

**API changes**

- Cleanup to handle context/authority ([aosp/836270](https://android-review.googlesource.com/c/836270))

### Version 1.0.0-alpha01

December 3, 2018

- Remote Callback is a new library aimed at making generating and receiving`PendingIntents`easier. This is the first version of Remote Callback.