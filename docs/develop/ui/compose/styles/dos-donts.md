---
title: Do's and don'ts with Styles  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/styles/dos-donts
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Do's and don'ts with Styles Stay organized with collections Save and categorize content based on your preferences.




This page describes best practices for working with styles that achieve consistency
across your codebase, as well as principles we've followed while
designing the APIs.

## Do's

Follow these best practices:

### Do: Use Styles for visuals and modifiers for behaviors

Use the Styles API for visual configuration (backgrounds, padding, borders), and
reserve modifiers for behaviors like click logic, gesture detection, or
accessibility.

### Do: Expose Style parameters in design systems

For your own custom design-system components, you should expose a `Style` object
after the modifier parameter.

```
@Composable
fun GradientButton(
    modifier: Modifier = Modifier,
    // ✅ DO: for design system components, expose a style modifier to consumers to be able to customize the components
    style: Style = Style
) {
    // Consume the style
}

DosDonts.kt
```

### Do: Replace visual-based parameters with a Style

Consider replacing parameters on your composables with a single `Style` parameter.
For example:

```
// Before
@Composable
fun OldButton(background: Color, fontColor: Color) {
}

// After
// ✅ DO: Replace visual-based parameters with a style that includes same properties
@Composable
fun NewButton(style: Style = Style) {
}

DosDonts.kt
```

### Do: Prioritize Styles for animations

Use the built-in `animate` block for state-based styling with animations for
performance gains over modifiers.

### Do: Take advantage of "Last-write-wins"

Take advantage of the fact that `style` properties overwrite rather than stack.
Use this to override default component borders or backgrounds without
needing multiple parameters.

## Don'ts

The following patterns are discouraged:

### Don't: Use Styles for interaction logic

Don't attempt to handle `onClick` or gesture detection within a style. Styles
are limited to visual configurations based on state, so they shouldn't handle
business logic; instead, they should only have a different visual based on state.

### Don't: Provide a default style as a default parameter

Style parameters should always be declared using `style: Style = Style`:

```
@Composable
fun BadButton(
    modifier: Modifier = Modifier,
    // ❌ DON'T set a default style here as a parameter
    style: Style = Style { background(Color.Red) }
) {
}

DosDonts.kt
```

To include a "default" parameter, merge the incoming parameter style with the default defined:

```
@Composable
fun GoodButton(
    modifier: Modifier = Modifier,
    // ✅ Do: always pass it as a Style, do not pass other defaults
    style: Style = Style
) {
    // ...
    val defaultStyle = Style { background(Color.Red) }
    // ✅ Do Combine defaults inside with incoming parameter
    Box(modifier = modifier.styleable(styleState, defaultStyle, style)) {
      // your logic
    }
}

DosDonts.kt
```

### Don't: Provide style parameters to layout-based composables

Although you could provide a style to any composable, it's not expected that
layout-based composables, or screen-level composables, will accept style - it's
unclear from a consumer standpoint what a style would do at this level.
Styles are designed for components, not necessarily layouts.