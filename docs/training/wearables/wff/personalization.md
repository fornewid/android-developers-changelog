---
title: Support personalization  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/wff/personalization
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Support personalization Stay organized with collections Save and categorize content based on your preferences.



Once you have a basic watch face put together, letting the user customize both
the appearance of the watch face and the information shown on it, helps make the watch
more personal and more useful.

For personalization, use `UserConfigurations` to allow the user to
tailor the appearance. For customizing the information shown, include support for Complications.

For both types of customizations, the user uses the Watch Face Editor to make
changes. To enable the editor, set the watch face to be *editable* (see
the packaging guidance for more information).