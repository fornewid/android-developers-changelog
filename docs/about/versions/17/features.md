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
- [`TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE): Trigger occurs when an app is killed due to abnormal and excessive CPU usage and provides a call stack sample in response.

To understand how to set up the system trigger, see the documentation on
[trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) and how to [retrieve and analyze profiling data
documentation](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze).

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

## Privacy

Android 17 includes the following new features to improve user privacy.

### Android contacts picker

The Android Contact Picker is a standardized, browsable interface for users to
share contacts with your app. Available on devices running
Android 17 or higher, the picker offers a privacy-preserving
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
the `setHandoffEnabled()` method for the activity. Additional data may need to
be passed along with the handoff so the recreated activity on the receiving
device can restore appropriate state. Implement the
`onHandoffActivityRequested()` callback to return a `HandoffActivityData` object
which contains details that specify how Handoff should handle and recreate
the activity on the receiving device.

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
its position relative to multiple anchors by measuring the relative arrival
times of signals.

The following snippet demonstrates how to initialize the [Ranging Manager](https://developer.android.com/reference/android/ranging/RangingManager),
verify device capabilities, and start a DL-TDoA session:

### Kotlin

    class RangingApp {

        fun initDlTdoa(context: Context) {
            // Initialize the Ranging Manager
            val rangingManager = context.getSystemService(RangingManager::class.java)

            // Register for device capabilities
            val capabilitiesCallback = object : RangingManager.CapabilitiesCallback {
                override fun onRangingCapabilities(capabilities: RangingCapabilities) {
                    // Make sure Dl-TDoA is supported before starting the session
                    if (capabilities.uwbCapabilities != null && capabilities.uwbCapabilities!!.isDlTdoaSupported) {
                        startDlTDoASession(context)
                    }
                }
            }
            rangingManager.registerCapabilitiesCallback(Executors.newSingleThreadExecutor(), capabilitiesCallback)
        }

        fun startDlTDoASession(context: Context) {

            // Initialize the Ranging Manager
            val rangingManager = context.getSystemService(RangingManager::class.java)

            // Create session and configure parameters
            val executor = Executors.newSingleThreadExecutor()
            val rangingSession = rangingManager.createRangingSession(executor, RangingSessionCallback())
            val rangingRoundIndexes = intArrayOf(0)
            val config: ByteArray = byteArrayOf() // OOB config data
            val params = DlTdoaRangingParams.createFromFiraConfigPacket(config, rangingRoundIndexes)

            val rangingDevice = RangingDevice.Builder().build()
            val rawTagDevice = RawRangingDevice.Builder()
                .setRangingDevice(rangingDevice)
                .setDlTdoaRangingParams(params)
                .build()

            val dtTagConfig = RawDtTagRangingConfig.Builder(rawTagDevice).build()

            val preference = RangingPreference.Builder(DEVICE_ROLE_DT_TAG, dtTagConfig)
                .setSessionConfig(SessionConfig.Builder().build())
                .build()

            // Start the ranging session
            rangingSession.start(preference)
        }
    }

    private class RangingSessionCallback : RangingSession.Callback {
        override fun onDlTdoaResults(peer: RangingDevice, measurement: DlTdoaMeasurement) {
            // Process measurement results here
        }
    }

### Java

    public class RangingApp {

        public void initDlTdoa(Context context) {

            // Initialize the Ranging Manager
            RangingManager rangingManager = context.getSystemService(RangingManager.class);

            // Register for device capabilities
            RangingManager.CapabilitiesCallback capabilitiesCallback = new RangingManager.CapabilitiesCallback() {
                @Override
                public void onRangingCapabilities(RangingCapabilities capabilities) {
                    // Make sure Dl-TDoA is supported before starting the session
                    if (capabilities.getUwbCapabilities() != null && capabilities.getUwbCapabilities().isDlTdoaSupported) {
                        startDlTDoASession(context);
                    }
                }
            };
            rangingManager.registerCapabilitiesCallback(Executors.newSingleThreadExecutor(), capabilitiesCallback);
        }

        public void startDlTDoASession(Context context) {
            RangingManager rangingManager = context.getSystemService(RangingManager.class);

            // Create session and configure parameters
            Executor executor = Executors.newSingleThreadExecutor();
            RangingSession rangingSession = rangingManager.createRangingSession(executor, new RangingSessionCallback());
            int[] rangingRoundIndexes = new int[] {0};
            byte[] config = new byte[0]; // OOB config data
            DlTdoaRangingParams params = DlTdoaRangingParams.createFromFiraConfigPacket(config, rangingRoundIndexes);

            RangingDevice rangingDevice = new RangingDevice.Builder().build();
            RawRangingDevice rawTagDevice = new RawRangingDevice.Builder()
                    .setRangingDevice(rangingDevice)
                    .setDlTdoaRangingParams(params)
                    .build();

            RawDtTagRangingConfig dtTagConfig = new RawDtTagRangingConfig.Builder(rawTagDevice).build();

            RangingPreference preference = new RangingPreference.Builder(DEVICE_ROLE_DT_TAG, dtTagConfig)
                    .setSessionConfig(new SessionConfig.Builder().build())
                    .build();

            // Start the ranging session
            rangingSession.start(preference);
        }

        private static class RangingSessionCallback implements RangingSession.Callback {

            @Override
            public void onDlTdoaResults(RangingDevice peer, DlTdoaMeasurement measurement) {
                // Process measurement results here
            }
        }
    }

### Out-of-Band (OOB) Configurations

The following snippet provides an example of DL-TDoA OOB configuration data for
Wi-Fi and BLE:

### Java

    // Wifi Configuration
    byte[] wifiConfig = {
        (byte) 0xDD, (byte) 0x2D, (byte) 0x5A, (byte) 0x18, (byte) 0xFF, // Header
        (byte) 0x5F, (byte) 0x19, // FiRa Sub-Element
        (byte) 0x02, (byte) 0x00, // Profile ID
        (byte) 0x06, (byte) 0x02, (byte) 0x20, (byte) 0x08, // MAC Address
        (byte) 0x14, (byte) 0x01, (byte) 0x0C, // Preamble Index
        (byte) 0x27, (byte) 0x02, (byte) 0x08, (byte) 0x07, // Vendor ID
        (byte) 0x28, (byte) 0x06, (byte) 0xCA, (byte) 0xC8, (byte) 0xA6, (byte) 0xF7, (byte) 0x6F, (byte) 0x08, // Static STS IV
        (byte) 0x08, (byte) 0x02, (byte) 0x60, (byte) 0x09, // Slot Duration
        (byte) 0x1B, (byte) 0x01, (byte) 0x0A, // Slots per RR
        (byte) 0x09, (byte) 0x04, (byte) 0xE8, (byte) 0x03, (byte) 0x00, (byte) 0x00, // Duration
        (byte) 0x9F, (byte) 0x04, (byte) 0x67, (byte) 0x45, (byte) 0x23, (byte) 0x01  // Session ID
    };

    // BLE Configuration
    byte[] bleConfig = {
        (byte) 0x2D, (byte) 0x16, (byte) 0xF4, (byte) 0xFF, // Header
        (byte) 0x5F, (byte) 0x19, // FiRa Sub-Element
        (byte) 0x02, (byte) 0x00, // Profile ID
        (byte) 0x06, (byte) 0x02, (byte) 0x20, (byte) 0x08, // MAC Address
        (byte) 0x14, (byte) 0x01, (byte) 0x0C, // Preamble Index
        (byte) 0x27, (byte) 0x02, (byte) 0x08, (byte) 0x07, // Vendor ID
        (byte) 0x28, (byte) 0x06, (byte) 0xCA, (byte) 0xC8, (byte) 0xA6, (byte) 0xF7, (byte) 0x6F, (byte) 0x08, // Static STS IV
        (byte) 0x08, (byte) 0x02, (byte) 0x60, (byte) 0x09, // Slot Duration
        (byte) 0x1B, (byte) 0x01, (byte) 0x0A, // Slots per RR
        (byte) 0x09, (byte) 0x04, (byte) 0xE8, (byte) 0x03, (byte) 0x00, (byte) 0x00, // Duration
        (byte) 0x9F, (byte) 0x04, (byte) 0x67, (byte) 0x45, (byte) 0x23, (byte) 0x01  // Session ID
    };

If you can't use an OOB configuration because it is missing, or if you need to
change default values that aren't in the OOB config, you can build parameters
with `DlTdoaRangingParams.Builder` as shown in the following snippet. You can use
these parameters in place of `DlTdoaRangingParams.createFromFiraConfigPacket()`:

### Kotlin

    val dlTdoaParams = DlTdoaRangingParams.Builder(1)
        .setComplexChannel(UwbComplexChannel.Builder()
                .setChannel(9).setPreambleIndex(10).build())
        .setDeviceAddress(deviceAddress)
        .setSessionKeyInfo(byteArrayOf(0x01, 0x02, 0x03, 0x04))
        .setRangingIntervalMillis(240)
        .setSlotDuration(UwbRangingParams.DURATION_2_MS)
        .setSlotsPerRangingRound(20)
        .setRangingRoundIndexes(byteArrayOf(0x01, 0x05))
        .build()

### Java

    DlTdoaRangingParams dlTdoaParams = new DlTdoaRangingParams.Builder(1)
        .setComplexChannel(new UwbComplexChannel.Builder()
                .setChannel(9).setPreambleIndex(10).build())
        .setDeviceAddress(deviceAddress)
        .setSessionKeyInfo(new byte[]{0x01, 0x02, 0x03, 0x04})
        .setRangingIntervalMillis(240)
        .setSlotDuration(UwbRangingParams.DURATION_2_MS)
        .setSlotsPerRangingRound(20)
        .setRangingRoundIndexes(new byte[]{0x01, 0x05})
        .build();