---
title: Common shared element use cases  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/shared-elements/common-use-cases
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Common shared element use cases Stay organized with collections Save and categorize content based on your preferences.




When animating shared elements, there are some particular use cases that have
specific recommendations.

## Asynchronous images

It's common to use a library to load up an image asynchronously, such as when
using [Coil's `AsyncImage` composable](https://coil-kt.github.io/coil/compose/).
For it to work seamlessly between two composables, its recommended to set the
`placeholderMemoryCacheKey()` and `memoryCacheKey()` to the same key as a string
derived from the shared element key, such that the cache key is the same for the
matched shared elements. The new shared element will be using its match's cache
as the placeholder until it loads the new image.

The typical usage for `AsyncImage` is as follows:

```
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data("your-image-url")
        .crossfade(true)
        .placeholderMemoryCacheKey("image-key") //  same key as shared element key
        .memoryCacheKey("image-key") // same key as shared element key
        .build(),
    placeholder = null,
    contentDescription = null,
    modifier = Modifier
        .size(120.dp)
        .sharedBounds(
            rememberSharedContentState(
                key = "image-key"
            ),
            animatedVisibilityScope = this
        )
)

SharedElementCommonUseCaseSnippets.kt
```

## Text

To animate `fontSize` changes, use `Modifier.sharedBounds()`, `resizeMode =
ScaleToBounds()`. This transition makes the size
change relatively fluid. The `contentScale` parameter can be tweaked to animate
a specific font weight or style.

```
Text(
    text = "This is an example of how to share text",
    modifier = Modifier
        .wrapContentWidth()
        .sharedBounds(
            rememberSharedContentState(
                key = "shared Text"
            ),
            animatedVisibilityScope = this,
            enter = fadeIn(),
            exit = fadeOut(),
            resizeMode = SharedTransitionScope.ResizeMode.scaleToBounds()
        )
)

SharedElementCommonUseCaseSnippets.kt
```

`TextAlign` changes are **not** animated by default. Instead, use
`Modifier.wrapContentSize()` or `Modifier.wrapContentWidth()` over using different
`TextAlign` for shared transitions.

[Previous

arrow\_back

Customize](/develop/ui/compose/animation/shared-elements/customize)

[Next

With navigation

arrow\_forward](/develop/ui/compose/animation/shared-elements/navigation)