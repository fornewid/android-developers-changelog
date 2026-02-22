---
title: https://developer.android.com/training/wearables/watch-faces/adding-complications
url: https://developer.android.com/training/wearables/watch-faces/adding-complications
source: md.txt
---

A watch face complication displays data from a data source. Using the
[Watch Face Format](https://developer.android.com/training/wearables/wff), you can choose the data sources to get the underlying
data. This lets your watch faces display information beyond the time of day
without needing code for getting the data.

## Use the Watch Face Format

The [`Complication`](https://developer.android.com/training/wearables/wff/complication/complication) element lets you define up to eight complications within
a single watch face. The element also lets you define where on the watch face
each complication appears.

For more information, check out the [WatchFaceFormat sample](https://github.com/android/wear-os-samples/blob/main/WatchFaceFormat/Complications/watchface/src/main/res/raw/watchface.xml) on
GitHub.

## Types and fields

The following table describes the types and fields of the
[`ComplicationData`](https://developer.android.com/reference/kotlin/androidx/wear/watchface/complications/data/ComplicationData) object. If a watch face requests a field that is invalid
for a complication type, a default value for the field is returned. For example,
if a watch face tries to access a `LONG_TEXT` field in a `SHORT_TEXT` type, the
default value for the `LONG_TEXT` field, null, is returned. Note optional fields
are not guaranteed to be displayed.

<br />

<br />

<br />

| Type | Required fields | Optional fields | Notes |
|---|---|---|---|
| `SHORT_TEXT` | Short text | Icon Burn-in protection icon Short title Content description <br /> | Shows only one icon or short title if either or both are provided. |
| `MONOCHROMATIC_IMAGE` | Monochromatic image | Burn-in protection icon Content description <br /> | Used when text is not needed. The icon is expected to be single color and might be tinted by the watch face. |
| `RANGED_VALUE` | Value Min value Max value | Monochromatic image Burn-in protection icon Short text Short title Color ramp Dynamic value Content description <br /> | If you want to draw your own progress bar, you can use the [`isRangedValueProgressHidden()`](https://developer.android.com/reference/androidx/wear/watchface/complications/rendering/ComplicationDrawable#isRangedValueProgressHidden()) method to hide the progress bar provided by the [`ComplicationDrawable`](https://developer.android.com/reference/androidx/wear/watchface/complications/rendering/ComplicationDrawable) class. |
| `GOAL_PROGRESS` | Value Target value | Monochromatic image Burn-in protection icon Short text Short title Color ramp Dynamic value Content description <br /> | GOAL_PROGRESS is intended for things like step count where the Value starts at zero, and it's allowed to go past the Target value. |
| `LONG_TEXT` | Long text | Long title Monochromatic image Burn-in protection icon Small image Content description | Shows the long title if it's provided. |
| `SMALL_IMAGE` | Small image | Content description | A small image has one of two styles: *photo style* or *icon style* . Photo style means it is expected to fill the space and can be cropped. Icon style means it can't be cropped and can be padded. Image variability can result in an unsuitable image for display in ambient mode on devices with burn-in protection or with low-bit ambient mode. When burn-in protection or low-bit ambient mode is enabled, the watch face might use the burn-in protection small image because it is safe. Otherwise, since it is hard for a watch face to determine suitability, an image isn't displayed. |
| `LARGE_IMAGE` | Large image | Content description | This image is expected to be large enough to fill the watch face. Image variability can result in an unsuitable image for display in ambient mode on devices with burn-in protection or with low-bit ambient mode. Since it is hard for a watch face to determine suitability for display, a watch face doesn't display an image in ambient mode if burn-in protection or low-bit ambient is enabled. |
| `WEIGHTED_ELEMENTS` | Elements list | Monochromatic image Burn-in protection icon Short text Short title Content description | Each Element consists of a color and a weight (greater than zero). The size of the element when rendered should be proportional to its weight. Weights are not required to sum to any particular value. Note watch faces are allowed to recolor WEIGHTED_ELEMENTS. |


The following table describes complication types for empty data that
can be sent for any complication slot. These types have no fields
and don't need to be included in a
list of supported types. These types enable watch
faces to differentiate among the following three cases:

- No source was chosen
- The user has selected "empty" for a slot
- A source has no data to send


Sources can't send `TYPE_EMPTY` in response to
update requests. Send `TYPE_NO_DATA` instead.

| Complication type | Description |
|---|---|
| `TYPE_NOT_CONFIGURED` | Sent by the system when a complication activates but the user has not selected a source and no default was set. Can't be sent by sources. |
| `TYPE_EMPTY` | Sent by the system when a complication activates and the user chooses "empty" instead of a source, or when the watch face chooses no source and this complication type as the default. Can't be sent by sources. |
| `TYPE_NO_DATA` | Sent by the system when a complication that has a source activates to clear the complication before actual data is received from the source. Can be sent by sources if they have no actual data to send. |

### On some devices, watch faces and complications must use Watch Face Format

If your existing watch face uses the [Jetpack Watch Face library](https://developer.android.com/jetpack/androidx/releases/wear-watchface) or the
[Wearable Support Library](https://developer.android.com/reference/android/support/wearable/watchface/package-summary), users continue to see data from all data sources
in watch face complications on the following devices:

- Devices that run Wear OS 4 or earlier.
- Devices that receive an OTA upgrade to Wear OS 5.

Furthermore, if your existing watch face utilizes the Jetpack Watch Face library
or the Wearable Support Library and is installed on one of these devices, the
watch face can continue to receive updates.

However, on new watches launched with Wear OS 5, watch faces must use the
[Watch Face Format](https://developer.android.com/training/wearables/wff). For this reason, we recommend that you migrate to using
the Watch Face Format.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Exposing data to watch face complications on Wear OS](https://developer.android.com/codelabs/data-sources)
- [Complication](https://developer.android.com/training/wearables/wff/complication/complication)
- [DefaultProviderPolicy](https://developer.android.com/training/wearables/wff/complication/default-provider-policy)