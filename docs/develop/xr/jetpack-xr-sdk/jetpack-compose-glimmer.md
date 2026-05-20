---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Jetpack Compose Glimmer is a Compose UI toolkit for building augmented Android
XR experiences, optimized for display glasses. Build beautiful, minimal, and
comfortable UI for devices that are worn all day. Jetpack Compose Glimmer
optimizes the developer experience by handling many complexities behind the
scenes.

> [!TIP]
> **Tip:** We released an agent skill to help you work with Jetpack Compose Glimmer. Try out the skill from the [Android skills repository](https://github.com/android/skills).

Here are the main features of Jetpack Compose Glimmer:

- **Glasses-specific theming** : [Jetpack Compose Glimmer's design language](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles) features a simplified theme for optimal visibility on display glasses.
- **Wearable-specific visual behavior**: Jetpack Compose Glimmer offers its own specific focus indicators and visual feedback that are better suited for display glasses, differing from typical Android behaviors like ripples and overscroll effects.
- **Built on Jetpack Compose**: The Jetpack leverages lower-level Compose features to support user input methods like tap and swipe by default.
- **Pre-built components and extensibility**: Jetpack Compose Glimmer offers prebuilt composables and components like cards and lists for common use cases, while also being extensible for more custom needs.

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_bento.jpg) An example of different UI layouts that you might create with Jetpack Compose Glimmer.

This guide explains the following areas:

- [What's included in Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included)
- Jetpack Compose Glimmer components, including the following:
  - [Buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons)
  - [Cards](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards)
  - [Icons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons)
  - [Icon buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icon-buttons)
  - [Lists](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists)
  - [List items](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/list-items)
  - [Surfaces](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces)
  - [Text](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text)
  - [Toggle buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/toggle-buttons)
  - [Title Chips](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)
  - [Vertical stacks](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/vertical-stacks)
- Theming in Jetpack Compose Glimmer:
  - [Colors](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/colors)
  - [Shapes](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/shapes)
- Input from both audio glasses and display glasses:
  - [Focus](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/focus)
  - For receiving input: [Handle indirect pointer inputs](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/indirect-pointer)
- [Preview your Jetpack Compose Glimmer UI with composable previews](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/preview)

This guide assumes you're familiar with the following concepts:

- [Jetpack Compose](https://developer.android.com/compose), especially [composables](https://developer.android.com/develop/ui/compose/layouts/basics#composable-functions), [modifiers](https://developer.android.com/develop/ui/compose/modifiers), and [state](https://developer.android.com/develop/ui/compose/state)