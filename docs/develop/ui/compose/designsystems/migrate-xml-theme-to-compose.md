---
title: Migrate XML themes to Material 3 in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/designsystems/migrate-xml-theme-to-compose
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Migrate XML themes to Material 3 in Compose Stay organized with collections Save and categorize content based on your preferences.




When you introduce Compose in an existing app, you need to migrate your Material
XML themes to use `MaterialTheme` for Compose components. This means your app's
theming will have two sources of truth: the View-based theme and the Compose
theme. Any changes to your styling need to be made in multiple places. Once
your app is fully migrated to Compose, remove your XML theming.

You can use the [Material Theme Builder](https://m3.material.io/theme-builder)
tool for migrating colors.

When you start the migration from XML to Compose, migrate the theming to
Material 3 Compose theming.

## Glossary

| Term | Definition |
| --- | --- |
| `MaterialTheme` | The composable function that provides theming (colors, typography, shapes) to Compose UI components. |
| `Shape` | A Compose object used to define custom component shapes for a `MaterialTheme`. |
| `Typography` | A Compose object used to define custom text styles (font families, sizes, weights) for a `MaterialTheme`. |
| `Color` | A Compose object used to define custom color schemes for `MaterialTheme`. |
| XML Theme | The Android theming system defined in XML files, used by the View system. |

## Limitations

Before migrating, be aware of the following limitations:

* This guide focuses on migrating to Material 3 only. For migrating from
  alternative design systems, see [Material 2](/develop/ui/compose/designsystems/material) or
  [Custom design systems in Compose](/develop/ui/compose/designsystems/custom).
* The ultimate goal is a complete migration to Compose, which allows for the
  removal of XML theming. This guide explains how to migrate, but it doesn't
  explain how to finally remove XML theming.

## Step 1: Evaluate the design system

Identify which design system is used in the XML View project.
Analyze the migration path and necessary steps to migrate the existing design
system to Material 3 in Compose.

## Step 2: Identify theme source files

Identify and locate all XML resources and files necessary for theming:
light and dark color schemes, themes, shapes, dimensions, typography, styles
and other relevant files.

Resources such as strings can be reused as is and don't need to be migrated.

## Step 3: Migrate colors

Migrate the dark and light color schemes from XML to their equivalents in
Material 3 Compose.

**Note:** Material 3 naming differs from Material 2 color naming.

## Step 4: Migrate custom shapes and typography

* If your app uses custom shapes:

  1. In your Compose code, define a `Shape` object to replicate your XML shape
     definitions.
  2. Provide this `Shape` object to your `MaterialTheme`.

     For more details, see [shapes](/develop/ui/compose/designsystems/material3#shapes).
* If your app uses custom typography:

  1. In your Compose code, define a `Typography` object in your Compose code to
     replicate your XML text styles and font definitions.
  2. Provide this `Typography` object to your `MaterialTheme`.

     For more details, see [typography](/develop/ui/compose/designsystems/material3#typography).

## Step 5: Validate the theme migration

Always use the existing theme values from the original XML theme as the source
of truth for the new Material Theme in Compose
Never invent new theme values during migration, to maintain brand consistency
and avoid visual regressions.

Verify all new Compose theme values match the existing XML values.
Don't hardcode any migrated values.