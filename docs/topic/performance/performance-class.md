---
title: https://developer.android.com/topic/performance/performance-class
url: https://developer.android.com/topic/performance/performance-class
source: md.txt
---

# Performance class

*Performance class*is a standard first introduced in Android 12. A performance class defines a set of device capabilities that goes beyond Android's baseline requirements.

Each version of Android has its own corresponding performance class, which is defined in that version's[Android Compatibility Definition Document (CDD)](https://source.android.com/compatibility/cdd). The[Android Compatibility Test Suite (CTS)](https://source.android.com/compatibility/cts)verifies the CDD requirements.

Each Android-powered device declares the performance class that it supports. Developers can find the device's performance class at runtime and provide upgraded experiences that take full advantage of the device's capabilities.

To find a device's performance class level, use the Jetpack[Core Performance](https://developer.android.com/jetpack/androidx/releases/core#core_performance_version_10_2)library. This library reports the device's media performance class (MPC) level as declared in the[build version information](https://developer.android.com/reference/android/os/Build.VERSION#MEDIA_PERFORMANCE_CLASS)or based on data from Google Play services.

Start by adding a dependency for the relevant modules in your gradle file:  

### Kotlin

```kotlin
// Implementation of Jetpack Core library.
implementation("androidx.core:core-ktx:1.12.0")
// Enable APIs to query for device-reported performance class.
implementation("androidx.core:core-performance:1.0.0")
// Enable APIs to query Google Play services for performance class.
implementation("androidx.core:core-performance-play-services:1.0.0")
```

### Groovy

```groovy
// Implementation of Jetpack Core library.
implementation 'androidx.core:core-ktx:1.12.0'
// Enable APIs to query for device-reported performance class.
implementation 'androidx.core:core-performance:1.0.0'
// Enable APIs to query Google Play services for performance class.
implementation 'androidx.core:core-performance-play-services:1.0.0'
```

Then, create an instance of a[`DevicePerformance`](https://developer.android.com/reference/androidx/core/performance/DevicePerformance)implementation, such as[`PlayServicesDevicePerformance`](https://developer.android.com/reference/androidx/core/performance/play/services/PlayServicesDevicePerformance), in the`onCreate()`lifecycle event of your`Application`. This should only be done once in your app.  

### Kotlin

```kotlin
import androidx.core.performance.play.services.PlayServicesDevicePerformance

class MyApplication : Application() {
  lateinit var devicePerformance: DevicePerformance

  override fun onCreate() {
    // Use a class derived from the DevicePerformance interface
    devicePerformance = PlayServicesDevicePerformance(applicationContext)
  }
}
```

### Java

```java
import androidx.core.performance.play.services.PlayServicesDevicePerformance;

class MyApplication extends Application {
  DevicePerformance devicePerformance;

  @Override
  public void onCreate() {
    // Use a class derived from the DevicePerformance interface
    devicePerformance = new PlayServicesDevicePerformance(applicationContext);
  }
}
```

You can then retrieve the`mediaPerformanceClass`property to tailor your app's experience based on the device's capabilities:  

### Kotlin

```kotlin
class MyActivity : Activity() {
  private lateinit var devicePerformance: DevicePerformance
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Note: Good app architecture is to use a dependency framework. See
    // https://developer.android.com/training/dependency-injection for more
    // information.
    devicePerformance = (application as MyApplication).devicePerformance
  }

  override fun onResume() {
    super.onResume()
    when {
      devicePerformance.mediaPerformanceClass >= Build.VERSION_CODES.VANILLA_ICE_CREAM -> {
        // MPC level 35 and later.
        // Provide the most premium experience for the highest performing devices.
      }
      devicePerformance.mediaPerformanceClass == Build.VERSION_CODES.UPSIDE_DOWN_CAKE -> {
        // MPC level 34.
        // Provide a high quality experience.
      }
      else -> {
        // MPC level 33, 31, 30, or undefined.
        // Remove extras to keep experience functional.
      }
    }
  }
}
```

### Java

```java
class MyActivity extends Activity {
  private DevicePerformance devicePerformance;
  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // Note: Good app architecture is to use a dependency framework. See
    // https://developer.android.com/training/dependency-injection for more
    // information.
    devicePerformance = ((MyApplication) getApplication()).devicePerformance;
  }

  @Override
  public void onResume() {
    super.onResume();
    if (devicePerformance.getMediaPerformanceClass() >= Build.VERSION_CODES.VANILLA_ICE_CREAM) {
      // MPC level 35 and later.
      // Provide the most premium experience for the highest performing devices.
    } else if (devicePerformance.getMediaPerformanceClass() == Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
      // MPC level 34.
      // Provide a high quality experience.
    } else {
      // MPC level 33, 31, 30, or undefined.
      // Remove extras to keep experience functional.
    }
  }
}
```

Performance class levels are forward-compatible. A device can upgrade to a newer platform version without updating its performance class. For example, a device that initially supports performance class 33 can upgrade to Android 14 and continue to report it supports performance class 33 if it doesn't meet the performance class 34 requirements. This allows grouping devices together without relying on a particular Android version.

![](https://developer.android.com/static/images/topic/performance/perf-class.svg)
**Figure 1.**Devices can upgrade Android versions and continue reporting that they support the class they originally support.

<br />

## Media Performance Class 35

MPC 35 was introduced in Android 15 and builds on the requirements introduced in[MPC 34](https://developer.android.com/topic/performance/performance-class#class-34). The specific MPC 35 requirements are published in the[Android 15 CDD](https://source.android.com/docs/compatibility/15/android-15-cdd#227_handheld_media_performance_class). In addition to increased requirements for items from MPC 34, the CDD specifies requirements in the following areas:

### Media

- Decoding frame drops
- HDR editing
- Dynamic color aspects
- Portrait aspect ratio

### Camera

- JPEG_R
- Preview stabilization

### Graphics

- EGL extensions
- Vulkan structures

## Media Performance Class 34

MPC 34 was introduced in Android 14 and builds on the requirements introduced in[MPC 33](https://developer.android.com/topic/performance/performance-class#class-33). The specific MPC 34 requirements are published in the[Android 14 CDD](https://source.android.com/docs/compatibility/14/android-14-cdd#227_handheld_media_performance_class). In addition to increased requirements for items from MPC 33, the CDD specifies requirements in the following areas:

### Media

- Film grain effect support in AV1 hardware decoders
- AVIF Baseline Profile
- AV1 encoder performance
- HDR video codecs
- RGBA_1010102 color format
- YUV texture sampling
- Video encoding quality
- Multichannel audio mixing

### Camera

- Night mode extension
- HDR-capable primary camera
- Face detection scene mode

### General

- Hardware overlays
- HDR display

## Media Performance Class 33

MPC 33 was introduced in Android 13 and builds on the requirements introduced in[MPC 31](https://developer.android.com/topic/performance/performance-class#class-31). The specific MPC 33 requirements are published in the[Android 13 CDD](https://source.android.com/docs/compatibility/13/android-13-cdd#227_handheld_media_performance_class). In addition to increased requirements for items from MPC 31, the CDD specifies requirements in the following areas:

### Media

- AV1 hardware decoder
- Secure hardware decoders
- Decoder initialization latency
- Round-trip audio latency
- Wired headsets and USB audio devices
- MIDI devices
- Hardware-backed trusted execution environment

### Camera

- Preview stabilization
- Slow-mo recording
- Minimum zoom ratio for ultrawide cameras
- Concurrent camera
- Logical multi-camera
- Stream use case

| **Note:** There is no MPC level 32 definition.

## Media Performance Class 31

MPC 31 was introduced in Android 12. The specific MPC 31 requirements are published in the[Android 12 CDD](https://source.android.com/docs/compatibility/12/android-12-cdd#227_handheld_media_performance_class). The CDD specifies requirements in the following areas:

### Media

- Concurrent video codec sessions
- Encoder initialization latency
- Decoder frame drops
- Encoding quality

### Camera

- Resolution and frame rate
- Startup and capture latencies
- [`FULL`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_FULL)or better hardware level
- Timestamp source is realtime
- RAW capability

### General

- Memory
- Read and write performance
- Screen resolution
- Screen density

## Media Performance Class 30

MPC 30 includes a subset of the requirements for MPC 31, letting developers provide a tailored experience on earlier but still highly capable devices. The specific performance class requirements are published in the[Android 11 CDD](https://source.android.com/docs/compatibility/11/android-11-cdd#227_handheld_media_performance_class).
| **Note:** There are no MPC level definitions prior to MPC 30. An MPC level of 0 indicates that the MPC level is undefined for the current device and build.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)