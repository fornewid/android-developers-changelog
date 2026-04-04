---
title: https://developer.android.com/guide/topics/connectivity/omapi
url: https://developer.android.com/guide/topics/connectivity/omapi
source: md.txt
---

# Open Mobile API reader support

On Android 11 and higher, Open Mobile API (OMAPI) supports checking for eSE, SD, and UICC support hardware on devices with the following flags:

- [`FEATURE_SE_OMAPI_ESE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_ESE)
- [`FEATURE_SE_OMAPI_SD`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_SD)
- [`FEATURE_SE_OMAPI_UICC`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_UICC)

Use these values with[`getSystemAvailableFeatures()`](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())or[`hasSystemFeature()`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))to check for device support.