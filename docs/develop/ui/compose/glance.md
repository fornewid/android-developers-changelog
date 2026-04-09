---
title: Jetpack Glance  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Jetpack Glance Stay organized with collections Save and categorize content based on your preferences.




Jetpack Glance is a framework built on top of the [Jetpack Compose runtime](/jetpack/androidx/releases/compose-runtime)
that lets you develop and design app widgets using Kotlin APIs. *App widgets*
are miniature application views that can be embedded in other applications and
receive periodic updates.

![An information widget from a weather app.](/static/develop/ui/compose/images/glance-widget.png)


**Figure 1.** An information widget from a weather app.

Glance provides a set of composables to help you build responsive widgets for
the home screen quickly and with less code. The pages in this doc set describe
how to use Glance to build app widgets.

**Note:** Jetpack Glance is in active development. File any issues on the [issue
tracker](https://b.corp.google.com/issues/new?component=1097239&template=1611667).

## Additional resources

For more information on canonical layouts visit [Canonical widget layouts](/design/ui/mobile/guides/widgets/layouts).
For more information on making your widget high quality and discoverable,
see [Widget quality](/docs/quality-guidelines/widget-quality).

**Caution:** Glance requires Compose to be enabled and depends on Runtime, Graphics,
and Unit [UI Compose layers](/develop/ui/compose/layering), but it's *not directly interoperable* with
other existing Jetpack Compose UI elements. Avoid mixing the two.

[Next

Glance setup

arrow\_forward](/develop/ui/compose/glance/setup)