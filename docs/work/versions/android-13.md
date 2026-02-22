---
title: https://developer.android.com/work/versions/android-13
url: https://developer.android.com/work/versions/android-13
source: md.txt
---

This page provides an overview of the new enterprise APIs, features, and
behavior changes introduced in Android 13 (API level 33).

## New Security Logs

To standardize the audit output on the device to meet the requirements of the
[Common Criteria Protection Profile for Mobile Device Fundamentals](https://www.niap-ccevs.org/Profile/Info.cfm?PPID=455&id=455)
(PP_MDF), additional audit events have been added to the SecurityLog that were
previously only available in logcat. The events are focused on Wi-Fi and
Bluetooth connectivity.

## Behavior changes

In Android 13 (API level 33) and higher, internet connectivity is required by
default to provision company-owned devices. If a device is expected to be
provisioned offline or in a closed-network environment, EMMs must include the
following flag in the provisioning extras:  

    DevicePolicyManager.EXTRA_PROVISIONING_ALLOW_OFFLINE = "android.app.extra.PROVISIONING_ALLOW_OFFLINE"

Provisioning without internet connectivity results in a loss of functionality,
so EMMs should only use this flag when devices can't access the internet as part
of deployment requirements.

## Deprecations

Android 13 (API level 33) and higher includes the following notable API
deprecation:

- `android.app.extra.PROVISIONING_LOGO_URI` is fully deprecated in Android 13 and higher. Logo customization is no longer supported during the provisioning flows.