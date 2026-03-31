---
title: Styles in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/styles
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Styles in Compose Stay organized with collections Save and categorize content based on your preferences.



**Note:** Styles are `@Experimental` and likely to change in upcoming releases, with
Material support for Styles added in future releases. If you have any feedback,
[file Styles issues here](https://issuetracker.google.com/issues/new?component=612128).

The Style API is a new paradigm for customizing or "styling" elements and
components in Jetpack Compose, which has traditionally been done through
modifiers. It is designed to unlock deeper, easier customization.

The Styles API improves flexibility across form factors, provides better
performance, and enables easier custom design system creation. Even if you don't
need custom components, the Styles API has many benefits for your design system.

An important distinction is that Styles are not a replacement for modifiers, but
they do act as a replacement for styling parameters, such as padding and colors.
We recommend transitioning to using Styles over parameters for increased
flexibility and performance.

## Benefits of Styles

* **Simplifies state-based styling:** The API provides a more concise and
  declarative way to define styles that change based on different states
  (e.g., hovered, focused, pressed), significantly reducing boilerplate code
  compared to the modifier system.
* **Improves animated state transitions:** The Style API allows for built-in
  animation of style properties between states with ideal performance
  characteristics, avoiding recompositions that occur with the current
  `animateColorAsState` approach.
* **Streamlines component APIs:** By introducing a single Style parameter for
  customization, component APIs are dramatically simplified and offer greater
  flexibility.
* **Less recompositions leading to better performance over modifiers:** Styles
  run in the Draw and Layout phases of Compose, skipping out on the
  Composition phase.
* **More standardized set of APIs:** A standard set of stylistic properties
  makes any component styleable.

## Core concepts

| Concept | Description |
| --- | --- |
| **[`Style`](/reference/kotlin/androidx/compose/foundation/style/Style)** | An interface that defines the appearance of a UI element, with a standard set of styleable properties. It's similar to CSS styles and can be customized locally or through a theme. Styles overwrite one another; setting a property twice (e.g., `background()`) results in a single, final value. |
| **[`StyleScope`](/reference/kotlin/androidx/compose/foundation/style/StyleScope)** | A receiver scope for the `applyStyle()` function within a Style. It provides functions to define visual properties (padding, background, border, etc.) and access the current `StyleState`. |
| **[`StyleState`](/reference/kotlin/androidx/compose/foundation/style/StyleState)** | Provides state (e.g., `isEnabled`, `isPressed`, `isChecked`, custom states) that you can use within a Style to define conditional styling. |

## Get started: Add dependencies

To use the APIs in your own project, make sure you are using the latest alpha
release of Jetpack Compose foundation. In your `settings.gradle.kts` file, add
the snapshot maven repository to the list of repositories to use.

Either in your `libs.versions.toml` or directly in your `app/build.gradle.kts`
file, set the version of Compose to `1.11.0-alpha06`:

```
compose = "1.11.0-alpha06"
```

```
androidx-compose-runtime = { group = "androidx.compose.runtime", name = "runtime", version.ref = "compose" }
androidx-compose-ui = { group = "androidx.compose.ui", name = "ui", version.ref = "compose" }
androidx-compose-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics", version.ref = "compose" }
androidx-compose-ui-tooling = { group = "androidx.compose.ui", name = "ui-tooling", version.ref = "compose" }
androidx-compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview", version.ref = "compose" }
androidx-compose-ui-test-manifest = { group = "androidx.compose.ui", name = "ui-test-manifest", version.ref = "compose" }
androidx-compose-ui-test-junit4 = { group = "androidx.compose.ui", name = "ui-test-junit4", version.ref = "compose" }
androidx-compose-foundation = { group = "androidx.compose.foundation", name = "foundation", version.ref = "compose" }
```