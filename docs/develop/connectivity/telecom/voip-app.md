---
title: Build a calling app  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/telecom/voip-app
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Build a calling app Stay organized with collections Save and categorize content based on your preferences.




Use the Telecom Jetpack library to offer the best video and audio experiences to
your users. With the Telecom framework, you get call and notification
management, foreground support and more. The new Jetpack library adds support
for:

* Call streaming and transfer
* Android Auto and Wear OS integration
* Backward compatibility

To learn more about how to build a calling app with the Telecom library, check
out the [Telecom](/guide/topics/connectivity/telecom/voip-app/telecom) guide.

## Supported telecom devices

Starting with Android 7 (API level 21), most phones support the Telecom
framework, and they must do so for SIM-based phone calls to work. For devices
like tablets, which don't traditionally require a Telephony implementation,
Android 14 (API level 34) introduces new requirements that mandate a proper
Telecom framework implementation for tablets that support VoIP.

Use `PackageManager` to see if the device supports Telecom:

```
packagemanager.hasSystemFeature(PackageManager.FEATURE_TELECOM)
```

**Note:** Non-Telecom based devices don't support other platforms such as Wear OS.