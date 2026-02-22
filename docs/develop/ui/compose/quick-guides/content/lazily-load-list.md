---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/lazily-load-list
url: https://developer.android.com/develop/ui/compose/quick-guides/content/lazily-load-list
source: md.txt
---

<br />

With lazy loading and Paging, you can support large lists of items---including an
infinite list---in your app by loading and displaying data incrementally. This
technique enables you to reduce initial load times and optimize memory usage,
enhancing performance.

> [!NOTE]
> **Note:** For optimized performance, use the Paging Library with a lazy list for an infinite list of data.

## Results

The following video shows the resulting behavior of a large list fetching data
as the user scrolls.

<br />

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/lazily-load-list_0b610db00227cbfa044efdcdd2a1ef78a34847e123170046a5dc4c36e932a6f3.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Display paged content

With the Paging library, you can load and display pages of data from a larger
dataset acquired from local storage or over a network. Use the following code to
display a paginated list that shows a progress bar to indicate to the user that
more data is being fetched:


```kotlin
@Composable
fun MessageList(
    modifier: Modifier,
    pager: Pager<Int, Message>
) {
    val lazyPagingItems = pager.flow.collectAsLazyPagingItems()

    LazyColumn {
        items(
            lazyPagingItems.itemCount,
            key = lazyPagingItems.itemKey { it.id }
        ) { index ->
            val message = lazyPagingItems[index]
            if (message != null) {
                MessageRow(message)
            } else {
                MessagePlaceholder()
            }
        }
    }
    @Composable
    fun MessagePlaceholder(modifier: Modifier) {
        Box(
            Modifier
                .fillMaxWidth()
                .height(48.dp)
        ) {
            CircularProgressIndicator()
        }
    }

    @Composable
    fun MessageRow(
        modifier: Modifier,
        message: Message
    ) {
        Card(modifier = Modifier.padding(8.dp)) {
            Column(
                modifier = Modifier.padding(8.dp),
                verticalArrangement = Arrangement.Center
            ) {
                Text(message.sender)
                Text(message.text)
            }
        }
    }
}
```

<br />

### Key points about the code

- [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)): This composable is used to display a large list of items (messages) efficiently. It only renders the items that are visible on the screen, thus saving resources and memory.
- The [`lazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems) object efficiently manages the loading and presentation of paged data within the `LazyColumn`. It passes `LazyPagingItems` to [`items`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) in the `LazyColumn` composable.
- `MessageRow(message: Text)` is responsible for rendering individual message items, likely displaying the sender and text of the message within a Card.
- `MessagePlaceholder()` provides a visual placeholder (a loading spinner) while the actual message data is being fetched, enhancing the user experience.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs, quickly showing you what's available and how to use them. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/compose-basics) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)