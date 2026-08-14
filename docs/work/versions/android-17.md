---
title: https://developer.android.com/work/versions/android-17
url: https://developer.android.com/work/versions/android-17
source: md.txt
---

This page provides an overview of the enterprise APIs, features, and behavior
changes introduced in Android 17 (API level 37). Some of the new enterprise
features and updates in Android 17 are described in the following sections:

## Agentic Automation on Android

A framework is established for AI agents to automate app workflows while
preventing automation inside work profiles. On fully managed devices and the
personal profile of COPE devices, administrators can disable AI automation
entirely by leveraging the existing [`setNearbyAppStreamingPolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNearbyAppStreamingPolicy(int)).

## Localhost Restriction

Cross-profile loopback traffic (e.g., to `127.0.0.1`) is restricted in Android
17 to safeguard corporate data. Read the behavior change guide on [blocking
cross profile loopback traffic](https://developer.android.com/about/versions/17/behavior-changes-all#block-cross-profile-loopback) for details.

## Local Network Protection

Android 17 introduces the `ACCESS_LOCAL_NETWORK` runtime permission for apps to
discover and communicate with local devices. IT administrators can pre-grant
this permission using [`setPermissionGrantState()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setPermissionGrantState(android.content.ComponentName,%20java.lang.String,%20java.lang.String,%20int)) to prevent workflow
disruptions. For more information, refer to [this local network permission
guide](https://developer.android.com/privacy-and-security/local-network-permission).

## Enable Certificate Transparency by default

Certificate Transparency (CT) verification will be enabled by default for
network connections to protect against MitM attacks. Connections relying on
private or internal certificates may fail unless those domains are explicitly
opted out using a custom [Network Security Configuration](https://developer.android.com/training/articles/security-config).

## Android Contacts Picker

The system Contacts Picker is enhanced to allow apps to receive full-fidelity
contact records across profile boundaries, transitioning to a secure one-by-one
user selection model. Cross-profile contact visibility remains governed by the
[`DevicePolicyManager.setCrossProfileContactsSearchDisabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setCrossProfileContactsSearchDisabled(android.content.ComponentName,%20boolean)) policy.

## Android HID API

Direct application access to raw Human Interface Device (HID) datastreams is now
gated behind the dangerous-level `ACCESS_HID` permission. Administrators can
implicitly block this access on enterprise-managed devices by using
[`DevicePolicyManager.setUsbDataSignalingEnabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUsbDataSignalingEnabled(boolean)) to disable USB data
signaling.

## USB4 and Thunderbolt Support

Enables high-speed USB4 and Thunderbolt PCIe tunneling, which actively respects
physical data layer restrictions. If USB data access is restricted using
[`DevicePolicyManager.setUsbDataSignalingEnabled`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUsbDataSignalingEnabled(boolean)), high-speed tunnels are
blocked to secure the device attack surface.

## Device State for LLMs

Authorized assistant applications can consume device-level data to on-device
agents using [the App Functions framework](https://developer.android.com/ai/appfunctions) to enable context-aware
responses. This won't return any data from work profiles, and admins can
globally disable this pipeline using
[`DevicePolicyManager.setAppFunctionsPolicy`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setAppFunctionsPolicy(int)) with the
[`DevicePolicyManager.APP_FUNCTIONS_DISABLED`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#APP_FUNCTIONS_DISABLED) flag.