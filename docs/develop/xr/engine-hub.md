---
title: https://developer.android.com/develop/xr/engine-hub
url: https://developer.android.com/develop/xr/engine-hub
source: md.txt
---

## Android XR Engine Hub

A desktop tool for streamlining your XR development workflow. Android XR Engine Hub serves as your centralized mission control, managing device connections, runtime configurations, and streaming tools across multiple game engines.
<button class="devsite-dialog-button button button-primary gc-analytics-event" data-category="xr_engine_hub" data-label="xr_engine_hub_windows" data-action="download" data-modal-dialog-id="xr_engine_hub_windows"> Download Android XR Engine Hub </button>

*Currently available for Windows*
![](http://developer.android.com/static/images/develop/xr/engine-hub/engine-hub-hero.png)

### Key features

[![](http://developer.android.com/static/images/develop/xr/engine-hub/direct-preview-192px.svg)](http://developer.android.com/develop/xr/engine-hub/direct-preview)

### [Direct Preview](http://developer.android.com/develop/xr/engine-hub/direct-preview)

Direct Preview lets you test and iterate on complex interactions directly inside your game engine's editor using live data from the Android XR Device. This completely bypasses the usual, time-consuming build-and-deploy cycle within XR development. [Set up Direct Preview](http://developer.android.com/develop/xr/engine-hub/direct-preview) [![](http://developer.android.com/static/images/picto-icons/improve-performance.svg)](http://developer.android.com/develop/xr/engine-hub/performance-tracing)

### [Performance tracing \& Gemini analysis](http://developer.android.com/develop/xr/engine-hub/performance-tracing)

Capture high-frequency performance traces directly from the Engine Hub, visualize them instantly in the Perfetto Web UI, and diagnose bottlenecks with Gemini.

- **Perfetto integration**: Record detailed performance traces directly from the dedicated Performance page using on-screen device recording controls.
- **Local trace data reduction** : Automatically process raw `.perfetto` captures locally on your workstation into concise summaries of CPU and GPU utilization, frame timing stats, and dropped frames.
- **AI-powered diagnostics with Gemini**: Connect your Google AI Studio API key (BYOK) in Settings to analyze reduced trace summaries with Gemini and receive actionable frame rate optimization recommendations.
- **Automated visualization \& file management** : Open captured traces in the Perfetto Web UI with pre-configured viewport parameters (`visStart` and `visEnd`) and access saved captures from the default output directory.
[Analyze performance traces](http://developer.android.com/develop/xr/engine-hub/performance-tracing) [![](http://developer.android.com/static/images/picto-icons/prepare.svg)](http://developer.android.com/develop/xr/engine-hub/manage-devices#sideload-apk)

### [Sideload APK \& package installation](http://developer.android.com/develop/xr/engine-hub/manage-devices#sideload-apk)

Install and test local APK builds directly on your connected Android XR device without switching to a command-line terminal.

- **Direct APK installation** : Browse and sideload local `.apk` files from the Device Actions card with real-time progress and status notifications.
- **Configurable install flags** : Enable **Allow Downgrade** (`-d`) to test older version codes or **Grant All Permissions** (`-g`) to automatically grant manifest permissions upon installation.
[Sideload an APK](http://developer.android.com/develop/xr/engine-hub/manage-devices#sideload-apk) [![](http://developer.android.com/static/images/picto-icons/policy.svg)](http://developer.android.com/develop/xr/engine-hub/manage-devices#feature-permissions)

### [Feature permissions controller](http://developer.android.com/develop/xr/engine-hub/manage-devices#feature-permissions)

Inspect and toggle runtime Android XR perception permissions for any installed application in real time.

- **XR capability groups** : View real-time status badges (**Granted** , **Denied** , or **Not Requested**) and toggle permissions for Head Tracking, Hand Tracking, Eye Tracking, Spatial Anchors, Scene Understanding, Camera, Microphone, and Face Tracking.
- **Batch \& granular controls** : Use **Grant All** or **Revoke All** to rapidly test permission states, or expand any capability group to toggle individual Android permission strings.
[Manage feature permissions](http://developer.android.com/develop/xr/engine-hub/manage-devices#feature-permissions) [![](http://developer.android.com/static/images/picto-icons/code.svg)](http://developer.android.com/develop/xr/engine-hub/manage-devices#adb-commands)

### [ADB commands \& shortcuts](http://developer.android.com/develop/xr/engine-hub/manage-devices#adb-commands)

Run custom ADB commands and one-click diagnostic presets directly from the Device Manager dashboard.

- **Built-in diagnostic presets**: Run one-click preset chips for Battery Status, Display Size, Third-Party Apps, WLAN IP Address, and Wake Up Screen.
- **Custom command shortcuts**: Execute arbitrary ADB commands with live exit codes and terminal output, and bookmark up to 10 custom commands as reusable shortcut chips.
[Run ADB commands](http://developer.android.com/develop/xr/engine-hub/manage-devices#adb-commands) ![](http://developer.android.com/static/images/picto-icons/brackets.svg)

### Device logcat streaming

Stream, inspect, and filter device logcat messages in real time with dedicated window controls, saved filter shortcuts, and smart search.

- **Standalone window**: Pop out the logcat viewer into a separate, resizable desktop window to support multi-monitor development setups.
- **Smart keyword filtering**: Filter log streams using case-insensitive searches matching both log tags and message content.
- **Filter shortcuts**: Bookmark up to 10 frequently used log filter queries as one-click shortcut chips.
![](http://developer.android.com/static/images/picto-icons/cast.svg)

### Screencasting

Mirror your Android XR device screen directly to your workstation in real time with high resolution and low latency.

- **Low-latency mirroring**: Stream real-time device visuals into a resizable desktop sub-window powered by an integrated scrcpy backend.
- **Interactive casting controls**: Start and stop screencasting sessions with a single click directly from the Engine Hub interface.
![](http://developer.android.com/static/images/picto-icons/text-images.svg)

### Screenshot \& screen recording

Capture screenshots and record video of your connected XR device display with a single click. Media is automatically saved and immediately opened in your default viewer for instant inspection. [![](http://developer.android.com/static/images/picto-icons/tools-2.svg)](http://developer.android.com/develop/xr/engine-hub/manage-devices)

### [Remote configuration](http://developer.android.com/develop/xr/engine-hub/manage-devices)

Configure device settings, debug toggles, and runtime performance overlays directly from the desktop interface.

- **Performance Insight** : Toggle **Show XR performance data overlay** to enable or disable real-time on-device performance metric overlays with a single click.
- **Stay awake mode** : Toggle **Stay awake while charging (even when doffed)** to prevent your headset from entering sleep mode between test sessions.
[Manage and debug devices](http://developer.android.com/develop/xr/engine-hub/manage-devices)

## Download Android XR Engine Hub

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

By using Android XR Engine Hub, you agree to the [Google Terms of Service](https://policies.google.com/terms). I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Android XR Engine Hub for Windows </button> [Download Android XR Engine Hub
for
Windows](https://dl.google.com/android_xr/dev_hub/AndroidXREngineHub_installer.exe)

*AndroidXREngineHub_installer.exe*