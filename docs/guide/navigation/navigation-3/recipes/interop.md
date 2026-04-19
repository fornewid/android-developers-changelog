---
title: https://developer.android.com/guide/navigation/navigation-3/recipes/interop
url: https://developer.android.com/guide/navigation/navigation-3/recipes/interop
source: md.txt
---

# Interop Recipe

This recipe demonstrates how to use `AndroidFragment` and `AndroidView` within a Navigation3 application.

## Features

- **AndroidFragment**: Shows how to embed a Fragment inside a Composable destination.
- **AndroidView**: Shows how to embed a classic Android View inside a Composable destination.

## Key Components

- `InteropActivity`: The main activity hosting the navigation.
- `MyCustomFragment`: A simple Fragment used in the example.
- `AndroidFragment<T>`: A Composable that hosts a Fragment.
- `AndroidView`: A Composable that hosts an Android View.

## Usage

1. Run the `InteropActivity`.
2. The initial screen shows a Fragment.
3. Click "Go to View" to navigate to a screen displaying a `TextView`.

[![](https://developer.android.com/static/images/picto-icons/code.svg) Explore View the full recipe on GitHub.](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/interop)

```
package com.example.nav3recipes.interop

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment

class MyCustomFragment : Fragment() {
    @SuppressLint("SetTextI18n")
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        return TextView(requireContext()).apply {
            text = "My Fragment"
        }
    }
}
```

```
package com.example.nav3recipes.interop

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.TextView
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.wrapContentSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import androidx.fragment.app.FragmentActivity
import androidx.fragment.compose.AndroidFragment
import androidx.lifecycle.compose.dropUnlessResumed
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.ui.NavDisplay
import com.example.nav3recipes.ui.setEdgeToEdgeConfig
import kotlinx.serialization.Serializable

@Serializable
private data object FragmentRoute : NavKey

@Serializable
private data class ViewRoute(val id: String) : NavKey

class InteropActivity : FragmentActivity() {

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        setEdgeToEdgeConfig()
        super.onCreate(savedInstanceState)
        setContent {
            val backStack = rememberNavBackStack(FragmentRoute)

            NavDisplay(
                backStack = backStack,
                onBack = { backStack.removeLastOrNull() },
                entryProvider = entryProvider {
                    entry<FragmentRoute> {
                        Column(Modifier.fillMaxSize().wrapContentSize()) {
                            AndroidFragment<MyCustomFragment>()
                            Button(onClick = dropUnlessResumed {
                                backStack.add(ViewRoute("123"))
                            }) {
                                Text("Go to View")
                            }
                        }
                    }
                    entry<ViewRoute> { key ->
                        AndroidView(
                            modifier = Modifier.fillMaxSize().wrapContentSize(),
                            factory = { context ->
                                TextView(context).apply {
                                    text = "My View with key: ${key.id}"
                                }
                            }
                        )
                    }
                }
            )
        }
    }
}
```