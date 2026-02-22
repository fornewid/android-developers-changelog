---
title: https://developer.android.com/training/wearables/get-started/creating
url: https://developer.android.com/training/wearables/get-started/creating
source: md.txt
---

# Create and run your first Wear OS app

This page provides a guide for you to build your first app for Wear OS, using a template from Android Studio. The app showcases the different ways to view information at a glance on Wear OS devices, and introduces some best practices for developing apps on the platform.

This guide builds upon some prior knowledge about the Android platform and the[Android Studio IDE](https://developer.android.com/studio). If you're completely new to Android,[create an app using this codelab](https://developer.android.com/codelabs/basic-android-kotlin-compose-first-app). To learn more about Android Studio's capabilities, visit the[Meet Android Studio](https://developer.android.com/studio/intro)page.

## Create a Wear OS app

After you download and install the latest version of Android Studio, complete the**New Project**wizard:

1. Open Android Studio, and then go to**File \> New \> New Project** . The**New Project**window appears.
2. In the**Templates** pane, select**Wear OS** . Then, in the main pane, select**Empty Wear App**.
3. Name your project, and then click**Finish**. Android Studio downloads the necessary dependencies and builds your project.

You're now ready to run your first app on Wear OS.
| **Note:** By default, the**New Project** wizard creates a standalone, independent Wear OS app that doesn't need to connect to another device in order to run. If your app's experience or complexity requires you to connect to a phone, see the guide on how to[connect a watch to a phone](https://developer.android.com/training/wearables/get-started/connect-phone).

## Run an app on the emulator

A straightforward way to run your Wear OS app is on an emulator.

### Configure an emulator

To configure an emulator in Android Studio, complete the following steps:

1. In the SDK Manager, Open the**SDK Tools** tab. Confirm that you have the latest version of**Android SDK Platform-Tools**. Close the SDK Manager.
2. Go to**Tools \> Device Manager**.
3. Select**Create (+)** . The**Virtual Device Configuration**wizard appears.
4. In the**Category** pane, select**Wear OS** and choose a hardware profile, such as**Wear OS Small Round** . Click**Next**.
5. Unless you need specific customizations, keep the default settings on this screen. Android Studio selects the latest API and system image by default. Click**Finish**.

For more information about using emulators, see the guide about how to[run apps on the Android Emulator](https://developer.android.com/studio/run/emulator).

### Open the app in the emulator

1. In the main toolbar, find the[**Run Widget**](https://developer.android.com/studio/intro/new-ui#run-configs). From the device drop-down menu, select the emulator you created and click the**Run** !["Run button"](https://developer.android.com/static/studio/images/buttons/toolbar-run.png)button to launch the app.
2. After a few moments, a "Hello..." message appears in the emulator.

## Run an app on a physical watch (optional)

Running and debugging your app on a physical watch lets you better evaluate the total user experience. This is particularly important if your app relies on specific hardware, such as sensors or a GPU.

To run an app on a physical watch, prepare the device for testing, and then connect it to your development machine.

### Prepare watch for testing

To prepare your watch for testing, enable ADB debugging by completing the following steps:

1. On the watch, open the**Settings**menu.
2. Go to the bottom of the menu. If no**Developer options** item appears, complete the following sub-steps. Otherwise, continue to the next step.
   1. Tap**System \> About** or**System \> About \> Versions**.
   2. Find the**Build number**item and tap it seven times. If your watch is protected by a PIN or pattern, enter it when prompted to do so.
3. From the**Settings** menu, tap**Developer options**.
4. Enable the**ADB debugging**option.

For more information, see[Configure on-device developer options](https://developer.android.com/studio/debug/dev-options).

### Connect watch to development machine

Some watches let you connect over USB. Others require a wireless connection.

#### Set up a wired connection over USB

Connect the watch using the following steps:

1. Using a USB cable, connect the watch to your development machine.
2. On the watch, enable**Always allow from this computer** , and then tap**OK**.

#### Set up a wireless connection

If it's not possible to debug your watch over a USB port, see[Connect to your device using Wi-Fi](https://developer.android.com/studio/run/device).

### Open the app on the watch

1. In the[**Run Widget**](https://developer.android.com/studio/intro/new-ui#run-configs)(part of the main toolbar), use the device drop-down to select your physical device.
2. Click the**Run** !["Run button"](https://developer.android.com/static/studio/images/buttons/toolbar-run.png)button in the[**Run Widget**](https://developer.android.com/studio/intro/new-ui#run-configs).
3. After a few moments, a "Hello..." message appears on your device.

| **Note:** To more accurately replicate real-world performance, run your app using the 'release' build variant. The default 'debug' build variant is unlikely to provide an accurate representation of your app's true performance, especially if your app uses[Compose](https://developer.android.com/training/wearables/compose). For more information, see[Choose a build variant for measurements](https://developer.android.com/training/wearables/compose/performance#release-mode-for-measurements).

## Plan your app architecture

Now that you have a basic app running, you're ready to move beyond the template. Before you begin adding new features, it's helpful to think about the key architectural decisions that will shape your app. The following sections explore some important questions to consider.

### App model: Standalone, non-standalone, or hybrid

Consider how much your app relies on a paired phone:

- **Hybrid (recommended for most apps):**This is the most common and flexible approach. The app's core features work without a phone (like tracking a workout), but it offers enhanced functionality when a phone is connected, such as syncing data or offering easier configuration.
- **Standalone:**Your app works completely on its own, without requiring a phone for core features. This is great for apps that can function offline or use their own internet connection. The "Empty Wear App" template creates a standalone app by default.
- **Non-standalone:**Your app requires a phone for its core functionality.

For more information and guidance on this choice, see[Standalone versus non-standalone Wear OS apps](https://developer.android.com/training/wearables/apps/standalone-apps).

### Build your user interface

[Compose for Wear OS](https://developer.android.com/training/wearables/compose)is a modern declarative framework that is the recommended way to build UIs for Wear OS apps. The template you used is built with Compose, giving you a great starting point.

When building with Compose, use the libraries designed specifically for Wear OS. These provide watch-optimized components that are essential for a great user experience.

For example, instead of a standard[`LazyColumn`](https://developer.android.com/training/wearables/apps/standalone-apps), use[`TransformingLazyColumn`](https://developer.android.com/develop/ui/compose/lists), which supports scaling and morphing animations.

Similarly, for navigation, use the[`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary#SwipeDismissableNavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState,kotlin.String,kotlin.Function1))from the[Wear OS Navigation library](https://developer.android.com/training/wearables/compose/navigation)to integrate with the system's swipe-to-dismiss gesture.

### Data storage and synchronization

How you manage data is a core architectural choice. For on-device persistence, your options are the same as on mobile, with[DataStore](https://developer.android.com/topic/libraries/architecture/datastore)for key-value data or typed objects, and[Room](https://developer.android.com/training/data-storage/room)for more complex, structured data being the recommended modern choices.

- **Store data on-device first:** Design your app to be[offline-first](https://developer.android.com/topic/architecture/data-layer/offline-first), storing necessary data directly on the watch so it remains functional without a phone connection.
- **Sync data with the phone:** When you need to sync or stream data (like user settings or workout data) with a companion phone app, use the[Data Layer API](https://developer.android.com/training/wearables/data/overview). It provides a communication channel that works over Bluetooth and Wi-Fi.

### Manage long-running work

Many core Wear OS experiences, like workouts or media playback, are long-running. It's crucial to manage this work correctly to help maintain reliability and preserve battery.

- **For user-initiated, long-running tasks:** When a user starts a task that needs to continue even if they navigate away (like tracking a run), you must use a[foreground service](https://developer.android.com/develop/background-work/services/fgs). On Wear OS, pair this service with the[Ongoing Activity API](https://developer.android.com/training/wearables/notifications/ongoing-activity). This creates a persistent notification and a tappable icon on the watch face, which lets the user return to your app.
- **For deferrable background tasks:** For work that doesn't need to happen immediately (like syncing data periodically), use**WorkManager**. It is battery-aware and respects system optimizations like Doze mode, making it a good choice for non-urgent background processing.

### Think beyond the app: Surfaces and power

Finally, remember that a Wear OS experience is more than just the main application.

- **Support other surfaces:** To create a high-quality, engaging app, plan to support other wrist-optimized surfaces. Consider creating a[tile](https://developer.android.com/training/wearables/tiles)for quick actions and information, and a[complication](https://developer.android.com/training/wearables/complications)to display important data directly on the user's watch face.
- **Plan for power efficiency:** Battery life is critical on a wearable device. From the very beginning, design your app to be power-efficient. This means being thoughtful about how you fetch data, use sensors, and run background tasks. Deferring work until the watch is charging is often a good strategy. You can learn more in the guide to[conserving power](https://developer.android.com/training/wearables/apps/power).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Connect a watch to a phone](https://developer.android.com/training/wearables/get-started/connect-phone)
- [Use Jetpack Compose on Wear OS](https://developer.android.com/training/wearables/compose)
- [Release notes](https://developer.android.com/training/wearables/versions/6/release-notes)