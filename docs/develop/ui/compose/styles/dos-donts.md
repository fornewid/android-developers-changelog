---
title: https://developer.android.com/develop/ui/compose/styles/dos-donts
url: https://developer.android.com/develop/ui/compose/styles/dos-donts
source: md.txt
---

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


```kotlin
@Composable
fun GradientButton(
    modifier: Modifier = Modifier,
    // ✅ DO: for design system components, expose a style modifier to consumers to be able to customize the components
    style: Style = Style
) {
    // Consume the style
}
```

<br />

### Do: Replace visual-based parameters with a Style

Consider replacing parameters on your composables with a single `Style` parameter.
For example:


```kotlin
// Before
@Composable
fun OldButton(background: Color, fontColor: Color) {
}

// After
// ✅ DO: Replace visual-based parameters with a style that includes same properties
@Composable
fun NewButton(style: Style = Style) {
}
```

<br />

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


```kotlin
@Composable
fun BadButton(
    modifier: Modifier = Modifier,
    // ❌ DON'T set a default style here as a parameter
    style: Style = Style { background(Color.Red) }
) {
}
```

<br />

To include a "default" parameter, merge the incoming parameter style with the default defined:


```kotlin
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
```

<br />

### Don't: Provide style parameters to layout-based composables

Although you could provide a style to any composable, it's not expected that
layout-based composables, or screen-level composables, will accept style - it's
unclear from a consumer standpoint what a style would do at this level.
Styles are designed for components, not necessarily layouts.

## Don't: Create styles in Composition

`CompositionLocals` are read at the point the style is defined, not where it's
consumed. When the style is actually used, the state of the `CompositionLocal`
could have changed, resulting in an inaccurate style.


```kotlin
// DON'T - Create styles in Composition that access composition locals in this way - this will likely lead to issues when style is used / accessed, as it would not get updated when the value changes.
@Composable
fun containerStyle(): Style {
    val background = MaterialTheme.colorScheme.background
    val onBackground = MaterialTheme.colorScheme.onBackground
    return Style {
        background(background)
        contentColor(onBackground)
    }
}

// Do: Instead, Create StyleScope extension functions for your subsystems to access themed composition Locals
val StyleScope.colors: JetsnackColors
    get() = JetsnackTheme.LocalJetsnackTheme.currentValue.colors

val StyleScope.typography: androidx.compose.material3.Typography
    get() = JetsnackTheme.LocalJetsnackTheme.currentValue.typography
val StyleScope.shapes: Shapes
    get() = JetsnackTheme.LocalJetsnackTheme.currentValue.shapes
// Access CompositionLocals
val button = Style {
    background(colors.brandSecondary)
    shape(shapes.small)
}
```

<br />

## Do: Create one style for subsystem value changes

For example, if switching between dark and light mode, query existing themed
values (through the `CompositionLocal`) to change the `Style` dynamically:


```kotlin
// Do: Use CompositionLocals or themed values to create a single style
val buttonStyle = Style {
    background(colors.brandSecondary)
    shape(shapes.small)
}
```

<br />

## Do: Switch out whole Styles when the component fundamentally differs across theme definitions

You can switch out whole style objects at a theme level if they are
fundamentally different themes.

For example, if you're creating an app that has different themes per product /
page or offering, and many properties for a Style are different, switching out
whole sets of styles at a theme level is acceptable.


```kotlin
// DO Switch out whole styles when many properties differ - if Product A and Product B are two white labelled apps that provide different Themes.
val productBThemedButton = Style {
    shape(shapes.small)
    background(colors.brandSecondary)
    // other properties are fundamentally different
}

val productAThemedButton = Style {
    shape(shapes.large)
    background(colors.brand)
    // other properties are fundamentally different
}
```

<br />