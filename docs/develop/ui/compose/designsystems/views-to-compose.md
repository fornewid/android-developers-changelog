---
title: https://developer.android.com/develop/ui/compose/designsystems/views-to-compose
url: https://developer.android.com/develop/ui/compose/designsystems/views-to-compose
source: md.txt
---

When you introduce Compose in an existing app, you need to migrate your themes in XML to use `MaterialTheme` for Compose screens. This means your app's theming will have two sources of truth: the View-based theme and the Compose theme. Any changes to your styling need to be made in multiple places. Once your app is fully migrated to Compose, you can remove your XML theming.
| **Note:** For non-Material design systems, see [Custom design systems in Compose](https://developer.android.com/develop/ui/compose/designsystems/custom).

To migrate your XML themes to Compose, use the [Material Theme Builder](https://m3.material.io/theme-builder) to migrate from an XML theme to [Material 3](https://developer.android.com/develop/ui/compose/designsystems/material3#material-theming) in Compose. You can use your existing color roles, such as primary and secondary colors from your XML theme, and pass them to the Material Theme Builder. This creates a fully Material 3 theme in Compose and provides downloadable color and theme files to use in your app.

Material Theme Builder generates a `MaterialTheme` and light and dark color schemes for your app. If your app uses custom shapes or typography, migrate your custom shapes and typography by defining a `Shape` and `Typography`, respectively. Once defined, provide that information to your `MaterialTheme`. See [shapes](https://developer.android.com/develop/ui/compose/designsystems/material3#shapes) and [typography](https://developer.android.com/develop/ui/compose/designsystems/material3#typography) to learn more.
| **Note:** If you are not using Material 3, see [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material) to learn how to create a theme. See [Migrate from Material 2 to Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material2-material3) when you are ready to migrate to Material 3.