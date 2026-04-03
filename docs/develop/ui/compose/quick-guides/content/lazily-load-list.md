---
title: Lazily load data with lists and Paging  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/lazily-load-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Lazily load data with lists and Paging Stay organized with collections Save and categorize content based on your preferences.



With lazy loading and Paging, you can support large lists of items—including an
infinite list—in your app by loading and displaying data incrementally. This
technique enables you to reduce initial load times and optimize memory usage,
enhancing performance.

**Note:** For optimized performance, use the Paging Library with a lazy list for an
infinite list of data.

## Results

The following video shows the resulting behavior of a large list fetching data
as the user scrolls.

[](/static/develop/ui/compose/quick-guides/content/lazy-loading.mp4)

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Display paged content

With the Paging library, you can load and display pages of data from a larger
dataset acquired from local storage or over a network. Use the following code to
display a paginated list that shows a progress bar to indicate to the user that
more data is being fetched:

```
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

LazyListSnippets.kt
```

### Key points about the code

* [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable): This composable is used to display a large list of items
  (messages) efficiently. It only renders the items that are visible on
  the screen, thus saving resources and memory.
* The [`lazyPagingItems`](/reference/kotlin/androidx/paging/compose/LazyPagingItems) object efficiently manages the loading and presentation of
  paged data within the `LazyColumn`. It passes `LazyPagingItems` to [`items`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) in the
  `LazyColumn` composable.
* `MessageRow(message: Text)` is responsible for rendering individual message
  items, likely displaying the sender and text of the message within a Card.
* `MessagePlaceholder()` provides a visual placeholder (a loading spinner) while
  the actual message data is being fetched, enhancing the user experience.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a
visually pleasing form that's easy for users to consume.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs,
quickly showing you what’s available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)