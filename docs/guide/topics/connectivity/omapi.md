---
title: Open Mobile API reader support  |  Connectivity  |  Android Developers
url: https://developer.android.com/guide/topics/connectivity/omapi
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)

# Open Mobile API reader support Stay organized with collections Save and categorize content based on your preferences.



On Android 11 and higher, Open Mobile API (OMAPI) supports checking for eSE, SD,
and UICC support hardware on devices with the following flags:

* [`FEATURE_SE_OMAPI_ESE`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_ESE)
* [`FEATURE_SE_OMAPI_SD`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_SD)
* [`FEATURE_SE_OMAPI_UICC`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_UICC)

Use these values with
[`getSystemAvailableFeatures()`](/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())
or
[`hasSystemFeature()`](/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))
to check for device support.