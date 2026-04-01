---
title: https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple
url: https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple
source: md.txt
---

To improve composition performance of interactive components that use
`Modifier.clickable`, we've introduced new APIs. These APIs allow for more
efficient `Indication` implementations, such as ripples.

`androidx.compose.foundation:foundation:1.7.0+` and
`androidx.compose.material:material-ripple:1.7.0+` include the following API
changes:

| **Deprecated** | **Replacement** |
|---|---|
| `Indication#rememberUpdatedInstance` | `IndicationNodeFactory` |
| `rememberRipple()` | New `ripple()` APIs provided in Material libraries instead. Note: In this context, "Material libraries" refers to `androidx.compose.material:material`, `androidx.compose.material3:material3`, `androidx.wear.compose:compose-material` and `androidx.wear.compose:compose-material3.` |
| `RippleTheme` | Either: - Use the Material library `RippleConfiguration` APIs, or - Build your own design system ripple implementation |

This page describes the behavior change impact and instructions for migrating to
the new APIs.

## Behavior change

The following library versions include a ripple behavior change:

- `androidx.compose.material:material:1.7.0+`
- `androidx.compose.material3:material3:1.3.0+`
- `androidx.wear.compose:compose-material:1.4.0+`

These versions of Material libraries no longer use `rememberRipple()`; instead,
they use the new ripple APIs. As a result, they do not query `LocalRippleTheme`.
Therefore, if you set `LocalRippleTheme` in your application, **Material
components will not use these values**.

The following sections describe how to migrate to the new APIs.

## Migrate from `rememberRipple` to `ripple`

### Using a Material library

If you are using a Material library, directly replace `rememberRipple()` with a
call to `ripple()` from the corresponding library. This API creates a ripple
using values derived from the Material theme APIs. Then, pass the returned
object to `Modifier.clickable` and/or other components.

For example, the following snippet uses the deprecated APIs:


```kotlin
Box(
    Modifier.clickable(
        onClick = {},
        interactionSource = remember { MutableInteractionSource() },
        indication = rememberRipple()
    )
) {
    // ...
}
```

<br />

You should modify the above snippet to:


```kotlin
@Composable
private fun RippleExample() {
    Box(
        Modifier.clickable(
            onClick = {},
            interactionSource = remember { MutableInteractionSource() },
            indication = ripple()
        )
    ) {
        // ...
    }
}
```

<br />

Note that `ripple()` is no longer a composable function and does not need to be
remembered. It can also be reused across multiple components, similar to
modifiers, so consider extracting the ripple creation to a top-level value to
save allocations.

### Implementing custom design system

If you're implementing your own design system, and you were previously using
`rememberRipple()` along with a custom `RippleTheme` to configure the ripple,
you should instead provide your own ripple API that delegates to the ripple node
APIs exposed in `material-ripple`. Then, your components can use your own ripple
that consumes your theme values directly. For more information, see [Migrate
from`RippleTheme`](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple#migrate-ripple-theme).

## Migrate from `RippleTheme`

### Using `RippleTheme` to disable a ripple for a given component

The `material` and `material3` libraries expose `RippleConfiguration` and
`LocalRippleConfiguration`, which allow you to configure the appearance of
ripples within a subtree. Note that `RippleConfiguration` and
`LocalRippleConfiguration` are experimental, and only intended for per-component
customization. Global/theme-wide customization is not supported with these
APIs; see [Using `RippleTheme` to globally change all ripples in an
application](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple#globally-change-ripples) for more information on that use case.

For example, the following snippet uses the deprecated APIs:


```kotlin
private object DisabledRippleTheme : RippleTheme {

    @Composable
    override fun defaultColor(): Color = Color.Transparent

    @Composable
    override fun rippleAlpha(): RippleAlpha = RippleAlpha(0f, 0f, 0f, 0f)
}

// ...
    CompositionLocalProvider(LocalRippleTheme provides DisabledRippleTheme) {
        Button {
            // ...
        }
    }
```

<br />

You should modify the above snippet to:


```kotlin
CompositionLocalProvider(LocalRippleConfiguration provides null) {
    Button {
        // ...
    }
}
```

<br />

### Using `RippleTheme` to change the color/alpha of a ripple for a given component

As described in the previous section, `RippleConfiguration` and
`LocalRippleConfiguration` are experimental APIs and are only intended for
per-component customization.

For example, the following snippet uses the deprecated APIs:


```kotlin
private object DisabledRippleThemeColorAndAlpha : RippleTheme {

    @Composable
    override fun defaultColor(): Color = Color.Red

    @Composable
    override fun rippleAlpha(): RippleAlpha = MyRippleAlpha
}

// ...
    CompositionLocalProvider(LocalRippleTheme provides DisabledRippleThemeColorAndAlpha) {
        Button {
            // ...
        }
    }
```

<br />

You should modify the above snippet to:


```kotlin
@OptIn(ExperimentalMaterialApi::class)
private val MyRippleConfiguration =
    RippleConfiguration(color = Color.Red, rippleAlpha = MyRippleAlpha)

// ...
    CompositionLocalProvider(LocalRippleConfiguration provides MyRippleConfiguration) {
        Button {
            // ...
        }
    }
```

<br />

### Using `RippleTheme` to globally change all ripples in an application

Previously, you could use `LocalRippleTheme` to define ripple behavior at a
theme-wide level. This was essentially an integration point between custom
design system composition locals and ripple. Instead of exposing a generic
theming primitive, `material-ripple` now exposes a `createRippleModifierNode()`
function. This function allows for design system libraries to create higher
order `wrapper` implementation, that query their theme values and then delegate
the ripple implementation to the node created by this function.

This allows for design systems to directly query what they need, and expose any
required user-configurable theming layers on top without having to conform to
what is provided at the `material-ripple` layer. This change also makes more
explicit what theme/specification the ripple is conforming to, as it is the
ripple API itself that defines that contract, rather than being implicitly
derived from the theme.

For guidance, see the [ripple API implementation](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Ripple.kt) in Material
libraries, and replace the calls to Material composition locals as needed for
your own design system.

## Migrate from `Indication` to `IndicationNodeFactory`

### Passing around `Indication`

If you are just creating an `Indication` to pass around, such as creating a
ripple to pass to `Modifier.clickable` or `Modifier.indication`, you don't
need to make any changes. `IndicationNodeFactory` inherits from `Indication`,
so everything will continue to compile and work.

### Creating `Indication`

If you are creating your own `Indication` implementation, the migration should
be simple in most cases. For example, consider an `Indication` that applies a
scale effect on press:


```kotlin
object ScaleIndication : Indication {
    @Composable
    override fun rememberUpdatedInstance(interactionSource: InteractionSource): IndicationInstance {
        // key the remember against interactionSource, so if it changes we create a new instance
        val instance = remember(interactionSource) { ScaleIndicationInstance() }

        LaunchedEffect(interactionSource) {
            interactionSource.interactions.collectLatest { interaction ->
                when (interaction) {
                    is PressInteraction.Press -> instance.animateToPressed(interaction.pressPosition)
                    is PressInteraction.Release -> instance.animateToResting()
                    is PressInteraction.Cancel -> instance.animateToResting()
                }
            }
        }

        return instance
    }
}

private class ScaleIndicationInstance : IndicationInstance {
    var currentPressPosition: Offset = Offset.Zero
    val animatedScalePercent = Animatable(1f)

    suspend fun animateToPressed(pressPosition: Offset) {
        currentPressPosition = pressPosition
        animatedScalePercent.animateTo(0.9f, spring())
    }

    suspend fun animateToResting() {
        animatedScalePercent.animateTo(1f, spring())
    }

    override fun ContentDrawScope.drawIndication() {
        scale(
            scale = animatedScalePercent.value,
            pivot = currentPressPosition
        ) {
            this@drawIndication.drawContent()
        }
    }
}
```

<br />

You can migrate this in two steps:

1. Migrate `ScaleIndicationInstance` to be a `DrawModifierNode`. The API surface
   for `DrawModifierNode` is very similar to `IndicationInstance`: it exposes a
   `ContentDrawScope#draw()` function that is functionally equivalent to
   `IndicationInstance#drawContent()`. You need to change that function, and then
   implement the `collectLatest` logic inside the node directly, instead of the
   `Indication`.

   For example, the following snippet uses the deprecated APIs:


   ```kotlin
   private class ScaleIndicationInstance : IndicationInstance {
       var currentPressPosition: Offset = Offset.Zero
       val animatedScalePercent = Animatable(1f)

       suspend fun animateToPressed(pressPosition: Offset) {
           currentPressPosition = pressPosition
           animatedScalePercent.animateTo(0.9f, spring())
       }

       suspend fun animateToResting() {
           animatedScalePercent.animateTo(1f, spring())
       }

       override fun ContentDrawScope.drawIndication() {
           scale(
               scale = animatedScalePercent.value,
               pivot = currentPressPosition
           ) {
               this@drawIndication.drawContent()
           }
       }
   }
   ```

   <br />

   You should modify the above snippet to:


   ```kotlin
   private class ScaleIndicationNode(
       private val interactionSource: InteractionSource
   ) : Modifier.Node(), DrawModifierNode {
       var currentPressPosition: Offset = Offset.Zero
       val animatedScalePercent = Animatable(1f)

       private suspend fun animateToPressed(pressPosition: Offset) {
           currentPressPosition = pressPosition
           animatedScalePercent.animateTo(0.9f, spring())
       }

       private suspend fun animateToResting() {
           animatedScalePercent.animateTo(1f, spring())
       }

       override fun onAttach() {
           coroutineScope.launch {
               interactionSource.interactions.collectLatest { interaction ->
                   when (interaction) {
                       is PressInteraction.Press -> animateToPressed(interaction.pressPosition)
                       is PressInteraction.Release -> animateToResting()
                       is PressInteraction.Cancel -> animateToResting()
                   }
               }
           }
       }

       override fun ContentDrawScope.draw() {
           scale(
               scale = animatedScalePercent.value,
               pivot = currentPressPosition
           ) {
               this@draw.drawContent()
           }
       }
   }
   ```

   <br />

2. Migrate `ScaleIndication` to implement `IndicationNodeFactory`. Because the
   collection logic is now moved into the node, this is a very simple factory
   object whose only responsibility is to create a node instance.

   For example, the following snippet uses the deprecated APIs:


   ```kotlin
   object ScaleIndication : Indication {
       @Composable
       override fun rememberUpdatedInstance(interactionSource: InteractionSource): IndicationInstance {
           // key the remember against interactionSource, so if it changes we create a new instance
           val instance = remember(interactionSource) { ScaleIndicationInstance() }

           LaunchedEffect(interactionSource) {
               interactionSource.interactions.collectLatest { interaction ->
                   when (interaction) {
                       is PressInteraction.Press -> instance.animateToPressed(interaction.pressPosition)
                       is PressInteraction.Release -> instance.animateToResting()
                       is PressInteraction.Cancel -> instance.animateToResting()
                   }
               }
           }

           return instance
       }
   }
   ```

   <br />

   You should modify the above snippet to:


   ```kotlin
   object ScaleIndicationNodeFactory : IndicationNodeFactory {
       override fun create(interactionSource: InteractionSource): DelegatableNode {
           return ScaleIndicationNode(interactionSource)
       }

       override fun hashCode(): Int = -1

       override fun equals(other: Any?) = other === this
   }
   ```

   <br />

### Using `Indication` to create an `IndicationInstance`

In most cases, you should use `Modifier.indication` to display `Indication` for a
component. However, in the rare case that you are manually creating an
`IndicationInstance` using `rememberUpdatedInstance`, you need to update your
implementation to check if the `Indication` is an `IndicationNodeFactory` so you
can use a lighter implementation. For example, `Modifier.indication` will
internally delegate to the created node if it is an `IndicationNodeFactory`. If
not, it will use `Modifier.composed` to call `rememberUpdatedInstance`.