---
title: https://developer.android.com/training/wearables/apps
url: https://developer.android.com/training/wearables/apps
source: md.txt
---

# Apps

An app is a focused view that handles tasks that are too complex for a complication, tile, or notification. Apps on Wear OS are similar to a mobile app's main user interface. Use surfaces such as tiles, complications, and notifications to accomplish tasks, but link these surfaces into an app to carry out more complex tasks.

Read the following principles and use cases for a better understanding of apps.

## UX principles

Design apps with the following principles in mind:

**Focus**

Focus apps on critical tasks to help people get things done within seconds to avoid ergonomic discomfort or arm fatigue

**Shallow and linear**

Avoid hierarchies deeper than two levels. Show navigation inline

**Scroll**

Views can scroll. This is a natural gesture for users to see more content on the watch

## When to use an app

Use apps in the following situations:

**For additional info**

Focus apps on critical tasks to help people get things done within seconds to avoid ergonomic discomfort or arm fatigue.
![A map on Wear](https://developer.android.com/static/wear/images/apps/Map.png)**Figure 1.**: A map on Wear.

<br />

**For richer interactions**

To provide richer interaction than a complication or Tile.
![A timer on Wear](https://developer.android.com/static/wear/images/apps/Timer.png)**Figure 2.**: A timer on Wear.

<br />

**For long activities**

To support long-running activities like[workouts](https://developer.android.com/training/wearables/principles#fitness-apps)and[playing media](https://developer.android.com/training/wearables/principles#media-apps).
![A media app on Wear](https://developer.android.com/static/wear/images/apps/MediaPlayer.png)**Figure 3.**: A media app on Wear.

<br />

## Build an app

[Jetpack Compose](https://developer.android.com/training/wearables/compose)is a modern declarative UI toolkit and is the recommended approach for building apps on Wear OS.

In most cases result, UIs that use Jetpack Compose result in less code and accelerate the development process of Android apps as a whole. See[Why Compose](https://developer.android.com/jetpack/compose/why-adopt)for more information on the general advantages of a declarative UI framework.

[Compose for Wear OS](https://developer.android.com/jetpack/androidx/releases/wear-compose)follows[Material 3 Expressive design](https://developer.android.com/design/ui/wear/guides/get-started), includes built-in accessibility, and implements material theming, which lets you customize the design for your brand. Compose for Wear OS is designed to help you create user experiences that conform to Wear OS design guidelines.

## Guides for creating apps with Compose for Wear OS

To build the best experience possible using Compose for Wear OS, review the following guides:

- **[Use Jetpack Compose on Wear OS](https://developer.android.com/training/wearables/apps/lists):**Learn how to build with Compose for Wear OS.
- **[Create lists](https://developer.android.com/training/wearables/compose/lists):**Learn how to create lists that are optimized for wearable devices.
- **[Navigating with Compose for Wear OS](https://developer.android.com/training/wearables/compose/navigation):**Learn more about building navigation in Compose.
- **[Handle rotary input on Wear OS](https://developer.android.com/training/wearables/compose/rotary-input):**Learn more about how to handle rotary input on Wear OS.
- **[Support different devices screen sizes](https://developer.android.com/training/wearables/compose/screen-size):**Learn more about how to make sure your app should work well on Wear OS devices of all sizes.
- **[Compose performance on Wear OS](https://developer.android.com/training/wearables/compose/performance):**Learn more about performance and testing your app performance.