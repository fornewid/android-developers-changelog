---
title: Filter a list while typing  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/filter-list-while-typing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Filter a list while typing Stay organized with collections Save and categorize content based on your preferences.




This guide explains how to filter through a list of strings based on text input
in Jetpack Compose. Use this approach to dynamically update a list based on user
search queries.

## Version compatibility

This implementation works with Compose versions 1.2.0 and higher.

### Dependencies

Include the following dependencies in your `build.gradle`:

## Filter a list based on text input

Together, the following snippets produce a list that updates in real time as the
user types. This example uses a [`ViewModel`](/reference/androidx/lifecycle/ViewModel)
to hold the list data and filtering logic, while the `FilterTextView()` function
creates the UI that updates automatically whenever the filter text changes.

```
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

FilterText.kt
```

### Key points about the code

* The `ViewModel` code abstracts the filtering work away from the composable.
* The `ViewModel` holds both the original and filtered lists. It defines a list
  of items and a `MutableStateFlow` to hold the filtered items.
* The `filterText` function filters the list based on the provided input string
  and updates the `filteredItems` state, which is passed back into the UI.

```
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

FilterText.kt
```

### Key points about the code

* Displays an [`OutlinedTextField`](/reference/kotlin/androidx/compose/material3/OutlinedTextField.composable#OutlinedTextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors)) for user input and a [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) to
  display the filtered list items.
* Collects the `filteredItems` state flow from the `ViewModel` and converts it
  into a lifecycle-aware `State` object.
  + [`collectAsStateWithLifecycle`](/reference/kotlin/androidx/lifecycle/compose/collectAsStateWithLifecycle.composable#(kotlinx.coroutines.flow.StateFlow).collectAsStateWithLifecycle(androidx.lifecycle.Lifecycle,androidx.lifecycle.Lifecycle.State,kotlin.coroutines.CoroutineContext)) collects the latest value from the
    `StateFlow` and recomposes the UI when the value changes.
* `text by rememberSaveable { mutableStateOf("") }` creates a state variable
  `text` to hold the current text entered in the filter text field.
  + `rememberSaveable` preserves the value of text across configuration
    changes.
  + The `by` keyword delegates the value of text to the value property of the
    `MutableState` object.
* `OutlinedTextField` calls the `filterText` function from the view model when
  text changes trigger the `onValueChange` callback.

### Result

[

](/static/develop/ui/compose/quick-guides/content/FilterTextViewSample1.mp4)


**Figure 1.** A filtered list that updates as new text is entered.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Request user input

Learn how to implement ways for users to interact
with your app by entering text and using other means of input.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/request-user-input)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)