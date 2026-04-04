---
title: Watch faces  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/watch-faces
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Watch faces Stay organized with collections Save and categorize content based on your preferences.




A watch face is the first surface users interact with when they check their
smartwatch and the most used surface of Wear OS. Users can customize their
watch face to their style or for their needs.

![watchface-hero](/static/wear/images/design/watchface-hero.png)

## UX Principles

The following sections describe principles to keep in mind when creating
watch faces.

|  |  |  |
| --- | --- | --- |
| Time-telling | Expressive | Useful |
| The purpose of a watch face is foremost to tell the time. On average, people check the time 150 times a day. Ensure that time is highly visible on your screen. | Watch faces provide unique ways for users to express their personality and style. Include variety in your watch face designs and facilitate customization. | Watch faces provide users with the ability to quickly glance at important information. Use complications on the watch face to let users to view what they want. |

## Guidelines

Watch faces are a core experience on every watch. When designing watch faces
you have flexibility to create unique watch faces that resonate with users. Keep
in mind the following guidelines.

|  |  |
| --- | --- |
|  | **Make glanceable** Make watch faces glanceable with clear fonts, legible icons, and a simple layout. This lets users access important information quickly. |
|  | **Include complications** Complications provide quick access to important information and can be personalized to display what is relevant to the user. |
|  | **Allow for customization** Offer customization options for watch faces such as color ways, customizable hands and complications. This allows users to personalize their smartwatch to their style and functional needs. This enhances the aesthetic appeal and practicality of the watch face. |
|  | **Use the color black** Use black as the primary color as this helps to conserve battery life on your watch. Black is also versatile and neutral, so it allows other design elements to stand out. |
|  | **Stay within the bezel** Design watch faces to fit within the bezel of the smartwatch to ensure a clean appearance and minimize essential elements being cropped or covered by the bezel. |

## Power considerations

Design watch faces to conserve battery life with simple graphics, dark
backgrounds, and optimized code. This improves the user experience and allows
the battery to last longer.

Every watch face has two modes.

|  |  |
| --- | --- |
|  |  |
| **Interactive** This is the watch face shown when the user is interacting with the watch. | **Always-on display (AoD)** This is the watch face shown when the users are not interacting with the watch. AoD watch faces must illuminate 15% or less of the pixels on the watch face to conserve battery life. |

For more information about watch faces, see
[Build watch faces](/training/wearables/watch-faces).