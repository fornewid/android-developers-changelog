---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-compositefilter
url: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-compositefilter
source: md.txt
---

# Composite DeepLinkMatcher.Filter Recipe

This recipe demonstrates how to combine multiple `DeepLinkMatcher.Filter` instances using infix functions (`and`, `or`) to create composite filtering logic in Navigation 3.

## How it works

`DeepLinkMatcher` natively evaluates a list of filters using implicit logical AND (`filters.all { it.filterRequest(request) }`). By defining infix operator functions (`and`, `or`), developers can construct flexible boolean expressions combining intent actions, MIME types, or custom criteria.

This recipe consists of two activities:

- `CompositeFilterDeepLinkActivity`: An interactive playground allowing you to configure the intent's action and MIME type, preview whether the composite filter will match, and launch the deep link request.
- `MainActivity`: Constructs a `DeepLinkRequest(intent)`, matches it using a `UriDeepLinkMatcher` configured with a composite filter (`actionFilter(ACTION_VIEW) and (mimeTypeFilter("image/png") or mimeTypeFilter("image/jpeg"))`), and navigates to either `ViewerKey` or `FallbackKey`.

## Key Concepts

1. **Infix `and` Operator**:
   Combines two filters using logical AND with short-circuiting:

       infix fun Filter.and(other: Filter): Filter = Filter { request ->
           filterRequest(request) && other.filterRequest(request)
       }

2. **Infix `or` Operator**:
   Combines two filters using logical OR with short-circuiting:

       infix fun Filter.or(other: Filter): Filter = Filter { request ->
           filterRequest(request) || other.filterRequest(request)
       }

3. **Operator `!` (NOT)**:
   Inverts the result of a filter using logical NOT:

       operator fun Filter.not(): Filter = Filter { request ->
           !filterRequest(request)
       }

4. **Composite Filter Expressions**:
   Operators allow expressive and readable composition:

       val imageMimeTypeFilter = DeepLinkMatcher.mimeTypeFilter("image/png") or
           DeepLinkMatcher.mimeTypeFilter("image/jpeg")
       val compositeFilter = DeepLinkMatcher.actionFilter(Intent.ACTION_VIEW) and
           imageMimeTypeFilter and !DeepLinkMatcher.mimeTypeFilter("application/pdf")

       val matcher = UriDeepLinkMatcher(
           uriPattern = VIEWER_URI_PATTERN.toUri(),
           serializer = serializer<ViewerKey>(),
           filters = listOf(compositeFilter)
       )

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/deeplink/usecases/filter)

```
package com.example.nav3recipes.deeplink.usecases.filter

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import androidx.core.net.toUri
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.common.deeplink.EntryScreen
import com.example.nav3recipes.common.deeplink.PaddedButton
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable

private const val DEMO_URI = "https://www.nav3recipes.com/viewer?title=SamplePhoto"

@Serializable
private data object FilterHomeKey : NavKey

class CompositeFilterDeepLinkActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {
            EntryScreen {
                val backStack = rememberNavBackStack(FilterHomeKey)
                NavDisplay(
                    backStack = backStack,
                    onBack = { backStack.removeLastOrNull() },
                    entryProvider = entryProvider {
                        entry<FilterHomeKey> {
                            CompositeFilterScreen(
                                onLaunch = { action, mimeType ->
                                    val uri = DEMO_URI.toUri()
                                    val intent = Intent(
                                        this@CompositeFilterDeepLinkActivity,
                                        MainActivity::class.java
                                    ).apply {
                                        this.action = action
                                        if (mimeType != null) {
                                            setDataAndType(uri, mimeType)
                                        } else {
                                            data = uri
                                        }
                                    }
                                    startActivity(intent)
                                }
                            )
                        }
                    }
                )
            }
        }
    }
}

@Composable
private fun CompositeFilterScreen(onLaunch: (action: String, mimeType: String?) -> Unit) {
    var selectedAction by remember { mutableStateOf(Intent.ACTION_VIEW) }
    var selectedMimeType by remember { mutableStateOf<String?>("image/png") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 24.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Card(
            modifier = Modifier.fillMaxWidth(),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surfaceVariant
            )
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Composite Filter Rule:",
                    style = MaterialTheme.typography.labelMedium,
                    fontWeight = FontWeight.Bold
                )
                Spacer(modifier = Modifier.height(4.dp))
                val ruleText = buildAnnotatedString {
                    append("ACTION_VIEW ")
                    withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
                        append("AND")
                    }
                    append(" (image/png ")
                    withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
                        append("OR")
                    }
                    append(" image/jpeg)")
                }
                Text(
                    text = ruleText,
                    style = MaterialTheme.typography.bodyMedium
                )
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        Text("Intent Action:", style = MaterialTheme.typography.labelLarge)
        Spacer(modifier = Modifier.height(4.dp))
        FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            listOf(
                Intent.ACTION_VIEW to "ACTION_VIEW",
                Intent.ACTION_SEND to "ACTION_SEND"
            ).forEach { (action, label) ->
                FilterChip(
                    selected = selectedAction == action,
                    onClick = { selectedAction = action },
                    label = { Text(label) }
                )
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        Text("MIME Type:", style = MaterialTheme.typography.labelLarge)
        Spacer(modifier = Modifier.height(4.dp))
        FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            listOf(
                "image/png" to "PNG",
                "image/jpeg" to "JPEG",
                "application/pdf" to "PDF",
                null to "None"
            ).forEach { (mime, label) ->
                FilterChip(
                    selected = selectedMimeType == mime,
                    onClick = { selectedMimeType = mime },
                    label = { Text(label) }
                )
            }
        }

        Spacer(modifier = Modifier.height(24.dp))

        val willMatch = selectedAction == Intent.ACTION_VIEW &&
            (selectedMimeType == "image/png" || selectedMimeType == "image/jpeg")

        Text(
            text = if (willMatch) "Result: Will Match (Viewer)" else "Result: Will Fail (Fallback)",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.Bold,
            color = if (willMatch) Color(0xFF2E7D32) else Color(0xFFC62828)
        )

        Spacer(modifier = Modifier.height(16.dp))

        PaddedButton(
            text = "Test Deep Link",
            onClick = dropUnlessResumed { onLaunch(selectedAction, selectedMimeType) }
        )
    }
}
```

```
package com.example.nav3recipes.deeplink.usecases.filter

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.net.toUri
import androidx.navigation3.runtime.NavBackStack
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.deeplink.DeepLinkMatcher
import androidx.navigation3.runtime.deeplink.DeepLinkRequest
import androidx.navigation3.runtime.deeplink.UriDeepLinkMatcher
import androidx.navigation3.runtime.deeplink.actionFilter
import androidx.navigation3.runtime.deeplink.invoke
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.common.deeplink.EntryScreen
import com.example.nav3recipes.common.deeplink.TextContent
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable
import kotlinx.serialization.serializer

internal const val VIEWER_URI_PATTERN = "https://www.nav3recipes.com/viewer?title={title}"

@Serializable
internal data class ViewerKey(val title: String) : NavKey

@Serializable
internal data object FallbackKey : NavKey

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        val request = DeepLinkRequest(intent)
        val compositeFilter =
            DeepLinkMatcher.actionFilter(Intent.ACTION_VIEW) and
                    (DeepLinkMatcher.mimeTypeFilter("image/png") or
                            DeepLinkMatcher.mimeTypeFilter("image/jpeg"))
        val deepLinkMatcher = UriDeepLinkMatcher(
            VIEWER_URI_PATTERN.toUri(),
            serializer<ViewerKey>(),
            filters = listOf(compositeFilter)
        )

        val matchResult = deepLinkMatcher.match(request)
        val key = matchResult?.key ?: FallbackKey

        setContent {
            val backStack: NavBackStack<NavKey> = rememberNavBackStack(key)
            NavDisplay(
                backStack = backStack,
                onBack = backStack::removeLastOrNull,
                entryProvider = entryProvider {
                    entry<ViewerKey> { key ->
                        EntryScreen("Viewer") {
                            TextContent(
                                "Matched composite filter!\n\n" +
                                    "Title: ${key.title}\n" +
                                    "Action: ${intent.action}\n" +
                                    "MIME Type: ${intent.type}"
                            )
                        }
                    }
                    entry<FallbackKey> {
                        EntryScreen("Fallback Key") {
                            TextContent(
                                "Failed to deep link - Request did not satisfy composite filter!\n\n" +
                                    "Required Filter:\n" +
                                    "ACTION_VIEW and (image/png or image/jpeg)\n\n" +
                                    "Received:\n" +
                                    "Action: ${intent.action ?: "none"}\n" +
                                    "MIME Type: ${intent.type ?: "none"}"
                            )
                        }
                    }
                }
            )
        }
    }
}
```

````
package com.example.nav3recipes.deeplink.usecases.filter

import androidx.navigation3.runtime.deeplink.DeepLinkMatcher.Filter

/**
 * Combines this [Filter] with [other] using logical AND.
 *
 * Short-circuits evaluation if this filter returns `false`.
 *
 * **Example:**
 * ```kotlin
 * val compositeFilter = actionFilter(Intent.ACTION_VIEW) and mimeTypeFilter("image/png")
 * ```
 */
infix fun Filter.and(other: Filter): Filter = Filter { request ->
    filterRequest(request) && other.filterRequest(request)
}

/**
 * Combines this [Filter] with [other] using logical OR.
 *
 * Short-circuits evaluation if this filter returns `true`.
 *
 * **Example:**
 * ```kotlin
 * val imageFilter = mimeTypeFilter("image/png") or mimeTypeFilter("image/jpeg")
 * ```
 */
infix fun Filter.or(other: Filter): Filter = Filter { request ->
    filterRequest(request) || other.filterRequest(request)
}

/**
 * Inverts the result of this [Filter] using logical NOT.
 *
 * **Example:**
 * ```kotlin
 * val nonPdfFilter = !mimeTypeFilter("application/pdf")
 * ```
 */
operator fun Filter.not(): Filter = Filter { request ->
    !filterRequest(request)
}

````