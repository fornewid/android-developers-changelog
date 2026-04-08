---
title: ConstraintLayout in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/layouts/constraintlayout
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)

# ConstraintLayout in Compose Stay organized with collections Save and categorize content based on your preferences.




**Warning:** It is recommended to use other layouts to achieve the same concepts. In
each area below, there is a recommendation for the equivalent in Compose that
does not use ConstraintLayout.

[`ConstraintLayout`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayout.composable#ConstraintLayout(androidx.compose.ui.Modifier,kotlin.Int,androidx.compose.animation.core.AnimationSpec,kotlin.Function0,kotlin.Function1)) is a layout that lets you place composables relative to
other composables on the screen. It is an alternative to using multiple nested
`Row`, `Column`, `Box`, and [other custom layout elements](/reference/kotlin/androidx/compose/foundation/layout/Row.composable#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)).

In the View system, `ConstraintLayout` was the recommended way to create large
and complex layouts, as a flat view hierarchy was better for performance than
nested views are. However, this is not a concern in Compose, which is able to
efficiently handle deep layout hierarchies, so ConstraintLayout is not as
beneficial.

## Get started with `ConstraintLayout`

To use `ConstraintLayout` in Compose, you need to add this dependency in your
`build.gradle` (in addition to the [Compose setup](/develop/ui/compose/interop/adding#setup)):

```
implementation "androidx.constraintlayout:constraintlayout-compose:$constraintlayout_compose_version"
```

**Note:** The `constraintLayout-compose` artifact has a different versioning than
Jetpack Compose. Check the latest version in the [ConstraintLayout release
page](/jetpack/androidx/releases/constraintlayout).

`ConstraintLayout` in Compose works in the following way using a
[DSL](https://kotlinlang.org/docs/reference/type-safe-builders.html):

* Create references for each composable in the `ConstraintLayout` using the
  [`createRefs()`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayoutScope#createrefs) or [`createRefFor()`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintSetScope#createreffor).
* Constraints are provided using the `constrainAs()` modifier, which takes the
  reference as a parameter and lets you specify its constraints in the body
  lambda.
* Constraints are specified using `linkTo()` or other helpful methods.
* `parent` is an existing reference that can be used to specify constraints
  towards the `ConstraintLayout` composable itself.

Here's an example of a composable using a `ConstraintLayout`:

```
@Composable
fun ConstraintLayoutContent() {
    ConstraintLayout {
        // Create references for the composables to constrain
        val (button, text) = createRefs()

        Button(
            onClick = { /* Do something */ },
            // Assign reference "button" to the Button composable
            // and constrain it to the top of the ConstraintLayout
            modifier = Modifier.constrainAs(button) {
                top.linkTo(parent.top, margin = 16.dp)
            }
        ) {
            Text("Button")
        }

        // Assign reference "text" to the Text composable
        // and constrain it to the bottom of the Button composable
        Text(
            "Text",
            Modifier.constrainAs(text) {
                top.linkTo(button.bottom, margin = 16.dp)
            }
        )
    }
}

ConstraintLayoutSnippets.kt
```

This code constrains the top of the `Button` to the parent with a margin of
`16.dp` and a `Text` to the bottom of the `Button` also with a margin of
`16.dp`.

![The button appears above the text](/static/develop/ui/compose/images/layout-button-text.png)


**Figure 1.** A `Button` and a `Text` composable constrained to each other in a
`ConstraintLayout`.

## Decoupled API

In the `ConstraintLayout` example, constraints are specified inline, with a
modifier in the composable they're applied to. However, there are situations
when it's preferable to decouple the constraints from the layouts they apply to.
For example, you might want to change the constraints based on the screen
configuration, or animate between two constraint sets.

For cases like these, you can use `ConstraintLayout` in a different way:

1. Pass in a [`ConstraintSet`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintSet) as a parameter to `ConstraintLayout`.
2. Assign references created in the `ConstraintSet` to composables using the
   [`layoutId`](/reference/kotlin/androidx/compose/ui/layout/layoutId.modifier#(androidx.compose.ui.Modifier).layoutId(kotlin.Any)) modifier.

```
@Composable
fun DecoupledConstraintLayout() {
    BoxWithConstraints {
        val constraints = if (minWidth < 600.dp) {
            decoupledConstraints(margin = 16.dp) // Portrait constraints
        } else {
            decoupledConstraints(margin = 32.dp) // Landscape constraints
        }

        ConstraintLayout(constraints) {
            Button(
                onClick = { /* Do something */ },
                modifier = Modifier.layoutId("button")
            ) {
                Text("Button")
            }

            Text("Text", Modifier.layoutId("text"))
        }
    }
}

private fun decoupledConstraints(margin: Dp): ConstraintSet {
    return ConstraintSet {
        val button = createRefFor("button")
        val text = createRefFor("text")

        constrain(button) {
            top.linkTo(parent.top, margin = margin)
        }
        constrain(text) {
            top.linkTo(button.bottom, margin)
        }
    }
}

ConstraintLayoutSnippets.kt
```

Then, when you need to change the constraints, you can just pass a different
`ConstraintSet`.

## `ConstraintLayout` concepts

`ConstraintLayout` contains concepts such as guidelines, barriers, and chains
that can help with positioning elements inside your composable.

### Guidelines

Guidelines are small visual helpers to design layouts with. Composables can be
constrained to a guideline. Guidelines are useful for positioning elements at a
certain [`dp`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayoutBaseScope#createGuidelineFromTop(androidx.compose.ui.unit.Dp)) or [`percentage`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayoutBaseScope#createGuidelineFromStart(kotlin.Float)) inside the parent composable.

There are two different kinds of [guidelines](/reference/kotlin/androidx/constraintlayout/compose/ConstraintSet#guidelines), vertical and horizontal. The
two horizontal ones are `top` and `bottom`, and the two vertical are `start` and
`end`.

```
ConstraintLayout {
    // Create guideline from the start of the parent at 10% the width of the Composable
    val startGuideline = createGuidelineFromStart(0.1f)
    // Create guideline from the end of the parent at 10% the width of the Composable
    val endGuideline = createGuidelineFromEnd(0.1f)
    //  Create guideline from 16 dp from the top of the parent
    val topGuideline = createGuidelineFromTop(16.dp)
    //  Create guideline from 16 dp from the bottom of the parent
    val bottomGuideline = createGuidelineFromBottom(16.dp)
}

ConstraintLayoutSnippets.kt
```

To create a guideline, use `createGuidelineFrom*` with the type of guideline
required. This creates a reference that can be used in the
`Modifier.constrainAs()` block.

**Warning:** Consider using the `Spacer` composable to achieve the same effect with
`Row`s and `Column`s instead.

### Barriers

[Barriers](/reference/kotlin/androidx/constraintlayout/compose/ConstraintSet#barriers) reference multiple composables to create a virtual guideline
based on the most extreme widget on the specified side.

To create a barrier, use `createTopBarrier()` (or: `createBottomBarrier()`,
`createEndBarrier()`, `createStartBarrier()`), and provide the references that
should make up the barrier.

```
ConstraintLayout {
    val constraintSet = ConstraintSet {
        val button = createRefFor("button")
        val text = createRefFor("text")

        val topBarrier = createTopBarrier(button, text)
    }
}

ConstraintLayoutSnippets.kt
```

The barrier can then be used in a `Modifier.constrainAs()` block.

**Warning:** Consider using [Intrinsic measurements](/develop/ui/compose/layouts/intrinsic-measurements) to achieve a similar effect
with `Row`s and `Column`s.

### Chains

[Chains](/reference/kotlin/androidx/constraintlayout/compose/ConstraintSet#chains) provide group-like behavior in a single axis (horizontally or
vertically). The other axis can be constrained independently.

To create a chain, use either [`createVerticalChain`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayoutBaseScope#createVerticalChain(kotlin.Array,androidx.constraintlayout.compose.ChainStyle)) or
[`createHorizontalChain`](/reference/kotlin/androidx/constraintlayout/compose/ConstraintLayoutBaseScope#createHorizontalChain(kotlin.Array,androidx.constraintlayout.compose.ChainStyle)):

```
ConstraintLayout {
    val constraintSet = ConstraintSet {
        val button = createRefFor("button")
        val text = createRefFor("text")

        val verticalChain = createVerticalChain(button, text, chainStyle = ChainStyle.Spread)
        val horizontalChain = createHorizontalChain(button, text)
    }
}

ConstraintLayoutSnippets.kt
```

The chain can then be used in the `Modifier.constrainAs()` block.

A chain can be configured with different [`ChainStyles`](/reference/kotlin/androidx/constraintlayout/compose/ChainStyle), which decide how
to deal with the space surrounding a composable, such as:

* `ChainStyle.Spread`: Space is distributed evenly across all the composables,
  including free space before the first composable and after the last
  composable.
* `ChainStyle.SpreadInside`: Space is distributed evenly across the all
  composables, without any free space before the first composable or after the
  last composable.
* `ChainStyle.Packed`: Space is distributed before the first and after the
  last composable, composables are packed together without space in between
  each other.

**Warning:** Consider using `Rows` and `Columns` with different[Arrangements](/reference/kotlin/androidx/compose/foundation/layout/Arrangement)
to achieve a similar effect to chains in `ConstraintLayout`.