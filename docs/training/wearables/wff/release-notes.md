---
title: Release notes for Watch Face Format  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/wff/release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Release notes for Watch Face Format Stay organized with collections Save and categorize content based on your preferences.



All versions of the Watch Face Format offer the following capabilities:

* **Style editing:** Customize the watch face, including its color, background
  image, and font.
* **Groups and complications:** Group components so that you can control or
  move those components with a single action. You can also handle an entire
  [complication](/training/wearables/design/complications) as one group.
* **Tag expressions:** Add tags with date, time, battery, step count
  information, and more.

## Version 4

Version 4 of the Watch Face Format adds several capabilities, including the
following:

* Support for [user-selected photos](/training/wearables/wff/personalization/photos).
* [Transitions](/training/wearables/wff/transform) when entering and exiting ambient mode.
* Support for [color transformations](/reference/wear-os/wff/common/transform/transform#transformable) on most elements and [color tinting](/reference/wear-os/wff/user-configuration/color-configuration) on grouped elements.
* A new [`Reference`](/reference/wear-os/wff/common/reference/reference) element that lets you single-source your transform configurations.

To view features from version 4 in the [XML reference](/reference/wear-os/wff/watch-face), check that the
**Version 4** button is selected at the top of the documentation page.

## Version 3

Version 3 of the Watch Face Format adds several capabilities, including the
following:

* [Auto-sizing text](/reference/wear-os/wff/group/part/text/text).
* More capabilities for combining graphical objects, including
  [blend mode](/reference/wear-os/wff/common/attributes/blend-mode).
* Support for weighted constraints on [line elements](/reference/wear-os/wff/group/part/draw/shape/line).
* Several additional [data sources](/reference/wear-os/wff/common/attributes/source-type), primarily related to time zones.

To view features from version 3 in the [XML reference](/reference/wear-os/wff/watch-face), check that the
**Version 3** button is selected at the top of the documentation page.

## Version 2

Version 2 of the Watch Face Format adds several capabilities related to data
visualization, weather forecasts, and system data source types.

Highlights include the following:

* [Flavors](/reference/wear-os/wff/user-configuration/flavor): Preset configurations for your watch face that users can
  browse in a companion app.
* **Goal progress complication type:** Useful when users can exceed a goal
  such as step count.
* **Weighted elements complication type:** Useful for showing discrete subsets
  of data.
* **Weather conditions:** Show the current weather, as well as forecast
  conditions for hours or days into the future.
* A new **heart rate** system data source for complications.

To view features from version 2 in the [XML reference](/reference/wear-os/wff/watch-face), check that the
**Version 2** button is selected at the top of the documentation page.