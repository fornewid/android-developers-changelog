---
title: https://developer.android.com/training/wearables/wff/release-notes
url: https://developer.android.com/training/wearables/wff/release-notes
source: md.txt
---

All versions of the Watch Face Format offer the following capabilities:

- **Style editing:** Customize the watch face, including its color, background
  image, and font.

- **Groups and complications:** Group components so that you can control or
  move those components with a single action. You can also handle an entire
  [complication](https://developer.android.com/training/wearables/design/complications) as one group.

- **Tag expressions:** Add tags with date, time, battery, step count
  information, and more.

## Version 4

Version 4 of the Watch Face Format adds several capabilities, including the
following:

- Support for [user-selected photos](https://developer.android.com/training/wearables/wff/personalization/photos).
- [Transitions](https://developer.android.com/training/wearables/wff/transform) when entering and exiting ambient mode.
- Support for [color transformations](https://developer.android.com/reference/wear-os/wff/common/transform/transform#transformable) on most elements and [color tinting](https://developer.android.com/reference/wear-os/wff/user-configuration/color-configuration) on grouped elements.
- A new [`Reference`](https://developer.android.com/reference/wear-os/wff/common/reference/reference) element that lets you single-source your transform configurations.

To view features from version 4 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the
**Version 4** button is selected at the top of the documentation page.

## Version 3

Version 3 of the Watch Face Format adds several capabilities, including the
following:

- [Auto-sizing text](https://developer.android.com/reference/wear-os/wff/group/part/text/text).
- More capabilities for combining graphical objects, including [blend mode](https://developer.android.com/reference/wear-os/wff/common/attributes/blend-mode).
- Support for weighted constraints on [line elements](https://developer.android.com/reference/wear-os/wff/group/part/draw/shape/line).
- Several additional [data sources](https://developer.android.com/reference/wear-os/wff/common/attributes/source-type), primarily related to time zones.

To view features from version 3 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the
**Version 3** button is selected at the top of the documentation page.

## Version 2

Version 2 of the Watch Face Format adds several capabilities related to data
visualization, weather forecasts, and system data source types.

Highlights include the following:

- [Flavors](https://developer.android.com/reference/wear-os/wff/user-configuration/flavor): Preset configurations for your watch face that users can browse in a companion app.
- **Goal progress complication type:** Useful when users can exceed a goal such as step count.
- **Weighted elements complication type:** Useful for showing discrete subsets of data.
- **Weather conditions:** Show the current weather, as well as forecast conditions for hours or days into the future.
- A new **heart rate** system data source for complications.

To view features from version 2 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the
**Version 2** button is selected at the top of the documentation page.