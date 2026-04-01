---
title: https://developer.android.com/develop/ui/compose/system/keyboard-animations
url: https://developer.android.com/develop/ui/compose/system/keyboard-animations
source: md.txt
---

You can apply `Modifier.imeNestedScroll()` to a scrolling container to open and
close the IME automatically when scrolling to the bottom of the container.


```kotlin
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
```

<br />

![Animation showing a UI element scrolling up and down to make way for a keyboard](https://developer.android.com/static/develop/ui/compose/images/interop-keyboard.gif) **Figure 3.** IME animations.