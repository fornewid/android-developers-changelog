---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-nested-list
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-nested-list
source: md.txt
---

<br />

You can display nested scrolling items within a list to present complex layouts,
such as product catalogs, media galleries, news feeds, and more.

## Results

The following video shows the resulting behaviors of nested horizontal lists
within a vertical scrolling list.

<br />

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-nested-list_d7f56e813ae273a474e3b0cc70d876c83c80af5be2179fb3cca30e39105a8182.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement nested horizontal scrolling in vertical list

The following code produces a list that scrolls two ways. The rows of the list
scroll horizontally; the list as a whole---a single column---scrolls vertically.


```kotlin
@Composable
fun NestedScrollingRowsList(urls: List<String>) {
    LazyColumn {
        items(10) {
            LazyRow {
                item { Text("Row: $it") }
                items(urls.size) { index ->
                    // AsyncImage provided by Coil.
                    AsyncImage(
                        model = urls[index],
                        modifier = Modifier.size(150.dp),
                        contentDescription = null
                    )
                }
            }
        }
    }
}
```

<br />

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