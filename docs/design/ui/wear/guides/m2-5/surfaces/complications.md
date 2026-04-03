---
title: Complications  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/complications
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Complications Stay organized with collections Save and categorize content based on your preferences.



A complication is a UI element on a watch face that contains highly-glanceable
information that users want to see often throughout the day. For example, you
could create a current weather complication, or a heart rate complication.

![complication-hero](/static/wear/images/design/hero-complication.png)

## UX Principles

The following sections describe principles to keep in mind when creating
complications.

|  |  |  |
| --- | --- | --- |
| Glanceable | Content forward | Privacy first |
| Complications are small components designed to help users complete frequent tasks quickly. Make content simple and readable. | Complications are most valuable when the content that the user needs is made visible by simply raising their wrist, without needing further interaction. | The watch travels with the user everywhere they go. Consider how the content in the complications is relevant to the user's context. |

## Use cases

When tapped, complications can help users access a specific part of an app.
They can also perform a self-contained action. For example, tapping a
Water Count complication changes the glass count.

![water-complication](/static/wear/images/design/complications_1.png)

WearOS automatically includes an app shortcut complication, so you don't need to
create your own. Instead focus on creating complications that can help users
complete focused tasks.

## Types

Complication types refer to the kinds of data shown on the complication or
supplied by a data source. A complication always has a single type that includes
required and optional fields. A required field contains the primary data. Most
complication types take their name from their required field. You can choose how
many complications to include in your watch face and the complication types to
support. There are five complication types.

| Type | Required fields | Optional fields | Class name | Example |
| --- | --- | --- | --- | --- |
| SHORT\_TEXT | Short text | Icon, Burn in protection icon, Short title | `ShortTextComplicationData` |  |
| ICON | Icon | Burn in protection icon | `MonochromaticImageComplicationData` |  |
| RANGED\_VALUE | Value Min value Max value | Icon, Burn in protection icon, Short text, Short title | `RangedValueComplicationData` |  |
| LONG\_TEXT | Long text | Long title, Icon, Burn in protection icon, Small image | `LongTextComplicationData` |  |
| SMALL\_IMAGE | Small image |  | `SmallImageComplicationData` |  |
| LARGE\_IMAGE | Large image |  | `PhotoImageComplicationData` |  |

For more information about complication data sources, see
[Complication types](/training/wearables/watch-faces/complications#types).