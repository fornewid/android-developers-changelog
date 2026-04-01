---
title: Title chips in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Title chips in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`TitleChip`](/reference/kotlin/androidx/xr/glimmer/TitleChip.composable#TitleChip(androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)) component is designed to
provide brief, non-interactive label for associated content, such as a Card. Use
title chips to display concise information like a short title, a name, or a
status. Since title chips are not focusable or interactive, they serve a purely
informational role within the a Jetpack Compose Glimmer UI. For example, you
might provide a title chip labeled "Ingredients" next to a scrollable list of
ingredients.

![](/static/images/design/ui/glasses/guides/glasses_components_titlechips.png)


**Figure 1.** An example of some different styles of title chips in Jetpack Compose Glimmer.

## Basic example: Display a short title chip

You can create a short title chip with very little code:

```
TitleChip { Text("Messages") }
```

## Detailed example: Display a title chip with a card

To use a title chip with another component, place the title chip
[`TitleChipDefaults.AssociatedContentSpacing`](/reference/kotlin/androidx/xr/glimmer/TitleChipDefaults#AssociatedContentSpacing()) above the other component in
the composable. The following code shows how to use a title chip with a card:

```
@Composable
fun TitleChipExample() {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        TitleChip { Text("Title Chip") }
        Spacer(Modifier.height(TitleChipDefaults.AssociatedContentSpacing))
        Card(
            title = { Text("Title") },
            subtitle = { Text("Subtitle") },
            leadingIcon = { Icon(FavoriteIcon, "Localized description") },
        ) {
            Text("Card Content")
        }
    }
}
```

### Key points about the code

* The [`Spacer`](/reference/kotlin/androidx/compose/foundation/layout/Spacer.composable#Spacer(androidx.compose.ui.Modifier)) has a fixed height to provide the correct vertical
  spacing, defined by [`TitleChipDefaults.AssociatedContentSpacing`](/reference/kotlin/androidx/xr/glimmer/TitleChipDefaults#AssociatedContentSpacing()),
  between the two components.