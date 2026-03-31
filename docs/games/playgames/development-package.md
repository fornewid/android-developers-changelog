---
title: Package a game for Google Play Games on PC  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/development-package
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Package a game for Google Play Games on PC Stay organized with collections Save and categorize content based on your preferences.



Since Google Play Games on PC provides a standard Android runtime environment,
there are no differences between packing your game for mobile or PC outside of
ensuring that you include x86 or x86-64 binaries. When possible, you should use
the same APK or [App Bundle](/guide/app-bundle) on PC as you do for mobile
builds.

When using one package across mobile and Google Play Games on PC, it is best to
enable Google Play Games on PC specific features at runtime either by
[detecting the presence of a keyboard](/games/develop/all-screens#handle-interaction-models):

### Kotlin

```
val hasKeyboard = resources.configuration.keyboard == KEYBOARD_QWERTY
```