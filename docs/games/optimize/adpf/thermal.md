---
title: https://developer.android.com/games/optimize/adpf/thermal
url: https://developer.android.com/games/optimize/adpf/thermal
source: md.txt
---

**Released**:

Android 11 (API Level 30) - [Thermal API](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int))

Android 12 (API Level 31) - [NDK API](https://developer.android.com/ndk/reference/group/thermal#athermal_getthermalheadroom)

(Preview) Android 15 (DP1) - [`getThermalHeadroomThresholds()`](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroomThresholds())

The potential performance of your app is limited by the thermal state of the
device, which can vary based on characteristics such as weather, recent usage,
and the device's thermal design. Devices can only maintain a high level of
performance for a limited amount of time before being thermally throttled. A key
goal of your implementation should be to achieve performance goals without
exceeding thermal limitations. Thermal API makes it possible without the need
for device specific optimizations. Furthermore, when debugging performance
issues, knowing if the thermal state of your device is limiting performance is
important.

Game engines usually have runtime performance parameters that can adjust the
workload the engine puts on the device. For example, these parameters can set
the number of worker threads, worker-thread affinity for big and small cores,
GPU fidelity options, and framebuffer resolutions. In Unity Engine, game
developers can adjust the workload by changing the [Quality
Settings](https://docs.unity3d.com/Manual/class-QualitySettings.html) using the [Adaptive Performance plugin](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.0/manual/index.html).
For Unreal Engine, use the [Scalability Settings](https://docs.unrealengine.com/5.3/en-US/scalability-reference-for-unreal-engine/) to adjust
quality levels dynamically.

When a device approaches an unsafe thermal state, your game can avoid being
throttled by decreasing the workload through these parameters. To avoid
throttling, you should monitor the thermal state of the device and proactively
adjust the game engine workload.

Once the device overheats, the workload must
drop below the sustainable performance level in order to dissipate heat. After
the thermal headroom decreases to safer levels, the game can increase the
quality settings again but make sure to find a sustainable quality level for
optimal play time.

You can monitor the thermal state of the device by polling the
[`getThermalHeadroom`](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int)) method. This method predicts how long the device can
maintain the current performance level without overheating. If the time is less
than the amount needed to run the workload, then your game should decrease the
workload to a sustainable level. For example, the game can shift to smaller
cores, reduce the frame rate, or lower fidelity.
| **Note:** If your game collects performance telemetry from players, the device's thermal state is a good metric to include because it gives more context to any related issues.
![ADPF Thermal API Pre-Integration](https://developer.android.com/static/games/optimize/adpf/images/adpf_thermal_pre-integration.png) **Figure 1.** Thermal Headroom without actively monitoring getThermalHeadroom ![ADPF Thermal API Post-Integration](https://developer.android.com/static/games/optimize/adpf/images/adpf_thermal_post-integration.png) **Figure 2.**Thermal Headroom with active monitoring of \`getThermalHeadroom\`

## Acquire Thermal Manager

In order to use Thermal API, first you'll need to acquire the Thermal Manager

### C++

    AThermalManager* thermal_manager = AThermal_acquireManager();

### Java

    PowerManager powerManager = (PowerManager)this.getSystemService(Context.POWER_SERVICE);

## Query the thermal headroom

You can ask the system for the current thermal headroom. This provides an
indication of how close your workload is to thermal throttling. The API
also lets you forecast the temperature x seconds ahead with the
current workload. This can give your application more time to respond, but will
be less accurate than using the current thermal status.

The result ranges from 0.0f (no throttling,
[`THERMAL_STATUS_NONE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_NONE))

to 1.0f (heavy throttling,
[`THERMAL_STATUS_SEVERE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_SEVERE)).
If you have different graphics quality levels in your games, you can follow our
[Thermal Headroom Guidelines](https://developer.android.com/games/optimize/adpf/thermal#thermal-headroom).

### C++

    float thermal_headroom = AThermal_getThermalHeadroom(0);
    ALOGI("ThermalHeadroom: %f", thermal_headroom);

### Java

    float thermalHeadroom = powerManager.getThermalHeadroom(0);
    Log.d("ADPF", "ThermalHeadroom: " + thermalHeadroom);

| **Note:** If [`getThermalHeadroom`](https://developer.android.com/ndk/reference/group/thermal#athermal_getthermalheadroom) returns NaN, make sure that you are not calling it more than once every 10 seconds. If it is still returning NaN, the device model may not have the thermal hardware and Thermal API is not supported.

## Alternatively, rely on thermal status for clarification

Each device model may be designed differently. Some devices may be able to
distribute heat better and thus be able to withstand higher thermal headroom
before being throttled. If you want to read a simplified grouping of ranges of
thermal headroom, you can check on the thermal status to make sense of the
thermal headroom value on the current device.

### C++

    AThermalStatus thermal_status = AThermal_getCurrentThermalStatus(thermal_manager);
    ALOGI("ThermalStatus is: %d", thermal_status);

### Java

    int thermalStatus = powerManager.getCurrentThermalStatus();
    Log.d("ADPF", "ThermalStatus is: " + thermalStatus);

| **Note:** The same `thermalHeadroom` value may be mapped to a certain `thermalStatus` on one device model but a different `thermalStatus` on another device. This is expected due to differences in device design, thermal characteristics, and performance profile.
| **Note:** Some devices might not fully support this technology yet and return `THERMAL_STATUS_NONE` regardless of the actual value of the thermal headroom and throttling state. For this reason we recommend using `getThermalHeadroom` instead. Check out [Device limitations of the Thermal API](https://developer.android.com/games/optimize/adpf/thermal#device-limitations) for a solution to this situation.

## Get notified when thermal status changes

You can also avoid polling the `thermalHeadroom` until the `thermalStatus` hits
a certain level (for example:
[`THERMAL_STATUS_LIGHT`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_LIGHT)).
To do so, you can register a callback to let the system notify you whenever the
status has changed.
| **Note:** Check out the [Device limitations of the Thermal API](https://developer.android.com/games/optimize/adpf/thermal#device-limitations) and don't rely only on `GetCurrentThermalStatus()` without validating with `GetThermalHeadroom()`

### C++

    int result = AThermal_registerThermalStatusListener(thermal_manager, callback);
    if ( result != 0 ) {
      // failed, check whether you have previously registered callback that
      // hasn't been unregistered
    }

### Java

    // PowerManager.OnThermalStatusChangedListener is an interface, thus you can
    // also define a class that implements the methods
    PowerManager.OnThermalStatusChangedListener listener = new
      PowerManager.OnThermalStatusChangedListener() {
        @Override
        public void onThermalStatusChanged(int status) {
            Log.d("ADPF", "ThermalStatus changed: " + status);
            // check the status and flip the flag to start/stop pooling when
            // applicable
        }
    };
    powerManager.addThermalStatusListener(listener);

Remember to remove the listener when done

### C++

    int result = AThermal_unregisterThermalStatusListener(thermal_manager, callback);
    if ( result != 0 ) {
      // failed, check whether the callback has been registered previously
    }

### Java

    powerManager.removeThermalStatusListener(listener);

## Cleanup

Once you're done, you'll need to clean up the thermal_manager that you acquired.
If you're using Java, the PowerManager reference can be automatically garbage
collected for you. But if you're using the Java API through JNI and have
retained a reference, remember to clean up the reference!

### C++

    AThermal_releaseManager(thermal_manager);

For a complete guide on how to implement Thermal API on a native C++ game using
both the C++ API (NDK API) and Java API (through JNI), check out the **Integrate
Thermal API** section in the [Adaptability
codelab](https://developer.android.com/codelabs/adaptability-codelab) section.

## Thermal headroom guidelines

You can monitor the thermal state of the device by polling the
[`getThermalHeadroom`](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int))
method. This method predicts how long the device can maintain the current
performance level before reaching
[`THERMAL_STATUS_SEVERE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_SEVERE).
For example, if `getThermalHeadroom(30)` returns 0.8, it indicates that in 30
seconds, the headroom is expected to reach 0.8, where there is 0.2 distance away
from severe throttling, or 1.0. If the time is less than the amount needed to
run the workload, then your game should decrease the workload to a sustainable
level. For example, the game can reduce the frame rate, lower fidelity, or
reduce network connectivity work.

## Thermal statuses and meaning

- If the device is not being thermally throttled:
  - [`THERMAL_STATUS_NONE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_NONE)
- Some throttling, but no significant impact on performance:
  - [`THERMAL_STATUS_LIGHT`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_LIGHT)
  - [`THERMAL_STATUS_MODERATE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_MODERATE)
- Significant throttling that impacts performance:
  - [`THERMAL_STATUS_SEVERE`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_SEVERE)
  - [`THERMAL_STATUS_CRITICAL`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_CRITICAL)
  - [`THERMAL_STATUS_EMERGENCY`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_EMERGENCY)
  - [`THERMAL_STATUS_SHUTDOWN`](https://developer.android.com/reference/android/os/PowerManager#THERMAL_STATUS_SHUTDOWN)

## Device limitations of the Thermal API

There are some known limitations or additional requirements of Thermal API, due
to implementations of the thermal API on older devices. The limitations and how
to work around them are as follows:

- Don't call the `GetThermalHeadroom()` API too frequently. If you do so, the API returns `NaN`. You shouldn't call it more than once every 10 seconds.
- Avoid calling from multiple threads, it is harder to ensure the calling frequency and may cause the API returning `NaN`.
- If the initial value of `GetThermalHeadroom()` is NaN, the API is not available on the device
- If `GetThermalHeadroom()` returns a high value (e.g: 0.85 or more) and `GetCurrentThermalStatus()` still returns `THERMAL_STATUS_NONE`, the status is likely not updated. Use heuristics to estimate the correct thermal throttling status or just use `getThermalHeadroom()` without `getCurrentThermalStatus()`.

Heuristics example:

1. Check that Thermal API is supported. `isAPISupported()` checks the value of the first call to `getThermalHeadroom` to ensure that it is not 0 or NaN and skips using the API if the first value is either 0 or NaN.
2. If `getCurrentThermalStatus()` returns a value other than `THERMAL_STATUS_NONE`, the device is being thermally throttled.
3. If `getCurrentThermalStatus()` keeps returning `THERMAL_STATUS_NONE`, it doesn't necessarily mean the device isn't being thermally throttled. It could mean that `getCurrentThermalStatus()` is not supported on the device. Check the return value of `getThermalHeadroom()` to ensure the condition of the device.
4. If `getThermalHeadroom()` returns a value of \> 1.0, the status could actually be `THERMAL_STATUS_SEVERE` or higher, reduce workload immediately and maintain lower workload until `getThermalHeadroom()` returns lower value
5. If `getThermalHeadroom()` returns a value of 0.95, the status could actually be `THERMAL_STATUS_MODERATE` or higher, reduce workload immediately and keep the watchout to prevent higher reading
6. If `getThermalHeadroom()` returns a value of 0.85, the status could actually be `THERMAL_STATUS_LIGHT`, keep the watchout and reduce workload if possible

Pseudocode:

      bool isAPISupported() {
        float first_value_of_thermal_headroom = getThermalHeadroom();
        if ( first_value_of_thermal_headroom == 0 ||
          first_value_of_thermal_headroom == NaN ) {
            // Checked the thermal Headroom API's initial return value
            // it is NaN or 0，so, return false (not supported)
            return false;
        }
        return true;
      }

      if (!isAPISupported()) {
        // Checked the thermal Headroom API's initial return value, it is NaN or 0
        // Don't use the API
      } else {
          // Use thermalStatus API to check if it returns valid values.
          if (getCurrentThermalStatus() > THERMAL_STATUS_NONE) {
              // The device IS being thermally throttled
          } else {
          // The device is not being thermally throttled currently. However, it
          // could also be an indicator that the ThermalStatus API may not be
          // supported in the device.
          // Currently this API uses predefined threshold values for thermal status
          // mapping. In the future  you may be able to query this directly.
          float thermal_headroom = getThermalHeadroom();
          if ( thermal_headroom > 1.0) {
                // The device COULD be severely throttled.
          } else  if ( thermal_headroom > 0.95) {
                // The device COULD be moderately throttled.
          } else if ( thermal_headroom > 0.85) {
                // The device COULD be experiencing light throttling.
          }
        }
      }

Diagram:
![ADPF Heuristic
Example](https://developer.android.com/static/games/optimize/adpf/images/adpf_heuristic.svg) **Figure 3.**Example of Heuristic to determine Thermal API support on older devices