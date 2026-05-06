---
title: Make composables more accessible  |  App quality  |  Android Developers
url: https://developer.android.com/guide/topics/ui/accessibility/composables
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Make composables more accessible Stay organized with collections Save and categorize content based on your preferences.





**Note:** Documentation across [developer.android.com](/) is being refactored to
show how to accomplish tasks with Compose. We recommend using Compose for your
app, but you can still access the Views-specific information for the concepts
on this page at [Make custom views more accessible (Views)](/guide/topics/ui/accessibility/views/custom-views).

Try to make the composables in your app more accessible. The following steps
can improve your composable's accessibility:

* Describe your composable
* Add interactions
* Handle complex UIs

## Describe your composable

To describe a composable, declare its semantic properties (such as its `role`,
`label`, `state`, or actions) using [`Modifier.semantics`](/reference/kotlin/androidx/compose/ui/semantics/package-summary). Accessibility
services can read these semantic properties and use the information to interact
with and announce the UI.

The `Role` property is especially important because it provides the necessary
context for accessibility services to announce a component's purpose and
expected interactions. For example, consider a custom icon that behaves like a
clickable button. By setting its role to `Role.button`, you can make sure that
screen readers announce it as an interactive element, not a static image.

For more information, see [Semantics](/develop/ui/compose/accessibility/semantics).

## Add interactions

To add interactions to your composable, use the [`clickable`](/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) or
[`toggleable`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).toggleable(kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.semantics.Role,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) modifiers. These modifiers come with built-in semantic
properties that accessibility services can read. To make complex touchscreen
gestures more accessible, use [`CustomAccessibilityAction`](/reference/kotlin/androidx/compose/ui/semantics/CustomAccessibilityAction).

For more information, see [Custom actions](/develop/ui/compose/accessibility/semantics#custom-actions).

## Handle complex UIs

Although Compose supports many accessibility features by default, a more
complex UI might require more customized behavior. You can make complex UIs
more accessible by logically structuring the UI hierarchy and providing a
logical reading order for accessibility services to traverse.

**Structure the UI hierarchy logically:** If a parent composable consists of
multiple child elements, you can explicitly specify how those elements are
grouped or override them entirely. For more information, see
[Merging and clearing](/develop/ui/compose/accessibility/merging-clearing).

**Control the traversal order:** If Compose's default reading order is
insufficient, you can manually control how screen readers navigate your UI
elements. For more information, see [Modify traversal order](/develop/ui/compose/accessibility/traversal).

**Control focus:** For keyboard and D-pad navigation, you can manually override
the focus traversal order. For more information, see [Change focus behavior](/develop/ui/compose/touch-input/focus/change-focus-behavior)
and [Change focus traversal order](/develop/ui/compose/touch-input/focus/change-focus-traversal-order).

## Additional resources

For more information about making your UI accessible, see the following
additional resources:

### Documentation

* [Accessibility in Jetpack Compose](/develop/ui/compose/accessibility)

### Views content

* [Make custom views more accessible (Views)](/guide/topics/ui/accessibility/views/custom-views)