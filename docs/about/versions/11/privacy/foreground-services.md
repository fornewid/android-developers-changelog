---
title: Foreground services in Android 11  |  Android Developers
url: https://developer.android.com/about/versions/11/privacy/foreground-services
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Foreground services in Android 11 Stay organized with collections Save and categorize content based on your preferences.



Android 11 changes when foreground services can
access the device's location, camera, and microphone. This helps protect
sensitive user data.

Camera and microphone foreground service types
:   If your app targets Android 11 or higher and accesses the
    camera or microphone in a foreground service, you must include the `camera` and
    `microphone` [foreground service
    types](/guide/components/foreground-services#types).

Restrictions to access while in use
:   If your app [starts a foreground service while running in the
    background](/guide/components/foreground-services#while-in-use-restrictions), the
    foreground service cannot access the microphone or camera. Additionally,
    the service cannot access location unless your app
    has [background location](/training/location/permissions#background) access.

Learn more about how to use [foreground
services](/guide/components/foreground-services) in your app.