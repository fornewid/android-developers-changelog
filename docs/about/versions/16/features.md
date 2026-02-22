---
title: https://developer.android.com/about/versions/16/features
url: https://developer.android.com/about/versions/16/features
source: md.txt
---

<br />

Android 16 introduces great new features and APIs for developers. The following
sections summarize these features to help you get started with the related APIs.
For a detailed list of new, modified, and removed APIs, read the [API diff
report](https://developer.android.com/sdk/api_diff/b-beta1/changes). For details on new APIs visit the [Android API reference](https://developer.android.com/reference) --- new APIs are highlighted for visibility.

You should also review areas where platform changes might affect your apps. For
more information, see the following pages:

- [Behavior changes that affect apps when they target Android 16](https://developer.android.com/about/versions/16/behavior-changes-16)
- [Behavior changes that affect all apps regardless of `targetSdkVersion`](https://developer.android.com/about/versions/16/behavior-changes-all).

## Core functionality

Android includes new APIs that expand core capabilities of the Android system.

### Two Android API releases in 2025

- This preview is for the next major release of Android with a planned launch in Q2 of 2025. This release is similar to all of our API releases in the past, where we can have planned behavior changes that are often tied to a targetSdkVersion.
- We're planning the major release a quarter earlier (Q2 rather than Q3 in prior years) to better align with the schedule of device launches across our ecosystem, so more devices can get the major release of Android sooner. With the major release coming in Q2, you'll need to do your annual compatibility testing a few months earlier than in previous years to make sure your apps are ready.
- We plan to have another release in Q4 of 2025 which also will include new developer APIs. The Q2 major release will be the only release in 2025 to include planned behavior changes that could affect apps.

In addition to new developer APIs, the Q4 minor release will pick up feature
updates, optimizations, and bug fixes; it will not include any app-impacting
behavior changes.
![Timeline view of Android releases in 2025, noting that the 25Q2
release is a major release and the 25Q4 release is a minor release.](https://developer.android.com/static/about/versions/16/images/2025-releases.png)

We'll continue to have quarterly Android releases. The Q1 and Q3 updates
in-between the API releases will provide incremental updates to help ensure
continuous quality. We're actively working with our device partners to bring the
Q2 release to as many devices as possible.

#### Using new APIs with major and minor releases

Guarding a code block with a check for API level is done today using
the [`SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT) constant with
[`VERSION_CODES`](https://developer.android.com/reference/android/os/Build.VERSION_CODES). This will continue
to be supported for major Android releases.  

    if (SDK_INT >= VERSION_CODES.BAKLAVA) {
      // Use APIs introduced in Android 16
    }

The new [`SDK_INT_FULL`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT_FULL)
constant can be used for API checks against both major and minor versions with
the new [`VERSION_CODES_FULL`](https://developer.android.com/reference/android/os/Build.VERSION_CODES_FULL)
enumeration.  

    if (SDK_INT_FULL >= VERSION_CODES_FULL.[MAJOR or MINOR RELEASE]) {
      // Use APIs introduced in a major or minor release
    }

You can also use the
[`Build.getMinorSdkVersion()`](https://developer.android.com/reference/android/os/Build#getMinorSdkVersion%28int%29)
method to get just the minor SDK version.  

    val minorSdkVersion = Build.getMinorSdkVersion(VERSION_CODES_FULL.BAKLAVA)

These APIs have not yet been finalized and are subject to change, so please send
us [feedback](https://developer.android.com/about/versions/16/feedback) if you have any concerns.
| **Note:** There's no change to the [target API level
| requirements](https://developer.android.com/google/play/requirements/target-sdk) and the associated dates for apps in Google Play; our plans are for one annual requirement each year, and that will be tied to the major API level.

## User experience and system UI

Android 16 gives app developers and users more control and flexibility for
configuring their device to fit their needs.

### Progress-centric notifications

Android 16 introduces progress-centric notifications to help users seamlessly
track user-initiated, start-to-end journeys.

[`Notification.ProgressStyle`](https://developer.android.com/reference/android/app/Notification.ProgressStyle) is a new notification
style that lets you create progress-centric notifications. Key use cases include
rideshare, delivery, and navigation. Within the `Notification.ProgressStyle`
class, you can denote states and milestones in a user journey using
[points](https://developer.android.com/reference/android/app/Notification.ProgressStyle.Point) and [segments](https://developer.android.com/reference/android/app/Notification.ProgressStyle.Segment).

To learn more, see the
[Progress-centric notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications)
documentation page.  
![](https://developer.android.com/static/about/versions/16/images/progress-style-lockscreen.png)  
A progress-centric notification displayed on the lockscreen.  
![](https://developer.android.com/static/about/versions/16/images/progress-style-notification-shade.png)  
A progress-centric notification displayed in the notification shade.

<br />

### Predictive back updates

Android 16 adds new APIs to help you enable predictive back system animations in
gesture navigation such as the back-to-home animation. [Registering the
`onBackInvokedCallback`](https://developer.android.com/reference/android/window/OnBackInvokedDispatcher#registerOnBackInvokedCallback(int,%20android.window.OnBackInvokedCallback)) with the new
[`PRIORITY_SYSTEM_NAVIGATION_OBSERVER`](https://developer.android.com/reference/android/window/OnBackInvokedDispatcher#PRIORITY_SYSTEM_NAVIGATION_OBSERVER) allows your app to
receive the regular [`onBackInvoked`](https://developer.android.com/reference/android/window/OnBackInvokedCallback#onBackInvoked()) call whenever the
system handles a back navigation without impacting the normal back navigation
flow.

Android 16 additionally adds the
[`finishAndRemoveTaskCallback()`](https://developer.android.com/reference/android/window/SystemOnBackInvokedCallbacks#finishAndRemoveTaskCallback(android.app.Activity)) and
[`moveTaskToBackCallback`](https://developer.android.com/reference/android/window/SystemOnBackInvokedCallbacks#moveTaskToBackCallback(android.app.Activity))(). By registering these callbacks
with the [`OnBackInvokedDispatcher`](https://developer.android.com/reference/android/window/OnBackInvokedDispatcher), the system can trigger
specific behaviors and play corresponding ahead-of-time animations when the back
gesture is invoked.

### Richer haptics

Android has exposed control over the haptic actuator ever since its inception.

Android 11 added support for more complex haptic effects that more advanced
actuators could support through
[`VibrationEffect.Compositions`](https://developer.android.com/reference/android/os/VibrationEffect.Composition) of device-defined semantic
primitives.

Android 16 adds [haptic APIs](https://developer.android.com/reference/android/os/vibrator/package-summary) that let apps define the
amplitude and frequency curves of a haptic effect while abstracting away
differences between device capabilities.

## Developer productivity and tools

While most of our work to improve your productivity centers around tools like
[Android Studio](https://developer.android.com/studio), [Jetpack Compose](https://developer.android.com/jetpack/compose), and the [Android
Jetpack](https://developer.android.com/jetpack) libraries, we always look for ways in the platform to help
you realize your vision.

### Content handling for live wallpapers

In Android 16, the live wallpaper framework is gaining a new content API to
address the challenges of dynamic, user-driven wallpapers. Currently, live
wallpapers incorporating user-provided content require complex, service-specific
implementations. Android 16 introduces
[`WallpaperDescription`](https://developer.android.com/reference/android/app/wallpaper/WallpaperDescription) and
[`WallpaperInstance`](https://developer.android.com/reference/android/app/wallpaper/WallpaperInstance). WallpaperDescription lets you
identify distinct instances of a live wallpaper from the same service. For
example, a wallpaper that has instances on both the home screen and on the lock
screen may have unique content in both places. The wallpaper picker and
[`WallpaperManager`](https://developer.android.com/reference/android/app/WallpaperManager) use this metadata to better present
wallpapers to users, streamlining the process for you to create diverse and
personalized live wallpaper experiences.

## Performance and battery

Android 16 introduces APIs that help gather insights about your apps.

### System-triggered profiling

[`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) was
[added in Android 15](https://developer.android.com/about/versions/15/features#app-start-info), giving apps the ability to
request profiling data collection using Perfetto on public devices in the field.
However, since this profiling must be started from the app, critical flows such
as startups or ANRs would be difficult or impossible for apps to capture.

To help with this, Android 16 introduces system-triggered profiling to
`ProfilingManager`. Apps can register interest in receiving traces for certain
triggers such as cold start [`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn())
or ANRs, and then the system starts and stops a trace on the app's behalf. After
the trace completes, the results are delivered to the app's data directory.

### Start component in ApplicationStartInfo

`ApplicationStartInfo` was [added in Android
15](https://developer.android.com/about/versions/15/features#app-start-info), allowing an app to see reasons
for process start, start type, start times, throttling, and other useful
diagnostic data. Android 16 adds
[`getStartComponent()`](https://developer.android.com/reference/android/app/ApplicationStartInfo#getStartComponent())
to distinguish what component type triggered the start, which can be helpful for
optimizing the startup flow of your app.

### Better job introspection

The [`JobScheduler#getPendingJobReason()`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReason(int)) API returns a reason why a job
might be pending. However, a job might be pending for multiple reasons.

In Android 16, we are introducing a new API
[`JobScheduler#getPendingJobReasons(int jobId)`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReasons(int)), which returns multiple
reasons why a job is pending, due to both explicit constraints set by the
developer and implicit constraints set by the system.

We're also introducing
[`JobScheduler#getPendingJobReasonsHistory(int jobId)`](https://developer.android.com/reference/android/app/job/JobScheduler#getPendingJobReasonsHistory(int)), which returns a list
of the most recent constraint changes.

We recommend using the API to help you debug why your jobs may not be executing,
especially if you're seeing reduced success rates of certain tasks or have bugs
around latency of certain job completion. For example, updating widgets in the
background failed to occur or prefetch job failed to be called prior to app
start.

This can also better help you understand if certain jobs are not completing due
to system defined constraints versus explicitly set constraints.

### Adaptive refresh rate

Adaptive refresh rate (ARR), introduced in Android 15, enables the display
refresh rate on supported hardware to adapt to the content frame rate using
discrete VSync steps. This reduces power consumption while eliminating the need
for potentially jank-inducing mode-switching.

Android 16 introduces [`hasArrSupport()`](https://developer.android.com/reference/android/view/Display#hasArrSupport()) and
[`getSuggestedFrameRate(int)`](https://developer.android.com/reference/android/view/Display#getSuggestedFrameRate(int)) while restoring
[`getSupportedRefreshRates()`](https://developer.android.com/reference/android/view/Display#getSupportedRefreshRates()) to make it easier for your apps to take
advantage of ARR. [RecyclerView
1.4](https://developer.android.com/jetpack/androidx/releases/recyclerview#version_14_2) internally supports ARR when it is [settling from a fling or
smooth scroll](https://android.googlesource.com/platform/frameworks/support/+/a1e9ab3e5fd52e885731bd762ff7dd4a64b25505), and we're continuing our work to add ARR
support into more Jetpack libraries. This [frame rate article](https://developer.android.com/media/optimize/performance/frame-rate) covers
many of the APIs you can use to set the frame rate so that your app can directly
use ARR.

### Headroom APIs in ADPF

The [`SystemHealthManager`](https://developer.android.com/sdk/api_diff/b-beta2-incr/changes/android.os.health.SystemHealthManager) introduces the
[`getCpuHeadroom`](https://developer.android.com/reference/android/os/health/SystemHealthManager#getCpuHeadroom(android.os.CpuHeadroomParams)) and
[`getGpuHeadroom`](https://developer.android.com/reference/android/os/health/SystemHealthManager#getGpuHeadroom(android.os.GpuHeadroomParams)) APIs, designed to provide games and
resource-intensive apps with estimates of available CPU and GPU resources. These
methods offer a way for you to gauge how your app or game can best improve
system health, particularly when used in conjunction with other [Android Dynamic
Performance Framework](https://developer.android.com/games/optimize/adpf) (ADPF) APIs that [detect thermal
throttling](https://developer.android.com/games/optimize/adpf/thermal).

By using [`CpuHeadroomParams`](https://developer.android.com/reference/android/os/CpuHeadroomParams) and
[`GpuHeadroomParams`](https://developer.android.com/reference/android/os/GpuHeadroomParams) on supported devices, you can
customize the time window used to compute the headroom and select between
average or minimum resource availability. This can help you reduce your CPU or
GPU resource usage accordingly, leading to better user experiences and improved
battery life.

## Accessibility

Android 16 adds new accessibility APIs and features that can help you bring your
app to every user.

### Improved accessibility APIs

Android 16 adds additional APIs to enhance UI semantics that help improve
consistency for users that rely on accessibility services, such as
[TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback).

#### Outline text for maximum text contrast

Users with low vision often have reduced contrast sensitivity, making it
challenging to distinguish objects from their backgrounds. To help these users,
Android 16 introduces outline text, replacing high contrast text, which
draws a larger contrasting area around text to greatly improve legibility.

Android 16 contains new [`AccessibilityManager`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager) APIs to let
your apps [check](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#isHighContrastTextEnabled()) or [register a listener](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#addHighContrastTextStateChangeListener(java.util.concurrent.Executor,%20android.view.accessibility.AccessibilityManager.HighContrastTextStateChangeListener)) to
see if this mode is enabled. This is primarily for UI Toolkits like Compose to
offer a similar visual experience. If you maintain a UI Toolkit library or your
app performs custom text rendering that bypasses the
[`android.text.Layout`](https://developer.android.com/reference/android/text/Layout) class then you can use this to know
when outline text is enabled.
![](https://developer.android.com/static/about/versions/16/images/outline-text.png) Text with enhanced contrast before and after Android 16's new outline text accessibility feature

#### Duration added to TtsSpan

Android 16 extends `TtsSpan` with a [`TYPE_DURATION`](https://developer.android.com/reference/android/text/style/TtsSpan#TYPE_DURATION),
consisting of [`ARG_HOURS`](https://developer.android.com/reference/android/text/style/TtsSpan#ARG_HOURS), [`ARG_MINUTES`](https://developer.android.com/reference/android/text/style/TtsSpan#ARG_MINUTES),
and [`ARG_SECONDS`](https://developer.android.com/reference/android/text/style/TtsSpan#ARG_SECONDS). This lets you directly annotate time
duration, ensuring accurate and consistent text-to-speech output with services
like [TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback).

#### Support elements with multiple labels

Android currently allows UI elements to derive their accessibility label from
another, and now offers the ability for multiple labels to be associated, a
common scenario in web content. By introducing a list-based API within
[`AccessibilityNodeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo), Android can directly support these
multi-label relationships. As part of this change, we've deprecated
[`AccessibilityNodeInfo#setLabeledBy`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setLabeledBy(android.view.View)) and
[`#getLabeledBy`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getLabeledBy()) in favor of
[`#addLabeledBy`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#addLabeledBy(android.view.View)), [`#removeLabeledBy`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#removeLabeledBy(android.view.View)), and
[`#getLabeledByList`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getLabeledByList()).

#### Improved support for expandable elements

Android 16 adds accessibility APIs that allow you to convey the expanded or
collapsed state of interactive elements, such as menus and expandable lists. By
setting the expanded state using [`setExpandedState`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setExpandedState(int)) and
dispatching [TYPE_WINDOW_CONTENT_CHANGED AccessibilityEvents](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_WINDOW_CONTENT_CHANGED)
with a [`CONTENT_CHANGE_TYPE_EXPANDED`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#CONTENT_CHANGE_TYPE_EXPANDED) content change type,
you can ensure that screen readers like [TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback) announce
state changes, providing a more intuitive and inclusive user experience.

#### Indeterminate ProgressBars

Android 16 adds [`RANGE_TYPE_INDETERMINATE`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.RangeInfo#RANGE_TYPE_INDETERMINATE), giving a way for
you to expose [`RangeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo.RangeInfo) for both determinate and
indeterminate [`ProgressBar`](https://developer.android.com/reference/android/widget/ProgressBar) widgets, allowing services like
[TalkBack](https://developer.android.com/guide/topics/ui/accessibility/testing#talkback) to more consistently provide feedback for progress
indicators.

#### Tri-state CheckBox

The new [`AccessibilityNodeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)
[`getChecked`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getChecked()) and [`setChecked(int)`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setChecked(int))
methods in Android 16 now support a "partially checked" state in addition to
"checked" and "unchecked." This replaces the deprecated boolean
[`isChecked`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#isChecked()) and [`setChecked(boolean)`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setChecked(boolean)).

#### Supplemental descriptions

When an accessibility service describes a [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup), it
combines content labels from its child views. If you provide a
`contentDescription` for the `ViewGroup`, accessibility services assume you are
also overriding the description of non-focusable child views. This can be
problematic if you want to label things like a drop-down (for example, "Font
Family") while preserving the current selection for accessibility (for example,
"Roboto"). Android 16 adds [`setSupplementalDescription`](https://developer.android.com/reference/android/view/View#setSupplementalDescription(java.lang.CharSequence)) so
you can provide text that provides information about a `ViewGroup` without
overriding information from its children.

#### Required form fields

Android 16 adds [`setFieldRequired`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setFieldRequired(boolean)) to
[`AccessibilityNodeInfo`](https://developer.android.com/sdk/api_diff/b-beta1-incr/changes/android.view.accessibility.AccessibilityNodeInfo) so apps can tell an accessibility
service that input to a form field is required. This is an important scenario
for users filling out many types of forms, even things as simple as a required
terms and conditions checkbox, helping users to consistently identify and
quickly navigate between required fields.

### Phone as microphone input for voice calls with LEA hearing aids

Android 16 adds the capability for users of LE Audio hearing aids to switch
between the built-in microphones on the hearing aids and the microphone on their
phone for voice calls. This can be helpful in noisy environments or other
situations where the hearing aid's microphones might not perform well.

### Ambient volume controls for LEA hearing aids

Android 16 adds the capability for users of LE Audio hearing aids to adjust the
volume of ambient sound that is picked up by the hearing aid's microphones. This
can be helpful in situations where background noise is too loud or too quiet.

## Camera

Android 16 enhances support for professional camera users, allowing for hybrid
auto exposure along with precise color temperature and tint adjustments. A new
night mode indicator helps your app know when to switch to and from a night mode
camera session. New `Intent` actions make it easier to capture motion photos,
and we're continuing to improve UltraHDR images with support for HEIC encoding
and new parameters from the ISO 21496-1 draft standard.

### Hybrid auto-exposure

Android 16 adds new hybrid auto-exposure modes to [Camera2](https://developer.android.com/media/camera/camera2), allowing
you to manually control specific aspects of exposure while letting the
auto-exposure (AE) algorithm handle the rest. You can control
[ISO + AE](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_PRIORITY_MODE_SENSOR_SENSITIVITY_PRIORITY), and [exposure time + AE](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_PRIORITY_MODE_SENSOR_EXPOSURE_TIME_PRIORITY), providing greater
flexibility compared to the current approach where you either have full manual
control or rely entirely on auto-exposure.  

    fun setISOPriority() {
        // ... (Your existing code before the snippet) ...

        val availablePriorityModes = mStaticInfo.characteristics.get(
            CameraCharacteristics.CONTROL_AE_AVAILABLE_PRIORITY_MODES
        )

        // ... (Your existing code between the snippets) ...

        // Turn on AE mode to set priority mode
        reqBuilder.set(
            CaptureRequest.CONTROL_AE_MODE,
            CameraMetadata.CONTROL_AE_MODE_ON
        )
        reqBuilder.set(
            CaptureRequest.CONTROL_AE_PRIORITY_MODE,
            CameraMetadata.CONTROL_AE_PRIORITY_MODE_SENSOR_SENSITIVITY_PRIORITY
        )
        reqBuilder.set(
            CaptureRequest.SENSOR_SENSITIVITY,
            TEST_SENSITIVITY_VALUE
        )
        val request: CaptureRequest = reqBuilder.build()

        // ... (Your existing code after the snippet) ...
    }

### Precise color temperature and tint adjustments

Android 16 adds camera support for fine color temperature and tint adjustments
to better support professional video recording applications. In previous Android
versions, you could control white balance settings through
[`CONTROL_AWB_MODE`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AWB_MODE), which contains options limited to a
preset list, such as [Incandescent](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AWB_MODE_INCANDESCENT),
[Cloudy](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AWB_MODE_CLOUDY_DAYLIGHT), and [Twilight](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AWB_MODE_TWILIGHT). The
[`COLOR_CORRECTION_MODE_CCT`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#COLOR_CORRECTION_MODE_CCT) enables the use of
[`COLOR_CORRECTION_COLOR_TEMPERATURE`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#COLOR_CORRECTION_COLOR_TEMPERATURE) and
[`COLOR_CORRECTION_COLOR_TINT`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#COLOR_CORRECTION_COLOR_TINT) for precise adjustments of
white balance based on the correlated color temperature.  

    fun setCCT() {
        // ... (Your existing code before this point) ...

        val colorTemperatureRange: Range<Int> =
            mStaticInfo.characteristics[CameraCharacteristics.COLOR_CORRECTION_COLOR_TEMPERATURE_RANGE]

        // Set to manual mode to enable CCT mode
        reqBuilder[CaptureRequest.CONTROL_AWB_MODE] = CameraMetadata.CONTROL_AWB_MODE_OFF
        reqBuilder[CaptureRequest.COLOR_CORRECTION_MODE] = CameraMetadata.COLOR_CORRECTION_MODE_CCT
        reqBuilder[CaptureRequest.COLOR_CORRECTION_COLOR_TEMPERATURE] = 5000
        reqBuilder[CaptureRequest.COLOR_CORRECTION_COLOR_TINT] = 30

        val request: CaptureRequest = reqBuilder.build()

        // ... (Your existing code after this point) ...
    }

The following examples show how a photo would look after applying different
color temperature and tint adjustments:  
![](https://developer.android.com/static/about/versions/16/images/color-temperature-tint.jpg) The original image with no color temperature or tint adjustments applied.  
![](https://developer.android.com/static/about/versions/16/images/color-temperature-3000.jpg) The image with color temperature adjusted to 3000.  
![](https://developer.android.com/static/about/versions/16/images/color-temperature-7000.jpg) The image with color temperature adjusted to 7000.

<br />

![](https://developer.android.com/static/about/versions/16/images/color-tint-minus-50.jpg) The image with tint levels lowered by 50.  
![](https://developer.android.com/static/about/versions/16/images/color-tint-plus-50.jpg) The image with tint levels raised by 50.  

### Camera night mode scene detection

To help your app know when to switch to and from a night mode camera session,
Android 16 adds [`EXTENSION_NIGHT_MODE_INDICATOR`](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#EXTENSION_NIGHT_MODE_INDICATOR). If
supported, it's available in the [`CaptureResult`](https://developer.android.com/reference/android/hardware/camera2/CaptureResult) within
Camera2.

This is the API we briefly mentioned as coming soon in the [How Instagram
enabled users to take stunning low light photos](https://android-developers.googleblog.com/2024/12/instagram-on-android-low-light-photos.html)
blog post. That post is a practical guide on how to implement night mode
together with a case study that links higher-quality in-app night mode photos
with an increase in the number of photos shared from the in-app camera.

### Motion photo capture intent actions

Android 16 adds standard Intent actions ---
[`ACTION_MOTION_PHOTO_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_MOTION_PHOTO_CAPTURE), and
[`ACTION_MOTION_PHOTO_CAPTURE_SECURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_MOTION_PHOTO_CAPTURE_SECURE) --- which request that
the camera application capture a [motion photo](https://developer.android.com/media/platform/motion-photo-format) and return
it.

You must either pass an extra [`EXTRA_OUTPUT`](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_OUTPUT) to control
where the image will be written, or a [`Uri`](https://developer.android.com/reference/android/net/Uri) through
[`Intent.setClipData(ClipData)`](https://developer.android.com/reference/android/content/Intent#setClipData(android.content.ClipData)). If you don't set a
[`ClipData`](https://developer.android.com/reference/android/content/ClipData), it will be copied there for you when calling
[`Context.startActivity(Intent)`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)).
An example of a motion photo, showing the still image followed by the motion playback.

### UltraHDR image enhancements

![](https://developer.android.com/static/about/versions/16/images/SDR-HDR-compare.png) An illustration of Standard Dynamic Range (SDR) versus High Dynamic Range (HDR) image quality.

Android 16 continues our work to deliver dazzling image quality with UltraHDR
images. It adds support for [UltraHDR](https://developer.android.com/media/platform/hdr-image-format) images in the HEIC file
format. These images will get `ImageFormat` type
[`HEIC_ULTRAHDR`](https://developer.android.com/reference/android/graphics/ImageFormat#HEIC_ULTRAHDR) and will contain an embedded gainmap similar
to the existing UltraHDR JPEG format. We're working on AVIF support for UltraHDR
as well, so stay tuned.

In addition, Android 16 implements additional parameters in UltraHDR from the
[ISO 21496-1 draft standard](https://www.iso.org/standard/86775.html), including the ability
to get and set the colorspace that gainmap math should be applied in, as well as
support for HDR encoded base images with SDR gainmaps.


## Graphics

Android 16 includes the latest graphics improvements, such as custom graphic
effects with AGSL.

### Custom graphical effects with AGSL

Android 16 adds [`RuntimeColorFilter`](https://developer.android.com/reference/android/graphics/RuntimeColorFilter) and
[`RuntimeXfermode`](https://developer.android.com/reference/android/graphics/RuntimeXfermode), allowing you to author complex effects like
Threshold, Sepia, and Hue Saturation and apply them to draw calls. Since Android
13, you've been able to use [AGSL](https://developer.android.com/develop/ui/views/graphics/agsl) to create custom
[RuntimeShaders](https://developer.android.com/reference/android/graphics/RuntimeShader) that extend [`Shader`](https://developer.android.com/reference/android/graphics/Shader). The new API
mirrors this, adding an AGSL-powered [`RuntimeColorFilter`](https://developer.android.com/reference/android/graphics/RuntimeColorFilter) that
extends [`ColorFilter`](https://developer.android.com/reference/android/graphics/ColorFilter), and a [`Xfermode`](https://developer.android.com/reference/android/graphics/Xfermode) effect that
lets you implement AGSL-based custom compositing and blending between source and
destination pixels.  

    private val thresholdEffectString = """
        uniform half threshold;

        half4 main(half4 c) {
            half luminosity = dot(c.rgb, half3(0.2126, 0.7152, 0.0722));
            half bw = step(threshold, luminosity);
            return bw.xxx1 * c.a;
        }"""

    fun setCustomColorFilter(paint: Paint) {
       val filter = RuntimeColorFilter(thresholdEffectString)
       filter.setFloatUniform(0.5);
       paint.colorFilter = filter
    }

## Connectivity

Android 16 updates the platform to give your app access to the latest advances
in communication and wireless technologies.

### Ranging with enhanced security

Android 16 adds support for [robust security features](https://developer.android.com/reference/android/net/wifi/rtt/SecureRangingConfig) in
Wi-Fi location on supported devices with Wi-Fi 6's 802.11az, allowing apps to
combine the higher accuracy, greater scalability, and dynamic scheduling of the
protocol with security enhancements including AES-256-based encryption and
protection against MITM attacks. This allows it to be used more safely in
proximity use cases, such as unlocking a laptop or a vehicle door. 802.11az is
integrated with the Wi-Fi 6 standard, leveraging its infrastructure and
capabilities for wider adoption and easier deployment.

### Generic ranging APIs

Android 16 includes the new [`RangingManager`](https://developer.android.com/reference/android/ranging/RangingManager), which provides
ways to determine the distance and angle on supported hardware between the local
device and a remote device. `RangingManager` supports the usage of a variety of
ranging technologies such as BLE channel sounding, BLE RSSI-based ranging, Ultra
Wideband, and Wi-Fi round trip time.

### Companion device manager device presence

In Android 16, new APIs are being introduced for binding your companion app
service. Service will be bound when BLE is in range and Bluetooth is connected
and service will be unbound when BLE is out of range or Bluetooth is
disconnected. App will receives a new
['onDevicePresenceEvent()'](https://developer.android.com/reference/android/companion/CompanionDeviceService#onDevicePresenceEvent(android.companion.DevicePresenceEvent)) callback based on various
of [`DevicePresenceEvent`](https://developer.android.com/reference/android/companion/DevicePresenceEvent).
More details can be found in
['startObservingDevicePresence(ObservingDevicePresenceRequest)'](https://developer.android.com/reference/android/companion/CompanionDeviceManager#startObservingDevicePresence(android.companion.ObservingDevicePresenceRequest)).

## Media

Android 16 includes a variety of features that improve the media experience.

### Photo picker improvements

The [photo picker](https://developer.android.com/training/data-storage/shared/photopicker) provides a safe, built-in way for users
to grant your app access to selected images and videos from both local and cloud
storage, instead of their entire media library. Using a combination of [Modular
System Components](https://source.android.com/devices/architecture/modular-system)
through [Google System Updates](https://support.google.com/product-documentation/answer/11412553)
and [Google Play services](https://developers.google.com/android/guides/overview), it's supported back
to [Android 4.4 (API level 19)](https://developer.android.com/reference/android/os/Build.VERSION_CODES#KITKAT). Integration requires just a
few lines of code with the associated
[Android Jetpack library](https://developer.android.com/jetpack/androidx/releases/activity).

Android 16 includes the following improvements to the photo picker:

- **Embedded photo picker** : [New APIs](https://developer.android.com/reference/android/widget/photopicker/package-summary) that enable apps to embed the photo picker into their view hierarchy. This allows it to feel like a more integrated part of the app while still leveraging the process isolation that allows users to select media without the app needing overly broad permissions. To maximize compatibility across platform versions and simplify your integration, you'll want to use the forthcoming Android Jetpack library if you want to integrate the embedded photo picker.
- **Cloud search in photo picker** : [New APIs that enable searching](https://developer.android.com/sdk/api_diff/b-dp2-incr/changes/pkg_android.provider) from the cloud media provider for the Android photo picker. Search functionality in the photo picker is coming soon.

### Advanced Professional Video

Android 16 introduces support for the [Advanced Professional
Video](https://www.ietf.org/archive/id/draft-lim-apv-00.html) (APV) codec which is designed to be used for
professional level high quality video recording and post production.

The APV codec standard has the following features:

- Perceptually lossless video quality (close to raw video quality)
- Low complexity and high throughput intra-frame-only coding (without pixel domain prediction) to better support editing workflows
- Support for high bit-rate range up to a few Gbps for 2K, 4K and 8K resolution content, enabled by a lightweight entropy coding scheme
- Frame tiling for immersive content and for enabling parallel encoding and decoding
- Support for various chroma sampling formats and bit-depths
- Support for multiple decoding and re-encoding without severe visual quality degradation
- Support multi-view video and auxiliary video like depth, alpha, and preview
- Support for HDR10/10+ and user-defined metadata

A reference implementation of APV is provided through the
[OpenAPV project](https://github.com/openapv/openapv). Android 16 will
[implement support](https://developer.android.com/reference/android/media/MediaFormat#MIMETYPE_VIDEO_APV) for the APV 422-10 Profile that provides YUV 422
color sampling along with 10-bit encoding and for target bitrates of up to
2Gbps.

## Privacy

Android 16 includes a variety of features that help app developers protect user
privacy.

### Health Connect updates

Health Connect adds `ACTIVITY_INTENSITY`, a data type defined according to World
Health Organization guidelines around moderate and vigorous activity. Each
record requires the start time, the end time, and whether the activity intensity
is moderate or vigorous.

Health Connect also contains updated APIs supporting
[medical records](https://developer.android.com/health-and-fitness/guides/medical-records). This allows apps to read and write
medical records in [FHIR format](https://hl7.org/fhir/) with explicit
user consent.

### Privacy Sandbox on Android

Android 16 incorporates the latest version of the
[Privacy Sandbox on Android](https://developers.google.com/privacy-sandbox/overview/android), part of our
ongoing work to develop technologies where users know their privacy is
protected. Our [website has more](https://developer.android.com/design-for-safety/privacy-sandbox/program-overview) about the Privacy
Sandbox on Android developer beta program to help you get started. Check out the
[SDK Runtime](https://developers.google.com/privacy-sandbox/private-advertising/sdk-runtime)
which allows SDKs to run in a dedicated runtime environment separate from the
app they are serving, providing stronger safeguards around user data collection
and sharing.

## Security

Android 16 includes features that help you enhance your app's security and
protect your app's data.

### Key sharing API

Android 16 adds APIs that support sharing access to
[Android Keystore](https://developer.android.com/privacy-and-security/keystore) keys with other apps. The new
[`KeyStoreManager`](https://developer.android.com/reference/android/security/keystore/KeyStoreManager) class supports
[granting](https://developer.android.com/reference/android/security/keystore/KeyStoreManager#grantKeyAccess(java.lang.String,%20int)) and [revoking](https://developer.android.com/reference/android/security/keystore/KeyStoreManager#revokeKeyAccess(java.lang.String,%20int)) access to keys
by app [uid](https://developer.android.com/reference/android/os/Process#myUid()), and includes an API for apps to access shared
keys.

## Device form factors

Android 16 gives your apps the support to get the most out of Android's form
factors.

### Standardized picture and audio quality framework for TVs

The new [`MediaQuality`
package](https://developer.android.com/reference/android/media/quality/package-summary) in Android 16 exposes
a set of standardized APIs for access to audio and picture profiles and
hardware-related settings. This allows streaming apps to query profiles and
apply them to media dynamically:

- Movies mastered with a wider dynamic range require greater color accuracy to see subtle details in shadows and adjust to ambient light, so a profile that prefers color accuracy over brightness may be appropriate.
- Live sporting events are often mastered with a narrow dynamic range, but are often watched in daylight, so a profile that preferences brightness over color accuracy can give better results.
- Fully interactive content wants minimal processing to reduce latency, and wants higher frame rates, which is why many TV's ship with a game profile.

The API allows apps to switch between profiles and users to enjoy tuning
supported TVs to best suit their content.

## Internationalization

Android 16 adds features and capabilities that complement the user experience
when a device is used in different languages.

### Vertical text

Android 16 adds low-level support for rendering and measuring text vertically to
provide foundational vertical writing support for library developers. This is
particularly useful for languages like Japanese that commonly use vertical
writing systems. A new flag,
[`VERTICAL_TEXT_FLAG`](https://developer.android.com/reference/android/graphics/Paint#VERTICAL_TEXT_FLAG),
has been added to the [`Paint`](https://developer.android.com/reference/android/graphics/Paint) class. When
this flag is set using
[`Paint.setFlags`](https://developer.android.com/reference/android/graphics/Paint#setFlags(int)), Paint's
text measurement APIs will report vertical advances instead of horizontal
advances, and [`Canvas`](https://developer.android.com/reference/android/graphics/Canvas) will draw text
vertically.
**Note:** Current high-level text APIs, such as Text in Jetpack Compose, TextView, Layout classes and their subclasses don't support vertical writing systems, and don't support using the `VERTICAL_TEXT_FLAG`.  

    val text = "「春は、曙。」"
    Box(
        Modifier.padding(innerPadding).background(Color.White).fillMaxSize().drawWithContent {
            drawIntoCanvas { canvas ->
                val paint = Paint().apply { textSize = 64.sp.toPx() }
                // Draw text vertically
                paint.flags = paint.flags or VERTICAL_TEXT_FLAG
                val height = paint.measureText(text)
                canvas.nativeCanvas.drawText(
                    text,
                    0,
                    text.length,
                    size.width / 2,
                    (size.height - height) / 2,
                    paint
                )
            }
        }
    ) {}

### Measurement system customization

Users can now customize their measurement system in regional preferences within
Settings. The user preference is included as part of the locale code, so you can
register a [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) on
[`ACTION_LOCALE_CHANGED`](https://developer.android.com/reference/android/content/Intent#ACTION_LOCALE_CHANGED) to handle locale configuration changes when
regional preferences change.

Using [formatters](https://developer.android.com/guide/topics/resources/multilingual-support#formatters) can help match the local experience. For example,
"0.5 in" in English (United States), is "12,7 mm" for a user who has set their
phone to English (Denmark) or who uses their phone in English (United States)
with the metric system as the measurement system preference.

To find these settings, open the Settings app and navigate to **System \>
Languages \& region**.