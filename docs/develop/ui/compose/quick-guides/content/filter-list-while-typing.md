---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/filter-list-while-typing
url: https://developer.android.com/develop/ui/compose/quick-guides/content/filter-list-while-typing
source: md.txt
---

<br />

This guide explains how to filter through a list of strings based on text input
in Jetpack Compose. Use this approach to dynamically update a list based on user
search queries.

## Version compatibility

This implementation works with Compose versions 1.2.0 and higher.

### Dependencies

Include the following dependencies in your `build.gradle`:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/filter-list-while-typing_001484963577bfc707b73b4b52991a87aa138867a07f2bcb7db27c9e469d1df4.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Filter a list based on text input

Together, the following snippets produce a list that updates in real time as the
user types. This example uses a [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)
to hold the list data and filtering logic, while the `FilterTextView()` function
creates the UI that updates automatically whenever the filter text changes.


```kotlin
class FilterTextViewModel : ViewModel() {
    private val items = listOf(
        "Cupcake",
        "Donut",
        "Eclair",
        "Froyo",
        "Gingerbread",
        "Honeycomb",
        "Ice Cream Sandwich"
    )

    private val _filteredItems = MutableStateFlow(items)
    var filteredItems: StateFlow<List<String>> = _filteredItems

    fun filterText(input: String) {
        // This filter returns the full items list when input is an empty string.
        _filteredItems.value = items.filter { it.contains(input, ignoreCase = true) }
    }
}
```

<br />

### Key points about the code

- The `ViewModel` code abstracts the filtering work away from the composable.
- The `ViewModel` holds both the original and filtered lists. It defines a list of items and a `MutableStateFlow` to hold the filtered items.
- The `filterText` function filters the list based on the provided input string and updates the `filteredItems` state, which is passed back into the UI.


```kotlin
@Composable
fun FilterTextView(modifier: Modifier = Modifier, viewModel: FilterTextViewModel = viewModel()) {
    val filteredItems by viewModel.filteredItems.collectAsStateWithLifecycle()
    var text by rememberSaveable { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(all = 10.dp)
    ) {
        OutlinedTextField(
            value = text,
            onValueChange = {
                text = it
                viewModel.filterText(text)
            },
            label = { Text("Filter Text") },
            modifier = Modifier.fillMaxWidth()
        )

        LazyColumn {
            items(
                count = filteredItems.size,
                key = { index -> filteredItems[index] }
            ) {
                ListItem(
                    headlineContent = { Text(filteredItems[it]) },
                    modifier = Modifier
                        .fillParentMaxWidth()
                        .padding(10.dp)
                )
            }
        }
    }
}
```

<br />

### Key points about the code

- Displays an [`OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedTextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors)) for user input and a [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) to display the filtered list items.
- Collects the `filteredItems` state flow from the `ViewModel` and converts it into a lifecycle-aware `State` object.
  - [`collectAsStateWithLifecycle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/package-summary#(kotlinx.coroutines.flow.StateFlow).collectAsStateWithLifecycle(androidx.lifecycle.Lifecycle,androidx.lifecycle.Lifecycle.State,kotlin.coroutines.CoroutineContext)) collects the latest value from the `StateFlow` and recomposes the UI when the value changes.
- `text by rememberSaveable { mutableStateOf("") }` creates a state variable `text` to hold the current text entered in the filter text field.
  - `rememberSaveable` preserves the value of text across configuration changes.
  - The `by` keyword delegates the value of text to the value property of the `MutableState` object.
- `OutlinedTextField` calls the `filterText` function from the view model when text changes trigger the `onValueChange` callback.

### Result

<br />

**Figure 1.** A filtered list that updates as new text is entered.

<br />

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Request user input

Learn how to implement ways for users to interact with your app by entering text and using other means of input. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/request-user-input) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)