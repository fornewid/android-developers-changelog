---
title: https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice
url: https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/installreferrer/llms.txt

This document provides a technical reference for using the Play Install
Referrer API. The Play Install Referrer API is an [Android Interface Definition
Language (AIDL) service interface](https://developer.android.com/develop/background-work/services/aidl) for developers who aren't using Kotlin or
the Java programming language.

> [!NOTE]
> **Note:** If you're developing your app using Kotlin or the Java programming language, use the [Play Install Referrer Library](https://developer.android.com/google/play/installreferrer/library.md.txt), which provides a wrapper around the Play Install Referrer API.

## Get the install referrer

The `getInstallReferrer()` method returns the app install referrer information
corresponding to the given package name sent through a `Bundle` (key mapped in
table 1). In the response `Bundle` sent by Google Play, the referral
information is stored in fields mapped to the keys detailed in table 2.


**Table 1.** `getInstallReferrer()` bundle data
request.

| Parameter | Type | Description |
|---|---|---|
| `package_name` | `String` | The package name of the caller, used for disambiguation. |


**Table 2.** Response data from a `getInstallReferrer()`
request.

| Key | Type | Description |
|---|---|---|
| `install_referrer` | `String` | The referrer URL of the installed package. |
| `referrer_click_timestamp_seconds` | `long` | The client-side timestamp, in seconds, when the referrer click happened. |
| `install_begin_timestamp_seconds` | `long` | The client-side timestamp, in seconds, when app installation began. |
| `referrer_click_timestamp_server_seconds` | `long` | The server-side timestamp, in seconds, when the referrer click happened. |
| `install_begin_timestamp_server_seconds` | `long` | The server-side timestamp, in seconds, when app installation began. |
| `install_version` | `string` | The app's version at the time when the app was first installed. |
| `google_play_instant` | `boolean` | Indicates whether your app's instant experience was launched within the past 7 days. |

> [!CAUTION]
> **Caution:** The install referrer information is available for 90 days and **doesn't
> change** unless the app is reinstalled. To avoid unnecessary API calls in your app, invoke the API **only once** the first time your app runs after install.