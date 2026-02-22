---
title: https://developer.android.com/develop/ui/compose/glance
url: https://developer.android.com/develop/ui/compose/glance
source: md.txt
---

Jetpack Glance is a framework built on top of the [Jetpack Compose runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime)
that lets you develop and design app widgets using Kotlin APIs. *App widgets*
are miniature application views that can be embedded in other applications and
receive periodic updates.
![An information widget from a weather app.](https://developer.android.com/static/develop/ui/compose/images/glance-widget.png) **Figure 1.** An information widget from a weather app.

Glance provides a set of composables to help you build responsive widgets for
the home screen quickly and with less code. The pages in this doc set describe
how to use Glance to build app widgets.
| **Note:** Jetpack Glance is in active development. File any issues on the [issue
| tracker](https://b.corp.google.com/issues/new?component=1097239&template=1611667).

## Additional resources

For more information on canonical layouts visit [Canonical widget layouts](https://developer.android.com/design/ui/mobile/guides/widgets/layouts).
For more information on making your widget high quality and discoverable,
see [Widget quality](https://developer.android.com/docs/quality-guidelines/widget-quality).
| **Caution:** Glance requires Compose to be enabled and depends on Runtime, Graphics, and Unit [UI Compose layers](https://developer.android.com/develop/ui/compose/layering), but it's *not directly interoperable* with other existing Jetpack Compose UI elements. Avoid mixing the two.