---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/build-list-multiple-item-types
url: https://developer.android.com/develop/ui/compose/quick-guides/content/build-list-multiple-item-types
source: md.txt
---

<br />

You can use a list with multiple item types to display mixed content types such
as text, images, and interactive elements.

## Results

![Code output showing audio and text messages](https://developer.android.com/static/develop/ui/compose/quick-guides/content/multiple-item-types.png) **Figure 1.** Code output showing audio and text messages.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/build-list-multiple-item-types_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Add multiple item types

You can specify the content type for each item of the layout when you compose a
list or a grid with multiple types of items:


```kotlin
@Composable
fun ListWithMultipleItems(messages: List<Any>) {
    LazyColumn {
        items(
            messages.size,
            contentType = { it }
        ) {
            for (message in messages)
                when (message) {
                    is MediaStore.Audio -> AudioMessage(message)
                    is Text -> TextMessage(message)
                }
        }
    }
}

@Composable
fun AudioMessage(message: MediaStore.Audio) {
    TODO("Not yet implemented.")
}

@Composable
fun TextMessage(message: Text) {
    TODO("Not yet implemented.")
}

data class SampleMessage(val text: String, val content: Any)
```

<br />

### Key points about the code

- Specifies the content type for each item by setting [`contentType`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#extension-functions-summary) in [`items()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)).
- Maps each content type to a corresponding composable. For example, `Audio` is a `contentType` that is defined elsewhere and is mapped to an `AudioMessage` composable.
- Compose reuses the rendered composables for each item of a given content type.

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