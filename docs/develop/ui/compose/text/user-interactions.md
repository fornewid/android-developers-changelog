---
title: https://developer.android.com/develop/ui/compose/text/user-interactions
url: https://developer.android.com/develop/ui/compose/text/user-interactions
source: md.txt
---

Jetpack Compose enables fine-grained interactivity in `Text`. Text selection is
now more flexible and can be done across composable layouts. User interactions
in text are different from other composable layouts, as you can't add a modifier
to a portion of a `Text` composable. This page highlights the APIs
that enable user interactions.

## Select text

By default, composables aren't selectable, which means that users can't
select and copy text from your app. To enable text selection, wrap
your text elements with a [`SelectionContainer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/selection/package-summary#SelectionContainer(androidx.compose.ui.Modifier,kotlin.Function0)) composable:


```kotlin
@Composable
fun SelectableText() {
    SelectionContainer {
        Text("This text is selectable")
    }
}
```

<br />

![A short passage of text, selected by the user.](https://developer.android.com/static/develop/ui/compose/images/text-selected.png)

You may want to disable selection on specific parts of a selectable area. To do
so, you need to wrap the unselectable part with a [`DisableSelection`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/selection/package-summary#DisableSelection(kotlin.Function0))
composable:


```kotlin
@Composable
fun PartiallySelectableText() {
    SelectionContainer {
        Column {
            Text("This text is selectable")
            Text("This one too")
            Text("This one as well")
            DisableSelection {
                Text("But not this one")
                Text("Neither this one")
            }
            Text("But again, you can select this one")
            Text("And this one too")
        }
    }
}
```

<br />

![A longer passage of text. The user tried to select the whole passage, but since two lines had DisableSelection applied, they were not selected.](https://developer.android.com/static/develop/ui/compose/images/text-partially-selected.png)

## Create clickable sections of text with `LinkAnnotation`

To listen for clicks on `Text`, you can add the [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0))
modifier. However, you may want to attach extra information to a certain part of
the `Text` value, like a URL attached to a certain word to be opened in a
browser. In cases like this, you need to use a [`LinkAnnotation`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/LinkAnnotation), which is
an annotation that represents a clickable part of the text.

With `LinkAnnotation`, you can attach a URL to a part of a `Text` composable
that automatically opens once clicked, as shown in the following snippet:


```kotlin
@Composable
fun AnnotatedStringWithLinkSample() {
    // Display multiple links in the text
    Text(
        buildAnnotatedString {
            append("Go to the ")
            withLink(
                LinkAnnotation.Url(
                    "https://developer.android.com/",
                    TextLinkStyles(style = SpanStyle(color = Color.Blue))
                )
            ) {
                append("Android Developers ")
            }
            append("website, and check out the")
            withLink(
                LinkAnnotation.Url(
                    "https://developer.android.com/jetpack/compose",
                    TextLinkStyles(style = SpanStyle(color = Color.Green))
                )
            ) {
                append("Compose guidance")
            }
            append(".")
        }
    )
}
```

<br />

You can also configure a custom action in response to a user click on a part of
the `Text` composable. In the following snippet, when the user clicks on
"Jetpack Compose," a link is displayed, and metrics are logged if the user
clicks the link:


```kotlin
@Composable
fun AnnotatedStringWithListenerSample() {
    // Display a link in the text and log metrics whenever user clicks on it. In that case we handle
    // the link using openUri method of the LocalUriHandler
    val uriHandler = LocalUriHandler.current
    Text(
        buildAnnotatedString {
            append("Build better apps faster with ")
            val link =
                LinkAnnotation.Url(
                    "https://developer.android.com/jetpack/compose",
                    TextLinkStyles(SpanStyle(color = Color.Blue))
                ) {
                    val url = (it as LinkAnnotation.Url).url
                    // log some metrics
                    uriHandler.openUri(url)
                }
            withLink(link) { append("Jetpack Compose") }
        }
    )
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Semantics in Compose](https://developer.android.com/develop/ui/compose/semantics)
- [Accessibility in Compose](https://developer.android.com/develop/ui/compose/accessibility)
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material)