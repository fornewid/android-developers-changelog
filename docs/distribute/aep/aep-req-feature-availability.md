---
title: https://developer.android.com/distribute/aep/aep-req-feature-availability
url: https://developer.android.com/distribute/aep/aep-req-feature-availability
source: md.txt
---

Maintain feature consistency on Android relative to comparable non-Android
platforms to ensure a consistent and premium experience for users regardless of
their device choice.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- **Launch timing** : All features^\*^ must be fully launched on Android in any AEP active country within three weeks of their full launch on a non-Android platform in that same country.
- **Functional equivalence**: The Android version of a feature must support the same core capabilities and use cases as non-Android versions. A feature fails this requirement if it lacks a capability available elsewhere or fails to match the native implementation level, such as using an unoptimized webview where a native feature exists on other platforms.

(\***) Feature definition** : A **feature** is defined as a distinct, identifiable
capability, utility, user journey, content grouping, or method of value exchange
within an app that provides material functional value to the end-user. This
includes additional entry points such as widgets, personalization and ranking
optimizations of experiences, and access to special content.

## Guideline applicability

This guideline applies to all apps across all form factors.

## Exemptions

The following exemptions are applicable for this guideline:

- **Technical infeasibility**: A feature may be exempt if it is technically infeasible to support on Android. Developers must document the feature and the specific technical blockers for review.
- **Feature regressions**: If a feature previously live on Android was disabled to resolve a significant production issue, an exemption may be granted provided evidence is given that a resolution is being actively worked on and the issue and expected resolution time has been accepted by Google.
- **EEA**: This guideline does not apply in the EEA. However, when distributing to the EEA, Android users should be able to access all new experiences and capabilities within the Android title provided by the developer. Developers are therefore required to fully optimize their titles for Android.