---
title: https://developer.android.com/develop/ui/compose/animation/shared-elements
url: https://developer.android.com/develop/ui/compose/animation/shared-elements
source: md.txt
---

[Video](https://www.youtube.com/watch?v=PR6rz1QUkAM)

Shared element transitions are a seamless way to transition between composables
that have content that is consistent between them. They are often used for
navigation, allowing you to visually connect different screens as a user
navigates between them.

For example, in the following video, you can see the image and title of the
snack are shared from the listing page, to the detail page.
**Figure 1.** Jetsnack shared element demo.

In Compose, there are a few high level APIs that help you create shared
elements:

- [`SharedTransitionLayout`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#SharedTransitionLayout(androidx.compose.ui.Modifier,kotlin.Function1)): The outermost layout required to implement shared element transitions. It provides a `SharedTransitionScope`. Composables need to be in a `SharedTransitionScope` to use the shared element modifiers.
- [`Modifier.sharedElement()`](https://developer.android.com/develop/ui/compose/animation/shared-elements#basic-usage): The modifier that flags to the `SharedTransitionScope` the composable that should be matched with another composable.
- [`Modifier.sharedBounds()`](https://developer.android.com/develop/ui/compose/animation/shared-elements#shared-bounds): The modifier that flags to the `SharedTransitionScope` that this composable's bounds should be used as the container bounds for where the transition should take place. In contrast to `sharedElement()`, `sharedBounds()` is designed for visually different content.

An important concept when creating shared elements in Compose is how they work
with overlays and clipping. See [the clipping and
overlays](https://developer.android.com/develop/ui/compose/animation/shared-elements/customize#clip-overlays)
section to learn more about this important topic.

## Basic usage

The following transition will be built in this section, transitioning from the
smaller "list" item, to the larger detailed item:
![](https://developer.android.com/static/develop/ui/compose/images/animations/shared-element/basic_shared_element_jetsnack.gif) **Figure 2.** Basic example of a shared element transition between two composables.

The best way to use `Modifier.sharedElement()` is in conjunction with
`AnimatedContent`, [`AnimatedVisibility`](https://developer.android.com/develop/ui/compose/animation/shared-elements#animated-visibility), or [`NavHost`](https://developer.android.com/develop/ui/compose/animation/shared-elements/navigation), as this manages
the transition between composables automatically for you.

The starting point is an existing basic `AnimatedContent` that has a
`MainContent`, and `DetailsContent` composable before adding shared elements:
![](https://developer.android.com/static/develop/ui/compose/images/animations/shared-element/basic_no_animation_jetsnack.gif) **Figure 3.** Starting `AnimatedContent` without any shared element transitions.

<br />

1. To make the shared elements animate between the two layouts,
   surround the `AnimatedContent` composable with `SharedTransitionLayout`. The
   scopes from [`SharedTransitionLayout`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#SharedTransitionLayout(androidx.compose.ui.Modifier,kotlin.Function1)) and `AnimatedContent` are passed
   to the `MainContent` and `DetailsContent`:


   ```kotlin
   var showDetails by remember {
       mutableStateOf(false)
   }
   SharedTransitionLayout {
       AnimatedContent(
           showDetails,
           label = "basic_transition"
       ) { targetState ->
           if (!targetState) {
               MainContent(
                   onShowDetails = {
                       showDetails = true
                   },
                   animatedVisibilityScope = this@AnimatedContent,
                   sharedTransitionScope = this@SharedTransitionLayout
               )
           } else {
               DetailsContent(
                   onBack = {
                       showDetails = false
                   },
                   animatedVisibilityScope = this@AnimatedContent,
                   sharedTransitionScope = this@SharedTransitionLayout
               )
           }
       }
   }
   ```

   <br />

2. Add [`Modifier.sharedElement()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope#(androidx.compose.ui.Modifier).sharedElement(androidx.compose.animation.SharedTransitionScope.SharedContentState,androidx.compose.animation.AnimatedVisibilityScope,androidx.compose.animation.BoundsTransform,androidx.compose.animation.SharedTransitionScope.PlaceHolderSize,kotlin.Boolean,kotlin.Float,androidx.compose.animation.SharedTransitionScope.OverlayClip)) to your composable modifier chain on the
   two composables that match. Create a `SharedContentState` object and
   remember it with [`rememberSharedContentState()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope#rememberSharedContentState(kotlin.Any)). The
   `SharedContentState` object is storing the unique key which determines the
   elements that are shared. Provide a unique key to identify the content, and
   use `rememberSharedContentState()` for the item to be remembered. The
   `AnimatedContentScope` is passed into the modifier, which is used to
   coordinate the animation.


   ```kotlin
   @Composable
   private fun MainContent(
       onShowDetails: () -> Unit,
       modifier: Modifier = Modifier,
       sharedTransitionScope: SharedTransitionScope,
       animatedVisibilityScope: AnimatedVisibilityScope
   ) {
       Row(
           // ...
       ) {
           with(sharedTransitionScope) {
               Image(
                   painter = painterResource(id = R.drawable.cupcake),
                   contentDescription = "Cupcake",
                   modifier = Modifier
                       .sharedElement(
                           rememberSharedContentState(key = "image"),
                           animatedVisibilityScope = animatedVisibilityScope
                       )
                       .size(100.dp)
                       .clip(CircleShape),
                   contentScale = ContentScale.Crop
               )
               // ...
           }
       }
   }

   @Composable
   private fun DetailsContent(
       modifier: Modifier = Modifier,
       onBack: () -> Unit,
       sharedTransitionScope: SharedTransitionScope,
       animatedVisibilityScope: AnimatedVisibilityScope
   ) {
       Column(
           // ...
       ) {
           with(sharedTransitionScope) {
               Image(
                   painter = painterResource(id = R.drawable.cupcake),
                   contentDescription = "Cupcake",
                   modifier = Modifier
                       .sharedElement(
                           rememberSharedContentState(key = "image"),
                           animatedVisibilityScope = animatedVisibilityScope
                       )
                       .size(200.dp)
                       .clip(CircleShape),
                   contentScale = ContentScale.Crop
               )
               // ...
           }
       }
   }
   ```

   <br />

To get information on if a shared element match has occurred, extract
`rememberSharedContentState()` into a variable, and query `isMatchFound`.

> [!IMPORTANT]
> **Important:** The [order of where this modifier](https://developer.android.com/develop/ui/compose/animation/shared-elements#modifier-ordering) is placed in the modifier chain is important. Put anything **you don't want to
> be shared before** the **`sharedElement()`** in the modifier chain.

This results in the following automatic animation:
![](https://developer.android.com/static/develop/ui/compose/images/animations/shared-element/basic_shared_element_jetsnack.gif) **Figure 4.** Basic example of a shared element transition between two composables.

You may notice that the background color and size of the whole container still
uses the default `AnimatedContent` settings.

## Shared bounds versus shared element

[`Modifier.sharedBounds()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope#(androidx.compose.ui.Modifier).sharedBounds(androidx.compose.animation.SharedTransitionScope.SharedContentState,androidx.compose.animation.AnimatedVisibilityScope,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,androidx.compose.animation.BoundsTransform,androidx.compose.animation.SharedTransitionScope.PlaceHolderSize,kotlin.Boolean,kotlin.Float,androidx.compose.animation.SharedTransitionScope.OverlayClip)) is similar to `Modifier.sharedElement()`.
However, the modifiers are different in the following ways:

- `sharedBounds()` is for content that is visually different but should share the same area between states, whereas `sharedElement()` expects the content to be the same.
- With `sharedBounds()`, the content entering and exiting the screen is visible during the transition between the two states, whereas with `sharedElement()` only the target content is rendered in the transforming bounds. `Modifier.sharedBounds()` has `enter` and `exit` parameters for specifying how the content should transition, similar to how `AnimatedContent` works.
- The most common use case for `sharedBounds()` is the [container transform
  pattern](https://m3.material.io/styles/motion/transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187), whereas for `sharedElement()` the example use case is a hero transition.
- When using `Text` composables, `sharedBounds()` is preferred to support font changes such as transitioning between italic and bold or color changes.

From the previous example, adding `Modifier.sharedBounds()` onto the `Row` and
`Column` in the two different scenarios will allow us to share the bounds of the
two and perform the transition animation, allowing them to grow
between each other:


```kotlin
@Composable
private fun MainContent(
    onShowDetails: () -> Unit,
    modifier: Modifier = Modifier,
    sharedTransitionScope: SharedTransitionScope,
    animatedVisibilityScope: AnimatedVisibilityScope
) {
    with(sharedTransitionScope) {
        Row(
            modifier = Modifier
                .padding(8.dp)
                .sharedBounds(
                    rememberSharedContentState(key = "bounds"),
                    animatedVisibilityScope = animatedVisibilityScope,
                    enter = fadeIn(),
                    exit = fadeOut(),
                    resizeMode = SharedTransitionScope.ResizeMode.scaleToBounds()
                )
                // ...
        ) {
            // ...
        }
    }
}

@Composable
private fun DetailsContent(
    modifier: Modifier = Modifier,
    onBack: () -> Unit,
    sharedTransitionScope: SharedTransitionScope,
    animatedVisibilityScope: AnimatedVisibilityScope
) {
    with(sharedTransitionScope) {
        Column(
            modifier = Modifier
                .padding(top = 200.dp, start = 16.dp, end = 16.dp)
                .sharedBounds(
                    rememberSharedContentState(key = "bounds"),
                    animatedVisibilityScope = animatedVisibilityScope,
                    enter = fadeIn(),
                    exit = fadeOut(),
                    resizeMode = SharedTransitionScope.ResizeMode.scaleToBounds()
                )
                // ...

        ) {
            // ...
        }
    }
}
```

<br />

**Figure 5.** Shared bounds between two composables.

## Understand scopes

To use `Modifier.sharedElement()`, the composable needs to be in a
`SharedTransitionScope`. The `SharedTransitionLayout` composable provides the
`SharedTransitionScope`. Make sure to place at the same top-level point in your
UI hierarchy that contains the elements you want to share.

Generally, the composables should also be placed inside an
`AnimatedVisibilityScope`. This is typically provided by using `AnimatedContent`
to switch between composables or when using `AnimatedVisibility` directly, or by
the [`NavHost`](https://developer.android.com/develop/ui/compose/animation/shared-elements/navigation) composable function, unless you [manage the visibility
manually](https://developer.android.com/develop/ui/compose/animation/shared-elements#managing-visibility). In order
to use multiple scopes, save your required scopes in a
[`CompositionLocal`](https://developer.android.com/develop/ui/compose/compositionlocal), use [context receivers in Kotlin](https://github.com/Kotlin/KEEP/blob/master/proposals/context-receivers.md), or pass the
scopes as parameters to your functions.

Use `CompositionLocals` in the scenario where you have multiple scopes to keep
track of, or a deeply nested hierarchy. A `CompositionLocal` lets you choose the
exact scopes to save and use. On the other hand, when you use context receivers,
other layouts in your hierarchy might accidentally override the provided scopes.
For example, if you have multiple nested `AnimatedContent`, the scopes could be
overridden.


```kotlin
val LocalNavAnimatedVisibilityScope = compositionLocalOf<AnimatedVisibilityScope?> { null }
val LocalSharedTransitionScope = compositionLocalOf<SharedTransitionScope?> { null }

@Composable
private fun SharedElementScope_CompositionLocal() {
    // An example of how to use composition locals to pass around the shared transition scope, far down your UI tree.
    // ...
    SharedTransitionLayout {
        CompositionLocalProvider(
            LocalSharedTransitionScope provides this
        ) {
            // This could also be your top-level NavHost as this provides an AnimatedContentScope
            AnimatedContent(state, label = "Top level AnimatedContent") { targetState ->
                CompositionLocalProvider(LocalNavAnimatedVisibilityScope provides this) {
                    // Now we can access the scopes in any nested composables as follows:
                    val sharedTransitionScope = LocalSharedTransitionScope.current
                        ?: throw IllegalStateException("No SharedElementScope found")
                    val animatedVisibilityScope = LocalNavAnimatedVisibilityScope.current
                        ?: throw IllegalStateException("No AnimatedVisibility found")
                }
                // ...
            }
        }
    }
}
```

<br />

Alternatively, if your hierarchy isn't deeply nested you can pass the scopes
down as parameters:


```kotlin
@Composable
fun MainContent(
    animatedVisibilityScope: AnimatedVisibilityScope,
    sharedTransitionScope: SharedTransitionScope
) {
}

@Composable
fun Details(
    animatedVisibilityScope: AnimatedVisibilityScope,
    sharedTransitionScope: SharedTransitionScope
) {
}
```

<br />

## Shared elements with `AnimatedVisibility`

Previous examples showed how to use shared elements with `AnimatedContent`, but
shared elements work with `AnimatedVisibility` too.

For example, in this lazy grid example, each element is wrapped in
`AnimatedVisibility`. When the item is clicked on, the content has the
visual effect of being pulled out of the UI into a dialog-like component.


```kotlin
var selectedSnack by remember { mutableStateOf<Snack?>(null) }

SharedTransitionLayout(modifier = Modifier.fillMaxSize()) {
    LazyColumn(
        // ...
    ) {
        items(listSnacks) { snack ->
            AnimatedVisibility(
                visible = snack != selectedSnack,
                enter = fadeIn() + scaleIn(),
                exit = fadeOut() + scaleOut(),
                modifier = Modifier.animateItem()
            ) {
                Box(
                    modifier = Modifier
                        .sharedBounds(
                            sharedContentState = rememberSharedContentState(key = "${snack.name}-bounds"),
                            // Using the scope provided by AnimatedVisibility
                            animatedVisibilityScope = this,
                            clipInOverlayDuringTransition = OverlayClip(shapeForSharedElement)
                        )
                        .background(Color.White, shapeForSharedElement)
                        .clip(shapeForSharedElement)
                ) {
                    SnackContents(
                        snack = snack,
                        modifier = Modifier.sharedElement(
                            sharedContentState = rememberSharedContentState(key = snack.name),
                            animatedVisibilityScope = this@AnimatedVisibility
                        ),
                        onClick = {
                            selectedSnack = snack
                        }
                    )
                }
            }
        }
    }
    // Contains matching AnimatedContent with sharedBounds modifiers.
    SnackEditDetails(
        snack = selectedSnack,
        onConfirmClick = {
            selectedSnack = null
        }
    )
}
```

<br />

**Figure 6.** Shared elements with `AnimatedVisibility`.

## Modifier ordering

With `Modifier.sharedElement()` and `Modifier.sharedBounds()`, the [order of your
modifier](https://developer.android.com/develop/ui/compose/modifiers#order-modifier-matters) chain matters,
as with the rest of Compose. The incorrect placement of size-affecting modifiers
can cause unexpected visual jumps during shared element matching.

For example, if you place a padding modifier in a different position on two
shared elements, there is a visual difference in the animation.


```kotlin
var selectFirst by remember { mutableStateOf(true) }
val key = remember { Any() }
SharedTransitionLayout(
    Modifier
        .fillMaxSize()
        .padding(10.dp)
        .clickable {
            selectFirst = !selectFirst
        }
) {
    AnimatedContent(targetState = selectFirst, label = "AnimatedContent") { targetState ->
        if (targetState) {
            Box(
                Modifier
                    .padding(12.dp)
                    .sharedBounds(
                        rememberSharedContentState(key = key),
                        animatedVisibilityScope = this@AnimatedContent
                    )
                    .border(2.dp, Color.Red)
            ) {
                Text(
                    "Hello",
                    fontSize = 20.sp
                )
            }
        } else {
            Box(
                Modifier
                    .offset(180.dp, 180.dp)
                    .sharedBounds(
                        rememberSharedContentState(
                            key = key,
                        ),
                        animatedVisibilityScope = this@AnimatedContent
                    )
                    .border(2.dp, Color.Red)
                    // This padding is placed after sharedBounds, but it doesn't match the
                    // other shared elements modifier order, resulting in visual jumps
                    .padding(12.dp)

            ) {
                Text(
                    "Hello",
                    fontSize = 36.sp
                )
            }
        }
    }
}
```

<br />

| Matched bounds | Unmatched bounds: Notice how the shared element animation appears a bit off as it needs to resize to the incorrect bounds |
|---|---|
|   |   |

The modifiers used ***before*** the shared element modifiers provide constraints
to the shared element modifiers, which are then used to derive the initial and
target bounds, and subsequently the bounds animation.

The modifiers used ***after*** the shared element modifiers use the constraints
from before to measure and calculate the child's target size. The shared element
modifiers create a series of animated constraints to gradually transform the
child from the initial size to the target size.

The exception to this is if you use `resizeMode = ScaleToBounds()` for
the animation, or `Modifier.skipToLookaheadSize()` on a composable. In this
case, Compose lays out the child using the target constraints, and instead uses
a scale factor to perform the animation instead of changing the layout size
itself.

> [!IMPORTANT]
> **Important:** Be consistent with the order of modifiers on the matching items. Place size modifiers after the shared element modifiers, except when you use `requiredSize()`. If you use `requiredSize()` after shared element modifiers, there will be no relayout of children during the transform, even if you use `ScaleToBounds()`. On the other hand, if `requiredSize()` is before shared element modifiers, the parent of `requiredSize()` can never observe the shared elements `animatedSize`.

## Unique keys

When working with complex shared elements, it is a good practice to create a key
that is not a string, because strings can be error prone to match. Each key must
be unique for matches to occur. For example, in Jetsnack we have the following
shared elements:
![](https://developer.android.com/static/develop/ui/compose/images/animations/shared-element/unique_keys_shared_elements.jpeg) **Figure 7.** Image showing Jetsnack with annotations for each part of the UI.

You could create an enum to represent the shared element type. In this example
the whole snack card can also appear from multiple different places on the home
screen, for example in a "Popular" and a "Recommended" section. You can create a
key that has the `snackId`, the `origin` ("Popular" / "Recommended"), and the
`type` of the shared element that will be shared:


```kotlin
data class SnackSharedElementKey(
    val snackId: Long,
    val origin: String,
    val type: SnackSharedElementType
)

enum class SnackSharedElementType {
    Bounds,
    Image,
    Title,
    Tagline,
    Background
}

@Composable
fun SharedElementUniqueKey() {
    // ...
            Box(
                modifier = Modifier
                    .sharedElement(
                        rememberSharedContentState(
                            key = SnackSharedElementKey(
                                snackId = 1,
                                origin = "latest",
                                type = SnackSharedElementType.Image
                            )
                        ),
                        animatedVisibilityScope = this@AnimatedVisibility
                    )
            )
            // ...
}
```

<br />

Data classes are recommended for keys since they implement `hashCode()` and
`isEquals()`.

> [!IMPORTANT]
> **Important:** When working with lists of content, you need to either append the item number to the key, or use a different unique identifier.

## Manage the visibility of shared elements manually

In cases where you may not be using `AnimatedVisibility` or `AnimatedContent`,
you can manage the shared element visibility yourself. Use
`Modifier.sharedElementWithCallerManagedVisibility()` and provide your own
conditional that determines when an item should be visible or not:


```kotlin
var selectFirst by remember { mutableStateOf(true) }
val key = remember { Any() }
SharedTransitionLayout(
    Modifier
        .fillMaxSize()
        .padding(10.dp)
        .clickable {
            selectFirst = !selectFirst
        }
) {
    Box(
        Modifier
            .sharedElementWithCallerManagedVisibility(
                rememberSharedContentState(key = key),
                !selectFirst
            )
            .background(Color.Red)
            .size(100.dp)
    ) {
        Text(if (!selectFirst) "false" else "true", color = Color.White)
    }
    Box(
        Modifier
            .offset(180.dp, 180.dp)
            .sharedElementWithCallerManagedVisibility(
                rememberSharedContentState(
                    key = key,
                ),
                selectFirst
            )
            .alpha(0.5f)
            .background(Color.Blue)
            .size(180.dp)
    ) {
        Text(if (selectFirst) "false" else "true", color = Color.White)
    }
}
```

<br />

> [!IMPORTANT]
> **Important:** The shared element remains in the UI tree even when `visible ==
> false`. The shared element starts a transition whenever its size or position changes as it has an active match. Therefore it is recommended to remove the shared element with `visible == false` from the tree once the transition is finished, by observing `SharedTransitionScope.isTransitionActive`.

## Current limitations

These APIs have a few limitations. Most notably:

- No interoperability between Views and Compose is supported. This includes any composable that wraps `AndroidView`, such as a `Dialog` or `ModalBottomSheet`.
- There is no automatic animation support for the following:
  - **Shared Image composables** :
    - `ContentScale` is not animated by default. It snaps to the set end `ContentScale`.
  - **Shape clipping** - There is no built-in support for automatic animation between shapes - for example, animating from a square to a circle as the item transitions.
  - For the unsupported cases, use `Modifier.sharedBounds()` instead of `sharedElement()` and add `Modifier.animateEnterExit()` onto the items.