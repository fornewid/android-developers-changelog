---
title: https://developer.android.com/develop/connectivity/telecom/voip-app
url: https://developer.android.com/develop/connectivity/telecom/voip-app
source: md.txt
---

Use the Telecom Jetpack library to offer high-quality video and audio
experiences to your users. With the Telecom framework, you get call and
notification management, foreground support, and more. The Jetpack library adds
support for:

- Call streaming and transfer
- Android Auto and Wear OS integration
- [System call log integration (unified call history)](https://developer.android.com/develop/connectivity/telecom/call-log-integration)
- Backward compatibility

For more information about how to build a calling app with the Telecom library,
see [Core-Telecom](https://developer.android.com/develop/connectivity/telecom/voip-app/telecom).

## Supported telecom devices

On Android 5.0 (API level 21) and higher, most phones support the Telecom
framework, and they must do so for SIM-based phone calls to work. For devices
like tablets, which don't traditionally require a Telephony implementation,
Android 14 (API level 34) introduces requirements that mandate a proper
Telecom framework implementation for tablets that support VoIP.

Use `PackageManager` to see if the device supports Telecom:

    packagemanager.hasSystemFeature(PackageManager.FEATURE_TELECOM)

> [!NOTE]
> **Note:** Non-Telecom based devices don't support other platforms such as Wear OS.