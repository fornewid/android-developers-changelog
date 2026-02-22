---
title: Features and APIs  |  Android Developers
url: https://developer.android.com/about/versions/17/features
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Releases](https://developer.android.com/about/versions)

# Features and APIs Stay organized with collections Save and categorize content based on your preferences.




Android 17 introduces great new features and APIs for developers. The following
sections summarize these features to help you get started with the related APIs.

For a detailed list of new, modified, and removed APIs, read the [API diff
report](/sdk/api_diff/c-dp1/changes). For details on new APIs visit the [Android API reference](/reference) — new
APIs are highlighted for visibility.

You should also review areas where platform changes might affect your apps. For
more information, see the following pages:

* [Behavior changes that affect apps when they target Android 17](/about/versions/17/behavior-changes-17)
* [Behavior changes that affect all apps regardless of `targetSdkVersion`](/about/versions/17/behavior-changes-all).

**Note:** This page lists some of the more important new features. For more detailed
information, see the [Android 17 release notes](/about/versions/17/release-notes).

## Core functionality

Android 17 adds the following new features related to core Android
functionality.

### New ProfilingManager triggers

Android 17 adds several new system triggers to [`ProfilingManager`](/topic/performance/tracing/profiling-manager/overview) to
help you collect in-depth data to debug performance issues.

The new triggers are:

* [`TRIGGER_TYPE_COLD_START`](/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_COLD_START): Trigger occurs during app cold start. It
  provides both a call stack sample and a system trace in the response.
* [`TRIGGER_TYPE_OOM`](/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM): Trigger occurs when an app throws an
  [`OutOfMemoryError`](/reference/java/lang/OutOfMemoryError) and provides a Java Heap Dump in response.
* [`TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE`](/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE): Trigger occurs when an app is
  killed due to abnormal and excessive CPU usage and provides a call stack
  sample in response.

To understand how to set up the system trigger, see the documentation on
[trigger-based profiling](/topic/performance/tracing/profiling-manager/trigger-based-capture) and how to [retrieve and analyze profiling data
documentation](/topic/performance/tracing/profiling-manager/retrieve-and-analyze).

## Security

Android 17 adds the following new features to improve device and app
security.

### Android Advanced Protection Mode (AAPM)

Android Advanced Protection Mode offers Android users a powerful new set of
security features, marking a significant step in safeguarding users—particularly
those at higher risk—from sophisticated attacks. Designed as an opt-in feature,
AAPM is activated with a single configuration setting that users can turn on at
any time to apply an opinionated set of security protections.

These core configurations include blocking app installation from unknown sources
(sideloading), restricting USB data signaling, and mandating Google Play Protect
scanning, which significantly reduces the device's attack surface area.
Developers can integrate with this feature using the
[`AdvancedProtectionManager`](/reference/android/security/advancedprotection/AdvancedProtectionManager) API to detect the mode's status, enabling
applications to automatically adopt a hardened security posture or restrict
high-risk functionality when a user has opted in.

## Connectivity

Android 17 adds the following features to improve device and app
connectivity.

### Constrained satellite networks

Implements optimizations to enable apps to function effectively over
low-bandwidth satellite networks.

**Note:** This feature went live with the Android 16 QPR2 quarterly release.
For more information, see [Develop for constrained satellite
networks](/develop/connectivity/satellite/constrained-networks).

## User experience and system UI

Android 17 includes the following changes to improve user experience.

### Handoff

Handoff is a new feature and API coming to Android 17 that app
developers can integrate with to provide cross-device continuity for their
users. It allows the user to start an app activity on one Android device and
transition it to another Android device. Handoff runs in the background of a
user's device and surfaces available activities from the user's other nearby
devices through various entry points, like the launcher and taskbar, on the
receiving device.

Apps can designate Handoff to launch the same native Android app, if it is
installed and available on the receiving device. In this app-to-app flow, the
user is deep-linked to the designated activity. Alternatively, app-to-web
Handoff can be offered as a fallback option or directly implemented with URL
Handoff.

Handoff support is implemented on a per-activity basis. To enable Handoff, call
the `setHandoffEnabled()` method for the activity. Additional data may need to
be passed along with the handoff so the recreated activity on the receiving
device can restore appropriate state. Implement the
`onHandoffActivityRequested()` callback to return a `HandoffActivityData` object
which contains details that specify how Handoff should handle and recreate
the activity on the receiving device.