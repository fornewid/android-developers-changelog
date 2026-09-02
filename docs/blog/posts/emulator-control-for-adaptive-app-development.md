---
title: https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development
url: https://developer.android.com/blog/posts/emulator-control-for-adaptive-app-development
source: md.txt
---

[Documentation](https://developer.android.com/blog/categories/documentation)

# Emulator control for adaptive app development

2 min read ![](https://developer.android.com/static/blog/assets/ABL_123_Streamline_adaptive_testing_with_emulator_commands_Strapi_0d1336f9a2_do9zK.webp) 31 Aug 2026 [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)](https://developer.android.com/blog/authors/rob-orgiu) [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) Developer Relations Engineer Adaptive app development is fundamental on Android, but making sure everything looks good and every feature works the way it should require multiple tests on multiple devices. Or does it?

Well, yes... and no! While Android Studio is bundled with the Resizable Emulator to let you test layouts manually, there's a faster, more streamlined way to control form factors directly from your terminal. By leveraging *fire-and-forget* console commands using the adb emu shortcut, you can execute commands that immediately return control to your invoking shell.

If you have multiple emulators running at the same time, you can target a specific virtual device by passing in the shortcut's serial:

```
adb -s <serial> emu <command> <parameter>
```

## First things first: Fold and unfold

To test foldable-specific user journeys and layout configurations, you can fold and unfold your emulated device programmatically.

```
adb emu fold
```

If your foldable emulator is unfolded, you can fold it to display its smaller screen configuration, powering on the (virtual) external display. To unfold the emulator and power on the internal display, simply run:

```
adb emu unfold
```

Now, you can instantly verify that your app preserves its state and that layouts appear exactly as they should on different display sizes.

## Rotation, rotation, rotation

Correctly handling orientation changes is a cornerstone of adaptive app development. You can trigger device rotations programmatically to test how well your app handles configuration changes, including state restoration. The following command rotates the device 90\&deg; clockwise:

```
adb emu rotate
```

## Simulating postures using sensors

What about placing the emulator into a specific physical posture, like tabletop mode? The easiest approach is querying for the number of available positions with .

First, list all available sensors and their current status:

```
adb emu posture
```

This returns a list of positions similar to the following:

```
Usage: "posture <posture_id>" 1: closed	2: half-opened	3: opened	…
```

You can then invoke the tabletop posture by using the half-opened ID:

```
adb emu posture 2
```

|---|
| ***Note: Not all postures are supported by every virtual device. Standard AVD templates like the Pixel Fold or the Resizable AVD only support postures 1 , 2 , and 3 . Attempting to set 4 or 5 on these templates will return a KO: Failed to set posture error.*** |

## What about the resizable emulator?

The resizable emulator has the super power to change its size with ease. With the adb emu command, you can move it freely with one command. Before you can do any changes, querying for the available resize presets requires only one call:

```
adb emu resize-display
```

This will return the list of available presents:

```
KO usage: "resize-display <index>" 0: phone	1: unfolded	2: tablet
```

Now, invoking the resize-display parameter with the wanted ID will resize the emulator to the wanted size:

```
adb emu resize-display 1
```

## Streamline your testing today

And that's it! By integrating fire-and-forget commands into your command-line workflow, you save a lot of time and resources compared to running multiple emulators simultaneously.

Now is the time to start experimenting. If you haven't used these console shortcuts before, open up your terminal, fire up your emulator, [head over to the documentation](https://developer.android.com/studio/run/emulator-console), and get started today!
- [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
- [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
Written by:

-

  ## [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/rob-orgiu) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)
Continue reading
- [![View Wei Wang's profile](https://developer.android.com/static/blog/assets/weiwa_web_6a7b6f6114_Z1kCd5W.webp)](https://developer.android.com/blog/authors/wei-wang) 20 Jul 2026 20 Jul 2026 ![](https://developer.android.com/static/blog/assets/Upcoming_Changes_to_the_Nearby_Connections_API_Strapi_11b1de50e2_K0lSy.webp) [Documentation](https://developer.android.com/blog/categories/documentation)

  ## [Upcoming Changes to the Nearby Connections API](https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api)

  [arrow_forward](https://developer.android.com/blog/posts/upcoming-changes-to-the-nearby-connections-api) User privacy and transparency are core to the Android experience. To better align with these principles, we are updating the default behavior of the Nearby Connections API regarding how it interacts with device radios.
  [Wei Wang](https://developer.android.com/blog/authors/wei-wang) • 1 min read
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)