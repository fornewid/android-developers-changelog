---
title: https://developer.android.com/training/wearables/get-started/emulator
url: https://developer.android.com/training/wearables/get-started/emulator
source: md.txt
---

# Test on the Wear OS emulator

The[Android Emulator](https://developer.android.com/studio/run/emulator)lets you test your Wear OS applications on virtual devices. Much of its functionality is covered in the main[Android Emulator documentation](https://developer.android.com/studio/run/emulator); this page focuses on features, testing capabilities, and troubleshooting tips specific to Wear OS development.

For basic setup instructions, see[Create and run an app on Wear OS](https://developer.android.com/training/wearables/get-started/creating).

## Wear OS testing capabilities

The emulator provides specialized tools for testing Wear OS features.

### Test Bluetooth audio

See[Test Bluetooth audio on emulators](https://developer.android.com/training/wearables/apps/test-bluetooth-audio).

### Simulate sensors

The emulator provides different ways to simulate sensor data from the toolbar, depending on the type of data.
![Android Studio toolbar icons](https://developer.android.com/static/studio/images/buttons/emulator-toolbar.png)**Figure 1.**: Android Studio's "Running Devices" toolbar.

- **Health Services data:**
  - Access the dedicated**Health Services** panel directly from the emulator toolbar (look for the heart icon!["heart icon"](https://developer.android.com/static/images/tools/e-health-services.png)). This panel allows fine-grained control for simulating data specific to[Health Services](https://developer.android.com/health-and-fitness/guides/health-services), like exercise metrics. For detailed instructions, see[Simulate sensor data with Health Services](https://developer.android.com/health-and-fitness/guides/health-services/simulated-data).
- **Other sensors (such as location, pose, heart rate):**
  - For other sensor types, open the[**Extended Controls**](https://developer.android.com/studio/run/emulator-extended-controls)window by clicking the overflow button (**...**) in the emulator toolbar.
  - **Location:** Navigate to**Extended Controls \> Location** to provide single GPS points or simulate routes. This is useful for testing apps with the[Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider)and verifying[approximate location](https://developer.android.com/training/wearables/versions/4/changes#approximate-location-permission)handling.
  - **Device Pose (Accelerometer \& Gyroscope):** Navigate to**Extended Controls \> Virtual Sensors \> Device Pose**. Adjust Rotation (X-Rot, Y-Rot, Z-Rot) and Movement (X, Y, Z) sliders to test motion-based interactions.
  - **Heart Rate \& Additional Sensors:** Navigate to**Extended Controls \> Virtual Sensors \> Additional Sensors** . Simulate**Heart rate** and other sensors like**Ambient temperature** ,**Magnetic field** ,**Proximity** ,**Light** ,**Pressure** , and**Relative Humidity**.

### Simulate watch inputs

- **Touch and Gestures:**Standard mouse interaction mimics touch.
- **Physical Buttons (including rotating side button and bezel):**

  - Buttons at the top of the[emulator panel](https://developer.android.com/studio/run/emulator#tasks)can be used to simulate hardware buttons (Button 1!["button 1 icon"](https://developer.android.com/static/studio/images/run/wear-emu-button-1.png), Button 2!["button 2 icon"](https://developer.android.com/static/studio/images/run/wear-emu-button-2.png)) as well as other physical interactions such as palming !["palm icon"](https://developer.android.com/static/studio/images/run/wear-emu-palm-button.png)tilting the device![](https://developer.android.com/static/studio/images/run/wear-emu-tilt-button.png)and swiping back![](https://developer.android.com/static/images/tools/e-iback.png)

  - For**Rotary input** , open the emulator toolbar's overflow menu (**...** ), and select**Rotary input**.

### Pair devices

The emulator supports pairing with physical or virtual phones. Use the**Wear OS emulator pairing assistant** in Android Studio's Device Manager for a guided setup. See[Connect a watch to a phone](https://developer.android.com/training/wearables/get-started/connect-phone)for details.

## Important considerations

Note the following key technical and performance considerations when testing.

### 64-bit architecture only (recent images)

Emulator system images for Wear OS 4 (API 33) and higher only support**64-bit architectures** (`x86-64`,`arm64-v8a`).

### Performance differences

Emulator performance, especially regarding battery consumption and rendering speed, may differ significantly from physical devices. Always test on real hardware for final performance validation and battery optimization.

## Known issues

This section lists common issues specific to the Wear OS emulator. For general emulator problems, see the main[Troubleshoot known issues with Android Emulator](https://developer.android.com/studio/run/emulator-troubleshooting)page.

- **Wrist Tilt Sensor Warnings:** You might see repeated log messages like`the host has not provided value yet for sensorHandle=16`. These can be ignored.
- **Tiles Renderer:** [`DashedArcLine`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders.DashedArcLine)objects, as well as elements constructed by[`circularProgressIndicator()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).circularProgressIndicator(kotlin.Float,androidx.wear.protolayout.expression.DynamicBuilders.DynamicFloat,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,androidx.wear.protolayout.material3.ProgressIndicatorColors,androidx.wear.protolayout.DimensionBuilders.ContainerDimension)), might not render correctly on the API 36 emulator.