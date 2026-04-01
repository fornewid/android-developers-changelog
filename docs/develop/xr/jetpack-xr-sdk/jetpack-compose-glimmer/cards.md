---
title: Cards in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Cards in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`Card`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)) component is designed to group and
display related information in a single unit. Cards are highly adaptable,
supporting combinations of main content, optional titles and subtitles, and
leading or trailing icons. Cards fill the maximum full width of the AI glasses
display by default, are focusable, and can also be made clickable.

![](/static/images/design/ui/glasses/guides/glasses_components_cards.png)


**Figure 1.** An example of some different styles of cards in Jetpack Compose Glimmer.

## Card Anatomy and Slots

A Jetpack Compose Glimmer Card is built from several specialized elements,
allowing you to customize its content and layout.

* **Header**: The top section of the card, designed to hold an image.
* **Title and Subtitle**: These text fields provide the main and secondary
  labels for the card.
* **Leading Icon**: An optional icon that appears at the beginning of the
  card's content area.
* **Trailing Icon**: An optional icon that appears at the end of the card's
  content area.
* **Action**: A slot for a primary interactive element, such as a Button. This
  allows users to perform an action directly from the card. The slot is
  available on a separate overload of the Card composable.
* **Main Content**: The core body of the card, where you place the primary
  Text or other content.

## Basic example: Create a basic card

You can create a very basic card with very little code:

```
Card { Text("This is a card") }
```

## Detailed example: Display a complex card

The following code shows how to use multiple slots together to build a card. It
also shows how to pair a [`Card`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)) with a [`TitleChip`](/reference/kotlin/androidx/xr/glimmer/TitleChip.composable#TitleChip(androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)).

```
@Composable
fun SampleGlimmerCard() {
    val myHeaderImage = painterResource(id = R.drawable.header_image)
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        TitleChip { Text("Title Chip") }
        Spacer(Modifier.height(TitleChipDefaults.AssociatedContentSpacing))
        Card(
            action = {
                Button(onClick = {}) {
                    Text("Action Button")
                }
            },
            header = {
                Image(
                    painter = myHeaderImage,
                    contentDescription = "Header image for the card",
                    contentScale = ContentScale.FillWidth
                )
            },
            title = { Text("Card Title") },
            subtitle = { Text("Card Subtitle") },
            leadingIcon = { FavoriteIcon, "Localized description" },
            trailingIcon = { FavoriteIcon, "Localized description" }
        ) {
            Text("A Jetpack Compose Glimmer Card using all available slots")
        }
    }
}
```

### Key points about the code

* Shows how to utilize various card elements, such as [`header`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)),
  [`title`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)), [`subtitle`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)), [`leadingIcon`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)), and [`action`](/reference/kotlin/androidx/xr/glimmer/Card.composable#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0)), to
  customize the card's content and structure.
* Shows an example of how to place a [`TitleChip`](/reference/kotlin/androidx/xr/glimmer/TitleChip.composable#TitleChip(androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)) and use a [`Spacer`](/reference/kotlin/androidx/compose/foundation/layout/Spacer.composable#Spacer(androidx.compose.ui.Modifier)).