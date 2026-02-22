---
title: https://developer.android.com/games/optimize/display-refresh-rate-change
url: https://developer.android.com/games/optimize/display-refresh-rate-change
source: md.txt
---

# Optimize refresh rates

[Android 15](https://developer.android.com/about/versions/15)sets a default 60Hz refresh rate for games to optimize power consumption. To unlock higher frame rates like 120 FPS, you must now explicitly request them using the[Frame Rate API](https://developer.android.com/media/optimize/performance/frame-rate)or the Swappy library.

However, the system may override this request based on factors like battery level or device temperature. While higher refresh rates enhance visual smoothness, they also demand more power and generate additional heat. Therefore, it's crucial to offer users the option to choose their preferred refresh rate and carefully monitor performance to ensure a balanced user experience.

## Use the[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int))API

The[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int))API allows the game devs to use a specific display refresh rate. There are two steps to doing this:

1. Verify device and Android version compatibility.
2. Request high FPS using[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int)).

### Verify Device and Android Version Compatibility:

Use methods[`Display.getSupportedModes()`](https://developer.android.com/reference/android/view/Display#getSupportedModes())to determine if the device supports 90Hz, 120Hz, or other refresh rates. If the device is limited to 60Hz, it is not possible to exceed this limit.  

### Kotlin

    val display = windowManager.defaultDisplay
    val supportedModes = display.supportedModes
    for (mode in supportedModes) {
      Log.d("DisplayInfo", "Supported mode: ${mode.physicalWidth}x${mode.physicalHeight}, ${mode.refreshRate}Hz")
    }

### Request High FPS

Invoke[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int))when your rendering loop starts, during game window initialization, or when the target FPS needs to change the display refresh rate.

Even if you request a higher rate, the system might still limit the refresh rate to 60Hz due to factors like power saving mode or thermal throttling. If your game's rendering performance doesn't reach the target FPS, requesting higher refresh rate may consume unnecessary power consumption and increase the device's temperature.

The following snippet demonstrates how to avoid an overly high refresh rate with the`setFrameRate()`API.  

### Kotlin

    val targetFps = 120f
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
      window.setFrameRate(
          targetFps,
          Window.FrameRateCompatibility.FRAME_RATE_COMPATIBILITY_FIXED_SOURCE,
          0
      )
    }

[The Framerate page](https://developer.android.com/media/optimize/performance/frame-rate)provides more detailed information for further reading.

## Use Frame pacing library

[The frame pacing library](https://developer.android.com/media/optimize/performance/frame-rate), or Swappy, is an open-source library designed to simplify[VSync](https://en.wikipedia.org/wiki/Vertical_blanking_interval)management and frame scheduling in C/C++ Android game engines. This tool streamlines the process of optimizing refresh rates, effectively acting as a higher-level abstraction layer over functionalities like[`setFrameRate()`](https://developer.android.com/reference/android/view/Surface#setFrameRate(float,%20int)). Furthermore, Swappy provides additional features that can enhance your game's overall smoothness and performance.

[The Swappy page](https://developer.android.com/media/optimize/performance/frame-rate)gives more detailed information.

## Additional Tips for Best Results

The following section lay out several top tips:

1. Dynamic Frame Rate Switching.
2. Performance Monitoring.
3. Provide FPS options based on maximum display refresh rate.

### Dynamic Frame Rate Switching

To optimize both performance and power consumption, consider implementing dynamic frame rate switching in your game. This technique lets you seamlessly transition between higher refresh rates like 120Hz for smoother gameplay during demanding scenes, and lower rates like 60Hz during less intensive moments or when battery life is a concern or targeting under 60FPS. Constantly running at 120Hz can lead to excessive[heat generation](https://developer.android.com/games/optimize/adpf/thermal)and rapid battery drain, potentially resulting in a negative user experience. By intelligently adjusting the refresh rate based on the current rendering load and device conditions, you can strike a balance between visual fidelity and[power efficiency](https://developer.android.com/games/optimize/power).

### Performance Monitoring

To ensure your game performs optimally at higher refresh rates, integrate performance monitoring tools such as a frame counter or performance overlay. These tools provide real-time feedback on your game's actual frame rate, allowing you to verify whether you're consistently achieving the target 120 FPS.

If your frame rate fluctuates significantly, consider targeting a lower achievable framerate on the given device. This can deliver a smoother experience without the performance hiccups that might occur when striving for the highest refresh rate.

### Provide FPS options based on maximum display refresh rate

Your game should detect the maximum display refresh rate supported by the current device, such as 60Hz, 90Hz, or 120Hz, and limit the FPS settings accordingly. For example, if the device only supports up to 60Hz, it is advisable to disable any options higher than 60FPS in the game settings to avoid confusing the player.