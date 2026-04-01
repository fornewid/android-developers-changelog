---
title: Build UI for AI glasses with Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Build UI for AI glasses with Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

Jetpack Compose Glimmer is a Compose UI toolkit for building augmented Android
XR experiences, optimized for display AI Glasses. Build beautiful, minimal, and
comfortable UI for devices that are worn all day. Jetpack Compose Glimmer
optimizes the developer experience by handling many complexities behind the
scenes.

Here are the main features of Jetpack Compose Glimmer:

* **Glasses-specific theming**: [Jetpack Compose Glimmer's design language](/design/ui/ai-glasses/guides/foundations/design-principles)
  features a simplified theme for optimal visibility on AI glasses with a
  display.
* **Wearable-specific visual behavior**: Jetpack Compose Glimmer offers its
  own specific focus indicators and visual feedback that are better suited for
  AI glasses, differing from typical Android behaviors like ripples and
  overscroll effects.
* **Built on Jetpack Compose, allowing for pre-compatible input**: The Jetpack
  Compose Glimmer library leverages lower-level Compose features to support
  user input methods like tap and swipe by default.
* **Pre-built components and extensibility**: Jetpack Compose Glimmer offers
  prebuilt composables and components like cards and lists for common use
  cases, while also being extensible for more custom needs.

![](/static/images/develop/xr/jetpack-xr-sdk/glimmer/glimmer-overview.jpg)


An example of different UI layouts that you might create with
Jetpack Compose Glimmer.

This guide explains the following areas:

* [What's included in Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included)
* Jetpack Compose Glimmer components, including the following:
  + [Text](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text)
  + [Icons](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons)
  + [Title chips](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)
  + [Cards](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards)
  + [Lists](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists)
  + [Buttons](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons)
* [Focus in Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/focus)

This guide assumes you're familiar with the following concepts:

* [Jetpack Compose](/compose), especially [composables](/develop/ui/compose/layouts/basics#composable-functions), [modifiers](/develop/ui/compose/modifiers), and
  [state](/develop/ui/compose/state)