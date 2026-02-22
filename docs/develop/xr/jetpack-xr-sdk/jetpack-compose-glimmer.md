---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg)AI Glasses[](https://developer.android.com/develop/xr/devices#ai-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Jetpack Compose Glimmer is a Compose UI toolkit for building augmented Android XR experiences, optimized for display AI Glasses. Build beautiful, minimal, and comfortable UI for devices that are worn all day. Jetpack Compose Glimmer optimizes the developer experience by handling many complexities behind the scenes.

Here are the main features of Jetpack Compose Glimmer:

- **Glasses-specific theming** :[Jetpack Compose Glimmer's design language](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)features a simplified theme for optimal visibility on AI glasses with a display.
- **Wearable-specific visual behavior**: Jetpack Compose Glimmer offers its own specific focus indicators and visual feedback that are better suited for AI glasses, differing from typical Android behaviors like ripples and overscroll effects.
- **Built on Jetpack Compose, allowing for pre-compatible input**: The Jetpack Compose Glimmer library leverages lower-level Compose features to support user input methods like tap and swipe by default.
- **Pre-built components and extensibility**: Jetpack Compose Glimmer offers prebuilt composables and components like cards and lists for common use cases, while also being extensible for more custom needs.

![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/glimmer/glimmer-overview.jpg)An example of different UI layouts that you might create with Jetpack Compose Glimmer.

This guide explains the following areas:

- [What's included in Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included)
- Jetpack Compose Glimmer components, including the following:
  - [Text](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text)
  - [Icons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons)
  - [Title chips](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)
  - [Cards](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards)
  - [Lists](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists)
  - [Buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons)
- [Focus in Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/focus)

This guide assumes you're familiar with the following concepts:

- [Jetpack Compose](https://developer.android.com/compose), especially[composables](https://developer.android.com/develop/ui/compose/layouts/basics#composable-functions),[modifiers](https://developer.android.com/develop/ui/compose/modifiers), and[state](https://developer.android.com/develop/ui/compose/state)