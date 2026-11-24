---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-deeplinkkey
url: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-deeplinkkey
source: md.txt
---

> Documentation index: https://developer.android.com/guide/navigation/navigation-3/llms.txt

# DeepLinkKey Recipe

This recipe demonstrates how to associate deep link URI pattern templates with navigation keys using a `DeepLinkKey` interface in Navigation 3.

## How it works

This recipe consists of two activities:

- `DeepLinkKeyActivity`: A sandbox UI that allows testing deep links for different destinations (`HomeKey`, `UserKey`, `ProductKey`) by constructing URI strings and launching `MainActivity`.
- `MainActivity`: Constructs a `DeepLinkRequest(intent)`, matches it against a list of `UriDeepLinkMatcher`s created from each key's `uriPattern`, and displays the matched destination in `NavDisplay`.

## Key Concepts

1. **`DeepLinkKey` Interface**:
   Associates a navigation key with its supported URI pattern:

   - For singleton destinations (`HomeKey`), the object implements both `DeepLinkKey` and `NavKey`.
   - For parameterized destinations (`UserKey`), the companion object implements `DeepLinkKey`.

   ```kotlin
   interface DeepLinkKey {
       val uriPattern: String
   }

   @Serializable
   data object HomeKey : DeepLinkKey, NavKey {
       override val uriPattern: String = "https://www.nav3recipes.com/home"
   }

   @Serializable
   data class UserKey(val id: Int) : NavKey {
       companion object : DeepLinkKey {
           override val uriPattern: String = "https://www.nav3recipes.com/user/{id}"
       }
   }
   ```
2. **`UriDeepLinkMatcher` Registration** :
   `UriDeepLinkMatcher` instances are created using `Key.uriPattern` and `serializer<T>()`:

   ```kotlin
   private val deepLinkMatchers = listOf(
       UriDeepLinkMatcher(HomeKey.uriPattern.toUri(), serializer<HomeKey>()),
       UriDeepLinkMatcher(UserKey.uriPattern.toUri(), serializer<UserKey>()),
       UriDeepLinkMatcher(ProductKey.uriPattern.toUri(), serializer<ProductKey>()),
   )
   ```
3. **`bestMatch` Resolution** :
   Matches are evaluated using `matches.maxOrNull()`, which selects the most specific match based on exact path segments, query parameters, and scheme/host.

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/deeplink/usecases/deeplinkkey)

```
package com.example.nav3recipes.deeplink.usecases.deeplinkkey

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.core.net.toUri
import androidx.lifecycle.compose.dropUnlessResumed
import com.example.nav3recipes.common.deeplink.EntryScreen
import com.example.nav3recipes.common.deeplink.TextContent
import com.example.nav3recipes.ui.setEdgeToEdgeConfig

/**
 * Activity presenting a UI sandbox to test [DeepLinkKey] deep links.
 */
class DeepLinkKeyActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {
            EntryScreen("DeepLinkKey Sandbox") {
                Column(
                    verticalArrangement = Arrangement.spacedBy(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                ) {
                    var userIdText by remember { mutableStateOf("42") }
                    var categoryText by remember { mutableStateOf("electronics") }
                    var productIdText by remember { mutableStateOf("laptop-101") }

                    TextContent("Test launching deep links defined by DeepLinkKey implementations:")

                    // 1. Home Key Deep Link
                    ElevatedButton(
                        onClick = dropUnlessResumed {
                            launchDeepLink(HomeKey.uriPattern)
                        }
                    ) {
                        Text("Launch Home DeepLink\n(${HomeKey.uriPattern})")
                    }

                    Spacer(modifier = Modifier.height(8.dp))

                    // 2. User Key Deep Link
                    OutlinedTextField(
                        value = userIdText,
                        onValueChange = { userIdText = it },
                        label = { Text("User ID") },
                        singleLine = true,
                    )
                    ElevatedButton(
                        onClick = dropUnlessResumed {
                            val id = userIdText.toIntOrNull() ?: 1
                            val uri = "https://www.nav3recipes.com/user/$id"
                            launchDeepLink(uri)
                        }
                    ) {
                        Text("Launch User DeepLink")
                    }

                    Spacer(modifier = Modifier.height(8.dp))

                    // 3. Product Key Deep Link
                    OutlinedTextField(
                        value = categoryText,
                        onValueChange = { categoryText = it },
                        label = { Text("Category") },
                        singleLine = true,
                    )
                    OutlinedTextField(
                        value = productIdText,
                        onValueChange = { productIdText = it },
                        label = { Text("Product ID") },
                        singleLine = true,
                    )
                    ElevatedButton(
                        onClick = dropUnlessResumed {
                            val uri = "https://www.nav3recipes.com/products/$categoryText/$productIdText"
                            launchDeepLink(uri)
                        }
                    ) {
                        Text("Launch Product DeepLink")
                    }
                }
            }
        }
    }

    private fun launchDeepLink(uriString: String) {
        val intent = Intent(this, MainActivity::class.java).apply {
            data = uriString.toUri()
        }
        startActivity(intent)
    }
}
```

```
package com.example.nav3recipes.deeplink.usecases.deeplinkkey

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.core.net.toUri
import androidx.navigation3.runtime.NavBackStack
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.deeplink.DeepLinkRequest
import androidx.navigation3.runtime.deeplink.UriDeepLinkMatcher
import androidx.navigation3.runtime.deeplink.invoke
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.common.deeplink.EntryScreen
import com.example.nav3recipes.common.deeplink.TextContent
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.serializer

class MainActivity : ComponentActivity() {

    // Register UriDeepLinkMatchers using the uriPattern from each DeepLinkKey
    private val deepLinkMatchers = listOf(
        UriDeepLinkMatcher(HomeKey.uriPattern.toUri(), serializer<HomeKey>()),
        UriDeepLinkMatcher(UserKey.uriPattern.toUri(), serializer<UserKey>()),
        UriDeepLinkMatcher(ProductKey.uriPattern.toUri(), serializer<ProductKey>()),
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        val request = DeepLinkRequest(intent)
        val matches = deepLinkMatchers.mapNotNull { it.match(request) }
        val bestMatch = matches.maxOrNull()
        val key = bestMatch?.key ?: FallbackKey

        setContent {
            val backStack: NavBackStack<NavKey> = rememberNavBackStack(key)
            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                entryProvider = entryProvider {
                    entry<HomeKey> {
                        EntryScreen("Home Screen") {
                            TextContent("Welcome Home!\n(Matched: ${HomeKey.uriPattern})")
                        }
                    }
                    entry<UserKey> { key ->
                        EntryScreen("User Profile") {
                            TextContent("User ID: ${key.id}\n(Matched: ${UserKey.uriPattern})")
                        }
                    }
                    entry<ProductKey> { key ->
                        EntryScreen("Product Details") {
                            TextContent("Category: ${key.category}\nProduct ID: ${key.productId}\n(Matched: ${ProductKey.uriPattern})")
                        }
                    }
                    entry<FallbackKey> {
                        EntryScreen("Fallback Destination") {
                            TextContent("No deep link pattern matched the incoming request.")
                        }
                    }
                }
            )
        }
    }
}
```

```
package com.example.nav3recipes.deeplink.usecases.deeplinkkey

import androidx.navigation3.runtime.NavKey
import kotlinx.serialization.Serializable

/**
 * Interface for navigation keys that support deep linking.
 *
 * Associating the URI pattern with the key definition keeps the URL template
 * and parameter structure together in a single place.
 */
interface DeepLinkKey {
    val uriPattern: String
}

@Serializable
data object HomeKey : DeepLinkKey, NavKey {
    override val uriPattern: String = "https://www.nav3recipes.com/home"
}

@Serializable
data class UserKey(
    val id: Int
) : NavKey {
    companion object : DeepLinkKey {
        override val uriPattern: String = "https://www.nav3recipes.com/user/{id}"
    }
}

@Serializable
data class ProductKey(
    val category: String,
    val productId: String
) : NavKey {
    companion object : DeepLinkKey {
        override val uriPattern: String = "https://www.nav3recipes.com/products/{category}/{productId}"
    }
}

@Serializable
data object FallbackKey : NavKey
```