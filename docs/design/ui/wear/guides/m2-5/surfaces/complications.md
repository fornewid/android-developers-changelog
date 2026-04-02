---
title: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/complications
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/complications
source: md.txt
---

# Complications

A complication is a UI element on a watch face that contains highly-glanceable information that users want to see often throughout the day. For example, you could create a current weather complication, or a heart rate complication.

![complication-hero](https://developer.android.com/static/wear/images/design/hero-complication.png)

## UX Principles

The following sections describe principles to keep in mind when creating complications.

|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ## Glanceable                                                                                                                | ## Content forward                                                                                                                                       | ## Privacy first                                                                                                                     |
| Complications are small components designed to help users complete frequent tasks quickly. Make content simple and readable. | Complications are most valuable when the content that the user needs is made visible by simply raising their wrist, without needing further interaction. | The watch travels with the user everywhere they go. Consider how the content in the complications is relevant to the user's context. |

## Use cases

When tapped, complications can help users access a specific part of an app. They can also perform a self-contained action. For example, tapping a Water Count complication changes the glass count.

![water-complication](https://developer.android.com/static/wear/images/design/complications_1.png)

WearOS automatically includes an app shortcut complication, so you don't need to create your own. Instead focus on creating complications that can help users complete focused tasks.

## Types

Complication types refer to the kinds of data shown on the complication or supplied by a data source. A complication always has a single type that includes required and optional fields. A required field contains the primary data. Most complication types take their name from their required field. You can choose how many complications to include in your watch face and the complication types to support. There are five complication types.

|     Type     |      Required fields      |                    Optional fields                     |              Class name              |                                          Example                                           |
|--------------|---------------------------|--------------------------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------|
| SHORT_TEXT   | Short text                | Icon, Burn in protection icon, Short title             | `ShortTextComplicationData`          | ![](https://developer.android.com/static/wear/images/design/short-text-complication.png)   |
| ICON         | Icon                      | Burn in protection icon                                | `MonochromaticImageComplicationData` | ![](https://developer.android.com/static/wear/images/design/icon-complication.png)         |
| RANGED_VALUE | Value Min value Max value | Icon, Burn in protection icon, Short text, Short title | `RangedValueComplicationData`        | ![](https://developer.android.com/static/wear/images/design/ranged-value-complication.png) |
| LONG_TEXT    | Long text                 | Long title, Icon, Burn in protection icon, Small image | `LongTextComplicationData`           | ![](https://developer.android.com/static/wear/images/design/long-text-complication.png)    |
| SMALL_IMAGE  | Small image               |                                                        | `SmallImageComplicationData`         | ![](https://developer.android.com/static/wear/images/design/small-image-complication.png)  |
| LARGE_IMAGE  | Large image               |                                                        | `PhotoImageComplicationData`         | ![](https://developer.android.com/static/wear/images/design/large-image-complication.png)  |

For more information about complication data sources, see[Complication types](https://developer.android.com/training/wearables/watch-faces/complications#types).