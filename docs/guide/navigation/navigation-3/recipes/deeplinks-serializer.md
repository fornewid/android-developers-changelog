---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-serializer
url: https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-serializer
source: md.txt
---

# Custom DeepLinkSerializer Recipe

This recipe demonstrates how to use a custom `DeepLinkSerializer` in Navigation 3 using `UriDeepLinkMatcher` and Kotlinx Serialization.

## How it works

This recipe consists of two activities:

- `DeepLinkSerializerActivity`: Takes user input for product details (name, color, and quantity), serializes the custom `Product` object into a URI query parameter string (`?product={product}&quantity={quantity}`), constructs a `DeepLinkRequest` URI, and launches `MainActivity`.
- `MainActivity`: Constructs a `DeepLinkRequest(intent)`, matches it using `UriDeepLinkMatcher` configured with `ProductDetailsKey` (which uses `ProductSerializer` for `product` and native serialization for `quantity`), and displays the deserialized product details in `NavDisplay`.

## Key Concepts

1. **`DeepLinkSerializer<T>`** :
   Extends `DeepLinkSerializer<T>` to provide custom string serialization and deserialization logic for custom objects or types (such as `Color` or packed string formats) that need to be parsed from or encoded into URI path/query parameters.

2. **Annotating NavKey properties with `@Serializable(with = ...)`** :
   The custom `NavKey` uses `@Serializable(with = ProductSerializer::class)` on properties whose types require custom serialization (e.g. `product: Product`).

3. **Mixing Standard and Custom Serialized Parameters** :
   Parameters with standard types (like `quantity: Int`) are serialized natively out-of-the-box by Kotlinx Serialization, while custom parameters (like `product: Product`) use `ProductSerializer`.

4. **`UriDeepLinkMatcher` integration** :
   `UriDeepLinkMatcher(uriPattern, serializer<ProductDetailsKey>())` automatically applies custom and standard serializers when matching and decoding deep link URIs.

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/deeplink/usecases/serializer)

```
package com.example.nav3recipes.deeplink.usecases.serializer

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuAnchorType
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.core.net.toUri
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.common.deeplink.EntryScreen
import com.example.nav3recipes.content.ContentOrange
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable

@Serializable
private data object Home: NavKey

class DeepLinkSerializerActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        setContent {
            EntryScreen {
                val backStack = rememberNavBackStack(Home)
                NavDisplay(
                    backStack = backStack,
                    onBack = { backStack.removeLastOrNull() },
                    entryProvider = entryProvider {
                        entry<Home> {
                            HomeScreen(
                                onAddProduct = { product, quantity ->
                                    val serializedProduct = ProductSerializer.serialize(product)
                                    val uriString = "https://www.nav3recipes.com/products?product=$serializedProduct&quantity=$quantity"
                                    val intent = Intent(
                                        this@DeepLinkSerializerActivity,
                                        MainActivity::class.java
                                    ).apply {
                                        data = uriString.toUri()
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
private fun HomeScreen(onAddProduct: (Product, Int) -> Unit) {
    ContentOrange(title = "Deep link serializer demo") {
        Column(
            modifier = Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            var name by remember { mutableStateOf("") }
            OutlinedTextField(
                placeholder = { Text("Product name...", color = Color.Black.copy(alpha = 0.5f)) },
                value = name,
                singleLine = true,
                onValueChange = { name = it },
            )
            Spacer(modifier = Modifier.height(16.dp))
            var color by remember { mutableStateOf(Color.Red) }
            ProductDropdownColorPicker(onColorSelected = { color = it })
            Spacer(modifier = Modifier.height(16.dp))
            var quantity by remember { mutableIntStateOf(1) }
            ProductQuantityPicker(selectedQuantity = quantity, onQuantitySelected = { quantity = it })
            Spacer(modifier = Modifier.height(16.dp))
            ElevatedButton(
                onClick = dropUnlessResumed {
                    if (name.isNotBlank()) {
                        onAddProduct(Product(name, color), quantity)
                    }
                }
            ) {
                Text("Add product")
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ProductQuantityPicker(selectedQuantity: Int, onQuantitySelected: (Int) -> Unit) {
    val quantities = listOf(1, 2, 3, 4, 5)
    var expanded by remember { mutableStateOf(false) }

    ExposedDropdownMenuBox(expanded = expanded, onExpandedChange = { expanded = !expanded }) {
        OutlinedTextField(
            modifier = Modifier.menuAnchor(ExposedDropdownMenuAnchorType.PrimaryNotEditable),
            readOnly = true,
            value = selectedQuantity.toString(),
            onValueChange = {},
            label = { Text("Select Quantity") },
            trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expanded) },
            colors = ExposedDropdownMenuDefaults.outlinedTextFieldColors()
        )
        ExposedDropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            quantities.forEach { qty ->
                DropdownMenuItem(
                    text = { Text(qty.toString()) },
                    onClick = {
                        onQuantitySelected(qty)
                        expanded = false
                    },
                    contentPadding = ExposedDropdownMenuDefaults.ItemContentPadding
                )
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ProductDropdownColorPicker(onColorSelected: (Color) -> Unit) {
    val colors: List<ProductColor> = listOf(
        ProductColor("Red", Color.Red),
        ProductColor("Green", Color.Green),
        ProductColor("Blue", Color.Blue),
        ProductColor("Yellow", Color.Yellow),
        ProductColor("Magenta", Color.Magenta),
        ProductColor("Cyan", Color.Cyan),
    )
    var expanded by remember { mutableStateOf(false) }
    var selectedColor by remember { mutableStateOf(colors.first()) }

    ExposedDropdownMenuBox(expanded = expanded, onExpandedChange = { expanded = !expanded }) {
        OutlinedTextField(
            modifier = Modifier.menuAnchor(ExposedDropdownMenuAnchorType.PrimaryNotEditable),
            readOnly = true,
            value = selectedColor.name,
            onValueChange = {},
            label = { Text("Select Color") },
            leadingIcon = {
                Box(
                    modifier = Modifier
                        .size(20.dp)
                        .background(selectedColor.color, shape = CircleShape)
                )
            },
            trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expanded) },
            colors = ExposedDropdownMenuDefaults.outlinedTextFieldColors()
        )
        ExposedDropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            colors.forEach { color ->
                DropdownMenuItem(
                    text = { Text(color.name) },
                    leadingIcon = {
                        Box(
                            modifier = Modifier
                                .size(20.dp)
                                .background(color.color, shape = CircleShape)
                        )
                    },
                    onClick = {
                        selectedColor = color
                        onColorSelected(color.color)
                        expanded = false
                    },
                    contentPadding = ExposedDropdownMenuDefaults.ItemContentPadding
                )
            }
        }
    }
}

private data class ProductColor(val name: String, val color: Color)
```

```
package com.example.nav3recipes.deeplink.usecases.serializer

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Text
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
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
import kotlinx.serialization.Serializable
import kotlinx.serialization.serializer

internal const val PRODUCT_URI_PATTERN =
    "https://www.nav3recipes.com/products?product={product}&quantity={quantity}"

internal data class Product(val name: String, val color: Color)

@Serializable
internal data class ProductDetailsKey(
    @Serializable(with = ProductSerializer::class)
    val product: Product,
    val quantity: Int,
): NavKey

@Serializable
internal object FallbackKey: NavKey

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)

        val request = DeepLinkRequest(intent)
        val deepLinkMatcher = UriDeepLinkMatcher(
            PRODUCT_URI_PATTERN.toUri(),
            serializer<ProductDetailsKey>()
        )

        val matchResult = deepLinkMatcher.match(request)
        val key = matchResult?.key ?: FallbackKey

        setContent {
            val backStack: NavBackStack<NavKey> = rememberNavBackStack(key)
            NavDisplay(
                backStack = backStack,
                onBack = backStack::removeLastOrNull,
                entryProvider = entryProvider {
                    entry<ProductDetailsKey> { key ->
                        EntryScreen(key.product.name) {
                            Spacer(modifier = Modifier.height(16.dp))
                            Box(
                                modifier = Modifier
                                    .size(100.dp)
                                    .background(key.product.color, shape = CircleShape),
                                contentAlignment = Alignment.Center,
                            ) {
                                Text(key.quantity.toString(), color = Color.White)
                            }
                        }
                    }
                    entry<FallbackKey> {
                        EntryScreen("Fallback Key") {
                            TextContent(
                                "Failed to deep link - DeepLinkRequest " +
                                        "did not match with any DeepLinkMatcher"
                            )
                        }
                    }
                }
            )
        }
    }
}
```

```
package com.example.nav3recipes.deeplink.usecases.serializer

import android.net.Uri
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.navigation3.runtime.deeplink.DeepLinkSerializer
import kotlinx.serialization.SerializationException

internal object ProductSerializer : DeepLinkSerializer<Product>() {
    override val serialName: String = "com.example.nav3recipes.deeplink.usecases.serializer.Product"

    override fun serialize(value: Product): String = Uri.encode("${value.name}-${value.color.toArgb()}")

    override fun deserialize(value: String): Product {
        val decodedValue = Uri.decode(value)
        val splitArgs = decodedValue.split("-", limit = 2)
        if (splitArgs.size < 2) {
            throw SerializationException("Invalid product format: $decodedValue")
        }
        val name = splitArgs[0]
        val colorCode = splitArgs[1].toIntOrNull()
            ?: throw SerializationException("Invalid color code: ${splitArgs[1]}")
        val color = Color(colorCode)
        return Product(name, color)
    }
}
```