---
title: https://developer.android.com/google/play/installreferrer/release-notes
url: https://developer.android.com/google/play/installreferrer/release-notes
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/installreferrer/llms.txt

This page provides release notes for each version of the Play Install Referrer
API Library.

## Play Install Referrer API Library 2.2 Release (2021-01-14)

Version 2.2 launched. Fixed an issue where apps might crash because of a
`SecurityException` (see [Issue #72926755](https://issuetracker.google.com/issues/72926755)).

Added a new `InstallReferrerResponse` constant: `PERMISSION_ERROR`, which is
returned whenever the app isn't allowed to bind to the Service.

## Play Install Referrer API Library 2.1 Release (2020-07-08)

Version 2.1 launched. Fixed an issue where apps might crash with a
`NoClassDefFoundError` error when calling the
[`InstallReferrerClient.startConnection()`](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient.md.txt#startconnection) method (see
[Issue #145557612](https://issuetracker.google.com/issues/145557612)).

## Play Install Referrer API Library 2.0 Release (2020-07-06)

Version 2.0 launched. Added new fields to the response of the
[`getInstallReferrer()`](https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice.md.txt#the_getinstallreferrer_method) method to help developers understand and discover
information about fraudulent clicks.

## Play Install Referrer API Library 1.1 Release (2019-11-22)

Version 1.1 launched. Added the [`getGooglePlayInstantParam()`](https://developer.android.com/reference/com/android/installreferrer/api/ReferrerDetails.md.txt#getgoogleplayinstantparam) method, which
checks whether the user has interacted with your app's [instant experience](https://developer.android.com/topic/google-play-instant/overview.md.txt)
within the past 7 days.

## Play Install Referrer API Library 1.0 Release (2017-11-15)

Version 1.0 launched. The initial version focuses on a library that wraps the
Android Interface Definition Language (AIDL) API. For more information about the
AIDL interface, refer to the [Play Install Referrer API](https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice.md.txt) page.