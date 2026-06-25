---
title: https://developer.android.com/distribute/aep/aep-req-predictive-background
url: https://developer.android.com/distribute/aep/aep-req-predictive-background
source: md.txt
---

Adopt the predictive back-to-home gesture to provide a smoother, more
predictable navigation experience. By opting into the ahead-of-time back
navigation model, your app will automatically support system animations that
make transitions feel more fluid and intuitive, helping users navigate with
confidence.

## Required implementation

To qualify for AEP, your app must support the back-to-home gesture from your
main activities. To achieve this, **keep back-to-home Predictive Back system
animations enabled** by:

- Ensuring [`android:enableOnBackInvokedCallback="true`](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-out)" in your AndroidManifest.xml for launcher activities.
- Allowing the system to execute the back-to-home animation. If your launcher activity intercepts back events, use `OnBackInvokedDispatcher` with the `PRIORITY_SYSTEM_NAVIGATION_OBSERVER` to observe the events without blocking the animation.

## Guideline applicability

This guideline applies to all apps on the phone, tablet, foldable, and Wear form
factors.

## Exemptions

There are no exemptions for this guideline.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Predictive Background** feature. These resources are for your reference
only and don't contain additional program requirements.

- [About predictive background](https://developer.android.com/develop/ui/compose/system/predictive-back)
- [Add support for the predictive back gesture](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture)