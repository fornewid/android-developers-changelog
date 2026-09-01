---
title: AEP guideline: Android Telecom Framework  |  Apps Experience Program  |  Android Developers
url: https://developer.android.com/distribute/aep/aep-req-telecom-api
source: html-scrape
---

You are currently viewing the Apps Experience Program (AEP) documentation.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Apps Experience Program](https://developer.android.com/distribute/aep)

# AEP guideline: Android Telecom Framework Stay organized with collections Save and categorize content based on your preferences.





Integrate with the Android Telecom framework using the [Core-Telecom Jetpack
library](/develop/connectivity/telecom/voip-app/telecom) to ensure that Voice over IP (VoIP) calls are treated as a core
feature by the operating system, on par with traditional SIM-based calls. This
integration unifies call management, improves audio handling, and enables
compatibility with remote devices like headsets and watches.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

| ID | Guideline |
| --- | --- |
| AEP-TC-GAA | **Call registration**: All incoming and outgoing VoIP calls must be registered with the Telecom framework using the CallsManager#addCall API. |
| AEP-TC-GAB | **State management**: Use the CallControlScope and other library constructs to accurately reflect and manage the call state lifecycle, including dialing, ringing, active, held, and disconnected states. |
| AEP-TC-GAC | **Audio handling**: Don't directly use Audio or Bluetooth APIs to manage audio focus and routing; instead, rely on the Telecom framework to handle concurrent call scenarios and audio device changes. |
| AEP-TC-GAD | **Notifications**: Use the [callStyle API](/reference/android/app/Notification.CallStyle) to display call-style notifications that are consistent with the Android system. |
| AEP-TC-GAE | **Foreground service lifecycle**: Manage the lifecycle of any necessary Foreground Services for the call in accordance with Android best practices and limitations. |
| AEP-TC-GAF | **Remote surface integration**: Synchronizes call state and controls with connected remote surfaces, such as Bluetooth headsets, Wear OS devices, and Android Auto. |
| AEP-TC-GAG | **Multi-call scenarios**: Gracefully handles interactions with other calls, such as incoming SIM calls or calls from other VoIP applications, ensuring predictable audio behavior and user experience. |

## Guideline applicability

This guideline applies to:

* Apps provide Voice over IP (VoIP) calling capabilities.
* All form factors on which the app is available.

## Exemptions

The following exemptions apply for this guideline:

| ID | Exemption |
| --- | --- |
|  | Apps that are technically unable to take AndroidX dependencies due to technical barriers such as: |
| AEP-TC-EAA | SDK dependency collisions. |
| AEP-TC-EAB | Android Open Source Project (AOSP) constraints. |
| AEP-TC-EAC | Original Equipment Manufacturer (OEM) build system restrictions. |
| AEP-TC-EAD | Temporary exemptions may be granted for apps encountering significant platform or library issues that prevent a stable migration, provided there is a clear timeline for resolution and the issue has been accepted by Google. |
| AEP-TC-EAE | Apps can use an equivalent alternative framework that provides similar quality, user capabilities, stability and compatibility across the ecosystem. [Contact support](/distribute/aep/aep-get-support) if you have a suitable framework for consideration. |

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Android Telecom Framework**. These resources are for your reference only
and don't contain additional program requirements.

* [Build a calling app](/develop/connectivity/telecom/voip-app)
* [Telecom framework overview](/develop/connectivity/telecom)
* [Call log integration](/develop/connectivity/telecom/call-log-integration)
* [Bring native visibility to your VoIP app experience](https://android-developers.googleblog.com/2026/05/voip-native-visibility-telecom-alpha.html)