---
title: Use keyboard IME animations  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/keyboard-animations
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Use keyboard IME animations Stay organized with collections Save and categorize content based on your preferences.




You can apply `Modifier.imeNestedScroll()` to a scrolling container to open and
close the IME automatically when scrolling to the bottom of the container.

```
class WindowInsetsExampleActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        WindowCompat.setDecorFitsSystemWindows(window, false)

        setContent {
            MaterialTheme {
                MyScreen()
            }
        }
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun MyScreen() {
    Box {
        LazyColumn(
            modifier = Modifier
                .fillMaxSize() // fill the entire window
                .imePadding() // padding for the bottom for the IME
                .imeNestedScroll(), // scroll IME at the bottom
            content = { }
        )
        FloatingActionButton(
            modifier = Modifier
                .align(Alignment.BottomEnd)
                .padding(16.dp) // normal 16dp of padding for FABs
                .navigationBarsPadding() // padding for navigation bar
                .imePadding(), // padding for when IME appears
            onClick = { }
        ) {
            Icon(imageVector = Icons.Filled.Add, contentDescription = "Add")
        }
    }
}

MigrationOtherConsiderationsSnippets.kt
```

![Animation showing a UI element scrolling up and down to make way for a keyboard](/static/develop/ui/compose/images/interop-keyboard.gif)


**Figure 3.** IME animations.

[Previous

arrow\_back

Set up window insets](/develop/ui/compose/system/insets-ui)

[Next

Use Material 3 insets

arrow\_forward](/develop/ui/compose/system/material-insets)