---
title: https://developer.android.com/training/wearables/kids/develop
url: https://developer.android.com/training/wearables/kids/develop
source: md.txt
---

# Develop experiences for kids on Wear OS

Review the following guidelines to optimize your Wear OS app's experience for kids. Also, confirm that your app or game[satisfies requirements for kid-friendly experiences](https://developer.android.com/training/wearables/packaging#kids).

## Review Wear OS principles

Review the following resources for creating new Wear OS apps:

- [Get started with Wear OS](https://developer.android.com/training/wearables)
- [Principles of Wear OS development](https://developer.android.com/training/wearables/principles)
- [UI design](https://developer.android.com/design/ui/wear)
- [Create and run an app on Wear OS](https://developer.android.com/training/wearables/get-started/creating)
- [App quality requirements](https://developer.android.com/docs/quality-guidelines/wear-app-quality#requirements)

## Don't port the phone app

Don't port your mobile app onto Wear OS. Wear OS devices have much smaller batteries and components than mobile devices, which makes directly-ported mobile games very difficult to play.

Learn more about how to[design experiences for kids on Wear OS](https://developer.android.com/design/ui/wear/guides/foundations/wear-os-for-kids).

## Choose a development environment

To develop kid-friendly experiences, you can use[Compose for Wear OS](https://developer.android.com/training/wearables/compose), our recommended approach for building UIs on Wear OS, as well as[Unity for Android](https://unity.com/solutions/mobile/android-game-development).

If you're more familiar with[Unity's](https://developer.android.com/games/engines/unity/start-in-unity)workflows and capabilities, or if your game is more complex and has 3D graphics and physics, we recommend using Unity to develop your game. It also comes with a variety of performance optimization features. Some Wear OS quality requirements may require custom implementations in Unity, such as support for[rotary input](https://developer.android.com/training/wearables/compose/rotary-input).

For games with only a few simple and short animations, the[Compose Animation API](https://developer.android.com/develop/ui/compose/animation/introduction)should be sufficient and is better supported within the Android environment.

## Minimize impact on device battery

Minimize events that affect battery life over the course of one session. Kids use watches that provide important safety features for their parents or guardians, which depend on the device having enough battery life.

The following list includes some best practices for reducing battery impact. You can also learn more about how to[conserve power and battery](https://developer.android.com/training/wearables/apps/power).

- Design for offline use cases so that kids can play without incurring network-related battery costs.
- Minimize tasks that require an internet or GPS connection.
- Limit active gameplay time per day.
- Use power efficient APIs for[all day activity tracking](https://developer.android.com/health-and-fitness/guides/health-services/monitor-background)as well as tracking[exercises](https://developer.android.com/health-and-fitness/guides/health-services/active-data).
- Reduce manual creation of wakelocks and use[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started).

The following list includes elements that you shouldn't include in your experience:

- Don't use[direct sensor tracking](https://developer.android.com/training/wearables/apps/power#sensors)as this significantly reduces the battery life.
- Don't include long-running animations.
- Don't encourage the user to keep the screen on longer than necessary.

## Prepare for standalone experiences

**Important:** Kids apps must[identify themselves as standalone](https://developer.android.com/training/wearables/apps/standalone-apps)to be made available on watches in kids mode.

When developing[standalone experiences](https://developer.android.com/training/wearables/apps/standalone-apps), consider the following:

- Design for offline use cases so that kids can always play.
- Test how your app behaves on an emulator that doesn't have an active connection to a mobile device.

## Use Watch Face Format to create watch faces

A watch face that's designed for kids must be created using Watch Face Format. Be mindful of how color saturation affects battery performance.

Learn more about how you can either[design a watch face using Watch Face Studio](https://developer.samsung.com/watch-face-studio/overview.html)or[manually configure the Watch Face Format](https://developer.android.com/training/wearables/wff), and check out our[watch face validation tools](https://github.com/google/watchface).

## Hide open-on-phone actions

Starting in Wear OS 5, the[`RemoteActivityHelper`](https://developer.android.com/reference/androidx/wear/remote/interactions/RemoteActivityHelper)API includes support for detecting whether a Wear OS device is in standalone mode. If a device is in standalone mode, hide any**Open on phone**interactions that your app or game might otherwise show.

For use cases where an app needs to be able to open a public URL on the phone to display Terms of Service, legal notices, a privacy policy, or something similar, display a short-link or QR Code using the[`Dialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/dialog/package-summary)component. If you provide a QR Code, parents and guardians can scan it using a mobile device.
| **Note:** If your app tries to send a remote intent to a device that's in standalone mode, the operation fails with the`RESULT_FAILED`status.

## Check standalone mode status before sending cross-device authorization requests

If your app makes OAuth authorization requests to other devices, first check whether the device is in standalone mode. To do so, call[`getAvailabilityStatus()`](https://developer.android.com/reference/androidx/wear/phone/interactions/authentication/RemoteAuthClient#getAvailabilityStatus())from a`RemoteAuthClient`object:

- If the return value is`STATUS_UNAVAILABLE`, the device is in standalone mode, and you should wait to send any OAuth authorization requests to mobile devices.
- If the return value is`STATUS_TEMPORARILY_UNAVAILABLE`, wait for the value to change to`STATUS_AVAILABLE`before sending authorization requests.