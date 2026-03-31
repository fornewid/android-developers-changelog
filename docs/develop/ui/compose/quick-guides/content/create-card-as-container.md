---
title: Create a card as a container  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-card-as-container
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a card as a container Stay organized with collections Save and categorize content based on your preferences.



The [`Card`](/reference/kotlin/androidx/compose/material3/Card.composable#Card(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,androidx.compose.foundation.BorderStroke,kotlin.Function1)) composable acts as a Material Design container for your UI.
Cards present a single coherent piece of content, such as:

* A product in a shopping app.
* A news story in a news app.
* A message in a communications app.

The focus on portraying a single piece of content distinguishes
`Card` from other containers. For example, `Scaffold` provides general structure
to a whole screen. Card is a smaller UI element inside a larger
layout, whereas a layout component such as `Column` or `Row` provides a simpler
and more generic API.

This topic shows you how to implement four types of cards:

* [Basic](#basic)
* [Filled](#filled)
* [Elevated](#elevated)
* [Outlined](#outlined)

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a basic card

`Card` behaves much like other containers in Compose. You declare its content by
calling other composables within it. For example, consider how `Card` contains a
call to `Text` in the following minimal example:

**Note:** By default, a `Card` wraps its content in a `Column` composable, placing
each item inside the card beneath one another.

## Create a filled card

The key here is the use of the `colors` property to change the filled
color:

### Results

![A card is filled with the surface variant color from the material theme.](/static/develop/ui/compose/images/components/card-filled.png)


**Figure 1.** Example of a filled card.

## Create an elevated card

The following snippet demonstrates how to implement an elevated card. Use the
dedicated [`ElevatedCard`](/reference/kotlin/androidx/compose/material3/ElevatedCard.composable#ElevatedCard(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,kotlin.Function1)) composable.

You can use the `elevation` property to control the appearance of elevation and
the resulting shadow.

### Results

![A card is elevated above the background of the app, with a shadow.](/static/develop/ui/compose/images/components/card-elevated.png)


**Figure 2.** Example of an elevated card.

## Create an outlined card

The following is an example of an outlined card. Use the dedicated
[`OutlinedCard`](/reference/kotlin/androidx/compose/material3/OutlinedCard.composable#OutlinedCard(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,androidx.compose.foundation.BorderStroke,kotlin.Function1)) composable.

### Results

![A card is outlined with a thin black border.](/static/develop/ui/compose/images/components/card-outlined.png)


**Figure 3.** Example of an outlined card.

## Key points

See the [reference](/reference/kotlin/androidx/compose/material3/Card.composable#Card(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,androidx.compose.foundation.BorderStroke,kotlin.Function1)) for the API definition of `Card`. It defines several
parameters that you can use to customize the appearance and behavior of the
component.

Some key parameters include:

* **`elevation`**: Adds a shadow to the component that makes it look
  elevated above the background.
* **`colors`**: Uses the `CardColors` type to set the default color of both
  the container and any children.
* **`enabled`**: If you pass `false` for this parameter, the card appears as
  disabled and does not respond to user input.
* **`onClick`**: Ordinarily, a `Card` does not accept click events. As such,
  the primary overload you would like to note is that which defines an
  `onClick` parameter. Use this overload when you want your
  implementation of `Card` to respond to clicks from the user.

**Beta:** The `Card` overload that defines the `onClick` parameter is experimental.

Cards don't come with inherent scroll or dismiss actions, but can integrate into
composables offering these features. For example, to implement swipe to dismiss
on a card, integrate it with the [`SwipeToDismiss`](/reference/kotlin/androidx/compose/material3/SwipeToDismiss.composable) composable. To integrate
with scroll, use scroll modifiers such as [`verticalScroll`](/reference/kotlin/androidx/compose/foundation/verticalScroll.modifier#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)). See the [`Scroll`
documentation](/develop/ui/compose/touch-input/pointer-input/scroll) for more information.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)