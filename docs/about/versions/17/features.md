---
title: https://developer.android.com/about/versions/17/features
url: https://developer.android.com/about/versions/17/features
source: md.txt
---

<br />

Android 17 introduces great new features and APIs for developers. The following
sections summarize these features to help you get started with the related APIs.

For a detailed list of new, modified, and removed APIs, read the [API diff
report](https://developer.android.com/sdk/api_diff/c-beta2/changes). For details on new APIs visit the [Android API reference](https://developer.android.com/reference) --- new
APIs are highlighted for visibility.

You should also review areas where platform changes might affect your apps. For
more information, see the following pages:

- [Behavior changes that affect apps when they target Android 17](https://developer.android.com/about/versions/17/behavior-changes-17)
- [Behavior changes that affect all apps regardless of `targetSdkVersion`](https://developer.android.com/about/versions/17/behavior-changes-all).

> [!NOTE]
> **Note:** This page lists some of the more important new features. For more detailed information, see the [Android 17 release notes](https://developer.android.com/about/versions/17/release-notes).

## Core functionality

Android 17 adds the following new features related to core Android
functionality.

### New ProfilingManager triggers

Android 17 adds several new system triggers to [`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/overview) to
help you collect in-depth data to debug performance issues.

The new triggers are:

- [`TRIGGER_TYPE_COLD_START`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_COLD_START): Trigger occurs during app cold start. It provides both a call stack sample and a system trace in the response.
- [`TRIGGER_TYPE_OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM): Trigger occurs when an app throws an [`OutOfMemoryError`](https://developer.android.com/reference/java/lang/OutOfMemoryError) and provides a Java Heap Dump in response.
- [`TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE): Trigger occurs when an app is killed due to abnormal and excessive CPU usage and provides a snapshot of a running background system trace in response.
- [`TRIGGER_TYPE_ANOMALY`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANOMALY): Detect system performance anomalies such as excessive binder calls and excessive memory usage.

To understand how to set up the system trigger, see the documentation on
[trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) and how to [retrieve and upload
profiles](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker) and [analyze profiling data](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze).

#### Profiling trigger for app anomalies

Android 17
introduces an on-device anomaly detection service that monitors for
resource-intensive behaviors and potential compatibility regressions. Integrated
with [`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/overview), this service allows your app to receive profiling
artifacts triggered by specific system-detected events.

Use the [`TRIGGER_TYPE_ANOMALY`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_ANOMALY) trigger to detect system performance issues
such as excessive binder calls and excessive memory usage. When an app breaches
OS-defined memory limits, the anomaly trigger allows developers to receive
app-specific heap dumps to help identify and fix memory issues. Additionally,
for excessive binder spam, the anomaly trigger provides a stack sampling profile
on binder transactions.

This API callback occurs prior to any system imposed enforcements. For
example, it can help developers collect debug data before the app is
terminated by the system for exceeding memory limits.

    fun registerAnomalyTrigger(context: Context) {
        val profilingManager =
            context.getSystemService(ProfilingManager::class.java) ?: return
        val triggers = listOf(
            ProfilingTrigger.Builder(ProfilingTrigger.TRIGGER_TYPE_ANOMALY).build()
        )
        val callbackExecutor: Executor = Executors.newSingleThreadExecutor()
        val resultCallback = Consumer<ProfilingResult> { profilingResult ->
            if (profilingResult.errorCode == ProfilingResult.ERROR_NONE) {
                // Upload profile result to server for further analysis
                profilingResult.resultFilePath?.let { setupProfileUploadWorker(it) }
            }
        }
        profilingManager.registerForAllProfilingResults(
            callbackExecutor,
            resultCallback
        )
        profilingManager.addProfilingTriggers(triggers)
    }

### JobDebugInfo APIs

Android 17 introduces new `JobDebugInfo` APIs to help developers debug
their JobScheduler jobs--why they aren't running, how long they ran for, and
other aggregated information.

The first method of the expanded JobDebugInfo APIs is
`getPendingJobReasonStats()`, which returns a map of [reasons why the job was in
a pending execution state](https://developer.android.com/reference/android/app/job/JobScheduler#constants_1) and their respective cumulative pending
durations. This method joins the [`getPendingJobReasonsHistory()`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReasonsHistory(int)) and
[`getPendingJobReasons()`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReasons(int)) methods to give you insight into why a scheduled
job is not running as expected, but simplifies information retrieval by making
both duration and job reason available in a single method.

For example, for a specified `jobId`, the method might return
`PENDING_JOB_REASON_CONSTRAINT_CHARGING` and a duration of 60000 ms, indicating
the job was pending for 60000ms due to the charging constraint not being
satisfied.

### Reduce wake locks with listener support for allow-while-idle alarms

Android 17
introduces a new variant of [`AlarmManager.setExactAndAllowWhileIdle`](https://developer.android.com/reference/android/app/AlarmManager#setExactAndAllowWhileIdle(int,%20long,%20java.lang.String,%20java.util.concurrent.Executor,%20android.app.AlarmManager.OnAlarmListener)) that
accepts an [`OnAlarmListener`](https://developer.android.com/reference/android/app/AlarmManager.OnAlarmListener) instead of a `PendingIntent`. This new
callback-based mechanism is ideal for apps that currently rely on continuous
wakelocks to perform periodic tasks, such as messaging apps maintaining socket
connections.

## Privacy

Android 17 includes the following new features to improve user privacy.

### Encrypted Client Hello (ECH) platform support

Android 17 introduces platform support for Encrypted Client Hello (ECH), a
significant privacy enhancement for network communications. ECH is a TLS 1.3
extension that encrypts the Server Name Indication (SNI) during the initial TLS
handshake. This encryption helps protect user privacy by making it more
difficult for network intermediaries to identify the specific domain an app is
connecting to.

The platform now includes the necessary APIs for networking libraries to
implement ECH. This includes new capabilities in [`DnsResolver`](https://developer.android.com/reference/android/net/DnsResolver) to query for
HTTPS DNS records containing ECH configurations, and new methods in Conscrypt's
SSLEngines and SSLSockets to enable ECH by passing in these configurations when
connecting to a domain. Developers can configure ECH preferences, such as
enabling it opportunistically or mandating its use, through the new
[`<domainEncryption>`](https://developer.android.com/privacy-and-security/security-config#domainEncryption) element within the Network Security Configuration file,
applicable globally or on a per-domain basis.

Popular networking libraries such as HttpEngine, WebView, and OkHttp are
expected to integrate these platform APIs in future updates, making it easier
for apps to adopt ECH and enhance user privacy.

For more information, see the [Encrypted Client Hello](https://developer.android.com/privacy-and-security/security-config#EncryptedClientHelloSummary) documentation.

### Android contacts picker

The Android Contact Picker is a standardized, browsable interface for users to
share contacts with your app. Available on devices running
Android 17 (API level 37) or higher, the picker offers a privacy-preserving
alternative to the broad `READ_CONTACTS` permission. Instead of requesting
access to the user's entire address book, your app specifies the data fields it
needs, such as phone numbers or email addresses, and the user selects specific
contacts to share. This grants your app read access to only the selected data,
ensuring granular control while providing a consistent user experience with
built-in search, profile switching, and multi-selection capabilities without
having to build or maintain the UI.

For more information, see the [contact picker documentation](https://developer.android.com/about/versions/17/features/contact-picker).

## Security

Android 17 adds the following new features to improve device and app
security.

### Android Advanced Protection Mode (AAPM)

Android Advanced Protection Mode offers Android users a powerful new set of
security features, marking a significant step in safeguarding users---particularly
those at higher risk---from sophisticated attacks. Designed as an opt-in feature,
AAPM is activated with a single configuration setting that users can turn on at
any time to apply an opinionated set of security protections.

These core configurations include blocking app installation from unknown sources
(sideloading), restricting USB data signaling, and mandating Google Play Protect
scanning, which significantly reduces the device's attack surface area.
Developers can integrate with this feature using the
[`AdvancedProtectionManager`](https://developer.android.com/reference/android/security/advancedprotection/AdvancedProtectionManager) API to detect the mode's status, enabling
applications to automatically adopt a hardened security posture or restrict
high-risk functionality when a user has opted in.

### PQC APK Signing

Android now supports a hybrid APK signature scheme to future-proof your app's
signing identity against the potential threat of attacks that make use of
quantum computing. This feature introduces a new APK Signature Scheme, which
lets you pair a classical signing key (such as RSA or EC) with a new
post-quantum cryptography (PQC) algorithm (ML-DSA).

This hybrid approach ensures your app remains secure against future quantum
attacks while maintaining full backward compatibility with older Android
versions and devices that rely on classical signature verification.

> [!NOTE]
> **Note:** You will need to create a new classical signing key to pair with the PQC key. You cannot reuse your pre-hybrid classical signing key.

#### Impact on developers

- **Apps using Play App Signing:** If you use Play App Signing, you can wait for Google Play to give you the option to upgrade a hybrid signature using a PQC key generated by Google Play, ensuring your app is protected without requiring manual key management.
- **Apps using self-managed keys:** Developers who manage their own signing keys can utilize updated Android build tools (like apksigner) to rotate to a hybrid identity, combining a PQC key with a new classical key. (You must create a new classical key, you cannot reuse the older one.)

## Connectivity

Android 17 adds the following features to improve device and app
connectivity.

### Constrained satellite networks

Implements optimizations to enable apps to function effectively over
low-bandwidth satellite networks.

> [!NOTE]
> **Note:** This feature went live with the Android 16 QPR2 quarterly release. For more information, see [Develop for constrained satellite
> networks](https://developer.android.com/develop/connectivity/satellite/constrained-networks).

## User experience and system UI

Android 17 includes the following changes to improve user experience.

### Dedicated Assistant volume stream

Android 17 introduces a dedicated Assistant volume stream for Assistant apps,
for playback with [`USAGE_ASSISTANT`](https://developer.android.com/reference/android/media/AudioAttributes#USAGE_ASSISTANT). This change decouples Assistant audio
from the standard media stream, providing users with isolated control over both
volumes. This enables scenarios such as muting media playback while maintaining
audibility for Assistant responses, and the other way around.

Assistant apps with access to the new [`MODE_ASSISTANT_CONVERSATION`](https://developer.android.com/reference/android/media/AudioManager#MODE_ASSISTANT_CONVERSATION) audio
mode can further improve the volume control consistency. Assistant apps can use
this mode to provide a hint to the system about an active Assistant session,
ensuring the Assistant stream can be controlled outside of the active
`USAGE_ASSISTANT` playback or with connected Bluetooth peripherals.

### Handoff

Handoff is a new feature and API coming to Android 17 that app
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
the
[`setHandoffEnabled()`](https://developer.android.com/reference/android/app/Activity#setHandoffEnabled(boolean,%20android.app.HandoffActivityParams))
method for the activity. Additional data may need to be passed along with the
handoff so the recreated activity on the receiving device can restore
appropriate state. Implement the
[`onHandoffActivityDataRequested()`](https://developer.android.com/reference/android/app/Activity#onHandoffActivityDataRequested(android.app.HandoffActivityDataRequestInfo))
callback to return a
[`HandoffActivityData`](https://developer.android.com/reference/android/app/HandoffActivityData) object which
contains details that specify how Handoff should handle and recreate the
activity on the receiving device.

### Live Update - Semantic color API

With Android 17, [Live Update](https://developer.android.com/develop/ui/views/notifications/live-update) launches the Semantic Coloring APIs to
support colors with universal meaning.

The following classes support semantic coloring:

- [`Notification`](https://developer.android.com/partners/android-17/features/semantic-coloring/reference/Notification)
- [`Notification.Metric`](https://developer.android.com/partners/android-17/features/semantic-coloring/reference/Notification.Metric)
- [`Notification.ProgressStyle.Point`](https://developer.android.com/partners/android-17/features/semantic-coloring/reference/Notification.ProgressStyle.Point)
- [`Notification.ProgressStyle.Segment`](https://developer.android.com/partners/android-17/features/semantic-coloring/reference/Notification.ProgressStyle.Segment)

#### Coloring

- Green: Associated with safety. This color should be used for the case where it lets people know you are in the safe situation.
- Orange: For designating caution and marking physical hazards. This color should be used in the situation where users need to pay attention to set better protection setting.
- Red: Generally indicates danger, stop. It should be presented for the case where need people's attention urgently.
- Blue: Neutral color for content that is informational and should stand out from other content.

The following example shows how to apply semantic styles to text in a notification:

      val ssb = SpannableStringBuilder()
            .append("Colors: ")
            .append("NONE", Notification.createSemanticStyleAnnotation(SEMANTIC_STYLE_UNSPECIFIED), 0)
            .append(", ")
            .append("INFO", Notification.createSemanticStyleAnnotation(SEMANTIC_STYLE_INFO), 0)
            .append(", ")
            .append("SAFE", Notification.createSemanticStyleAnnotation(SEMANTIC_STYLE_SAFE), 0)
            .append(", ")
            .append("CAUTION", Notification.createSemanticStyleAnnotation(SEMANTIC_STYLE_CAUTION), 0)
            .append(", ")
            .append("DANGER", Notification.createSemanticStyleAnnotation(SEMANTIC_STYLE_DANGER), 0)

        Notification.Builder(context, channelId)
              .setSmallIcon(R.drawable.ic_icon)
              .setContentTitle("Hello World!")
              .setContentText(ssb)
              .setOngoing(true)
                  .setRequestPromotedOngoing(true)

### UWB Downlink-TDoA API for Android 17

Downlink Time Difference of Arrival (DL-TDoA) ranging lets a device determine
its position relative to multiple UWB anchors by measuring the relative arrival
times of signals.

> [!NOTE]
> **Note:** To use DL-TDoA ranging, the calling app must request and be granted `Manifest.permission.ACCESS_FINE_LOCATION`, and `Manifest.permission.ACCESS_BACKGROUND_LOCATION` if ranging is required while the app is in the background. For more information, see [Request location
> permissions](https://developer.android.com/develop/sensors-and-location/location/permissions).

For more information and code samples, see [UWB Downlink-TDoA
API](https://developer.android.com/develop/connectivity/ranging#dl-tdoa-api-android).