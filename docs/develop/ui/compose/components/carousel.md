---
title: https://developer.android.com/develop/ui/compose/components/carousel
url: https://developer.android.com/develop/ui/compose/components/carousel
source: md.txt
---

A carousel displays a scrollable list of items that adapt dynamically based on
window size. Use carousels to showcase a collection of related content.
Carousel items emphasize visuals, but can also contain brief text that adapts to
the item size.

There are four carousel layouts available to suit different use cases:

- **Multi-browse**: Includes differently sized items. Recommended for browsing many items at once, like photos.
- **Uncontained**: Contains items that are a single size and flow past the edge of the screen. Can be customized to show more text or other UI above or below each item.
- **Hero**: Highlights one large image to focus on and provides a peek of what's next with a small item. Recommended for spotlighting content that you want to emphasize, like movie or show thumbnails.
- **Full-screen**: Shows one edge-to-edge large item at a time and scrolls vertically. Recommended for content that is taller than it is wide.

![An uncontained and full-screen carousel type shown next to each other. The uncontained carousel type has multiple carousel items, while full-screen has one item taking up the screen](https://developer.android.com/static/develop/ui/compose/images/components/carousel-uncontained-and-full-screen.png) **Figure 1.** Uncontained (1) and full-screen (2) carousel types.

This page shows you how to implement the multi-browse and uncontained carousel
layouts. See the [Carousel Material 3 guidelines](https://m3.material.io/components/carousel/overview) for
more information about the layout types.

## API surface

To implement multi-browse and uncontained carousels, use the
[`HorizontalMultiBrowseCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalMultiBrowseCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) and [`HorizontalUncontainedCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalUncontainedCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2))
composables. These composables share the following key parameters:

- `state`: A `CarouselState` instance that manages the current item index and scroll position. Create this state using `rememberCarouselState { itemCount }`, where `itemCount` is the total number of items in the carousel.
- `itemSpacing`: Defines the amount of empty space between adjacent items in the carousel.
- `contentPadding`: Applies padding around the content area of the carousel. Use this to add space before the first item or after the last item, or to provide margins for the items within the scrollable region.
- `content`: A composable function that receives an integer index. Use this lambda to define the UI for each item in the carousel based on its index.

These composables differ in how they specify item sizing:

- `itemWidth` (for `HorizontalUncontainedCarousel`): Specifies the exact width for each item in an uncontained carousel.
- `preferredItemWidth` (for `HorizontalMultiBrowseCarousel`): Suggests the ideal width for items in a multi-browse carousel, letting the component display multiple items if space permits.

## Example: Multi-browse carousel

This snippet implements a multi-browse carousel:


```kotlin
@Composable
fun CarouselExample_MultiBrowse() {
    data class CarouselItem(
        val id: Int,
        @DrawableRes val imageResId: Int,
        val contentDescription: String
    )

    val items = remember {
        listOf(
            CarouselItem(0, R.drawable.cupcake, "cupcake"),
            CarouselItem(1, R.drawable.donut, "donut"),
            CarouselItem(2, R.drawable.eclair, "eclair"),
            CarouselItem(3, R.drawable.froyo, "froyo"),
            CarouselItem(4, R.drawable.gingerbread, "gingerbread"),
        )
    }

    HorizontalMultiBrowseCarousel(
        state = rememberCarouselState { items.count() },
        modifier = Modifier
            .fillMaxWidth()
            .wrapContentHeight()
            .padding(top = 16.dp, bottom = 16.dp),
        preferredItemWidth = 186.dp,
        itemSpacing = 8.dp,
        contentPadding = PaddingValues(horizontal = 16.dp)
    ) { i ->
        val item = items[i]
        Image(
            modifier = Modifier
                .height(205.dp)
                .maskClip(MaterialTheme.shapes.extraLarge),
            painter = painterResource(id = item.imageResId),
            contentDescription = item.contentDescription,
            contentScale = ContentScale.Crop
        )
    }
}
```

<br />

### Key points about the code

- Defines a `CarouselItem` data class, which structures the data for each element in the carousel.
- Creates and remembers a `List` of `CarouselItem` objects that are populated with image resources and descriptions.
- Uses the `HorizontalMultiBrowseCarousel` composable, which is designed for displaying multiple items in a carousel.
  - The carousel's state is initialized using `rememberCarouselState`, which is given the total count of items.
  - Items have a `preferredItemWidth` (here, `186.dp`), which suggests an optimal width for each item. The carousel uses this to determine how many items can fit on the screen at once.
  - The `itemSpacing` parameter adds a small gap between items.
  - The trailing lambda of `HorizontalMultiBrowseCarousel` iterates through the `CarouselItems`. In each iteration, it retrieves the item at index `i` and renders an `Image` composable for it.
  - `Modifier.maskClip(MaterialTheme.shapes.extraLarge)` applies a predefined shape mask to each image, giving it rounded corners.
  - `contentDescription` provides an accessibility description for the image.

### Result

The following image shows the result from the preceding snippet:
![A multi-browse carousel with 3 images, two of which are fully shown and one which is partially offscreen.](https://developer.android.com/static/develop/ui/compose/images/components/carousel-multibrowse.png) **Figure 2.** A multi-browse carousel, with the last item clipped.

## Example: Uncontained carousel

The following snippet implements an uncontained carousel:


```kotlin
@Composable
fun CarouselExample() {
    data class CarouselItem(
        val id: Int,
        @DrawableRes val imageResId: Int,
        val contentDescription: String
    )

    val carouselItems = remember {
        listOf(
            CarouselItem(0, R.drawable.cupcake, "cupcake"),
            CarouselItem(1, R.drawable.donut, "donut"),
            CarouselItem(2, R.drawable.eclair, "eclair"),
            CarouselItem(3, R.drawable.froyo, "froyo"),
            CarouselItem(4, R.drawable.gingerbread, "gingerbread"),
        )
    }

    HorizontalUncontainedCarousel(
        state = rememberCarouselState { carouselItems.count() },
        modifier = Modifier
            .fillMaxWidth()
            .wrapContentHeight()
            .padding(top = 16.dp, bottom = 16.dp),
        itemWidth = 186.dp,
        itemSpacing = 8.dp,
        contentPadding = PaddingValues(horizontal = 16.dp)
    ) { i ->
        val item = carouselItems[i]
        Image(
            modifier = Modifier
                .height(205.dp)
                .maskClip(MaterialTheme.shapes.extraLarge),
            painter = painterResource(id = item.imageResId),
            contentDescription = item.contentDescription,
            contentScale = ContentScale.Crop
        )
    }
}
```

<br />

### Key points about the code

- The `HorizontalUncontainedCarousel` composable creates the carousel layout.
  - The `itemWidth` parameter sets a fixed width for each item in the carousel.

### Result

The following image shows the result from the preceding snippet:
![An uncontained carousel with 3 items. The last item is partially visible, but not clipped.](https://developer.android.com/static/develop/ui/compose/images/components/carousel-uncontained.png) **Figure 3.** An uncontained carousel, where the last item in the carousel is not clipped.